import copy
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from instrumentation.records import Record, parse_record, references, validate_approval, validate_claims, validate_evidence, validate_graph, validate_recovery, validate_transition, validate_tree
from instrumentation.scope import compare_snapshots, git_provenance, resolve_scoped_path, snapshot_tree, verify_snapshot


def record(identifier='TASK-000001', **updates):
    fields = {'ID': identifier, 'Target System': 'organization', 'Change Classification': 'organization', 'Authorized Scope': 'agent-org/**', 'Affected Paths or Resources': 'agent-org/**', 'Owning Role': 'Developer', 'Related Requirements': 'REQ-000001', 'Related Tasks': 'none', 'Approval Requirements': 'APP-000001'}
    if identifier.startswith('TASK-'):
        fields.update({'Status': 'ready', 'Parent': 'none', 'Dependencies': 'none', 'Dependency Type': 'blocked_by', 'Plan Approval': 'APP-000001', 'Authorized': 'yes'})
    fields.update(updates)
    return Record(Path(identifier + '.md'), fields)


def grant(**updates):
    return record('APP-000001', Status='approved', **updates)


class RecordsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def write(self, item, directory='tasks'):
        path = self.root / directory / item.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('\n'.join('- ' + k + ': ' + v for k, v in item.fields.items()) + '\n')
        return path

    def candidate(self):
        self.write(grant(), 'approvals')
        self.write(record('REQ-000001'), 'requirements')
        return self.write(record())

    def test_valid_tree_reload_and_references_not_definitions(self):
        path = self.candidate()
        with path.open('a') as stream:
            stream.write('\n## TASK-000001 references TASK-000001\n')
        self.assertEqual(parse_record(path).id, 'TASK-000001')
        result = validate_tree(self.root)
        self.assertTrue(result['valid'], result)
        self.assertEqual(result['record_count'], 3)

    def test_missing_scope_duplicate_id_and_missing_definition(self):
        self.candidate()
        other = self.root / 'tasks' / 'nested' / 'TASK-000001.md'
        other.parent.mkdir()
        other.write_text((self.root / 'tasks/TASK-000001.md').read_text())
        self.assertTrue(any('duplicate ID' in e for e in validate_tree(self.root)['errors']))
        other.unlink()
        target = self.root / 'tasks/TASK-000001.md'
        target.write_text('- ID: TASK-000001\n')
        self.assertTrue(any('missing Authorized Scope' in e for e in validate_tree(self.root)['errors']))
        target.write_text('# TASK-000001\n')
        self.assertTrue(any('missing formal ID' in e for e in validate_tree(self.root)['errors']))

    def test_duplicate_metadata_and_broken_traceability(self):
        path = self.candidate()
        with path.open('a') as stream:
            stream.write('- Authorized: yes\n')
        self.assertFalse(validate_tree(self.root)['valid'])
        self.write(record(**{'Related Requirements': 'REQ-999999'}))
        self.assertTrue(any('broken' in e for e in validate_tree(self.root)['errors']))

    def test_intake_templates_and_code_fences_skipped(self):
        self.candidate()
        intake = self.root / 'intake/approved-v0.1'
        intake.mkdir(parents=True)
        (intake / 'TASK-000001.md').write_text('- ID: TASK-000001\n')
        (self.root / 'tasks/TEMPLATE.md').write_text('- ID: TASK-000001\n')
        self.assertTrue(validate_tree(self.root)['valid'])

    def test_range_reference_expansion(self):
        self.assertEqual(references('REQ-000001 through REQ-000003'), {'REQ-000001', 'REQ-000002', 'REQ-000003'})

    def test_cycle_and_unsatisfied_dependencies(self):
        a = record(**{'Dependencies': 'TASK-000002'})
        b = record('TASK-000002', Dependencies='TASK-000001')
        errors = validate_graph({a.id: a, b.id: b, 'APP-000001': grant()})
        self.assertTrue(any('cycle' in e for e in errors))
        self.assertTrue(any('unsatisfied' in e for e in errors))

    def test_blocked_dependency_is_not_premature_readiness(self):
        a = record(**{'Status': 'blocked', 'Dependencies': 'TASK-000002'})
        b = record('TASK-000002')
        self.assertEqual(validate_graph({a.id: a, b.id: b, 'APP-000001': grant()}), [])
        a.fields['Status'] = 'ready'
        self.assertTrue(any('unsatisfied' in e for e in validate_graph({a.id: a, b.id: b, 'APP-000001': grant()})))

    def test_evidence_missing_and_changed_provenance_rejected(self):
        expected = {k: 'a' * 64 for k in ('candidate_hash', 'instruction_hash', 'policy_hash', 'input_hash', 'output_hash')}
        evidence = {**expected, 'source': 'fixture', 'verifier': 'independent', 'outcome': 'passed'}
        self.assertEqual(validate_evidence(evidence, expected), [])
        evidence['candidate_hash'] = 'b' * 64
        self.assertTrue(validate_evidence(evidence, expected))
        del evidence['policy_hash']
        self.assertTrue(any('policy_hash' in e for e in validate_evidence(evidence, expected)))

    def test_explicit_claim_overlap_and_unknown(self):
        claims = [dict(run_id='RUN-000001', task_id='TASK-000001', status='running', paths=['org/**']), dict(run_id='RUN-000002', task_id='TASK-000002', status='running', paths=['org/rules'])]
        self.assertTrue(validate_claims(claims))
        claims[1]['paths'] = ['project/**']
        self.assertEqual(validate_claims(claims), [])
        claims[1]['status'] = 'unknown'
        self.assertTrue(validate_claims(claims))

    def test_no_records_or_missing_root_fails(self):
        self.assertFalse(validate_tree(self.root)['valid'])
        self.assertFalse(validate_tree(self.root / 'missing')['valid'])

    def test_hierarchy_cycle_and_capability_records(self):
        a = record(Parent='TASK-000002')
        b = record('TASK-000002', Parent=a.id)
        self.assertTrue(any('cycle' in e for e in validate_graph({a.id: a, b.id: b, 'APP-000001': grant()})))
        self.candidate()
        self.write(record('CAP-000001'), 'capabilities')
        self.assertEqual(validate_tree(self.root)['record_count'], 4)

    def test_parent_of_is_nonblocking(self):
        parent = record(**{'Dependencies': 'TASK-000002', 'Dependency Type': 'parent_of'})
        child = record('TASK-000002', Parent='TASK-000001')
        self.assertEqual(validate_graph({parent.id: parent, child.id: child, 'APP-000001': grant()}), [])

    def test_missing_approval_and_unauthorized(self):
        task = record(Authorized='no')
        errors = validate_graph({task.id: task})
        self.assertTrue(any('not authorized' in e for e in errors))
        self.assertTrue(any('plan grant' in e for e in errors))

    def test_claim_conflict_and_unknown_recovery(self):
        a = record('RUN-000001', Status='unknown', Task='TASK-000001')
        b = record('RUN-000002', Status='running', Task='TASK-000001')
        errors = validate_graph({a.id: a, b.id: b})
        self.assertTrue(any('conflicting' in e for e in errors))
        self.assertTrue(any('unresolved ownership' in e for e in errors))

    def test_retries_budget_and_reconciliation(self):
        checkpoint = {'native_status': 'stopped', 'artifacts_verified': True, 'external_effects_reconciled': True}
        self.assertEqual(validate_recovery(checkpoint, attempts=[{'duration_seconds': 1}]), [])
        self.assertTrue(validate_recovery(checkpoint, attempts=[{'duration_seconds': 1}] * 3))
        self.assertTrue(validate_recovery(checkpoint, attempts=[{'duration_seconds': 1}], budget_seconds=1))
        checkpoint['native_status'] = 'unknown'
        self.assertTrue(validate_recovery(checkpoint, attempts=[]))

    def test_state_transitions_and_premature_parent_acceptance(self):
        self.assertEqual(validate_transition('ready', 'in_progress'), [])
        self.assertTrue(validate_transition('ready', 'accepted'))
        parent = record(Status='accepted')
        child = record('TASK-000002', Parent=parent.id)
        errors = validate_graph({parent.id: parent, child.id: child, 'APP-000001': grant()})
        self.assertTrue(any('premature' in e for e in errors))
        self.assertTrue(any('acceptance lacks' in e for e in errors))

    def test_exact_scoped_approval_candidate_operations_expiry(self):
        approval = grant(**{'Authorized Scope': 'org/**', 'Operations': 'write', 'Candidate Hash': 'pinned'})
        self.assertEqual(validate_approval(approval, target='organization', paths=['org/policy.md'], operation='write', candidate_hash='pinned'), [])
        self.assertTrue(validate_approval(approval, target='project', paths=['project/app.py']))
        self.assertTrue(validate_approval(approval, target='organization', paths=['org2/policy.md']))
        self.assertTrue(validate_approval(approval, target='organization', paths=['../org/policy.md']))
        self.assertTrue(validate_approval(approval, target='organization', paths=['org/x'], operation='deploy'))
        self.assertTrue(validate_approval(approval, target='organization', paths=['org/x'], candidate_hash='changed'))
        approval.fields['Expires At'] = '2026-01-01T00:00:00Z'
        self.assertTrue(validate_approval(approval, target='organization', paths=['org/x'], now='2026-10-01T00:00:00Z'))

    def test_X04_X05_cross_boundary_independent_approval(self):
        approval = grant(**{'Target System': 'cross_boundary', 'Authorized Scope': 'org/**; project/**'})
        self.assertTrue(validate_approval(approval, target='project', paths=['project/app']))
        approval.fields['Approved Targets'] = 'organization, project'
        self.assertEqual(validate_approval(approval, target='project', paths=['project/app']), [])
        self.assertEqual(validate_approval(approval, target='organization', paths=['org/rules']), [])

    def test_X06_X07_X08_X09_parent_needs_separate_acceptance(self):
        parent = record(Status='accepted', **{'Target System': 'cross_boundary', 'Acceptance Evidence': 'pinned', 'Intent Reconciliation': 'matched'})
        org = record('TASK-000002', Status='accepted', Parent=parent.id, **{'Acceptance Evidence': 'org tests', 'Intent Reconciliation': 'matched'})
        project = record('TASK-000003', Status='accepted', Parent=parent.id, **{'Target System': 'project', 'Acceptance Evidence': 'product tests', 'Intent Reconciliation': 'matched'})
        records = {r.id: r for r in [parent, org, project, grant()]}
        errors = validate_graph(records)
        self.assertTrue(any('Organization Acceptance' in e for e in errors))
        self.assertTrue(any('Project Acceptance' in e for e in errors))
        self.assertTrue(any('Integration Acceptance' in e for e in errors))
        for label in ('Organization Acceptance', 'Project Acceptance', 'Integration Acceptance'):
            parent.fields[label] = 'passed'
        self.assertEqual(validate_graph(records), [])

    def test_cli_pass_and_fail(self):
        path = self.candidate()
        cli = Path(__file__).resolve().parents[1] / 'instrumentation/check.py'
        passed = subprocess.run([sys.executable, str(cli), '--root', str(self.root)], capture_output=True)
        self.assertEqual(passed.returncode, 0, passed.stdout)
        path.unlink()
        # Add a broken formal task so the failure is meaningful.
        self.write(record(**{'Plan Approval': 'APP-999999'}))
        failed = subprocess.run([sys.executable, str(cli), '--root', str(self.root)], capture_output=True)
        self.assertEqual(failed.returncode, 1)


class ScopeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'org').mkdir()
        (self.root / 'project').mkdir()
        (self.root / 'org/rules').write_text('original')
        (self.root / 'project/app').write_text('original')

    def test_X01_X02_X10_boundary_diff(self):
        before = snapshot_tree(self.root)
        (self.root / 'project/app').write_text('authorized product')
        after = snapshot_tree(self.root)
        self.assertTrue(compare_snapshots(before, after, allowed=['project'])['boundary_preserved'])
        self.assertEqual(compare_snapshots(before, after, allowed=['org'])['violations'], ['project/app'])
        (self.root / 'org/rules').write_text('violation')
        final = snapshot_tree(self.root)
        self.assertEqual(compare_snapshots(after, final, allowed=['project'])['violations'], ['org/rules'])

    def test_traversal_and_symlink_escape(self):
        for path in ('../escape', '/tmp/escape', 'project/app'):
            with self.assertRaises(ValueError):
                resolve_scoped_path(self.root, path, allowed=['org'])
        with tempfile.TemporaryDirectory() as outside:
            (self.root / 'org/link').symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                resolve_scoped_path(self.root, 'org/link/file', allowed=['org'])
            with self.assertRaises(ValueError):
                snapshot_tree(self.root)

    def test_snapshot_tamper_exclusions_bounds_and_deleted_file(self):
        before = snapshot_tree(self.root, exclude=['project'])
        self.assertNotIn('project/app', before['files'])
        tampered = copy.deepcopy(before)
        tampered['files']['org/rules']['sha256'] = 'changed'
        with self.assertRaises(ValueError):
            verify_snapshot(tampered)
        with self.assertRaises(ValueError):
            snapshot_tree(self.root, max_bytes=1)
        (self.root / 'org/rules').unlink()
        after = snapshot_tree(self.root, exclude=['project'])
        self.assertEqual(compare_snapshots(before, after)['violations'], ['org/rules'])

    def test_real_independent_git_provenance(self):
        identities = []
        for name in ('org', 'project'):
            repo = self.root / name
            subprocess.run(['git', 'init', '-q', str(repo)], check=True, capture_output=True)
            initial = git_provenance(repo)
            self.assertIsNone(initial['head'])
            subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(repo), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'fixture'], check=True)
            clean = git_provenance(repo)
            self.assertFalse(clean['dirty'])
            (repo / 'untracked').write_text('fixture')
            dirty = git_provenance(repo)
            self.assertTrue(dirty['dirty'])
            self.assertNotEqual(clean['status_sha256'], dirty['status_sha256'])
            self.assertEqual(len(clean['head']), 40)
            identities.append(clean['repository_identity'])
        self.assertNotEqual(*identities)
