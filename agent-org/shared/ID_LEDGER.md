# Identifier allocation ledger

Coordinator serializes allocations; never reuse IDs, including rejected/canceled work. Actual formal definitions plus this ledger are authoritative. Archived references and synthetic fixture namespaces do not allocate live records. Unknown concurrent allocation blocks mutation.

Allocated through: AGENT-000008, DEC-000015, REQ-000052, AC-000048, CAP-000022, WF-000006, TASK-000078, RUN-000074, APP-000021, ART-000005, INIT-000001, INTENT-000001, TRG-000001, EXP-000002, EVAL-000007, FAIL-000016. Failure definitions are in evaluations/FAILURES.md. DEC-000001..14 remain in intake history. EVT-000001..000004 are actual installation stream events; synthetic test events remain separately labeled.

Research admission reconciled merged REQ-000050, TASK-000054..56 and RUN-000048..50 omitted by the prior ledger checkpoint. New research allocations are serialized in this worktree; workers allocate no IDs.

APP-000015 is reserved for the independent research-delivery decision by TASK-000062/RUN-000056. The exact-head decision will be retained with PR evidence; reservation alone grants no promotion.

Progressive disclosure reserves TASK-000066..71, RUN-000062..67, APP-000018..19. Concurrent cleanup reservations TASK-000063..65/RUN-000058..61/APP-000016 and superseded provisional RUN-000057/APP-000017 are preserved. This was reconciled against remote main79298fe and the source ledger before continuation; do not reuse.

Upstream cleanup reservation/provenance retained on integration:

Delivery admission observed Tessl published TASK-000054..56/RUN-000048..50, and active autonomy worktree reservations TASK-000057..62/RUN-000051..56/REQ-000051/APP-000015. Cleanup delivery records were remapped before publication to TASK-000063..65, RUN-000058..61 and APP-000016. No published or reserved identities were reused.
Active cleanup delivery reservations: TASK-000063 Coordinator, TASK-000064 Reviewer, TASK-000065 Chief of Staff; RUN-000058 Planner, RUN-000059 Reviewer, RUN-000060 Chief of Staff, RUN-000061 Coordinator; APP-000016 direct operator grant. RUN-000057 and APP-000017 observed concurrent reservations are preserved for their other owner. These cleanup identities must not be reallocated.
Research admission reconciled merged REQ-000050, TASK-000054..56 and RUN-000048..50 omitted by the prior ledger checkpoint. New research allocations are serialized in this worktree; workers allocate no IDs.
APP-000015 is reserved for the independent research-delivery decision by TASK-000062/RUN-000056. The exact-head decision will be retained with PR evidence; reservation alone grants no promotion.

Autonomy implementation reservation 2026-10-22T01:39:44.573658+00:00: TASK-000072..78, RUN-000068..74, REQ-000052, EXP-000002, APP-000020..21. Coordinator /root in feat/autonomy-workflow owns these; preserve progressive-disclosure reservations66..71/62..67/18..19. No worker allocates IDs.

