# Identifier allocation ledger

Coordinator serializes allocations; never reuse IDs, including rejected/canceled work. Actual formal definitions plus this ledger are authoritative. Archived references and synthetic fixture namespaces do not allocate live records. Unknown concurrent allocation blocks mutation.

Allocated through: AGENT-000008, DEC-000015, REQ-000042, AC-000042, CAP-000022, WF-000006, TASK-000024, RUN-000025, APP-000007, ART-000005, INIT-000001, INTENT-000001, TRG-000001, EXP-000001, EVAL-000007, FAIL-000016. Failure definitions are in evaluations/FAILURES.md. DEC-000001..14 remain in intake history. EVT-000001..000004 are actual installation stream events; synthetic test events remain separately labeled.
