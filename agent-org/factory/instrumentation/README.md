# Explicit deterministic instrumentation

Python 3.11+ standard library, POSIX `fcntl`/process groups. No service, hook installation, scheduler or tool interception.

From the Git repository root:

```sh
python3 -m unittest discover -s agent-org/factory/tests -v
python3 agent-org/factory/instrumentation/check.py --root agent-org
```

`records.parse_record(path)` reads exact metadata definitions outside fenced code. `validate_tree(root)` checks formal ID-named files in record directories, eight mandatory scope fields, task fields, known references and graph rules. It excludes intake, indexes, templates and fixtures. `validate_graph(records)`, `validate_transition(previous,current)`, `validate_claims(claims)`, `validate_evidence(evidence,expected)` and `validate_recovery(checkpoint,attempts=...)` provide explicit admission/recovery checks. `validate_approval(grant,target=...,paths=[...],operation=...,candidate_hash=...,now=...)` requires explicit target/operation/candidate authority; ordinary Markdown references do not prove exact authority. Operators must supply the approved interpretation of legacy prose grants. Cross-boundary grants enumerate `Approved Targets`, comma separated; paths are semicolon separated. Evidence requires pinned candidate/instruction/policy/input/output SHA-256 identities and source/verifier. Explicit claim helpers compare normalized scopes across tasks, including unresolved ownership; graph checks detect duplicate task claims and blocking/hierarchy cycles. These helpers return errors; callers must refuse mutation on errors.

`scope.resolve_scoped_path(root,relative,allowed=(...))` rejects traversal and resolved symlink escape. `snapshot_tree(root,exclude=...)` binds named small safe evidence roots, files/modes, explicit exclusions and symlink targets. Caller excludes secrets before hashing. `compare_snapshots(before,after,allowed=...)` identifies all changed and unauthorized paths; `git_provenance(root)` records real HEAD/branch, dirty-state and sanitized remote identity hashes. Parent Git status does not cover nested/ignored file contents; snapshot them explicitly. No hostile filesystem race protection is claimed.

`runner.run_command(argv,cwd=...,timeout=...,max_output_bytes=...)` executes a string array with no shell. Returns exit code, elapsed wall time, output hashes/counts and timeout/limit flags, never raw arguments, output or environment. A missing executable gives 127. A killed command preserves its signal return code. Output-limit hashes cover the observed prefix only; limits may overshoot by one 64 KiB read. Arguments/output are not durable raw files. Callers authorize effects and handle nonzero status.

`events.EventStore` is specified in ../events/README.md. `coverage_report(events,expected_classes=None)` counts observed classes; expected class coverage and actual models/tokens/cost remain null if unknown. Direct tools, connectors and subagent internals are unobserved.

Structural validation is assistance, not acceptance of quality, authority, independence, behavior or truth of evidence. A successful check cannot establish complete interception or a trusted provenance anchor. CI must also run the tests and independent review.
