# RUN-000017 / TASK-000020 independent review

Decision: REJECT the exact ART-000005 retry1 combined measurement candidate under the original normative contract. Review completed 2026-10-21T21:00:49.771619Z. No adoption, promotion, merge or final acceptance is granted. No implementation authorship, source edits, live Git writes, network, external messaging or delegation occurred. Requested model/reasoning are recorded in RUN17; actual harness identity remains unknown.

Gate source SHA256: fd82a00452c2c334b8ca353312a0479b8fb1c846f2ec16c3f7d9548e399bb2d4.
DORA source SHA256: b458bca90e118fa9a381cea860202661191ea22cbb1cf752006eca3c988b0c7d.
Reviewed RUN15 final manifest SHA256: 6748ea2b4cb2ceddeabeddce235d6cb27f3b92372af929cf01eb728693b8f940.
Retry1 freeze manifest SHA256: 6b8742b02c3774114ee41fe8944a7522e38d41a1ab40680d3ad31ed210c4d80b.

## Blocking finding

improvement.py lines 278–283 incorrectly equates complete pair-row coverage with complete attempt telemetry. With all twenty pairs present, usage.attempts=40, and one candidate_attempts null, absent or empty, only 39 attempt records are observable. The other count is unknown. Candidate returns reject with reason `reported attempts differ from observable attempt records`; retained 1.0.0 returns inconclusive. Both record the missing telemetry gap and produce no benefit. Six independent cases reproduce the classification regression: three representations for each of outcome and efficiency. This is a false rejection, not an unsafe pass.

Original retained gate DEFINITION.md line 21 explicitly says missing telemetry is inconclusive. TASK15's prior retry preserved this meaning for missing whole pair rows, but the equality guard still overlooks missing attempt containers within supplied rows. Reporting a claimed count greater than an incomplete observed lower bound does not prove an inconsistency. All valid pair identities and order, source/version-adapted trust pins, approved evidence hashes, budgets and primary values are otherwise unchanged. The reproducer and complete input/output bundles are missing_attempts_repro.py and missing-attempts-results.json.

Narrow repair criteria: outcome and efficiency with full pair rows but one missing/null/empty attempt container and usage=40 must remain inconclusive, with no benefit. Observable underreporting (usage=38 when 39 known records remain) must reject. Complete attempt telemetry with summary mismatch must continue rejecting. Observed or reported exhaustion must continue preventing pass under the original budget policy. No widening of authority, budget, criteria or passing thresholds is implied. Preserve this rejected candidate and reports before any correction, then freeze the new candidate and obtain a fresh review and separate Chief of Staff decision.

## Verified evidence

- All ten candidate paths match the retry freeze and final manifest at start and end. All eighteen protected original/EXP1 pins match RUN15 before.json; all forty raw evidence hashes match artifact-sha256.json. No protected changes observed.
- Independent full suite: 77 tests passed. Original 22-observation dual replay reproduced; all 58 frozen typed mutations replayed with no invalid candidate benefit. Three valid claim controls and DORA arithmetic were retained.
- Fresh independent checks: 333 gate cases plus six DORA cases met their bounded expectations. These include exact untrimmed pin comparison, typed authority/approval fields, recursive booleans, hidden failed retry costs, observable attempt limits, cumulative checkpoint/exhaustion, missing rows, orphan cutoff and unchanged causal arithmetic. Their general malformed-telemetry checks originally required only nonpass; the six focused regression cases additionally enforce the prior inconclusive classification and expose the blocker.
- Isolated restoration of retained 1.0.0 sources/fixtures: all thirty original tests passed. Original test_dora remains byte-identical; original test_improvement changes only the plan version fixture. Original 22-case source and prior criteria remain unchanged. Initial candidate's ten retained files match its freeze; first execution's two actual failures remain byte-identical in both preserved report locations.
- DORA source inspection shows only version substitutions and orphan causality health disclosure, without altered arithmetic or thresholds. No DORA blocker found in this scope. Gate pin/type/boolean fixes, observed undercount protection and cumulative checkpoint are demonstrated; attempt completeness classification remains failed.

## Limits and effects

Synthetic qualification cannot authenticate supplied trust records, establish live telemetry completeness, find uninstrumented attempts, prove production behavior or authorize adoption. Source pins were verified; final repository head, PR/CI, independent Chief of Staff approval and operator acceptance remain separate. Reused workload adapters substitute declared source/version pins only; these synthetic substitutions supply no real trust. Protected evidence verification covers enumerated pre-edit hashes, not every possible unrelated file. Validation wrote only /private/tmp/RUN-000017, including authorized temporary synthetic Git fixtures; no live repository Git mutation occurred. Source and protected end pins were captured before handing control back.
