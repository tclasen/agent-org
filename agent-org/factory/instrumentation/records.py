"""Markdown definitions and explicit approval/work-graph checks.

Only an exact '- ID: TYPE-000001' metadata line defines a record. References,
headings, historical intake, indexes, templates and fixture code define no IDs.
"""
import fnmatch
import re
from dataclasses import dataclass
from pathlib import Path

SCOPE_FIELDS = ('Target System', 'Change Classification', 'Authorized Scope', 'Affected Paths or Resources', 'Owning Role', 'Related Requirements', 'Related Tasks', 'Approval Requirements')
TASK_FIELDS = ('Status', 'Parent', 'Dependencies', 'Dependency Type', 'Plan Approval', 'Authorized')
STATES = ('proposed requirements_ready planned awaiting_approval ready in_progress blocked in_review verified integrated awaiting_acceptance accepted rejected canceled archived').split()
ACTIVE = {'ready', 'in_progress', 'in_review', 'verified', 'integrated', 'awaiting_acceptance'}
BLOCKING = {'blocked_by', 'requires', 'awaits_approval', 'awaits_condition'}
DEPENDENCIES = BLOCKING | {'validates', 'parent_of', 'discovered_from', 'supersedes', 'related_to'}
ID_RE = re.compile(r'\b([A-Z][A-Z0-9]*-[0-9]{6,})\b')
RECORD_DIRS = {'REQ': 'requirements', 'TASK': 'tasks', 'RUN': 'runs',
               'APP': 'approvals', 'DEC': 'decisions', 'EVAL': 'evaluations',
               'EXP': 'experiments', 'ART': 'artifacts', 'INIT': 'initiatives',
               'INTENT': 'intents', 'PLAN': 'plans', 'WF': 'workflows',
               'CAP': 'capabilities', 'TRG': 'triggers'}
FORMAL_DIRS = set(RECORD_DIRS.values())
CLASSIFICATION_DIRS = {'organization': 'organization', 'project': 'project',
                       'cross-boundary': 'cross_boundary'}


@dataclass
class Record:
    path: Path
    fields: dict

    @property
    def id(self):
        return self.fields.get('ID')


def parse_record(path):
    path = Path(path)
    fields = {}
    in_fence = False
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('```') or line.startswith('~~~'):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.fullmatch(r'- ([A-Za-z][A-Za-z0-9 /_-]*):\s*(.*)', line)
        if match:
            key, value = match.groups()
            if key in fields:
                raise ValueError(f'{path}: duplicate metadata {key}')
            fields[key] = value.strip()
    if 'ID' in fields and not re.fullmatch(r'[A-Z][A-Z0-9]*-[0-9]{6,}', fields['ID']):
        raise ValueError(f'{path}: malformed ID')
    return Record(path, fields)


def references(value):
    """Expand explicit inclusive same-prefix 'REQ-000001 through REQ-000040'."""
    result = set(ID_RE.findall(value))
    for prefix, start, end in re.findall(r'([A-Z][A-Z0-9]*)-(\d{6,}) through \1-(\d{6,})', value):
        a, b = int(start), int(end)
        if b < a or b - a > 10000:
            raise ValueError('invalid reference range')
        result.update(f'{prefix}-{number:0{len(start)}d}' for number in range(a, b + 1))
    return result


def _scopes(value):
    return [p.strip() for p in value.split(';') if p.strip()]


def _contains(scope, path):
    if scope.endswith('/**'):
        prefix = scope[:-3].rstrip('/')
        return path == prefix or path.startswith(prefix + '/')
    if scope.endswith('/*'):
        return fnmatch.fnmatchcase(path, scope) and '/' not in path[len(scope) - 1:]
    if scope.endswith('/'):
        return path == scope.rstrip('/') or path.startswith(scope)
    return path == scope


