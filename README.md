# AILex

**/A-I-lex/**  
**Dictionary of the AI Era**

AILex is a living, searchable dictionary of the language emerging around artificial intelligence.

**Development approach: Vibe coded · Human-directed · AI-assisted · Human-reviewed**

AILex catalogs technical concepts, new ways of working, emerging slang, and terminology related to AI risk, safety, and governance.

## Brand

**AILex** combines **AI** with **lexicon**. It is pronounced **/A-I-lex/**, saying the letters A and I followed by “lex.”

**Dictionary of the AI Era** is the project descriptor/tagline rather than the primary brand name.

See [`BRAND.md`](BRAND.md) for naming usage and the future repository/domain strategy.

## AI transparency

This project is intentionally and substantially developed through an AI-assisted, vibe-coding workflow. AI is not only something AILex documents; it is part of how AILex itself is built.

Jeff Thomas III provides the project direction, requirements, editorial judgment, testing, review, and final decisions. AI tools assist with research support, architecture, coding, debugging, documentation, definition drafting, copy editing, and implementation.

Vibe coding here does not mean blindly accepting AI output. It means a human-directed development workflow in which AI generates or modifies significant portions of the implementation while the human project owner evaluates, tests, redirects, accepts, or rejects the results.

See [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md) for the full development and editorial transparency policy.

## Current MVP

- Plain-English dictionary entries
- Pronunciation for every term
- Definition + natural usage example
- Instant client-side search
- Category filters
- A–Z browsing
- List and grid views
- Light and dark modes
- Shareable term anchors
- Dedicated About, Categories, Contribute, and Methodology pages
- Structured JSON dictionary data
- Separate provenance and source-research data
- GitHub Pages-ready static site
- No database, framework, build step, or API required

## Repository structure

```text
dictionary-of-the-ai-era/
├── index.html
├── about.html
├── categories.html
├── contribute.html
├── methodology.html
├── 404.html
├── data/
│   ├── terms.json
│   └── provenance.json
├── assets/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
├── AI-TRANSPARENCY.md
├── BRAND.md
├── CONTENT-LICENSE.md
├── CONTRIBUTING.md
├── DESIGN.md
├── PROVENANCE.md
├── LICENSE
└── README.md
```

## Dictionary data model

`data/terms.json` remains the lightweight source of truth for what appears in the browse interface.

```json
{
  "term": "Vibe Coding",
  "slug": "vibe-coding",
  "pronunciation": "vybe KOH-ding",
  "partOfSpeech": "noun",
  "definition": "A plain-English definition.",
  "example": "A natural example sentence.",
  "categories": ["AI Culture & Slang", "AI Ways of Working"],
  "aliases": [],
  "status": "Established emerging term",
  "added": "2026-08-28",
  "lastReviewed": "2026-08-28",
  "sources": []
}
```

The existing `sources` array in this core dataset is retained for compatibility during the research transition. The canonical provenance and source model now lives in `data/provenance.json`.

## Provenance data model

Each term slug can have a separate research record:

```json
{
  "vibe-coding": {
    "researchStatus": "researched",
    "origin": "A carefully sourced origin statement.",
    "firstKnownUse": {
      "date": "2025-02-02",
      "precision": "day",
      "note": "Why this date is defensible."
    },
    "history": [
      {
        "date": "2025-02-02",
        "event": "A material event in the term's history."
      }
    ],
    "relatedTerms": ["prompt-engineering", "ai-agent"],
    "sources": [
      {
        "id": "source-id",
        "type": "primary",
        "publisher": "Publisher",
        "title": "Source title",
        "published": "2025-02-02",
        "url": "https://example.com",
        "supports": ["origin", "definition", "history"]
      }
    ]
  }
}
```

See [`PROVENANCE.md`](PROVENANCE.md) for the sourcing standard, research statuses, source types, origin-language rules, first-known-use policy, and human-review requirements.

## Provenance research phase

The provenance system is being introduced as a vertical slice before researching every term. The first researched set intentionally covers different kinds of AI-era vocabulary:

- Few-Shot
- MCP
- Model Collapse
- Prompt Injection
- RAG
- Vibe Coding

Every other published term already has a provenance record marked `pending`, making the remaining research backlog explicit rather than leaving empty fields ambiguous.

## Editorial principle

AILex is intended to be a dictionary, not a list of AI buzzwords. Terms should have documented real-world usage and definitions should distinguish between established technical vocabulary, emerging terminology, slang, research language, and contested concepts.

AI can assist with identifying and researching candidate terms, drafting definitions, organizing evidence, and maintaining the software. Inclusion, source evaluation, final wording, classification, provenance claims, and publication remain human-reviewed decisions.

A source that supports a definition does not automatically establish a term's origin. AILex intentionally distinguishes meaning, origin, first known use, history, and broader adoption.

## Categories

1. AI Culture & Slang
2. AI Ways of Working
3. AI Systems & Technical Concepts
4. AI Risks, Safety & Governance

## Running locally

Because the app loads JSON data with `fetch`, serve the folder over a local web server instead of double-clicking `index.html`.

With Python:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## GitHub Pages

The project is intentionally static.

1. Open **Settings → Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose `main` and `/ (root)`.
4. Save.

No build process is required.

## Next milestones

- Complete provenance research across the remaining published terms
- Surface source and research information through dedicated term detail pages
- Audible pronunciation controls for dictionary terms
  - Speaker control beside the written pronunciation
  - Browser-based speech synthesis as the initial implementation
  - Optional curated audio for unusual, ambiguous, or poorly synthesized terms
  - Keyboard and screen-reader accessible playback controls
- Expand related-term relationships
- Emerging-term lifecycle
- AI-language timeline
- Submission workflow
- Editorial review status
- Automated candidate-term discovery with human approval
- Repository and domain transition from the working `dictionary-of-the-ai-era` identity to AILex once naming, redirects, and link preservation are planned

## Licensing

This repository uses a **dual-license model**.

- **Software and website code:** MIT License
- **Original dictionary and editorial content:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Third-party material:** remains subject to its original copyright, license, trademark, or other applicable terms

See [`LICENSE`](LICENSE) for the MIT software license and scope statement, and [`CONTENT-LICENSE.md`](CONTENT-LICENSE.md) for the dictionary content license and attribution guidance.
