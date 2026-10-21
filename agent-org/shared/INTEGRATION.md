# Adapters, provenance and independent integration

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/INTEGRATION.md
- Affected Paths or Resources: agent-org/shared/INTEGRATION.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Name source/destination repositories/resources, canonical roots/remotes, source authority, approved read/write/event/command permissions, schema/version, identity mapping and known bypass gaps. Link project profile to authoritative existing specs/issues rather than replacing them. No standing blanket integration grant or production service is installed.

Before adapter execution capture input revisions/hashes, expected output/effect and causal IDs; validate/redact/limit imported evidence and retain occurrence/ingestion time and transformation provenance. Reject ambiguous service/environment/commit/deployment attribution rather than infer from proximity. Unknown metadata stays unknown. Direct tool calls/connectors/subagent internals are unobserved unless explicitly imported.

Cross-boundary parent has separate organization/project/integration children with authorities, preservation snapshots and acceptance. Verify adapter success and refusal cases independently of each system's tests. Separate commits and repository identity. Factory root .gitignore/CI are installation-only host exceptions; future integration needs named scope. After PR/merge verify exact revisions and hashes and reconcile each child's obligations.
