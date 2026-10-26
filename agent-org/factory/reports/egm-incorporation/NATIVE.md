# Native trial observation record

- Target System: organization
- Change Classification: organization
- Authorized Scope: root-observed native trial invocation/completion evidence only
- Affected Paths or Resources: factory/reports/egm-incorporation/NATIVE.md
- Owning Role: Coordinator
- Related Requirements: REQ-000059
- Related Tasks: TASK-000243, TASK-000246, TASK-000247
- Approval Requirements: APP-000448; unchanged prior-rule evaluation and final approval

Coordinator directly invoked collaboration.spawn_agent twice, with fork_turns:none, requested model gpt-6.1-sol and reasoning high. Native tool returned identities /root/egm_baseline_trial and /root/egm_candidate_trial. Both used explicit version-specific task/run/source manifests and fixed CASES. No parent history was supplied by this invocation. Inputs and model selection are observed request parameters, not trusted actual configuration.

Baseline: returned native final completion states all16cases once in order, no tool failures/retries, parent-only marker UNKNOWN. Output BASELINE_REPLAY.md SHA256 b89f1ca98c3a8777987776da986532ad248bfa4f19304432d93f94cdafaa0041. Caller observed native completion and verifies output bytes separately; evaluator scores outcomes independently.

Candidate: native final completion observed; all16ordered raw decisions authored once, no omissions, semantic reruns, diagnosed tool faults or prohibited effects reported. Output CANDIDATE_REPLAY.md SHA256 bfcdb54b32886083d8f928d6bcffee1cd0968869f03ebd88183158c70e9e1f09. All11manifest inputs reported hash-verified; parent-only marker UNKNOWN. Candidate read the higher-priority startup AGENTS before the manifest, then verified versioned inputs before cases; raw replay preserves that read-order detail and a recovered clipped display. It did not claim synthetic child IDs were actual native executions. Actual returned artifact bytes verified by Coordinator; outcome scoring remains independent.

Read coverage: source-reading and hash claims inside workers are worker-reported; their artifacts/identities/hashes are independently inspectable. Complete child tool traces were not imported into this root evidence record, so full trace coverage is unknown. Native child creation/identity and returned completion/progress are observed root tool events. Actual model/reasoning/usage/cost remain unknown. The marker result is one bounded observation; no shared-filesystem, memory-service or universal fresh-context guarantee follows. No hidden marker value was put in child prompts or shared inputs.
