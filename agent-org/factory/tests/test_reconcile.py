import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from instrumentation.reconcile import reconcile
from instrumentation.records import parse_record


class ReconcileTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name).resolve()
        self.root = self.repo / 'agent-org'
        self.root.mkdir()
        self.write('shared/ID_LEDGER.md', 'Allocated through: TASK-000002, RUN-000001.\n')
        self.task = self.formal('tasks/organization/TASK-000001.md', 'TASK-000001',
                                 'Research source evidence', Status='awaiting_acceptance')
        self.write('tasks/INDEX.md', '- [TASK-000001 — Research source evidence](organization/TASK-000001.md) — awaiting_acceptance\n')

    def write(self, relative, text, root=None):
        path = (root or self.root) / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def formal(self, relative, identifier, title, root=None, **fields):
        return self.write(relative, '# ' + title + '\n\n- ID: ' + identifier + '\n' +
                          ''.join('- ' + key + ': ' + value + '\n' for key, value in fields.items()), root)

    def codes(self, result, level='warnings'):
        return {item['code'] for item in result[level]}

    def git(self, *args):
        result = subprocess.run(['git', '-C', str(self.repo), *args], capture_output=True, text=True, check=True)
        return result.stdout.strip()

    def observation(self):
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('remote', 'add', 'origin', 'https://example.invalid/owning.git')
        self.git('add', '.')
        self.git('commit', '-qm', 'candidate')
        candidate = self.git('rev-parse', 'HEAD')
        self.write('artifact.md', 'artifact')
        self.git('add', '.')
        self.git('commit', '-qm', 'merge-equivalent fixture')
        merge = self.git('rev-parse', 'HEAD')
        with self.task.open('a') as stream:
            stream.write('- Delivery Repository: https://example.invalid/owning.git\n'
                         '- Delivery Ref: refs/heads/main\n- Candidate Commit: ' + candidate + '\n')
        return {'schema_version': 1, 'delivery': [{
            'task_id': 'TASK-000001', 'availability': 'observed',
            'repository': 'https://example.invalid/owning.git', 'ref': 'refs/heads/main',
            'candidate_commit': candidate, 'merge_commit': merge, 'remote_tip': merge,
            'observed_at': '2026-10-22T01:00:00Z', 'evidence': 'fixture remote receipt',
            'local_repository': str(self.repo)}]}

    def test_registry_title_and_suffix_incident(self):
        self.write('tasks/INDEX.md', '- [TASK-000001 — Superseded provisional title](organization/TASK-000001.md) — running\n')
        result = reconcile(self.root)
        self.assertTrue({'registry_title_mismatch', 'registry_status_mismatch'} <= self.codes(result))
        self.assertEqual(result['records'][0]['fields'], parse_record(self.task).fields)
        self.assertFalse(result['clean'])

    def test_duplicate_definition_and_registry_identity(self):
        self.formal('tasks/project/TASK-000001.md', 'TASK-000001', 'Conflicting identity', Status='ready')
        original = (self.root / 'tasks/INDEX.md').read_text()
        self.write('tasks/INDEX.md', original + original)
        result = reconcile(self.root)
        self.assertTrue({'duplicate_id', 'duplicate_registry_id'} <= self.codes(result, 'errors'))
        self.assertFalse(result['ok'])

    def test_lost_response_observed_delivery_retains_claim(self):
        self.formal('runs/RUN-000001.md', 'RUN-000001', 'Research Coordinator',
                    Status='running', Task='TASK-000001', Claim='research outputs')
        observation = self.observation()
        before = {path: path.read_bytes() for path in self.root.rglob('*.md')}
        result = reconcile(self.root, observation)
        delivery = result['delivery'][0]
        self.assertEqual(delivery['state'], 'observed_delivery')
        self.assertEqual(delivery['local_check'], 'ancestry_corroborated')
        self.assertFalse(delivery['verified_delivery'])
        self.assertFalse(delivery['claim_released'])
        self.assertIn('stale_checkpoint', self.codes(result))
        self.assertIn('unresolved_owner', self.codes(result))
        self.assertEqual(before, {path: path.read_bytes() for path in self.root.rglob('*.md')})
        self.assertFalse(result['ownership'][0]['claim_released'])

    def test_unavailable_remote_remains_unknown(self):
        result = reconcile(self.root, {'schema_version': 1, 'delivery': [{
            'task_id': 'TASK-000001', 'availability': 'unavailable', 'evidence': 'API timeout'}]})
        self.assertEqual(result['delivery'][0]['state'], 'unknown')
        self.assertIn('delivery_unavailable', self.codes(result))
        self.assertFalse(result['delivery'][0]['verified_delivery'])
        self.assertIn('observations_unavailable', self.codes(reconcile(self.root)))

    def test_wrong_repository_ref_and_candidate_block(self):
        observation = self.observation()
        for field, value in [('repository', 'https://example.invalid/wrong.git'),
                             ('candidate_commit', 'b' * 40), ('ref', 'refs/heads/other')]:
            with self.subTest(field=field):
                wrong = copy.deepcopy(observation)
                wrong['delivery'][0][field] = value
                result = reconcile(self.root, wrong)
                self.assertIn('delivery_binding_mismatch', self.codes(result, 'errors'))
                self.assertEqual(result['delivery'][0]['state'], 'conflict')

    def test_unbound_prose_and_unknown_commit_cannot_verify(self):
        observation = self.observation()
        fields = self.task.read_text().split('- Delivery Repository:')[0]
        self.task.write_text(fields + '\nDelivered successfully, candidate was merged!\n')
        result = reconcile(self.root, observation)
        self.assertEqual(result['delivery'][0]['state'], 'unbound')
        self.assertIn('unbound_delivery', self.codes(result))

    def test_mismatched_merge_and_remote_tip_ancestry(self):
        observation = self.observation()
        observation['delivery'][0]['remote_tip'] = observation['delivery'][0]['candidate_commit']
        result = reconcile(self.root, observation)
        self.assertIn('delivery_ancestry_mismatch', self.codes(result, 'errors'))
        self.assertEqual(result['delivery'][0]['state'], 'conflict')

    def test_cross_worktree_ranges_reserve_max_without_allocation(self):
        known = self.repo / 'known' / 'agent-org'
        self.formal('tasks/organization/TASK-000090.md', 'TASK-000090', 'Other work', root=known, Status='ready')
        self.write('shared/ID_LEDGER.md', 'Reserved TASK-000091..99, RUN-000062..67, APP-000018..19.\n', known)
        ignored = self.repo / 'projects/hidden/agent-org'
        self.formal('tasks/organization/TASK-999999.md', 'TASK-999999', 'Out of scope', root=ignored, Status='ready')
        result = reconcile(self.root, worktrees=[known.parent])
        self.assertEqual(result['max_reserved']['TASK'], 99)
        self.assertEqual(result['max_reserved']['RUN'], 67)
        self.assertEqual(result['max_reserved']['APP'], 19)
        self.assertNotIn('TASK-999999', {item['id'] for item in result['records']})
        self.assertFalse((self.root / 'tasks/organization/TASK-000100.md').exists())

    def test_cross_worktree_identity_conflict(self):
        known = self.repo / 'known/agent-org'
        self.formal('tasks/organization/TASK-000001.md', 'TASK-000001', 'Other title', root=known, Status='ready')
        self.write('shared/ID_LEDGER.md', 'TASK-000001', known)
        result = reconcile(self.root, worktrees=[known])
        self.assertIn('cross_worktree_identity_conflict', self.codes(result, 'errors'))

    def test_ledger_checkpoint_behind_formal_and_through_range(self):
        self.write('shared/ID_LEDGER.md', 'TASK-000001 through TASK-000003\n')
        self.formal('runs/RUN-000009.md', 'RUN-000009', 'Reserved definition', Status='completed')
        result = reconcile(self.root)
        self.assertEqual(result['max_reserved']['TASK'], 3)
        self.assertEqual(result['max_reserved']['RUN'], 9)
        self.assertIn('ledger_checkpoint_behind', self.codes(result))

    def test_malformed_claim_reference_is_diagnostic(self):
        self.formal('runs/RUN-000001.md', 'RUN-000001', 'Worker', Status='unknown',
                    Task='TASK-000001 through TASK-999999')
        result = reconcile(self.root)
        self.assertIn('invalid_claim_reference', self.codes(result, 'errors'))
        self.assertFalse(result['ownership'][0]['claim_released'])

    def test_conflicting_unknown_owners(self):
        for number, status in [(1, 'unknown'), (2, 'running')]:
            self.formal(f'runs/RUN-{number:06d}.md', f'RUN-{number:06d}', 'Worker',
                        Status=status, Task='TASK-000001', Claim='same file')
        result = reconcile(self.root)
        self.assertIn('conflicting_owners', self.codes(result, 'errors'))
        self.assertTrue(all(item['native_status'] == 'unknown' for item in result['ownership']))

    def test_missing_root_empty_root_unsafe_registry_and_symlinks(self):
        self.assertFalse(reconcile(self.repo / 'absent')['ok'])
        empty = self.repo / 'empty'
        empty.mkdir()
        self.assertIn('no_records', self.codes(reconcile(empty), 'errors'))
        self.write('tasks/INDEX.md', '- [TASK-000001 — X](../outside.md) — ready\n')
        self.assertIn('unsafe_registry_target', self.codes(reconcile(self.root), 'errors'))
        self.task.unlink()
        self.task.symlink_to(self.repo / 'outside')
        self.assertIn('unsafe_family', self.codes(reconcile(self.root), 'errors'))

    def test_unknown_schema_malformed_duplicate_observations(self):
        for observations in ({}, {'schema_version': 2, 'delivery': []},
                             {'schema_version': 1, 'delivery': [], 'magic': True}):
            self.assertIn('invalid_observations', self.codes(reconcile(self.root, observations), 'errors'))
        item = {'task_id': 'TASK-000001', 'availability': 'unavailable', 'evidence': 'timeout'}
        result = reconcile(self.root, {'schema_version': 1, 'delivery': [item, item]})
        self.assertIn('duplicate_observation', self.codes(result, 'errors'))
        self.assertEqual(result['delivery'][0]['state'], 'unknown')
        self.assertIn('invalid_observation', self.codes(reconcile(self.root, {
            'schema_version': 1, 'delivery': [dict(item, mystery='x')]}), 'errors'))

    def test_cli_help_json_error_and_markdown(self):
        cli = Path(__file__).resolve().parents[1] / 'instrumentation/reconcile.py'
        command = [sys.executable, str(cli)]
        help_result = subprocess.run(command + ['--help'], capture_output=True, text=True)
        self.assertEqual(help_result.returncode, 0)
        self.assertIn('--worktree', help_result.stdout)
        output = subprocess.run(command + ['--root', str(self.root)], capture_output=True, text=True)
        self.assertEqual(output.returncode, 0, output.stderr)
        self.assertFalse(json.loads(output.stdout)['clean'])
        malformed = self.repo / 'bad.json'
        malformed.write_text('{"schema_version":1,"schema_version":1,"delivery":[]}')
        output = subprocess.run(command + ['--root', str(self.root), '--observations', str(malformed)], capture_output=True, text=True)
        self.assertEqual(output.returncode, 1)
        self.assertIn('observation_input_error', self.codes(json.loads(output.stdout), 'errors'))
        markdown = subprocess.run(command + ['--root', str(self.root), '--format', 'markdown'], capture_output=True, text=True)
        self.assertIn('Claims retained', markdown.stdout)

    def test_current_repository_registry_regression(self):
        # Real canonical records, not a parallel hand-written parser/fixture:
        # RUN48..50 and research TASK54..62 checkpoints preserve historical state.
        actual = Path(__file__).resolve().parents[2]
        result = reconcile(actual)
        self.assertGreater(len(result['records']), 100)
        ids = {item['id'] for item in result['records']}
        self.assertTrue({'TASK-000054', 'RUN-000048'} <= ids)
        self.assertTrue(any(item['task_id'] == 'TASK-000054' and item['state'] == 'unknown'
                            for item in result['delivery']))
        self.assertIn('observations_unavailable', self.codes(result))
        self.assertTrue(any(item['code'] == 'registry_title_mismatch' and 'TASK-000054' in item['message']
                            for item in result['warnings']))
        self.assertTrue(all(not item['claim_released'] for item in result['ownership']))


if __name__ == '__main__':
    unittest.main()
