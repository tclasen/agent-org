"""Deterministic DORA v1; pure calculation, never infers service facts or causality."""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timezone, timedelta
import hashlib
import json
import math
import re
from pathlib import Path

CALCULATOR_VERSION = "1.0.1"
DEFINITIONS = {
    "1.0.1": {
        "version": "1.0.1", "window": "UTC [start,end)",
        "lead_time": "committer to first qualifying production per service/commit",
        "frequency": "distinct qualifying rollout IDs / exact window days",
        "failure_rate": "causally failed qualifying rollout IDs / cohort IDs",
        "recovery": "confirmed stabilized recovery minus impairment onset; onset cohort",
        "rework": "explicit unplanned rollback/fixforward/remediation / cohort IDs",
        "percentiles": "nearest-rank seconds; p50 and p90", "empty": "unavailable",
    }
}
TYPES = {"commit", "build", "artifact", "deployment", "failure", "recovery", "correction"}


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be an offset-aware ISO string")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("invalid timestamp") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("timestamp requires timezone")
    return result.astimezone(timezone.utc)


def utc(value):
    return value.isoformat().replace("+00:00", "Z")


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def require_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"missing/invalid {label}")
    return value


def ledger_events(records):
    """Project native v1 ledger entries. Store verification remains caller's duty."""
    result = []
    for record in records:
        if type(record.get("schema_version")) is not int or record["schema_version"] != 1:
            raise ValueError("unsupported ledger schema")
        data = copy.deepcopy(record["data"])
        provenance = data.pop("provenance", None)
        if record["event_type"] == "correction":
            replacement = data.get("replacement")
            if replacement and "event_type" in replacement:
                replacement = copy.deepcopy(replacement)
                replacement_data = replacement["data"]
                data["replacement"] = {
                    "event_id": data["target_event_id"], "type": replacement["event_type"],
                    "occurred_at": replacement["occurred_at"],
                    "payload": {k: v for k, v in replacement_data.items() if k != "provenance"},
                    "provenance": replacement_data.get("provenance"), "schema_version": 1,
                }
        result.append({"schema_version": 1, "event_id": record["event_id"],
                       "type": record["event_type"], "occurred_at": record["occurred_at"],
                       "sequence": record["sequence"], "payload": data,
                       "provenance": provenance})
    return result


def _validate_event(event):
    if set(event) - {"schema_version", "event_id", "type", "occurred_at", "sequence", "payload", "provenance"}:
        raise ValueError("unknown normalized envelope field")
    if type(event.get("schema_version", 1)) is not int or event.get("schema_version", 1) != 1 or event.get("type") not in TYPES:
        raise ValueError("unsupported event schema/type")
    require_text(event.get("event_id"), "event_id")
    timestamp(event.get("occurred_at"))
    require_text(event.get("provenance"), "provenance")
    if not isinstance(event.get("payload"), dict):
        raise ValueError("payload must be an object")
    if type(event.get("sequence")) is not int or event["sequence"] <= 0:
        raise ValueError("sequence must be positive integer")
    canonical_json(event)


def replay(events, as_of=None):
    if as_of is not None and (type(as_of) is not int or as_of < 0):
        raise ValueError("as_of must be nonnegative ingestion sequence")
    identities, sequences = {}, {}
    for original in events:
        event = copy.deepcopy(original)
        _validate_event(event)
        if as_of is not None and event["sequence"] > as_of:
            continue
        identity = {k: v for k, v in event.items() if k != "sequence"}
        prior = identities.get(event["event_id"])
        if prior and {k: v for k, v in prior.items() if k != "sequence"} != identity:
            raise ValueError("conflicting duplicate event_id")
        if event["sequence"] in sequences and sequences[event["sequence"]] != event["event_id"]:
            raise ValueError("conflicting ingestion sequence")
        sequences[event["sequence"]] = event["event_id"]
        if not prior or event["sequence"] < prior["sequence"]:
            identities[event["event_id"]] = event
    snapshot = sorted(identities.values(), key=lambda e: (e["sequence"], e["event_id"]))
    active = {}
    for event in snapshot:
        if event["type"] != "correction":
            active[event["event_id"]] = event
            continue
        data = event["payload"]
        target = data.get("target_event_id")
        if target not in active:
            raise ValueError("correction must reference an earlier non-correction event")
        replacement = copy.deepcopy(data.get("replacement"))
        if not isinstance(replacement, dict):
            raise ValueError("correction requires full replacement")
        replacement["sequence"] = active[target]["sequence"]
        if replacement.get("event_id") != target or replacement.get("type") != active[target]["type"]:
            raise ValueError("correction cannot change target identity or type")
        _validate_event(replacement)
        active[target] = replacement
    return list(active.values()), snapshot


