# Publication-byte deterministic qualification

- Target System: organization
- Change Classification: organization
- Authorized Scope: publication selector/output pairing and unchanged static assertions on exact normalized publication bytes
- Affected Paths or Resources: qualify.py, test-results-publication.json, QUALIFICATION-PUBLICATION.md
- Owning Role: Developer
- Related Requirements: REQ-000085
- Related Tasks: TASK-000403, TASK-000400
- Approval Requirements: parent-authorized nonsemantic publication normalization; affected independent Reviewer/CoS exact-byte confirmation and normal PR/main delivery remain required

Publication static qualification passed103/103 checks, exit0, in one execution using `--candidate-manifest candidate-publication-manifest.json --output test-results-publication.json --final`. All33live source bytes and snapshots match the selected publication manifest. The corpus remains15,600→13,645 words (−1,955), with unchanged per-role reductions. This is publication-byte verification, not a third behavioral experiment or a behavioral qualification result.

Before this run, read-only comparison of every publication snapshot to the frozen candidate2 snapshot established exactly two differences: AGENTS.md and agents/design-director/CONTEXT.md each lose one trailing LF byte. For both, `before == after + b'\n'` and whitespace-split words are identical; all31other snapshots are byte-identical. The publication manifest records their before/after hashes. Original candidate2 sources, raw behavior, manifest and results remain intact; candidate1 rejection remains intact.

The harness change only adds the publication manifest/output to exact allowlists and their pairing; previous pairings remain supported and mismatches remain refused. All23original `check(...)` call ASTs are identical both to the immediately preceding harness and retained candidate1 harness. No assertion, evaluator, schema, source instruction or production tool changed. The same original historical protocol assertions are integrity checks and are not revised behavioral scoring. No broad software rerun was performed for these two LF removals; parent-reported earlier144tests are not independently re-executed here.

Reads for this continuation: PUBLICATION-NORMALIZATION.md, publication manifest/snapshots, candidate2 manifest/snapshots, existing/retained qualifier, and the normal unchanged static-check source/input/link/temporary-inline-plan fixture reads. No revised held-out cases/rubric/order/responses or dispatch contents were read, and no subject was executed. Read coverage is worker-reported visible-tool evidence, not host-enforced secrecy. Host model/context/token/cost metadata remains unknown.

The versioned report retains preparation history and prior-result lineage. Previous test-results.json, test-results-v2.json and reports were not overwritten. The earlier result identifies the version of qualify.py it used; the current qualifier has a new hash for selector support. No fresh behavioral result is inferred from this static run. Parent owns cumulative budgets, final review/CoS decision, exact PR checks, merge/main verification and cleanup. Worker mutation claim is released to parent. Exact next safe action: affected independent Reviewer and CoS confirm final assembled publication bytes, then parent completes authorized delivery. No acceptance or verified remote-main delivery is claimed.

Artifact SHA256 identities:

- qualify.py: 896e2f7e9f7c09e22f64cfaa20492887df6b4f535c2ecf10441e7c9800a15f06
- test-results-publication.json: b0e3e40286102de2d3c9d700008b4a435933ac0489a645b4fdbee96080258fbb
- candidate-publication-manifest.json: a09cfaef62926cf091b81a582766bc49df20db650267aad84e255f9795fb6b9a
- candidate-v2-manifest.json: fe69bb5f53877753cdd56fcfde30b3167a3e1dbd0d5d6f3adff36e6586932874
- test-results-v2.json: 7ba09f6e2a10dbd48c00680662ed33899cc38ed56a7027d5e410eef466aa528d
- test-results.json: 9f3035972d48783993880d2fac6a217f9284adce77209301754d32a3ceffab0e
