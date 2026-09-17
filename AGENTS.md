# EpochLex Codex Instructions

## Project identity

EpochLex — Dictionary of the AI Era — is an open-source, searchable, data-driven reference work for terminology of the AI era.

Pronunciation: `/EP-uk-leks/`.

The repository `jeffthomasiii/dictionary-of-the-ai-era` and its current `main` branch are the source of truth for established EpochLex behavior, architecture, standards, and project state.

Do not use the historical name AILex except when discussing project history.

## Development model

EpochLex is:

**Vibe coded · Human-directed · AI-assisted · Human-reviewed**

Codex may assist with implementation, debugging, testing, documentation, refactoring, and repository analysis.

Human review remains responsible for product direction, editorial judgment, source evaluation, acceptance of architecture changes, and merging/publishing changes.

## Source-of-truth hierarchy

Before implementing a change, inspect the relevant current repository documentation.

Start with:

* `README.md`
* `docs/ARCHITECTURE.md`
* `CONTRIBUTING.md`

Then consult task-specific sources as needed:

* `DESIGN.md`
* `BRAND.md`
* `PROVENANCE.md`
* `docs/TAXONOMY.md`
* `docs/ROADMAP.md`
* `docs/QA.md`
* `EDITIONS.md`
* `AI-TRANSPARENCY.md`
* `docs/ORIGIN.md`

Current repository implementation takes precedence over older planning notes or external project-context files when they conflict.

Do not convert proposals, roadmap ideas, common practices, or assumptions into established EpochLex requirements.

When relevant, distinguish between:

* **Established** — documented or implemented in the repository.
* **Proposed** — suggested or identified for future work but not adopted.
* **Open** — undecided or insufficiently specified.

## Architecture guardrails

EpochLex is intentionally a static, data-driven reference site hosted through GitHub Pages.

Preserve this architecture unless the requested feature explicitly requires reconsidering it and the human owner approves that architectural change.

Do not introduce any of the following merely because they are common development patterns:

* server-side database
* application backend
* server API
* JavaScript framework
* required build pipeline
* authentication system
* duplicated content datastore

Prefer progressive enhancement and existing project patterns.

Canonical content belongs in the established source-controlled datasets.

Important current locations include:

* `data/terms.json`
* `data/provenance.json`
* `data/editions.json`
* `terms/<slug>/index.html`
* `assets/js/`
* `assets/css/`
* `word-of-the-day/`
* `manifest.webmanifest`
* `assets/js/pwa.js`
* `service-worker.js`

Do not create duplicate editorial datasets merely to simplify UI implementation.

## Data integrity

Treat canonical term and provenance data as connected records.

When adding or materially changing dictionary entries:

* preserve the established schemas;
* keep `terms.json` alphabetically sorted by `term`;
* keep term and provenance slug sets synchronized;
* verify related-term targets exist;
* do not create self-links;
* preserve dedicated term pages and indexing metadata;
* preserve written pronunciation;
* add speech overrides when necessary;
* update sitemap or other publishing surfaces when required.

Do not infer missing provenance claims.

`null`, unresolved information, or documented uncertainty is preferable to invented precision.

AI output is never a source.

## Related-term semantics

EpochLex currently supports related-term discovery but does not encode typed semantic relationships.

Do not infer or display relationship claims such as:

* depends on
* subtype of
* broader than
* owned by
* developed by
* powers
* contrasts with

unless the underlying data model explicitly supports that relationship.

## Editorial constraints

Definitions should explain rather than promote.

Avoid hype and marketing language.

Prefer plain language where practical.

Represent contested or emerging meanings appropriately.

Examples should demonstrate natural usage.

Do not invent project standards that are not established in the repository.

Editorial publication decisions remain human decisions.

## Design constraints

Follow `DESIGN.md`, `BRAND.md`, approved logo assets, and current implementation.

Preserve EpochLex's established direction:

* modern dictionary/reference-work character;
* calm and editorial rather than dashboard-like;
* restrained technical layer;
* strong readability;
* editorial serif for identity, term names, and major headings;
* clean sans-serif for controls, navigation, metadata, and supporting copy;
* paper-like light mode;
* charcoal/blue-black dark mode;
* muted teal system accent;
* established semantic category colors.

Avoid introducing:

* dominant electric blue;
* neon cyberpunk aesthetics;
* dominant glassmorphism;
* decorative AI imagery competing with reference content;
* unnecessary animation;
* oversized dashboard statistics;
* dense interface chrome;
* low-contrast text.

Preserve responsive behavior, keyboard access, visible focus states, accessible controls, and non-color-only meaning.

## Change workflow

Before editing:

1. Inspect the relevant implementation and documentation.
2. Identify the smallest coherent change that satisfies the request.
3. Note any architecture, editorial, data-model, accessibility, or publishing implications.
4. Do not silently expand the task into unrelated cleanup or modernization.

During implementation:

* preserve existing working behavior unless the change requires otherwise;
* reuse existing patterns before introducing new abstractions;
* avoid unnecessary dependencies;
* keep changes reviewable;
* update documentation when implementation makes existing documentation inaccurate.

Do not push directly to `main` unless explicitly requested.

Prefer:

1. update local `main`;
2. create a focused feature/fix branch;
3. implement the change;
4. validate it;
5. review the diff;
6. create a pull request;
7. leave merge/publish judgment to the human owner.

## Validation

Use the validation expectations in `CONTRIBUTING.md` and `docs/QA.md`.

Depending on the change, verify:

* JSON parses successfully;
* JavaScript syntax is valid;
* term/provenance slug sets remain synchronized;
* related-term targets resolve;
* dedicated term pages remain available;
* canonical and social metadata remain correct;
* sitemap remains accurate;
* light and dark themes remain usable;
* desktop and mobile layouts remain usable;
* installed-PWA behavior remains usable when affected;
* keyboard and accessibility behavior are preserved;
* no-JavaScript/indexable fallback content remains intact where applicable.

Run the most relevant checks available rather than claiming validation that was not performed.

Report checks that could not be run.

## Local serving

Do not open the site using `file://`.

Serve the repository locally:

```bash
python -m http.server 8000
```

Then use:

`http://localhost:8000`

## Scope discipline

Do not redesign, refactor, migrate, rename, reorganize, or modernize unrelated parts of EpochLex unless explicitly requested.

When a requested feature requires a meaningful architectural or data-model decision that the repository has not established, identify that decision rather than silently creating a new project standard.
