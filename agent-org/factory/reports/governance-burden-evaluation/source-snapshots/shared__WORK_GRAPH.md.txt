# Task graph, readiness and claims

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/WORK_GRAPH.md
- Affected Paths or Resources: agent-org/shared/WORK_GRAPH.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Lifecycle states: proposed → requirements_ready → planned → awaiting_approval → ready → in_progress → in_review → verified → integrated → awaiting_acceptance → accepted. Blocked interrupts active work and records reason plus prior stage/return condition; rejected/canceled retain terminal evidence; archived retains links/history. Rework returns to the required earlier stage with reason and renewed affected approvals; never skip proof by editing status. Requirements_ready requires identified sources/criteria; planned requires revisioned plan; ready requires valid authority and admission checks. Worker done moves to in_review, not accepted.

Use '- Dependencies: none' or comma-separated existing task IDs and '- Dependency Type: blocked_by' (or another declared relation). Relations are blocked_by, parent_of, requires, validates, discovered_from, supersedes, related_to, awaits_approval, awaits_condition. Blocking/required graph is acyclic; missing links, self-links and cycles reject admission. Parent hierarchy is not a dependency cycle: children point to Parent, while parent acceptance waits for required children. Nonblocking related/discovery links never imply execution readiness.

`validates` identifies the existing subject of review and does not require that subject to be accepted before review can start. The independent reviewer must verify the pinned candidate and its evidence; the structural graph check establishes existence, not candidate provenance. `blocked_by`, `requires`, `awaits_approval` and `awaits_condition` remain acceptance prerequisites. Every dependency relation rejects self-links, including nonblocking relations; parent self-links and hierarchy/blocking cycles also reject admission.

Formal ID prefixes must match their record-family directory (for example, TASK in tasks/ and REQ in requirements/). TASK and REQ records require the canonical organization/, project/ or cross-boundary/ subdirectory directly within that family; both Target System and Change Classification must match it. Flat, missing/unknown, deeper or mismatched target directories reject these records. Other families retain their flat record layout. Directory checks do not infer or expand authority.

Coordinator derives readiness from scope/plan/authority, satisfied prerequisites and conditions, capability/budget, single claim and source freshness. Parent cannot be accepted before required children and independent integration pass. Register one accountable owner and active mutation claim per overlapping scope; claims include task/run/native owner, scope, observation/checkpoint time and release condition. Serialize admission/allocation and Git index operations. Multiple-session uncertainty blocks overlapping mutation; Markdown is not a distributed lock.

At most two retries per diagnosed operation, preserving all attempts and cumulative budget. Cancellation stops delegation, interrupts owned workers, journals effects and reconciles actual results before terminal status. Priority is P2 normally, P1 important, P3 improvement, P0 only authorized urgent safety/production work; record actual deadlines only. Archive inactive terminal work after 90 days without deleting identity/history.
