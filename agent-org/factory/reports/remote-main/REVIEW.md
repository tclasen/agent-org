# Independent remote-main policy review

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/factory/reports/remote-main/REVIEW.md
- Affected Paths or Resources: agent-org/factory/reports/remote-main/REVIEW.md
- Owning Role: Reviewer
- Related Requirements: REQ-000049
- Related Tasks: TASK-000052, TASK-000051
- Approval Requirements: APP-000013; independent candidate approval remains required

Reviewer execution: /root/remote_policy_review, RUN-000046, 2026-10-21. Fresh delegated execution with no implementation authorship. Requested model/reasoning inherited; actual metadata unknown. Review write scope is only this report. No commits, staging, remote writes or other record changes performed.

## Pinned inputs and rubric

Baseline: b2ba96964de7d60a74bb4319465b83f860bd0c44, tree 34620ff2a05cf53e03b8aeac14c6309971549b42. Candidate: c94d91b10640eba7f5359971c5a04e1fe1a25fec, tree 54b26f3da0c453bcf5108e68eddd25ec2c645043. HEAD matched candidate and tracked/untracked status was clean before this report. Origin observed as https://github.com/tclasen/agent-org.git. Diff contains 22 organization paths only; no project, root integration, runtime or old/ change. The original checkout and its backlog were not independently inventoried by this worker; BACKLOG.md is a pending-delivery record, not independently verified delivery evidence.

Rubric: the operator directive and REQ-000049, with evaluation/separation/scope/approval requirements from the baseline versions of AGENTS.md, AUTHORITY.md, SCOPE_BOUNDARIES.md, ACCEPTANCE.md, APPROVALS.md, CHANGE_CONTROL.md and GIT.md. No candidate rule was used to relax prior evaluation requirements. Documentation inspection verifies specified policy behavior only; no runtime interception or observed behavioral refusal is claimed.

REQ-000049 SHA-256: 81c309726fa05945da6737919b2e48456c686024243e37c2426df11128db1fab.

Baseline policy SHA-256 identities:

| Path under agent-org | SHA-256 |
| --- | --- |
| AGENTS.md | 57526e486fbeccd8d90647f8c33df681cd92805bb83af5a4cdd5174b6662f139 |
| policies/AUTHORITY.md | 082de2f8fec06bc6dc9027d2f8605ca61cda12a5f5c175d1c3019bd1035d1118 |
| policies/SCOPE_BOUNDARIES.md | fc60f7184e429f4f267a245a081755a4a889b109ef65bdaeff67c84fa47a7c8f |
| policies/ACCEPTANCE.md | 9be920d150d903cc2d4bd2cd9b082d406837707050f8534165018d7a6d11462f |
| policies/APPROVALS.md | 65e6f15ab93cdf1aba5eecc172a51aa8484e0be35a67e29936b5b3cacca976b2 |
| policies/CHANGE_CONTROL.md | c71a9730a4e16b29f5b50e8f2956449e68e162572b5655ba33ff4381758c513f |
| policies/GIT.md | 9b27009867e4bf8a654aea804b4225ceb62aef004c5bdaaa7992808d8ced41e2 |

## Criterion-level review

| Criterion/scenario | Observed policy and expected consequence | Outcome |
| --- | --- | --- |
| Local edits, passing tests, local commits | AGENTS and ACCEPTANCE explicitly make these intermediate states; no completion without verified owning-remote main | verified by inspection |
| Pushed feature branch or open PR | GIT and CHANGE_CONTROL explicitly retain pending delivery through merge and verification | verified by inspection |
| Normal PR merge | ACCEPTANCE requires remote identity, merged PR, tested candidate, merge SHA, observed main tip/time and containment/content evidence; GIT gives fetched-main ancestry check | verified by inspection |
| Squash/rebase merge | ACCEPTANCE and GIT require approved-content equivalence and mapping rather than original branch ancestry alone | verified by inspection |
| Multiple repositories and parent closure | PROJECT_CHANGES requires each project's own remote/main and authority; ACCEPTANCE requires child-repository and integration delivery before parent completion | verified by inspection |
| Missing authority, checks, network or main | Existing authority limits remain intact; candidate records precise blocker, owner and next action, retains nonterminal state and forbids bypass | verified by inspection |
| Startup and previously accepted local work | SESSION_LIFECYCLE inventories local/branch/PR backlog; prior local-only acceptance remains historical, pending current delivery | verified by inspection |
| Administrative closure delivery | ACCEPTANCE and CHANGE_CONTROL make proposed closure conditional until its own merge/verification, with observed session handoff and later durable reconciliation; avoids recursive pre-merge completion assertion | verified by inspection |
| Scope and independence | All candidate changes are within organization grant APP-000013; prior PR, fresh review, independent approval, exact-candidate and host-protection rules retained | verified by inspection; promotion still pending |
| Runtime enforcement | No runtime change; structural tools do not enforce all behavior and no live failure/refusal scenarios executed | excluded from documentation task |
| Actual delivery of this task/backlog | No PR merge or remote-main verification performed by Reviewer; candidate task/run records remain pending | unverified; not accepted as complete |

## Checks and limitations

On the pinned candidate in the isolated worktree, `python3 agent-org/factory/instrumentation/check.py --root agent-org` exited 0: valid true, 191 records, no errors. Its declared limits remain: structural checks do not prove behavioral acceptance; approval scope APIs require admission callers; no universal interception; callers supply provenance. Evaluator SHA-256: check.py da22192e7b87d2c054f070ab2b7841cb133a11cd7a19f39e87ea0e9f70f27fb2; records.py e4bc284cececd7dcb02733eac5edf6a23209ba0b898cd17397facdcc36a35f08. `git diff --check b2ba969 c94d91b` exited 0 with no output. Tooling itself is unchanged. No product tests warranted for this documentation-only candidate; host checks and actual final remote verification remain Coordinator obligations.

No substantive policy defects found. The additive gate satisfies the requested completion boundary while retaining prior scope, authority, review and rollback controls. Run worker identities/next actions and independent approval are still pending administrative reconciliation; they are not evidence of approval or delivery. APP-000013 is the operator grant, not a substitute for a bound candidate promotion decision.

Recommendation: approve the pinned policy content through a separate Chief of Staff execution, then follow the required PR/check/merge/remote-main workflow. This report does not approve a later head: adding this report, approval evidence or administrative reconciliation changes the candidate under the prior exact-head rule and requires proportional fresh review/approval of the final candidate. If policy content changes, rerun affected scenario inspection. Do not call the task complete before verified remote-main delivery.

Handoff: only this report changed; external effects none. No failed checks. Claim returns to Coordinator after report handoff. Next action: independent Chief of Staff decision and reconciliation of the exact final delivery candidate, followed by authorized PR delivery and verification.
