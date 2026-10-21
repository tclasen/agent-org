# Requirements baseline v0.1 — awaiting approval

- Target System: organization
- Change Classification: organization
- Authorized Scope: Provisional Markdown installation records in /Users/Shared/agent-org/intake/; operational changes require explicit installation approval.
- Affected Paths or Resources: agent-org/intake/; read-only workspace and GitHub discovery.
- Owning Role: Coordinator.
- Related Requirements: REQ-000001 through REQ-000040 in REQUIREMENTS_BASELINE.md (proposed baseline v0.1).
- Related Tasks: Initial installation request; operational task records not yet created.
- Approval Requirements: Recommendations delegated by SRC-005; implementation and final installation acceptance remain explicit operator gates.

This baseline turns SRC-001 into testable obligations with SRC-002/SRC-005/SRC-006 refinements. It is not an implementation grant. The coverage matrix supplies detailed delegated decisions for each domain; this baseline and those decisions must be read together.

## Requirement metadata and authority

Every row is a distinct requirement. Stable IDs are reserved here and must not be reused; implementation will split them into the corresponding requirements/organization, requirements/project, or requirements/cross-boundary records without changing identity. AC-000001 through AC-000040 are the acceptance identifiers paired by number with each requirement below; subcases get new IDs when instantiated. Each row inherits:

- Authorized Scope: proposed scope only, no implementation authorization until this baseline and the contracts/plan are approved.
- Related Tasks: installation parent and scoped children to be registered after approval; none executed.
- Approval Requirements: operator initial installation approval; subsequent organization changes use autonomous Chief of Staff and independent review, project changes use project authority, cross-boundary changes use both.
- Change Classification: identical to the row's Target System.
- Source: SRC-001 and the referenced delegated coverage decisions; latest explicit operator changes take precedence.
- Status: proposed baseline, no criterion claimed passed.

The row supplies Target System, Affected Paths or Resources, Owning Role, Related Requirements (self and coverage links), and acceptance evidence. Protected safety requirements also apply to all other rows.

## Organization requirements

