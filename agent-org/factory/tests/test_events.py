import copy
import json
import multiprocessing
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from instrumentation.events import EventStore, coverage_report, validate_event, verify_event_snapshot


def event(number=1):
    return dict(schema_version=1, event_id=f'EVT-{number:06}', event_type='checkpoint', task_id='TASK-000001', run_id='RUN-000001', agent_id='AGENT-000001', classification='organization', occurred_at='2026-10-01T00:00:00Z', ingested_at='2026-10-02T00:00:00Z', data={'checkpoint': 'fixture'})


def writer(path, number):
    EventStore(path).append(event(number))


class EventsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'events.jsonl'
        self.store = EventStore(self.path)

    def test_append_duplicate_and_conflict(self):
        self.assertTrue(self.store.append(event())['appended'])
        raw = self.path.read_bytes()
        self.assertFalse(self.store.append(event())['appended'])
        changed = event()
        changed['data']['checkpoint'] = 'other'
        with self.assertRaises(ValueError):
            self.store.append(changed)
        self.assertEqual(self.path.read_bytes(), raw)

    def test_invalid_metadata_never_appends(self):
        for change in ({'event_id': 'TASK-000001'}, {'schema_version': True}, {'occurred_at': 'yesterday'}, {'occurred_at': '2026-01-01Z'}, {'causal_event_ids': [{}]}, {'classification': []}, {'classification': 'unknown'}, {'data': {'raw_output': 'secret'}}, {'data': {'reason': 'api_key=abc123'}}, {'data': {'reason': 'x' * 4097}}, {'data': {'cost': float('nan')}}):
            candidate = event()
            candidate.update(change)
            with self.subTest(change=list(change)):
                with self.assertRaises((ValueError, TypeError)):
                    self.store.append(candidate)
        self.assertFalse(self.path.exists())

    def test_concurrent_writers(self):
        context = multiprocessing.get_context('spawn')
        processes = [context.Process(target=writer, args=(str(self.path), n)) for n in range(1, 7)]
        for process in processes:
            process.start()
        for process in processes:
            process.join(15)
            self.assertEqual(process.exitcode, 0)
        rows = self.store.read_events()
        self.assertEqual([r['sequence'] for r in rows], list(range(1, 7)))
        self.assertEqual(len({r['event_id'] for r in rows}), 6)

    def test_incomplete_and_corrupt_tail_preserved(self):
        self.store.append(event())
        with self.path.open('ab') as stream:
            stream.write(b'{"event_id":')
        raw = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            self.store.append(event(2))
        self.assertEqual(raw, self.path.read_bytes())

    def test_tamper_detected(self):
        self.store.append(event())
        data = self.path.read_text().replace('fixture', 'tampered')
        self.path.write_text(data)
        with self.assertRaisesRegex(ValueError, 'hash'):
            self.store.read_events()

    def test_correction_and_late_as_of(self):
        self.store.append(event())
        old = self.store.snapshot('2026-10-02T00:00:00Z')
        correction = event(2)
        correction.update(event_type='correction', ingested_at='2026-10-03T00:00:00Z', causal_event_ids=['EVT-000001'], data={'target_event_id': 'EVT-000001', 'reason': 'fixed attribution', 'replacement': {'outcome': 'passed'}})
        self.store.append(correction)
        self.assertEqual(old, self.store.snapshot('2026-10-02T00:00:00Z'))
        self.assertEqual(len(self.store.read_events()), 2)
        self.assertNotEqual(old['snapshot_hash'], self.store.snapshot()['snapshot_hash'])
        self.assertIsNone(old['trusted_anchor'])
        self.assertTrue(verify_event_snapshot(old))
        altered = copy.deepcopy(old)
        altered['events'][0]['data']['checkpoint'] = 'altered'
        with self.assertRaises(ValueError):
            verify_event_snapshot(altered)

    def test_duplicate_json_key_and_backdated_ingestion_rejected(self):
        self.store.append(event())
        second = event(2)
        second['ingested_at'] = '2026-10-01T00:00:00Z'
        with self.assertRaisesRegex(ValueError, 'backwards'):
            self.store.append(second)
        raw = self.path.read_bytes()
        self.path.write_bytes(raw.replace(b'"schema_version":1', b'"schema_version":1,"schema_version":1'))
        with self.assertRaises(ValueError):
            self.store.read_events()

    def test_causal_reference_must_exist(self):
        item = event()
        item['causal_event_ids'] = ['EVT-000099']
        with self.assertRaisesRegex(ValueError, 'causal'):
            self.store.append(item)
        self.assertEqual(self.path.read_bytes(), b'')

    def test_missing_correction_reason(self):
        item = event()
        item.update(event_type='correction', data={'replacement': {'outcome': 'passed'}})
        with self.assertRaises(ValueError):
            validate_event(item)

    def test_coverage_unknowns(self):
        report = coverage_report([event()], ['checkpoint', 'command'])
        self.assertEqual(report['observed'], {'checkpoint': 1})
        self.assertEqual(report['missing_classes'], ['command'])
        self.assertIsNone(report['cost'])
        self.assertIsNone(report['coverage_fraction'])
