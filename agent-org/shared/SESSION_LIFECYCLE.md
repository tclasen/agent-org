# Startup, execution and shutdown

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/SESSION_LIFECYCLE.md
- Affected Paths or Resources: agent-org/shared/SESSION_LIFECYCLE.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Start Codex in the Git repository root. Its root AGENTS.md entrypoint directs loading of agent-org/AGENTS.md, authority/scope, this lifecycle, role/task registries and Coordinator instructions/context. No cd into agent-org or separate activation prompt is required when the harness loads the root AGENTS.md. Delegated workers retain their assigned role and scope. This is instruction loading through the existing harness, not a new runtime. If a client does not load AGENTS.md, the explicit fallback is: “Read AGENTS.md at the Git repository root and initialize the organization.” Fresh workers receive explicit role AGENTS/CONTEXT and task/run/context manifest paths, not inherited conversation as authority.

At startup discover active roles, read authority/scope and open tasks/runs/claims. Reconcile native worker status, actual artifacts/hashes, Git index/worktree/remotes and known external operations before resuming or retrying. Resolve ownership uncertainty first. Check trigger occurrence dedup, enabled state, authority and cumulative resources; active-session startup and every five accepted substantive tasks may propose improvement review. CI PR/push checks run only through installed native Actions. No daemon/calendar or post-session organization execution is claimed.

During work remain interactive, use bounded waits, checkpoint every transition/before effects/15 active minutes, preserve actual failures and side effects. On cancellation stop new work, interrupt owned workers and reconcile results. On shutdown/compaction save handoff, claim status, evidence and exact safe next action. A session ending does not mean effects were undone or workers permanently continue. A fresh replacement re-admits work after reconciliation, not blind replay.
