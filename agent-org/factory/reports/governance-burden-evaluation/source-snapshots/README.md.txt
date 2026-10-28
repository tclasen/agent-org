# Agent organization

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/
- Affected Paths or Resources: agent-org/
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

This Markdown-first organization uses native Codex workers and bounded deterministic tools. Coordinator owns intent/routing/reconciliation; independent Chief of Staff governs organization changes. Projects retain their own repositories, remotes and authoritative specifications.

Start in the repository root: [root AGENTS.md](../AGENTS.md) activates [canonical startup and action routes](AGENTS.md). No directory change or activation prompt is required. Clients that do not load AGENTS.md can explicitly read it. Read the bounded startup core, then only sources triggered by the task; this README adds no mandatory reading list.

| Looking for | Start here when needed |
| --- | --- |
| Roles/capability selection | [Agents](agents/INDEX.md), [capability evidence](capabilities/INDEX.md) |
| Current assignment/history | [Tasks](tasks/INDEX.md), [runs](runs/INDEX.md); search active/relevant entries before opening records |
| Rules and schemas | [Policy triggers](policies/INDEX.md), [shared references](shared/INDEX.md) |
| Admission, execution, review, recovery or enrollment | [Workflow catalog](workflows/INDEX.md) |
| Project enrollment/profile | [Enrollment guide](knowledge/PROJECT_ENROLLMENT.md), [project-local templates and storage boundary](knowledge/projects/INDEX.md) |
| Validation, metrics or instrumentation | [Factory commands and components](factory/README.md) |
| Historical installation/authority or decisions | [Approvals](approvals/INDEX.md), [decisions](decisions/INDEX.md), [preserved intake](intake/INDEX.md) |
| Intent, priorities or authoritative requirements | [Intents](intents/INDEX.md), [initiatives](initiatives/INDEX.md), [requirements](requirements/INDEX.md) |
| Evaluations, experiments or retained evidence | [Evaluations](evaluations/INDEX.md), [experiments](experiments/INDEX.md), [artifacts](artifacts/INDEX.md), [baselines](factory/baselines/INDEX.md), [reports](factory/reports/INDEX.md) |
| Invoke/check active-session triggers | [Trigger mechanism, dedup and limits](triggers/TRG-000001.md) |
| Research behind this disclosure design | [Sources, rationale and limitations](factory/reports/progressive-disclosure/RESEARCH.md) |

APP-000001 authorizes installation and qualified evolution; APP-000008 accepts installation and the narrow root bridge. Historical pending wording does not override current grants. Current evidence, not documentation alone, proves behavior. All content follows independent review/approval, PR and verified owning-remote main completion. No permanent runtime, new service, legacy migration, universal interception, unavailable telemetry or post-session execution is claimed.
