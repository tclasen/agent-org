# Bounded operational observations

- Target System: organization
- Change Classification: organization
- Authorized Scope: task-owned operational evidence only; no new instruction or evaluator rule
- Affected Paths or Resources: this evidence, local native-dispatch requests and publication handoff
- Owning Role: Coordinator
- Related Requirements: REQ-000085
- Related Tasks: TASK-000400
- Approval Requirements: APP-000601; independent APP-000602 and APP-000603

The native task API documents a1000UTF8-byte prompt limit. Three initial lane-dispatch requests exceeded it and returned “prompt exceeded the maximum context budget”, with no new task identity. This was a tool-argument rejection, not an observed model context-window exhaustion. The cause was Coordinator's overlong dispatch text; the existing declared API limit was not checked before sending. Subsequent requests were measured before invocation and shortened to868,901and897bytes, each accepted with observed native identity. No outcome-driven retry or new provider/runtime was used. Existing prompt limit and per-task source manifests suffice; no new universal prompt rule is proposed. The repaired dispatches preserve role, scope, source and independence obligations. Detailed native identities remain session-only.

Fresh readiness Reviewer initially attempted a required scope source at an abbreviated root-relative filename, received a missing-file error, then followed the existing core's canonical policies path and read it successfully. Cause is a contained source-location/read mistake, not evidence of a defective missing-file control. No source/evidence/authority effects were observed. Current prior policy still routes this actual bounded diagnosis for CoS assessment; the unpromoted local-closure candidate was not applied operationally. No new catalog or general instruction is justified by this error alone.

A second public push attempt was rejected before execution. The user had assented to publication and ordered fixes, but automatic review requires public destination/payload explicitly in the user's own message; it did not accept the assistant's stated destination as sufficient. Publication remains blocked pending that exact authorization. No alternate export route or bypass was used. This external approval result is not solved by adding agent-org guardrails. Local authorized fixes continue. Original evaluation results, all failed attempts and fixed protocol remain retained.

The explicitly bound public-payload/destination question received the operator's structured answer “I authorize all of that.” The host accepted the subsequent same-destination push; evaluation PR49 was created and hosted verification passed. A normal merge request was separately rejected as requiring explicit immediate-main merge authority. No alternate tool route was attempted; final merge permission will be requested only once the requested fix PR is concrete. This is an external host authorization condition, not a reason to add organization guardrails.

The GitHub review-thread connector's advertised argument name was rejected by its actual schema, which required repo_full_name. The read-only request was retried once with the field named by the observed validation error, returning an empty thread list. This was a bounded connector-contract mismatch with no remote mutation, not a model context failure or organization-policy defect. Existing exact-error reconciliation suffices; no unsupported external connector maintenance was undertaken.
