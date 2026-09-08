#!/usr/bin/env python3
import json
import re
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-08"
PUBLIC_BASE = "https://epochlex.justathoughtblog.org"

BATCH = [
    {
        "term": "Artificial Intelligence",
        "slug": "artificial-intelligence",
        "pronunciation": "ar-tuh-FISH-ul in-TEL-uh-jens",
        "definition": "The broad field of creating machine-based systems that can perform tasks associated with human intelligence, such as perception, learning, reasoning, language use, decision-making, or goal-directed action.",
        "example": "Artificial intelligence includes many approaches, from machine-learning classifiers to generative models and autonomous systems.",
        "categories": ["AI Systems & Technical Concepts"],
        "aliases": ["AI"],
        "status": "Established",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["machine-learning", "generative-ai", "artificial-general-intelligence", "ai-governance"],
    },
    {
        "term": "Ground Truth",
        "slug": "ground-truth",
        "pronunciation": "ground trooth",
        "definition": "The reference information treated as the correct or verified answer when training, testing, or evaluating an AI or machine-learning system, even though the reference itself can contain measurement, labeling, or judgment errors.",
        "example": "The evaluator compared the model's predictions with the ground-truth labels to calculate accuracy.",
        "categories": ["AI Systems & Technical Concepts", "AI Ways of Working"],
        "aliases": ["Ground-truth data"],
        "status": "Established technical term",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["eval", "benchmark", "supervised-learning", "training-data"],
    },
    {
        "term": "Hybrid Search",
        "slug": "hybrid-search",
        "pronunciation": "HY-brid serch",
        "definition": "A search approach that combines two or more retrieval methods—commonly keyword or full-text search with vector or semantic search—and merges their results into one ranked set.",
        "example": "The RAG system used hybrid search so exact product numbers and semantically similar passages could both rank highly.",
        "categories": ["AI Systems & Technical Concepts"],
        "aliases": ["Hybrid retrieval"],
        "status": "Established technical term",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["semantic-search", "vector-search", "retrieval", "rag"],
    },
    {
        "term": "Natural Language Processing",
        "slug": "natural-language-processing",
        "pronunciation": "NATCH-er-ul LANG-gwij PRAH-sess-ing",
        "definition": "A field of artificial intelligence and computer science focused on enabling computers to analyze, understand, generate, and otherwise work with human language in text or speech.",
        "example": "Natural language processing is used for tasks such as translation, search, sentiment analysis, speech systems, and conversational AI.",
        "categories": ["AI Systems & Technical Concepts"],
        "aliases": ["NLP"],
        "status": "Established",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["large-language-model", "machine-learning", "transformer", "tokenization"],
    },
    {
        "term": "Open-Weight Model",
        "slug": "open-weight-model",
        "pronunciation": "OH-puhn wayt MOD-ul",
        "definition": "An AI model whose trained weights are made available for others to download and run. Open weights do not by themselves establish that the training data, source code, development process, or license satisfies a broader definition of open-source AI.",
        "example": "The team chose an open-weight model so it could run the model on infrastructure it controlled and adapt the weights locally.",
        "categories": ["AI Systems & Technical Concepts"],
        "aliases": ["Open-weight AI model", "Open weights model"],
        "status": "Established technical term",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["model-weights", "quantization", "llama", "deepseek-r1"],
    },
    {
        "term": "Responsible AI",
        "slug": "responsible-ai",
        "pronunciation": "ree-SPON-suh-bul A-I",
        "definition": "An approach to designing, developing, deploying, and governing AI with explicit attention to trustworthiness and societal impacts such as fairness, safety, privacy, transparency, accountability, and human oversight.",
        "example": "The organization's responsible AI program requires risk review, documentation, human oversight, and monitoring before high-impact systems are deployed.",
        "categories": ["AI Risks, Safety & Governance", "AI Ways of Working"],
        "aliases": ["Responsible artificial intelligence"],
        "status": "Governance term",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["ai-governance", "ai-alignment", "guardrail", "human-in-the-loop"],
    },
    {
        "term": "Tokenization",
        "slug": "tokenization",
        "pronunciation": "toh-kuh-nuh-ZAY-shun",
        "definition": "The process of converting text or other input into tokens that a model can represent and process, often by splitting text into words, subwords, characters, bytes, or other learned units and mapping them to token IDs.",
        "example": "Different tokenization methods can split the same sentence into different numbers and kinds of tokens.",
        "categories": ["AI Systems & Technical Concepts"],
        "aliases": [],
        "status": "Technical",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["token", "large-language-model", "context-window", "transformer"],
    },
    {
        "term": "Workslop",
        "slug": "workslop",
        "pronunciation": "WURK-slop",
        "definition": "Low-effort AI-generated work that appears polished but lacks the context, substance, or judgment needed to be useful, shifting cleanup or thinking work onto the recipient.",
        "example": "The report looked finished, but it was workslop: the citations were weak, the analysis missed the actual question, and the reviewer had to redo the thinking.",
        "categories": ["AI Culture & Slang", "AI Ways of Working"],
        "aliases": ["AI workslop"],
        "status": "Emerging slang",
        "partOfSpeech": "noun",
        "added": DATE,
        "lastReviewed": DATE,
        "sources": [],
        "related": ["ai-slop", "meat-proxy", "human-in-the-loop", "ai-washing"],
    },
]

