# Handoff schema

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/templates/HANDOFF.md
- Affected Paths or Resources: agent-org/shared/templates/HANDOFF.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Copy into an authorized record/checkpoint and replace angle-bracket placeholders. This schema allocates no ID, claim, result or approval. Include the eight metadata fields with actual scope when used.

- Task: <allocated task reference>
- Run: <allocated run reference>
- Native Worker: <observed ID or unknown>
- Checkpoint Time: <UTC>
- User Instruction and Context: <exact statement/source, or explicitly labeled summary and missing context>
- Agent Interpretation and Approach: <selected means and rationale; attribute proposals>
- Requirement and Plan Chain: <source → requirement/matrix → criteria → task and current plan revision>
- Source Availability: <original message/link available, agent-maintained excerpt, paraphrase or missing; do not invent provenance>
- Execution Authorization: <absent|unresolved|granted; distinct explicit build instruction/source, bound plan revision/slice, concrete scope and exclusions; request/plan acceptance alone is not a grant>
- Decision State and Basis: <accepted, proposed, superseded and unresolved choices with source/revision>
- Intended Outcome: <accepted objective>
- Completed Actions: <actual actions>
- Changed Files: <exact paths or none>
- Deliverables: <artifact paths/hashes>
- Actual Validation: <commands/exits, expected/actual, evidence hashes>
- Criterion Outcomes: <verified|failed|unverified|blocked|excluded with limits>
- Unresolved Questions: <remaining items or none>
- External Effects: <intent/key/observed IDs/results or unknown/none>
- Resource Use: <cumulative known totals/retries and unknowns>
- Claim Disposition: <retain/release/transfer state>
- Next Action: <one exact safe action and required authority>

- Delivery State: <pending or verified on owning remote main; local/branch/PR only is pending>
- Delivery Evidence: <repository/remote, main, PR URL/merged status, tested candidate, merge SHA, observed main tip/time, ancestry/content result, checks>
- Pending Delivery Owner and Next Action: <owner, blocker and exact action, or none after verification>
