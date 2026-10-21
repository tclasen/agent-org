# Checkpoint schema

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/templates/CHECKPOINT.md
- Affected Paths or Resources: agent-org/shared/templates/CHECKPOINT.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Copy into an authorized record/checkpoint and replace angle-bracket placeholders. This schema allocates no ID, claim, result or approval. Include the eight metadata fields with actual scope when used.

- Task: <allocated task reference>
- Run: <allocated run reference>
- Observed At: <UTC>
- Stage: <actual current stage>
- Native Worker: <observed native ID or unknown>
- Claim Owner: <role/execution>
- Candidate: <revision/tree/dirty identity>
- Completed Actions: <actual actions>
- Artifacts: <paths and content hashes>
- Checks: <commands/exits and evidence>
- External Effects: <intent/key/observed ID/result or unknown/none>
- Budget and Attempts: <cumulative observed usage and gaps>
- Unresolved: <dependencies/uncertainty>
- Claim Disposition: <retain|release|transfer after reconciliation>
- Next Action: <exact action and authority>
