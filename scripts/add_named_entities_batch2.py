#!/usr/bin/env python3
import json
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TERMS = ROOT / "data" / "terms.json"
PROV = ROOT / "data" / "provenance.json"
SITEMAP = ROOT / "sitemap.xml"
DATE = "2026-08-29"
CATEGORY = "AI Organizations, Products & Models"
BASE = "https://jeffthomasiii.github.io/dictionary-of-the-ai-era/terms"

new_terms = [
  {
    "term":"Google","slug":"google","pronunciation":"GOO-gul","definition":"A technology company whose work includes artificial intelligence research, products, developer platforms, and model families such as Gemini.","example":"Google publishes Gemini models and makes Gemini available across several of its products and developer services.","categories":[CATEGORY],"aliases":[],"status":"Established","partOfSpeech":"noun","entryType":"organization","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"Gemini","slug":"gemini","pronunciation":"JEM-ih-nye","definition":"Google's AI assistant and product brand, and also the name used for a continuing family of multimodal AI models.","example":"A person may use the Gemini app while a developer refers separately to a Gemini model through an API.","categories":[CATEGORY],"aliases":["Google Gemini"],"status":"Established","partOfSpeech":"noun","entryType":"product","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"Meta","slug":"meta","pronunciation":"MET-uh","definition":"A technology company, formerly branded as the Facebook company, whose AI work includes products, research, and the Llama model family.","example":"Meta publishes Llama models while also using AI throughout products such as Facebook, Instagram, WhatsApp, and Meta AI.","categories":[CATEGORY],"aliases":["Meta Platforms"],"status":"Established","partOfSpeech":"noun","entryType":"organization","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"Llama","slug":"llama","pronunciation":"LAH-muh","definition":"A continuing family and platform of AI models released by Meta, first introduced in 2023 under the styling LLaMA.","example":"A developer evaluating Llama should distinguish the overall model family from a specific release such as Llama 4 Scout.","categories":[CATEGORY],"aliases":["LLaMA"],"status":"Established","partOfSpeech":"noun","entryType":"model-family","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"xAI","slug":"xai","pronunciation":"ex-A-I","definition":"An AI company founded in 2023 that developed Grok before being acquired by SpaceX in February 2026; its AI services are now presented under SpaceXAI.","example":"Older articles may describe Grok as an xAI product, while current official materials identify SpaceXAI as the operator.","categories":[CATEGORY],"aliases":["X.AI"],"status":"Historical organization","partOfSpeech":"noun","entryType":"organization","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"Grok","slug":"grok","pronunciation":"grok","definition":"A conversational generative AI product and brand originally developed by xAI and now offered by SpaceXAI, with related model and multimodal services carrying the Grok name.","example":"Someone using Grok may be interacting with the consumer assistant, while a developer may refer to a Grok model through the API.","categories":[CATEGORY],"aliases":[],"status":"Established","partOfSpeech":"noun","entryType":"product","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"Mistral AI","slug":"mistral-ai","pronunciation":"MIS-truhl A-I","definition":"An AI company founded in 2023 that develops and provides AI models, developer tools, and services for building and deploying AI systems.","example":"Mistral AI publishes several generalist and specialist model lines rather than a single permanent model called Mistral.","categories":[CATEGORY],"aliases":[],"status":"Established","partOfSpeech":"noun","entryType":"organization","added":DATE,"lastReviewed":DATE,"sources":[]
  },
  {
    "term":"Mistral","slug":"mistral","pronunciation":"MIS-truhl","definition":"A name used across continuing families of AI models from Mistral AI, including model lines such as Mistral Large, Mistral Medium, and Mistral Small.","example":"Saying an application uses Mistral is less specific than naming the particular Mistral model or model line it uses.","categories":[CATEGORY],"aliases":[],"status":"Established","partOfSpeech":"noun","entryType":"model-family","added":DATE,"lastReviewed":DATE,"sources":[]
  }
]

