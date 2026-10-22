"""Exercise persisted candidate history and lineage contamination refusals."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "instrumentation/learning.py"
SPEC = importlib.util.spec_from_file_location("learning", MODULE)
learning = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(learning)


class LearningTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.root = self.repo / "agent-org"
        self.root.mkdir()
        (self.root / "AGENTS.md").write_text("# Organization")
        (self.root / "policies").mkdir()

    def write(self, candidate="baseline", content_hash="a" * 64, incident_family="recovery", **kwargs):
        directory = self.root / "knowledge/improvement-candidates"
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{candidate}.md"
        path.write_text(learning.scaffold(candidate, content_hash, incident_family, **kwargs))
        return path

    def result(self):
        return learning.validate_candidates(learning.read_candidates(self.root))

    def test_history_keeps_rejected_and_inconclusive(self):
        self.write(status="rejected")
        self.write("repair", "b" * 64, parent="baseline", status="inconclusive")
        result = self.result()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["lineage"]["repair"], ["baseline"])
        self.assertIn("does not approve", result["permission_effect"])

    def test_cycle_missing_parent_and_duplicate_content(self):
        self.write(parent="repair")
        self.write("repair", "a" * 64, parent="baseline")
        result = self.result()
        self.assertTrue(any("parent cycle" in error for error in result["errors"]))
        self.assertTrue(any("duplicate content hash" in error for error in result["errors"]))
        (self.root / "knowledge/improvement-candidates/repair.md").unlink()
        self.assertTrue(any("missing parent" in error for error in self.result()["errors"]))

    def test_duplicate_id_across_two_archive_roots(self):
        path = self.write()
        other = self.root / "experiments/candidates/copy.md"
        other.parent.mkdir(parents=True)
        other.write_text(path.read_text())
        self.assertTrue(any("duplicate candidate ID" in error for error in self.result()["errors"]))

    def test_transitive_descendant_inherits_final_exposure(self):
        self.write(exposures="final")
        self.write("middle", "b" * 64, parent="baseline", status="rejected")
        self.write("descendant", "c" * 64, parent="middle", status="inconclusive")
        result = self.result()
        self.assertTrue(any("descendant <- baseline" in error for error in result["errors"]))
        self.assertTrue(result["warnings"])

    def test_family_overlap_refused_even_without_parent(self):
        self.write(partition="selection")
        self.write("held-out", "b" * 64, partition="final")
        self.assertTrue(any("incident-family partition leakage" in error for error in self.result()["errors"]))

    def test_malformed_persisted_fields_and_duplicate_field(self):
        path = self.write()
        path.write_text(path.read_text().replace("Exposures: none", "Exposures: train,final") + "- Candidate: baseline\n")
        result = self.result()
        self.assertTrue(any("malformed Exposures" in error for error in result["errors"]))
        self.assertTrue(any("duplicate field Candidate" in error for error in result["errors"]))
        self.assertTrue(learning.validate_candidates([None, {"Candidate": "x"}])["errors"])
        for key, invalid in (("Candidate", "BAD ID"), ("Parent", "../escape"), ("Content Hash", "ABC"),
                             ("Partition", "training"), ("Incident Family", "x/y"), ("Status", "promoted")):
            row = learning.read_candidates(self.root)[0]
            row[key] = invalid
            self.assertTrue(learning.validate_candidates([row])["errors"], key)

    def test_symlink_escape_refused(self):
        path = self.write()
        outside = self.repo / "outside.md"
        outside.write_text(path.read_text())
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaises(ValueError):
            learning.read_candidates(self.root)

    def test_cli_actual_archive_and_stdout_scaffold(self):
        self.write()
        completed = subprocess.run([sys.executable, str(MODULE), "validate", "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stdout)
        self.assertEqual(json.loads(completed.stdout)["errors"], [])
        path = self.root / "knowledge/improvement-candidates/baseline.md"
        path.write_text(path.read_text().replace("Parent: none", "Parent: missing"))
        completed = subprocess.run([sys.executable, str(MODULE), "validate", "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 1)
        self.assertIn("missing parent", completed.stdout)
        completed = subprocess.run([sys.executable, str(MODULE), "scaffold", "--candidate", "new", "--content-hash", "d" * 64,
                                    "--incident-family", "new-family"], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0)
        self.assertIn("- Candidate: new", completed.stdout)
        self.assertFalse((self.root / "knowledge/improvement-candidates/new.md").exists())


if __name__ == "__main__":
    unittest.main()
