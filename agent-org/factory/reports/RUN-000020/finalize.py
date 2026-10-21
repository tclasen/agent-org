import json,hashlib,datetime
from pathlib import Path
root=Path('/Users/Shared/agent-org');out=Path('/private/tmp/RUN-000020');e=Path('/private/tmp/RUN-000019-evidence');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
x=json.loads((e/'extended58.stdout').read_text());assert len(x['typed_records'])==58
assert all(r['candidate']['decision']!='pass' and not r['candidate']['benefit'] for r in x['typed_records'])
assert all(r['candidate']['decision']==r['baseline']['decision']=='pass' and r['candidate']['benefit']==r['baseline']['benefit'] for r in x['positive_controls'])
assert x['valid_dora_baseline']['services']==x['valid_dora_candidate']['services']
a=json.loads((e/'original22.stdout').read_text());assert len(a['baseline'])==len(a['candidate'])==22
assert [r['case'] for r in a['baseline']]==[r['case'] for r in a['candidate']]
for r in json.loads((e/'sixcase-sameversion.stdout').read_text())['six_fixed_cases']:
 assert r['baseline']['result']['decision']=='inconclusive'
 assert r['retry1_same_version']['result']['decision']=='reject'
 assert r['retry2_same_version']['result']['decision']=='inconclusive'
 assert not r['retry2_same_version']['result']['benefit']
