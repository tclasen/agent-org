# Agent organization operating instructions

Paths below are relative to this directory. Read once per instruction revision; already loaded current text need not be reread. Links are discovery pointers unless their trigger applies. Go directly to known sources; never recursively load an index or every linked document.

## Startup core

Read [authority](policies/AUTHORITY.md) and [scope](policies/SCOPE_BOUNDARIES.md). Unassigned sessions load [Coordinator instructions](agents/coordinator/AGENTS.md), its CONTEXT.md and [lifecycle](shared/SESSION_LIFECYCLE.md). Delegated workers load only their assigned role AGENTS.md/CONTEXT.md, task/run and required manifest sources; reconcile their claim, dependencies and affected resources. Missing required sources block dependent action.

Classify intent before admission. Organization grants never authorize project changes. Preserve user changes, old/ and harness configuration; root AGENTS.md is solely the APP-000008 startup bridge. Keep organization state here in Markdown; deterministic tooling/telemetry retain native formats. No new runtime, daemon, deployment, spending or outside messaging grant.

Before mutations/delegation establish scope, valid plan/authority, dependency readiness and ownership. Every substantive delegation needs task/run/claim, per-run model choice and explicit context. Coordinator allocates IDs serially; at most three workers plus Coordinator. Shared files provide procedural coordination, not isolation. Reconcile uncertain effects before retry; report unknown telemetry honestly.

Organization changes require independent Reviewer and Chief of Staff approval; implementers cannot approve their own work. All content uses PRs and verified owning-remote main delivery before completion. Standing delivery authority covers routine commit/push/PR/allowed merge/verification, preserving protections. Worker done, local changes and open PRs remain intermediate.

Before sending a final response to any change request, apply the [final-response delivery audit](policies/ACCEPTANCE.md#final-response-delivery-audit). This is a mandatory stopping check, including for a one-file documentation edit; do not wait for the operator to remind you to deliver.

## Read before the matching action

| Action | Source |
| --- | --- |
| Admit/plan work | [Planning](policies/PLANNING.md), [task graph/claims](shared/WORK_GRAPH.md), [record fields](shared/RECORD_FORMATS.md) |
| Discover roles/delegate | [Role registry](agents/INDEX.md), [routing](policies/ROUTING.md), [models](policies/MODEL_SELECTION.md), [budgets](policies/RESOURCE_BUDGETS.md), [context manifests](shared/CONTEXT_MANAGEMENT.md) |
| Change organization | [Admission](policies/ORGANIZATION_CHANGES.md), [improvement/evidence gates](policies/SELF_IMPROVEMENT.md) |
| Change/enroll project or cross boundaries | [Project admission](policies/PROJECT_CHANGES.md), [cross-boundary rules](policies/CROSS_BOUNDARY_CHANGES.md), [enrollment guide](knowledge/PROJECT_ENROLLMENT.md) |
| Review/approve/deliver | [Acceptance](policies/ACCEPTANCE.md), [approvals](policies/APPROVALS.md), [Git](policies/GIT.md), [change control](policies/CHANGE_CONTROL.md) |
| Recover/handoff | [Reconciliation](shared/RECONCILIATION.md), [handoffs](shared/HANDOFFS.md) |
| Other procedures/tools/history | [Policy triggers](policies/INDEX.md), [shared schemas](shared/INDEX.md), [workflows](workflows/INDEX.md), [factory](factory/README.md), [knowledge](knowledge/INDEX.md), [organization catalog](README.md) |

Read each applicable source before its action; summaries never replace authority. Stop expanding when scope, procedure and acceptance are clear. Use targeted search for uncertain obligations.

Record storage follows [record ownership](policies/RECORD_OWNERSHIP.md): organization governance stays here; project-specific records stay in their owning repositories. Organization entries retain only minimal routing links.
