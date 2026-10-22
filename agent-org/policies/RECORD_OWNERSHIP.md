# Record ownership

- Target System: organization
- Change Classification: organization
- Authorized Scope: organization record storage and routing rules
- Affected Paths or Resources: organization governance and links to separately owned records
- Owning Role: Chief of Staff
- Related Requirements: REQ-000056
- Related Tasks: TASK-000151, TASK-000157
- Approval Requirements: APP-000109 user instruction; independent review and Chief of Staff decision before promotion

Keep agent-org governance, role definitions, policies, organization evaluations and coordination records in agent-org. The owner permits organization-related content to be pushed to its public repository through the normal protected PR workflow.

Store project specifications, project task/run/approval details, progress, tests, experiment results, model-run records and evidence metadata in the owning project's repository. Push them only to that repository under its own authority and protections. Mixed records must be split by ownership before publication; never copy another project's details into an unrelated repository.

The organization may retain minimal identity/routing pointers and allocation reservations needed to locate external canonical records. A forwarding entry is not a project specification, operational state, approval or source of authority. The canonical project record controls its own history and current state. Organization record status must not be confused with product acceptance.

Retain immutable source provenance and original recovery evidence during migration. Preserve failures, requirements, unknowns and acceptance boundaries. Do not publish private project content in the organization branch's ancestry: start a filtered publication from already-public main rather than pushing unpublished mixed-history ancestors. Preserve existing public history; no force push or history rewrite is authorized.

Before delivery, independently check both current content and newly introduced history, per-project provenance/ownership, links and normal owning-main delivery. A changed content split invalidates the affected earlier mixed-candidate approval. Publication authorization for one repository does not authorize a new inference payload, provider, deployment or unrelated external destination.
