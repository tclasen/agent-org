"""Version 1 append-only JSONL API. Local flock is not distributed authority."""
import fcntl
import hashlib
import json
import os
import math
import re
from pathlib import Path
try:
    from .common import canonical, digest, utc
except ImportError:
    from common import canonical, digest, utc

ID = re.compile(r'^[A-Z][A-Z0-9]*-[0-9]{6,}$')
SAFE_DATA = frozenset(('provenance source reason target_event_id replacement outcome checkpoint '
    'command command_hash argv_sha256 cwd_sha256 exit_code duration_seconds stdout_sha256 stderr_sha256 '
    'stdout_bytes stderr_bytes timed_out output_limit_exceeded error_code '
    'requested_model actual_model requested_reasoning actual_reasoning tokens cost '
    'input_hash output_hash instruction_hash policy_hash candidate_hash snapshot_hash '
    'project_id service_id environment commit_id commit_ids committed_at build_id artifact_id '
    'deployment_id failure_id traffic healthy degradation_started_at causal_evidence '
    'healthy_since confirmed_at health_evidence health_criteria rework_kind remediates_deployment_id unplanned definition_version classification_version '
    'type occurred_at event_id data payload sequence adapter_id approved_scope requirement_ids '
    'task_id run_id agent_id classification schema_version ingested_at event_type causal_event_ids').split())
SECRET = re.compile(r'(?i)(?:bearer\s+\S+|(?:password|api[_-]?key|secret|access[_-]?token)\s*[:=]\s*\S+|-----BEGIN .*PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{12,}|sk-[A-Za-z0-9]{16,})')
LEDGER = {'sequence', 'previous_hash', 'hash'}
REQUIRED = {'schema_version', 'event_id', 'event_type', 'task_id', 'run_id', 'agent_id', 'classification', 'occurred_at', 'ingested_at', 'data'}


def safe_data(value, depth=0):
    if depth > 8:
        raise ValueError('metadata nesting too deep')
    if isinstance(value, dict):
        for key, item in value.items():
            if key not in SAFE_DATA:
                raise ValueError('unapproved metadata field')
            safe_data(item, depth + 1)
    elif isinstance(value, list):
        if len(value) > 1000:
            raise ValueError('metadata list too large')
        for item in value:
            safe_data(item, depth + 1)
    elif isinstance(value, str):
        if len(value) > 4096 or SECRET.search(value):
            raise ValueError('sensitive or excessive metadata rejected')
    elif isinstance(value, float) and not math.isfinite(value):
        raise ValueError('non-finite metadata number')
    elif value is not None and not isinstance(value, (bool, int, float)):
        raise ValueError('unsupported metadata type')


def validate_event(event):
    if not isinstance(event, dict) or set(event) - REQUIRED - {'causal_event_ids'} or REQUIRED - set(event):
        raise ValueError('unknown or missing event envelope fields')
    if type(event['schema_version']) is not int or event['schema_version'] != 1:
        raise ValueError('unsupported event schema')
    for key, prefix in [('event_id', 'EVT'), ('task_id', 'TASK'), ('run_id', 'RUN'), ('agent_id', 'AGENT')]:
        if not isinstance(event[key], str) or not ID.fullmatch(event[key]) or not event[key].startswith(prefix + '-'):
            raise ValueError('invalid event identity: ' + key)
    if not isinstance(event['event_type'], str) or not re.fullmatch(r'[a-z][a-z0-9_.-]{0,63}', event['event_type']):
        raise ValueError('invalid event type')
    if not isinstance(event['classification'], str) or event['classification'] not in {'organization', 'project', 'cross_boundary'}:
        raise ValueError('invalid classification')
    utc(event['occurred_at'])
    utc(event['ingested_at'])
    if not isinstance(event['data'], dict):
        raise ValueError('data must be an object')
    safe_data(event['data'])
    links = event.get('causal_event_ids', [])
    if not isinstance(links, list) or any(not isinstance(x, str) or not re.fullmatch(r'EVT-[0-9]{6,}', x) for x in links) or len(links) != len(set(links)):
        raise ValueError('invalid causal identities')
    if event['event_id'] in links:
        raise ValueError('self causal link')
    if event['event_type'] == 'correction':
        data = event['data']
        if not isinstance(data.get('reason'), str) or not data['reason'].strip() or not isinstance(data.get('replacement'), dict) or not data['replacement'] or data.get('target_event_id') not in links:
            raise ValueError('correction requires target, reason, replacement and causal link')
    if len(canonical(event)) > 65536:
        raise ValueError('event too large')
    return event


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


