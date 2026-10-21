#!/usr/bin/env python3
"""Fingerprint manually reviewed documentary sources and the ignored build exception."""
import collections, hashlib, json, os, pathlib, stat
BASE=pathlib.Path('/Users/Shared/old/projects');OUT=pathlib.Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
DOCS={
'S01':['work/docs/evals/2026-10-08-screening/README.md','Screening findings, manual hard failure and oracle limitations'],
'S02':['work/docs/evals/2026-10-08-outcomes/README.md','Outcome screen, post-hoc corrections, recovery and usage missingness'],
'S03':['competition/docs/lessons-learned.md','Append-only lesson lifecycle and concrete controls'],
'S04':['competition/docs/main-readiness-gaps.md','Missing usage, pilot limitations and prospective changes'],
'S05':['competition/docs/evidence-analysis.md','Independent trajectories, multiplicity and practical bands'],
'S06':['competition/docs/measurement.md','Timing, request-native accounting and sandbox DORA definitions'],
'S07':['competition/lessons/records.jsonl','All latest73 lesson observations inspected;531 records structurally parsed'],
'S08':['penny/docs/factory/ARCHIVE.md','Sanitized deterministic archival, reconstruction and limits'],
'S09':['penny/docs/FACTORY.md','Hierarchy, bounded repairs, videos and explicit-session scope'],
'S10':['factory/evals/state-handoff/READINESS.md','Setup-only diagnostics, actual isolation and handoff gaps'],
'S11':['factory/evals/state-handoff/PILOT.md','Natural-compaction and distinct-agent acceptance protocol'],
'S12':['factory_catalog/docs/research/software-factory-learnings.md','Revision-bound secondary synthesis; not operational evidence'],
'S13':['factory_catalog/docs/research/classwork-learnings.md','Canonical concepts, transfer evidence and uncertain effects'],
'S14':['factory_catalog/docs/research/semantic-search-learnings.md','Extraction/retrieval separation and correction-preserving recovery'],
'S15':['commons/agent-org/factory/reports/SCORECARDS.md','Synthetic denominator and missing provenance separation'],
'S16':['commons/agent-org/factory/reports/VERIFICATION.md','Original90-test implementation observation and fixture replay'],
'S17':['commons/agent-org/factory/reports/SYNTHETIC_DELIVERY.md','Synthetic five-metric oracle'],
'S18':['commons/agent-org/evaluations/EVAL-000005.md','110-test corrective acceptance preserves metric semantics'],
'S19':['commons/agent-org/evaluations/EVAL-000006.md','Independent integration,4/4 blind coordination and native limits'],
'S20':['voldenites/agent-org/INSTALLATION_REPORT.md','Research-specific organization, actual-model unknown and trusted boundary'],
'S21':['voldenites/agent-org/runs/FAIL-000001.md','Protected-main rejection, retained attempts and later operator resolution'],
'S22':['voldenites/agent-org/evaluations/EVAL-000082.md','Instrumentation wrapper semantics and loader evidence rejection'],
'S23':['voldenites/agent-org/evaluations/EVAL-000085.md','Strict helper cannot repair omitted whole-run evidence'],
'S24':['voldenites/agent-org/evaluations/EVAL-000088.md','Versioned consumer coverage and conditional admission'],
'S25':['voldenites/agent-org/evaluations/EVAL-000152.md','Mismatched observable native-session chain accepted by consumer'],
'S26':['voldenites/agent-org/evaluations/EVAL-000155.md','Corrected launch/poll/terminal binding and retained failures'],
'S27':['voldenites/agent-org/evaluations/EVAL-000164.md','Credential/helper admission must precede acquisition'],
'S28':['voldenites/agent-org/evaluations/EVAL-000162.md','Proof assumptions/typed names/universe fields and retained partial raw loss'],
'S29':['svkg/docs/work-state.md','Live queue versus historical prose; failed independent review remains explicit'],
'S30':['meertecha_arcade/factory/assessment.md','58 development checks do not establish enjoyment/control effectiveness'],
'S31':['udop/docs/evaluation.md','Technical evidence versus pending analyst value judgment'],
'S32':['atelier/docs/operations.md','Pinned inputs, bounded scope, denied traversal and failed outputs retained'],
'S33':['every_game/docs/m3-schema-order-diagnostic.md','Specific schema-order hypothesis, no causal inference from diagnostics'],
'S34':['every_game/docs/m3-composed-schema-diagnostic.md','Targeted diagnostic with unchanged provider/safety/acceptance'],
'S35':['every_game/docs/m3-third-person-scope-correction.md','Scope correction and preserved historical evidence'],
'S36':['every_game/docs/m3-current-cumulative-video.md','Exact asset identity, automated footage and hardware/owner limits'],
'S37':['classwork/AGENTS.md','Canonical concepts, pinned ontology and learner-private workspace boundary'],
'S38':['atmospheric-processes-knowledge-graph/AGENTS.md','Separate teaching/bundle modes and ignored local lesson plans'],
'S39':['ashwake/AGENTS.md','Causal edges require evidence and graph reconciliation'],
'S40':['onboarding/README.md','Partial external setup and reconcile-before-retry'],
'S41':['wired_to_survive/evidence/factory-experiments.json','40-trial local experiment remains inconclusive'],
'S42':['wired_to_survive/evidence/factory-native-qualification.json','Native hook observations versus owner-reported trust and waived re-review'],
'S43':['reactive_space/README.md','Authenticated sender, reducer-only writes and fail-closed policy'],
'S44':['agent/README.md','MCP discovery failure stops entire execution'],
'S45':['cards/README.md','Deterministic engine, atomic plans, idempotency and hidden-state boundaries'],
'S46':['fmodel/AGENTS.md','Risk-proportionate checks and preserve unrelated changes'],
'S47':['games/AGENTS.md','Unimplemented native gates remain blocked'],
'S48':['meertecha_arcade/AGENTS.md','Evidence-based rule ledger and distinct native release gates'],
'S49':['wired_to_survive/AGENTS.md','Bounded repairs, worktree ownership and remote-main acceptance'],
'S50':['semantic_search/docs/verification/factory-readiness.md','Framework, pilot and product readiness are distinct'],
'S51':['coding_evals/README.md','Task/harness/model matrix and graded metrics are planned tooling'],
'S52':['videos/AGENTS.md','Diagnose environment separately from code, bounded native validation'],
'S53':['example/AGENTS.md','Outcome verification and containment precede wider autonomy'],
'S54':['backup.resume/AGENTS.md','Single canonical resume source, no invented facts, regenerate exports after each logical change'],
'S55':['resume/AGENTS.md','Completion includes verification and coherent commits; blocked checks remain unknown'],
'S56':['tclasen/AGENTS.md','Canonical identity, evidence truth states and history preservation; personal graph content excluded'],
}
docs={}
for sid,(rel,note) in DOCS.items():
    p=BASE/rel
    try:
        raw=p.read_bytes();docs[sid]={'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'review':'targeted documentary review; source claims not rerun','finding_scope':note}
    except OSError as e:docs[sid]={'path':rel,'error':type(e).__name__}
# Hash top-level policy/readme files without preserving personal content.
roots=[]
for top in sorted(BASE.iterdir()):
    if not top.is_dir() or top.is_symlink():continue
    for name in ['AGENTS.md','README.md','PROJECT.md']:
        p=top/name
        if p.is_file():
            raw=p.read_bytes(); roots.append({'path':str(p.relative_to(BASE)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'review':'entrypoint purpose/process inspection; private biography/resume payload not reproduced'})
# Explicitly revisit factory_catalog/build, excluded by the broad scanner.
build=[];excluded=[]
prune={'.git','node_modules','.venv','__pycache__','.cache','.next','target','dist','vendor'}
for d,ds,fs in os.walk(BASE/'factory_catalog/build',followlinks=False):
    for n in list(ds):
        p=pathlib.Path(d)/n
        if n in prune or p.is_symlink():ds.remove(n);excluded.append(str(p.relative_to(BASE)))
    for n in fs:
        p=pathlib.Path(d)/n
        if p.is_symlink() or not p.is_file() or p.suffix.lower() not in {'.md','.txt','.json','.jsonl','.csv'}:continue
        s=p.stat();row={'path':str(p.relative_to(BASE)),'bytes':s.st_size}
        if s.st_size<=32*1024*1024:
            h=hashlib.sha256()
            with p.open('rb') as f:
                for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
            row['sha256']=h.hexdigest()
        else:row['excluded_content']='over-32-MiB'
        build.append(row)
(OUT/'project-learning-evidence.json').write_text(json.dumps({'documentary_sources':docs,'top_level_entrypoints':roots,'ignored_build_exception':build,'build_exception_pruned_directories':excluded,'limits':'No raw prompts, private biography/resume data, credentials or arbitrary environment copied. Hashes identify source; narrative report preserves transferable findings. Most corpus files only inventoried/fingerprinted.'},indent=2)+'\n')
print(json.dumps({'documentary_sources':len(docs),'missing':{k:v for k,v in docs.items() if 'error'in v},'entrypoints':len(roots),'build_candidates':len(build),'build_excluded':len(excluded)}))
