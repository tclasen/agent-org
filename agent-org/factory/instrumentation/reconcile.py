"""Read-only reconciliation of explicitly bounded organization state.

API: reconcile(root, observations=None, worktrees=()) returns a JSON-safe dict
with schema_version, ok (no errors), clean (no errors or warnings), diagnostics
in errors/warnings, roots, records, registries, id_reservations, max_reserved,
ownership, delivery and limits. No claims, files, IDs or Git refs are changed.
root is an agent-org directory; each worktree is an explicit repository directory
containing agent-org (or an agent-org directory). Only formal family directories,
TASK/REQ classification directories, agent role directories, indexes and the ID
ledger are read. Projects, old/, intake and arbitrary nested trees are not scanned.

Observations are None (unavailable) or exactly
{"schema_version": 1, "delivery": [
 {"task_id": "TASK-000001", "availability": "observed",
  "repository": "https://example/repo.git", "ref": "refs/heads/main",
  "candidate_commit": "<full sha>", "merge_commit": "<full sha>",
  "remote_tip": "<full sha>", "observed_at": "<ISO8601 with timezone>",
  "evidence": "attributed receipt/source", "local_repository": "/explicit/repo"}
]}. availability="unavailable" needs only task_id, availability, evidence.
The task must independently bind Delivery Repository, Delivery Ref, and Candidate
Commit (Candidate Revision also accepted) metadata. Optional Merge Commit must
match too. Observed facts are caller-supplied, never authenticated remote truth.
Local Git commit/ancestry checks can corroborate them, never prove remote delivery.
Unknown, contradictory, duplicate or unbound observations never release claims.
"""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

try:
    from .records import CLASSIFICATION_DIRS, ID_RE, RECORD_DIRS, parse_record, references
except ImportError:
    from records import CLASSIFICATION_DIRS, ID_RE, RECORD_DIRS, parse_record, references

ACTIVE = {'ready', 'running', 'in_progress', 'in_review', 'unknown', 'interrupted'}
SHA = re.compile(r'(?:[0-9a-f]{40}|[0-9a-f]{64})')
FORMAL = re.compile(r'[A-Z][A-Z0-9]*-[0-9]{6,}\.md')
LINK = re.compile(r'^- \[([^\]]+)\]\(([^)]+)\)(?:\s+[—–-]\s+(.+))?\s*$')
MAX_BYTES = 2_000_000


def _path(value):
    if not isinstance(value, (str, Path)) or not str(value) or '..' in Path(value).parts:
        raise ValueError('path must be explicit and contain no traversal')
    path = Path(value).absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('symlink paths are refused: ' + str(path))
    return path


def _read(path):
    _path(path)
    if not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError('missing, non-file or oversized input: ' + str(path))
    return path.read_text(encoding='utf-8')


def _title(text):
    return next((line[2:].strip() for line in text.splitlines() if line.startswith('# ')), '')


def _normal_title(title, identifier):
    # Historical indexes sometimes repeat the identifier before the real title.
    while title == identifier or title.startswith(identifier + ' — '):
        title = title[len(identifier):].removeprefix(' — ').strip()
    return ' '.join(title.split()).casefold()


def _git(repo, *args):
    try:
        result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True,
                                text=True, timeout=10, env=None)
        return result.returncode, result.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return -1, ''


def _json_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: ' + key)
        result[key] = value
    return result


