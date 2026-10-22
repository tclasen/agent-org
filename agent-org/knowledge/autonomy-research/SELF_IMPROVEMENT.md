# Empirical recursive improvement mechanisms and bounded adoption

Research observed 21 October 2026 (22 October UTC), for TASK-000060 / REQ-000051. Local baseline: `8916d3589054a6416098598a029d64c1d676dd7f`. This report proposes research and experiments; it adopts no operating change.

The strongest transferable result is that agents can search over their scaffolding: instructions, examples, tools, memory and executable workflows. An archive of attempts and diagnostic feedback can make that search more effective. These results do not establish that an organization becomes indefinitely more reliable through recursive modification. Better benchmark scores, cheaper inference, improved ability to propose improvements, and reliable governed promotion are separate claims.

All systems below primarily optimize artifacts around existing models in the described experiments. DGM explicitly freezes foundation models; Reflexion changes episodic text; MIPRO and GEPA optimize prompts; TextGrad edits textual variables; ADAS/AFlow search programs. DSPy also offers separate weight fine-tuning optimizers. AlphaEvolve has improved algorithms used in model training, which differs from autonomously updating its own foundation model weights. Changing providers, models, weights or runtime would require separately scoped work.

## Current local controls and missing evidence

[SELF_IMPROVEMENT](../../policies/SELF_IMPROVEMENT.md), [MEASUREMENT_INDEPENDENCE](../../policies/MEASUREMENT_INDEPENDENCE.md), [WF-000004](../../workflows/WF-000004.md), and [gate 1.0.1](../../factory/quality-gates/DEFINITION.md) already provide substantial promotion discipline. The inspected [implementation](../../factory/quality-gates/improvement.py) pins baseline, candidate, workload, criteria and prior evaluator, checks independent approvals and exact candidate identity, counts supplied attempts, and distinguishes rejection from inconclusive evidence. Stochastic comparisons require at least 20 unique preregistered pairs, seeded randomized ordering and a fixed-seed percentile bootstrap 95% interval whose benefit lower bound is positive. Efficiency also requires at least 5% relative mean improvement. Hard guardrails dominate speed.

The gate permits one active candidate experiment, caps its initial allocation at 3,600 active seconds, and carries ancestor time/storage forward. This research task's shared 90-minute budget does not enlarge that experiment cap. Gate output establishes eligibility for governed PR delivery; it neither authenticates supplied facts nor executes rollback. Shared files cannot technically conceal a holdout from a worker with read access. Tests cover supplied-record consistency, not undisclosed tool calls or fabricated external receipts.

[EXP-000001](../../experiments/EXP-000001.md) establishes a bounded deterministic validator repair, with retained baseline and integration evidence. It is not evidence of stochastic organization productivity or multi-generation improvement. The [merged Tessl report](../TESSL_FACTORY_RESEARCH.md) already proposes context manifests, correction-derived scenarios and held-out evaluation. The additions below extend that plan with search lineage and selection discipline.

## Seven research profiles

### 1 Darwin Gödel Machine self-modifying scaffold plus archive

