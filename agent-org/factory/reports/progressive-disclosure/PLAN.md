# Progressive disclosure plan — revision 3

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: named organization instruction surfaces and the separately granted root startup bridge; no managed-project product changes
- Affected Paths or Resources: listed below
- Owning Role: Coordinator; Planner authored revision 1; Coordinator normalized revision 2 identities only
- Related Requirements: REQ-000001, REQ-000008, REQ-000034
- Related Tasks: TASK-000066, TASK-000067, TASK-000068, TASK-000069, TASK-000070, TASK-000071
- Approval Requirements: APP-000001, APP-000008; APP-000018 before reconciled continuation; independent exact-candidate review and APP-000019 before promotion

## Status and intended result

This is the preregistered plan, not an implementation result or a grant. Baseline is `ca6ff20e551bf974c6f52cbdb2f7ebe15facf378`. Revision 1 preceded instruction implementation; revision 2 normalizes identities after concurrent publication (see impact below). Chief of Staff must approve this revision before TASK-000067 and TASK-000068 continuation. Preserve this revision and append a new revision with impact assessment if scope, thresholds, workload, evaluator, assumptions or authority changes; do not revise criteria after seeing a result to make a candidate pass.

The operator requests extensive online research and maximum useful progressive disclosure: retain a small unavoidable core, supply clear hints about available resources, and load detailed instructions when the task or intended action needs them. The practical claim is a deterministic correction to unnecessarily broad instruction loading and repetitive navigation. This plan does not claim higher productivity, lower total task cost, better model accuracy or a statistically measured efficiency improvement.

[RESEARCH.md](RESEARCH.md) owns source URLs, access evidence and synthesis. Its primary-source evidence supports small entrypoints, action-based retrieval, shallow references and discoverable labels. Applying human interface information scent research to agent navigation is a design inference. Published model ablations are contextual evidence, not proof for this organization. Existing SELF_IMPROVEMENT and MEASUREMENT_INDEPENDENCE rules govern this change unchanged; any later stochastic benefit claim needs their separate preregistered experiment.

## Scope, ownership and dependencies

All paths below are relative to the repository root in the isolated worktree `/private/tmp/agent-org-progressive-disclosure-reconciled`. The original `/Users/Shared` checkout and its pending cleanup/delivery work remain untouched by this task except Coordinator's separately recorded ID reservation.

| Task/run | Owner and exact surface | Gate |
| --- | --- | --- |
| TASK-000071 / RUN-000067 | Planner: this `agent-org/factory/reports/progressive-disclosure/PLAN.md` only | Return plan; no implementation or Git effects |
| TASK-000070 / RUN-000066 | Independent Chief of Staff: report `PLAN-APPROVAL.md`, `APPROVAL.md`; `agent-org/approvals/APP-000018.md` and `APP-000019.md` | Plan decision first; promotion decision only after candidate and review exist |
| TASK-000067 / RUN-000063 | Coordinator: `agent-org/AGENTS.md`; existing eight roles' `agents/*/AGENTS.md` and `CONTEXT.md`; `shared/CONTEXT_MANAGEMENT.md`, `shared/SESSION_LIFECYCLE.md`; `policies/INDEX.md`; `agent-org/README.md`; existing indexes only as needed for relevant route hints/current task records; scoped task evidence | APP-000018 and valid nonoverlapping claim before edits |
| TASK-000068 / RUN-000064 | Coordinator: root `AGENTS.md` startup bridge only, under APP-000008 | Separately scoped host integration child; same continuation approval (original implementation preceded this reconciliation) |
| TASK-000069 / RUN-000065 | Fresh independent Reviewer: report `REVIEW.md` only | Pinned candidate, approved plan/evaluator, completed implementation evidence |
| TASK-000066 / RUN-000062 | Coordinator: parent reconciliation, research/evidence, registered task/run/index records, normal scoped PR delivery | Required children pass; final verified owning-remote main containment/content |

The eight current role directories are coordinator, chief-of-staff, planner, researcher, architect, developer, executor and reviewer. No new role or capability is introduced. Index edits mean relevant navigation or current records, not wholesale rewriting of historical registries. Any required additional substantive surface returns to Coordinator for explicit scope/approval impact review.