EVIDENCE = {
    "artificial-intelligence": [
        ("NIST AI glossary", "https://csrc.nist.gov/glossary/term/artificial_intelligence"),
    ],
    "natural-language-processing": [
        ("IBM: What is NLP?", "https://www.ibm.com/think/topics/natural-language-processing"),
    ],
    "tokenization": [
        ("Hugging Face tokenization pipeline", "https://huggingface.co/docs/tokenizers/main/pipeline"),
        ("Hugging Face tokenization algorithms", "https://huggingface.co/docs/transformers/main/tokenizer_summary"),
    ],
    "ground-truth": [
        ("Google Machine Learning Glossary", "https://developers.google.com/machine-learning/glossary"),
        ("IBM: Ground truth", "https://www.ibm.com/think/topics/ground-truth"),
    ],
    "hybrid-search": [
        ("Elastic hybrid search documentation", "https://www.elastic.co/docs/solutions/search/hybrid-search"),
        ("Microsoft Azure AI Search hybrid search overview", "https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview"),
    ],
    "open-weight-model": [
        ("OpenAI open-weight models overview", "https://help.openai.com/en/articles/11870455-openai-open-weight-models"),
        ("OpenAI gpt-oss model card", "https://openai.com/index/gpt-oss-model-card/"),
    ],
    "responsible-ai": [
        ("NIST trustworthy and responsible AI glossary", "https://www.nist.gov/publications/language-trustworthy-ai-depth-glossary-terms"),
        ("Microsoft Responsible AI", "https://www.microsoft.com/en/ai/responsible-ai"),
    ],
    "workslop": [
        ("BetterUp Labs / Stanford Social Media Lab workslop research", "https://www.betterup.com/workslop"),
        ("Harvard Business Review, Why People Create AI Workslop", "https://hbr.org/2026/01/why-people-create-ai-workslop-and-how-to-stop-it"),
    ],
}

PUBLISH_NEXT = [
    "AI Literacy", "Indirect Prompt Injection", "Data Poisoning", "Model Card", "System Card",
    "Agentic Workflow", "Agent Loop", "AI Companion", "Human-AI Collaboration", "Sampling",
    "Top-p", "Speech-to-Text", "Text-to-Speech", "Text-to-Video", "Loss Function",
    "Gradient Descent", "Backpropagation", "Overfitting", "Underfitting", "Unsupervised Learning",
    "Latent Space", "AI Assurance", "Subagent", "Autonomous Agent", "AI Fluency",
]

