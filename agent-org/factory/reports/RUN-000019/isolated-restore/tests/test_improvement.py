"""Synthetic S-01–S-10 evidence decisions; this is not actual agent approval."""
import copy
import importlib.util
import json
from pathlib import Path
import random
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("improvement_gate", ROOT / "quality-gates/improvement.py")
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)


def bundle(claim="repair"):
    artifacts = {"baseline": {"instruction": "broken behavior"}, "candidate": {"instruction": "correct behavior"},
                 "workload": {"version": "1.0.0", "cases": [f"case-{i}" for i in range(20)]},
                 "evaluator": {"version": "1.0.0", "rules": "prior approved pinned rules"},
                 "criteria": {"version": "1.0.0", "confidence": .95, "relative_efficiency_minimum": .05}}
    spec = {"version": "1.0.0", "registered_at": "2026-01-01T00:00:00Z", "hypothesis": "Repair retained behavior with no regression",
            "scope": "organization", "claim": claim, "task_class": "synthetic qualification", "expected_benefit": "fixed tested behavior",
            "target_metric": "outcome" if claim == "repair" else "latency_seconds", "direction": "lower", "implementer": "implementer-a",
            "candidate_head": "head-a", "guardrails": sorted(gate.HARD_GUARDRAILS), "changes_evaluator": False,
            "budget": {"active_seconds": 3600, "storage_bytes": 1000000, "depth": 3, "attempts": 100},
            "rollback": {"known_good_hash": gate.digest(artifacts["baseline"]), "conditions": ["any hard regression", "post-promotion evidence failure"],
                         "stop_new_work": True, "reconcile_active_runs": True, "revert_pr_required": True},
            "stopping_rule": {"fixed_sample_size": 20, "case_ids": artifacts["workload"]["cases"], "seed": 42, "bootstrap_samples": 1000}}
    plan = gate.register(spec, artifacts)
    evidence = {"started_at": "2026-01-01T00:01:00Z", "completed_at": "2026-01-01T00:02:00Z", "plan_hash": gate.digest(plan), "artifacts": artifacts,
                "guardrails": {g: True for g in gate.HARD_GUARDRAILS}, "usage": {"active_seconds": 60, "storage_bytes": 1000, "depth": 1, "attempts": 40},
                "authority_hash": "existing-authority", "repair": {"baseline_pass": False, "candidate_pass": True, "regression_pass": True, "independent_regression_hash": "retained-regression"}}
    context = {"approved_baseline_hash": plan["baseline_hash"], "approved_evaluator_hash": plan["evaluator_hash"],
               "approved_evaluator_code_hash": gate.evaluator_digest(), "current_candidate_hash": plan["candidate_hash"], "current_head": "head-a",
               "authority_hash": "existing-authority", "prior_consumed_seconds": 0, "prior_consumed_storage_bytes": 0,
               "limits": copy.deepcopy(spec["budget"]), "active_experiments": 1, "independent_regression_hash": "retained-regression",
               "registered_plan_hash": gate.digest(plan), "authorized_approvers": {"reviewer": ["reviewer-a"], "chief-of-staff": ["chief-a"]}}
    if claim != "repair":
        rng = random.Random(42)
        evidence["pairs"] = [{"case_id": case, "order": ["baseline", "candidate"] if rng.randrange(2) == 0 else ["candidate", "baseline"],
                              "baseline": 100, "candidate": 90,
                              "baseline_attempts": [{"value": 100, "status": "passed"}],
                              "candidate_attempts": [{"value": 90, "status": "passed"}]} for case in spec["stopping_rule"]["case_ids"]]
    result = {"plan": plan, "evidence": evidence, "context": context, "approvals": []}
    reapprove(result)
    return result


def reapprove(data):
    data["approvals"] = [{"role": role, "agent_id": agent, "fresh_context": True, "approved": True,
                          "candidate_hash": data["plan"]["candidate_hash"], "candidate_head": data["plan"]["candidate_head"],
                          "plan_hash": gate.digest(data["plan"]), "evidence_hash": gate.digest(data["evidence"]),
                          "evaluator_hash": data["context"]["approved_evaluator_hash"], "approved_at": "2026-01-01T00:03:00Z"}
                         for role, agent in (("reviewer", "reviewer-a"), ("chief-of-staff", "chief-a"))]


def decision(data):
    return gate.evaluate(data["plan"], data["evidence"], data["approvals"], data["context"])


