# EpochLex Architecture

EpochLex is intentionally a **static, data-driven reference site**. The public website is an interface over editorial datasets rather than a separate application with its own database or backend.

## Design goals

The architecture favors:

- simple hosting;
- transparent source-controlled content;
- stable public URLs;
- low operational cost;
- easy local inspection;
- human-reviewable changes through Git pull requests;
- progressive enhancement rather than framework dependence.

GitHub Pages serves the repository directly from `main` at **https://epochlex.justathoughtblog.org/**.

## Canonical data

### `data/terms.json`

The lightweight reader-facing dictionary dataset. It contains the information required for Browse, search, category collections, Word of the Day, and the fallback content on dedicated term pages.

Typical fields include term, slug, pronunciation, part of speech, definition, example, categories, entry type, aliases, status, added date, and last-reviewed date.

EpochLex uses two complementary classification layers. `categories` describes the editorial areas through which a reader may discover an entry, while `entryType` identifies whether the entry is a general `term`, `organization`, `product`, `model-family`, or individual `model`. Existing records without an explicit `entryType` are treated as `term` for backward compatibility; new or materially revised named-entity records should identify their type explicitly. See [`TAXONOMY.md`](TAXONOMY.md).

### `data/provenance.json`

The canonical research dataset. Every published term has a matching provenance record containing some combination of origin context, first-known-use information when defensible, history, related terms, source records, and research status.

A source that supports a definition does not automatically establish origin. The provenance schema exists to keep those claims separate.

### `data/editions.json`

The machine-readable registry for the continuously updated Living Dictionary and planned/released annual editions.

## Public pages

### Browse: `index.html`

The main dictionary interface provides client-side search, A-Z navigation, category filtering, list/grid views, term counts, theme preference, audible pronunciation, and the homepage Word of the Day feature.

### Word of the Day: `word-of-the-day/index.html`

Word of the Day is a current product feature, not a manually maintained editorial schedule. The daily term is derived from `data/terms.json` by `assets/js/word-of-the-day.js`.

The current selection model:

- uses the EpochLex day in `America/Los_Angeles`;
- changes at midnight Pacific Time;
- sorts eligible terms by canonical slug before selection so JSON ordering does not control the result;
- makes terms eligible beginning the day after their `added` date so a same-day corpus merge cannot change that day's selection;
- applies deterministic date-based selection so all visitors receive the same term for the same EpochLex date;
- protects against reuse within the previous 90 Word of the Day dates when the eligible corpus is large enough;
- progressively releases the oldest exclusion only if the eligible pool is too small to maintain the full protection window;
- dynamically reconstructs recent history from the same algorithm rather than storing a separate Word-of-the-Day dataset.

This design keeps Word of the Day compatible with the static architecture. It requires no daily commit, scheduled GitHub Action, server process, or second editorial data source.

The dynamically reconstructed Word of the Day history is a discovery feature, not an immutable historical publication record. If future requirements demand permanent daily-history preservation, that would require an explicit persistence decision.

### Categories: `categories.html`

Builds reader-facing category collections from `data/terms.json`. There is no separate category-content datastore. The current reader-facing taxonomy contains five editorial categories, including **AI Organizations, Products & Models** for named entities that meet EpochLex inclusion standards.

### Dedicated terms: `terms/<slug>/index.html`

Every term has a stable, indexable URL with core fallback content in HTML. JavaScript progressively enriches the page with provenance, history, sources, aliases, research status, entry type where applicable, and related-term discovery.

This hybrid approach preserves useful no-JavaScript/indexing content while avoiding hundreds of independent hand-maintained content sources.

### Reader documentation

- `about.html`: what EpochLex is, how it began, current reader features, pronunciation, Living Dictionary context, PWA availability, and a brief open-source/AI-transparency statement.
- `methodology.html`: reader-friendly explanation of how terms are selected, researched, reviewed, and maintained.
- `contribute.html`: low-friction ways a reader can help, with a path into the repository for deeper contribution workflows.

## Progressive Web App foundation

EpochLex includes an installable Progressive Web App while remaining a static GitHub Pages site.

- `manifest.webmanifest` provides install metadata and uses `display: "standalone"`.
- `assets/js/pwa.js` ensures the manifest, touch icon, mobile-app metadata, service-worker registration, and installed-app shell are available across pages that load the shared scripts.
- standalone mode is detected with the standard `display-mode: standalone` media query plus the iOS `navigator.standalone` fallback.
- the standalone app shell is injected only when the installed PWA is actually running; ordinary desktop and mobile-browser views retain the normal responsive website navigation.
- the installed app uses a compact branded header and a persistent bottom navigation with **Browse**, **Categories**, **Word**, **About**, and **More**.
- **More** exposes lower-frequency destinations such as Contribute and Methodology without expanding the primary bottom navigation.
- `service-worker.js` maintains a versioned core cache and runtime cache.
- the main app-navigation destinations, core site assets, the dictionary dataset, and Word of the Day assets are cached for offline-aware behavior.
- navigation and canonical dictionary/provenance data use a network-first strategy so fresh content is preferred when connectivity is available.
- style, script, image, and font requests use stale-while-revalidate behavior.
- navigation can fall back to `offline.html` when the requested page is unavailable from the network and no cached navigation response exists.

