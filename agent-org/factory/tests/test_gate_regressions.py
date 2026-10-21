"""APP-000004 / ART-000004 fixed semantic replay; eligibility is not adoption.

Only plan version and evaluator source pins, with dependent hashes, are substituted
between versions. The retained 22-case script remains byte-for-byte unchanged.
"""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import types
import unittest

import test_improvement as T
import test_dora as D

ROOT = Path(__file__).resolve().parents[1]
RETAINED_SHA = 'fcdf4d23e1d089fcdc271b45232f93440fb0a522cd7155d3bc08edd24c7d7442'
SUBSTITUTIONS = [
    'plan.version: 1.0.0 -> 1.0.1',
    'plan.evaluator_code_hash: retained source SHA256 -> candidate source SHA256',
    'context.approved_evaluator_code_hash: same source substitution (synthetic trust fixture only)',
    'context.registered_plan_hash, evidence.plan_hash: derived plan digest',
    'approvals[*].plan_hash, approvals[*].evidence_hash: derived association digests',
    'DORA calculator/default definition version: 1.0.0 -> 1.0.1; definition digest follows version',
]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OLD_GATE = load('retained_gate_100', ROOT / 'baselines/gate-1.0.0/improvement.py')
OLD_DORA = load('retained_dora_100', ROOT / 'baselines/dora-1.0.0/calculator.py')


def bundle_for(gate, claim='repair'):
    """Shared semantic fixture; no defect input is rewritten for either side."""
    b = T.bundle(claim)
    b['plan']['version'] = gate.VERSION
    b['plan']['evaluator_code_hash'] = gate.evaluator_digest()
    b['context']['approved_evaluator_code_hash'] = gate.evaluator_digest()
    rebind(b)
    return b


def rebind(b):
    b['context']['registered_plan_hash'] = T.gate.digest(b['plan'])
    b['evidence']['plan_hash'] = T.gate.digest(b['plan'])
    T.reapprove(b)


def decision(gate, b):
    return gate.evaluate(b['plan'], b['evidence'], b['approvals'], b['context'])


def replay_original(gate, dora):
    """Run every retained observation, injecting only source/fixture adapters."""
    path = ROOT / 'reports/RUN-000011/adversarial.py'
    source = path.read_text()
    if hashlib.sha256(path.read_bytes()).hexdigest() != RETAINED_SHA:
        raise AssertionError('retained workload changed')
    # Replace module imports only, retaining every mutation, assertion and label.
    source = source.replace('import test_improvement as T', 'T = injected_T')
    source = source.replace('import test_dora as D', 'D = injected_D')
    adapter_t = types.SimpleNamespace(gate=gate, bundle=lambda claim='repair': bundle_for(gate, claim),
                                      reapprove=T.reapprove, decision=lambda b: decision(gate, b))
    adapter_d = types.SimpleNamespace(dora=dora, fixture=D.fixture,
        report=lambda events=None, **kw: dora.calculate(D.fixture() if events is None else events,
                                                       D.CLASSIFICATION, D.START, D.END, **kw))
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        exec(compile(source, str(path), 'exec'), {'injected_T': adapter_t, 'injected_D': adapter_d})
    return [json.loads(line) for line in capture.getvalue().splitlines()]


def typed_cases():
    """Preregistered invalid/missing JSON values plus controls for each family."""
    invalid = [False, 0, 1, {}, [], '']
    cases = []
    for field in ('authority_hash', 'plan_hash'):
        for value in invalid + [None, '   ']:
            cases.append(('evidence ' + field + ' ' + repr(value), 'repair', ('evidence', field), value, False))
    for value in invalid + [None, '   ']:
        cases.append(('regression pin ' + repr(value), 'repair', ('evidence', 'repair', 'independent_regression_hash'), value, False))
    for value in (0, 1, {}, [], 'true', 'false', '', None):
        cases.append(('change flag ' + repr(value), 'repair', ('plan', 'changes_evaluator'), value, False))
    for claim in ('outcome', 'efficiency'):
        for value in (None, False, '100', {}, [], float('inf')):
            # Nonfinite JSON rejected by canonicalization, never interpreted as benefit.
            cases.append((claim + ' attempt value ' + repr(value), claim,
                          ('evidence', 'pairs', 0, 'candidate_attempts', 0, 'value'), value, False))
        for status in (None, False, 0, {}, [], 'unknown', 'passed '):
            cases.append((claim + ' attempt status ' + repr(status), claim,
                          ('evidence', 'pairs', 0, 'candidate_attempts', 0, 'status'), status, False))
    return cases


