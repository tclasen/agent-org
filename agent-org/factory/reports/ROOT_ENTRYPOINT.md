# Root entrypoint verification

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: APP-000008 root startup amendment and acceptance evidence
- Affected Paths or Resources: root AGENTS.md; scoped agent-org startup/boundary and acceptance records
- Owning Role: Coordinator
- Related Requirements: REQ-000002, REQ-000040, REQ-000043
- Related Tasks: TASK-000025, TASK-000026, TASK-000027, TASK-000028
- Approval Requirements: APP-000008; independent review and Chief of Staff

Baseline9f9abd7 has no root AGENTS.md and requires explicit nested startup. Candidate creates a thin root bridge and keeps canonical organization state under agent-org. Operator clarified: this implementation has a root entrypoint and must not require cd into agent-org before starting Codex. Fresh RUN-000026 actually received root AGENTS.md automatically and followed its bootstrap references while preserving the Reviewer role. All referenced files/links were readable and eight roles were discovered. No cd or extra activation prompt was needed. A new top-level Codex process was not launched; this evidence is the actual native worker path.

No source or measurement changes are intended. Frozen approved-v0.1, prior approvals, raw evidence and old are protected. First independent review checked65 pinned files,151 valid records, links and whitespace, but required correction of stale current startup/acceptance documentation. RUN-000026 retains those findings. Root repaired only the identified current views; re-review and PR integration remain required.

## Final source qualification

RUN-000028 independently accepted all76 source paths with separate organization, host and observed-bootstrap passes;152 records valid,205 links valid, whitespace clean. All six current-documentation findings corrected; original rejection retained in RUN-000026. Final canonical review mappinge8e4b09d0cc699e8516a5ad605bf9d65eb37b1e1dd325949afb9fce93009e551. Distinct Chief RUN-000027 / APP-000009 approves exact adoption mappinga99fe2eecc7a61b1836b3dbe0732d43fe33f7b845b70d161c24fa098a3c59640 with factual outcome envelope. Root source SHA2565112b8c7dff94123c127b4c0b1da1481782c125edefb0fb85fd1c4b2db451e88. Chief also automatically received root instructions and preserved role.

PR delivery and CI/merge verification are pending. No additional operator acceptance is required: APP-000008 accepts the original installation and authorizes this requested amendment; existing independent and normal PR gates remain mandatory.
