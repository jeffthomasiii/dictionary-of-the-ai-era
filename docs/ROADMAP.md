# EpochLex Roadmap

EpochLex is a Living Dictionary. The roadmap is therefore a statement of current priorities and likely directions, not a promise that every listed feature will ship or that priorities cannot change.

## Current product state

The initial product and corpus MVP is substantially complete:

- 100 published dictionary terms;
- 100 researched provenance records;
- dedicated term pages;
- Browse search, A-Z navigation, filters, list/grid views;
- category collections;
- related-term discovery;
- written and audible pronunciation;
- responsive/mobile behavior;
- publishing and SEO foundation;
- Living Dictionary and annual-edition model;
- open-source repository and contribution guidance;
- repeatable accessibility and product-readiness QA baseline;
- EpochLex selected as the public identity after a brand-collision review of the earlier AILex name.

The focus now shifts from accumulating MVP features to improving readiness, identity infrastructure, contribution quality, and long-term maintainability.

## Product readiness

### Cross-device and accessibility QA

The repository now includes a repeatable QA baseline in [`QA.md`](QA.md). Remaining readiness work includes deliberate human spot checks across representative devices, browsers, keyboard-only use, screen-reader behavior, themes, reduced motion, pronunciation, and graceful degradation.

### Public identity and URL migration

The short-form brand decision is complete: **EpochLex** is the public product name and **Dictionary of the AI Era** remains the descriptor.

The next identity work is infrastructure rather than naming:

- confirm a suitable EpochLex domain or subdomain;
- decide whether the repository itself should eventually be renamed;
- plan redirects and GitHub Pages behavior before changing URLs;
- migrate canonical and sitemap URLs only as one coordinated change;
- create a deliberate EpochLex social-preview image and add `og:image` support after the durable public URL is chosen.

The current `dictionary-of-the-ai-era` repository slug and GitHub Pages URL remain valid during this transition.

### Publishing verification

- optional search-engine console submission;
- sitemap/indexing verification;
- social-card preview testing after the branded preview asset exists;
- periodic metadata integrity checks as the corpus grows.

## Contribution and editorial operations

The next operational maturity step is making outside participation easier without weakening editorial quality.

Possible work includes:

- a clearer term/correction submission path for non-developers;
- issue templates or structured proposal forms;
- contributor-oriented validation tooling;
- clearer review states for proposed/revised terms;
- documented handling of contested terminology and source disagreements;
- contributor recognition and release-note practices.

EpochLex should remain open to contributions beyond code, including term suggestions, source research, corrections, pronunciation guidance, accessibility testing, design feedback, and documentation improvements.

## Corpus growth

The 100-term corpus is a floor, not a target ceiling. Future additions should be driven by documented usage, reader value, and coverage gaps rather than arbitrary term-count milestones.

Ongoing corpus work may include:

- newly emerging AI-era vocabulary;
- missing foundational concepts;
- workplace and cultural language;
- governance and safety terminology;
- evaluation and agent vocabulary;
- terminology whose meaning materially changes over time.

## Editorial evolution

Potential improvements include:

- a more explicit emerging-term lifecycle;
- review reminders for fast-changing entries;
- stronger handling of disputed origin claims;
- clearer status normalization;
- historical corrections/errata practices connected to annual editions;
- richer documentation of meaning changes over time.

## Discovery features

Potential post-MVP reader features include:

- typed relationship semantics, such as broader/narrower/related concepts, when supported by data;
- an AI-language timeline;
- graph-style exploration of term relationships;
- curated collections around themes or historical moments;
- improved ways to compare related or easily confused terms.

These should be implemented only when they improve reference value rather than adding visualization for its own sake.

## Pronunciation

Browser speech synthesis remains the default because it preserves the static architecture. Future pronunciation work may include curated audio for terms that are ambiguous, newly coined, acronym-heavy, or consistently mispronounced by browser engines.

## AI-assisted project development

EpochLex will continue exploring human-directed AI collaboration as part of the project itself.

Future experimentation may include:

- candidate-term discovery assistance;
- automated consistency and metadata checks;
- source-discovery assistance;
- documentation drift detection;
- QA assistance across the term corpus;
- release preparation and change summaries.

Automation should support, not replace, human editorial and release judgment.

## Annual editions

The Living Dictionary remains continuously updateable. Annual editions provide immutable historical snapshots. The planned inaugural edition is **EpochLex 2026**, governed by [`../EDITIONS.md`](../EDITIONS.md).

## Guiding question

Roadmap decisions should continue to answer two questions:

1. **Does this make EpochLex a more useful, credible, understandable dictionary?**
2. **Does this help the open-source, human-directed AI experiment remain transparent and maintainable?**
