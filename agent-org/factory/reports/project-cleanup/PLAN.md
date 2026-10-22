# Five-project local cleanup plan

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: APP-000012 five clone cleanup scopes and TASK-000048 .gitignore exclusions
- Affected Paths or Resources: Five independent /Users/Shared clones, root .gitignore, scoped agent-org records
- Owning Role: Coordinator
- Related Requirements: none
- Related Tasks: TASK-000041, TASK-000042, TASK-000043, TASK-000044, TASK-000045, TASK-000046, TASK-000047, TASK-000048
- Approval Requirements: APP-000012 direct operator grant; independent local review; organization evidence adoption separately reviewed

- Task: TASK-000041; organization evidence TASK-000042; project children TASK-000043 through TASK-000047.
- Grant: APP-000012, approved direct operator request. Plan revision 1; Coordinator owns execution admission and acceptance.
- Planner run: RUN-000042, native worker `/root/cleanup_plan`; requested gpt-6.1-sol/medium, actual model/reasoning unknown.
- Planner write claim: this file only. No project mutation, staging, commit, remote write, ID allocation or shared handoff write performed by Planner.
- Budget: Planner delegation bounded to ten minutes; execution remains within Coordinator's recorded cumulative task budget.

## Outcome and boundaries

Keep five independent direct clones at `/Users/Shared/{commons,every_game,semantic_search,wired_to_survive,llm-cost-calculator}`. Retire their embedded organization and factory governance so `/Users/Shared/agent-org` is the primary organization. Preserve application behavior, useful project instructions, requirements, safety/privacy constraints, authoritative product records, Git history and each origin remote.

This is local cleanup, not project feature development or permission to resume historical backlogs. No pushes, PR creation, issue/Project changes, workflow dispatch, deployment, paid inference, media intake or legacy `old/` mutation. The organization PR requirement remains a deferred delivery obligation; it does not authorize publishing. No parent root governance or user/global harness changes. Coordinator additionally admits host-integration TASK-000048: add five exact root `.gitignore` directory entries (`/commons/`, `/every_game/`, `/semantic_search/`, `/wired_to_survive/`, `/llm-cost-calculator/`) so nested checkouts cannot enter the parent index. This uses the existing `.gitignore` integration exception; root AGENTS remains untouched. Verify each exact directory is ignored and no parent project files were staged.

## Execution order and evidence

Coordinator executes projects sequentially: commons, every_game, semantic_search, wired_to_survive, llm-cost-calculator. Finish each project's inventory, cleanup and local verification before advancing. Independent Reviewer examines the final pinned candidate, including organization evidence; worker completion is not acceptance.

For each project, before mutation:

1. Confirm canonical directory, Git top level, independent `.git`, origin URL, branch, HEAD, refs and full status including untracked files. Resolve symlinks before deleting anything; never follow an escape into another checkout, parent organization or `old/`.
2. Record baseline commit and tracked-file inventory/content hashes in Coordinator-owned evidence. Baseline must distinguish fresh clone content from any concurrent/user changes. Stop only dependent edits if unexpected changes appear.
3. Read root/nested AGENTS and inspect hidden configuration, workflows, package/manifests, verification entry points, factory/agent-org directories, documentation links and imports. Classify exact paths before removal: embedded governance/tooling, application implementation, mixed product/process guidance, or passive historical evidence.
4. Record an explicit removal/edit allowlist and reason per group. Name matching is insufficient: product factories, simulation agents, application orchestration and data schemas remain unless their content proves they are organization scaffolding.

After mutation, preserve the baseline-to-candidate diff, changed-path list and candidate content identity. `HEAD`, refs, origin and historical objects stay unchanged; do not rewrite history or create commits during this local-only phase. Preserve unrelated files and changes.

## Project-specific work

### TASK-000043 — commons

Observed: Rust simulator application plus a complete embedded `agent-org/` containing governance, records and organization factory instrumentation. README's final paragraph currently points to that directory. No `.github/` was present during inspection.

