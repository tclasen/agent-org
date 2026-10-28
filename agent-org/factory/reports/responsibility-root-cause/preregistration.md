# Preregistered qualification

```json
{
  "baseline": "306557c",
  "cases_sha256": "32fc103524e7bbef7cbfea8a5be9cdd39bdaebd8a3c777d58915b681ef42b12d",
  "scenarios_sha256": "46c2b33e585cbeef67e65f46e496ac93b1e5371b55564bdd6d5b495d103a8462",
  "claim": "bounded deterministic instruction repair only; no stochastic benefit or universal prevention claim",
  "observed_baseline_failure": "sanitized incident and control-escape analysis in baseline-diagnosis.md; replay may independently succeed",
  "stopping_rule": "one baseline and one candidate replay over all12cases; retain all outcomes, diagnose at most2retries, changes invalidate affected evidence",
  "prior_evaluator": "policies/SELF_IMPROVEMENT.md and policies/MEASUREMENT_INDEPENDENCE.md at baseline306557c; unchanged stochastic thresholds"
}
```
