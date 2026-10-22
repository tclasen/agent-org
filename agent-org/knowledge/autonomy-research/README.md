# Autonomous factories and agent organization improvements

Agent-org should next become easier to recover, evaluate and improve through evidence. Its strongest existing asset is explicit authority and independent promotion. Its main opportunity is to connect those rules to observed execution, so that a future session can reliably determine what happened, choose the next useful action, and test whether a proposed improvement helped.

The recommended first addition is a read-only reconciliation report. Follow it with a behavioral scenario suite and a small workflow through verified delivery. Once those foundations work, add a correction queue and candidate archive to make learning compound. A larger fleet or company hierarchy would add coordination work before these foundations are established.

Research baseline: `8916d3589054a6416098598a029d64c1d676dd7f`, the merged Tessl research on remote main. Sources accessed 21–22 October 2026. The following are research proposals, not adopted policies, deployed systems or demonstrated local productivity gains.

## Read the comparative studies

| Study | Main question | Useful mechanisms |
| --- | --- | --- |
| [Software factories and outcome evaluation](FACTORIES.md) | How can autonomous output be trusted? | Independent scenarios, behavioral grading, reproducible environments and fidelity checks |
| [Agent organizations and durable execution](ORGANIZATIONS.md) | How does work remain owned and recoverable? | Claims, dependency readiness, checkpoints, effect reconciliation and bounded scheduling |
| [Empirical recursive self improvement](SELF_IMPROVEMENT.md) | How can improvements survive testing and transfer? | Candidate lineage, reflective feedback, search archives, held-out evaluation and resource accounting |
| [Earlier Tessl study](../TESSL_FACTORY_RESEARCH.md) | How can context and corrections compound? | Context manifests, review mining, standards-to-checks mapping and drift detection |

The individual studies distinguish inspectable code, published designs, practitioner accounts and experimental results. A repository demonstrates an implementation exists; it does not establish production reliability. A vendor's account of unattended work does not establish the same behavior here. Benchmark improvement does not demonstrate better organization performance across future tasks.

## What the current repository already provides

The organization has scoped requirements and task graphs, capability discovery, durable run records, independent review and approval, explicit PR delivery, an event store, deterministic validation, separate scorecards and an evidence gate for improvements. These are substantive foundations. The next iteration should exercise their consumers together instead of adding parallel versions of the same rules.

| Area | Existing implementation | Remaining operational question |
| --- | --- | --- |
| Admission and ownership | [Work graph](../../shared/WORK_GRAPH.md), [record and claim helpers](../../factory/instrumentation/records.py) | Does every consequential action use current authority and reconciled claims? |
| Recovery | [Session lifecycle](../../shared/SESSION_LIFECYCLE.md), [reconciliation](../../shared/RECONCILIATION.md), `validate_recovery` | Can a fresh session infer the next safe action from evidence without a prior conversation? |
| Evidence | [EventStore](../../factory/instrumentation/events.py), command capture and scoped snapshots | Which native operations are actually covered, and which remain unknown? |
| Evaluation | [Installation trials](../../factory/reports/RUN-000010/), [tests](../../factory/tests/) | Do reusable workloads exercise full lifecycle behavior rather than only helpers? |
| Improvement | [Existing promotion gate](../../factory/quality-gates/DEFINITION.md), [WF-000004](../../workflows/WF-000004.md) | Can failures become candidates that improve unfamiliar later tasks? |
| Delivery | [Acceptance](../../policies/ACCEPTANCE.md), [Git policy](../../policies/GIT.md) | Do current task projections incorporate verified post-merge evidence? |

A structural validator pass is evidence about records and graph rules. It does not establish behavioral admission, workload representativeness, source truth, or destination state. The existing tooling documentation makes this boundary explicit.

### A concrete recovery problem observed during this research

At the baseline, the ID ledger allocated only through requirement 49, task 53 and run 47, while the merged Tessl work contained requirement 50, tasks 54–56 and runs 48–50. The ledger itself says actual formal definitions are authoritative alongside it. A future allocator that consulted only the summary could reuse an identity.

