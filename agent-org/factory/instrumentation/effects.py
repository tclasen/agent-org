"""Explicit local effect observations; never executes or authorizes an effect.

EffectJournal(path).prepare(intent), attempt(effect_id), observe(effect_id, receipt)
and decision(effect_id) use a locked, fsynced JSONL hash chain. Intent keys are
effect_id, operation, resource, target, candidate_hash (SHA256), authority, task,
run. An effect_id is a caller-chosen stable idempotency key, not an allocated
organization ID. Exact repeats are idempotent; conflicting identity is persisted
and rejected. Conflicts are terminal and require independent authorized
reconciliation elsewhere.

Receipts have status confirmed|not_executed|unknown, resource, target,
candidate_hash, source, observed_at (UTC Z), remote_identity (string, or null for
unconfirmed observations). These are attributed caller observations: this module
does not authenticate their source or independently verify remote state. The
decision is local replay eligibility, never authority to dispatch. Record attempt
BEFORE dispatch; a lost response stays unknown until an explicit observation.
Only a definitive not_executed observation permits another recorded attempt.

Partial/corrupt files are preserved and block all use; there is no repair or
truncation. Hashes are corruption checks, not a trusted external anchor. Local
flock is cooperative, not distributed isolation. Direct tools can bypass this API.
"""
import argparse
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import re
import stat
import sys

try:
    from .common import canonical, digest, now, utc
except ImportError:
    from common import canonical, digest, now, utc


INTENT = frozenset('effect_id operation resource target candidate_hash authority task run'.split())
RECEIPT = frozenset('status resource target candidate_hash source observed_at remote_identity'.split())
BOUND = ('resource', 'target', 'candidate_hash')
ROW = frozenset('schema_version sequence previous_hash hash recorded_at kind effect_id data'.split())
SHA256 = re.compile(r'[0-9a-f]{64}')


class EffectConflict(ValueError):
    """Rejected conflict durably recorded; existing effect is blocked."""


def _string(value, field):
    if not isinstance(value, str) or not value.strip() or len(value) > 4096 or any(ord(c) < 32 for c in value):
        raise ValueError('invalid string: ' + field)


def _object(value, keys, label):
    if not isinstance(value, dict) or set(value) != keys:
        raise ValueError('invalid ' + label + ' fields')


def _intent(value):
    _object(value, INTENT, 'intent')
    for key in INTENT:
        _string(value[key], key)
    if not SHA256.fullmatch(value['candidate_hash']):
        raise ValueError('candidate_hash must be lowercase SHA256')


def _receipt(value):
    _object(value, RECEIPT, 'receipt')
    for key in RECEIPT - {'remote_identity'}:
        _string(value[key], key)
    if value['status'] not in {'confirmed', 'not_executed', 'unknown'}:
        raise ValueError('invalid receipt status')
    utc(value['observed_at'])
    if not SHA256.fullmatch(value['candidate_hash']):
        raise ValueError('candidate_hash must be lowercase SHA256')
    if value['remote_identity'] is not None:
        _string(value['remote_identity'], 'remote_identity')
    if value['status'] == 'confirmed' and value['remote_identity'] is None:
        raise ValueError('confirmed receipt requires remote_identity')
    if value['status'] != 'confirmed' and value['remote_identity'] is not None:
        raise ValueError('unconfirmed receipt must have null remote_identity')


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


