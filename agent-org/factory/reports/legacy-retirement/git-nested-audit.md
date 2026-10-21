# Nested Git and non-repository audit

TASK-000033 / RUN-000033, Executor `/root/legacy_git_audit`. Observed 2026-10-21. Source root `/Users/Shared/old` remained read-only. No network, legacy code, hooks, source/index/ref writes, staging, commits or external messages occurred. Optional Git locks and filesystem monitor disabled. Organization outputs use only `git-nested-*` plus this run's checkpoint. Parent Coordinator owns remote verification, preservation and final acceptance.

## Coverage and classification

Expanded the prior 852-marker traversal through `.cache`, `.pytest_cache`, `.mypy_cache`, `build`, `dist`, `target` and `vendor`. Found 8 additional markers: six udop pytest repositories, a zero-byte uv `.git` sentinel, and a clean third-party `every_game/target/codex-proxy` clone. Total observed markers: **860**, comprising the parent's 58 primary markers and **802 nested markers**. `git-nested-classification.json` has exactly one disposition for every nested path.

| Nested class | Markers | Positive evidence / treatment |
| --- | ---: | --- |
| Evaluation builder checkouts | 454 | Competition run manifests map builder roots; task application commits and native-history.bundle restoration reflog establish evaluation outputs. All committed checkouts clean; one unborn PM shadow. Preserve lessons/evaluation originals according to competition evidence plan; no 454 new remotes. |
| Penny linked worktrees | 30 | Shared Penny common Git directory, individual HEAD/index and remapped metadata inspected. All tracked/staged/untracked statuses clean. |
| Penny historical/unit source fixtures | 262 | Tests explicitly create `--shared` clones at pinned source commits; historical schema and unit-runtime structure. 261 depend on relocated object alternates; one independent unit-runtime repair source clone. |
| Penny synthetic probe fixtures | 12 | HEAD subjects explicitly say synthetic inputs/fixture/review inputs. One deliberately untracked synthetic symlink test target. |
| Competition evaluation recovery/shadow checkouts | 5 | PM-only diagnostic/identical starter/task application histories and local per-builder history.bundle origins; includes one unborn shadow. |
| Modified upstream source: Ollama | 1 | Third-party origin and three local custom source changes; preserve separately as detailed below. |
| Clean upstream dependency: codex-proxy | 1 | Origin `https://github.com/mehdic/codex-proxy`, main `da828dafa0bb98a932e022edb608e6b35f0a8d9b`, clean status. This meaningful build-directory exception was inspected rather than assumed generated. |
| Factory captured application sources | 16 | Calibration-generated workspace/task histories and capture manifests. Six dirty snapshots, four unique change sets; see exact source metadata. |
| Factory host canary fixtures | 6 | Unborn repos containing only AGENTS.md, canary.txt and optional heartbeat.txt, 108–485 bytes each. |
| Factory partial Git capture snapshots | 8 | Explicit Git-directory validation fails: six config-only markers, one empty marker, one partial metadata capture. These are source snapshots, not functioning separate repositories. |
| udop pytest fixtures | 6 | Unborn test_clean_* test directories with synthetic source/pyproject/draft inputs; two intentionally stage dist/source.txt. Covered by operator's inaccessible-udop lessons-then-discard disposition. |
| uv cache sentinel | 1 | Empty `.git` file, invalid Git format. |

779 nested markers have committed HEADs; all 779 received successful status inspection after read-only recovery. Of these, 771 are clean and 8 dirty. Fourteen further markers are valid unborn repositories; twelve have intended fixture inputs, two PM shadows are empty. Nine markers are invalid/partial/sentinel metadata. No stash refs found in nested or supplemental unborn ref listings. Five detached Penny worktree tips all occur in named local-ref ancestry.

Traversal still explicitly excludes 2,620 package/virtualenv/bytecode directory instances (`node_modules`, `.venv`, `venv`, `__pycache__`, `uv-cache`); `.git` internals are inspected as metadata rather than traversed as source. This is an observed marker denominator, not a claim that package internals contain no further Git markers or user edits. Expanded scan returned zero traversal errors. Symlinks were recorded without following them. A prior broad text search returned excessive raw transcript matches and was interrupted; no such payload was retained in these artifacts, and final findings use bounded metadata/source reads.

## Original-source preservation exceptions

