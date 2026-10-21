# Lessons retained from the retired organizations

- Target System: organization
- Change Classification: organization
- Authorized Scope: Historical learning reference in agent-org; no product or evaluator change
- Affected Paths or Resources: agent-org/shared/LEGACY_LEARNINGS.md and linked evidence
- Owning Role: Coordinator
- Related Requirements: none
- Related Tasks: TASK-000029, TASK-000031, TASK-000032, TASK-000039, TASK-000040
- Approval Requirements: APP-000010; independent review/adoption under existing rules

Use this reference when planning evaluations, interpreting telemetry, checking completion or recovering interrupted work. It preserves historical evidence; it does not change authority, adopt a new evaluator, choose a model, or claim current production performance. Exact source identities, fuller findings and limitations live in the [factory/work harvest](../factory/reports/legacy-retirement/factory-learnings.md) and [project harvest](../factory/reports/legacy-retirement/project-learnings.md). The [recovery map](../factory/reports/legacy-retirement/README.md) separates remotely preserved source from summarized raw evidence.

## Lessons to carry into decisions

1. **Completion needs independent evidence.** Keep builder declaration, observed checks, accepted outcome and delivery/recovery status distinct. Legacy builders declared complete while grading was missing or failed and trackers remained unfinished. Existing acceptance gates still apply.
2. **Qualify the evaluator, including its final consumer.** Prove valid alternatives pass and real defects fail. Zero selected tests, schema assumptions, mixed native session IDs and helper-only tests caused false conclusions. Retain original primary results when later corrections change interpretation.
3. **Measure the full attempted work and its missingness.** Start from dispatches, include failed calls/retries, and leave absent native usage unknown. Cached input is a subset of input; nested phase time is a subset of enclosing time. Elapsed time, active labor, subscription cost and estimated token tariffs are different quantities.
4. **A promising aggregate is not a proven improvement.** Small, incomplete, fixed-order trials and per-cell regressions did not support adoption. Honor preregistered benefit thresholds, hard constraints and workload boundaries; preserve inconclusive and adverse outcomes.
5. **A later pass does not prove a repair.** Equal committed trees produced different results when ignored/runtime state differed. Bind effective input, environment, observer version and workload before attributing a change to code or policy.
6. **Reconcile effects before retrying.** Lost responses and partially completed setup need destination-state checks, ownership and durable operation identity. An idempotent broker preventing a duplicate does not erase an agent's duplicate-attempt defect.
7. **Observation, integrity and remote recovery need separate proof.** Local events, hash chains and acknowledgment rows do not establish an independently recoverable archive. Verify actual remote bytes/refs and distinguish a source summary from a backup.
8. **Qualify the exact runtime boundary.** Stream chunks are not frames; an exited unreaped child is not a live child; a successful scoped privacy canary is not whole-store privacy; a clean scanner with zero discovery is not a clean runtime. Keep coverage and untested boundaries visible.
9. **Keep current state in its authoritative system.** Durable records retain decisions, hashes and unfinished obligations. Reconcile live Git/ticket/effect state before acting on old status prose. A merge alone does not prove independent review occurred.
10. **Product and beneficiary evidence stays distinct from process assurance.** Synthetic DORA, fixtures, setup diagnostics, screenshots and component tests cannot close a live user journey, physical hardware test or owner-value judgment. Label demonstration modality and bind human verdicts to exact artifacts.
11. **Keep canonical knowledge separate from private user context.** Preserve source revisions, uncertainty, semantic identity and correction history. A generated index, resume or report must not become a second conflicting authority or silently import personal material.
12. **Retirement must inspect more than main.** This harvest found broken moved worktrees/alternates, an untracked instrumentation file, standalone non-Git tooling and a unique reflog commit. Archive meaningful source, classify fixtures/dependencies, and say which ignored evidence is summarized rather than restorable.

## Quantitative anchors and their limits

| Historical evidence | Retained observation | What it does not establish |
| --- | --- | --- |
| Meta-factory three-arm state comparison | N=1 each;80 grading groups; conversation17pass/6fail/57untested, Projects32/6/42;Git-file original grading entries missing | No workflow winner, reliable cost-per-accepted-task or production DORA |
| Catalog partial desktop trial |243 assigned,211 objective scores;primary53/71,57/70,57/70 | No confirmed treatment effect; cancelled/unbalanced remainder retained |
| Work selected outcome screen |104 episodes/296sessions;49/104 primary successes;usage275/296 |21 missing usage receipts are not zero; later61/104 is a separate exploratory correction |
| Work matched comparison |Candidate7/16,baseline6/16;two wins,one loss,13ties;median time ratio1.04 |Aggregate gain does not waive the frozen no-cell-loss rule |
| Competition journal |531 records,73 unique lessons;failed/superseded/infrastructure-attention runs retained |Records/events are not independent trials or completed trajectories |
| Penny local observation DB |58,347events;0bundle rows/acknowledgments |Local observation history is not proof of remote archival |
| Wired local trial |40trials;median ratios0.9813 and0.9527,below required10%improvement |Inconclusive, despite narrower successful checks |

These are source-bound historical findings, not newly executed experiments. See the full reports for exact definitions, dates, source digests, missingness and counterevidence. Concrete policy/tool changes suggested by this evidence still need a separately admitted task, current baseline, independent review and the existing approval process.