The standalone shell is a presentation/navigation layer over the same public pages and canonical datasets; it does not create a second app content model.

The PWA does **not** currently implement push notifications or maintain user subscription data.

## JavaScript responsibilities

### `assets/js/app.js`

Shared Browse behavior, search/filter state, theme controls, view preference, entry-type handling, the Web Speech API pronunciation engine, and loading of the homepage Word of the Day module.

Speech overrides are used where browsers are likely to guess incorrectly, especially for acronyms and the EpochLex brand name.

### `assets/js/word-of-the-day.js`

Calculates the deterministic daily selection from the canonical term dataset, renders the homepage and dedicated Word of the Day experiences, reconstructs recent daily history, reuses the pronunciation engine, and provides native share/copy-link behavior.

### `assets/js/term-page.js`

Loads canonical term and provenance data for dedicated pages and renders the richer entry experience, including named-entity entry types when present.

### `assets/js/categories.js`

Builds category collections dynamically from the canonical term dataset.

### `assets/js/pwa.js`

Loads install metadata, registers the service worker, detects installed/standalone execution, and creates the PWA-only app shell. It also provides a fallback compact header on older/lean term pages that do not already contain the shared site header.

### Mobile behavior

Mobile-browser navigation and Browse refinements remain in focused shared scripts/styles rather than duplicated across pages. The installed PWA is intentionally a different shell over the same content: it removes the browser-style hamburger/desktop navigation and exposes app-style bottom navigation instead.

Responsive browser testing or a mobile viewport in desktop developer tools should therefore continue to show the normal website interface. The app shell is tied to standalone execution, not viewport width alone.

## Related-term discovery

`provenance.relatedTerms` stores canonical relationship targets as slugs. Dedicated pages show direct relationships first and can also surface reciprocal/inbound connections.

The current schema does **not** encode relationship semantics. The UI therefore avoids inventing claims such as “depends on,” “contrasts with,” “developed by,” “owned by,” “powers,” or “is a subtype of” unless the data model is expanded to support them explicitly.

This matters particularly for named organizations, products, and model families: a related-term connection may help discovery without claiming a typed relationship that the data does not encode.

## Pronunciation

Written pronunciation lives with each term in `terms.json`. Audible pronunciation uses the browser Web Speech API when supported.

No autoplay is used. Controls are keyboard accessible and labeled for assistive technology. Explicit speech strings handle acronyms and terms that browser voices commonly misread.

Curated audio files remain an optional future enhancement for cases where browser speech synthesis is not reliable enough.

## Publishing and indexing

The static site includes:

- canonical URLs using `https://epochlex.justathoughtblog.org/` as the public base;
- Open Graph metadata;
- Twitter/X card metadata;
- Schema.org `DefinedTermSet` metadata on the dictionary home;
- Schema.org `DefinedTerm` metadata on dedicated term pages;
- `sitemap.xml`;
- `robots.txt`;
- explicit `noindex` treatment for the 404 page.

The custom domain is the current public canonical base. Canonical URLs, sitemap URLs, social metadata URLs, redirects, and GitHub Pages configuration should remain aligned with it whenever publishing metadata changes.

## Annual editions

The public site remains the mutable Living Dictionary. Annual editions are intended to be immutable Git-tagged snapshots rather than duplicated yearly website trees.

See [`../EDITIONS.md`](../EDITIONS.md) for the release model.

## Why no framework or backend?

At the current scale, a framework, database, server API, or build pipeline would add operational complexity without enough reader benefit to justify it. The static architecture keeps the project portable, inspectable, and inexpensive while still supporting the current product, including the installed PWA shell and Word of the Day.

That choice is not ideological. Architecture should change if future requirements make the current approach materially harder to maintain, validate, search, publish, or contribute to.

True background Web Push is one example of a feature that would cross the current boundary. Reliable push delivery would require persistent storage for browser push subscriptions plus a server-side or scheduled sender holding private application credentials. That possibility is recorded in [`ROADMAP.md`](ROADMAP.md), but it is not part of the current architecture.

## Contribution boundary

The architecture is designed so that changes remain reviewable in source control. A complete published term affects more than one surface: canonical term data, provenance, relationships, dedicated fallback content, pronunciation handling where necessary, indexing metadata, and any discovery features that derive from the canonical dataset.

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for the current contribution and validation expectations.
