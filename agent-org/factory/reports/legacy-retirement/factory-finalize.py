"""Add immutable source identity table and final coverage to the authored report."""
import collections,gzip,hashlib,json,pathlib,shutil
BASE=pathlib.Path('/Users/Shared');OUT=BASE/'agent-org/factory/reports/legacy-retirement'
if (OUT/'factory-inventory-summary.json').exists():
 for name in ['factory-files.jsonl','factory-hash-groups.jsonl']:
  source=OUT/name
  if source.exists():
   with source.open('rb') as reader,(OUT/(name+'.gz')).open('wb') as raw:
    with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as writer:
     shutil.copyfileobj(reader,writer)
   source.unlink()
sources={
'F01':'old/factory/evaluation/reports/req007-three-arm-v2.md',
'F02':'old/factory/.factory-planning/REQ-007-THREE-ARM-V2-COMPARISON-SNAPSHOT.json',
'F03':'old/factory/.factory-planning/REQ-007-MATCHED-PILOT-STATUS.md',
'F04':'old/factory/.factory-planning/REQ-007-COMPLETION-AUDIT.md',
'F05':'old/factory/.factory-planning/NEXT-CALIBRATION-REVIEW.md',
'F06':'old/factory/.factory-planning/REQ-007-NATURAL-CALIBRATION-V5-TERMINAL-REVIEW.json',
'F07':'old/factory/.factory-planning/REQ-007-NATURAL-CALIBRATION-V6-TERMINAL-REVIEW.json',
'F08':'old/factory/.factory-planning/REQ-007-NATURAL-CALIBRATION-V8-TERMINAL-REVIEW.json',
'F09':'old/factory/.factory-planning/REQ-007-CHECKPOINT-NATURAL-CALIBRATION-V9-TERMINAL.json',
'F10':'old/factory/.factory-planning/REQ-007-CALIBRATION-V9-GRADE-V1-ACTUALS.json',
'F11':'old/factory/.factory-planning/REQ-007-CALIBRATION-V9-GRADE-V1-REVIEW.json',
'F12':'agent-org/factory/reports/legacy-retirement/factory-quantitative-evidence.json',
'F13':'old/factory/.factory-planning/REQ-007-STORAGE-GROWTH-COMPARISON.json',
'F14':'old/work/factory/docs/evidence/lean-acceptance-review.md',
'F15':'old/work/factory/docs/i0-evidence.md',
'F16':'old/work/factory/docs/decisions/0006-terminated-agent-capture.md',
'F17':'old/work/factory/docs/decisions/0007-fresh-patch-verification.md',
'F18':'old/work/factory/docs/decisions/0008-node-cleanup-evidence.md',
'F19':'old/work/factory/docs/decisions/0012-unstarted-run-cleanup.md',
'F20':'old/work/factory/docs/decisions/0003-collector-supervision.md',
'F21':'old/work/factory/docs/decisions/0009-lean-audit-ledger.md',
'F22':'old/work/factory/docs/decisions/0010-lean-metrics-buffer.md',
'F23':'old/work/factory/docs/decisions/0005-lean-mvp.md',
'F24':'old/work/factory/docs/decisions/0011-lean-storage-cleanup.md',
'F25':'old/work/factory/docs/evidence/lean-schema38-isolated-restore.json',
'F26':'old/work/factory/docs/evidence/workspace-consolidation.json',
'F27':'old/work/factory/.local/installed-recovery37-footprint/summary.json',
'F28':'old/work/factory/.local/scheduled-recovery-footprint-with-helper/summary.json',
'F29':'old/work/factory/docs/garage-candidate-review.md',
'F30':'old/work/factory/docs/seaweed-candidate-review.md',
'F31':'old/work/factory/docs/evidence/lean-dependency-review.md',
'F32':'old/work/AegisTrace/docs/governance/acceptance.md',
'F33':'old/work/AegisTrace/docs/engineering/test-strategy.md',
'F34':'old/work/AegisTrace/TASKS.md',
'F35':'old/work/CognitionGrid/.codex-notes.md',
'F36':'old/work/CognitionGrid/db/migrations/README.md',
'F37':'old/work/CognitionGrid/README.md',
'F38':'old/work/Exaptra/README.md',
'F39':'old/work/Exaptra/WORKFLOW.md',
'F40':'old/work/PortionGuard/docs/design-decisions.md',
'F41':'old/work/PortionGuard/docs/public-contract-review.md',
'F42':'old/work/PortionGuard/docs/phase-1-release-readiness.md',
'F43':'old/work/PortionGuard/docs/security-limits.md',
'F44':'old/work/PortionGuard/docs/source-locations.md',
'F45':'old/work/PortionGuard/NOTES.md',
'F46':'old/work/PortionGuard/benchmarks/baselines/2026-07-21-darwin-arm64.md',
'F47':'old/work/ai_cost/src/calculator.ts',
'F48':'old/work/ai_cost/src/defaultScenario.ts',
'F49':'old/work/ai_cost/src/calculator.test.ts',
'F50':'old/work/coding_evals/README.md',
'F51':'old/work/coding_evals/docs/ADDING_PROJECTS.md',
'F52':'old/work/ism-tools/README.md',
'F53':'old/work/marked/docs/architecture.md',
'F54':'old/work/marked/docs/supply-chain.md',
'F55':'old/work/marked/README.md',
'F56':'old/work/odni-sdk/index.md',
'F57':'old/work/odni-sdk/specifications/index.md',
'F58':'old/work/odni-sdk/AGENTS.md',
'F59':'old/work/portions/docs/POLICY-PROVENANCE.md',
'F60':'old/work/portions/SECURITY.md',
'F61':'old/work/portions/CHANGELOG.md',
'F62':'old/agent-collaboration/factory_catalog/taxonomy-discussion-2026-09-28.md',
'F63':'old/agent-handoffs/factory-catalog-knowledge-work-taxonomy-2026-09-28.md',
'F64':'old/factory/.factory-planning/DECISIONS.md',
'F65':'old/factory/.factory-planning/EVALUATION.md',
}
rows=[]
for key,path in sources.items():
 p=BASE/path;b=p.read_bytes();rows.append({'id':key,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(OUT/'factory-source-index.json').write_text(json.dumps(rows,indent=2)+'\n')
table='| ID | Historical source path | SHA-256 |\n| --- | --- | --- |\n'+'\n'.join(f"| {r['id']} | `{r['path']}` | `{r['sha256']}` |" for r in rows)
p=OUT/'factory-learnings.md';text=p.read_text();text=text.replace('<!-- SOURCE_IDENTITIES -->',table)
summary=OUT/'factory-inventory-summary.json'
if summary.exists():
 d=json.loads(summary.read_text());lines=['### Final file inventory','', '| Root | Entries | Logical bytes | Hashed files | Classes |','| --- | ---: | ---: | ---: | --- |']
 for root,entry in d['roots'].items():
  c=entry['counts'];lines.append(f"| `{root}` | {c.get('entries',0):,} | {c.get('bytes',0):,} | {c.get('hashed',0):,} | `{json.dumps(entry['classes'],sort_keys=True)}` |")
 lines+=['',f"Unique hashed contents across all roots: {d['unique_hashes']:,}. Read/directory errors: {len(d['errors'])}. Complete per-path dispositions remain in the compressed inventory."]
 text=text.replace('<!-- COVERAGE_ACCOUNTING -->','\n'.join(lines))
p.write_text(text)
print('source_ids',len(rows),'inventory_complete',summary.exists())
