# Legacy learning harvest and cleanup map

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: Source-grounded harvest, scoped Git preservation and cleanup guidance under APP10/11; no deletion
- Affected Paths or Resources: old/ source inventory; agent-org retained evidence; listed project remotes
- Owning Role: Coordinator
- Related Requirements: REQ-000044, REQ-000045, REQ-000046, REQ-000047
- Related Tasks: TASK-000029, TASK-000031, TASK-000032, TASK-000033, TASK-000039, TASK-000040
- Approval Requirements: APP-000010, APP-000011; independent REVIEW.md and APPROVAL.md

The reusable [legacy lessons](../../../shared/LEGACY_LEARNINGS.md) are now discoverable from Coordinator context. Detailed [factory/work findings](factory-learnings.md) and [project findings](project-learnings.md) retain sources, metrics, negative results, uncertainty and coverage limits. This is historical knowledge adoption, not a new policy/evaluator/model promotion.

## What was preserved

- **58 main checkouts accounted for:**44 local project copies explicitly permitted to be discarded after harvesting despite47 inaccessible configured remotes;14 remaining checkouts have all9,153 local branch/tag refs' commits verified reachable from live advertised durable remote heads/tags. Annotated tag object identity was checked separately. Counts include repeated checkout identities, not58 distinct products.
- **235 dated archive refs added:**46 catalog,151 Penny (including one unique reflog-only documentation commit),21 semantic-search,17 Wired. These preserve original historical commits without merging unapproved changes or rewriting current branches.
- **factory_evals populated:** its existing empty remote now contains local main `0559d82db5da43beda51f2ca7676ec268313026e` and its existing three-commit history.
- **Independent retrieval:**236 archived/main commits and trees retrieved into fresh independent object stores, with matching original IDs. Seven selected changed source/document blobs, including both Penny orphan documents, were downloaded and compared byte-for-byte. Four historical repositories used blob-filtered fetches; this is not a full application/asset restore test.
- **Voldenites LFS availability verified:**113unique objects,3,031,592,588logical bytes, all returned live download actions without object errors. A22,057,981-byte median-size object and a623-byte object were downloaded and matched their SHA256 IDs. This checks availability plus samples, not a full3GBrestore; [evidence](git-lfs-verification.json) retains counts/limits without credentials or signed URLs.
- **Unique loose source saved:** [onboarding tool](git-recovery-onboarding.md), three files22,249bytes, and [Ollama metering instrumentation](git-recovery-ollama-metered-source.md), three Go files/license/patch200,301bytes, survive as inert exact-byte Markdown recovery records. Verified decoding preserves hashes and file modes; they are not installed organization tools.
- **Nested repositories reconciled:**860 total discovered markers,58 primary and802 nested, all nested entries classified;30 moved Penny worktree pointers and261 object-alternate dependencies inspected through read-only remapping. These are not860 independent projects. Fixture and dependent-cache distinctions are in [nested audit](git-nested-audit.md).

No old/ source file, local index or project branch was intentionally modified. No local or remote repository was deleted, no product changes merged, and no legacy application/test/hook executed. Live external effects were additive Git history preservation only. One connector attempt to create the Penny orphan ref failed because the object was absent; Git uploaded it successfully and readback verified it.

## Cleanup meaning and limits

This map supports the requested learning-led cleanup. **Recloning restores preserved Git source, not the complete original disk state.** The harvest explicitly distinguishes inventoried/hashed material, parsed numeric records, reviewed conclusions, exact duplicates and excluded content. It does not claim every unique raw event, private transcript, proof, video, dependency cache or product source file was semantically reviewed.

Ignored raw sessions, telemetry databases, recordings, deployment/runtime databases, protected evaluation inputs, caches and private VM/account state generally remain only in old/. Their useful findings and selected replayable arithmetic/identity derivatives are retained, but full forensic replay is not. Keep an additional secure raw archive only if that separate future use is wanted. APP11 expressly permits disposal of the44 named inaccessible-project copies after harvesting; the current task does not invent a new full-disk-backup prerequisite. Remaining read limits/errors—including one owner-private factory log symlink—are recorded in the source manifests and reports.

Primary untracked exceptions were8empty SQLite WAL files and their shared-memory indexes,3generated Voldenites Python cache files, and an empty note in a waived copy. Meaningful nested custom source and the unique Penny worktree reflog commit were preserved separately. General unreachable-object recovery, full Git LFS/submodule payload restoration and every asset-byte download were not performed; known limitations stay visible rather than a blanket all-bytes-backed-up claim.

## Each main checkout

Paths are relative to old/. `Remote verified` means branch/tag/HEAD commit recovery, with the raw-state limits above. `Operator disposal waiver` means remote preservation was deliberately waived after learning harvest; it does not assert the inaccessible remote contains the local changes. Historical access failures are retained in [case list](git-access-cases.md).

