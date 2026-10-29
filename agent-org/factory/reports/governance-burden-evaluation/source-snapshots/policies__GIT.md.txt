# Git delivery quick reference

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/GIT.md
- Affected Paths or Resources: agent-org/policies/GIT.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Apply CHANGE_CONTROL.md for complete candidate/PR rules. Verify canonical repository root, origin identity, branch/base and dirty/untracked/nested state before any Git write. Preserve user changes and old/ exclusions, stage only owned explicit paths, serialize index writes and respect native restrictions. Project commits remain in independent repositories; root integration is separately scoped.

All factory content requires PR, fresh independent review and valid exact-candidate approval before allowed merge. Inspect current host protections/checks and resolve threads without bypass. Record tested/merged identities and post-merge evidence. Empty-main bootstrap is one approved zero-file exception only, already established; never reuse it for content. No force pushes, silent history changes or staging another worker's paths.

Completion requires the approved change on main at the owning remote, not only on a local branch or a remote feature branch. After normal PR merge, fetch the canonical remote main, record its tip and verify the merge commit is contained (for example git merge-base --is-ancestor <merge-sha> <fetched-main>). Verify approved content equivalence for squash/rebase and required check results. Use a read-only remote/API alternative when fetching is unavailable, with equally explicit content/ancestry evidence. Never assert delivery from a push response, PR creation, local main or a missing merge response. Reconcile remote PR/ref state before retrying an uncertain effect.

During the active task, continue authorized commit/push/PR/review/merge work through verified delivery. Do not leave locally finished work as accepted or defer authorized delivery as optional follow-up. Missing merge authority is a pending blocker, not permission to bypass controls. Project work uses each project’s own main and remote; a parent-repository commit cannot deliver nested project changes.

The standing operator completion directive authorizes the normal commit/push/PR/merge steps for already authorized change scope until the operator directs otherwise. Do not infer a local-only delivery restriction from a request to edit files or clone/clean repositories. Complete the authorized delivery in the same active task. New product scope, deployments, spending, unrelated messages and protection bypass remain outside this standing delivery authorization.

## Worktree lifecycle and cleanup

Creating a task worktree also assigns its cleanup to that task's Coordinator. Record its canonical path, branch, owning task/run and retention reason. Keep worktrees only while needed for active work, undelivered changes, review, or explicit recovery. After verified owning-remote main delivery and release of all users/claims, remove the task worktree during the same session. Reconcile leftovers at startup and shutdown. Delivery and local cleanup are separate outcomes; report any retained worktree's owner, reason and exact next action.

Before removal recheck `git worktree list --porcelain`, the exact checkout's head/status, tracked modifications, untracked and ignored files, pending commits/PRs, nested repositories/submodules and active ownership. A clean checkout or old timestamp alone does not establish that it is unused. Verify the candidate is delivered on the owning remote main, mapping content for squash/rebase merges. A superseded or canceled checkout may be removed only after its disposition is established and unique work is retained in a named durable ref or verified archive; preserve its branch and evidence. Do not delete branches as a side effect of worktree cleanup.

Preserve unique uncommitted files and local-only handoffs outside the retiring worktree in the appropriate authorized repository records or an explicitly recorded recovery archive. Verify hashes and recovery paths before removing originals; temporary files or a stash alone are not durable preservation. Identify ignored files explicitly, distinguishing disposable build caches from unique data. Retain uncertain, locked, active or unfinished worktrees with ownership and next action; never delete another session's resources or expand scope into project data.

Run ordinary `git worktree remove <verified-path>` from the primary or another retained checkout after leaving the retiring directory and releasing its users. Do not use `--force`, recursive directory deletion, reset or clean to defeat a refusal; investigate and preserve the cause. Recheck paths/status immediately before removal. Verify the directory is absent and no longer registered, and that retained worktrees/refs/evidence remain intact. Prune stale administrative registrations only after confirming their directories are already gone and no owner/lock remains. Never remove the primary checkout or the checkout still in use by a worker. A task performing cleanup must also remove its own temporary worktree once delivery is verified and users are released.