Do not edit `old/`, legacy evidence/history, another project's checkout, harness settings, CI implementation, tooling/evaluator code or substantive policy bodies. In particular AUTHORITY, SCOPE_BOUNDARIES, SELF_IMPROVEMENT, MEASUREMENT_INDEPENDENCE, ACCEPTANCE and GIT retain their authoritative semantics and files. No deployments, purchases, new providers or external messages are authorized. PR/remote effects follow existing grants and policies.

## Proposed instruction architecture

1. Root `AGENTS.md` remains a short startup bridge. It activates the canonical organization core by direct path, preserves path resolution and missing-core failure handling, and distinguishes unassigned Coordinator startup from an already delegated role. It grants no project authority.
2. `agent-org/AGENTS.md` keeps universal safety/authority invariants and direct action triggers. AUTHORITY and SCOPE_BOUNDARIES remain mandatory for every substantive worker. Known-role workers go directly to their role AGENTS/CONTEXT and exact task/run/approved manifest. An index is a discovery aid when a target is unknown, not a compulsory stop when the exact path is supplied.
3. Coordinator startup loads its own role/context and SESSION_LIFECYCLE. Reconcile current/open/undelivered work, native workers/claims, Git state and known external effects for involved resources before action. Locate exact records by supplied IDs or a scoped search; read a registry when necessary to discover unknown state. Follow links into relevant interrupted or unfinished records. Do not open every historical task/run/approval or unrelated repository merely because a registry exists.
4. Role AGENTS describe role-specific duties; CONTEXT gives stable orientation and useful routes. Remove unconditional read-back loops to organization/core/lifecycle/role files already loaded. A link back can identify authority or serve navigation without commanding another read. Do not copy generic policy prose into every role. Retain each role's independent duties and readiness/scope checks.
5. `shared/CONTEXT_MANAGEMENT.md` provides an explicit context-loading protocol and a compact trigger-to-resource map. Load requirements, plan/approval, evidence, relevant policies and project sources when the assigned action depends on them, before that action. Hints are optional navigation; a matching action trigger is a required precondition. Unknown relevance is resolved before consequential action, rather than interpreted as permission to skip a guardrail.
6. Policy/shared/workflow indexes and README provide clearly labeled discovery routes, with direct links to canonical details. References stay shallow: core links to a relevant detail directly, or to one route map whose rows link directly to canonical details. Detail documents can cite related material; they must not impose a recursive read-everything chain. Keep links to historical lessons, but make their loading conditional on a relevant precedent, evaluation, recovery question or evidence gap.

The route map must cover all current policy/shared domains, not only software implementation. At minimum its labels and direct destinations must cover:

| Trigger/domain | Canonical detail reachable from hints |
| --- | --- |
| Authority, classification and boundaries | AUTHORITY, SCOPE_BOUNDARIES; organization/project/cross-boundary change policies |
| Admit, plan or change requirements/scope | PLANNING; requirements/task sources; WORK_GRAPH and applicable workflows |
| Choose/discover/delegate a capability | agents registry; ROUTING, MODEL_SELECTION, RESOURCE_BUDGETS; explicit worker context |
| Start, resume, interrupt, checkpoint or hand off | SESSION_LIFECYCLE, RECONCILIATION, HANDOFFS and templates; active task/run/claim sources |
| Allocate IDs or write formal records | IDENTIFIERS, CONVENTIONS, RECORD_FORMATS, record templates |
| Permission, sensitive data or external effects | PERMISSIONS, DATA_HANDLING, applicable approval record |
| Review, accept, approve or reconcile intent | ACCEPTANCE, APPROVALS, INTENT_RECONCILIATION, INTEGRATION |
| Change files, commit, push, PR, merge or verify delivery | CHANGE_CONTROL, GIT; owning remote/main and scoped resource provenance |
| Improve the organization or change an evaluator | SELF_IMPROVEMENT, MEASUREMENT_INDEPENDENCE; pinned prior criteria and evidence |
| Measure, report, instrument or evaluate | SCORECARDS, factory README, relevant definitions and evidence; telemetry limitations |
| Project enrollment, product work or integration | projects registry/profile, applicable project guide/workflow and canonical project authority/specification; separate grant |
| Research, architecture, writing or operations | appropriate capability/workflow and canonical task sources; source/evidence and effect policies |
| Native triggers and historical precedent | triggers registry/workflow; LEGACY_LEARNINGS when pertinent; no autonomous Markdown/runtime claim |