new_prov = {
  "google": {
    "researchStatus":"researched","origin":"Google began as a search-engine project at Stanford and Google Inc. was formally established in 1998. The company later became a major developer and deployer of AI technologies across research, products, cloud services, and model families.","firstKnownUse":None,
    "history":[{"date":"1998","event":"Google Inc. was formally established after the search project created by Larry Page and Sergey Brin attracted early investment."},{"date":"2023-12-06","event":"Google introduced Gemini, a new family of AI models developed through Google DeepMind and teams across Google."}],
    "relatedTerms":["gemini"],
    "sources":[
      {"id":"google-company-info","type":"primary","publisher":"Google","title":"About Google: History, office locations, commitments, initiatives","published":None,"url":"https://about.google/company-info/","supports":["definition","usage"]},
      {"id":"google-story","type":"primary","publisher":"Google","title":"From the garage to the Googleplex","published":None,"url":"https://about.google/company-info/our-story/","supports":["origin","history"]},
      {"id":"google-gemini-2023","type":"primary","publisher":"Google","title":"Introducing Gemini: our largest and most capable AI model","published":"2023-12-06","url":"https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/","supports":["history","usage"]}
    ]
  },
  "gemini": {
    "researchStatus":"researched","origin":"Google introduced Gemini on December 6, 2023 as a new generation of multimodal AI models. The Gemini name later also became the consumer-facing assistant and app brand, so current usage spans both a product experience and model families.","firstKnownUse":"2023-12-06",
    "history":[{"date":"2023-12-06","event":"Google introduced Gemini as its new family of multimodal AI models."},{"date":"2026-05-19","event":"Google described the Gemini app as an AI assistant while continuing to release Gemini model families, illustrating the name's dual product-and-model usage."}],
    "relatedTerms":["google","multimodal","large-language-model"],
    "sources":[
      {"id":"google-gemini-2023","type":"primary","publisher":"Google","title":"Introducing Gemini: our largest and most capable AI model","published":"2023-12-06","url":"https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/","supports":["definition","origin","first-known-use","history"]},
      {"id":"google-gemini-app-2026","type":"primary","publisher":"Google","title":"The Gemini app becomes more agentic, delivering proactive, 24/7 help","published":"2026-05-19","url":"https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/","supports":["definition","usage","history"]},
      {"id":"google-gemini-3-5-2026","type":"primary","publisher":"Google","title":"Gemini 3.5: frontier intelligence with action","published":"2026-05-19","url":"https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/","supports":["definition","usage"]}
    ]
  },
  "meta": {
    "researchStatus":"researched","origin":"The company formerly branded as Facebook adopted the Meta company brand in October 2021. Meta now develops social platforms, devices, AI products, and model families including Llama.","firstKnownUse":"2021-10-28",
    "history":[{"date":"2021-10-28","event":"The Facebook company introduced Meta as its new company brand."},{"date":"2023-02-24","event":"Meta introduced the first LLaMA large language model release."}],
    "relatedTerms":["llama"],
    "sources":[
      {"id":"meta-company-2021","type":"primary","publisher":"Meta","title":"Introducing Meta: A Social Technology Company","published":"2021-10-28","url":"https://about.fb.com/news/2021/10/facebook-company-is-now-meta/","supports":["definition","origin","first-known-use","history"]},
      {"id":"meta-llama-2023","type":"primary","publisher":"Meta AI","title":"Introducing LLaMA: A foundational, 65-billion-parameter large language model","published":"2023-02-24","url":"https://ai.meta.com/blog/large-language-model-llama-meta-ai/","supports":["history","usage"]}
    ]
  },
  "llama": {
    "researchStatus":"researched","origin":"Meta introduced the original model in February 2023 using the styling LLaMA, short for Large Language Model Meta AI. Meta's current materials use Llama as the continuing family and platform name.","firstKnownUse":"2023-02-24",
    "history":[{"date":"2023-02-24","event":"Meta introduced LLaMA, short for Large Language Model Meta AI."},{"date":"2026","event":"Meta's current Llama documentation presents Llama as an ongoing model platform with multiple current models and resources."}],
    "relatedTerms":["meta","large-language-model","foundation-model","multimodal"],
    "sources":[
      {"id":"meta-llama-2023","type":"primary","publisher":"Meta AI","title":"Introducing LLaMA: A foundational, 65-billion-parameter large language model","published":"2023-02-24","url":"https://ai.meta.com/blog/large-language-model-llama-meta-ai/","supports":["definition","origin","first-known-use","history","alias"]},
      {"id":"meta-llama-current","type":"primary","publisher":"Meta AI","title":"Get started with Llama","published":None,"url":"https://ai.meta.com/llama/get-started/","supports":["definition","usage","history"]}
    ]
  },
  "xai": {
    "researchStatus":"researched","origin":"xAI was established in 2023 as an artificial-intelligence company and developed the Grok product and model line. SpaceX announced on February 2, 2026 that it had acquired xAI; current x.ai legal materials identify the operating company as SpaceXAI LLC.","firstKnownUse":None,
    "history":[{"date":"2026-02-02","event":"SpaceX announced that it had acquired xAI."},{"date":"2026-08-24","event":"Current x.ai legal materials identify SpaceXAI LLC as the company providing Grok and related services."}],
    "relatedTerms":["grok"],
    "sources":[
      {"id":"xai-series-e-2026","type":"primary","publisher":"xAI","title":"xAI Raises $20B Series E","published":"2026-01-06","url":"https://x.ai/news/series-e","supports":["definition","usage","history"]},
      {"id":"xai-joins-spacex-2026","type":"primary","publisher":"xAI","title":"xAI joins SpaceX","published":"2026-02-02","url":"https://x.ai/news/xai-joins-spacex","supports":["definition","history"]},
      {"id":"spacexai-privacy-2026","type":"primary","publisher":"SpaceXAI","title":"SpaceXAI Privacy Policy","published":"2026-08-24","url":"https://x.ai/legal/privacy-policy","supports":["definition","history","usage"]}
    ]
  },
  "grok": {
    "researchStatus":"researched","origin":"Grok was introduced by xAI as its conversational generative-AI product and model brand. After SpaceX acquired xAI in February 2026, current x.ai materials describe Grok as a SpaceXAI service powered by SpaceXAI models.","firstKnownUse":None,
    "history":[{"date":"2026-02-02","event":"SpaceX announced its acquisition of xAI, changing the organizational context around Grok."},{"date":"2026-08-24","event":"SpaceXAI's current privacy policy described Grok as a conversational generative AI powered by SpaceXAI large language models."}],
    "relatedTerms":["xai","large-language-model","multimodal"],
    "sources":[
      {"id":"spacexai-privacy-2026","type":"primary","publisher":"SpaceXAI","title":"SpaceXAI Privacy Policy","published":"2026-08-24","url":"https://x.ai/legal/privacy-policy","supports":["definition","history","usage"]},
      {"id":"spacexai-home-2026","type":"primary","publisher":"SpaceXAI","title":"SpaceXAI","published":None,"url":"https://x.ai/","supports":["definition","usage"]}
    ]
  },
  "mistral-ai": {
    "researchStatus":"researched","origin":"Mistral was founded in April 2023 with the goal of developing accessible and customizable frontier AI. Its early public work focused on open generative models, followed by broader model, platform, and deployment offerings.","firstKnownUse":None,
    "history":[{"date":"2023-04","event":"Mistral's official company history dates the company's founding to April 2023."},{"date":"2023-09-27","event":"Mistral published an early statement of its approach to open generative AI models."}],
    "relatedTerms":["mistral"],
    "sources":[
      {"id":"mistral-about","type":"primary","publisher":"Mistral","title":"About Mistral","published":None,"url":"https://mistral.ai/about/","supports":["definition","origin","history"]},
      {"id":"mistral-open-models-2023","type":"primary","publisher":"Mistral AI","title":"Bringing open AI models to the frontier","published":"2023-09-27","url":"https://mistral.ai/news/about-mistral-ai/","supports":["history","usage"]},
      {"id":"mistral-docs-current","type":"primary","publisher":"Mistral AI","title":"Mistral AI Documentation","published":None,"url":"https://docs.mistral.ai/","supports":["definition","usage"]}
    ]
  },
  "mistral": {
    "researchStatus":"researched","origin":"Mistral AI has used Mistral as a recurring family name across multiple general-purpose model lines rather than as the identifier for one permanent model. Current model listings include Mistral Large, Mistral Medium, and Mistral Small alongside specialist families.","firstKnownUse":None,
    "history":[{"date":"2023-12-11","event":"Mistral AI's early platform documentation exposed multiple Mistral-branded model endpoints rather than a single fixed Mistral model."},{"date":"2026","event":"Current Mistral model documentation lists multiple continuing Mistral model lines, including Large, Medium, and Small."}],
    "relatedTerms":["mistral-ai","large-language-model","foundation-model"],
    "sources":[
      {"id":"mistral-platform-2023","type":"primary","publisher":"Mistral AI","title":"La Plateforme","published":"2023-12-11","url":"https://mistral.ai/news/la-plateforme/","supports":["origin","history","usage"]},
      {"id":"mistral-models-current","type":"primary","publisher":"Mistral AI","title":"Models - from cloud to edge","published":None,"url":"https://mistral.ai/models/","supports":["definition","history","usage"]},
      {"id":"mistral-docs-models","type":"primary","publisher":"Mistral AI","title":"Models Overview","published":None,"url":"https://docs.mistral.ai/models","supports":["definition","usage"]}
    ]
  }
}


