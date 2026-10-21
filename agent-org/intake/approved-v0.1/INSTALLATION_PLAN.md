# Installation plan v0.1 — awaiting implementation authorization

- Target System: organization
- Change Classification: organization
- Authorized Scope: Provisional Markdown installation records in /Users/Shared/agent-org/intake/; operational changes require explicit installation approval.
- Affected Paths or Resources: agent-org/intake/; read-only workspace and GitHub discovery.
- Owning Role: Coordinator.
- Related Requirements: REQ-000001 through REQ-000040 in REQUIREMENTS_BASELINE.md (proposed baseline v0.1).
- Related Tasks: Initial installation request; operational task records not yet created.
- Approval Requirements: Recommendations delegated by SRC-005; implementation and final installation acceptance remain explicit operator gates.

## Outcome and design

Install one Markdown-first organization using native Codex collaboration, not a new orchestration service. Coordinator handles intake, classification, requirements, approvals and reconciliation; Chief of Staff governs autonomous evidence-based organization evolution; Planner decomposes work; Researcher, Architect, Developer, Executor and Reviewer supply capabilities. Agents are discovered from directories and registry. Each execution gets fresh task-selected model/reasoning and scoped instructions. Shared records support interrupted-session recovery; deterministic Python tools validate, instrument and calculate metrics.

Independent projects keep their own Git histories, remotes and issue/board/specification authority. Central Markdown project profiles map those authorities and permissible overrides. No actual legacy project is enrolled or migrated in installation; two isolated temporary repositories prove portfolio behavior.

## Prerequisites and approval gate

1. Operator approves REQUIREMENTS_BASELINE.md, SCOPE_CONTRACT.md, ACCEPTANCE_CONTRACT.md and this plan, including exclusions and the one-empty-commit bootstrap exception.
2. Reconcile Git state and verify current remote rules. Preserve provisional records and all user changes. Do not stage old.
3. Bootstrap a zero-file main commit only if approved; verify empty tree and push through normal permissions. If refused, stop that step, report the exact server restriction and await admin bootstrap; never weaken/bypass protections.
4. Use a short-lived installation branch and task-owned worktrees as needed. Native worktree permission restrictions must be respected; no claim of isolation until actual path/status verified.

## 1. Organization configuration — organization-only

- Register installation cross-boundary parent with separate organization, root-integration, synthetic-project and verification children. Each has requirements, plan, scope, approval reference, history and independent acceptance.
- Promote intake requirement IDs into durable requirement records, preserving history and sources; create useful indexes/templates, never empty placeholder operational records.
- Create the eight role AGENTS.md/CONTEXT.md pairs, discovery registry, root agent-org instructions and concise README bootstrap.
- Implement governance, authority boundaries, lifecycle, planning, model selection, context/handoff/recovery, project enrollment, work graphs, resources and autonomous improvement policies.
- Define stable IDs and required metadata for requirements/tasks/plans/decisions/runs/approvals/artifact manifests/evaluations. Validate ID uniqueness, graph links, scoped paths, states, claims and evidence completeness.
- Define autonomous approval: independent Reviewer checks candidate under prior rules; Chief of Staff approves qualified organization changes; Coordinator reconciles boundaries/outcomes; PR is mandatory. User-granted authority cannot be expanded by the organization.
- Do not use role-fixed model assignments. Policies recommend configurations per risk/type, validate availability and preserve actual-metadata uncertainty.

Planned organization layout (every directory gets useful content/indexes only when implemented; no fabricated runs):

```text
agent-org/
  AGENTS.md  README.md
  agents/{INDEX.md,coordinator/,chief-of-staff/,planner/,researcher/,architect/,developer/,executor/,reviewer/}
  intake/                    # existing interview and contracts preserved
  requirements/{INDEX.md,TEMPLATE.md,organization/,project/,cross-boundary/}
  tasks/{INDEX.md,TEMPLATE.md,organization/,project/,cross-boundary/}
  initiatives/ intents/ workflows/ decisions/ runs/ approvals/ artifacts/
  knowledge/projects/ capabilities/ triggers/ evaluations/ experiments/
  policies/                  # all policies specified in original Part 7
  shared/                    # all shared conventions specified in original Part 7
  factory/
    README.md
    instrumentation/ events/ provenance/ metrics/ dora/ quality-gates/
    baselines/ benchmarks/ reports/ tests/ artifacts/
```

All policy/shared filenames from the original layout remain requirements; the abbreviated tree is not a reduction. Native code/telemetry are confined to factory where practical. Framework code must remain small deterministic utilities, never an agent runtime, scheduler or message broker.

## 2. Host-project integration — cross-boundary

Organization child: project profiles, Git/CI adapter contract, provenance, scoped approval/verification rules.
Project/root child: add only root .gitignore and .github/workflows/agent-org.yml. Ignore old, future project checkouts and explicitly declared worktree/runtime artifact paths. Never ignore durable governance records. Keep independent repository contents out of the outer index.
Integration child: validate exclusions, root CI invocation of organization checks, repository/PR identity, linked commit provenance, and independent organization/root acceptance.