ALIASES = {
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

OBSERVE = [
    "AI Boom", "AI Bubble", "AI Gold Rush", "AI Race", "AI Hype", "AI Hype Cycle",
    "AI Arms Race", "AI Delusion", "AI Psychosis", "AI Girlfriend/Boyfriend", "AI Friend",
    "AI Therapist", "AI Employee", "Synthetic Employee", "AI Clone", "AI Twin", "Digital Clone",
    "AI-Enabled", "AI-Assisted", "AI-First", "AI Adoption", "AI Transformation", "AI Upskilling",
    "AI Reskilling", "AI Workforce", "AI Exceptionalism", "AI Maximalist", "AI Booster",
    "Decelerationism", "AI Skeptic", "AI Skepticism", "AI Optimism", "AI Anxiety",
    "AI Fatigue", "Model Roulette", "Model Hopping", "Cyborg Workflow", "Vibe Debugging",
]

NEW_CANDIDATES = {
    "Agents, protocols & agentic systems": [
        "Agent Skills", "SKILL.md", "Agentic Commerce", "Agentic Payments", "Agentic Web", "AI Browser",
        "Agent Session", "Agent Trace", "Agent Observability", "Agent Telemetry", "Agent Sandbox",
        "Agent Permission", "Agent Authorization", "Agent Security", "Agent Benchmark", "Tool Permission",
        "Tool Approval", "Tool Result", "Tool Schema", "Tool Discovery", "Tool Search",
        "Programmatic Tool Calling", "Human Approval Gate", "Least-Privilege Agent", "Agentic UI",
    ],
    "MCP ecosystem": [
        "MCP Apps", "MCP Extension", "MCP Elicitation", "MCP Sampling", "MCP Roots",
        "MCP Authorization", "MCP OAuth", "MCP Tasks", "MCP Progress Notification", "MCP Structured Content",
        "MCP Security", "MCP UI Resource",
    ],
    "Local AI, hardware & inference": [
        "Neural Processing Unit (NPU)", "AI PC", "TOPS", "Edge Inference", "Local Inference",
        "Unified Memory", "GPU Offloading", "Model Offloading", "CPU Offloading", "KV Cache Quantization",
        "Inference Engine", "Inference Backend", "Hardware Acceleration", "AI Accelerator Card", "Memory Footprint",
    ],
    "Reasoning & model behavior": [
        "Reasoning Effort", "Inference-Time Scaling", "Test-Time Scaling", "Deliberation", "Hidden Chain of Thought",
        "Reasoning Trace", "Reasoning Summary", "Verifiable Reward", "Sparse MoE", "Expert Routing",
        "Activation Sparsity", "Long-Context Model", "Reasoning Budget", "Compute-Optimal Inference",
    ],
    "Training & adaptation": [
        "QLoRA", "Adapter", "LoRA Adapter", "Full Fine-Tuning", "Continued Pretraining",
        "Domain-Adaptive Pretraining", "Instruction Fine-Tuning", "Synthetic Data Generation", "RLHF Data",
        "Preference Pair", "Rejection Sampling", "Rejection Sampling Fine-Tuning", "Distillation Loss",
        "Reward Hacking", "Specification Gaming", "Process Reward Model", "Outcome Reward Model",
        "Verifier Model", "Critic Model",
    ],
    "Retrieval, RAG & search": [
        "RAG Evaluation", "RAG Pipeline", "RAG Chunking", "Retrieval Quality", "Query Routing",
        "Semantic Router", "Agentic Retrieval", "Multi-Hop Retrieval", "Retrieval Fusion",
        "Reciprocal Rank Fusion (RRF)", "ColBERT", "Late Interaction", "Retrieval Grounding",
        "Citation Retrieval", "Contextual Reranking",
    ],
    "Evaluation & observability": [
        "Evals Framework", "Benchmark Gaming", "Benchmark Leakage", "Capability Benchmark", "Safety Benchmark",
        "Multimodal Benchmark", "Long-Context Evaluation", "Needle-in-a-Haystack Evaluation",
        "Human Preference Evaluation", "Evaluation Harness", "Evaluation Trace", "Agent Evaluation Trace",
        "LLM Observability", "Prompt Observability", "Model Telemetry",
    ],
    "Safety, security & governance": [
        "Safety Case", "AI Safety Case", "Frontier Safety Framework", "Responsible Scaling Policy",
        "Capability Threshold", "Deployment Threshold", "Model Behavior Specification", "Model Spec",
        "Constitutional Classifier", "Safeguard Model", "AI Red Team", "AI Security Testing",
        "Prompt Injection Defense", "Tool Injection", "Kill Switch (AI)", "AI Incident Response",
        "Deployment Safeguard", "Capability Gate", "Model Safeguard", "Agent Risk Assessment",
    ],
    "Generative media & provenance": [
        "Video Diffusion Model", "Diffusion Transformer (DiT)", "Flow Matching", "Rectified Flow",
        "Image-to-Video Model", "Text-to-Audio Model", "Voice Conversion", "Speaker Cloning",
        "Digital Watermark", "Content Authenticity Initiative (CAI)", "Provenance Signal", "Synthetic Media Detection",
    ],
    "Work, roles & operations": [
        "AI Procurement", "AI Readiness", "AI Operating Model", "AI Center of Excellence (AI CoE)",
        "AI Governance Board", "AI Product Manager", "AI Engineer", "Prompt Engineer", "AI Generalist",
        "Agent Manager", "Human-Agent Collaboration", "Agentic Organization", "Agentic Operations",
        "AI Change Management", "AI Adoption Framework",
    ],
    "Economics & compute": [
        "Inference Economics", "AI Capex", "GPU Scarcity", "Compute Governance", "Compute Efficiency",
        "Inference Budget", "Token Budget", "Compute Allocation", "AI Infrastructure Cost", "Cost per Inference",
    ],
}

PUBLISHED_CANDIDATE_LINES = [
    "Artificial Intelligence (AI)", "Ground Truth", "Hybrid Search", "Natural Language Processing (NLP)",
    "Open-Weight Model", "Responsible AI", "Tokenization", "Workslop",
]


def page_html(entry):
    term = escape(entry["term"])
    definition = escape(entry["definition"], quote=True)
    pronunciation = escape(entry["pronunciation"])
    slug = entry["slug"]
    url = f"{PUBLIC_BASE}/terms/{slug}/"
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": entry["term"],
        "description": entry["definition"],
        "url": url,
        "inDefinedTermSet": f"{PUBLIC_BASE}/",
        "inLanguage": "en",
    }, ensure_ascii=False, separators=(",", ":"))
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{term} | EpochLex</title>
  <meta name="description" content="{definition}">
  <link rel="canonical" href="{url}">
  <meta property="og:site_name" content="EpochLex">
  <meta property="og:title" content="{term} | EpochLex">
  <meta property="og:description" content="{definition}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{term} | EpochLex">
  <meta name="twitter:description" content="{definition}">
  <script type="application/ld+json">{schema}</script>
  <script>
    (() => {{
      try {{
        const saved = localStorage.getItem("ai-era-theme");
        const systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        document.documentElement.dataset.theme = saved || (systemDark ? "dark" : "light");
      }} catch (_) {{ document.documentElement.dataset.theme = "light"; }}
    }})();
  </script>
  <link rel="stylesheet" href="../../assets/css/styles.css">
  <link rel="stylesheet" href="../../assets/css/term-pages.css">
  <link rel="stylesheet" href="../../assets/css/brand-theme.css">
