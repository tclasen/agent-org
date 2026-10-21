# Installation report

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: APP-000001 approved installation and evidence only
- Affected Paths or Resources: agent-org; root .gitignore and .github/workflows/agent-org.yml; isolated project fixtures; factory Git/PR
- Owning Role: Coordinator
- Related Requirements: REQ-000001 through REQ-000042
- Related Tasks: TASK-000001, TASK-000006, TASK-000008, TASK-000021
- Approval Requirements: APP-000001; final operator acceptance pending

Current state: **INCOMPLETE_OR_BLOCKED**. Implementation and bounded local evidence exist; measurement qualification is independently approved; final Git integration and operator acceptance remain pending. This report describes observed evidence, not predicted acceptance.

| Required topic | Installed design, actual evidence or explicit limit |
| --- | --- |
| 1 Repository findings | The factory repository is /Users/Shared, with private tclasen/agent-org remote and an originally empty main branch. old/ is read-only legacy material. The installation uses Python standard-library utilities, Git and native Codex workers. See [discovery](../intake/DISCOVERY.md). |
| 2 Interview decisions | The [coverage record](../intake/COVERAGE.md) preserves 25 interview domains and 318 dispositions. Decisions include delegated recommendations, autonomous evidence-qualified organization approval, separate project grants and mandatory PR delivery. The operator removed the linear-history requirement. |
| 3 Requirements baseline | The [requirements registry](../requirements/INDEX.md) contains 40 initial requirements and two bounded qualification requirements. Organization, project and cross-boundary records retain separate targets and canonical project references. |
| 4 Scope contract | All of Shared is readable; organization writes are limited to agent-org, with named root ignore/CI, Git/PR and temporary-fixture exceptions. old/ must never be staged, migrated or deleted. Real project writes require enrollment and a grant. See the [scope contract](../intake/SCOPE_CONTRACT.md). |
| 5 Organization architecture | Eight durable capability roles use Markdown requirements, tasks, plans, decisions and handoffs. Native workers execute tasks; small deterministic utilities validate records and measure evidence. No orchestration service is installed. |
| 6 Project integration | [Project profiles](../knowledge/projects/INDEX.md) preserve independent repositories, remotes, ticket/specification authority and overrides. Two isolated Git fixtures demonstrate bounded scope and product work. No real product repository has been enrolled. |
| 7 Cross-boundary architecture | A classified parent links separately scoped organization, project and integration children. Each side needs its own impact analysis, approval, evidence and acceptance. Root CI invokes organization verification; parent acceptance requires both systems. |
| 8 Complete structure | The [directory inventory](DIRECTORY_STRUCTURE.md) lists installation source, records and evidence. Ignored temporary fixtures are listed separately from factory Git content. |
| 9 Agents | The [role registry](../agents/INDEX.md) lists Coordinator, Chief of Staff, Planner, Researcher, Architect, Developer, Executor and Reviewer. Each has AGENTS.md and CONTEXT.md. Routing uses capabilities; models are selected per task. |
| 10 Native delegation | Actual fresh and parallel workers have separate run identities, including independent reviewer and approver executions. Their shared filesystem provides procedural coordination, not isolation from a hostile process. See the [independent review](../factory/reports/RUN-000012/HANDOFF.md). |
| 11 Model and reasoning selection | Native invocations requested gpt-6.1-sol/high, gpt-6-astra/high and gpt-6-luna/medium. Requested settings are recorded; actual model, reasoning, token use and cost remain unknown without trusted harness metadata. A live worker refused an unsupported-selection gap; no failed native invocation or successful fallback is claimed. |
| 12 Organization changes | EXP-000001 repaired the record validator and WORK_GRAPH instructions under prior criteria. Independent review and distinct [APP-000005](../approvals/APP-000005.md) qualify exactly four frozen files for PR promotion. The separate [APP-000006](../approvals/APP-000006.md) qualifies measurement1.0.1 for adoption through PR. Final integration remains pending. |
| 13 Project changes | A fresh specialist changed alpha/title.py in an isolated synthetic project. Three tests passed after two initial failures, and exact source was integrated locally as commit 89e6d4b. [Project acceptance](../evaluations/EVAL-000004.md) is separate from organization acceptance. |
| 14 Cross-boundary approval | Organization authority never grants project authority. Named grants and scoped children are required. Negative fixtures and cooperative live-worker ambiguity/scope refusals exercise this boundary; they do not establish hostile-worker enforcement. |
| 15 Task and requirement tracking | Stable IDs, eight mandatory scope fields, typed graphs, prerequisite/approval checks, conflict claims and durable handoffs support tracking. Fresh-worker recovery reconciles persisted artifacts. Markdown claims are not atomic locks. See [WORK_GRAPH](../shared/WORK_GRAPH.md). |
| 16 Planning behavior | The workflow is dialogue, requirements, plan, review, authorized implementation, verification, integration and acceptance. APP-000001 preceded installation; APP-000002/3/4 bound corrections. A plan alone does not grant permission. |
| 17 Instrumentation | Versioned append-only JSONL events, an explicit command wrapper and hashed snapshots record bounded evidence. Actual wrapper captures include exits 0 and 7. Direct tools, connectors and worker internals are outside that capture coverage; local hashes have no trusted immutable anchor. |
| 18 DORA | A deterministic calculator implements five metrics with causal attribution, UTC windows, as-of replay, versioned definitions and nearest-rank percentiles. The production registry is empty; observations are synthetic. Version1.0.1 passed local and independent replay; [EVAL-000006](../evaluations/EVAL-000006.md) and APP-000006 approve its bounded adoption through PR. Production observations remain unavailable. |
| 19 Measurement integrity | Original events, rejected cases and source versions remain available; corrections append rather than rewrite history. Organization, project and measurement-health scorecards are separate. Exact workload/evidence pins support comparisons; unknown cost is never treated as zero. |
| 20 Quality gates | Record/scope/approval/evidence validation and positive/negative tests exist. Final RUN-000019 passed 85 tests, original22/58 replays, six independent regressions and30 restoration tests; fresh RUN-000020 passed120 additional cases. Earlier failed candidates remain retained. Initial hosted CI passed77 tests; final-head CI remains required. |
| 21 Self-improvement controls | Observation, evidence, preregistration, baseline comparison, guardrails, independent review, distinct approval, PR delivery and rollback bound improvement. EXP-000001 demonstrates a bounded repair under the original normative contract. Gate1.0.0 and intermediate1.0.1 candidates were rejected and retained. Exact final1.0.1 is independently qualified by APP-000006 for PR adoption. No change may grant itself authority or rewrite its scoreboard. |
| 22 Executed tests | The [70-scenario matrix](../intake/INSTALLATION_RESULTS.md) distinguishes actual workers, executed synthetic tests and pending acceptance. Raw reports preserve failures, versions, hashes, exit codes and elapsed-time proxies. A documented design is not a test pass. |
| 23 Known limitations | Startup requires an explicit prompt. Autonomy operates during active sessions; there is no 24/7 scheduler, background runtime, universal interception, trusted actual-model cost feed, hostile-worker isolation or production deployment evidence. |
| 24 Open gaps | Final Git-head binding, hosted CI on that head, merge verification and the operator gap interview/final acceptance remain pending. The code and root integration have separate independent acceptance decisions. Real repositories, production services and ticket systems require separately authorized enrollment. |
| 25 Operator acceptance | APP-000001 approves the initial contract, not future outcomes. Post-installation gap responses and final operator acceptance remain pending. Only the operator can accept the installation as complete or agree to a limited installation. |
| 26 Start Coordinator | From /Users/Shared request: “Read agent-org/AGENTS.md, initialize the Coordinator, reconcile open work and interrupted runs, and report the next authorized action.” See the [startup lifecycle](../shared/SESSION_LIFECYCLE.md). |