def validate_approval(grant, *, target, paths, operation=None, candidate_hash=None, now=None):
    """Exact functional admission check; prose grants require explicit caller mapping.

    Cross-boundary grants may enumerate per-system children in 'Approved Targets'.
    Their mere classification does not imply both systems are authorized.
    """
    fields = grant.fields if isinstance(grant, Record) else grant
    errors = []
    if fields.get('Status') != 'approved':
        errors.append('approval not approved')
    approved_targets = {p.strip() for p in fields.get('Approved Targets', fields.get('Target System', '')).split(',')}
    if target not in approved_targets:
        errors.append('target not explicitly approved')
    if fields.get('Revoked', 'no').lower() != 'no':
        errors.append('approval revoked')
    if fields.get('Expires At'):
        try:
            from .common import utc
        except ImportError:
            from common import utc
        if now is None or utc(now) >= utc(fields['Expires At']):
            errors.append('approval expired or current time unknown')
    allowed = _scopes(fields.get('Authorized Scope', ''))
    for path in paths:
        if Path(path).is_absolute() or '..' in Path(path).parts or not any(_contains(a, path) for a in allowed):
            errors.append('path not approved: ' + path)
    if operation is not None and operation not in {p.strip() for p in fields.get('Operations', '').split(',')}:
        errors.append('operation not explicitly approved')
    if candidate_hash is not None and fields.get('Candidate Hash') != candidate_hash:
        errors.append('candidate hash changed or unbound')
    return errors


def validate_transition(previous, current):
    if previous not in STATES or current not in STATES:
        return ['unknown task state']
    if previous == current:
        return []
    allowed = {
        'proposed': {'requirements_ready', 'canceled', 'rejected'},
        'requirements_ready': {'planned', 'blocked', 'canceled'},
        'planned': {'awaiting_approval', 'ready', 'blocked', 'canceled'},
        'awaiting_approval': {'ready', 'rejected', 'blocked', 'canceled'},
        'ready': {'in_progress', 'blocked', 'canceled'},
        'in_progress': {'blocked', 'in_review', 'canceled'},
        'blocked': {'ready', 'in_progress', 'canceled'},
        'in_review': {'in_progress', 'verified', 'rejected', 'canceled'},
        'verified': {'integrated', 'in_progress', 'canceled'},
        'integrated': {'awaiting_acceptance', 'in_progress'},
        'awaiting_acceptance': {'accepted', 'in_progress', 'rejected'},
        'accepted': {'in_progress', 'archived'}, 'rejected': {'planned', 'archived'},
        'canceled': {'planned', 'archived'}, 'archived': set(),
    }
    return [] if current in allowed[previous] else [f'invalid transition {previous} -> {current}']


