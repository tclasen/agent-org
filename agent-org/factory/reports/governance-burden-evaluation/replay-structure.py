#!/usr/bin/env python3
"""Replay the historical structural census using inert, hash-checked snapshots."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

report = Path(__file__).resolve().parent
index = json.loads((report / "source-snapshot-index.json").read_text())
with tempfile.TemporaryDirectory(prefix="governance-evaluation-replay-") as temporary:
    overlay = Path(temporary).resolve()
    for source, item in index.items():
        artifact = (report / item["snapshot"]).resolve()
        artifact.relative_to(report)
        data = artifact.read_bytes()
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise SystemExit("snapshot hash mismatch: " + source)
        target = overlay / source
        target.resolve().relative_to(overlay)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    result = subprocess.run([sys.executable, str(report / "measure-structure.py"),
        "--source-overlay", str(overlay), "--bridge-source", str(overlay / "root-bridge")],
        check=True, capture_output=True)
    expected = (report / "structural-metrics.json").read_bytes()
    observed = result.stdout
    outcome = {"snapshot_files_verified": len(index), "byte_identical": observed == expected,
        "expected_sha256": hashlib.sha256(expected).hexdigest(),
        "observed_sha256": hashlib.sha256(observed).hexdigest()}
    print(json.dumps(outcome, indent=2))
    raise SystemExit(0 if outcome["byte_identical"] else 1)
