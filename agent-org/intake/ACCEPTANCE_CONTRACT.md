# Installation Acceptance Contract v0.1 — operator accepted; root startup amendment

Implementation approval recorded in [APP-000001](../approvals/APP-000001.md). Exact approved v0.1 is preserved under approved-v0.1/. APP-000008 records final operator acceptance and the root startup amendment.
- Target System: organization
- Change Classification: organization
- Authorized Scope: Current approved installation contract and evidence view under agent-org/intake; APP-000001 defines operational scope.
- Affected Paths or Resources: agent-org/ plus explicitly approved root .gitignore and .github/workflows/agent-org.yml integration; isolated fixtures and Git/PR flow.
- Owning Role: Coordinator.
- Related Requirements: REQ-000001 through REQ-000040 in REQUIREMENTS_BASELINE.md (proposed baseline v0.1).
- Related Tasks: TASK-000001 and separately scoped linked children.
- Approval Requirements: Recommendations delegated by SRC-005; implementation and final installation acceptance remain explicit operator gates.

Installation state: FULLY_ACCEPTED for the delivered installation under APP-000008. Historical scenario cells below are superseded by INSTALLATION_RESULTS.md; root entrypoint amendment is independently verified under TASK-000025.

## Operator decisions

Multi-repository factory in /Users/Shared; organization in agent-org; all Shared readable; preserve old uncommitted and migrate later. Project overrides allowed under central governance. Initialization recommendations delegated. Organization recursively improves and independently self-approves autonomously when evidence supports benefit; PRs required. Operator removed linear-history requirement, verified via GitHub. Initial plan approval and final acceptance remain operator decisions.

## Capability contract

| Capability ID | Requested capability | Classification | Requirements | Mechanism / test references | Actual result |
| --- | --- | --- | --- | --- | --- |
| CAP-000001 | Classification and reconciliation | organization | REQ-000001, REQ-000006, REQ-000011 | O-01, X-03 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000002 | Multi-repository boundaries / profiles | cross_boundary | REQ-000003, REQ-000004, REQ-000007 | P-01, X-01–X-10 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000003 | General-purpose Coordinator | organization | REQ-000005, REQ-000006, REQ-000011 | O-01, O-13 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000004 | Autonomous authority / approval | organization | REQ-000008, REQ-000009, REQ-000010, REQ-000030 | S-01–S-10 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000005 | Planning separation | organization | REQ-000012 | O-06, P-03 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000006 | Dynamic roles / fresh delegation | organization | REQ-000013, REQ-000014 | O-02–O-05 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000007 | Per-run models / reasoning | organization | REQ-000015 | O-05 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000008 | Durable recovery | organization | REQ-000016 | O-09–O-11 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000009 | Tasks / work graphs / claims | organization | REQ-000017, REQ-000018 | O-06–O-10 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000010 | Requirement traceability | organization | REQ-000019 | O-07, P-02 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000011 | Git / PR delivery | cross_boundary | REQ-000020, REQ-000021 | P-07, G-01–G-04 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000012 | Deterministic quality gates | organization | REQ-000022, REQ-000023 | I-07, O-12, P-05 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000013 | Factory CI integration | cross_boundary | REQ-000024 | G-03–G-04 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000014 | DORA calculator | organization | REQ-000025, REQ-000026 | D-01–D-13 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000015 | Event and command instrumentation | organization | REQ-000027, REQ-000028 | I-01–I-08 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000016 | Data handling / scope protection | cross_boundary | REQ-000029, REQ-000030 | X-01–X-10, I-06 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000017 | Separate scorecards / reporting | organization | REQ-000031, REQ-000032, REQ-000038 | I-08, O-14 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000018 | Budgets / retry limits | organization | REQ-000033 | O-10, S-09 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000019 | Native session / CI triggers | organization | REQ-000034 | O-15 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000020 | Recursive self-improvement | organization | REQ-000008, REQ-000035, REQ-000036 | S-01–S-10 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000021 | History / baseline integrity | organization | REQ-000037 | I-03, S-07 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |
| CAP-000022 | Installation acceptance | organization | REQ-000039, REQ-000040 | A-01–A-02 below; native agents/Markdown/Python/Git as detailed in plan | NOT RUN |

## Installation test matrix

Every test must record tested revision/environment, expected result, actual result, evidence path/hash, verifier, outcome and limitations. Synthetic fixtures, live-agent behavior and external integration results remain distinguishable. Expected failures in negative fixtures count as pass only when the expected refusal/detection actually occurs. Deterministic structure tests cannot substitute for behavioral agent trials.

