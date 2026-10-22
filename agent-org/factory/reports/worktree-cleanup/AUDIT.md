# Worktree cleanup inventory and disposition

Observed 2026-10-22T02:16:09.382166+00:00

Owning repository: https://github.com/tclasen/agent-org.git. Fetched main: 9b09a46cd683793b2046a3bfe9fe014d71e2a508. Remote PR list confirms PR9/10/13/14 merged and PR12 closed, superseded by PR13. Current plan TASK-000095 revision 1; explicit operator grant APP-000026.

## /private/tmp/agent-org-progressive-disclosure

Remove: PR12 closed and explicitly superseded by merged PR13; retain branch docs/progressive-disclosure and all its unmerged commits.

HEAD: `05ebfd82d2ae28a9f62bd6563c22fe8a618a847f`

Branch: `docs/progressive-disclosure`

Status:

```text
## docs/progressive-disclosure...origin/docs/progressive-disclosure
```

Ignored: 17 files; all disposable Python bytecode caches.

## /private/tmp/agent-org-progressive-disclosure-reconciled

Remove: candidate delivered by merged PR13; HEAD ancestor of fetched origin/main.

HEAD: `67c61bf20f3f848d6c7afe8614fed0d9998967bb`

Branch: `docs/progressive-disclosure-reconciled`

Status:

```text
## docs/progressive-disclosure-reconciled...origin/docs/progressive-disclosure-reconciled
```

Ignored: 17 files; all disposable Python bytecode caches.

## /Users/Shared/autonomy-research

Remove: candidate delivered by merged PR10; HEAD ancestor of fetched origin/main.

HEAD: `7090312e1bfd64cf1580d42414bf3eee429c5425`

Branch: `research/autonomous-factories`

Status:

```text
## research/autonomous-factories...origin/research/autonomous-factories
```

Ignored: 17 files; all disposable Python bytecode caches.

## /Users/Shared/commons-video-org

Remove: candidate delivered by merged PR14; HEAD ancestor of fetched origin/main.

HEAD: `d4e7769cb02f823040783e360c5387168c3a806a`

Branch: `docs/commons-demo-video`

Status:

```text
## docs/commons-demo-video...origin/docs/commons-demo-video
```

Ignored: 1 files; all disposable Python bytecode caches.

## /Users/Shared/tessl-research

Remove: candidate delivered by merged PR9; HEAD ancestor of fetched origin/main; unique note archived verbatim before removal.

HEAD: `2b3560fa082e8ffa7f552d57d4cd5ba93600fc2d`

Branch: `research/tessl-factory`

Status:

```text
## research/tessl-factory...origin/research/tessl-factory
?? agent-org/factory/reports/tessl-research/DELIVERY_HANDOFF.md
```

Ignored: 17 files; all disposable Python bytecode caches.

## /Users/Shared/autonomy-implementation

Retain: unfinished autonomous workflow commits, no merged delivery PR observed; HEAD not contained in fetched main and branch advanced during this session.

HEAD: `e4ecd58c05dafd7b95ba80081ed8423726f83b4f`

Branch: `feat/autonomy-workflow`

Status:

```text
## feat/autonomy-workflow...origin/feat/autonomy-workflow [ahead 1]
```

Ignored: 29 files; all disposable Python bytecode caches.

## /Users/Shared/project-demos-org

Retain: active task reservations and dirty/untracked requirement/task/run records for unfinished demo verification.

HEAD: `9b09a46cd683793b2046a3bfe9fe014d71e2a508`

Branch: `verify/all-project-demos`

Status:

