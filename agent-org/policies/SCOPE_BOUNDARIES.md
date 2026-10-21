# Target classification and scope boundaries

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/SCOPE_BOUNDARIES.md
- Affected Paths or Resources: agent-org/policies/SCOPE_BOUNDARIES.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Before registration or delegation classify intent as organization, project, cross_boundary, clarification_only or status_or_information_only. Ask if a materially ambiguous target changes permissible writes. Clarification/status by itself authorizes no mutation. Substantive research/deliverables still need a task.

Organization means agent-org records, governance and instrumentation. Project means a separately enrolled repository/application and its product sources; it never authorizes policy changes. Cross_boundary means linked changes or obligations in both systems, including host-root integration. Create a parent with independently scoped organization/project/integration children, approvals, evidence and acceptance. A parent plan may cover named children only when its grant explicitly covers them.

Only agent-org is general organization write scope. The installation names .gitignore and .github/workflows/agent-org.yml as separate host integration exceptions, not blanket root authority. No root AGENTS or harness configuration. old/ is read-only reference, never edited/migrated/deleted/staged. Project checkouts retain separate histories/remotes and stay out of the factory index. Scope includes resources and external effects, not only file names.

Establish canonical paths, before/after inventories/hashes and Git state, including untracked/nested changes and explicit unreadable/excluded paths. Resolve traversal/symlink escape before mutation. Shared filesystem claims are procedural coordination, not hostile-worker isolation. Out-of-scope dependencies return to Coordinator as linked work; they never justify silent edits.
