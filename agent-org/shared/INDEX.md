# Shared operating conventions

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/INDEX.md
- Affected Paths or Resources: agent-org/shared/INDEX.md
- Owning Role: Coordinator
- Related Requirements: REQ-000059, REQ-000001, REQ-000008, REQ-000011, REQ-000012, REQ-000013, REQ-000015, REQ-000016, REQ-000034
- Related Tasks: TASK-000243, TASK-000002
- Approval Requirements: APP-000001; future revisions follow policies/APPROVALS.md

Open the matching reference when its trigger applies. Schemas preserve state; they do not execute work. Go directly to known files; this catalog does not require loading every entry.

| Need | Source |
| --- | --- |
| Startup/resumption/shutdown | [Session lifecycle](SESSION_LIFECYCLE.md) |
| Write formal records | [Required fields](RECORD_FORMATS.md), [communication conventions](CONVENTIONS.md) |
| Allocate IDs | [Identifiers](IDENTIFIERS.md), [current allocation ledger](ID_LEDGER.md) |
| Admit/claim/depend on a task | [Work graph](WORK_GRAPH.md) |
| Delegate or trim context | [Context manifests and retrieval](CONTEXT_MANAGEMENT.md) |
| Return/checkpoint worker results | [Handoff contract](HANDOFFS.md), [copyable schemas](templates/INDEX.md) |
| Retry interrupted/uncertain effects | [Reconciliation](RECONCILIATION.md) |
| Integrate independent systems/adapters | [Integration](INTEGRATION.md) |
| Compare delivery with original intent | [Intent reconciliation](INTENT_RECONCILIATION.md) |
| Interpret organization/product/measurement scores | [Separate scorecards](SCORECARDS.md) |
| Consult historical evaluation/recovery precedents | [Legacy lessons](LEGACY_LEARNINGS.md) |
| Review a consequential design or scoped document/source discrepancy | [Design and bounded drift review](DESIGN_REVIEW.md) |
