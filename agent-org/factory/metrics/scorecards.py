"""Separate deterministic organization, project, and measurement-health scorecards.

Inputs are explicit normalized observations, not inferred labels or model scores.
Unknown fields remain unavailable. No composite organization/project score exists.
"""
import json
import math


def _observed_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value >= 0


def _rate(numerator, denominator, total):
    return {"numerator": numerator, "denominator": denominator,
            "value": numerator / denominator if denominator else None,
            "coverage": {"observed": denominator, "total": total}}


def _binary(records, key):
    known = [record[key] for record in records if type(record.get(key)) is bool]
    return _rate(sum(known), len(known), len(records))


def _measurement(records, key):
    values = [record[key] for record in records if _observed_number(record.get(key))]
    return {"observations": len(values), "missing": len(records) - len(values),
            "total": sum(values) if values else None,
            "mean": sum(values) / len(values) if values else None}


def scorecards(organization, projects, measurement_health):
    """Records must include attempts/retries separately; caller supplies census.

    Organization rows: task_class, configuration (model/reasoning descriptor),
    expected_route/actual_route, delegation_attempt, accepted, latency_seconds,
    observed_cost, requirements_total/requirements_covered, unauthorized_deviation,
    replan_cause, handoff_complete, recovery_resumed, retained_scenario_failed,
    rework. Projects maps immutable project ID to explicit dimension bool/null.
    """
    if not isinstance(organization, list) or not isinstance(projects, dict) or not isinstance(measurement_health, dict):
        raise ValueError("explicit organization list, project mapping and health mapping required")
    routes = [row for row in organization if isinstance(row.get("expected_route"), str) and row["expected_route"] and isinstance(row.get("actual_route"), str)]
    delegations = [row for row in organization if row.get("delegation_attempt") is True]
    groups = {}
    for row in organization:
        key = (row.get("task_class"), row.get("configuration"))
        if not all(isinstance(value, str) and value for value in key):
            key = ("unknown", "unknown")
        groups.setdefault(key, []).append(row)
    models = []
    for (task_class, configuration), rows in sorted(groups.items()):
        observable = [row for row in rows if type(row.get("accepted")) is bool and _observed_number(row.get("observed_cost"))]
        costs = sum(row["observed_cost"] for row in observable)
        models.append({"task_class": task_class, "configuration": configuration,
                       "acceptance": _binary(rows, "accepted"), "latency_seconds": _measurement(rows, "latency_seconds"),
                       "observed_cost": _measurement(rows, "observed_cost"),
                       "accepted_per_observed_cost": {"accepted": sum(row["accepted"] for row in observable),
                            "cost": costs if observable else None, "comparable_observations": len(observable),
                            "value": sum(row["accepted"] for row in observable) / costs if costs > 0 else None}})
    coverage_rows = [row for row in organization if type(row.get("requirements_total")) is int and type(row.get("requirements_covered")) is int and 0 <= row["requirements_covered"] <= row["requirements_total"]]
    dimensions = ("requirement_satisfaction", "correctness", "security", "reliability", "maintainability",
                  "escaped_defects", "delivery_efficiency", "rework", "user_acceptance")
    project_cards = {}
    for project_id, observations in sorted(projects.items()):
        if not isinstance(project_id, str) or not project_id or not isinstance(observations, list):
            raise ValueError("project identity and observation list required")
        project_cards[project_id] = {dimension: _binary(observations, dimension) for dimension in dimensions}
    return {"version": "1.0.0", "organization": {
        "routing_accuracy": _rate(sum(row["expected_route"] == row["actual_route"] for row in routes), len(routes), len(organization)),
        "delegation_acceptance": _binary(delegations, "accepted"), "rework": _binary(organization, "rework"),
        "by_task_class_configuration": models,
        "planning_requirement_coverage": {**_rate(sum(row["requirements_covered"] for row in coverage_rows), sum(row["requirements_total"] for row in coverage_rows), len(organization)),
            "coverage": {"observed": len(coverage_rows), "total": len(organization)}},
        "unauthorized_deviations": _binary(organization, "unauthorized_deviation"),
        "replan_causes": sorted(row["replan_cause"] for row in organization if isinstance(row.get("replan_cause"), str)),
        "handoff_completeness": _binary(organization, "handoff_complete"),
        "independent_recovery_success": _binary(organization, "recovery_resumed"),
        "retained_scenario_failures": _binary(organization, "retained_scenario_failed")},
        "projects": project_cards, "measurement_health": json.loads(json.dumps(measurement_health, allow_nan=False))}
