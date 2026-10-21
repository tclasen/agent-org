# Installation approval review — v0.1

- Target System: organization
- Change Classification: organization
- Authorized Scope: Provisional Markdown installation records in /Users/Shared/agent-org/intake/; operational changes require explicit installation approval.
- Affected Paths or Resources: agent-org/intake/; read-only workspace and GitHub discovery.
- Owning Role: Coordinator.
- Related Requirements: REQ-000001 through REQ-000040 in REQUIREMENTS_BASELINE.md (proposed baseline v0.1).
- Related Tasks: Initial installation request; operational task records not yet created.
- Approval Requirements: Recommendations delegated by SRC-005; implementation and final installation acceptance remain explicit operator gates.

## Decision to approve

Approve the [Requirements Baseline](REQUIREMENTS_BASELINE.md), [Scope Contract](SCOPE_CONTRACT.md), [Acceptance Contract](ACCEPTANCE_CONTRACT.md), and [Installation Plan](INSTALLATION_PLAN.md), including stated limitations and the single empty-commit bootstrap exception. This is permission to implement and verify, not final acceptance of results.

## What will be installed

- Eight discoverable roles, durable Markdown requirements/tasks/plans/decisions/approvals/handoffs, and governed multi-repository profiles.
- Autonomous recursive organization changes with predeclared evidence, fresh independent review, Chief of Staff self-approval, exact-candidate gates, PR delivery and rollback. No routine human promotion approval.
- Python standard-library record/scope validation, explicit command/event instrumentation, provenance, deterministic five-metric DORA replay, separate scorecards, and controlled experiment gates.
- Two isolated synthetic project repositories for acceptance; no legacy project migration or modification.
- Root .gitignore and one native GitHub Actions workflow as explicitly scoped cross-boundary integration.

## Material tradeoffs

Autonomy applies while native sessions/workers run; durable records enable later recovery. No separate always-on service is installed. Root-started sessions use an explicit load prompt. Wrapper-based telemetry covers invoked paths, not all tools; actual model/token/cost metadata may remain unknown. Fresh reviewers/worktrees are not hostile-worker isolation or tamper-proof storage. No real production DORA is claimed without enrolled services/data.

## Git status and bootstrap

GitHub PR requirement remains; operator's removal of linear-history requirement was verified. The remote has no branches. Propose one initial zero-file commit on main solely to create a PR base, then all installation content via PR. If ordinary server permissions reject bootstrap, ask an administrator to establish the base rather than bypass protections. No branch-rule settings changes are proposed.

## Checks so far

Only read-only discovery and provisional document checks have run. Package contains 318 interview decisions across 25 domains, 40 requirements, 22 capabilities and 70 planned acceptance scenarios. No operational capability, CI result, model trial, experiment or installation acceptance has been claimed. old remains unstaged/uncommitted.

## Document fingerprints

Approval applies to these exact v0.1 documents; preserve their approved versions before updating result fields.

| Document | SHA-256 |
| --- | --- |
| REQUIREMENTS_BASELINE.md | 04d2636d75ebd72dd28ce65a54ae03c5d1e2d2719783e383d0fd77cbc00bdc56 |
| SCOPE_CONTRACT.md | a2c9c9c267ca8fe4eb40a11f4ad3ac56cc45dca09f131c3c28fa44c9685f0f2c |
| ACCEPTANCE_CONTRACT.md | 9ac84a1c3ed82d3986b20067b5f3e83b2a82f0b67ce13ff5be6c5eb8593571b6 |
| INSTALLATION_PLAN.md | 93a4775e7d0dcaa810ddacf1d07431e1d70d1daa2275ee3f3e1ef478080a5476 |

Operator implementation approval: PENDING. Operator final acceptance after verification and gap interview: PENDING.
