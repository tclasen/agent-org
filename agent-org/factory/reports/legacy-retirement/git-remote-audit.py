import json,os,subprocess,concurrent.futures,datetime,re
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
x=json.loads((OUT/'git-primary-inventory.json').read_text());urls={}
for r in x['repositories']:
 for line in r.get('remotes',{}).get('out','').splitlines():
  name,url,kind=line.split()
  if kind!='(push)':continue
  if url.startswith('git@github.com:'):url='https://github.com/'+url.split(':',1)[1]
  urls.setdefault(url,[]).append({'path':r['path'],'remote':name})
def audit(item):
 url,users=item
 try:
  r=subprocess.run(['git','ls-remote',url],capture_output=True,text=True,timeout=45,env=dict(os.environ,GIT_TERMINAL_PROMPT='0'))
  return {'url':url,'users':users,'code':r.returncode,'refs':r.stdout,'error':r.stderr}
 except subprocess.TimeoutExpired:return {'url':url,'users':users,'code':124,'refs':'','error':'timeout 45s'}
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for row in ex.map(audit,urls.items()):
  results.append(row);(OUT/'git-remote-refs.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'remotes':results},indent=2));print(row['code'],row['url'],len(row['refs'].splitlines()),flush=True)
