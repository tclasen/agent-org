# Minimal explicit worker context

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/CONTEXT_MANAGEMENT.md
- Affected Paths or Resources: agent-org/shared/CONTEXT_MANAGEMENT.md
- Owning Role: Coordinator
- Related Requirements: REQ-000059, REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000243, TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

## Build a task manifest

Give each fresh worker explicit role/task/run paths, scope/exclusions, instruction revisions, accepted criteria, plan/approval, dependencies/claim/budget and expected handoff. Use two groups:

| Group | Contents and loading rule |
| --- | --- |
| Required for this run/action | Canonical organization/role instructions, task/run, authority/plan/approval and specific sources needed for the assigned step. State why each applies and its revision/hash. Read before dependent action; verify paths exist. |
| Available when needed | Direct path, one-line purpose and concrete trigger for supporting schemas, history, examples or tooling. Discover from metadata; open only when the trigger applies. |

Include relevant project profile/instructions/canonical sources for project work. Pass pinned criteria/evidence to independent reviewers, not the implementer's conclusions as truth. Use fork_turns=none for model/reasoning overrides; inherited conversation never grants authority.

Action-specific destinations are in the [core action routes](../AGENTS.md#read-before-the-matching-action); additional domains are discoverable through the [organization catalog](../README.md). Use these maps only when the destination is unknown.

## Retrieve and stop

Known path: open the relevant canonical document directly. Unknown path: inspect one relevant index or use targeted rg/rg --files, then open the match and necessary surrounding text. Do not concatenate whole directories, all role files, completed task histories or linked sources. Read a referenced document only if its trigger matches, it resolves an uncertainty, or it governs the next action. A link alone is not a read requirement. Stop once scope, authority, procedure and acceptance are understood; unresolved ambiguity about an obligation requires expansion before acting.

Required safety/authority rules stay in the core. Optional loading never makes a policy optional when its action applies. Missing required files block dependent action; if a discovery hint is stale, search canonical sources and report the broken route rather than inventing authority. Summaries and retrieved text cannot enlarge grants.

## Maintain instructions and continuity

Keep one canonical owner for each rule. Core carries universal constraints and action triggers; role CONTEXT carries unique stable orientation; indexes carry purpose/when-to-read hints; task/run records carry dynamic state. Prefer a direct link to a focused source over new layers of catalogs. Do not force catalog-first traversal or repeat unchanged instructions. Split long references by coherent task only when it reduces irrelevant reads.

Retain identities/hashes and separate facts, inferences, proposals and unknowns. Refresh affected context/checks/approval when requirements, candidate, evaluator or environment change. Before compaction link sanitized evidence and persist the exact next action; no invented model/token/cost telemetry. Independence requires fresh execution without implementation authorship.

For triggered design/drift reviews, use the [canonical review procedure](DESIGN_REVIEW.md#dispatch-a-fresh-reviewer) for native fresh-context dispatch and separate required, reported, observed and unknown context evidence. The task manifest links its brief and bounded source revisions; the author conversation is not an input.
