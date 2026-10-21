"""Read-only legacy Git metadata inventory; does not execute repository code."""
import os,json,subprocess,concurrent.futures,datetime,re
from pathlib import Path
ROOT=Path('/Users/Shared/old'); OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
def git(p,*args):
 try:
  r=subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',str(p),*args],capture_output=True,text=True,env=ENV,timeout=35)
  return {'code':r.returncode,'out':r.stdout,'err':r.stderr}
 except subprocess.TimeoutExpired:return {'code':124,'out':'','err':'timeout 35s'}
def sanitize(x):return re.sub(r'(https?://)[^/@\s]+:[^/@\s]+@',r'\1[REDACTED]@',x)
def audit(p):
 result={'path':str(p.relative_to(ROOT)),'git_marker':'directory' if (p/'.git').is_dir() else 'file'}
 if (p/'.git').is_file():result['git_pointer']=(p/'.git').read_text(errors='replace').strip()
 for name,args in [('root',('rev-parse','--show-toplevel')),('common_dir',('rev-parse','--git-common-dir')),('head',('rev-parse','HEAD')),('status',('status','--porcelain=v1','--untracked-files=all')),('branch',('branch','--show-current')),('remotes',('remote','-v')),('refs',('for-each-ref','--format=%(refname) %(objectname) %(upstream) %(upstream:track)','refs/heads','refs/tags','refs/stash')),('worktrees',('worktree','list','--porcelain')),('ignored',('ls-files','--others','--ignored','--exclude-standard','--directory'))]:
  r=git(p,*args);r['out']=sanitize(r['out']);r['err']=sanitize(r['err']);result[name]=r
  if name=='root' and r['code']:break
 return result
if __name__=='__main__':
 primary=[]; nonrepos=[]
 for family in ['projects','work']:
  for p in sorted((ROOT/family).iterdir()):
   if p.is_dir() and not p.is_symlink():
    (primary if (p/'.git').exists() else nonrepos).append(p)
 primary.append(ROOT/'factory')
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
  for result in ex.map(audit,primary):
   results.append(result); (OUT/'git-primary-inventory.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repositories':results,'nonrepository_top_level':[str(p.relative_to(ROOT)) for p in nonrepos]},indent=2))
   print(result['path'], 'invalid' if result['root']['code'] else 'dirty='+str(len(result['status']['out'].splitlines()))+' remotes='+str(len(result['remotes']['out'].splitlines())),flush=True)
 # Complete marker traversal excluding dependencies and build caches; these exclusions are recorded.
 prune={'.git','node_modules','.venv','venv','__pycache__','.next','.cache','vendor','target','dist','build','uv-cache','.mypy_cache','.pytest_cache'}
 markers=[]; excluded=[]; links=[]; errors=[]
 def error(e):errors.append(str(e))
 for p,ds,fs in os.walk(ROOT,followlinks=False,onerror=error):
  p=Path(p)
  if '.git' in ds or '.git' in fs:
   item={'path':str(p.relative_to(ROOT)),'kind':'directory' if '.git' in ds else 'file'}
   if item['kind']=='file':
    try:item['pointer']=(p/'.git').read_text(errors='replace').strip()
    except OSError as e:item['error']=str(e)
   markers.append(item)
  for d in ds[:]:
   q=p/d
   if q.is_symlink():links.append({'path':str(q.relative_to(ROOT)),'target':os.readlink(q)});ds.remove(d)
   elif d in prune:excluded.append(str(q.relative_to(ROOT)));ds.remove(d)
 (OUT/'git-all-markers.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'markers':markers,'excluded_directories':excluded,'symlinks':links,'errors':errors},indent=2))
 print('DONE',len(results),'primary',len(markers),'markers',len(errors),'errors',flush=True)
