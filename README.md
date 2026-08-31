# EpochLex

**/EP-uk-leks/**  
**Dictionary of the AI Era**

EpochLex is an open-source, living dictionary of the language developing around artificial intelligence. It documents technical concepts, ways of working, emerging slang, cultural language, terminology related to AI risk, safety, governance, and research, and selected named organizations, products, and models that provide meaningful AI-era context.

**Development approach: Vibe coded · Human-directed · AI-assisted · Human-reviewed**

**Public site:** https://epochlex.justathoughtblog.org

## What EpochLex is

EpochLex is built to be used like a modern reference work rather than a static glossary. Readers can search, browse, hear pronunciations, move through categories and related concepts, and inspect the provenance and sources behind individual entries.

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

The 100-term corpus is an MVP floor, not a ceiling. EpochLex is intended to continue growing when new terms meet the editorial standard.

## How it started

The project began with a term seen in a post on X: **Meat Proxy**. The definition was humorous, but the larger idea was more interesting: the AI era was already producing a vocabulary of its own.

The first goal was personal. ChatGPT helped assemble an initial list of AI-related terms and plain-English definitions, but a Word document or long static list quickly felt like the wrong form for something meant to grow and be explored. The idea became a searchable dictionary.

Then the question expanded from **“What does this term mean?”** to **“Where did this term come from?”** That curiosity led to the provenance model, source research, history, careful first-known-use claims, and the editorial methodology behind the project.

The project began under the working name **Dictionary of the AI Era**, later adopted **AILex** as its first short-form brand, and became **EpochLex** after a public-identity review found meaningful collisions around the AILex name. The rename happened before a repository rename, allowing the underlying project to continue without breaking its project history.

The dictionary came first. The vibe-coding experiment came later, with another question:

> **“Wouldn't it be cool if the Dictionary of the AI Era was actually built using AI?”**

That became a second purpose for the project: not only to document AI-era language, but to explore how far a serious public reference project can be built and maintained through transparent, human-directed AI collaboration.

Read the fuller story in [`docs/ORIGIN.md`](docs/ORIGIN.md).

## An open-source AI experiment

EpochLex is intended to remain open source.

That openness matters to both halves of the project. The dictionary should be inspectable: definitions, sources, methodology, changes, and corrections can be reviewed publicly. The development experiment should be inspectable too: architecture, code, documentation, regressions, fixes, QA, and AI-assisted workflows are visible rather than hidden behind the finished site.

AI may assist with brainstorming, research support, source discovery, architecture, coding, debugging, documentation, definition drafting, consistency review, QA, and implementation. Human judgment remains responsible for project direction, editorial inclusion, source evaluation, testing, revision, merge decisions, and what ultimately gets published.

AI output is never treated as evidence merely because a model produced it.

See [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md).

## Brand

**EpochLex** combines **epoch** with **lexicon**. It is pronounced **/EP-uk-leks/**, saying “epoch” followed by “lex.”

The name reflects the project's broader purpose: documenting the vocabulary emerging during an AI-shaped era, not merely defining components of AI systems.

**Dictionary of the AI Era** remains the descriptor rather than the primary brand name.

See [`BRAND.md`](BRAND.md) for current naming, historical continuity, and identity guidance.

## Documentation

The website and repository serve different documentation audiences.

**The website explains EpochLex to readers. The repository explains EpochLex to builders, contributors, maintainers, researchers, and people interested in the experiment behind it.**

Start with [`docs/README.md`](docs/README.md) for the complete documentation map.

| Document | Purpose |
| --- | --- |
| [`docs/ORIGIN.md`](docs/ORIGIN.md) | How Meat Proxy, a personal catalog, provenance curiosity, the AILex stage, and the AI-building experiment became EpochLex |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Static-site architecture, datasets, term pages, pronunciation, discovery, and publishing |
| [`docs/TAXONOMY.md`](docs/TAXONOMY.md) | Editorial categories, entry types, named-entity inclusion, and model-version granularity |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Current readiness priorities and longer-term direction |
| [`docs/QA.md`](docs/QA.md) | Product-readiness, accessibility, responsive, and regression QA baseline |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to contribute terms, research, corrections, code, design, testing, or documentation |
| [`PROVENANCE.md`](PROVENANCE.md) | Detailed sourcing, origin, attribution, and first-known-use standards |
| [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md) | How and why AI is used in the project |
| [`DESIGN.md`](DESIGN.md) | Visual system, interaction principles, responsive behavior, and UI guardrails |
| [`EDITIONS.md`](EDITIONS.md) | Living Dictionary versus immutable annual editions |
| [`BRAND.md`](BRAND.md) | Naming, pronunciation, descriptor, brand history, and identity guidance |

## Community and project work

EpochLex uses different GitHub surfaces for different kinds of participation so exploratory conversation and actionable work do not have to compete in the same place.

| If you want to... | Start here |
| --- | --- |
| Discuss terminology, research questions, ideas, or project direction | [GitHub Discussions](https://github.com/jeffthomasiii/dictionary-of-the-ai-era/discussions) |
| Find current priorities and contributor-ready work | [EpochLex Projects](https://github.com/jeffthomasiii/dictionary-of-the-ai-era/projects) |
| Suggest a term, report a bug, propose a feature, submit a research correction, or share accessibility findings | [GitHub Issues](https://github.com/jeffthomasiii/dictionary-of-the-ai-era/issues/new/choose) |
| Prepare a direct code, content, research, design, or documentation contribution | [`CONTRIBUTING.md`](CONTRIBUTING.md) and pull requests |

Discussions are useful when a topic still benefits from conversation. Issues are best for concrete work that can be tracked to completion. The Project provides a view of active priorities and available work, while pull requests remain the review surface for proposed repository changes.

## Architecture at a glance

EpochLex is intentionally static and data-driven.

- `data/terms.json` is the lightweight reader-facing dictionary dataset, including editorial categories and entry type where applicable.
- `data/provenance.json` is the canonical research and sourcing dataset.
- `data/editions.json` records Living Dictionary and annual-edition metadata.
- `terms/<slug>/index.html` provides stable, indexable fallback content for each entry.
- shared JavaScript progressively adds search, category discovery, pronunciation, provenance, history, sources, and related-term navigation.
- GitHub Pages serves the repository directly from `main`.

There is no database, framework, backend, server API, or required build process for the public site.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Editorial model

EpochLex is intended to be a dictionary, not a list of AI buzzwords or a vendor catalog. A candidate entry should represent language or a named entity with documented real-world usage and add enough reader value to justify its own entry.

Named AI organizations, products, model families, and individual models may qualify when understanding the name provides meaningful context for understanding AI-era terminology, technology, history, or culture. Inclusion is not automatic merely because an organization develops AI, a product uses AI, or a model has been released.

Every published entry has a matching researched provenance record. A source that explains what an entry means does not automatically prove who coined, introduced, named, or released it or when it first appeared. EpochLex intentionally distinguishes meaning, origin, first known use, history, broader adoption, and current usage.

AI may assist with discovery and research organization, but publication remains human reviewed.

See [`docs/TAXONOMY.md`](docs/TAXONOMY.md), [`PROVENANCE.md`](PROVENANCE.md), and the public [Methodology](https://epochlex.justathoughtblog.org/methodology.html).

## Taxonomy

EpochLex uses five reader-facing editorial categories:

1. AI Culture & Slang
2. AI Ways of Working
3. AI Systems & Technical Concepts
4. AI Risks, Safety & Governance
5. AI Organizations, Products & Models

Entries may belong to more than one category when that better reflects actual usage.

A separate `entryType` dimension identifies what an entry is. The current values are `term`, `organization`, `product`, `model-family`, and `model`. This allows EpochLex to distinguish a generic concept such as **Copilot** from named products such as **Microsoft Copilot** and **GitHub Copilot**, or a product such as **ChatGPT** from the **GPT** model family.

See [`docs/TAXONOMY.md`](docs/TAXONOMY.md).

## Living Dictionary and annual editions

The public site and `main` branch are the **EpochLex Living Dictionary** and remain continuously updateable.

Named annual editions, such as the planned **EpochLex 2026**, are immutable snapshots created at a declared editorial cutoff for historical reference, citation, and comparison. They use `epochlex-YYYY` Git tags and GitHub Releases rather than duplicate yearly website folders.

See [`EDITIONS.md`](EDITIONS.md) and [`data/editions.json`](data/editions.json).

## Contributing

Contributions do not have to involve code. EpochLex can benefit from new term suggestions, stronger definitions or sources, provenance corrections, pronunciation guidance, accessibility and device testing, UI/design work, code, automation, documentation, editing, bug reports, and quality review.

The public site provides a low-friction [Contribute](https://epochlex.justathoughtblog.org/contribute.html) entry point. Contributors can also use [Discussions](https://github.com/jeffthomasiii/dictionary-of-the-ai-era/discussions) for conversation, [Issues](https://github.com/jeffthomasiii/dictionary-of-the-ai-era/issues/new/choose) for structured proposals and reports, and the [EpochLex Project](https://github.com/jeffthomasiii/dictionary-of-the-ai-era/projects) to find current work. Contributors who want to work directly with the repository should use [`CONTRIBUTING.md`](CONTRIBUTING.md).

AI-assisted contributions are welcome when disclosed appropriately, but contributors remain responsible for verifying factual claims and sources.

## Running locally

Because the site loads JSON data with `fetch`, serve the repository through a local web server rather than opening `index.html` directly.

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Publishing and URLs

GitHub Pages deploys directly from `main` at the repository root. No build step is required.

The public site uses the custom domain **https://epochlex.justathoughtblog.org/**. The repository slug remains `dictionary-of-the-ai-era`. Canonical URLs, sitemap URLs, social metadata URLs, redirects, and GitHub Pages configuration should remain aligned with the custom domain whenever publishing metadata changes.

## Roadmap

The major MVP capabilities are implemented. Current work is focused on product quality and sustainable growth rather than feature count, including cross-device QA, contribution/review workflows, publishing verification, continued editorial corpus growth, and long-term maintenance.

See [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Licensing

This repository uses a dual-license model.

- **Software and website code:** MIT License
- **Original dictionary and editorial content:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Third-party material:** remains subject to its original copyright, license, trademark, or other applicable terms

See [`LICENSE`](LICENSE) and [`CONTENT-LICENSE.md`](CONTENT-LICENSE.md).
