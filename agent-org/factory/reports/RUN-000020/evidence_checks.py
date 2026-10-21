import sys,json,hashlib,datetime
from pathlib import Path
sys.dont_write_bytecode=True
root=Path('/Users/Shared/agent-org');e=Path('/private/tmp/RUN-000019-evidence');out=Path('/private/tmp/RUN-000020')
sys.path.insert(0,str(root/'factory'))
from instrumentation.events import EventStore
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((e/'final-manifest.json').read_text());before=json.loads((e/'before-inventory.json').read_text())['files']
for p,v in m['artifacts'].items():assert sha(e/p)==v['sha256'],p
for p,v in m['candidate'].items():assert sha(root/p)==v['sha256'],p
# Raw process outcome records and their actual output hashes.
for f in e.glob('*.metadata.json'):
 j=json.loads(f.read_text());assert j['exit']==0,f.name
 for stream in ('stdout','stderr'):assert sha(e/(f.name.replace('.metadata.json','.')+stream))==j[stream+'_sha256']
# Exact concurrent append only: prior bytes retained, valid chain, named ownership.
ledger=root/'factory/events/installation.jsonl';raw=ledger.read_bytes();old=before['factory/events/installation.jsonl']
assert hashlib.sha256(raw[:old['bytes']]).hexdigest()==old['sha256']
with ledger.open('rb') as stream:events=EventStore(ledger)._read(stream)
new=[json.loads(s) for s in raw[old['bytes']:].splitlines()]
assert [r['event_id'] for r in new]==['EVT-000003','EVT-000004']
assert [r['event_type'] for r in new]==['pr.created','ci.observed']
assert all(r['run_id']=='RUN-000001' and r['task_id']=='TASK-000005' and r['agent_id']=='AGENT-000001' for r in new)
# Account for every previously inventoried factory path, retaining reconciliation failure.
changed=[p for p,v in before.items() if sha(root/p)!=v['sha256']]
assert sorted(changed)==sorted(list(m['candidate'])+['factory/events/installation.jsonl']),changed
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'run19_manifest_sha256':sha(e/'final-manifest.json'),'run19_artifacts_verified':len(m['artifacts']),'previous_factory_inventory_count':len(before),'changed_existing_paths':changed,'ledger_old_prefix_hash':old['sha256'],'ledger_current_hash':sha(ledger),'ledger_events_validated':len(events),'root_event_ids':[r['event_id'] for r in new],'attribution':'Coordinator explicitly declared RUN1/TASK5/APP1 authorship. Local chain/prefix/identities verified; external GitHub claims not independently fetched in read-only no-network review.','scope_failure_preserved':sha(e/'end-inventory-failure.json')}
(out/'evidence-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
