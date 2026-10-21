# Installation intake and acceptance

- Target System: organization
- Change Classification: organization
- Authorized Scope: Installation records under agent-org/intake
- Affected Paths or Resources: Approved contracts, interview history and current evidence
- Owning Role: Coordinator
- Related Requirements: REQ-000001 through REQ-000040
- Related Tasks: TASK-000001, TASK-000008
- Approval Requirements: APP-000001; final operator acceptance remains separate

The operator approved the baseline, scope, acceptance contract, implementation plan and exclusions in [APP-000001](../approvals/APP-000001.md). Exact original bytes are preserved in [approved-v0.1](approved-v0.1/INDEX.md); their pending wording is historical. Do not ask for implementation permission again.

Current state: **FULLY_ACCEPTED** under APP-000008; root startup amendment tracked by TASK-000025. See [status](STATUS.md), [results](INSTALLATION_RESULTS.md) and [report](../artifacts/INSTALLATION_REPORT.md).

- [Requirements Baseline](REQUIREMENTS_BASELINE.md): accepted initial requirements; individual durable records live under requirements/.
- [Scope Contract](SCOPE_CONTRACT.md): separate organization/project authority and named integration exceptions.
- [Acceptance Contract](ACCEPTANCE_CONTRACT.md): 22 capabilities, 70 scenarios and approved exclusions.
- [Installation Plan](INSTALLATION_PLAN.md): organization, host integration, instrumentation, DORA and acceptance stages.
- [Discovery](DISCOVERY.md), [interview](INTERVIEW.md) and [coverage](COVERAGE.md): historical evidence and 318 dispositions across Domains A–Y.
- [Original approval review](REVIEW.md): pre-implementation document fingerprints and review package.

Organization self-approval remains autonomous within the explicit grant and evidence controls. It does not grant project writes. PRs remain mandatory; the approved empty bootstrap is complete, and no later content bypass is permitted. old/ remains untouched and uncommitted. Final installation acceptance belongs to the operator after the gap interview.

Current IDs are allocated in [ID_LEDGER](../shared/ID_LEDGER.md), not the historical intake reservations. Open work is in [tasks](../tasks/INDEX.md), with native identities, handoffs and evidence in [runs](../runs/INDEX.md).
