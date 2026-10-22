# Effect reconciliation record

Link the admitted task, run, authority and exact candidate. The journal is native telemetry, not a permission grant.

| Field | Required value |
| --- | --- |
| effect_id | Stable identity for one operation intent |
| operation | Already authorized native action |
| resource | Exact owning repository or service resource |
| target | Exact branch, ref or destination |
| candidate_hash | SHA-256 of the approved content identity |
| authority | Existing applicable grant |
| task and run | Accountable task and native run |
| receipt | Matching source, observation time, remote identity and confirmed/not_executed/unknown status |

Prepare → record attempt → perform native action → inspect destination → record matching observation. Unknown or corrupt evidence requires reconciliation, never blind retry. Confirmed receipt prevents repeat dispatch. Source attribution is not authentication; verify it independently. Preserve all failed attempts and bounded retries. Include verified main delivery and next safe action in the handoff.
