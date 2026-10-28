# Intent provenance and tangible checkpoints

- Target System: organization
- Change Classification: organization
- Authorized Scope: task admission, current-plan reconciliation, review and handoff within existing grants
- Affected Paths or Resources: existing task/plan/source records and bounded demonstrations; no new publication or execution authority
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000059
- Related Tasks: TASK-000381
- Approval Requirements: APP-000001; APP-000587 admission; independent exact-candidate review and final approval before promotion

Apply this protocol when interpreting a request, selecting a milestone, revising direction, reviewing outcome fit or summarizing a handoff. It operationalizes [planning](../policies/PLANNING.md), [authority](../policies/AUTHORITY.md) and [acceptance](../policies/ACCEPTANCE.md); it changes none of their grants, independence or delivery gates. Keep one owning task and current plan. Add the following distinctions to existing records rather than creating a second planning system.

## Preserve request, choice and authorization

Record these separately before substantive work, at a level proportional to the task:

| Record | Required content |
| --- | --- |
| User instruction and context | Exact relevant statement, speaker/source and enough surrounding context to preserve its referent. Link the original source where available. If only a summary survives, label it a summary with missing context; never reconstruct a quotation. |
| Agent interpretation and approach | Intended user outcome, proposed sequence or implementation choice, rationale, assumptions and material alternatives. Attribute agent choices to the agent. |
| Execution authorization | The actual instruction or standing grant authorizing this concrete scope, its conditions/exclusions and any unresolved consequential choice. Distinguish permission to try a slice from acceptance of the slice or its wider design. |

