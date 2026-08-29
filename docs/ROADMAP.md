# AILex Roadmap

AILex is a Living Dictionary. The roadmap is therefore a statement of current priorities and likely directions, not a promise that every listed feature will ship or that priorities cannot change.

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
- open-source repository and contribution guidance.

The focus now shifts from accumulating MVP features to improving readiness, identity, contribution quality, and long-term maintainability.

## Product readiness

### Cross-device and accessibility QA

- systematic desktop, tablet, and mobile review;
- keyboard-only navigation checks;
- screen-reader labeling review;
- focus-order and visible-focus checks;
- reduced-motion and theme behavior checks;
- pronunciation controls across representative browsers;
- graceful behavior when JavaScript or speech synthesis is unavailable.

### Public identity

- AILex name/brand collision review;
- domain availability and custom-domain decision;
- migration plan that preserves existing GitHub Pages links;
- branded social-preview image and `og:image` support;
- canonical/sitemap migration when a custom domain is adopted.

### Publishing verification

- optional search-engine console submission;
- sitemap/indexing verification;
- social-card preview testing;
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

AILex should remain open to contributions beyond code, including term suggestions, source research, corrections, pronunciation guidance, accessibility testing, design feedback, and documentation improvements.

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

AILex will continue exploring human-directed AI collaboration as part of the project itself.

Future experimentation may include:

- candidate-term discovery assistance;
- automated consistency and metadata checks;
- source-discovery assistance;
- documentation drift detection;
- QA assistance across the term corpus;
- release preparation and change summaries.

Automation should support, not replace, human editorial and release judgment.

## Annual editions

The Living Dictionary remains continuously updateable. Annual editions provide immutable historical snapshots. The planned inaugural edition is **AILex 2026**, governed by [`../EDITIONS.md`](../EDITIONS.md).

## Guiding question

Roadmap decisions should continue to answer two questions:

1. **Does this make AILex a more useful, credible, understandable dictionary?**
2. **Does this help the open-source, human-directed AI experiment remain transparent and maintainable?**
