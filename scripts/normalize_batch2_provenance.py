#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'data' / 'provenance.json'
current = json.loads(path.read_text())
new_slugs = ['google','gemini','meta','llama','xai','grok','mistral-ai','mistral']
new_records = {slug: current[slug] for slug in new_slugs}
base_text = subprocess.check_output(['git','show','origin/main:data/provenance.json'], text=True)
base = json.loads(base_text)
for slug in new_slugs:
    if slug in base:
        raise SystemExit(f'{slug} already exists on main')
    base[slug] = new_records[slug]
path.write_text(json.dumps(base, ensure_ascii=False, indent=2) + '\n')
json.loads(path.read_text())
print('Provenance restored to main ordering with 8 appended batch-2 records.')
