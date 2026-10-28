# Intent-provenance instruction implementation

- Target System: organization
- Change Classification: organization
- Authorized Scope: sanitized implementation comparison and fixed-case evidence for TASK-000381
- Affected Paths or Resources: scoped intent-provenance instructions; no project records, runtime, publication or evaluator change
- Owning Role: Developer
- Related Requirements: REQ-000001, REQ-000008, REQ-000059
- Related Tasks: TASK-000381
- Approval Requirements: APP-000587 admission only; independent Reviewer and Chief of Staff approval remain required

## Scope and baseline

Implemented one canonical protocol with short integration points in existing planning, acceptance, role and handoff guidance. Baseline is public main `17809de263f6990efeeda9b2240fffd504e96a32`. No evaluator algorithm, approval threshold, permission grant, runtime, background service or project behavior changed. The handoff template gained separate fields, keeping the existing schema and delivery evidence.

The baseline already states that proposals remain proposals, a plan is not permission, assumptions cannot enlarge grants and the Coordinator reconciles original intent. Those safeguards were retained. The admitted repair clarifies the information that must survive admission, selection, review and handoff, plus a conditional tangible-demo path. It does not claim that more instructions alone guarantee model behavior.

## Source comparison

| Path | Baseline SHA-256 | Candidate SHA-256 |
| --- | --- | --- |
| `shared/INTENT_PROVENANCE.md` | `Absent` | `5fe49831d9cca64612d2ff80b02fa17633b05d992882c4e11db9e209d866d368` |
| `policies/PLANNING.md` | `1b3d3433722364abac2135f1785b5ab150b3535d5065cac9532b596532eca87f` | `56cfd1ff4ef01d29592a4a43c9b5efeafa4b6d516d0815eddd01e562a8512a9d` |
| `policies/ACCEPTANCE.md` | `e4df277eb7c64b7a3f89f8620e914912e6772a130a96b6891e2bea7935d202c5` | `193a3150240ad64542b033d9c31f500077c5ff80c824510808f3660f974a33a8` |
| `agents/coordinator/AGENTS.md` | `9516140c08d3f00f999efd1e2095bb89eaaf016cb9d195edc42f23d9757a009a` | `41c4fef6823d65c6a73016f174b4c42abd2cd4f8c168a4a560bfe636dfa77e7c` |
| `agents/planner/AGENTS.md` | `7947e9ff1b445b8e5deda8481ebf012e4aae8f408406bd36fd8f4b65490d2759` | `8e01bcbf27ec1a8a3312e6b84cb260e660379b3dee4d6c96482c3be3d92dad59` |
| `agents/reviewer/AGENTS.md` | `bcb96c96d1146c5dea3eaf9acd24a44195b41fb521ffeb0f01fc1a6b1599bf47` | `dfc07b7bba5f24669aa2267df48aedef63fd88cc51f87cc3793cdde2898b66a3` |
| `shared/HANDOFFS.md` | `13fc25db64217141174977257bc5656e48b456180d163ae6925af468d6e964ec` | `301097f99ec138bce5d7fe2ee88811e27542140f2fab45cfda97f8f7f15e0e40` |
| `shared/templates/HANDOFF.md` | `7c860a8a7fceb312b2ee6e1d1a3b1bcc0ff5b119db421be0543cd898d3c59674` | `903639de8e9410e88454e88a70d1686969386b96968cc240d1ad1671dc8fa155` |

The baseline has no canonical request/agent-choice/authorization protocol, no separate ordered outcome-fit and technical-review result, and no specific handling of brief assent or demo observation. Existing permission rules already forbid unauthorized effects; the new source explains their application without replacing them.

## Verification performed and pending

Developer inspection mapped every predeclared scenario to candidate text in [CASES.md](CASES.md). `git diff --check` exited 0 after instruction edits. A bounded Python source check exited 0: every relative file link in the ten developer-owned files exists; the canonical protocol retains all five intent states and six sections; the scenario table retains all twelve fixed cases. These are structural source checks, not behavioral results. Full organization structural/regression checks and independent scenario execution are Coordinator/Reviewer-owned; no pass is claimed here for work not run by this developer.

The twelve scenario outcomes, exact assembled candidate, independent review, independent Chief of Staff decision and ordinary PR/main delivery remain required. Worker completion transfers authored paths for review; it is not acceptance or promotion. No Git mutation or external effect was performed by this implementation worker. No private project identity, source quotation, local root or machine binding was copied into these reusable instructions or synthetic cases.

Rollback is an ordinary scoped revert preserving failed observations. A changed candidate invalidates affected review; broader stochastic benefit still requires the unchanged improvement evidence policy.
