# Autonomous execution and learning

This is the active procedure for authorized organization work. It connects existing governance to deterministic tools; it grants no additional permission and does not replace independent review or the prior improvement gate. Use routine standing organization and delivery authority without asking the operator again.

## Reconcile before admission and continuation

From the repository root run:

```sh
python3 agent-org/factory/instrumentation/reconcile.py --root agent-org
```

Supply known organization worktrees with repeated `--worktree` options. Supply explicit destination observations with `--observations` only after inspecting the real repository/API. The report identifies registry disagreements, ID reservations, ownership uncertainty and attributed delivery observations. It never releases a claim or accepts a task. Verify the actual owning remote/main and approved content using GIT.md; a supplied observation is not authenticated evidence by itself. Preserve historical checkpoints and record current observations separately. Do not replay an effect merely because a local record says running or pending.

Fix an owned registry discrepancy by deriving the full display title and status suffix from its canonical record. Preserve unrelated reservations and user changes. Unknown worktree ownership blocks overlapping mutation; the tool is not a distributed lock.

## Prepare a scoped worker manifest

After task, run, plan and authority exist:

```sh
python3 agent-org/factory/instrumentation/context.py --root agent-org --task TASK-000072 --run RUN-000068 --role coordinator --format markdown
```

Use the actual admitted task/run/role. The manifest pins required instructions, authority, plan, requirements and task-specific sources. Pass its exact output and paths to a fresh worker. Missing, mismatched or escaped sources stop preparation. A manifest establishes availability and identities; it does not prove that a worker read or applied the instructions. Keep scope and source freshness checks before execution. It creates no task identity or permission.

## Record effects before dispatch and reconcile uncertain outcomes

Use `effects.py --help` and its subcommand help. The native journal is explicit telemetry under a task-owned `factory/reports/` or `factory/events/` path. Prepare an intent binding effect identity, operation, resource, target, candidate content hash, authority, task and run. The same intent is idempotent; changed payload under its identity is a conflict.

Record the attempt immediately before the already authorized external operation. Dispatch using the existing native tool, then independently inspect the destination and record the matching receipt. If the operation or acknowledgement is interrupted, inspect the destination before another attempt. A missing lookup or ambiguous response stays unknown. Confirmed effects are not reissued; changed targets or candidates require a new admitted intent. An incomplete/corrupt journal blocks further journal writes; preserve it and reconcile, never silently truncate it.

Receipt source, time and remote identity are caller-attributed observations. Journal state does not authenticate them, grant tool authority or make a provider idempotent. The journal dispatches nothing. Direct native tools remain possible, so Coordinator must apply this procedure explicitly; no universal interception is claimed.

## Convert corrections into tested candidates

Apply the canonical [first-occurrence diagnosis and resolution rules](../policies/SELF_IMPROVEMENT.md#root-cause-diagnosis-and-repair) to every actual unexpected problem/correction during the active task. Retain evidence and bounded diagnosis even for eligible local resolution. Coordinator ensures ownership and routes exclusions to Chief of Staff; recurrence reopens the prior incident/countermeasure. The periodic review supplements this duty. Local resolution does not create an improvement candidate or qualify an organization repair.

At the existing startup/five-accepted-task improvement review, inspect [the correction queue](../knowledge/improvement-candidates/INDEX.md). Each candidate links an observed failure, affected task/run, causal hypothesis, permitted mutation, owner, counterexample, representative test, exposure history and rollback. Keep rejected and inconclusive ancestors. An observation from a single task remains a scoped hypothesis until transfer is tested.

```sh
python3 agent-org/factory/instrumentation/learning.py validate --root agent-org
```

Candidate Markdown lives in `knowledge/improvement-candidates/` and `experiments/candidates/`. Use `learning.py scaffold --help` for deterministic record scaffolding on stdout; Coordinator still allocates formal task/run/experiment identities. Validate lineage before selection. Duplicate content, cycles, missing parents and incident-family partition overlap are errors. Final-test feedback exposed to a proposer makes that case development evidence for descendants; do not reuse it as independent final evidence.

Select one admitted bounded experiment under [WF-000004](../workflows/WF-000004.md). Apply the canonical [preregistration, independent qualification, prior-evaluator and delivery requirements](../policies/SELF_IMPROVEMENT.md); the archive never promotes a candidate or resets cumulative budget. Preserve all outcomes and known-good rollback. These tool procedures do not change the evaluator.


## Exercise behavior and disclose measurement coverage

```sh
python3 agent-org/factory/instrumentation/scenarios.py --root agent-org
python3 agent-org/factory/metrics/autonomy.py path/to/attempt-observations.json
```

The scenario command invokes actual tool CLIs against resettable local fixtures and reports expected-positive and expected-refusal outcomes. It neither invokes external services nor proves native tool interception, hidden holdout confidentiality or production reliability. Fresh-worker qualification is separate; keep the worker's manifest, actual continuation/refusal and destination observations.

Autonomy scorecards count failed, blocked and retried attempts, repeated-task consistency, recovery, effect reconciliation, lesson recurrence and known resources. Unknown usage never means zero. Inputs require an attributed source; omitted operations remain outside coverage. These additional views do not alter existing organization/project/measurement-health scorecards or the promotion evaluator.

## Deliver and preserve the next action

The Coordinator follows the existing reviewed PR workflow through verified owning-remote main. Preserve exact head/tree, source/evaluator hashes, review and approval, effect reconciliation and current host checks. Record the observed merge/main outcome even where committed records are conditional pre-merge checkpoints. A fresh worker must recover from the durable manifest and observations without predecessor conversation. Stop/reconcile/revert through the prior rollback procedure on regression.

The mapping is explicit: records/registry readiness → reconciliation; source identity → context manifest; external attempts → effect journal and independent lookup; repeated corrections → queue/lineage; deterministic cases → scenarios; resource and reliability observations → separate scorecards; promotion → unchanged independent gate and PR/main verification. No new service or background scheduler is installed.
