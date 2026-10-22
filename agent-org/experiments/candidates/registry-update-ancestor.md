# Rejected registry update ancestor

- Candidate: registry-update-ancestor
- Parent: none
- Content Hash: 83321d38ac20087a3ce2d4a8660578b8ae7bd294465c3261e0af32dc0127e5fd
- Incident Family: registry-state-drift
- Partition: development
- Exposures: development
- Status: rejected

Observed artifact: tasks/INDEX.md at research candidate49161116fbe372514cf86f386020c4ef7b1294c3. Independent final review rejected its labels/status suffix mismatch; correction7090312 and PR10 retain the failure and repaired delivery. This hashes the actual historical index bytes, not an invented performance score. The output changed display titles while suffix statuses stayed stale. Structural validation passed, so a separate consumer was needed to expose semantic disagreement.

Evidence: [research Coordinator record](../../runs/RUN-000051.md) and [PR10](https://github.com/tclasen/agent-org/pull/10). Searchable failed ancestry grants no authority. No historical result is rewritten.
