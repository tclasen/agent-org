"""Manifest sources, canonical linkage, failure paths and real CLI behavior."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "instrumentation/context.py"
SPEC = importlib.util.spec_from_file_location("context", MODULE)
context = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(context)


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.root = self.repo / "agent-org"
        self.root.mkdir()
        (self.repo / "AGENTS.md").write_text("Read organization startup instructions.")
        for path in ("AGENTS.md", "policies/AUTHORITY.md", "policies/SCOPE_BOUNDARIES.md",
                     "shared/SESSION_LIFECYCLE.md", "shared/CONTEXT_MANAGEMENT.md", "agents/INDEX.md",
                     "tasks/INDEX.md", "agents/developer/AGENTS.md", "agents/developer/CONTEXT.md",
                     "factory/reports/example/PLAN.md"):
            self.write(path, "# Required source\n")
        self.write("tasks/organization/TASK-000001.md", """- ID: TASK-000001
- Owning Role: Developer
- Authorized Scope: agent-org/factory/instrumentation/example.py
- Related Requirements: REQ-000001
- Approval Requirements: APP-000001
- Plan Approval: APP-000002
- Plan Revision: 1
- Authorized: yes
- Claim: RUN-000001
- Dependencies: none
""")
        self.write("runs/RUN-000001.md", """- ID: RUN-000001
