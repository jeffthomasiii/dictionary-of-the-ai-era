# AILex

**/A-I-lex/**  
**Dictionary of the AI Era**

AILex is a living, searchable dictionary of the language developing around artificial intelligence. It documents technical concepts, ways of working, emerging slang, and terminology related to AI risk, safety, governance, and culture.

**Development approach: Vibe coded · Human-directed · AI-assisted · Human-reviewed**

Public site: https://jeffthomasiii.github.io/dictionary-of-the-ai-era/

## Current state

AILex currently includes:

- **100 published dictionary entries**
- **100 researched provenance records** with supporting sources
- Dedicated, stable term pages at `/terms/<slug>/`
- Plain-English definitions and natural usage examples
- Written and audible pronunciation
- Explicit pronunciation handling for acronyms and ambiguous terms
- Instant client-side search
- A-Z browsing
- Category filtering and dedicated category collections
- List and grid views
- Related-term discovery
- Light and dark modes
- Responsive mobile navigation and mobile Browse behavior
- Canonical URLs, Open Graph metadata, Twitter/X metadata, structured data, sitemap, and robots directives
- A Living Dictionary plus a defined annual-edition model
- No database, framework, backend, API, or build process required for the public site

The **100-term corpus is the MVP floor, not a ceiling**. AILex is intended to keep growing when new terms meet the editorial standard.

## Brand

**AILex** combines **AI** with **lexicon**. It is pronounced **/A-I-lex/**, saying the letters A and I followed by “lex.”

**Dictionary of the AI Era** is the project descriptor rather than the primary brand name.

See [`BRAND.md`](BRAND.md) for naming guidance and the future repository/domain strategy.

## Documentation map

Use these documents according to what you are trying to understand or change:

| Document | Purpose |
| --- | --- |
| [`README.md`](README.md) | Current product overview and repository orientation |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to propose or revise terms, provenance, code, and documentation |
| [`PROVENANCE.md`](PROVENANCE.md) | Research, sourcing, attribution, origin, and first-known-use standards |
| [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md) | How AI is used in development and editorial work |
| [`DESIGN.md`](DESIGN.md) | Visual system, interaction principles, and UI guardrails |
| [`BRAND.md`](BRAND.md) | AILex naming, pronunciation, hierarchy, and identity guidance |
| [`EDITIONS.md`](EDITIONS.md) | Living Dictionary versus annual edition policy |
| [`CONTENT-LICENSE.md`](CONTENT-LICENSE.md) | CC BY 4.0 licensing for original dictionary/editorial content |

The public site also includes reader-facing **About**, **Categories**, **Contribute**, and **Methodology** pages.

## Architecture

AILex is intentionally static and data-driven.

- `data/terms.json` is the lightweight published dictionary dataset used by Browse and category discovery.
- `data/provenance.json` is the canonical research/provenance dataset.
- `data/editions.json` records Living Dictionary and annual-edition metadata.
- `terms/<slug>/index.html` provides stable, indexable fallback content for each term.
- `assets/js/term-page.js` enriches dedicated pages with provenance, history, sources, and related-term discovery.
- `assets/js/app.js` powers Browse, search, view state, theme behavior, and the shared pronunciation engine.
- GitHub Pages serves the repository directly from `main`.

The website is an interface over the editorial datasets, not a separate content store.

## Repository structure

```text
dictionary-of-the-ai-era/
├── index.html
├── about.html
├── categories.html
├── contribute.html
├── methodology.html
├── 404.html
├── robots.txt
├── sitemap.xml
├── data/
│   ├── terms.json
│   ├── provenance.json
│   └── editions.json
├── terms/
│   └── <slug>/
│       └── index.html
├── assets/
│   ├── css/
│   │   ├── styles.css
│   │   ├── term-pages.css
│   │   ├── related-discovery.css
│   │   ├── browse-pronunciation.css
│   │   ├── mobile-nav.css
│   │   ├── mobile-browse.css
│   │   └── category-browser.css
│   └── js/
│       ├── app.js
│       ├── term-page.js
│       ├── mobile-nav.js
│       ├── mobile-browse.js
│       └── categories.js
├── AI-TRANSPARENCY.md
├── BRAND.md
├── CONTENT-LICENSE.md
├── CONTRIBUTING.md
├── DESIGN.md
├── EDITIONS.md
├── PROVENANCE.md
├── LICENSE
└── README.md
```

## Dictionary data model

`data/terms.json` contains the reader-facing entry data.

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

The `sources` array in this lightweight dataset is retained for compatibility. Canonical research sources live in `data/provenance.json`.

## Provenance data model

Every published term has a matching researched record in `data/provenance.json`.

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

See [`PROVENANCE.md`](PROVENANCE.md) for the full sourcing standard.

## Editorial principle

AILex is intended to be a dictionary, not a list of AI buzzwords. A candidate should represent language with documented real-world usage and should add enough reader value to justify its own entry.

Definitions should distinguish established technical vocabulary, emerging terminology, slang, research language, governance language, and contested concepts. AI may assist with candidate discovery, research organization, drafting, coding, and editing, but inclusion, source evaluation, final wording, classification, provenance claims, and publication remain human-reviewed decisions.

A source that supports a definition does not automatically establish a term's origin. AILex intentionally distinguishes meaning, origin, first known use, history, broader adoption, and current usage.

## Categories

1. AI Culture & Slang
2. AI Ways of Working
3. AI Systems & Technical Concepts
4. AI Risks, Safety & Governance

Terms may belong to more than one category when that better reflects actual usage.

## Living Dictionary and annual editions

The public site and `main` branch are the **AILex Living Dictionary** and remain continuously updateable.

Named annual editions, such as the planned **AILex 2026**, are immutable snapshots created at a declared editorial cutoff for historical reference, citation, and comparison. Annual editions use Git tags and GitHub Releases rather than duplicate yearly website folders.

See [`EDITIONS.md`](EDITIONS.md) and [`data/editions.json`](data/editions.json).

## AI transparency

AILex is intentionally and substantially developed through an AI-assisted, vibe-coding workflow.

Jeff Thomas III provides project direction, requirements, editorial judgment, testing, review, and final decisions. AI tools may assist with research support, architecture, coding, debugging, documentation, definition drafting, copy editing, and implementation.

AI output is never treated as evidence merely because a model produced it.

See [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md).

## Running locally

Because the site loads JSON data with `fetch`, serve the repository through a local web server rather than opening `index.html` directly.

With Python:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Publishing

GitHub Pages deploys directly from `main` at the repository root. No build step is required.

The published site currently includes:

- canonical URLs for all public pages
- Schema.org `DefinedTermSet` metadata on home
- Schema.org `DefinedTerm` metadata on all dedicated term pages
- `sitemap.xml`
- `robots.txt`
- explicit `noindex` behavior on the 404 page

A future custom-domain migration should update canonical URLs, sitemap URLs, Open Graph URLs, and redirects as one coordinated change.

## Current readiness work

The major MVP capabilities are implemented. Remaining readiness and post-MVP work should be driven by quality rather than feature count. Current priorities include:

- documentation consistency and ongoing maintenance
- final cross-device and accessibility QA
- public AILex name/domain collision review and custom-domain decision
- a deliberate branded social-preview image
- optional search-console submission and indexing verification
- continued corpus expansion based on editorial value and coverage gaps
- stronger contribution/review workflow as outside participation grows

Potential later features include richer relationship semantics, timelines, curated pronunciation audio where browser synthesis remains unreliable, and automated candidate discovery with human approval.

## Licensing

This repository uses a dual-license model.

- **Software and website code:** MIT License
- **Original dictionary and editorial content:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Third-party material:** remains subject to its original copyright, license, trademark, or other applicable terms

See [`LICENSE`](LICENSE) and [`CONTENT-LICENSE.md`](CONTENT-LICENSE.md).
