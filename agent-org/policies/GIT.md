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
