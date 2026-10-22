"""Generate scoped source manifests from canonical organization records.

Sources and hashes prove availability at generation time, never actual reading,
permission, review, claim allocation or permission to execute a next action.
"""
import argparse
from collections import deque
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


class ManifestError(ValueError):
    """Canonical context is missing, mismatched or outside its permitted scope."""


def _fields(text):
    result = {}
    in_fence = False
    for line in text.splitlines():
        if line.startswith(('```', '~~~')):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.fullmatch(r"- ([A-Za-z][A-Za-z0-9 /_-]*):\s*(.*)", line)
        if not match:
            continue
        key, value = match.groups()
        if key in result:
            raise ManifestError(f"duplicate metadata field: {key}")
        result[key] = value.strip()
    return result


def build_manifest(root, task_id, run_id, role, sources=()):
    """Build a read-only manifest; root accepts agent-org or its repository root.

    Additional sources are additive and restricted to agent-org. Mandatory
    instructions are retained intact; registry links are never recursively loaded.
    """
    supplied_root = Path(root).resolve(strict=True)
    org = supplied_root / "agent-org" if (supplied_root / "agent-org").is_dir() else supplied_root
    org = org.resolve(strict=True)
    repo = org.parent
    if org.name != "agent-org" or not (org / "policies").is_dir():
        raise ManifestError("root must resolve to the canonical agent-org directory")
    if not re.fullmatch(r"TASK-\d{6}", task_id) or not re.fullmatch(r"RUN-\d{6}", run_id):
        raise ManifestError("malformed task or run identity")
    if not re.fullmatch(r"[a-z]+(?:-[a-z]+)*", role):
        raise ManifestError("malformed role")
    entries, texts = {}, {}

    def add(path, source_class, required=True, base=None, allow_root=False):
        raw = str(path).replace("\\", "/")
        lexical = PurePosixPath(raw)
        if lexical.is_absolute() or ".." in lexical.parts:
            raise ManifestError(f"absolute or traversing source: {raw}")
        candidate = (base or org) / raw
        try:
            resolved = candidate.resolve(strict=True)
        except OSError as exc:
            raise ManifestError(f"missing source: {raw}") from exc
        if not resolved.is_relative_to(org) and not (allow_root and resolved == repo / "AGENTS.md"):
            raise ManifestError(f"escaped source: {raw}")
        if not resolved.is_file():
            raise ManifestError(f"source is not a file: {raw}")
        relative = resolved.relative_to(repo).as_posix()
        data = resolved.read_bytes()
        try:
            content = data.decode("utf-8")
        except UnicodeError as exc:
            raise ManifestError(f"source is not UTF-8: {raw}") from exc
        if relative not in entries:
            entries[relative] = {"path": relative, "sha256": hashlib.sha256(data).hexdigest(),
                                 "classes": [], "required": required}
            texts[relative] = content
        entries[relative]["required"] |= required
        if source_class not in entries[relative]["classes"]:
            entries[relative]["classes"].append(source_class)
        return content

    def record(category, identity, source_class):
        paths = sorted((org / category).rglob(identity + ".md"))
        if len(paths) != 1:
            raise ManifestError(f"expected one canonical {identity}; found {len(paths)}")
        text = add(paths[0].relative_to(org), source_class)
        values = _fields(text)
        if values.get("ID") != identity:
            raise ManifestError(f"record identity mismatch: {identity}")
        return values, text

    add("AGENTS.md", "startup", base=repo, allow_root=True)
    for path, cls in (
        ("AGENTS.md", "organization_instructions"),
        ("policies/AUTHORITY.md", "authority"),
        ("policies/SCOPE_BOUNDARIES.md", "scope"),
        ("shared/SESSION_LIFECYCLE.md", "startup"),
        ("shared/CONTEXT_MANAGEMENT.md", "context_contract"),
        ("agents/INDEX.md", "role_registry"),
        ("tasks/INDEX.md", "task_registry"),
        (f"agents/{role}/AGENTS.md", "role_instructions"),
        (f"agents/{role}/CONTEXT.md", "role_context"),
    ):
        add(path, cls)
    task, task_text = record("tasks", task_id, "task")
    run, run_text = record("runs", run_id, "run")
    if run.get("Task") != task_id:
        raise ManifestError(f"run/task mismatch: {run_id} does not belong to {task_id}")
    normalize_role = lambda value: value.strip().lower().replace(" ", "-")
    for values in (task, run):
        if normalize_role(values.get("Owning Role", "")) != role:
            raise ManifestError("task/run role mismatch")
    if not task.get("Authorized Scope") or not run.get("Authorized Scope"):
        raise ManifestError("missing task/run scope")
    if task["Authorized Scope"] != run["Authorized Scope"]:
        raise ManifestError("task/run scope mismatch")
    if task.get("Authorized") != "yes":
        raise ManifestError("task is not explicitly authorized")
    if task.get("Claim") and run_id not in task["Claim"]:
        raise ManifestError("task claim/run mismatch")
    requirements = re.findall(r"REQ-\d{6}", task.get("Related Requirements", ""))
    if not requirements:
        raise ManifestError("missing source requirement")
    for identity in sorted(set(requirements)):
        record("requirements", identity, "requirement")
    approval_ids = set(re.findall(r"APP-\d{6}", task.get("Approval Requirements", "")))
    approval_ids.add("APP-000001")
    plan_approval = task.get("Plan Approval", "")
    if not re.fullmatch(r"APP-\d{6}", plan_approval):
        raise ManifestError("missing or malformed Plan Approval")
    approval_ids.add(plan_approval)
    approval_text = ""
    for identity in sorted(approval_ids):
        values, text = record("approvals", identity, "plan_approval" if identity == plan_approval else "authority_approval")
        if values.get("Revoked", "no").lower() != "no":
            raise ManifestError(f"approval is revoked: {identity}")
        if values.get("Expires At"):
            raise ManifestError(f"time-bound approval needs independent freshness verification: {identity}")
        if values.get("Status") != "approved":
            raise ManifestError(f"approval is not approved: {identity}")
        if identity == plan_approval:
            approval_text = text
            if values.get("Plan Revision") != task.get("Plan Revision"):
                raise ManifestError("plan approval revision mismatch")
    plan_path = task.get("Plan Path") or task.get("Plan Source")
    if not plan_path:
        plans = re.findall(r"`([^`\n]*\bPLAN\.md)`", approval_text)
        if len(set(plans)) != 1:
            raise ManifestError("missing or ambiguous canonical plan source")
        plan_path = plans[0]
    if plan_path.startswith("agent-org/"):
        plan_path = plan_path[len("agent-org/"):]
    add(plan_path, "plan")
    # Keep all required-reading directives, including plain-text relative paths,
    # verbatim. Only explicit local Markdown links in Read/Load paragraphs are
    # followed; index tables cannot fan out into every organization record.
    directives = []
    reading_classes = {"startup", "organization_instructions", "role_instructions", "role_context"}
    scheduled = {path for path in texts if reading_classes.intersection(entries[path]["classes"])}
    pending = deque(path for path in texts if path in scheduled)
    # Refuse excessive instruction graphs instead of silently truncating context.
    # Canonical paths deduplicate cycles and aliases; discovery/index links are
    # followed only when an explicit reading directive makes them mandatory.
    reading_limit = 256
    while pending:
        path = pending.popleft()
        text = texts[path]
        for paragraph in text.split("\n\n"):
            if not re.search(r"\b(?:[Rr]ead|[Ll]oad|[Bb]efore substantive work)\b", paragraph):
                continue
            directives.append({"source": path, "instruction": paragraph})
            targets = []
            # Sentence/clause scope matters: adjacent historical, conditional or
            # unassigned-session links do not inherit an earlier Read directive.
            for clause in re.split(r"(?<=[.!?;])\s+", paragraph):
                clause = clause.strip()
                if not re.match(r"(?:Read|Load|You must (?:read|load))\b", clause, re.I):
                    continue
                if re.search(r"\b(?:if|when|unless|unassigned)\b|not a startup reading assignment", clause, re.I):
                    continue
                targets += re.findall(r"\[[^\]]+\]\(([^)]+)\)", clause)
                targets += re.findall(r"`([^`\n]+\.md)`", clause)
                targets += re.findall(r"(?<![\w`/.])((?:\.\./|\./)[A-Za-z0-9_./-]+\.md)\b", clause)
            for target in dict.fromkeys(targets):
                if re.match(r"[a-z]+:", target) or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                # Instruction paths may legitimately climb to their own org
                # parent; canonicalize first, then enforce containment.
                joined = repo / Path(path).parent / target
                try:
                    canonical = joined.resolve(strict=True)
                except OSError as exc:
                    raise ManifestError(f"missing required reading: {target}") from exc
                if not canonical.is_relative_to(org):
                    raise ManifestError(f"escaped required reading: {target}")
                add(canonical.relative_to(org), "required_reading")
                source_path = canonical.relative_to(repo).as_posix()
                if source_path not in scheduled:
                    if len(scheduled) >= reading_limit:
                        raise ManifestError(f"required reading graph exceeds {reading_limit} sources")
                    scheduled.add(source_path)
                    pending.append(source_path)
    for path in sources:
        raw = str(path)
        if raw.startswith("agent-org/"):
            raw = raw[len("agent-org/"):]
        add(raw, "additional", required=False)
    return {"schema_version": "1.0", "root": "agent-org", "task": task_id, "run": run_id, "role": role,
            "authorized_scope": task["Authorized Scope"], "run_scope": run["Authorized Scope"],
            "dependency_state": task.get("Dependencies", "unknown"), "budget": run.get("Budget", "unknown"),
            "next_action": run.get("Next Action", "unknown"),
            "sources": sorted(entries.values(), key=lambda entry: entry["path"]),
            "required_reading_instructions": directives,
            "permission_effect": "none; availability and hashes do not prove reading, grant authority or allocate a claim"}


