import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('autonomy', Path(__file__).parents[1] / 'metrics/autonomy.py')
autonomy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(autonomy)


class AutonomyMetricsTest(unittest.TestCase):
    def test_failed_retries_and_unknown_usage_remain_visible(self):
        rows = [dict(attempt_id='a1', task_id='t1', source='receipt1', outcome='failed', attempt_number=1, resources={'active_seconds': 10}),
                dict(attempt_id='a2', task_id='t1', source='receipt2', outcome='accepted', attempt_number=2,
                     recovery_success=True, resources={'active_seconds': 15, 'tokens': 200}),
                dict(attempt_id='a3', task_id='t2', source='checkpoint', outcome='unknown', attempt_number=1)]
        report = autonomy.summarize(rows)
        self.assertEqual(report['attempts'], 3)
        self.assertEqual(report['retry_attempts'], 1)
        self.assertEqual(report['accepted_rate'], 0.5)
        self.assertEqual(report['outcome_denominator'], 2)
        self.assertEqual(report['resources']['active_seconds']['observed_sum'], 25)
        self.assertIsNone(report['resources']['active_seconds']['total'])
        self.assertIsNone(report['resources']['cost_usd']['total'])
        self.assertEqual(report['reliability']['recovery_success']['unknown'], 2)
        self.assertEqual(report['all_attempts_accepted'], {'tasks': 0, 'known_tasks': 1, 'unknown_tasks': 1})

    def test_no_observations_is_not_perfect_or_free(self):
        report = autonomy.summarize([])
        self.assertIsNone(report['accepted_rate'])
        self.assertIsNone(report['resources']['cost_usd']['total'])
        self.assertIsNone(report['reliability']['recovery_success']['rate'])

    def test_conflicts_and_malformed_usage_refused(self):
        row = dict(attempt_id='a', task_id='t', source='receipt')
        for bad in ([row, row], [dict(row, resources={'tokens': True})], [dict(row, outcome='great')],
                    [dict(row, recovery_success=1)], [dict(row, resources={'cost_usd': float('nan')})]):
            with self.assertRaises(ValueError):
                autonomy.summarize(bad)

    def test_missing_ordinals_are_unknown_and_conflicts_refused(self):
        first = dict(attempt_id='a', task_id='t', source='receipt', outcome='failed')
        second = dict(attempt_id='b', task_id='t', source='receipt', outcome='accepted')
        result = autonomy.summarize([first, second])
        self.assertEqual(result['attempts'], 2)
        self.assertIsNone(result['retry_attempts'])
        self.assertEqual(result['unknown_attempt_ordinals'], 2)
        with self.assertRaisesRegex(ValueError, 'duplicate per-task'):
            autonomy.summarize([dict(first, attempt_number=1), dict(second, attempt_number=1)])
