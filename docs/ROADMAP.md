# EpochLex Roadmap

EpochLex is a Living Dictionary. The roadmap is therefore a statement of current priorities and likely directions, not a promise that every listed feature will ship or that priorities cannot change.

## Current product state

The initial product and corpus MVP is substantially complete:

- 122 published dictionary entries;
- researched provenance records for the published corpus;
- dedicated term pages;
- Browse search, A-Z navigation, filters, list/grid views;
- category collections;
- related-term discovery;
- written and audible pronunciation;
- responsive/mobile behavior;
- publishing and SEO foundation;
- Living Dictionary and annual-edition model;
- open-source repository and contribution guidance;
- structured issue forms and pull-request guidance;
- GitHub Discussions for community conversation;
- a linked GitHub Project for priorities and contributor-ready work;
- a source-controlled corpus candidate inventory for terminology that may merit future research;
- repeatable accessibility and product-readiness QA baseline;
- EpochLex selected as the public identity after a brand-collision review of the earlier AILex name;
- the custom public domain `epochlex.justathoughtblog.org` configured for GitHub Pages.

The focus now shifts from accumulating MVP features to improving readiness, contribution quality, publishing integrity, and long-term maintainability.

## Product readiness

### Cross-device and accessibility QA

The repository now includes a repeatable QA baseline in [`QA.md`](QA.md). Remaining readiness work includes deliberate human spot checks across representative devices, browsers, keyboard-only use, screen-reader behavior, themes, reduced motion, pronunciation, and graceful degradation.

### Mobile web app and install identity

EpochLex now has a first-launch installable web-app foundation. During initial mobile testing, the installed app uses the existing `assets/brand/epochlex/epochlex-logo-stacked-pronunciation-light.png` brand asset as a pragmatic launcher icon rather than treating it as the permanent app-icon design.

Future refinement should include:

- design and validate a dedicated EpochLex app icon that remains legible across Android and other supported launcher treatments;
- create appropriate standard and maskable icon variants and sizes rather than relying on a general-purpose brand asset;
- verify icon safe areas, background treatment, cropping, and launcher masking on representative devices;
- keep the app icon consistent with the approved EpochLex identity without changing the underlying logo artwork solely to satisfy launcher behavior.

This is product-polish work, not a new logo or brand-direction decision.

### Public identity and URLs

The short-form brand decision is complete: **EpochLex** is the public product name and **Dictionary of the AI Era** remains the descriptor.

The custom public domain **https://epochlex.justathoughtblog.org/** is now configured for GitHub Pages. The repository itself remains `dictionary-of-the-ai-era`.

Remaining identity/infrastructure work may include:

- deciding whether the repository itself should eventually be renamed;
- preserving redirects and GitHub Pages behavior before any repository URL change;
- keeping canonical URLs, sitemap URLs, social metadata URLs, and public documentation aligned with the custom domain;
- creating a deliberate EpochLex social-preview image and adding `og:image` support.

### Publishing verification

- optional search-engine console submission;
- sitemap/indexing verification;
- social-card preview testing after the branded preview asset exists;
- periodic metadata integrity checks as the corpus grows;
- periodic checks that canonical and social URLs continue to use the current public domain.

## Contribution and editorial operations

EpochLex now has a basic contributor-participation system in place:

- a reader-friendly public Contribute page;
- repository-level contribution guidance;
- structured issue forms for term suggestions, research corrections, bugs, feature requests, and accessibility testing;
- a pull-request template;
- GitHub Discussions for terminology conversations, research questions, and ideas that are not yet concrete work items;
- a linked GitHub Project for current priorities and contributor-ready work;
- a source-controlled [`CORPUS-CANDIDATES.md`](CORPUS-CANDIDATES.md) inventory for possible future coverage;
- individual research issues for selected candidates that are sufficiently actionable for focused contributor work;
- a growing set of bounded issues suitable for outside contributors.

The candidate inventory is a planning and research surface, not a publication queue. A candidate's appearance there does not mean it has been approved as a future entry. Research can result in a separate entry, an alias, continued observation, or a decision not to include the candidate. Human editorial review remains responsible for publication decisions.

The next operational maturity work is less about creating entry points and more about making contribution quality and review sustainable.

Possible work includes:

- contributor-oriented validation tooling;
- clearer review states for proposed/revised terms;
- documented handling of contested terminology and source disagreements;
- contributor recognition and release-note practices;
- periodic review of whether Discussions, Issues, the Project, the candidate inventory, and public contribution guidance still route people clearly.

EpochLex should remain open to contributions beyond code, including term suggestions, source research, corrections, pronunciation guidance, accessibility testing, design feedback, and documentation improvements.

## Corpus growth

The current published corpus is a foundation, not a target ceiling. Future additions should be driven by documented usage, reader value, and coverage gaps rather than arbitrary term-count milestones.

[`CORPUS-CANDIDATES.md`](CORPUS-CANDIDATES.md) is the source-controlled working inventory of unpublished terminology that may merit future review. It provides a durable place to preserve possible coverage without implying that every candidate belongs in the dictionary. Selected candidates can be promoted into focused research issues when they are ready for contributor work.

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
