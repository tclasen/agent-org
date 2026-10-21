import json,sys,copy,hashlib,datetime
from pathlib import Path
sys.dont_write_bytecode=True
root=Path('/Users/Shared/agent-org/factory');sys.path[:0]=[str(root),str(root/'tests')]
import test_gate_regressions as R
import test_improvement as T
import test_dora as D
records=[]
for label,claim,path,value,_ in R.typed_cases():
    row={'case':label,'claim':claim,'path':path,'input_value_repr':repr(value)}
    for name,gate in [('baseline',R.OLD_GATE),('candidate',T.gate)]:
        b=R.bundle_for(gate,claim);target=b
        for part in path[:-1]:target=target[part]
        target[path[-1]]=copy.deepcopy(value)
        try:
            if path[0]=='plan':R.rebind(b)
            elif value != float('inf'):T.reapprove(b)
            row[name]=R.decision(gate,b)
        except Exception as exc:
            row[name]={'exception':type(exc).__name__,'message':str(exc)}
    assert row['candidate'].get('decision') in ('reject','inconclusive'),row
    assert not row['candidate']['benefit'],row
    records.append(row)
positive=[]
for claim in ('repair','outcome','efficiency'):
    pair={name:R.decision(g,R.bundle_for(g,claim)) for name,g in [('baseline',R.OLD_GATE),('candidate',T.gate)]}
    assert pair['baseline']['decision']==pair['candidate']['decision']=='pass'
    assert pair['baseline']['benefit']==pair['candidate']['benefit']
    positive.append({'claim':claim,**pair})
old=R.OLD_DORA.calculate(D.fixture(),D.CLASSIFICATION,D.START,D.END);new=D.report()
changed={k for k in old if old[k]!=new[k]}
assert changed=={'calculator_version','definition_version','definition_digest'},changed
b=R.bundle_for(T.gate,'efficiency');b['evidence']['pairs'].pop();T.reapprove(b);incomplete=R.decision(T.gate,b);assert incomplete['decision']=='inconclusive'
b['evidence']['usage']['attempts']=0;T.reapprove(b);underreport=R.decision(T.gate,b);assert underreport['decision']=='reject'
print(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'substitutions':R.SUBSTITUTIONS,'typed_records':records,'positive_controls':positive,'valid_dora_baseline':old,'valid_dora_candidate':new,'only_valid_report_differences':sorted(changed),'incomplete_workload':incomplete,'incomplete_underreport':underreport},sort_keys=True))