| ID / related requirement | Target System | Owning Role | Affected Paths or Resources | Requirement | Acceptance criterion / evidence |
| --- | --- | --- | --- | --- | --- |
| REQ-000001 | organization | Coordinator | agent-org/ | **Classify every substantive request before admission:** Record intended target; clarify ambiguity; status/clarification create no mutation tasks. | AC-000001: Five-way classification and ambiguous-request live scenarios; all ten boundary scenarios. |
| REQ-000002 | organization | Chief of Staff | agent-org/ | **Single organization namespace:** Keep durable organization records in Markdown under agent-org; native telemetry/program exceptions only; no root AGENTS/harness directory or replacement runtime. | AC-000002: Namespace scan, record-type validation, directory review. |
| REQ-000005 | organization | Coordinator | agent-org/agents/ and workflows/ | **General-purpose work:** Route software, research, analysis, writing, operations, planning and organizational tasks through authorized native tools. | AC-000005: Representative software, research and writing/planning task trials. |
| REQ-000006 | organization | Coordinator | agent-org/intents/, tasks/, artifacts/ | **Intent and outcome reconciliation:** Bind user intent to requirements and evidence; do not accept worker completion as user satisfaction. | AC-000006: Mismatch/reopen and successful reconciliation scenarios. |
| REQ-000008 | organization | Chief of Staff | agent-org/ | **Autonomous recursive self-improvement:** Autonomously observe, propose, plan, experiment, independently approve and promote proven organization changes through PRs within inherited authority. | AC-000008: Actual harmless governed correction plus promotion/rejection/inconclusive tests. |
| REQ-000009 | organization | Coordinator | agent-org/approvals/, plans in tasks/ | **Approval evidence:** Bind grants to scope, resources, plan/candidate revision, owner and conditions; no self-approval by implementing worker. | AC-000009: Missing/stale/wrong-scope approval rejection and legitimate autonomous approval tests. |
| REQ-000011 | organization | Coordinator | agent-org/agents/coordinator/ | **Responsive Coordinator:** Clarify material uncertainty, decide routine details, communicate progress/blockers and repair dissatisfied outcomes. | AC-000011: Live clarification/status/delegation interaction and review. |
| REQ-000012 | organization | Planner | agent-org/tasks/, workflows/, approvals/ | **Separate planning from execution:** Use requirements/plan/review/authorization/implementation/verification/integration/acceptance lifecycle; replan material deviations. | AC-000012: Unapproved-plan refusal, approved bounded execution, version-change invalidation. |
| REQ-000013 | organization | Chief of Staff | agent-org/agents/ | **Dynamic role discovery:** Eight initial roles with AGENTS and CONTEXT; discover directories and capabilities without hard-coded routing. | AC-000013: Add/remove synthetic agent discovery fixture, registry consistency. |
| REQ-000014 | organization | Coordinator | agent-org/runs/, tasks/; native collaboration tools | **Fresh delegation:** Persist task, check scope/dependencies, choose model/reasoning, create run, spawn fresh worker, load instructions, receive durable handoff. | AC-000014: Real independent-context and parallel-worker trials with native IDs. |
| REQ-000015 | organization | Coordinator | agent-org/policies/MODEL_SELECTION.md and runs/ | **Per-run model and reasoning selection:** Record task rationale, requested/actual configurations, tool support and fallback; unknown actual metadata stays unknown. | AC-000015: Two live requested configurations; unsupported-model/reasoning and fallback tests. |
| REQ-000016 | organization | Coordinator | agent-org/shared/, tasks/, runs/ | **Durability and recovery:** Checkpoint claims/artifacts/side effects; reconcile after interruption with fresh context; no execution-survival claim. | AC-000016: Fresh agent resumes solely from durable records; stale claim/cancellation/retry tests. |
| REQ-000017 | organization | Coordinator | agent-org/tasks/, requirements/, shared/ | **Stable record identity and task state:** Unique never-reused typed IDs, required metadata, state transitions, append history and traceability; serialize allocation. | AC-000017: Duplicate IDs, missing scope, wrong location and illegal-state negative tests. |
| REQ-000018 | organization | Planner | agent-org/tasks/, initiatives/ | **Work graph correctness:** Typed dependencies; blocking DAG, derived readiness, parent/child obligations and claim collision detection. | AC-000018: Cycle, unmet dependency, duplicate claim and incomplete-parent rejection tests. |
| REQ-000019 | organization | Coordinator | agent-org/requirements/ | **Requirements durability:** Separate organization/project/cross-boundary requirements, revisions, AC IDs and canonical source references. | AC-000019: Traceability/revision/supersession/conflict fixtures and live task registration. |
| REQ-000022 | organization | Reviewer | agent-org/factory/ and evaluations/ | **Deterministic organization verification:** Python standard-library tests validate records, governance, instrumentation and negative cases; behavior claims require live agents. | AC-000022: Full organization test suite plus live scenario evidence, no invented passes. |
| REQ-000025 | organization | Chief of Staff | agent-org/factory/dora/ | **Versioned DORA semantics:** Define all five metrics, identities, causality, thresholds, timestamps, corrections and window rules; live values only on service enrollment. | AC-000025: Explicit expected synthetic fixture outputs including attribution and missing data. |
| REQ-000026 | organization | Reviewer | agent-org/factory/metrics/, dora/, reports/ | **Reproducible delivery calculations:** Same snapshot/definition/classification yields same canonical result; retain snapshot hashes and versions. | AC-000026: Repeated byte-identical replay, event order/dedup/late/correction tests. |
| REQ-000027 | organization | Executor | agent-org/factory/instrumentation/, events/ | **Deterministic instrumentation:** Append-only JSONL writer with schema validation, idempotency/conflict rules, hash chain and correction events; explicit command runner. | AC-000027: Real command recording, malformed/duplicate/correction/concurrent-append/tamper tests. |
| REQ-000028 | organization | Reviewer | agent-org/factory/provenance/, reports/ | **Provenance and coverage honesty:** Record actual revisions, dirty state, hashes, tool/environment and available model metadata; identify bypass paths and unknown data. | AC-000028: Provenance hash comparisons and coverage/unknown-field fixtures. |
| REQ-000031 | organization | Chief of Staff | agent-org/factory/reports/ and evaluations/ | **Separate scorecards:** Organization performance, project quality and measurement health remain distinct with denominators and uncertainty. | AC-000031: Report structure and missing-data tests; no opaque composite score. |
| REQ-000032 | organization | Reviewer | agent-org/factory/quality-gates/, baselines/, evaluations/ | **Measurement independence:** Evaluate candidate under pinned prior rules and independently reviewed evidence; disclose shared-filesystem limits. | AC-000032: Baseline alteration/mismatched candidate rejection, independent review trial. |
| REQ-000033 | organization | Coordinator | agent-org/policies/RESOURCE_BUDGETS.md and runs/ | **Cumulative resource limits:** Bound workers/retries/depth/time/storage/experiments; recursion cannot reset budgets; unknown costs remain unknown. | AC-000033: Budget aggregation/exhaustion/retry/depth cases. |
| REQ-000034 | organization | Coordinator | agent-org/triggers/ and factory CI integration | **Honest native triggers:** Session-start/after-five-tasks checks and CI events only; no self-running Markdown or persistent agent service. | AC-000034: Trigger dedup/disable/ownership tests; explicit execution mechanism evidence. |
| REQ-000035 | organization | Chief of Staff | agent-org/experiments/, evaluations/, factory/benchmarks/ | **Predeclared improvement experiments:** Pin hypothesis, baseline, candidate, workload, metrics, guardrails, stopping rules and rollback before results. | AC-000035: Accept/reject/inconclusive fixtures and one actual bounded correction. |
| REQ-000036 | organization | Chief of Staff | agent-org/policies/, factory/quality-gates/, approvals/ | **Recursive promotion and rollback:** Previous approved evaluator governs changes to evaluator/promotion logic; exact candidate/head binds approval; PR promotion and rollback. | AC-000036: Self-validation prevention, guardrail violation, stale head, known-good rollback tests. |
| REQ-000037 | organization | Researcher | agent-org/knowledge/, factory/baselines/ | **Historical evidence discipline:** Legacy references retain source revision; no bulk import or production-history fabrication; synthetic/live/production evidence distinct. | AC-000037: Evidence provenance validation and missing/untrusted-source rejection. |
| REQ-000038 | organization | Coordinator | agent-org/README.md, indexes and reports/ | **Auditable reporting:** Concise human reports plus native telemetry outputs; list failures, gaps, exclusions, tests actually run and acceptance state. | AC-000038: Report completeness review, links, start instructions and gap reporting. |
| REQ-000039 | organization | Reviewer | agent-org/intake/ACCEPTANCE_CONTRACT.md and evaluations/ | **Complete installation test matrix:** Execute organization, project, ten cross-boundary, instrumentation, DORA and self-improvement scenarios; no omitted mandatory test. | AC-000039: Criterion-level evidence matrix, independent review and discrepancy tasks. |
| REQ-000040 | organization | Coordinator | agent-org/intake/ACCEPTANCE_CONTRACT.md and final report | **Operator final acceptance:** Post-install gap interview and explicit operator acceptance; use FULLY_ACCEPTED/LIMITED_INSTALLATION/INCOMPLETE_OR_BLOCKED honestly. | AC-000040: Ten gap questions disposition, no unresolved mandatory capabilities, operator decision. |