**Competition's custom Ollama metering source:** `projects/competition/.local/ollama-metered-source`, detached baseline `cf2a313a298066d572c36812e5ad30a21c0db13b`, origin `https://github.com/ollama/ollama.git`. Changed `llm/llama_server.go` (90,264 B), `server/routes.go` (105,229 B), plus untracked `llm/ff_usage.go` (1,574 B). Current three files total **197,067 B**; tracked binary-capable diff is **2,176 B**. Exact SHA-256 identities are in `git-nested-source-state.json`. The upstream origin does not preserve local instrumentation. Suggested recovery: in an isolated competition preservation checkout, review a curated `preservation/ollama-metered-source/` containing baseline/restore instructions, the tracked patch, added file, source digests and upstream identity; verify applying patch plus added file to pinned upstream source. Do not push to upstream Ollama or copy its full dependency checkout. No source-content or secret scan was performed here; Coordinator must review the three files/patch before publication.

**Penny's unique reflog-only commit:** `16342ccc52864b1cc3a917b1c743280a18dbf1ff`, from `141-product-reconciliation` worktree HEAD log, changes `docs/TRACEABILITY.md` and `docs/adr/0004-layered-city-and-installed-content.md` (10 insertions, 6 deletions). It exists locally, is absent from all current local ref ancestry, and no reachable commit has its same tree `c5b9397135a1b8411b17a34faa38d80a955f947e`. Suggested recovery: review and preserve the exact commit through an explicit archival branch/ref in Penny's existing authorized remote, verifying the advertised OID and fetched content. `git-nested-orphan.json` identifies the delta; `git-nested-reflogs.json` accounts for all 41 distinct nonzero OIDs in 30 worktree HEAD reflogs: 40 reachable, this one not. General branch reflogs/dangling-object recovery outside these worktree logs remains the parent's scope.

**Penny linked-worktree ignored evidence:** 17 worktrees have ignored entries; sixteen have only build/dependency/bytecode categories. `143-integrated-acceptance/test-results/` also contains **5,713 files / 1,402,212,948 B**, excluding `.git` and node_modules. This includes 36 historical source clones and 708 PNG files. The 8,395,800-byte Playwright results.json has now been parsed into `git-nested-penny-test-outcomes.json`: **162 tests, 162 expected, 0 skipped/unexpected/flaky, 0 top-level errors**, one synthetic suite starting 2026-10-05T13:17:14.887Z. The derivative retains individual test identity, outcomes, retry, duration and attachment types; excludes raw logs, request/config arguments and screenshot bodies. It preserves these measured learnings, not browser replay or raw screenshot recovery. `git-nested-worktree-evidence.json` fingerprints every covered file. Coordinator/project researcher must decide raw evidence retention under the operator's applicable disposition; do not infer it from a clean Git status.

## Calibration-generated source and synthetic dirt

`git-nested-source-state.json` enumerates exact dirty files, baseline OID, per-file size/hash, tracked diff size/hash and generated classification. The six factory dirty captures reduce to four unique baseline/change sets:

| Under `factory/.factory-planning/` | Baseline | Dirty files / payload bytes | Recovery suggestion |
| --- | --- | ---: | --- |
| req007-matched-pilot-logs/run-7w1x7t3a/captured-source | 6093585d81b74de7efa5868bbc9cf970f9cc1793 | 3 / 10,121 | One reviewed source-state artifact; tracked patch 1,851 B plus new network policy. |
| req007-matched-pilot-logs/run-p0jplbet/captured-source | 328dcead7075cbad546b8d54a42d620bc2dab8a4 | 31 / 104,258 | One generated app snapshot; distinguish 10 bytecode files from original source. |
| req007-native-git-capture-integration-v1-logs/run-enmdcyui/capture and captured-source; req007-stopped-source-selection-v1-logs/run-y1bqxhnj/selected-source | 92d566e9a03044c8ffd9b52df918a2c4f9ad1a1a | 34 / 292,298 each | These three baseline/path/hash sets are exact duplicates; preserve once if recovery required. Tracked config patch 721 B; distinguish web/dist generated outputs. |
| req007-natural-calibration-v4-logs/run-l_ulr06h/captured-source | 1e8395f96a310e72368d6e6d09ef345db29cb3b9 | 6 / 5,120 | One small generated Kubernetes/ops artifact. |

