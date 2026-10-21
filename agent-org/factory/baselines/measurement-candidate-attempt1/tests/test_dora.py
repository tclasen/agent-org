"""D-01–D-13 synthetic acceptance; no live production claims."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("dora_calculator", ROOT / "dora/calculator.py")
dora = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dora)
START, END = "2026-01-02T00:00:00Z", "2026-01-03T00:00:00Z"
CLASSIFICATION = {"version": "1.0.0", "observation_kind": "synthetic", "services": {"service-a": {
    "project_id": "project-a", "environments": {"prod": "production", "stage": "staging"},
    "production_threshold": 1.0, "stabilization_seconds": 1800, "health_criteria": "all-required-probes-green"}}}


def event(kind, identity, when, sequence, **payload):
    return {"schema_version": 1, "event_id": identity, "type": kind, "occurred_at": when,
            "sequence": sequence, "provenance": "synthetic://authoritative-fixture", "payload": {
                "project_id": "project-a", "service_id": "service-a", **({"health_criteria": "all-required-probes-green"} if kind in {"deployment", "recovery"} else {}), **payload}}


def fixture():
    return [
        event("commit", "c1", "2026-01-01T00:00:00Z", 1, commit_id="git1", committed_at="2026-01-01T00:00:00Z"),
        event("build", "b1", "2026-01-01T01:00:00Z", 2, build_id="build1", commit_ids=["git1"]),
        event("artifact", "a1", "2026-01-01T02:00:00Z", 3, artifact_id="artifact1", build_id="build1"),
        event("deployment", "d1", "2026-01-02T00:00:00Z", 4, deployment_id="rollout1", artifact_id="artifact1", environment="prod", traffic=1.0, healthy=True, health_evidence="synthetic://health/rollout1"),
        event("failure", "f1", "2026-01-02T01:10:00Z", 5, failure_id="incident1", deployment_id="rollout1", degradation_started_at="2026-01-02T01:00:00Z", causal_evidence="synthetic://incident1/root-cause"),
        event("deployment", "d2", "2026-01-02T02:00:00Z", 6, deployment_id="rollback1", artifact_id="artifact1", environment="prod", traffic=1.0, healthy=True, health_evidence="synthetic://health/rollback1", rework_kind="rollback", unplanned=True, remediates_deployment_id="rollout1"),
        event("recovery", "r1", "2026-01-02T02:30:00Z", 7, failure_id="incident1", healthy_since="2026-01-02T02:00:00Z", confirmed_at="2026-01-02T02:30:00Z", healthy=True, health_evidence="synthetic://continuous-health")]


def report(events=None, **kwargs):
    return dora.calculate(fixture() if events is None else events, CLASSIFICATION, START, END, **kwargs)


def service(events=None, **kwargs):
    return report(events, **kwargs)["services"]["service-a"]


class DoraTests(unittest.TestCase):
    def test_D01_classification_threshold_health(self):
        for mutation in ({"environment": "stage"}, {"environment": "unknown"}, {"traffic": .99}, {"healthy": False}, {"health_evidence": None}):
            events = fixture()[:4]
            events[-1]["payload"].update(mutation)
            self.assertEqual(service(events)["deployment_frequency"]["count"], 0)
        events = fixture()[:4]
        events[-1]["payload"]["service_id"] = "unknown"
        self.assertEqual(service(events)["deployment_frequency"]["count"], 0)
        self.assertEqual(service()["deployment_frequency"]["count"], 2)
        bad = copy.deepcopy(CLASSIFICATION)
        bad["services"]["service-a"]["production_threshold"] = 0
        with self.assertRaises(ValueError):
            dora.calculate([], bad, START, END)

    def test_D02_chain_absence_not_inferred(self):
        for removed in ("c1", "b1", "a1"):
            events = [e for e in fixture() if e["event_id"] != removed]
            result = report(events)
            self.assertIsNone(result["services"]["service-a"]["lead_time"]["p50_seconds"])
            self.assertEqual(result["measurement_health"]["status"], "partial")
        events = fixture()
        events[0]["provenance"] = ""
        with self.assertRaises(ValueError):
            report(events)

    def test_D03_first_committer_lead_and_negative(self):
        result = service()["lead_time"]
        self.assertEqual(result["samples_seconds"], [86400.0])
        self.assertEqual(result["sample_size"], 1)
        events = fixture()
        events[0]["payload"]["committed_at"] = "2026-01-03T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "negative"):
            report(events)
        events = fixture()
        events[3]["occurred_at"] = "2026-01-01T23:00:00Z"
        self.assertEqual(service(events)["lead_time"]["sample_size"], 0)

    def test_D04_frequency_half_open(self):
        events = fixture()
        events[5]["occurred_at"] = END
        self.assertEqual(service(events)["deployment_frequency"]["count"], 1)
        self.assertEqual(service(events)["deployment_frequency"]["per_day"], 1.0)
        partial = dora.calculate(fixture(), CLASSIFICATION, START, "2026-01-02T12:00:00Z")
        self.assertEqual(partial["services"]["service-a"]["deployment_frequency"]["per_day"], 4.0)

    def test_D05_failure_causality_followup_denominator(self):
        result = service()["change_fail_rate"]
        self.assertEqual(result, {"numerator": 1, "denominator": 2, "value": .5, "status": "available"})
        events = fixture()
        events[4]["payload"].pop("causal_evidence")
        self.assertEqual(service(events)["change_fail_rate"]["numerator"], 0)
        self.assertTrue(report(events)["measurement_health"]["issues"])
        events = fixture()
        events[4]["occurred_at"] = "2026-01-03T01:00:00Z"
        self.assertEqual(service(events)["change_fail_rate"]["numerator"], 0)
        self.assertEqual(service(events, followup_until="2026-01-04T00:00:00Z")["change_fail_rate"]["numerator"], 1)
        self.assertIsNone(service([])["change_fail_rate"]["value"])

    def test_D06_recovery_onset_stabilization_unresolved(self):
        self.assertEqual(service()["failed_deployment_recovery_time"]["p50_seconds"], 5400)
        for healthy_since in ("2026-01-02T02:01:00Z",):
            events = fixture()
            events[-1]["payload"]["healthy_since"] = healthy_since
            recovery = service(events)["failed_deployment_recovery_time"]
            self.assertIsNone(recovery["p50_seconds"])
            self.assertEqual(recovery["unresolved_failure_ids"], ["incident1"])
        events = fixture()[:-1]
        self.assertEqual(service(events)["failed_deployment_recovery_time"]["missing"], 1)
        events = fixture()
        events[-1]["payload"]["healthy_since"] = START
        with self.assertRaises(ValueError):
            report(events)

    def test_D07_rework_explicit_causal_unplanned(self):
        self.assertEqual(service()["deployment_rework_rate"]["value"], .5)
        for patch in ({"unplanned": False}, {"remediates_deployment_id": "unrelated"}, {"rework_kind": "planned"}):
            events = fixture()
            events[5]["payload"].update(patch)
            self.assertEqual(service(events)["deployment_rework_rate"]["numerator"], 0)

    def test_D08_idempotency_conflict_real_rollout(self):
        events = fixture()
        self.assertEqual(dora.canonical_json(report(events)), dora.canonical_json(report(events + [copy.deepcopy(events[3])])))
        repeated = copy.deepcopy(events[3])
        repeated["event_id"], repeated["sequence"] = "retry", 8
        self.assertEqual(service(events + [repeated])["deployment_frequency"]["count"], 2)
        repeated["payload"]["deployment_id"] = "new-rollout"
        self.assertEqual(service(events + [repeated])["deployment_frequency"]["count"], 3)
        duplicate = copy.deepcopy(events[3])
        duplicate["payload"]["traffic"] = .5
        with self.assertRaises(ValueError):
            report(events + [duplicate])
        duplicate["event_id"], duplicate["sequence"] = "conflict", 8
        duplicate["payload"]["artifact_id"] = "different-artifact"
        with self.assertRaisesRegex(ValueError, "logical"):
            report(events + [duplicate])
        duplicate["sequence"] = 1
        with self.assertRaisesRegex(ValueError, "sequence"):
            report(events + [duplicate])

    def test_rollout_progress_first_threshold_observation(self):
        events = fixture()[:4]
        partial = copy.deepcopy(events[3])
        partial["event_id"], partial["sequence"] = "partial-rollout", 5
        partial["occurred_at"] = "2026-01-01T23:00:00Z"
        partial["payload"]["traffic"] = .5
        self.assertEqual(service(events + [partial])["deployment_frequency"]["count"], 1)
        self.assertEqual(service(events + [partial])["lead_time"]["p50_seconds"], 86400)
        retry = copy.deepcopy(events[3])
        retry["event_id"], retry["sequence"] = "later-retry", 6
        retry["occurred_at"] = "2026-01-02T04:00:00Z"
        self.assertEqual(service(events + [partial, retry])["deployment_frequency"]["count"], 1)
        self.assertEqual(service(events + [partial, retry])["lead_time"]["p50_seconds"], 86400)

    def test_D09_rollback_no_duplicate_commit_lead(self):
        result = service()
        self.assertEqual(result["lead_time"]["sample_size"], 1)
        self.assertEqual(result["deployment_rework_rate"]["classifications"][0]["kind"], "rollback")

    def test_D10_fixforward_new_commit(self):
        events = fixture()
        events += [event("commit", "c2", "2026-01-02T01:20:00Z", 8, commit_id="git2", committed_at="2026-01-02T01:20:00Z"),
                   event("build", "b2", "2026-01-02T01:30:00Z", 9, build_id="build2", commit_ids=["git2"]),
                   event("artifact", "a2", "2026-01-02T01:40:00Z", 10, artifact_id="artifact2", build_id="build2")]
        events[5]["payload"].update(artifact_id="artifact2", rework_kind="fixforward")
        result = service(events)
        self.assertEqual(result["lead_time"]["samples_seconds"], [2400.0, 86400.0])
        self.assertEqual(result["deployment_rework_rate"]["classifications"][0]["kind"], "fixforward")
        self.assertEqual(result["failed_deployment_recovery_time"]["p50_seconds"], 5400)

    def test_D11_version_pins(self):
        before = report()
        with self.assertRaises(ValueError):
            report(definition_version="2.0.0")
        with self.assertRaises(ValueError):
            report(definition_digest="altered")
        self.assertEqual(report(definition_digest=before["definition_digest"]), before)
        changed = copy.deepcopy(CLASSIFICATION)
        changed["version"] = "2.0.0"
        self.assertNotEqual(dora.calculate(fixture(), changed, START, END)["classification_digest"], before["classification_digest"])
        self.assertEqual(report(), before)
        with self.assertRaises(ValueError):
            report(classification_digest="altered")
        self.assertEqual(report(classification_digest=before["classification_digest"]), before)

    def test_D12_replay_late_correction_asof(self):
        events = fixture()
        before = dora.canonical_json(report(events))
        self.assertEqual(dora.canonical_json(report(list(reversed(events)))), before)
        replacement = copy.deepcopy(events[4])
        replacement.pop("sequence")
        replacement["payload"]["degradation_started_at"] = "2026-01-02T01:05:00Z"
        correction = event("correction", "correction1", "2026-01-04T00:00:00Z", 8,
                           target_event_id="f1", replacement=replacement)
        corrected = report(events + [correction])
        self.assertEqual(corrected["services"]["service-a"]["failed_deployment_recovery_time"]["p50_seconds"], 5100)
        self.assertNotEqual(corrected["snapshot_digest"], report()["snapshot_digest"])
        self.assertEqual(dora.canonical_json(report(events + [correction], as_of=7)), before)
        correction["payload"]["target_event_id"] = "absent"
        with self.assertRaises(ValueError):
            report(events + [correction])
        early = report(events, as_of=4)
        self.assertEqual(early["services"]["service-a"]["change_fail_rate"]["numerator"], 0)
        self.assertNotEqual(early["snapshot_digest"], report()["snapshot_digest"])
        late_commit = fixture()
        late_commit[0]["sequence"] = 9
        self.assertIsNone(service(late_commit, as_of=7)["lead_time"]["p50_seconds"])
        self.assertEqual(service(late_commit, as_of=9)["lead_time"]["p50_seconds"], 86400)
        self.assertEqual(report(late_commit, as_of=7), report(late_commit[1:], as_of=7))

    def test_D13_percentiles_timezone_empty_invalid(self):
        self.assertEqual(dora._distribution(list(range(1, 11)))["p50_seconds"], 5)
        self.assertEqual(dora._distribution(list(range(1, 11)))["p90_seconds"], 9)
        self.assertIsNone(service([])["lead_time"]["p50_seconds"])
        self.assertIsNone(service([])["deployment_frequency"]["per_day"])
        self.assertEqual(report()["window"]["start"], dora.calculate(fixture(), CLASSIFICATION, "2026-01-01T16:00:00-08:00", END)["window"]["start"])
        self.assertEqual(dora.calculate([], CLASSIFICATION, end=END)["window"]["start"], "2025-12-04T00:00:00Z")
        for kwargs in ({"start": END, "end": START}, {"start": "2026-01-02", "end": END}, {"start": START, "end": END, "followup_until": START}):
            with self.assertRaises(ValueError):
                dora.calculate([], CLASSIFICATION, **kwargs)
        for schema in (True, 2, "1"):
            invalid = fixture()
            invalid[0]["schema_version"] = schema
            with self.assertRaises(ValueError):
                report(invalid)
        with self.assertRaises(ValueError):
            report(as_of=-1)
        self.assertEqual(dora.calculate([], {"version": "1.0.0", "services": {}}, START, END)["services"], {})

    def test_complete_empty_observation_window_vs_missing_coverage(self):
        classification = copy.deepcopy(CLASSIFICATION)
        classification["services"]["service-a"]["observation_coverage"] = {
            "start": START, "end": END, "available_at_sequence": 0,
            "provenance": "synthetic://independent-empty-window-audit"}
        result = dora.calculate([], classification, START, END)
        self.assertEqual(result["services"]["service-a"]["deployment_frequency"]["per_day"], 0)
        self.assertIsNone(result["services"]["service-a"]["change_fail_rate"]["value"])
        classification["services"]["service-a"]["observation_coverage"]["available_at_sequence"] = 8
        result = dora.calculate([], classification, START, END, as_of=7)
        self.assertIsNone(result["services"]["service-a"]["deployment_frequency"]["per_day"])

    def test_actual_eventstore_roundtrip_correction_and_replay(self):
        sys.path.insert(0, str(ROOT))
        from instrumentation.events import EventStore
        with tempfile.TemporaryDirectory() as folder:
            store = EventStore(Path(folder) / "synthetic-dora.jsonl")
            for number, observation in enumerate(fixture(), 1):
                native = {"schema_version": 1, "event_id": f"EVT-{number:06}", "event_type": observation["type"],
                          "task_id": "TASK-000004", "run_id": "RUN-000004", "agent_id": "AGENT-000006",
                          "classification": "organization", "occurred_at": observation["occurred_at"],
                          "ingested_at": "2026-01-04T01:00:00Z", "data": {**observation["payload"], "provenance": observation["provenance"]}}
                store.append(native)
            before = report(dora.ledger_events(store.read_events()))
            self.assertEqual(before["services"], report()["services"])
            replacement = copy.deepcopy(fixture()[4]["payload"])
            replacement.update(degradation_started_at="2026-01-02T01:05:00Z", provenance="synthetic://corrected-incident")
            store.append({"schema_version": 1, "event_id": "EVT-000008", "event_type": "correction",
                          "task_id": "TASK-000004", "run_id": "RUN-000004", "agent_id": "AGENT-000006",
                          "classification": "organization", "occurred_at": "2026-01-04T00:00:00Z",
                          "ingested_at": "2026-01-05T00:00:00Z", "causal_event_ids": ["EVT-000005"],
                          "data": {"target_event_id": "EVT-000005", "reason": "correct source impairment time",
                                   "provenance": "synthetic://source-correction", "replacement": {
                                       "event_type": "failure", "occurred_at": "2026-01-02T01:10:00Z", "data": replacement}}})
            corrected = report(dora.ledger_events(store.read_events()))
            self.assertEqual(corrected["services"]["service-a"]["failed_deployment_recovery_time"]["p50_seconds"], 5100)
            self.assertNotEqual(corrected["snapshot_digest"], before["snapshot_digest"])
            self.assertEqual(report(dora.ledger_events(store.read_events()), as_of=7), before)

    def test_ledger_adapter_and_cli_fixture(self):
        events = fixture()
        ledger = [{"schema_version": 1, "event_id": e["event_id"], "event_type": e["type"], "sequence": e["sequence"],
                   "occurred_at": e["occurred_at"], "data": {**e["payload"], "provenance": e["provenance"]}} for e in events]
        self.assertEqual(report(dora.ledger_events(ledger)), report())
        ledger[0]["schema_version"] = 2
        with self.assertRaises(ValueError):
            dora.ledger_events(ledger)
        completed = subprocess.run([sys.executable, str(ROOT / "dora/calculator.py"), str(ROOT / "dora/fixtures/events.json"), str(ROOT / "dora/fixtures/classification.json"), "--start", START, "--end", END], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout), report())
        self.assertEqual(completed.stdout, (ROOT / "dora/fixtures/expected.json").read_text())


if __name__ == "__main__":
    unittest.main()