class ImprovementTests(unittest.TestCase):
    def test_S01_hypothesis_predeclared(self):
        self.assertEqual(decision(bundle())["decision"], "pass")
        data = bundle()
        data["plan"]["registered_at"] = "2026-01-01T00:02:00Z"
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["plan"].pop("hypothesis")
        self.assertNotEqual(decision(data)["decision"], "pass")

    def test_S02_pinned_baseline_workload_rules(self):
        for name in gate.PINS:
            data = bundle()
            data["evidence"]["artifacts"][name]["tampered"] = True
            reapprove(data)
            self.assertEqual(decision(data)["decision"], "reject", name)
        data = bundle()
        data["context"]["approved_baseline_hash"] = "different"
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["context"].pop("approved_baseline_hash")
        self.assertEqual(decision(data)["decision"], "inconclusive")

    def test_S03_repair_and_paired_comparison(self):
        data = bundle()
        self.assertEqual(decision(data)["decision"], "pass")
        for patch in ({"baseline_pass": True}, {"candidate_pass": False}, {"regression_pass": False}):
            changed = copy.deepcopy(data)
            changed["evidence"]["repair"].update(patch)
            reapprove(changed)
            self.assertEqual(decision(changed)["decision"], "reject")
        paired = bundle("efficiency")
        result = decision(paired)
        self.assertEqual(result["decision"], "pass", result)
        self.assertEqual(result["benefit"]["interval_95"], [10.0, 10.0])
        self.assertEqual(result["benefit"]["relative_benefit"], .1)
        self.assertEqual(gate.canonical_json(decision(paired)), gate.canonical_json(result))
        self.assertEqual(gate.paired_interval([-1, 2, 3], 7), gate.paired_interval([-1, 2, 3], 7))

    def test_S04_hard_guardrails_dominate_speed(self):
        for guardrail in gate.HARD_GUARDRAILS:
            data = bundle("efficiency")
            data["evidence"]["guardrails"][guardrail] = False
            reapprove(data)
            self.assertEqual(decision(data)["decision"], "reject", guardrail)
        data = bundle()
        data["plan"]["guardrails"].remove("security")
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")

    def test_S05_approval_independence(self):
        for patch in ({"agent_id": "implementer-a"}, {"fresh_context": False}, {"approved": False}):
            data = bundle()
            data["approvals"][0].update(patch)
            self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["approvals"][1]["agent_id"] = data["approvals"][0]["agent_id"]
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["approvals"] = []
        self.assertEqual(decision(data)["decision"], "inconclusive")
        data = bundle()
        data["approvals"][0]["approved_at"] = "2025-12-31T00:00:00Z"
        self.assertEqual(decision(data)["decision"], "reject")

    def test_S06_inconclusive_measurement_samples_uncertainty_budget(self):
        data = bundle("efficiency")
        data["evidence"]["pairs"].pop()
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "inconclusive")
        data = bundle("efficiency")
        data["evidence"]["pairs"][0]["candidate"] = None
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "inconclusive")
        data = bundle("efficiency")
        for pair in data["evidence"]["pairs"]:
            pair["candidate"] = 96
            pair["candidate_attempts"][0]["value"] = 96
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "inconclusive")
        for key in ("active_seconds", "storage_bytes", "depth", "attempts"):
            data = bundle()
            data["evidence"]["usage"][key] = data["plan"]["budget"][key]
            reapprove(data)
            self.assertEqual(decision(data)["decision"], "inconclusive", key)
        data = bundle()
        data["evidence"]["usage"]["active_seconds"] = None
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "inconclusive")
        data = bundle("outcome")
        for index, pair in enumerate(data["evidence"]["pairs"]):
            pair["candidate"] = 99 if index % 2 else 101
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "inconclusive")

    def test_S07_anti_gaming_attempts_denominators_history(self):
        data = bundle("efficiency")
        data["evidence"]["pairs"][0]["candidate_attempts"].append({"value": 50, "status": "failed"})
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle("efficiency")
        data["evidence"]["pairs"].append(copy.deepcopy(data["evidence"]["pairs"][0]))
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle("efficiency")
        data["evidence"]["pairs"][0]["order"].reverse()
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["plan"]["stopping_rule"]["fixed_sample_size"] = 1
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["evidence"]["repair"]["independent_regression_hash"] = "rewritten"
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        existing = gate.immutable_versions({}, {"1.0.0": {"criteria": "original"}})
        self.assertEqual(gate.immutable_versions(existing, {"1.0.0": {"criteria": "original"}}), existing)
        with self.assertRaises(ValueError):
            gate.immutable_versions(existing, {"1.0.0": {"criteria": "altered"}})
        self.assertIn("2.0.0", gate.immutable_versions(existing, {"2.0.0": {"criteria": "altered"}}))

    def test_S08_exact_candidate_head_tree_evidence(self):
        for key in ("current_head", "current_candidate_hash"):
            data = bundle()
            data["context"][key] = "changed"
            self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["evidence"]["usage"]["active_seconds"] += 1
        self.assertEqual(decision(data)["decision"], "reject")
        for key in ("candidate_hash", "candidate_head", "evaluator_hash", "plan_hash", "evidence_hash"):
            data = bundle()
            data["approvals"][0][key] = "changed"
            self.assertEqual(decision(data)["decision"], "reject")

    def test_S09_prior_evaluator_limits_authority(self):
        data = bundle()
        data["plan"]["changes_evaluator"] = True
        data["evidence"].update(prior_evaluator_hash=data["context"]["approved_evaluator_hash"], adversarial_fixtures_hash="prior-adversarial", dual_version_replay=True)
        data["context"]["adversarial_fixtures_hash"] = "prior-adversarial"
        data["context"]["registered_plan_hash"] = gate.digest(data["plan"])
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "pass", decision(data))
        data["evidence"]["prior_evaluator_hash"] = "candidate-self-evaluator"
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        for key in ("approved_evaluator_hash", "approved_evaluator_code_hash", "authority_hash"):
            data = bundle()
            data["context"][key] = "self-granted"
            self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["context"]["prior_consumed_seconds"] = 3590
        self.assertEqual(decision(data)["decision"], "inconclusive")
        data = bundle()
        data["context"]["active_experiments"] = 2
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["plan"]["budget"]["active_seconds"] = 7200
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")

    def test_S10_rollback_containment_and_checkpoint(self):
        data = bundle()
        data["plan"]["scope"] = "project"
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["plan"]["rollback"]["known_good_hash"] = "unrelated"
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertEqual(decision(data)["decision"], "reject")
        data = bundle()
        data["evidence"]["usage"]["active_seconds"] = 2880
        reapprove(data)
        self.assertTrue(decision(data)["checkpoint_required"])
        self.assertEqual(decision(data)["permission_effect"], "none; pass only establishes eligibility for governed PR promotion")

    def test_trusted_registration_role_and_missing_metadata(self):
        data = bundle()
        data["plan"]["stopping_rule"]["fixed_sample_size"] = 21
        data["evidence"]["plan_hash"] = gate.digest(data["plan"])
        reapprove(data)
        self.assertIn("durably registered plan changed", decision(data)["reasons"])
        data = bundle()
        data["approvals"][0]["agent_id"] = "unassigned-reviewer"
        self.assertEqual(decision(data)["decision"], "reject")
        for key in ("approved_evaluator_hash", "approved_evaluator_code_hash", "registered_plan_hash", "authorized_approvers"):
            data = bundle()
            data["context"].pop(key)
            self.assertEqual(decision(data)["decision"], "inconclusive", (key, decision(data)))

    def test_separate_scorecards_missing_cost_and_recovery(self):
        spec = importlib.util.spec_from_file_location("scorecards", ROOT / "metrics/scorecards.py")
        metrics = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(metrics)
        rows = [
            {"task_class": "repair", "configuration": "model-a/high", "expected_route": "developer", "actual_route": "developer", "delegation_attempt": True, "accepted": False, "latency_seconds": 12, "observed_cost": None, "handoff_complete": True, "recovery_resumed": False, "requirements_covered": 3, "requirements_total": 4},
            {"task_class": "repair", "configuration": "model-a/high", "delegation_attempt": True, "accepted": True, "latency_seconds": 8, "observed_cost": None, "handoff_complete": True, "recovery_resumed": True},
            {"delegation_attempt": True, "accepted": False}]
        result = metrics.scorecards(rows, {"project-a": [{"correctness": True}], "project-b": [{"correctness": False}]}, {"unknown_cost": 3, "unobserved_commands": None})
        self.assertEqual(result["organization"]["delegation_acceptance"]["denominator"], 3)
        self.assertEqual(result["organization"]["routing_accuracy"]["coverage"], {"observed": 1, "total": 3})
        grouped = result["organization"]["by_task_class_configuration"][0]
        self.assertIsNone(grouped["accepted_per_observed_cost"]["cost"])
        self.assertIsNone(grouped["accepted_per_observed_cost"]["value"])
        self.assertEqual(result["organization"]["handoff_completeness"]["value"], 1)
        self.assertEqual(result["organization"]["independent_recovery_success"]["value"], .5)
        self.assertEqual(result["projects"]["project-a"]["correctness"]["value"], 1)
        self.assertEqual(result["projects"]["project-b"]["correctness"]["value"], 0)
        self.assertIsNone(result["projects"]["project-b"]["security"]["value"])
        self.assertIsNone(result["measurement_health"]["unobserved_commands"])
        self.assertEqual(result["organization"]["planning_requirement_coverage"]["coverage"]["observed"], 1)

    def test_cli_repair_fixture(self):
        completed = subprocess.run([sys.executable, str(ROOT / "quality-gates/improvement.py"), str(ROOT / "benchmarks/repair.json")], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
        self.assertEqual(json.loads(completed.stdout)["decision"], "pass")


if __name__ == "__main__":
    unittest.main()
