#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_SLUGS = [
    "artificial-intelligence",
    "ground-truth",
    "hybrid-search",
    "natural-language-processing",
    "open-weight-model",
    "responsible-ai",
    "tokenization",
    "workslop",
]

current_path = ROOT / "data/provenance.json"
current = json.loads(current_path.read_text(encoding="utf-8"))
base_text = subprocess.check_output(
    ["git", "show", "origin/main:data/provenance.json"],
    cwd=ROOT,
    text=True,
)
base = json.loads(base_text)

for slug in NEW_SLUGS:
    base[slug] = current[slug]

current_path.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Restored main-branch provenance order and retained {len(NEW_SLUGS)} new records.")
