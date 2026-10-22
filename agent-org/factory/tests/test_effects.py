import json
import multiprocessing
import os
from pathlib import Path
import subprocess
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from instrumentation.common import canonical, digest, now
from instrumentation.effects import EffectConflict, EffectJournal, journal_path


def intent(effect_id='publish-candidate'):
    return {'effect_id': effect_id, 'operation': 'publish', 'resource': 'org/repository',
            'target': 'refs/heads/main', 'candidate_hash': 'a' * 64,
            'authority': 'APP-000020', 'task': 'TASK-000074', 'run': 'RUN-000070'}


def receipt(status='confirmed', **changes):
    result = {'status': status, 'resource': 'org/repository', 'target': 'refs/heads/main',
              'candidate_hash': 'a' * 64, 'source': 'explicit destination lookup',
              'observed_at': now(), 'remote_identity': 'remote-operation-1' if status == 'confirmed' else None}
    result.update(changes)
    return result


def writer(path):
    EffectJournal(path).prepare(intent())
    EffectJournal(path).attempt('publish-candidate')


class EffectsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        # macOS /var may itself be a symlink; API deliberately rejects symlinks.
        self.root = Path(self.tmp.name).resolve()
        self.path = self.root / 'effects.jsonl'
        self.store = EffectJournal(self.path)

    def test_prepared_before_attempt_and_unknown_missing(self):
        self.assertFalse(self.store.decision('missing')['attempt_eligible'])
        self.assertFalse(self.path.exists())
        result = self.store.prepare(intent())
        self.assertEqual(result['observation'], 'prepared')
        self.assertTrue(result['attempt_eligible'])
        self.assertEqual(result['attempts'], 0)
        raw = self.path.read_bytes()
        self.assertFalse(self.store.prepare(intent())['appended'])
        self.assertEqual(raw, self.path.read_bytes())
        attempted = self.store.attempt('publish-candidate')
        self.assertTrue(attempted['appended'])
        self.assertEqual(attempted['observation'], 'attempted_unknown')
        self.assertFalse(attempted['attempt_eligible'])
        self.assertFalse(attempted['authority_granted'])

    def test_successful_effect_lost_ack_and_failed_lookup_never_replays(self):
        self.store.prepare(intent())
        self.store.attempt('publish-candidate')
        # Dispatch may have succeeded. A replacement only sees local attempt.
        recovered = EffectJournal(self.path)
        self.assertFalse(recovered.attempt('publish-candidate')['appended'])
        unknown = recovered.observe('publish-candidate', receipt('unknown'))
        self.assertEqual(unknown['observation'], 'attempted_unknown')
        self.assertFalse(unknown['attempt_eligible'])
        self.assertFalse(recovered.attempt('publish-candidate')['appended'])
        result = recovered.observe('publish-candidate', receipt())
        self.assertEqual(result['observation'], 'destination_confirmed')
        self.assertEqual(result['next_action'], 'no_additional_attempt')
        self.assertEqual(result['source_authentication'], 'caller_attributed_only')

    def test_existing_receipt_and_duplicate_receipt_no_new_attempt(self):
        self.store.prepare(intent())
        confirmed = receipt()
        self.store.observe('publish-candidate', confirmed)
        raw = self.path.read_bytes()
        self.assertFalse(self.store.observe('publish-candidate', confirmed)['appended'])
        self.assertFalse(self.store.attempt('publish-candidate')['appended'])
        self.assertEqual(self.store.decision('publish-candidate')['attempts'], 0)
        self.assertEqual(raw, self.path.read_bytes())
        self.store.observe('publish-candidate', receipt('unknown'))
        self.assertEqual(self.store.decision('publish-candidate')['observation'], 'destination_confirmed')

    def test_definitive_nonexecution_allows_one_explicit_new_attempt(self):
        self.store.prepare(intent())
        self.store.attempt('publish-candidate')
        absent = receipt('not_executed')
        result = self.store.observe('publish-candidate', absent)
        self.assertTrue(result['attempt_eligible'])
        self.assertEqual(result['observation'], 'definitively_not_executed')
        result = self.store.attempt('publish-candidate')
        self.assertTrue(result['appended'])
        self.assertEqual(result['attempts'], 2)
        # Replaying an earlier nonexecution receipt cannot clear the new attempt.
        self.assertFalse(self.store.observe('publish-candidate', absent)['attempt_eligible'])
        self.assertFalse(self.store.attempt('publish-candidate')['appended'])

    def test_conflicting_intent_identity_is_persistent_and_terminal(self):
        for field, value in [('operation', 'merge'), ('resource', 'wrong/repo'),
                             ('target', 'other'), ('candidate_hash', 'b' * 64),
                             ('authority', 'other'), ('task', 'other'), ('run', 'other')]:
            with self.subTest(field=field):
                path = self.root / (field + '.jsonl')
                store = EffectJournal(path)
                store.prepare(intent())
                changed = {**intent(), field: value}
                with self.assertRaises(EffectConflict):
                    store.prepare(changed)
                decision = EffectJournal(path).decision('publish-candidate')
                self.assertEqual(decision['observation'], 'conflicted')
                self.assertFalse(decision['attempt_eligible'])
                self.assertFalse(store.attempt('publish-candidate')['appended'])

    def test_stale_nonexecution_receipt_cannot_clear_new_attempt(self):
        self.store.prepare(intent())
        self.store.attempt('publish-candidate')
        with self.assertRaisesRegex(EffectConflict, 'predates'):
            self.store.observe('publish-candidate', receipt('not_executed', observed_at='2020-01-01T00:00:00Z'))
        self.assertFalse(self.store.decision('publish-candidate')['attempt_eligible'])

    def test_wrong_candidate_target_resource_blocks_even_before_attempt(self):
        for field, value in [('candidate_hash', 'b' * 64), ('target', 'wrong'), ('resource', 'wrong/repository')]:
            with self.subTest(field=field):
                store = EffectJournal(self.root / (field + '.jsonl'))
                store.prepare(intent())
                with self.assertRaises(EffectConflict):
                    store.observe('publish-candidate', receipt(**{field: value}))
                self.assertEqual(store.decision('publish-candidate')['observation'], 'conflicted')
                self.assertFalse(store.attempt('publish-candidate')['appended'])

    def test_conflicting_remote_identity_or_nonexecution_blocks(self):
        for other in (receipt(remote_identity='different-remote-effect'), receipt('not_executed')):
            with self.subTest(receipt=other):
                store = EffectJournal(self.root / (digest(other) + '.jsonl'))
                store.prepare(intent())
                store.observe('publish-candidate', receipt())
                with self.assertRaises(EffectConflict):
                    store.observe('publish-candidate', other)
                self.assertEqual(store.decision('publish-candidate')['observation'], 'conflicted')

    def test_incomplete_write_blocks_read_and_append_preserving_bytes(self):
        self.store.prepare(intent())
        with self.path.open('ab') as stream:
            stream.write(b'{"kind":"attempted"')
        raw = self.path.read_bytes()
        for action in (lambda: self.store.prepare(intent('second')),
                       lambda: self.store.attempt('publish-candidate'),
                       lambda: self.store.observe('publish-candidate', receipt()),
                       lambda: self.store.decision('publish-candidate')):
            with self.assertRaisesRegex(ValueError, 'incomplete'):
                action()
            self.assertEqual(self.path.read_bytes(), raw)

    def test_corruption_full_read_duplicate_keys_and_hash_chain(self):
        self.store.prepare(intent())
        original = self.path.read_bytes()
        for corrupt in (original.replace(b'org/repository', b'other/repo'),
                        original.replace(b'"schema_version":1', b'"schema_version":1,"schema_version":1'),
                        original + b'null\n'):
            self.path.write_bytes(corrupt)
            with self.assertRaises(ValueError):
                self.store.attempt('publish-candidate')
            self.assertEqual(self.path.read_bytes(), corrupt)
        self.path.write_bytes(original)
        self.store.attempt('publish-candidate')
        rows = [json.loads(line) for line in self.path.read_bytes().splitlines()]
        rows[-1]['previous_hash'] = '0' * 64
        rows[-1]['hash'] = digest({k: v for k, v in rows[-1].items() if k != 'hash'})
        self.path.write_bytes(b''.join(canonical(r) + b'\n' for r in rows))
        with self.assertRaisesRegex(ValueError, 'chain'):
            self.store.decision('publish-candidate')

    def test_hashed_but_invalid_transition_is_rejected(self):
        self.store.prepare(intent())
        self.store.attempt('publish-candidate')
        rows = [json.loads(line) for line in self.path.read_bytes().splitlines()]
        extra = {**rows[-1], 'sequence': 3, 'previous_hash': rows[-1]['hash'], 'data': {'attempt': 2}}
        extra['hash'] = digest({k: v for k, v in extra.items() if k != 'hash'})
        with self.path.open('ab') as stream:
            stream.write(canonical(extra) + b'\n')
        with self.assertRaisesRegex(ValueError, 'unsafe'):
            self.store.decision('publish-candidate')

    def test_malformed_types_rejected_before_append(self):
        for value in (None, [], 12, {**intent(), 'effect_id': []}, {**intent(), 'candidate_hash': True},
                      {**intent(), 'authority': ''}, {**intent(), 'unknown': 'field'}):
            with self.subTest(intent=value), self.assertRaises(ValueError):
                self.store.prepare(value)
        self.assertFalse(self.path.exists())
        self.store.prepare(intent())
        raw = self.path.read_bytes()
        for value in (None, [], {**receipt(), 'status': []}, {**receipt(), 'observed_at': 17},
                      {**receipt(), 'remote_identity': None}, receipt('unknown', remote_identity='bad'),
                      {**receipt(), 'candidate_hash': 'invalid'}, {**receipt(), 'source': {}}):
            with self.subTest(receipt=value), self.assertRaises(ValueError):
                self.store.observe('publish-candidate', value)
            self.assertEqual(raw, self.path.read_bytes())

    def test_fsync_failure_does_not_claim_success_and_recovery_reads_disk(self):
        self.store.prepare(intent())
        real_fsync = os.fsync
        def fail_file_fsync(fd):
            if stat.S_ISREG(os.fstat(fd).st_mode):
                raise OSError('simulated durability failure after write')
            real_fsync(fd)
        with patch('instrumentation.effects.os.fsync', side_effect=fail_file_fsync):
            with self.assertRaises(OSError):
                self.store.attempt('publish-candidate')
        # Lost durability acknowledgement may leave a complete row. Re-read it;
        # never assume failure means the attempt was not recorded.
        self.assertEqual(self.store.decision('publish-candidate')['attempts'], 1)
        self.assertFalse(self.store.attempt('publish-candidate')['appended'])

    def test_concurrent_exact_identity_and_attempt_are_single(self):
        context = multiprocessing.get_context('spawn')
        processes = [context.Process(target=writer, args=(str(self.path),)) for _ in range(4)]
        for process in processes:
            process.start()
        for process in processes:
            process.join(15)
        for process in processes:
            self.assertEqual(process.exitcode, 0)
        result = self.store.decision('publish-candidate')
        self.assertEqual(result['attempts'], 1)
        self.assertEqual(len(self.path.read_bytes().splitlines()), 2)

    def test_symlinks_traversal_and_nonregular_files_rejected(self):
        outside = self.root / 'outside'
        outside.mkdir()
        parent = self.root / 'linked'
        parent.symlink_to(outside, target_is_directory=True)
        with self.assertRaises((ValueError, OSError)):
            EffectJournal(parent / 'journal').prepare(intent())
        self.assertFalse((outside / 'journal').exists())
        self.path.symlink_to(outside / 'journal')
        with self.assertRaises((ValueError, OSError)):
            self.store.prepare(intent())
        with self.assertRaises(ValueError):
            EffectJournal(self.root / '..' / 'escaped')
        for relative in ('../effects.jsonl', '/absolute', 'factory/other/a', 'factory/reports/../a', 'factory/reports'):
            with self.subTest(path=relative), self.assertRaises(ValueError):
                journal_path(self.root, relative)
        directory = self.root / 'directory'
        directory.mkdir()
        with self.assertRaises((OSError, ValueError)):
            EffectJournal(directory).prepare(intent())

    def test_cli_actual_sequence_and_boundaries(self):
        script = Path(__file__).resolve().parents[1] / 'instrumentation' / 'effects.py'
        def call(*args, code=0):
            result = subprocess.run([sys.executable, str(script), '--root', str(self.root), *args], capture_output=True, text=True)
            self.assertEqual(result.returncode, code, result.stderr)
            return json.loads(result.stdout if code == 0 else result.stderr)
        self.assertTrue(call('prepare', '--intent', json.dumps(intent()))['appended'])
        self.assertTrue(call('attempt', '--effect-id', 'publish-candidate')['appended'])
        self.assertFalse(call('attempt', '--effect-id', 'publish-candidate')['appended'])
        path = self.root / 'receipt.json'
        path.write_text(json.dumps(receipt()))
        self.assertEqual(call('observe', '--effect-id', 'publish-candidate', '--receipt-file', str(path))['observation'], 'destination_confirmed')
        self.assertFalse(call('decision', '--effect-id', 'publish-candidate')['attempt_eligible'])
        self.assertFalse(call('--journal', '../escape', 'decision', '--effect-id', 'missing', code=2)['attempt_eligible'])
        call('prepare', '--intent', '[]', code=2)
        call('prepare', '--intent', '{"a":1,"a":2}', code=2)
        (self.root / 'factory' / 'reports').symlink_to(self.root / 'factory' / 'events', target_is_directory=True)
        call('--journal', 'factory/reports/escaped.jsonl', 'prepare', '--intent', json.dumps(intent()), code=2)
        self.assertFalse((self.root / 'factory' / 'events' / 'escaped.jsonl').exists())


if __name__ == '__main__':
    unittest.main()
