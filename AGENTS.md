# Agent organization entrypoint

Activate the organization in `agent-org/` for sessions started in this directory. Resolve the paths below relative to this file's directory (the Git repository root), not the shell's later working directory. Do not require the operator to change into `agent-org/` or provide a separate activation prompt.

Before substantive work, read:

1. `agent-org/AGENTS.md`
2. `agent-org/policies/AUTHORITY.md` and `agent-org/policies/SCOPE_BOUNDARIES.md`
3. `agent-org/shared/SESSION_LIFECYCLE.md`
4. `agent-org/agents/INDEX.md` and `agent-org/tasks/INDEX.md`

For an unassigned interactive session, initialize the Coordinator by reading `agent-org/agents/coordinator/AGENTS.md` and `agent-org/agents/coordinator/CONTEXT.md`. Reconcile open tasks, interrupted runs, claims, Git state and known external effects before proceeding with the user's request. A worker already delegated a role must load that role's instructions/context and its task/run instead; this entrypoint does not turn specialists into Coordinators or start duplicate work.

The canonical organization instructions, governance and durable state remain in `agent-org/`. Resolve paths inside those instructions relative to their containing files. Follow applicable project instructions and overrides within separately authorized project scope; loading this entrypoint grants no project write authority. If required organization files are unavailable, report the startup blocker rather than inventing an organization or continuing without its instructions.
