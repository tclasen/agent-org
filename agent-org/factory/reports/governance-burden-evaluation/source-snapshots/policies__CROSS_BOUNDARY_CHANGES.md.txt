# Cross-boundary decomposition and acceptance

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/CROSS_BOUNDARY_CHANGES.md
- Affected Paths or Resources: agent-org/policies/CROSS_BOUNDARY_CHANGES.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Coordinator owns the parent intent and names all affected systems/resources. Create separate organization and project children, plus an integration child when adapters, host configuration or evidence transfers cross the boundary. Each child has eight metadata fields, specific requirements, plan, authority, scope, verifier and independent acceptance. Missing approval blocks its own mutations and parent acceptance; another child's success cannot substitute.

Separate commits and repository identities; root integration has its own linked commit/review. Snapshot both protected surfaces, test approved adapter inputs/outputs with causal identities and preserve each requirement set. Independently verify organization behavior, product behavior and integration. A single combined test result is insufficient.

Mandatory boundary checks cover project-to-organization refusal, organization-to-project refusal, ambiguous-target clarification, separate children, independent approvals, separate organization/project verification, adapter evidence, requirement preservation and out-of-scope dependency routing (ACCEPTANCE_CONTRACT X-01 through X-10). Record deliberate negative fixtures distinctly from actual violations. Parent acceptance requires all required children, integration and original intent reconciled.