| Local copy | Disposition | Verified source remote / recovery |
| --- | --- | --- |
| `projects/DriftWise` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/Foundry` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/K8s_app_demo` | Remote verified | [K8s_app_demo](https://github.com/Ctandersonjr/K8s_app_demo) |
| `projects/PlenuMesh` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/agent` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/ashwake` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/atelier` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/atmospheric-processes-knowledge-graph` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/backup.resume` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/backup.resume-final` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/backup.resume2` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/backup.resume3` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/cards` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/classwork` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/coding_evals` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/commons` | Remote verified | [commons](https://github.com/tclasen/commons) |
| `projects/competition` | Remote verified | [features_and_futures](https://github.com/tclasen/features_and_futures) |
| `projects/drag-and-drop-kanban-board` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/every_game` | Remote verified | [every_game](https://github.com/tclasen/every_game) |
| `projects/example` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/exploring` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/factory` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/factory_catalog` | Remote verified | [factory_catalog](https://github.com/tclasen/factory_catalog) |
| `projects/factory_evals` | Remote verified | [factory_evals](https://github.com/tclasen/factory_evals) |
| `projects/fmodel` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/games` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/gof` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/meertecha_arcade` | Remote verified | [meertecha-arcade](https://github.com/tclasen/meertecha-arcade) |
| `projects/models` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/myshellium` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/penny` | Remote verified | [Penny](https://github.com/Viixle/Penny) |
| `projects/penny-hook-review-79` | Remote verified | [Penny](https://github.com/Viixle/Penny) |
| `projects/reactive_space` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/resume` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/resume-skill` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/semantic_search` | Remote verified | [semantic_search](https://github.com/tclasen/semantic_search) |
| `projects/splunker` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/sudoku` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/svkg` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/tclasen` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/udop` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/videos` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `projects/voldenites` | Remote verified | [voldenites](https://github.com/tclasen/voldenites) |
| `projects/wired_to_survive` | Remote verified | [wired_to_survive](https://github.com/tclasen/wired_to_survive) |
| `projects/work` | Remote verified | [sparkle](https://github.com/tclasen/sparkle) |
| `projects/workflow` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/AegisTrace` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/CognitionGrid` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/Exaptra` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/PortionGuard` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/ai_cost` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/coding_evals` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/factory` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/ism-tools` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/marked` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/odni-sdk` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `work/portions` | Operator disposal waiver | [APP11](../../../approvals/APP-000011.md); see case list |
| `factory` | Remote verified | [meta-factory](https://github.com/tclasen/meta-factory) |

## Nonrepository roots and grouped evidence

| Legacy group | Disposition |
| --- | --- |
| `agent-collaboration/`, `agent-handoffs/` | Taxonomy/control proposals preserved with proposal status and source identities; not adopted automatically. |
| `factory-eval-workspaces/`, `factory-evals-workspaces/` |211completion declarations and22synthetic answers parsed with exact missingness/declaration limits; fixture source/code is not a new product requiring a remote. |
| `projects/features-and-futures-builders/` |454clean builder repositories grouped under competition; published experiment histories remain in `features_and_futures` (8,697 local refs verified). |
| `projects/features-and-futures-deployments/` |Competition deployment/runtime evidence; useful failure/recovery lessons retained, raw runtime state not promised recoverable by clone. |
| `projects/penny-evidence/` and ignored Penny stores |Penny evidence family; source/review/acceptance/archival lessons retained, including a sanitized162-case outcome derivative. Raw recordings/images/DB events are not fully copied. |
| `projects/sparkle-eval-evidence/` |Private work-screen archives; findings and archive identities retained, raw private sessions not published. |
| `projects/onboarding/` |Exact three-file inert recovery snapshot in this organization repository; no standalone remote existed. |
| `work/foundry/` |Empty at inspection; no substantive payload/learning invented. |
| `projects/ai_bullet_heaven` symlink |Points to pre-relocation path; link inventoried, not followed. Physical Wired family covered separately; no unique link-target content asserted. |
| Generated dependencies, caches, build output and synthetic captures |Explicitly classified/excluded; meaningful build/eval exception and four unique dirty factory capture families inspected for learning. No promise every cache is reproducible. |

## Selective recloning

Choose a `Remote verified` URL above and clone into a separately enrolled project directory (the current organization excludes `/Users/Shared/projects/` from its own Git history). Follow the existing [project enrollment guide](../../../knowledge/PROJECT_ENROLLMENT.md) when assigning the clone to this organization. Each project keeps its own Git history, instructions and authoritative tickets. This harvest does not automatically enroll, activate or deploy any project.

Normal clones fetch remote branches, including `archive/legacy-20261021/...`. Inspect those archival refs only when recovering historical/unfinished work; they are not accepted replacements for current main. Penny's orphan is `archive/legacy-20261021/reflog-16342ccc5286`. The source recovery Markdown records include safe decoding guidance and hashes for their small nonrepository exceptions.

## Evidence and review

[Final Git verification](git-final-verification.json), [live remote readback](git-remote-refs-final.json), [external-effect journal](git-preservation-effects.json), [independent commit/tree recovery](git-remote-recovery-proof.json), [downloaded blob comparison](git-remote-blob-proof.json), [inert snapshot verification](git-recovery-snapshot-verification.json), [source-scoped plan revision2](PLAN.md), [independent review](REVIEW.md), and separate Chief of Staff adoption decision in APPROVAL.md bind the result. Initial observations are retained separately from later corrections; current hosting/PR state should be checked live rather than inferred from this static report.
