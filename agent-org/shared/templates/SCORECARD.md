# Scorecard schema

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/templates/SCORECARD.md
- Affected Paths or Resources: agent-org/shared/templates/SCORECARD.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Copy into an authorized record/checkpoint and replace angle-bracket placeholders. This schema allocates no ID, claim, result or approval. Include the eight metadata fields with actual scope when used.

- Kind: <organization|project identity|measurement_health>
- Observed At: <UTC>
- Baseline: <approved identity/hash>
- Candidate: <exact identity/hash>
- Evaluator Version: <approved prior evaluator>
- Definition Version: <metric/classification versions>
- Window: <UTC [start,end)>
- As Of: <snapshot cutoff/hash>
- Cohort and Denominator: <explicit identities/count>
- Samples: <count and retained failure/retry count>
- Results: <values/units and evidence paths/hashes>
- Missing and Excluded: <counts/reasons/coverage>
- Unknown Metadata: <model/token/cost/provenance gaps>
- Hard Gates: <criterion outcomes>
- Interpretation: <bounded claim and limits>
- Next Action: <safe action; no result implies promotion>
