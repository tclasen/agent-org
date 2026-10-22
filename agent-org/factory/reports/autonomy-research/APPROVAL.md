# Independent research delivery approval

- ID: APP-000015
- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/knowledge/autonomy-research/*.md; agent-org/knowledge/INDEX.md; task-owned research governance and delivery records for REQ-000051, TASK-000057 through TASK-000062 and RUN-000051 through RUN-000056
- Affected Paths or Resources: pinned research documents, their knowledge index and task-owned records; ordinary owning-repository PR delivery only after final-head confirmation
- Owning Role: Chief of Staff
- Related Requirements: REQ-000051
- Related Tasks: TASK-000062; TASK-000057
- Approval Requirements: APP-000001; explicit operator research instruction; existing prior approval and acceptance policies

Decision: **Approve the pinned research content for research delivery only, conditional on final committed-head confirmation and the existing PR/check/merge/remote-main gates.** This approves no operating change, evaluator revision, runtime, service, provider, project work or productivity claim. Research completion remains pending delivery.

Approver: AGENT-000002, fresh native execution `/root/autonomy_approval`, TASK-000062 / RUN-000056. Decision time: 2026-10-22T01:17:40.533702+00:00. Plan revision: 1. APP-000015 was allocated serially by Coordinator; this execution made the independent decision after reading the completed Reviewer report. Requested model/reasoning: gpt-6-astra/high, justified in the run for consequential independent governance review; actual model/reasoning/token/cost metadata remain unknown. This execution authored neither research nor review and did not delegate.

## Decision basis

The four documents satisfy the research rubric: substantially more than twelve relevant systems, primary-source links and revision/observation limits, current local comparisons, priorities with proposed paths and ownership, dependencies, evaluation and rollback. The reports distinguish inspected implementation, specifications, vendor claims, research results and local hypotheses. Contrary evidence and failure modes are retained. A read-only reconciliation report is a plausible first candidate; that judgment is a research recommendation, not evidence that implementation would improve outcomes.

Independent Reviewer RUN-000055 reports PASS with no material findings, sampled source checks, all 85 existing tests passed, structural validation of 211 records, 30 resolving local link occurrences and whitespace checks. I read the entire review and all four research documents; checked the existing policies, gate definition and relevant gate implementation; observed no policy/workflow/gate diff; and confirmed current report hashes against the snapshot. Heading-only cleanup occurred before this decision and the current pins below supersede initial worker handoff artifact pins for delivery.

I independently spot-checked [DGM paper v3](https://arxiv.org/html/2505.22954v3), including its staged 200-task SWE-bench evaluation and historical search-cost estimates, and [Temporal Activity documentation](https://docs.temporal.io/activity-definition), including the unrecorded-completion retry interval and provider-enforced idempotency. These support the report's bounded treatment of benchmark benefit and effect recovery. Other source checks rely on the explicitly bounded independent Reviewer assessment and named research evidence; this is not an exhaustive upstream audit or reproduced benchmark.

The research task's shared 90 active minutes is an admitted research budget. It does not change the existing improvement gate's 3,600-second initial allocation, one-active-experiment rule, cumulative ancestor accounting, at-least-20 paired cases, randomized order, positive 95% benefit interval, 5% practical efficiency threshold or hard guardrails. The reports state that distinction. Proposed scenario/evaluator work would require separate admission and prior-rule evaluation; no candidate judge validates its own adoption. Existing model-selection rules and actual-metadata uncertainty are preserved.

## Candidate and evidence identity

Base/current HEAD at this artifact decision: `8916d3589054a6416098598a029d64c1d676dd7f`, on `research/autonomous-factories`. Research is currently an uncommitted candidate with procedural path ownership. This base HEAD is not the future research commit. Final integration head/tree must be confirmed separately before delivery; no approval of unseen future administrative bytes is implied.

| Research artifact | SHA-256 |
| --- | --- |
| `agent-org/knowledge/autonomy-research/FACTORIES.md` | `06c516c34c0d07082f76c9dcabbbe9034bbc57ced10ba95938d61c1ddc684ce0` |
| `agent-org/knowledge/autonomy-research/ORGANIZATIONS.md` | `b7e4ad251db14a9582c9aa962046205caf4fcac2fb91df40af4324a80f42c23c` |
| `agent-org/knowledge/autonomy-research/README.md` | `1ac77e2aeaf7a6c8fa4a11f58235e82878644123cc9e3b3d3a188915d42487a6` |
| `agent-org/knowledge/autonomy-research/SELF_IMPROVEMENT.md` | `20781525ed8186dd365a8809485f1bcec00855c900b1c291dd29ec8a0cf4a6a7` |
| `agent-org/knowledge/INDEX.md` | `c629a01c2a71166be0af01615c13979dae4f2eba8c3177c10170f8aac9487eb9` |

| Evidence / plan artifact | SHA-256 |
| --- | --- |
| `agent-org/factory/reports/autonomy-research/REVIEW.md` | `cfc0e846fe8964237b56e236c987378bd96860768e5ae1a580b31ef1a8c54ddd` |
| `agent-org/factory/reports/autonomy-research/research-snapshot.json` | `d59dc60436d092fe38a098d741b12c88eef2d603c91e0136c22d3f707269ed9f` |
| `agent-org/factory/reports/autonomy-research/DELIVERY.md` | `c91a3f9932054f7ed1cc231a2d16a7fe3028fc1e803e67ce6479aacd620ffe7f` |
| `agent-org/requirements/organization/REQ-000051.md` | `6a44d768ad70be9b7a002190c5bd25cb03d7b48d2423eb1aa478ae6aa0458cd9` |
| `agent-org/tasks/organization/TASK-000062.md` | `1ef4f19b0441847c36f5b8c45e4594c795d942feb76824c7c510bece0b85dc65` |

The prior evaluator remains improvement gate 1.0.1. These governing inputs were read and pinned; no proposed research semantics replace them.

| Prior rule / evaluator | SHA-256 |
| --- | --- |
| `agent-org/policies/AUTHORITY.md` | `082de2f8fec06bc6dc9027d2f8605ca61cda12a5f5c175d1c3019bd1035d1118` |
| `agent-org/policies/SCOPE_BOUNDARIES.md` | `fc60f7184e429f4f267a245a081755a4a889b109ef65bdaeff67c84fa47a7c8f` |
| `agent-org/policies/APPROVALS.md` | `65e6f15ab93cdf1aba5eecc172a51aa8484e0be35a67e29936b5b3cacca976b2` |
| `agent-org/policies/ACCEPTANCE.md` | `758fdb2825ab129e1c8d8753decb43e694322b645db82013a9c6dcd534dbf5b4` |
| `agent-org/policies/CHANGE_CONTROL.md` | `95b9916fbbd0ce42e8d32c70b98c20b9bc15103761e62af18df8c69459254207` |
| `agent-org/policies/SELF_IMPROVEMENT.md` | `cc0bb4daca4a99e6925846e10b43d19405d191d321304f736024d0ee16c38e5e` |
| `agent-org/policies/MEASUREMENT_INDEPENDENCE.md` | `899d12e5d92d5a22ef16aa929f154efe1c7748997b071b043769d06a03970194` |
| `agent-org/policies/MODEL_SELECTION.md` | `d500ac114d42bdae6dc72e434b393815dd6f7c0e6d9a39f3cb0ae6e9a9d416b5` |
| `agent-org/policies/RESOURCE_BUDGETS.md` | `47416e3ad0ee31ba15e3c1c8cd92373caa6b500d296ef3956f1d82a6ee474f8c` |
| `agent-org/factory/quality-gates/DEFINITION.md` | `2303a0dc02641378c2c85b6612c8edb4bece18f561e9791c0db35c2c1e3f3f88` |
| `agent-org/factory/quality-gates/improvement.py` | `b85841b308ebe73cb0dcd9b33e9672ccc87eee1767c4e64eae5a2f7b62aa9c60` |

## Conditions, limits and continuation

Approval expires for affected checks if research, evidence, requirement, plan, evaluator or final candidate identity changes. Routine integration record completion still needs final-head review and approval. The final committed candidate must remain within the task-owned research/admin inventory and contain unchanged approved research. Preserve distinct final Reviewer and Chief of Staff decisions externally on the PR without changing the confirmed head; changed head requires renewed confirmation.

Coordinator owns scoped staging/commit, ordinary PR publication, current host checks and protection compliance, merge and verification on `https://github.com/tclasen/agent-org.git` main. Record PR URL/status, tested head/tree, merge commit, observed main tip/time and containment or equivalent-content result. No completion claim follows merely from this decision, a test pass, push or open PR. Historical pre-merge checkpoints must be reconciled with observed delivery evidence rather than replayed blindly.

No operational effectiveness, production reliability, continuous execution, hidden holdout enforcement, universal tool coverage or stochastic productivity is accepted. Shared filesystem ownership remains procedural. Primary sources and benchmark claims were inspected, not reproduced. Missing actual usage metadata stays unknown. Existing root cleanup, old/, nested projects and other worktrees remain outside this delivery.

Rollback is a scoped corrective/revert PR to the known baseline research state, preserving source history and failed evidence; stop relying on a defective recommendation while correcting it. No operational rollout occurred. Next safe action: Coordinator freezes task-owned integration records, commits the candidate, obtains final-head Reviewer confirmation followed by this approver's confirmation, and completes the existing delivery gates.
