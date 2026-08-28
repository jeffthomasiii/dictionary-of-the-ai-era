# AILex Visual Direction

**Dictionary of the AI Era**

This document records the visual direction established before the project's provenance and research phase. It is intended to keep future UI work consistent, including AI-assisted and vibe-coded changes.

## Brand hierarchy

The primary product name is **AILex**.

The descriptor/tagline is **Dictionary of the AI Era**.

AILex is pronounced **/A-I-lex/**, saying the letters A and I followed by “lex.” The main interface may keep the masthead visually clean, while the About page and repository documentation should make the pronunciation explicit.

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

## Site structure

The site should behave like a reference website, not a single-page landing page.

Primary navigation is divided into dedicated pages:

- **Browse:** the searchable dictionary home page
- **Categories:** explains the editorial category system
- **About:** project purpose, pronunciation, transparency, and licensing context
- **Contribute:** public-facing contribution guidance and current submission path
- **Methodology:** explains how terms are identified, evaluated, categorized, defined, reviewed, and maintained

Markdown governance documents may remain in the repository, but the public site should provide readable HTML pages for core reader-facing information.

## Typography

Use an editorial serif for AILex identity, term names, and major headings. Use a clean system sans-serif for interface controls, metadata, labels, navigation, and supporting copy.

The serif/sans-serif contrast is deliberate: **dictionary tradition + contemporary technical interface**.

## Color system

The overall palette is intentionally muted. Avoid dominant electric blue, excessive gradients, neon glows, or high-saturation backgrounds.

### System accent

Muted teal is the primary interface accent. It is used for focus states, the identity mark, technical details, and selected interface elements.

### Category colors

Category color is semantic, not decorative. The same category should retain its color anywhere it appears.

- **AI Culture & Slang:** muted violet
- **AI Ways of Working:** muted teal
- **AI Systems & Technical Concepts:** muted steel blue
- **AI Risks, Safety & Governance:** muted clay/coral

Colors should remain accessible and legible in both light and dark themes.

## Light mode

Light mode should feel paper-like rather than stark white. Use warm off-white backgrounds, restrained borders, generous whitespace, and subtle technical line work.

## Dark mode

Dark mode should be deep charcoal/blue-black rather than saturated navy. Category colors and the teal system accent remain visible but subdued. Avoid luminous neon treatments.

The light and dark themes are two expressions of the same design system, not separate visual identities.

## Technical visual language

Technical flair should appear primarily through subtle structure:

- faint grid systems
- fine connecting lines and nodes
- restrained waveform or mesh motifs
- small geometric marks
- precise metadata labels
- measured use of monospace-like interface conventions such as keyboard shortcuts

The hero should combine multiple subtle technical layers rather than relying on a grid alone. Network/node diagrams and layered wave or mesh lines should create depth comparable to the approved visual mockup without becoming decorative noise.

These elements should remain in the background and never compete with the dictionary content.

## Category iconography

Category icons should be simple line icons with semantic meaning rather than abstract typographic symbols.

- Culture & Slang: conversation/speech
- Ways of Working: people/collaboration
- Systems & Technical: cube/system
- Risks & Governance: shield/protection
- All Terms: simple collection/grid

Icons inherit their category color and remain secondary to the category label.

## Dictionary entries

Term entries should prioritize this reading hierarchy:

1. Term
2. Pronunciation and part of speech
3. Definition
4. Use in a sentence
5. Category, status, aliases, and supporting metadata

Category color may appear as a narrow rule, icon, label, or other small semantic indicator. Do not flood entire cards with category colors.

### View modes

The Browse page supports both:

- **List view:** information-rich scanning with definition and usage visible together
- **Grid view:** compact dictionary cards comparable to the approved mockup

The user's view preference should persist locally. Neither view changes the underlying term data or filtering behavior.

## Interaction

Search is the primary action and should remain visually dominant.

The interface should support:

- instant search
- category filtering
- A–Z browsing
- list/grid view switching
- keyboard search shortcut
- persistent light/dark preference
- responsive layouts

## Dates and living status

When the interface displays an updated date, use a human-readable full date such as **August 28, 2026**, rather than only the year. The dictionary's living status may appear separately from the date.

## Theme behavior

On first visit, the site follows the operating system's preferred color scheme. A user-selected light or dark preference is then saved locally and takes precedence on future visits.

## Roadmap design item: dedicated term pages

Individual dictionary entries should eventually have dedicated pages with stable URLs. Those pages may contain expanded provenance, related terms, source citations, history, status, aliases, and other supporting metadata. This is intentionally deferred until the provenance/data model work is mature enough to support it well.

## Roadmap design item: audible pronunciation

Dictionary terms should eventually include an accessible speaker control beside the written pronunciation so a reader can hear the term spoken aloud.

The initial implementation should favor browser-based speech synthesis to preserve the static GitHub Pages architecture. Terms that are ambiguous, newly coined, acronym-heavy, or consistently mispronounced by browser speech engines may later use curated audio files.

Pronunciation controls should:

- appear as a secondary control beside the phonetic pronunciation
- work with keyboard navigation
- expose a clear screen-reader label such as **Hear pronunciation of Agentic**
- avoid autoplay
- provide a consistent interaction in list view, grid view, and future dedicated term pages

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
- collapsing primary reader-facing content back into a single-page navigation pattern

The design should always answer the same question: **Does this still feel like a dictionary first, with the AI era expressed through its details?**
