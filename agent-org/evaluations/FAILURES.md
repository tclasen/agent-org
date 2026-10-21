# Installation failure register

- Target System: organization
- Change Classification: organization
- Authorized Scope: Durable record of observed installation failures only
- Affected Paths or Resources: Related task/evaluation evidence; no source changes
- Owning Role: Coordinator
- Related Requirements: REQ-000017, REQ-000028, REQ-000037
- Related Tasks: TASK-000001, TASK-000003, TASK-000004, TASK-000005, TASK-000015, TASK-000018
- Approval Requirements: APP-000001

Stable failure IDs identify actual substantive findings and reconciliation stops. Original raw evidence remains authoritative; this register does not erase failures or turn expected negative test inputs into incidents. Synthetic fixture events have separate fixture namespaces. IDs never reused.

| Failure ID | Affected system | Task | Evidence | Observed failure | Disposition |
| --- | --- | --- | --- | --- | --- |
| FAIL-000001 | organization | TASK-000003 | EVAL-000001 | Review validates edge blocked until its subject was accepted | Repaired and independently accepted in EXP-000001 |
| FAIL-000002 | organization | TASK-000003 | EVAL-000001 | Nonblocking task self-link accepted | Repaired in EXP-000001 |
| FAIL-000003 | organization | TASK-000003 | EVAL-000001 | Task definition accepted in requirement family | Repaired and canonical task/requirement paths qualified |
| FAIL-000004 | organization | TASK-000004 | EVAL-000002 | False required pins bypassed truthiness checks | Repaired in final1.0.1; independent120cases |
| FAIL-000005 | organization | TASK-000004 | EVAL-000002 | Malformed recursive evaluator booleans accepted | Repaired in final1.0.1 |
| FAIL-000006 | organization | TASK-000004 | EVAL-000002 | Observable attempts did not constrain usage summary | Repaired with preserved incomplete-telemetry distinction |
| FAIL-000007 | organization | TASK-000004 | EVAL-000002 | Cumulative80% checkpoint missed prior consumption | Repaired in final1.0.1 |
| FAIL-000008 | organization | TASK-000004 | EVAL-000002 | Unknown outcome attempt records established benefit | Repaired in final1.0.1 |
| FAIL-000009 | organization | TASK-000004 | EVAL-000002 | Orphan recovery silently reported complete measurement health | Versioned DORA1.0.1 disclosure correction; arithmetic preserved |
| FAIL-000010 | organization | TASK-000015 | RUN-000015 | Missing pair row became reject instead of inconclusive | First-attempt failure preserved; retry1 corrected |
| FAIL-000011 | organization | TASK-000015 | RUN-000015 | New regression demanded identical health despite authorized orphan disclosure | Fixed expectation requires previous issues plus exact new orphan issue |
| FAIL-000012 | organization | TASK-000015 | EVAL-000005 | Missing/null/empty attempt list with complete pair rows rejected | Six independent cases fixed in finalretry2; original inconclusive restored |
| FAIL-000013 | organization | TASK-000018 | RUN-000012 | Guide omitted explicitly required startup procedure | Initial rejected guide retained; narrow repair independently accepted |
| FAIL-000014 | project | TASK-000005 | RUN-000001 | Copied rollback scratch checkout entered initial staging selection | Index audit caught gitlinks; unstaged and moved copy to ignored execution area; no commit contained it |
| FAIL-000015 | project | TASK-000005 | RUN-000001 | Unscoped whitespace check conflicted with immutable archive/raw diff bytes | Original evidence preserved; active-source check excludes only declared immutable data |
| FAIL-000016 | organization | TASK-000015 | RUN-000019 | Whole-factory inventory detected concurrent root event append | Stopped; owner attributed independently, old prefix and exact EVT3/4 chain verified; no unauthorized worker edit |
