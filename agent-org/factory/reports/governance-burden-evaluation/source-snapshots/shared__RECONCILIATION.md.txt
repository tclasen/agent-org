# Interrupted work and side-effect reconciliation

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/RECONCILIATION.md
- Affected Paths or Resources: agent-org/shared/RECONCILIATION.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Compare task/run/claim state to native worker status, timestamps, actual filesystem artifacts/content hashes, Git branch/index/worktree/remotes, PR/CI state and external operation identifiers. Journal expected versus observed effects before any retry. A timeout, missing response, stale checkpoint or absent worker is unknown outcome, not success/failure proof. Inspect destination or mark blocked ownership/effect uncertainty.

If work exists and is valid, recover it under current scope and candidate identity; do not duplicate mutations or blindly rerun external actions. If worker is active, message/reconcile ownership; if stale, verify no competing execution and record claim transfer before fresh replacement. Never kill/delete another session's resources. Preserve attempts, partial artifacts and failures.

Cancellation checkpoints effects and known unresolved work, interrupts owned workers and prevents new delegation; it does not undo external effects. At acceptance compare intended outcome to independently verified behavior and actual merge state. Mismatch reopens scoped work. Report observation time, missing evidence, remaining capability gaps and exact next action; no stale Markdown status overrides reality.

## Executable reconciliation and recovery

Apply [autonomous execution](AUTONOMOUS_EXECUTION.md) during startup/resumption and before uncertain effect replay. Run the read-only reconciliation consumer, inspect all attributed source disagreements, prepare the scoped manifest, and reconcile journal observations with the real destination before another authorized action. Use its learning and scenario procedures for recurring corrections and fresh-worker recovery; keep existing authority and independent acceptance rules.
