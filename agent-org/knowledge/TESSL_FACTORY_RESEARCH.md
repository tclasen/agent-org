# Tessl software factory lessons for agent organization

Research date: 21 October 2026. Recommendations for the organization at revision `ca6ff20`; research and proposal only, with no change to active policies, evaluation thresholds, tool permissions or project sources.

Tessl’s most useful lesson for agent-org is to make corrections compound: capture a recurring failure, improve the context available before work starts, check the resulting behavior, and verify that later tasks need less correction. Agent-org already has substantial governance for this. Its next investment should make that governance easier to apply and measure, rather than add agents or another orchestration service.

My recommended first experiment is a smaller, task-specific context manifest with observable read evidence. Next, turn repeated review corrections into a shared standard plus a regression scenario. Develop focused semantic verifiers only after deterministic checks and behavioral tests cover what they can. These are benefit hypotheses, not established productivity gains.

## What Tessl actually operates

Tessl’s internal factory is Kikimora. It should be distinguished from Tessl’s commercial context platform and from StrongDM’s separate software factory. Tessl’s current website describes skills, loops and factories; its September 2025 launch described a spec-driven Framework and Spec Registry. The older launch is useful history, not proof of current product availability or CLI behavior. Current documentation explicitly describes migration from tiles to plugins. [Tessl platform](https://tessl.io/), [2025 launch](https://tessl.io/blog/tessl-launches-spec-driven-framework-and-registry), [package migration](https://docs.tessl.io/use/tile-to-plugin-migration).

The 28 July 2026 account describes Linear tickets dispatched to coding agents in isolated sandboxes, followed by review and merge. It reports roughly 65–70% of the speaker’s team PRs going through the factory, roughly 40% of company production changes, and 95% of factory-shipped code without human inspection. These populations differ. It also describes a duplicate-comment queue bug producing conflicting sandbox commits, and an Elixir rebuild exposing Linear routing and GitHub batching gaps missing from end-to-end coverage. These are vendor-reported operating experiences, not an independently audited reliability study. [Rob Willoughby interview](https://tessl.io/podcast/116).

On 2 September, Tessl reported a peak of about 850 PRs in one week, with 85–90% agent-handled end to end. The account emphasizes context-specific review and a progression from skills to feedback loops. The peak is neither a sustained throughput baseline nor a measure of customer value. It cannot be combined with July’s percentages into a growth calculation because scope and definitions differ. [Dru Knox interview](https://tessl.io/podcast/121).

Tessl also documents a risk ladder: some internal work can merge automatically, while feature owners retain final responsibility for more sensitive areas. This is stronger evidence for selective automation than for removing review everywhere. [Amy Heineike on harness engineering](https://tessl.io/blog/the-rise-of-the-harness-engineer).

StrongDM’s account describes a distinct system using scenario validation and a Digital Twin Universe. It is a useful comparison for external behavior testing, but it does not establish that Tessl uses the same architecture. [StrongDM factory](https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai).

## What agent-org already has

The following assessment concerns implemented instructions and tooling, not a claim that every mechanism has been proven on live work.

| Tessl practice | Current agent-org mechanism | Increment worth investigating |
| --- | --- | --- |
| Specify intent before execution | [Planning](../policies/PLANNING.md), scoped requirements and tasks | Reduce repeated discovery with validated task context manifests |
| Treat context as maintained software | [Context management](../shared/CONTEXT_MANAGEMENT.md), role AGENTS and CONTEXT, Git revisions | Track what was available, read and applied separately |
| Learn from corrections | [Self improvement](../policies/SELF_IMPROVEMENT.md), [WF-000004](../workflows/WF-000004.md), [legacy lessons](../shared/LEGACY_LEARNINGS.md) | Create a searchable route from correction to proposed rule and retained scenario |
| Layer checks and review | [Factory tooling](../factory/README.md), independent Reviewer and Chief of Staff | Name semantic checks precisely and calibrate their applicability |
| Observe quality and resource use | [Scorecards](../factory/metrics/DEFINITIONS.md), explicit missing telemetry | Measure total effort through verified delivery, including repair and review |
| Control task ownership and recovery | [Work graph](../shared/WORK_GRAPH.md), [session lifecycle](../shared/SESSION_LIFECYCLE.md) | Exercise duplicate, interrupted and stale-state sequences at final consumers |
| Preserve accountability | [Authority](../policies/AUTHORITY.md), [acceptance](../policies/ACCEPTANCE.md), PR delivery | Keep existing independent decisions while reducing avoidable preparation work |

The principal gap is an operational connection among these mechanisms. A lesson in Markdown, a completed checklist and an approved experiment definition are different from a later agent avoiding the mistake. This distinction also follows Tessl’s warning that implementation and review can agree because both received the same flawed context. [Context-driven factory engineering](https://tessl.io/blog/engineering-a-context-driven-software-factory).

## Prioritized changes to investigate

Priority below is my judgment of likely value and ease of evaluation. Each item needs its own admitted implementation plan; this research does not promote it.

### 1 Make task context easier to discover and verify

**Owner:** Coordinator with Developer implementation. **Priority:** first experiment.

Extend the existing context manifest rather than introduce another memory store. Give each task a compact entrypoint listing mandatory authority and scope, its requirement and approved plan, the relevant role, applicable checks, and expandable evidence links. Validate paths and revisions before delegation. Keep the required startup readings intact; experiment with reducing redundant task-specific loading after startup.

Proposed paths: a manifest example under `agent-org/shared/templates/` and a deterministic resolver under `agent-org/factory/instrumentation/`. Existing [context instructions](../shared/CONTEXT_MANAGEMENT.md) remain authoritative until a separately approved change.

Record three distinct observations: context available in the manifest; a supported tool trace showing the worker opened it; independently verified behavior satisfying the requirement. A read receipt alone proves neither attention nor correct application. Unsupported trace coverage stays unknown. Tessl’s activation measurement currently detects explicit Claude Skill calls; other access paths can escape that signal, and other agents may report activation as unmeasured. [Test variants and activation](https://docs.tessl.io/improving-your-skills/comparing-with-test-variants).

**Benefit hypothesis:** less rediscovery and stale-path repair without losing authority or correctness. Compare existing and proposed manifests on paired tasks. Count missing required context, unnecessary reads, correction rounds and time to accepted output. Reject any missing authority material. Do not strip mandatory rules to create an artificially cheap baseline.

### 2 Turn review corrections into a governed learning queue

**Owner:** Chief of Staff governs; Researcher extracts evidence. **Priority:** next.

At the existing five-accepted-task review opportunity, inspect a bounded sample of recent reviews and failed runs. Group repeated corrections by cause, not wording. For each candidate retain the source revision, original defect, rejected and accepted artifacts, proposed scope, contradictory examples, owner and regression case. Route it to one of: clearer context, deterministic test, semantic verifier, environment repair, or no generalizable lesson.

A proposed `agent-org/knowledge/improvement-candidates/INDEX.md` can point to evidence without duplicating canonical rules. Keep it a proposal queue, not authority. Tessl’s documented optimization workflow mines review history and CI results, proposes improvements, and does not itself make changes; its review miner similarly proposes checks from repeated feedback. [Quality improvement workflow](https://docs.tessl.io/tutorials/improving-agent-code-quality), [review mining](https://docs.tessl.io/automations/overview/overview/example-schedules/use-case-review-miner).

**Benefit hypothesis:** fewer repeats of already understood errors. Evaluate later held-out tasks for recurrence and reviewer effort, including false generalizations. Keep domain-specific lessons local until transfer is demonstrated. Run during active sessions under existing triggers; Tessl’s hosted scheduling is not an instruction to install a daemon here.

### 3 Maintain a mapping from standards to checks

**Owner:** Architect defines scope; Developer implements; Reviewer calibrates. **Priority:** high.

For each important standard record its authoritative source and revision, applicable task or file scope, enforcement mechanism, evidence, known blind spots and dependent checks. Prefer existing deterministic checks for record structure, links, candidate identity and graph validity. Use an LLM verifier only for an observable yes/no judgment those checks cannot reliably express. Keep general independent review for unforeseen defects.

Tessl’s verifier documentation distinguishes instruction from verification, separates applicability from severity, and excludes broad aesthetic judgments. Its CI guide recommends advisory operation and scope inspection before blocking changes. [Verifier concepts](https://docs.tessl.io/codifying-and-enforcing-your-skill-standards/verifiers-overview), [verifier calibration](https://docs.tessl.io/codifying-and-enforcing-your-skill-standards/verify-agent-changes-in-ci).

Start with an organization-specific question such as whether a handoff’s claimed next action is supported by its cited authority and observed state. Do not ask a file-only judge to establish live remote delivery. A remote/API check must establish that fact. Require an applicability result, evidence location and unknown outcome when essential context is absent.

Proposed artifact: `agent-org/knowledge/standards-to-checks.md`. Any implementation belongs in the existing factory tooling. **Evaluation:** independently label valid, invalid, ambiguous and inapplicable cases before running the judge; measure false positives, false negatives and abstention. Check adversarial instructions in evaluated artifacts. A semantic judge must not replace scope enforcement, independent approval or remote verification.

### 4 Build behavioral regression cases from actual incidents

**Owner:** Reviewer specifies cases; Developer maintains fixtures. **Priority:** high.

Expand beyond synthetic schema examples to tasks that reproduce real decision failures. Useful initial cases are a misleading old acceptance record, stale source paths, a lost response after a remote effect, a changed requirement, a rejected candidate, and an out-of-scope dependency. Each fixture needs an input task, pinned initial state, allowed actions, protected evidence, expected behavior and independent grading.

The source for these cases is local history and retained failures, including [legacy lessons](../shared/LEGACY_LEARNINGS.md); do not import private data into fixtures. Place cases under a proposed `agent-org/factory/benchmarks/behavior/` and bind each to its source correction. Existing tests and live fresh-worker qualification remain useful and should be reused.

Tessl distinguishes review of skill quality from task evaluation, compares agents with and without context, and supports scenarios derived from commit history. That is inspiration for task-level regression, not a reason to upload repositories. [Task evaluation](https://docs.tessl.io/improving-your-skills/evaluate-skill-quality-using-scenarios).

**Evaluation:** prove a retained failure can be reproduced, a legitimate alternative passes, and the candidate fixes the failure without relaxing the rubric. Keep optimization cases separate from held-out acceptance cases; generated rubrics require independent inspection.

### 5 Test ownership and recovery as sequences

**Owner:** Architect and Developer, with independent Reviewer. **Priority:** high for reliability.

Model the permitted transitions around task claim, candidate pin, review, effect attempt, response loss and reconciliation. Exercise sequences, not just isolated helper calls: duplicate dispatch; interrupted owner; old approval with a changed candidate; effect succeeded but response was lost; two requests for one claim; cancellation during review; delivery verified while closure prose remains stale.

The relevant existing surface is [work graph](../shared/WORK_GRAPH.md), [lifecycle](../shared/SESSION_LIFECYCLE.md) and `agent-org/factory/tests/test_records.py`. Markdown claims remain procedural coordination. A test passing against a model does not establish that native tools universally enforce it.

**Evaluation:** retain minimal counterexample sequences and run them against the actual admission/recovery consumer where one exists. Where behavior is Coordinator-mediated, include fresh-worker trials. Use local simulated effect receipts rather than production services. This targets the class of duplicate ownership and incomplete end-to-end coverage Tessl reports, without copying its infrastructure.

### 6 Measure effort through accepted and delivered work

**Owner:** Coordinator and measurement Reviewer. **Priority:** start observation early.

Extend the existing scorecard inputs with evidence for intake-to-verified-delivery elapsed time, active implementation effort, review effort, correction rounds, failed attempts, handoff repair and recurring defects. Keep these quantities separate; overlapping agent time must not be summed as elapsed time. Report per task class and configuration, with denominators and missing coverage.

Tessl’s results documentation distinguishes mean and standard deviation, shows incomplete repeat counts, and treats unavailable activation as unmeasured. Its visual noise threshold is not agent-org’s required 95% paired benefit interval. [Reading evaluation results](https://docs.tessl.io/improving-your-skills/reading-evaluation-results).

**Benefit hypothesis:** choosing improvements by total completion burden will avoid optimizing fast drafting that creates slow review. Preserve [existing scorecards](../factory/metrics/DEFINITIONS.md), cost unknowns and production DORA definitions. Do not use PR count, generated lines or factory adoption as the success objective. Any changed evaluator requires separate prior-evaluator review and dual-version replay.

### 7 Supply the same scoped standard to creation and review

**Owner:** Chief of Staff, with relevant subject expert. **Priority:** medium.

Use one versioned source of a standard for implementation, review and maintenance; specialize its application by task. Build examples by comparing several rejected artifacts with their accepted corrections. Extract what recurs and preserve exceptions. This can apply to research quality, handoffs and project enrollment as well as software.

Tessl’s design account describes deriving explicit rules from three before-and-after screen pairs, then using shared guidance at creation and review. It also describes whole-surface sweeps catching drift outside new diffs. [Design context](https://tessl.io/blog/what-your-design-system-cant-teach-ai-agents).

**Evaluation:** test on held-out artifact types and explicit exception cases. Reviewer independence remains a fresh execution, even when implementer and reviewer use the same standard. Agreement is not sufficient if the shared source is wrong. Avoid a new specialist role until repeated demand establishes a distinct capability gap.

### 8 Add bounded drift sweeps

**Owner:** Coordinator and Researcher. **Priority:** medium, after checks are trustworthy.

During authorized active-session maintenance, inspect a declared subset of agent-org for stale links, superseded guidance, accepted claims missing delivery evidence and checks linked to old requirements. Begin with deterministic discovery and advisory findings. Report examined and excluded paths; zero discovered files cannot count as a clean audit.

Proposed output: dated findings under `agent-org/factory/reports/`, linking canonical records rather than rewriting history. **Evaluation:** seed stale and valid references in fixtures and verify the sweep catches the former while preserving the latter. Measure actionable findings and repair effort. Project sweeps require separately scoped authority. No new background scheduler is needed.

### 9 Make context provenance useful for invalidation

**Owner:** Architect and Coordinator. **Priority:** medium.

Add dependency links from a standard to its examples, scenarios, verifiers and affected workflow manifests. When its authoritative requirement changes, identify which checks and context need review. Record source trust: approved instruction, accepted example, historical evidence, or untrusted external material.

The first implementation can be a small Markdown mapping and deterministic broken-reference check, not a knowledge graph service. Existing [context management](../shared/CONTEXT_MANAGEMENT.md) already requires source identities and impact review; this proposal makes those dependencies easier to find. **Evaluation:** mutate a pinned source in a fixture, detect its dependents, and verify a stale example cannot silently outrank current policy. Include both accidental bad examples and malicious retrieved instructions.

Tessl documents inventorying skills and configurations across connected repositories and treating third-party skill installation as a governed supply-chain action. Borrow the provenance discipline; registry scores do not grant local authority or prove behavioral safety. [Context inventory](https://docs.tessl.io/use/understand-your-skill-estate), [skill security](https://docs.tessl.io/tutorials/protecting-against-insecure-skills).

### 10 Reduce preparation overhead before reducing controls

**Owner:** Chief of Staff. **Priority:** evaluate after baseline measurements.

Generate task-owned record scaffolding, validated manifests and evidence summaries from canonical inputs where that is deterministic and worthwhile. Keep substantive judgment, independent review and approval intact. Measure how much time is spent preparing records before claiming bureaucracy is the bottleneck.

Tessl’s risk-dependent approach can inform review depth, but agent-org’s current rules still require independent review, distinct approval and PR delivery for content. A lower-risk path could use smaller context and narrower checks while retaining those obligations. Any proposed policy relaxation is a separate governance candidate. **Evaluation:** compare preparation and correction effort, missing obligations, and recovery success; shorter documents alone are not a win.

## Recommended first experiment

Test only task-specific context manifest preparation and loading. Do not combine it with a model change, new judge or weaker approval process.

1. **Preregister:** Chief of Staff admits a bounded hypothesis under [WF-000004](../workflows/WF-000004.md). Pin current instructions, candidate manifest generator, workload, evaluator, budget and rollback before results.
2. **Workload:** prepare at least 20 representative paired cases covering research, scoped document work, dependency decisions, recovery and review preparation. Include stale paths and misleading historical records. Reset task state between variants and randomize ordering. Both variants receive mandatory authority and startup context.
3. **Primary endpoint:** predeclare a reproducible measure of active effort through accepted output, including preparation, correction and review. Observe remote-delivery outcomes separately on authorized live tasks. If effort cannot be measured credibly, report inconclusive rather than substitute a favorable token proxy.
4. **Guardrails:** no authority or evidence failure, no required-test regression, no degraded correctness; preserve rejected and missing observations. Track unnecessary reads and stale-path retries as diagnostic measures, not replacement success criteria.
5. **Decision:** retain the existing requirement of a positive 95% paired benefit interval and at least 5% practical relative efficiency improvement. Twenty pairs are the minimum, not a promise of adequate power. If the preregistered workload exceeds the shared 60-minute budget, checkpoint and replan before running; do not lower sample requirements or reset cumulative consumption.
6. **Promotion:** fresh Reviewer examines the pinned candidate; separate Chief of Staff approves only supported benefit; Coordinator completes PR checks, merge and remote-main verification. Otherwise retain the candidate as inconclusive or rejected. Roll back through the established corrective PR process.

After this experiment, investigate the correction queue and one well-calibrated check. Observe whether a lesson improves later work before extending it across task classes. Model comparisons should hold context and judge fixed, preserve actual metadata gaps and use the same quality floor. Tessl’s example model results do not select a winning model for this organization.

## Practices to leave out of the initial adoption

An agent fleet, autonomous weekend execution, hosted schedules, a new runtime, a Tessl subscription or repository upload would add scope and operational obligations before the local benefit is known. This report proposes none of those actions. The existing session lifecycle explicitly limits post-session execution claims.

Do not replace independent review with a generic model judgment, copy throughput targets, or rewrite the organization from a test suite to demonstrate completeness. A reconstruction exercise can expose test gaps, but a successful rebuild still cannot prove that the suite captures all intended behavior. Preserve domain boundaries and evaluate the final workflow consumers.

## Research evidence and limits

The research uses Tessl’s public product pages, dated practitioner articles, public podcast write-ups and current technical documentation, plus StrongDM’s primary account solely to distinguish the factories. Podcast claims above come from the published pages; the audio and complete verbatim transcripts were not independently analyzed. Sources were accessed on the research date. Technical documentation is evolving: current plugin and variant documentation takes precedence over older tile-based examples for current product descriptions.

Public accounts explain mechanisms and failures but do not provide the raw task distributions, audited costs, incident denominators or controlled comparisons needed to forecast agent-org’s savings. The local comparison is grounded in the linked canonical files and existing tests. No Tessl CLI, hosted eval, integration, skill installation or new provider was used. The output is a research deliverable; all ten operating changes remain proposals pending their own evidence-qualified adoption.
