# Discovery evidence

- Target System: organization
- Change Classification: organization
- Authorized Scope: Provisional Markdown discovery, interview, coverage, and draft-contract records in /Users/Shared/agent-org/intake/ only.
- Affected Paths or Resources: /Users/Shared/agent-org/intake/; read-only discovery of /Users/Shared.
- Owning Role: Coordinator (current installation session).
- Related Requirements: Operator installation specification; approved baseline not yet established.
- Related Tasks: Installation request in this conversation; operational task registration awaits implementation authorization.
- Approval Requirements: Provisional intake records authorized by operator answer 5. Requirements Baseline, Scope Contract, Installation Acceptance Contract, and implementation plan require explicit approval before implementation.

Observed: 2026-10-21. This document separates local observations from tool-advertised capabilities and unverified proposals.

## Organization capability discovery

| Capability | Evidence / disposition |
| --- | --- |
| Existing outer organization | No /Users/Shared/AGENTS.md or agent-org/ existed at discovery; no AGENTS.md at / or /Users either |
| Historical organizations | old/factory and old/projects/factory describe Copier templates; old/work/factory describes a separate sandbox orchestration application |
| Instruction hierarchy | Nested AGENTS.md files exist in historical projects; new organization's automatic loading from sessions rooted above agent-org is not verified |
| Fresh agents and independent contexts | Native collaboration.spawn_agent declares fork_turns=none; not yet exercised |
| Model overrides | Tool advertises gpt-6.1-sol, gpt-6-astra, gpt-6-sol, gpt-6-luna, gpt-5.6-sol; fresh-context overrides supported by declaration; no execution validation yet |
| Reasoning controls | Model-specific levels low through high/xhigh/max, with ultra on several models, exposed in tool declarations; not yet tested |
| Parallelism | Four agent slots including root; shared filesystem; no isolation implied by independent contexts |
| Nonblocking interaction | Asynchronous user questions, collaboration messaging, and background Codex task tools exposed; not yet tested as installed workflow |
| Worktrees | Native worktree tools and Git executable available; no worktree operation performed |
| Session independence | Task/thread persistence tools exposed; durable execution after session termination is not demonstrated |
| Scheduling | macOS crontab/launchctl executables present; a Sites-specific schedule connector exists; no general approved agent scheduler established or inspected |
| Hooks / interception | No active outer Git hook files observed, core.hooksPath unset; local CLI now reports hooks enabled; registration/trust and coverage in this session remain unverified |
| Tool integrations | GitHub, Pages, Sites, and other connectors advertised; enrollment-specific authentication/permissions untested |
| Actual model / tokens / cost | Availability of authoritative per-run metadata unverified |
| Permission enforcement | Session sandbox restricts writes to workspace/temp with protected paths; network restricted; approval review applies to escalation. Markdown is not an access-control mechanism |

## Project capability discovery

- /Users/Shared is an existing Git root on unborn branch main, with zero tracked files and no commits. Git status initially reported only untracked old/. Remote name origin is configured; destination/access subsequently inspected below.
- The visible working tree initially consisted of old/, containing projects/, work/, factory/, factory-eval-workspaces/, factory-evals-workspaces/, agent-collaboration/, and agent-handoffs/.
- Many first-level directories in old/projects/ and old/work/ have their own .git marker. Each is a candidate future enrollment, not an already authorized managed project.
- No standard root CI files or application manifests found. Root has no established build, application tests, deployment identity, production history, or DORA semantics.
- Git, Python 3, Node/npm, Go, Cargo, Make, Docker, GitHub CLI, Codex, crontab, and launchctl executables were located. Versions, credentials, services, and health were not inferred from executable presence.
- Existing project requirements, tests, CI, production classifications, ticket-system authority, security controls, and measurement systems must be discovered per enrollment. No nested project's historical operational claims are adopted as current verification.

## Historical references inspected

| Reference | Relevant lesson / incompatibility |
| --- | --- |
| old/factory/AGENTS.md and README.md | Python fixture tests, protected independent evaluation, explicit evidence limits, template adoption/update and hook composition; root AGENTS/.factory/.agents installation conflicts with new namespace constraints |
| old/projects/factory/AGENTS.md and README.md | Preserve each project's existing task source; behavioral claims need measured evidence; automatic commit/push policy is historical and not inherited |
| old/work/factory/AGENTS.md and README.md | Provenance, scope discipline, independent verification, and recovery lessons; Kubernetes/service/controller architecture conflicts with no separate harness/daemon requirement |

Only selected sections were inspected; this is not an exhaustive audit of these repositories. No historical test or deployment was run.