class GateRegressionTests(unittest.TestCase):
    def test_retained_22_observations_and_controls(self):
        old = replay_original(OLD_GATE, OLD_DORA)
        new = replay_original(T.gate, D.dora)
        self.assertEqual(len(old), 22)
        self.assertEqual([r['case'] for r in old], [r['case'] for r in new])
        for prior, current in zip(old, new):
            label = prior['case']
            if label.startswith('F'):
                self.assertEqual(prior['decision'], 'pass', label)
                if label.startswith('F3'):
                    self.assertTrue(current['checkpoint_required'], label)
                    self.assertEqual(current['decision'], 'pass')
                else:
                    self.assertNotEqual(current['decision'], 'pass', label)
                self.assertNotIn('unsupported gate version', current.get('reasons', []))
            elif label == 'sparse unlinked recovery':
                self.assertEqual(prior['health']['status'], 'complete')
                self.assertEqual(current['health']['status'], 'partial')
                self.assertTrue(any(x['reason'] == 'missing_failure_causality' for x in current['health']['issues']))
                self.assertEqual(prior['service'], current['service'])
            elif label == 'missing causality excludes failure and rework':
                self.assertEqual(prior['decision'], current['decision'])
                expected = copy.deepcopy(prior['health'])
                expected['issues'].append({'event_id': 'r1', 'reason': 'missing_failure_causality'})
                expected['issues'].sort(key=lambda i: (i['event_id'], i['reason']))
                self.assertEqual(expected, current['health'])
            elif label.startswith('sparse '):
                self.assertEqual(prior, current)
            elif label.startswith('control '):
                self.assertEqual(prior['decision'], current['decision'], label)
            else:
                self.assertEqual(prior, current)

    def test_known_invalid_types_never_establish_benefit(self):
        for label, claim, path, value, _ in typed_cases():
            with self.subTest(label=label):
                b = bundle_for(T.gate, claim)
                target = b
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                # Retain malformed pins deliberately. Rebind only declared plan changes.
                if path[0] == 'plan':
                    rebind(b)
                elif value != float('inf'):
                    T.reapprove(b)
                result = decision(T.gate, b)
                self.assertNotEqual(result['decision'], 'pass')
                self.assertFalse(result['benefit'])

    def test_required_pin_types_in_plan_context_and_approvals(self):
        paths = [('plan', key + '_hash') for key in T.gate.PINS]
        paths += [('context', key) for key in ('authority_hash', 'registered_plan_hash', 'approved_evaluator_code_hash', 'current_head')]
        paths += [('approvals', 0, key) for key in ('candidate_hash', 'candidate_head', 'evidence_hash', 'agent_id')]
        for path in paths:
            for value in (False, 0, {}, [], None, '', '   '):
                b = bundle_for(T.gate)
                target = b
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                self.assertNotEqual(decision(T.gate, b)['decision'], 'pass', (path, value))

    def test_recursive_exact_boolean_replay_and_positive_controls(self):
        for value in (True, False, 'failed', 'true', 0, 1, {}, [], None):
            b = bundle_for(T.gate)
            b['plan']['changes_evaluator'] = True
            b['context']['adversarial_fixtures_hash'] = 'prior-adversarial'
            b['evidence'].update(prior_evaluator_hash=b['context']['approved_evaluator_hash'],
                                 adversarial_fixtures_hash='prior-adversarial', dual_version_replay=value)
            rebind(b)
            self.assertEqual(decision(T.gate, b)['decision'] == 'pass', value is True, repr(value))
        for gate in (OLD_GATE, T.gate):
            for claim in ('repair', 'outcome', 'efficiency'):
                result = decision(gate, bundle_for(gate, claim))
                self.assertEqual(result['decision'], 'pass', result)
                if claim != 'repair':
                    self.assertEqual(result['benefit']['interval_95'], [10.0, 10.0])
                    self.assertEqual(result['benefit']['relative_benefit'], .1)

    def test_attempt_accounting_unknown_rows_and_cumulative_checkpoint(self):
        for claim in ('outcome', 'efficiency'):
            for supplied in (0, 39, 41):
                b = bundle_for(T.gate, claim)
                b['evidence']['usage']['attempts'] = supplied
                T.reapprove(b)
                self.assertNotEqual(decision(T.gate, b)['decision'], 'pass')
            for attempts in (None, [], [None], [False], ['unknown']):
                b = bundle_for(T.gate, claim)
                b['evidence']['pairs'][0]['candidate_attempts'] = attempts
                T.reapprove(b)
                self.assertNotEqual(decision(T.gate, b)['decision'], 'pass')
        for prior, current, expected in ((2819, 60, False), (2820, 60, True), (2850, 60, True), (0, 2880, True)):
            b = bundle_for(T.gate)
            b['context']['prior_consumed_seconds'] = prior
            b['evidence']['usage']['active_seconds'] = current
            T.reapprove(b)
            self.assertEqual(decision(T.gate, b)['checkpoint_required'], expected)

    def test_dora_orphan_failure_rejected_causality_and_followup(self):
        for events in ([D.fixture()[-1]], [e for e in D.fixture() if e['type'] != 'failure']):
            prior = OLD_DORA.calculate(events, D.CLASSIFICATION, D.START, D.END)
            current = D.report(events)
            self.assertEqual(prior['services'], current['services'])
            self.assertTrue(any(i['event_id'] == 'r1' and i['reason'] == 'missing_failure_causality'
                                for i in current['measurement_health']['issues']))
            self.assertEqual(current['services']['service-a']['failed_deployment_recovery_time']['sample_size'], 0)
        events = D.fixture()
        events[4]['payload']['causal_evidence'] = None
        self.assertTrue(any(i['event_id'] == 'r1' for i in D.report(events)['measurement_health']['issues']))
        future = [copy.deepcopy(D.fixture()[-1])]
        future[0]['occurred_at'] = '2026-01-04T00:00:00Z'
        self.assertEqual(D.report(future)['measurement_health']['status'], 'complete')
        for dora in (OLD_DORA, D.dora):
            r = dora.calculate([], D.CLASSIFICATION, D.START, D.END)
            self.assertIsNone(r['services']['service-a']['deployment_frequency']['per_day'])

    def assert_missing_attempt_container_is_inconclusive(self, claim, mutation):
        # RUN17's six independent inputs: all rows remain, usage stays at 40,
        # and one candidate attempt container contributes an unknown count.
        for gate in (OLD_GATE, T.gate):
            b = bundle_for(gate, claim)
            pair = b['evidence']['pairs'][0]
            if mutation == 'missing':
                del pair['candidate_attempts']
            else:
                pair['candidate_attempts'] = None if mutation == 'null' else []
            T.reapprove(b)
            result = decision(gate, b)
            self.assertEqual(result['decision'], 'inconclusive', (claim, mutation, result))
            self.assertFalse(result['benefit'])
            self.assertEqual(result['reasons'], [])
            self.assertIn('all attempts including failures/retries required', result['measurement_gaps'])

    def test_outcome_missing_attempt_container_is_inconclusive(self):
        self.assert_missing_attempt_container_is_inconclusive('outcome', 'missing')

    def test_outcome_null_attempt_container_is_inconclusive(self):
        self.assert_missing_attempt_container_is_inconclusive('outcome', 'null')

    def test_outcome_empty_attempt_container_is_inconclusive(self):
        self.assert_missing_attempt_container_is_inconclusive('outcome', 'empty')

    def test_efficiency_missing_attempt_container_is_inconclusive(self):
        self.assert_missing_attempt_container_is_inconclusive('efficiency', 'missing')

    def test_efficiency_null_attempt_container_is_inconclusive(self):
        self.assert_missing_attempt_container_is_inconclusive('efficiency', 'null')

    def test_efficiency_empty_attempt_container_is_inconclusive(self):
        self.assert_missing_attempt_container_is_inconclusive('efficiency', 'empty')

    def test_incomplete_attempt_lower_bound_and_exhaustion_remain_enforced(self):
        for claim in ('outcome', 'efficiency'):
            for side in ('baseline', 'candidate'):
                for mutation in ('missing', 'null', 'empty'):
                    for supplied in (38, 39, 40):
                        with self.subTest(claim=claim, side=side, mutation=mutation, supplied=supplied):
                            b = bundle_for(T.gate, claim)
                            pair = b['evidence']['pairs'][0]
                            if mutation == 'missing':
                                del pair[side + '_attempts']
                            else:
                                pair[side + '_attempts'] = None if mutation == 'null' else []
                            b['evidence']['usage']['attempts'] = supplied
                            T.reapprove(b)
                            result = decision(T.gate, b)
                            self.assertEqual(result['decision'], 'reject' if supplied < 39 else 'inconclusive')
                            self.assertFalse(result['benefit'])
                            if supplied < 39:
                                self.assertIn('reported attempts differ from observable attempt records', result['reasons'])
                    # Reported and observed limits each continue to prevent pass.
                    for limit in (38, 39, 40):
                        b = bundle_for(T.gate, claim)
                        b['evidence']['pairs'][0][side + '_attempts'] = None
                        b['plan']['budget']['attempts'] = limit
                        rebind(b)
                        result = decision(T.gate, b)
                        self.assertEqual(result['decision'], 'inconclusive')
                        self.assertFalse(result['benefit'])
                        self.assertIn('resource budget exhausted: attempts', result['measurement_gaps'])

    def test_complete_attempt_telemetry_reconciles_exactly(self):
        for claim in ('outcome', 'efficiency'):
            for supplied in (39, 40, 41):
                b = bundle_for(T.gate, claim)
                b['evidence']['usage']['attempts'] = supplied
                T.reapprove(b)
                result = decision(T.gate, b)
                self.assertEqual(result['decision'], 'pass' if supplied == 40 else 'reject')
                if supplied == 40:
                    self.assertEqual(result['benefit']['interval_95'], [10.0, 10.0])
                    self.assertEqual(result['benefit']['relative_benefit'], .1)
                else:
                    self.assertFalse(result['benefit'])
                    self.assertIn('reported attempts differ from observable attempt records', result['reasons'])


if __name__ == '__main__':
    if '--replay-json' in sys.argv:
        # Raw dual-version results belong in the caller's designated evidence path.
        print(json.dumps({'substitutions': SUBSTITUTIONS,
                          'baseline': replay_original(OLD_GATE, OLD_DORA),
                          'candidate': replay_original(T.gate, D.dora)}, sort_keys=True))
    else:
        unittest.main()
