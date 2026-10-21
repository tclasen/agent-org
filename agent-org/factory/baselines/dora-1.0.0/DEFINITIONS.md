# DORA definitions 1.0.0

Task: TASK-000004. Requirements: REQ-000025, REQ-000026. Approved authority: APP-000001; approved-v0.1 Domain O. This is deterministic calculation tooling, without a runtime, production integration, or inferred LLM measurements. All checked-in observations are synthetic. No production service is enrolled; the live classification file deliberately has no services.

Run from the repository root with Python 3.11+:

```sh
python3 agent-org/factory/dora/calculator.py agent-org/factory/dora/fixtures/events.json agent-org/factory/dora/fixtures/classification.json --start 2026-01-02T00:00:00Z --end 2026-01-03T00:00:00Z
python3 -m unittest discover -s agent-org/factory/tests -p 'test_dora.py' -v
```

The first command prints canonical, sorted compact JSON. Compare it byte for byte with fixtures/expected.json (including the CLI's final newline). No clock is read. End is required; start defaults to exactly 30 days before end. All timestamps require timezone offsets and normalize to UTC; windows are half-open [start,end). Explicit `--as-of N` selects ingestion sequences ≤N, and `--followup-until` sets the observation cutoff (default end, never earlier than end).

The Python API is `calculate(events, classification, start=None, end=..., as_of=None, followup_until=None, definition_version="1.0.0", definition_digest=None, classification_digest=None)`. `canonical_json`, `digest`, `replay`, and `ledger_events` are also available. Imports require no event store or third-party packages.

## Explicit classification input

Classification is an object with immutable semantic `version`, an explicit `observation_kind` label (checked-in fixtures say synthetic), and `services`, mapping immutable service ID to `project_id`, `environments` (explicit environment-name → development/test/staging/production), `production_threshold` (fraction >0 and ≤1), `health_criteria` (named enrolled health contract), and `stabilization_seconds` (nonnegative). Unknown services, projects and environments are health gaps and never production. There is no repository-name inference. The synthetic classification uses intended traffic 1.0, named all-required-probes-green health, and 1800 seconds stabilization; those values do not configure a real service.

## Normalized event schema

Input is a JSON array. Each envelope contains exactly these fields: `schema_version` (1; omission means 1), `event_id` (nonempty immutable string), `type`, `occurred_at` (offset-aware ISO 8601), `sequence` (positive ingestion integer), `provenance` (nonempty authoritative source reference), and `payload` (object). Each ordinary payload includes exact `project_id` and `service_id`. Unsupported schema versions/types and unknown envelope fields reject the entire calculation. Source references are required but are not authenticated by the calculator.

| Type | Additional payload fields | Semantics |
| --- | --- | --- |
| commit | commit_id, committed_at | Original Git committer timestamp from commit object, never author/detection time |
| build | build_id, commit_ids (nonempty list) | Explicit commit identities used by this build |
| artifact | artifact_id, build_id | Artifact identity and originating build |
| deployment | deployment_id, artifact_id, environment, traffic (0..1), healthy (boolean), health_evidence, health_criteria | Rollout observation; qualifies only at threshold and matching service health contract |
| failure | failure_id, deployment_id, degradation_started_at, causal_evidence | Explicit source-backed causal failure link; occurred_at is observation/detection, separately preserved |
| recovery | failure_id, healthy_since, confirmed_at, healthy, health_evidence, health_criteria | Explicit continuous-health evidence from healthy_since through confirmed_at, meeting enrolled stabilization interval |
| correction | target_event_id, replacement | Full replacement normalized envelope without sequence; same target event_id/type; source correction gets its own envelope ID/sequence/provenance |

Deployment payload may additionally include `rework_kind` (`rollback`, `fixforward`, `remediation`), `unplanned: true`, and `remediates_deployment_id`. All three must support an explicit prior failed deployment for rework credit. Planned work receives no rework classification. Rollbacks and redeployments have new actual rollout IDs and count as deployments; transport retries and incremental health/traffic observations retain their rollout ID. Its immutable artifact/environment/rework identity cannot change. The first qualifying observation sets the rollout's production timestamp. Health/traffic progress cannot generate extra rollouts.

The canonical chain is service/project → commit → build → artifact → rollout → causal failure → confirmed recovery, with explicit remediation → prior failed rollout. A fix-forward can introduce new commits. A rollback of previously introduced commits creates no duplicate lead-time samples. Missing attribution is reported rather than guessed. Negative lead duration or impossible build/artifact, impairment/recovery or remediation chronology rejects input.

A service/commit/build/artifact/failure identity cannot have conflicting payloads. Identical event ID and canonical content are idempotent, including a repeated ingestion with a different sequence; earliest sequence wins. Conflicting event-ID payload or ingestion-sequence ownership rejects input. Distinct event IDs observing the same immutable rollout are collapsed to the first qualifying observation. Corrections append only, reference an earlier original event, and may themselves be followed by another correction of that original. An ingestion sequence is availability, not source-event chronological order. Out-of-order and late source events therefore replay deterministically.

The native ledger adapter accepts only schema_version 1, projects `event_type`/`data` to `type`/`payload`, and extracts `data.provenance`. `--ledger` accepts a JSON array of already verified ledger rows; the calculator does not authenticate ledger chain hashes. Verify through EventStore before projecting. Native correction replacements `{event_type,occurred_at,data}` are projected with the target identity. The adapter does not fetch external systems or make unsupported ingestion claims.

## Metric contract

| Metric | Cohort and numerator | Denominator/output |
| --- | --- | --- |
| Change lead time | Per service/commit first qualifying production introduction in window, minus original committer timestamp | Nearest-rank p50/p90 seconds, sorted samples, sample size and missing attribution count; history before the window prevents redeploy double count |
| Deployment frequency | Distinct qualifying rollout IDs first qualifying in window | Exact window seconds/86400; expose count and days |
| Change fail rate | Distinct qualifying cohort rollout IDs with explicit attributed production failures observed by follow-up cutoff | All qualifying rollout IDs in deployment cohort; repeated failures count rollout once |
| Failed-deployment recovery time | Failures with attributed impairment onset in window; confirmation minus onset | Nearest-rank p50/p90 seconds, sample size; disclose unresolved/censored failure IDs and count; unresolved never becomes zero |
| Deployment rework rate | Qualifying unplanned, causally linked rollback/fixforward/remediation rollout IDs in window | All qualifying rollout IDs in window, with numerator classifications |

No observations or no duration samples produce unavailable/null. Empty deployment frequency is zero only when the service classification explicitly supplies source-backed `observation_coverage` with start/end spanning the window, `available_at_sequence` no later than the as-of snapshot, and nonempty provenance. Without that declaration an empty window remains unavailable; absence of rows cannot establish zero deployments. Ratio denominators of zero remain unavailable. A measured zero numerator with a nonzero denominator remains zero. Missing health, environment, chain, causality or recovery evidence appears in measurement_health and duration missing fields. Values describe only observed qualifying evidence and must be read with that health report; incomplete source coverage does not establish the absence of incidents. p50/p90 use sorted[ceil(p*n)-1]. No interpolation or time-only failure inference occurs.

Reports bind calculator version, definition version/digest, classification version/digest, selected as-of sequence and input snapshot digest. Snapshots sort by ingestion sequence/event ID independently of input list order. Corrections and late data create new snapshot digests. Reusing an old snapshot and version reproduces the old bytes. Retain input snapshots, definitions and classification artifacts alongside report digests; a digest cannot reconstruct deleted input. Version 1.0.0 is the only installed definition; unsupported versions and mismatched requested definition/classification digests reject. New semantics must add a version and retain the old implementation, never replace its meaning. The general immutable-version validator is available in quality-gates/improvement.py; the same registry discipline applies to classification releases.

D-01–D-13 map directly to named tests in tests/test_dora.py. This evidence tests the synthetic contract; source authenticity, live completeness and service enrollment remain separate obligations.
