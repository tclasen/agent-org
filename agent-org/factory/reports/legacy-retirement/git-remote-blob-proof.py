import json,subprocess,os,hashlib,datetime
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');data=json.loads((OUT/'git-remote-recovery-proof.json').read_text());ENV=dict(os.environ,GIT_TERMINAL_PROMPT='0',GIT_OPTIONAL_LOCKS='0');rows=[]
for r in data['results']:
 local='/Users/Shared/old/'+r['path'];sample=r['ref_results'][0]['actual_oid'];paths=subprocess.check_output(['git','-C',local,'diff-tree','--root','--no-commit-id','--name-only','-r',sample],text=True,env=ENV).splitlines();selected=[]
 for p in paths:
  q=subprocess.run(['git','-C',local,'cat-file','-t',sample+':'+p],capture_output=True,text=True,env=ENV)
  if q.returncode==0 and q.stdout.strip()=='blob':selected=[(sample,p)];break
 if r['path']=='projects/penny':selected += [('16342ccc52864b1cc3a917b1c743280a18dbf1ff',p) for p in ['docs/TRACEABILITY.md','docs/adr/0004-layered-city-and-installed-content.md']]
 # Explicit read-only remote configuration in disposable independent clone for promised blobs.
 subprocess.run(['git','-C',r['scratch'],'config','remote.origin.url',r['remote']],check=True,env=ENV)
 subprocess.run(['git','-C',r['scratch'],'config','remote.origin.promisor','true'],check=True,env=ENV)
 for oid,p in selected:
  remote=subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',r['scratch'],'show',oid+':'+p],capture_output=True,env=ENV,timeout=60);original=subprocess.check_output(['git','-C',local,'show',oid+':'+p],env=ENV)
  rows.append({'repository':r['path'],'commit':oid,'path':p,'remote_read_code':remote.returncode,'bytes':len(remote.stdout),'sha256':hashlib.sha256(remote.stdout).hexdigest(),'matches_original':remote.returncode==0 and remote.stdout==original,'error':remote.stderr.decode(errors='replace') if remote.returncode else ''})
 print(r['path'],len(selected),'source blobs checked',flush=True)
(OUT/'git-remote-blob-proof.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':rows,'limits':'Targeted changed source/doc blob retrieval in addition to every archived commit/tree. Does not verify all historical asset blobs or application behavior.'},indent=2))
assert all(r['matches_original'] for r in rows)
