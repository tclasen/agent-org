# Evaluation checks and retained operational observations

- Target System: organization
- Change Classification: organization
- Authorized Scope: task-owned evaluation evidence checks only
- Affected Paths or Resources: this report directory and allocated evidence records
- Owning Role: Coordinator
- Related Requirements: REQ-000084
- Related Tasks: TASK-000394
- Approval Requirements: APP-000598; independent APP-000599 and APP-000600; normal PR/main delivery

Frozen protocol: all nine protocol-hashes.json identities still match after both executions. Behavioral response arrays each contain twenty unique IDs, preserve assigned case order and parse as JSON. No outcome-driven retry or exclusion occurred. Both requested routine model invocations returned handoffs without reported configuration errors; actual runtime configuration and usage remain unknown.

Structural replay: replay-structure.py verifies 43 inert snapshots (41 census documents, one additional baseline-read policy, and the separately measured bridge), then runs measure-structure.py with a temporary source overlay. Observed exit0, byte-identical metrics; expected/observed SHA256 912fa8337e75bf8d1797adf14a8e5c5f91ea5cd1057bd06c344abb09da95af49. Reported-source word counts are post-hoc self-report-based measurements in reported-read-footprint.json.

Retained first replay failure: the helper initially canonicalized the child path but compared it with an unresolved temporary-root alias. A standard host temporary-directory symlink caused a containment ValueError before the measurement subprocess ran. Diagnosis is supported by the traceback and the differing normalized parent/child strings. Repair resolved the parent before comparison; the retry passed and reproduced the fixed metric bytes. No source or evaluator changed. This is a bounded artifact implementation repair, not proof that governance caused the error. Independent review covers the repair and the no-new-policy disposition; no new universal guardrail is proposed.

Network observation: initial sandboxed configured-remote lookup failed DNS. A normal authorized elevated read succeeded; fetching and a clean evidence-only delivery worktree succeeded. There was no automatic approval-review rejection or protection bypass. Existing dirty/untracked sources and other repositories remain outside the evidence-only candidate. Local runtime mappings and native identities stay in session context, not this report.

Formal record validation, scoped registry/reservation reconciliation, clean-worktree replay and whitespace observations are appended before final evidence review. Hosted required checks and observed PR/main verification remain separate from local checks. No production-tool changes or broad productivity claim is made; the evaluation helpers are retained reproducibility artifacts.

Initial formal validation was run during incomplete assembly and returned missing planned APP-000599/APP-000600 references plus four machine-unrecognized Authorized values. Pending approval records were expected unfinished work. The task writer used a prose authority statement where the existing parser expects a yes/no value; corrected to Authorized: yes with the actual source and scope retained in a separate Authorization Source field. This repairs the artifact's encoding, not the approval rule, and supplies no new authority. Final validation waits for actual independent decisions rather than fabricating approved placeholders.

Seed derivation disclosure after independent review: the original assembly used random.Random(20261028 + (1 if condition == "candidate" else 0)) for case ordering. Baseline therefore used 20261028 and candidate20261029. The root-plus-condition formula was not explicit in revision1; no strict seed-protocol compliance is claimed. Hashes/order were frozen before subjects ran; neither order, raw response, fixed rubric nor original preregistration has been edited. See PROTOCOL-DEVIATIONS.md.