- Owning Role: Developer
- Authorized Scope: agent-org/factory/instrumentation/example.py
- Task: TASK-000001
- Budget: shared 3600 seconds
- Next Action: run only assigned checks
""")
        self.write("requirements/organization/REQ-000001.md", "- ID: REQ-000001\n")
        self.write("approvals/APP-000001.md", "- ID: APP-000001\n- Status: approved\n")
        self.write("approvals/APP-000002.md", "- ID: APP-000002\n- Status: approved\n- Plan Revision: 1\n\n`factory/reports/example/PLAN.md`\n")

    def write(self, path, text):
        destination = self.root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text)
        return destination

    def manifest(self, **kwargs):
        return context.build_manifest(self.root, "TASK-000001", "RUN-000001", "developer", **kwargs)

    def test_hashes_required_classes_root_and_no_registry_fanout(self):
        self.write("tasks/INDEX.md", "[unrelated missing task](organization/TASK-999999.md)")
        result = self.manifest()
        paths = {source["path"]: source for source in result["sources"]}
        required = paths["agent-org/policies/AUTHORITY.md"]
        self.assertEqual(required["classes"], ["authority"])
        self.assertEqual(required["sha256"], hashlib.sha256(b"# Required source\n").hexdigest())
        self.assertTrue(required["required"])
        self.assertIn("agent-org/approvals/APP-000002.md", paths)
        self.assertIn("agent-org/factory/reports/example/PLAN.md", paths)
        self.assertTrue(all(not Path(path).is_absolute() for path in paths))
        self.assertIn("do not prove reading", result["permission_effect"])
        self.assertEqual(result, context.build_manifest(self.repo, "TASK-000001", "RUN-000001", "developer"))

    def test_missing_authority_and_plan_fail(self):
        for path in ("policies/AUTHORITY.md", "approvals/APP-000001.md", "approvals/APP-000002.md", "factory/reports/example/PLAN.md"):
            target = self.root / path
            content = target.read_text()
            target.unlink()
            with self.assertRaises(ValueError, msg=path):
                self.manifest()
            target.write_text(content)

    def test_wrong_run_task_role_scope_and_revision_fail(self):
        run_path = self.root / "runs/RUN-000001.md"
        original = run_path.read_text()
        for old, new in (("Task: TASK-000001", "Task: TASK-000002"), ("Owning Role: Developer", "Owning Role: Coordinator"),
                         ("Scope: agent-org/factory/instrumentation/example.py", "Scope: agent-org/**")):
            run_path.write_text(original.replace(old, new))
            with self.assertRaises(ValueError):
                self.manifest()
        run_path.write_text(original)
        approval = self.root / "approvals/APP-000002.md"
        approval.write_text(approval.read_text().replace("Plan Revision: 1", "Plan Revision: 2"))
        with self.assertRaises(ValueError):
            self.manifest()

    def test_traversal_absolute_outside_and_symlink_escape_fail(self):
        for source in ("../outside.md", str(self.repo / "outside.md"), "agent-org/../AGENTS.md"):
            with self.assertRaises(ValueError, msg=source):
                self.manifest(sources=[source])
        outside = self.repo / "outside.md"
        outside.write_text("outside")
        (self.root / "escaped.md").symlink_to(outside)
        with self.assertRaises(ValueError):
            self.manifest(sources=["escaped.md"])
        authority = self.root / "policies/AUTHORITY.md"
        authority.unlink()
        authority.symlink_to(outside)
        with self.assertRaises(ValueError):
            self.manifest()

    def test_explicit_required_readings_and_additive_sources(self):
        self.write("agents/developer/AGENTS.md", "Read [extra criteria](../../shared/EXTRA.md) before acting.\n")
        with self.assertRaises(ValueError):
            self.manifest()
        self.write("shared/EXTRA.md", "# Criteria")
        self.write("knowledge/evidence.md", "# Evidence")
        manifest = self.manifest(sources=["agent-org/knowledge/evidence.md"])
        entries = {entry["path"]: entry for entry in manifest["sources"]}
        self.assertTrue(entries["agent-org/shared/EXTRA.md"]["required"])
        self.assertFalse(entries["agent-org/knowledge/evidence.md"]["required"])
        self.assertTrue(manifest["required_reading_instructions"])

    def test_second_hop_missing_required_source_is_refused(self):
        self.write("agents/developer/AGENTS.md", "Read [criteria](../../shared/EXTRA.md).\n")
        self.write("shared/EXTRA.md", "Read [authority](MISSING.md).\n")
        with self.assertRaisesRegex(ValueError, "missing required reading: MISSING.md"):
            self.manifest()

    def test_second_hop_escaped_required_sources_are_refused(self):
        self.write("agents/developer/AGENTS.md", "Read [criteria](../../shared/EXTRA.md).\n")
        outside = self.repo / "outside.md"
        outside.write_text("# Outside organization")
        self.write("shared/ESCAPED.md", "placeholder").unlink()
        (self.root / "shared/ESCAPED.md").symlink_to(outside)
        for target in ("../../outside.md", "ESCAPED.md"):
            with self.subTest(target=target):
                self.write("shared/EXTRA.md", f"Read [authority]({target}).\n")
                with self.assertRaisesRegex(ValueError, "escaped required reading"):
                    self.manifest()

    def test_required_reading_cycles_deduplicate_without_discovery_fanout(self):
        self.write("agents/developer/AGENTS.md", "Read [criteria](../../shared/EXTRA.md).\n")
        self.write("shared/EXTRA.md", "Read [more](MORE.md).\n\n[Discovery index](MISSING-INDEX.md)\n")
        self.write("shared/MORE.md", "Read [criteria](EXTRA.md).\n\n[Unrelated source](MISSING.md)\n")
        self.write("tasks/INDEX.md", "[Irrelevant task](organization/TASK-999999.md)\n")
        manifest = self.manifest()
        paths = [entry["path"] for entry in manifest["sources"]]
        self.assertEqual(paths.count("agent-org/shared/EXTRA.md"), 1)
        self.assertEqual(paths.count("agent-org/shared/MORE.md"), 1)
        directives = [directive["source"] for directive in manifest["required_reading_instructions"]]
        self.assertEqual(directives.count("agent-org/shared/EXTRA.md"), 1)
        self.assertEqual(directives.count("agent-org/shared/MORE.md"), 1)
        self.assertFalse(any("MISSING" in path or "999999" in path for path in paths))

    def test_excessive_required_reading_graph_fails_without_truncation(self):
        self.write("agents/developer/AGENTS.md", "Read [criteria](../../shared/CHAIN-0.md).\n")
        for index in range(260):
            self.write(f"shared/CHAIN-{index}.md", f"Read [next](CHAIN-{index + 1}.md).\n")
        with self.assertRaisesRegex(ValueError, "required reading graph exceeds 256 sources"):
            self.manifest()

    def test_plain_and_quoted_required_paths_are_checked(self):
        self.write("agents/developer/AGENTS.md", "Read ../../shared/EXTRA.md and `../../shared/MORE.md`.\n")
        with self.assertRaises(ValueError):
            self.manifest()
        self.write("shared/EXTRA.md", "# Extra")
        self.write("shared/MORE.md", "# More")
        entries = {entry["path"] for entry in self.manifest()["sources"]}
        self.assertIn("agent-org/shared/EXTRA.md", entries)
        self.assertIn("agent-org/shared/MORE.md", entries)

    def test_fenced_metadata_examples_do_not_define_fields(self):
        path = self.root / "tasks/organization/TASK-000001.md"
        path.write_text(path.read_text() + "\n```markdown\n- Authorized: no\n- ID: TASK-999999\n```\n")
        self.assertEqual(self.manifest()["task"], "TASK-000001")

    def test_actual_cli_markdown_json_and_missing_source_refusal(self):
        command = [sys.executable, str(MODULE), "--root", str(self.root), "--task", "TASK-000001", "--run", "RUN-000001", "--role", "developer"]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(json.loads(result.stdout)["run"], "RUN-000001")
        result = subprocess.run(command + ["--format", "markdown"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("SHA-256", result.stdout)
        result = subprocess.run(command + ["--source", "missing.md"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing source", json.loads(result.stdout)["errors"][0])


if __name__ == "__main__":
    unittest.main()
