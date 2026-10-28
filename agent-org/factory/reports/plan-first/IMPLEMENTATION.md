# Planning-first instruction correction: system diagnosis and evidence

- Target System: organization
- Change Classification: organization
- Authorized Scope: bounded instruction correction and sanitized evidence under TASK-000386 revision 1
- Affected Paths or Resources: seven admitted instruction files and allocated records; no product code or execution-gate tooling
- Owning Role: Coordinator
- Related Requirements: REQ-000059
- Related Tasks: TASK-000385, TASK-000386
- Approval Requirements: APP-000590 admission; independent APP-000591 review and APP-000592 final approval; ordinary PR/main delivery

## System failure, not a missing feature description

The failure class is the promotion of desired-state intent into immediate execution authority. The prior source at `0aa2591ed8206ba8018f17aee71e6b2c9eb7815d` already separated requests, agent choices and authorization, required source-fit review, and said a plan is not permission. It did not explicitly make ordinary feature requests planning-only. A broad sentence that approval of a set of changes authorizes that set also left plan acceptance versus build approval ambiguous.

This permits a reinforcing sequence: an agent interprets a request as permission to build, writes an Authorized/task framing using that interpretation, delegates against it, and a technically independent reviewer checks the same unchallenged premise. Requirements mapping establishes what was requested; successful tests and PRs establish behavior and delivery. Neither establishes the separate authorization to build now. A preference for tangible demonstrations can further bias that interpretation despite the existing words “within already authorized scope.” More documents and more reviewers do not repair that shared premise by themselves.

The diagnosis is supported by the instruction comparison and the operator's direct correction; affected project records retain the concrete source/history. It does not claim all agents or all historical changes followed this sequence. Local source records can outlive context, but agent-maintained excerpts are not independently authenticated proof. A fresh context must be able to identify that limitation rather than treating a quote, accepted label or commit as consent.

## Where the correction acts

| Decision point | New required behavior | What it cannot prove |
| --- | --- | --- |
| Entry and admission | Feature request defaults to requirements/traceability/current-plan updates, including small reversible changes | A prose instruction cannot intercept every tool call |
| Before build delegation or mutation | Distinct build source bound to a plan revision/slice; absent/unresolved state blocks dependent build | Self-authored Authorized fields cannot create a grant |
| Independent review | Independently establish requested behavior and source-backed build instruction as separate findings | Multiple reviewers sharing an unsupported premise are not independent evidence |
| Fresh-context handoff | Carry source availability, requirement/criteria/plan chain and distinct authorization state | Missing original transcripts cannot be recreated or authenticated from summaries |
| Reconciliation | Record retrospective matrix corrections as retrospective; preserve actual delivery and missing build grant | Backfilling rows cannot retroactively pass pre-build admission |
| Already authorized work | Continue routine implementation/test/review/delivery within unchanged explicit scope | Prior build authority does not include newly requested features |

The direct instruction to update operating instructions authorizes this correction now. Planning/instruction documentation delivery is not itself a product build and does not trigger recursive approval. An instruction explicitly asking to plan and implement can authorize both, in sequence. A hypothetical feature-removal audit is not removal authorization.

## Fixed verification and limits

The unchanged TASK-000386 C1–C6 and fourteen fixed scenarios were declared before edits. Seven instruction files are affected: core entry, planning, intent provenance, Coordinator, Planner, Reviewer and handoff template. Existing evaluators, permissions, PR rules and role identities remain unchanged. No new role, service, runtime gate or product functionality is built.

Initial structural check failed on missing Plan Approval/Authorized task metadata and reserved decision references that had no records. A later lifecycle-state check also rejected explanatory prose inside the exact Authorized boolean; that scope explanation was moved to a separate field while retaining the direct instruction source. Those preparation defects were corrected by linking the admitted decision and creating explicitly proposed (not approved) reserved decisions. The subsequent structural check reports 774 records and zero errors. `python3 -m unittest discover -s agent-org/factory/tests` passes all 144 tests. These checks validate structure and existing deterministic behavior, not user-consent semantics or future model reliability. Independent scenario reasoning and source comparison establish only bounded instruction clarity. Reviewer and Chief of Staff decisions bind exact candidate/evidence separately.

An enforced execution gate that refuses product mutations without an authenticated source-bound grant remains a possible future design, not implemented or authorized by this correction. Such a mechanism would need its own plan, authority model, bypass analysis and explicit build instruction. No guarantee that this can never recur is claimed.
