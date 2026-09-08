# EpochLex Product Readiness QA

This document records the repeatable quality checks used before broader public release and after changes that affect shared site behavior.

EpochLex is a static, data-driven GitHub Pages site. Automated repository checks can catch many structural regressions, but they do not replace browser, device, keyboard, screen-reader, visual, or editorial testing.

## Automated repository checks

The following should be checked whenever relevant files change:

- `data/terms.json` and `data/provenance.json` parse successfully.
- Published term and provenance slug sets remain equal.
- Every provenance record uses a supported `researchStatus`. Under the current model, supported values are `pending` and `researched`.
- A `pending` provenance record may leave unresearched origin, first-known-use, history, or source fields empty or unresolved; those empty fields must not be treated as structural validation failures.
- The matching core dictionary entry must still satisfy the publication requirements in `CONTRIBUTING.md`; `pending` does not permit an incomplete or unreviewed definition.
- A `researched` provenance record represents an initial human-reviewed sourcing pass under `PROVENANCE.md`. Structural validation can confirm the status value and record shape, but source judgment remains a human editorial check.
- All related-term targets resolve to published entries and do not self-link.
- Every published term has a dedicated `terms/<slug>/index.html` page.
- Shared JavaScript files parse successfully.
- Public pages retain canonical URLs and expected indexing metadata.
- The sitemap includes the intended public page set.
- The 404 page remains excluded from indexing.
- Browse filters and list/grid controls expose selected state programmatically.
- Pronunciation buttons have accessible names and do not autoplay.
- Storage-dependent preferences fail gracefully if browser storage is unavailable.
- Reduced-motion preferences are respected for smooth scrolling and transitions.
- Keyboard focus is visibly indicated on interactive controls.

## Editorial-state checks

Repository structure alone cannot determine whether an entry deserves publication or whether provenance research is sufficient to be called `researched`.

For a newly published entry, confirm that:

1. documented real-world usage supports inclusion;
2. the entry provides distinct reader value rather than duplicating an alias or generic phrase;
3. the definition and example are human reviewed and useful without relying on unfinished provenance work;
4. the matching provenance record explicitly declares either `pending` or `researched`;
5. any provenance claim already populated is no stronger than its evidence supports.

For a transition from `pending` to `researched`, confirm the human-reviewed sourcing checks in `PROVENANCE.md` rather than treating the status change as a purely mechanical edit.

## Keyboard checks

On desktop, test the public site without a mouse:

1. Tab through the brand/home link, navigation, theme control, search, filters, A-Z controls, view controls, term links, and pronunciation buttons.
2. Confirm every focused control has a visible focus indicator.
3. Confirm Enter/Space activates buttons and native navigation controls appropriately.
4. Confirm `Ctrl+K` and `Cmd+K` focus Browse search.
5. Confirm Escape clears and exits focused Browse search.
6. Open the mobile navigation with keyboard input at a narrow viewport and confirm Escape closes it and restores focus to the menu control.

## Screen-reader and semantics checks

Spot-check with at least one common screen reader/browser combination when practical.

Verify:

- primary and mobile navigation are announced as navigation landmarks;
- the Browse result count is announced when filtering changes results;
- category filters communicate pressed/not-pressed state;
- list/grid view controls communicate the active state;
- pronunciation controls announce which term will be spoken;
- decorative SVGs are hidden from assistive technology;
- headings preserve a useful document outline;
- links make sense from their accessible text without relying only on surrounding visual context.

## Responsive/device matrix

Before a broader public launch, spot-check at minimum:

- narrow mobile viewport around 360–390 CSS px;
- larger mobile viewport around 412–430 CSS px;
- tablet portrait around 768 CSS px;
- tablet/compact desktop around 980–1024 CSS px;
- standard desktop around 1280–1440 CSS px.

At each size, check:

- header and navigation;
- Browse hero and search;
- category/filter access;
- A-Z navigation;
- list and grid layouts;
- term-page source/history/related-term layout;
- category collections;
- footer wrapping;
- no clipped controls, horizontal page overflow, or unreachable content.

## Theme checks

Check light and dark modes for:

- readable body and muted text;
- visible borders and focus indicators;
- semantic category accents that remain distinguishable;
- pronunciation controls and active states;
- mobile menu and filter surfaces;
- term-page sources and relationship cards.

The site should remain usable if local storage is unavailable. A saved theme/view preference may not persist in that case, but content and controls should continue to function.

## Reduced motion

With `prefers-reduced-motion: reduce` enabled:

- A-Z jumps should not use smooth scrolling;
- CSS transitions and animations should be effectively suppressed;
- no essential information should depend on motion.

## No-JavaScript / fallback checks

EpochLex uses JavaScript for Browse interaction and rich term-page enrichment, but dedicated term pages include static fallback content for indexing and basic reading.

Periodically verify that a dedicated term URL still contains, before JavaScript enhancement:

- term name;
- pronunciation;
- plain-English definition;
- page title and description;
- canonical URL;
- structured metadata.

A pending provenance state must not make the static fallback unusable as a dictionary entry. The core definition and identifying metadata should remain available even when deeper provenance fields have not been researched.

## Pronunciation checks

Browser speech engines vary by operating system and browser. Spot-check:

- EpochLex;
- acronym-heavy entries such as MCP, RLHF, RLAIF, PEFT, and LLM-as-a-Judge;
- newly coined or ambiguous terms;
- any entry reported by a reader as being mispronounced.

Add explicit shared speech overrides when a browser is likely to interpret an acronym or coined term incorrectly.

## Regression checks after shared UI changes

Any change to `assets/js/app.js`, shared CSS, mobile navigation, or term-page rendering should trigger a quick review of:

- Browse on desktop and mobile;
- at least one dedicated term page;
- at least one `researched` entry and, once present in the corpus, at least one `pending` entry;
- About, Categories, Contribute, and Methodology;
- theme switching;
- pronunciation;
- keyboard focus;
- mobile navigation.

## Known limitation of automated QA

Repository validation can confirm structure, syntax, supported status values, and dataset relationships. It cannot prove that a definition is editorially sound, that provenance evidence justifies a `researched` status, that a page looks correct on every browser, that a particular speech voice pronounces a term correctly, or that a screen-reader experience is clear. Those require human spot checks and editorial judgment and should remain part of release readiness rather than being represented as fully automated guarantees.