## Project requirements

| ID / related requirement | Target System | Owning Role | Affected Paths or Resources | Requirement | Acceptance criterion / evidence |
| --- | --- | --- | --- | --- | --- |
| REQ-000023 | project | Developer | Temporary test repositories within agent-org/factory test-artifact scope | **Synthetic project workflow acceptance:** Demonstrate requirements, approved plan, file change, tests, review, integration and intent reconciliation without modifying old projects. | AC-000023: Actual synthetic project diff, executed tests, fresh review, acceptance record. |

## Cross-boundary requirements

| ID / related requirement | Target System | Owning Role | Affected Paths or Resources | Requirement | Acceptance criterion / evidence |
| --- | --- | --- | --- | --- | --- |
| REQ-000003 | cross_boundary | Coordinator | agent-org/ and explicitly enrolled project roots | **Enforce separate authority and scope:** Organization and project grants never imply each other; cross-boundary parent has separately scoped children and acceptance. | AC-000003: Positive/negative path, authority, dependency and boundary tests. |
| REQ-000004 | cross_boundary | Coordinator | agent-org/knowledge/projects/ and future registered repositories | **Independent portfolio management:** Register project ID, canonical root, remote, ticket source, requirements authority, overrides and owners; preserve independent Git histories. | AC-000004: Two temporary repository enrollment/routing fixtures; no legacy migration. |
| REQ-000007 | cross_boundary | Coordinator | agent-org/knowledge/projects/; no real product edits initially | **Project enrollment and overrides:** Profiles reference canonical project instructions/tickets; overrides cannot weaken user authority or protected organization rules. | AC-000007: Override conflict, remote identity mismatch and source-of-truth tests. |
| REQ-000010 | cross_boundary | Coordinator | Explicitly approved repository/workspace integrations | **External actions remain bounded:** Organization autonomy does not grant project deployment, public messaging, purchases, credential access or destruction. | AC-000010: External-effect reconciliation and permission-negative fixtures. |
| REQ-000020 | cross_boundary | Reviewer | Factory origin, task branches/worktrees, enrolled project remotes | **PR-based delivery and isolation:** Factory PR required; independent review; separate org/project commits; no force push or unrelated staging. | AC-000020: Scope diff, review-head binding, GitHub PR/CI/merge evidence where authorized. |
| REQ-000021 | cross_boundary | Coordinator | Root Git integration and .gitignore | **Preserve legacy and safely bootstrap:** Never commit old or project checkouts; propose one empty initial main commit solely as PR base, subject to explicit installation approval/server rules. | AC-000021: Empty tree inspection, ignore checks, staged-path checks, remote base verification. |
| REQ-000024 | cross_boundary | Executor | agent-org/factory/ and .github/workflows/agent-org.yml | **Factory CI integration:** Minimal native GitHub Actions invokes same local validators; read-only token, no secrets, pinned actions; no product CI edits. | AC-000024: Local command equivalence and actual PR CI run; unavailable CI remains unverified. |

