# Startup, execution and shutdown

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/SESSION_LIFECYCLE.md
- Affected Paths or Resources: agent-org/shared/SESSION_LIFECYCLE.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

The repository-root AGENTS.md activates the canonical organization entrypoint; no directory change or separate activation prompt is required. A client that does not load it can explicitly read that file. This uses the existing harness, not a new runtime. Do not reread unchanged startup sources or initialize a second Coordinator for a delegated worker.

## Startup and resumption

Coordinator checks native workers, Git status/branch/remotes and task/run summaries for nonterminal work. Search registries or canonical records for active status and relevant paths; open records only for pending delivery, interrupted work, overlapping claims, blocking dependencies or affected external effects. Do not read all historical tasks/runs/handoffs. Summaries are discovery aids: verify against actual state and broaden the search if missing, stale or inconsistent. Resolve ownership/effect uncertainty before overlapping mutation or retry.

Inventory undelivered changes/branches/PRs for organization and active managed repositories. Keep them owned and pending until verified owning-remote main delivery; pursue authorized delivery during the active session. Preserve unrelated work. For recovery details read [reconciliation](RECONCILIATION.md) before retrying. Delegated workers reconcile only assigned task/run/dependencies/claims/resources and report other conflicts to Coordinator.

## Work and shutdown

Remain interactive; checkpoint transitions, before effects and every 15 active minutes. Check trigger dedup, enabled state, authority and cumulative resources before invoking triggers; startup/every five accepted substantive tasks may propose improvement review, not automatically launch it. CI runs only through installed native Actions.

On cancellation stop new delegation, interrupt owned workers and reconcile effects. Before shutdown/compaction persist [handoff](HANDOFFS.md): evidence, claim ownership, pending repository/branch/PR, blocker and exact safe next action. No post-session execution or universal tool interception is promised. A fresh session reconciles before resuming; termination never proves effects undone or delivery complete.
