# Evidence, verification and acceptance

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/policies/ACCEPTANCE.md
- Affected Paths or Resources: agent-org/policies/ACCEPTANCE.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Every criterion records expected and observed behavior, tested revision/environment, evidence path/hash, verifier, outcome and limitations. Report verified, failed, unverified, excluded or blocked; insufficient improvement proof is inconclusive. A documented mechanism or complete template is not an operational pass. Expected-negative tests pass only when the refusal/detection actually occurs.

Workers return handoffs; fresh independent Reviewer checks the pinned candidate, scope and accepted criteria. Chief of Staff approves qualified organization outcomes autonomously; project authority decides product acceptance; Coordinator reconciles original intent, task graph and integration. Do not close a parent before required children. A superficially complete deliverable that misses intent reopens for scoped repair.

Approval binds exact candidate and evidence. A changed head/tree/artifact, requirement, evaluator or environment invalidates affected checks/approval; rerun proportionately. PRs and allowed host checks/thread resolution remain mandatory. Final installation acceptance is separately operator-owned after all required scenarios, exclusions and gap interview. FULLY_ACCEPTED requires no mandatory unresolved capability; LIMITED_INSTALLATION requires explicit operator acceptance of extra exclusions, otherwise INCOMPLETE_OR_BLOCKED.

## Remote-main completion gate

A change task is complete/accepted only after its reviewed and approved content has merged through a PR into main on its owning remote and the Coordinator has verified that remote main contains it. This applies to organization content and every managed project, including documentation, governance and administrative changes. Local work, passing tests, worker handoffs, approvals, local commits, pushed branches and open PRs are intermediate evidence only. A local main branch alone proves nothing about remote delivery.

Record repository/remote identity, PR URL and merged status, tested candidate, merge commit, observed remote-main tip, verification time and containment/content result. Squash/rebase merges require mapping the approved candidate to the merged content, rather than requiring the original branch commit to be an ancestor. Relevant checks must pass and merge content must match the approval. Parent completion requires separate delivery evidence for each changed child repository and integration.

Keep undelivered work in an existing nonterminal state (for example in_review, verified or blocked), with owner, blocker, PR/branch if available and exact next action. Do not invent new task-state names. If permission, network, protection, review or CI prevents delivery, report the task incomplete and preserve its work. Final reports must distinguish implementation/review from verified remote-main delivery. The gate applies to the acceptance record itself: a proposed closure committed in a PR takes effect only after its merge and verification; record the observed outcome in the session handoff, with later durable reconciliation as needed. No recursive pre-merge claim that a closure is already delivered.

Prior local-only acceptance remains historical evidence, not proof of delivery under this directive. Reconcile outstanding changes without altering historical evidence or silently expanding earlier grants.
