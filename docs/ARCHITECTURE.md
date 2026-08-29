# AILex Architecture

AILex is intentionally a **static, data-driven reference site**. The public website is an interface over editorial datasets rather than a separate application with its own database or backend.

## Design goals

The architecture favors:

- simple hosting;
- transparent source-controlled content;
- stable public URLs;
- low operational cost;
- easy local inspection;
- human-reviewable changes through Git pull requests;
- progressive enhancement rather than framework dependence.

GitHub Pages serves the repository directly from `main`.

## Canonical data

### `data/terms.json`

The lightweight reader-facing dictionary dataset. It contains the information required for Browse, search, category collections, and the fallback content on dedicated term pages.

Typical fields include term, slug, pronunciation, part of speech, definition, example, categories, aliases, status, added date, and last-reviewed date.

### `data/provenance.json`

The canonical research dataset. Every published term has a matching researched provenance record containing some combination of origin context, first-known-use information when defensible, history, related terms, source records, and research status.

A source that supports a definition does not automatically establish origin. The provenance schema exists to keep those claims separate.

### `data/editions.json`

The machine-readable registry for the continuously updated Living Dictionary and planned/released annual editions.

## Public pages

### Browse: `index.html`

The main dictionary interface provides client-side search, A-Z navigation, category filtering, list/grid views, term counts, theme preference, and audible pronunciation.

### Categories: `categories.html`

Builds reader-facing category collections from `data/terms.json`. There is no separate category-content datastore.

### Dedicated terms: `terms/<slug>/index.html`

Every term has a stable, indexable URL with core fallback content in HTML. JavaScript progressively enriches the page with provenance, history, sources, aliases, research status, and related-term discovery.

This hybrid approach preserves useful no-JavaScript/indexing content while avoiding 100 independent hand-maintained content sources.

### Reader documentation

- `about.html`: what AILex is, how it began, site features, pronunciation, Living Dictionary context, and a brief open-source/AI-transparency statement.
- `methodology.html`: reader-friendly explanation of how terms are selected, researched, reviewed, and maintained.
- `contribute.html`: low-friction ways a reader can help, with a path into the repository for deeper contribution workflows.

## JavaScript responsibilities

### `assets/js/app.js`

Shared Browse behavior, search/filter state, theme controls, view preference, and the Web Speech API pronunciation engine.

Speech overrides are used where browsers are likely to guess incorrectly, especially for acronyms and the AILex brand name.

### `assets/js/term-page.js`

Loads canonical term and provenance data for dedicated pages and renders the richer entry experience.

### `assets/js/categories.js`

Builds category collections dynamically from the canonical term dataset.

### Mobile behavior

Mobile navigation and Browse refinements are kept in focused shared scripts/styles rather than duplicated across pages.

## Related-term discovery

`provenance.relatedTerms` stores canonical relationship targets as slugs. Dedicated pages show direct relationships first and can also surface reciprocal/inbound connections.

The current schema does **not** encode relationship semantics. The UI therefore avoids inventing claims such as “depends on,” “contrasts with,” or “is a subtype of” unless the data model is expanded to support them explicitly.

## Pronunciation

Written pronunciation lives with each term in `terms.json`. Audible pronunciation uses the browser Web Speech API when supported.

No autoplay is used. Controls are keyboard accessible and labeled for assistive technology. Explicit speech strings handle acronyms and terms that browser voices commonly misread.

Curated audio files remain an optional future enhancement for cases where browser speech synthesis is not reliable enough.

## Publishing and indexing

The static site includes:

- canonical URLs;
- Open Graph metadata;
- Twitter/X card metadata;
- Schema.org `DefinedTermSet` metadata on the dictionary home;
- Schema.org `DefinedTerm` metadata on dedicated term pages;
- `sitemap.xml`;
- `robots.txt`;
- explicit `noindex` treatment for the 404 page.

The current canonical base is the GitHub Pages URL. A future custom-domain migration should update canonical URLs, sitemap URLs, social metadata URLs, and redirects as one coordinated change.

## Annual editions

The public site remains the mutable Living Dictionary. Annual editions are intended to be immutable Git-tagged snapshots rather than duplicated yearly website trees.

See [`../EDITIONS.md`](../EDITIONS.md) for the release model.

## Why no framework or backend?

At the current scale, a framework, database, server API, or build pipeline would add operational complexity without enough reader benefit to justify it. The static architecture keeps the project portable, inspectable, and inexpensive while still supporting the current product.

That choice is not ideological. Architecture should change if future requirements make the current approach materially harder to maintain, validate, search, publish, or contribute to.

## Contribution boundary

The architecture is designed so that changes remain reviewable in source control. A complete published term affects more than one surface: canonical term data, provenance, relationships, dedicated fallback content, pronunciation handling where necessary, and indexing metadata.

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for the current contribution and validation expectations.
