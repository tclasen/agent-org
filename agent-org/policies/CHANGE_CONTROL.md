# Candidate identity, Git and promotion control

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/CHANGE_CONTROL.md
- Affected Paths or Resources: agent-org/policies/CHANGE_CONTROL.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

All factory content uses short-lived scoped branches and PRs; only the explicitly approved empty-main bootstrap exception establishes the initial base. Respect remote protections and review-thread resolution, never force-push or bypass. Inspect current rules at use time. Separate organization, project and root integration commits and keep repository identities explicit.

Before mutation inspect dirty/untracked/nested state and ownership. Stage only known owned paths; never old/ or independent checkouts. Prefer task worktrees, verify path/branch/status and preserve others' resources. Concurrent disjoint edits in one checkout require Coordinator path ownership; staging/commit operations remain serialized. Approved atomic commits use Conventional Commits where appropriate.

Pin base/head/tree, dirty inventory, input/instruction/policy/evaluator hashes and evidence provenance. PR description states problem/result, requirements, scope, validation, exact tested candidate and limits. Fresh review plus independent approval binds that candidate. Changed head invalidates approval. Pass relevant current/candidate regression and host checks before allowed merge; no organization rule can waive host protection. Verify merged revision/content/checks and reconcile tasks afterwards. Roll back through a scoped corrective/revert PR from a known-good revision, preserving failed evidence and active-run reconciliation.