## Candidate integration points — not implementation authorization

- Per-repository identity and ticket-source mappings inside agent-org with explicit project enrollment.
- Read-only Git provenance, working-tree inventories, instruction and artifact fingerprints.
- Approved project build/test wrappers and CI event imports.
- Project-specific delivery/failure/recovery event sources once their semantics are approved.
- Existing project instructions referenced with defined override precedence.

## Material gaps and conflicts

1. Sessions start at /Users/Shared while organization instructions must remain below agent-org/. Establish a tested explicit bootstrap or a permitted native loading mechanism without creating root AGENTS.md.
2. Independent repositories must not be accidentally staged into the outer factory repository. Decide checkout layout and exclusion strategy before enrollment.
3. Per-project overrides must coexist with protected organization-wide governance and separately authorized project changes.
4. Native fresh agents share the filesystem; review independence and access isolation require distinct evidence.
5. Durable Markdown supports recovery, not autonomous execution or atomic task locking.
6. Production deployment/failure definitions, historical data, and actual observability coverage are unknown. Synthetic tests cannot establish production metrics.
7. Legacy instructions conflict about Git workflows and infrastructure. Adopt useful lessons only through the new approved contracts.

## Discovery commands and limitations

Used bounded directory listings; file-name searches; selected Markdown reads; shutil.which; git --no-optional-locks rev-parse, symbolic-ref, ls-files, status, remote (names only), config --get core.hooksPath, and log. Initial broad filename enumeration was too large, so follow-up inspection was narrowed. rev-parse HEAD and log returned the expected errors for an unborn repository. No secrets/configuration dumps, Git fetch/push, installations, migrations, or operational test commands were run. Read-only GitHub metadata was subsequently inspected below.


## Follow-up discovery after delegated interview decisions

- Origin is https://github.com/tclasen/agent-org.git. GitHub metadata reports private repository 1428856720, default main, size zero and no branches. Connector permissions: pull/push/triage true, maintain/admin false. No active managed worktrees returned.
- Ruleset 25586177 initially required both linear history and PRs allowing only merge commits. Operator removed linear history; reinspection confirms it is absent. Current rules protect deletion/non-fast-forward changes and require PRs; zero formal approvals, review-thread resolution required, merge-only; current connection cannot bypass. This supports procedural agent approval without a required human GitHub review, subject to actual merge/CI validation.
- Local Python is 3.15.0. Codex executable resolves to installed 0.163.0 path. CLI help supports native exec, model selection, workspace sandbox, worktrees and JSON event output. CLI help emitted a warning that optional PATH-alias creation was denied; commands returned help successfully. No successful installation/configuration write is inferred.
- Local feature listing reports hooks enabled. Official documentation describes lifecycle hooks discovered from active configuration layers and requiring trust for changed non-managed hook definitions. This is advertised support, not active instrumentation in this organization. [Official hooks reference](https://learn.chatgpt.com/docs/hooks).
- The configuration reference describes model_instructions_file as replacing built-in instructions; do not use it as a casual additive organization bootstrap. The selected initial design uses an explicit load prompt. [Official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).
- No namespace-compatible automatic hook activation or complete observation of tools/subagents has been demonstrated; core acceptance uses explicit instrumentation with a coverage report. No new global or harness configuration is proposed.

Read-only GitHub evidence endpoints: [repository](https://github.com/tclasen/agent-org), [current ruleset](https://github.com/tclasen/agent-org/rules/25586177). GitHub facts are snapshots, to recheck before mutation.

## Additional historical lessons (reference-only)

Read selected measured-process-improvement, qualified-artifact-promotion, protected-acceptance and persistent-state-recovery controls in old/projects/factory_catalog, plus old/factory/docs/task-state-workflows.md. Relevant lessons: predeclare comparisons and retain failures, bind approval to exact artifact, distinguish fresh reviewer from technical isolation, and reconcile state before retry. No old runtime or approval is adopted. Source revisions observed: old/factory bfd0ba68d4cc078f157f4461d0565eb919b3264d; old/projects/factory d805db18ea05199ae5bde42242119c355b16bef3; old/work/factory 2c1fb6c7c3180ae9c1f5deb8f1f514abc462bb44; old/projects/factory_catalog 8ed6618f173cfebc464e2268a9dd3a35386449ee. Dirty-state equivalence was not established, so these hashes identify repository heads, not exact inspected file snapshots.

Initial production/history discovery is complete for the empty factory: none exists there. Archived projects remain future enrollments and have not been exhaustively audited. Future enrollment must discover each project's build/tests/CI/deployment/observability/requirements/security before any corresponding task executes.

