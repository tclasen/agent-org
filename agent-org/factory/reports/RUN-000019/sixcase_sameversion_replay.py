import sys,json,copy,datetime
from pathlib import Path
sys.dont_write_bytecode=True
root=Path('/Users/Shared/agent-org/factory')
sys.path[:0]=[str(root/'tests'),str(root)]
import test_improvement as T
import test_gate_regressions as R
retry1=R.load('retry1_gate_101',Path('/private/tmp/RUN-000019-evidence/retry1-before/factory/quality-gates/improvement.py'))
records=[]
for original in json.loads((root/'reports/RUN-000017/missing-attempts-results.json').read_text())['results']:
 row={k:original[k] for k in ('claim','mutation','expected_under_prior_contract')}
 for label,gate,expected in [('baseline',R.OLD_GATE,'inconclusive'),('retry1_same_version',retry1,'reject'),('retry2_same_version',T.gate,'inconclusive')]:
  b=copy.deepcopy(original['baseline' if label=='baseline' else 'candidate']['bundle'])
  b['plan']['version']=gate.VERSION
  b['plan']['evaluator_code_hash']=gate.evaluator_digest()
  b['context']['approved_evaluator_code_hash']=gate.evaluator_digest()
  R.rebind(b)
  result=R.decision(gate,b)
  assert result['decision']==expected,(row,label,result)
  assert not result['benefit'],(row,label,result)
  row[label]={'version':gate.VERSION,'bundle':b,'result':result}
 records.append(row)
assert len(records)==6
print(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'six_fixed_cases':records,'source_of_inputs':'RUN17 preserved independent missing-attempts-results.json; source/version and dependent digest substitutions only'},sort_keys=True))
