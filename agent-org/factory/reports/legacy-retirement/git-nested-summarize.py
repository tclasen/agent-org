"""Generate deterministic classification and compact telemetry evidence from audit JSON."""
import json,collections,hashlib,datetime
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');ROOT=Path('/Users/Shared/old')
a=json.loads((OUT/'git-nested-inventory.json').read_text())['repositories'];rec=json.loads((OUT/'git-nested-recovery.json').read_text())['results'];supp={r['path']:r for r in rec};state=json.loads((OUT/'git-nested-source-state.json').read_text());rows=[]
for row in a:
 p=row['path'];r={'path':p,'kind':row['kind'],'head':row['head']['out'].strip() if row['head']['code']==0 else None};s=supp.get(p,{})
 if p.startswith('projects/features-and-futures-builders/'):
  cls='evaluation-builder-checkout';ev='competition/runs/instruction-effects/<run>/manifest.json paths.builders; builder logs contain task application commits; eval-011/b001 reflog restored native-history.bundle; these are evaluation outputs, not additional operator project identities'
 elif p.startswith('projects/penny/.penny-factory/worktrees/') and row['kind']=='file':
  cls='linked-project-worktree';ev='gitdir points to Penny .git/worktrees; ../.. commondir; branch/HEAD/index verified with remapped Git directory'
 elif p.startswith('projects/penny/.penny-factory/'):
  cls='historical-or-unit-test-fixture';ev='Penny tests/e2e/invitations.spec.ts:456-480 and tests/fixtures/historical-recording-domain.ts intentionally clone shared original pinned source; 261 alternates remapped and clean; unit-runtime repair checkout pins real source commit 0fe4aba481de07088dfe7a1647666662fdbea4bb for unit-runtime testing'
 elif p.startswith('projects/penny-evidence/'):
  cls='synthetic-probe-fixture';ev='All 12 HEAD commit subjects explicitly identify synthetic inputs, synthetic fixture, or synthetic review inputs; synthetic-probes placement; one purposely untracked synthetic-symlink-target.json'
 elif p=='projects/competition/.local/ollama-metered-source':
  cls='modified-upstream-source';ev='origin https://github.com/ollama/ollama.git; detached pinned tag baseline; 2 tracked modifications plus ff_usage.go; meaningful custom metering code'
 elif p.startswith('projects/competition/.local/'):
  cls='evaluation-recovery-or-shadow';ev='HEAD subjects identify task application recovery, PM-only immutable diagnostic, or identical pilot starter; observer-proof origins point to per-builder history.bundle; one unborn shadow'
 elif p=='projects/every_game/target/codex-proxy':
  cls='clean-upstream-dependency-clone';ev='origin github.com/mehdic/codex-proxy; main da828dafa0bb98a932e022edb608e6b35f0a8d9b; clean tracked/untracked status; build target location alone was insufficient'
 elif p.startswith('projects/udop/.cache/tmp/'):
  cls='pytest-fixture';ev='unborn Git repos; test_clean_* fixture paths; exact staged dist/source.txt and synthetic draft/source/pyproject inputs; excludes remote sync per operator inaccessible-udop disposition'
 elif p=='projects/udop/.cache/uv/sdists-v9':
  cls='cache-sentinel';ev='Zero-byte .git file is invalid gitfile format, not a Git repository'
 elif p.startswith('factory/.factory-planning/'):
  if row['head']['code']==0:cls='evaluation-captured-application-source';ev='Captured/selected source within named req007 calibration runs; HEAD generated workspace/task subjects; native Git snapshot, not an independent project; dirty source exceptions separately enumerated'
  elif '/evaluation-host-logs/' in p:cls='evaluation-host-canary-fixture';ev='Unborn Git HEAD; only AGENTS.md/canary.txt/optional heartbeat.txt, 108–485 bytes per fixture'
  else:cls='evaluation-partial-git-snapshot';ev='Explicit Git directory validation fails; source-capture fixture has partial/empty metadata; do not fall through to parent factory repository identity'
 else:raise RuntimeError('unclassified '+p)
 r.update(classification=cls,evidence=ev,branch=row.get('branch',{}).get('out','').strip())
 status=s.get('status') if 'alternates' in s or row['head']['code'] else row.get('status')
 r['status_exit']=status.get('code') if status else None;r['dirty_paths']=status.get('out','').splitlines() if status and status['code']==0 else None
 if row.get('original_gitdir'):r.update(original_gitdir=row['original_gitdir'],original_target_exists=row.get('original_target_exists'),remapped_gitdir=row.get('remapped_gitdir'))
 if 'alternates' in s:r['alternate_dependencies']=s['alternates']
 rows.append(r)
counts=collections.Counter(r['classification'] for r in rows)
(OUT/'git-nested-classification.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':counts,'markers':rows,'limits':'802 nested markers in expanded traversal; dependency/package/bytecode exclusions remain explicit in git-nested-discovery.json; hash/status is not backup.'},indent=2))
# Preserve useful Playwright outcomes without raw stdout, screenshots or request payloads.
p=ROOT/'projects/penny/.penny-factory/worktrees/143-integrated-acceptance/test-results/results.json';raw=p.read_bytes();report=json.loads(raw);tests=[]
def visit(suite,prefix=''):
 title='/'.join(x for x in [prefix,suite.get('title','')] if x)
 for spec in suite.get('specs',[]):
  for t in spec.get('tests',[]):
   tests.append({'suite':title,'spec':spec.get('title'),'file':spec.get('file',suite.get('file')),'line':spec.get('line'),'project':t.get('projectName'),'expectedStatus':t.get('expectedStatus'),'status':t.get('status'),'results':[{'status':r.get('status'),'duration':r.get('duration'),'retry':r.get('retry'),'errors_count':len(r.get('errors',[])),'attachments':[{'name':x.get('name'),'contentType':x.get('contentType')} for x in r.get('attachments',[])]} for r in t.get('results',[])]})
 for child in suite.get('suites',[]):visit(child,title)
for s in report.get('suites',[]):visit(s)
(OUT/'git-nested-penny-test-outcomes.json').write_text(json.dumps({'source':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(raw).hexdigest(),'source_bytes':len(raw),'stats':report['stats'],'errors_count':len(report.get('errors',[])),'tests':tests,'redaction':'Preserves test identity/outcome/duration/retry/attachment type; excludes stdout/stderr/raw error messages/attachment payloads/config arguments. Aggregates are one synthetic browser suite, not production success rates. Cannot replay without source/screenshots/native runtime.'},indent=2))
print('CLASSES',dict(counts),'total',len(rows));print('PLAYWRIGHT',len(tests),report['stats'])