def validate_graph(records):
    if not isinstance(records, dict):
        records = {record.id: record for record in records}
    errors, graph = [], {}
    tasks = {key: r for key, r in records.items() if key.startswith('TASK-')}
    for key, record in tasks.items():
        fields = record.fields
        deps = references(fields.get('Dependencies', ''))
        kind = fields.get('Dependency Type', '')
        if kind not in DEPENDENCIES:
            errors.append(f'{key}: invalid dependency type')
        graph[key] = deps if kind in BLOCKING else set()
        for dep in deps:
            if dep == key:
                errors.append(f'{key}: dependency self-link')
            if dep not in records:
                errors.append(f'{key}: missing dependency {dep}')
            elif kind in BLOCKING and fields.get('Status') in ACTIVE | {'accepted'} and records[dep].fields.get('Status') not in {'accepted', 'archived'}:
                errors.append(f'{key}: unsatisfied prerequisite {dep}')
        if fields.get('Status') in ACTIVE | {'accepted'}:
            if fields.get('Authorized', '').lower() != 'yes':
                errors.append(f'{key}: not authorized')
            approvals = references(fields.get('Plan Approval', ''))
            if not approvals or any(a not in records or records[a].fields.get('Status') != 'approved' for a in approvals):
                errors.append(f'{key}: missing approved plan grant')
            if fields.get('Budget Available', 'yes') != 'yes' or fields.get('Capability Available', 'yes') != 'yes':
                errors.append(f'{key}: budget or capability unavailable')
        children = [r for r in tasks.values() if key in references(r.fields.get('Parent', ''))]
        if fields.get('Status') == 'accepted':
            if not fields.get('Acceptance Evidence') or not fields.get('Intent Reconciliation'):
                errors.append(f'{key}: acceptance lacks evidence/reconciliation')
            if any(r.fields.get('Status') != 'accepted' for r in children):
                errors.append(f'{key}: premature parent acceptance')
        if fields.get('Target System') == 'cross_boundary' and fields.get('Status') == 'accepted':
            if not {'organization', 'project'} <= {r.fields.get('Target System') for r in children}:
                errors.append(f'{key}: missing separately scoped boundary children')
            for field in ('Organization Acceptance', 'Project Acceptance', 'Integration Acceptance'):
                if fields.get(field) != 'passed':
                    errors.append(f'{key}: missing independent {field}')
    visiting, visited = set(), set()
    def visit(key):
        if key in visiting:
            errors.append(f'{key}: dependency/hierarchy cycle')
            return
        if key in visited:
            return
        visiting.add(key)
        for dep in graph.get(key, ()):
            visit(dep)
        visiting.remove(key)
        visited.add(key)
    for key in graph:
        visit(key)
    # Parent relationships are a separate hierarchy, never blocking prerequisites.
    graph = {key: references(r.fields.get('Parent', '')) for key, r in tasks.items()}
    visiting.clear()
    visited.clear()
    for key in graph:
        visit(key)
    active_claims = {}
    for key, record in records.items():
        if not key.startswith('RUN-') or record.fields.get('Status') not in {'ready', 'in_progress', 'running', 'unknown', 'interrupted'}:
            continue
        for task in references(record.fields.get('Task', record.fields.get('Related Tasks', ''))):
            if task in active_claims:
                errors.append(f'{task}: conflicting/unknown active claims {active_claims[task]}, {key}')
            active_claims[task] = key
        if record.fields.get('Status') in {'unknown', 'interrupted'} and record.fields.get('Reconciled') != 'yes':
            errors.append(f'{key}: unresolved ownership; mutation blocked')
    return errors


def validate_recovery(checkpoint, *, attempts, retry_limit=2, budget_seconds=None):
    """Unknown effects/status must be reconciled before retry; history stays caller-owned."""
    errors = []
    for field in ('native_status', 'artifacts_verified', 'external_effects_reconciled'):
        if checkpoint.get(field) not in ({'completed', 'failed', 'stopped'} if field == 'native_status' else {True}):
            errors.append('unresolved recovery field: ' + field)
    if not isinstance(attempts, list) or any(not isinstance(a, dict) or type(a.get('duration_seconds')) not in (int, float) or a['duration_seconds'] < 0 for a in attempts):
        return errors + ['invalid attempt history']
    if len(attempts) > retry_limit:
        errors.append('retry limit exhausted')
    if budget_seconds is not None and sum(a['duration_seconds'] for a in attempts) >= budget_seconds:
        errors.append('cumulative time budget exhausted')
    return errors


