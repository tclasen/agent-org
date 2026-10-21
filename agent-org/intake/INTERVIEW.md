# Operator interview

- Target System: organization
- Change Classification: organization
- Authorized Scope: Provisional Markdown discovery, interview, coverage, and draft-contract records in /Users/Shared/agent-org/intake/ only.
- Affected Paths or Resources: /Users/Shared/agent-org/intake/; read-only discovery of /Users/Shared.
- Owning Role: Coordinator (current installation session).
- Related Requirements: Operator installation specification; approved baseline not yet established.
- Related Tasks: Installation request in this conversation; operational task registration awaits implementation authorization.
- Approval Requirements: Provisional intake records authorized by operator answer 5. Requirements Baseline, Scope Contract, Installation Acceptance Contract, and implementation plan require explicit approval before implementation.

Date: 2026-10-21. All decision sections below inherit the mandatory scope metadata above. These are installation decisions, not implementation authorization.

## Sources

- SRC-001: Initial operator installation specification in this conversation, including mandatory discovery/interview/approval gates, Markdown-first organizational state, agent-org namespace, no separate harness/daemon, and organization/project/cross-boundary separation.
- SRC-002: Operator's numbered response to Interview Round 1 in this conversation.
- SRC-003: Read-only local discovery on 2026-10-21; commands and observations summarized in DISCOVERY.md.
- SRC-004: Native tool declarations and active session permission configuration. Advertised capabilities remain distinct from tested behavior.

## DEC-000001 — Multi-repository factory

Source: SRC-002 answers 1–2. Status: answered. Affected system: organization and project portfolio.

The repository rooted at /Users/Shared is the factory/agent organization. It manages itself and a collection of independent Git repositories, each with its own remote and project-specific issue/project board or other ticket system, sometimes local. This is not installation into one product repository. Exact future checkout locations and initial project enrollments remain undecided.

## DEC-000002 — Preserve old/ as reference material

Source: SRC-002 answer 1. Status: answered. Affected system: project portfolio and organization migration boundary.

The operator will gradually migrate material from old/ after initialization. Do not commit old/. Learning from its contents is permitted. Keep it ignored or unstaged before eventual deletion. Current disposition: leave it unstaged; no .gitignore change, migration, deletion, or automatic adoption is authorized by this interview answer.

Old repository instructions and historical approvals are reference evidence, not standing authorization in the new factory. Their future adoption requires explicit disposition.

## DEC-000003 — Workspace read scope

Source: SRC-002 answer 3. Status: answered. Affected system: organization and project portfolio.

The operator permits reading the entire /Users/Shared folder. This covers relevant discovery by organization-maintenance agents as well as project agents. Read permission does not imply permission to modify repositories, operate external services, or persist secrets in organizational records. Existing harness security restrictions remain applicable.

## DEC-000004 — Root startup and organization namespace

Source: SRC-002 answer 4 and SRC-001. Status: answered. Affected system: organization.

New Codex sessions will start in /Users/Shared. Keep organizational material separable inside /Users/Shared/agent-org/. Do not create a root AGENTS.md or harness-specific configuration directory. The root-startup instruction-loading mechanism must be demonstrated or explicitly accepted as a manual bootstrap; it is not presently verified.

## DEC-000005 — Project-specific overrides

Source: SRC-002 answer 4. Status at Round 1: answered in principle; storage/precedence subsequently resolved by DEC-000010. Affected system: organization, individual projects, and their integration.

Individual projects may have their own overrides. Storage location, ownership, conflict handling, and protected rules were pending at Round 1; DEC-000010 and COVERAGE.md Domain A now provide the delegated disposition. No project receives authority to weaken organization governance merely by having an override.

## DEC-000006 — Provisional intake persistence

Source: SRC-002 answer 5, responding to the precise limited permission requested in Round 1. Status: answered. Affected system: organization.

Authorized now: Markdown discovery, interview, coverage, and draft-contract records inside agent-org/intake/. Not authorized by this permission: operational configuration, executable instrumentation, project edits, migration, or installation implementation. Four approval gates remain mandatory: Requirements Baseline, Scope Contract, Installation Acceptance Contract, and implementation plan.

## Round 2 disposition

SRC-005 accepted recommendations by delegation except the explicit autonomous organization authority and PR policies below. Domain A is resolved at the interview-decision level. Operational controls and initial implementation still require qualification and approval.


## Additional sources

- SRC-005: Operator response: “From now on for all these initialization interview questions, assume that I accept all of your recommendations unless I specify otherwise.” Also explicitly requires fully autonomous recursive organization self-improvement/self-approval conditional on proof of good changes; PRs required for this repo and most managed repos; worktree choice delegated.
- SRC-006: Operator subsequently states the linear-history requirement was removed.
- SRC-007: Read-only GitHub connector discovery: private tclasen/agent-org, repository ID 1428856720, main default, no remote branches, pull/push/triage true and admin/maintain false; initial ruleset required PRs and linear history with merge-only method.
- SRC-008: Read-only GitHub ruleset 25586177 reinspection after SRC-006: linear-history rule absent; deletion/non-fast-forward protections and PR rule remain; zero formal approvals required, review threads must resolve, merge-only, current identity cannot bypass.
- SRC-009: Local CLI help/features and official OpenAI hook/config references; Python version and installed Codex path; details in DISCOVERY.md.