```text
## verify/all-project-demos...origin/main
 M agent-org/knowledge/projects/INDEX.md
 M agent-org/knowledge/projects/commons/PROFILE.md
 M agent-org/requirements/INDEX.md
 M agent-org/runs/INDEX.md
 M agent-org/shared/ID_LEDGER.md
 M agent-org/tasks/INDEX.md
?? agent-org/approvals/APP-000024.md
?? agent-org/factory/reports/project-demos/
?? agent-org/knowledge/projects/every_game/
?? agent-org/knowledge/projects/llm-cost-calculator/
?? agent-org/knowledge/projects/semantic_search/
?? agent-org/knowledge/projects/wired_to_survive/
?? agent-org/requirements/cross-boundary/REQ-000054.md
?? agent-org/runs/RUN-000080.md
?? agent-org/runs/RUN-000081.md
?? agent-org/runs/RUN-000082.md
?? agent-org/runs/RUN-000083.md
?? agent-org/runs/RUN-000084.md
?? agent-org/runs/RUN-000085.md
?? agent-org/runs/RUN-000086.md
?? agent-org/runs/RUN-000087.md
?? agent-org/runs/RUN-000088.md
?? agent-org/tasks/cross-boundary/TASK-000085.md
?? agent-org/tasks/organization/TASK-000091.md
?? agent-org/tasks/organization/TASK-000092.md
?? agent-org/tasks/organization/TASK-000093.md
?? agent-org/tasks/organization/TASK-000094.md
?? agent-org/tasks/project/TASK-000086.md
?? agent-org/tasks/project/TASK-000087.md
?? agent-org/tasks/project/TASK-000088.md
?? agent-org/tasks/project/TASK-000089.md
?? agent-org/tasks/project/TASK-000090.md
```

Ignored: 0 files; none.

## /Users/Shared

Retain: primary checkout and shared ledger reservations owned across sessions.

HEAD: `e08e2ff512d9b7f5abc799aa7bace75492b919b7`

Branch: `main`

Status:

```text
## main
 M agent-org/shared/ID_LEDGER.md
?? autonomy-implementation/
?? autonomy-research/
?? commons-video-org/
?? project-demos-org/
?? tessl-research/
```

Ignored: 113 files; 96 non-bytecode paths; retained without mutation.

## /private/tmp/agent-org-worktree-cleanup

Retain until this task delivers, then remove after all reviewers release this checkout.

HEAD: `9b09a46cd683793b2046a3bfe9fe014d71e2a508`

Branch: `chore/worktree-lifecycle`

Status:

```text
## chore/worktree-lifecycle...origin/main
 M agent-org/approvals/INDEX.md
 M agent-org/policies/GIT.md
 M agent-org/runs/INDEX.md
 M agent-org/shared/ID_LEDGER.md
 M agent-org/shared/SESSION_LIFECYCLE.md
 M agent-org/tasks/INDEX.md
?? agent-org/approvals/APP-000026.md
?? agent-org/factory/reports/worktree-cleanup/
?? agent-org/runs/RUN-000089.md
?? agent-org/runs/RUN-000090.md
?? agent-org/runs/RUN-000091.md
?? agent-org/tasks/organization/TASK-000095.md
?? agent-org/tasks/organization/TASK-000096.md
?? agent-org/tasks/organization/TASK-000097.md
```

Ignored: 0 files; none.

## Preservation and limitations

The Tessl unique untracked note is copied verbatim to [tessl-delivery-handoff.md](tessl-delivery-handoff.md), SHA256 `d09301e805758243ad2403644d3fdbc815902e1e286e833dcd930178d0ec5fd9`. It must be committed to this retained branch before removing its original. Original absolute path: /Users/Shared/tessl-research/agent-org/factory/reports/tessl-research/DELIVERY_HANDOFF.md. Retain every local branch, including superseded PR12; no branch deletion is requested.

Eligible checkouts have no tracked changes or nested Git/submodule repositories; their only ignored files are disposable Python bytecode. No current-work claim remains for merged/superseded tasks in their recorded delivery handoffs/PR outcomes. Native process listing was denied by the sandbox; no claim of exhaustive host-process visibility. Unfinished/advancing resources are retained. This cleanup does not resume their work or close their tasks. Root shared ledger reservations are preserved, with only this task's appended reservation.

Initial plain git worktree creation failed because .git is sandbox protected; the normal approved escalation succeeded. Plain gh network inspection was unavailable; approved escalation and the GitHub connector supplied remote-state evidence. No bypass or force removal is used.
