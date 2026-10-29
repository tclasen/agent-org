# Formal record fields and provenance

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/RECORD_FORMATS.md
- Affected Paths or Resources: agent-org/shared/RECORD_FORMATS.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Every formal requirement, task, plan, decision, run, approval, artifact manifest, evaluation, workflow and governed policy record includes these exact metadata lines:

```text
- Target System: organization, project, or cross_boundary; name project identities/systems in separate fields
- Change Classification: organization, project, or cross_boundary
- Authorized Scope: exact granted paths/resources/actions and exclusions
- Affected Paths or Resources: explicit intended surface, including external effects
- Owning Role: one accountable role
- Related Requirements: comma-separated known requirement IDs or none
- Related Tasks: comma-separated known task IDs or none
- Approval Requirements: applicable grant/decision references and conditions
```

Allocated operational records additionally have one '- ID: TYPE-NNNNNN' field (replace placeholder with Coordinator allocation), '- Status: value', source/revision/history, observation time and next action. Policy/index/template documents do not allocate IDs. Role guidance preserves '- Agent ID: AGENT-NNNNNN'; workflow definitions have allocated WF identities. Requirements store source/accepted revision, criterion/evidence/verifier and supersession. Plans retain steps/dependencies/verification/budget/rollback and revision approval. Decisions retain alternatives/reason/authority. Artifact manifests retain location/content hashes, producer run and sensitivity/retention.

Tasks store Original Request, Intended Outcome, Parent, Dependencies, Dependency Type, Responsible Agent, Model Selection, Plan Revision, Plan Approval, Authorized and Claim. Dependencies is 'none' or comma-separated task IDs. Dependency Type names the relation; split mixed relation groups into scoped children or explicit relation records without packing hidden IDs into prose. Store requirements/plan/history/artifacts/blockers/intent reconciliation in clear sections.

Runs store Task, Status, claimed scope/owner/native worker ID, started/checkpoint/ended time, requested model/reasoning/rationale, actual configuration/source or unknown, context manifest/revisions, baseline/candidate/evaluator provenance, cumulative budgets/retries, command/result evidence, side-effect journal and handoff. Missing actual configuration is unknown, never inferred from requested model.

Approvals bind authorized source, approver and independence, plan/task/scope, exact candidate and evidence hashes, evaluator, conditions/expiry/decision/time. Evaluations bind expected/actual criterion outcomes, workload/window/version/snapshot, baseline/candidate, verifier, limits and reject/inconclusive/pass disposition. Machine validation checks structure and references; fresh review establishes semantics. Consult current instrumentation API/help for actual supported checks; do not claim every prose constraint is technically enforced.
