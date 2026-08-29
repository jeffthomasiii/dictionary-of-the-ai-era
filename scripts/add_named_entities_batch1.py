#!/usr/bin/env python3
import json
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TERMS_PATH = ROOT / "data" / "terms.json"
PROVENANCE_PATH = ROOT / "data" / "provenance.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
TEMPLATE_PATH = ROOT / "terms" / "copilot" / "index.html"
DATE = "2026-08-29"
ENTITY_CATEGORY = "AI Organizations, Products & Models"
TECH_CATEGORY = "AI Systems & Technical Concepts"
BASE_URL = "https://jeffthomasiii.github.io/dictionary-of-the-ai-era/terms/"

entries = [
    {
        "term": "OpenAI", "slug": "openai", "pronunciation": "OH-puhn A-I",
        "definition": "An AI research and deployment organization known for developing the GPT model family and the ChatGPT product.",
        "example": "OpenAI publishes research, models, and products that are frequently referenced in discussions of generative AI.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "organization"
    },
    {
        "term": "ChatGPT", "slug": "chatgpt", "pronunciation": "chat G-P-T",
        "definition": "A conversational AI product from OpenAI that lets people interact with AI models through natural-language conversation and built-in tools.",
        "example": "She used ChatGPT to discuss the document, ask follow-up questions, and revise a draft.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "product"
    },
    {
        "term": "GPT", "slug": "gpt", "pronunciation": "G-P-T",
        "definition": "The name for OpenAI's Generative Pre-trained Transformer model family and lineage, used across successive generations of general-purpose AI models.",
        "example": "GPT refers to the model lineage, while ChatGPT refers to the product people use to interact with models and tools.",
        "categories": [ENTITY_CATEGORY, TECH_CATEGORY], "aliases": ["Generative Pre-trained Transformer"], "status": "Established", "partOfSpeech": "proper noun", "entryType": "model-family"
    },
    {
        "term": "Anthropic", "slug": "anthropic", "pronunciation": "an-THRAH-pik",
        "definition": "An AI company and public benefit corporation that develops Claude and conducts research on AI capabilities, safety, and societal impacts.",
        "example": "Anthropic publishes Claude models as well as research about AI safety and behavior.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "organization"
    },
    {
        "term": "Claude", "slug": "claude", "pronunciation": "klawd",
        "definition": "Anthropic's AI assistant and product, built around the Claude family of AI models and available through conversational and developer-facing interfaces.",
        "example": "The team used Claude to analyze documents and then tested the same workflow through Anthropic's developer tools.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "product"
    },
    {
        "term": "Claude Opus", "slug": "claude-opus", "pronunciation": "klawd OH-pus",
        "definition": "A recurring model line in Anthropic's Claude family, introduced as the Opus tier in the Claude 3 family and continued across later Claude generations.",
        "example": "The documentation referred to Claude Opus as a model line rather than treating each Opus release as an unrelated name.",
        "categories": [ENTITY_CATEGORY, TECH_CATEGORY], "aliases": ["Opus"], "status": "Established", "partOfSpeech": "proper noun", "entryType": "model-family"
    },
    {
        "term": "Claude Sonnet", "slug": "claude-sonnet", "pronunciation": "klawd SON-it",
        "definition": "A recurring model line in Anthropic's Claude family, introduced as the Sonnet tier in the Claude 3 family and continued across later Claude generations.",
        "example": "A developer may encounter several numbered releases that all belong to the Claude Sonnet model line.",
        "categories": [ENTITY_CATEGORY, TECH_CATEGORY], "aliases": ["Sonnet"], "status": "Established", "partOfSpeech": "proper noun", "entryType": "model-family"
    },
    {
        "term": "Claude Haiku", "slug": "claude-haiku", "pronunciation": "klawd HY-koo",
        "definition": "A recurring model line in Anthropic's Claude family, introduced as the Haiku tier in the Claude 3 family and continued across later Claude generations.",
        "example": "Claude Haiku identifies a continuing model line even as individual Haiku versions change over time.",
        "categories": [ENTITY_CATEGORY, TECH_CATEGORY], "aliases": ["Haiku"], "status": "Established", "partOfSpeech": "proper noun", "entryType": "model-family"
    },
    {
        "term": "Microsoft", "slug": "microsoft", "pronunciation": "MY-kroh-soft",
        "definition": "A technology company whose AI-era products and services include Microsoft Copilot and other Copilot-branded experiences across its software ecosystem.",
        "example": "Microsoft uses the Copilot name across several AI experiences, so the organization and individual products should be distinguished.",
        "categories": [ENTITY_CATEGORY], "aliases": ["Microsoft Corporation"], "status": "Established", "partOfSpeech": "proper noun", "entryType": "organization"
    },
    {
        "term": "Microsoft Copilot", "slug": "microsoft-copilot", "pronunciation": "MY-kroh-soft KOH-py-lot",
        "definition": "Microsoft's general-purpose AI companion product, distinct from the generic AI-era use of copilot and from specialized products such as GitHub Copilot.",
        "example": "Microsoft Copilot is a product name, while copilot can also be used generically for an AI assistant that works alongside a person.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "product"
    },
    {
        "term": "GitHub", "slug": "github", "pronunciation": "GIT-hub",
        "definition": "An organization and software development platform used to host, build, review, and collaborate on software, including AI-assisted development through GitHub Copilot.",
        "example": "Developers may use GitHub for repositories and collaboration while using GitHub Copilot for AI-assisted coding workflows.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "organization"
    },
    {
        "term": "GitHub Copilot", "slug": "github-copilot", "pronunciation": "GIT-hub KOH-py-lot",
        "definition": "An AI coding assistant from GitHub that provides contextual assistance across code editors, GitHub, command-line tools, and software-development workflows.",
        "example": "The developer used GitHub Copilot to explain code, propose edits, and help work through a repository task.",
        "categories": [ENTITY_CATEGORY], "aliases": [], "status": "Established", "partOfSpeech": "proper noun", "entryType": "product"
    },
]

