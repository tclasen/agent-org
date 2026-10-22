# Observed worktree cleanup results

2026-10-22T02:16:57.456117+00:00

- Removed `/private/tmp/agent-org-progressive-disclosure` with ordinary `git worktree remove`; HEAD `05ebfd82d2ae28a9f62bd6563c22fe8a618a847f` retained in its original local branch; directory absent and registration absent.
- Removed `/private/tmp/agent-org-progressive-disclosure-reconciled` with ordinary `git worktree remove`; HEAD `67c61bf20f3f848d6c7afe8614fed0d9998967bb` retained in its original local branch; directory absent and registration absent.
- Removed `/Users/Shared/autonomy-research` with ordinary `git worktree remove`; HEAD `7090312e1bfd64cf1580d42414bf3eee429c5425` retained in its original local branch; directory absent and registration absent.
- Removed `/Users/Shared/commons-video-org` with ordinary `git worktree remove`; HEAD `d4e7769cb02f823040783e360c5387168c3a806a` retained in its original local branch; directory absent and registration absent.
- Removed `/Users/Shared/tessl-research` with ordinary `git worktree remove`; HEAD `2b3560fa082e8ffa7f552d57d4cd5ba93600fc2d` retained in its original local branch; directory absent and registration absent.

All five local branches and exact heads remain intact. No force, reset, clean, branch deletion or stale-registration pruning used. Only Tessl's hash-verified, committed note was removed separately from its original checkout. Ignored Python caches were disposable.

Retained unfinished worktrees `/Users/Shared/autonomy-implementation` and `/Users/Shared/project-demos-org` without modifying their contents or refs. Primary checkout and shared ledger reservations retained. This task's own worktree remains temporarily until verified delivery and reviewer release; its final removal is reported in the session handoff.

Post-removal registrations:

```text
/Users/Shared                           e08e2ff [main]
/private/tmp/agent-org-worktree-cleanup 5a4f5c7 [chore/worktree-lifecycle]
/Users/Shared/autonomy-implementation   e4ecd58 [feat/autonomy-workflow]
/Users/Shared/project-demos-org         9b09a46 [verify/all-project-demos]
```