## Shared safety and authority constraints

| ID / related requirement | Target System | Owning Role | Affected Paths or Resources | Requirement | Acceptance criterion / evidence |
| --- | --- | --- | --- | --- | --- |
| REQ-000029 | cross_boundary | Coordinator | Organization records, project data and authorized integrations | **Confidentiality and least privilege:** No secrets/unnecessary private content in records; respect sandbox/network permissions; no unsupported residency/compliance claims. | AC-000029: Redaction, path/symlink escape, output-sanitization tests; permission inventory. |
| REQ-000030 | cross_boundary | Chief of Staff | Governance, acceptance and measurement definitions across scopes | **Protected authority and history:** Cannot self-expand user authority, bypass host controls, erase evidence or silently weaken explicit requirements; past approvals retained. | AC-000030: Anti-gaming, governance-mutation and out-of-scope dependency tests. |

## Cross-boundary acceptance obligations

For each cross-boundary requirement, independently verify organization-side records/governance and project-side file/resource effects, then their integration. REQ-000003/4/7 require portfolio/scope records plus independent project fixtures; REQ-000010 requires permission records plus actual/simulated side-effect reconciliation; REQ-000020/21/24 require organization checks plus root Git/ignore/CI behavior; REQ-000029/30 require organization evidence controls and matching project/external boundary behavior. Passing only one side never accepts the parent.

## Initial portfolio and exclusions

There is no enrolled production service or real product project in this installation. REQ-000023 uses actual temporary test repositories solely for acceptance. All future product requirements preserve their own authoritative specifications/tickets. No requirement grants old/ migration, deletion, or publication.

Core capabilities to install are detailed in ACCEPTANCE_CONTRACT.md. Exclusions are explicit and part of the approval package, not unstated gaps. No automatic background execution after session termination, full tool interception, exact cost telemetry, or hostile-worker containment is claimed.

## Approval

Operator approval: PENDING. Approved revision/hash: PENDING. Approval source/time: PENDING. Material changes reopen affected approvals. Initial installation acceptance is distinct from baseline approval.