### O scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| O-01 | Coordinator startup | Fresh worker starts from /Users/Shared, explicitly loads nested organization instructions, identifies scope and next action. | NOT RUN |
| O-02 | Chief of Staff discovery | Registry and filesystem discovery route an organization change to the governance owner. | NOT RUN |
| O-03 | Dynamic discovery / instruction loading | Synthetic added/retired role changes discovery; selected worker reads correct AGENTS/CONTEXT revision. | NOT RUN |
| O-04 | Fresh and parallel delegation | Actual two independent workers, persisted tasks/runs, native IDs, nonconflicting scopes and structured handoffs. | NOT RUN |
| O-05 | Model / reasoning selection | At least two explicitly selected supported configurations invoked; requested/observable actual metadata separated; failure/fallback case retained. | NOT RUN |
| O-06 | Task / plan / approval lifecycle | Durable task, valid state transitions, approval before implementation, no plan-as-permission. | NOT RUN |
| O-07 | Requirements persistence | Stable IDs, revisions, classification, authority references and criterion-to-evidence links survive reload. | NOT RUN |
| O-08 | Work graph / claims | Reject cycles, unsatisfied prerequisites, duplicate IDs, conflicting claims, premature parent acceptance. | NOT RUN |
| O-09 | Handoff / recovery | Fresh replacement uses persisted records without inherited conversation; verifies artifacts and safe next action. | NOT RUN |
| O-10 | Cancellation / retries / budgets | Interrupt or controlled interrupted-run fixture; reconcile side effects, preserve attempt history, enforce cumulative limits. | NOT RUN |
| O-11 | Stale claim reconciliation | Unknown run status never causes duplicate mutation; check native status or record unresolved ownership. | NOT RUN |
| O-12 | Organization instruction change | Actual harmless scoped correction under Chief of Staff plan/approval, independent review and regression verification. | NOT RUN |
| O-13 | Non-software work | Fresh Researcher and/or Executor produces a bounded source-grounded research/writing artifact with requirements and acceptance. | NOT RUN |
| O-14 | Reports / intent repair | Distinct scorecards and explicit unknowns; intentionally mismatched deliverable reopens task. | NOT RUN |
| O-15 | Triggers | Session/manual/CI mechanism named; disabled/duplicate trigger rejected; no fictitious calendar execution. | NOT RUN |

### P scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| P-01 | Project classification / enrollment | Two independent temporary repositories retain identities, paths, remotes-as-fixture metadata and separate authority. | NOT RUN |
| P-02 | Project requirements | Register synthetic project requirement by reference; no organization-policy mutation. | NOT RUN |
| P-03 | Project planning / approval | Plan and scope approved before specialist edits; negative missing-approval scenario. | NOT RUN |
| P-04 | Specialist implementation | Actual synthetic source/test file changes only within authorized project fixture. | NOT RUN |
| P-05 | Project tests | Run actual project fixture checks; capture exit code/output hashes; retain failing counterexample. | NOT RUN |
| P-06 | Project review | Fresh reviewer verifies product behavior and boundary compliance against pinned candidate. | NOT RUN |
| P-07 | Integration | Integrate tested fixture change in its local Git history; real factory installation content delivered through PR when possible. | NOT RUN |
| P-08 | Intent / acceptance | Reconcile requested project result, evidence and acceptance; worker done alone does not close task. | NOT RUN |

### X scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| X-01 | Project cannot modify organization | Authorized project work leaves organization instructions unchanged; deliberate violation detected/rejected. | NOT RUN |
| X-02 | Organization cannot modify project | Organization work leaves application fixture unchanged; deliberate violation detected/rejected. | NOT RUN |
| X-03 | Ambiguous testing request | Live ambiguous request prompts clarification and no broader edit. | NOT RUN |
| X-04 | Cross-boundary decomposition | Parent has separately scoped organization, project and necessary integration children. | NOT RUN |
| X-05 | Cross-boundary approvals | Missing organization or project approval blocks respective mutation and parent acceptance. | NOT RUN |
| X-06 | Organization independent verification | Organization behavior criteria checked independently of product tests. | NOT RUN |
| X-07 | Project independent verification | Product requirement/test criteria checked independently of organization evaluations. | NOT RUN |
| X-08 | Integration verification | Real fixture event crosses approved adapter and produces correct linked record/metric. | NOT RUN |
| X-09 | Preserve both requirement sets | Candidate cannot satisfy one system by weakening the other's accepted obligations. | NOT RUN |
| X-10 | Out-of-scope dependency | Worker records dependency and notifies Coordinator; no unauthorized edit; unrelated in-scope work may continue. | NOT RUN |

