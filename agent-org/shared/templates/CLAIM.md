# Claim schema

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/templates/CLAIM.md
- Affected Paths or Resources: agent-org/shared/templates/CLAIM.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Copy into an authorized record/checkpoint and replace angle-bracket placeholders. This schema allocates no ID, claim, result or approval. Include the eight metadata fields with actual scope when used.

- Task: <allocated task reference>
- Run: <allocated run reference>
- Claim Owner: <role/execution>
- Native Worker: <native ID or unknown>
- Claimed Scope: <canonical paths/resources>
- Observed At: <UTC>
- Checkpoint: <record path/time>
- Conflicting Claims: <checked references or unresolved>
- Release Condition: <completion/cancel/verified transfer>
- Reconciliation: <native and actual state checks>
- Claim Disposition: <active|released|uncertain; uncertainty blocks mutation>