def _classify(classification):
    require_text(classification.get("version"), "classification version")
    if not re.fullmatch(r"\d+\.\d+\.\d+", classification["version"]):
        raise ValueError("classification semantic version required")
    services = classification.get("services")
    if not isinstance(services, dict):
        raise ValueError("services must be explicit mapping")
    for service, config in services.items():
        require_text(service, "service_id")
        require_text(config.get("project_id"), "project_id")
        require_text(config.get("health_criteria"), "health_criteria")
        if not isinstance(config.get("environments"), dict) or any(v not in {"development", "test", "staging", "production"} for v in config["environments"].values()):
            raise ValueError("invalid explicit environment mapping")
        threshold = config.get("production_threshold")
        stabilization = config.get("stabilization_seconds")
        if not finite_number(threshold) or not 0 < threshold <= 1:
            raise ValueError("service production_threshold must be in (0,1]")
        if not finite_number(stabilization) or stabilization < 0:
            raise ValueError("invalid stabilization interval")
    return services


def _distribution(samples, missing=0):
    samples = sorted(samples)
    return {"samples_seconds": samples, "sample_size": len(samples), "missing": missing,
            "p50_seconds": samples[math.ceil(.5 * len(samples)) - 1] if samples else None,
            "p90_seconds": samples[math.ceil(.9 * len(samples)) - 1] if samples else None,
            "status": "partial" if samples and missing else "available" if samples else "unavailable"}


def _ratio(numerator, denominator):
    return {"numerator": numerator, "denominator": denominator,
            "value": numerator / denominator if denominator else None,
            "status": "available" if denominator else "unavailable"}