- Remove the embedded `agent-org/` after confirming its full inventory is organizational, leaving Rust source/tests, technical docs and tools intact.
- Replace the obsolete README paragraph with accurate parent-organization guidance or remove it. Do not touch simulation agent logic or the useful application proxy/viewer/Antithesis tooling merely because it concerns agents/testing.
- Verify no application/build import depends on deleted paths. Unchanged application bytes plus reference checks and `git diff --check` are sufficient for purely organizational removal; run relevant application checks if inspection finds a real executable dependency.

### TASK-000044 — every_game

Observed: no embedded agent-org/factory tree at top level. AGENTS contains extensive useful Rust/Bevy, desktop isolation, testing, product terminology and requirements guidance alongside autonomous task-selection, hierarchy/tracking and remote-delivery instructions.

- Preserve product requirements, technical commands, input/desktop isolation, test/trace/video constraints and product source-of-truth links. Do not alter engine, mods, fixtures or milestone requirements.
- Prepend a narrow parent bridge establishing parent organizational workflow/authority; retain the substantive project-specific technical sections in AGENTS. Do not erase technical guidance to achieve a short AGENTS file.
- State that project work is admitted by the parent organization and current task grants; historical task-selection/remote-integration directions do not trigger work or remote writes in this cleanup. Do not mechanically remove ordinary product acceptance rules.
- Verify preserved links and technical guidance, absence of competing autonomous routing and clean whitespace. No game or GPU run is necessary if application and verification behavior remain byte-identical.

### TASK-000045 — semantic_search

Observed: AGENTS routes to PROJECT.md, which in turn activates `docs/process/{factory,execution,authority,delivery,...}.md`, dispatcher/fresh-lead operation and historical remote completion. No top-level factory directory remains; many historical factory mentions occur in requirements and verification records.

- Inspect active process files and their inbound references individually. Remove standalone `docs/process/{factory,execution,instructions}.md` agent/factory policies and update live Markdown links to the parent AGENTS. Retire embedded factory operating model/agent hierarchy, not the video-search application or its local worker/model scripts.
- Preserve product specifications, requirement IDs/status, current acquisition/retry/privacy/security limits, unresolved dependencies and technical verification commands. Historical grants are project evidence, not current cleanup authorization.
- Make AGENTS/PROJECT clearly defer organization admission and execution to the parent. Retain project authority/delivery/verification/requirements records with a parent precedence notice. Mark historical factory material superseded; preserve domain requirements and evidence without destructive historical record churn. Integrated factory-readiness material may become product-readiness while retaining product criteria and historical evidence. Remove or rewrite live links that would reactivate deleted policies.
- Do not rewrite historical REQ/verification evidence solely to remove the word factory; label history when needed and ensure it is not an active startup route. Verify live relative links and script/import references after retirement.

### TASK-000046 — wired_to_survive

Observed: a substantial embedded factory in `factory/`, `docs/factory/`, scripts, tests and evidence; AGENTS activates it. `.codex/hooks.json` invokes `scripts/factory_hook.py` across lifecycle events and `.codex/config.toml` defines the hierarchy. `scripts/verify.py` runs factory tests/audits and reads vendored catalog provenance. Its manual GitHub workflow invokes that verifier.

