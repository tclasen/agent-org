# Progressive disclosure verification

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: approved PLAN.md revision 1 instruction/navigation correction and root bridge
- Affected Paths or Resources: named organization surfaces; root AGENTS.md only
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000034
- Related Tasks: TASK-000066, TASK-000067, TASK-000068, TASK-000069, TASK-000070, TASK-000071
- Approval Requirements: APP-000018 for implementation; independent exact-candidate review and APP-000019 before promotion

Initial implementation followed then-valid provisional APP16 on draft PR12. Reconciled continuation requires renewed APP-000018; no instruction implementation bytes changed. Baseline is ca6ff20; unchanged prior policies/evaluator govern this candidate. This is deterministic document/route inspection, not a live adherence trial or productivity experiment. Required task/run, manifest and action-dependent reads remain additional to fixed startup counts.

## PD-01: fixed reading sets

[measurements.json](measurements.json) lists every counted file, unique once, UTF-8 Python str.split lexical words. Baseline common: 4 files / 1,190 words; baseline Coordinator: 9 / 3,012. Candidate common: 4 / 901; Coordinator: 7 / 1,732. All eight known-role closures (common plus assigned AGENTS/CONTEXT, without Coordinator lifecycle) fit six files / 1,600 words; maximum 1,411. These meet preregistered thresholds. Candidate Coordinator fixed words decrease 42.5%; actual model tokens, runtime, cost and task performance are unmeasured.

Counts can be reproduced by reading the file lists in measurements.json and summing len(Path(path).read_text().split()). Baseline sources are git show ca6ff20:<path>. Task sources and action details below must not be represented as zero cost.

## PD-02: mandatory reading graph

Root bridge → organization core → AUTHORITY + SCOPE_BOUNDARIES. For an unassigned session core additionally → Coordinator AGENTS + CONTEXT + SESSION_LIFECYCLE. For an assigned role core → only that role AGENTS + CONTEXT and required task/run/manifest sources. Coordinator also queries current status and relevant records. All eight role instruction/context pairs were inspected. References back to core explicitly reuse current loaded text; lifecycle says not to reread unchanged startup sources. No mandatory back edge or read-every-link instruction remains.

Known roles/tasks/policies bypass discovery catalogs; unknown role selection still checks actual directories/registry. This graph describes instruction obligations, not a claim of harness-level lazy loading.

## PD-03: fixed scenario traces

Each row adds its selected details to the relevant fixed core and exact assignment/criteria sources. These are semantic route inspections, not actual worker executions. All skipped sources remain available when the task changes.

| Preregistered case | Required route before dependent action | Irrelevant reads avoided |
| --- | --- | --- |
| Unassigned interactive session | Coordinator role/context/lifecycle; native status and Git; search nonterminal tasks/runs and open pending/overlapping records; check actual PR/effect state | All completed task/run bodies, every role and unrelated repositories |
| Known Developer with approved manifest | Assigned AGENTS/CONTEXT and task/run; accepted criteria/plan/approval; applicable project sources; CHANGE_CONTROL and verification details before edits/delivery | agents/tasks catalogs and second Coordinator initialization |
| Known Researcher report | Assigned source/criteria/task/run and plan/approval; source rules in role duties; DATA_HANDLING/PERMISSIONS when handling sensitive sources/effects; GIT/CHANGE_CONTROL/ACCEPTANCE at delivery | Enrollment, all software workflows and metrics definitions at research intake |
| Exact policy/status question | Open exact canonical policy through known path; role-appropriate current-state check; classification forbids mutation authority from a question alone | Admission/delegation records for a simple information response |
| Unknown capability | agents/INDEX plus actual role directories; ROUTING, MODEL_SELECTION, RESOURCE_BUDGETS, task/run/claim and context manifest before spawn | All unselected role bodies |
| Interrupted/uncertain remote effect | Relevant run/checkpoint and RECONCILIATION; actual artifacts/PR/refs before retry; retain unrelated work | Unrelated historical handoffs and blind effect replay |
| Organization/evaluator change | ORGANIZATION_CHANGES, SELF_IMPROVEMENT, MEASUREMENT_INDEPENDENCE via policy map; pinned prior criteria/plan/evidence; fresh review/approval | Unrelated project profiles; no skipped statistical gate when a stochastic claim applies |
| Product versus startup bridge | PROJECT_CHANGES/profile/canonical grant for product; CROSS_BOUNDARY_CHANGES and explicit APP8 child for root bridge | Organization authority treated as sufficient product authority; unrelated projects |
| Delivery/closure | CHANGE_CONTROL, GIT, ACCEPTANCE, APPROVALS; exact candidate, PR/check/thread state, owning-remote main verification | No local-only shortcut; historical installation acceptance cannot prove delivery |
| Metrics, IDs/records, triggers | Shared map → SCORECARDS/factory definitions for metrics; IDENTIFIERS/ID_LEDGER/RECORD_FORMATS/templates for new records; README → TRG-000001 for trigger mechanism/dedup/budget | Metrics for a simple report, every schema for status-only questions, invented telemetry or background workers |

