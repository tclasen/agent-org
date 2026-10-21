# Improvement evidence gate 1.0.1

Task TASK-000004; REQ-000031, REQ-000032, REQ-000035, REQ-000036; approved Domain S/V. `improvement.py` validates evidence and returns pass, reject, or inconclusive. It does not implement an agent runtime, permission sandbox, approval issuer, PR creation, merge, or rollback executor. Shared writable files and source references do not authenticate evidence; independent review and a trusted durable context are still required.

```sh
python3 agent-org/factory/quality-gates/improvement.py agent-org/factory/benchmarks/repair.json
python3 agent-org/factory/quality-gates/improvement.py agent-org/factory/benchmarks/efficiency.json
python3 -m unittest discover -s agent-org/factory/tests -p 'test_improvement.py' -v
```

CLI input is one JSON object with `plan`, `evidence`, `approvals` and `context`. Canonical output includes exact plan/evidence/candidate/evaluator digests. Exit codes are 0 pass, 1 reject, 2 inconclusive or invalid bundle. Checked-in bundles are synthetic examples, including synthetic approval records; they confer no authority.

`register(specification, artifacts)` creates a plan pinning SHA-256 of baseline, candidate, workload, evaluator and criteria artifacts plus the hypothesis digest and the executing evaluator's source bytes. Persist the plan and anchor its digest independently before any outcome. `evaluate(plan,evidence,approvals,context)` compares those pins and evaluates benefit. JSON serialization rejects NaN/Infinity. Context is supplied from trusted approved records; the program never creates trust by repeating candidate assertions.

## Input contract

The plan declares semantic version, registered_at, hypothesis, organization scope, claim (`repair`, `outcome`, `efficiency`), task_class, expected_benefit, target_metric, direction (`lower`/`higher`), implementer identity, exact candidate_head, required guardrails, budget, rollback, stopping_rule, changes_evaluator and all content pins produced by register. Stochastic stopping rules require at least 20 unique case_ids, fixed_sample_size matching that list, a fixed integer seed, and 1000–10000 fixed bootstrap samples. Workload artifact `cases` must equal the preregistered case list. Baseline and workload must represent the declared task class; that representativeness is independently reviewed.

Evidence includes started_at and completed_at (registration strictly before start), plan_hash, full pinned artifacts, authority_hash, explicit boolean hard guardrail outcomes, and measured usage. The evidence object itself is hashed for independent approval. Failed/blocked cases and retries remain in the evidence. Repair evidence requires baseline_pass false, candidate_pass true, regression_pass true, and independent_regression_hash matching a previously specified regression from context.

Stochastic evidence supplies one `pairs` row per case: case_id, seeded randomized order of baseline/candidate, numeric baseline and candidate primary outcomes, and baseline_attempts/candidate_attempts. Each attempt has value and status (passed/failed/blocked); efficiency totals must include every attempt's resource value. A changed case list, duplicate case, excess cases, changed ordering or omitted measured retry costs rejects. Missing telemetry, fewer than the fixed workload, fewer than 20 cases or unknown target values is inconclusive. The tool can detect discrepancies in supplied records; it cannot discover omitted uninstrumented attempts.

The 95% interval is a fixed-seed percentile bootstrap of paired mean differences, taking nearest-rank 2.5% and 97.5% bounds. The lower bound must be strictly positive. Relative efficiency additionally requires at least 5% mean benefit divided by baseline mean, with positive baseline denominator. Confidence and minimum benefit cannot be weakened by candidate-supplied criteria. This establishes evidence under the declared workload; it is not universal correctness or guaranteed deployment productivity.

Hard guardrails are scope_authority, evidence_integrity, required_tests, independent_review, critical_correctness, security, acceptance_traceability and project_correctness. Any observed false guardrail rejects regardless of speed. Missing guardrail results remain inconclusive. Candidate policy cannot remove these gates. Authority pins must match existing authority; organization evidence grants no project mutation.

Context supplies registered_plan_hash, approved_baseline_hash, approved_evaluator_hash, approved_evaluator_code_hash, current_candidate_hash/current_head, authority_hash, prior_consumed_seconds, prior_consumed_storage_bytes, limits, active_experiments, authorized_approvers (role → assigned agent IDs), and independent_regression_hash for repairs. These are independent trust anchors, not values to regenerate from a changed candidate. The baseline, criteria, denominator, workload, evaluator and preregistration cannot be rewritten to justify the same run.

Approvals require one fresh reviewer and one distinct Chief of Staff, both distinct from implementer and present in context's authorized_approvers for their assigned role. Each approval records approved true, agent_id, approved_at after evidence completion, exact candidate_hash/candidate_head, plan_hash, evidence_hash and prior evaluator_hash. Missing approvals are inconclusive; mismatched pins, self-review, unassigned identities, stale head/tree or rejected approval reject. `pass` establishes only eligibility for the required governed PR process. Coordinator still checks scope/intent, host checks/merge and post-merge identity.

Budget and context limits include active_seconds, storage_bytes, depth and attempts. Usage is measured; unknown usage is inconclusive. Budget cannot exceed context limits or the initial 3600-second allocation. Prior consumed time/storage from ancestors count against the same cumulative budget. One candidate experiment is permitted at a time. At 80% of active time the report requires a durable checkpoint; reaching/exceeding any limit is inconclusive and requires stopping/replanning. Recursion cannot reset the trusted cumulative counters.

Rollback requires exact known_good_hash equal to baseline, explicit trigger conditions, stop_new_work, reconcile_active_runs and revert_pr_required true. The governing workflow must stop failed-candidate use, reconcile runs, open a corrective/revert PR and verify known-good behavior before resuming. No filesystem rollback is performed by the gate.

Evaluator/promotion changes require changes_evaluator true, prior_evaluator_hash, a context-pinned adversarial_fixtures_hash, and successful dual_version_replay. Execute the retained prior evaluator and match its source hash to the approved context; candidate code cannot approve its adoption. Keep the proposed evaluator a separate artifact until accepted. Missing recursive evidence is inconclusive; self-validation or altered prior fixtures reject.

`immutable_versions(existing_version_to_digest, proposed_version_to_content)` rejects semantic-version reuse with changed contents. Preserve that registry and previous artifacts externally. New evaluator semantics require a new version and their own prior-rule evaluation; versions and histories are not rewritten. S-01–S-10 named synthetic tests cover the decision logic. An actual harmless correction, fresh agents, PR promotion, host checks and actual rollback acceptance are separate integration evidence.

## Version 1.0.1 correction (APP-000004)

Retained 1.0.0 source, fixtures and the original experiment remain under baselines and reports. The prior normative contract remains the approval authority. This candidate does not adopt itself; synthetic source substitutions exercise behavior only.

Required text fields and content pins must be actual nonempty strings, compared exactly without normalization. Required booleans, including changes_evaluator and recursive dual_version_replay, must be JSON booleans; successful replay is exactly true. Objects, arrays and numeric counters are validated before use. Missing data remains inconclusive; malformed contract types reject. Repair false baseline_pass remains a required valid boolean.

Both outcome and efficiency claims require finite numeric attempt values and explicit passed/failed/blocked statuses. Unknown or malformed attempt observations cannot establish benefit. The total supplied baseline and candidate attempt record count must equal usage.attempts; observable attempts also consume the trusted limit. Failed or retried efficiency costs remain included. Usage may not conceal supplied records; uninstrumented omissions remain outside the tool's visibility. Checkpoint reporting uses prior_consumed_seconds plus current active_seconds against 80% of the same cumulative allocation.