### I scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| I-01 | Event schema / invalid input | Validate applicable fields/types/IDs/time/classification; malformed input rejected without partial accepted append. | NOT RUN |
| I-02 | Append / duplicate / concurrency | Idempotent identical event, conflicting duplicate rejection, serialized valid append, incomplete-tail recovery with explicit gap. | NOT RUN |
| I-03 | Provenance / tamper detection | Verify real Git/dirty/input/output/instruction/policy identities; changed chain/snapshot detected; absence of trusted anchor disclosed. | NOT RUN |
| I-04 | Late events / corrections | Append correction events, valid causal links, reproducible as-of snapshots; original reports remain reconstructable. | NOT RUN |
| I-05 | Command recording | Actual successful and failing bounded commands record exit codes/duration/hashes and preserve nonzero status. | NOT RUN |
| I-06 | Security boundaries | Traversal, symlink escape, secret-like metadata and excessive output fixtures; no raw secret persistence. | NOT RUN |
| I-07 | Quality-gate execution | Run CLI validator/test entrypoint with passing/failing candidates; reject missing approvals, traceability and provenance. | NOT RUN |
| I-08 | Coverage / machine reports | Known instrumented commands counted; direct tools/connectors marked unobserved; missing models/cost not treated as zero. | NOT RUN |

### D scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| D-01 | Classification | Only versioned service/environment and serving-threshold-qualified production events count. | NOT RUN |
| D-02 | Commit attribution | Explicit commit-build-artifact-deployment chain; absent link flagged, no time-only inference. | NOT RUN |
| D-03 | Lead time | First qualifying production introduction minus committer time, dedup per service/commit, negative duration invalid. | NOT RUN |
| D-04 | Frequency | Distinct qualifying deployment IDs over exact UTC half-open window duration. | NOT RUN |
| D-05 | Change fail rate | Attributed failed deployment count / cohort deployments, with follow-up cutoff and unavailable zero denominator. | NOT RUN |
| D-06 | Recovery time | Confirmed stabilized recovery minus attributed impairment onset; unresolved failures disclosed. | NOT RUN |
| D-07 | Rework rate | Explicit linked unplanned remediation production deployments / all qualifying deployments. | NOT RUN |
| D-08 | Retries / dedup | Transport retries same rollout, conflicting duplicate rejected, new rollout identity counted only if real deployment. | NOT RUN |
| D-09 | Rollback | Explicit rollback counted/classified under declared policy, causal failure link retained, no repeated commit lead-time sample. | NOT RUN |
| D-10 | Fix-forward | Remediation deployment and recovery linked explicitly; preserve new commits and rework classification. | NOT RUN |
| D-11 | Metric versions | Old version reproduces old result; new semantic version cannot silently overwrite history. | NOT RUN |
| D-12 | Historical replay / late data | Same snapshot/definition/classification yields byte-identical canonical output; late/correction snapshot separately identified. | NOT RUN |
| D-13 | Window / percentile / missing data | Boundary timestamps, nearest-rank p50/p90, timezone normalization, empty samples, missing health/causality. | NOT RUN |

### S scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| S-01 | Hypothesis registration | Predeclared scope/claim/metrics/budget/guardrails and rollback before candidate outcome. | NOT RUN |
| S-02 | Baseline selection | Pinned approved baseline/evaluator/workload; invalid or untraceable baseline blocks promotion. | NOT RUN |
| S-03 | Comparison | Deterministic baseline-fail/candidate-pass and fixed paired-outcome comparisons; retain failed/blocked attempts. | NOT RUN |
| S-04 | Guardrail enforcement | Faster candidate with correctness/scope/evidence regression rejected. | NOT RUN |
| S-05 | Approval separation | Fresh independent reviewer and distinct Chief of Staff approval; implementer's assertion insufficient. | NOT RUN |
| S-06 | Inconclusive | Missing target measurements, insufficient sample/uncertainty, changed workload, or exhausted budget yields inconclusive. | NOT RUN |
| S-07 | Measurement anti-gaming | Reject revised denominator/history/window/criteria used to justify same candidate; versioned separate change required. | NOT RUN |
| S-08 | Promotion / exact candidate | Reject stale head or changed artifact after evaluation; accepted candidate gets scoped PR and verifies merge result. | NOT RUN |
| S-09 | Recursive improvement / limits | Evaluator/promotion change judged by prior evaluator; nested attempts share resource budgets; no self-granted authority. | NOT RUN |
| S-10 | Rollback / cross-boundary containment | Revert known-bad harmless fixture/instruction candidate and resume; no project mutation from organization experiment. | NOT RUN |

### G scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| G-01 | Bootstrap | Verify empty root tree, no legacy files, branch rules, and explicit one-time approval before initial base push. | NOT RUN |
| G-02 | Git exclusions / worktrees | old/projects/worktree exclusions and path-specific staging; task worktree ownership and cleanup evidence. | NOT RUN |
| G-03 | PR / CI | Actual factory PR and workflow run, correct candidate revision, independent review, required checks and thread resolution. | NOT RUN |
| G-04 | Merge / release | Allowed merge method, post-merge revision/content verification and retained evidence; no bypass; final operator acceptance separate. | NOT RUN |

