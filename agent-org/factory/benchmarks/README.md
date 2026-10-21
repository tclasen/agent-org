# Synthetic benchmark inputs

repair.json and efficiency.json are illustrative native telemetry fixtures for TASK-000004. Their candidate, approvals, times and authority labels are synthetic; they do not authorize promotion. repair.json demonstrates baseline-fail/candidate-pass plus retained regressions. efficiency.json demonstrates 20 paired preregistered cases with seeded randomized order, 10% synthetic latency benefit and a fixed 95% paired bootstrap interval. All attempt costs are retained. Actual acceptance needs independently observed executions and exact pinned reviews.

The evaluator source hash is intentional: changes to its source invalidate these example bundles. Regenerate fixtures in a new reviewed implementation revision rather than changing historical evidence. Baseline artifacts and old fixtures must remain reconstructable through the repository history.
