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

From `/Users/Shared`, start a Codex session and request: “Read agent-org/AGENTS.md, initialize the Coordinator, reconcile open work and interrupted runs, and report the next authorized action.” This explicit loading step is required; merely starting at the workspace root does not automatically load nested instructions. See [session lifecycle](../shared/SESSION_LIFECYCLE.md).

## Before enrollment

Project enrollment is a record of bounded authority; it does not authorize a project change by itself. Read the organization [authority policy](../policies/AUTHORITY.md), [scope boundaries](../policies/SCOPE_BOUNDARIES.md), [project change policy](../policies/PROJECT_CHANGES.md), [permission policy](../policies/PERMISSIONS.md), and [cross-boundary policy](../policies/CROSS_BOUNDARY_CHANGES.md). Resolve the target, repository identity, and source-of-truth conflicts before any write. Project reads do not grant project writes, and a connected tool is not permission.

The [project registry](projects/INDEX.md) currently records no real product repository as enrolled. The factory repository is organization infrastructure; synthetic repositories support qualification only. Neither grants authority to migrate a legacy or product repository.

## Enrollment record

Coordinator allocates the project ID and records a Markdown profile under `agent-org/knowledge/projects/<project-id>/`. Follow the [project profile template](projects/TEMPLATE.md). At minimum, the enrollment task and profile must make these eight scope fields explicit:

1. **Target system** — project, organization, or cross-boundary.
2. **Change classification** — consistent with the target.
3. **Authorized scope** — exact paths, resources, and operations granted.
4. **Affected paths or resources** — all known surfaces the work may touch.
5. **Owning role** — accountable owner.
6. **Related requirements** — canonical requirement IDs.
7. **Related tasks** — task IDs, or none.
8. **Approval requirements** — the applicable grant IDs and approval status.

Also record the allocated project ID, verified canonical local root, repository identity and remote, authoritative ticket/board and specification references, owner and delegates, permitted environments and commands, protected paths, Git/PR rules, verification commands and baseline, project overrides, service mappings, and observability gaps. Use the profile as a pointer to those authorities; do not copy requirements that could diverge. Keep the project checkout and Git history separate from `agent-org`.

## Authority and work

Record explicit project authority for the exact repository and bounded grant before project writes. An enrollment profile or an approval for another project does not supply that grant. Each project task still needs its own scope, requirements, plan, authority, verifier, and acceptance evidence. Preserve unrelated and user changes.

Overrides may specialize project workflow, but cannot expand authority, erase evidence, bypass native restrictions, or change organization policy. If work changes both organization governance and project sources, classify it as cross-boundary: create separately scoped organization and project children, and an integration child where needed. Each child needs its own authority and independent verification; one child’s approval does not cover another.

Keep project-specific instructions and canonical tickets/specifications in their owning project. A necessary organization profile, policy, or adapter change is separately scoped organization work. Follow project Git rules for product changes and organization Git rules for organization records.

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