for entry in entries:
    entry["added"] = DATE
    entry["lastReviewed"] = DATE
    entry["sources"] = []

provenance = {
    "openai": {
        "researchStatus": "researched",
        "origin": "OpenAI is the name of an AI research and deployment organization. Its current structure consists of the nonprofit OpenAI Foundation and the for-profit OpenAI Group, which operates as a public benefit corporation.",
        "firstKnownUse": None,
        "history": [],
        "relatedTerms": ["chatgpt", "gpt"],
        "sources": [{"id":"openai-about","type":"primary","publisher":"OpenAI","title":"About","published":None,"url":"https://openai.com/about/","supports":["definition","usage"]}]
    },
    "chatgpt": {
        "researchStatus": "researched",
        "origin": "OpenAI introduced ChatGPT publicly as a conversational system in November 2022. The name now refers to OpenAI's conversational AI product rather than to the GPT model family itself.",
        "firstKnownUse": None,
        "history": [{"date":"2022-11-30","event":"OpenAI publicly introduced ChatGPT as a research preview built for conversational interaction."}],
        "relatedTerms": ["openai", "gpt", "large-language-model"],
        "sources": [
            {"id":"openai-chatgpt-2022","type":"primary","publisher":"OpenAI","title":"Introducing ChatGPT","published":"2022-11-30","url":"https://openai.com/index/chatgpt/","supports":["origin","history","usage"]},
            {"id":"openai-chatgpt-faq-2026","type":"primary","publisher":"OpenAI","title":"What is ChatGPT: FAQ","published":None,"url":"https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq","supports":["definition","usage"]}
        ]
    },
    "gpt": {
        "researchStatus": "researched",
        "origin": "GPT expands to Generative Pre-trained Transformer. OpenAI uses GPT as the recurring name for a model lineage that combines transformer architectures with generative pre-training and has continued through multiple model generations.",
        "firstKnownUse": None,
        "history": [
            {"date":"2018-06-11","event":"OpenAI published its early work combining transformers with generative pre-training for language understanding."},
            {"date":"2023-03-17","event":"An OpenAI publication explicitly described GPT models as Generative Pre-trained Transformer models."}
        ],
        "relatedTerms": ["openai", "chatgpt", "transformer", "pretraining", "large-language-model"],
        "sources": [
            {"id":"openai-language-unsupervised-2018","type":"primary","publisher":"OpenAI","title":"Improving language understanding with unsupervised learning","published":"2018-06-11","url":"https://openai.com/index/language-unsupervised/","supports":["history"]},
            {"id":"openai-gpts-are-gpts-2023","type":"primary","publisher":"OpenAI","title":"GPTs are GPTs: An early look at the labor market impact potential of large language models","published":"2023-03-17","url":"https://openai.com/index/gpts-are-gpts/","supports":["definition","origin","usage"]},
            {"id":"openai-gpt5","type":"primary","publisher":"OpenAI","title":"GPT-5 is here","published":None,"url":"https://openai.com/gpt-5/","supports":["usage"]}
        ]
    },
    "anthropic": {
        "researchStatus": "researched",
        "origin": "Anthropic is an AI company organized as a public benefit corporation. It develops Claude and publishes research concerning AI capabilities, safety, governance, and societal impacts.",
        "firstKnownUse": None,
        "history": [],
        "relatedTerms": ["claude", "claude-opus", "claude-sonnet", "claude-haiku"],
        "sources": [
            {"id":"anthropic-home","type":"primary","publisher":"Anthropic","title":"Anthropic","published":None,"url":"https://www.anthropic.com/","supports":["definition","usage"]},
            {"id":"anthropic-company","type":"primary","publisher":"Anthropic","title":"Company","published":None,"url":"https://www.anthropic.com/company","supports":["definition","usage"]}
        ]
    },
    "claude": {
        "researchStatus": "researched",
        "origin": "Anthropic introduced Claude publicly in March 2023 as an AI assistant accessible through conversational and developer-facing interfaces. Claude now names Anthropic's assistant product while also serving as the umbrella brand for Claude models.",
        "firstKnownUse": None,
        "history": [{"date":"2023-03-14","event":"Anthropic publicly introduced Claude as an AI assistant for conversational and text-processing tasks."}],
        "relatedTerms": ["anthropic", "claude-opus", "claude-sonnet", "claude-haiku"],
        "sources": [
            {"id":"anthropic-introducing-claude-2023","type":"primary","publisher":"Anthropic","title":"Introducing Claude","published":"2023-03-14","url":"https://www.anthropic.com/news/introducing-claude","supports":["origin","history","definition"]},
            {"id":"anthropic-meet-claude","type":"primary","publisher":"Anthropic","title":"Meet Claude","published":None,"url":"https://www.anthropic.com/claude","supports":["definition","usage"]}
        ]
    },
    "claude-opus": {
        "researchStatus": "researched",
        "origin": "Anthropic introduced Opus as one of the three named model lines in the Claude 3 family in March 2024. The Opus name has continued across later Claude generations, so EpochLex treats Claude Opus as a model-family entry rather than creating an entry for every numbered release.",
        "firstKnownUse": None,
        "history": [{"date":"2024-03-04","event":"Anthropic announced the Claude 3 family with Haiku, Sonnet, and Opus model names."}],
        "relatedTerms": ["anthropic", "claude", "claude-sonnet", "claude-haiku"],
        "sources": [
            {"id":"anthropic-claude3-family-2024","type":"primary","publisher":"Anthropic","title":"Introducing the next generation of Claude","published":"2024-03-04","url":"https://www.anthropic.com/research/claude-3-family","supports":["origin","history","definition"]},
            {"id":"anthropic-claude-opus","type":"primary","publisher":"Anthropic","title":"Claude Opus","published":None,"url":"https://www.anthropic.com/claude/opus","supports":["usage"]}
        ]
    },
    "claude-sonnet": {
        "researchStatus": "researched",
        "origin": "Anthropic introduced Sonnet as one of the three named model lines in the Claude 3 family in March 2024. The Sonnet name has continued across later Claude generations, so EpochLex treats Claude Sonnet as a model-family entry rather than creating an entry for every numbered release.",
        "firstKnownUse": None,
        "history": [{"date":"2024-03-04","event":"Anthropic announced the Claude 3 family with Haiku, Sonnet, and Opus model names."}],
        "relatedTerms": ["anthropic", "claude", "claude-opus", "claude-haiku"],
        "sources": [{"id":"anthropic-claude3-family-2024","type":"primary","publisher":"Anthropic","title":"Introducing the next generation of Claude","published":"2024-03-04","url":"https://www.anthropic.com/research/claude-3-family","supports":["origin","history","definition","usage"]}]
    },
    "claude-haiku": {
        "researchStatus": "researched",
        "origin": "Anthropic introduced Haiku as one of the three named model lines in the Claude 3 family in March 2024. The Haiku name has continued across later Claude generations, so EpochLex treats Claude Haiku as a model-family entry rather than creating an entry for every numbered release.",
        "firstKnownUse": None,
        "history": [{"date":"2024-03-04","event":"Anthropic announced the Claude 3 family with Haiku, Sonnet, and Opus model names."}],
        "relatedTerms": ["anthropic", "claude", "claude-opus", "claude-sonnet"],
        "sources": [{"id":"anthropic-claude3-family-2024","type":"primary","publisher":"Anthropic","title":"Introducing the next generation of Claude","published":"2024-03-04","url":"https://www.anthropic.com/research/claude-3-family","supports":["origin","history","definition","usage"]}]
    },
    "microsoft": {
        "researchStatus": "researched",
        "origin": "Microsoft is a technology company whose current product ecosystem includes Microsoft Copilot and other AI-assisted software and services.",
        "firstKnownUse": None,
        "history": [],
        "relatedTerms": ["microsoft-copilot"],
        "sources": [{"id":"microsoft-about","type":"primary","publisher":"Microsoft","title":"Our Mission and Values","published":None,"url":"https://www.microsoft.com/en-us/about","supports":["definition","usage"]}]
    },
    "microsoft-copilot": {
        "researchStatus": "researched",
        "origin": "Microsoft consolidated Bing Chat and Bing Chat Enterprise under the Copilot name in 2023 as part of a broader Copilot product strategy. The product name is distinct from the generic AI-era use of the word copilot.",
        "firstKnownUse": None,
        "history": [{"date":"2023-11-15","event":"Microsoft announced that Bing Chat and Bing Chat Enterprise would become Copilot as it simplified its Copilot product line."}],
        "relatedTerms": ["microsoft", "copilot"],
        "sources": [
            {"id":"microsoft-copilot-2023","type":"primary","publisher":"Microsoft","title":"Introducing Microsoft Copilot Studio and new features in Copilot for Microsoft 365","published":"2023-11-15","url":"https://www.microsoft.com/en-us/microsoft-365/blog/2023/11/15/introducing-microsoft-copilot-studio-and-new-features-in-copilot-for-microsoft-365/","supports":["origin","history","usage"]},
            {"id":"microsoft-copilot-current","type":"primary","publisher":"Microsoft","title":"Get Copilot","published":None,"url":"https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/get-copilot","supports":["definition","usage"]}
        ]
    },
    "github": {
        "researchStatus": "researched",
        "origin": "GitHub is an organization and software-development platform centered on hosting code and supporting software collaboration. Its current platform includes AI-assisted development through GitHub Copilot.",
        "firstKnownUse": None,
        "history": [],
        "relatedTerms": ["github-copilot"],
        "sources": [{"id":"github-about","type":"primary","publisher":"GitHub","title":"About GitHub","published":None,"url":"https://github.com/about","supports":["definition","usage"]}]
    },
    "github-copilot": {
        "researchStatus": "researched",
        "origin": "GitHub introduced GitHub Copilot in a technical preview in June 2021 as an AI pair-programming tool. The product has since expanded beyond code completion into broader contextual assistance across software-development workflows.",
        "firstKnownUse": None,
        "history": [{"date":"2021-06-29","event":"GitHub launched a technical preview of GitHub Copilot as an AI pair programmer."}],
        "relatedTerms": ["github", "copilot"],
        "sources": [
            {"id":"github-copilot-launch-2021","type":"primary","publisher":"GitHub","title":"Introducing GitHub Copilot: your AI pair programmer","published":"2021-06-29","url":"https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/","supports":["origin","history","usage"]},
            {"id":"github-copilot-docs","type":"primary","publisher":"GitHub","title":"What is GitHub Copilot?","published":None,"url":"https://docs.github.com/en/copilot/get-started/what-is-github-copilot","supports":["definition","usage"]}
        ]
    }
}


