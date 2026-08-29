# Contributing

AILex · Dictionary of the AI Era is a curated, open-source reference project. Contributions should improve the accuracy, clarity, provenance, usability, accessibility, documentation, maintainability, or coverage of the dictionary.

Contributions do **not** have to involve code.

Useful contributors may include developers, researchers, writers, editors, designers, accessibility testers, documentation contributors, AI practitioners, and readers who simply notice a missing term, weak source, broken pronunciation, or site problem.

## Ways to contribute

You can help AILex by contributing:

- new term suggestions;
- clearer definitions or examples;
- aliases, acronyms, or pronunciation guidance;
- stronger sources or provenance corrections;
- historical context or evidence of early usage;
- accessibility and cross-device testing;
- UI, design, or interaction improvements;
- bug fixes and technical maintenance;
- validation or automation improvements;
- documentation, editing, or information-architecture improvements;
- review feedback on existing entries or features.

The public [Contribute page](https://jeffthomasiii.github.io/dictionary-of-the-ai-era/contribute.html) is the reader-friendly entry point. This document describes contribution expectations for people working directly with the repository.

## Before contributing

Start with [`docs/README.md`](docs/README.md), then use the document that matches your change:

- [`docs/ORIGIN.md`](docs/ORIGIN.md) for project history and intent;
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for site/data structure and technical boundaries;
- [`docs/ROADMAP.md`](docs/ROADMAP.md) for current priorities;
- [`PROVENANCE.md`](PROVENANCE.md) for sourcing, origin, first-known-use, and attribution standards;
- [`DESIGN.md`](DESIGN.md) for interface and interaction guardrails;
- [`BRAND.md`](BRAND.md) for AILex naming and identity;
- [`EDITIONS.md`](EDITIONS.md) for Living Dictionary and annual-edition behavior;
- [`AI-TRANSPARENCY.md`](AI-TRANSPARENCY.md) for the project's AI-assisted development and editorial policy.

## AI-assisted contributions

AI-assisted contributions are welcome. Contributors should be transparent when AI materially helped draft code, definitions, research summaries, documentation, or other submitted work.

AI output is not evidence by itself. Claims about terminology, history, origin, usage, or attribution should be verified against appropriate external sources before publication. Human contributors remain responsible for what they submit.

Generated code or documentation should also be reviewed rather than submitted solely because it runs or reads plausibly.

## Proposing a term

A proposed term should include:

- Term
- Slug
- Written pronunciation
- Plain-English definition
- Natural example sentence
- Part of speech
- One or more categories
- Status
- Known aliases or acronyms
- Evidence of real-world usage
- Suggested related terms
- A researched provenance record with credible sources

A candidate should add distinct reader value. Before proposing a new entry, consider whether the phrase is better represented as an alias of an existing term or is too generic to require its own AI-era definition.

## Published-term completeness

AILex treats a published term as a complete reference entry rather than a placeholder.

A new published term should have:

1. one entry in `data/terms.json`;
2. one matching researched record in `data/provenance.json`;
3. valid related-term slugs that point only to published entries;
4. a dedicated `terms/<slug>/index.html` page;
5. search/social metadata consistent with the existing dedicated pages;
6. inclusion in the sitemap;
7. a pronunciation override when browser speech synthesis would reasonably misread the term or acronym.

The term and provenance slug sets should remain equal.

## Provenance contributions

Provenance research belongs in `data/provenance.json` and should follow `PROVENANCE.md`.

When adding or revising a provenance record:

- distinguish sources that support meaning from sources that support origin;
- prefer primary sources for technical definitions, naming events, specifications, original research, standards, and release dates;
- use `firstKnownUse: null` when available evidence does not responsibly establish an earliest use;
- distinguish **coined by**, **introduced by**, **formalized by**, **popularized by**, and **associated with**;
- include only history events that materially help explain the term;
- identify what each source supports rather than treating every citation as evidence for every field;
- preserve uncertainty and disagreement when the historical record is unclear.

A `researched` status means an initial human-reviewed sourcing pass has been completed. It does not imply permanent certainty or prevent later revision.

## Editorial standards

Definitions should:

- explain rather than promote;
- avoid hype and marketing language;
- distinguish established meanings from emerging or contested usage;
- avoid defining a term using equally obscure jargon when plain English is available;
- be concise enough to scan but complete enough to stand alone;
- be human-reviewed before publication.

Examples should sound like natural usage rather than miniature definitions rewritten as sentences.

## Status vocabulary

Statuses may include:

- Established
- Technical
- Emerging
- Emerging slang
- Governance term
- Research term
- Technical security term
- Contested
- Deprecated

Compound labels may be used when they add useful context, but status should remain reader-facing rather than becoming an internal workflow field.

## Updating `terms.json`

Keep terms sorted alphabetically by `term`. Use a lowercase hyphenated slug and preserve the existing schema.

Before submitting changes, verify that search can find the entry through relevant term text, definition text, aliases, categories, and examples.

## Pronunciation

Every term has a written pronunciation. Audible pronunciation uses the shared browser speech engine in `assets/js/app.js`.

When an acronym or unusual term is likely to be pronounced incorrectly by browser voices, add an explicit entry to the shared speech override table. Acronyms such as RLHF, RLAIF, PEFT, MCP, and LLM are spoken letter-by-letter where appropriate.

Do not remove the written pronunciation even when audible playback exists. Audio is supplemental and must fail gracefully when speech synthesis is unavailable.

## Site and interface contributions

UI changes should follow `DESIGN.md` and preserve the reference-first character of AILex.

In particular:

- do not create duplicate editorial datasets for UI convenience;
- preserve keyboard access and visible focus states;
- preserve responsive/mobile behavior;
- avoid color-only meaning;
- preserve no-JavaScript/indexable fallback content on dedicated term pages;
- avoid inventing semantic relationship labels that the provenance data does not encode;
- keep public-facing documentation focused on readers rather than repository mechanics.

## Documentation contributions

Documentation is part of the product and should be maintained with the same care as code and dictionary content.

Use this boundary:

- **Public website documentation** should help readers understand AILex, its features, origin, categories, methodology, Living Dictionary behavior, and easy ways to contribute.
- **Repository documentation** should preserve project history, architecture, governance, detailed editorial standards, development philosophy, contribution workflows, roadmap, release mechanics, and the open-source AI experiment.

When a feature moves from roadmap to implemented, update the relevant documentation rather than leaving stale future-state language behind.

## Validation checklist

Depending on the change, verify:

- JSON parses successfully;
- term/provenance slug parity is preserved;
- related-term targets resolve and do not self-link;
- JavaScript syntax is valid;
- dedicated term pages exist for all published entries;
- canonical/social metadata remains present;
- sitemap URLs reflect the published page set;
- pronunciation controls remain keyboard and screen-reader accessible;
- light, dark, desktop, tablet, and mobile behavior remain usable;
- public documentation still points readers toward the site rather than exposing unnecessary repository mechanics;
- repository documentation links remain valid.

## Contribution licensing

By contributing original software or code to this project, you agree that your contribution may be distributed under the project's MIT License.

By contributing original dictionary or editorial content, you agree that your contribution may be distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

Do not submit material you do not have the right to contribute. Third-party quotations and source material should be clearly identified and remain subject to their original rights and licensing terms.