</head>
<body>
  <header class="site-header">
    <div class="shell header-inner">
      <a class="brand" href="../../" aria-label="EpochLex home"><span class="brand-lockup" aria-hidden="true"><img class="brand-lockup-image brand-lockup-light" src="../../assets/brand/epochlex/epochlex-logo-horizontal-light.png" alt=""><img class="brand-lockup-image brand-lockup-dark" src="../../assets/brand/epochlex/epochlex-logo-horizontal-dark.png" alt=""></span><span class="sr-only">EpochLex</span></a>
      <nav class="primary-nav" aria-label="Primary navigation">
        <a class="active" href="../../">Browse</a><a href="../../categories.html">Categories</a><a href="../../about.html">About</a><a href="../../contribute.html">Contribute</a><a href="../../methodology.html">Methodology</a>
      </nav>
      <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Switch color theme" title="Switch color theme"><span class="sun" aria-hidden="true">☼</span><span class="toggle-track"><span class="toggle-knob"></span></span><span class="moon" aria-hidden="true">☾</span></button>
    </div>
  </header>

  <main id="term-page" class="term-page shell" data-term-slug="{slug}">
    <div id="term-fallback" class="term-fallback">
      <nav class="term-breadcrumb" aria-label="Breadcrumb"><a href="../../">Browse</a><span aria-hidden="true">/</span><span>{term}</span></nav>
      <p class="eyebrow">EpochLex entry</p>
      <h1>{term}</h1>
      <p class="fallback-pronunciation">{pronunciation}</p>
      <p class="fallback-definition">{escape(entry['definition'])}</p>
    </div>
  </main>

  <footer class="site-footer"><div class="shell footer-inner"><span class="footer-mark" aria-hidden="true">◎</span><p><strong>EpochLex · Dictionary of the AI Era</strong><br>Vibe coded · Human-directed · AI-assisted · Human-reviewed</p><p class="footer-license">Code: MIT · Content: CC BY 4.0</p></div></footer>
  <script src="../../assets/js/app.js"></script>
  <script src="../../assets/js/term-page.js"></script>
