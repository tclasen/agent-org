# Stable identity and serialized allocation

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/IDENTIFIERS.md
- Affected Paths or Resources: agent-org/shared/IDENTIFIERS.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Coordinator alone allocates monotonic typed identities after scanning all current/archived records; never allocate concurrently, reuse an identity or derive a new authority from a filename. Use TYPE plus six digits (for example TASK-000002). Existing approved baseline identities are preserved; source/question/test labels such as SRC-005 or X-01 are local contract references, not newly allocated records.

Namespaces include AGENT, REQ, AC, TASK, INIT, INTENT, WF, DEC, RUN, APP, ART, CAP, TRG, EVAL and EXP. Source event identifiers follow their versioned instrumentation schema; never invent metadata unavailable from the harness. No operational record is created merely to fill a directory. Templates show TYPE-NNNNNN, avoiding a live ID.

Role instructions retain '- Agent ID: AGENT-NNNNNN' with their allocated identity; they are capability definitions rather than formal ID-named operational records. Actual workflows use '- ID: WF-NNNNNN'. Coordinator maintains the durable allocation ledger and reconciles it to records before reserving IDs; this policy does not freeze next counters.

Store the canonical identity once in its formal record. Cross-reference via fields/indexes without duplicating a record's ID declaration. Keep identity, revisions, previous/native/external IDs and supersession links distinct. Reconcile files and registries before admission; duplicate/missing/dangling IDs block dependent actions. Terminal/archive history remains linked indefinitely.
