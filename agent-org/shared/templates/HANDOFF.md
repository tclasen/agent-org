# Handoff schema

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/templates/HANDOFF.md
- Affected Paths or Resources: agent-org/shared/templates/HANDOFF.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Copy into an authorized record/checkpoint and replace angle-bracket placeholders. This schema allocates no ID, claim, result or approval. Include the eight metadata fields with actual scope when used.

- Task: <allocated task reference>
- Run: <allocated run reference>
- Native Worker: <observed ID or unknown>
- Checkpoint Time: <UTC>
- Intended Outcome: <accepted objective>
- Completed Actions: <actual actions>
- Changed Files: <exact paths or none>
- Deliverables: <artifact paths/hashes>
- Actual Validation: <commands/exits, expected/actual, evidence hashes>
- Criterion Outcomes: <verified|failed|unverified|blocked|excluded with limits>
- Unresolved Questions: <remaining items or none>
- External Effects: <intent/key/observed IDs/results or unknown/none>
- Resource Use: <cumulative known totals/retries and unknowns>
- Claim Disposition: <retain/release/transfer state>
- Next Action: <one exact safe action and required authority>
