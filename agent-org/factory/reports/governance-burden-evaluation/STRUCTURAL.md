# Structural instruction-footprint audit

- Target System: organization
- Change Classification: organization
- Authorized Scope: read-only source measurement; writes only STRUCTURAL.md, structural-metrics.json and measure-structure.py in this evaluation directory
- Affected Paths or Resources: these three task-owned artifacts
- Owning Role: Researcher
- Related Requirements: REQ-000084
- Related Tasks: TASK-000395; parent TASK-000394; RUN-000389
- Approval Requirements: APP-000598 admission; independent APP-000599/APP-000600 and Coordinator delivery remain pending

The pinned 26-file instruction corpus contains **13,237 whitespace-separated words**. Mandatory static startup profiles range from 1,635 words for a delegated Researcher to 2,623 for an unassigned Coordinator, before the root bridge and task-specific materials. Repeated headers and role paragraphs provide concrete subtraction candidates. These measurements establish textual structure, not a cause of failures, a smaller effective context window, token usage or productivity improvement.

## Authority, identity and reproducibility

This delegated Researcher independently measured source structure under preregistration revision 1 and approved APP-000598. The request selects a read-only structural audit with three exclusive output paths; it grants no active instruction implementation. TASK-000395/RUN-000389 still say planned/pending admission in their recorded fields, while APP-000598 is approved and the explicit dispatch supplies the current assignment. Coordinator owns reconciliation of those records; this worker did not change them. Requested inherited configuration is known; actual model, reasoning, context capacity, tokens and cost are unknown. No additional delegation occurred.

Run from the repository root:

```sh
python3 agent-org/factory/reports/governance-burden-evaluation/measure-structure.py > agent-org/factory/reports/governance-burden-evaluation/structural-metrics.json
```

[measure-structure.py](measure-structure.py) only reads files and prints deterministic JSON. The shell redirects stdout to the assigned metric artifact. It uses Python standard-library pathlib, hashlib, re, collections and json; no Git, network, tokenizer or recursive link traversal. File paths are checked for escape from the canonical organization root. [structural-metrics.json](structural-metrics.json) retains per-file hashes/counts, startup members, route members and exact repeated text with locations.

All **26/26 source-manifest SHA256 identities match**, with zero word-count mismatches. The manifest itself hashes to `2d6cd50f77ae7cdb17bcd7e4a68baa9ba59f85b56c1b55ef07d1ca5e26db16e7`. The supplied base commit is a reference label only; no Git provenance or clean-main verification was performed. The manifest describes current working instructions, including pre-existing edits. This audit does not retroactively approve that baseline.

Coordinator subsequently reports that the delivery worktree is clean current remote main and that three of the 26 pinned sources differ from the measured working bytes: AGENTS.md, policies/RESOURCE_BUDGETS.md and agents/coordinator/AGENTS.md. This comparison is parent-reported, not independently Git-verified by this worker. The structural results describe the pinned working baseline, not current remote main. No measured input was changed to make delivery counts agree.

For later replay, Coordinator may retain sanitized original bytes under an authorized source-overlay directory using organization-relative paths, then run `python3 measure-structure.py --source-overlay INPUT_DIRECTORY`. Overlay files replace only matching read inputs; other reads use the checkout. `--bridge-source FILE` can supply the separately measured root bridge. No active instructions need modification. Metrics retain hashes for **all 41 distinct organization documents measured** (26 manifest sources plus 26 direct route sources, with 11 overlapping), and separately for the root bridge and source manifest. Parent must check the 15 nonmanifest route sources and root bridge too, retaining any additional differing inputs. Unavailable original bytes make exact historical replay blocked; hashes alone cannot reconstruct them. No retained snapshots are claimed by this worker.

Words mean `len(text.split())` after UTF-8 decoding, including Markdown syntax, links, IDs and metadata. Header metadata means the eight named governance fields in the first contiguous bullet block, excluding identical field examples later in schema documents. Exact repeated nonmetadata lines require at least eight words; repeated prose sentences use the documented heuristic split. The two repetition metrics overlap and must not be added. Neither detects all semantic repetition.

## Static startup and conditional footprint

The core explicitly distinguishes startup from triggered reads and forbids recursive catalog loading ([core](../../../AGENTS.md), lines 3–7 and 23–36). The following are source-defined static profiles, not observed tool-read telemetry:

