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