pins=json.loads((out/'pins-start.json').read_text())
for p,h in pins['candidate'].items():assert sha(root/p)==h
for p,h in pins['protected'].items():assert sha(root/p)==h
assert sha(e/'final-manifest.json')==sha(root/'factory/reports/RUN-000019/final-manifest.json')=='bfc056e0575a261e78a70680c769c89437960b04d7800075013b1ca97fb28a1f'
at=datetime.datetime.now(datetime.timezone.utc).isoformat()
(out/'pins-end.json').write_text(json.dumps({'at':at,'candidate':pins['candidate'],'protected':pins['protected']},indent=2)+'\n')
whole=hashlib.sha256(json.dumps(pins['candidate'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
review=f'''# RUN-000020 / TASK-000020 independent final retry review

Decision: ACCEPT the exact whole 1.0.1 measurement candidate for independent Chief of Staff consideration under APP-000004 and the original normative contract. Decision time: {at}. This is a bounded independent review recommendation, not adoption, promotion, merge, production assurance or final operator acceptance. The reviewer is a fresh execution distinct from implementers; actual model metadata remains unknown.

Whole candidate is the ten-path SHA256 mapping in pins-end.json, including unchanged prior-reviewed DORA, definitions and tests. Canonical compact sorted-JSON mapping SHA256: {whole}. Gate: {pins['candidate']['factory/quality-gates/improvement.py']}. DORA: {pins['candidate']['factory/dora/calculator.py']}. Regression driver: {pins['candidate']['factory/tests/test_gate_regressions.py']}.

Final RUN19 evidence manifest: bfc056e0575a261e78a70680c769c89437960b04d7800075013b1ca97fb28a1f. Final retry2 freeze: 215eb5a839bf36c27e22ecefc56380e1eb9ce1c5f309bd62698180373dcbb7fc. Prior independent RUN17 evidence manifest: 06ee5331fa8f6a928be6aeeb094fd49659e58c7d2a192f0b34f498c523efdee5. All 52 RUN19 artifacts and all 21 RUN17 artifacts verified, as did all 18 protected baseline/EXP1 evidence pins. Ten candidate pins matched at start and end.

## Criterion outcomes

- VERIFIED: six exact independent EVAL5 input bundles now return inconclusive with no benefit for missing/null/empty attempt containers in outcome and efficiency. Their only substitutions were source pins and dependent synthetic digests. Recorded three-way results are retained baseline inconclusive, rejected retry1 reject, final retry2 inconclusive. Same-version correction demonstrates repair without unsupported-version rejection.
- VERIFIED: fresh independent 120-case execution covers both sides and all three missing forms; observable undercount still rejects, incomplete counts at/above lower bound remain inconclusive, complete known counts reconcile exactly, reported/observed exhaustion prevents pass, and missing/false primary values, malformed attempt values/statuses and false authority/regression pins cannot establish benefit. Hidden failed retry costs reject and cumulative checkpoint/exhaustion controls hold.
- VERIFIED: narrow source delta adds a nonempty-list completeness predicate before equality, retaining unconditional observed lower-bound and budget guards. Required telemetry validation still prevents benefit. Only four candidate files differ from RUN17: gate, appended regression methods, and two fixtures with exactly the eight derived source/association hash fields. Every original driver AST node/method is unchanged; original 22-case script and 58-case function remain unchanged. test_improvement differs from retained original only in spec.version; original test_dora is byte-identical.
- VERIFIED WITH RETAINED EVIDENCE: prior RUN17 333 gate plus six DORA checks remain applicable to unchanged code; no new concern justified repeating the broad suite. RUN19 actual full suite passed 85 tests (77 retained plus eight new methods); original 22 observations and 58 typed mutations passed their original assertions; three positive claim controls and valid DORA service arithmetic agree with retained baseline. Isolated rollback passed 30 original tests. Existing DORA code/definitions/fixtures are unchanged from RUN17 and its original-contract review found no DORA blocker.
- VERIFIED: original failures/rejections remain preserved. Two local reviewer-script setup mistakes (overbroad fixture version replacement, then inventory-envelope key) were corrected without touching candidate or evidence; details retained in reviewer-check-correction.txt. They occurred before their affected checks, which subsequently passed.
- VERIFIED / ATTRIBUTED: all 320 preexisting factory inventory entries were checked. Exactly four worker candidate paths and the concurrently appended installation ledger differ. The initial inventory assertion failure is retained (SHA256 b500d5f3fcde104ad2b891fd93c1fcd09af48e799ac6eb872c77a53b274e583e). Ledger old byte prefix is unchanged; entire four-event chain validates, and exact new EVT3/EVT4 rows identify Coordinator RUN1/TASK5. Coordinator explicitly confirmed their APP1 ownership. External GitHub facts in those events were not independently fetched in this no-network review. This is a scoped concurrent-owner reconciliation, not an ignored global difference or another candidate retry.
- VERIFIED: recorded RUN19 cumulative elapsed wall time since ART4 is 1157.55 seconds and raw evidence 703136 bytes, within original 3600-second/100-MiB limits; final retry2 is the last authorized retry. Review completes within the original elapsed time bound. No criteria, thresholds, retained history, authority or retry counter was changed to achieve acceptance.

## Effects, limits and handoff

All reviewer writes are in /private/tmp/RUN-000020. No source edits, live Git writes, network, external messages or delegation occurred. Source inspection and synthetic execution cannot authenticate real trust records, prove production telemetry completeness, detect uninstrumented attempts or establish live production benefit. No production threshold changed. Separate exact-candidate Chief of Staff approval, final delivered-head/CI checks and operator acceptance remain required. Next action: Coordinator preserves this evidence and sends the exact whole candidate mapping plus frozen and final evidence manifests to a distinct Chief of Staff; candidate changes invalidate this recommendation.
'''
(out/'REVIEW.md').write_text(review)
manifest={'run':'RUN-000020','task':'TASK-000020','at':at,'decision':'ACCEPT','whole_candidate':pins['candidate'],'whole_candidate_mapping_sha256':whole,'run19_final_manifest_sha256':sha(e/'final-manifest.json'),'run17_prior_manifest_sha256':pins['prior_review_manifest'],'freeze_sha256':pins['freeze'],'artifacts':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='evidence-manifest.json'}}
(out/'evidence-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'decision':'ACCEPT','at':at,'review_sha256':sha(out/'REVIEW.md'),'manifest_sha256':sha(out/'evidence-manifest.json'),'whole_candidate_mapping_sha256':whole}))
