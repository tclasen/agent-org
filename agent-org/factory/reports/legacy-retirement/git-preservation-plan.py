import json,subprocess,os,re,datetime
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');ROOT=Path('/Users/Shared/old');ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
x=json.loads((OUT/'git-reachability.json').read_text());plans=[]
patterns=[('private_key',re.compile(rb'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----')),('github_token',re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b')),('aws_access_key',re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b')),('openai_like_key',re.compile(rb'\bsk-(?:proj-)?[A-Za-z0-9_-]{40,}\b'))]
def git(p,*args):return subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',str(p),*args],capture_output=True,env=ENV,timeout=60)
for r in x['repositories']:
 if not r['remote_refs'] or not r['uncovered_refs'] or r['remote_objects_missing_locally']:continue
 p=ROOT/r['path'];dest=sorted({q['url'] for q in r['remote_refs']})[0]; refs=[]
 for q in r['uncovered_refs']:
  old=q['ref'];suffix=old.removeprefix('refs/heads/') if old.startswith('refs/heads/') else old.removeprefix('refs/').replace('/','-')
  refs.append({'source_ref':old,'oid':q['oid'],'destination_ref':'refs/heads/archive/legacy-20261021/'+suffix})
 remotes=sorted({q['oid'] for q in r['remote_refs']});local=sorted({q['oid'] for q in refs}); rr=git(p,'rev-list','--objects',*local,'--not',*remotes)
 if rr.returncode:raise RuntimeError(rr.stderr.decode())
 objects={line.split(b' ',1)[0].decode():line.split(b' ',1)[1].decode(errors='replace') if b' ' in line else '' for line in rr.stdout.splitlines()};findings=[];total=0;blobs=0;large=[]
 for oid,path in objects.items():
  t=git(p,'cat-file','-t',oid)
  if t.stdout.strip()!=b'blob':continue
  size=int(git(p,'cat-file','-s',oid).stdout)
  if size>20*1024*1024:large.append({'oid':oid,'path':path,'size':size});continue
  data=git(p,'cat-file','blob',oid).stdout;total+=len(data);blobs+=1
  for name,pat in patterns:
   if pat.search(data):findings.append({'kind':name,'oid':oid,'path':path})
  if re.search(r'(^|/)(\.env(?:\.[^/]+)?|id_rsa|credentials(?:\.json)?)$',path) and not re.search(r'(example|sample|test|fixture)',path,re.I):findings.append({'kind':'sensitive_filename','oid':oid,'path':path})
 plan={'path':r['path'],'destination':dest,'refs':refs,'scanned_new_blobs':blobs,'scanned_bytes':total,'findings':findings,'large_unscanned_blobs':large,'scan_limits':'High-confidence token/private-key patterns and sensitive filenames only; not a comprehensive secret audit. Existing repository content only; no working-tree or ignored payload included.'};plans.append(plan)
 (OUT/'git-preservation-plan.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'plans':plans},indent=2));print(r['path'],len(refs),'refs',blobs,'blobs',len(findings),'findings',len(large),'large',flush=True)
