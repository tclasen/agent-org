"""Fixed independent EVAL-000001 criteria, replayable against either source.

Normal unittest discovery checks the candidate only. Explicit --baseline replay
qualifies retained defects separately, without requiring broken behavior in CI.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import tempfile
import unittest

FACTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY))
sys.path.insert(0, str(FACTORY / 'instrumentation'))
from instrumentation import records as candidate


RELATIONS = ('blocked_by', 'requires', 'validates', 'awaits_approval',
             'awaits_condition', 'parent_of', 'discovered_from', 'supersedes',
             'related_to')
FAMILIES = (('REQ', 'requirements'), ('TASK', 'tasks'), ('RUN', 'runs'),
            ('APP', 'approvals'), ('DEC', 'decisions'), ('EVAL', 'evaluations'),
            ('EXP', 'experiments'), ('ART', 'artifacts'), ('INIT', 'initiatives'),
            ('INTENT', 'intents'), ('PLAN', 'plans'), ('WF', 'workflows'),
            ('CAP', 'capabilities'), ('TRG', 'triggers'))
TARGETS = (('organization', 'organization'), ('project', 'project'),
           ('cross_boundary', 'cross-boundary'))


def load_source(path):
    """Load the exact retained source; common.py remains the pinned dependency."""
    spec = importlib.util.spec_from_file_location('regression_records', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def record(module, identifier='TASK-000001', **updates):
    fields = {'ID': identifier, 'Target System': 'organization',
              'Change Classification': 'organization', 'Authorized Scope': 'agent-org/**',
              'Affected Paths or Resources': 'agent-org/**', 'Owning Role': 'Developer',
              'Related Requirements': 'REQ-000001', 'Related Tasks': 'none',
              'Approval Requirements': 'APP-000001'}
    if identifier.startswith('TASK-'):
        fields.update({'Status': 'ready', 'Parent': 'none', 'Dependencies': 'none',
                       'Dependency Type': 'blocked_by', 'Plan Approval': 'APP-000001',
                       'Authorized': 'yes'})
    fields.update(updates)
    return module.Record(Path(identifier + '.md'), fields)


def graph_cases(module):
    """Independent acceptance expectations; no use of module relation constants."""
    grant = record(module, 'APP-000001', Status='approved')
    subject = record(module, 'TASK-000002', Status='in_review',
                     **{'Candidate Hash': 'a' * 64})

    def graph(task, others=(subject,), extra=()):
        return module.validate_graph({r.id: r for r in (grant, task, *others, *extra)})

    yield ('review_in_review_subject', True,
           graph(record(module, Dependencies=subject.id, **{'Dependency Type': 'validates'})))
    for relation in ('blocked_by', 'requires', 'awaits_approval', 'awaits_condition'):
        for status in ('ready', 'in_progress'):
            yield (f'{relation}_{status}_unaccepted', False,
                   graph(record(module, Status=status, Dependencies=subject.id,
                                **{'Dependency Type': relation})))
    yield ('missing_review_subject', False,
           graph(record(module, Dependencies=subject.id,
                        **{'Dependency Type': 'validates'}), others=()))
    for relation in RELATIONS:
        yield (f'self_dependency_{relation}', False,
               graph(record(module, Dependencies='TASK-000001',
                            **{'Dependency Type': relation})))
    yield ('parent_selflink', False, graph(record(module, Parent='TASK-000001')))
    yield ('parent_cycle', False,
           graph(record(module, Parent=subject.id),
                 others=(record(module, subject.id, Parent='TASK-000001'),)))
    for relation in ('blocked_by', 'requires'):
        yield (f'{relation}_cycle', False,
               graph(record(module, Status='blocked', Dependencies=subject.id,
                            **{'Dependency Type': relation}),
                     others=(record(module, subject.id, Status='blocked',
                                    Dependencies='TASK-000001', **{'Dependency Type': relation}),)))
        yield (f'{relation}_accepted_subject', True,
               graph(record(module, Dependencies=subject.id, **{'Dependency Type': relation}),
                     others=(record(module, subject.id, Status='accepted',
                                    **{'Acceptance Evidence': 'pinned', 'Intent Reconciliation': 'matched'}),)))
    for field, value in (('Authorized', 'no'), ('Plan Approval', 'APP-999999'),
                         ('Budget Available', 'no'), ('Capability Available', 'no')):
        yield ('review_guard_' + field, False,
               graph(record(module, Dependencies=subject.id,
                            **{'Dependency Type': 'validates', field: value})))


def tree_result(module, identifier, directory, target='organization', classification=None):
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        items = [(record(module, 'REQ-000001'), 'requirements/organization'),
                 (record(module, 'APP-000001', Status='approved'), 'approvals')]
        item = record(module, identifier, **{'Target System': target,
                                            'Change Classification': classification or target})
        # A tested canonical requirement/approval replaces its support record.
        items = [(r, d) for r, d in items if r.id != item.id] + [(item, directory)]
        for entry, location in items:
            path = root / location / entry.path
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('\n'.join(f'- {key}: {value}' for key, value in entry.fields.items()) + '\n')
        return module.validate_tree(root)['errors']


def tree_cases(module):
    yield ('task_in_requirements', False, tree_result(module, 'TASK-000001', 'requirements/organization'))
    yield ('requirement_in_tasks', False, tree_result(module, 'REQ-000001', 'tasks/organization'))
    for prefix, directory in FAMILIES:
        identifier = prefix + '-000001'
        valid_directory = directory + '/organization' if prefix in ('TASK', 'REQ') else directory
        yield (f'family_valid_{prefix}', True, tree_result(module, identifier, valid_directory))
        wrong = 'tasks' if directory != 'tasks' else 'requirements'
        yield (f'family_wrong_{prefix}', False, tree_result(module, identifier, wrong + '/organization'))
    for prefix, family in (('TASK', 'tasks'), ('REQ', 'requirements')):
        for suffix in ('', '/unknown', '/cross_boundary', '/organization/deeper'):
            yield (f'canonical_{prefix}_{suffix or "flat"}', False,
                   tree_result(module, prefix + '-000001', family + suffix))
    for prefix, family in FAMILIES:
        for target, correct_directory in TARGETS:
            for directory_target, directory in TARGETS:
                yield (f'class_{prefix}_{target}_in_{directory}', target == directory_target,
                       tree_result(module, prefix + '-000001', family + '/' + directory, target))
            other_target = 'project' if target != 'project' else 'organization'
            yield (f'class_metadata_{prefix}_{target}', False,
                   tree_result(module, prefix + '-000001', family + '/' + correct_directory,
                               target, other_target))


def replay(module):
    return [{'case': name, 'expected_valid': valid, 'actual_valid': not errors,
             'passed': valid == (not errors), 'errors': errors}
            for name, valid, errors in (*graph_cases(module), *tree_cases(module))]


def qualify_baseline(results):
    """Assert the three independently supplied defects only in explicit replay."""
    indexed = {row['case']: row for row in results}
    required_failures = ('review_in_review_subject', 'self_dependency_related_to',
                         'task_in_requirements')
    guardrails = ('blocked_by_ready_unaccepted', 'requires_ready_unaccepted',
                  'missing_review_subject', 'parent_selflink', 'parent_cycle',
                  'blocked_by_cycle', 'requires_cycle')
    return (all(not indexed[name]['passed'] for name in required_failures)
            and all(indexed[name]['passed'] for name in guardrails))


class ValidatorRegressions(unittest.TestCase):
    def test_independent_criteria(self):
        for result in replay(candidate):
            with self.subTest(case=result['case']):
                self.assertTrue(result['passed'], result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    args = parser.parse_args()
    source = args.baseline or Path(candidate.__file__)
    module = load_source(source) if args.baseline else candidate
    results = replay(module)
    qualified = qualify_baseline(results) if args.baseline else all(r['passed'] for r in results)
    print(json.dumps({'mode': 'baseline_qualification' if args.baseline else 'candidate',
                      'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                      'workload_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'python': sys.version, 'platform': platform.platform(),
                      'case_count': len(results), 'passing_cases': sum(r['passed'] for r in results),
                      'qualified': qualified, 'results': results}, indent=2, sort_keys=True))
    raise SystemExit(0 if qualified else 1)
