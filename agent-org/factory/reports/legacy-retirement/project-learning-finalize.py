#!/usr/bin/env python3
"""Finalize metadata-only coverage and verify research artifacts, without legacy execution."""
import ast, collections, hashlib, json, os, pathlib, re
BASE=pathlib.Path('/Users/Shared/old/projects');OUT=pathlib.Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
inventory=json.loads((OUT/'project-learning-inventory.json').read_text())
for r in inventory['exclusions']:
    if r['reason']=='symlink-not-followed':r['target']=os.readlink(BASE/r['path'])
inventory['root_nondirectory_entries']=[{'path':p.name,'bytes':p.lstat().st_size,'disposition':'OS metadata excluded from learning; not a project'} for p in BASE.iterdir() if not p.is_dir() and not p.is_symlink()]
(OUT/'project-learning-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
evidence=json.loads((OUT/'project-learning-evidence.json').read_text());metrics=json.loads((OUT/'project-learning-metrics.json').read_text())
records={}
with (OUT/'project-learning-sources.jsonl').open() as f:
    for l in f:
        r=json.loads(l);records[r['path']]=r
for r in evidence['ignored_build_exception']:records[r['path']]=r
for path,r in metrics['source_manifest'].items():records.setdefault(path,{'path':path,**r})
for r in evidence['documentary_sources'].values():records.setdefault(r['path'],r)
reviewed={r['path'] for r in evidence['documentary_sources'].values()}
parsed=set(metrics['source_manifest'])
groups=collections.defaultdict(list);categories=collections.defaultdict(collections.Counter);projects=collections.defaultdict(collections.Counter)
def category(path):
    p=pathlib.PurePosixPath(path);s=path.lower()
    if p.name in {'AGENTS.md','CONTEXT.md','SKILL.md'}:return 'instructions-context-skills'
    if '/agent-org/' in s and any('/'+k+'/' in s for k in ['policies','decisions','approvals','requirements','tasks','plans']):return 'governance-and-task-records'
    if any(k in s for k in ['/evidence/','/artifacts/','/runs/','/evals/','/.local/','/reports/','/events','/lessons/']):return 'telemetry-evaluation-evidence'
    return 'other-documentation-and-data'
for path,r in records.items():
    c=categories[category(path)];p=projects[path.split('/')[0]];c['files']+=1;p['candidate_files']+=1;c['bytes']+=r.get('bytes',0);p['candidate_bytes']+=r.get('bytes',0)
    if r.get('sha256'):groups[r['sha256']].append(path);c['hashed_files']+=1;p['hashed_files']+=1
    if path in reviewed:c['documentary_review_sources']+=1;p['documentary_review_sources']+=1
    if path in parsed:c['parsed_metric_sources']+=1;p['parsed_metric_sources']+=1
coverage={'scope':'Broad source candidates plus ignored-build exception and explicitly parsed DB/raw report sources; excludes dependency/cache internals and noncandidate product binaries/code. Categories are deterministic path heuristics, not semantic validation. Review and parsed source sets overlap and cannot be added as disjoint coverage.','broad_files_outside_pruned_subtrees':sum(r.get('files',0) for r in inventory['projects']),'broad_hidden_path_files':sum(r.get('hidden_path_files',0) for r in inventory['projects']),'broad_candidates':inventory['candidate_count'],'broad_unique_hashes':inventory['unique_candidate_hashes'],'broad_duplicate_instances':inventory['duplicate_candidate_instances'],'union_candidate_files':len(records),'union_unique_hashes':len(groups),'union_duplicate_instances':sum(len(ps)-1 for ps in groups.values()),'categories':{k:dict(v) for k,v in categories.items()},'projects':{k:dict(v) for k,v in projects.items()},'explicit_documentary_review_sources':len(reviewed),'explicitly_parsed_metric_sources':len(parsed),'remaining_candidate_paths':'All paths not in reviewed or parsed sets are fingerprint-only, not semantically audited; exact source locations remain in source/evidence manifests.'}
(OUT/'project-learning-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
report=(OUT/'project-learnings.md').read_text(); checks={}
names={p.name for p in BASE.iterdir() if p.is_dir() and not p.is_symlink()}
rows={m.group(1) for m in re.finditer(r'^\| ([^|]+?) \|',report,re.M)}
checks['all_51_project_rows']=names<=rows and len(names)==51
checks['symlink_row']='| ai_bullet_heaven (symlink) |' in report
checks['documentary_ids_resolve']=all(s in evidence['documentary_sources'] for s in set(re.findall(r'\bS\d\d\b',report)))
links=re.findall(r'\]\(([^)]+)\)',report)
checks['local_links_resolve']=all((OUT/l.split('#')[0]).exists() for l in links if not l.startswith(('http:','https:')))
checks['source_registry_no_errors']=all('error' not in r for r in evidence['documentary_sources'].values())
checks['all_reader_syntax_valid']=True
for p in OUT.glob('project-learning-*.py'):ast.parse(p.read_text())
checks['penny_raw_counts_match']=metrics['penny_143_raw_recomputed']['tests']==162 and metrics['penny_143_raw_recomputed']['result_statuses']=={'passed':162} and metrics['penny_143_raw_recomputed']['retry_values']=={'0':162}
checks['work_csv_primary_matches']=metrics['work_csv_recomputed']['2026-10-08-outcomes']['compliant_successes']==49 and metrics['work_csv_recomputed']['2026-10-08-screening']['sums']['checks_passed']==489
checks['broad_hash_denominator_matches']=sum('sha256' in r for r in records.values())>=inventory['candidate_count']-26
checks['derived_under_100_MiB']=sum(p.stat().st_size for p in OUT.glob('project-learning*'))<100*1024*1024
secret_patterns=[rb'(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{30,}',rb'(?<![A-Za-z0-9])AKIA[A-Z0-9]{16}',rb'(?<![A-Za-z0-9])sk-(?:proj-)?[A-Za-z0-9_-]{35,}']
matches=[]
for p in OUT.glob('project-learning*'):
    if p.is_file():
        raw=p.read_bytes()
        if any(re.search(pat,raw) for pat in secret_patterns):matches.append(p.name)
checks['bounded_credential_pattern_scan_no_hits']=not matches
verification={'checks':checks,'passed':all(checks.values()),'retained_failed_check':'Initial unbounded sk- substring pattern flagged645 path fragments inside ordinary words such as task/risk; all were preceded by alphanumeric characters. Token-boundary diagnostic found0 actual prefix matches. Corrected prefix-boundary scan is narrower and its limits remain explicit; no raw candidate value was printed.','limits':'Own artifact consistency checks and bounded credential patterns; not independent acceptance, comprehensive secret detection, legacy evaluator replay or source backup.','artifacts':{p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(OUT.glob('project-learning*')) if p.is_file() and p.name!='project-learning-verification.json'}}
(OUT/'project-learning-verification.json').write_text(json.dumps(verification,indent=2)+'\n')
print(json.dumps({'checks':checks,'coverage':{k:v for k,v in coverage.items() if k not in {'categories','projects'}},'artifact_bytes':sum(p.stat().st_size for p in OUT.glob('project-learning*'))},indent=2))
if not verification['passed']:raise SystemExit(1)
