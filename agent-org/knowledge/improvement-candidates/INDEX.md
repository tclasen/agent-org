# Correction and improvement queue

Use this queue during existing active-session improvement reviews. Entries retain source incidents, candidate lineage and test exposure. Validate with `python3 agent-org/factory/instrumentation/learning.py validate --root agent-org` before selection. Only one admitted experiment runs at a time; this queue grants no authority or promotion.

- [Registry reconciliation](registry-reconciliation.md) — implemented deterministic candidate under EXP-000002; qualification and delivery tracked by TASK-000072. Protects canonical status and ID interpretation after the observed registry-label and stale-checkpoint incidents.

Current execution procedure: [autonomous execution](../../shared/AUTONOMOUS_EXECUTION.md). New corrections are records with evidence and counterexamples, not immediate global instructions. Prior promotion and rollback rules remain authoritative.

Every observed unexpected problem also triggers immediate root-cause diagnosis and repair under SELF_IMPROVEMENT.md#root-cause-diagnosis-and-repair; periodic selection is not a waiting period. Use the existing candidate/task for cause, escaped control, tested generic repair and recurrence follow-up. First occurrences count; uncertainty and authority blockers remain explicit. See the existing improvement-candidate template for required diagnosis fields.

- [Responsibility boundaries and root-cause repair](responsibility-root-cause-context.md) — current bounded instruction candidate under TASK-000390; retains [its unpromoted ancestor](responsibility-root-cause.md) and finite qualification, not a universal prevention claim.