| Profile | Distinct files | Words, excluding bridge and dynamic context |
| --- | ---: | ---: |
| Delegated Researcher | 5 | 1,635 |
| Delegated Chief of Staff | 5 | 1,842 |
| Delegated Reviewer | 5 | 1,927 |
| Unassigned Coordinator | 6 | 2,623 |

Each profile includes core, AUTHORITY, SCOPE_BOUNDARIES and the named role AGENTS/CONTEXT. Coordinator additionally includes SESSION_LIFECYCLE. The root startup bridge separately measures 75 words and is not pinned by the supplied manifest; its current hash is recorded in the metrics. Assigned task/run, applicable plan/approval, dependency evidence and action-triggered sources add variable reads. Consequently these profiles are lower bounds for source-defined task startup, not complete execution input sizes. Host/system/developer messages and inherited history are outside the census.

The eight direct rows in the core's action table link to 26 distinct files totaling 11,698 words. This is a conditional navigation inventory, **not** a requirement to load all 26. Only 11 of those files overlap the separate 26-file manifest corpus. Fifteen route targets are measured with current hashes outside that manifest; their counts are additional descriptive evidence, not preregistered source identities. This census stops after the direct row targets, so it does not claim full transitive fan-out.

| Trigger row | Direct files | Direct words | Researcher static profile plus row |
| --- | ---: | ---: | ---: |
| List projects/report portfolio status | 1 | 831 | 2,466 |
| Admit/plan | 3 | 1,874 | 3,509 |
| Discover roles/delegate | 5 | 2,093 | 3,728 |
| Change organization | 2 | 1,396 | 3,031 |
| Change/enroll project or cross boundaries | 3 | 1,151 | 2,786 |
| Review/approve/deliver | 4 | 2,018 | 3,653 |
| Recover/handoff | 2 | 1,056 | 2,691 |
| Other procedures/tools/history | 6 | 1,279 | 2,914 |

Rows are alternatives that can co-occur; summing them would not describe an ordinary execution. Researcher-plus-row is a standardized arithmetic comparison, not a claim that Researchers perform every listed action. Existing known-path and matching-trigger rules already reduce navigation; no evidence here establishes that compliant workers actually over-read. Link occurrences in each manifest file are retained as navigation surface counts, not required reads or measured search effort.

## Repetition and competing interpretations

The corpus has 200 header-field occurrences totaling **1,190 words (9.0%)**, with 68 distinct complete metadata lines. Retaining one copy of each exact line would remove 786 repeated words arithmetically. That is a textual upper-bound comparison, not an approved deletion plan: file-local scope, ownership and traceability have independent value. Startup header words are 184 for Researcher and 229 for Coordinator.

Four complete nonmetadata paragraphs occur identically in each of the four sampled roles. Their lengths are 51 and 43 words in role AGENTS lines 16/18, and 35 and 49 words in CONTEXT lines 12/16. Across 16 occurrences they contribute 712 words, or **534 words beyond one copy of each paragraph**. Eleven repeated prose sentence groups independently yield 444 excess words under the heuristic; that subset overlaps the paragraphs and excludes short rules. This is a selected four-role result, not an organization-wide census of all role files.

There is also within-role repetition: Researcher CONTEXT line 14 restates its AGENTS capability at line 14. Broad rule themes recur across canonical documents: authority boundaries in core/AUTHORITY/SCOPE_BOUNDARIES, plan/build separation in core/PLANNING, and delivery obligations in core/ACCEPTANCE/SESSION_LIFECYCLE/HANDOFFS. Those thematic observations are analyst findings, not exact-duplicate word totals. A universal core warning plus detailed triggered procedure can be intentional defense in depth; deleting the detail merely because the theme repeats could remove exceptions and actionable steps.

The measured HANDOFFS route source contains 787 words: 297 in the reusable contract before `## Remote-main policy delivery`, then 490 in historical handoff sections. The marker-based decomposition is reproduced by the script. Historical records can preserve useful provenance, but co-location makes them part of a full-file contract read; no causal confusion is demonstrated here.

## Subtractive proposals and bounded next tests

These four proposals require separate admission and qualification under the unchanged evaluator. None is implemented or qualified by this audit. Order prioritizes directly evidenced removals before navigation redesign.

