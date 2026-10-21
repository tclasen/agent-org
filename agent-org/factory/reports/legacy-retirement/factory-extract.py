"""Deterministic, read-only source claim/telemetry extraction (not evaluation).

This extracts selected conclusions and numeric/status fields; it does not copy
transcripts, command arguments, credentials, complete source or raw log payloads.
Run from /Users/Shared. Outputs factory-* only. No legacy modules are imported.
"""
import collections, contextlib, gzip, hashlib, io, json, os, pathlib, re

BASE = pathlib.Path('/Users/Shared')
OUT = BASE / 'agent-org/factory/reports/legacy-retirement'
ROOTS = ['old/factory','old/work','old/agent-collaboration','old/agent-handoffs','old/factory-eval-workspaces','old/factory-evals-workspaces']
SKIP = {'.git','node_modules','.venv','venv','__pycache__','.next','.cache','.ruff_cache','.pytest_cache','vendor','dist','build','.build-dist','.conformance-dist'}
PRIVATE = re.compile(r'(?i)(password|passwd|secret|credential|authorization|access.token|refresh.token|private.key|cookie|auth.json|kubeconfig|\.pem$|\.key$)')
DROPKEY = re.compile(r'(?i)(password|passwd|secret|credential|authorization|token$|cookie|private.key|raw|stdout|stderr|prompt|message|transcript|command|argv|environment|headers|payload|body|content|salt|digest_value|errors?$)')
KEEP = re.compile(r'(?i)(pass|fail|block|inconclusive|unknown|limit|not |no |retain|risk|scope|evidence|decision|require|reject|accept|deni|denia|observ|verif|correct|fix|replay|restart|source|release|baseline|partial|defer|implement|count|metric|bound|test|latency|coverage|\d)')
SENSITIVE = re.compile(r'(?i)(-----BEGIN [^-]*PRIVATE KEY|(?:gh[pousr]_|github_pat_|sk-[A-Za-z0-9])[A-Za-z0-9_\-]{16,}|Bearer\s+[A-Za-z0-9._~+/=-]{12,})')
def safe_string(s):
  if SENSITIVE.search(s):return '[REDACTED: credential-like pattern]'
  if len(s)>3000:return s[:3000]+' [TRUNCATED: source required for remaining text]'
  return s
def sanitize(data):
  if isinstance(data,dict):return {k:sanitize(v) for k,v in data.items() if not DROPKEY.search(k)}
  if isinstance(data,list):return [sanitize(v) for v in data[:300]] + (['[TRUNCATED: list over300]'] if len(data)>300 else [])
  if isinstance(data,str):return safe_string(data)
  return data
def prose_only(text):
  """Remove entire CommonMark-style fenced blocks before paragraph splitting.

  A fence can contain blank lines. Only an empty trailing closing fence of the
  same character and at least the opening length closes it. Unclosed fences
  conservatively exclude the rest of the file. Indented code and blockquotes
  are omitted line by line. Counts make this intentional loss visible.
  """
  clean=[];fence=None;excluded=0
  for line in text.splitlines():
    match=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
    if fence:
      excluded+=1
      if match and match[1][0]==fence[0] and len(match[1])>=fence[1] and not match[2].strip():fence=None
      continue
    if match:
      fence=(match[1][0],len(match[1]));excluded+=1;clean.append('');continue
    if line.startswith('    ') or line.startswith('\t') or line.lstrip().startswith('>'):
      excluded+=1;clean.append('');continue
    clean.append(line)
  return '\n'.join(clean),excluded,fence is not None
selected=[];seen={};stats=collections.Counter();errors=[];eval_completion=collections.Counter();eval_answers=collections.Counter();rootgroups=collections.defaultdict(collections.Counter)
@contextlib.contextmanager
def gztext(path):
 with path.open('wb') as raw:
  with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as compressed:
   with io.TextIOWrapper(compressed,encoding='utf-8') as stream:
    yield stream
