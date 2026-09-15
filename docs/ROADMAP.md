# EpochLex Roadmap

EpochLex is a Living Dictionary. The roadmap is therefore a statement of current priorities and likely directions, not a promise that every listed feature will ship or that priorities cannot change.

## Current product state

The initial product and corpus MVP is substantially complete:

- 365 published dictionary entries;
- 183 researched provenance records and 182 pending provenance records in the current published corpus;
- an editorial model that separates publishable dictionary completeness from provenance-research completion;
- dedicated term pages;
- Browse search, A-Z navigation, filters, list/grid views;
- category collections;
- related-term discovery;
- written and audible pronunciation;
- responsive/mobile behavior;
- an installable Progressive Web App foundation with a manifest, service worker, and offline-aware caching;
- an automated Word of the Day feature on the homepage plus a dedicated daily page and recent-word history;
- deterministic Pacific-Time Word of the Day selection with rolling no-repeat protection and no manually maintained daily schedule;
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

The focus now shifts from accumulating MVP features to improving readiness, useful corpus coverage, contribution quality, publishing integrity, and long-term maintainability.

## Product readiness

### Cross-device and accessibility QA

The repository now includes a repeatable QA baseline in [`QA.md`](QA.md). Remaining readiness work includes deliberate human spot checks across representative devices, browsers, keyboard-only use, screen-reader behavior, themes, reduced motion, pronunciation, PWA installation behavior, Word of the Day, and graceful degradation.

### Mobile web app and install identity

EpochLex now has an installable web-app foundation backed by `manifest.webmanifest`, `assets/js/pwa.js`, and `service-worker.js`. The service worker provides versioned caching for core site assets and offline-aware behavior while the public site remains a static GitHub Pages deployment.

During initial mobile testing, the installed app uses the existing `assets/brand/epochlex/epochlex-logo-stacked-pronunciation-light.png` brand asset as a pragmatic launcher icon rather than treating it as the permanent app-icon design.

Future refinement may include:

- design and validate a dedicated EpochLex app icon that remains legible across Android and other supported launcher treatments;
- create appropriate standard and maskable icon variants and sizes rather than relying on a general-purpose brand asset;
- verify icon safe areas, background treatment, cropping, and launcher masking on representative devices;
- continue validating installation, offline behavior, cache updates, and standalone display across representative browsers and devices;
- keep the app icon consistent with the approved EpochLex identity without changing the underlying logo artwork solely to satisfy launcher behavior.

This is product-polish work, not a new logo or brand-direction decision.

### Word of the Day

Word of the Day is now a current feature rather than a future concept. It is intentionally automated from the canonical dictionary dataset instead of being maintained as a separate editorial schedule.

The current implementation uses the EpochLex day in `America/Los_Angeles`, changes at midnight Pacific Time, makes newly added terms eligible the following day, and uses a deterministic algorithm so all visitors receive the same daily term. It also protects against reuse within the previous 90 daily selections when the eligible corpus is large enough.

The homepage feature, dedicated `/word-of-the-day/` page, recent-word history, pronunciation, term-entry links, and share behavior all derive from the existing static site and require no daily commit or scheduled job.

The reconstructed history is a discovery experience, not an immutable historical publication record. If EpochLex later needs permanent daily-history preservation, that should be treated as a separate persistence decision rather than assumed from the current feature.

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
- a growing set of bounded issues suitable for outside contributors;
- separate publication and provenance-research thresholds, with `pending` and `researched` used to communicate provenance-review state.

The candidate inventory is a planning and research surface, not a publication queue. A candidate's appearance there does not mean it has been approved as a future entry. Research can result in a separate entry, an alias, continued observation, or a decision not to include the candidate. Human editorial review remains responsible for publication decisions.

A term that passes the dictionary publication threshold may be published with `researchStatus: "pending"` while deeper origin and historical sourcing remains unfinished. This does not lower the standard for the core definition or inclusion decision. A term moves to `researched` only after the provenance record receives the initial human-reviewed sourcing pass defined in [`../PROVENANCE.md`](../PROVENANCE.md).

The next operational maturity work is less about creating entry points and more about making contribution quality and review sustainable.

Possible work includes:

- contributor-oriented validation tooling;
- clearer review states for proposed/revised terms beyond the established provenance statuses;
- documented handling of contested terminology and source disagreements;
- contributor recognition and release-note practices;
- periodic review of whether Discussions, Issues, the Project, the candidate inventory, and public contribution guidance still route people clearly.

EpochLex should remain open to contributions beyond code, including term suggestions, source research, corrections, pronunciation guidance, accessibility testing, design feedback, and documentation improvements.

## September 2026 corpus audit

The September 2026 audit classified the candidate inventory into Publish, Alias, Research Further, and Exclude/Observe planning dispositions, expanded the research pool, and published the first eight entries under the separate publication/provenance model. See [`CORPUS-AUDIT-2026-09.md`](CORPUS-AUDIT-2026-09.md).

## Corpus growth

The current published corpus is a foundation, not a target ceiling. Future additions should be driven by documented usage, reader value, and coverage gaps rather than arbitrary term-count milestones.

[`CORPUS-CANDIDATES.md`](CORPUS-CANDIDATES.md) is the source-controlled working inventory of unpublished terminology that may merit future review. It provides a durable place to preserve possible coverage without implying that every candidate belongs in the dictionary. Selected candidates can be promoted into focused research issues when they are ready for contributor work.

The current operating focus is a **provenance-consolidation phase** rather than continued systematic bulk publication. The original working review order for the remaining provenance records is documented in [`PROVENANCE-REVIEW-QUEUE-2026-09.md`](PROVENANCE-REVIEW-QUEUE-2026-09.md). After completing the 61-record Wave 1 milestone, the corpus stands at **183 researched / 182 pending**. The post-Wave-1 reassessment preserves the original 94/88 Wave 2 / Wave 3 queue as a baseline while revising the near-term working order around governance-family consolidation and high-volatility records; see [`POST-WAVE-1-REASSESSMENT-2026-09-08.md`](POST-WAVE-1-REASSESSMENT-2026-09-08.md). These are current prioritization aids, not new permanent editorial standards.

Corpus growth does not require every accepted term to complete its full provenance investigation before it can help readers. Once an entry satisfies the core publication standard in `CONTRIBUTING.md`, it may enter the Living Dictionary with a transparent `pending` provenance status. Deeper sourcing can then continue without representing unresolved origin or history claims as settled fact.

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

## PWA notifications

**Push notifications are a future possibility, not a current feature or committed implementation.**

A possible future use would be an opt-in Word of the Day notification, with other notification types considered only if they provide clear reader value.

True Web Push would materially change the current architecture. Although the browser/PWA can request notification permission and create a push subscription, EpochLex would need a private place to persist those subscriptions and a server-side or scheduled sender with private application credentials to deliver notifications while the app is closed. GitHub Pages alone cannot provide that persistent subscriber storage and sender role.

For that reason, push notifications are intentionally deferred. They should be reconsidered only if the reader value justifies introducing EpochLex's first small backend or equivalent server-side component. A future implementation should preserve the current static site wherever possible and keep any new backend boundary narrowly focused on subscription management and push delivery.

No third-party push-notification platform is currently required or planned.

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
