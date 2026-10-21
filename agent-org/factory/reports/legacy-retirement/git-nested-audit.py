"""Task 33 read-only Git nested-marker audit. Does not import or execute legacy code."""
import os,json,subprocess,concurrent.futures,datetime,hashlib,re,collections
from pathlib import Path
ROOT=Path('/Users/Shared/old'); OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0',GIT_CONFIG_NOSYSTEM='1')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
def clean(s):return re.sub(r'(https?://)[^/@\s]+:[^/@\s]+@',r'\1[REDACTED]@',s)
def git(p,*args,gd=None):
 cmd=['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','-c','diff.external=']
 if gd:cmd += ['--git-dir='+str(gd),'--work-tree='+str(p)]
 else:cmd+=['-C',str(p)]
 try:
  r=subprocess.run(cmd+list(args),capture_output=True,text=True,errors='replace',env=ENV,timeout=30)
  return {'code':r.returncode,'out':clean(r.stdout),'err':clean(r.stderr)}
 except subprocess.TimeoutExpired:return {'code':124,'out':'','err':'timeout 30s'}
def audit(item):
 p=ROOT/item['path'];r=dict(item);gd=None
 if item['kind']=='file':
  ptr=(p/'.git').read_text().strip();t=Path(ptr.removeprefix('gitdir: '));t=t if t.is_absolute() else p/t
  r['original_gitdir']=str(t);r['original_target_exists']=t.exists()
  if not t.exists() and str(t).startswith('/Users/Shared/'):
   mapped=ROOT/t.relative_to('/Users/Shared')
   r['remapped_gitdir']=str(mapped);r['remapped_target_exists']=mapped.exists()
   if mapped.exists():gd=mapped
 r['effective_gitdir']=str(gd or p/'.git')
 for name,args in [('head',('rev-parse','HEAD')),('branch',('symbolic-ref','-q','HEAD')),('common_dir',('rev-parse','--git-common-dir')),('refs',('for-each-ref','--format=%(refname) %(objectname)','refs/heads','refs/tags','refs/stash')),('remotes',('remote','-v')),('log',('log','-3','--format=%H %s')),('status',('status','--porcelain=v1','--untracked-files=all'))]:
  r[name]=git(p,*args,gd=gd)
  if name=='head' and r[name]['code']:break
 if item['kind']=='file' and r.get('head',{}).get('code')==0:
  r['ignored']=git(p,'ls-files','--others','--ignored','--exclude-standard','--directory',gd=gd)
  r['index']=git(p,'ls-files','--stage',gd=gd)
  r['tracked_delta']=git(p,'diff','--no-ext-diff','--no-textconv','--raw',gd=gd)
  r['staged_delta']=git(p,'diff','--cached','--no-ext-diff','--no-textconv','--raw',gd=gd)
 return r
if __name__=='__main__':
 old=json.loads((OUT/'git-all-markers.json').read_text());prim=json.loads((OUT/'git-primary-inventory.json').read_text());pri={r['path'] for r in prim['repositories']}
 # Expand all prior cache/build/vendor exclusions. Dependency package internals and bytecode remain explicitly excluded.
 markers={r['path']:r for r in old['markers']};exclusions=[];errors=[];links=[]
 prune={'.git','node_modules','.venv','venv','__pycache__','uv-cache'}
 def err(e):errors.append(str(e))
 for base,ds,fs in os.walk(ROOT,followlinks=False,onerror=err):
  p=Path(base)
  if '.git' in ds or '.git' in fs:
   rel=str(p.relative_to(ROOT));markers.setdefault(rel,{'path':rel,'kind':'directory' if '.git' in ds else 'file','discovery':'expanded traversal'})
  for d in ds[:]:
   q=p/d
   if q.is_symlink():links.append({'path':str(q.relative_to(ROOT)),'target':os.readlink(q)});ds.remove(d)
   elif d in prune:
    if d!='.git':exclusions.append(str(q.relative_to(ROOT)))
    ds.remove(d)
 nested=[r for k,r in sorted(markers.items()) if k not in pri]
 (OUT/'git-nested-discovery.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'total_markers':len(markers),'original_markers':len(old['markers']),'nested_count':len(nested),'new_markers':[r for r in nested if r.get('discovery')],'remaining_exclusions':exclusions,'symlinks':links,'errors':errors},indent=2))
 print('DISCOVERY',len(markers),'nested',len(nested),'new',len(markers)-len(old['markers']),flush=True)
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for i,r in enumerate(ex.map(audit,nested),1):
   results.append(r)
   if i%100==0:print('AUDIT',i,flush=True)
 payload={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_hashes':{f:sha(OUT/f) for f in ['git-all-markers.json','git-primary-inventory.json']},'repositories':results,'constraints':'No Git mutations/network/legacy code; optional locks off; hooks/fsmonitor/external diff disabled; 30s command timeout.'}
 (OUT/'git-nested-inventory.json').write_text(json.dumps(payload,indent=2))
 print('DONE',len(results),collections.Counter(r.get('head',{}).get('code') for r in results),flush=True)
