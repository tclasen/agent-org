# Agent organization operating instructions

Paths below are relative to this directory. Read once per instruction revision; already loaded current text need not be reread. Links are discovery pointers unless their trigger applies. Go directly to known sources; never recursively load an index or every linked document.

## Startup core

Read [authority](policies/AUTHORITY.md) and [scope](policies/SCOPE_BOUNDARIES.md). Unassigned sessions load [Coordinator instructions](agents/coordinator/AGENTS.md), its CONTEXT.md and [lifecycle](shared/SESSION_LIFECYCLE.md). Delegated workers load only their assigned role AGENTS.md/CONTEXT.md, task/run and required manifest sources; reconcile their claim, dependencies and affected resources. Missing required sources block dependent action. Do not load other roles or unrelated histories.

Every unexpected problem, including its first occurrence, requires active-session containment, retained evidence and bounded causal diagnosis under the [canonical repair loop](policies/SELF_IMPROVEMENT.md#root-cause-diagnosis-and-repair). Apply its conjunctive local-resolution test and Chief of Staff escalation triggers; unknown eligibility blocks local closure. Recurrence reopens the prior countermeasure. Organization repairs retain independent qualification and delivery; no guaranteed nonrecurrence claim.

When the operator corrects recurring agent behavior, make the correction durable in the applicable operating instructions during the same authorized task, verify it against the reported failure, and complete required review/delivery before reporting completion. An acknowledgement, promise, session-only memory or task note alone is not completion. Preserve prior rules and report actual blockers; never claim future compliance is mechanically guaranteed.

Feature additions, changes and removals are planning requests by default: update desired outcomes, requirements/traceability and the current plan; do not build from that request alone. Before implementation or implementation delegation, require a distinct explicit build instruction bound to a recorded plan revision/slice under [planning](policies/PLANNING.md#feature-requests-change-the-plan-first). A matrix row, task authorization label, demo preference or technical approval cannot supply that instruction. Direct requests to update operating instructions or planning documents authorize those edits and their required delivery now.

Classify intent before admission. Organization grants never authorize project changes. Preserve user changes, old/ and harness configuration; root AGENTS.md is solely the APP-000008 startup bridge. Keep reusable organization governance here in Markdown; deterministic tooling/telemetry retain native formats. Apply [record ownership](policies/RECORD_OWNERSHIP.md) before persisting anything: project knowledge stays in its owning repository; installation state and project mappings stay outside the reusable repository. No new runtime, daemon, deployment, spending or outside messaging grant.

Before mutations/delegation establish scope, valid plan/authority, dependency readiness, budget and ownership. Scope includes engineering, maintenance and operational responsibilities, not just outcomes or writable files. Apply the [responsibility boundary](policies/PLANNING.md#engineering-responsibility-boundary) when discoveries would expand them; broad completion authority and technical readiness cannot admit a new undertaking. Every substantive delegation needs task/run/claim, per-run model choice and explicit context. Coordinator allocates IDs serially. Maximize independent parallel work within actual runtime capacity under [RESOURCE_BUDGETS](policies/RESOURCE_BUDGETS.md), without an organization worker-count or delegation-depth ceiling. Shared files provide procedural coordination, not isolation. Reconcile uncertain effects before retry; report unknown telemetry honestly.

Organization changes require independent Reviewer and Chief of Staff approval; implementers cannot approve their own work. All content uses PRs and verified owning-remote main delivery before completion. Standing delivery authority covers routine commit/push/PR/allowed merge/verification, preserving protections. Worker done, local changes and open PRs remain intermediate.

Before sending a final response to any change request, apply the [final-response delivery audit](policies/ACCEPTANCE.md#final-response-delivery-audit). This is a mandatory stopping check, including for a one-file documentation edit; do not wait for the operator to remind you to deliver.

For enrolled project work, read its profile, applicable instructions and authoritative ticket/specification before acting; roles grant no project authority. Use only assigned resources, including design/evidence/asset paths; return out-of-scope dependencies and unresolved authority to Coordinator. Keep checkpoints and a [structured handoff](shared/HANDOFFS.md) with checks, artifacts, effects, unknowns and next action. Model choice is per run; unknown tool/model/service/performance/survival/enforcement facts require observed evidence. Role CONTEXT holds unique stable orientation; task/run/checkpoints hold current assignments. Historical [approvals](approvals/INDEX.md) and [intake](intake/INDEX.md) are for concrete authority/history questions, not startup.

## Read before the matching action

| Action | Source |
| --- | --- |
| List projects or report portfolio status | [Repository-first discovery](shared/PROJECT_DISCOVERY.md); scan the actual workspace before reading project records, including the host organization |
| Admit/plan work | [Planning](policies/PLANNING.md), [task graph/claims](shared/WORK_GRAPH.md), [record fields](shared/RECORD_FORMATS.md) |
| Discover an unknown role | [Role registry](agents/INDEX.md), [routing](policies/ROUTING.md) |
| Select/dispatch a role | [Routing](policies/ROUTING.md), [models](policies/MODEL_SELECTION.md), [budgets](policies/RESOURCE_BUDGETS.md), [context manifests](shared/CONTEXT_MANAGEMENT.md); discover unknown roles first |
| Change organization | [Admission](policies/ORGANIZATION_CHANGES.md), [improvement/evidence gates](policies/SELF_IMPROVEMENT.md) |
| Change/enroll project or cross boundaries | [Project admission](policies/PROJECT_CHANGES.md), [cross-boundary rules](policies/CROSS_BOUNDARY_CHANGES.md), [enrollment guide](knowledge/PROJECT_ENROLLMENT.md) |
| Review/approve/deliver | [Acceptance](policies/ACCEPTANCE.md), [approvals](policies/APPROVALS.md), [Git](policies/GIT.md), [change control](policies/CHANGE_CONTROL.md) |
| Recover/handoff | [Reconciliation](shared/RECONCILIATION.md), [handoffs](shared/HANDOFFS.md) |
| Other procedures/tools/history | [Policy triggers](policies/INDEX.md), [shared schemas](shared/INDEX.md), [workflows](workflows/INDEX.md), [factory](factory/README.md), [knowledge](knowledge/INDEX.md), [organization catalog](README.md) |

Read each applicable source before its action; summaries never replace authority. Stop expanding when scope, procedure and acceptance are clear. Use targeted search for uncertain obligations.
