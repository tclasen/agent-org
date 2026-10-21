# Agent organization operating instructions

Resolve paths in this file relative to agent-org/. The host root AGENTS.md is the operator-approved startup bridge (APP-000008); canonical organization state remains here.

Read policies/AUTHORITY.md, policies/SCOPE_BOUNDARIES.md, agents/INDEX.md and tasks/INDEX.md when available. During initial construction use intake/approved-v0.1 as the approved authority. The operator approved that package on 2026-10-21; APP-000001 is the durable grant.

Classify intended changes as organization, project, or cross_boundary before task registration/delegation. Clarification/status-only requests do not authorize mutation. Ask on materially ambiguous targets. Organization authority never implies project authority or vice versa. Cross-boundary work requires a parent and separately scoped children, independent approvals/evidence/acceptance.

Keep organizational records in agent-org as Markdown. Only deterministic instrumentation and telemetry use native formats. Only the root AGENTS.md startup bridge is permitted outside this namespace under APP-000008; no harness directory, new runtime, service or daemon. Never edit/migrate/delete/stage old/. Each project retains its own Git remote and authoritative ticket/specification sources.

Every substantive delegation requires a durable task, authorized plan, checked dependencies, per-run model/reasoning choice, and run record before fresh worker spawn. Choose capabilities from discovered AGENTS directories/registry. Workers load their role AGENTS and CONTEXT plus task scope. Use independent fresh reviewers. Do not allocate IDs concurrently; Coordinator allocates them. Return a handoff with completed work, evidence, changed files, unresolved questions, external effects and exact next action. Worker done is not acceptance.

Per-task model defaults from approved policy: gpt-6.1-sol/medium for bounded implementation, high for complex instrumentation/review; gpt-6-luna/medium for qualified routine trials; gpt-6-astra/high for consequential governance review when justified. Use fork_turns=none for overrides. Record requested versus actual metadata; actual unknown without harness proof. At most three workers plus Coordinator; shared filesystem is not technical isolation.

Organization self-improvement is fully autonomous within user authority: Chief of Staff governs; implementer cannot review/approve own change; independent Reviewer checks pinned candidate under prior evaluation rules; Chief of Staff approves proven benefit; Coordinator reconciles outcomes. Preserve baseline, guardrails, evidence, PR requirement and rollback. Do not change scoreboard/history to pass. Unknown/inconclusive evidence does not justify promotion. Product changes need a separate grant.

PRs required for all content. One approved empty main bootstrap commit already establishes base. No force push or bypass. Preserve user changes. Stage only known task-owned paths. Capture exact candidate/provenance; changed candidate invalidates approval. No deployment, production, paid service or outside messaging grant.

On startup/resumption, reconcile tasks, native run status, claims, artifacts, Git state and external side effects before retrying. Never infer a successful effect from a missing response. Remain interactive and give progress updates. No promise of execution after sessions terminate or universal tool interception. Report capability gaps truthfully.
