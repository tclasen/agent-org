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

For every change handoff include delivery state and owning repository/remote/main, tested candidate, branch/PR, merged commit, observed remote-main tip/time, content or ancestry verification and relevant checks. Until those prove delivery, report pending with owner, blocker and next action. A handoff or local-only acceptance cannot close a change task. Proposed durable closure takes effect only after its own verified remote-main merge.

## Remote-main policy delivery — proposed closure

TASK-000051 and review/approval tasks remain awaiting_acceptance until PR8 merges and remote main is verified. Candidate changes are limited to canonical policy and their governance records in an isolated worktree. Structural validation and all 85 tests passed. Independent final-head review and Chief of Staff approval are recorded in PR8 before merge; their pinned decisions do not change the reviewed head. Coordinator owns final merge/main verification and reports its observed identifiers. Any failure leaves the tasks pending. Existing cleanup remains separately owned pending delivery as recorded in factory/reports/remote-main/BACKLOG.md; it was not included in this PR. No post-session execution is promised.

## Tessl research proposed delivery handoff

TASK-000054 with independent TASK-000055 and TASK-000056; Coordinator RUN-000048 owns branch research/tessl-factory in isolated tessl-research worktree. Research report is knowledge/TESSL_FACTORY_RESEARCH.md,2948words,18primary web sources; report hash and detailed verification are in factory/reports/tessl-research/checks.json and REVIEW.md. Independent initial review supports the content and Chief of Staff conditionally supports research delivery. All ten operating changes remain proposals. Structural checks,85tests,18local link occurrences and whitespace passed. Requested versus actual worker metadata remains separate; actual cost unknown.

Existing root cleanup and nested project work are preserved outside this branch. PR8 was independently observed merged at remote main ca6ff20e551bf974c6f52cbdb2f7ebe15facf378; historical prior-run pending prose is not a new blocker. Current task delivery is pending. Exact next action: freeze candidate, obtain both independent final-head confirmations, publish the scoped PR, pass CI, merge normally and verify remote main contains the approved commit. Proposed closure takes effect only then; report live identifiers to the operator. No execution after session termination is promised.
## TASK-000041 / RUN-000041 — local cleanup complete (2026-10-22T00:33:11.887765+00:00)

Coordinator reconciled five clones and scoped cleanup under APP-000012 with independent Planner, Reviewer and Chief of Staff runs42..44. Claims released. Exact changes, checks, preserved failures, candidate/evidence hashes, local-only effects and rollback are in [CLOSURE.md](../factory/reports/project-cleanup/CLOSURE.md). No remote writes or shared promotion. Intended outcome matched; parent organization is primary. Next safe action: no further work for this local request; any later shared delivery uses a separately admitted authorized PR workflow.

## Renewed mandatory delivery — TASK-000041 / RUN-000061

The prior local-only cleanup completion was reopened under APP-000016. Five project PRs now have verified fetched-main content equality (delivery-heads.json). Parent standing authorization/instructions and records remain pending this PR normal review/checks/merge. Proposed closure takes effect only after its own merge and verified remote main; final observed result is returned in the session handoff without leaving another unshipped evidence edit. No research worktree mutation or protection bypass.
