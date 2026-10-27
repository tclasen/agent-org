# Project change admission

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/PROJECT_CHANGES.md
- Affected Paths or Resources: agent-org/policies/PROJECT_CHANGES.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Enroll only with explicit project authority: canonical root, independent repository/remote identity, owner/delegate, authoritative ticket/specification/instructions, permitted commands/events, merge/deployment grants, exclusions and overrides. Keep the complete portable authority/profile in the owning project, with local machine bindings in authorized external runtime state; never create a project pointer under agent-org. Initial installation enrolls no live legacy project.

Admit a project task with exact writable paths/resources, product requirements/acceptance, plan and applicable approval. Snapshot organization instructions/policies before and after project mutation. Project overrides can specialize workflow but cannot expand authority, erase evidence, bypass native restrictions or mutate organization policy. Preserve unrelated and user changes.

Implement/test/review product behavior in the project's own repository. Maintain its own commits/PRs under its policy, and independently accept outcomes using recorded project authority. Organization evaluation cannot replace product verification. A necessary policy/adapter change is a linked organization child, with a cross-boundary parent if both systems change.

Every managed-project change is subject to the organization remote-main completion gate in ACCEPTANCE.md. Admission must identify that project’s canonical remote/main, PR/review/check requirements and merge authority. Overrides cannot waive this completion gate. If a required main branch or merge grant is missing, record the specific blocker before dependent delivery; keep work pending. Track delivery separately for every repository, without treating the organization repository as a substitute.

Record storage follows [record ownership](RECORD_OWNERSHIP.md): organization governance stays here; project-specific records stay in their owning repositories. Do not retain managed-project pointers or installation state here; discover authority from authorized session/project sources.
