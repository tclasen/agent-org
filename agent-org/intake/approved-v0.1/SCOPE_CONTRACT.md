# Scope contract v0.1 — awaiting approval

- Target System: organization
- Change Classification: organization
- Authorized Scope: Provisional Markdown installation records in /Users/Shared/agent-org/intake/; operational changes require explicit installation approval.
- Affected Paths or Resources: agent-org/intake/; read-only workspace and GitHub discovery.
- Owning Role: Coordinator.
- Related Requirements: REQ-000001 through REQ-000040 in REQUIREMENTS_BASELINE.md (proposed baseline v0.1).
- Related Tasks: Initial installation request; operational task records not yet created.
- Approval Requirements: Recommendations delegated by SRC-005; implementation and final installation acceptance remain explicit operator gates.

## Current authority

Only provisional intake Markdown is writable under this interview grant. Discovery reads are authorized throughout /Users/Shared and through the connected GitHub repository tools. The proposed permissions below become installation authority only on explicit approval of this contract, baseline, acceptance contract and plan.

## Systems and path ownership

| System | Paths/resources | Proposed installation writes | Exclusions |
| --- | --- | --- | --- |
| Organization | /Users/Shared/agent-org/ | All organizational instructions, Markdown records, deterministic instrumentation/tests/telemetry, provenance, evaluations and reports | No root AGENTS, no new harness configuration directory, no replacement runtime/service |
| Factory host integration | /Users/Shared/.gitignore; /Users/Shared/.github/workflows/agent-org.yml; factory Git branches/worktrees/PR/CI | Named integration files, atomic commits, task branch pushes, PR, CI verification and reviewed merge | No unrelated root files, no protected-rule bypass or admin policy changes |
| Project acceptance fixtures | Unique task-owned temporary Git repositories under agent-org/factory/artifacts/installation/ or temporary paths, with durable manifests in agent-org | Synthetic source/tests, local fixture Git histories and task-scoped cleanup | No real product repo or external fixture remote mutation |
| Existing projects / old | /Users/Shared/old/** | None during installation | Never stage/commit/migrate/delete old; historical permissions are not inherited |
| Future portfolio | Recommended /Users/Shared/projects/<id>/ and explicit worktree roots | None until separate enrollment/task authorization | Never stage nested projects into outer Git; no automatic migration |
| External identity | github.com/tclasen/agent-org, private, repository ID 1428856720 | After approval: organization task branches, task-related PR content, CI and organization merge through required rules | No settings/admin changes, unrelated issues/messages, production deploy, purchases or new services |

All durable organizational records stay in agent-org; temporary execution artifacts and native Git metadata are not competing organizational record stores. .gitignore and .github/workflows are explicit native integration exceptions, classified cross_boundary. Fixture Git data and telemetry use native formats under the instrumentation exception.

## Approval and autonomy

- Initial installation: operator approves the four named v0.1 documents, including the bootstrap exception below. Operator retains final installation acceptance.
- Subsequent organization work: Chief of Staff can initiate, plan, implement through specialists, independently approve, and promote changes autonomously when preregistered evidence proves benefit within tested scope, guardrails pass, and PR requirements are met. No routine human promotion gate.
- Implementing worker may not be its own Reviewer or approval owner. Use fresh contexts and pinned evidence. Role separation is procedural, not an OS security boundary.
- Project work: requires explicit project task/standing grant; one repository's grant does not cover another. Operator is initial project authority; enrollment can name delegates.
- Cross-boundary work: parent identifies organization, project and integration children, requirements, authority, exact resources, evidence and independent acceptance. One explicit parent approval can cover enumerated children; new scope requires a new grant.
- Project-specific organization profiles live in agent-org/knowledge/projects/<id>/ and refer to canonical project instructions/tickets. A profile cannot silently weaken organization authority/history protections.
- Protected authority, explicit user requirements, security boundaries, and historical evidence cannot be weakened to pass a candidate. Measurement/evaluator changes are separately versioned and accepted under prior rules.

## Git bootstrap exception proposed for explicit approval

The remote has no branches and local main is unborn. PRs need a base. Propose exactly one empty initial commit on main, containing no files, to establish the common base; verify its tree is empty before pushing. Every content change, including installation, then goes through a task branch and PR. This is a narrow exception to PR-only changes, not authority to push implementation directly to main. If GitHub rejects the initial branch creation, do not bypass protections: preserve local work and request administrator bootstrap. Worktrees cannot be assumed usable until a base commit exists.

## Project reads, secrets and writes

All /Users/Shared is readable for relevant work; credential dumps and unnecessary sensitive copies are excluded from records. Use native authenticated tools without copying secrets. Writes outside the named scope require matching approval and actual sandbox permission. No sudo, trust-bypass flags, global tools, background daemon, new paid API or production credentials are required.

## Isolation and evidence

Before/after snapshots include repository identity, current branch/head (or unborn state), staged/unstaged/untracked changes, policy/instruction fingerprints, and relevant ignored/nested files. Do not scan/hash secret contents or massive unrelated caches merely for a boundary claim; define and disclose the evidence boundary. Fixture tests can completely snapshot their small roots; real project scope must name exclusions. Parent Git status alone cannot prove nested repositories unchanged.

Serialized assignment and ID allocation prevent ordinary conflicts within one Coordinator. Multiple simultaneous Coordinators must reconcile claims before writes; Markdown is not atomic locking. Native worktrees isolate Git changes, not credentials or filesystem permissions. Deterministic validators detect supported violations; direct tool paths can bypass wrappers and remain disclosed gaps.

## Protected resources and rollback

Preserve old/, unrelated project files, user modifications, other sessions' resources, secrets, branch protections and authoritative source histories. Cleanup is limited to positively identified temporary fixtures owned by this installation, after durable evidence is retained. Rollback is a reviewed revert PR plus configuration/checkpoint reconciliation; no destructive Git reset or deletion of user work.

## Approval

Operator approval: PENDING. Contract revision: v0.1. Approved hash/time/source: PENDING. No project migration or production grant is included.

