"""Fresh object retrieval for newly preserved Git history, without executing source."""
from pathlib import Path
import subprocess,json,os,datetime
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');TMP=Path('/private/tmp/agent-org-legacy-remote-proof');TMP.mkdir(exist_ok=True);ENV=dict(os.environ,GIT_TERMINAL_PROMPT='0',GIT_OPTIONAL_LOCKS='0')
plans=json.loads((OUT/'git-authorized-archive-plan.json').read_text())['plans'];results=[]
plans.append({'path':'projects/factory_evals','destination':'https://github.com/tclasen/factory_evals.git','refs':[{'destination_ref':'refs/heads/main','oid':'0559d82db5da43beda51f2ca7676ec268313026e'}]})
for p in plans:
 dst=TMP/(p['path'].replace('/','-')+'.git');r=subprocess.run(['git','init','--bare',str(dst)],capture_output=True,text=True,env=ENV);assert r.returncode==0
 refs=p['refs'][:]
 if p['path']=='projects/penny':refs.append({'destination_ref':'refs/heads/archive/legacy-20261021/reflog-16342ccc5286','oid':'16342ccc52864b1cc3a917b1c743280a18dbf1ff'})
 filter_args=[] if p['path'].endswith('factory_evals') else ['--filter=blob:none']
 fetch=['git','-c','core.hooksPath=/dev/null','-C',str(dst),'fetch','--no-tags',*filter_args,p['destination'],*[q['destination_ref']+':'+q['destination_ref'] for q in refs]]
 r=subprocess.run(fetch,capture_output=True,text=True,env=ENV,timeout=120)
 row={'path':p['path'],'remote':p['destination'],'scratch':str(dst),'independent_object_store':not (dst/'objects/info/alternates').exists(),'fetch_code':r.returncode,'fetch_error':r.stderr if r.returncode else '', 'ref_results':[]}
 if r.returncode==0:
  for q in refs:
   actual=subprocess.check_output(['git','-C',str(dst),'rev-parse',q['destination_ref']],env=ENV,text=True).strip();tree=subprocess.check_output(['git','-C',str(dst),'rev-parse',actual+'^{tree}'],env=ENV,text=True).strip();local_tree=subprocess.check_output(['git','-C','/Users/Shared/old/'+p['path'],'rev-parse',q['oid']+'^{tree}'],env=ENV,text=True).strip();row['ref_results'].append({'ref':q['destination_ref'],'expected_oid':q['oid'],'actual_oid':actual,'tree':tree,'matches_local_commit_and_tree':actual==q['oid'] and tree==local_tree})
 row['verified']=r.returncode==0 and row['independent_object_store'] and all(q['matches_local_commit_and_tree'] for q in row['ref_results']);results.append(row)
 (OUT/'git-remote-recovery-proof.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':results,'limits':'Four historical repositories fetched blob-filtered; verifies every preserved commit/tree in independent Git object stores, not all asset blobs. factory_evals fetched without filter. No source code run, no full application restore claimed.'},indent=2));print(p['path'],len(refs),'verified',row['verified'],flush=True)
