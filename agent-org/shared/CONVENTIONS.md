# Record and communication conventions

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/CONVENTIONS.md
- Affected Paths or Resources: agent-org/shared/CONVENTIONS.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Keep durable organizational knowledge as Markdown under agent-org, linked by stable identities and repository-relative paths. Native deterministic code/tests/telemetry remain in factory. Use UTF-8, descriptive titles, UTC ISO-8601 observation/effect times and explicit unknown/none values. Preserve original sources, revision reasons and append history. Never claim source facts from inference.

Formal records include eight metadata fields defined in RECORD_FORMATS.md. Use one '- Field: value' line per machine-readable field; IDs are '- ID: TYPE-000001'. Templates contain placeholders, not live claims or fabricated allocations. Do not store machine fields in tables. Tables may present human-readable indexes/evidence.

Report target system, intended outcome, stage, evidence, blockers, exact next action, scope changes and acceptance state. Use concise outcome-first updates at milestones and at least every 60 seconds during active work where feasible. Separate proposed, implemented and verified status. Notify in-conversation on boundary/evidence/budget failures; no unsolicited outside messages. Read instructions explicitly on startup; Markdown records do not execute or schedule work.
