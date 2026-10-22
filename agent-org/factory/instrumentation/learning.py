"""Read-only candidate archive validation; never a promotion or permission gate.

Markdown records use Candidate, Parent, Content Hash, Incident Family, Partition
and Exposures bullet fields. Exposures is 'none' or comma-separated partitions.
Rejected and inconclusive records remain ordinary lineage history.
"""
import argparse
import json
from pathlib import Path
import re

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
PARTITIONS = {"development", "selection", "final"}
FIELDS = ("Candidate", "Parent", "Content Hash", "Incident Family", "Partition", "Exposures")


def organization_root(root):
    path = Path(root).resolve(strict=True)
    if (path / "agent-org").is_dir():
        path = (path / "agent-org").resolve(strict=True)
    if not (path / "AGENTS.md").is_file() or not (path / "policies").is_dir():
        raise ValueError("root must be an organization directory or its repository root")
    return path


def read_candidates(root):
    """Read persisted Markdown without following paths outside the organization."""
    root = organization_root(root)
    rows = []
    for folder in ("knowledge/improvement-candidates", "experiments/candidates"):
        directory = root / folder
        if not directory.exists():
            continue
        if not directory.resolve().is_relative_to(root):
            raise ValueError(f"escaped candidate directory: {folder}")
        for path in sorted(directory.rglob("*.md")):
            if path.name.upper() in {"INDEX.MD", "README.MD", "TEMPLATE.MD"}:
                continue
            if not path.resolve().is_relative_to(root):
                raise ValueError(f"escaped candidate source: {path.relative_to(root)}")
            values = {"source": f"agent-org/{path.relative_to(root).as_posix()}"}
            duplicates = []
            in_fence = False
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith(("```", "~~~")):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                match = re.fullmatch(r"- ([^:]+):\s*(.*)", line)
                if match and match[1] in (*FIELDS, "Status"):
                    key, value = match.groups()
                    if key in values:
                        duplicates.append(key)
                    values[key] = value
            values["_duplicates"] = duplicates
            rows.append(values)
    return rows


def validate_candidates(rows):
    """Return errors, warnings and transitive lineage for field-name dictionaries."""
    errors, warnings, candidates, hashes = [], [], {}, {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"row {index + 1}: record must be a mapping")
            continue
        label = row.get("source", f"row {index + 1}")
        for key in row.get("_duplicates", []):
            errors.append(f"{label}: duplicate field {key}")
        valid = True
        for key in FIELDS:
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f"{label}: missing or malformed {key}")
                valid = False
        if not valid:
            continue
        candidate = row["Candidate"]
        for key in ("Candidate", "Incident Family"):
            if not SLUG.fullmatch(row[key]):
                errors.append(f"{label}: malformed {key}")
        if row["Parent"] != "none" and not SLUG.fullmatch(row["Parent"]):
            errors.append(f"{label}: malformed Parent")
        if not re.fullmatch(r"[0-9a-f]{64}", row["Content Hash"]):
            errors.append(f"{label}: malformed Content Hash")
        if row["Partition"] not in PARTITIONS:
            errors.append(f"{label}: malformed Partition")
        exposure = [] if row["Exposures"] == "none" else [x.strip() for x in row["Exposures"].split(",")]
        if any(x not in PARTITIONS for x in exposure) or len(set(exposure)) != len(exposure):
            errors.append(f"{label}: malformed Exposures")
        if row.get("Status", "proposed") not in {"proposed", "active", "rejected", "inconclusive", "retired"}:
            errors.append(f"{label}: malformed Status")
        if candidate in candidates:
            errors.append(f"duplicate candidate ID: {candidate}")
            continue
        candidates[candidate] = dict(row, _exposures=exposure)
        content_hash = row["Content Hash"]
        if content_hash in hashes:
            errors.append(f"duplicate content hash: {candidate} and {hashes[content_hash]}")
        else:
            hashes[content_hash] = candidate
    lineage = {}
    families = {}
    for candidate, row in candidates.items():
        family = row["Incident Family"]
        families.setdefault(family, set()).add(row["Partition"])
        seen, ancestors = {candidate}, []
        parent = row["Parent"]
        while parent != "none":
            if parent in seen:
                errors.append(f"parent cycle: {candidate} through {parent}")
                break
            if parent not in candidates:
                errors.append(f"missing parent: {candidate} -> {parent}")
                break
            seen.add(parent)
            ancestors.append(parent)
            ancestor = candidates[parent]
            if "final" in ancestor["_exposures"]:
                errors.append(f"final-test exposure used by descendant: {candidate} <- {parent}")
            parent = ancestor["Parent"]
        lineage[candidate] = ancestors
        if "final" in row["_exposures"]:
            warnings.append(f"{candidate}: final-test exposure retained; descendants cannot reuse it")
    for family, partitions in families.items():
        if len(partitions) > 1:
            errors.append(f"incident-family partition leakage: {family} spans {', '.join(sorted(partitions))}")
    return {"errors": sorted(set(errors)), "warnings": sorted(set(warnings)), "lineage": lineage,
            "permission_effect": "none; archive validation does not approve or promote candidates"}


def scaffold(candidate, content_hash, incident_family, parent="none", partition="development", exposures="none", status="proposed"):
    row = dict(zip(FIELDS, (candidate, parent, content_hash, incident_family, partition, exposures)), Status=status)
    # Parent existence belongs to archive validation, not a standalone scaffold.
    result = validate_candidates([dict(row, Parent="none")])
    if parent != "none" and not SLUG.fullmatch(parent):
        result["errors"].append("malformed Parent")
    if result["errors"]:
        raise ValueError("; ".join(result["errors"]))
    return "# Improvement candidate\n\n" + "\n".join(f"- {k}: {v}" for k, v in row.items()) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="validate persisted Markdown candidate archive")
    validate.add_argument("--root", default="agent-org")
    create = commands.add_parser("scaffold", help="emit a candidate record to stdout only")
    for name in ("candidate", "content-hash", "incident-family"):
        create.add_argument("--" + name, required=True)
    create.add_argument("--parent", default="none")
    create.add_argument("--partition", choices=sorted(PARTITIONS), default="development")
    create.add_argument("--exposures", default="none")
    create.add_argument("--status", default="proposed")
    args = parser.parse_args(argv)
    try:
        if args.command == "scaffold":
            print(scaffold(**{k: v for k, v in vars(args).items() if k != "command"}), end="")
            return 0
        result = validate_candidates(read_candidates(args.root))
        print(json.dumps(result, indent=2, sort_keys=True))
        return int(bool(result["errors"]))
    except (ValueError, OSError) as exc:
        print(json.dumps({"errors": [str(exc)], "warnings": [], "lineage": {}}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