class EffectJournal:
    """Cooperative local journal. All path components must be real directories.

    API callers own the scope of path; CLI callers are additionally bounded to
    root/factory/{reports,events}. Nothing in the journal grants scope/approval.
    """

    def __init__(self, path):
        supplied = Path(path)
        if '..' in supplied.parts:
            raise ValueError('journal traversal rejected')
        self.path = Path(os.path.abspath(supplied))

    @contextmanager
    def _open(self, write):
        # Traverse with directory descriptors and NOFOLLOW, including parents.
        # Holding the opened parent avoids a symlink swap between check and use.
        directory = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
        try:
            for name in self.path.parent.parts[1:]:
                if write:
                    try:
                        os.mkdir(name, mode=0o700, dir_fd=directory)
                        os.fsync(directory)
                    except FileExistsError:
                        pass
                child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
                os.close(directory)
                directory = child
            flags = (os.O_RDWR | os.O_APPEND) if write else os.O_RDONLY
            flags |= os.O_NOFOLLOW | os.O_NONBLOCK
            if write:
                try:
                    fd = os.open(self.path.name, flags | os.O_CREAT | os.O_EXCL, 0o600, dir_fd=directory)
                except FileExistsError:
                    fd = os.open(self.path.name, flags, dir_fd=directory)
            else:
                fd = os.open(self.path.name, flags, dir_fd=directory)
            try:
                if not stat.S_ISREG(os.fstat(fd).st_mode):
                    raise ValueError('journal must be a regular file')
                with os.fdopen(fd, 'a+b' if write else 'rb') as stream:
                    fd = None
                    fcntl.flock(stream, fcntl.LOCK_EX if write else fcntl.LOCK_SH)
                    if write:
                        os.fsync(directory)
                    yield stream
            finally:
                if fd is not None:
                    os.close(fd)
        finally:
            os.close(directory)

    def _read(self, stream):
        stream.seek(0)
        rows, states, previous = [], {}, None
        for number, raw in enumerate(stream, 1):
            if not raw.endswith(b'\n'):
                raise ValueError('incomplete journal tail; preserve bytes and reconcile explicitly')
            if len(raw) > 131072:
                raise ValueError('journal line too large')
            try:
                row = json.loads(raw, object_pairs_hook=_unique)
            except (ValueError, UnicodeError) as error:
                raise ValueError('invalid journal JSON') from error
            _object(row, ROW, 'journal row')
            if type(row['schema_version']) is not int or row['schema_version'] != 1:
                raise ValueError('unsupported journal schema')
            if type(row['sequence']) is not int or row['sequence'] != number or row['previous_hash'] != previous:
                raise ValueError('broken journal chain')
            if row['hash'] != digest({k: v for k, v in row.items() if k != 'hash'}):
                raise ValueError('journal hash mismatch')
            utc(row['recorded_at'])
            _string(row['effect_id'], 'effect_id')
            self._apply(states, row)
            rows.append(row)
            previous = row['hash']
        return rows, states

    @staticmethod
    def _apply(states, row):
        key, kind, data = row['effect_id'], row['kind'], row['data']
        if kind == 'prepared':
            _intent(data)
            if data['effect_id'] != key or key in states:
                raise ValueError('duplicate/conflicting journal identity')
            states[key] = {'intent': data, 'state': 'prepared', 'attempts': 0,
                           'latest_attempt_at': None, 'receipts': [], 'conflicts': []}
            return
        if key not in states:
            raise ValueError('journal effect has no prepared intent')
        state = states[key]
        if kind == 'conflict':
            _object(data, {'reason', 'submitted_hash'}, 'conflict')
            _string(data['reason'], 'reason')
            if not isinstance(data['submitted_hash'], str) or not SHA256.fullmatch(data['submitted_hash']):
                raise ValueError('invalid conflict hash')
            state['conflicts'].append(data)
            state['state'] = 'conflicted'
        elif kind == 'attempted':
            _object(data, {'attempt'}, 'attempt')
            if type(data['attempt']) is not int or data['attempt'] != state['attempts'] + 1 or state['state'] not in {'prepared', 'definitively_not_executed'}:
                raise ValueError('unsafe or duplicate journal attempt')
            state['attempts'] += 1
            state['latest_attempt_at'] = row['recorded_at']
            state['state'] = 'attempted_unknown'
        elif kind == 'observed':
            _receipt(data)
            if any(data[k] != state['intent'][k] for k in BOUND):
                raise ValueError('journal receipt binding mismatch')
            if data in state['receipts'] or state['state'] == 'conflicted':
                raise ValueError('duplicate/blocked journal observation')
            if data['status'] == 'not_executed' and state['latest_attempt_at'] is not None and utc(data['observed_at']) < utc(state['latest_attempt_at']):
                raise ValueError('nonexecution observation predates latest attempt')
            confirmed = [r for r in state['receipts'] if r['status'] == 'confirmed']
            if confirmed and (data['status'] == 'not_executed' or (data['status'] == 'confirmed' and data['remote_identity'] != confirmed[0]['remote_identity'])):
                raise ValueError('conflicting journal receipt identity')
            state['receipts'].append(data)
            if data['status'] == 'confirmed':
                state['state'] = 'destination_confirmed'
            elif data['status'] == 'not_executed':
                state['state'] = 'definitively_not_executed'
            elif state['state'] != 'destination_confirmed':
                state['state'] = 'attempted_unknown'
        else:
            raise ValueError('unknown journal row kind')

    @staticmethod
    def _decision(key, state):
        status = state['state'] if state else 'unknown'
        eligible = status in {'prepared', 'definitively_not_executed'}
        return {'effect_id': key, 'observation': status, 'attempt_eligible': eligible,
                'attempts': state['attempts'] if state else 0,
                'next_action': 'record_attempt_before_authorized_dispatch' if eligible else (
                    'no_additional_attempt' if status == 'destination_confirmed' else 'reconcile_without_replay'),
                'source_authentication': 'caller_attributed_only', 'authority_granted': False,
                'receipts': state['receipts'] if state else [], 'conflicts': state['conflicts'] if state else []}

    def _append(self, stream, rows, states, key, kind, data):
        row = {'schema_version': 1, 'sequence': len(rows) + 1,
               'previous_hash': rows[-1]['hash'] if rows else None,
               'recorded_at': now(), 'kind': kind, 'effect_id': key, 'data': data}
        self._apply(states, row)
        row['hash'] = digest(row)
        stream.write(canonical(row) + b'\n')
        stream.flush()
        os.fsync(stream.fileno())
        return {**self._decision(key, states[key]), 'appended': True, 'journal_hash': row['hash']}

    def _conflict(self, stream, rows, states, key, reason, submitted):
        self._append(stream, rows, states, key, 'conflict', {'reason': reason, 'submitted_hash': digest(submitted)})
        raise EffectConflict(reason + '; conflict recorded, effect blocked')

    def prepare(self, intent):
        """Durably bind a stable key. Exact duplicates do not append."""
        _intent(intent)
        key = intent['effect_id']
        with self._open(True) as stream:
            rows, states = self._read(stream)
            if key in states:
                if states[key]['intent'] != intent:
                    self._conflict(stream, rows, states, key, 'conflicting intent identity', intent)
                return {**self._decision(key, states[key]), 'appended': False}
            return self._append(stream, rows, states, key, 'prepared', intent)

    def attempt(self, effect_id):
        """Record BEFORE dispatch. Repeated calls never authorize blind replay."""
        _string(effect_id, 'effect_id')
        with self._open(True) as stream:
            rows, states = self._read(stream)
            state = states.get(effect_id)
            if state is None:
                raise ValueError('effect is not prepared')
            if not self._decision(effect_id, state)['attempt_eligible']:
                return {**self._decision(effect_id, state), 'appended': False}
            return self._append(stream, rows, states, effect_id, 'attempted', {'attempt': state['attempts'] + 1})

    def observe(self, effect_id, receipt):
        """Record explicit observation, not proof of authenticated remote state.

        Wrong resource/target/candidate or contradictory identity is durably
        recorded as a terminal conflict before raising EffectConflict.
        """
        _string(effect_id, 'effect_id')
        _receipt(receipt)
        with self._open(True) as stream:
            rows, states = self._read(stream)
            state = states.get(effect_id)
            if state is None:
                raise ValueError('effect is not prepared')
            if state['state'] == 'conflicted':
                raise EffectConflict('effect blocked by recorded conflict')
            if any(receipt[k] != state['intent'][k] for k in BOUND):
                self._conflict(stream, rows, states, effect_id, 'receipt target/resource/candidate mismatch', receipt)
            if receipt in state['receipts']:
                return {**self._decision(effect_id, state), 'appended': False}
            if receipt['status'] == 'not_executed' and state['latest_attempt_at'] is not None and utc(receipt['observed_at']) < utc(state['latest_attempt_at']):
                self._conflict(stream, rows, states, effect_id, 'nonexecution observation predates latest attempt', receipt)
            confirmed = [r for r in state['receipts'] if r['status'] == 'confirmed']
            if confirmed and (receipt['status'] == 'not_executed' or (receipt['status'] == 'confirmed' and receipt['remote_identity'] != confirmed[0]['remote_identity'])):
                self._conflict(stream, rows, states, effect_id, 'conflicting remote receipt identity', receipt)
            return self._append(stream, rows, states, effect_id, 'observed', receipt)

    def decision(self, effect_id):
        """Read full validated history; missing/corrupt history never permits replay."""
        _string(effect_id, 'effect_id')
        try:
            with self._open(False) as stream:
                _, states = self._read(stream)
        except FileNotFoundError:
            states = {}
        return self._decision(effect_id, states.get(effect_id))