### A scenarios

| Test ID | Scenario | Required observation | Actual result |
| --- | --- | --- | --- |
| A-01 | Post-installation gap interview | All ten operator questions from specification Part 19 presented; discrepancies become durable requirements/tasks. | NOT RUN |
| A-02 | Final acceptance/report | All 26 required final-report topics plus separated organization/project/cross-boundary change lists; operator decision recorded. | NOT RUN |

## Explicit limitations and exclusions for approval

| Item | Initial disposition | Consequence |
| --- | --- | --- |
| 24/7 organization execution after sessions end | Excluded; active native sessions plus durable resume | Autonomy is decision/execution authority while running, not a new permanent service |
| Calendar scheduler / continuous monitors | Excluded initially | Active-session and native CI events only |
| Root startup through AGENTS.md | APP-000008 authorizes the thin root bridge; no universal-client guarantee | Start Codex in /Users/Shared without cd or activation prompt. Fresh native worker RUN-000026 received root instructions automatically and followed the bootstrap; a separate top-level process was not launched. |
| Universal tool interception / trusted hooks | Excluded from core acceptance | Explicit command wrapper and event import cover only invoked paths; bypasses reported |
| Exact actual-model/token/cost metadata | Optional if observable; unknown otherwise | Requested selection must work; no exact cost-efficiency claim without evidence |
| Hostile-worker isolation / tamper-proof ledger | Excluded | Shared filesystem and same identity remain; hashes/PR review detect covered changes but are not immutable storage |
| Production DORA / product CI deployment integration | No live services enrolled | Calculator/fixtures mandatory; production reports unavailable until service-specific enrollment |
| Legacy migration / deletion | Deferred separate project/cross-boundary work | old remains untouched and uncommitted |
| Additional providers/tools/services or purchases | Excluded initially | Existing harness, Python standard library, Git and native GitHub capabilities only |
| Automatic GitHub rules changes | Excluded | Respect protections; operator/admin resolves unavailable bootstrap or required permissions |

These exclusions were explicitly approved in APP-000001; excluded capabilities are not test passes. Native hook support was discovered; automatic activation is not implied by the feature flag. Exact config/trust changes outside agent-org would require a revised cross-boundary scope. Potential local hook invocation can be a subsequent evaluated improvement.

## Evidence standards for autonomous improvement

Deterministic fixes require a retained baseline failure, candidate pass, independent acceptance criteria and relevant regression suite. Stochastic benefit claims require predeclared paired workload, at least 20 paired cases, fixed sampling/stopping, a 95% paired interval excluding no benefit, practical benefit threshold (5% for relative efficiency), and no hard-guardrail regression. If this cannot be established, record inconclusive/reject; do not seek a routine human waiver as a substitute for proof. Governance/evaluator changes use prior approved evaluation semantics and separate versioned approval. Evidence supports bounded claims, never universal correctness.

## Discovery results already obtained

Local Git root/branch/unborn state, read scope, installed executable availability, remote private identity, push/read connector permissions, absence of remote branches, active PR rules, and linear-history removal were inspected. That statement applied at discovery; current execution evidence is in INSTALLATION_RESULTS.md. Production observations remain unavailable. Intake link/path checks passed; they are document checks only.

## Acceptance rules

FULLY_ACCEPTED requires all mandatory in-scope scenarios passing, explicit acceptance of exclusions, all four pre-implementation approvals, completed gap interview, no mandatory unresolved capability and explicit operator final acceptance. LIMITED_INSTALLATION requires explicit operator acceptance of additional unresolved capability exclusions. Otherwise remain INCOMPLETE_OR_BLOCKED. GitHub bootstrap/CI/PR availability is mandatory for the proposed full installation; local-only success does not satisfy it.

## Approval and final acceptance

Contract/implementation approval: APP-000001; original approved hashes and operator source retained there and in approved-v0.1/. Post-installation gap interview: presented after verified PR1 merge and successful main CI; operator accepted all ten checks under APP-000008. Final operator acceptance: APP-000008, explicit acceptance after the ten-question interview. This record must be updated with actual results; no approval of predicted outcomes is requested.

## Current evidence view

Implementation approval is complete under APP-000001. Read [installation results](INSTALLATION_RESULTS.md), task/run/approval records and [final report](../artifacts/INSTALLATION_REPORT.md) for current outcomes. Original approved wording and hashes remain immutable in approved-v0.1/. Operator final acceptance remains separate.

## Accepted outcome and operator amendment

APP-000008 explicitly accepts the completed installation and limits. It also authorizes root AGENTS.md activation from /Users/Shared without cd or a special prompt. This supersedes only the root-entrypoint exclusion; all other scope protections remain. TASK-000025 / REQ-000043 require scoped review and integration evidence.
