"""Independent RUN17 prior-contract regression, source files read only."""
import sys,json,copy,datetime
from pathlib import Path
sys.dont_write_bytecode=True
sys.path[:0]=['/Users/Shared/agent-org/factory/tests','/Users/Shared/agent-org/factory']
import test_improvement as T
import test_gate_regressions as R
results=[]
for claim in ('outcome','efficiency'):
 for mutation in ('null','missing','empty'):
  row={'claim':claim,'mutation':mutation,'expected_under_prior_contract':'inconclusive'}
  for label,gate in [('baseline',R.OLD_GATE),('candidate',T.gate)]:
   b=R.bundle_for(gate,claim)
   if mutation=='missing':del b['evidence']['pairs'][0]['candidate_attempts']
   else:b['evidence']['pairs'][0]['candidate_attempts']=None if mutation=='null' else []
   T.reapprove(b)
   row[label]={'bundle':b,'result':R.decision(gate,b)}
  assert row['baseline']['result']['decision']=='inconclusive'
  assert row['candidate']['result']['decision']=='reject'
  assert row['candidate']['result']['reasons']==['reported attempts differ from observable attempt records']
  results.append(row)
print(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_regressions':6,'results':results},sort_keys=True))
