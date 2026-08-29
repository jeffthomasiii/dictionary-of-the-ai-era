# AILex

**/A-I-lex/**  
**Dictionary of the AI Era**

AILex is an open-source, living dictionary of the language developing around artificial intelligence. It documents technical concepts, ways of working, emerging slang, cultural language, and terminology related to AI risk, safety, governance, and research.

**Development approach: Vibe coded · Human-directed · AI-assisted · Human-reviewed**

**Public site:** https://jeffthomasiii.github.io/dictionary-of-the-ai-era/

## What AILex is

AILex is built to be used like a modern reference work rather than a static glossary. Readers can search, browse, hear pronunciations, move through categories and related concepts, and inspect the provenance and sources behind individual entries.

The public site currently includes:

- **100 published dictionary entries**;
- **100 researched provenance records** with supporting sources;
- stable dedicated pages for every term;
- plain-English definitions and natural usage examples;
- written and audible pronunciation;
- explicit speech handling for acronyms and ambiguous terms;
- instant client-side search and A-Z browsing;
- category filtering and dedicated category collections;
- list and grid views;
- related-term discovery;
- light and dark themes;
- responsive desktop, tablet, and mobile behavior;
- canonical URLs, social metadata, structured data, sitemap, and robots directives;
- a continuously updated Living Dictionary plus a defined annual-edition model.

The 100-term corpus is an MVP floor, not a ceiling. AILex is intended to continue growing when new terms meet the editorial standard.

## How it started

AILex began with a term seen in a post on X: **Meat Proxy**. The definition was humorous, but the larger idea was more interesting: the AI era was already producing a vocabulary of its own.

The first goal was personal. The project began as an attempt to use ChatGPT to help collect AI-related terms and plain-English definitions for reference. A static Word document or long list quickly felt like the wrong form for something meant to grow and be explored, so the idea evolved into a searchable dictionary.

Then the question expanded from **“What does this term mean?”** to **“Where did this term come from?”** That curiosity led to the provenance model, source research, history, careful first-known-use claims, and the editorial methodology behind AILex.

The project was originally named **Dictionary of the AI Era**. As the identity developed, **AILex** became the primary product name and *Dictionary of the AI Era* became its descriptor.

The dictionary came first. The vibe-coding experiment came later, with another question:

> **“Wouldn't it be cool if the Dictionary of the AI Era was actually built using AI?”**

That became a second purpose for the project: not only to document AI-era language, but to explore how far a serious public reference project can be built and maintained through transparent, human-directed AI collaboration.

Read the fuller story in [`docs/ORIGIN.md`](docs/ORIGIN.md).

## An open-source AI experiment

AILex is intended to remain open source.

That openness matters to both halves of the project. The dictionary should be inspectable: definitions, sources, methodology, changes, and corrections can be reviewed publicly. The development experiment should be inspectable too: architecture, code, documentation, regressions, fixes, QA, and AI-assisted workflows are visible rather than hidden behind the finished site.

AI may assist with brainstorming, research support, source discovery, architecture, coding, debugging, documentation, definition drafting, consistency review, QA, and implementation. Human judgment remains responsible for project direction, editorial inclusion, source evaluation, testing, revision, merge decisions, and what ultimately gets published.

AI output is never treated as evidence merely because a model produced it.

See [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md) for the development and editorial principles behind the experiment.

## Brand

**AILex** combines **AI** with **lexicon**. It is pronounced **/A-I-lex/**, saying the letters A and I followed by “lex.”

**Dictionary of the AI Era** is the project descriptor rather than the primary brand name.

See [`BRAND.md`](BRAND.md) for naming and identity guidance.

## Documentation

The website and repository serve different documentation audiences.

**The website explains AILex to readers. The repository explains AILex to builders, contributors, maintainers, researchers, and people interested in the experiment behind it.**

Start with [`docs/README.md`](docs/README.md) for the complete documentation map.

Key documents include:

| Document | Purpose |
| --- | --- |
| [`docs/ORIGIN.md`](docs/ORIGIN.md) | How the Meat Proxy post, personal catalog, provenance curiosity, and AI-building experiment became AILex |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Static-site architecture, datasets, term pages, pronunciation, discovery, and publishing |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Current readiness priorities and longer-term direction |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to contribute terms, research, corrections, code, design, testing, or documentation |
| [`PROVENANCE.md`](PROVENANCE.md) | Detailed sourcing, origin, attribution, and first-known-use standards |
| [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md) | How and why AI is used in the project |
| [`DESIGN.md`](DESIGN.md) | Visual system, interaction principles, responsive behavior, and UI guardrails |
| [`EDITIONS.md`](EDITIONS.md) | Living Dictionary versus immutable annual editions |
| [`BRAND.md`](BRAND.md) | Naming, pronunciation, descriptor, and identity guidance |

## Architecture at a glance

AILex is intentionally static and data-driven.

- `data/terms.json` is the lightweight reader-facing dictionary dataset.
- `data/provenance.json` is the canonical research and sourcing dataset.
- `data/editions.json` records Living Dictionary and annual-edition metadata.
- `terms/<slug>/index.html` provides stable, indexable fallback content for each entry.
- shared JavaScript progressively adds search, category discovery, pronunciation, provenance, history, sources, and related-term navigation.
- GitHub Pages serves the repository directly from `main`.

There is no database, framework, backend, server API, or required build process for the public site.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the full architecture guide.

## Editorial model

AILex is intended to be a dictionary, not a list of AI buzzwords. A candidate term should represent language with documented real-world usage and add enough reader value to justify its own entry.

Every published entry has a matching researched provenance record. A source that explains what a term means does not automatically prove who coined it or when it first appeared. AILex intentionally distinguishes meaning, origin, first known use, history, broader adoption, and current usage.

AI may assist with discovery and research organization, but publication remains human reviewed.

See [`PROVENANCE.md`](PROVENANCE.md) and the public [Methodology](https://jeffthomasiii.github.io/dictionary-of-the-ai-era/methodology.html).

## Categories

AILex currently uses four reader-facing categories:

1. AI Culture & Slang
2. AI Ways of Working
3. AI Systems & Technical Concepts
4. AI Risks, Safety & Governance

Terms may belong to more than one category when that better reflects actual usage.

## Living Dictionary and annual editions

The public site and `main` branch are the **AILex Living Dictionary** and remain continuously updateable.

Named annual editions, such as the planned **AILex 2026**, are immutable snapshots created at a declared editorial cutoff for historical reference, citation, and comparison. They use Git tags and GitHub Releases rather than duplicate yearly website folders.

See [`EDITIONS.md`](EDITIONS.md) and [`data/editions.json`](data/editions.json).

## Contributing

Contributions do not have to involve code.

AILex can benefit from people who contribute:

- new term suggestions;
- stronger definitions or examples;
- primary or secondary sources;
- provenance corrections;
- pronunciation guidance;
- accessibility and cross-device testing;
- UI or design improvements;
- code and automation;
- documentation and editing;
- bug reports and quality review.

The public site provides a low-friction [Contribute](https://jeffthomasiii.github.io/dictionary-of-the-ai-era/contribute.html) entry point. Contributors who want to work directly with the repository should use [`CONTRIBUTING.md`](CONTRIBUTING.md).

AI-assisted contributions are welcome when disclosed appropriately, but contributors remain responsible for verifying factual claims and sources.

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
│   └── <slug>/index.html
├── assets/
│   ├── css/
│   └── js/
├── docs/
│   ├── README.md
│   ├── ORIGIN.md
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
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

## Running locally

Because the site loads JSON data with `fetch`, serve the repository through a local web server rather than opening `index.html` directly.

With Python:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Publishing

GitHub Pages deploys directly from `main` at the repository root. No build step is required.

The site has canonical URLs, structured metadata, `sitemap.xml`, `robots.txt`, and noindex handling for the 404 page. A future custom-domain migration should update canonical URLs, sitemap URLs, social metadata URLs, and redirects together.

## Roadmap

The major MVP capabilities are implemented. Current work is focused on product quality and sustainable growth rather than feature count, including cross-device/accessibility QA, public identity and domain decisions, contribution/review workflows, publishing verification, and continued editorial corpus growth.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the current roadmap.

## Licensing

This repository uses a dual-license model.

- **Software and website code:** MIT License
- **Original dictionary and editorial content:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Third-party material:** remains subject to its original copyright, license, trademark, or other applicable terms

See [`LICENSE`](LICENSE) and [`CONTENT-LICENSE.md`](CONTENT-LICENSE.md).