Every policy and shared convention currently listed in their indexes must have a route (some may share a row). All current top-level organization domains must remain discoverable through direct canonical links or an index. A route is not a new grant, workflow replacement or required catalog read.

## Preregistered workload and acceptance

Reviewer evaluates under the unchanged baseline policy rules. Criteria are conjunctive. A failure blocks promotion; missing evidence is unverified/inconclusive. Baseline and candidate snapshots, commands, expected/observed outputs and hashes go into task evidence before independent review. Count fixed instruction words using Python `str.split()` over UTF-8 source; this is a lexical size measure, not model tokens. Count each unique mandatory file once. Preserve the explicit file sets and conditional traversal decisions so another execution can reproduce them.

Measured baseline at `ca6ff20`: root bridge + organization core + AUTHORITY + SCOPE_BOUNDARIES are four files / 1,190 words. Baseline Coordinator fixed startup adds SESSION_LIFECYCLE, agents and tasks indexes, Coordinator AGENTS and CONTEXT: nine files / 3,012 words. These baseline sets follow the baseline explicit startup instructions; record any additional transitive action-required reads separately rather than silently changing the denominator.

| ID / mapping | Observable expected result | Verifier and evidence |
| --- | --- | --- |
| PD-01 / operator intent | Common mandatory core is at most four files / 1,000 words; known-role fixed closure at most six files / 1,600 words; Coordinator fixed startup at most seven files / 1,800 words. Common files remain root bridge, organization core, AUTHORITY, SCOPE_BOUNDARIES; known role adds AGENTS/CONTEXT; Coordinator adds lifecycle. Exact task/run/source and action-dependent docs are listed separately in each scenario, never concealed as zero cost. | Coordinator records baseline/candidate file sets, lexical counts and fixed/conditional distinction; Reviewer reproduces. |
| PD-02 / operator intent | No unconditional instruction-loading cycle between root, core, lifecycle or role AGENTS/CONTEXT. Known task/role/policy paths do not require reading their catalog first. There is no instruction to recursively load all referenced documents. | Annotated mandatory-read graph and all eight role inspection; Reviewer checks text semantics, not merely link existence. |
| PD-03 / operator intent, REQ-000034 | Scenario matrix below routes to relevant canonical details before consequential action; Coordinator reconciliation preserves open/undelivered state while unrelated history is conditional. Historical lessons remain discoverable without universal startup loading. | Baseline/candidate route traces: trigger, mandatory core, selected details, skipped irrelevant history and reason; fresh Reviewer checks every row. |
| PD-04 / REQ-000001, REQ-000008, REQ-000034 | Classification, separate grants/children, sandbox/scope, old exclusion, requested/actual metadata honesty, cumulative budgets, independent review/approval, exact candidate identity, PR and verified remote-main completion remain intact. No changed promotion/evaluation semantics and no live/background-runtime claim. | Baseline-to-candidate invariant matrix and text diff; Reviewer checks authoritative policy consistency, Chief of Staff decides. |
| PD-05 / operator intent | All route-map domains above and all existing policy/shared index entries have discoverable canonical destinations. New/changed local Markdown links resolve within authorized repository paths; fragments, when added, match targets. No direct known-target path is replaced by a required catalog. | Link inventory/resolution output plus manual route coverage table; document any untouched preexisting broken link separately. Reviewer verifies changed routes. |
| PD-06 / regression | `python3 agent-org/factory/instrumentation/check.py --root agent-org`, `python3 -m unittest discover -s agent-org/factory/tests -v` and `git diff --check` pass on the candidate. Preserve any baseline failures and diagnose rather than modifying tooling or criteria here. | Coordinator records interpreter/environment, exact command, exit/output, tested identity; Reviewer reproduces or explicitly verifies pinned evidence. |
| PD-07 / delivery | Changes remain within named child scopes; independent plan approval precedes implementation; fresh Reviewer and Chief of Staff approve the exact final content; normal PR merges and approved content is verified on owning remote main. | Review/approval hashes, scoped diff, PR URL/status/checks, tested head, merge/main identities, UTC observation and ancestry or content-equivalence evidence. Coordinator reconciles parent last. |

