import subprocess,json,urllib.request,urllib.error,base64,hashlib,datetime
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');repo='/Users/Shared/old/projects/voldenites'
raw=json.loads(subprocess.check_output(['git','-C',repo,'lfs','ls-files','--all','--json'],text=True));unique={f['oid']:f for f in raw['files']}
cred=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,check=True);vals=dict(l.split('=',1) for l in cred.stdout.splitlines() if '=' in l)
auth='Basic '+base64.b64encode((vals['username']+':'+vals['password']).encode()).decode();results=[];actions={}
items=list(unique.values())
for start in range(0,len(items),100):
 batch=items[start:start+100];body={'operation':'download','transfers':['basic'],'objects':[{'oid':f['oid'],'size':f['size']} for f in batch]}
 req=urllib.request.Request('https://github.com/tclasen/voldenites.git/info/lfs/objects/batch',data=json.dumps(body).encode(),headers={'Authorization':auth,'Accept':'application/vnd.git-lfs+json','Content-Type':'application/vnd.git-lfs+json'},method='POST')
 with urllib.request.urlopen(req,timeout=60) as stream:response=json.load(stream)
 for o in response['objects']:
  a=o.get('actions',{}).get('download');error=o.get('error');results.append({'oid':o['oid'],'size':o['size'],'download_action_available':bool(a),'error_code':error.get('code') if error else None,'error_message':error.get('message') if error else None})
  if a:actions[o['oid']]=a
 print('batch',len(results),'missing',sum(not r['download_action_available'] for r in results),flush=True)
# Verify one median-size representative object fully; signed URLs and authorization never persisted.
available=sorted((r for r in results if r['download_action_available']),key=lambda r:r['size']);selected=available[len(available)//2] if available else None;proof=None
if selected:
 a=actions[selected['oid']];req=urllib.request.Request(a['href'],headers=a.get('header',{}));digest=hashlib.sha256();n=0
 with urllib.request.urlopen(req,timeout=60) as stream:
  while True:
   chunk=stream.read(1024*1024)
   if not chunk:break
   digest.update(chunk);n+=len(chunk)
 proof={'oid':selected['oid'],'expected_size':selected['size'],'downloaded_bytes':n,'sha256':digest.hexdigest(),'verified':n==selected['size'] and digest.hexdigest()==selected['oid']}
report={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'tclasen/voldenites','files':raw['files'],'unique_object_count':len(unique),'unique_logical_bytes':sum(f['size'] for f in unique.values()),'objects':results,'representative_download':proof,'limits':'All referenced local-history LFS object download actions checked live; only median-size representative payload downloaded/hashed. No full-LFS restore or code execution. Credentials/signed URLs stayed in process memory and are not retained.'}
(OUT/'git-lfs-verification.json').write_text(json.dumps(report,indent=2));print('DONE',len(unique),'objects',report['unique_logical_bytes'],'bytes',sum(not r['download_action_available'] for r in results),'missing',proof,flush=True)