def build_page(template: str, entry: dict) -> str:
    old_definition = "An AI assistant designed to work alongside a person by suggesting, drafting, analyzing, summarizing, or completing portions of a task while the human remains responsible for the work."
    page = template
    page = page.replace("terms/copilot/", f"terms/{entry['slug']}/")
    page = page.replace('data-term-slug="copilot"', f'data-term-slug="{entry["slug"]}"')
    page = page.replace("KOH-py-lot", entry["pronunciation"])
    page = page.replace(old_definition, entry["definition"])
    page = page.replace("Copilot", entry["term"])
    return page


def main():
    terms = json.loads(TERMS_PATH.read_text(encoding="utf-8"))
    existing = {t["slug"] for t in terms}
    for entry in entries:
        if entry["slug"] in existing:
            raise SystemExit(f"Entry already exists: {entry['slug']}")
    terms.extend(entries)
    terms.sort(key=lambda t: t["term"].casefold())
    TERMS_PATH.write_text(json.dumps(terms, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    prov = json.loads(PROVENANCE_PATH.read_text(encoding="utf-8"))
    overlap = set(provenance) & set(prov)
    if overlap:
        raise SystemExit(f"Provenance already exists: {sorted(overlap)}")
    prov.update(provenance)
    if "copilot" in prov:
        rel = prov["copilot"].setdefault("relatedTerms", [])
        for slug in ["microsoft-copilot", "github-copilot"]:
            if slug not in rel:
                rel.append(slug)
    PROVENANCE_PATH.write_text(json.dumps(prov, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    for entry in entries:
        out_dir = ROOT / "terms" / entry["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(build_page(template, entry), encoding="utf-8")

    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    existing_urls = {u.find(f"{ns}loc").text for u in root.findall(f"{ns}url")}
    for entry in entries:
        url = f"{BASE_URL}{entry['slug']}/"
        if url in existing_urls:
            continue
        node = ET.SubElement(root, f"{ns}url")
        ET.SubElement(node, f"{ns}loc").text = url
        ET.SubElement(node, f"{ns}lastmod").text = DATE
    ET.indent(tree, space="  ")
    tree.write(SITEMAP_PATH, encoding="utf-8", xml_declaration=True)

    terms2 = json.loads(TERMS_PATH.read_text(encoding="utf-8"))
    prov2 = json.loads(PROVENANCE_PATH.read_text(encoding="utf-8"))
    slugs = {t["slug"] for t in terms2}
    assert len(terms2) == 112, len(terms2)
    assert set(prov2) == slugs, (len(prov2), len(slugs), sorted(set(prov2) ^ slugs))
    for entry in entries:
        assert entry["entryType"] in {"organization", "product", "model-family", "model"}
        assert (ROOT / "terms" / entry["slug"] / "index.html").exists()
    for slug, record in prov2.items():
        for related in record.get("relatedTerms", []):
            assert related in slugs, f"{slug} -> missing {related}"
            assert related != slug, f"{slug} links to itself"
    ET.parse(SITEMAP_PATH)
    print(f"Added {len(entries)} entries; corpus now has {len(terms2)} entries and matching provenance records.")


if __name__ == "__main__":
    main()