Fixed-route scenarios, specified before candidate implementation:

| Case | Required decision/routing observation |
| --- | --- |
| Unassigned fresh interactive session | Coordinator initializes; reconciles open/unfinished work, claims, Git and effects; discovers unknown records through scoped search/index as needed; does not scan unrelated completed history. |
| Known delegated Developer with exact task/run and approved manifest | Direct role/task route; no forced agents/tasks registry or Coordinator initialization; relevant change/verification policy loads before its action. |
| Known delegated Researcher writing a bounded report | Direct source/criteria/scope route; data/source handling applies; Git policies trigger when delivery begins, without requiring every software/metrics policy for research intake. |
| Exact policy question/status-only request | Direct known detail; no mutation/admission/delegation authority inferred; startup reconciliation obligations remain role-appropriate. |
| Unknown capability selection | Discover and validate actual active role directories/registry before assignment; model/budget/claim and durable task/run gates apply. |
| Interrupted run or uncertain remote effect | Load relevant run/checkpoint and reconciliation detail; inspect actual artifact/ref/PR state before retry; preserve unrelated work. |
| Organization change and evaluator proposal | Load prior SELF_IMPROVEMENT/MEASUREMENT_INDEPENDENCE rules and pinned plan/evidence; implementer cannot self-review/approve; criteria cannot change to pass. |
| Product change versus bridge integration | Project sources/grant/profile needed for product; root bridge requires APP-000008 child; organization grant does not authorize either by implication. |
| Git delivery or proposed task closure | Load CHANGE_CONTROL/GIT/ACCEPTANCE before effect/closure; pushed branch/open PR/local pass remains pending until verified remote main. |
| Metrics, ID/record writing and trigger operation | Each reaches its own named canonical detail, definitions/schema or trigger mechanism before action; unknown telemetry and unsupported background execution remain explicit. |

These are deterministic instruction/route inspections and regression checks. They do not establish actual worker adherence, recovery success under arbitrary conditions, universal tool interception or stochastic productivity. No synthetic route trace may be described as a live behavioral trial.

## Execution and stopping sequence

1. Coordinator confirms baseline, claim, scoped Git state and research artifact; independent Chief of Staff records APP-000018 against this plan and the unchanged evaluation rules. Record revision 2 plan hash before continuation; revision 1 and provisional APP16 preceded original implementation.
2. Coordinator implements TASK-000067 and separately TASK-000068 in the isolated worktree, using only named surfaces. Preserve original historical evidence and grants. Inspect the whole mandatory-read graph, not only individual file lengths.
3. Capture baseline/candidate counts, route matrix, governance diff, changed-link resolution and regression results. Diagnose any failure; at most two retries after diagnosis per operation. Do not modify tests/evaluator to achieve passage.
4. Freeze implementation content and evidence identities. Spawn the independent Reviewer with explicit role/task/run, approved plan and pinned evidence, then obtain independent Chief of Staff promotion decision. Requested model/reasoning defaults to `gpt-6.1-sol/high` for bounded implementation/review; independent Chief of Staff RUN-000066 uses `gpt-6-astra/high` for consequential governance review per MODEL_SELECTION; actual model/reasoning remain unknown without native evidence. Independence comes from separate executions without implementation authorship, not model variety.
5. Coordinator carries out authorized scoped commit/push/PR/check/thread/merge work under current policy and exact-candidate decisions. Any subsequent implementation/content change invalidates affected review/approval and requires proportionate recheck. Reviewer/approval reports added to the delivery commit must be bound to the implementation snapshot and separately reconciled so they cannot silently alter approved content.
6. Verify owning canonical remote main contains the approved content; record PR, merge, observed main tip/time and content/ancestry evidence. Parent and children remain nonterminal until their required delivery is verified. No session-end or local-only completion claim.