def validate_tree(root):
    root = Path(root)
    records, errors = {}, []
    if not root.is_dir():
        return {'valid': False, 'record_count': 0, 'errors': ['record root does not exist or is not a directory'], 'limits': []}
    for path in sorted(root.rglob('*.md')):
        rel = path.relative_to(root)
        if not rel.parts or rel.parts[0] not in FORMAL_DIRS or path.name.upper() in {'INDEX.MD', 'TEMPLATE.MD', 'README.MD'} or any(p.lower() in {'fixtures', 'templates', 'archive-snapshots'} for p in rel.parts):
            continue
        if not re.fullmatch(r'[A-Z][A-Z0-9]*-\d{6,}\.md', path.name):
            continue
        try:
            record = parse_record(path)
        except ValueError as error:
            errors.append(str(error))
            continue
        if not record.id:
            errors.append(f'{rel}: missing formal ID')
            continue
        if path.stem != record.id:
            errors.append(f'{rel}: filename/ID mismatch')
        expected_dir = RECORD_DIRS.get(record.id.split('-', 1)[0])
        if rel.parts[0] != expected_dir:
            errors.append(f'{rel}: wrong record-family directory for {record.id}')
        if record.id.startswith(('TASK-', 'REQ-')):
            if len(rel.parts) != 3 or rel.parts[1] not in CLASSIFICATION_DIRS:
                errors.append(f'{rel}: missing/invalid canonical target directory')
        # An explicit target directory constrains both target metadata fields.
        for directory in rel.parts[1:-1]:
            if directory in CLASSIFICATION_DIRS:
                expected_target = CLASSIFICATION_DIRS[directory]
                for field in ('Target System', 'Change Classification'):
                    if record.fields.get(field) != expected_target:
                        errors.append(f'{rel}: wrong classification directory for {field}')
        if record.id in records:
            errors.append(f'{rel}: duplicate ID {record.id}')
        else:
            records[record.id] = record
        for field in SCOPE_FIELDS + (TASK_FIELDS if record.id.startswith('TASK-') else ()):
            if not record.fields.get(field):
                errors.append(f'{record.id}: missing {field}')
        for field in ('Target System', 'Change Classification'):
            if record.fields.get(field) not in {'organization', 'project', 'cross_boundary'}:
                errors.append(f'{record.id}: invalid {field}')
        if record.id.startswith('TASK-') and record.fields.get('Status') not in STATES:
            errors.append(f'{record.id}: invalid task state')
    for record in records.values():
        for field in ('Related Requirements', 'Related Tasks', 'Approval Requirements', 'Plan Approval', 'Parent', 'Task'):
            try:
                for ref in references(record.fields.get(field, '')):
                    if ref not in records:
                        errors.append(f'{record.id}: broken {field} reference {ref}')
            except ValueError as error:
                errors.append(f'{record.id}: {error}')
        if record.id.startswith('TASK-') and not references(record.fields.get('Related Requirements', '')):
            errors.append(f'{record.id}: missing requirement traceability')
    if not records:
        errors.append('no formal records found')
    errors.extend(validate_graph(records))
    return {'valid': not errors, 'record_count': len(records), 'errors': errors,
            'limits': ['structural checks do not prove behavioral acceptance', 'approval exact-scope APIs must be called by admission workflow', 'no universal interception', 'provenance required by evidence-producing callers']}


def validate_evidence(evidence, expected):
    """Require exact pinned provenance identities; unknown is not passing evidence."""
    errors = []
    for field in ('candidate_hash', 'instruction_hash', 'policy_hash', 'input_hash', 'output_hash'):
        actual = evidence.get(field)
        if not isinstance(actual, str) or not re.fullmatch(r'[0-9a-f]{64}', actual):
            errors.append('missing/invalid provenance ' + field)
        if field not in expected or actual != expected[field]:
            errors.append('unbound/changed provenance ' + field)
    if not evidence.get('source') or not evidence.get('verifier'):
        errors.append('missing evidence source/verifier')
    if evidence.get('outcome') not in {'passed', 'failed', 'unknown'}:
        errors.append('invalid evidence outcome')
    return errors


def validate_claims(claims):
    """Check explicit normalized resource claims (not prose inferred authority).

    Claim schema: run_id, task_id, status, paths; paths are exact, trailing slash
    directory scopes or '/**' trees. Unknown ownership remains active.
    """
    errors = []
    active = []
    for claim in claims:
        if claim.get('status') not in {'ready', 'running', 'in_progress', 'unknown', 'interrupted'}:
            continue
        paths = claim.get('paths')
        if not isinstance(paths, list) or not paths or any(not isinstance(p, str) or not p or Path(p).is_absolute() or '..' in Path(p).parts for p in paths):
            errors.append('invalid explicit claim scope')
            continue
        if claim.get('status') in {'unknown', 'interrupted'}:
            errors.append('unresolved ownership: ' + str(claim.get('run_id')))
        for previous in active:
            overlap = any(_contains(a, b.removesuffix('/**').rstrip('/')) or _contains(b, a.removesuffix('/**').rstrip('/')) for a in paths for b in previous['paths'])
            if claim.get('task_id') == previous.get('task_id') or overlap:
                errors.append('conflicting claims: ' + str(previous.get('run_id')) + ', ' + str(claim.get('run_id')))
        active.append(claim)
    return errors
