from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).parents[1]))
from instrumentation.scenarios import run_scenarios


class ScenarioConsumerTest(unittest.TestCase):
    def test_real_cli_sequences_and_refusals(self):
        result = run_scenarios(Path(__file__).parents[2])
        self.assertTrue(result['passed'], result)
        self.assertGreaterEqual(result['scenario_count'], 9)
        self.assertTrue(all(row['passed'] for row in result['results']))
