# Retained protocol limitation: seed derivation

- Target System: organization
- Change Classification: organization
- Authorized Scope: truthful task-owned evaluation provenance amendment only
- Affected Paths or Resources: this disclosure and affected SUMMARY/CHECKS explanations; no fixed protocol, case orders, subject responses or active policy changes
- Owning Role: Coordinator
- Related Requirements: REQ-000084
- Related Tasks: TASK-000394, TASK-000397, TASK-000398, TASK-000399
- Approval Requirements: affected APP-000599 review refresh and independent APP-000600; normal evidence PR/main delivery

Revision1 names seed20261028 and independent randomized ordering. The actual pre-execution assembly used `random.Random(20261028 + (1 if condition == "candidate" else 0)).shuffle(ordered)`. Baseline therefore used20261028 and candidate20261029. The per-condition offset was not explicitly preregistered. Independent review reproduced both orders and identified the gap; no outcome-driven reordering is established.

Expected: explicitly specified seed/order derivation before outcomes. Observed: frozen actual orders, but incomplete derivation disclosure. Causal chain: Coordinator used a deterministic condition offset while describing only the root seed; pre-dispatch freezing verified file identity, not exact correspondence between the prose seed and the generating formula. This is an evaluation assembly/specification omission. It does not establish an organization-wide policy defect or model instruction failure.

Containment/remedy: preserve original preregistration, hashes, orders and all forty responses; disclose this retrospective explanation; refresh affected independent review. No rerun or changed denominator; no claim of strict seed-protocol compliance, statistical treatment benefit or promotion. Existing predeclared-protocol requirements already apply; no new universal instruction, approval layer or evaluator change is proposed. Independent Reviewer and CoS assess this bounded evidence-only remedy and its limits. A later experiment must specify its actual formula before execution under existing rules, rather than retroactively adopting this explanation as prior registration.

This limitation does not prevent retaining observed cases and descriptive counts, but narrows interpretation. Root historical explanation is session-source evidence, not authenticated external proof. The fixed case files independently establish the actual retained orders; subject-read/execution isolation remains self-reported.
