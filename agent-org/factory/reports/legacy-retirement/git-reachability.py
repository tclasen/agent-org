import json,subprocess,os,datetime
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');ROOT=Path('/Users/Shared/old');ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
a=json.loads((OUT/'git-primary-inventory.json').read_text());b=json.loads((OUT/'git-remote-refs.json').read_text());rows=[]
def run(p,args,stdin=None):return subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',str(p),*args],input=stdin,text=True,capture_output=True,env=ENV,timeout=60)
for r in a['repositories']:
 p=ROOT/r['path']; remotes=[v for v in b['remotes'] if v['code']==0 and any(u['path']==r['path'] for u in v['users'])];remote_refs=[]
 for v in remotes:
  for line in v['refs'].splitlines():
   oid,ref=line.split()
   if ref.startswith(('refs/heads/','refs/tags/')):remote_refs.append({'url':v['url'],'ref':ref,'oid':oid})
 remote_oids=set(x['oid'] for x in remote_refs);known=set();unknown=set()
 if remote_oids:
  chk=run(p,['cat-file','--batch-check=%(objectname) %(objecttype)'],'\n'.join(sorted(remote_oids))+'\n')
  for line in chk.stdout.splitlines():
   oid,typ=line.split()[:2]
   (unknown if typ=='missing' else known).add(oid)
 local=[{'ref':line.split()[0],'oid':line.split()[1]} for line in r['refs']['out'].splitlines()];head=r['head']['out'].strip()
 if head not in {x['oid'] for x in local}:local.append({'ref':'HEAD','oid':head})
 query='\n'.join(sorted({x['oid'] for x in local}))+ '\n' + ''.join('^'+oid+'\n' for oid in sorted(known))
 rev=run(p,['rev-list','--stdin'],query);uncovered=set(rev.stdout.splitlines())
 for ref in local:ref['reachable_from_advertised_branch_or_tag']=rev.returncode==0 and ref['oid'] not in uncovered
 row={'path':r['path'],'head':head,'reachable_head':rev.returncode==0 and head not in uncovered,'local_ref_count':len(local),'covered_ref_count':sum(x['reachable_from_advertised_branch_or_tag'] for x in local),'uncovered_refs':[x for x in local if not x['reachable_from_advertised_branch_or_tag']],'remote_refs':remote_refs,'remote_objects_missing_locally':sorted(unknown),'rev_list_code':rev.returncode,'rev_list_error':rev.stderr,'uncovered_commit_count':len(uncovered)};rows.append(row)
 print(row['path'],row['covered_ref_count'],'/',len(local),'uncovered commits',len(uncovered),'remote objects missing',len(unknown),flush=True)
 (OUT/'git-reachability.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Local commit reachability from live advertised remote heads/tags whose objects are present locally. Missing remote objects leave coverage unknown, not lost. GitHub pull refs excluded.','repositories':rows},indent=2))
