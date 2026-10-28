# Independent planning-first review

- Target System: organization
- Change Classification: organization
- Authorized Scope: independent examination of TASK-000386 fixed criteria; no instruction implementation or product mutation
- Affected Paths or Resources: assigned review reports and APP-000591 only
- Owning Role: Reviewer
- Related Requirements: REQ-000059
- Related Tasks: TASK-000386, TASK-000388
- Approval Requirements: APP-000590; prior SELF_IMPROVEMENT.md and ACCEPTANCE.md; independent final APP-000592 and ordinary PR/main verification

- Reviewed At: 2026-10-28T03:48:07.022747+00:00
- Reviewer Execution: RUN-000380; independent of instruction authorship
- Baseline: 0aa2591ed8206ba8018f17aee71e6b2c9eb7815d
- Candidate: current scoped instruction hashes below; exact assembled commit confirmation pending
- Model Selection: inherited; actual model/reasoning/cost telemetry unknown

## Outcome and source fit

The inherited original operator messages request changing the operating instructions so feature additions/changes update the plan rather than immediately build. The next message prioritizes preventing recurrence and asks what failed systemically. These directly authorize this bounded instruction correction and a read-only audit; they do not authorize feature deletion, product implementation, a new enforcement service or retroactive permission. I inspected those statements independently of the implementer’s task summary.

## Failure mechanism and corrective coverage

The observed failure chain lets one interpretation cross several distinct gates: a desired outcome becomes a task’s asserted authorization; a requirements row proves desired behavior and is mistaken for a timing/build grant; reviewers inherit that premise while verifying correctness; tests and PR delivery provide strong technical evidence that cannot establish user consent. A preference for tangible demonstrations does not answer the missing authorization question. The baseline already demanded source-fit review, so this is also failure to operationalize an existing obligation, not merely absence of all policy.

The candidate makes the default and checkpoints explicit in the entrypoint, planning policy, Coordinator, Planner, Reviewer and handoff. It requires the separate source-backed build instruction before implementation delegation and again at review. Requirement acceptance and build authorization remain separate. It expressly forbids using self-authored task labels, matrix entries, successful tests, merges, silence or demo preference to supply the missing grant. This closes the documented ambiguity at instruction level; it is not mechanically enforced. The structural checker itself reports that approval exact-scope APIs must be called by the admission workflow and that there is no universal interception. Passing that checker cannot prove semantic consent or future adherence.

An enforceable tool/runner gate would be separate system work requiring its own plan and explicit implementation grant. No such gate is implemented or approved here. Source-link absence remains an evidentiary limit: a future context can follow durable excerpts and references, but agent-maintained excerpts without an independently accessible original are recorded claims, not authenticated proof.

## Fixed acceptance

| Criterion | Finding | Outcome |
| --- | --- | --- |
| C1 | Feature additions/changes/removals and implied desired-outcome requests default to planning; small/reversible work and prototypes are included. | verified instruction clarity |
| C2 | Explicit build instruction binds a recorded revision/slice; combined plan-and-build is sequentially allowed; plan approval alone is insufficient; routine scoped work remains autonomous. | verified instruction clarity |
| C3 | Source → requirement/matrix → criteria → plan/task → distinct build instruction chain is required; missing source and retrospective corrections remain explicit. | verified instruction clarity |
| C4 | Short checkpoints persist, but urgency/demo preferences/silence cannot bypass authorization; only unresolved execution questions require clarification. | verified instruction clarity |
| C5 | Direct documentation/instruction edits proceed now without recursion; existing independent evaluation, delivery and rollback gates are unchanged. | verified instruction clarity |
| C6 | Hypothetical removal is audit-only; historical overclaims must be reconciled in the owning records, not retroactively authorized. Separate owning-record review confirms explicit retrospective mappings and no product mutation. | verified instruction and bounded documentation reconciliation |

All S1–S14 are recorded in CASES.md. They are independent reasoning evidence with limited predictive value, not stochastic benefit measurements.

## Review finding and repair

Initial inspection found the legacy sentence “Explicit approval of a clearly identified set of changes authorizes that set” could still be read as plan approval granting build. The Coordinator repaired it to explicitly refer to approval **to build** and clarified the tangible-demo paragraph’s build boundary. The repaired text agrees with C2/S5. No remaining scoped instruction blocker was found.

## Source bindings

| Instruction | SHA-256 |
| --- | --- |
| AGENTS.md | `81cf0abc8ba96814bc8ce03118e5b32b6b7d121ac4cc6a010c384b471add2003` |
| policies/PLANNING.md | `e060f9e91a66ba5078b98eaf42b14ef2b1c2997a00d36fe7dfa4f53cabc8b51a` |
| shared/INTENT_PROVENANCE.md | `ec0a646cae64423e74bf6b5c6251d0dd0e72536cc99a85abb363f1972794316f` |
| agents/coordinator/AGENTS.md | `639aae80a785c158b70119171524863d304c2c643219b2e7089dbda7563e097b` |
| agents/planner/AGENTS.md | `716096f2cc787cf5dcc83b26c7e527b8f9dff214bd343f0f0ee820bb66001256` |
| agents/reviewer/AGENTS.md | `6e8b8de85da80856c30ffc65e33ad10ef0af5e03ce1e005ee703d5b7eb9a2924` |
| shared/templates/HANDOFF.md | `d56ff1c7405ccdcfc3ceb9e973cd584fa4716dcf8a60f7083aaf00c0333363e6` |

Prior evaluator files remain unchanged from the baseline: SELF_IMPROVEMENT.md and ACCEPTANCE.md. Structural check independently reports 774 records and zero errors. Independent regression execution passes all 144 tests in 8.111 seconds. Final approval requires the assembled candidate, independent Chief of Staff decision and ordinary PR/main verification.
