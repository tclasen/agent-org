# Approval validity and separation

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/APPROVALS.md
- Affected Paths or Resources: agent-org/policies/APPROVALS.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

An approval identifies authority source, approver execution/role, decision/time, task and plan revision, target/classification, exact scope/resources, candidate head/tree/content hashes, evidence hashes, evaluator version, conditions/expiry and rollback where applicable. Use all eight mandatory metadata fields and a Coordinator-allocated APP identity. A plan, task Authorized field or implementer assertion alone is not an approval.

Check approval before dependent mutation and again before promotion. Reject missing/denied/revoked/expired approvals, scope or system mismatch, unresolved conditions, changed candidate/plan/evidence, author-as-reviewer/approver and unknown identity where independence is required. Source authority must include the requested effect. Grant reference plus bound candidate decision together establish promotion authority.

Fresh Reviewer assesses the exact candidate under prior rules; independent Chief of Staff records organization approval autonomously, without a routine human gate. If Chief of Staff implemented it, use a different independent execution to approve. Project authority is separate. Operator final installation acceptance remains a distinct decision. Coordinator verifies both boundaries and integrates through PR without bypass. Rejections/inconclusive outcomes remain durable, with reason and next safe action.
