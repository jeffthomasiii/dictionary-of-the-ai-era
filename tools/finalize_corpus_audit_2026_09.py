#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_SLUGS = [
    "artificial-intelligence", "ground-truth", "hybrid-search",
    "natural-language-processing", "open-weight-model", "responsible-ai",
    "tokenization", "workslop",
]

# Restore the existing main-branch provenance order, then append only the eight new records.
prov_path = ROOT / "data/provenance.json"
current = json.loads(prov_path.read_text(encoding="utf-8"))
base = json.loads(subprocess.check_output(
    ["git", "show", "origin/main:data/provenance.json"], cwd=ROOT, text=True
))
for slug in NEW_SLUGS:
    base[slug] = current[slug]
prov_path.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Move the September expansion into the inventory itself and correct the inventory count.
candidate_path = ROOT / "docs/CORPUS-CANDIDATES.md"
text = candidate_path.read_text(encoding="utf-8")
marker = "## September 2026 audit expansion"
related = "## Related documentation"
if marker in text and related in text:
    marker_pos = text.index(marker)
    section_start = text.rfind("\n---\n", 0, marker_pos)
    if section_start < 0:
        section_start = marker_pos
    expansion = text[section_start:].strip()
    text = text[:section_start].rstrip() + "\n"
    related_pos = text.index(related)
    text = text[:related_pos].rstrip() + "\n\n---\n\n" + expansion.lstrip("-\n ") + "\n\n" + text[related_pos:]

inventory_slice = text[text.index("## Repository roadmap candidates"):text.index(related)]
count = sum(1 for line in inventory_slice.splitlines() if line.startswith("- "))
text = re.sub(
    r"\*\*Current unpublished inventory: [^\n]+\*\*[^\n]*",
    f"**Current unpublished inventory: {count} candidates.** The inventory combines the original repository-roadmap and research pools with later audit expansions.",
    text,
    count=1,
)
candidate_path.write_text(text, encoding="utf-8")

# Validate expected expansion math and term/provenance parity.
terms = json.loads((ROOT / "data/terms.json").read_text(encoding="utf-8"))
provenance = json.loads(prov_path.read_text(encoding="utf-8"))
term_slugs = {item["slug"] for item in terms}
if term_slugs != set(provenance):
    raise SystemExit("term/provenance slug parity failed")
if len(terms) != 130:
    raise SystemExit(f"expected 130 published terms, found {len(terms)}")
if count != 754:
    raise SystemExit(f"expected 754 unpublished candidates, found {count}")
for slug in NEW_SLUGS:
    if provenance[slug].get("researchStatus") != "pending":
        raise SystemExit(f"expected pending provenance for {slug}")
print("Validated 130 published terms, 8 pending records, and 754 unpublished candidates.")