## Organization changes

Policies, shared protocols, workflows, requirements, tasks, approvals, evaluations, experiments, capability records, project profiles, guides and deterministic factory code/tests/telemetry live under agent-org. The [inventory](DIRECTORY_STRUCTURE.md) identifies the files. Original approved intake snapshots remain unchanged. AGENTS instructions do not themselves enforce sandbox boundaries or continued execution after a session ends.

The source-grounded enrollment guide was initially rejected for omitting explicit startup instructions. A bounded repair preserved REQ-000042, and an independent reviewer accepted final SHA256 d1e27d8391bdad0c9cd8fe7a68f83a70773d9f25c6d9c1b99c61373d25f8d67c. The [repair addendum](../factory/reports/RUN-000012/TASK-000018-repair-addendum.md) preserves this actual intent-repair history.

## Project changes

The alpha fixture's title normalizer was changed, tested, independently reviewed and integrated locally; beta and pinned organization sources were preserved. These are synthetic project exercises. No real managed project or legacy file was modified. See [EVAL-000004](../evaluations/EVAL-000004.md).

## Cross-boundary changes

APP-000001 names root .gitignore and .github/workflows/agent-org.yml as installation integration exceptions. The ignore file excludes legacy/project/worktree/temporary/cache content. The workflow is configured for PR, main push and manual checks on Python 3.13/Ubuntu 24.04 with read-only token permissions and pinned Actions. Local execution used Python 3.15/macOS; the initial hosted CI run passed. Final-head CI will be checked before merge.

The approved empty bootstrap commit is a9d57b9. The installation branch and isolated worktree/exclusion checks exist. [Draft PR1](https://github.com/tclasen/agent-org/pull/1) contains separate organization7214089 and root5ab279c commits. [Initial CI](https://github.com/tclasen/agent-org/actions/runs/39675768661) passed; final-head binding/CI, allowed merge and post-merge verification remain pending. No protection bypass or automatic rule change is claimed.

## Evidence and acceptance

Read the [current matrix](../intake/INSTALLATION_RESULTS.md), [authority grant](../approvals/APP-000001.md), [requirements](../requirements/INDEX.md), [task registry](../tasks/INDEX.md) and [enrollment guide](../knowledge/PROJECT_ENROLLMENT.md). The evidence supports bounded installation claims; it does not establish general productivity, universal correctness or production readiness. The Coordinator must record operator gap responses before FULLY_ACCEPTED or an explicitly agreed LIMITED_INSTALLATION outcome.

## Preserved review history

EVAL-000001 rejected three validator defects; EXP-000001 repaired them and earned independent APP-000005 eligibility. EVAL-000002 rejected malformed-evidence gate behavior and a DORA disclosure gap. The first measurement correction had two suite failures; retry1 passed77 tests but EVAL-000005 found six missing-telemetry cases. Final retry2 passed85 tests and120 independent cases, then earned APP-000006. The original criteria, source versions and all failures remain preserved. A concurrent root event append triggered an inventory stop; its ownership, unchanged prefix and valid chain were independently reconciled.

The staging audit also caught a copied temporary rollback checkout. It was removed from the index and retained under the ignored execution area. No nested project repository or old/ content is committed. [EVAL-000007](../evaluations/EVAL-000007.md) independently accepts the exact two root files and their limited privileges.
