# EpochLex Visual Direction

**Dictionary of the AI Era**

This document records the visual and interaction direction for EpochLex. It exists to keep future UI work consistent, including AI-assisted and vibe-coded changes.

## Brand hierarchy

The primary product name is **EpochLex**.

The descriptor is **Dictionary of the AI Era**.

EpochLex is pronounced **/EP-uk-leks/**, saying **epoch** followed by **lex**. The masthead remains visually clean, while the About page and repository documentation make the pronunciation explicit. The About page also provides an audible pronunciation control.

## Design intent

The interface should feel like a **modern dictionary with a restrained technical layer**. It should preserve the authority, clarity, and scanability of a reference work while acknowledging that the subject is the language of the AI era.

The selected visual direction combines **editorial reference + AI-era digital signal**. Traditional reference cues come from serif typography, paper-like surfaces, strong hierarchy, and generous whitespace. The AI-era layer appears through restrained blue-green technical accents, subtle grids, segmented geometry, precise metadata, and controlled interaction states.

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

EpochLex behaves like a reference website rather than a single landing page.

Primary navigation includes:

- **Browse:** searchable dictionary home page with A-Z navigation, category filters, list/grid views, and audible pronunciation
- **Categories:** taxonomy explanation plus live browsable collections generated from the dictionary dataset
- **About:** project purpose, EpochLex pronunciation, Living Dictionary/edition model, transparency, and licensing
- **Contribute:** contribution guidance
- **Methodology:** editorial, provenance, sourcing, and maintenance process

Each published term also has a stable dedicated URL at `terms/<slug>/` with definition, pronunciation, provenance, history, related terms, sources, and research status.

Repository governance documents remain Markdown, while the public site provides readable HTML for the main reader-facing concepts.

## Typography

The primary editorial typeface is **Playfair Display**. Use it for:

- EpochLex identity and wordmark-adjacent typography;
- page titles;
- term names and headwords;
- major section headings;
- other moments where the site should feel like a reference publication.

The primary sans-serif is **Inter**. Use it for:

- body copy;
- navigation;
- buttons and controls;
- metadata and labels;
- filters;
- technical and supporting UI.

Both font families should include practical system fallbacks so the site remains readable if remote font loading fails.

The serif/sans-serif contrast is deliberate: **dictionary tradition + contemporary technical interface**.

## Color system

The approved EpochLex palette is restrained, scholarly, and digital without relying on the familiar bright-blue or neon AI aesthetic.

### Core palette

- **Ink Navy:** `#0F1D2D` — primary light-mode text, authority, depth
- **Charcoal:** `#2B333B` — secondary dark neutral
- **Sage:** `#7A9276` — primary brand accent, knowledge, continuity, horizon/epoch cue
- **Blue Green:** `#5C8F95` — technical accent, focus, digital/AI signal
- **Paper:** `#F5F2EC` — primary light-mode background
- **Warm Gray:** `#E4E0DB` — secondary neutral surface
- **Slate:** `#A7AEB3` — borders and subdued supporting detail

### Accent roles

**Sage** is the primary brand accent. It should appear in selected states, restrained brand details, active navigation cues, and the visual identity's horizon/epoch language.

**Blue Green** is the technical accent. It is preferred for focus treatments, search interaction, pronunciation controls, subtle diagrams, digital geometry, and other interface details that communicate the AI-era layer.

Neither accent should flood large areas of the interface.

### Category colors

Category color remains semantic rather than decorative. Categories retain distinct visual signals, but those signals should be muted so they sit inside the EpochLex system rather than becoming a competing palette.

- **AI Culture & Slang:** slate-derived neutral
- **AI Ways of Working:** sage-derived
- **AI Systems & Technical Concepts:** blue-green-derived
- **AI Risks, Safety & Governance:** muted warm neutral

Never depend on color alone to communicate category or state.

## Light mode

Light mode uses **Paper** as the dominant field rather than stark white. Surfaces may lift slightly toward soft white while Warm Gray and Slate provide borders and secondary structure.

Ink Navy carries most primary text. Sage and Blue Green remain restrained accents. Shadows should be soft and editorial rather than dramatic.

## Dark mode

Dark mode is a designed counterpart, not a literal inversion.

Use a near-black ink/navy background with slightly lighter blue-charcoal surfaces. Primary text shifts toward Paper, Sage becomes lighter and quieter, and Blue Green remains visible as the technical/focus accent.

Avoid luminous neon treatments, pure black surfaces, or oversaturated green/teal.

The light and dark themes are two expressions of the same identity.

## Surfaces and controls

Buttons, search inputs, cards, menus, and toggles should use restrained rounded rectangles rather than pills everywhere or sharp dashboard boxes.

General treatment:

- medium corner radius;
- thin neutral borders;
- Paper/soft-white surfaces in light mode;
- subtle depth rather than heavy shadows;
- selected states indicated by a soft Sage tint;
- focus states indicated primarily with Blue Green;
- hover states should clarify interaction without shifting layout dramatically.

Search remains the most visually prominent control on Browse.

## Technical visual language

Technical flair appears through subtle structure:

- faint grid systems;
- fine connecting lines and nodes;
- restrained waveform or mesh motifs;
- segmented geometry that can suggest digital transition;
- small geometric marks;
- precise metadata labels;
- measured keyboard/technical interface conventions.

These elements should remain secondary and never compete with dictionary content.

Avoid generic AI clichés such as robot heads, glowing brains, sparkles, or dominant neural-network imagery.

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

- term and pronunciation;
- part of speech;
- definition and example;
- category, status, and aliases;
- origin/context;
- first known use when defensible;
- history;
- related-term discovery;
- sources;
- research status and review dates.

Stable URLs and meaningful fallback HTML are important because term pages are indexable and may be opened without JavaScript.

## Related-term discovery

Related terms should help a reader continue through connected concepts without inventing relationship semantics that the data does not support.

Current discovery uses explicit outbound relationships plus reciprocal inbound relationships. Unless the provenance schema gains typed relationships, the UI should describe them simply as connected or related entries rather than claiming “depends on,” “is a subtype of,” or similar semantics.

## Audible pronunciation

Audible pronunciation is implemented through the browser Web Speech API while preserving written pronunciation as the primary reference.

Pronunciation controls should:

- appear as a secondary speaker control beside written pronunciation;
- avoid autoplay;
- work with keyboard navigation;
- expose clear screen-reader labels;
- use the same interaction model on Browse and dedicated term pages;
- use explicit speech overrides for acronyms or terms browser voices commonly misread;
- fail gracefully when speech synthesis is unsupported.

EpochLex itself uses the explicit speech form **“epoch lex.”**

Curated audio files may be added later for unusual or consistently unreliable pronunciations, but are not required for the static architecture.

## Category browsing

The Categories page has two responsibilities:

1. explain the four editorial categories;
2. provide live, browsable term collections sourced from `data/terms.json`.

Category counts and membership should never be maintained in a second manual dataset.

## Responsive behavior

Desktop and tablet layouts should preserve the editorial reference feel. Mobile should simplify controls without removing core discovery capability.

Current mobile behavior includes:

- native `<details>/<summary>` primary navigation;
- compact search/filter treatment;
- horizontally scrollable A-Z navigation;
- single-column term layouts where necessary;
- responsive category collections and related-term cards.

Avoid mobile-specific UI that creates a second behavioral model when the same semantic control can adapt responsively.

## Search and interaction

Search is the primary action and should remain visually dominant.

The interface currently supports:

- instant search;
- category filtering;
- A-Z browsing;
- list/grid switching;
- keyboard search shortcut;
- persistent light/dark preference;
- audible pronunciation;
- related-term navigation;
- category collection navigation.

## Publishing and metadata

EpochLex is a reference site and should remain indexable by default.

Current publishing behavior includes:

- canonical URLs;
- Open Graph and Twitter/X metadata;
- Schema.org `DefinedTermSet` on home;
- Schema.org `DefinedTerm` on term pages;
- sitemap and robots directives;
- noindex behavior for the 404 page.

A custom-domain migration must update canonical URLs, sitemap URLs, social URLs, and redirects together.

## Dates and living status

When the interface displays an updated date, use a human-readable full date such as **August 28, 2026** rather than only the year. The Living Dictionary status is conceptually separate from the last-updated date.

Annual editions are immutable historical snapshots and should not be confused with the continuously updated public site.

## Theme behavior

On first visit, the site follows the operating system's preferred color scheme. A user-selected light or dark preference is then saved locally and takes precedence on future visits.

## Accessibility baseline

Design changes should preserve:

- semantic headings and landmarks;
- keyboard-operable controls;
- visible focus states;
- screen-reader labels for icon-only controls;
- sufficient contrast in both themes;
- reduced-motion behavior where motion is used;
- written equivalents for audible information;
- functionality that does not depend on color alone.

Brand palette values are starting points, not permission to use low-contrast text. Supporting text may use darker or lighter derived tones when required for readable contrast.

## Guardrails

Future design changes should avoid:

- excessive blue;
- dominant teal SaaS styling;
- neon cyberpunk styling;
- glassmorphism as a dominant motif;
- unnecessary animation;
- oversized dashboard statistics;
- dense UI chrome;
- low-contrast text;
- generic decorative AI imagery;
- category colors used inconsistently;
- collapsing reader-facing content back into a single-page navigation pattern;
- UI labels that imply editorial certainty not present in the underlying data.

The design should always answer the same question: **Does this still feel like a dictionary first, with the AI era expressed through its details?**