Budget is 90 active minutes cumulatively for parent and children, including research, planning, implementation, retries, review and delivery, as registered. At most Coordinator plus three workers; no more than two delegation edges. Stop/checkpoint at 80% (72 minutes), at transitions/before external effects and every 15 active minutes. Ordinary command limit 120 seconds and tests 10 minutes; bounded waits preserve interaction. No paid resources; unknown token/cost metadata stays unknown. If the cumulative limit, authority, independence, regression or remote-delivery gate cannot be satisfied, preserve results and request/record a replan; do not lower acceptance criteria or claim completion.

## Rollback, risks and handoff

Known-good rollback content is baseline `ca6ff20`. Before merge, reject or revise the candidate without adopting it. After a demonstrated regression, stop new use, reconcile affected active runs, and deliver a normal independently reviewed corrective/revert PR restoring task-owned instruction content to baseline as needed. Do not reset history, force push, overwrite unrelated changes, undo unrelated later remote-main content or roll back preserved evidence. Include root bridge and organization child together when their routing depends on each other.

Primary risks are omitted policy discovery, overlong conditional routes, stale links, a guardrail demoted to an optional hint, and mistaking retrieval-size reduction for better task performance. Route coverage, read-graph review and the invariant matrix address covered cases. The fixed lexical bounds are engineering acceptance thresholds rather than scientifically optimal context sizes. Future growth, tools bypassing these instructions, native loading behavior and actual resource usage remain limitations.

Revision 1 Planner handoff: only this file was authored under TASK-000071/RUN-000067; no implementation, external messaging, commit/push/PR or acceptance effect. Coordinator owns continuation. Exact next safe action is independent Chief of Staff plan review under TASK-000070/RUN-000066 and APP-000018, before continuing TASK-000067 and TASK-000068. Artifact hash and actual file-check result are returned in the native handoff; delivery remains pending.

## Revision 2 — concurrent identity reconciliation

Revision 1 original hash aa5f1369237f85c4272e8cfed08034014599add8cc12748d9ca9451824950459 is preserved on draft PR12 at05ebfd8. Remote main advanced to79298fe via unrelated research PR9/10 and allocated overlapping provisional records. No original review/promotion decision was issued. Retain baseline ca6ff20, all criteria/thresholds/workload/budget/rollback and unchanged substantive policies/evaluator. New delivery base79298fe preserves all research. Only provisional task/run/approval references and worktree identity change; new Chief plan decision required before continuation. Earlier implementation was produced after the then-valid provisional APP16; its content is unchanged. New APP18 independently authorizes continued evaluation/delivery, and APP19 will govern promotion. This is not a reset of budget or an outcome-driven criterion change.

Identity mapping: original provisional TASK57..62 → TASK66..71; RUN52..57 → RUN62..67; APP16/17 → APP18/19. Other owners' already published/reserved records remain intact. Coordinator records source-ledger reservation before transfer.

## Revision 3 — integrate concurrently delivered cleanup

Remote main e08e2ff merged cleanup PR11 after revision2 approval. Normal branch merge preserves all its project-cleanup records, exclusions and policy clarification. No criteria, workload, numeric bounds, budget or evaluator code changed. GIT.md's upstream standing-delivery paragraph is retained verbatim; compare our policy delta against e08e2ff. Relative to original ca6ff20, sixteen substantive policies remain byte-identical and GIT differs only by that independently authorized upstream clarification. Candidate core already expressed the same standing routine commit/push/PR/allowed merge/main-verification directive; resolving the AGENTS conflict keeps its existing bounded text and that rule. Registry/ledger conflicts union both owners' entries; no identities reused or historical content overwritten. New continuation approval for this revision is required before refreshed evaluation. Original baseline counts stay fixed; latest delivery base becomes e08e2ff.
