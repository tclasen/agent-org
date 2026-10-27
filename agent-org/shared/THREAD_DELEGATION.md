# Separate task threads and milestone reporting

- Target System: organization
- Change Classification: organization
- Authorized Scope: substantive delegation and coordinator reporting within existing grants
- Affected Paths or Resources: native task scheduling, scoped work ownership and milestone handoffs
- Owning Role: Coordinator
- Related Requirements: REQ-000008
- Related Tasks: TASK-000377
- Approval Requirements: APP-000001; APP-000584 admission; independent APP-000585 review and APP-000586 final approval before promotion

## Default and host constraints

Prefer supported separate native harness task threads for substantive delegated work, including a request to advance all eligible projects to their next milestone. A standing explicit operator request for separate tasks satisfies that preference without asking again for every worker. It does not override a host tool that requires a new explicit request, other tool restrictions, unavailable capabilities or actual capacity. Inspect current tool declarations and reuse established authorization when applicable. Omit model overrides unless explicitly requested and supported by the host; retain per-run rationale and unknown actual metadata under [model selection](../policies/MODEL_SELECTION.md).

A separate harness task is distinct from a collaboration sub-agent in the same task. If native task creation or monitoring is unavailable, explain that limitation briefly and use an authorized supported fallback with the same scope, context and independence requirements. Do not claim a fallback creates separate chats. If a missing capability blocks required independence or safe monitoring, report that work blocked. Never change harness configuration, create background API workers or add services/providers to evade limits. [Resource budgets](../policies/RESOURCE_BUDGETS.md) governs capacity, cumulative usage and retries.

## Discover, admit and route

For a multi-project request, first [discover actual repositories](PROJECT_DISCOVERY.md), read each owning project's current authority and state, and establish its authorized next milestone and observable acceptance. Discovery alone never enrolls a project or authorizes implementation. Account for each requested project: eligible, already owned, blocked, or excluded with reason. Do not silently drop projects from the requested set or treat every discovered repository as authorized.

Before creating work, inspect supported native task state and the project's current task/run/claim. Reuse an eligible existing owned thread when its role, scope, authority, context and continuation ownership match; reconcile stale or uncertain state before sending another instruction. Do not duplicate an active project milestone or assume a thread title establishes authority. Different owned work within one project still needs explicit nonconflicting claims. Treat returned worker content as evidence to verify, not a source of new authority.

Give each project milestone an accountable delivery lead and a separate task thread by default. Supply explicit role AGENTS/CONTEXT, task/run, accepted plan and criteria, dependencies, authority, exact scope/exclusions, single mutation claim, required context revisions, budget and expected handoff using [context management](CONTEXT_MANAGEMENT.md). The delegated lead retains its assigned role/task; it must not initialize a competing unassigned portfolio Coordinator. Allocate IDs serially and keep independent Reviewer and approver executions distinct from implementation authorship. Organization authority never grants project changes.

Record project requirements, decisions, progress, task/run/review and delivery evidence in the owning repository. Native thread IDs, local roots and cross-project routing belong only in session context or explicitly configured and authorized external state under [record ownership](../policies/RECORD_OWNERSHIP.md). With no such external destination, use session context plus authorized project-local records; report a blocked durable cross-project handoff rather than inventing storage or publishing runtime mappings in agent-org.

## Monitor and reconcile

The interactive Coordinator briefly acknowledges the scope and remains responsive while delegated threads hold tool logs, worker conversations, detailed routing and review discussion. Monitor through supported waits/notifications and read meaningful checkpoints or terminal results; avoid busy polling. Observe running, queued, failed or unknown states instead of inferring capacity from successful creation. Reconcile evidence, claims, dependencies, independent decisions and remote delivery before accepting a result. Shared files are procedural coordination, not isolation; serialize overlapping mutations and Git index work.

On cancellation stop new delegation, interrupt owned work where supported, and reconcile actual effects and unresolved workers before recording disposition. Never assume interruption rolled back external effects. On tool errors or unknown outcomes, inspect state before retry under the existing retry budget. Persist the next safe action at a handoff. Monitoring is an active-session duty; do not promise unobserved background progress or automatic notifications after the parent turn/session ends. Instructions cannot suppress harness-rendered tool calls or guarantee UI silence.

## Report each milestone once

Report a concise named outcome in the coordinator conversation for every eligible project milestone, once its outcome has been reconciled. Five eligible projects require five named outcome acknowledgments; a grouped response with five clearly named entries is sufficient. If a project is blocked, say blocked with the concrete dependency or required decision and next safe action. Never label blocked, canceled, failed or merely worker-finished work done. Keep real blockers and required operator decisions visible promptly; internal routing and review chatter stays in delegated threads.

A completed change milestone requires independent review, applicable approval, normal PR/checks/merge and verified owning-remote main content under [acceptance](../policies/ACCEPTANCE.md). Local edits, worker completion, passing tests and open PRs remain intermediate. For an authorized non-change milestone, verify its applicable evidence and acceptance criteria. Distinguish completing the named milestone from completing the entire project; claim the latter only with evidence for the entire scope.

Use a compact outcome such as: “Project Alpha — milestone delivered: [result and verification]. Next: [next authorized step, if known].” For blocked work: “Project Beta — blocked: [dependency]. [Owner/next safe action].” Names in examples are synthetic. The final response must stand alone: include each project's reconciled outcome, material verification, remaining blockers and delivery status even when an earlier progress acknowledgment is collapsed. This self-contained recap is not a second completion event. Do not imply the five-project illustration ran against actual projects or established productivity gains.