def term_page(term):
    title = term["term"]
    slug = term["slug"]
    desc = term["definition"]
    pron = term["pronunciation"]
    canonical = f"{BASE}/{slug}/"
    schema = json.dumps({"@context":"https://schema.org","@type":"DefinedTerm","name":title,"description":desc,"url":canonical,"inDefinedTermSet":"https://jeffthomasiii.github.io/dictionary-of-the-ai-era/","inLanguage":"en"}, ensure_ascii=False, separators=(",",":"))
    return f'''<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <meta name="color-scheme" content="light dark">\n  <title>{title} | EpochLex</title>\n  <meta name="description" content="{desc.replace('&','&amp;').replace('"','&quot;')}">\n  <link rel="canonical" href="{canonical}">\n  <meta property="og:site_name" content="EpochLex">\n  <meta property="og:title" content="{title} | EpochLex">\n  <meta property="og:description" content="{desc.replace('&','&amp;').replace('"','&quot;')}">\n  <meta property="og:type" content="article">\n  <meta property="og:url" content="{canonical}">\n  <meta name="twitter:card" content="summary">\n  <meta name="twitter:title" content="{title} | EpochLex">\n  <meta name="twitter:description" content="{desc.replace('&','&amp;').replace('"','&quot;')}">\n  <script type="application/ld+json">{schema}</script>\n  <script>\n    (() => {{\n      try {{\n        const saved = localStorage.getItem("ai-era-theme");\n        const systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches;\n        document.documentElement.dataset.theme = saved || (systemDark ? "dark" : "light");\n      }} catch (_) {{ document.documentElement.dataset.theme = "light"; }}\n    }})();\n  </script>\n  <link rel="stylesheet" href="../../assets/css/styles.css">\n  <link rel="stylesheet" href="../../assets/css/term-pages.css">\n  <link rel="stylesheet" href="../../assets/css/brand-theme.css">\n</head>\n<body>\n  <header class="site-header">\n    <div class="shell header-inner">\n      <a class="brand" href="../../" aria-label="EpochLex home"><span class="brand-lockup" aria-hidden="true"><img class="brand-lockup-image brand-lockup-light" src="../../assets/brand/epochlex/epochlex-logo-horizontal-light.png" alt=""><img class="brand-lockup-image brand-lockup-dark" src="../../assets/brand/epochlex/epochlex-logo-horizontal-dark.png" alt=""></span><span class="sr-only">EpochLex</span></a>\n      <nav class="primary-nav" aria-label="Primary navigation">\n        <a class="active" href="../../">Browse</a><a href="../../categories.html">Categories</a><a href="../../about.html">About</a><a href="../../contribute.html">Contribute</a><a href="../../methodology.html">Methodology</a>\n      </nav>\n      <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Switch color theme" title="Switch color theme"><span class="sun" aria-hidden="true">☼</span><span class="toggle-track"><span class="toggle-knob"></span></span><span class="moon" aria-hidden="true">☾</span></button>\n    </div>\n  </header>\n\n  <main id="term-page" class="term-page shell" data-term-slug="{slug}">\n    <div id="term-fallback" class="term-fallback">\n      <nav class="term-breadcrumb" aria-label="Breadcrumb"><a href="../../">Browse</a><span aria-hidden="true">/</span><span>{title}</span></nav>\n      <p class="eyebrow">EpochLex entry</p>\n      <h1>{title}</h1>\n      <p class="fallback-pronunciation">{pron}</p>\n      <p class="fallback-definition">{desc}</p>\n    </div>\n  </main>\n\n  <footer class="site-footer"><div class="shell footer-inner"><span class="footer-mark" aria-hidden="true">◎</span><p><strong>EpochLex · Dictionary of the AI Era</strong><br>Vibe coded · Human-directed · AI-assisted · Human-reviewed</p><p class="footer-license">Code: MIT · Content: CC BY 4.0</p></div></footer>\n  <script src="../../assets/js/app.js"></script>\n  <script src="../../assets/js/term-page.js"></script>\n</body>\n</html>'''