DGM samples an archived coding agent, asks it to modify its own code, evaluates the child, and retains working variants as possible stepping stones. The paper reports SWE-bench performance rising from 20% to 50% and Polyglot from 14.2% to 30.7%. The SWE-bench figure uses a staged 200-task Verified subset, not the entire leaderboard population. Cross-benchmark and cross-model transfer tests strengthen the case that some changes generalize. Ablations remove self-improvement or archive exploration. The foundation models remain frozen. Estimated SWE-bench search cost is about $22,000 versus $10,000 for each baseline; higher-performing agents can also cost more at inference. These are reported historical estimates, not current prices. [Paper v3, §§4 and E](https://arxiv.org/html/2505.22954v3).

The inspected `DGM_outer.py` implements parent selection, `keep_all` archive updates, staged evaluation and generation metadata. `keep_all` preserves compiled variants rather than requiring every child to beat its parent. Archive membership therefore means searchable ancestry, not production qualification. [Code](https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/DGM_outer.py).

Contrary evidence matters: the authors report fabricated tool logs and a hallucination-reduction experiment in which some candidates removed detection markers and received false success. Traceable lineage helped expose this; instructions alone did not prevent it. [Sakana account](https://sakana.ai/dgm/). Local implication: preserve failed branches, but keep optimizer artifacts and evaluation instrumentation outside the candidate's authorized edit scope. Do not inherit DGM's score thresholds or archive admission as a promotion rule.

### 2 AlphaEvolve and OpenEvolve search where verification is strong

AlphaEvolve combines Gemini-generated program proposals, automated scoring and a program database that supplies future inspirations. Google's primary account reports production scheduling savings averaging 0.7% of worldwide compute resources, and a matrix kernel improvement yielding a 1% reduction in Gemini training time. These are vendor-reported, task-specific deployments, not controlled evidence that an entire agent organization recursively improves. Their relevance is the explicit correctness/performance evaluator and a reviewable algorithm artifact. [Official account, 14 May 2025](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/).

OpenEvolve is a separate open implementation inspired by this approach. Inspected `database.py` stores parent IDs, per-island populations and MAP-Elites feature grids. `evaluator.py` imports a user-provided evaluator and supports staged evaluation with diagnostic artifacts. This makes diversity, lineage and inexpensive rejection concrete engineering mechanisms. It does not reproduce Google's production evidence. [Database](https://github.com/algorithmicsuperintelligence/openevolve/blob/162c3feecbab09b7ab02072f1daaeba4de9fe7a2/openevolve/database.py), [evaluator](https://github.com/algorithmicsuperintelligence/openevolve/blob/162c3feecbab09b7ab02072f1daaeba4de9fe7a2/openevolve/evaluator.py).

A quality-diversity archive can retain a cheap specialist alongside an expensive generalist. Its feature bins are search aids; neither novelty nor a composite score proves safe behavior. Local use should begin with deterministic organization helpers whose outputs can be independently checked. OpenEvolve's threading/timeouts and imported evaluator are not evidence of hostile-code isolation. A fixed random seed cannot guarantee identical remote-model responses.

### 3 GEPA diagnose trajectories and preserve complementary candidates

GEPA reflects on execution trajectories, proposes prompt mutations and combines complementary candidates from a Pareto frontier. Its paper reports improvement over GRPO across six tasks with up to 35 times fewer rollouts; this is a comparison under the paper's workloads, not a universal cost multiplier. [Paper v2](https://arxiv.org/abs/2507.19457v2).

The current DSPy adapter exposes candidate ancestry, aggregate validation scores, per-instance scores and metric-call counts. The GEPA repository now describes optimization of broader textual artifacts as well as prompts; that current interface should be distinguished from the original prompt experiments. [DSPy adapter](https://github.com/stanfordnlp/dspy/blob/b4beb23d94711857f618042f4e89260b2e8e09b3/dspy/teleprompt/gepa/gepa.py), [GEPA implementation overview](https://github.com/gepa-ai/gepa/blob/8f287de942f41a6d1e0e7e5b2d576247c4bedee9/README.md).

Local hypothesis: a proposed correction should include diagnostic evidence explaining the failure, rather than only a scalar pass rate. Keep per-task outcomes so aggregate gains cannot conceal a weak task class. A Pareto frontier selected on validation data still needs independent final evaluation. Optimizing a judge prompt and optimizing the artifact judged by it must remain separate candidates.

### 4 MIPROv2 a simpler prompt-search comparator

MIPROv2 bootstraps demonstrations, proposes instructions grounded in the program/data, then searches combinations using a surrogate-guided process. The inspected code separates `trainset` from `valset`, periodically evaluates candidates, and returns a selected program. Its validation set is used for optimization; it is not automatically an untouched acceptance test. [Optimizer documentation](https://github.com/stanfordnlp/dspy/blob/b4beb23d94711857f618042f4e89260b2e8e09b3/docs/docs/learn/optimization/optimizers.md), [implementation](https://github.com/stanfordnlp/dspy/blob/b4beb23d94711857f618042f4e89260b2e8e09b3/dspy/teleprompt/mipro_optimizer_v2.py).

This offers a useful comparator to elaborate self-modifying search: hold the workflow fixed and optimize only a small approved instruction or example set. It reduces the number of moving parts and helps identify whether benefits come from better context rather than recursive capability. No optimizer-specific benchmark gain is asserted here. Example quality, metric validity, train/test overlap and optimization expenditure determine whether compilation helps locally. Prompt optimization does not imply weight training, although DSPy's separate `BootstrapFinetune` does update model weights.

### 5 Reflexion memory improves subsequent attempts

Reflexion converts feedback into episodic reflective text that conditions later trials without weight updates. The paper reports 91% HumanEval pass@1 versus an 80% GPT-4 baseline. That headline should not be interpreted as an equal-compute single unassisted attempt: the framework uses trial feedback and reflection, so total attempts and environment access matter. [Paper v4](https://arxiv.org/abs/2303.11366v4).

The repository provides task-specific notebooks, code and logged runs; its README explicitly notes the expense and access constraints of reproducing the original experiments. [Repository](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/README.md).

Local implication: maintain a correction linked to the observed incident, its scope and a later test. An eloquent reflection is a hypothesis, not verified learning. Evaluate recurrence on new tasks and include misleading reflections as negative cases. Keep task-specific retry memory separate from a generally adopted organizational rule. This complements Tessl's correction queue without treating every anecdote as a universal standard.

### 6 TextGrad propagate textual criticism through a computation graph

TextGrad models components as variables and uses natural-language feedback as an analogue of gradients. Its paper demonstrates applications including question answering, code and scientific design, reporting GPQA accuracy moving from 51% to 55% in one setting. These heterogeneous demonstrations support a reusable optimization interface; they do not establish equivalent reliability across domains or recursive governance. [Paper](https://arxiv.org/abs/2406.07496).

The inspected README illustrates `TextLoss`, backward feedback and textual parameter updates, including prompt optimization. [Implementation examples](https://github.com/zou-group/textgrad/blob/75e912e210864b61999781778cdf756d4468120f/README.md).

Local hypothesis: feedback should identify which context or workflow component caused an error, allowing a narrow mutation. Textual criticism can be wrong or correlated with the producing model. Preserve the original observations and test whether the proposed edit helps held-out cases; do not allow a persuasive critique to overwrite canonical authority or acceptance criteria. Scientific application examples are not evidence for adopting the system here.

### 7 ADAS and AFlow search the workflow itself

ADAS's Meta Agent Search programs agents in code using an archive of prior designs. Its paper reports coding, science and mathematics experiments and transfer across models/domains. This expands the search space beyond a fixed prompt, while leaving the meta-search designer/evaluator as important dependencies. [Paper v2](https://arxiv.org/abs/2408.08435v2), [author repository](https://github.com/ShengranHu/ADAS/blob/2702bee8fefda42255efc5be9f60e3bd3db96ae4/README.md).

AFlow searches code-represented workflows with a Monte Carlo tree search variant, execution feedback and predefined operators such as Review, Revise, Ensemble and Test. Its paper reports a 5.7% average improvement across six datasets and a task-specific smaller-model cost comparison. The repository documents separate validation/test artifacts and warns of possible operator bugs from migration. [Paper v4](https://arxiv.org/abs/2410.10762v4), [repository](https://github.com/FoundationAgents/AFlow/blob/3f457218fc716093fe53f6df8a5d5e6379d66346/README.md).

Local implication: only search over explicitly permitted workflow components. Extra critique or ensemble calls can purchase accuracy while increasing total effort. Compare workflow search with a fixed-template baseline under the same observable resource budget. Research benchmark superiority is not evidence that changing role boundaries, approvals or dispatch topology improves this organization.

## Proposed additions and experiments

The following paths are proposals. Existing role ownership, prior evaluator and delivery rules continue to apply.

| Priority and owner | Proposed artifact | Dependencies, evaluation and rollback |
| --- | --- | --- |
| P1: Coordinator; Chief of Staff selects hypotheses | `agent-org/knowledge/improvement-candidates/INDEX.md` and one Markdown record per candidate | Link existing task/run/experiment records; record parent artifact hashes, hypothesis, permitted mutation, observed task classes, all attempts, resource gaps and disposition. Fixture-check a lineage with rejected, interrupted and duplicate branches. Roll back the index consumer through a scoped PR; preserve history. |
| P1: independent Reviewer specifies cases; Developer builds fixtures | `agent-org/factory/benchmarks/behavior/README.md` and task-owned case manifests | Extend Tessl's scenario proposal with development, selection and final held-out partitions, provenance and exposure history. Test overlap detection and a deliberately benchmark-specific candidate. Remove candidate use on leakage; retain consumed tests as development evidence. |
| P2: Architect designs; Developer implements | `agent-org/factory/instrumentation/candidate_archive.py` | Only after the Markdown archive proves useful. Validate parent references, duplicate hashes, missing outcomes and recovery from interrupted search. Keep selection advisory; it cannot promote. Revert the helper and return to manual records if it loses evidence. |
| P2: measurement Reviewer; Coordinator records usage | `agent-org/factory/reports/<experiment>/RESOURCE_ACCOUNT.md` | Account for proposal, evaluation, review, repair and rejected branches, including unknown prices/model metadata. Verify supplied totals against observable receipts. Missing essential telemetry is inconclusive; stop rather than substitute a favorable proxy. |
| P3: Chief of Staff; independent Reviewer and distinct approver | A newly allocated experiment under `agent-org/experiments/` | Test a frozen improvement producer against an evolving producer on fresh organization tasks at matched budget. Depends on trustworthy partitions/lineage and the P1 context experiment. Roll back each promoted artifact to its pinned known-good baseline via corrective PR. |

### First experiment one bounded context mutation

Reuse Tessl's recommended context-manifest experiment before adopting a search framework. Preregister one hypothesis, one mutation surface and one finalist; preserve mandatory startup/authority context in both arms. Development cases may guide mutations, but lock the candidate before final testing. Compare baseline/candidate on at least 20 representative paired organization tasks with randomized ordering, fixed stopping and the unchanged 95% positive benefit bound plus 5% practical efficiency threshold. Twenty pairs are a minimum, not a power guarantee.

Cover research preparation, scoped document work, dependency decisions and interrupted-run recovery. Include stale acceptance prose, misleading tool logs, out-of-scope dependencies and changed candidate identities. Measure effort through independently accepted output, including review and correction; report delivery separately where live authorization exists. Predeclare treatment of failed/blocked tasks and record their costs. No observed authority, evidence, safety or correctness failure is acceptable.

### Prevent search from consuming its own test

Use three roles for data: development feedback, selection validation, and final acceptance. Split by originating incident/task family, not merely paraphrased rows; near-duplicate scenarios can leak the answer across partitions. Record which candidate executions saw which inputs, labels, outputs and critiques. Once a final-test result influences a mutation, that test has become development evidence for descendants. A fresh Reviewer execution alone does not erase that exposure.

Repeatedly selecting the best of many noisy candidates creates selection bias. The existing paired bootstrap does not itself correct for searching many candidates on the same acceptance set. Keep the current gate unchanged: limit search before final testing, pin one finalist, and preregister any multi-candidate comparison design separately. Do not pool task pairs across generations to manufacture the required sample size. Preserve every failed comparison and carry cumulative resources forward.

In this environment holdout separation is procedural. Do not claim a technically secret evaluator while all workers share readable files. Independent ownership, access manifests and receipt-backed grading improve assurance within that limit. Any future evaluator change remains a separate candidate under previous rules, fixed adversarial fixtures and dual-version replay.

### Test recursive benefit as an additional claim

After a single change qualifies, compare a static baseline improvement producer against the candidate producer on fresh improvement opportunities. Hold allowed mutation surface, tools, workload difficulty, model configuration and proposal/evaluation budget fixed. Evaluate descendants independently for correctness, efficiency and authority adherence. Record useful qualified improvements per total observable effort alongside downstream task performance; distinguish failed proposals from missing observations.

A two-generation trial can demonstrate a bounded recurrence of benefit. It cannot establish indefinite acceleration or organization-wide reliability. Compare equal-budget alternatives, including a simpler fixed prompt search; DGM's archive is useful inspiration without being a reason to run an expensive evolutionary campaign. Unknown token/cost telemetry stays unknown. Before expenditure, state a break-even horizon: expected later task savings must justify proposal, evaluation, review and maintenance effort. If required sampling cannot fit the existing cumulative budget, checkpoint and replan; do not weaken thresholds or reset counters.

## Evidence boundaries and reproducibility

Primary-source register (all accessed on the research date):

| System | Observed primary publication revision | Implementation evidence |
| --- | --- | --- |
| DGM | Paper v3, 12 March 2026; Sakana account, 30 May 2025 | Author README and outer loop; pinned links above |
| AlphaEvolve / OpenEvolve | DeepMind account, 14 May 2025 | OpenEvolve database and evaluator; separate implementation |
| GEPA | Paper v2, 14 February 2026 | GEPA README and DSPy adapter |
| MIPROv2 | Current DSPy source/docs at `b4beb23d94711857f618042f4e89260b2e8e09b3` | Optimizer initialization and compilation stages |
| Reflexion | Paper v4, 10 October 2023 | Author repository README |
| TextGrad | arXiv v1, 11 June 2024 | Author repository examples |
| ADAS / AFlow | ADAS v2, 2 March 2025; AFlow v4, 15 April 2025 | Author repository READMEs |

Primary paper pages, author/vendor accounts and public repositories were read; no experiment here was reproduced. DGM methods, evaluation and cost sections received full-text inspection. Reflexion, TextGrad, ADAS and AFlow numerical/mechanism claims were checked against primary abstract pages; their full experimental appendices and external raw logs were not audited. GitHub source was inspected through read tools. Code claims are based on the named files; ADAS, AFlow, Reflexion and TextGrad received README/example-level inspection, not a full implementation audit. AlphaEvolve's proprietary runtime was not inspected. Public results do not supply local task distributions, independent raw cost receipts or production failure denominators.

Repository links pin the observed commit; file receipts additionally identified DGM outer-loop blob `2c87f4bdc303d0ab3c4ad2333b03ecf0a74392be`, OpenEvolve database `ab1dad21b9879c0783873108cfc084dc3b0017e8`, evaluator `084d1c04ca41b22407c4ecf4227a69539f6379dc`, DSPy GEPA `c202c0c9d42af7f346acedc2f0bf580441e36514` and MIPRO `0d7c6f6883a6f9c1b8c95cecadc3e0e118637c4d`. Local gate SHA-256 was `b85841b308ebe73cb0dcd9b33e9672ccc87eee1767c4e64eae5a2f7b62aa9c60`; Tessl report SHA-256 was `64da9988873e20cf21ae96c0697848260b8333e49f9a823c04f386066cd11875`.

Two guessed GitHub paths returned 404 (the DGM owner and AFlow root optimizer path); canonical author links corrected the DGM source, and AFlow claims remain limited to its paper/README. GEPA's full HTML exceeded the browsing size limit; its abstract, repository overview and DSPy adapter were inspected instead. Public reads were the only external effects. No installation, provider enrollment, remote mutation, paid experiment or policy/evaluator change occurred.
