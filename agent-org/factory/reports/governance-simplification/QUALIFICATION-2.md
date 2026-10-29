# Revised candidate deterministic qualification

- Target System: organization
- Change Classification: organization
- Authorized Scope: APP-000604 qualifier source-selector/versioned-output support and revised deterministic report only
- Affected Paths or Resources: qualify.py, QUALIFICATION-2.md, test-results-v2.json; candidate1 retained files and originals remain immutable
- Owning Role: Developer
- Related Requirements: REQ-000085
- Related Tasks: TASK-000403, TASK-000400
- Approval Requirements: APP-000604 bounded admission; APP-000605 independent revised review and APP-000603 exact-candidate CoS decision; parent-owned normal delivery

Status: candidate2 final deterministic source qualification passed103/103 checks, command exit0, after explicit parent source-ready. The versioned command ran once against candidate-v2-manifest.json. All33live source bytes and inert snapshots match that frozen manifest; old baseline/protocol/evaluator checks also pass. Candidate1 remains behaviorally rejected despite its static pass. Its retained qualifier, reports, results and raw outcomes remain unchanged. No old workload replay is final revised behavioral evidence.

The qualifier now accepts `--candidate-manifest candidate-v2-manifest.json --output test-results-v2.json`. Its original candidate/output pairing remains supported; mismatched pairings are refused before any write. Source-manifest choices and output choices are exact allowlists. Every original assertion remains: retained baseline and original protocol identities, original order derivation/permutations, exact source snapshots, role/context/metadata/history/links, original evaluator and census. Existing old-case/order checks verify historical protocol integrity only; they neither execute subjects nor score candidate2 behavior. No revised held-out case or rubric is read by this harness.

Verification before source readiness: Python AST comparison found all23original `check(...)` call expressions identical to the retained candidate1 qualifier (including original nested assertions); parsing succeeded and CLI `--help` exited0. At that pre-readiness observation no qualification run had occurred. Following parent source readiness the single versioned final command passed, without behavioral execution or revised-workload reads. Candidate1 retained qualifier SHA256:444421deee61c55b6ad6862107bb2227b702179211432134195ea47584349193. Prepared revised qualifier SHA256:3ba3b5db48f90bd16b77fee6d550ed0733d1e0d9a72b6da6a59c9b90d2cbd1db.

On a new versioned output, preparation history is copied from the immutable retained candidate1 results and its exact result identity is referenced. This preserves failure lineage without overwriting candidate1. New source identity and qualifier identity appear in the versioned result. The final static result does not imply that revised behavioral outcomes passed, evaluator semantics are equivalent, or independent review/approval/delivery occurred.

Read account for this harness revision: APP-000604, REPLAN-2.md, existing qualify.py, retained candidate1 qualify.py. A lookup of the abbreviated REPLAN2.md failed read-only; APP604's canonical REPLAN-2.md reference resolved it. The final deterministic command additionally read the selected candidate-v2 manifest/snapshots, pinned baseline/original protocol inputs, active33sources, linked static contracts and the retained prior result needed for lineage. It executed only the existing temporary inline-plan fixture. No revised-case/rubric/order/response files or subject dispatch contents were read, no subject was invoked, and no active source or frozen-input file was edited. This is a worker-reported read account from visible tools, not host-enforced secrecy or an independently audited full trace. Shared-filesystem exposure limits remain. Actual host model/context/token/cost telemetry is unknown.

Parent owns cumulative90active-minute budget, the one revised experiment, source readiness, held-out workload/dispatch freeze, fresh subject execution, independent scoring, exact-candidate review/approval and delivery. This worker claims only selector/output-version changes and deterministic evidence when subsequently run. Final scoped corpus:15,600→13,645 words (−1,955;12.53%); every measured role contract remains shorter. Source-policy SELF_IMPROVEMENT SHA256:39d1305251ab835d310e34a552035ae227d60440370fae6e22ae626c36d457a2. Full per-file/per-role census and source hashes appear in test-results-v2.json. Word counts do not establish tokens, capacity or productivity.

Post-run AST comparison again confirmed all23original check-call expressions identical. Versioned results retain prior preparation history and refer to the immutable rejected-candidate1 result hash. Neither original test-results.json nor original QUALIFICATION.md was edited for this revision.

Exact next action: parent completes source-frozen held-out workload/dispatch materialization, fresh subject execution and independent scoring/review, then obtains exact-candidate CoS decision and normal delivery. No acceptance, promotion or verified remote-main delivery is claimed.
