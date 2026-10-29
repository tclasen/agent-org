# Design review and bounded drift review

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org/shared/DESIGN_REVIEW.md
- Affected Paths or Resources: agent-org/shared/DESIGN_REVIEW.md
- Owning Role: Chief of Staff
- Related Requirements: REQ-000059
- Related Tasks: TASK-000243
- Approval Requirements: operator incorporation request; APP-000448; independent exact-candidate review and Chief of Staff approval before normal PR/main delivery

This is the canonical procedure for the incorporated EGM practices. Planner/Architect prepares the brief, a fresh Reviewer assesses it, and Coordinator reconciles readiness under existing grants and dependencies. The [research assessment](../knowledge/EGM_RESEARCH.md) records the source and tradeoffs. Existing [authority](../policies/AUTHORITY.md), [acceptance](../policies/ACCEPTANCE.md) and [improvement evidence rules](../policies/SELF_IMPROVEMENT.md) govern this procedure; its checklist cannot approve its own adoption or replace final review.

## When to use it

Before implementation, apply design review to a material architecture decision, new or materially changed interface, migration/compatibility change, or another costly-to-reverse change. Coordinator records the trigger and links the brief and review from the admitted task. A routine correction with no such effect uses the existing plan and a short non-trigger reason; a typo does not need a design document. If scope changes materially, reassess the trigger and affected approval.

Use bounded drift review when an admitted change affects behavior described by an approved specification, or a discrepancy is reported. Pin the relevant document and source set in the task before scanning. This is a scoped task action, not a recurring schedule or whole-repository sweep. Work already pending under a plan must not be mislabeled a regression merely because it is unfinished.

Organization artifacts stay in agent-org. Product briefs, source maps and findings stay in their owning repository under its actual authority, with no project pointers retained here; use session/project sources for routing. Never create a project grant through a brief or a drift finding. Component-contract generation is not part of this procedure; admit it separately only if repeated context gaps justify it.

## Prepare one compact brief

Planner/Architect uses the [implementation brief schema](templates/IMPLEMENTATION_BRIEF.md), or the same fields inline in the existing plan. Link canonical requirements, grants and decisions rather than copying them. Make the brief understandable without drafting history:

- State the user outcome, exclusions and observable success and failure journeys.
- Explain the chosen approach, existing components to reuse and rejected alternatives.
- Name interfaces/files, compatibility obligations, checks and rollback proportional to risk.
- Classify open questions as blocking, delegated implementation choices or deferred work; name each owner and decision source. Routine coding choices may remain delegated.

A link is sufficient only if the referenced source is accessible and current for the decision. A missing mandatory source or unresolved blocking decision prevents readiness. Preparing a brief neither allocates authority nor permits implementation.

## Dispatch a fresh reviewer

Follow [context management](CONTEXT_MANAGEMENT.md). Coordinator supplies the role/task/run, accepted criteria and applicable authority, pinned brief/target, source list and standards, with identities/hashes and reasons to read. Separate required sources from triggered references. Exclude the drafting conversation, private rationale and proposed answers the brief must explain. Load relevant sources with the existing retrieval bounds; never recursively load every linked document.

Use a native child with no inherited conversation; when the tool has `fork_turns`, explicitly choose `none`. Use the supported equivalent only when its schema establishes fresh context. Do not simulate an independent reviewer in the author session. If a fresh child is unavailable, record the review blocked; do not substitute same-thread review.

Record the actual native child identifier, requested inheritance/model parameters, required sources and their revisions, returned evidence of reading, completion and tool failures. Distinguish requested, reviewer-reported and directly observed facts. Verify available native results/traces; missing host telemetry remains unknown. Reviewer reports which required sources were read and unavailable. A known missing required read/input leaves the affected review incomplete. An unavailable full host trace does not prove a read failed, and must not be presented as verified read coverage or secure isolation. Record content-review outcomes and provenance limitations separately under existing acceptance rules.

An optional parent-only marker probe may observe whether one fresh child knows drafting history. Keep the marker out of child prompts, artifacts and shared sources until the response is captured. A response of UNKNOWN is one bounded observation, not filesystem/memory isolation or a guarantee for future sessions. Mandatory safety and authority context remains available.

## Review three distinct questions

Use the [design review schema](templates/DESIGN_REVIEW.md). One fresh Reviewer can cover these lenses; record that this is one perspective. Independent parallel perspectives, when justified, use actual runtime capacity and nonconflicting claims under RESOURCE_BUDGETS.md; there is no organization worker-count or delegation-depth ceiling. No new permanent role or synthesizer is required.

