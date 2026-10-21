# Complete installation file structure

Actual installation files below exclude ignored execution checkouts/bytecode. Root integration consists only of `.gitignore` and `.github/workflows/agent-org.yml`. No root AGENTS or harness configuration is added.

```text
agent-org/
├── AGENTS.md
├── README.md
├── agents/
│   ├── INDEX.md
│   ├── architect/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   ├── chief-of-staff/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   ├── coordinator/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   ├── developer/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   ├── executor/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   ├── planner/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   ├── researcher/
│   │   ├── AGENTS.md
│   │   └── CONTEXT.md
│   └── reviewer/
│       ├── AGENTS.md
│       └── CONTEXT.md
├── approvals/
│   ├── APP-000001.md
│   ├── APP-000002.md
│   ├── APP-000003.md
│   ├── APP-000004.md
│   ├── APP-000005.md
│   ├── APP-000006.md
│   └── INDEX.md
├── artifacts/
│   ├── ART-000001.md
│   ├── ART-000002.md
│   ├── ART-000003.md
│   ├── ART-000004.md
│   ├── ART-000005.md
│   ├── DIRECTORY_STRUCTURE.md
│   ├── INDEX.md
│   └── INSTALLATION_REPORT.md
├── capabilities/
│   ├── CAP-000001.md
│   ├── CAP-000002.md
│   ├── CAP-000003.md
│   ├── CAP-000004.md
│   ├── CAP-000005.md
│   ├── CAP-000006.md
│   ├── CAP-000007.md
│   ├── CAP-000008.md
│   ├── CAP-000009.md
│   ├── CAP-000010.md
│   ├── CAP-000011.md
│   ├── CAP-000012.md
│   ├── CAP-000013.md
│   ├── CAP-000014.md
│   ├── CAP-000015.md
│   ├── CAP-000016.md
│   ├── CAP-000017.md
│   ├── CAP-000018.md
│   ├── CAP-000019.md
│   ├── CAP-000020.md
│   ├── CAP-000021.md
│   ├── CAP-000022.md
│   └── INDEX.md
├── decisions/
│   ├── DEC-000015.md
│   └── INDEX.md
├── evaluations/
│   ├── EVAL-000001.md
│   ├── EVAL-000002.md
│   ├── EVAL-000003.md
│   ├── EVAL-000004.md
│   ├── EVAL-000005.md
│   ├── EVAL-000006.md
│   ├── EVAL-000007.md
│   ├── FAILURES.md
│   └── INDEX.md
├── experiments/
│   ├── EXP-000001.md
│   ├── INDEX.md
│   └── TEMPLATE.md
├── factory/
│   ├── README.md
│   ├── artifacts/
│   │   └── INDEX.md
│   ├── baselines/
│   │   ├── EXP-000001/
│   │   │   └── records.py
│   │   ├── INDEX.md
│   │   ├── dora-1.0.0/
│   │   │   ├── DEFINITIONS.md
│   │   │   ├── calculator.py
│   │   │   ├── classification.json
│   │   │   ├── events.json
│   │   │   ├── expected.json
│   │   │   └── test_dora.py
│   │   ├── gate-1.0.0/
│   │   │   ├── DEFINITION.md
│   │   │   ├── efficiency.json
│   │   │   ├── improvement.py
│   │   │   ├── repair.json
│   │   │   └── test_improvement.py
│   │   ├── guide-initial/
│   │   │   └── PROJECT_ENROLLMENT.md
│   │   ├── measurement-candidate-attempt1/
│   │   │   ├── benchmarks/
│   │   │   │   ├── efficiency.json
│   │   │   │   └── repair.json
│   │   │   ├── dora/
│   │   │   │   ├── DEFINITIONS.md
│   │   │   │   ├── calculator.py
│   │   │   │   └── fixtures/
│   │   │   │       └── expected.json
│   │   │   ├── quality-gates/
│   │   │   │   ├── DEFINITION.md
│   │   │   │   └── improvement.py
│   │   │   └── tests/
│   │   │       ├── test_dora.py
│   │   │       ├── test_gate_regressions.py
│   │   │       └── test_improvement.py
│   │   └── measurement-candidate-retry1/
│   │       ├── benchmarks/
│   │       │   ├── efficiency.json
│   │       │   └── repair.json
│   │       ├── quality-gates/
│   │       │   └── improvement.py
│   │       └── tests/
│   │           └── test_gate_regressions.py
│   ├── benchmarks/
│   │   ├── README.md
│   │   ├── efficiency.json
│   │   └── repair.json
│   ├── dora/
│   │   ├── DEFINITIONS.md
│   │   ├── calculator.py
│   │   ├── classification.json
│   │   └── fixtures/
│   │       ├── classification.json
│   │       ├── events.json
│   │       └── expected.json
│   ├── events/
│   │   ├── README.md
│   │   └── installation.jsonl
│   ├── instrumentation/
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── check.py
│   │   ├── common.py
│   │   ├── events.py
│   │   ├── records.py
│   │   ├── runner.py
│   │   └── scope.py
│   ├── metrics/
│   │   ├── DEFINITIONS.md
│   │   └── scorecards.py
│   ├── provenance/
│   │   ├── README.md
│   │   ├── installation-environment.json
│   │   └── installation-precommit.json
│   ├── quality-gates/
│   │   ├── DEFINITION.md
│   │   └── improvement.py
│   ├── reports/
│   │   ├── EXP-000001-after-approvals.json
│   │   ├── EXP-000001-before-approvals.json
│   │   ├── EXP-000001-preregistration.json
│   │   ├── EXP-000001-qualification.json
│   │   ├── INDEX.md
│   │   ├── RUN-000008/
│   │   │   ├── baseline.metadata.json
│   │   │   ├── baseline.stderr.txt
│   │   │   ├── baseline.stdout.json
│   │   │   ├── candidate.metadata.json
│   │   │   ├── candidate.stderr.txt
│   │   │   ├── candidate.stdout.json
│   │   │   ├── records_cli.metadata.json
│   │   │   ├── records_cli.stderr.txt
│   │   │   ├── records_cli.stdout.txt
│   │   │   ├── rollback.json
│   │   │   ├── suite.metadata.json
│   │   │   ├── suite.stderr.txt
│   │   │   └── suite.stdout.txt
│   │   ├── RUN-000010/
│   │   │   ├── HANDOFF.md
│   │   │   ├── artifact-manifest.json
│   │   │   ├── checkpoint.json
│   │   │   ├── controlled-scenarios.json
│   │   │   ├── discovery/
│   │   │   │   └── agents/
│   │   │   │       ├── INDEX.md
│   │   │   │       ├── architect/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── chief-of-staff/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── coordinator/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── developer/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── executor/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── planner/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── qualification-specialist/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       ├── researcher/
│   │   │   │       │   ├── AGENTS.md
│   │   │   │       │   └── CONTEXT.md
│   │   │   │       └── reviewer/
│   │   │   │           ├── AGENTS.md
│   │   │   │           └── CONTEXT.md
│   │   │   ├── discovery.json
│   │   │   ├── recovery.json
│   │   │   └── source-pins.json
│   │   ├── RUN-000011/
│   │   │   ├── adversarial-output.jsonl
│   │   │   ├── adversarial.py
│   │   │   └── pins.json
│   │   ├── RUN-000012/
│   │   │   ├── EXP-000001-binding-approval.json
│   │   │   ├── HANDOFF.md
│   │   │   ├── TASK-000018-repair-addendum.md
│   │   │   ├── TASK-000018-review.md
│   │   │   ├── baseline.stderr
│   │   │   ├── baseline.stdout
│   │   │   ├── candidate.stderr
│   │   │   ├── candidate.stdout
│   │   │   ├── checks.json
│   │   │   ├── end-pins.json
│   │   │   ├── evidence-manifest.json
│   │   │   ├── identities-project-rollback.json
│   │   │   ├── project.stderr
│   │   │   ├── project.stdout
│   │   │   ├── provenance.json
│   │   │   ├── records.stderr
│   │   │   ├── records.stdout
│   │   │   ├── rollback-records.py
│   │   │   ├── suite.stderr
│   │   │   ├── suite.stdout
│   │   │   ├── test_records.migration.diff
│   │   │   └── test_records.original.py
│   │   ├── RUN-000015/
│   │   │   ├── artifact-sha256.json
│   │   │   ├── before.json
│   │   │   ├── candidate-freeze-proposal.json
│   │   │   ├── candidate-freeze-retry1-proposal.json
│   │   │   ├── dora-cli.metadata.json
│   │   │   ├── dora-cli.stderr.txt
│   │   │   ├── dora-cli.stdout.txt
│   │   │   ├── dual-version.metadata.json
│   │   │   ├── dual-version.stderr.txt
│   │   │   ├── dual-version.stdout.json
│   │   │   ├── extended-replay.py
│   │   │   ├── final-git-readonly.stderr.txt
│   │   │   ├── final-git-readonly.stdout.txt
│   │   │   ├── final-manifest.json
│   │   │   ├── full-suite.metadata.json
│   │   │   ├── full-suite.stderr.txt
│   │   │   ├── full-suite.stdout.txt
│   │   │   ├── gate-efficiency-cli.metadata.json
│   │   │   ├── gate-efficiency-cli.stderr.txt
│   │   │   ├── gate-efficiency-cli.stdout.txt
│   │   │   ├── gate-repair-cli.metadata.json
│   │   │   ├── gate-repair-cli.stderr.txt
│   │   │   ├── gate-repair-cli.stdout.txt
│   │   │   ├── isolated-restore.metadata.json
│   │   │   ├── isolated-restore.stderr.txt
│   │   │   ├── isolated-restore.stdout.txt
│   │   │   ├── original/
│   │   │   │   └── factory/
│   │   │   │       ├── benchmarks/
│   │   │   │       │   ├── efficiency.json
│   │   │   │       │   └── repair.json
│   │   │   │       ├── dora/
│   │   │   │       │   ├── DEFINITIONS.md
│   │   │   │       │   ├── calculator.py
│   │   │   │       │   └── fixtures/
│   │   │   │       │       └── expected.json
│   │   │   │       ├── quality-gates/
│   │   │   │       │   ├── DEFINITION.md
│   │   │   │       │   └── improvement.py
│   │   │   │       └── tests/
│   │   │   │           ├── test_dora.py
│   │   │   │           └── test_improvement.py
│   │   │   ├── records-cli.metadata.json
│   │   │   ├── records-cli.stderr.txt
│   │   │   ├── records-cli.stdout.txt
│   │   │   ├── retained-original.metadata.json
│   │   │   ├── retained-original.stderr.txt
│   │   │   ├── retained-original.stdout.jsonl
│   │   │   ├── retry1-dual-version.metadata.json
│   │   │   ├── retry1-dual-version.stderr.txt
│   │   │   ├── retry1-dual-version.stdout.txt
│   │   │   ├── retry1-extended-replay.metadata.json
│   │   │   ├── retry1-extended-replay.stderr.txt
│   │   │   ├── retry1-extended-replay.stdout.txt
│   │   │   ├── retry1-full-suite.metadata.json
│   │   │   ├── retry1-full-suite.stderr.txt
│   │   │   └── retry1-full-suite.stdout.txt
│   │   ├── RUN-000015-attempt1/
│   │   │   ├── before.json
│   │   │   ├── candidate-freeze-proposal.json
│   │   │   ├── dual-version.metadata.json
│   │   │   ├── dual-version.stderr.txt
│   │   │   ├── dual-version.stdout.json
│   │   │   ├── full-suite.metadata.json
│   │   │   ├── full-suite.stderr.txt
│   │   │   ├── full-suite.stdout.txt
│   │   │   ├── original/
│   │   │   │   └── factory/
│   │   │   │       ├── benchmarks/
│   │   │   │       │   ├── efficiency.json
│   │   │   │       │   └── repair.json
│   │   │   │       ├── dora/
│   │   │   │       │   ├── DEFINITIONS.md
│   │   │   │       │   ├── calculator.py
│   │   │   │       │   └── fixtures/
│   │   │   │       │       └── expected.json
│   │   │   │       ├── quality-gates/
│   │   │   │       │   ├── DEFINITION.md
│   │   │   │       │   └── improvement.py
│   │   │   │       └── tests/
│   │   │   │           ├── test_dora.py
│   │   │   │           └── test_improvement.py
│   │   │   ├── retained-original.metadata.json
│   │   │   ├── retained-original.stderr.txt
│   │   │   └── retained-original.stdout.jsonl
│   │   ├── RUN-000017/
│   │   │   ├── REVIEW.md
│   │   │   ├── dora.diff
│   │   │   ├── dora_definition.diff
│   │   │   ├── evidence-manifest.json
│   │   │   ├── extended58.metadata.json
│   │   │   ├── extended58.stderr
│   │   │   ├── extended58.stdout
│   │   │   ├── full-suite.metadata.json
│   │   │   ├── full-suite.stderr
│   │   │   ├── full-suite.stdout
│   │   │   ├── gate.diff
│   │   │   ├── gate_definition.diff
│   │   │   ├── independent-results.json
│   │   │   ├── independent_checks.py
│   │   │   ├── missing-attempts-results.json
│   │   │   ├── missing_attempts_repro.py
│   │   │   ├── original22.json
│   │   │   ├── pins-end.json
│   │   │   ├── pins-start.json
│   │   │   ├── rollback30.metadata.json
│   │   │   ├── rollback30.stderr
│   │   │   └── rollback30.stdout
│   │   ├── RUN-000019/
│   │   │   ├── before-git-readonly-safe.json
│   │   │   ├── before-git-readonly.json
│   │   │   ├── before-inventory.json
│   │   │   ├── candidate-freeze-proposal.json
│   │   │   ├── concurrent-root-ledger-append.json
│   │   │   ├── efficiency.json.diff
│   │   │   ├── end-git-readonly.json
│   │   │   ├── end-inventory-failure.json
│   │   │   ├── end-inventory.json
│   │   │   ├── extended58.metadata.json
│   │   │   ├── extended58.stderr
│   │   │   ├── extended58.stdout
│   │   │   ├── final-manifest.json
│   │   │   ├── full-suite.metadata.json
│   │   │   ├── full-suite.stderr
│   │   │   ├── full-suite.stdout
│   │   │   ├── gate-efficiency-cli.metadata.json
│   │   │   ├── gate-efficiency-cli.stderr
│   │   │   ├── gate-efficiency-cli.stdout
│   │   │   ├── gate-repair-cli.metadata.json
│   │   │   ├── gate-repair-cli.stderr
│   │   │   ├── gate-repair-cli.stdout
│   │   │   ├── improvement.py.diff
│   │   │   ├── isolated-restore/
│   │   │   │   ├── benchmarks/
│   │   │   │   │   ├── efficiency.json
│   │   │   │   │   └── repair.json
│   │   │   │   ├── dora/
│   │   │   │   │   ├── calculator.py
│   │   │   │   │   └── fixtures/
│   │   │   │   │       ├── classification.json
│   │   │   │   │       ├── events.json
│   │   │   │   │       └── expected.json
│   │   │   │   ├── instrumentation/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── common.py
│   │   │   │   │   └── events.py
│   │   │   │   ├── metrics/
│   │   │   │   │   └── scorecards.py
│   │   │   │   ├── quality-gates/
│   │   │   │   │   └── improvement.py
│   │   │   │   └── tests/
│   │   │   │       ├── test_dora.py
│   │   │   │       └── test_improvement.py
│   │   │   ├── isolated-restore-input-pins.json
│   │   │   ├── isolated-restore30.metadata.json
│   │   │   ├── isolated-restore30.stderr
│   │   │   ├── isolated-restore30.stdout
│   │   │   ├── original22.metadata.json
│   │   │   ├── original22.stderr
│   │   │   ├── original22.stdout
│   │   │   ├── repair.json.diff
│   │   │   ├── retry1-before/
│   │   │   │   └── factory/
│   │   │   │       ├── benchmarks/
│   │   │   │       │   ├── efficiency.json
│   │   │   │       │   └── repair.json
│   │   │   │       ├── quality-gates/
│   │   │   │       │   └── improvement.py
│   │   │   │       └── tests/
│   │   │   │           └── test_gate_regressions.py
│   │   │   ├── sixcase-sameversion.metadata.json
│   │   │   ├── sixcase-sameversion.stderr
│   │   │   ├── sixcase-sameversion.stdout
│   │   │   ├── sixcase_sameversion_replay.py
│   │   │   └── test_gate_regressions.py.diff
│   │   ├── RUN-000020/
│   │   │   ├── REVIEW.md
│   │   │   ├── efficiency.json.diff
│   │   │   ├── evidence-manifest.json
│   │   │   ├── evidence-verification.json
│   │   │   ├── evidence_checks.py
│   │   │   ├── finalize.py
│   │   │   ├── focused-results.json
│   │   │   ├── improvement.py.diff
│   │   │   ├── pins-end.json
│   │   │   ├── pins-start.json
│   │   │   ├── repair.json.diff
│   │   │   ├── review_checks.py
│   │   │   ├── reviewer-check-correction.txt
│   │   │   └── test_gate_regressions.py.diff
│   │   ├── initial-ci.json
│   │   ├── live-command-capture.json
│   │   ├── scorecard-observations.json
│   │   └── scorecards.json
│   └── tests/
│       ├── test_dora.py
│       ├── test_events.py
│       ├── test_gate_regressions.py
│       ├── test_improvement.py
│       ├── test_records.py
│       ├── test_runner.py
│       └── test_validator_regressions.py
├── initiatives/
│   ├── INDEX.md
│   └── INIT-000001.md
├── intake/
│   ├── ACCEPTANCE_CONTRACT.md
│   ├── COVERAGE.md
│   ├── DISCOVERY.md
│   ├── INDEX.md
│   ├── INSTALLATION_PLAN.md
│   ├── INSTALLATION_RESULTS.md
│   ├── INTERVIEW.md
│   ├── REQUIREMENTS_BASELINE.md
│   ├── REVIEW.md
│   ├── SCOPE_CONTRACT.md
│   ├── STATUS.md
│   └── approved-v0.1/
│       ├── ACCEPTANCE_CONTRACT.md
│       ├── COVERAGE.md
│       ├── DISCOVERY.md
│       ├── INDEX.md
│       ├── INSTALLATION_PLAN.md
│       ├── INTERVIEW.md
│       ├── REQUIREMENTS_BASELINE.md
│       ├── REVIEW.md
│       └── SCOPE_CONTRACT.md
├── intents/
│   ├── INDEX.md
│   └── INTENT-000001.md
├── knowledge/
│   ├── INDEX.md
│   ├── PROJECT_ENROLLMENT.md
│   └── projects/
│       ├── INDEX.md
│       └── TEMPLATE.md
├── policies/
│   ├── ACCEPTANCE.md
│   ├── APPROVALS.md
│   ├── AUTHORITY.md
│   ├── CHANGE_CONTROL.md
│   ├── CROSS_BOUNDARY_CHANGES.md
│   ├── DATA_HANDLING.md
│   ├── GIT.md
│   ├── INDEX.md
│   ├── MEASUREMENT_INDEPENDENCE.md
│   ├── MODEL_SELECTION.md
│   ├── ORGANIZATION_CHANGES.md
│   ├── PERMISSIONS.md
│   ├── PLANNING.md
│   ├── PROJECT_CHANGES.md
│   ├── RESOURCE_BUDGETS.md
│   ├── ROUTING.md
│   ├── SCOPE_BOUNDARIES.md
│   └── SELF_IMPROVEMENT.md
├── requirements/
│   ├── INDEX.md
│   ├── TEMPLATE.md
│   ├── cross-boundary/
│   │   ├── REQ-000003.md
│   │   ├── REQ-000004.md
│   │   ├── REQ-000007.md
│   │   ├── REQ-000010.md
│   │   ├── REQ-000020.md
│   │   ├── REQ-000021.md
│   │   ├── REQ-000024.md
│   │   ├── REQ-000029.md
│   │   └── REQ-000030.md
│   ├── organization/
│   │   ├── REQ-000001.md
│   │   ├── REQ-000002.md
│   │   ├── REQ-000005.md
│   │   ├── REQ-000006.md
│   │   ├── REQ-000008.md
│   │   ├── REQ-000009.md
│   │   ├── REQ-000011.md
│   │   ├── REQ-000012.md
│   │   ├── REQ-000013.md
│   │   ├── REQ-000014.md
│   │   ├── REQ-000015.md
│   │   ├── REQ-000016.md
│   │   ├── REQ-000017.md
│   │   ├── REQ-000018.md
│   │   ├── REQ-000019.md
│   │   ├── REQ-000022.md
│   │   ├── REQ-000025.md
│   │   ├── REQ-000026.md
│   │   ├── REQ-000027.md
│   │   ├── REQ-000028.md
│   │   ├── REQ-000031.md
│   │   ├── REQ-000032.md
│   │   ├── REQ-000033.md
│   │   ├── REQ-000034.md
│   │   ├── REQ-000035.md
│   │   ├── REQ-000036.md
│   │   ├── REQ-000037.md
│   │   ├── REQ-000038.md
│   │   ├── REQ-000039.md
│   │   ├── REQ-000040.md
│   │   └── REQ-000042.md
│   └── project/
│       ├── REQ-000023.md
│       └── REQ-000041.md
├── runs/
│   ├── INDEX.md
│   ├── RUN-000001.md
│   ├── RUN-000002.md
│   ├── RUN-000003.md
│   ├── RUN-000004.md
│   ├── RUN-000005.md
│   ├── RUN-000006.md
│   ├── RUN-000007.md
│   ├── RUN-000008.md
│   ├── RUN-000009.md
│   ├── RUN-000010.md
│   ├── RUN-000011.md
│   ├── RUN-000012.md
│   ├── RUN-000013.md
│   ├── RUN-000014.md
│   ├── RUN-000015.md
│   ├── RUN-000016.md
│   ├── RUN-000017.md
│   ├── RUN-000018.md
│   ├── RUN-000019.md
│   ├── RUN-000020.md
│   ├── RUN-000021.md
│   └── RUN-000022.md
├── shared/
│   ├── CONTEXT_MANAGEMENT.md
│   ├── CONVENTIONS.md
│   ├── HANDOFFS.md
│   ├── IDENTIFIERS.md
│   ├── ID_LEDGER.md
│   ├── INDEX.md
│   ├── INTEGRATION.md
│   ├── INTENT_RECONCILIATION.md
│   ├── RECONCILIATION.md
│   ├── RECORD_FORMATS.md
│   ├── SCORECARDS.md
│   ├── SESSION_LIFECYCLE.md
│   ├── WORK_GRAPH.md
│   └── templates/
│       ├── BOUNDARY_ASSESSMENT.md
│       ├── CHECKPOINT.md
│       ├── CLAIM.md
│       ├── HANDOFF.md
│       ├── INDEX.md
│       └── SCORECARD.md
├── tasks/
│   ├── INDEX.md
│   ├── TEMPLATE.md
│   ├── cross-boundary/
│   │   ├── TASK-000001.md
│   │   └── TASK-000006.md
│   ├── organization/
│   │   ├── TASK-000002.md
│   │   ├── TASK-000003.md
│   │   ├── TASK-000004.md
│   │   ├── TASK-000008.md
│   │   ├── TASK-000009.md
│   │   ├── TASK-000011.md
│   │   ├── TASK-000012.md
│   │   ├── TASK-000013.md
│   │   ├── TASK-000014.md
│   │   ├── TASK-000015.md
│   │   ├── TASK-000017.md
│   │   ├── TASK-000018.md
│   │   ├── TASK-000019.md
│   │   ├── TASK-000020.md
│   │   ├── TASK-000021.md
│   │   └── TASK-000022.md
│   └── project/
│       ├── TASK-000005.md
│       ├── TASK-000007.md
│       ├── TASK-000010.md
│       ├── TASK-000016.md
│       └── TASK-000023.md
├── triggers/
│   └── TRG-000001.md
└── workflows/
    ├── INDEX.md
    ├── WF-000001.md
    ├── WF-000002.md
    ├── WF-000003.md
    ├── WF-000004.md
    ├── WF-000005.md
    └── WF-000006.md
```

Ignored live fixtures under factory/artifacts/installation contain alpha/beta Git repositories, behavior copies and the retained rollback scratch copy. Raw evidence and hashes remain in factory/reports. old/ is outside the organization and stays read-only/uncommitted.
