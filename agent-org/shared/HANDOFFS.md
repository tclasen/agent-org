# Structured handoff contract

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/HANDOFFS.md
- Affected Paths or Resources: agent-org/shared/HANDOFFS.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Every substantive worker returns/persists a handoff with Task/Run/role/native identity, target/classification, authorized scope and checkpoint time; original intended outcome and completed actions; exact changed paths; artifact locations/hashes and actual commands/exit results; criterion outcomes/failures/limits; unresolved questions/dependencies; intended/observed external effects and identifiers; cumulative budgets/retries; current claim/continuation ownership; and one exact next safe action with required authority.

Use templates/HANDOFF.md for a copyable schema. Link canonical records rather than copying secrets or entire transcripts. Separate requested from observed metadata and implemented from verified results. If nothing changed/effected, say none. Mark uncertainty explicitly; a missing tool response is not success.

Coordinator validates scope, hashes, claim and evidence, then admits independent review. Handoff completion is not approval or acceptance. Fresh replacement must be able to act from linked records without inherited conversation; demonstrate this with actual recovery trial, not only field completeness. Persist handoff at transitions/interruption or before handing ownership to another native worker.
