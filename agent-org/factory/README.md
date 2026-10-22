# Deterministic factory tooling

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/factory/
- Affected Paths or Resources: agent-org/factory/
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Factory contains small deterministic Python standard-library validation, scoped snapshot, explicit-command capture, event/provenance, metric and experiment utilities. They assist native workers; they never dispatch agents or provide a permanent scheduler/service/message broker. Governance/decisions remain Markdown; code/tests and versioned native telemetry are the narrow format exception.

From the Git repository root the installation verification entrypoints are:

```sh
python3 -m unittest discover -s agent-org/factory/tests -v
python3 agent-org/factory/instrumentation/check.py --root agent-org
git diff --check
```

These are commands to run against implemented tooling, not asserted passing results. Read component documentation/help and actual tests for current supported behavior. Recorded integration APIs are records.parse_record/validate_tree/validate_graph/validate_approval; scope.resolve_scoped_path/snapshot_tree/git_provenance/verify_snapshot; events.EventStore(path).append/read_events/snapshot; runner.run_command(argv,cwd,timeout,max_output_bytes). Do not infer undocumented CLI flags from API names. Run evidence records tested revision/interpreter/environment, expected/actual result, exits and content hashes; Python runner version differences stay explicit.

Explicit command capture uses argument arrays, bounded runtime/output and sanitization; preserve nonzero exit results. Event append is versioned and correction-based: identical duplicates are idempotent, conflicting duplicates invalid, incomplete writes/gaps disclosed. Short-lived append locks and hashes detect covered corruption; storage is not immutable or trusted isolation. Bind reports to source snapshot/evaluator/definition/classification versions and UTC half-open window/as-of parameters so prior results replay.

Live service registry starts without production services. DORA values require canonical explicit service/environment and commit/build/artifact/deployment/failure/remediation/recovery attribution; do not infer causality. Fixtures are labeled synthetic; their 100% traffic and 30-minute stabilization are not live defaults. Missing denominator, health, model, token or cost telemetry stays unknown/unavailable.

Separate organization behavior, project quality and measurement-health scorecards. Direct native tools, connectors and subagent internals can bypass explicit instrumentation; coverage reports must disclose them. Deterministic positive/negative tests cannot replace actual fresh-worker/recovery/independent-review trials or real PR/CI verification. Broader optimization requires prior-evaluator-governed evidence, fresh review, independent Chief of Staff approval and exact-candidate PR promotion, with rollback. See [policies](../policies/INDEX.md) and [shared conventions](../shared/INDEX.md).
