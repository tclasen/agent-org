# Agent organizations and durable execution

Research observed 21 October 2026 (22 October UTC). TASK-000059 / RUN-000053. Local comparison baseline: organization remote-main revision `8916d3589054a6416098598a029d64c1d676dd7f`, with the current research admission records added in the isolated worktree. This is research and proposed experimentation, not operational adoption.

The strongest transferable idea is to separate an agent's identity, its current execution, the work item, the saved evidence and the actual external outcome. An org chart can organize responsibilities; it cannot establish that an interrupted operation did or did not happen. Agent-org already distinguishes roles, tasks, runs, independent decisions and verified delivery. Its useful next increment is a reliable reconciliation view over those records and observed effects, followed by recovery experiments that demonstrate correct continuation.

## What the implementations actually provide

### Paperclip organization management with an executing control plane

Paperclip's company metaphor sits on a Node server, React interface, persistent database and adapters to agent harnesses. Its README describes goals, reporting relationships, budgets, approvals and heartbeat wakeups. Those are project descriptions, not independently verified evidence that an autonomous company delivers business outcomes. [Repository overview](https://github.com/paperclipai/paperclip/blob/00818634632779cb717bb7539f88c05da699b2dc/README.md).

There are concrete ownership mechanisms beneath the metaphor. The inspected `issues.ts` implements checkout with dependency-readiness checks and run identity. Adoption of an unowned checkout locks the actor run, rejects a terminal actor, and conditionally updates an issue only when assignee, status and prior ownership conditions match. Stale-owner adoption similarly binds the update to the expected old checkout. This is stronger than two agents agreeing through prose that one owns a task. It is still a database-level ownership mechanism, not proof that every possible external tool respects the owner. [Checkout implementation](https://github.com/paperclipai/paperclip/blob/00818634632779cb717bb7539f88c05da699b2dc/server/src/services/issues.ts).

Recovery also distinguishes process status from resource settlement. `recovery.ts` can block automatic recovery when native execution ownership is unverified. Cleanup defers leases with pending workspace export and checks whether another lease still owns the same provider resource. A retained test constructs an unexported workspace, restarts the service, checks that cleanup preserves its file, marks export finalized, then checks cleanup occurs. These are inspected code and test expectations; this research did not run the test suite. [Recovery implementation](https://github.com/paperclipai/paperclip/blob/00818634632779cb717bb7539f88c05da699b2dc/server/src/services/heartbeat/recovery.ts), [restart/cleanup tests](https://github.com/paperclipai/paperclip/blob/00818634632779cb717bb7539f88c05da699b2dc/server/src/__tests__/heartbeat-orphaned-active-lease-sweep.test.ts).

**Transfer:** bind continuation to both task and run; retain ambiguous resources and evidence until reconciliation. **Limit:** adopting Paperclip would add an executing service and operational database, exceeding this repository's current no-new-runtime boundary.

### Gas Town durable assignments plus an active workspace manager

Gas Town separates persistent worker identity from ephemeral sessions. A Mayor coordinates projects; workers receive work on persistent hooks; convoys group work; Witnesses monitor workers; a Refinery processes merge requests. The current README describes long-lived services, patrols, runtime adapters and a capacity scheduler. Thus its reported background autonomy comes from running infrastructure, not from the names of its roles. Its scale descriptions are maintainer claims, not measured reliability results here. [Architecture and operating model](https://github.com/gastownhall/gastown/blob/ef70b0bf9e588dce00708e36564bfc06b51fac2c/README.md).

An especially useful detail is selective persistence. Formula templates can remain inline checklists under a root-only ephemeral work item, or materialize steps as sub-items using `pour = true`. The documentation says completed materialized steps support checkpoint recovery, while root-only steps reduce ledger growth. It explicitly recommends the latter for frequent cheap work and the former where losing progress is expensive. Neither mode establishes exactly-once external effects merely by closing a step. [Molecule mechanisms](https://github.com/gastownhall/gastown/blob/ef70b0bf9e588dce00708e36564bfc06b51fac2c/docs/concepts/molecules.md).

**Transfer:** checkpoint expensive or consequential transitions, instead of turning every reasoning step into permanent state. **Limit:** running Gas Town's daemon, continuous patrols and merge processor would require a separate authority decision. Agent-org's independent review and approval cannot be replaced by an automatically advancing merge queue.

### Beads a work ledger, not an autonomous executor

Current Beads is a dependency-aware issue graph backed by Dolt. `bd ready` discovers unblocked work; `bd update --claim` is documented as an atomic assignment plus status change. Hash-based issue IDs reduce identity collisions. Dependency links, audit history and durable project facts provide structured continuation context. This gives a concrete distinction between a ledger that tells an agent what remains and a runtime that wakes the agent to do it. [Current README and storage contract](https://github.com/gastownhall/beads/blob/ae4d7e90dff886758e9ed87eee014961980c10ad/README.md).

Freshness matters: older descriptions of Beads as a JSONL/Git tracker are incomplete for this revision. Embedded Dolt is now the documented default with a single writer; server mode supports multiple concurrent writers. `.beads/issues.jsonl` is an export for interchange, explicitly not the source of truth or a backup. Its experimental HTTP mode documents behavior differences, including cases where ready-and-claim falls back to separate operations. Therefore “atomic claim” must be qualified by operation, backend and version; it should not be generalized to every remote workflow.

**Transfer:** compute readiness and conflicts from canonical records; make storage and concurrency assumptions explicit. **Limit:** replacing agent-org's Markdown governance with Beads/Dolt would be a migration and new dependency, not a small documentation improvement. Hash IDs would also change existing identity governance without solving external outcome ambiguity.

### OpenHands saved conversations, execution environments and scheduling are separate layers

The current `OpenHands/OpenHands` repository is Agent Canvas. Its README assigns SDK, Agent Server, conversations, tools and workspaces to `software-agent-sdk`, while `automation` owns scheduling, webhooks, run history and dispatch. This differs from older monolithic descriptions. Canvas documents local execution and separate Docker conversations; it also warns that conversations sharing a host workspace share the files. Multiple containers do not by themselves create independent project histories. [Current repository boundaries and workspace limits](https://github.com/OpenHands/OpenHands/blob/main/README.md).

The SDK persistence example constructs a conversation with a unique ID and persistence directory, runs it, deletes the Python conversation object, then reconstructs it with the same ID and directory and continues. This is inspectable restoration behavior, not proof of correct recovery at every crash boundary. The persistence documentation describes saved messages, configuration, execution state, tool outputs and statistics. An event recording that a tool ran remains different from fresh evidence about the outside system after interruption. [Pinned persistence example](https://github.com/OpenHands/software-agent-sdk/blob/4b8cb431a66c1f4b813d6c9c0181ce63a4e30d0a/examples/01_standalone_sdk/10_persistence.py), [persistence documentation](https://docs.openhands.dev/sdk/guides/convo-persistence).

**Transfer:** explicit continuation identity and environment references in handoffs; distinguish conversation restoration from workspace recovery and scheduling. **Limit:** a new Agent Server or automation service is outside scope; this lane ran neither OpenHands nor a sandbox isolation test.

### MetaGPT SOPs, routed messages and explicit serialization

MetaGPT translates the software-company idea into role-specific actions, standardized intermediate artifacts and an environment for communication. In inspected source, `publish_message` routes a message to matching member addresses and records history; `run` executes non-idle roles with `asyncio.gather`. `Team.serialize` writes model state and context to `team.json`; `deserialize` reconstructs the team and rejects missing stored state. These are actual mechanisms beyond role naming. [Team state](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/metagpt/team.py), [environment routing and execution](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/metagpt/environment/base_env.py).

They do not establish transactional coupling between an external action and serialization. Nor does an internal reviewer persona establish the fresh, independently scoped review required locally. **Transfer:** standardized intermediate outputs make handoffs inspectable and route only relevant context. **Limit:** role proliferation and additional debate are hypotheses with cost, not evidence of better accepted outcomes.

### ChatDev bounded collaboration phases; distinguish legacy from current platform

Legacy ChatDev's default configuration is concrete: demand analysis, language choice, coding, completion, review, test and documentation phases. Review alternates comment/modification for three configured cycles; testing similarly alternates error summary/modification. The same configuration sets `git_management`, `self_improve` and `with_memory` to false. A “virtual software company” therefore does not imply enabled persistent memory or recursive improvement in that default. [Pinned legacy configuration](https://github.com/OpenBMB/ChatDev/blob/31fd994416a251ecdeb1f0a73c329271743bfb56/CompanyConfig/Default/ChatChainConfig.json).

The current main README labels this software-company version as ChatDev 1.0 legacy and describes 2.0/DevAll as a configurable multi-agent orchestration platform. Legacy results must not be attributed to the current platform or used as proof of durable service execution. [Current version distinction](https://github.com/OpenBMB/ChatDev/blob/a2ea4a263cebe9a7abd01ee3b5b0bf95698ed328/README.md).

**Transfer:** revisioned phases and explicit iteration limits. **Limit:** configured conversation cycles and self-reported completion do not verify remote delivery, independent acceptance or correctness on real repositories.

### LangGraph explicit checkpoints and replay boundaries

LangGraph distinguishes thread-scoped graph checkpoints from stores for cross-thread application data. In-memory savers lose data on restart; a persistent backend is necessary for process recovery. Checkpoints retain state and scheduled tasks; pending node writes can be retained separately. Replay from a checkpoint re-executes later nodes, including API and LLM calls. `exit`, `async` and `sync` durability modes trade persistence frequency for overhead; synchronous checkpointing precedes the next step, while exit-only mode cannot recover intermediate crash state. [Persistence overview](https://docs.langchain.com/oss/python/langgraph/persistence), [checkpointer contract and durability modes](https://docs.langchain.com/oss/python/langgraph/checkpointers).

The Functional API distinguishes an entrypoint from discrete tasks; task results are saved to the entrypoint's checkpoint. [Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api). **Transfer:** name the saved boundary and the work that may re-execute. **Limit:** a checkpoint is not a transaction with an arbitrary external API. Installing LangGraph would introduce a new runtime and persistence dependency; borrowing its state distinctions does not require that installation.

### Temporal deterministic history replay still needs effect idempotency

Temporal's Workflow code produces commands matched against persisted event history during replay. Workflow code must remain deterministic and compatible with histories; ordinary nondeterministic external work belongs outside that replay logic. [Workflow definition](https://docs.temporal.io/workflow-definition).

Completed Activities are not rerun during replay, but an Activity's result reaches history only when it returns or reports an error. If it performs an effect and fails to report, retry remains possible. Temporal therefore recommends idempotent Activities. Durable orchestration does not remove the “effect succeeded, acknowledgement lost” interval. [Activity idempotency](https://docs.temporal.io/activity-definition).

**Transfer:** separate intended action, observed effect, durable receipt and retry eligibility. **Limit:** Temporal requires a service and workers; adopting it is outside this research and current runtime constraint. Its orchestration guarantees also cannot certify that the requested business outcome was good.

## Local comparison and incremental proposals

Agent-org already has [readiness and single claims](../../shared/WORK_GRAPH.md), [startup reconciliation](../../shared/SESSION_LIFECYCLE.md), [context manifests](../../shared/CONTEXT_MANAGEMENT.md), [independent acceptance and remote-main verification](../../policies/ACCEPTANCE.md), and an [event store](../../factory/instrumentation/events.py) with local locking, duplicate-event checks, hash chaining and `fsync`. The [factory contract](../../factory/README.md) explicitly discloses bypass routes and forbids permanent scheduling. Event identity deduplication does not deduplicate an external operation; Markdown claims are procedural, not database compare-and-set locks.

The merged [Tessl research](../TESSL_FACTORY_RESEARCH.md) already proposes context manifests, correction mining and behavioral sequences. The following are narrower implementation candidates for its recovery proposal. Each requires its own admitted plan, prior-evaluator evidence, fresh Reviewer and independent Chief of Staff decision. No file or policy below is created by this report.

| Priority and proposed paths | Owner and dependencies | Proposed experiment and rollback |
| --- | --- | --- |
| 1. `agent-org/factory/instrumentation/reconcile.py`; `agent-org/factory/tests/test_reconcile.py`; dated reports under `agent-org/factory/reports/reconciliation/` | Coordinator defines inputs; Developer implements read-only projection over canonical tasks/runs, ID inventory, Git provenance and explicitly supplied GitHub/main observations. Reuse existing parsers. | Preserve source hashes and observation times; distinguish historical record, observed delivery, stale warning, active conflict and unknown. Compare decisions and effort against current startup. Remove advisory tool/report dependency if benefit is inconclusive; retain original records. |
| 2. `agent-org/shared/templates/EFFECT_RECONCILIATION.md`; fixtures under `agent-org/factory/benchmarks/behavior/effect-recovery/` | Architect specifies with Coordinator; Reviewer defines cases. Depends on operation-specific authorized lookup. | Record intended target, authority/candidate, stable operation identity, attempt, observed receipt, ambiguity and safe lookup before retry. Test local simulated receipts. Withdraw template if it causes premature success or unsafe retry; preserve incident evidence. |
| 3. `agent-org/shared/templates/CONTINUATION_CHECKPOINT.md`; `agent-org/factory/benchmarks/behavior/checkpoint-recovery/` | Coordinator and Architect; depends on context manifest and native-status evidence. | Compare existing handoff with compact checkpoints only at expensive transitions: source inventory, candidate pin, review decision, effect attempt and verified delivery. Measure recovery reads, repeated work and errors. Revert added fields if overhead exceeds demonstrated benefit. |
| 4. `agent-org/factory/benchmarks/behavior/ownership-recovery/`; `agent-org/factory/reports/recovery-trials/` | Fresh Reviewer owns expected behavior before Developer fixtures; Coordinator conducts native trials. Depends on the first three candidates only when separately admitted. | Reproduce failure, verify a legitimate alternative, then use held-out sequences and fresh replacement workers. Keep current evaluators and budget rules. Reject or roll back any proposal that weakens authority, independence or delivery proof. |

A useful projection must handle legitimate premerge snapshots. The baseline's ledger and completed-delivery records can lag later merged evidence: Coordinator's startup audit identified TASK-000051..56 and their runs as examples. That audit is supplied evidence, not a new GitHub verification by this lane. Do not infer failed delivery solely from committed `awaiting_acceptance` prose, or infer a live conflicting worker from a stale `running` field. Conversely, a PR body saying “complete” cannot substitute for observed merge content and remote-main verification. Emit the disagreement and its sources; repair canonical state through separately scoped reconciliation rather than rewriting history automatically.

## Recovery evaluation that would justify adoption

Use pinned synthetic initial states and fake external-effect receipts first. Run sequences through the actual Coordinator admission/recovery consumer, not only a pure transition model. Give fresh workers the durable handoff without predecessor conversation. Require independent expected outcomes and retained counterexample traces. The initial suite should include:

- Duplicate dispatch for one task, overlapping scope and two owners: identify the conflict before another mutation; do not claim that a Markdown checker provides a distributed lock.
- Interruption before a checkpoint, after artifact write, during review and after an approved candidate changes: preserve artifacts, reconcile native ownership, invalidate affected approval and resume only remaining authorized work.
- Effect succeeds but response is lost; effect fails before execution; lookup itself fails: recover using operation identity and observed state, retain unknown when lookup is unavailable, and avoid blind duplication.
- Replayed intent with changed payload or target; an identical repeated receipt; a late result from an old worker: reject conflicting identity reuse and prevent stale output from authorizing a new candidate.
- Cancellation while a worker may still run, or sandbox output awaiting export: reconcile status and preserve undelivered evidence before releasing a claim or resource.
- Remote merge succeeds while local closure is stale; source records claim delivery while remote evidence is absent: distinguish verified outcome, incomplete delivery and unavailable evidence without silently altering history.

Measure outcome correctness, duplicate effects, authority violations, unnecessary re-execution, manual repair, total accepted-delivery effort and unknown evidence coverage. Paired benefit evaluation must use the existing organization rules; no new numerical promotion threshold is adopted here. Every expected refusal must actually occur. One safe fixture pass is insufficient evidence of native-tool interception or post-session execution.

## Primary-source register

All entries were observed 22 October 2026 UTC. Commit links in the analysis identify exact inspected mechanisms; short revisions below are their prefixes.

| System | Revision or observation | Primary material and coverage |
| --- | --- | --- |
| Paperclip | `008186346327` | README; transactional issue checkout; recovery implementation and workspace-cleanup test. Source/test inspection only. |
| Gas Town | `ef70b0bf9e58` | Current README and molecule guide; roles, active services and selective step persistence. Old `steveyegge/gastown` file endpoint failed; current location is `gastownhall/gastown`. |
| Beads | `ae4d7e90dff8` | Current README; Dolt modes, claiming and documented HTTP differences. Old owner path failed; current location is `gastownhall/beads`. |
| OpenHands | SDK `4b8cb431a66c`; Canvas moving main | SDK persistence example; official persistence guide; Canvas README boundaries. Current SDK/automation split distinguished from historical monolith. |
| MetaGPT | `11cdf466d042` | Team serialization and environment messaging/execution source. No inference that persistence covers every effect boundary. |
| ChatDev | legacy `31fd994416a2`; current `a2ea4a263ceb` | Legacy default phase configuration; current README identifying 1.0/2.0 distinction. Legacy configuration is not a claim about 2.0 defaults. |
| LangGraph | Official docs, dated read | Persistence, checkpointers and Functional API; backend requirements, replay and durability options. Documentation URLs can change. |
| Temporal | Official docs, dated read | Workflow determinism and Activity idempotency; documented acknowledgement-loss limit. No deployment or benchmark. |

## Authority and evidence limits

Small Markdown contracts, read-only projections, deterministic fixtures and active-session native trials can be considered through existing organization improvement authority. Installation of Paperclip, Gas Town, Beads, OpenHands, LangGraph or Temporal; background patrols/schedulers; new databases replacing canonical state; harness hooks; hosted accounts; external messaging; project enrollment; and automated merge/deployment need separately scoped authority where outside existing grants. This research authorizes none of them.

Primary sources were read through the GitHub plugin and official documentation. GitHub file revisions were checked against the commit links above for the detailed Beads, Gas Town molecule, OpenHands persistence, MetaGPT and legacy ChatDev mechanisms. Paperclip code is pinned to `0081863`. OpenHands Canvas overview is a dated moving-branch read; LangGraph and Temporal documentation are also dated observations, not immutable specifications. Old `steveyegge` file reads failed and were resolved through the author's linked `gastownhall` repositories. No framework was installed, executed or benchmarked; no independent production reliability, economic benefit or universal exactly-once outcome is established. This lane changed only its research report and run checkpoint; public reads were the only external interactions.
