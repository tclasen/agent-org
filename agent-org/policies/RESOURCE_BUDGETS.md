# Cumulative resources and retry limits

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/RESOURCE_BUDGETS.md
- Affected Paths or Resources: agent-org/policies/RESOURCE_BUDGETS.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Coordinator accounts per task and parent across child runs/retries; recursion never resets consumption. Maximize independent parallel work within actual runtime capacity; do not impose an organization worker-count or delegation-depth ceiling or use cost to throttle already authorized work. Maintain one active mutation claim per overlapping surface and one candidate improvement experiment at a time. Prefer verified task-owned worktrees for same-repository concurrent mutation; disjoint owned paths in a shared checkout require explicit Coordinator coordination and still provide no isolation.

This actual-capacity rule supersedes older organization worker/depth defaults wherever repeated, including the three-worker wording in the organization core and DESIGN_REVIEW.md. It never supersedes hard host limits, current tool restrictions, independent review requirements or operator authority.

Distinguish a collaboration agent tree's advertised slots from app-level task scheduling. Default to supported separate native task threads under [thread delegation](../shared/THREAD_DELEGATION.md), using standing explicit operator requests where host tools permit. Each task retains its delegated role, task/run/context, exclusive scope and accountable Coordinator; it does not initialize a competing unassigned Coordinator. Keep native task identities in session or authorized external state, never reusable organization records. Observe running, queued, failed or unknown state: successful creation alone does not establish active capacity. Respect hard host limits, disclose unavailable native tools and use only authorized supported fallback; never evade limits through harness edits, background API workers or new providers/services.

Default checkpoint at least every 15 active minutes and every transition/external effect. Ordinary command timeout 120 seconds, tests 10 minutes; record a task-specific override before a known longer operation. At most two retries after diagnosis per failing operation, preserving each attempt and side-effect reconciliation. Improvement candidate default is 60 active minutes with disposition/checkpoint at limit. Checkpoint at 80% of observable allocation and stop/replan at exhaustion.

Soft storage thresholds are 100 MiB/run and 1 GiB active telemetry/fixtures; propose compact/archive at threshold, never silently delete evidence. Use existing subscription, no paid runners/providers or purchased quotas. Respect rate limits/Retry-After, cancel only owned superseded CI runs, avoid polling loops. No invented token counter or dollar cap; unknown usage remains a gap and does not justify unbounded work. Attribute organization and project resource totals separately or mark shared cost unknown.
