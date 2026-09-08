#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
prov_path=ROOT/'data/provenance.json'
prov=json.loads(prov_path.read_text())
prov['data-poisoning']['relatedTerms']=['training-data','model-collapse','fine-tuning','ai-alignment']
prov['model-card']['relatedTerms']=['system-card','eval','benchmark','responsible-ai']
prov['sampling']['relatedTerms']=['temperature','inference','token','large-language-model']
prov_path.write_text(json.dumps(prov,ensure_ascii=False,indent=2)+'\n')
terms=json.loads((ROOT/'data/terms.json').read_text())
slugs={t['slug'] for t in terms}
assert len(terms)==140
assert slugs==set(prov)
assert sum(1 for x in prov.values() if x.get('researchStatus')=='pending')==18
for record in prov.values():
    for slug in record.get('relatedTerms',[]):
        assert slug in slugs, f'unpublished related term: {slug}'
print('Validated Batch B related terms and corpus parity.')