#!/usr/bin/env python3
"""Read-only structural census. Stdout is deterministic JSON; no tokenizer/Git/network.

Run from any directory: python3 /path/to/measure-structure.py > structural-metrics.json
Use --source-overlay DIR to replay retained organization-relative source deltas
over the current checkout. --bridge-source FILE supplies a retained root bridge.
Only the shell redirection writes. This script reads the pinned manifest corpus,
the root bridge, and direct core-table route targets; it never traverses links.
"""
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-overlay", type=Path)
parser.add_argument("--bridge-source", type=Path)
args = parser.parse_args()
MANIFEST = Path(__file__).with_name("source-manifest.json")
manifest = json.loads(MANIFEST.read_text())
def digest(data):
    return hashlib.sha256(data).hexdigest()
def words(text):
    return len(text.split())
def read(relative):
    path = ROOT / relative
    path.resolve().relative_to(ROOT.resolve())
    if args.source_overlay:
        retained = args.source_overlay / relative
        retained.resolve().relative_to(args.source_overlay.resolve())
        if retained.is_file():
            path = retained
    data = path.read_bytes()
    return data, data.decode("utf-8")

sources = {}
texts = {}
metadata = collections.defaultdict(list)
repeated_lines = collections.defaultdict(list)
repeated_sentences = collections.defaultdict(list)
keys = {"Target System", "Change Classification", "Authorized Scope",
        "Affected Paths or Resources", "Owning Role", "Related Requirements",
        "Related Tasks", "Approval Requirements"}
for name, expected in manifest["sources"].items():
    data, text = read(name)
    texts[name] = text
    meta_words = 0
    text_lines = text.splitlines()
    header_start = next((i for i, line in enumerate(text_lines) if line.startswith("- ")), len(text_lines))
    header_end = next((i for i in range(header_start, len(text_lines)) if not text_lines[i].strip()), len(text_lines))
    for n, line in enumerate(text_lines, 1):
        field = re.match(r"^- ([^:]+): (.*)$", line)
        if header_start <= n - 1 < header_end and field and field[1] in keys:
            metadata[line].append({"path": name, "line": n})
            meta_words += words(line)
        elif words(line) >= 8 and not line.startswith(("#", "|")):
            repeated_lines[line].append({"path": name, "line": n})
    for paragraph in re.split(r"\n\s*\n", text):
        if paragraph.startswith(("#", "-", "|")):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z])", paragraph):
            sentence = " ".join(sentence.split())
            if words(sentence) >= 8:
                repeated_sentences[sentence].append(name)
    sources[name] = {"sha256": digest(data), "hash_matches": digest(data) == expected["sha256"],
                     "words": words(text), "manifest_words_match": words(text) == expected["words"],
                     "metadata_words": meta_words,
                     "nonmetadata_words": words(text) - meta_words,
                     "markdown_link_occurrences": len(re.findall(r"\[[^\]]+\]\(([^)]+)\)", text))}

base = ["AGENTS.md", "policies/AUTHORITY.md", "policies/SCOPE_BOUNDARIES.md"]
profiles = {}
for role in ["researcher", "coordinator", "reviewer", "chief-of-staff"]:
    files = base + [f"agents/{role}/AGENTS.md", f"agents/{role}/CONTEXT.md"]
    if role == "coordinator":
        files += ["shared/SESSION_LIFECYCLE.md"]
    profiles[role] = {"files": files, "file_count": len(files),
                      "words": sum(sources[p]["words"] for p in files)}

routes = []
route_sources = {}
for line in texts["AGENTS.md"].splitlines():
    if not line.startswith("| ") or "](" not in line:
        continue
    action = line.split("|")[1].strip()
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", line)
    targets = list(dict.fromkeys(p.split("#")[0] for p in targets))
    for p in targets:
        data, text = read(p)
        route_sources[p] = {"sha256": digest(data), "words": words(text),
                            "pinned_in_manifest": p in sources}
    routes.append({"action": action, "direct_files": targets, "direct_file_count": len(targets),
                   "direct_words": sum(route_sources[p]["words"] for p in targets),
                   "researcher_union_words": profiles["researcher"]["words"] + sum(
                       route_sources[p]["words"] for p in targets if p not in profiles["researcher"]["files"])})

def duplicates(mapping):
    return [{"text": text, "words_per_occurrence": words(text), "occurrences": refs,
             "occurrence_count": len(refs), "excess_words_over_one_copy": words(text) * (len(refs)-1)}
            for text, refs in sorted(mapping.items()) if len(refs) > 1]
md = duplicates(metadata)
lines = duplicates(repeated_lines)
sentences = duplicates(repeated_sentences)
bridge = args.bridge_source or ROOT.parent / "AGENTS.md"
bridge_bytes = bridge.read_bytes()
handoff_text = read("shared/HANDOFFS.md")[1]
handoff_contract = handoff_text.split("## Remote-main policy delivery", 1)[0]
out = {
    "method_version": 1,
    "word_definition": "len(UTF-8 decoded text.split()); Markdown syntax and metadata included",
    "scope": "26 manifest files; root bridge separately; direct core route targets separately; no recursive closure",
    "source_manifest_sha256": digest(MANIFEST.read_bytes()),
    "baseline_label": manifest["baseline"],
    "manifest_verification": {"checked": len(sources), "hash_mismatches": [p for p,v in sources.items() if not v["hash_matches"]],
                              "word_mismatches": [p for p,v in sources.items() if not v["manifest_words_match"]]},
    "sources": sources,
    "totals": {"files": len(sources), "words": sum(v["words"] for v in sources.values()),
               "metadata_words": sum(v["metadata_words"] for v in sources.values()),
               "nonmetadata_words": sum(v["nonmetadata_words"] for v in sources.values()),
               "metadata_field_occurrences": sum(len(v) for v in metadata.values()),
               "distinct_metadata_lines": len(metadata),
               "exact_duplicate_metadata_excess_words": sum(v["excess_words_over_one_copy"] for v in md),
               "exact_duplicate_nonmetadata_line_excess_words": sum(v["excess_words_over_one_copy"] for v in lines),
               "exact_duplicate_sentence_excess_words": sum(v["excess_words_over_one_copy"] for v in sentences)},
    "startup_profiles_excluding_bridge_and_dynamic_task_context": profiles,
    "root_bridge": {"words": words(bridge_bytes.decode()), "sha256": digest(bridge_bytes), "pinned_in_manifest": False},
    "direct_core_action_routes": routes,
    "route_source_inventory": route_sources,
    "core_direct_route_unique_files": len(route_sources),
    "core_direct_route_unique_words": sum(v["words"] for v in route_sources.values()),
    "handoff_source_sections": {"split_marker": "## Remote-main policy delivery",
                                "total_words": words(handoff_text), "contract_words": words(handoff_contract),
                                "historical_section_words": words(handoff_text)-words(handoff_contract)},
    "exact_repeated_metadata": md,
    "exact_repeated_nonmetadata_lines_min_8_words": lines,
    "exact_repeated_prose_sentences_min_8_words": sentences,
    "limits": ["No tokenizer, token/context/time/cost/productivity or causal estimate.",
               "Sentence splitting is a declared heuristic; semantic rule repetition is assessed separately.",
               "Direct routes are conditional alternatives, not a universal load requirement or transitive closure.",
               "Manifest is a selected corpus, not all organization instructions; unpinned route hashes are measured now.",
               "Repeated-text counts overlap between metrics and are not additive deletable-word totals."]}
print(json.dumps(out, indent=2, sort_keys=True))