def reconcile(root, observations=None, worktrees=()):
    """Return attributed state/diagnostics; see module docstring for schemas."""
    result = dict(schema_version=1, ok=False, clean=False, errors=[], warnings=[],
                  roots=[], records=[], registries=[], id_reservations=[],
                  max_reserved={}, ownership=[], delivery=[], limits=[
                      'Read-only; no ID allocation, claim release, retry or acceptance.',
                      'Supplied external observations are attributed, not authenticated.',
                      'Local Git ancestry does not authenticate a remote tip.',
                      'Only explicitly named roots and canonical bounded paths are inspected.'])

    def diag(level, code, message, source=''):
        result[level].append(dict(code=code, message=message, source=str(source)))

    roots = []
    for index, value in enumerate((root, *worktrees)):
        try:
            path = _path(value)
            if index and (path / 'agent-org').is_dir():
                path = _path(path / 'agent-org')
            if not path.is_dir():
                raise ValueError('organization root does not exist or is not a directory')
            if path in roots:
                diag('warnings', 'duplicate_root', 'Explicit root already inspected', path)
                continue
            roots.append(path)
            result['roots'].append(str(path))
        except (OSError, ValueError) as error:
            diag('errors', 'invalid_root', str(error), value)

    by_root = {}
    all_ids = {}

    def reserve(identifier, source, kind):
        result['id_reservations'].append(dict(id=identifier, source=str(source), kind=kind))
        prefix, number = identifier.rsplit('-', 1)
        result['max_reserved'][prefix] = max(int(number), result['max_reserved'].get(prefix, 0))

    for org in roots:
        records, paths = {}, {}
        by_root[str(org)] = records
        families = dict(RECORD_DIRS, AGENT='agents')
        for prefix, directory in families.items():
            base = org / directory
            candidates = []
            try:
                _path(base)
                if not base.is_dir():
                    diag('warnings', 'missing_family', 'Canonical family directory unavailable', base)
                    continue
                for child in sorted(base.iterdir()):
                    _path(child)
                    if child.is_file() and FORMAL.fullmatch(child.name):
                        candidates.append(child)
                    elif child.is_dir() and prefix in {'TASK', 'REQ'} and child.name in CLASSIFICATION_DIRS:
                        for record_path in sorted(child.iterdir()):
                            _path(record_path)
                            if record_path.is_file() and FORMAL.fullmatch(record_path.name):
                                candidates.append(record_path)
                    elif child.is_dir() and prefix == 'AGENT':
                        if (child / 'AGENTS.md').exists():
                            candidates.append(child / 'AGENTS.md')
                for path in candidates:
                    try:
                        text = _read(path)
                        parsed = parse_record(path)  # Existing formal metadata parser is authoritative.
                        identifier = parsed.fields.get('Agent ID') if prefix == 'AGENT' else parsed.id
                        if not identifier or not re.fullmatch(prefix + r'-\d{6,}', identifier):
                            raise ValueError('missing or wrong-family formal identity')
                        if prefix != 'AGENT' and path.stem != identifier:
                            raise ValueError('filename/ID mismatch')
                        if prefix in {'TASK', 'REQ'} and path.parent.name not in CLASSIFICATION_DIRS:
                            raise ValueError('missing canonical classification directory')
                        item = dict(id=identifier, root=str(org), path=str(path),
                                    title=_title(text), status=parsed.fields.get('Status', 'unknown'),
                                    fields=parsed.fields)
                        result['records'].append(item)
                        reserve(identifier, path, 'definition')
                        if identifier in records:
                            diag('errors', 'duplicate_id', 'Duplicate formal definition: ' + identifier, path)
                        else:
                            records[identifier] = item
                        paths[str(path)] = item
                        all_ids.setdefault(identifier, []).append(item)
                    except (OSError, UnicodeError, ValueError) as error:
                        diag('errors', 'invalid_record', str(error), path)
            except (OSError, ValueError) as error:
                diag('errors', 'unsafe_family', str(error), base)

            index_path = base / 'INDEX.md'
            try:
                index_text = _read(index_path)
                entries = []
                if prefix == 'AGENT':
                    for line in index_text.splitlines():
                        match = re.match(r'^\| (AGENT-\d{6,}) \| \[([^\]]+)\]\(([^)]+)\) \|.*\| ([^|]+) \|$', line)
                        if match:
                            identifier, title, link, status = match.groups()
                            entries.append((identifier + ' — ' + title, link, status.strip()))
                else:
                    for line in index_text.splitlines():
                        match = LINK.fullmatch(line)
                        if match and ID_RE.search(match[1]):
                            entries.append(match.groups())
                seen = set()
                for label, link, suffix in entries:
                    identifier = ID_RE.search(label)[0]
                    registry = dict(root=str(org), index=str(index_path), id=identifier,
                                    title=label, status=suffix or 'unknown', target=link)
                    result['registries'].append(registry)
                    if identifier in seen:
                        diag('errors', 'duplicate_registry_id', 'Repeated index identity: ' + identifier, index_path)
                    seen.add(identifier)
                    try:
                        decoded = unquote(link)
                        if urlsplit(decoded).scheme or Path(decoded).is_absolute() or '..' in Path(decoded).parts or '#' in decoded or '?' in decoded:
                            raise ValueError('registry target must be a canonical relative file')
                        target = _path(base / decoded)
                        if not target.is_relative_to(base):
                            raise ValueError('registry target escapes family')
                        canonical = paths.get(str(target))
                        if canonical is None or canonical['id'] != identifier:
                            diag('errors', 'registry_target_mismatch', 'Registry identity/target has no matching formal definition: ' + identifier, index_path)
                            continue
                        title = _normal_title(label, identifier)
                        expected_title = _normal_title(canonical['title'], identifier)
                        # Identity-only indexes are legacy labels and need refreshing too.
                        if title != expected_title:
                            diag('warnings', 'registry_title_mismatch', identifier + ': registry title differs from record', index_path)
                        if suffix is None:
                            diag('warnings', 'registry_status_missing', identifier + ': registry has no status suffix', index_path)
                        elif suffix != canonical['status']:
                            diag('warnings', 'registry_status_mismatch', identifier + ': registry=' + suffix + ', record=' + canonical['status'], index_path)
                    except (OSError, ValueError) as error:
                        diag('errors', 'unsafe_registry_target', str(error), index_path)
                for identifier, item in records.items():
                    if identifier.startswith(prefix + '-') and identifier not in seen:
                        diag('warnings', 'unindexed_record', identifier + ': formal record absent from index', item['path'])
            except (OSError, UnicodeError, ValueError) as error:
                diag('warnings', 'registry_unavailable', str(error), index_path)

        ledger = org / 'shared/ID_LEDGER.md'
        try:
            ledger_text = _read(ledger)
            ledger_ids = references(ledger_text)
            # Preserve every explicit identity and compact inclusive reservations,
            # including historical reservations; never suggest reuse or allocate IDs.
            for identifier in sorted(ledger_ids):
                reserve(identifier, ledger, 'ledger_reference')
            ranges = re.findall(r'\b([A-Z][A-Z0-9]*)-(\d{6,})\.\.(?:\1-)?(\d+)\b', ledger_text)
            for prefix, start, end in ranges:
                a, b = int(start), int(end)
                if b < a or b - a > 10000:
                    diag('errors', 'invalid_ledger_range', 'Invalid or excessive reservation range', ledger)
                    continue
                for number in range(a, b + 1):
                    identifier = f'{prefix}-{number:0{len(start)}d}'
                    reserve(identifier, ledger, 'ledger_range')
                    ledger_ids.add(identifier)
            if not ID_RE.search(ledger_text):
                diag('errors', 'empty_ledger', 'No explicit identity reservations in ledger', ledger)
            ledger_max = {}
            for identifier in ledger_ids:
                prefix, number = identifier.rsplit('-', 1)
                ledger_max[prefix] = max(int(number), ledger_max.get(prefix, 0))
            for identifier in records:
                prefix, number = identifier.rsplit('-', 1)
                if int(number) > ledger_max.get(prefix, 0):
                    diag('warnings', 'ledger_checkpoint_behind', identifier + ': formal definition exceeds ledger reservation checkpoint; identity remains reserved', ledger)
        except (OSError, UnicodeError, ValueError) as error:
            diag('errors', 'ledger_unavailable', str(error), ledger)
        if not records:
            diag('errors', 'no_records', 'No formal records found; state is unavailable', org)

    # Copies across explicitly named worktrees are reservations, not new definitions
    # in one namespace. Divergent titles for one identity need human reconciliation.
    for identifier, copies in all_ids.items():
        if len({item['root'] for item in copies}) > 1:
            diag('warnings', 'cross_worktree_reservation', identifier + ': identity reserved in multiple explicit roots', ', '.join(item['root'] for item in copies))
            if len({_normal_title(item['title'], identifier) for item in copies}) > 1:
                diag('errors', 'cross_worktree_identity_conflict', identifier + ': differing formal titles across worktrees', '')

    cross_root_owners = {}
    for org, records in by_root.items():
        owners = {}
        for identifier, record in records.items():
            if not identifier.startswith('RUN-') or record['status'] not in ACTIVE:
                continue
            fields = record['fields']
            try:
                tasks = sorted(references(fields.get('Task', fields.get('Related Tasks', ''))))
            except ValueError as error:
                diag('errors', 'invalid_claim_reference', str(error), record['path'])
                tasks = []
            item = dict(run_id=identifier, root=org, task_ids=tasks, status=record['status'],
                        claim=fields.get('Claim', 'unknown'), native_status='unknown',
                        resolution='requires_observation', claim_released=False)
            result['ownership'].append(item)
            diag('warnings', 'unresolved_owner', identifier + ': native ownership is unobserved; claim retained', record['path'])
            for task in tasks:
                if task in owners:
                    diag('errors', 'conflicting_owners', task + ': active runs ' + owners[task] + ', ' + identifier, org)
                owners[task] = identifier
                previous = cross_root_owners.get(task)
                if previous and previous[0] != identifier and previous[1] != org:
                    diag('errors', 'cross_worktree_owner_conflict', task + ': different active run identities across explicit roots', org)
                cross_root_owners[task] = (identifier, org)

    _delivery(result, observations, by_root, roots, diag)
    result['ok'] = not result['errors']
    result['clean'] = not (result['errors'] or result['warnings'])
    return result