def journal_path(root, relative):
    """CLI scope: literal relative path below factory/reports or factory/events."""
    root, relative = Path(root), Path(relative)
    if relative.is_absolute() or '..' in relative.parts or len(relative.parts) < 3 or relative.parts[:2] not in {('factory', 'reports'), ('factory', 'events')}:
        raise ValueError('journal must be relative below factory/reports or factory/events')
    # Descriptor traversal in EffectJournal additionally refuses parent symlinks.
    return root / relative


def _load_json(inline, filename):
    raw = inline if inline is not None else Path(filename).read_text(encoding='utf-8')
    value = json.loads(raw, object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError('JSON input must be an object')
    return value


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--root', required=True, help='organization root, e.g. agent-org')
    parser.add_argument('--journal', default='factory/events/effects.jsonl', help='relative path under factory/reports or factory/events')
    commands = parser.add_subparsers(dest='command', required=True)
    prepare = commands.add_parser('prepare', help='bind stable effect_id to exact intent')
    group = prepare.add_mutually_exclusive_group(required=True)
    group.add_argument('--intent', help='JSON object; see module help for required keys')
    group.add_argument('--intent-file', help='file containing JSON intent object')
    for name in ('attempt', 'observe', 'decision'):
        command = commands.add_parser(name, help={'attempt': 'record before authorized dispatch; never dispatches', 'observe': 'attribute a receipt, unknown lookup or definitive nonexecution', 'decision': 'read validated local replay eligibility'}[name])
        command.add_argument('--effect-id', required=True)
        if name == 'observe':
            group = command.add_mutually_exclusive_group(required=True)
            group.add_argument('--receipt', help='JSON receipt object; see module help for required keys')
            group.add_argument('--receipt-file', help='file containing JSON receipt object')
    args = parser.parse_args(argv)
    try:
        journal = EffectJournal(journal_path(args.root, args.journal))
        if args.command == 'prepare':
            result = journal.prepare(_load_json(args.intent, args.intent_file))
        elif args.command == 'observe':
            result = journal.observe(args.effect_id, _load_json(args.receipt, args.receipt_file))
        else:
            result = getattr(journal, args.command)(args.effect_id)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (OSError, ValueError) as error:
        print(json.dumps({'error': str(error), 'attempt_eligible': False, 'authority_granted': False}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
