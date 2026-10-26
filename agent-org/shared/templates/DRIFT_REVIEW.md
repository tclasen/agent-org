# Bounded drift review schema

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/templates/DRIFT_REVIEW.md
- Affected Paths or Resources: agent-org/shared/templates/DRIFT_REVIEW.md
- Owning Role: Coordinator
- Related Requirements: REQ-000059
- Related Tasks: TASK-000243
- Approval Requirements: operator incorporation request; APP-000448; independent exact-candidate review and Chief of Staff approval before normal PR/main delivery

Copy into the owning task/run evidence with actual metadata/scope. This schema grants no scan, code change, specification change, schedule or approval. Follow [bounded drift review](../DESIGN_REVIEW.md#compare-approved-intent-with-bounded-source).

- Trigger and Admitted Scope: <behavior-changing work or reported discrepancy>
- Document Manifest: <path; status; authority; approved revision/hash>
- Source Manifest: <repository/revision; exact files/symbols; hashes>
- Coverage: <what was actually inspected; method; no inferred runtime check>
- Exclusions and Missing Inputs: <excluded/unreadable/stale; effects on result>

| Item | Document intent and location | Source behavior and location | Classification and reason | Decision/task evidence | Owner and next action |
| --- | --- | --- | --- | --- | --- |
| <D01> | <status/hash/claim> | <revision/hash/observed behavior> | <defect/incomplete admitted work/approved revision/outdated documentation/unresolved question> | <canonical link or missing> | <scoped follow-up> |

- Covered-Scope Result: <differences; no drift detected in covered scope; unresolved>
- Equivalence and Unknowns: <renames/behavior comparison; unavailable evidence>
- Recommended Follow-up: <admitted work, owner and authority needed; no auto-repair>
- Verification Limits: <static reading vs executed tests; actual trace coverage>
- Next Safe Action: <exact bounded action or none>
