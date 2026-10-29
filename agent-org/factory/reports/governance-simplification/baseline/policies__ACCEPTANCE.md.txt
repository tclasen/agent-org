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

Review [outcome and authority fit before implementation correctness](../shared/INTENT_PROVENANCE.md#review-fit-before-correctness). Inspect user-source context separately from the implementer's framing, and record the two outcomes separately. A technical pass cannot establish user priority, expand authorization or accept an unresolved proposal; existing evaluator and promotion gates remain unchanged.

Approval binds exact candidate and evidence. A changed head/tree/artifact, requirement, evaluator or environment invalidates affected checks/approval; rerun proportionately. PRs and allowed host checks/thread resolution remain mandatory. Final installation acceptance is separately operator-owned after all required scenarios, exclusions and gap interview. FULLY_ACCEPTED requires no mandatory unresolved capability; LIMITED_INSTALLATION requires explicit operator acceptance of extra exclusions, otherwise INCOMPLETE_OR_BLOCKED.

## Remote-main completion gate

A change task is complete/accepted only after its reviewed and approved content has merged through a PR into main on its owning remote and the Coordinator has verified that remote main contains it. This applies to organization content and every managed project, including documentation, governance and administrative changes. Local work, passing tests, worker handoffs, approvals, local commits, pushed branches and open PRs are intermediate evidence only. A local main branch alone proves nothing about remote delivery.

Record repository/remote identity, PR URL and merged status, tested candidate, merge commit, observed remote-main tip, verification time and containment/content result. Squash/rebase merges require mapping the approved candidate to the merged content, rather than requiring the original branch commit to be an ancestor. Relevant checks must pass and merge content must match the approval. Parent completion requires separate delivery evidence for each changed child repository and integration.

Keep undelivered work in an existing nonterminal state (for example in_review, verified or blocked), with owner, blocker, PR/branch if available and exact next action. Do not invent new task-state names. If permission, network, protection, review or CI prevents delivery, report the task incomplete and preserve its work. Final reports must distinguish implementation/review from verified remote-main delivery. The gate applies to the acceptance record itself: a proposed closure committed in a PR takes effect only after its merge and verification; record the observed outcome in the session handoff, with later durable reconciliation as needed. No recursive pre-merge claim that a closure is already delivered.

Prior local-only acceptance remains historical evidence, not proof of delivery under this directive. Reconcile outstanding changes without altering historical evidence or silently expanding earlier grants.

## Final-response delivery audit

Before ending a change request, Coordinator checks every task-owned change and required child against the remote-main completion gate above. Apply this audit even when the request only says to create or edit a file, and even for documentation or administrative records. Task size and wording do not remove standing delivery authority.

1. Inventory owned changes, pending branches/PRs, required children and cleanup obligations. Preserve unrelated work.
2. For each undelivered change, continue the authorized commit, push, independent review/approval, PR checks, normal merge and remote-main verification during the active task. Local edits, a commit, a push or an open PR are intermediate states; do not end with those as the completed outcome or ask whether to perform already authorized delivery.
3. Before reporting completion, obtain the repository/PR/merge/main/content/check evidence required above, reconcile required children and release claims, and complete safe task-worktree cleanup. Keep any cleanup blocker explicit and separate from delivery status.
4. If an actual permission, network, review, protection or CI blocker prevents progress, attempt applicable authorized recovery and ordinary tool escalation within retry limits. Preserve ownership and a durable handoff with the exact failed action, observed error, pending branch/PR and next safe action. Report the task incomplete and the concrete blocker; an unattempted delivery step or an assumed need for renewed operator approval is not a blocker.

Explicit operator instructions to work locally only, pause or cancel override standing delivery for their stated scope. Status-only replies authorize no changes. This audit is an agent obligation using existing tools; it does not claim a harness-enforced final-response hook or guaranteed future compliance.
