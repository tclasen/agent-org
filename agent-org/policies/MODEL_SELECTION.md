# Per-run model and reasoning selection

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/MODEL_SELECTION.md
- Affected Paths or Resources: agent-org/policies/MODEL_SELECTION.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Choose per task/risk/tool/privacy/budget, never by permanent role assignment. Probe current native declarations and required tool support. Baseline recommendation is gpt-6.1-sol/medium for bounded implementation; gpt-6.1-sol/high for complex instrumentation or independent review; gpt-6-astra/high for consequential governance/architecture when justified. Qualified routine trials may use gpt-6-luna/medium. Other advertised models are eligible only with task rationale and supported reasoning level. Prefer minimum sufficient configuration; model diversity cannot establish review independence.

Record task class, rationale, requested model/reasoning, required tools/privacy, invocation parameters/native worker ID, observed support, fallback and actual metadata source in the run before execution. Use fresh workers with fork_turns=none for overrides; supply role/context/task/run paths and minimal manifest explicitly. Actual model/reasoning/token/cost/context capacity remain unknown unless returned by trusted harness metadata. Worker self-report and requested selection are not proof. No prices or quality superiority are assumed.

On unsupported configuration retain exact failure, inspect support, then record a same-authorized-provider/class fallback and recheck capabilities. Weaker tools/privacy/independence require replanning; do not silently substitute. Two explicitly requested configurations must be exercised for installation qualification, preserving metadata gaps. Costs include failed attempts when observable; unknown cost is never zero. No new provider/purchase path is authorized.
