"""Bounded source-state metadata for nested preservation exceptions; no source payload copy."""
import os,json,subprocess,hashlib,datetime,concurrent.futures
from pathlib import Path
ROOT=Path('/Users/Shared/old');OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
a=json.loads((OUT/'git-nested-inventory.json').read_text())['repositories']
def g(p,*args,gd=None):
 cmd=['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','-c','diff.external=']
 cmd+=['--git-dir='+str(gd),'--work-tree='+str(p)] if gd else ['-C',str(p)]
 return subprocess.run(cmd+list(args),env=env,capture_output=True,timeout=30)
def evidence(row):
 p=ROOT/row['path'];r={'path':row['path'],'baseline':row['head']['out'].strip(),'files':[],'status':row['status'],'remote':row.get('remotes')}
 raw=g(p,'diff','--no-ext-diff','--no-textconv','--binary','HEAD');r['tracked_diff']={'bytes':len(raw.stdout),'sha256':hashlib.sha256(raw.stdout).hexdigest(),'exit':raw.returncode}
 for line in row['status']['out'].splitlines():
  rel=line[3:];q=p/rel;v={'path':rel,'status':line[:2]}
  if q.is_symlink():v['symlink_target']=os.readlink(q)
  elif q.is_file():
   b=q.read_bytes();v.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  else:v['exists']=q.exists()
  v['generated']= '__pycache__/' in rel or rel.startswith('web/dist/')
  r['files'].append(v)
 r['file_payload_bytes']=sum(v.get('bytes',0) for v in r['files']);r['source_payload_bytes']=sum(v.get('bytes',0) for v in r['files'] if not v['generated'])
 return r
rows=[r for r in a if r.get('status',{}).get('out')]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:result=list(ex.map(evidence,rows))
worktrees=[]
for row in a:
 if row['kind']=='file' and row['head']['code']==0:
  p=ROOT/row['path'];gd=Path(row['effective_gitdir']);head=row['head']['out'].strip();contains=g(p,'for-each-ref','--contains='+head,'--format=%(refname) %(objectname)','refs/heads','refs/remotes',gd=gd)
  worktrees.append({'path':row['path'],'head':head,'branch':row['branch']['out'].strip(),'containing_refs':contains.stdout.decode(errors='replace').splitlines(),'exit':contains.returncode,'ignored':row['ignored']['out'].splitlines()})
(OUT/'git-nested-source-state.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'dirty_repositories':result,'linked_worktree_reachability':worktrees,'limits':'Hashes/size/status identify source state, not a backup. Local remote-tracking containment does not prove current remote availability. No secret scan/source copy performed.'},indent=2))
for r in result:print(r['path'],r['baseline'][:10],len(r['files']),'files',r['file_payload_bytes'],'bytes','diff',r['tracked_diff']['bytes'])