## DEC-000007 — Initialization recommendations delegated

Source: SRC-005. Status: answered. Affected system: organization/project/cross_boundary.

The operator explicitly accepts recommended initialization decisions unless they specify an exception. Use this to complete remaining applicable interview decisions without repeatedly asking routine questions. Record concrete defaults and their tradeoffs; do not fabricate factual answers or operational results. The original explicit approval gates for the concrete baseline/contracts/plan and final acceptance remain intact; this delegation does not pre-approve future test outcomes.

## DEC-000008 — Autonomous recursive organization governance

Source: SRC-005, superseding the proposed operator-as-routine-organization-approver default. Status: answered. Affected system: organization.

The organization autonomously initiates, changes, evaluates, approves, and evolves itself when it can prove the change beneficial within declared evidence scope. Chief of Staff is the approval owner; implementing worker and independent Reviewer are distinct fresh executions. Use pinned baseline, predeclared criteria/workload/budgets, hard guardrails, exact candidate identity, required PR, and rollback. No routine human approval for qualifying organization promotion. Changes to evaluation/promotion logic are themselves evaluated under the previous approved rules. Organization authority still does not authorize product changes or override user/harness constraints.

Proof means reproducible, independently checked evidence appropriate to the claim, with uncertainty retained; it is not a promise of universal correctness. Inconclusive evidence blocks promotion. Shared filesystem access is explicitly not a security-isolated reviewer or tamper-proof evaluator.

## DEC-000009 — PRs and worktrees

Source: SRC-005. Status: answered. Affected system: organization/project/cross_boundary.

Factory changes require PRs. Most projects also require PRs; discover each policy on enrollment. Trunk-based development is compatible with short-lived branches/small PRs. Coordinator autonomously manages suitable worktrees for concurrency, preserving existing resources. Required reviews/gates apply before merge. Subsequent evidence-qualified organization PRs may be approved and merged autonomously through the host's allowed path.

## DEC-000010 — Domain A defaults adopted

Source: SRC-005 delegation of Round 2 recommendations. Status: operator_delegated. Affected system: organization/project/cross_boundary.

Adopt central project override profiles referring to project authorities; no silent weakening of governance, permissions or measurement rules. Project approver remains operator until explicit delegates/grants are registered. One approved parent may cover separately scoped organization/project/integration children. No blanket product integration permission. Separate commits and linked independent review. Use before/after Git and relevant hash evidence with disclosed gaps; technical worker isolation is not an initial requirement. Original protected boundaries remain binding, with no extra unnamed exceptions.

## DEC-000011 — Remaining domains addressed by concrete recommendations

Source: SRC-005. Status: operator_delegated. Affected system: organization/project/cross_boundary.

COVERAGE.md v0.1 contains 318 question-level dispositions across A–Y, including all applicable requested domains. They define model selection, autonomy by operation, tasks/requirements, Git, tests, DORA, security, budgets, triggers, autonomous experimentation, histories and acceptance. Actual unknowns remain unknown; not-yet-enrolled production facts are deferred to enrollment with no live operations authorized. Those choices feed REQUIREMENTS_BASELINE.md, SCOPE_CONTRACT.md, ACCEPTANCE_CONTRACT.md and INSTALLATION_PLAN.md v0.1 for explicit implementation approval.

## DEC-000012 — GitHub merge conflict resolved

Source: SRC-006 and SRC-008. Status: verified. Affected system: cross_boundary.

Operator removed required_linear_history. Read-only ruleset reinspection confirms absence. Required PR, deletion/non-fast-forward protections and merge-only method remain. Earlier discovery of incompatible linear/merge-only settings is historical, not a current blocker. The connected identity reports no admin permission and cannot bypass current rules.

## DEC-000013 — Proposed empty-repository bootstrap

Source: SRC-007 and delegated recommendation. Status: operator_delegated; execution approval pending. Affected system: cross_boundary.

Local main and remote have no commits/branches. Recommend a single empty commit on main solely as PR base, then all content via task PR. This one-time exception is prominently included in the proposed scope and plan, awaiting explicit approval with the installation package. If normal permissions reject it, require administrator bootstrap; never weaken protections or direct-push installation content.

## DEC-000014 — Initial capability limits

Source: SRC-005 delegation and SRC-004/SRC-009 discovery. Status: operator_delegated; acceptance contract approval pending. Affected system: organization/cross_boundary.

Initial core is active-session native collaboration plus durable recovery, explicit command instrumentation, deterministic calculators, synthetic project acceptance and native GitHub CI/PR integration. Exclude always-on execution service, automatic legacy migration, real production telemetry, universal interception, guaranteed model/cost metadata, hostile-worker isolation, and automatic nested-instruction loading in arbitrary root sessions. Use explicit Coordinator startup prompt. These are visible acceptance-contract exclusions, not operational passes; operator approval of the concrete contract and final gap interview remain required.

## Resume checkpoint

All interview choices have explicit answered/verified/operator_delegated dispositions. Review the four v0.1 documents, validate links/IDs/scopes and request explicit implementation approval including exclusions and empty-commit bootstrap. Only intake Markdown may be written until that approval. Next unused decision ID: DEC-000015; requirement IDs REQ-000001–REQ-000040 and AC-000001–AC-000040 reserved; planned capabilities CAP-000001–CAP-000022. No task/run/approval IDs allocated and no operational test run yet.
