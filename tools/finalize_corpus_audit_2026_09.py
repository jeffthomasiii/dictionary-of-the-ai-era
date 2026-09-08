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
ALIAS_MAP = {
    "Function Calling": "Tool Calling",
    "Model Evaluation": "Eval",
    "Few-Shot Prompting": "Few-Shot",
    "Zero-Shot Prompting": "Zero-Shot",
    "Chain-of-Thought Prompting": "Chain-of-Thought",
    "Vector Embedding": "Embedding",
    "Vector Store": "Vector Database",
    "Retrieval-Augmented Generation": "RAG",
    "Knowledge Distillation": "Distillation",
    "Re-ranking": "Reranking",
    "Model Parameters": "Parameters",
    "Weights": "Model Weights",
    "Training Dataset": "Training Data",
    "System Message": "System Prompt",
    "Developer Message": "Developer Prompt",
    "User Message": "User Prompt",
    "Model-as-a-Judge": "LLM-as-a-Judge",
    "LLM Judge": "LLM-as-a-Judge",
    "AI Jailbreak": "Jailbreak",
    "LLM Jailbreak": "Jailbreak",
    "Jailbreaking": "Jailbreak",
    "AI Red Teaming": "Red Teaming",
    "Prompt Injection Attack": "Prompt Injection",
    "Artificial Neural Network": "Neural Network",
    "ANN": "Neural Network",
    "Supervised Machine Learning": "Supervised Learning",
    "Low-Rank Adaptation": "LoRA",
    "Parameter-Efficient Fine-Tuning": "PEFT",
    "One-Shot Prompting": "One-Shot",
}
ALIASES_TO_ADD = {
    "Eval": ["Model Evaluation"],
    "Few-Shot": ["Few-Shot Prompting"],
    "Zero-Shot": ["Zero-Shot Prompting"],
    "Chain-of-Thought": ["Chain-of-Thought Prompting"],
    "Jailbreak": ["Jailbreaking"],
    "Prompt Injection": ["Prompt Injection Attack"],
}

# Restore the existing main-branch provenance order, then append only the eight new records.
prov_path = ROOT / "data/provenance.json"
current = json.loads(prov_path.read_text(encoding="utf-8"))
base = json.loads(subprocess.check_output(
    ["git", "show", "origin/main:data/provenance.json"], cwd=ROOT, text=True
))
for slug in NEW_SLUGS:
    base[slug] = current[slug]
prov_path.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Apply resolved alias decisions to canonical term search metadata.
terms_path = ROOT / "data/terms.json"
terms = json.loads(terms_path.read_text(encoding="utf-8"))
by_name = {item["term"]: item for item in terms}
for target, additions in ALIASES_TO_ADD.items():
    aliases = by_name[target].setdefault("aliases", [])
    folded = {value.casefold() for value in aliases}
    for alias in additions:
        if alias.casefold() not in folded:
            aliases.append(alias)
            folded.add(alias.casefold())
terms_path.write_text(json.dumps(terms, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

# Keep the expansion section inside the active inventory; only move it if it still follows Related documentation.
candidate_path = ROOT / "docs/CORPUS-CANDIDATES.md"
text = candidate_path.read_text(encoding="utf-8")
marker = "## September 2026 audit expansion"
related = "## Related documentation"
if marker in text and related in text and text.index(marker) > text.index(related):
    marker_pos = text.index(marker)
    section_start = text.rfind("\n---\n", 0, marker_pos)
    if section_start < 0:
        section_start = marker_pos
    expansion = text[section_start:].strip()
    text = text[:section_start].rstrip() + "\n"
    related_pos = text.index(related)
    text = text[:related_pos].rstrip() + "\n\n---\n\n" + expansion.lstrip("-\n ") + "\n\n" + text[related_pos:]

# Remove candidates whose disposition is now a resolved alias rather than an open candidate.
for candidate in ALIAS_MAP:
    plain = re.compile(rf"^- {re.escape(candidate)}\s*$", re.MULTILINE | re.IGNORECASE)
    linked = re.compile(rf"^- \[{re.escape(candidate)}\]\([^\n]+\)\s*$", re.MULTILINE | re.IGNORECASE)
    text = plain.sub("", text)
    text = linked.sub("", text)
text = re.sub(r"\n{3,}", "\n\n", text)

inventory_slice = text[text.index("## Repository roadmap candidates"):text.index(related)]
count = sum(1 for line in inventory_slice.splitlines() if line.startswith("- "))
text = re.sub(
    r"\*\*Current unpublished inventory: [^\n]+",
    f"**Current unpublished inventory: {count} candidates.** The inventory combines the original repository-roadmap and research pools with later audit expansions.",
    text,
    count=1,
)
candidate_path.write_text(text, encoding="utf-8")

# Validate publication state and dataset parity.
provenance = json.loads(prov_path.read_text(encoding="utf-8"))
term_slugs = {item["slug"] for item in terms}
if term_slugs != set(provenance):
    raise SystemExit("term/provenance slug parity failed")
if len(terms) != 130:
    raise SystemExit(f"expected 130 published terms, found {len(terms)}")
for slug in NEW_SLUGS:
    if provenance[slug].get("researchStatus") != "pending":
        raise SystemExit(f"expected pending provenance for {slug}")
print(f"Validated 130 published terms, 8 pending records, and {count} unresolved/observed candidates.")
