#!/usr/bin/env python3
"""Run resettable behavioral scenarios through real deterministic tool CLIs.

Local fixtures only: no models, external services, dispatch or promotion. Positive
and expected-refusal results are distinguished; failures remain in the report.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def _record(root, relative, identifier, **fields):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    metadata = {'ID': identifier, 'Target System': 'organization', 'Change Classification': 'organization',
                'Authorized Scope': 'agent-org/**', 'Affected Paths or Resources': 'agent-org/**',
                'Owning Role': 'Developer', 'Related Requirements': 'REQ-999001',
                'Related Tasks': 'none', 'Approval Requirements': 'APP-999001', 'Status': 'in_progress'}
    metadata.update(fields)
    path.write_text('# Fixture ' + identifier + '\n\n' + '\n'.join('- ' + k + ': ' + v for k, v in metadata.items()) + '\n')
    return path


def _fixture(base):
    org = base / 'agent-org'
    for relative in ('AGENTS.md', 'policies/AUTHORITY.md', 'policies/SCOPE_BOUNDARIES.md',
                     'shared/SESSION_LIFECYCLE.md', 'shared/CONTEXT_MANAGEMENT.md', 'agents/INDEX.md',
                     'agents/developer/AGENTS.md', 'agents/developer/CONTEXT.md', 'shared/fixture-plan.md'):
        path = org / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('# Controlled scenario fixture\n')
    (base / 'AGENTS.md').write_text('# Controlled fixture entrypoint\n')
    _record(org, 'tasks/organization/TASK-999001.md', 'TASK-999001',
            **{'Authorized': 'yes', 'Plan Approval': 'APP-999001', 'Plan Revision': '1',
               'Plan Path': 'shared/fixture-plan.md', 'Claim': 'RUN-999001'})
    _record(org, 'runs/RUN-999001.md', 'RUN-999001', Task='TASK-999001')
    _record(org, 'requirements/organization/REQ-999001.md', 'REQ-999001')
    _record(org, 'approvals/APP-000001.md', 'APP-000001', Status='approved')
    _record(org, 'approvals/APP-999001.md', 'APP-999001', Status='approved', **{'Plan Revision': '1'})
    (org / 'tasks/INDEX.md').write_text('- [TASK-999001 — corrupted title](organization/TASK-999001.md) — accepted\n')
    (org / 'shared/ID_LEDGER.md').write_text('Allocated through: TASK-999000, RUN-999000, REQ-999000, APP-999000.\n')
    return org


def run_scenarios(root):
    root = Path(root).resolve(strict=True)
    if not (root / 'factory/instrumentation').is_dir():
        raise ValueError('expected an organization root with implemented instrumentation')
    tools = root / 'factory/instrumentation'
    results = []

    def cli(name, args):
        process = subprocess.run([sys.executable, str(tools / name), *map(str, args)],
                                 capture_output=True, text=True, timeout=30)
        try:
            data = json.loads(process.stdout)
        except ValueError:
            data = {'non_json_output': process.stdout, 'stderr': process.stderr}
        return process.returncode, data

    def outcome(name, passed, expected, code, data):
        results.append({'scenario': name, 'expected': expected, 'passed': bool(passed),
                        'exit_code': code, 'observation': data})

    with tempfile.TemporaryDirectory(prefix='agent-org-scenarios-') as temporary:
        base = Path(temporary).resolve()
        org = _fixture(base)
        code, data = cli('reconcile.py', ['--root', org])
        codes = {row['code'] for row in data.get('warnings', [])}
        outcome('registry_disagreement', {'registry_title_mismatch', 'registry_status_mismatch'} <= codes,
                'detect title and suffix discrepancy; do not release claim', code,
                {'diagnostic_codes': sorted(codes), 'claim_released': [x['claim_released'] for x in data.get('ownership', [])]})
        code, data = cli('context.py', ['--root', org, '--task', 'TASK-999001', '--run', 'RUN-999001', '--role', 'developer'])
        outcome('scoped_manifest', code == 0 and bool(data.get('sources')), 'manifest retains mandatory authority', code,
                {'source_count': len(data.get('sources', []))})
        (org / 'policies/AUTHORITY.md').unlink()
        code, data = cli('context.py', ['--root', org, '--task', 'TASK-999001', '--run', 'RUN-999001', '--role', 'developer'])
        outcome('missing_authority_refusal', code != 0, 'refuse missing authority', code, data)
        journal = 'factory/reports/sequence.jsonl'
        effect_id = 'controlled-write'
        intent = dict(effect_id=effect_id, operation='fixture_write', resource='fixture-repo', target='fixture-main',
                      candidate_hash=hashlib.sha256(b'fixture candidate').hexdigest(), authority='APP-999001',
                      task='TASK-999001', run='RUN-999001')
        prefix = ['--root', org, '--journal', journal]
        code, data = cli('effects.py', [*prefix, 'prepare', '--intent', json.dumps(intent)])
        outcome('effect_prepare', code == 0, 'prepare bounded intent', code, data)
        code, data = cli('effects.py', [*prefix, 'attempt', '--effect-id', effect_id])
        outcome('effect_attempt', code == 0 and data.get('appended') is True, 'record before dispatch', code, data)
        code, data = cli('effects.py', [*prefix, 'attempt', '--effect-id', effect_id])
        outcome('lost_acknowledgement_no_replay', code == 0 and data.get('appended') is False,
                'second attempt cannot redispatch while unknown', code, data)
        receipt = dict(status='confirmed', resource=intent['resource'], target=intent['target'],
                       candidate_hash=intent['candidate_hash'], source='controlled fixture destination lookup',
                       observed_at='2026-10-22T00:00:00Z', remote_identity='fixture-commit')
        code, data = cli('effects.py', [*prefix, 'observe', '--effect-id', effect_id, '--receipt', json.dumps(receipt)])
        outcome('destination_observed', code == 0, 'matching receipt retained', code, data)
        code, data = cli('effects.py', [*prefix, 'attempt', '--effect-id', effect_id])
        outcome('confirmed_effect_no_replay', code == 0 and data.get('appended') is False,
                'confirmed destination prevents another attempt', code, data)
        protected = org / 'protected.md'
        protected.write_text('preserve fixture\n')
        before = protected.read_bytes()
        code, data = cli('effects.py', ['--root', org, '--journal', '../protected.md', 'prepare', '--intent', json.dumps(intent)])
        outcome('escaped_journal_refusal', code != 0 and protected.read_bytes() == before,
                'refuse escaped journal and preserve resource', code, data)
        candidates = org / 'knowledge/improvement-candidates'
        candidates.mkdir(parents=True)
        template = '# Fixture candidate\n- Candidate: {name}\n- Parent: {parent}\n- Content Hash: {hash}\n- Incident Family: fixture-family\n- Partition: {partition}\n- Exposures: {exposure}\n'
        (candidates / 'a.md').write_text(template.format(name='ancestor', parent='none', hash='a'*64,
                                                       partition='development', exposure='final'))
        (candidates / 'b.md').write_text(template.format(name='descendant', parent='ancestor', hash='b'*64,
                                                       partition='final', exposure='none'))
        code, data = cli('learning.py', ['validate', '--root', org])
        errors = data.get('errors', [])
        outcome('exposed_final_partition_refusal', code != 0 and any('final-test exposure' in x for x in errors)
                and any('partition leakage' in x for x in errors), 'detect exposure and incident-family leakage', code, data)
    return {'schema_version': 1, 'observation_kind': 'controlled_local_cli_scenarios',
            'passed': all(x['passed'] for x in results), 'scenario_count': len(results), 'results': results,
            'limits': ['No remote service, model or hidden holdout tested.',
                       'Fresh-worker and real PR delivery evidence are separate.',
                       'No promotion decision or universal interception claim.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='agent-org')
    args = parser.parse_args()
    try:
        result = run_scenarios(args.root)
        print(json.dumps(result, indent=2))
        return 0 if result['passed'] else 1
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(json.dumps({'passed': False, 'error': str(error)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