</body>
</html>
'''


def update_terms():
    path = ROOT / "data/terms.json"
    terms = json.loads(path.read_text(encoding="utf-8"))
    existing = {t["slug"] for t in terms}
    for raw in BATCH:
        entry = {k: v for k, v in raw.items() if k != "related"}
        if entry["slug"] not in existing:
            terms.append(entry)
    terms.sort(key=lambda item: item["term"].casefold())
    path.write_text(json.dumps(terms, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def update_provenance():
    path = ROOT / "data/provenance.json"
    provenance = json.loads(path.read_text(encoding="utf-8"))
    for entry in BATCH:
        provenance.setdefault(entry["slug"], {
            "researchStatus": "pending",
            "origin": None,
            "firstKnownUse": None,
            "history": [],
            "relatedTerms": entry["related"],
            "sources": [],
        })
    ordered = {key: provenance[key] for key in sorted(provenance)}
    path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_pages():
    for entry in BATCH:
        directory = ROOT / "terms" / entry["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(page_html(entry), encoding="utf-8")


def update_sitemap():
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    closing = "</urlset>"
    additions = []
    for entry in BATCH:
        url = f"{PUBLIC_BASE}/terms/{entry['slug']}/"
        if url not in text:
            additions.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{DATE}</lastmod>\n  </url>\n")
    if additions:
        text = text.replace(closing, "".join(additions) + closing)
        path.write_text(text, encoding="utf-8")


def update_candidate_inventory():
    path = ROOT / "docs/CORPUS-CANDIDATES.md"
    text = path.read_text(encoding="utf-8")
    for name in PUBLISHED_CANDIDATE_LINES:
        pattern = re.compile(rf"^- (?:\[[^\]]*{re.escape(name)}[^\]]*\]\([^\n]*\)|{re.escape(name)})\s*$", re.MULTILINE | re.IGNORECASE)
        text = pattern.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Add a dated expansion section only once.
    marker = "## September 2026 audit expansion"
    if marker not in text:
        lines = [
            "\n---\n",
            marker,
            "",
            "The September 8, 2026 corpus audit added the following candidates after checking for gaps in agent standards, MCP evolution, local AI hardware, reasoning, retrieval, evaluation, safety/governance, generative media, work, and AI economics. These remain candidates, not approved entries. Their initial disposition is **Research Further** unless promoted by the audit document.",
            "",
        ]
        for heading, items in NEW_CANDIDATES.items():
            lines += [f"### {heading}", ""] + [f"- {item}" for item in items] + [""]
        text += "\n".join(lines)

    # Recalculate inventory count by bullet lines after the inventory header and before Related documentation.
    before_related = text.split("## Related documentation", 1)[0]
    candidates = []
    for line in before_related.splitlines():
        if line.startswith("- ") and not line.startswith("- **"):
            # Exclude workflow bullets before the candidate sections.
            if any(line.startswith(prefix) for prefix in ["- **This file**", "- **GitHub", "- **Issue", "- **Individual", "- **The GitHub", "- **`data/"]):
                continue
            candidates.append(line)
    count = len(candidates)
    text = re.sub(r"\*\*Current unpublished inventory: [^*]+\*\*", f"**Current unpublished inventory: {count} candidates**", text, count=1)
    path.write_text(text, encoding="utf-8")


def audit_document():
    path = ROOT / "docs/CORPUS-AUDIT-2026-09.md"
    lines = [
        "# EpochLex Corpus Audit — September 2026",
        "",
        "This audit applies the editorial model established on September 8, 2026: a dictionary entry may be publishable before its dedicated provenance review is complete. The four labels below are **planning dispositions for this audit**, not new permanent editorial lifecycle states.",
        "",
        "## Audit rules",
        "",
        "- **Publish** — documented usage and distinct reader value are strong enough to draft a human-reviewed core dictionary entry now; provenance may remain `pending`.",
        "- **Alias** — the phrase is useful for discovery but does not currently add enough distinct reader value for a separate page.",
        "- **Research Further** — plausible candidate, but boundaries, durability, evidence, or relationship to existing entries still need work.",
        "- **Exclude or Observe** — too generic, too overlapping, too volatile, or insufficiently useful as a separate entry today; retain only when future usage may change the decision.",
        "",
        "Any candidate in `CORPUS-CANDIDATES.md` that is not explicitly listed as Publish, Alias, or Exclude/Observe below is classified **Research Further** by default. That makes the full inventory classified without pretending that hundreds of unresolved candidates have received a deeper research pass.",
        "",
        "## Publish — Batch A (published in this change)",
        "",
    ]
    for e in BATCH:
        lines.append(f"### {e['term']}")
        lines.append("")
        lines.append(f"**Why publish:** {e['definition']}")
        lines.append("")
        lines.append("**Usage evidence:**")
        for title, url in EVIDENCE[e["slug"]]:
            lines.append(f"- [{title}]({url})")
        lines.append("")
        lines.append("**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.")
        lines.append("")

    lines += [
        "## Publish — next qualified group",
        "",
        "These candidates have strong reader value and should move next into definition drafting and meaning-evidence review under the new publication model:",
        "",
    ] + [f"- {item}" for item in PUBLISH_NEXT] + [
        "",
        "## Alias",
        "",
        "These should currently improve discovery through an existing entry rather than create a duplicate page:",
        "",
    ] + [f"- **{candidate}** → **{target}**" for candidate, target in ALIASES.items()] + [
        "",
        "## Exclude or Observe",
        "",
        "These are not recommended as separate entries now. Some are generic business phrases; others are unstable culture labels, narrow subtypes, or phrases whose reader value is not yet distinct enough. Observation does not mean permanent rejection.",
        "",
    ] + [f"- {item}" for item in OBSERVE] + [
        "",
        "## Research Further",
        "",
        "All remaining unpublished candidates in `CORPUS-CANDIDATES.md`, including the newly added September 2026 expansion pool, are classified **Research Further** unless later promoted. This is intentionally conservative: candidate status records possible reader value, while publication requires actual evidence and human editorial judgment.",
        "",
        "### Highest-priority research clusters",
        "",
        "1. **Agent and agentic systems:** AI Memory, Browser Use, Subagent, Agent Skills, Agentic Commerce, Agent Observability, agent permissions/authorization, and MCP-era interaction concepts.",
        "2. **Safety and governance:** AI Literacy, Indirect Prompt Injection, Data Poisoning, AI Assurance, Frontier Model, High-Risk AI, AI safety cases, and deployment safeguards.",
        "3. **Evaluation:** Model Card, System Card, faithfulness/groundedness, calibration, benchmark contamination, agent evaluation, and long-context evaluation.",
        "4. **Local/open deployment:** Local AI, open-source/open-model distinctions, NPUs, AI PCs, edge inference, model runtimes, and quantized deployment.",
        "5. **Reasoning and post-training:** reasoning effort, inference-time scaling, verifiable rewards, DPO/GRPO/RLVR-adjacent terminology, and reward/specification failure modes.",
        "6. **Retrieval:** hybrid and agentic retrieval, query routing, rerankers, retrieval fusion, RRF, and RAG evaluation.",
        "",
        "## Expansion result",
        "",
        f"This audit publishes {len(BATCH)} candidates immediately and adds {sum(len(v) for v in NEW_CANDIDATES.values())} new research candidates. The candidate inventory is intentionally broader than the publication queue; the goal is useful coverage without treating every AI-adjacent phrase as a dictionary entry.",
        "",
        "## Follow-up",
        "",
        "- Close or update candidate issues whose outcome is now established (for example, Function Calling → Tool Calling alias).",
        "- Promote the next Publish group in coherent batches while leaving provenance `pending` where the core definition is ready but historical research is not.",
        "- Keep Alias mappings discoverable in canonical term records when they are adopted.",
        "- Revisit Exclude/Observe terms only when new evidence shows durable, distinct usage.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_roadmap():
    path = ROOT / "docs/ROADMAP.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("- 122 published dictionary entries;", "- 130 published dictionary entries;")
    text = text.replace("- researched provenance records for the current published corpus;", "- 122 researched provenance records and 8 pending provenance records in the current published corpus;")
    if "September 2026 corpus audit" not in text:
        needle = "## Corpus growth\n"
        insert = "## September 2026 corpus audit\n\nThe September 2026 audit classified the candidate inventory into Publish, Alias, Research Further, and Exclude/Observe planning dispositions, expanded the research pool, and published the first eight entries under the separate publication/provenance model. See [`CORPUS-AUDIT-2026-09.md`](CORPUS-AUDIT-2026-09.md).\n\n"
        text = text.replace(needle, insert + needle)
    path.write_text(text, encoding="utf-8")


def validate():
    terms = json.loads((ROOT / "data/terms.json").read_text(encoding="utf-8"))
    provenance = json.loads((ROOT / "data/provenance.json").read_text(encoding="utf-8"))
    term_slugs = {t["slug"] for t in terms}
    prov_slugs = set(provenance)
    if term_slugs != prov_slugs:
        missing_p = sorted(term_slugs - prov_slugs)
        missing_t = sorted(prov_slugs - term_slugs)
        raise SystemExit(f"term/provenance parity failed: missing provenance={missing_p}, missing terms={missing_t}")
    for entry in BATCH:
        if provenance[entry["slug"]]["researchStatus"] != "pending":
            raise SystemExit(f"expected pending provenance: {entry['slug']}")
        if not (ROOT / "terms" / entry["slug"] / "index.html").exists():
            raise SystemExit(f"missing term page: {entry['slug']}")
    print(f"Validated {len(terms)} terms with term/provenance parity.")


def main():
    update_terms()
    update_provenance()
    update_pages()
    update_sitemap()
    update_candidate_inventory()
    audit_document()
    update_roadmap()
    validate()

if __name__ == "__main__":
    main()