CI uses read-only repository token and no deployment/secret access. Pin any required Actions by immutable commit during implementation. Use standard-library Python commands supported by the CI runner and current local interpreter; record version differences. Avoid pull_request_target and executing candidate code with privileged secrets. Branch-required status settings are not modified automatically; report whether workflow checks are host-enforced or procedural promotion gates.

Commit organization content separately from root integration changes; submit through the factory PR path. After independent review and passing checks, approved installation authority may merge the PR without bypass. Operator final installation acceptance is still separate.

## 3. Deterministic instrumentation — organization-only plus named integration

Implement small Python standard-library modules/entrypoints for record validation, scoped snapshots, explicit command execution, versioned event append/validation/replay, provenance, scorecard generation and experiment gate comparison. Commands are argument arrays with bounded runtime; preserve exit code; hash/redact output; avoid implicit shell interpolation. These tools assist native agents; they never dispatch agent workloads or run continuously.

Store versioned JSONL events under factory/events, with explicit event/task/run/agent IDs, classification, occurrence/ingestion times, known model/tool/revision/hash/causal/resource fields. Corrections append; identical duplicates idempotent, conflicting duplicates invalid. Use short-lived local append lock and detect incomplete writes; retain sequence/hash-chain consistency without claiming tamper-proof storage. Immutable snapshot content hashes bind reports and evidence. Unknown metadata stays null/unknown.

Wrappers observe their own commands; adapters consume explicit imported/native evidence. Direct tool calls, connector operations and subagent internals may bypass capture. Publish coverage gaps. No mandatory local/native hook activation is included because namespace-compatible config and trust have not been verified. No hidden global configuration edits.

## 4. DORA measurement — organization-only

Implement version 1 of the chosen definitions in COVERAGE.md Domain O, with explicit service/environment registry inputs and canonical commit/build/artifact/deployment/failure/remediation/recovery links. Live registry starts without production services. Synthetic fixtures use declared 100% traffic and 30-minute recovery stabilization; do not install those values into an actual project's service policy.

Calculate change lead time, deployment frequency, change fail rate, failed-deployment recovery time and deployment rework rate deterministically. Parameterize UTC half-open reporting windows and as-of snapshot, nearest-rank percentiles, classification/definition versions, and complete denominator/missing-data reporting. Preserve prior snapshots. Metrics code must not use LLM judgment to infer causal failures or authoritative values.

## 5. Verification and acceptance — separate organization/project/integration results

Execute the complete ACCEPTANCE_CONTRACT.md matrix. Use deterministic positive/negative fixtures and actual fresh-agent trials; neither substitutes for the other. Test all ten mandatory boundary scenarios. Test scoped project implementation in actual temporary Git repositories, not old projects. Demonstrate independent review, fresh-context recovery, dynamic discovery, per-run model/reasoning controls, invalid/missing approvals, append corrections, provenance, DORA replay, and self-improvement reject/inconclusive/promotion/rollback.

A harmless real organization correction exercises the approval lifecycle; label it installation qualification, not evidence of general productivity improvement. Broader recursive optimization starts only after baseline installation approval and qualified evidence. Candidate changes to promotion/evaluation logic are checked by prior approved rules, not their own altered evaluator.

Persist raw sanitized results and Markdown summaries with exact candidate hashes. Fresh Reviewer inspects final diff, tested artifacts, scope separation and coverage. Run local suite, then actual PR CI. Reconcile post-merge state. Present gap interview's ten questions and fix discrepancies within accepted authority. Produce the required 26-topic final report with separate organization/project/cross-boundary change lists. Record operator final acceptance.

## Expected verification commands — to be implemented, not yet available

- `python3 -m unittest discover -s agent-org/factory/tests -v`
- `python3 agent-org/factory/instrumentation/check.py --root agent-org`
- `git diff --check`, plus explicit untracked/staged/nested scope review.
- Deterministic event/metric/experiment replay commands documented next to implemented tooling.

Exact CLI names may be refined during implementation without expanding authority; contract changes require revised approval. No test result is implied by these command proposals.

## Startup contract

From /Users/Shared, start Codex with the prompt: “Read agent-org/AGENTS.md, initialize the Coordinator, reconcile open work and interrupted runs, and report the next authorized action.” The installation must demonstrate this in a fresh context. Merely opening an arbitrary root session is not claimed to load nested instructions automatically.

## Risks, failure handling and rollback

Native permissions may prevent Git metadata writes, remote bootstrap, task worktrees or PR/CI actions; obtain ordinary tool approvals if needed and never weaken controls. If remote bootstrap is blocked, complete reviewable local authorized work and retain blocked integration status. No FULLY_ACCEPTED claim before mandatory external checks succeed. Shared filesystem permits bypass; use evidence integrity and independent review, disclose enforcement limits. Preserve all failed trials. Revert only owned installation changes via PR after recording evidence; do not remove old or unrelated files.

## Approval requested

Approve v0.1 baseline, scope, acceptance contract (including explicit exclusions), this plan, and exactly one empty main bootstrap commit if needed. This grants implementation, bounded fixture tests/native agent trials, root ignore/CI integration, scoped commits/task-branch pushes/PR and reviewed merge for installation. It does not accept final results, authorize real project migration, or grant production access.

Operator authorization: PENDING. Approved document hashes/time/source: PENDING.