class EventStore:
    def __init__(self, path):
        self.path = Path(path)
        if self.path.is_symlink():
            raise ValueError('ledger symlinks unsupported')

    def _read(self, stream):
        stream.seek(0)
        result, identities, previous = [], set(), None
        for number, raw in enumerate(stream, 1):
            if not raw.endswith(b'\n'):
                raise ValueError('incomplete ledger tail; preserve bytes, quarantine and explicitly record gap before using a new ledger')
            if len(raw) > 131072:
                raise ValueError('ledger line too large')
            try:
                item = json.loads(raw, object_pairs_hook=_unique_object)
            except (ValueError, UnicodeError) as error:
                raise ValueError('invalid ledger JSON') from error
            if not isinstance(item, dict) or set(item) != REQUIRED | LEDGER | ({'causal_event_ids'} if 'causal_event_ids' in item else set()):
                raise ValueError('invalid ledger fields')
            body = {k: v for k, v in item.items() if k not in LEDGER}
            validate_event(body)
            if type(item['sequence']) is not int or item['sequence'] != number or item['previous_hash'] != previous:
                raise ValueError('broken ledger sequence/chain')
            expected = digest({k: v for k, v in item.items() if k != 'hash'})
            if item['hash'] != expected or item['event_id'] in identities:
                raise ValueError('ledger hash/identity conflict')
            if result and utc(item['ingested_at']) < utc(result[-1]['ingested_at']):
                raise ValueError('ingestion time moves backwards')
            if any(link not in identities for link in item.get('causal_event_ids', [])):
                raise ValueError('unresolved causal link')
            identities.add(item['event_id'])
            previous = item['hash']
            result.append(item)
        return result

    def append(self, event):
        validate_event(event)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # O_NOFOLLOW closes the final symlink race. Parent directory is caller-owned.
        fd = os.open(self.path, os.O_RDWR | os.O_CREAT | os.O_APPEND | getattr(os, 'O_NOFOLLOW', 0), 0o600)
        with os.fdopen(fd, 'a+b') as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            rows = self._read(stream)
            for row in rows:
                if row['event_id'] == event['event_id']:
                    if canonical({k: v for k, v in row.items() if k not in LEDGER}) == canonical(event):
                        return {'appended': False, 'event': row}
                    raise ValueError('conflicting duplicate event')
            if rows and utc(event['ingested_at']) < utc(rows[-1]['ingested_at']):
                raise ValueError('ingestion time moves backwards')
            known = {row['event_id'] for row in rows}
            if any(link not in known for link in event.get('causal_event_ids', [])):
                raise ValueError('causal event must already exist')
            row = {**event, 'sequence': len(rows) + 1, 'previous_hash': rows[-1]['hash'] if rows else None}
            row['hash'] = digest(row)
            stream.write(canonical(row) + b'\n')
            stream.flush()
            os.fsync(stream.fileno())
            return {'appended': True, 'event': row}

    def read_events(self, as_of=None):
        if not self.path.exists():
            return []
        if as_of is not None:
            utc(as_of)
        with self.path.open('rb') as stream:
            fcntl.flock(stream, fcntl.LOCK_SH)
            rows = self._read(stream)
        return [r for r in rows if as_of is None or utc(r['ingested_at']) <= utc(as_of)]

    def snapshot(self, as_of=None):
        rows = self.read_events(as_of)
        return {'schema_version': 1, 'as_of': as_of, 'events': rows, 'snapshot_hash': digest(rows), 'trusted_anchor': None}


def coverage_report(events, expected_classes=None):
    counts = {}
    for event in events:
        kind = event['event_type']
        counts[kind] = counts.get(kind, 0) + 1
    return {'observed': counts, 'expected_classes': sorted(expected_classes) if expected_classes is not None else None,
            'missing_classes': sorted(set(expected_classes) - counts.keys()) if expected_classes is not None else None,
            'coverage_denominator': None, 'coverage_fraction': None,
            'unobserved_routes': ['direct tools', 'connectors', 'subagent internals'],
            'actual_model': None, 'tokens': None, 'cost': None}


def verify_event_snapshot(snapshot):
    if snapshot.get('schema_version') != 1 or digest(snapshot.get('events')) != snapshot.get('snapshot_hash'):
        raise ValueError('event snapshot hash mismatch')
    if snapshot.get('as_of') is not None:
        utc(snapshot['as_of'])
    return True