| Lens | Required question and evidence |
| --- | --- |
| Architectural fit and simplicity | Does this solve the stated problem in the appropriate component? Could existing components meet the need? Explain the smallest adequate approach and any unnecessary abstraction or speculative optimization. |
| Comprehension | Can a fresh worker restate the goal, boundaries, prerequisites and behavior from the brief and its selected sources? Flag undefined concepts, unavailable references and assumptions that depend on the author's conversation. |
| Execution readiness | Can the assigned worker identify the affected interfaces/files, compatibility/failure behavior, verification, rollback and decisions it owns? Distinguish legitimate delegated choices from unresolved architectural or authority decisions. |

Return an outcome for each lens with concrete evidence. Do not invent flaws to satisfy a persona. Absence of findings is meaningful only within the declared scope and sources.

## Keep findings and readiness traceable

Use stable task-local finding labels, such as F01, not newly allocated formal IDs. For each raw finding retain the source reviewer, target revision/hash, location, severity, evidence and rationale. Keep a mapping when findings are deduplicated or consolidated; merging duplicates never deletes their raw identities or disagreements.

The author may propose a repair or contest a finding with source evidence. Record disposition, owner, repair revision and independent recheck. A disputed material finding remains unresolved until the independent reviewer and applicable decision authority resolve it under existing grants. The author cannot approve its own repair, waive authority or silently downgrade a blocker. Minor deferred issues need an explicit reason and owner; deferral cannot violate an accepted requirement.

Recheck affected findings, source bounds and approval when the target, requirements, evaluator or environment changes. Old line numbers and a review of an earlier hash cannot qualify a changed target. Preserve original reports and failures alongside revised evidence.

Design readiness is ready, not ready, incomplete or blocked, with reasons and open findings. An unresolved blocker, mandatory evidence gap or exhausted retry/budget is never a pass or an accepted tradeoff by default. Keep retry history and return to Coordinator for the exact safe next action. A ready design still requires valid admission, satisfied dependencies and applicable approval; it is not final implementation acceptance. Existing task states and final PR/main gate are unchanged.

## Compare approved intent with bounded source

Use the [drift review schema](templates/DRIFT_REVIEW.md). Pin each document's status and authority, source revision, covered files/symbols and exclusions. Distinguish approved specifications, historical proposals and generated descriptions. A generated contract describes observations, not approved intent or correctness.

Compare actual behavior as well as names: a renamed equivalent implementation is not automatically drift. Locate evidence in both document and source. Classify each discrepancy with its reason, evidence, owner and next action:

| Classification | Interpretation |
| --- | --- |
| Implementation defect | Implemented behavior conflicts with applicable approved intent and is not an approved revision or admitted pending work. |
| Incomplete admitted work | The behavior is required but an identified authorized task/plan has not finished it; report its real state without calling it a new regression. |
| Approved design revision | A current authorized decision supersedes the older intent; preserve the decision and identify any stale links or prose. |
| Outdated documentation | Descriptive prose is stale against established current behavior; distinguish description from a still-binding specification. |
| Unresolved question | Authority, intended status, source access or equivalence is uncertain; retain the gap and named next investigation rather than guessing. |

An unimplemented historical proposal alone is not a defect. Undocumented source alone proves neither incorrectness nor authorization; route an actual authority question to Coordinator. Reading code is not running it, and this procedure does not claim deterministic AST analysis or runtime validation.

Include coverage and excluded/unreadable sources even when clean. Say no drift detected in the covered scope only when the evidence supports it; unreadable mandatory source stays unresolved. Report missing or partial observations explicitly. Recommend scoped follow-up through existing admission; never automatically rewrite code, specifications, approvals or history to make a discrepancy disappear.

## Boundaries and qualification

Keep prior grants, independence, actual runtime capacity, retry limits and exact-candidate acceptance intact. Neither exhausted review rounds nor a generated report creates acceptance. This procedure installs no plugin, service, provider or new scheduler and claims no measured efficiency or universal compliance. Future productivity or evaluator changes require their own qualification under existing prior rules. Roll back a regression through a normal corrective PR restoring known-good instructions while retaining findings and trial evidence.

## Independently establish the responsibility delta

Before the three technical lenses, the fresh Reviewer reads the original authority and determines the engineering responsibilities already included, then compares the proposed aggregate work. Use the responsibility fields in the existing brief/review. Do not inherit the implementer's claim of unchanged scope, compare only writable files/features, or assume a technically small patch is a small maintenance commitment. Explicitly consider retaining a requirement gap and supported alternatives, rather than comparing only increasingly elaborate implementations.

Record separately: (1) outcome and responsibility/authority fit, (2) architectural simplicity and correctness/readiness. State the source authorizing any material added maintenance/operational obligation, prior support assumption changed and aggregate child effects. An unsupported addition fails admission even if technically feasible; return it for a scope decision under PLANNING.md. Existing explicit ownership can make low-level work legitimate; no universal technology exclusion or routine approval queue follows. Missing source or ambiguous responsibility remains unresolved. A technical pass cannot repair the authority finding.