def calculate(events, classification, start=None, end=None, *, as_of=None,
              followup_until=None, definition_version="1.0.1", definition_digest=None, classification_digest=None):
    if definition_version not in DEFINITIONS:
        raise ValueError("unsupported definition version")
    definition = DEFINITIONS[definition_version]
    if definition_digest is not None and digest(definition) != definition_digest:
        raise ValueError("definition version content mismatch")
    if end is None:
        raise ValueError("explicit end required; no current-clock dependency")
    end = timestamp(end)
    start = timestamp(start) if start else end - timedelta(days=30)
    followup = timestamp(followup_until) if followup_until else end
    if start >= end or followup < end:
        raise ValueError("invalid window/follow-up cutoff")
    if classification_digest is not None and digest(classification) != classification_digest:
        raise ValueError("classification version content mismatch")
    services = _classify(classification)
    active, snapshot = replay(events, as_of)
    issues = []
    available_sequence = as_of if as_of is not None else max((e["sequence"] for e in snapshot), default=0)
    tables = {kind: {} for kind in TYPES if kind != "correction"}
    key_names = {"commit": "commit_id", "build": "build_id", "artifact": "artifact_id",
                 "deployment": "deployment_id", "failure": "failure_id", "recovery": "failure_id"}
    for event in active:
        data, kind = event["payload"], event["type"]
        service = data.get("service_id")
        config = services.get(service)
        if config is None or data.get("project_id") != config["project_id"]:
            issues.append({"event_id": event["event_id"], "reason": "unknown_service_or_project"})
            continue
        key = (service, require_text(data.get(key_names[kind]), key_names[kind]))
        prior = tables[kind].get(key)
        if prior:
            if kind == "deployment":
                # Immutable rollout identity; progress/retry observations may differ
                # in health/traffic/time, but never create an additional rollout.
                immutable = ("project_id", "service_id", "deployment_id", "artifact_id", "environment",
                             "rework_kind", "unplanned", "remediates_deployment_id")
                if any(prior["payload"].get(field) != data.get(field) for field in immutable):
                    raise ValueError("conflicting logical deployment identity")
                prior.setdefault("observations", []).append(event)
            elif prior["payload"] != data or timestamp(prior["occurred_at"]) != timestamp(event["occurred_at"]):
                raise ValueError(f"conflicting logical {kind} identity")
        else:
            tables[kind][key] = copy.deepcopy(event)
    outputs = {}
    for service, config in sorted(services.items()):
        def issue(event, reason):
            issues.append({"event_id": event["event_id"], "reason": reason})
        deployments = {}
        for (svc, deployment_id), initial in tables["deployment"].items():
            if svc != service:
                continue
            observations = sorted([initial] + initial.get("observations", []), key=lambda e: (timestamp(e["occurred_at"]), e["event_id"]))
            for event in observations:
                if timestamp(event["occurred_at"]) > followup:
                    continue
                data = event["payload"]
                environment = config["environments"].get(data.get("environment"))
                if environment is None:
                    issue(event, "unknown_environment")
                    continue
                if environment != "production":
                    continue
                traffic = data.get("traffic")
                if not finite_number(traffic) or not 0 <= traffic <= 1 or type(data.get("healthy")) is not bool or not isinstance(data.get("health_evidence"), str) or not data["health_evidence"] or data.get("health_criteria") != config["health_criteria"]:
                    issue(event, "missing_or_invalid_rollout_health")
                    continue
                if data["healthy"] and traffic >= config["production_threshold"]:
                    deployments[deployment_id] = event
                    break
        cohort = {key: event for key, event in deployments.items() if start <= timestamp(event["occurred_at"]) < end}
        first, missing_lead = {}, 0
        for deployment_id, event in sorted(deployments.items(), key=lambda item: (timestamp(item[1]["occurred_at"]), item[0])):
            data = event["payload"]
            artifact = tables["artifact"].get((service, data.get("artifact_id")))
            build = tables["build"].get((service, artifact["payload"].get("build_id"))) if artifact else None
            commit_ids = build["payload"].get("commit_ids") if build else None
            if not isinstance(commit_ids, list) or not commit_ids or not all(isinstance(c, str) and c for c in commit_ids):
                issue(event, "missing_commit_build_artifact_chain")
                missing_lead += deployment_id in cohort
                continue
            for commit_id in sorted(set(commit_ids)):
                commit = tables["commit"].get((service, commit_id))
                if not commit or not commit["payload"].get("committed_at"):
                    issue(event, "missing_commit_provenance")
                    missing_lead += deployment_id in cohort
                    continue
                committed = timestamp(commit["payload"]["committed_at"])
                introduced = timestamp(event["occurred_at"])
                if committed > introduced:
                    raise ValueError("negative commit lead time")
                # Records may arrive out of order; their source chain must be chronological.
                if timestamp(build["occurred_at"]) < committed or timestamp(artifact["occurred_at"]) < timestamp(build["occurred_at"]) or introduced < timestamp(artifact["occurred_at"]):
                    raise ValueError("impossible commit/build/artifact/deployment chronology")
                first.setdefault(commit_id, (introduced, (introduced - committed).total_seconds()))
        failures = {}
        for (svc, failure_id), event in tables["failure"].items():
            if svc != service or timestamp(event["occurred_at"]) > followup:
                continue
            data = event["payload"]
            deployment_id = data.get("deployment_id")
            if deployment_id not in deployments or not data.get("causal_evidence") or not isinstance(data.get("causal_evidence"), str):
                issue(event, "missing_failure_causality")
                continue
            if not data.get("degradation_started_at"):
                issue(event, "missing_degradation_onset")
                continue
            onset = timestamp(data["degradation_started_at"])
            if onset < timestamp(deployments[deployment_id]["occurred_at"]) or onset > timestamp(event["occurred_at"]):
                raise ValueError("impossible degradation chronology")
            failures[failure_id] = event
        # Recovery cannot establish its own failure or deployment causality.
        # Disclose unmatched or rejected failure links without inventing samples.
        for (svc, failure_id), recovery in tables["recovery"].items():
            if svc == service and timestamp(recovery["occurred_at"]) <= followup and failure_id not in failures:
                issue(recovery, "missing_failure_causality")
        recovery_samples, unresolved, rework = [], [], []
        for failure_id, failure in failures.items():
            onset = timestamp(failure["payload"]["degradation_started_at"])
            if not start <= onset < end:
                continue
            recovery = tables["recovery"].get((service, failure_id))
            valid = False
            if recovery and timestamp(recovery["occurred_at"]) <= followup:
                data = recovery["payload"]
                if data.get("healthy") is True and data.get("health_criteria") == config["health_criteria"] and isinstance(data.get("health_evidence"), str) and data["health_evidence"] and data.get("healthy_since") and data.get("confirmed_at"):
                    healthy, confirmed = timestamp(data["healthy_since"]), timestamp(data["confirmed_at"])
                    if healthy < onset or confirmed < healthy or confirmed > timestamp(recovery["occurred_at"]):
                        raise ValueError("impossible recovery chronology")
                    valid = confirmed <= followup and (confirmed - healthy).total_seconds() >= config["stabilization_seconds"]
                    if valid:
                        recovery_samples.append((confirmed - onset).total_seconds())
                if not valid:
                    issue(recovery, "unconfirmed_or_unstabilized_recovery")
            if not valid:
                unresolved.append(failure_id)
        failed_deployments = {event["payload"]["deployment_id"] for event in failures.values()}
        for deployment_id, event in cohort.items():
            data = event["payload"]
            kind = data.get("rework_kind")
            if kind is None:
                continue
            cause = data.get("remediates_deployment_id")
            if kind not in {"rollback", "fixforward", "remediation"} or data.get("unplanned") is not True or cause not in failed_deployments:
                issue(event, "invalid_rework_classification_or_causality")
                continue
            cause_event = deployments[cause]
            if timestamp(cause_event["occurred_at"]) >= timestamp(event["occurred_at"]):
                raise ValueError("rework must follow failed deployment")
            if not any(f["payload"]["deployment_id"] == cause and timestamp(f["payload"]["degradation_started_at"]) <= timestamp(event["occurred_at"]) for f in failures.values()):
                raise ValueError("rework precedes attributed degradation")
            rework.append({"deployment_id": deployment_id, "kind": kind, "remediates_deployment_id": cause})
        samples = [duration for introduced, duration in first.values() if start <= introduced < end]
        days = (end - start).total_seconds() / 86400
        coverage = config.get("observation_coverage")
        coverage_complete = False
        if coverage is not None:
            if not isinstance(coverage, dict) or type(coverage.get("available_at_sequence")) is not int or coverage["available_at_sequence"] < 0:
                raise ValueError("invalid observation coverage availability")
            require_text(coverage.get("provenance"), "coverage provenance")
            coverage_start, coverage_end = timestamp(coverage.get("start")), timestamp(coverage.get("end"))
            if coverage_start >= coverage_end:
                raise ValueError("invalid observation coverage interval")
            coverage_complete = coverage_start <= start and coverage_end >= end and coverage["available_at_sequence"] <= available_sequence
        outputs[service] = {
            "project_id": config["project_id"], "deployment_ids": sorted(cohort),
            "lead_time": _distribution(samples, missing_lead),
            "deployment_frequency": {"count": len(cohort), "window_days": days,
                                     "per_day": len(cohort) / days if cohort or coverage_complete else None,
                                     "coverage_complete": coverage_complete,
                                     "status": "available" if cohort or coverage_complete else "unavailable"},
            "change_fail_rate": _ratio(len(set(cohort) & failed_deployments), len(cohort)),
            "failed_deployment_recovery_time": {**_distribution(recovery_samples, len(unresolved)), "unresolved_failure_ids": sorted(unresolved)},
            "deployment_rework_rate": {**_ratio(len(rework), len(cohort)), "classifications": sorted(rework, key=lambda r: r["deployment_id"])},
        }
    return {"calculator_version": CALCULATOR_VERSION, "definition_version": definition_version,
            "definition_digest": digest(definition), "classification_version": classification["version"],
            "classification_digest": digest(classification), "snapshot_digest": digest(snapshot),
            "as_of_sequence": as_of if as_of is not None else max((e["sequence"] for e in snapshot), default=0),
            "window": {"start": utc(start), "end": utc(end), "followup_until": utc(followup)},
            "services": outputs, "measurement_health": {"issues": sorted(issues, key=lambda i: (i["event_id"], i["reason"])),
                "input_events": len(snapshot), "active_events": len(active), "status": "partial" if issues else "complete"},
            "observation_kind": classification.get("observation_kind", "unverified_caller_supplied_telemetry")}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("events", type=Path)
    parser.add_argument("classification", type=Path)
    parser.add_argument("--end", required=True)
    parser.add_argument("--start")
    parser.add_argument("--as-of", type=int)
    parser.add_argument("--followup-until")
    parser.add_argument("--definition-version", default="1.0.1")
    parser.add_argument("--ledger", action="store_true", help="project already-verified native v1 ledger JSON array")
    args = parser.parse_args(argv)
    try:
        events = json.loads(args.events.read_text())
        if args.ledger:
            events = ledger_events(events)
        result = calculate(events, json.loads(args.classification.read_text()), args.start, args.end,
                           as_of=args.as_of, followup_until=args.followup_until,
                           definition_version=args.definition_version)
        print(canonical_json(result))
        return 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f"DORA input rejected: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