terms = json.loads(TERMS.read_text())
existing = {t["slug"] for t in terms}
for t in new_terms:
    if t["slug"] in existing:
        raise SystemExit(f"Refusing to overwrite existing term: {t['slug']}")
terms.extend(new_terms)
terms.sort(key=lambda x: x["term"].casefold())
TERMS.write_text(json.dumps(terms, ensure_ascii=False, separators=(",",":")) + "\n")

prov = json.loads(PROV.read_text())
for slug, record in new_prov.items():
    if slug in prov:
        raise SystemExit(f"Refusing to overwrite provenance: {slug}")
    prov[slug] = record
PROV.write_text(json.dumps(dict(sorted(prov.items())), ensure_ascii=False, indent=2) + "\n")

for t in new_terms:
    p = ROOT / "terms" / t["slug"] / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(term_page(t))

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
tree = ET.parse(SITEMAP)
root = tree.getroot()
ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
existing_locs = {u.find('s:loc', ns).text for u in root.findall('s:url', ns)}
for t in new_terms:
    loc = f"{BASE}/{t['slug']}/"
    if loc not in existing_locs:
        u = ET.SubElement(root, '{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        ET.SubElement(u, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text = loc
        ET.SubElement(u, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod').text = DATE
ET.indent(tree, space='  ')
tree.write(SITEMAP, encoding='utf-8', xml_declaration=True)

# Validation
terms = json.loads(TERMS.read_text())
prov = json.loads(PROV.read_text())
term_slugs = {t['slug'] for t in terms}
if len(terms) != 120:
    raise SystemExit(f"Expected 120 entries after batch 2, found {len(terms)}")
if term_slugs != set(prov):
    missing_p = sorted(term_slugs - set(prov)); missing_t = sorted(set(prov) - term_slugs)
    raise SystemExit(f"Term/provenance mismatch: missing provenance={missing_p}; missing terms={missing_t}")
valid_types = {'term','organization','product','model-family','model'}
for t in new_terms:
    if t['entryType'] not in valid_types:
        raise SystemExit(f"Invalid entryType: {t['slug']}")
    if not (ROOT / 'terms' / t['slug'] / 'index.html').exists():
        raise SystemExit(f"Missing page: {t['slug']}")
for slug, record in prov.items():
    for related in record.get('relatedTerms', []):
        if related == slug:
            raise SystemExit(f"Self-related slug: {slug}")
        if related not in term_slugs:
            raise SystemExit(f"Unresolved related slug: {slug} -> {related}")
ET.parse(SITEMAP)
print('Batch 2 validation passed: 120 entries, provenance parity, related links, pages, entry types, sitemap.')
