import json,subprocess,os,datetime,hashlib
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');ROOT=Path('/Users/Shared/old');ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
plan_path=OUT/'git-authorized-archive-plan.json';plan=json.loads(plan_path.read_text());journal={'plan_sha256':hashlib.sha256(plan_path.read_bytes()).hexdigest(),'effects':[]}
def save():(OUT/'git-preservation-effects.json').write_text(json.dumps(journal,indent=2))
for p in plan['plans']:
 if p['findings'] or p['large_unscanned_blobs']:raise RuntimeError('Unresolved scan findings')
 refs=p['refs'];dest=p['destination'];before=subprocess.run(['git','ls-remote',dest],capture_output=True,text=True,env=ENV,timeout=60)
 if before.returncode:raise RuntimeError(before.stderr)
 old={line.split()[1]:line.split()[0] for line in before.stdout.splitlines()}
 for r in refs:
  if r['destination_ref'] in old and old[r['destination_ref']]!=r['oid']:raise RuntimeError('Existing destination ref differs; refusing')
 missing=[r for r in refs if r['destination_ref'] not in old]
 effect={'path':p['path'],'destination':dest,'planned_refs':refs,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'intent-recorded'};journal['effects'].append(effect);save()
 if missing:
  cmd=['git','-c','core.hooksPath=/dev/null','-c','push.followTags=false','-C',str(ROOT/p['path']),'push','--atomic',dest,*[r['oid']+':'+r['destination_ref'] for r in missing]]
  r=subprocess.run(cmd,capture_output=True,text=True,env=ENV,timeout=120);effect['push_code']=r.returncode;effect['push_output']=r.stdout+r.stderr;save()
  if r.returncode:print('PUSH FAILED',p['path'],flush=True);continue
 after=subprocess.run(['git','ls-remote',dest,'refs/heads/archive/legacy-20261021/*'],capture_output=True,text=True,env=ENV,timeout=60);now={line.split()[1]:line.split()[0] for line in after.stdout.splitlines()};effect['readback_code']=after.returncode;effect['verified']=after.returncode==0 and all(now.get(r['destination_ref'])==r['oid'] for r in refs);effect['status']='verified' if effect['verified'] else 'unverified';effect['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();save();print(p['path'],len(refs),'refs',effect['status'],flush=True)
