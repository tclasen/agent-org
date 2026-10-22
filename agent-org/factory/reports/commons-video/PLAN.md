# Commons milestone video requirement — plan revision 1

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: this plan only for Planner; execution limited to TASK-000080 Commons documentation and TASK-000081 bounded enrollment/governance under APP-000022; no runtime changes, recording, spending or deployment
- Affected Paths or Resources: agent-org/factory/reports/commons-video/PLAN.md; proposed execution paths and normal separate PR delivery are enumerated below
- Owning Role: Planner
- Related Requirements: REQ-000053
- Related Tasks: TASK-000079, TASK-000084
- Approval Requirements: APP-000022; independent review, distinct Chief of Staff organization approval and normal PR delivery

- Task/Run/role: TASK-000084 / RUN-000078 / Planner; parent TASK-000079.
- Target/classification: cross_boundary; authority APP-000022. This plan does not enlarge that grant.
- Intended outcome: make cumulative, current-build video evidence a completion gate for future Commons product milestones, adapted to its deterministic headless CLI and offline archive viewer.
- Planning writer scope: this file only. Coordinator owns implementation and delivery; independent Reviewer and Chief of Staff own review and organization approval respectively.

## Scope and sources

Project child TASK-000080 may edit only `/Users/Shared/commons/AGENTS.md`, `README.md`, and `docs/implementation-plan.md`, delivered through the Commons owning remote and a separate PR. Organization child TASK-000081 may add the bounded `agent-org/knowledge/projects/commons/PROFILE.md`, update `agent-org/knowledge/projects/INDEX.md`, and maintain only task-owned admission, review, approval, run and delivery records. Coordinator reconciled the task's shortened `projects/INDEX.md` reference as relative to the knowledge prefix; this is the canonical registry, not an additional scope. This report resides in the isolated organization checkout `/Users/Shared/commons-video-org/`.

No additional operator authority is needed: the direct request authorizes these product documentation edits, APP-000022 binds that request and the necessary bounded organization records, and standing delivery authority covers their separate normal PRs. The plan preserves the grant's exclusions and required independent gates.

Authoritative inputs: Commons AGENTS.md, README.md, tools/viewer/README.md and implementation-plan completion evidence; sibling every_game/AGENTS.md “Demo video delivery”, semantic_search/docs/process/verification.md “Milestone Playwright recording”, and wired_to_survive/AGENTS.md deterministic capture policy. Adopt cumulative coverage, provenance, honest presentation and media integrity; adapt capture to real CLI output and actual offline viewer playback. The viewer does not recompute BLAKE3 hashes, so footage must not be represented as archive-integrity proof.

No runtime/source/tooling changes, new recording, cargo tests, paid inference, deployment, hosting, public release, unrelated project edits, or historical milestone-evidence rewrites are part of this documentation delivery. Do not import Bevy, Playwright or provider execution as Commons requirements.

## Executable steps and acceptance

1. Coordinator reconciles clean Commons baseline and organization claims, confirms bounded project admission under APP-000022, and preserves unrelated work. Record enrollment limited to this documentation request; no standing runtime authority.
2. In Commons AGENTS.md establish the canonical video contract; link it concisely from README and the implementation-plan completion section. Preserve the existing milestones 1–11 historical validation statement and make the new gate prospective for product feature/behavior milestone delivery. Documentation and housekeeping are exempt, including this task.
3. Require a pre-recording feature/acceptance checklist spanning the current and every preceding implemented milestone, actual final current-build CLI/viewer footage, observable success and relevant failure/recovery behavior. Map each criterion to video/part timestamps, observed outcomes and supporting nonvisual evidence; explicitly identify criteria whose proof requires deterministic checks rather than pictures.
4. Require source revision/tree, exact commands/build/dependency and environment identities, seed/configuration, archive and viewer-export provenance/digests, relevant logical tick/event sequence ranges, output locations and material limitations. Use existing verified archives when appropriate; label their original source/run and compatibility with the current viewer instead of presenting them as newly generated current-build simulation evidence. Do not require paid inference merely to record a demo.
5. Require readable captions showing scenario/criterion, expected and observed results; identify automation, cuts, separate sessions, replay/exported history and offscreen capture. Do not present narration, static claims or historical footage as proof of current behavior. Adopt the sibling-template stable latest-video convention intentionally for Commons: validate the new movie before replacing `artifacts/demonstration.mp4`, with its timestamp/provenance index. Ordered parts may supplement the watchable latest movie when necessary. Retain raw provenance and reproducible evidence; impose no ban on retaining older movies. Provide clickable local delivery links. Generated/private evidence stays out of Git; this policy does not authorize publication.
6. Require probe and full decode, representative encoded-frame/playback inspection, and reconciliation of the timestamp checklist before product milestone completion. Existing deterministic regression, archive verification/re-execution and milestone acceptance checks remain required where applicable; video supplements them. Missing, failed, misleading or unreadable required evidence blocks the affected milestone. This documentation change claims no recording or new product validation.
7. Independently review the frozen Commons candidate and organization candidate, obtain distinct Chief of Staff approval for organization changes, then deliver through separate normal PRs. Observe required checks, merge without bypass, fetch each owning remote main and verify approved content/ancestry before declaring delivery. Coordinator records exact heads, PRs, checks and remaining limitations.

Acceptance verifier: independent Reviewer checks steps 2–6 against all three Commons documents and the sources; Chief of Staff verifies bounded enrollment/administrative authority and organization scope. Coordinator verifies step 7 against remote evidence. Scope or authority changes require impact review and an updated plan/approval rather than silent expansion.

## Verification, budget and rollback

For this docs-only change run scoped diff/whitespace checks, inspect links and criterion coverage, check the three documents agree, verify historical claims are untouched, and inspect changed-file inventories plus required repository/organization CI. Use applicable organization structural checks for its records. Do not run cargo tests or create a video to validate policy prose. Record commands/results and candidly distinguish policy requirements from evidence actually produced.

Cumulative budget: 60 active minutes for the parent request, at most two diagnosed retries; no spending or deployment. Current Coordinator implementation plus fresh Planner (requested gpt-6.1-sol/medium), Reviewer (high) and Chief of Staff (medium) provide bounded planning, independent review and approval; actual native model/reasoning and monetary cost remain unknown unless observed. Stop dependent action on exhausted budget, unresolved authority or failed required checks and hand off precise blockers.

Risks: cumulative footage can be long; allow ordered readable parts with complete indexing. Headless checks may not have meaningful visuals; map them to honest machine evidence. Archive footage can be mistaken for a live simulation; provenance and labels resolve that distinction. Organization/project deliveries must not be conflated.

Rollback: before delivery, revert only task-owned edits while preserving unrelated work. After delivery, use scoped corrective/revert PRs in each affected owning repository with the same review/protection requirements; update task evidence to record the result. Never delete or falsify historical validation or captured evidence to manufacture compliance.
