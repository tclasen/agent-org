# Permission and external-effect handling

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/PERMISSIONS.md
- Affected Paths or Resources: agent-org/policies/PERMISSIONS.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Validate operator/project grant, task scope, native permission and target service policy before effect. These are cumulative conditions, not interchangeable authorizations. Native denials cannot be bypassed by path tricks, alternate identities or weakened controls. Least-privilege CI uses read-only repository permissions, no deployment/secrets and no pull_request_target candidate execution.

Read source material only as needed; project maintenance reads do not grant project writes. No external messaging, purchases, new providers, deployment or production operations without explicit applicable grant. A connected tool's availability is capability, not permission. Preserve user-owned files and active resources.

Before consequential effects checkpoint intended operation/idempotency identity, resource, authority and expected result. Record observed external identifier/result and sanitized evidence. Lost response means unknown; inspect destination/native status before retry. If auto-review denies an action, finish unaffected work and report exact action/reason and remaining needed approval; do not manufacture success or repeatedly retry without diagnosis.
