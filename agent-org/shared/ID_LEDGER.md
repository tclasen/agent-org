# Identifier allocation ledger

Coordinator serializes allocations; never reuse IDs, including rejected/canceled work. Actual formal definitions plus this ledger are authoritative. Archived references and synthetic fixture namespaces do not allocate live records. Unknown concurrent allocation blocks mutation.

Allocated through: AGENT-000008, DEC-000015, REQ-000053, AC-000048, CAP-000022, WF-000006, TASK-000084, RUN-000079, APP-000023, ART-000005, INIT-000001, INTENT-000001, TRG-000001, EXP-000002, EVAL-000007, FAIL-000016. Failure definitions are in evaluations/FAILURES.md. DEC-000001..14 remain in intake history. EVT-000001..000004 are actual installation stream events; synthetic test events remain separately labeled.

Research admission reconciled merged REQ-000050, TASK-000054..56 and RUN-000048..50 omitted by the prior ledger checkpoint. New research allocations are serialized in this worktree; workers allocate no IDs.

APP-000015 is reserved for the independent research-delivery decision by TASK-000062/RUN-000056. The exact-head decision will be retained with PR evidence; reservation alone grants no promotion.

Progressive disclosure reserves TASK-000066..71, RUN-000062..67, APP-000018..19. Concurrent cleanup reservations TASK-000063..65/RUN-000058..61/APP-000016 and superseded provisional RUN-000057/APP-000017 are preserved. This was reconciled against remote main79298fe and the source ledger before continuation; do not reuse.

Upstream cleanup reservation/provenance retained on integration:

Delivery admission observed Tessl published TASK-000054..56/RUN-000048..50, and active autonomy worktree reservations TASK-000057..62/RUN-000051..56/REQ-000051/APP-000015. Cleanup delivery records were remapped before publication to TASK-000063..65, RUN-000058..61 and APP-000016. No published or reserved identities were reused.
Active cleanup delivery reservations: TASK-000063 Coordinator, TASK-000064 Reviewer, TASK-000065 Chief of Staff; RUN-000058 Planner, RUN-000059 Reviewer, RUN-000060 Chief of Staff, RUN-000061 Coordinator; APP-000016 direct operator grant. RUN-000057 and APP-000017 observed concurrent reservations are preserved for their other owner. These cleanup identities must not be reallocated.
Research admission reconciled merged REQ-000050, TASK-000054..56 and RUN-000048..50 omitted by the prior ledger checkpoint. New research allocations are serialized in this worktree; workers allocate no IDs.
APP-000015 is reserved for the independent research-delivery decision by TASK-000062/RUN-000056. The exact-head decision will be retained with PR evidence; reservation alone grants no promotion.

Commons video reservation 2026-10-22T01:57:14.055392+00:00: TASK-000079..84, RUN-000075..78, APP-000022..23. Coordinator /root owns these; preserve autonomy TASK72..78/RUN68..74/REQ52/APP20..21. No worker allocates IDs.

REQ-000053 reserved for Commons video requirement under TASK-000079; distinct from autonomy REQ-000052.

Worktree cleanup reservation 2026-10-22T02:15:32.088934+00:00: TASK-000095..97, RUN-000089..91, APP-000026..27. Coordinator /root owns instruction cleanup; preserve project demos TASK85..94/RUN80..88/APP24..25 and all earlier allocations. No worker allocates IDs.

Autonomy implementation reservation 2026-10-22T01:39:44.573658+00:00: TASK-000072..78, RUN-000068..74, REQ-000052, EXP-000002, APP-000020..21. Coordinator /root in feat/autonomy-workflow owns these; preserve progressive-disclosure reservations66..71/62..67/18..19. No worker allocates IDs.

Identity reconciliation 2026-10-22T02:10:48.290517+00:00: published Commons PR14 owns RUN-000075..78. The unpublished autonomy second recovery execution provisionally labeledRUN75 is remapped to RUN-000079 before publication. Its original manifest/journal/report identifiers and hashes remain historical evidence; the new formal record discloses the alias. RUN79 is reserved to this owner; no published Commons definition is changed.

README delivery reservation 2026-10-22T02:53:36.975293+00:00: TASK-000102..104, RUN-000096..98, APP-000030. Coordinator /root owns root README and scoped delivery records; preserve all prior reservations.

README boundary correction reservation 2026-10-22T02:55:38.149659+00:00: TASK-000105 and RUN-000099 parent coordination; no reuse of prior IDs.

Final-response delivery safeguard reservation 2026-10-22T03:01:29.200686+00:00: TASK-000106..108, RUN-000100..102, APP-000032..33. Coordinator /root owns only core/acceptance safeguard and task-owned records; all prior reservations preserved.
