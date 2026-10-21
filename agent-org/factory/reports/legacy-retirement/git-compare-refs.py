import json,subprocess,os,datetime
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement'); ROOT=Path('/Users/Shared/old')
a=json.loads((OUT/'git-primary-inventory.json').read_text());b=json.loads((OUT/'git-remote-refs.json').read_text())
rows=[]
for r in a['repositories']:
 remotes=[v for v in b['remotes'] if any(u['path']==r['path'] for u in v['users'])];accessible=[v for v in remotes if v['code']==0]
 refs=[]
 for line in r.get('refs',{}).get('out','').splitlines():
  parts=line.split(); name,oid=parts[:2];matches=[]
  for v in accessible:
   for l in v['refs'].splitlines():
    rid,rname=l.split()
    if rid==oid:matches.append({'url':v['url'],'ref':rname})
  refs.append({'ref':name,'oid':oid,'remote_matches':matches})
 head=r.get('head',{}).get('out','').strip(); row={'path':r['path'],'head':head,'accessible_urls':[v['url'] for v in accessible],'inaccessible_urls':[v['url'] for v in remotes if v['code']!=0],'refs':refs,'status':r.get('status',{}),'ignored':r.get('ignored',{})};rows.append(row)
 print(r['path'],'accessible',len(accessible),'exact_refs',sum(bool(x['remote_matches']) for x in refs),'/',len(refs),'HEAD exact',any(x['oid']==head and x['remote_matches'] for x in refs))
(OUT/'git-ref-comparison.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repositories':rows},indent=2))
