# Local cleanup checks

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: APP-000012 named local clones, scoped records, root clone ignores
- Affected Paths or Resources: five local clones and root .gitignore
- Owning Role: Coordinator
- Related Requirements: none
- Related Tasks: TASK-000041, TASK-000042, TASK-000043, TASK-000044, TASK-000045, TASK-000046, TASK-000047, TASK-000048
- Approval Requirements: APP-000012; independent local review

Clean baseline HEAD, refs, origin, tracked file hashes and initial status are in baseline.json. Exact changed/new/deleted paths and current file hashes are in candidate.json. All five HEADs, refs and origin URLs are unchanged. Product source/build/lock/fixture files under each recorded protected set are byte-identical. Root AGENTS is unchanged. Five root .gitignore entries keep independent project repositories outside the parent index.

All five project git diff --check checks and the parent check passed. Relative links in every edited/new Markdown file resolve locally. All remaining Wired scripts parse; its verifier retains Rust, evidence-consumer, replay, negative-case and video checks and no longer refers to retired factory commands/catalogs. python3 -m unittest discover -s tests/verification -v passed all seven tests, including changed source, tampering, failed verdict, missing evidence, incomplete provenance and optimized-execution rejection. Full Rust/game/GPU suites were not run: application bytes did not change, and this task does not claim new product acceptance. Calculator/semantic/Every Game application checks were not needed for instruction-only edits.

Wired factory-ready-backlog.json was preserved byte-for-byte as docs/design/delivery-backlog.json. The product relationship reference was relocated to docs/design/game-backlog-reference.json with its manifest path repaired; docs/design/delivery-backlog.md preserves product details and replaces retired audit commands with parent routing. Historical mixed product evidence/requirements retain prior factory mentions and source hashes, clearly superseded as organization authority. Product uses of agents, Python factory functions and calculator swe-factory workloads remain application content.

External effects: five read-only GitHub clones; one sandbox DNS failure followed by approved network escalation. No commits, pushes, PRs, issue/Project edits, workflows, releases, paid calls or deployments. Cleanup remains uncommitted in local worktrees; any future shared delivery must use required PR/review rules. Rollback is restoration of task-owned paths from each baseline Git commit, never broad reset/clean.

Semantic-search secret-bearing diagnostic handling was carried from the retired generic instruction file into SECURITY.md, preserving the no-echo, allowlisted inspection, rotation, and safe-start restrictions. The project entrypoint lists domain policies once; mixed readiness is explicitly titled product readiness and historical assurance.

Organization-record check: an initial mistaken factory/factory.py help path was absent (exit 2); README identified the implemented instrumentation/check.py. Its first structural pass found missing new-task requirement traceability and two undeclared dependency relation values. Added the source-bound REQ-000048/AC-000048 and changed review relations to validates/requires, preserving the original check outcome here. No evaluator rules changed.

After the prerequisite-state correction, the organization structural validator passed with 199 records and zero errors. TASK-000050 remains planned until the independent Reviewer has passed; the checker's prerequisite rejection was honored rather than bypassed. All five nested clone directories are confirmed ignored by the parent Git repository.