A feature request expresses the desired outcome and defaults to planning-only under [the build boundary](../policies/PLANNING.md#feature-requests-change-the-plan-first). Keep requirement acceptance separate from implementation authorization. Before build delegation, identify the actual build instruction and the plan revision/slice it names; absent evidence remains absent. A task author cannot create permission by writing an Authorized field. A reviewer must derive the authority from source independently, not inherit that field as fact. Fresh-context handoffs carry source availability and the distinct build-authorization state; copied quotations without an accessible original are agent-maintained source evidence, not authenticated proof.

A brief assent such as a synthetic "build that" can authorize the clearly identified preceding slice. It does not prove the user read every detail, selected every alternative, authored the proposed ordering, or accepted future work. Preserve that bounded meaning in the task and later explanations. Explicit approval to build a clearly identified set of changes authorizes that implementation scope without another routine confirmation; accepting the plan or desired outcome alone does not. Routine engineering choices within valid scope remain autonomous.

If the referent or a consequential choice is materially ambiguous, resolve only the ambiguity that blocks dependent action. Continue independent authorized work. Do not bury a publication, destructive action, spending, priority change or other new external effect inside a long plan and treat a general assent as its authorization. Use existing permission boundaries; no new universal approval queue is introduced.

## Preserve decision state and evidence

Use these meanings in existing prose or supported record fields. They describe intent and decisions, not technical task completion:

| State | Meaning and evidence |
| --- | --- |
| Requested | A source expresses a desired outcome or constraint. It does not select all proposed means. |
| Proposed | An agent or another contributor suggests an approach, sequence or option. Name its proposer and rationale. |
| Accepted | The applicable decision authority explicitly selected the stated proposition, with source, time/revision and exact scope; or an existing governing decision demonstrably covers it. Execution authorization alone is not proof of broader design acceptance. |
| Superseded | A recorded later decision replaces this specific proposition; link the replacement and retain who originally proposed it. |
| Unresolved | Evidence, context, authority or a consequential choice is missing or disputed. State what is unknown and the next resolving step. |

A request or proposal can be accepted only on its recorded basis. A commit, merge, successful test, technical review, repeated reference, dependency graph, document status, source-author label, generated summary or elapsed time cannot supply that basis. Viewing a demo, silence, a preselected default and an unsubmitted choice are not acceptance. A new correction does not retroactively make the old approach user-authored. When summarizing or compacting, retain the source/choice/authorization distinction and unresolved limits; a summary cannot increase authority or certainty.

## Reconcile one current plan

When direction changes, update the current plan's outcome, selected approach and affected dependencies together. Identify superseded choices and their replacement; preserve historical evidence through ordinary versioning and links. Do not leave competing "next" steps active in different sections. Keep unresolved product choices visible rather than converting them into technical prerequisites. A dependency may justify an agent recommendation; it cannot establish a user priority.

Before beginning a milestone, give a compact outcome checkpoint, normally one to three sentences: what the user will be able to do, why this is the next useful slice, and any consequential choice still requiring a decision. Identify the intended demo or other observable evidence. This is orientation, not a demand to approve routine work again. Important choices must be understandable from that checkpoint without reading the whole design archive. Full reasoning remains accessible in the existing plan.

## Demonstrate before asking for broad direction

When the user prefers something tangible, or uncertainty is best resolved by use, choose the smallest useful reversible demonstration within already authorized scope. A working prototype or demo that implements feature behavior requires the explicit build authority above; tangible-review preference alone authorizes neither. Prefer a local working slice using real behavior and representative data. Identify a mockup, replay or prototype honestly; do not present it as completed integration. If a needed decision is not authorized, prepare the concrete reviewable work that is safe and independent of that decision, then ask only about the dependent effect.

Show the demo first at review, with a short readable video when that helps the user evaluate behavior. Explain relevant outcomes at the actual scene rather than substituting a presentation of requirements for demonstrated functionality. Keep unmet requirements and limitations explicit. Retain a concise text description, captions or equivalent accessible explanation and a link to detailed evidence; video preference does not eliminate accessibility or durable reasoning. Do not impose this style on users or tasks that need another form of review.

Generated videos and demo artifacts stay local by default. A stable review link specifies continuity of access, not a hosting destination or upload permission. An external upload needs an applicable explicit grant; general code/document PR delivery does not create it. Keep local artifacts out of commits and remote attachments unless specifically authorized. Normal reviewed delivery of authorized source and documentation remains required.

After review, record what the user actually accepted, rejected or left open. Approval to continue the demonstrated slice does not accept unread options, unshown behavior, all future milestones or a speculative architecture. A prototype's success does not waive independent review, existing release criteria or outstanding requirements.

## Review fit before correctness

The existing independent Reviewer checks two separate questions, in order:

1. **Outcome and authority fit:** inspect the user-source context and distinguish it from the agent's interpretation. Can the reviewer state the intended user experience, why the selected slice advances it, which choices remain proposals, and what authorizes its effects? Challenge the task framing when it loses that distinction. Missing material source evidence is an unresolved finding, not permission to inherit the implementer's conclusion.
2. **Implementation correctness:** verify the pinned candidate against that valid scope using the existing technical, evidence and boundary checks.

A technically correct result with failed outcome/authority fit is not accepted. Review independence must include the source of the problem framing, not merely a different execution checking the same assumed objective. Record the two outcomes separately in the existing review; no new permanent role or replacement evaluator is required.

## Authorization review checkpoint

Before implementation, outcome review asks two separate questions: “Is this behavior requested?” and “What explicitly authorizes building this plan/slice now?” Require a source for each. If only the first is established, return a plan; do not delegate the build. Recheck the same distinction before acceptance. Test/PR success and a complete requirements matrix cannot repair missing build permission. Technical review must record an authority failure even when the resulting behavior is useful and correct. This is a procedural checkpoint, not a claim that tools mechanically prevent code changes.

## Respond to corrections

Before proposing or delegating the next fix after a material correction, identify the failed assumption, affected decisions/requirements, and any pending external effects. Reconcile the current plan and authority, then continue the safe authorized work. Repeated corrections trigger the existing [bounded capability assessment](../policies/ROUTING.md#capability-mismatch-and-repeated-corrections). Prefer repairing interpretation, routing or an existing instruction when sufficient; do not create a role or another policy document for each mistake. Pause only dependent work whose intent or authority is unresolved.

Handoffs preserve original request/context, agent-selected approach, authorized scope, accepted/superseded/unresolved choices and observed results. The Coordinator reconciles those against the original user outcome before reporting completion. These are operating obligations and reviewable evidence, not a guarantee of universal model compliance.
