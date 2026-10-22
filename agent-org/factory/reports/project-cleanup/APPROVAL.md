# Independent local cleanup evidence decision

- Target System: organization
- Change Classification: organization
- Authorized Scope: Adopt the exact APP-000012 local cleanup evidence under TASK-000050; write this artifact only
- Affected Paths or Resources: agent-org/factory/reports/project-cleanup/APPROVAL.md; read-only assessment of five named clones, root exclusions and bound evidence
- Owning Role: Chief of Staff
- Related Requirements: REQ-000048 / AC-000048
- Related Tasks: TASK-000050; parent TASK-000041; TASK-000042 through TASK-000049
- Approval Requirements: Existing APP-000012 direct operator grant; fresh independent Reviewer and distinct Chief of Staff execution

**Decision: APPROVE adoption of the pinned organization evidence and acceptance of the authorized local cleanup.** No material evidence or scope finding remains. Coordinator may reconcile local completion after verifying these identities and the required child outcomes. Shared integration remains deferred.

Decision recorded 2026-10-22T00:32:08Z by fresh Chief of Staff execution `/root/cleanup_approval`, RUN-000044, TASK-000050. This execution implemented neither the cleanup nor its independent review. Requested model/reasoning are gpt-6.1-sol/high; actual metadata remain unknown. This artifact records a candidate-bound decision under existing APP-000012; it allocates no new APP identity or authority.

## Bound inputs

Plan revision 1 and the source-bound AC-000048 define the deterministic local acceptance criteria. Existing authority, scope, approval, acceptance and measurement-independence policies govern this decision; none were changed. This is completion of explicitly requested local operations, with organization evidence adoption, rather than a governance-policy or productivity experiment.

| Input | SHA256 |
| --- | --- |
| [PLAN.md](PLAN.md), revision 1 | `caaf9a8650c29b22c735eb5636ceefa7d7a019fe3711bb700aab643229ee2f79` |
| [baseline.json](baseline.json) | `769d03f64a971534de78f1f878a20b4f23544d76cd38259dd099356fdada9775` |
| [candidate.json](candidate.json), final candidate | `23954812f96e6345403ab3ac7c95616dad521427ddab717da955af8885d5fc8d` |
| [CHECKS.md](CHECKS.md), implementation evidence | `7179d322c8f864ef0cc26b93c1bb7273f349421bfc8eb6de350a097f16dd5cde` |
| [REVIEW.md](REVIEW.md), independent final verdict | `d504df3bf8b4dc5ddc7f0185752e6ec8c0052939ef7b33088aad5ae0a735ef95` |
| REQ-000048 revision 1 | `6e259eb731b6c63616ebf61d9e5bf3e9dc54c7b800ca0d00e820979a102394f4` |
| Existing structural evaluator, factory/instrumentation/check.py | `da22192e7b87d2c054f070ab2b7841cb133a11cd7a19f39e87ea0e9f70f27fb2` |

The superseded candidate identified in REVIEW.md is not approved. The final manifest binds complete project inventories and contents, the five unchanged baseline commits, and root `.gitignore` SHA256 `fb47b488ca07417d8b3e9b9422059e561b07cf7b48fc1139d74090506ebe52da`.

## Independent assessment

I read the source grant, task/run, plan, complete final review and supporting checks, and independently verified their content identities. TASK-000049 is accepted with independent review evidence and intent reconciliation. The Reviewer execution `/root/cleanup_review` is distinct from this approver and the implementation execution.

I independently matched all 1,222 baseline hashes to their recorded Git commit blobs and all 813 candidate file hashes to current local bytes. Complete retained/new inventories match; all 414 recorded removals are absent. Each canonical clone has the recorded HEAD, refs and origin, an unstaged index, and a passing `git diff --check`. The exact five root exclusions resolve through `git check-ignore`; root AGENTS has no diff. This corroborates the Reviewer's preservation and scope findings against the actual candidate.

I inspected all five entrypoint bridges, the Wired verifier diff, and the final semantic PROJECT/SECURITY changes. Parent admission and current grants take precedence; useful technical/product constraints remain. The secret-bearing diagnostic procedure survives retirement of its former policy file. Wired's executable diff removes factory-only checks/catalog dependencies while retaining product checks. I independently reran `python3 -B -m unittest discover -s tests/verification -v`: all seven evidence-consumer tests passed, covering valid evidence and six rejection cases. The Reviewer's separate link/dependency inspection verifies 26 edited/new Markdown files and the absence of live retired factory callers.

My first checker help probe used absent `agent-org/instrumentation/check.py` and failed without mutation. The canonical checker then reported one administrative error: accepted TASK-000049 lacked structured intent reconciliation. Coordinator corrected that record without changing the project candidate or evaluator. My rerun of `python3 -B agent-org/factory/instrumentation/check.py --root agent-org` passed 199 records with zero errors. These failed observations remain disclosed; structural validation does not establish product behavior.

## Conditions, limits and handoff

Approval is effective for the exact local candidate and evidence above. It grants no product qualification, governance change, deployment, remote publication or waiver of future PR rules. Application source/build/lock/scenario/fixture bytes are preserved as reviewed; full Rust/game/GPU and other application suites were not run. Local inspection cannot prove the exhaustive absence of external operations; Coordinator reports read-only clones, and this approver performed no network operation or external effect.

The operator expressly requested local cloning and embedded-organization retirement. APP-000012 authorizes those effects and excludes remote delivery. Therefore no further operator gate or publication is required to close this local task. Any later shared delivery must follow the existing scoped PR, fresh review, exact-candidate approval, hosted-check and merge-verification rules; this decision does not represent that future delivery as complete.

Coordinator's next action is to recheck the frozen candidate/review/approval bytes, reconcile required project/integration children and organization records, release completed claims, and report local completion with remote delivery deferred. Factual status reconciliation may update task/run records without changing this frozen project candidate. A changed project candidate or bound substantive evidence invalidates the affected approval and requires repinning plus proportionate independent review/adoption.

Rollback restores only task-owned tracked paths from each manifest's baseline commit and removes only task-created files. Preserve unrelated changes; use no broad reset/clean and do not alter refs, origins or old/. This worker wrote only this artifact, allocated no IDs and performed no Git write. The handoff returns through the native message channel under its single-file claim.