- Inventory the entire dependency graph before deletion: `factory/**`, factory-only scripts (`factory.py`, `factory_ops.py`, `factory_hook.py`, `factory_runtime/**`, audits/queue adapters where confirmed factory-only), dedicated factory/queue tests, docs, hook/config references, issue templates, README and THIRD_PARTY entries.
- Preserve Rust game/replay code, scenarios, deterministic traces, video verification, technical planning, licenses and any retained third-party attribution. Preserve project backlog JSON under `docs/design/` before removing the factory tree; retain IDs and provenance, without recreating an organization. Remove factory-only scripts/tests/evidence while retaining product evidence.
- Retire lifecycle hook registrations with their handlers to avoid dangling commands. Coordinator resolved applicability: project-local `.codex` hooks/config solely implementing this factory are within the user's explicit factory-removal grant. Retire those files; do not edit user/global/parent harness settings or leave broken active hooks.
- Refactor `scripts/verify.py` to remove only factory-specific commands and catalog checks together with removed tooling. Preserve Rust format/lint/build/tests, replay repeats, negative scenarios, source/binary identity, output manifests and video/frame integrity checks. Inspect `tests/verification/test_evidence.py` imports before retaining/removing; preserve product evidence tests.
- Remove obsolete live links and factory-only workflow/template content. Retain a product verification workflow only if it references surviving product checks; no dispatch or remote edit occurs.
- Verify remaining Python scripts parse, surviving relevant evidence tests pass, verifier command paths exist and no factory imports remain. Use affected product checks and local syntax/reference checks; record any unavailable Rust/GPU dependency honestly. Do not claim full game verification from factory retirement checks.

### TASK-000047 — llm-cost-calculator

Observed: AGENTS is predominantly data architecture and testing requirements, plus a standing commit/push/deploy directive. No top-level embedded organization/factory directory observed.

- Preserve data ownership, inventory generation, user-input migration, estimation labels and complete buy/rent/API behavior requirements. Keep application data, JS/build tooling, tests and CI/deployment definitions that serve the product.
- Prepend the narrow parent organization bridge establishing organizational workflow/authority precedence; preserve substantive AGENTS project guidance. The bridge makes clear the current task has no remote-delivery authority and historical completion directives do not initiate push/deployment. Do not delete AGENTS or its useful technical requirements wholesale.
- If only instructions change, verify links and whitespace; unchanged application/CI bytes are the preservation evidence. If any executable product tooling changes unexpectedly become necessary, re-evaluate scope and run `npm test` and `npm run build` as applicable.

## Acceptance, review and rollback

Coordinator records for every project: baseline SHA/origin/refs/status; classified exact removals; edited live references; hashes of retained application files; commands and actual results; candidate status/diff; limits and any unresolved ambiguity. Search all retained tracked/hidden files for deleted path names, organization startup directives, hook commands, factory imports and workflow/script callers. Classify each residual match as safe historical/product context or repair a live dependency. A zero count of the word factory is not the acceptance criterion.

Acceptance requires five distinct checkouts at exact paths with unchanged history/remotes; parent organization is the sole active organization route; no live dangling governance links/hooks/imports/checks; useful technical/product/privacy guidance preserved; and diffs limited to approved scaffolding retirement and necessary integration repairs. `git diff --check` must pass in every changed project. No unapproved external effects. Independent Reviewer checks pinned diffs and evidence under APP-000012 before Coordinator accepts local cleanup. Remote delivery remains explicitly deferred.

Rollback is selective restoration of task-owned tracked paths from each recorded baseline, plus removal of task-created files only. Never use a broad hard reset/clean or restore over unrelated changes. Baseline history retains all removed tracked scaffolding; do not create duplicate project archives.

## Planner handoff

Completed: required organization/Planner policies, tasks 41–47, run 42 and approval 12 read; all five clone top-level inventories inspected; selected AGENTS/PROJECT, wired hook/config/verifier/workflow and calculator manifest inspected; plan written only here. Git root status showed Coordinator-owned task/run/approval updates and fresh clones, not a clean root; preserved without alteration. No project edits or remote effects by Planner. Initial targeted search reported absent commons/every_game `.github` directories; this is an observed absence, not a failed cleanup.

Next action: Coordinator pin each clone baseline, apply the sequential allowlisted cleanup and exact clone ignores, then delegate a fresh independent review. Coordinator resolved wired project-local hook retirement and supplied the final semantic policy-retirement boundary before this plan finalized. Unknowns: complete factory dependency graph, exact project removal sets, surviving product-test availability and final candidate identities are execution evidence, not asserted by this plan.
