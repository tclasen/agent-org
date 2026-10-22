# Registry and identity reconciliation candidate

- Candidate: registry-reconciliation
- Parent: registry-update-ancestor
- Content Hash: 125fff48792ff19f921e825aca7d2383d324a153c87d52f11895806684c5c54f
- Incident Family: registry-state-drift
- Partition: development
- Exposures: development
- Status: active

Owner: Coordinator. Authorized experiment: [EXP-000002](../../experiments/EXP-000002.md), task72 under independent APP20. The candidate is the actual reconcile.py source artifact, with rejected output ancestry retained in the candidate archive.

Source incidents: research registry labels/status suffixes diverged in4916111, and merged task/run definitions exceeded the old ID-ledger summary. Current pre-merge checkpoints can also lag verified PR/main delivery. Hypothesis: a read-only view over canonical records, explicit known-worktree reservations and attributed destination observations detects these disagreements without rewriting history, allocating identities, releasing claims or accepting delivery.

Counterexample: a stale checkpoint can correspond to a valid completed merge. Missing remote observations must remain unknown; a local Git object alone cannot authenticate the remote. Valid alternative paths and unresolved native ownership are retained.

Qualification: independently preregistered C1 cases, executable tests/test_reconcile.py, actual CLI scenario consumer and fresh worker recovery. Current cases are visible development evidence, not a technically secret holdout. No productivity or cross-task generalization is asserted. All failed/retried and missing observations stay in task evidence.

Rollback: stop using the new consumer and return to the prior accepted manual reconciliation procedure through a corrective PR; preserve unknown effects and source records. Next action: independent candidate review and APP21, then normal PR/main delivery. Promotion still belongs to prior gates, never this archive row.
