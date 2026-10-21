import sys,copy,json,importlib.util,pathlib,tempfile,hashlib
ROOT=pathlib.Path('/Users/Shared/agent-org/factory')
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'tests')); sys.path.insert(0,str(ROOT))
import test_improvement as T
import test_dora as D
from instrumentation.events import EventStore

def rebind(b):
    b['context']['registered_plan_hash']=T.gate.digest(b['plan'])
    b['evidence']['plan_hash']=T.gate.digest(b['plan'])
    T.reapprove(b)

def run(label,b):
    r=T.decision(b)
    print(json.dumps({'case':label,**r},sort_keys=True))

b=T.bundle(); b['plan']['changes_evaluator']=True
b['evidence'].update(prior_evaluator_hash=b['context']['approved_evaluator_hash'],adversarial_fixtures_hash='prior-adversarial',dual_version_replay='failed')
b['context']['adversarial_fixtures_hash']='prior-adversarial'; rebind(b)
run('F1 recursive dual replay string failed',b)
for val in [0,{},'true']:
    b=T.bundle(); b['plan']['changes_evaluator']=val; rebind(b)
    run('F1 evaluator change flag '+repr(val),b)
b=T.bundle('efficiency'); b['evidence']['usage']['attempts']=0; T.reapprove(b)
run('F2 usage says 0 attempts while pairs contain 40',b)
b=T.bundle(); b['context']['prior_consumed_seconds']=2850
run('F3 cumulative 2910/3600 no checkpoint',b)
b=T.bundle('outcome')
for p in b['evidence']['pairs']:
    p['baseline_attempts']=[{'value':None,'status':'unknown'}]
    p['candidate_attempts']=[{'value':None,'status':'unknown'}]
T.reapprove(b); run('F4 outcome wholly unknown attempts',b)
# Validate standard negative checks independently of names in supplied tests.
for label,mutate in [
 ('authority mismatch',lambda b:b['evidence'].update(authority_hash='wrong')),
 ('current evaluator wrong',lambda b:b['context'].update(approved_evaluator_code_hash='wrong')),
 ('prior cumulative storage exhaustion',lambda b:b['context'].update(prior_consumed_storage_bytes=999999)),
 ('unassigned reviewer',lambda b:b['approvals'][0].update(agent_id='unknown')),
 ('missing independent regression',lambda b:b['context'].pop('independent_regression_hash')),
]:
 b=T.bundle();mutate(b)
 if label!='unassigned reviewer':T.reapprove(b)
 run('control '+label,b)

# Independent native round-trip, correction, snapshot as-of, causal omission, sparse data.
with tempfile.TemporaryDirectory(prefix='RUN-000011-native-') as tmp:
 store=EventStore(pathlib.Path(tmp)/'ledger.jsonl')
 normalized=D.fixture(); ids={e['event_id']:f'EVT-{i:06}' for i,e in enumerate(normalized,1)}
 for i,e in enumerate(normalized,1):
  store.append({'schema_version':1,'event_id':ids[e['event_id']],'event_type':e['type'],'task_id':'TASK-000014','run_id':'RUN-000011','agent_id':'AGENT-000008','classification':'project','occurred_at':e['occurred_at'],'ingested_at':f'2026-02-01T00:00:{i:02}Z','data':{**e['payload'],'provenance':e['provenance']}})
 baseline=D.report(D.dora.ledger_events(store.read_events()))
 assert baseline['services']==D.report()['services']
 replacement=copy.deepcopy(normalized[4]);replacement['payload']['degradation_started_at']='2026-01-02T01:05:00Z'
 store.append({'schema_version':1,'event_id':'EVT-000008','event_type':'correction','task_id':'TASK-000014','run_id':'RUN-000011','agent_id':'AGENT-000008','classification':'project','occurred_at':'2026-02-01T00:00:08Z','ingested_at':'2026-02-01T00:00:08Z','causal_event_ids':['EVT-000005'],'data':{'target_event_id':'EVT-000005','reason':'independent fixture onset correction','provenance':'synthetic://review/correction','replacement':{'event_type':'failure','occurred_at':replacement['occurred_at'],'data':{**replacement['payload'],'provenance':'synthetic://review/replacement'}}}})
 after=D.report(D.dora.ledger_events(store.read_events()))
 assert after['services']['service-a']['failed_deployment_recovery_time']['p50_seconds']==5100
 assert D.report(D.dora.ledger_events(store.read_events()),as_of=7)==baseline
 assert D.report(D.dora.ledger_events(store.read_events(as_of='2026-02-01T00:00:07Z')))==baseline
 assert after['snapshot_digest']!=baseline['snapshot_digest']
 print(json.dumps({'case':'independent native ledger correction ingestion-asof sequence-asof','decision':'pass','original_snapshot':baseline['snapshot_digest'],'corrected_snapshot':after['snapshot_digest']}))

for label,events in [('empty',[]),('commit-only',D.fixture()[:1]),('unlinked recovery',[D.fixture()[-1]]),('deployment no incidents',D.fixture()[:4])]:
 r=D.report(events)
 print(json.dumps({'case':'sparse '+label,'health':r['measurement_health'],'service':r['services']['service-a']},sort_keys=True))
events=D.fixture();events[4]['payload'].pop('causal_evidence')
r=D.report(events)
assert r['services']['service-a']['change_fail_rate']['numerator']==0
assert any(x['reason']=='missing_failure_causality' for x in r['measurement_health']['issues'])
print(json.dumps({'case':'missing causality excludes failure and rework','decision':'pass','health':r['measurement_health']}))
for label,mutate in [
 ('F1 false authority hash bypasses valid trusted authority',lambda b:b['evidence'].update(authority_hash=False)),
 ('F1 false independent regression hash bypasses valid trusted regression',lambda b:b['evidence']['repair'].update(independent_regression_hash=False)),
 ('F1 false evidence plan hash bypasses association check',lambda b:b['evidence'].update(plan_hash=False)),
]:
 b=T.bundle();mutate(b);T.reapprove(b);run(label,b)
b=T.bundle('efficiency');b['plan']['budget']['attempts']=1;b['context']['limits']['attempts']=1;b['evidence']['usage']['attempts']=0;rebind(b)
run('F2 40 actual supplied attempts passes limit 1',b)
