#!/usr/bin/env python3
"""Safely derive allowlisted counts from legacy records. Never import legacy code."""
import collections, csv, datetime, hashlib, json, pathlib, sqlite3
BASE=pathlib.Path('/Users/Shared/old/projects')
OUT=pathlib.Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
sources={}; result={}; errors=[]
def source(rel):
    p=BASE/rel
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    sources[rel]={'bytes':p.stat().st_size,'sha256':h.hexdigest()}
    return p
def data(rel):return json.loads(source(rel).read_text())
def rows(rel):
    with source(rel).open() as f:
        return [json.loads(l) for l in f if l.strip()]

fe=[]
for p in sorted((BASE/'factory_evals/.factory-evals/jobs').glob('*/report.json')):
    rel=str(p.relative_to(BASE)); x=data(rel); grouped=collections.defaultdict(list)
    for r in x['rows']:grouped[r['condition']].append(r)
    groups={}
    for k,rs in grouped.items():
        scored=[r for r in rs if r.get('result') is not None]
        telemetry=[r['result'].get('telemetry',{}) for r in scored]
        groups[k]={'assigned':len(rs),'scored':len(scored),'pass':sum(r['result'].get('pass') is True for r in scored),'states':dict(collections.Counter(r['state'] for r in rs)),
                   'telemetry_sums':{m:sum(t[m] for t in telemetry if isinstance(t.get(m),(int,float))) for m in ['input_tokens','output_tokens','tool_calls','elapsed_seconds']},
                   'missing_cost':sum(t.get('cost_usd') is None for t in telemetry)}
    fe.append({'source':rel,'groups':groups,'source_comparisons':x['comparisons'],'source_decision':x['decision'],'limits':'Fixed case pilot; unstarted/unscored never treated as failures or successes. Report is source grading, not re-executed grading.'})
result['factory_evals']=fe

wr={}
for name in ['summary.json','screen-summary.json','supplementary-v1.json','supplementary-v2.json','supplementary-v3.json']:
    rel='work/docs/evals/2026-10-08-outcomes/'+name;x=data(rel)
    wr[name]={k:x[k] for k in ['attempted','planned','original_plan_episodes','completed_matrix','compliant_successes','elapsed_seconds','hard_failure_episodes'] if k in x}
    if 'groups' in x:
        groups=collections.defaultdict(lambda:collections.Counter())
        for r in x['groups']:
            c=groups[r['cell']]; c['episodes']+=r['attempted'];c['successes']+=r['successes'];c['seconds']+=r['total_seconds'];c['tool_calls']+=r['tool_calls']
        wr[name]['cells']={k:dict(v) for k,v in groups.items()}
result['work_outcomes']=wr
csvresults={}
for family in ['2026-10-08-outcomes','2026-10-08-screening']:
    rel='work/docs/evals/'+family+'/metrics.csv'
    with source(rel).open() as f:rs=list(csv.DictReader(f))
    o={'rows':len(rs),'sums':{k:sum(float(r[k]) for r in rs if r.get(k) not in (None,'')) for k in ['elapsed_seconds','tool_calls','tool_errors','sessions','timeouts','usage_sessions','partial_usage_sessions','checks_passed','checks_total'] if any(k in r for r in rs)}}
    if family.endswith('outcomes'):o['compliant_successes']=sum(r.get('compliant_success')=='True' for r in rs)
    else:o['all_primary_checks']=sum(r.get('checks_passed')==r.get('checks_total') for r in rs);o['usage_statuses']=dict(collections.Counter(r.get('usage_status') for r in rs))
    o['limits']='CSV scalar recomputation. Automated hard_failure fields do not replace separately recorded manual findings. Missing usage is unknown.'
    csvresults[family]=o
result['work_csv_recomputed']=csvresults

lessons=rows('competition/lessons/records.jsonl');latest={}
for r in lessons:latest[r['lesson_id']]=r
result['competition_lessons']={'records':len(lessons),'unique_lesson_ids':len(latest),'all_record_statuses':dict(collections.Counter(r.get('status','missing') for r in lessons)),'latest_record_statuses':dict(collections.Counter(r.get('status','missing') for r in latest.values())),'limits':'Counts are journal records/status assertions; adoption and verification labels are not independently re-tested here.'}
cr=[]
for p in sorted((BASE/'competition/runs/instruction-effects').iterdir()):
    if not p.is_dir():continue
    row={'run':p.name}
    q=p/'state.json'
    if q.exists():
        x=data(str(q.relative_to(BASE)));row['source_state_status']=x.get('status')
        a=x.get('accepted',{});row['builder_entries']=len(a) if isinstance(a,(list,dict)) else None
        if isinstance(a,dict):row['accepted_value_types']=dict(collections.Counter(type(v).__name__ for v in a.values()))
    q=p/'events.jsonl'
    if q.exists():
        rs=rows(str(q.relative_to(BASE)));row['event_rows']=len(rs);row['event_kinds']=dict(collections.Counter(str(r.get('kind',r.get('event','missing'))) for r in rs))
    cr.append(row)
result['competition_run_inventory']=cr