## PD-04: preserved invariants

All 17 substantive policy bodies are byte-identical to baseline; [policy-hashes.json](policy-hashes.json) records hashes. Only policies/INDEX navigation changes. Existing tooling, evaluator, tests, authority grants, approved intake and historical evidence are unchanged.

| Invariant | Candidate evidence |
| --- | --- |
| Classification and separate grants/children | Core requires classification; AUTHORITY/SCOPE unchanged; TASK58 organization and TASK59 root child remain separately scoped |
| Native sandbox, old/ exclusion, no harness/service/product expansion | Core states exclusions; role confirms scope/ownership; no affected path outside named surfaces/root bridge |
| Per-run honest configuration and cumulative budgets | Core/roles retain unknown telemetry; model/budget policies linked before delegation; unchanged policies |
| Independent reviewer and Chief of Staff | Core and role duties retain independence, exact-candidate rules via action routes; APP16 plan approval precedes implementation |
| Candidate identity, PR and remote-main delivery | Core preserves standing routine delivery grant and intermediate-work distinction; unchanged CHANGE_CONTROL/GIT/ACCEPTANCE govern effects |
| No blind retry or background execution promise | Core/lifecycle require effect reconciliation, bounded active-session continuation and durable handoff |
| Statistical and evaluator rules | SELF_IMPROVEMENT/MEASUREMENT_INDEPENDENCE unchanged; deterministic requested correction only; no stochastic benefit claim |

## PD-05: discovery and links

[links.json](links.json) records 245 checked local links across the initial changed/new Markdown set, no missing destinations/invalid added anchors or path escape. Later review/approval links must also be checked before delivery. All old policy/shared index entries remain reachable through trigger-labeled maps. The core routes directly to common action sources; README exposes all current top-level domains: roles, tasks/runs, capabilities, requirements, intents/initiatives, policies/shared, workflows, knowledge, approvals/decisions/intake, experiments/evaluations/artifacts, factory baselines/reports and active triggers. Documents can be opened directly without reading the catalog.

Link check: extract Markdown local destinations in changed/new files, resolve relative to each containing file within repository, require existence; for fragments compare heading slugs. External URLs were researched separately; local link validation does not verify external availability or semantic truth. No new instruction loader, mandatory catalog, service or hierarchy introduced.

## PD-06: regression and retained failures

Interpreter: Python 3.15.0 on Darwin arm64. Exact baseline archive check: valid, 191 records, zero errors; existing unittest suite 85/85 passes. Reconciled candidate structural check: valid, 224 records, zero errors; 85/85 tests pass. Commands:

```sh
python3 agent-org/factory/instrumentation/check.py --root agent-org
python3 -m unittest discover -s agent-org/factory/tests -v
git diff --check
```

Raw results are baseline-validation.json, baseline-tests.log, candidate-validation.json and candidate-tests.log. An initial preapproval scaffold check failed on pending APP16 references and noncanonical Authorized text; retained separately as scaffold-validation.json, corrected in operational records before candidate validation. Initial whitespace check found extra trailing blank lines in seven CONTEXT files; removed, final diff check passes. Neither failure was hidden or fixed by changing the evaluator. Local read-only gh failed in restricted network, then succeeded via approved escalation; classic branch protection endpoint returned 404 because active rules are a ruleset. Current rules require PR, thread resolution, merge commits, no force push/deletion, and no bypass; no numeric reviewer count. Independent organization review/approval remains required.

## PD-07: review and delivery

Implementation/criteria are pinned in candidate-manifest.json before independent review. REVIEW.md and APP17 will bind candidate/evidence; no implementation author may self-approve. Review/approval outputs are excluded from self-hashing and must be reconciled against the final delivery commit. Any implementation change requires affected recheck/renewed approval.

At this point no completion is asserted: normal PR merge, host checks/thread handling and verified remote-main containment remain pending. Parent and child task statuses remain nonterminal. Coordinator owns delivery and the final observed PR/main identifiers. No deployment, messaging or project side effects occurred.

Reconciled candidate uses delivery base79298fe; all instructions/evaluator criteria remain based onca6ff20. Records remapped under PLAN revision2, preserving all new remote research. Refreshed counts/link/check/test evidence supersedes the initial snapshots; final review binds a new manifest.

Regeneration note: the first reconciled link scan found its own not-yet-written links.json/policy-hashes.json artifact references; both files were materialized before the diagnosed rerun. No instruction link was missing. The final regenerated scan result supersedes the initial-set count.

Final pre-review regenerated local-link inventory: 266 checked destinations, no errors; all updated references are within the reconciled repository.