def markdown(manifest):
    lines = ["# Worker context manifest", "", f"- Task: {manifest['task']}", f"- Run: {manifest['run']}",
             f"- Role: {manifest['role']}", f"- Authorized Scope: {manifest['authorized_scope']}",
             f"- Run Scope: {manifest['run_scope']}", f"- Dependencies: {manifest['dependency_state']}",
             f"- Budget: {manifest['budget']}", f"- Next Action: {manifest['next_action']}",
             f"- Permission Effect: {manifest['permission_effect']}", "", "## Source availability and hashes", ""]
    for source in manifest["sources"]:
        lines.append(f"- `{source['path']}` — SHA-256 `{source['sha256']}`; classes {', '.join(source['classes'])}; required {source['required']}")
    lines += ["", "## Retained reading instructions", ""]
    for directive in manifest["required_reading_instructions"]:
        lines.extend([f"Source: `{directive['source']}`", "", directive["instruction"], ""])
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="agent-org")
    parser.add_argument("--task", required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args(argv)
    try:
        manifest = build_manifest(args.root, args.task, args.run, args.role, args.source)
        print(markdown(manifest) if args.format == "markdown" else json.dumps(manifest, indent=2, sort_keys=True))
        return 0
    except (ValueError, OSError) as exc:
        print(json.dumps({"errors": [str(exc)], "permission_effect": "none"}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
