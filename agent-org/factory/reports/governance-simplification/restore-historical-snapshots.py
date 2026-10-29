#!/usr/bin/env python3
"""Verify lossless historical inputs; optionally restore to an explicit authorized directory."""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--restore-to", type=Path)
args = parser.parse_args()
report = Path(__file__).resolve().parent
snapshots = json.loads((report / "historical-source-bytes.json").read_text())["snapshots"]
base = args.restore_to.resolve() if args.restore_to else None
for name, item in snapshots.items():
    raw = item["utf8"].encode("utf8")
    if hashlib.sha256(raw).hexdigest() != item["sha256"] or len(raw) != item["length"]:
        raise SystemExit("historical input hash mismatch: " + name)
    if base:
        target = (base / name).resolve()
        target.relative_to(base)
        if target.exists():
            if target.read_bytes() != raw:
                raise SystemExit("refusing to overwrite different data: " + name)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
print(json.dumps({"verified": len(snapshots), "restored": bool(base)}))