def _delivery(result, observations, by_root, roots, diag):
    if observations is None:
        diag('warnings', 'observations_unavailable', 'No external delivery observations supplied; remote delivery remains unknown')
        observations = {'schema_version': 1, 'delivery': []}
    if (not isinstance(observations, dict) or set(observations) != {'schema_version', 'delivery'}
            or type(observations.get('schema_version')) is not int or observations['schema_version'] != 1
            or not isinstance(observations.get('delivery'), list)):
        diag('errors', 'invalid_observations', 'Expected schema_version=1 and delivery list only')
        return
    indexed = {}
    common = {'task_id', 'availability', 'evidence'}
    required = common | {'repository', 'ref', 'candidate_commit', 'merge_commit', 'remote_tip', 'observed_at'}
    for item in observations['delivery']:
        if not isinstance(item, dict):
            diag('errors', 'invalid_observation', 'Delivery observation must be an object')
            continue
        availability = item.get('availability')
        allowed = common if availability == 'unavailable' else required | {'local_repository'}
        if (availability not in {'observed', 'unavailable'} or set(item) - allowed
                or not (common if availability == 'unavailable' else required) <= set(item)
                or any(not isinstance(value, str) or not value.strip() for value in item.values())
                or not re.fullmatch(r'TASK-\d{6,}', item.get('task_id', ''))):
            diag('errors', 'invalid_observation', 'Unknown, missing or invalid delivery fields', str(item.get('task_id', '')))
            continue
        task = item['task_id']
        if task in indexed:
            diag('errors', 'duplicate_observation', 'Multiple observations are ambiguous; no automatic choice', task)
            indexed[task] = None
            continue
        if availability == 'observed':
            try:
                observed_at = datetime.fromisoformat(item['observed_at'].replace('Z', '+00:00'))
                if observed_at.utcoffset() is None:
                    raise ValueError('timezone required')
                if any(not SHA.fullmatch(item[field]) for field in ('candidate_commit', 'merge_commit', 'remote_tip')):
                    raise ValueError('full lowercase commit hashes required')
                if not re.fullmatch(r'refs/heads/[A-Za-z0-9][A-Za-z0-9._/-]*', item['ref']) or '..' in item['ref']:
                    raise ValueError('explicit branch ref required')
            except ValueError as error:
                diag('errors', 'invalid_observation', str(error), task)
                indexed[task] = None
                continue
        indexed[task] = item

    primary = by_root.get(str(roots[0]), {}) if roots else {}
    for task in indexed.keys() - primary.keys():
        diag('errors', 'unknown_observation_task', 'Observation has no primary-root task definition', task)
    for identifier, record in primary.items():
        if not identifier.startswith('TASK-'):
            continue
        item = indexed.get(identifier)
        delivery = dict(task_id=identifier, checkpoint_status=record['status'], state='unknown',
                        verified_delivery=False, claim_released=False, attribution=None,
                        local_check='not_checked')
        result['delivery'].append(delivery)
        if item is None:
            if record['status'] == 'accepted':
                diag('warnings', 'acceptance_delivery_unknown', identifier + ': acceptance prose does not establish current remote delivery', record['path'])
            continue
        delivery['attribution'] = item.copy()
        if item['availability'] == 'unavailable':
            diag('warnings', 'delivery_unavailable', identifier + ': external delivery observation unavailable; no replay decision', item['evidence'])
            continue
        fields = record['fields']
        binding = {'repository': fields.get('Delivery Repository', fields.get('Repository')),
                   'ref': fields.get('Delivery Ref'),
                   'candidate_commit': fields.get('Candidate Commit', fields.get('Candidate Revision'))}
        if not all(binding.values()):
            diag('warnings', 'unbound_delivery', identifier + ': task lacks explicit repository/ref/candidate metadata', record['path'])
            delivery['state'] = 'unbound'
            continue
        mismatches = [key for key, value in binding.items() if item[key] != value]
        if fields.get('Merge Commit') and item['merge_commit'] != fields['Merge Commit']:
            mismatches.append('merge_commit')
        if mismatches:
            diag('errors', 'delivery_binding_mismatch', identifier + ': wrong ' + ', '.join(mismatches), item['evidence'])
            delivery['state'] = 'conflict'
            continue
        try:
            repo = _path(item.get('local_repository', roots[0].parent))
            # Only explicitly scoped local repositories may supply object checks.
            allowed_repos = {org.parent for org in roots}
            if repo not in allowed_repos:
                raise ValueError('local_repository must be the parent of an explicit organization root')
            code, top = _git(repo, 'rev-parse', '--show-toplevel')
            if code or Path(top).resolve() != repo.resolve():
                raise ValueError('explicit local repository unavailable')
            code, remote_urls = _git(repo, 'config', '--get-regexp', r'^remote\..*\.url$')
            if code or item['repository'] not in [line.split(' ', 1)[1] for line in remote_urls.splitlines() if ' ' in line]:
                raise ValueError('repository target does not match any configured local remote URL')
            for field in ('candidate_commit', 'merge_commit', 'remote_tip'):
                if _git(repo, 'cat-file', '-e', item[field] + '^{commit}')[0]:
                    raise ValueError('local commit unavailable: ' + field)
            if _git(repo, 'merge-base', '--is-ancestor', item['candidate_commit'], item['merge_commit'])[0] or _git(repo, 'merge-base', '--is-ancestor', item['merge_commit'], item['remote_tip'])[0]:
                delivery['state'] = 'conflict'
                delivery['local_check'] = 'failed'
                diag('errors', 'delivery_ancestry_mismatch', identifier + ': candidate/merge is not contained in supplied remote tip', item['evidence'])
                continue
            delivery['state'] = 'observed_delivery'
            delivery['local_check'] = 'ancestry_corroborated'
            if record['status'] not in {'accepted', 'archived'}:
                diag('warnings', 'stale_checkpoint', identifier + ': supplied delivery observation corroborates local ancestry while checkpoint remains ' + record['status'], item['evidence'])
            diag('warnings', 'remote_observation_untrusted', identifier + ': supplied remote tip/time remain attributed external facts; independent verification required', item['evidence'])
        except (OSError, ValueError) as error:
            delivery['state'] = 'unconfirmed'
            delivery['local_check'] = 'unavailable'
            diag('warnings', 'delivery_local_check_unavailable', identifier + ': ' + str(error), item['evidence'])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--root', required=True, help='explicit agent-org directory')
    parser.add_argument('--observations', help='versioned delivery observation JSON file; omission means unknown')
    parser.add_argument('--worktree', action='append', default=[], help='explicit known repository/agent-org directory; repeatable')
    parser.add_argument('--format', choices=('json', 'markdown'), default='json')
    args = parser.parse_args(argv)
    observations = None
    input_error = None
    if args.observations:
        try:
            observations = json.loads(_read(_path(args.observations)), object_pairs_hook=_json_no_duplicates,
                                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError('nonfinite JSON: ' + value)))
        except (OSError, UnicodeError, ValueError) as error:
            input_error = str(error)
            observations = {}
    result = reconcile(args.root, observations, args.worktree)
    if input_error:
        result['errors'].append(dict(code='observation_input_error', message=input_error, source=args.observations))
        result['ok'] = result['clean'] = False
    if args.format == 'json':
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print('# Read-only reconciliation\n')
        print(f"Records: {len(result['records'])}; errors: {len(result['errors'])}; warnings: {len(result['warnings'])}\n")
        for level in ('errors', 'warnings'):
            for item in result[level]:
                print(f"- {level[:-1]} `{item['code']}`: {item['message']} ({item['source']})")
        print('\nClaims retained. External observations remain attributed; no verified delivery or acceptance is inferred.')
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