with gztext(OUT/'factory-source-claims.jsonl.gz') as out:
 for root in ROOTS:
  for directory,dirs,files in os.walk(BASE/root,followlinks=False):
   dirs[:]=sorted(d for d in dirs if d not in SKIP and not (pathlib.Path(directory)/d).is_symlink())
   for name in sorted(files):
    p=pathlib.Path(directory)/name;rel=str(p.relative_to(BASE));parts=p.parts
    if p.is_symlink():continue
    if PRIVATE.search(name):continue
    isplanning='old/factory/.factory-planning/' in rel
    local='old/work/factory/.local/' in rel
    # Explicitly inspect authored docs, root planning records, high-level run
    # results/summaries and operational receipts. Never inspect private trees.
    if '/.local/private/' in rel or '/.local/lean-backups/' in rel:continue
    md=p.suffix.lower()=='.md' and not local
    planning_json=isplanning and p.suffix=='.json' and p.parent==BASE/'old/factory/.factory-planning'
    high_result=isplanning and name in {'result.json','summary.json','comparison.json','runtime.json','grading-result.json'} and len(p.relative_to(BASE/'old/factory/.factory-planning').parts)<=4
    operation_json=local and p.suffix=='.json' and (name in {'index.json','application-verified.json','result.json','receipt.json','summary.json','footprint.json'} or 'footprint' in name) and not any(x in parts for x in ['python','uv-cache','postgres','minikube','pi-reference','pi-license-review','pi-notice-context','runtime-inputs','bin','seaweed-inputs'])
    authored_json=rel.startswith('old/work/factory/docs/evidence/') and p.suffix=='.json'
    benchmark=p.suffix=='.json' and ('/benchmarks/' in rel or '/.release-evidence/' in rel)
    completion=name=='completion.json' and root.endswith('factory-eval-workspaces')
    answer=name=='answer.json' and root.endswith('factory-evals-workspaces')
    if not any([md,planning_json,high_result,operation_json,authored_json,benchmark,completion,answer]):continue
    try:
     size=p.stat().st_size
     if size>8*1024*1024:errors.append({'path':rel,'status':'selected-too-large','bytes':size});continue
     raw=p.read_bytes();digest=hashlib.sha256(raw).hexdigest();text=raw.decode('utf-8')
     record={'path':rel,'sha256':digest,'bytes':size,'root':root,'status':'parsed','source_kind':'source_claims_not_independent_verification'}
     stats['selected_paths']+=1;rootgroups[root]['selected_paths']+=1
     if digest in seen:
      record['duplicate_of']=seen[digest];stats['duplicates']+=1
     else:
      seen[digest]=rel
      if md:
       chunks=[];heading='';prose,excluded_lines,unclosed=prose_only(text)
       for paragraph in re.split(r'\n\s*\n',prose):
        if re.match(r'^\s*(?:import\s|from\s+\S+\s+import\s|def\s|class\s|export\s|function\s|const\s|curl\s|gh\s|git\s)',paragraph):continue
        if paragraph.lstrip().startswith('#'):heading=paragraph.splitlines()[0][:240]
        if KEEP.search(paragraph) and not paragraph.lstrip().startswith('>'):
         chunks.append({'heading':heading,'claim_excerpt':safe_string(paragraph)})
       record['selected_paragraphs']=len(chunks);record['source_paragraphs']=len(re.split(r'\n\s*\n',text));record['excluded_code_or_quote_lines']=excluded_lines;record['unclosed_fence']=unclosed
       out.write(json.dumps({**record,'claims':chunks},sort_keys=True)+'\n')
      else:
       data=json.loads(text)
       if completion:
        eval_completion.update([json.dumps(data,sort_keys=True)])
       if answer:eval_answers.update([json.dumps(data,sort_keys=True)])
       out.write(json.dumps({**record,'derived_fields':sanitize(data)},sort_keys=True)+'\n')
      stats['unique_sources']+=1;rootgroups[root]['unique_sources']+=1
     selected.append(record)
    except (OSError,UnicodeError,json.JSONDecodeError) as err:errors.append({'path':rel,'status':type(err).__name__})
with gztext(OUT/'factory-extraction-coverage.jsonl.gz') as out:
 for row in selected:out.write(json.dumps(row,sort_keys=True)+'\n')
summary={'counts':dict(stats),'by_root':{k:dict(v) for k,v in rootgroups.items()},'errors':errors,'completion_unique_content_counts':dict(eval_completion),'answer_unique_content_counts':dict(eval_answers),'method':'Selected conclusions/paragraphs and sanitized high-level structured fields; exact content dedup; no command execution or raw log/transcript preservation. Duplicate completion counts represent unique content, not all211 paths; see fixture metrics separately.'}
(OUT/'factory-extraction-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,indent=2,sort_keys=True))
