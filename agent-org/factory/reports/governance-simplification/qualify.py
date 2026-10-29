#!/usr/bin/env python3
"""Task403 read-only source qualification; writes only the selected JSON report.
No Git, network, subject execution, production-tool mutation or promotion.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import re
import sys
import unicodedata
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIELDS = ('Target System', 'Change Classification', 'Authorized Scope', 'Affected Paths or Resources', 'Owning Role', 'Related Requirements', 'Related Tasks', 'Approval Requirements')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def unfenced(text):
    result, fenced = [], False
    for line in text.splitlines():
        if line.startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if not fenced:
            result.append(line)
    return '\n'.join(result)

def headings(text):
    counts, result = {}, set()
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'[`*_]', '', title).lower()
        title = ''.join(c for c in unicodedata.normalize('NFC', title) if c.isalnum() or c in '_- ')
        slug = title.replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug + (f'-{n}' if n else ''))
    return result

def links(path):
    result = []
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if re.match(r'[a-z]+://|mailto:', target):
            continue
        target = unquote(target.strip('<>'))
        file, _, anchor = target.partition('#')
        dest = (path.parent / file).resolve() if file else path.resolve()
        valid = dest.is_file() and dest.is_relative_to(ROOT)
        if valid and anchor:
            valid = anchor in headings(dest.read_text())
        result.append({'source': str(path.relative_to(ROOT)), 'target': target, 'resolved': str(dest.relative_to(ROOT)) if dest.is_relative_to(ROOT) else 'outside organization', 'valid': valid})
    return result

def inline_proof():
    # Reuse the maintained real manifest fixture; only a temporary fixture is changed.
    module = load_module(ROOT / 'factory/tests/test_context.py', 'qualification_context_tests')
    fixture = module.ContextTests()
    fixture.setUp()
    try:
        path = fixture.root / 'tasks/organization/TASK-000001.md'
        text = path.read_text() + '- Plan Path: tasks/organization/TASK-000001.md\n\n## Inline plan revision 1\n\nOutcome: exact typo correction. Scope: existing assigned instruction. Criterion: corrected spelling with semantics preserved. Verify diff and independent review. Budget: bounded task. Rollback: scoped corrective PR.\n'
        path.write_text(text)
        (fixture.root / 'factory/reports/example/PLAN.md').unlink()
        result = fixture.manifest()
        source = next(s for s in result['sources'] if s['path'] == 'agent-org/tasks/organization/TASK-000001.md')
        okay = {'task', 'plan'} <= set(source['classes']) and source['sha256'] == sha(path.read_bytes())
        return {'passed': okay, 'path': source['path'], 'classes': source['classes'], 'sha256': source['sha256'], 'separate_plan_file': False, 'limit': 'Manifest acceptance proves supported canonical source reuse, not semantic completeness or permission. Fresh review remains required.'}
    finally:
        fixture.doCleanups()

def qualify(final=False, candidate_manifest='candidate-manifest.json'):
    manifest = json.loads((HERE / 'baseline-manifest.json').read_text())
    old = {p: (HERE / item['snapshot']).read_text() for p, item in manifest['sources'].items()}
    current = {p: (ROOT / p).read_text() for p in old}
    checks = []
    def check(name, passed, evidence):
        checks.append({'name': name, 'passed': bool(passed), 'evidence': evidence})
    for p, item in manifest['sources'].items():
        check('baseline:' + p, sha((HERE / item['snapshot']).read_bytes()) == item['sha256'], item['sha256'])
    if final:
        candidate = json.loads((HERE / candidate_manifest).read_text())
        check('frozen-candidate-source-set', set(candidate['sources']) == set(old), sorted(candidate['sources']))
        for p, item in candidate['sources'].items():
            check('frozen-candidate:' + p,
                  sha((ROOT / p).read_bytes()) == item['sha256'] == sha((HERE / item['snapshot']).read_bytes()),
                  item['sha256'])
    for p, digest in json.loads((HERE / 'protocol-hashes.json').read_text()).items():
        check('frozen:' + p, sha((HERE / p).read_bytes()) == digest, digest)
    order = json.loads((HERE / 'ORDERING.json').read_text())
    rng = random.Random(order['seed'])
    expected = {}
    for condition in ('baseline', 'candidate'):
        values = [x['id'] for x in json.loads((HERE / 'CASES.json').read_text())]
        rng.shuffle(values)
        expected[condition] = values
        actual = json.loads((HERE / f'{condition}-cases.json').read_text())
        check('case-permutation:' + condition, [x['id'] for x in actual] == values, values)
    check('single-stream-ordering', expected == order['actual_orders'], expected)
    for p in ('policies/AUTHORITY.md', 'policies/SCOPE_BOUNDARIES.md', 'policies/MEASUREMENT_INDEPENDENCE.md', 'policies/APPROVALS.md', 'policies/ACCEPTANCE.md', 'policies/PLANNING.md', 'shared/RECORD_FORMATS.md', 'shared/CONTEXT_MANAGEMENT.md', 'shared/DESIGN_REVIEW.md'):
        check('unchanged-contract:' + p, current[p] == old[p], sha(current[p].encode()))
    p = 'policies/SELF_IMPROVEMENT.md'
    prefix = old[p].split('## Event-driven lessons and capability review')[0]
    check('prior-evaluator-exact-prefix', current[p].startswith(prefix), {'baseline_sha256': sha(prefix.encode()), 'words': len(prefix.split()), 'covers': 'preregistration, deterministic/stochastic thresholds, guardrails, independence, evaluator changes, rollback'})
    roles = sorted((ROOT / 'agents').glob('*/AGENTS.md'))
    registered = {str(p.relative_to(ROOT)) for p in roles}
    pinned = {p for p in old if p.startswith('agents/') and p.endswith('/AGENTS.md')}
    check('all-active-roles-pinned', registered == pinned, sorted(registered))
    metadata_errors, identity_errors, duty_changes = [], [], []
    for p in current:
        if p == 'AGENTS.md':
            continue
        for field in FIELDS:
            lines = re.findall(r'^- ' + re.escape(field) + r': .+$', unfenced(current[p]), re.M)
            original = re.findall(r'^- ' + re.escape(field) + r': .+$', unfenced(old[p]), re.M)
            if lines != original or (original and len(lines) != 1):
                metadata_errors.append([p, field])
        if p.startswith('agents/'):
            if p.endswith('/AGENTS.md'):
                for field in ('Agent ID', 'Status', 'Capabilities'):
                    original = re.findall(r'^- ' + field + r': .+$', old[p], re.M)
                    if original != re.findall(r'^- ' + field + r': .+$', current[p], re.M):
                        identity_errors.append([p, field])
                if '## Role duties' in old[p]:
                    for paragraph in old[p].split('## Role duties', 1)[1].strip().split('\n\n'):
                        if paragraph not in current[p] and not ((p == 'agents/chief-of-staff/AGENTS.md' and paragraph.startswith('Own active-session organization-level diagnosis')) or (p == 'agents/coordinator/AGENTS.md' and paragraph.startswith('Every observed unexpected problem')) or (p == 'agents/reviewer/AGENTS.md' and paragraph.startswith('For root-cause repairs,') and paragraph.replace('For root-cause repairs,', 'For organization root-cause repairs,') in current[p])):
                            duty_changes.append({'path': p, 'paragraph': paragraph})
    context_changes = []
    for p in current:
        if not (p.startswith('agents/') and p.endswith('/CONTEXT.md')):
            continue
        counterpart = current[p.replace('/CONTEXT.md', '/AGENTS.md')]
        for paragraph in old[p].strip().split('\n\n'):
            # Stable shared orientation/project triggers moved to mandatory core.
            if paragraph.startswith(('#', '-', 'This is stable', 'For enrolled project work,', 'Before a project assignment,')):
                continue
            if paragraph not in current[p] and paragraph not in counterpart:
                context_changes.append({'path': p, 'paragraph': paragraph})
    check('unique-context-orientation-retained', not context_changes, context_changes)
    role_loads = {p: '../../AGENTS.md' in current[p] for p in current if p.startswith('agents/')}
    check('every-role-and-context-links-mandatory-core', all(role_loads.values()), role_loads)
    check('required-metadata-exact', not metadata_errors, metadata_errors)
    check('role-identities-exact', not identity_errors, identity_errors)
    check('unique-role-duties-retained', not duty_changes, duty_changes)
    resource = (ROOT / 'policies/RESOURCE_BUDGETS.md').read_text()
    core = current['AGENTS.md']
    check('existing-actual-capacity-rule-aligned',
          'actual runtime capacity' in resource and 'supersedes older organization worker/depth defaults' in resource
          and 'actual runtime capacity' in core and 'at most three workers plus Coordinator' not in core,
          {'resource_sha256': sha(resource.encode()), 'canonical_rule': 'Existing RESOURCE_BUDGETS actual-capacity rule supersedes repeated worker/depth caps; no new ceiling or resource policy.'})
    shared = current['AGENTS.md']
    obligations = {'scope': r'(?i)scope', 'authority': r'(?i)authority', 'claim': r'(?i)claim', 'dependencies': r'(?i)dependenc', 'handoff': r'(?i)handoff', 'unknown telemetry': r'(?i)unknown telemetry|telemetry.*honest|never invent.*telemetry', 'required sources': r'(?i)missing required', 'project trigger': r'(?i)project.*(source|instruction|profile)|enrolled project'}
    check('canonical-core-obligations', all(re.search(v, shared) for v in obligations.values()), {k: bool(re.search(v, shared)) for k,v in obligations.items()})
    history = old['shared/HANDOFFS.md'].split('## Remote-main policy delivery — proposed closure', 1)[1]
    tail = '## Remote-main policy delivery — proposed closure' + history
    archives = [p for p in HERE.glob('*.md') if p.name not in {'QUALIFICATION.md'} and tail in p.read_text().replace('](../project-cleanup/CLOSURE.md)', '](../factory/reports/project-cleanup/CLOSURE.md)')]
    check('historical-tail-lossless-and-removed', len(archives) == 1 and tail not in current['shared/HANDOFFS.md'], {'tail_sha256': sha(tail.encode()), 'tail_words': len(tail.split()), 'only_allowed_rebase': '../factory/reports/project-cleanup/CLOSURE.md -> ../project-cleanup/CLOSURE.md; inverse rebase must equal complete original tail', 'archives': [p.name for p in archives]})
    link_paths = [ROOT / p for p in current] + archives
    all_links = [item for path in link_paths for item in links(path)]
    check('local-links-and-anchors', all(x['valid'] for x in all_links), {'count': len(all_links), 'failures': [x for x in all_links if not x['valid']]})
    if archives:
        archive_rel = str(archives[0].relative_to(ROOT))
        check('history-recoverable-from-contract', any(x['source'] == 'shared/HANDOFFS.md' and x['resolved'] == archive_rel and x['valid'] for x in all_links), archive_rel)
        # Original snapshot directory differs: recover original relative link destinations explicitly.
        old_targets = {(str((ROOT / 'shared' / t.partition('#')[0]).resolve().relative_to(ROOT)), t.partition('#')[2]) for t in re.findall(r'\[[^\]]*\]\(([^)]+)\)', tail)}
        archive_targets = {(x['resolved'], x['target'].partition('#')[2]) for x in links(archives[0])}
        check('historical-link-destinations-preserved', old_targets <= archive_targets, {'original': sorted(old_targets), 'archive': sorted(archive_targets)})
    census = {}
    for p in current:
        census[p] = {'baseline': len(old[p].split()), 'candidate': len(current[p].split())}
        census[p]['delta'] = census[p]['candidate'] - census[p]['baseline']
    common = ['AGENTS.md', 'policies/AUTHORITY.md', 'policies/SCOPE_BOUNDARIES.md']
    per_role = {}
    for role_path in sorted(pinned):
        context = role_path.replace('/AGENTS.md', '/CONTEXT.md')
        paths = common + [role_path, context]
        counts = {condition: sum(census[p][condition] for p in paths) for condition in ('baseline','candidate')}
        counts['delta'] = counts['candidate'] - counts['baseline']
        counts['paths'] = paths
        per_role[Path(role_path).parent.name] = counts
    check('each-role-contract-shorter', all(v['delta'] < 0 for v in per_role.values()), per_role)
    totals = {condition: sum(v[condition] for v in census.values()) for condition in ('baseline','candidate')}
    totals['delta'] = totals['candidate'] - totals['baseline']
    check('net-scoped-corpus-shorter', totals['delta'] < 0, totals)
    proof = inline_proof()
    check('existing-inline-plan-reuse', proof['passed'], proof)
    passed = all(x['passed'] for x in checks)
    return {'stage': 'final-source-snapshot' if final else 'preparation', 'disposition': ('passed' if passed else 'failed') if final else 'not-final', 'checks_passed': sum(x['passed'] for x in checks), 'checks_total': len(checks), 'checks': checks, 'source_hashes': {p: sha((ROOT/p).read_bytes()) for p in current}, 'word_count_method': 'Python str.split whitespace-delimited words, metadata included. Corpus counts each manifest path once. Role contracts count core/authority/scope once plus its own AGENTS and CONTEXT; action-specific sources excluded. Archived words retained but excluded from current instruction corpus. No tokens, capacity, productivity or universal compliance inference.', 'word_census': census, 'per_role_contracts': per_role, 'corpus': totals, 'limits': ['Static checks do not establish semantic equivalence; independent Reviewer must assess all changed duties/routing and evaluator semantics.', 'Behavioral executions and independent scoring are separate and may be missing.', 'No Git scope/remote-main/delivery verification performed by this worker.']}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--final', action='store_true', help='Use only after parent reports source integration ready')
    parser.add_argument('--candidate-manifest', choices=['candidate-manifest.json', 'candidate-v2-manifest.json', 'candidate-publication-manifest.json'], default='candidate-manifest.json')
    parser.add_argument('--output', choices=['test-results.json', 'test-results-v2.json', 'test-results-publication.json'], default='test-results.json')
    args = parser.parse_args()
    expected_output = {'candidate-manifest.json': 'test-results.json', 'candidate-v2-manifest.json': 'test-results-v2.json', 'candidate-publication-manifest.json': 'test-results-publication.json'}[args.candidate_manifest]
    if args.output != expected_output:
        parser.error('candidate manifest and versioned output must match')
    destination = (HERE / args.output).resolve()
    if destination.parent != HERE or destination.name not in {'test-results.json', 'test-results-v2.json', 'test-results-publication.json'}:
        parser.error('output must be an assigned versioned test-results file')
    previous = json.loads(destination.read_text()) if destination.exists() else {}
    result = qualify(args.final, args.candidate_manifest)
    result['candidate_manifest'] = args.candidate_manifest
    result['candidate_manifest_sha256'] = sha((HERE / args.candidate_manifest).read_bytes()) if args.final else 'not-final'
    if args.candidate_manifest in {'candidate-v2-manifest.json', 'candidate-publication-manifest.json'}:
        original = HERE / 'candidate1-retained/test-results.json'
        result['prior_results'] = {'path': str(original.relative_to(HERE)), 'sha256': sha(original.read_bytes()), 'disposition': 'candidate1 remains rejected; source static pass does not supersede behavioral rejection'}
        if not previous:
            previous = json.loads(original.read_text())
    result['preparation_attempts'] = previous.get('preparation_attempts', [])
    result['artifact_maintenance_observations'] = previous.get('artifact_maintenance_observations', [])
    result['qualifier_sha256'] = sha(Path(__file__).read_bytes())
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('stage','disposition','checks_passed','checks_total','corpus')}))
    sys.exit(1 if args.final and result['disposition'] != 'passed' else 0)