1. **Separate historical handoffs from the reusable contract.** Target [HANDOFFS](../../../shared/HANDOFFS.md), sections beginning at line 22. Move the 490 measured historical words into their existing owning task/report evidence where provenance can be preserved, leaving concise retrieval links only if needed. Keep the 297-word contract intact initially. Risk: broken provenance or removal of unique evidence; never silently discard history or infer that old pending states are live. Bounded next test: inventory those sections, verify lossless migration and links, then run one fresh routine handoff and one historical recovery fixture. Require correct current ownership and successful recovery of the retained source; measure candidate contract words after replacement links.

2. **Remove copied role boilerplate while preserving a canonical invariant.** Target the four exact paragraph groups at sampled role AGENTS lines 16/18 and CONTEXT lines 12/16, plus Researcher's duplicate capability at CONTEXT line 14. Keep role-specific duties/orientation; consolidate shared loading/resource/handoff/telemetry rules with the already-mandatory core rather than add another catalog. The 534-word excess is across this corpus, not a predicted per-run saving; canonical placement and replacement links change the net. Risk: a direct role entry without the core or a delegated worker losing a safety reminder. Bounded next test: four fresh synthetic role-start fixtures, including missing-core and missing-required-source cases, with authority/claim/readiness/handoff/unknown-telemetry checks. Retain core loading as mandatory; any authority regression rejects the candidate.

3. **Replace repeated default metadata with explicit exceptions where tooling permits.** Target default header lines 3–10 in the sampled instructions. For example, the identical broad Related Requirements line occurs 19 times and Approval Requirements line 23 times. Consider one canonical default declaration and retain local scope/owner/actual exceptions and useful source traceability; avoid introducing a second manually synchronized metadata registry. The measured 786 excess words are a comparison ceiling and cannot all be assumed removable. Risk: schema validators, portable standalone documents and requirement tracing may depend on complete headers. Bounded next test: first inventory field consumers read-only, then a separate admitted two-document candidate with one default and one exception; run existing validators and fresh authority/owner/requirement lookup fixtures. Reject if information is lost or the retrieval path expands enough to defeat the measured reduction.

4. **Narrow compound action routes using existing canonical sections.** Target core table rows Discover roles/delegate and Review/approve/deliver (lines 29/32), respectively five files/2,093 words and four files/2,018 words. Distinguish unknown-role discovery from dispatch of a known role, and review from approval/delivery, replacing broad row membership with precise existing-source triggers/anchors. [CONTEXT_MANAGEMENT](../../../shared/CONTEXT_MANAGEMENT.md#retrieve-and-stop) already says use a known canonical path directly; preserve that rule and remove redundant discovery hops rather than add a new decision catalog. Risk: a narrow route may hide a mandatory dependency or incorrectly make policies optional. Bounded next test: twelve frozen ordinary/adversarial action-to-source cases with independently specified required sets; compare actual fresh-execution reads and authority decisions before/after. Require every mandatory source retained and report read counts only where observed. This structural audit alone shows possible fan-out, not avoidable actual reads.

## Checks, limits and handoff

Checks: script execution exited 0; 26 manifest hashes and counts match; JSON parses; a second execution is compared byte-for-byte with the saved metrics. The measurement explicitly excludes schema-body examples from header counts. Required-source lookup found the assigned role, task/run, approval, preregistration and admission; three output paths were absent before creation. No operational test or policy-change trial was performed.

Only this report, structural-metrics.json and measure-structure.py were created. No active policy, project, harness, Git/index, provider or external messaging changes occurred. Script source reads include the manifest corpus for measurement and direct trigger targets; these are not claimed as a minimal actual subject exposure. No infrastructure retry was used. Runtime budget is bounded by the delegated approximately ten-minute track; exact token/cost/cumulative parent usage is unknown. Native worker identity is session-only and is not retained here.

Structural acceptance: reproducible census and source identity checks pass; causal/productivity/generalization claims remain untested. Proposed reductions need independent review and separately admitted next tests. No policy defect or behavioral failure is established solely by repetition. Reviewer should independently rerun the script and check the targeted source sections, especially the distinction between manifest corpus and route inventory.

Delivery state: local task-owned artifacts only; branch, PR, candidate Git head, merge and owning-remote main verification are pending with Coordinator and were not attempted under the explicit no-Git assignment. The worker releases its three-file mutation claim on handoff. Exact next safe action: Coordinator verifies these artifacts and identities, reconciles TASK-000395/RUN-000389 state, then submits the unchanged structural evidence to the fresh APP-000599 reviewer and APP-000600 approver. Parent owns integration, delivery and final acceptance.
