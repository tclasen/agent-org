import sys,json,hashlib,ast,copy,datetime,difflib
from pathlib import Path
sys.dont_write_bytecode=True
root=Path('/Users/Shared/agent-org'); out=Path('/private/tmp/RUN-000020'); prior=root/'factory/reports/RUN-000017'; before=Path('/private/tmp/RUN-000019-evidence/retry1-before')
sys.path[:0]=[str(root/'factory/tests'),str(root/'factory')]
import test_improvement as T
import test_gate_regressions as R
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((root/'factory/reports/RUN-000019/candidate-freeze-proposal.json').read_text())
pins=json.loads((prior/'pins-end.json').read_text())
current={p:sha(root/p) for p in pins['candidate']}
assert {p for p,h in current.items() if h!=pins['candidate'][p]}==set(freeze['changed'])
for p,v in freeze['changed'].items():
 assert current[p]==v['candidate']['sha256']; assert sha(before/p)==v['before']['sha256']
 (out/(Path(p).name+'.diff')).write_text(''.join(difflib.unified_diff((before/p).read_text().splitlines(True),(root/p).read_text().splitlines(True),fromfile='retry1/'+p,tofile='retry2/'+p)))
for p,h in pins['protected'].items():assert sha(root/p)==h,p
prior_manifest=json.loads((prior/'evidence-manifest.json').read_text())
for p,h in prior_manifest['artifacts'].items():assert sha(prior/p)==h,p
# Every preexisting top-level AST node / class method remains intact in driver.
a=ast.parse((before/'factory/tests/test_gate_regressions.py').read_text());b=ast.parse((root/'factory/tests/test_gate_regressions.py').read_text())
for old,new in zip(a.body,b.body):
 if isinstance(old,ast.ClassDef):
  methods={n.name:n for n in new.body if isinstance(n,ast.FunctionDef)}
  for n in old.body:
   assert ast.dump(n)==ast.dump(methods[n.name]),n.name
 else:assert ast.dump(old)==ast.dump(new)
assert len(R.typed_cases())==58
# Original improvement test changes only the declared version fixture.
orig=(root/'factory/baselines/gate-1.0.0/test_improvement.py').read_text()
assert orig.replace('spec = {"version": "1.0.0"','spec = {"version": "1.0.1"')==(root/'factory/tests/test_improvement.py').read_text()
# Fixture substitution exactly regenerated from original values; no weakened data.
for name in ('repair','efficiency'):
 old=json.loads((before/f'factory/benchmarks/{name}.json').read_text());new=json.loads((root/f'factory/benchmarks/{name}.json').read_text())
 old['plan']['evaluator_code_hash']=T.gate.evaluator_digest();old['context']['approved_evaluator_code_hash']=T.gate.evaluator_digest();R.rebind(old)
 assert old==new,name
(out/'pins-start.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate':current,'protected':pins['protected'],'prior_review_manifest':sha(prior/'evidence-manifest.json'),'freeze':sha(root/'factory/reports/RUN-000019/candidate-freeze-proposal.json')},indent=2)+'\n')
rows=[]
def check(label,b,expect,reason=None,gap=None):
 result=T.decision(b)
 assert result['decision']==expect,(label,result)
 if expect!='pass':assert not result['benefit'],(label,result)
 if reason:assert reason in result['reasons'],(label,result)
 if gap:assert gap in result['measurement_gaps'],(label,result)
 rows.append({'case':label,'expected':expect,'bundle':b,'result':result})
# Reuse immutable independent six input bundles, adapting only evaluator + dependent pins.
original=json.loads((prior/'missing-attempts-results.json').read_text())
for row in original['results']:
 b=copy.deepcopy(row['candidate']['bundle']);b['plan']['evaluator_code_hash']=T.gate.evaluator_digest();b['context']['approved_evaluator_code_hash']=T.gate.evaluator_digest();R.rebind(b)
 check('EVAL5 '+row['claim']+' '+row['mutation'],b,'inconclusive',gap='all attempts including failures/retries required')
# Fresh focused matrices covering both sides, all missing forms, count bounds and budgets.
for claim in ('outcome','efficiency'):
 for side in ('baseline','candidate'):
  for form in ('missing','null','empty'):
   for count in (0,38,39,40,100):
    b=T.bundle(claim); pair=b['evidence']['pairs'][7]
    if form=='missing':del pair[side+'_attempts']
    else:pair[side+'_attempts']=None if form=='null' else []
    b['evidence']['usage']['attempts']=count;T.reapprove(b)
    check(f'{claim} {side} {form} count {count}',b,'reject' if count<39 else 'inconclusive')
 for count,limit,expect in ((39,100,'reject'),(40,100,'pass'),(41,100,'reject'),(40,40,'inconclusive'),(40,41,'pass')):
  b=T.bundle(claim);b['evidence']['usage']['attempts']=count;b['plan']['budget']['attempts']=limit;R.rebind(b)
  check(f'{claim} complete {count}/{limit}',b,expect)
 for reported,limit in ((39,39),(40,40),(100,90)):
  b=T.bundle(claim);b['evidence']['pairs'][0]['candidate_attempts']=None;b['evidence']['usage']['attempts']=reported;b['plan']['budget']['attempts']=limit;R.rebind(b)
  check(f'{claim} incomplete exhaustion {reported}/{limit}',b,'inconclusive',gap='resource budget exhausted: attempts')
 for val in (None,False,'100',{},[]):
  for target in ('primary','attempt-value','attempt-status'):
   b=T.bundle(claim)
   if target=='primary':b['evidence']['pairs'][0]['candidate']=val
   else:b['evidence']['pairs'][0]['candidate_attempts'][0]['value' if target=='attempt-value' else 'status']=val
   T.reapprove(b);check(f'{claim} {target} {val!r}',b,'inconclusive')
 # Missing primary value must not skip observable lower-bound enforcement.
 b=T.bundle(claim);b['evidence']['pairs'][0]['candidate']=None;b['evidence']['usage']['attempts']=39;T.reapprove(b);check(claim+' missing primary undercount',b,'reject')
# Complete known failed retry costs must continue rejecting omitted efficiency totals.
b=T.bundle('efficiency');b['evidence']['pairs'][0]['candidate_attempts'].append({'status':'failed','value':50});b['evidence']['usage']['attempts']=41;T.reapprove(b);check('hidden failed retry cost',b,'reject',reason='failed/retried attempt omitted from efficiency total')
for field in ('authority_hash','plan_hash'):
 b=T.bundle();b['evidence'][field]=False;T.reapprove(b);check('false '+field,b,'reject')
b=T.bundle();b['evidence']['repair']['independent_regression_hash']=False;T.reapprove(b);check('false regression',b,'reject')
for prior_seconds,expect in ((2850,'pass'),(3540,'inconclusive')):
 b=T.bundle();b['context']['prior_consumed_seconds']=prior_seconds;T.reapprove(b);check(f'cumulative {prior_seconds}+60',b,expect);assert rows[-1]['result']['checkpoint_required']
(out/'focused-results.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cases':rows},sort_keys=True)+'\n')
print(json.dumps({'all_passed':True,'focused_cases':len(rows),'protected_pins':len(pins['protected']),'prior_evidence_artifacts':len(prior_manifest['artifacts']),'delta_files':len(freeze['changed']),'old_driver_nodes_unchanged':True,'typed_cases':58}))
