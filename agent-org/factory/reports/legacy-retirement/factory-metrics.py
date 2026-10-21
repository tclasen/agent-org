"""Bounded native telemetry derivative; reads data only, runs no legacy code."""
import collections, hashlib, json, pathlib, re
BASE=pathlib.Path('/Users/Shared'); OUT=BASE/'agent-org/factory/reports/legacy-retirement'
def src(p):
 b=p.read_bytes();return {'path':str(p.relative_to(BASE)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
result={'status':'historical_source_observations_not_reexecuted_or_accepted','fixtures':{},'qualification_log_verification':[],'resource_measurements':[],'actuals':[]}
for root,name in [('old/factory-eval-workspaces','completion.json'),('old/factory-evals-workspaces','answer.json')]:
 fs=sorted((BASE/root).rglob(name));counts=collections.Counter();refs=[]
 for p in fs:
  data=json.loads(p.read_text());counts[json.dumps(data,sort_keys=True)]+=1;refs.append(src(p))
 result['fixtures'][root]={'paths':len(fs),'content_counts':dict(counts),'source_files':refs,'limitation':'Builder-authored local artifact fields are declarations, not independent grading; duplicated content is not independent evidence.'}
planning=BASE/'old/factory/.factory-planning'
for p in sorted(planning.glob('*ACTUALS*.json')):
 d=json.loads(p.read_text()); result['actuals'].append({**src(p),'fields':{k:v for k,v in d.items() if any(s in k for s in ['minute','second','complete','acceptance','scope','attempt','effort','forecast','missing','reason','outcome','delivered'])}})
result['actuals_limit']='All root-level *ACTUALS*.json records; elapsed wall spans versus effort are distinct. Null effort and missingness retained. Scope differences/incomplete delivery prevent interpreting elapsed within forecast as success.'
q=BASE/'old/work/factory/.local/evidence/qualification'; idx=json.loads((q/'index.json').read_text())
for p in sorted(q.glob('*.log')):
 raw=p.read_bytes(); s=raw.decode('utf-8',errors='replace');identity=src(p);expected=idx.get(p.name,{}).get('sha256')
 result['qualification_log_verification'].append({**identity,'retained_index_sha256':expected,'matches_retained_index':None if expected is None else expected==identity['sha256'],'test_pass_lines':len(re.findall(r'^--- PASS:',s,re.M)),'test_fail_lines':len(re.findall(r'^--- FAIL:',s,re.M)),'suite_ok_seconds':re.findall(r'^ok\s+[^\n]*?\s([0-9.]+)s(?:\s|$)',s,re.M),'limitation':'Syntactic retained log counters, not new execution, independent acceptance or all test coverage.'})
for p in sorted((BASE/'old/work/factory/.local').glob('*footprint*/summary.json')):
 result['resource_measurements'].append({**src(p),'fields':json.loads(p.read_text())})
for n in ['REQ-007-THREE-ARM-V2-COMPARISON-SNAPSHOT.json','REQ-007-CALIBRATION-V9-GRADE-V1-REVIEW.json','REQ-007-CHECKPOINT-NATURAL-CALIBRATION-V9-TERMINAL.json','REQ-007-STORAGE-GROWTH-COMPARISON.json']:
 p=planning/n;d=json.loads(p.read_text())
 if 'arms' in d:
  d={k:v for k,v in d.items() if k in ['acceptance','accepted_packages','application_strict_success','arms','limits','denominators','interpretation','study_limits']}
 result.setdefault('study_observations',[]).append({**src(p),'fields':d})
(OUT/'factory-quantitative-evidence.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'actuals':len(result['actuals']),'logs':len(result['qualification_log_verification']),'index_mismatches':[x['path'] for x in result['qualification_log_verification'] if x['matches_retained_index'] is False],'resource_summaries':len(result['resource_measurements']),'fixtures':{k:v['paths'] for k,v in result['fixtures'].items()}},indent=2))