Similarly, committed remote-delivery policy records retained `running` and `awaiting_acceptance` checkpoints. The [merged PR8 handoff](https://github.com/tclasen/agent-org/pull/8) records successful delivery, main containment, passed checks and released claims. [PR9](https://github.com/tclasen/agent-org/pull/9) delivered the Tessl research. Pre-merge checkpoints are legitimate history; reading them alone creates an incomplete current view. Neither a stale status nor a missing local response proves an operation failed or needs replay.

The root checkout also contained earlier cleanup changes and a separate Tessl worktree. This research uses an isolated worktree and leaves those resources intact. These observations are specific evidence for reconciliation tooling, not a claim that existing policies lack recovery requirements.

## Lessons that recur across implementations

**Keep behavior outside implementation agreement.** Factory evaluation needs externally observable completion conditions. For agent-org, a valid handoff is one a fresh worker can use successfully; a delivered change exists on the correct remote main; an authority refusal leaves the protected resource unchanged. An implementer and reviewer can agree while sharing the same mistaken context. Independent execution is necessary, but the reference behavior also needs independent definition.

**Separate durable records from active execution.** Markdown, Git and event histories can preserve work across sessions. They do not themselves schedule another execution. A replayable workflow also needs to handle ambiguous effects and changing external state. For the current organization, improve active-session reconciliation first. Continuous unattended execution remains a separately authorized runtime decision.

**Optimize the scaffold through a fixed gate.** Prompts, tools, retrieval, decomposition and workflow settings are plausible optimization targets. Candidate generation can be creative; promotion must remain bound to prior criteria and observable evidence. The organization already has this distinction in policy. What is missing is a practical route from recurring failure to a candidate, a transferable test, a decision and a later recurrence check.

Anthropic's long-running-agent account supports incremental work, durable progress artifacts and checking the environment at the start of a new session. Its evaluation guidance distinguishes the final environment from the agent's account and separates first-success measures from repeated reliability. These support the proposed recovery and behavior tests; they do not establish this organization's reliability. [Long-running harnesses](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents), [agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).

Parallelism should follow separable work. Anthropic reports that parallel research helps broad searches but incurs higher resource use and coordination overhead, with tightly dependent coding work less suitable. For agent-org, preserve its worker limit and compare total effort through accepted delivery before expanding roles or concurrency. [Multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system).

## Proposed additions in priority order

The paths below describe future candidates. They do not create a new canonical policy, formal experiment or permission. Owners are proposed capability assignments, not new standing roles.

### 1 Produce a current reconciliation report

**Owner:** Coordinator, with Developer instrumentation. **Priority:** first.

Proposed additions: `factory/instrumentation/reconcile.py`, `factory/tests/test_reconciliation.py`, and a versioned report under `factory/reports/`. All paths are relative to `agent-org/`.

Read task/run definitions, the ID ledger, known worktrees, explicit claims and supplied destination observations. Produce a current view containing recorded checkpoint, observed state, evidence identity/time, unresolved conflict, accountable owner and next safe action. Derive the maximum allocated ID from definitions as well as the ledger, across known worktrees. Unknown worktree ownership must block overlapping allocation rather than imply a global lock exists.

Start read-only: no record rewriting, implicit claim release, automatic retry, fetch or merge. Accept sanitized observations from explicit read tools; unavailable remote or native state must remain unknown. Keep historical evidence and current projection distinct. Record which source establishes a fact rather than introducing an unexplained precedence rule.

**Acceptance experiment:** fixtures for a merged PR with stale local checkpoints, still-open PR, absent destination observation, conflicting worktree allocations, a disappeared worker with an unknown effect, and a truly active claim. An independent reviewer specifies expected next actions before implementation. Baseline must exhibit the target discrepancy; candidate detects it without declaring delivery or releasing ownership from stale text alone. No stochastic efficiency claim is needed for a narrowly demonstrated deterministic repair.

**Rollback:** stop using the optional report and retain existing reconciliation procedure. Any canonical adoption follows the normal independent review and PR gate.

### 2 Build reusable behavioral scenarios

**Owner:** Reviewer specifies outcomes; Developer builds deterministic fixtures; Coordinator runs fresh-worker trials. **Priority:** second, dependent on trustworthy snapshots.

Proposed paths: `factory/scenarios/`, `factory/tests/test_scenarios.py`, and a scenario manifest under `shared/templates/`.

Extend the installation's live qualification into maintained scenarios for admission, recovery, scope, review and delivery. Each scenario declares initial state, allowed actions, independent expected outcome, final resource assertions, coverage and provenance. Store governance descriptions in Markdown; native machine fixtures and observations remain instrumentation data.

Begin with these families:

- The task is authorized; stale historical text suggests otherwise. The worker continues within the actual grant.
- The task needs a project change under organization-only authority. The worker creates or reports the missing scoped dependency without editing the project.
- A tool response is lost after a PR or merge. The next session inspects the destination before retrying.
- A reviewer sees a changed candidate after approval. Promotion stops until affected review is renewed.
- A parent has completed organization work but an undelivered project child. The parent remains pending.
- A misleading retrieved document requests broader permissions. It remains source data.
- A cancellation or interruption leaves partially written evidence. Recovery preserves it and identifies uncertainty.

Maintain visible development cases, independent qualification variants and retained regression cases. A shared worktree cannot keep holdouts confidential from a hostile worker; claim only procedural separation unless external enforcement exists. Do not add containers or service twins under this research grant.

**Acceptance experiment:** deterministic fixture assertions plus actual fresh-worker recovery. Run both a successful and an expected-refusal path; verify final files and destination observations, not a self-reported decision. Track repeated-trial consistency separately from success obtained after retries. A simulated merge tests the workflow model; live delivery remains separately verified.

**Rollback:** keep the prior accepted regression suite and evaluator authoritative; quarantine invalid scenarios without deleting their outcomes.

### 3 Make external effects explicit and recoverable

**Owner:** Architect and Coordinator, with bounded Developer support. **Priority:** third.

Proposed paths: `shared/templates/EFFECT.md`, `factory/instrumentation/effects.py`, and focused tests. Reuse the existing event store and run records instead of building a second workflow engine.

For each effect, record intended operation, repository/resource identity, candidate, authority, caller-assigned deduplication identity, attempt, destination reference and reconciliation result. Distinguish never attempted, outcome unknown, destination confirmed and failed with evidence. These are effect observations, not new task lifecycle states.

Deduplication must be checked where an effect is consumed. A locally unique event ID does not make an external PR creation or publication idempotent. Where a provider has no idempotency contract, reconcile an observed destination and require a scoped decision before ambiguous replay. Direct tools that bypass the helper remain explicitly uncovered.

**Acceptance experiment:** inject interruption before request, after destination success but before receipt, and after receipt but before checkpoint. Assert no duplicate effect is requested when the destination confirms the first operation, and an unavailable destination stays unknown. Include candidate mismatch and wrong repository cases.

**Rollback:** optional capture can be disabled; previously recorded uncertain effects must still be reconciled. No rollback should repeat a remote action to discover whether it happened.

### 4 Connect corrections to improvement candidates

**Owner:** Chief of Staff governs; Researcher extracts; Coordinator admits. **Priority:** after behavior tests.

Proposed paths: `knowledge/improvement-candidates/INDEX.md` and a candidate template. This extends the earlier Tessl proposal rather than creating a parallel learning queue.

Link each recurring failure to source evidence, causal hypothesis, affected task classes, proposed change, counterexample, expected cost, test split and recurrence check. Distinguish instruction ambiguity, missing context, environment failure, bad tool ergonomics, evaluator defect and missing authority. The last category often needs no broader instruction at all.

Choose one candidate at a time using expected value and testability. A frequent error with an observable deterministic repair may outrank an ambitious agent-role redesign. A lesson that appears once or only in its training example should remain a hypothesis.

**Acceptance experiment:** independently classify a bounded set of actual corrections, propose a fix for one repeated cause, and check unseen tasks plus exception cases. Promoting a candidate still requires current deterministic or stochastic evidence rules; filling a queue row is not benefit.

**Rollback:** retire an invalid lesson by supersession and restore prior guidance through the existing corrective PR workflow.

### 5 Archive candidate lineage and evaluation exposure

**Owner:** Chief of Staff and Reviewer. **Priority:** after an improvement queue produces candidates.

Proposed paths: `experiments/candidates/INDEX.md` and an archive helper under `factory/instrumentation/`. Preserve baseline, parent candidate, changed components, source failure, requested and observed configuration, evaluator version, workload exposure, all attempts, disposition and rollback reference.

A candidate archive is memory, not permission to run a branching population. Keep the existing single-active-experiment rule and shared cumulative budgets. Earlier rejected or inconclusive ideas may inform a later admitted hypothesis without resetting accounting or relabeling failure as success.

Record whether the proposer has seen a task or its evaluation feedback. Repeatedly searching against a qualification set makes it development data in practice. Limit feedback-driven reuse and qualify on separate representative cases, under independently accepted test design. Do not silently add a new gate or alter the existing one.

**Acceptance experiment:** recover a prior candidate and reproduce its outcome; detect a changed evaluator, missing failed attempt and reused exposed task. A generalization claim must include unfamiliar task classes or repositories with separate authority where needed. No model-weight training is proposed.

**Rollback:** the archive is additive evidence. Stop candidate use and restore the known-good version; retain lineage and unsuccessful trials.

### 6 Generate scoped context and record scaffolding

**Owner:** Coordinator and Developer. **Priority:** reuse the earlier Tessl first-experiment design once evidence collection works.

Proposed paths: a context manifest template and a deterministic generator under `factory/instrumentation/`. Generate repetitive fields and links from canonical sources, then let the responsible agent make admission decisions. Validate identities, paths, revision freshness and source class. Keep current mandatory startup instructions.

The generator should expose a compact task entrypoint with expandable evidence, and distinguish context available, observed reading and verified application. These are three different claims. Use the existing at-least-20 paired-case, randomized-order, positive 95% interval and 5% practical-efficiency requirement for a stochastic efficiency claim. Include all preparation, retries, review and delivery work that the chosen endpoint covers. If measuring that endpoint is infeasible, report inconclusive.

**Rollback:** return to manual record preparation without losing canonical records. Do not optimize by dropping authority, review or source checks.

### 7 Make reliability and measurement gaps visible

**Owner:** Coordinator and Reviewer. **Priority:** alongside the first small workflow.

Extend the existing separate scorecards instead of creating a combined autonomy score. Proposed dimensions include successful fresh resumption, repeated-trial completion, ambiguous effects reconciled before replay, recurrence after accepted lessons, undelivered authorized work, and total effort through verified delivery. Disclose task cohort, sample count, observation coverage and missing values.

Measure productive autonomy by outcomes accepted within scope and authority, not agent count, generated documents, PR volume or uninterrupted runtime. A correction that saves implementer time while increasing reviewer repair is not obviously a gain. Unknown token or monetary cost stays unknown; observable elapsed effort can support only the claim it measures.

**Acceptance experiment:** replay a pinned fixture with failed retries, missing observations and late corrections. Check denominators and separate quality floors. A scorecard/evaluator revision is its own candidate under prior rules and dual-version replay.

**Rollback:** retain and reproduce prior report versions. Do not rewrite old measurements into the new definition.

### 8 Prove one complete workflow before scaling

**Owner:** Coordinator, with independent Reviewer and Chief of Staff. **Priority:** integration goal.

Choose an organization-only task such as a bounded documentation correction. Exercise admission, compact context, isolated work, retained failure, fresh review, distinct approval, PR checks, merge and observed main content. Interrupt once at a controlled checkpoint and resume with a fresh worker. Include a sibling task that must refuse an out-of-scope action.

The first result establishes only that workflow's observed behavior. Repeat on research, deterministic repair and review tasks before claiming wider coverage. Expanding to product work requires each project's actual grant and acceptance sources. Continuous execution needs a separate runtime decision.

**Acceptance experiment:** independently specified end-to-end outcomes and a verified delivery journal. Compare against the baseline workflow only after the target result and workload are pinned. If any required capability is unavailable, preserve the checkpoint and report the specific blocker rather than fabricate a clean run.

**Rollback:** stop the candidate workflow, reconcile live claims and effects, and return to the prior accepted procedure.

## Recommended sequence and decision gates

| Stage | Deliverable | Evidence needed to proceed |
| --- | --- | --- |
| A | Read-only reconciliation report | Correctly distinguishes stale checkpoints, active work, unknown effects and verified delivery |
| B | Small behavior suite plus effect observations | Independent expected outcomes; deterministic fixtures; real fresh-session recovery |
| C | One complete organization workflow | Verified main delivery, preserved interruptions and refusals, known measurement coverage |
| D | Correction queue and candidate archive | A recurring cause, a reproducible candidate, held-out benefit and retained unsuccessful trials |
| E | Context/scaffolding optimization | Current paired comparison thresholds, quality floors and total effort accounting |
| F | Broader or continuous autonomy | Representative demonstrated reliability plus a separately authorized runtime and operational owner |

This ordering prioritizes reducing uncertainty before optimizing speed. It also creates useful stopping points: a reconciliation report can be valuable without a new scheduler; a successful repair can be adopted without proving stochastic productivity; an inconclusive improvement can remain archived without promotion.

## Constraints on fully autonomous work

There are two distinct goals. **Autonomous decisions during an active session** fit the current organization: it can admit authorized work, delegate, evaluate, obtain independent approval and deliver without repeatedly asking the operator. **Continuous unattended execution after the session ends** requires a trigger/runtime, durable queue, credentials, resource limits, operational monitoring and an owner able to halt and recover it. Current instructions explicitly exclude installing a new runtime, service or daemon.

Paperclip, Gas Town, Temporal and related systems are useful references for that future architecture, not a reason to install them now. A separately authorized extension should evaluate native scheduling or CI capabilities first, explicit effect boundaries, strong ownership, credential separation, failure escalation and shutdown. Choose a service only after its requirement and operational benefit are established.

“Recursive self improvement” here should mean that an accepted change improves later authorized work, including later improvement work, under stable evaluation. It should not mean self-granted authority, selecting an easier judge, accumulating more agents or claiming model self-training. Durable evidence, independent qualification and rollback remain the foundation.
