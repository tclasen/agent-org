# Task template

Coordinator allocates ID and records classification before substantive work.

- ID: TASK-<allocated>
- Target System: organization | project | cross_boundary
- Change Classification: same as Target System
- Authorized Scope: exact paths/resources and operation bounds
- Affected Paths or Resources: exact paths/resources
- Owning Role: responsible role
- Related Requirements: requirement IDs
- Related Tasks: parent/related IDs or none
- Approval Requirements: required grant IDs or pending
- Status: proposed
- Original Request: exact request or durable source
- Intended Outcome: observable result
- Parent: parent ID or none
- Dependencies: comma-separated blocking task IDs or none
- Dependency Type: blocked_by (list other typed edges separately)
- Responsible Agent: role and active run
- Plan Revision: 1
- Plan Approval: pending
- Authorized: no
- Claim: none

## Plan

Requirements -> plan -> review/approval -> implementation -> verification -> integration -> acceptance. Record workflow ID/revision, scope, risk, exact checks and rollback. For cross-boundary parents, use separate organization/project/integration children with own obligations.

## Execution history

Append time, run, actions, outcomes and changed artifact identities. Record requested/actual model reasoning per run.

## Artifacts and evidence

Actual files/hashes/checks/results, including failed attempts and unknowns.

## Blockers and next action

Dependency, owner and exact safe next action. Out-of-scope discovery is a proposal, not permission.

## Intent-to-outcome reconciliation

Accepted requirements, unresolved gaps, user outcome and acceptance authority.
