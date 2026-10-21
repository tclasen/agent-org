# Separate scorecards and measurement health

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/SCORECARDS.md
- Affected Paths or Resources: agent-org/shared/SCORECARDS.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Produce separate organization behavior, individual project quality/outcomes and measurement-health views. Include baseline/candidate/evaluator/definition versions, UTC half-open window, as-of snapshot hash, observation time, cohort/denominator/sample counts, missing/invalid/excluded inputs, coverage and limits. Keep prior reports reconstructable; no opaque combined score conceals failures.

Organization indicators: independently labeled routing accuracy with unknown-label coverage, accepted handoffs per attempted delegation including retries/failures, task-class/configuration acceptance/latency/observable total cost, planning coverage/deviations, successful fresh recovery, regression incidents and evaluation outcomes. Per-project indicators: accepted requirements, correctness, security, reliability, maintainability, escaped defects, delivery/rework and user outcomes; DORA requires explicit service telemetry.

Measurement health shows missing events/provenance/links, invalid/corrected/late data, coverage/bypass paths and unknown actual-model/tokens/cost. Unknown costs are not zero. Hard scope/authority/evidence/test/security/acceptance gates dominate soft speed/cost/convenience objectives. Never move denominator/window/history after observing candidate results; adopt changed definitions only through separate prior-evaluator-governed change.
