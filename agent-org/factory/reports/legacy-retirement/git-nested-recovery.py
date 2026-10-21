"""Read-only follow-up for relocated pointers, alternate object stores and empty markers."""
import os,json,subprocess,concurrent.futures,datetime,hashlib,collections
from pathlib import Path
ROOT=Path('/Users/Shared/old'); OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
a=json.loads((OUT/'git-nested-inventory.json').read_text())['repositories']
ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
def call(p,args,env=None,gd=None):
 cmd=['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','-c','diff.external=']
 cmd+=['--git-dir='+str(gd),'--work-tree='+str(p)] if gd else ['-C',str(p)]
 r=subprocess.run(cmd+args,capture_output=True,text=True,errors='replace',env=env or ENV,timeout=30)
 return {'code':r.returncode,'out':r.stdout,'err':r.stderr}
def recover(row):
 p=ROOT/row['path'];gd=Path(row['effective_gitdir']);r={'path':row['path']}
 alt=gd/'objects/info/alternates'
 if alt.exists():
  targets=alt.read_text(errors='replace').splitlines();r['alternates']=[{'original':x,'exists':Path(x).exists(),'remapped':str(ROOT/Path(x).relative_to('/Users/Shared')) if x.startswith('/Users/Shared/') else None} for x in targets]
  maps=[x['remapped'] for x in r['alternates'] if x['remapped'] and Path(x['remapped']).exists()]
  if maps:
   env=dict(ENV,GIT_ALTERNATE_OBJECT_DIRECTORIES=os.pathsep.join(maps))
   for name,args in [('head_object',['cat-file','-t',row['head']['out'].strip()]),('log',['log','-3','--format=%H %s']),('status',['status','--porcelain=v1','--untracked-files=all'])]:r[name]=call(p,args,env=env,gd=gd)
 if row['head']['code']:
  r['gitdir_entries']=sorted(x.name for x in gd.iterdir()) if gd.is_dir() else None
  if r['gitdir_entries']:
   for name,args in [('refs',['for-each-ref','--format=%(refname) %(objectname)']),('status',['status','--porcelain=v1','--untracked-files=all']),('branch',['symbolic-ref','-q','HEAD'])]:r[name]=call(p,args,gd=gd)
 return r
res=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 for r in ex.map(recover,a):
  if len(r)>1:res.append(r)
(OUT/'git-nested-recovery.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Set remapped GIT_ALTERNATE_OBJECT_DIRECTORIES only in subprocess environment; explicit --git-dir/--work-tree; no source mutations. Empty dirs are placeholders, not valid repos.','results':res},indent=2))
print('supplement rows',len(res),'alternates',sum('alternates' in x for x in res),'status codes',collections.Counter(x.get('status',{}).get('code') for x in res),'object codes',collections.Counter(x.get('head_object',{}).get('code') for x in res))
# Dependency path metadata and reflog counts, no identities/content retained.
meta=[]
for row in a:
 gd=Path(row['effective_gitdir']);rec={'path':row['path']};found=[]
 for path in [gd/'logs/HEAD',gd/'index',gd/'config',gd/'HEAD',gd/'commondir',gd/'gitdir']:
  if path.is_file():
   b=path.read_bytes();d={'file':path.name,'size':len(b),'sha256':hashlib.sha256(b).hexdigest()}
   if path.name=='HEAD':d['value']=b.decode(errors='replace').strip()
   if path.name in ['commondir','gitdir']:d['value']=b.decode(errors='replace').strip()
   if path.name=='HEAD' and path.parent.name=='logs':d['line_count']=len(b.splitlines());d.pop('value',None)
   found.append(d)
 rec['git_metadata']=found
 meta.append(rec)
(OUT/'git-nested-metadata.json').write_text(json.dumps({'repositories':meta},indent=2))
