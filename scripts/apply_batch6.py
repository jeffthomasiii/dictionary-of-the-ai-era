import json
import pathlib
import html

root = pathlib.Path('.')
terms_path = root / 'data/terms.json'
prov_path = root / 'data/provenance.json'
stage_path = root / 'data/batch6-stage.json'
roadmap_path = root / 'CORPUS-ROADMAP.md'
app_path = root / 'assets/js/app.js'

terms = json.loads(terms_path.read_text())
prov = json.loads(prov_path.read_text())
stage_text = stage_path.read_text()
try:
    stage = json.loads(stage_text)
except json.JSONDecodeError:
    stage = json.loads(stage_text + '}')

assert len(terms) == 85, len(terms)
existing = {t['slug'] for t in terms}
new_slugs = [t['slug'] for t in stage['terms']]
assert len(new_slugs) == 15
assert len(new_slugs) == len(set(new_slugs))
assert not (existing & set(new_slugs))
assert set(new_slugs) == set(stage['provenance'])

terms.extend(stage['terms'])
terms.sort(key=lambda t: t['term'].lower())
prov.update(stage['provenance'])
slugs = {t['slug'] for t in terms}

assert len(terms) == 100, len(terms)
assert slugs == set(prov), (len(slugs), len(prov))

for term in terms:
    for field in ('term', 'slug', 'pronunciation', 'definition', 'example', 'categories', 'status', 'partOfSpeech'):
        assert term.get(field), (term.get('slug'), field)

for slug, rec in prov.items():
    assert rec.get('researchStatus') == 'researched', slug
    assert rec.get('sources'), slug
    for src in rec['sources']:
        assert src.get('id') and src.get('url') and src.get('supports'), (slug, src)
    for rel in rec.get('relatedTerms', []):
        assert rel in slugs, (slug, rel)
        assert rel != slug, (slug, rel)

terms_path.write_text(json.dumps(terms, ensure_ascii=False, separators=(',', ':')) + '\n')
prov_path.write_text(json.dumps(prov, ensure_ascii=False, indent=2) + '\n')

for term in stage['terms']:
    d = root / 'terms' / term['slug']
    d.mkdir(parents=True, exist_ok=True)
    title = html.escape(term['term'])
    desc = html.escape(term['definition'], quote=True)
    pron = html.escape(term['pronunciation'])
    body = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">
<title>{title} | AILex</title><meta name="description" content="{desc}">
<script>(()=>{{try{{const s=localStorage.getItem("ai-era-theme");const d=window.matchMedia("(prefers-color-scheme: dark)").matches;document.documentElement.dataset.theme=s||(d?"dark":"light")}}catch(_){{document.documentElement.dataset.theme="light"}}}})();</script>
<link rel="stylesheet" href="../../assets/css/styles.css"><link rel="stylesheet" href="../../assets/css/term-pages.css">
</head><body>
<header class="site-header"><div class="shell header-inner"><a class="brand" href="../../" aria-label="AILex home"><span class="brand-mark" aria-hidden="true">◎</span><span>AILex</span></a><nav class="primary-nav" aria-label="Primary navigation"><a class="active" href="../../">Browse</a><a href="../../categories.html">Categories</a><a href="../../about.html">About</a><a href="../../contribute.html">Contribute</a><a href="../../methodology.html">Methodology</a></nav><button id="theme-toggle" class="theme-toggle" type="button" aria-label="Switch color theme" title="Switch color theme"><span class="sun" aria-hidden="true">☼</span><span class="toggle-track"><span class="toggle-knob"></span></span><span class="moon" aria-hidden="true">☾</span></button></div></header>
<main id="term-page" class="term-page shell" data-term-slug="{term['slug']}"><div id="term-fallback" class="term-fallback"><nav class="term-breadcrumb" aria-label="Breadcrumb"><a href="../../">Browse</a><span aria-hidden="true">/</span><span>{title}</span></nav><p class="eyebrow">AILex entry</p><h1>{title}</h1><p class="fallback-pronunciation">{pron}</p><p class="fallback-definition">{html.escape(term['definition'])}</p></div></main>
<footer class="site-footer"><div class="shell footer-inner"><span class="footer-mark" aria-hidden="true">◎</span><p><strong>AILex · Dictionary of the AI Era</strong><br>Vibe coded · Human-directed · AI-assisted · Human-reviewed</p><p class="footer-license">Code: MIT · Content: CC BY 4.0</p></div></footer>
<script src="../../assets/js/app.js"></script><script src="../../assets/js/term-page.js"></script></body></html>
'''
    (d / 'index.html').write_text(body)

road = roadmap_path.read_text()
lines = road.splitlines()
lines[2] = 'AILex now has **100 published, researched entries** after Batch 6. The corpus portion of the MVP threshold has been reached; future additions should be driven by editorial value rather than a numeric target.'
road = '\n'.join(lines).rstrip() + '''

## Batch 6 — MVP Balancing & Completion

1. Multi-Agent System
2. Computer Use
3. Orchestration
4. Text-to-Image
5. Temperature
6. Mixture of Experts (MoE)
7. Benchmark
8. Eval
9. LLM-as-a-Judge
10. Red Teaming
11. AI Alignment
12. Guardrail
13. Jailbreak
14. AI Governance
15. Deepfake

After Batch 6, the published corpus reaches **100 terms**. This satisfies the numeric corpus threshold for the AILex MVP while deliberately broadening coverage across agents, generation, evaluation, safety, governance, and culture/media.

## Corpus MVP status

**Threshold reached: 100 published terms.** The remaining MVP work is product readiness: category browsing, publishing/SEO foundations, edition/versioning, documentation alignment, cross-device QA, and the public brand/domain decision.
'''
roadmap_path.write_text(road)

app = app_path.read_text()
anchor = '  "ai-agent": "A I agent",\n'
addition = '  "ai-agent": "A I agent",\n  "ai-alignment": "A I alignment",\n  "ai-governance": "A I governance",\n'
assert anchor in app
app = app.replace(anchor, addition, 1)
anchor2 = '  "mcp": "M C P",\n'
addition2 = '  "llm-as-a-judge": "L L M as a judge",\n  "mcp": "M C P",\n'
assert anchor2 in app
app = app.replace(anchor2, addition2, 1)
app_path.write_text(app)

stage_path.unlink()
print('Validated final AILex MVP corpus: 100 terms, 100 provenance records, 15 new pages.')
