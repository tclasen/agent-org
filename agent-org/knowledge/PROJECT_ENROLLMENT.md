# Project enrollment guide

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/knowledge/PROJECT_ENROLLMENT.md
- Affected Paths or Resources: agent-org/knowledge/PROJECT_ENROLLMENT.md
- Owning Role: Researcher
- Related Requirements: REQ-000005, REQ-000007, REQ-000042
- Related Tasks: TASK-000018
- Approval Requirements: APP-000001

## Start the Coordinator

Start Codex from the Git repository root. The [root AGENTS.md](../../AGENTS.md) entrypoint loads the organization and initializes the Coordinator, without cd into agent-org or an additional activation prompt. Delegated workers retain their assigned roles. If a client does not load AGENTS.md, explicitly reading the root entrypoint remains a fallback. See [session lifecycle](../shared/SESSION_LIFECYCLE.md).

## Before enrollment

Project enrollment is a record of bounded authority; it does not authorize a project change by itself. Read the organization [authority policy](../policies/AUTHORITY.md), [scope boundaries](../policies/SCOPE_BOUNDARIES.md), [project change policy](../policies/PROJECT_CHANGES.md), [permission policy](../policies/PERMISSIONS.md), and [cross-boundary policy](../policies/CROSS_BOUNDARY_CHANGES.md). Resolve the target, repository identity, and source-of-truth conflicts before any write. Project reads do not grant project writes, and a connected tool is not permission.

The [project registry](projects/INDEX.md) contains minimal identity and routing links for currently managed projects only. Detailed enrollment and authority records live in each owning repository. A registry entry alone grants no project work authority; synthetic qualification fixtures grant no real product authority. Neither an absent entry nor historical records authorize enrolling or resuming an unlisted project; obtain fresh explicit owner authority.

## Enrollment record

Coordinator allocates the project ID and records only identity and authoritative links under `agent-org/knowledge/projects/<project-id>/`. Follow the [routing template](projects/TEMPLATE.md). Store the detailed enrollment task and profile in the owning project repository. That owning record must make these eight scope fields explicit:

1. **Target system** — project, organization, or cross-boundary.
2. **Change classification** — consistent with the target.
3. **Authorized scope** — exact paths, resources, and operations granted.
4. **Affected paths or resources** — all known surfaces the work may touch.
5. **Owning role** — accountable owner.
6. **Related requirements** — canonical requirement IDs.
7. **Related tasks** — task IDs, or none.
8. **Approval requirements** — the applicable grant IDs and approval status.

In the owning project record, retain the project ID, verified local root, repository/remote, ticket/specification references, owner/delegates, scope, environments/commands, protected paths, Git rules, verification baseline, overrides, services and observability gaps. The organization profile links to that authority; it does not duplicate those details. Keep project checkout, records and Git history separate from `agent-org`, following [record ownership](../policies/RECORD_OWNERSHIP.md).

## Authority and work

Record explicit project authority for the exact repository and bounded grant before project writes. An enrollment profile or an approval for another project does not supply that grant. Each project task still needs its own scope, requirements, plan, authority, verifier, and acceptance evidence. Preserve unrelated and user changes.

Overrides may specialize project workflow, but cannot expand authority, erase evidence, bypass native restrictions, or change organization policy. If work changes both organization governance and project sources, classify it as cross-boundary: create separately scoped organization and project children, and an integration child where needed. Each child needs its own authority and independent verification; one child’s approval does not cover another.

Keep project-specific instructions and canonical tickets/specifications in their owning project. A necessary organization profile, policy, or adapter change is separately scoped organization work. Follow project Git rules for product changes and organization Git rules for organization records.

## Removing a project from management

Apply the canonical [project retirement and reusable lessons rule](../policies/RECORD_OWNERSHIP.md#project-retirement-and-reusable-lessons): remove current routing/profile entries, retain reusable lessons by general problem, and verify both before closure. Do not maintain a former-project roster or routinely reconcile past projects. Preserve existing audit evidence and source provenance without treating them as current routing, progress or authority.

## Sources

- [Authority and autonomy](../policies/AUTHORITY.md)
- [Target classification and scope boundaries](../policies/SCOPE_BOUNDARIES.md)
- [Project change admission](../policies/PROJECT_CHANGES.md)
- [Permission and external-effect handling](../policies/PERMISSIONS.md)
- [Cross-boundary decomposition and acceptance](../policies/CROSS_BOUNDARY_CHANGES.md)
- [Project enrollment registry](projects/INDEX.md)
- [Project profile template](projects/TEMPLATE.md)
- [REQ-000007: Project enrollment and overrides](../requirements/cross-boundary/REQ-000007.md)
- [REQ-000042: Source-grounded enrollment guide](../requirements/organization/REQ-000042.md)
- [Installation authorization](../approvals/APP-000001.md)

Startup guidance amended by APP-000008 / REQ-000043; other enrollment authority and project boundaries are unchanged. Prior guide revision and acceptance hashes remain historical evidence.
