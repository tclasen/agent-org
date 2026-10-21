"""Evidence gate v1. Validates a proposal; never dispatches, approves or merges work."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import random
import re
from datetime import datetime, timezone

VERSION = "1.0.1"
HARD_GUARDRAILS = {"scope_authority", "evidence_integrity", "required_tests", "independent_review",
                   "critical_correctness", "security", "acceptance_traceability", "project_correctness"}
PINS = ("baseline", "candidate", "workload", "evaluator", "criteria")


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def evaluator_digest():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _time(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timezone required")
    return result.astimezone(timezone.utc)


def _number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def immutable_versions(existing, proposed):
    """Check a retained version→content-digest map before adding a version."""
    result = dict(existing)
    for version, content in proposed.items():
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            raise ValueError("semantic version required")
        content_hash = digest(content)
        if version in result and result[version] != content_hash:
            raise ValueError("semantic version is immutable")
        result[version] = content_hash
    return result


def register(specification, artifacts):
    """Return a predeclaration. Persist its digest BEFORE execution (external duty)."""
    plan = json.loads(canonical_json(specification))
    for name in PINS:
        plan[name + "_hash"] = digest(artifacts[name])
    plan["evaluator_code_hash"] = evaluator_digest()
    plan["hypothesis_hash"] = digest(plan.get("hypothesis"))
    return plan


def paired_interval(differences, seed, samples=2000):
    """Fixed-seed percentile bootstrap of paired mean differences, 95% interval."""
    rng = random.Random(seed)
    count = len(differences)
    means = sorted(sum(differences[rng.randrange(count)] for _ in range(count)) / count
                   for _ in range(samples))
    return [means[math.ceil(.025 * samples) - 1], means[math.ceil(.975 * samples) - 1]]


def _evaluate(plan, evidence, approvals, context):
    """Return pass/reject/inconclusive, exact digests and bounded benefit evidence.

    Context is an independently supplied trust input, NOT an authority created by
    this program. A pass means eligible for governed PR promotion only.
    """
    rejected, missing = [], []
    details = {}
    def require(mapping, key, label=None):
        value = mapping.get(key)
        if value is None or value == "" or value == []:
            missing.append(label or key)
            return None
        return value
    def mismatch(condition, reason):
        if condition:
            rejected.append(reason)
    required_plan = ("version", "registered_at", "hypothesis", "hypothesis_hash", "scope", "claim",
                     "task_class", "expected_benefit", "target_metric", "direction", "implementer",
                     "candidate_head", "guardrails", "budget", "rollback", "stopping_rule",
                     "changes_evaluator", "evaluator_code_hash") + tuple(n + "_hash" for n in PINS)
    for field in required_plan:
        require(plan, field, "plan." + field)
    mismatch("version" in plan and plan["version"] != VERSION, "unsupported gate version")
    mismatch("scope" in plan and plan["scope"] != "organization", "organization gate cannot grant project authority")
    mismatch("claim" in plan and plan["claim"] not in {"repair", "outcome", "efficiency"}, "unsupported claim")
    mismatch("direction" in plan and plan["direction"] not in {"higher", "lower"}, "invalid metric direction")
    mismatch("hypothesis_hash" in plan and "hypothesis" in plan and plan["hypothesis_hash"] != digest(plan["hypothesis"]), "hypothesis changed")
    mismatch("guardrails" in plan and not HARD_GUARDRAILS.issubset(set(plan["guardrails"])), "hard guardrails removed")
    context_fields = ("approved_baseline_hash", "approved_evaluator_hash", "approved_evaluator_code_hash",
                      "current_candidate_hash", "current_head", "authority_hash", "prior_consumed_seconds",
                      "prior_consumed_storage_bytes", "limits", "active_experiments", "registered_plan_hash", "authorized_approvers")
    for field in context_fields:
        require(context, field, "context." + field)
    for field in ("started_at", "completed_at", "plan_hash", "artifacts", "guardrails", "usage", "authority_hash"):
        require(evidence, field, "evidence." + field)
    if context.get("registered_plan_hash"):
        mismatch(context["registered_plan_hash"] != digest(plan), "durably registered plan changed")
    if context.get("approved_baseline_hash") and plan.get("baseline_hash"):
        mismatch(context["approved_baseline_hash"] != plan["baseline_hash"], "unapproved or altered baseline")
    if context.get("approved_evaluator_hash") and plan.get("evaluator_hash"):
        mismatch(context["approved_evaluator_hash"] != plan["evaluator_hash"], "must use prior approved evaluator")
    if context.get("approved_evaluator_code_hash"):
        mismatch(context["approved_evaluator_code_hash"] != evaluator_digest() or plan.get("evaluator_code_hash") != evaluator_digest(), "executing evaluator differs from prior approved code")
    if context.get("current_candidate_hash"):
        mismatch(context["current_candidate_hash"] != plan.get("candidate_hash"), "stale candidate tree")
    if context.get("current_head"):
        mismatch(context["current_head"] != plan.get("candidate_head"), "stale candidate head")
    if evidence.get("plan_hash"):
        mismatch(evidence["plan_hash"] != digest(plan), "predeclared criteria/history/workload changed")
    if evidence.get("authority_hash") and context.get("authority_hash"):
        mismatch(evidence["authority_hash"] != context["authority_hash"], "authority changed")
    artifacts = evidence.get("artifacts", {})
    for name in PINS:
        if name not in artifacts:
            missing.append("artifact." + name)
        elif plan.get(name + "_hash"):
            mismatch(digest(artifacts[name]) != plan[name + "_hash"], name + " artifact changed")
    if all(plan.get(k) for k in ("registered_at",)) and evidence.get("started_at") and evidence.get("completed_at"):
        try:
            mismatch(not _time(plan["registered_at"]) < _time(evidence["started_at"]) <= _time(evidence["completed_at"]), "hypothesis must precede outcomes")
        except (ValueError, TypeError, AttributeError):
            rejected.append("invalid experiment timestamps")
    rollback = plan.get("rollback", {})
    for key in ("known_good_hash", "conditions", "stop_new_work", "reconcile_active_runs", "revert_pr_required"):
        require(rollback, key, "rollback." + key)
    mismatch(bool(rollback.get("known_good_hash")) and rollback["known_good_hash"] != plan.get("baseline_hash"), "rollback not pinned to baseline")
    for key in ("stop_new_work", "reconcile_active_runs", "revert_pr_required"):
        mismatch(key in rollback and rollback[key] is not True, "rollback procedure weakened")
    guardrails = evidence.get("guardrails", {})
    for name in sorted(HARD_GUARDRAILS | set(plan.get("guardrails", []))):
        if name not in guardrails or guardrails[name] is None:
            missing.append("guardrail." + name)
        elif guardrails[name] is not True:
            rejected.append("guardrail failure: " + name)
    budget, usage, limits = plan.get("budget", {}), evidence.get("usage", {}), context.get("limits", {})
    for key in ("active_seconds", "storage_bytes", "depth", "attempts"):
        consumed = require(usage, key, "usage." + key)
        allowed = require(budget, key, "budget." + key)
        ceiling = require(limits, key, "limits." + key)
        if any(value is not None and (not _number(value) or value < 0) for value in (consumed, allowed, ceiling)):
            rejected.append("invalid resource measure: " + key)
            continue
        if allowed is not None and ceiling is not None:
            mismatch(allowed > ceiling, "candidate expands resource budget: " + key)
        ancestor = context.get("prior_consumed_seconds", 0) if key == "active_seconds" else context.get("prior_consumed_storage_bytes", 0) if key == "storage_bytes" else 0
        if not _number(ancestor) or ancestor < 0:
            missing.append("observable cumulative resource usage")
        elif consumed is not None and allowed is not None and consumed + ancestor >= allowed:
            missing.append("resource budget exhausted: " + key)
    if _number(budget.get("active_seconds")) and budget["active_seconds"] > 3600:
        rejected.append("candidate exceeds initial 60-minute experiment allocation")
    if context.get("active_experiments") is not None:
        mismatch(context["active_experiments"] != 1, "only one active candidate experiment permitted")
    if plan.get("changes_evaluator") is True:
        for key in ("prior_evaluator_hash", "adversarial_fixtures_hash", "dual_version_replay"):
            require(evidence, key, "recursive." + key)
        mismatch(evidence.get("prior_evaluator_hash") not in {None, context.get("approved_evaluator_hash")}, "recursive self-validation")
        mismatch(evidence.get("dual_version_replay") is not True, "recursive dual-version replay failed")
        expected_adversarial = context.get("adversarial_fixtures_hash")
        if not expected_adversarial:
            missing.append("prior approved adversarial fixtures")
        elif evidence.get("adversarial_fixtures_hash"):
            mismatch(evidence["adversarial_fixtures_hash"] != expected_adversarial, "recursive adversarial fixtures changed")
    evidence_hash = digest(evidence)
    roles = {}
    for approval in approvals:
        role = approval.get("role")
        if role not in {"reviewer", "chief-of-staff"} or role in roles:
            rejected.append("invalid or duplicate approval role")
            continue
        roles[role] = approval
        for key, expected in (("candidate_hash", plan.get("candidate_hash")), ("candidate_head", plan.get("candidate_head")),
                              ("plan_hash", digest(plan)), ("evidence_hash", evidence_hash),
                              ("evaluator_hash", context.get("approved_evaluator_hash"))):
            if not approval.get(key):
                missing.append(role + "." + key)
            else:
                mismatch(expected is not None and approval[key] != expected, "approval pin mismatch: " + key)
        if not approval.get("agent_id"):
            missing.append(role + ".agent_id")
        mismatch(approval.get("agent_id") == plan.get("implementer"), "implementer cannot approve own work")
        authorized = context.get("authorized_approvers", {}).get(role)
        if authorized is None:
            missing.append("authorized approver identities: " + role)
        else:
            mismatch(approval.get("agent_id") not in authorized, "approver lacks assigned role: " + role)
        mismatch(approval.get("approved") is not True, "approval not granted")
        if role == "reviewer":
            mismatch(approval.get("fresh_context") is not True, "reviewer must have fresh context")
        if approval.get("approved_at") and evidence.get("completed_at"):
            try:
                mismatch(_time(approval["approved_at"]) < _time(evidence["completed_at"]), "approval predates completed evidence")
            except (ValueError, AttributeError):
                rejected.append("invalid approval timestamp")
        else:
            missing.append(role + ".approved_at")
    for role in ("reviewer", "chief-of-staff"):
        if role not in roles:
            missing.append("approval." + role)
    if len(roles) == 2:
        mismatch(roles["reviewer"].get("agent_id") == roles["chief-of-staff"].get("agent_id"), "reviewer and Chief of Staff must be distinct")
    if plan.get("claim") == "repair":
        repair = evidence.get("repair", {})
        for key in ("baseline_pass", "candidate_pass", "regression_pass", "independent_regression_hash"):
            require(repair, key, "repair." + key)
        if "baseline_pass" in repair:
            mismatch(repair["baseline_pass"] is not False, "repair baseline must fail")
        if "candidate_pass" in repair:
            mismatch(repair["candidate_pass"] is not True, "repair candidate must pass")
        if "regression_pass" in repair:
            mismatch(repair["regression_pass"] is not True, "retained regression suite must pass")
        expected = context.get("independent_regression_hash")
        if not expected:
            missing.append("independently specified regression")
        elif repair.get("independent_regression_hash"):
            mismatch(repair["independent_regression_hash"] != expected, "regression rewritten to pass")
    elif plan.get("claim") in {"outcome", "efficiency"}:
        stopping = plan.get("stopping_rule", {})
        for key in ("case_ids", "seed", "bootstrap_samples", "fixed_sample_size"):
            require(stopping, key, "stopping_rule." + key)
        case_ids, pairs = stopping.get("case_ids", []), evidence.get("pairs", [])
        sample_count = stopping.get("fixed_sample_size")
        if artifacts.get("workload", {}).get("cases") != case_ids:
            rejected.append("paired cases differ from pinned representative workload")
        if type(sample_count) is not int or sample_count < 20 or len(case_ids) != sample_count or len(set(case_ids)) != len(case_ids):
            missing.append("at least 20 unique preregistered paired cases")
        if type(stopping.get("seed")) is not int or type(stopping.get("bootstrap_samples")) is not int or not 1000 <= stopping.get("bootstrap_samples", 0) <= 10000:
            rejected.append("invalid fixed bootstrap configuration")
        if len(pairs) < len(case_ids):
            missing.append("incomplete preregistered workload")
        elif len(pairs) > len(case_ids):
            rejected.append("optional stopping or changed denominator")
        observed_ids = [pair.get("case_id") for pair in pairs]
        mismatch(len(set(observed_ids)) != len(observed_ids) or set(observed_ids) - set(case_ids) != set(), "paired workload changed")
        rng = random.Random(stopping["seed"] if type(stopping.get("seed")) is int else 0)
        orders = {case: (["baseline", "candidate"] if rng.randrange(2) == 0 else ["candidate", "baseline"]) for case in case_ids}
        differences, baselines = [], []
        observed_attempts = sum(len(pair[side + "_attempts"])
                                for pair in pairs for side in ("baseline", "candidate")
                                if isinstance(pair.get(side + "_attempts"), list))
        complete_attempt_telemetry = len(pairs) == len(case_ids) and all(
            isinstance(pair.get(side + "_attempts"), list) and pair[side + "_attempts"]
            for pair in pairs for side in ("baseline", "candidate"))
        for pair in pairs:
            mismatch(type(stopping.get("seed")) is int and pair.get("order") != orders.get(pair.get("case_id")), "paired ordering differs from preregistration")
            values = [pair.get("baseline"), pair.get("candidate")]
            if not all(_number(value) for value in values):
                missing.append("missing primary outcome telemetry")
                continue
            for side in ("baseline", "candidate"):
                attempts = pair.get(side + "_attempts")
                if not isinstance(attempts, list) or not attempts:
                    missing.append("all attempts including failures/retries required")
                else:
                    valid_attempts = all(isinstance(a, dict) and _number(a.get("value"))
                                         and a.get("status") in ("passed", "failed", "blocked")
                                         and (plan.get("claim") != "efficiency" or a["value"] >= 0)
                                         for a in attempts)
                    if not valid_attempts:
                        missing.append("missing or invalid attempt telemetry")
                    elif plan.get("claim") == "efficiency":
                        mismatch(not math.isclose(sum(a["value"] for a in attempts), pair[side], rel_tol=1e-12), "failed/retried attempt omitted from efficiency total")
            baseline, candidate = values
            if plan.get("claim") == "efficiency" and (baseline <= 0 or candidate < 0):
                missing.append("positive baseline efficiency denominator required")
            baselines.append(baseline)
            differences.append(baseline - candidate if plan.get("direction") == "lower" else candidate - baseline)
        if _number(usage.get("attempts")):
            # Missing rows or attempt containers leave the full count unknown.
            # Observed records always bound usage; complete telemetry is exact.
            mismatch(usage["attempts"] < observed_attempts or
                     (complete_attempt_telemetry and usage["attempts"] != observed_attempts),
                     "reported attempts differ from observable attempt records")
        if _number(budget.get("attempts")) and observed_attempts >= budget["attempts"]:
            missing.append("resource budget exhausted: attempts")
        if differences and len(differences) == len(case_ids) and len(case_ids) >= 20 and not rejected and not missing:
            interval = paired_interval(differences, stopping["seed"], stopping["bootstrap_samples"])
            mean = sum(differences) / len(differences)
            relative = mean / (sum(baselines) / len(baselines)) if sum(baselines) > 0 else None
            details = {"paired_cases": len(differences), "mean_benefit": mean, "interval_95": interval,
                       "relative_benefit": relative, "seed": stopping["seed"], "bootstrap_samples": stopping["bootstrap_samples"]}
            if interval[0] <= 0:
                missing.append("95% paired interval does not establish positive benefit")
            if plan["claim"] == "efficiency" and (relative is None or relative < .05):
                missing.append("relative efficiency benefit below 5%")
    return {"gate_version": VERSION, "evaluator_code_hash": evaluator_digest(), "plan_hash": digest(plan),
            "evidence_hash": evidence_hash, "candidate_hash": plan.get("candidate_hash"),
            "candidate_head": plan.get("candidate_head"),
            "decision": "reject" if rejected else "inconclusive" if missing else "pass",
            "reasons": sorted(set(rejected)), "measurement_gaps": sorted(set(missing)), "benefit": details,
            "permission_effect": "none; pass only establishes eligibility for governed PR promotion",
            "checkpoint_required": bool(_number(usage.get("active_seconds")) and _number(budget.get("active_seconds")) and _number(context.get("prior_consumed_seconds")) and usage["active_seconds"] + context["prior_consumed_seconds"] >= .8 * budget["active_seconds"])}



def evaluate(plan, evidence, approvals, context):
    """Validate required JSON types before evaluating evidence; never coerce pins.

    Missing data is inconclusive. Present malformed contract fields reject. Unknown
    attempt telemetry is inconclusive in either stochastic claim. This function
    confers no authority on its own source or result.
    """
    rejected, missing = [], []

    def field(mapping, key, kind, prefix):
        label = prefix + "." + key
        if key not in mapping or mapping[key] is None:
            missing.append(label)
            return None
        value = mapping[key]
        valid = (_number(value) if kind == "number" else type(value) is kind)
        if not valid:
            rejected.append("invalid type: " + label)
            return None
        if kind is str and not value.strip():
            missing.append(label)
        return value

    def fields(mapping, keys, kind, prefix):
        for key in keys.split():
            field(mapping, key, kind, prefix)

    for label, value, kind in (("plan", plan, dict), ("evidence", evidence, dict),
                                ("context", context, dict), ("approvals", approvals, list)):
        if type(value) is not kind:
            rejected.append("invalid type: " + label)
    if not rejected:
        fields(plan, "version registered_at hypothesis hypothesis_hash scope claim task_class expected_benefit target_metric direction implementer candidate_head evaluator_code_hash " + " ".join(n + "_hash" for n in PINS), str, "plan")
        field(plan, "changes_evaluator", bool, "plan")
        fields(context, "approved_baseline_hash approved_evaluator_hash approved_evaluator_code_hash current_candidate_hash current_head authority_hash registered_plan_hash", str, "context")
        fields(context, "prior_consumed_seconds prior_consumed_storage_bytes", "number", "context")
        field(context, "active_experiments", int, "context")
        fields(evidence, "started_at completed_at plan_hash authority_hash", str, "evidence")
        containers = [(plan, "rollback", "plan"), (plan, "budget", "plan"),
                      (plan, "stopping_rule", "plan"), (evidence, "usage", "evidence"),
                      (evidence, "artifacts", "evidence"), (evidence, "guardrails", "evidence"),
                      (context, "limits", "context"), (context, "authorized_approvers", "context")]
        for mapping, key, prefix in containers:
            field(mapping, key, dict, prefix)
        rails = field(plan, "guardrails", list, "plan")
        if rails is not None and any(type(r) is not str or not r.strip() for r in rails):
            rejected.append("invalid guardrail names")
        for parent, key in ((plan, "budget"), (evidence, "usage"), (context, "limits")):
            if type(parent.get(key)) is dict:
                fields(parent[key], "active_seconds storage_bytes", "number", key)
                fields(parent[key], "depth attempts", int, key)
        if type(plan.get("rollback")) is dict:
            rollback = plan["rollback"]
            field(rollback, "known_good_hash", str, "rollback")
            conditions = field(rollback, "conditions", list, "rollback")
            if conditions is not None and (not conditions or any(type(c) is not str or not c.strip() for c in conditions)):
                missing.append("rollback.conditions")
            fields(rollback, "stop_new_work reconcile_active_runs revert_pr_required", bool, "rollback")
        if type(evidence.get("guardrails")) is dict:
            for name, value in evidence["guardrails"].items():
                if value is not None and value is not True:
                    rejected.append("guardrail failure: " + str(name))
        if type(context.get("authorized_approvers")) is dict:
            for role, identities in context["authorized_approvers"].items():
                if type(identities) is not list or any(type(v) is not str or not v.strip() for v in identities):
                    rejected.append("invalid assigned approver identities: " + str(role))
        for approval in approvals:
            if type(approval) is not dict:
                rejected.append("invalid type: approval")
                continue
            fields(approval, "role agent_id approved_at candidate_hash candidate_head plan_hash evidence_hash evaluator_hash", str, "approval")
            field(approval, "approved", bool, "approval")
            if approval.get("role") == "reviewer":
                field(approval, "fresh_context", bool, "approval")
        if plan.get("claim") == "repair":
            repair = field(evidence, "repair", dict, "evidence")
            field(context, "independent_regression_hash", str, "context")
            if repair is not None:
                fields(repair, "baseline_pass candidate_pass regression_pass", bool, "repair")
                field(repair, "independent_regression_hash", str, "repair")
        if plan.get("changes_evaluator") is True:
            fields(evidence, "prior_evaluator_hash adversarial_fixtures_hash", str, "recursive")
            field(evidence, "dual_version_replay", bool, "recursive")
            field(context, "adversarial_fixtures_hash", str, "context")
        if plan.get("claim") in ("outcome", "efficiency"):
            stopping = plan.get("stopping_rule")
            if type(stopping) is dict:
                fields(stopping, "seed bootstrap_samples fixed_sample_size", int, "stopping_rule")
                ids = field(stopping, "case_ids", list, "stopping_rule")
                if ids is not None and any(type(v) is not str or not v.strip() for v in ids):
                    rejected.append("invalid paired case identities")
            pairs = field(evidence, "pairs", list, "evidence")
            if pairs is not None:
                for pair in pairs:
                    if type(pair) is not dict:
                        rejected.append("invalid paired row")
                        continue
                    field(pair, "case_id", str, "pair")
                    field(pair, "order", list, "pair")
            artifacts = evidence.get("artifacts")
            if type(artifacts) is dict and "workload" in artifacts and type(artifacts["workload"]) is not dict:
                rejected.append("invalid workload object")
    try:
        plan_hash, evidence_hash = digest(plan), digest(evidence)
    except (ValueError, TypeError):
        plan_hash, evidence_hash = None, None
        rejected.append("noncanonical JSON evidence")
    if not rejected and not missing:
        return _evaluate(plan, evidence, approvals, context)
    usage = evidence.get("usage", {}) if type(evidence) is dict else {}
    budget = plan.get("budget", {}) if type(plan) is dict else {}
    prior = context.get("prior_consumed_seconds") if type(context) is dict else None
    checkpoint = (type(usage) is dict and type(budget) is dict and _number(usage.get("active_seconds"))
                  and _number(budget.get("active_seconds")) and _number(prior)
                  and usage["active_seconds"] + prior >= .8 * budget["active_seconds"])
    return {"gate_version": VERSION, "evaluator_code_hash": evaluator_digest(), "plan_hash": plan_hash,
            "evidence_hash": evidence_hash, "candidate_hash": plan.get("candidate_hash") if type(plan) is dict else None,
            "candidate_head": plan.get("candidate_head") if type(plan) is dict else None,
            "decision": "reject" if rejected else "inconclusive", "reasons": sorted(set(rejected)),
            "measurement_gaps": sorted(set(missing)), "benefit": {},
            "permission_effect": "none; pass only establishes eligibility for governed PR promotion",
            "checkpoint_required": bool(checkpoint)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path, help="JSON object with plan/evidence/approvals/context")
    args = parser.parse_args(argv)
    try:
        bundle = json.loads(args.bundle.read_text())
        result = evaluate(bundle["plan"], bundle["evidence"], bundle["approvals"], bundle["context"])
        print(canonical_json(result))
        return {"pass": 0, "reject": 1, "inconclusive": 2}[result["decision"]]
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.exit(2, f"Invalid improvement bundle: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
