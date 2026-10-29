# Record ownership

- Target System: organization
- Change Classification: organization
- Authorized Scope: organization record storage and routing rules
- Affected Paths or Resources: organization governance and links to separately owned records
- Owning Role: Chief of Staff
- Related Requirements: REQ-000056
- Related Tasks: TASK-000151, TASK-000157
- Approval Requirements: APP-000109 user instruction; independent review and Chief of Staff decision before promotion

## Reusable organization, project knowledge and runtime state

The reusable agent-org repository contains generic governance, capability definitions, procedures, templates and sanitized organization qualification evidence. It must be useful without knowing an operator, installation or portfolio. Do not store managed-project names, repository URLs, project IDs, decision content, asset choices, routing links, opaque forwarding pointers, current/former project rosters, local absolute roots, usernames, hostnames, machine configuration or workspace inventories here. This supersedes the earlier exception permitting minimal project identity/routing pointers, including instructions elsewhere that still mention that exception. Organization-only allocation reservations may retain counters without mapping them to projects or installations.

Store each project's specifications, instructions, enrollment/authority, decisions, selected and rejected examples, assets, task/run/approval history, progress, tests and evidence in that project's own repository under its authority. Use repository-relative links and portable instructions. That repository must explain its purpose, accepted requirements, decisions, current state and verification to another agent system without needing agent-org history, private conversation or an external routing record. Follow existing project documentation conventions; expose the canonical documentation entrypoint from its README or applicable instructions. Organization review cannot confer product acceptance or authorize missing project writes.

Discover local roots, remotes, current assignments, worktrees and tool/environment configuration from the active session and authorized project sources. Keep installation-specific coordination, cross-repository mappings, native execution traces and recovery manifests in operator-controlled local state outside the reusable repository, if such a durable location is explicitly configured and authorized. Do not invent one, commit it, or use agent-org as fallback storage. With no external state location, use transient session context and project-local records within authority; report any blocked durable cross-project handoff. Shared counters do not require a public portfolio map. Parent coordination may refer to its private runtime mapping; its sanitized organization child must stand alone without identifying another repository.

## Learn the method; retain decisions with their project

When a correction concerns how a capability works across projects, update its generic operating instructions during the authorized task. For example, visual preference elicitation belongs in Design Director instructions; a selected palette, aesthetic, camera, interface or other product choice belongs only to the project. A personal or installation-specific preference that cannot be generalized belongs in authorized external operator context, not in the reusable organization. Mixed feedback requires separate destinations; a project decision never silently becomes a universal rule.

Before persisting a reusable lesson, extract the general trigger, actionable method, sanitized supporting observation, verification and limits. Remove project/owner identity, local paths, product choices, source links and opaque identifiers that could reconnect the lesson to private work. Use abstract or clearly synthetic examples. A useful lesson need not reproduce the conversation, project exercise or original evidence payload. Keep raw evidence and its provenance with its owner; independent reviewers may inspect it only under applicable authority and must return a sanitized organization finding. Do not claim sanitization guarantees anonymity or that a policy guarantees behavior.

## Publication and legacy migration

Before persistence, review the full payload for ownership and portability; before publication review changed content, deletions, attachments, fixtures, logs, manifests, filenames and newly introduced Git ancestry. A clean-looking final tree does not sanitize unpublished ancestors. Build a filtered candidate from already-public main when necessary; preserve unrelated work. Publish organization-only content through existing independent review/approval, PR and verified main delivery. Product content uses its owning repository and authority. No new destination, provider or publication grant is implied.

Existing historical records are legacy evidence, not a permitted destination for new project/runtime state, a current inventory or an authority source for resuming a project. A reported historical leak requires an explicitly scoped, evidence-preserving migration: inventory affected content privately, identify its owner, preserve unique source/provenance with authorized project or external local storage, verify hashes and recovery before removing or sanitizing tracked copies, reconcile dependent links and approvals, and independently review content and introduced ancestry. Report remaining coverage and blockers. Do not silently delete unique evidence, rewrite public history, force-push, or claim historical cleanup from an instruction change. Prior immutable-retention guidance does not require retaining identifying payloads in the reusable current tree once their verified migration is authorized; public history remains unchanged absent separate explicit authority.

## Project retirement and reusable lessons

When management ends, retain project knowledge in its owning repository and only sanitized reusable methods here. Do not maintain current, retired, excluded or tombstone project profiles. Discovery does not enroll or reactivate a repository. Load legacy evidence only for an authorized, concrete provenance/recovery question; ordinary startup and status reporting use live authorized sources. The [reusable lessons reference](../shared/LEGACY_LEARNINGS.md) is available for applicable general precedents, not a portfolio index.
