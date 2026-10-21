# Cumulative resources and retry limits

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/RESOURCE_BUDGETS.md
- Affected Paths or Resources: agent-org/policies/RESOURCE_BUDGETS.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Coordinator accounts per task and parent across child runs/retries; recursion never resets consumption. Defaults: maximum four native agents including interactive Coordinator (three workers); maximum two delegation edges below Coordinator; one active mutation claim per overlapping surface; one candidate improvement experiment at a time. Prefer verified task-owned worktrees for same-repository concurrent mutation; disjoint owned paths in a shared checkout require explicit Coordinator coordination and still provide no isolation.

Default checkpoint at least every 15 active minutes and every transition/external effect. Ordinary command timeout 120 seconds, tests 10 minutes; record a task-specific override before a known longer operation. At most two retries after diagnosis per failing operation, preserving each attempt and side-effect reconciliation. Improvement candidate default is 60 active minutes with disposition/checkpoint at limit. Checkpoint at 80% of observable allocation and stop/replan at exhaustion.

Soft storage thresholds are 100 MiB/run and 1 GiB active telemetry/fixtures; propose compact/archive at threshold, never silently delete evidence. Use existing subscription, no paid runners/providers or purchased quotas. Respect rate limits/Retry-After, cancel only owned superseded CI runs, avoid polling loops. No invented token counter or dollar cap; unknown usage remains a gap and does not justify unbounded work. Attribute organization and project resource totals separately or mark shared cost unknown.
