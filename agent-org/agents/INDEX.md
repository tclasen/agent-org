# Agent discovery and capability registry

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/agents/INDEX.md
- Affected Paths or Resources: agent-org/agents/INDEX.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

When selecting or reconciling a role, discover directories with AGENTS.md and pair each with CONTEXT.md. The table supplies discovery metadata; load only the selected role’s instructions/context, not every role. A worker already assigned a valid role does not repeat registry discovery unless identity/capability is uncertain. Reconcile the registry before admission: missing, duplicate, retired or mismatched identity blocks that assignment. Read declared capabilities, status and current role instructions; choose by task need, risk, budget, tools and permission. This registry is an index, not a fixed routing table or model map. Added roles become eligible only after governed lifecycle verification; retired IDs remain in history and active claims are reconciled.

| Identity | Role | Capability | Status |
| --- | --- | --- | --- |
| AGENT-000001 | [Coordinator](coordinator/AGENTS.md) | Own operator intent, task admission, routing, resource accounting and final reconciliation. | active |
| AGENT-000002 | [Chief of Staff](chief-of-staff/AGENTS.md) | Own organization governance, capability lifecycle and evidence-qualified recursive improvement under operator authority. | active |
| AGENT-000003 | [Planner](planner/AGENTS.md) | Convert admitted intent and authoritative requirements into a scoped executable plan with dependencies and observable acceptance. | active |
| AGENT-000004 | [Researcher](researcher/AGENTS.md) | Produce bounded source-grounded research, analysis and writing artifacts. | active |
| AGENT-000005 | [Architect](architect/AGENTS.md) | Design interfaces, adapters, system boundaries and technical decisions within an admitted task. | active |
| AGENT-000006 | [Developer](developer/AGENTS.md) | Implement and test only the approved task deliverable. | active |
| AGENT-000007 | [Executor](executor/AGENTS.md) | Carry out bounded operational, document, business or tool actions specified by the task and plan. | active |
| AGENT-000008 | [Reviewer](reviewer/AGENTS.md) | Independently verify a pinned candidate against accepted requirements, scope and prior approved evaluation rules. | active |