dbs=[]
for rel in ['penny/.penny-factory/events.sqlite3','wired_to_survive/.wired-factory/events.sqlite3']:
    p=source(rel); c=sqlite3.connect('file:'+str(p)+'?mode=ro&immutable=1',uri=True)
    names={r[0] for r in c.execute("select name from sqlite_master where type='table'")};o={'source':rel,'tables':{t:c.execute('select count(*) from '+t).fetchone()[0] for t in ['events','bundles','provenances'] if t in names}}
    if 'events' in names:
        ks=collections.Counter();timestamps=[];streams=set();runs=set()
        for (raw,) in c.execute('select record from events'):
            r=json.loads(raw);ks[r.get('kind','missing')]+=1
            if r.get('timestamp'):timestamps.append(r['timestamp'])
            streams.add(r.get('stream_id'));runs.add(r.get('run_id'))
        o.update(event_kinds=dict(ks),timestamp_min=min(timestamps) if timestamps else None,timestamp_max=max(timestamps) if timestamps else None,streams=len(streams),nonnull_runs=len(runs-{None}))
    if 'bundles' in names:o['acknowledged_bundles']=c.execute('select count(*) from bundles where acknowledged_at is not null').fetchone()[0]
    o['sidecar_names']=[q.name for q in p.parent.glob(p.name+'-*')]
    o['limits']='Read-only immutable SQLite main-file observation; no chain validation, archive download or acceptance inference. Nonempty sidecars would require separate consistent snapshot review.'
    dbs.append(o);c.close()
result['observation_databases']=dbs

fr=[]
for family in ['luna-56-20261001','luna-60-20261001']:
    prefix='factory_catalog/build/evals/'+family+'/'
    manifest=data(prefix+'manifest.json');rs=rows(prefix+'attempts.jsonl')
    entry={'family':family,'manifest_assignments':len(manifest),'manifest_conditions':dict(collections.Counter(r['condition_id'] for r in manifest)),'ledger_records':len(rs),'ledger_kinds':dict(collections.Counter(r['kind'] for r in rs)),'limits':'Lifecycle records, not scored passes. Manifest is a plan; reservations/restarts are not independent replicates. Objective outcomes are original primary scorer assertions, not regraded here; incomplete unbalanced assignment is not a treatment effect.'}
    idx={r['run_id']:r for r in manifest}; groups=collections.defaultdict(collections.Counter);failed=collections.Counter()
    for p in sorted((BASE/prefix/'runs').glob('*/objective.json')):
        x=data(str(p.relative_to(BASE)));m=idx.get(p.parent.name);condition=m['condition_id'] if m else 'not-in-manifest';g=groups[condition]
        g['scored']+=1;g['pass']+=x.get('pass') is True;g['structured_false_completion']+=x.get('structured_false_completion') is True
        for k,v in x.get('checks',{}).items():
            if not v:failed[k]+=1
    entry['primary_objective_by_condition']={k:dict(v) for k,v in groups.items()};entry['failed_check_labels']=dict(failed)
    fr.append(entry)
result['factory_catalog_ignored_evals']=fr

x=data('penny/.penny-factory/evidence/143-layout/integrated-acceptance/integrated-acceptance-report.json')
result['penny_143_source_claim']={'integrated_commit':x['integratedCommit'],'disposition':x['disposition'],'raw_acceptance':{k:v for k,v in x['rawAcceptance'].items() if k in ['rawStats','actualCases','uniqueCases','inventoryMatches','perProject','jsonAttachmentsDecoded','fullNativeSnapshotsAudited']},'limits':'Extracted reported acceptance; no browser rerun or global product/human acceptance.'}
x=data('penny/.penny-factory/worktrees/143-integrated-acceptance/test-results/results.json')
tests=[]
def visit(suite):
    for spec in suite.get('specs',[]):
        for test in spec.get('tests',[]):tests.append(test)
    for child in suite.get('suites',[]):visit(child)
for suite in x.get('suites',[]):visit(suite)
result['penny_143_raw_recomputed']={'tests':len(tests),'project_counts':dict(collections.Counter(t.get('projectName') for t in tests)),'test_statuses':dict(collections.Counter(t.get('status') for t in tests)),'result_statuses':dict(collections.Counter(r.get('status') for t in tests for r in t.get('results',[]))),'retry_values':dict(collections.Counter(str(r.get('retry')) for t in tests for r in t.get('results',[]))),'stats':x.get('stats'),'errors_count':len(x.get('errors',[])),'limits':'Direct raw report parsing confirms stored outcome counts only. No browser re-execution. Independent parent derivative git-nested-penny-test-outcomes.json supplies redacted scenario-level detail.'}
x=data('wired_to_survive/evidence/factory-experiments.json')
result['wired_experiment_source_claim']={k:x['experiment'][k] for k in ['pairs_per_workload','baseline','candidate','comparison','result']}
result['commons_final_source_claim']=data('commons/runs/final-validation/validation-summary.json')
x=data('commons/agent-org/factory/reports/synthetic-delivery-v1.factory-1.0.1.report.json')
result['commons_synthetic_source_claim']={k:x[k] for k in ['code_version','metric_definition_version','classification','window','deployment_frequency','change_fail_rate','deployment_rework_rate','failed_deployment_recovery_time','change_lead_time','measurement_health']}

result['observed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
result['method']='Original allowlisted standard-library reader; no imported/executed legacy scripts; exact source hashes retained. Counts recomputed from stored records, evaluator outcomes remain source claims.'
result['source_manifest']=sources
(OUT/'project-learning-metrics.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'source_files':len(sources),'output':'project-learning-metrics.json','database_observations':dbs,'factory_catalog':fr},indent=2))
