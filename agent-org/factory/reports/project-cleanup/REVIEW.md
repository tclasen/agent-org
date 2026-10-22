# Independent local cleanup review

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: Read-only review of APP-000012 five local project cleanups and root clone exclusions; write this review only
- Affected Paths or Resources: /Users/Shared/{commons,every_game,semantic_search,wired_to_survive,llm-cost-calculator}; root .gitignore; project-cleanup evidence
- Owning Role: Reviewer
- Related Requirements: REQ-000048 / AC-000048
- Related Tasks: TASK-000049; parent TASK-000041; TASK-000042 through TASK-000048
- Approval Requirements: APP-000012; independent Chief of Staff organization evidence decision; Coordinator local acceptance

Recommendation: accept the pinned cleanup for its authorized local scope. No material findings remain. This is an independent review recommendation, not shared delivery or product acceptance.

## Candidate and evidence identities

Reviewed under RUN-000043 by fresh worker `/root/cleanup_review`, without implementation authorship. Requested model/reasoning are recorded in the run; actual model/reasoning remain unknown.

- Baseline manifest: `baseline.json`, SHA256 `769d03f64a971534de78f1f878a20b4f23544d76cd38259dd099356fdada9775`.
- Final candidate manifest: `candidate.json`, SHA256 `23954812f96e6345403ab3ac7c95616dad521427ddab717da955af8885d5fc8d`.
- The earlier candidate `e6fe4e68d42f1ec855b0079888d1792c87eee52b57e2e12cfa6f6dd43e56b9bd` was superseded during review. The final semantic PROJECT, SECURITY and product-readiness changes and all final inventories/hashes were rechecked before this recommendation.
- Evaluation basis: APP-000012, PLAN.md acceptance/rollback criteria, organization authority/scope, acceptance and measurement-independence policies. REQ-000048 / AC-000048 records the same source-bound acceptance scope; it adds no new test or relaxed condition. CHECKS.md is supporting implementation evidence, not the independent verdict.

| Project | Unchanged baseline HEAD | Verified cleanup |
| --- | --- | --- |
| commons | ce2d170f78ef7e88be35e5368a1faae8de83aa7a | Embedded organization removed; README and new project bridge route to parent. |
| every_game | 80bf7a748cc45c419d6f0df88b84c64e4fdba8ca | Autonomous selection/delivery rules retired; Rust/Bevy, requirements, desktop isolation, testing and milestone video guidance retained. |
| semantic_search | 00cd8b698720caa20ba42ee9fde007e02b3e862b | Standalone factory/execution/instruction policies retired; product records and assurance mapping preserved with parent precedence. |
| wired_to_survive | f4ccf2e0a422d3266fdb37951889b416fb3186a0 | Factory runtime/catalog/hooks/tests retired; product backlog preserved; verifier retains product checks. |
| llm-cost-calculator | a0afd45a35b16ae0274455e64a896efb6e7465eb | Parent bridge replaces standing release mandate; data, estimation, saved-input and complete buy/rent/API requirements retained. |

## Criterion-level results

| Criterion | Outcome | Independent evidence |
| --- | --- | --- |
| Five direct, independent clones preserve history/remotes | verified | Canonical Git top levels match the five exact directories. All HEADs, refs and origin URLs match baseline; all project indexes remain unstaged. All 1,222 baseline tracked-file SHA256 values independently match their recorded Git commit blobs. |
| Candidate exactly identifies reviewed local content | verified | All 813 retained/new file hashes and complete inventories match final candidate.json; 414 removed paths are absent. Changes comprise 25 modified, 414 deleted and five new files. No retained-file symlink escape was found. |
| Application preservation and bounded executable repair | verified | Baseline-to-candidate inspection confines changes to instructions, organizational artifacts, reference repairs, preserved backlog relocation and Wired verifier retirement dependencies. Application source/build/lock/scenario/fixture content remains unchanged. Wired verify.py removes only factory tests/audits/catalog checks plus its descriptive wording. |
| Parent organization is primary | verified | Five project entrypoints route to parent AGENTS/agent-org. Active embedded hierarchy, dispatcher policies and Wired lifecycle hooks are retired. Wired project-local .codex files exclusively configured the retired factory; their removal is covered by the direct grant. Root AGENTS has no diff. |
| Useful project and safety constraints survive | verified | Retained technical instructions, domain requirements, owner game-design gates, deterministic replay/video rules, source/consent/privacy/retry limits and calculator data contract inspected. Semantic SECURITY preserves the actionable secret-bearing diagnostic procedure from the retired instruction policy. Historical grants cannot admit new work under the explicit parent-precedence notices. |
| Live references and verifier remain coherent | verified | All relative file links across 26 edited/new Markdown files resolve; no retained Markdown links point to removed paths. Retained Wired Python files parse. Its manual workflow calls surviving verify.py; no live factory import/hook/script caller remains. Historical source hashes and commands in retained evidence are explicitly historical. |
| Product backlog/provenance preserved | verified | Wired delivery-backlog.json is byte-identical to original factory-ready-backlog.json. game-backlog-reference.json differs only in its repaired manifest path. Product dependency/decision details remain in docs/design; semantic readiness preserves its product assurance content with a retirement notice. |
| Meaningful affected checks | verified | Independently reran `python3 -B -m unittest discover -s tests/verification -v`: seven tests pass, including valid evidence and six rejection cases. All five final project `git diff --check` checks pass. |
| Independent histories excluded from parent index | verified | Five exact root .gitignore directory entries are present and each resolves through git check-ignore. Root ignore bytes match candidate identity; root AGENTS is unchanged. |
| Local-only effects and rollback | verified within observation | No project commits/ref changes or staged content observed. Reviewer performed no network operations, project writes or external effects. Coordinator reports read-only clones only. Baseline commits preserve removed tracked content for selective rollback. |

## Limits and next action

Full application, Rust/GPU, remote protection and deployment checks are excluded from this cleanup verdict: application bytes are unchanged and this review does not claim fresh product qualification. A local filesystem review cannot independently prove an exhaustive absence of external operations; no contradictory external-effect evidence was observed. Retained mixed historical requirements are not a competing active organization, and broad historical rewrites are unnecessary for this scope.

PR delivery remains deferred under the explicit local-only grant; this recommendation does not waive future PR/review obligations or authorize publication. Changes to the pinned project contents invalidate the affected review. Chief of Staff should evaluate the organization evidence, then Coordinator should reconcile local acceptance and task/run records. Reviewer changed only this file and returns the handoff through the native message channel.
