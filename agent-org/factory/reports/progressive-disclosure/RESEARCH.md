# Progressive disclosure research and design rationale

- Target System: organization
- Change Classification: organization
- Authorized Scope: agent-org guidance and separately scoped root startup bridge
- Affected Paths or Resources: agent-org guidance and root AGENTS.md
- Owning Role: Coordinator
- Related Requirements: REQ-000001, REQ-000008, REQ-000034
- Related Tasks: TASK-000057, TASK-000058, TASK-000059
- Approval Requirements: APP-000001, APP-000008; independent review and promotion approval

Research observed 2026-10-22 UTC. Sources below were opened online, not inferred from search snippets. Vendor guidance describes design practice; UX findings concern human navigation; preprints have bounded empirical settings. Applying these to this organization is an explicit design inference. No source establishes a productivity gain for this repository.

## Evidence and application

| Primary source | Finding (paraphrased) | Application here and limit |
| --- | --- | --- |
| [Nielsen, Progressive Disclosure, 2006](https://www.nngroup.com/articles/progressive-disclosure/) | Put frequent essentials first; defer specialized options; make navigation obvious and labels predictive. | Keep authority, scope and effect gates visible. Give each deferred document an action trigger. Human UX findings motivate design, not an LLM performance guarantee. |
| [Budiu, Information Scent, 2020](https://www.nngroup.com/articles/information-scent/) | Labels and nearby context let a reader estimate a destination's relevance and effort. | Replace bare filenames with “before delegation”, “when recovering”, and similar cues. Plain domain terms support search. |
| [Anthropic, Effective context engineering, 2025](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Treat context as limited; retain useful references and retrieve details as needed. Exploration has latency and navigation risks. | Allow direct reads when a path is known; small core plus targeted search; avoid context dumps and unnecessary routing hops. Measure accessible content rather than claiming latency gains. |
| [Anthropic, Equipping agents with Agent Skills, 2025](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) | Discover compact metadata first, activate relevant instructions, and load supporting files selectively. Executable helpers can avoid reading large data. | Separate universal rules, role/task instructions and evidence. Adapt the pattern to Markdown organization guidance; no new skill loader or harness. |
| [Agent Skills specification](https://agentskills.io/specification) | Metadata, activated instructions and optional resources form three levels. References should be shallow and focused. | Direct links to canonical documents; do not force agents through a chain of indexes. Skill size recommendations are not universal organization limits. |
| [Agent Skills authoring best practices](https://agentskills.io/skill-creation/best-practices) | Include information the agent lacks, use coherent task units, specify when a reference applies, and inspect real execution traces. Moderate detail and clear defaults reduce distraction. | Remove repeated onboarding and mandatory rereading cycles; role CONTEXT contains stable role orientation. Keep fragile permission/review sequences explicit. |
| [OpenAI, Harness engineering, 2026](https://openai.com/index/harness-engineering/) | A compact AGENTS.md can guide agents toward a versioned knowledge base; monolithic instructions crowd context and drift. Links and freshness benefit from checks. | Root bridge activates one canonical entrypoint. Organization guide offers task routes. Keep provenance and use existing validators/regression checks. Their experience is not a general benchmark. |
| [OpenAI, Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) | AGENTS.md participates in instruction discovery by directory and client behavior. | Preserve the operator-approved root bridge; avoid adding AGENTS.md inside evidence/archive trees. Do not claim links are automatically lazy-loaded or that clients load every file. |
| [Cochran, preregistered wiki ablation, v2, 2026](https://arxiv.org/abs/2607.04576v2) | Study uses a 709-page corpus and identical page bodies; capable agents sometimes navigate directly. Judge/human agreement and forced-catalog quality limit conclusions. | Permit skipping catalogs when the target is known. Do not mandate an extra index for every action or claim universal quality preservation. Preprint, corpus/model specific. |
| [He et al., long-context agents study, 2026](https://arxiv.org/abs/2607.17598v1) | Benefit varies with harness and corpus scale; additional routing depth sometimes damages accuracy in their experiments. | Prefer a shallow map and direct destination links. Maximum useful disclosure does not mean maximum hierarchy. Preprint, document-QA setting. |

## Organization audit

Baseline ca6ff20 requires eight documents in the root bridge. Organization instructions repeat policy, model, approval and delivery details; each role repeats common rules and its CONTEXT points back to lifecycle, authority and AGENTS. README adds workflow reads. tasks/INDEX.md grows with every completed task. shared/HANDOFFS.md mixes schema with historical logs. These create unnecessary mandatory context and recursive reading invitations.

Keep authority/scope canonical and initially available. Keep classification, project separation, old/ and harness exclusions, PR/review/approval, verified remote-main completion, honest telemetry and no blind side-effect retry explicit. Defer full procedures until before their action, with links that state the trigger. Agents still inspect local Git state and current task/run summaries at startup; they open conflicting, pending or affected records, not every historical record. If summaries are missing/stale, search canonical records and actual state; do not invent certainty.

## Chosen design

1. Root bridge loads agent-org/AGENTS.md; the latter defines the bounded startup contract and direct action routes.
2. Authority and scope remain mandatory. Initialize only the assigned role; unassigned interactive sessions use Coordinator. Role CONTEXT provides unique orientation, not repeated startup instructions.
3. Coordinator uses targeted discovery of nonterminal tasks/runs and Git/native effects. Delegated workers reconcile their task/run/claim and affected resources; they do not initialize another Coordinator.
4. One conditional map covers admission/delegation, implementation, review/delivery, organization improvement, enrollment, recovery, metrics, evidence and historical sources. A link does not require a read unless its trigger applies.
5. Task manifests separate required-for-this-run sources from optional discovery pointers, with relevance and refresh conditions. Required authority is never optional or inferred from a summary.
6. Keep existing policy/evaluator bodies and historical evidence unchanged. Validate mandatory reading paths, direct links, scope and regressions; report document-size savings only as deterministic structural evidence.

Rejected: a new comprehensive manual, forced catalog-first traversal, a generated index requiring a background service, blindly loading all role contexts/tasks/handoffs, deleting history, or hiding permission gates to minimize words. More files and a lower word count alone do not prove effective disclosure.

## Verification limits

Acceptance is a requested deterministic instruction/navigation correction, not an autonomous stochastic efficiency promotion. Existing SELF_IMPROVEMENT statistical rules remain unchanged for any future productivity claim. Independent review must verify this distinction, retained gates, negative routes (no irrelevant enrollment/metrics/history for a bounded writing task), and root integration separately. Live behavior may reveal further refinements; no universal obedience, automatic lazy loading, cost, latency or token reduction is asserted.
