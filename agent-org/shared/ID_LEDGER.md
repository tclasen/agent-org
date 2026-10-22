# Identifier allocation ledger

Coordinator serializes allocations; never reuse IDs, including rejected/canceled work. Actual formal definitions plus this ledger are authoritative. Archived references and synthetic fixture namespaces do not allocate live records. Unknown concurrent allocation blocks mutation.

Allocated through: AGENT-000008, DEC-000015, REQ-000051, AC-000048, CAP-000022, WF-000006, TASK-000062, RUN-000056, APP-000015, ART-000005, INIT-000001, INTENT-000001, TRG-000001, EXP-000001, EVAL-000007, FAIL-000016. Failure definitions are in evaluations/FAILURES.md. DEC-000001..14 remain in intake history. EVT-000001..000004 are actual installation stream events; synthetic test events remain separately labeled.

Research admission reconciled merged REQ-000050, TASK-000054..56 and RUN-000048..50 omitted by the prior ledger checkpoint. New research allocations are serialized in this worktree; workers allocate no IDs.

APP-000015 is reserved for the independent research-delivery decision by TASK-000062/RUN-000056. The exact-head decision will be retained with PR evidence; reservation alone grants no promotion.
