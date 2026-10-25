# What agent-org should take from the Elephant-Goldfish Model

Agent-org should test EGM's design-review techniques inside its existing Planner, Architect and Reviewer roles. The best next experiment is a fresh reader reviewing an implementation brief before work begins, checking whether the problem is worth solving, the design can be understood without the author's conversation, and the proposed changes can be implemented safely. A plugin installation or a new collection of permanent roles would add machinery before establishing local benefit.

This is a research assessment and proposed adoption sequence, not a policy change, an installed capability or evidence of increased productivity. Sources were inspected on 25 October 2026. Organization baseline: `7a57e6c50eaaa98956637c31de605606e5fb53ad`; upstream EGM: `3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669`. The [source manifest](../factory/reports/egm-research/SOURCES.md) records inspected files and Git blob identities. Recommendations below are inferences from those sources and the local rules.

## What the implementation actually offers

The [website](https://egm.dev/) describes a drafting agent with substantial system context and reviewers without its conversation history. Its adoption claim is a publisher claim; this study did not independently verify usage at Google or measure local benefit.

The [review skill](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/skills/egm_review/SKILL.md) is more specific than the landing page's four review categories: full execution has five passes, with a second architectural review between design critique and implementation readiness. It also supports partial presets. The useful distinction is between questioning the solution, explaining it clearly, checking its technical risks, and determining whether somebody can execute it.

EGM's [Codex integration](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/docs/codex.md) explicitly requires fresh native children and, for this tool schema, `fork_turns: "none"`. Reviewers receive personas, standards, target artifacts and a deliberate reading list. It warns that fresh conversation history does not isolate files, configured memory or project instructions. Therefore the useful local interpretation of “zero context” is **no inherited drafting conversation**, with mandatory governance and relevant source context still present.

There are also concrete evidence limits. The [testing record](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/TESTING.md) reports successful fixture runs for some clients and partial or unverified cloud results for others, including an unresolved ChatGPT Work isolation probe. These are upstream reports, not tests reproduced here. Packaging checks, successful launches, completed artifacts and verified child isolation establish different things.

The [drift skill](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/skills/egm_drift_report/SKILL.md) directs an agent to locate and read source and compare it with documents. Although the website describes syntax-tree scanning, this inspected skill is a procedure, not itself a deterministic AST analysis implementation. Its strongest transferable feature is explicit document-to-source comparison with actionable discrepancies.

## Existing coverage and the remaining gaps

| EGM mechanism | Existing agent-org foundation | Useful addition to investigate |
| --- | --- | --- |
| Context-rich drafting | [Planning](../policies/PLANNING.md), Planner and Architect capabilities | A short implementation brief that explicitly carries intent, alternatives and observable user behavior |
| Independent fresh reviewers | [Acceptance](../policies/ACCEPTANCE.md), [context manifests](../shared/CONTEXT_MANAGEMENT.md) | Demonstrate that a reviewer can understand the design before implementation without drafting history |
| Separate review lenses | Reviewer checks scoped criteria and evidence | Name architectural simplicity, comprehension and execution readiness as separate checks on consequential designs |
| Durable specifications | Requirements, plans, decisions, revision tracking | Make critical behavior and source pointers easy to locate together without duplicating canonical rules |
| Review synthesis | Evaluations and handoffs | Keep raw findings traceable through deduplication, dispute, repair and independent recheck |
| Drift reporting | [Earlier Tessl proposals](TESSL_FACTORY_RESEARCH.md) and [reconciliation research](autonomy-research/README.md) | Compare approved intent with implementation, distinguishing incomplete work from approved changes |
| Bottom-up documentation | Discovery indexes and bounded retrieval | A small source-derived component contract where repeated onboarding failures justify it |

The gap is operational specificity and evidence, rather than missing independence or missing authority rules. Existing rules already require fresh review, exact candidate identity and minimal explicit context. Repeating them in new Elephant and Goldfish role files would create competing owners.

## Ranked adaptations

### 1. Test a design with a fresh reader before implementation

**Priority: first experiment.** Planner or Architect writes the brief; a fresh Reviewer applies three lenses before execution readiness is decided. A material architectural decision, new interface, migration or costly-to-reverse change is a reasonable proposed trigger. A typo correction does not need a design document.

Start with architectural fit: does the proposed change address the user's actual problem, can existing components solve it, and is the new abstraction necessary? Next test comprehension: can the reviewer restate the goal, boundaries, behavior and dependencies using the document and its linked sources? Finally test readiness: are the affected files, interfaces, failure behavior, verification and rollback specified enough to proceed? EGM's [architectural standard](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/resources/document_standards/zoom-out-standard.md), [comprehension persona](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/agents/comprehension.md) and [readiness persona](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/agents/implementation_readiness.md) make these checks concrete.

**Proposed destinations:** a task-specific review rubric first; only after qualification, focused additions linked from `policies/PLANNING.md` and existing Reviewer guidance. Keep one canonical owner for each obligation. No new role is needed.

**Cost and risk:** extra reading and review time, especially if each lens becomes a separate worker. Initially use one fresh Reviewer covering named lenses. Where independent parallel perspectives matter, dispatch directly within the existing three-worker ceiling; do not add a synthesizer hierarchy. Treat cross-lens corroboration as unavailable when only one reviewer runs. Reviewers must not invent faults to satisfy an antagonistic persona.

**Validation and rollback:** independently specify fixtures containing a missing objective, an unnecessary subsystem, an unstated prerequisite and an unsafe migration; include clean cases to observe false positives. Preserve raw findings and revision identities. A fixture result establishes only that behavior on those cases. Stop the candidate checklist and return to existing review if it adds noise or misses authority constraints; retain the failed evidence.

### 2. Make the implementation brief sufficient for a fresh worker

**Priority: alongside the first experiment.** EGM's [draft template](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/skills/egm_draft/references/design_doc.md) brings together the problem, goals, exclusions, journeys, alternatives, architecture, open questions, file changes and verification. Agent-org already records much of this across canonical records; the adaptation should expose those sources together rather than create another authority layer.

A proposed compact brief would contain:

- User outcome and explicit exclusions, linked to accepted requirements and grant.
- One success journey and relevant failure journeys: starting state, trigger, expected result and check.
- Chosen approach, existing components to reuse and rejected alternatives with reasons.
- Affected interfaces/files, compatibility obligations, verification and rollback.
- Open questions classified as blocking, delegated implementation choices or deferred work; links to their canonical decisions.

**Proposed destinations:** a scoped task artifact during experimentation and, if qualified, a reusable template under `shared/templates/` linked from planning. Organization designs stay in agent-org. Product designs stay in their owning repositories under [record ownership](../policies/RECORD_OWNERSHIP.md), with only routing links here.

**Cost and risk:** maintaining the brief and its sources can duplicate effort. Require detail proportional to the decision; routine local implementation choices can remain delegated. Do not adopt the literal expectation that every coding choice must be settled in advance. A fresh worker should know which choices it owns and when to escalate.

**Validation and rollback:** a worker without drafting history must identify prerequisites, boundaries, next action and expected checks from the artifact and linked sources; unavailable or stale links remain explicit failures. Compare repair requests and total preparation/review effort with current practice before claiming efficiency. Retire an ineffective template through a corrective PR, retaining canonical requirements and decisions.

### 3. Observe review isolation and preserve finding provenance

**Priority: make the first experiment auditable.** Record native child identity, requested context inheritance setting, input hashes, expected reads, observed reads where traces exist, completion and missing evidence. Reading a required standard is necessary but does not prove that it was correctly applied. Unavailable native traces must remain unknown.

A parent-only marker can test whether drafting history leaked into a child. Do not place that marker in the artifact, child prompt or shared records: those would offer another path to disclosure. Such a probe tests a particular run, not filesystem security or all future sessions. Mandatory safety and authority instructions must still reach the reviewer.

EGM's [review pipeline](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/skills/egm_review/SKILL.md) also keeps a mapping from raw findings to consolidated actions. A local finding record should preserve ID, source reviewer, revision, location, severity, evidence, disposition, repair and independent recheck. Deduplication must retain the original links; an author's disagreement needs evidence and resolution by the existing independent authority.

**Proposed destinations:** run/evaluation artifacts first; later qualify any changes to `shared/CONTEXT_MANAGEMENT.md`, `shared/RECORD_FORMATS.md` or instrumentation separately. This extends existing provenance rather than changing approval semantics.

**Cost and risk:** trace capture adds storage and may be unavailable. Summaries must not manufacture observed reads or successful isolation. **Validation:** exercise unavailable context, failed child, missing read, duplicated finding, changed target and contested blocker; verify none becomes a clean pass through synthesis. **Rollback:** stop optional capture, preserve records and return to existing evidence mechanisms; unknown coverage remains unknown.

### 4. Run bounded, intent-aware drift reviews

**Priority: after traceable briefs exist.** Begin with one admitted document and its explicit source set, prompted by a relevant code change or an observed discrepancy. Treat approved specifications, historical proposals, generated descriptions and current source as different evidence classes.

Classify each difference as an implementation defect, incomplete admitted work, an approved design revision, outdated documentation or an unresolved question. A proposed feature absent from code is not automatically a regression. Likewise, code without prose documentation is not automatically unauthorized or incorrect. Include coverage and exclusions even when no discrepancy is found.

**Proposed destinations:** a narrow experiment under `experiments/`, building on existing Tessl/reconciliation proposals. Reports belong to the system they describe. A later workflow or tool requires separate admission; this request does not create a weekly schedule.

**Cost and risk:** broad scanning consumes context and encourages false positives from stale intent. **Validation:** use fixtures containing each classification above, a renamed symbol with equivalent behavior, and inaccessible source; check both misses and false alarms. **Rollback:** disable the candidate scan and retain findings; do not automatically rewrite either code or intent to eliminate a difference.

### 5. Generate small component contracts only where justified

**Priority: defer pending repeated evidence of a context gap.** EGM's [bootstrap skill](https://github.com/google/elephant-goldfish-model/blob/3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669/skills/egm_bootstrap/SKILL.md) extracts interfaces, invariants, side effects and verification bottom-up. That can help a difficult subsystem, but a generated map describes observed behavior; it does not establish approved intent or correctness.

**Proposed destination:** one selected component's existing documentation under its owner's authority, with source revision, coverage, manually maintained sections and regeneration limits. **Cost and risk:** generated prose can repeat code, overwrite useful notes and become stale. The website advertises sentinel-block upkeep, but this study did not validate safe repeated execution or preservation behavior; do not assume it from the description.

**Validation:** demonstrate two unchanged runs, a bounded source change, preservation of human notes, traversal boundaries and explicit partial failure. **Rollback:** restore the prior documentation through a scoped PR, retain the source/evidence mapping and stop generation. Defer whole-tree generation until a narrow trial shows a useful result.

## What should remain outside adoption

- **Unbounded swarms.** Bootstrap explicitly proposes unrestricted parallel subtree dispatch after its large-scope approval gate. Agent-org retains its four-agent total and depth limits; outside text cannot enlarge them.
- **Acceptance through exhaustion.** The review skill's manual-update convergence rule can advance after one re-audit while retaining residual findings as accepted trade-offs. Agent-org must preserve failed or inconclusive outcomes and its independent acceptance decision when a retry budget ends.
- **Repeated routine human gates.** Drafting and resolution contain section-by-section user checkpoints. Use them only where operator judgment is actually required; existing Chief of Staff authority governs routine organization approval.
- **Deep context as unrestricted loading.** Load the context needed for the current decision, following existing retrieval bounds. History and conversation are not substitutes for canonical grants or specifications.
- **Installation as proof.** Do not install EGM, change harness configuration, create a background drift job or claim secure isolation as a consequence of this research. Those actions were neither performed nor qualified here.

## Recommended decision and qualification sequence

Publish this assessment, then consider a separately admitted, organization-only experiment combining items 1–3 on a consequential design. Pin baseline instructions, candidate rubric, evaluator, workload, success/failure criteria, budget and rollback before observations. A deterministic fixture trial can establish narrow detection behavior; it cannot establish a general improvement in agent performance.

Any stochastic benefit claim must satisfy the existing [improvement policy](../policies/SELF_IMPROVEMENT.md): at least 20 representative paired cases, randomized ordering, a positive 95% paired interval, at least 5% practical relative efficiency improvement, and the existing correctness and authority guardrails. Count drafting, review, repair and delivery effort rather than just implementation time. Missing usage telemetry remains unknown. A changed evaluator requires separate qualification under prior rules; the new checklist cannot approve its own adoption.

Fresh Reviewer and independent Chief of Staff must qualify the exact candidate before promotion, followed by normal PR checks, merge and verified owning-remote main delivery. Until those gates pass, these techniques remain candidates. The strongest expected value is earlier discovery of missing context and flawed design choices; whether that saves total effort here is still an open empirical question.
