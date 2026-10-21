import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from instrumentation.runner import run_command


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def run_python(self, script, **kwargs):
        return run_command([sys.executable, '-c', script], cwd=self.tmp.name, **kwargs)

    def test_success_hashes_and_no_raw_secret(self):
        result = self.run_python("print('api_key=private-fixture')")
        self.assertEqual(result['exit_code'], 0)
        self.assertEqual(result['stdout_sha256'], hashlib.sha256(b'api_key=private-fixture\n').hexdigest())
        self.assertNotIn('private-fixture', json.dumps(result))
        self.assertGreaterEqual(result['duration_seconds'], 0)

    def test_nonzero_preserved(self):
        result = self.run_python("import sys; print('failure',file=sys.stderr); sys.exit(7)")
        self.assertEqual(result['exit_code'], 7)
        self.assertGreater(result['stderr_bytes'], 0)

    def test_timeout(self):
        result = self.run_python('import time; time.sleep(10)', timeout=0.1)
        self.assertTrue(result['timed_out'])
        self.assertLess(result['exit_code'], 0)
        self.assertLess(result['duration_seconds'], 3)

    def test_output_cap(self):
        result = self.run_python("import sys; sys.stdout.write('x'*1000000); sys.stdout.flush()", max_output_bytes=1000)
        self.assertTrue(result['output_limit_exceeded'])
        self.assertLessEqual(result['stdout_bytes'], 65536)

    def test_no_shell(self):
        result = run_command([sys.executable, '-c', 'import sys; print(sys.argv[1])', '$(touch escaped)'], cwd=self.tmp.name)
        self.assertEqual(result['exit_code'], 0)
        self.assertFalse((Path(self.tmp.name) / 'escaped').exists())

    def test_invalid_arrays_limits_and_missing_command(self):
        for array in ('echo hi', [], [1]):
            with self.assertRaises(ValueError):
                run_command(array, cwd=self.tmp.name)
        for options in ({'timeout': 0}, {'timeout': float('nan')}, {'max_output_bytes': 0}):
            with self.assertRaises(ValueError):
                self.run_python('pass', **options)
        self.assertEqual(run_command(['/no/such/executable'], cwd=self.tmp.name)['exit_code'], 127)
