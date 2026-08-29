# AILex Visual Direction

**Dictionary of the AI Era**

This document records the visual and interaction direction for AILex. It exists to keep future UI work consistent, including AI-assisted and vibe-coded changes.

## Brand hierarchy

The primary product name is **AILex**.

The descriptor is **Dictionary of the AI Era**.

AILex is pronounced **/A-I-lex/**, saying the letters A and I followed by “lex.” The masthead remains visually clean, while the About page and repository documentation make the pronunciation explicit. The About page also provides an audible pronunciation control.

## Design intent

The interface should feel like a **modern dictionary with a restrained technical layer**. It should preserve the authority, clarity, and scanability of a reference work while acknowledging that the subject is the language of the AI era.

The design should not look like a generic SaaS dashboard, neon cyberpunk interface, conventional blog, or single-page marketing site.

### Core qualities

- Editorial
- Modern
- Technical
- Calm
- Credible
- Search-first
- Highly readable
- Lightly futuristic rather than overtly futuristic

## Current site structure

AILex behaves like a reference website rather than a single landing page.

Primary navigation includes:

- **Browse:** searchable dictionary home page with A-Z navigation, category filters, list/grid views, and audible pronunciation
- **Categories:** taxonomy explanation plus live browsable collections generated from the dictionary dataset
- **About:** project purpose, AILex pronunciation, Living Dictionary/edition model, transparency, and licensing
- **Contribute:** contribution guidance
- **Methodology:** editorial, provenance, sourcing, and maintenance process

Each published term also has a stable dedicated URL at `terms/<slug>/` with definition, pronunciation, provenance, history, related terms, sources, and research status.

Repository governance documents remain Markdown, while the public site provides readable HTML for the main reader-facing concepts.

## Typography

Use an editorial serif for AILex identity, term names, and major headings. Use a clean system sans-serif for interface controls, metadata, labels, navigation, and supporting copy.

The serif/sans-serif contrast is deliberate: **dictionary tradition + contemporary technical interface**.

## Color system

The palette is intentionally muted. Avoid dominant electric blue, excessive gradients, neon glows, or high-saturation backgrounds.

### System accent

Muted teal is the primary interface accent. It is used for focus states, the identity mark, technical details, pronunciation controls, and selected interface elements.

### Category colors

Category color is semantic, not decorative. The same category should retain its color anywhere it appears.

- **AI Culture & Slang:** muted violet
- **AI Ways of Working:** muted teal
- **AI Systems & Technical Concepts:** muted steel blue
- **AI Risks, Safety & Governance:** muted clay/coral

Colors should remain accessible and legible in both light and dark themes. Never depend on color alone to communicate category or state.

## Light mode

Light mode should feel paper-like rather than stark white. Use warm off-white backgrounds, restrained borders, generous whitespace, and subtle technical line work.

## Dark mode

Dark mode should be deep charcoal/blue-black rather than saturated navy. Category colors and the teal system accent remain visible but subdued. Avoid luminous neon treatments.

The light and dark themes are two expressions of the same design system, not separate identities.

## Technical visual language

Technical flair appears through subtle structure:

- faint grid systems
- fine connecting lines and nodes
- restrained waveform or mesh motifs
- small geometric marks
- precise metadata labels
- measured keyboard/technical interface conventions

These elements should remain secondary and never compete with dictionary content.

## Category iconography

Category icons are simple line icons with semantic meaning rather than abstract typographic symbols.

- Culture & Slang: conversation/speech
- Ways of Working: people/collaboration
- Systems & Technical: cube/system
- Risks & Governance: shield/protection
- All Terms: collection/grid

Icons inherit their category color and remain secondary to the label.

## Browse entries

Browse entries follow this hierarchy:

1. Term
2. Written and audible pronunciation
3. Part of speech
4. Definition
5. Use in a sentence
6. Category, status, aliases, and supporting metadata

Category color may appear as a narrow rule, icon, label, or other small semantic indicator. Do not flood entire cards with category colors.

### View modes

Browse supports:

- **List view:** information-rich scanning with definition and usage visible together
- **Grid view:** compact dictionary cards

The user's view preference persists locally. Neither view changes the underlying term data or filtering behavior.

## Dedicated term pages

Dedicated term pages are part of the current product, not a future roadmap item.

They should maintain a strong reference hierarchy and expose richer context than Browse, including:

- term and pronunciation
- part of speech
- definition and example
- category, status, and aliases
- origin/context
- first known use when defensible
- history
- related-term discovery
- sources
- research status and review dates

Stable URLs and meaningful fallback HTML are important because term pages are indexable and may be opened without JavaScript.

## Related-term discovery

Related terms should help a reader continue through connected concepts without inventing relationship semantics that the data does not support.

Current discovery uses explicit outbound relationships plus reciprocal inbound relationships. Unless the provenance schema gains typed relationships, the UI should describe them simply as connected or related entries rather than claiming “depends on,” “is a subtype of,” or similar semantics.

## Audible pronunciation

Audible pronunciation is implemented through the browser Web Speech API while preserving written pronunciation as the primary reference.

Pronunciation controls should:

- appear as a secondary speaker control beside written pronunciation
- avoid autoplay
- work with keyboard navigation
- expose clear screen-reader labels
- use the same interaction model on Browse and dedicated term pages
- use explicit speech overrides for acronyms or terms browser voices commonly misread
- fail gracefully when speech synthesis is unsupported

AILex itself should use the explicit speech form **“A I lex.”**

Curated audio files may be added later for unusual or consistently unreliable pronunciations, but are not required for the static architecture.

## Category browsing

The Categories page has two responsibilities:

1. explain the four editorial categories;
2. provide live, browsable term collections sourced from `data/terms.json`.

Category counts and membership should never be maintained in a second manual dataset.

## Responsive behavior

Desktop and tablet layouts should preserve the editorial reference feel. Mobile should simplify controls without removing core discovery capability.

Current mobile behavior includes:

- native `<details>/<summary>` primary navigation
- compact search/filter treatment
- horizontally scrollable A-Z navigation
- single-column term layouts where necessary
- responsive category collections and related-term cards

Avoid mobile-specific UI that creates a second behavioral model when the same semantic control can adapt responsively.

## Search and interaction

Search is the primary action and should remain visually dominant.

The interface currently supports:

- instant search
- category filtering
- A-Z browsing
- list/grid switching
- keyboard search shortcut
- persistent light/dark preference
- audible pronunciation
- related-term navigation
- category collection navigation

## Publishing and metadata

AILex is a reference site and should remain indexable by default.

Current publishing behavior includes:

- canonical URLs
- Open Graph and Twitter/X metadata
- Schema.org `DefinedTermSet` on home
- Schema.org `DefinedTerm` on term pages
- sitemap and robots directives
- noindex behavior for the 404 page

A custom-domain migration must update canonical URLs, sitemap URLs, social URLs, and redirects together.

## Dates and living status

When the interface displays an updated date, use a human-readable full date such as **August 28, 2026** rather than only the year. The Living Dictionary status is conceptually separate from the last-updated date.

Annual editions are immutable historical snapshots and should not be confused with the continuously updated public site.

## Theme behavior

On first visit, the site follows the operating system's preferred color scheme. A user-selected light or dark preference is then saved locally and takes precedence on future visits.

## Accessibility baseline

Design changes should preserve:

- semantic headings and landmarks
- keyboard-operable controls
- visible focus states
- screen-reader labels for icon-only controls
- sufficient contrast in both themes
- reduced-motion behavior where motion is used
- written equivalents for audible information
- functionality that does not depend on color alone

## Guardrails

Future design changes should avoid:

- excessive blue
- neon cyberpunk styling
- glassmorphism as a dominant motif
- unnecessary animation
- oversized dashboard statistics
- dense UI chrome
- low-contrast text
- decorative AI imagery that reduces readability
- category colors used inconsistently
- collapsing reader-facing content back into a single-page navigation pattern
- UI labels that imply editorial certainty not present in the underlying data

The design should always answer the same question: **Does this still feel like a dictionary first, with the AI era expressed through its details?**
