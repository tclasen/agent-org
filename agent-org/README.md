# Agent organization

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/
- Affected Paths or Resources: agent-org/
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

This is a Markdown-first general-purpose organization using native Codex workers and small deterministic factory tools. Coordinator owns intent/routing/reconciliation; Chief of Staff independently governs evidence-qualified autonomous organization evolution. Each project keeps its own repository, remote and authoritative specification/ticket sources. Software delivery is one instrumented workflow alongside research, writing, analysis and operations.

Start Codex from the Git repository root; the [root AGENTS.md](../AGENTS.md) activates this organization and initializes the Coordinator. You do not need to cd into agent-org or supply an activation prompt. Canonical instructions/state remain here. Clients that do not load AGENTS.md can explicitly read the root file; no universal harness behavior or background execution is claimed.

Read [authority](policies/AUTHORITY.md), [scope](policies/SCOPE_BOUNDARIES.md), [role discovery](agents/INDEX.md), [tasks](tasks/INDEX.md), [shared lifecycle](shared/SESSION_LIFECYCLE.md) and [workflows](workflows/INDEX.md). Formal records carry scope/authority metadata and serialized stable IDs. Fresh task-selected workers return durable handoffs; independent reviewers verify pinned candidates; every factory content change goes through PR. Organization maintenance approval is autonomous when evidence qualifies; project grants remain separate.

APP-000001 records implementation authority for [approved v0.1](intake/approved-v0.1/INDEX.md). Preserved intake snapshots contain historical pending wording; authority does not prove implementation or final acceptance. Consult current tasks/runs/evaluations/reports for actual results. APP-000008 records the operator’s final acceptance and explicit root-entrypoint amendment.

[Factory tooling](factory/README.md) instruments only explicit paths. No permanent runtime, daemon, paid service, live production enrollment, old/ migration, universal tool interception, exact unavailable telemetry or hostile-worker isolation is claimed. Autonomy operates while native sessions are active; durable files enable reconciliation after interruption.