These are evaluation-generated applications with no independent evidenced owner/remote. Target a factory evidence recovery artifact or lessons disposition, never guessed new remotes. Partial metadata snapshots likewise contain purposeful captured source (six 37-byte app.py cases, one 1,190-byte security fixture, one 212,115-byte generated web snapshot); do not call malformed metadata a failed original product repository. Penny's only dirty probe is `penny-evidence/ticket-88-2026-10-02/code-review/synthetic-probes-BojXeO/app/synthetic-symlink-target.json` (29 B), baseline synthetic fixture `f67bac29b9a3b4a1d547af6bd112bb2c8c1f67b9`; retain its lesson/test context rather than treating it as user product development.

## Non-Git top-level material

`git-nested-nonrepository.json` inventories all six immediate project/work children lacking their own top-level marker. It skips their nested `.git` directories but does not prune dependencies. Counts overlap marker/source inventories and must not be added as independent global totals.

| Path under old/ | Non-Git-metadata files / bytes | Disposition needed |
| --- | ---: | --- |
| projects/features-and-futures-builders | 2,568 / 16,370,827 | 454 nested evaluation repositories; treat with competition run evidence. |
| projects/features-and-futures-deployments | 30,160 / 448,104,908 | Evaluation runtime deployments include 3,738 SQLite DBs and 3,738 logs; source lessons/evidence retention, not independent remotes. |
| projects/onboarding | 3 / 22,249 | Meaningful GitHub setup wizard: README.md, create-project.sh, tests/test_cli.py; all file hashes retained. README associates embedded baseline with tclasen/software-factory, but no authoritative source remote identity established. Preserve desired lessons/tooling through an explicit destination; no scripts executed. |
| projects/penny-evidence | 20,579 / 12,242,921,844 | Browser images/video/logs/source/patches and 12 nested synthetic repos; one dependency symlink points outside old/ to agent worktree. Retain lessons and resolve any desired raw recovery separately. |
| projects/sparkle-eval-evidence | 3 / 13,033,613 | One JSON and two compressed evidence files; linked project research owns interpretation. |
| work/foundry | 0 / 0 | Empty directory. |

## Relocation and source-independence hazards

All 30 Penny worktree `.git` files and reciprocal metadata use pre-relocation absolute `/Users/Shared/projects/penny` paths that no longer exist. Existing `.git/worktrees/<name>` directories and `commondir=../..` support recovery through explicit read-only `--git-dir`/`--work-tree`; these checkout files are not independent clones. All 261 historical clones' `objects/info/alternates` refer to missing `/Users/Shared/projects/penny/.git/objects`; supplying relocated `/Users/Shared/old/projects/penny/.git/objects` only via `GIT_ALTERNATE_OBJECT_DIRECTORIES` recovered all committed objects and clean statuses. Copying those fixture directories without shared objects does not create a backup. Two competition observer-proof fixture origins likewise refer to local pre-relocation bundle paths, not hosted remotes.

An invalid nested marker can cause ordinary `git -C nested ...` to fall through to the enclosing factory repository and show misleading identity or dubious-ownership errors. Follow-up used explicit `--git-dir` and classified the eight partial capture markers, retaining original errors. No global safe.directory or other Git configuration was changed.

The Coordinator relayed the operator's later instruction that the 44 local project copies mapped to 47 inaccessible remotes in `git-access-cases.md` may be discarded after lessons harvest. Respect that case-specific waiver; this audit does not retain raw recovery as a blocker for those named families. It does not automatically extend that waiver to accessible competition/Penny original-source exceptions or unrelated non-Git tooling.

## Handoff and proof limits

Actionable remaining work is specific: preserve/review competition's 3-file metering delta; preserve/review Penny's unique reflog commit; reconcile ignored Penny test evidence using the saved outcomes and file manifest; complete project research dispositions for generated calibration/deployment outputs and onboarding. Current local refs/objects/status and source hashes do not prove a hosted recovery copy. Parent remote verification and final synthesis own that proof. No deletion readiness is inferred here.

Scripts: `git-nested-audit.py`, `git-nested-recovery.py`, `git-nested-state.py`, `git-nested-summarize.py`. Native telemetry JSON provides discovery/exclusions, per-marker commands/results, metadata fingerprints, classification, source states, reflog coverage, file hashes and sanitized test outcomes. `git-nested-artifact-sha256.json` pins this deliverable set; all derived artifacts remain below the 100 MiB run budget. Worker completed its read-only claim; remote preservation and task acceptance remain open with Coordinator.
