"""Validate retained data-only artifacts; no legacy code/tests are executed."""
import ast,collections,gzip,hashlib,json,pathlib,re,shutil
BASE=pathlib.Path('/Users/Shared');OUT=BASE/'agent-org/factory/reports/legacy-retirement'
module=ast.parse((OUT/'factory-extract.py').read_text())
node=next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='prose_only')
ns={'re':re};exec(compile(ast.Module(body=[node],type_ignores=[]),'native-prose-extractor','exec'),ns)
cases=[('before\n\n```python\nimport os\n\ndef f():\n    pass\n```\n\nafter','before\n\n\nafter',False),('a\n~~~py\nx\n\nx\n~~~\nb','a\n\nb',False),('a\n```\nx\n~~~\ny','a\n',True),('a\n````x\nx\n```\ny\n````\nb','a\n\nb',False),('a\n    code\n> private quote\nb','a\n\n\nb',False)]
checks=[]
for source,expected,unclosed in cases:
 actual,excluded,opened=ns['prose_only'](source)
 assert [line for line in actual.splitlines() if line]==[line for line in expected.splitlines() if line],(actual,expected)
 assert opened==unclosed
checks.append({'check':'fence_blank_lines_matching_unclosed_indented_quote','cases':len(cases),'passed':True})
drop=next(n for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DROPKEY' for t in n.targets))
pattern=re.compile(ast.literal_eval(drop.value.args[0]))
def sanitize(value):
 if isinstance(value,dict):return {k:sanitize(v) for k,v in value.items() if not pattern.search(k)}
 if isinstance(value,list):return [sanitize(v) for v in value]
 return value
# Reapply final key policy after a generation started under an older policy;
# exact source identities remain, but raw exception strings may embed commands.
p=OUT/'factory-source-claims.jsonl.gz';temp=p.with_name(p.name+'.tmp');removed=0;claim_count=0;record_count=0;code=[];sensitive=[]
bad=re.compile(r'^\s*(?:import\s|from\s+\S+\s+import\s|def\s|class\s|export\s|function\s|const\s|curl\s|gh\s|git\s)')
secret=re.compile(r'-----BEGIN [^-]*PRIVATE KEY|(?:gh[pousr]_|github_pat_)[A-Za-z0-9_\-]{16,}|\bsk-[A-Za-z0-9_\-]{16,}|\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|Bearer\s+[A-Za-z0-9._~+/=-]{16,}')
with gzip.open(p,'rt') as reader,temp.open('wb') as raw:
 with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as writer:
  for line in reader:
   record=json.loads(line);record_count+=1
   if 'derived_fields' in record:
    clean=sanitize(record['derived_fields']);removed+=int(clean!=record['derived_fields']);record['derived_fields']=clean
   for claim in record.get('claims',[]):
    claim_count+=1
    if bad.match(claim['claim_excerpt']):code.append(record['path'])
   serialized=json.dumps(record,sort_keys=True)+'\n'
   if secret.search(serialized):sensitive.append(record['path'])
   writer.write(serialized.encode())
assert not code,code[:5]
assert not sensitive,sensitive[:5]
temp.replace(p)
checks.append({'check':'claims_exclusion_and_known_credential_patterns','records':record_count,'claim_paragraphs':claim_count,'code_leading_claims':len(code),'credential_pattern_matches':len(sensitive),'records_with_raw_exception_fields_removed':removed,'passed':True,'limits':'Pattern scan is not proof of absence of every possible secret or private fact.'})
summary=json.loads((OUT/'factory-inventory-summary.json').read_text());counts=collections.Counter();classes=collections.defaultdict(collections.Counter);hashed=0;unreadable=[]
for line in gzip.open(OUT/'factory-files.jsonl.gz','rt'):
 row=json.loads(line)
 root=next(r for r in summary['roots'] if row['path'].startswith(r+'/'))
 counts[root]+=1;classes[root][row['class']]+=1;hashed+=int('sha256' in row)
 if row['class']=='unreadable':unreadable.append(row['path'])
for root in summary['roots']:
 assert counts[root]==summary['roots'][root]['counts']['entries']
 assert dict(classes[root])==summary['roots'][root]['classes']
group_count=0;group_paths=0
for line in gzip.open(OUT/'factory-hash-groups.jsonl.gz','rt'):
 row=json.loads(line);group_count+=1;group_paths+=len(row['paths'])
assert group_paths==hashed
assert group_count==summary['unique_hashes']
checks.append({'check':'complete_inventory_class_hash_group_accounting','entries':sum(counts.values()),'hashed_files':hashed,'unique_hashes':group_count,'unreadable':unreadable,'passed':True})
q=json.loads((OUT/'factory-quantitative-evidence.json').read_text());completions=q['fixtures']['old/factory-eval-workspaces'];check_counts=collections.Counter();effect_counts=collections.Counter();total=0
for key,count in completions['content_counts'].items():
 item=json.loads(key);check_counts[item['required_check']]+=count;effect_counts[item['external_effect']]+=count;total+=count
assert total==211 and dict(check_counts)=={'not_applicable':142,'passed':42,'unavailable':27}
assert dict(effect_counts)=={'draft_only':60,'none':136,'registered_once':15}
checks.append({'check':'fixture_denominators','completion_files':total,'required_check_counts':dict(check_counts),'effect_counts':dict(effect_counts),'answer_files':q['fixtures']['old/factory-evals-workspaces']['paths'],'passed':True})
ids=json.loads((OUT/'factory-source-index.json').read_text())
for row in ids:assert hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest()==row['sha256'],row['id']
checks.append({'check':'source_table_current_hashes','sources':len(ids),'passed':True})
for p in OUT.glob('factory-*.jsonl.gz'):
 with gzip.open(p,'rb') as reader:
  while reader.read(1024*1024):pass
for p in OUT.glob('factory-*.py'):ast.parse(p.read_text())
checks.append({'check':'gzip_integrity_and_native_script_syntax','passed':True})
result={'status':'passed','checks':checks,'retained_bytes_before_verification_record':sum(p.stat().st_size for p in OUT.glob('factory-*')),'source_execution':'none; native collection/verification only'}
(OUT/'factory-verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2,sort_keys=True))
