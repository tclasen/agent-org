import sys,copy,json,hashlib,datetime,subprocess,os,shutil,time
from pathlib import Path
sys.dont_write_bytecode=True
root=Path('/Users/Shared/agent-org'); factory=root/'factory';out=Path('/private/tmp/RUN-000017')
sys.path[:0]=[str(factory/'tests'),str(factory)]
import test_improvement as T
import test_dora as D
import test_gate_regressions as R
rows=[]
def check(label,b,expect='nonpass',checkpoint=None):
    result=T.decision(b)
    assert (result['decision']!='pass' if expect=='nonpass' else result['decision']==expect),(label,result)
    if expect=='nonpass':assert not result['benefit'],(label,result)
    if checkpoint is not None:assert result['checkpoint_required'] is checkpoint,(label,result)
    rows.append({'case':label,'result':result})
def bind(b):
    b['evidence']['plan_hash']=T.gate.digest(b['plan']);b['context']['registered_plan_hash']=T.gate.digest(b['plan']);T.reapprove(b)
# Fresh invalid types across all required string pins, preserving valid association hashes where possible.
paths=[('plan',key) for key in ['candidate_head','evaluator_code_hash','baseline_hash','candidate_hash','workload_hash','evaluator_hash','criteria_hash','implementer']]
paths += [('context',key) for key in ['approved_baseline_hash','approved_evaluator_hash','approved_evaluator_code_hash','current_candidate_hash','current_head','authority_hash','registered_plan_hash','independent_regression_hash']]
paths += [('evidence',key) for key in ['plan_hash','authority_hash']]
paths += [('evidence','repair','independent_regression_hash')]
paths += [('approvals',i,key) for i in [0,1] for key in ['agent_id','candidate_hash','candidate_head','plan_hash','evidence_hash','evaluator_hash']]
for path in paths:
    for val in [False,True,0,1,[],{},None,'',' \t\n']:
        b=T.bundle();target=b
        for key in path[:-1]:target=target[key]
        target[path[-1]]=val
        if path[0]=='plan':bind(b)
        elif path[0]=='evidence':T.reapprove(b)
        check('strict '+str(path)+' '+repr(val),b)
# Exact string comparison: no whitespace stripping for nonempty pins.
for path in [('evidence','authority_hash'),('evidence','repair','independent_regression_hash'),('approvals',0,'candidate_head')]:
    b=T.bundle();target=b
    for key in path[:-1]:target=target[key]
    target[path[-1]]+=' '
    if path[0]=='evidence':T.reapprove(b)
    check('exact '+str(path),b,'reject')
for claim in ['outcome','efficiency']:
    for usage,limit,expect in [(40,41,'pass'),(40,40,'inconclusive'),(0,1,'reject'),(39,100,'reject'),(41,100,'reject')]:
        b=T.bundle(claim);b['evidence']['usage']['attempts']=usage;b['plan']['budget']['attempts']=limit;b['context']['limits']['attempts']=limit;bind(b)
        check(f'{claim} attempts {usage}/{limit}',b,expect)
    for val in [None,[],{},'unknown',[{'value':90,'status':None}],[{'value':None,'status':'failed'}],[{'value':False,'status':'passed'}]]:
        b=T.bundle(claim);b['evidence']['pairs'][1]['candidate_attempts']=val;T.reapprove(b);check(claim+' malformed attempts '+repr(val),b)
    b=T.bundle(claim);b['evidence']['pairs'].pop();T.reapprove(b);check(claim+' incomplete known count upper summary',b,'inconclusive')
    b['evidence']['usage']['attempts']=37;T.reapprove(b);check(claim+' incomplete undercount',b,'reject')
# Failed costs retained and exact budget: extra retry counted yet omitted total rejected.
b=T.bundle('efficiency');b['evidence']['pairs'][3]['candidate_attempts'].append({'status':'failed','value':50});b['evidence']['usage']['attempts']=41;T.reapprove(b);check('failed retry costs hidden in summary',b,'reject')
# Recursive pin absence and exact replay boolean plus authentic synthetic positive.
for field in ['prior_evaluator_hash','adversarial_fixtures_hash','dual_version_replay']:
    for val in [False,1,'true',None,'','wrong']:
        b=T.bundle();b['plan']['changes_evaluator']=True;b['context']['adversarial_fixtures_hash']='prior-tests';b['evidence'].update(prior_evaluator_hash=b['context']['approved_evaluator_hash'],adversarial_fixtures_hash='prior-tests',dual_version_replay=True);b['evidence'][field]=val;bind(b);check('recursive '+field+' '+repr(val),b)
for prior,current,expect,checkpoint in [(2819,60,'pass',False),(2820,60,'pass',True),(2850,60,'pass',True),(3540,60,'inconclusive',True)]:
    b=T.bundle();b['context']['prior_consumed_seconds']=prior;b['evidence']['usage']['active_seconds']=current;T.reapprove(b);check(f'cumulative {prior}+{current}',b,expect,checkpoint)
# Orphan cutoff exact boundary, rejected attributed failure, and ingestion-asof.
dora=[]
for name,events,kwargs,partial in [
 ('orphan at cutoff',[dict(copy.deepcopy(D.fixture()[-1]),occurred_at=D.END)],{},True),
 ('orphan after cutoff',[dict(copy.deepcopy(D.fixture()[-1]),occurred_at='2026-01-03T00:00:00.000001Z')],{},False),
 ('recovery only',[D.fixture()[-1]],{},True),
 ('failure removed',[e for e in D.fixture() if e['type']!='failure'],{},True),
 ('asof pre-recovery',D.fixture(),{'as_of':6},False),
 ('full valid',D.fixture(),{},False)]:
    old=R.OLD_DORA.calculate(events,D.CLASSIFICATION,D.START,D.END,**kwargs);new=D.report(events,**kwargs)
    assert old['services']==new['services'],name
    assert (new['measurement_health']['status']=='partial')==partial,(name,new['measurement_health'])
    dora.append({'case':name,'baseline':old,'candidate':new})
# Retained original 22 observations and 58 frozen typed mutation cases, raw fresh executions.
original={'baseline':R.replay_original(R.OLD_GATE,R.OLD_DORA),'candidate':R.replay_original(T.gate,D.dora)}
assert len(original['baseline'])==len(original['candidate'])==22
(out/'original22.json').write_text(json.dumps(original,sort_keys=True)+'\n')
(out/'independent-results.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'gate_cases':rows,'dora_cases':dora},sort_keys=True)+'\n')
print(json.dumps({'independent_gate_cases':len(rows),'independent_dora_cases':len(dora),'original_observations':22,'all_passed':True}))
