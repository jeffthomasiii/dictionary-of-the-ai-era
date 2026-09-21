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

- **Browse:** searchable dictionary home page with A-Z navigation, category filters, list/grid views, audible pronunciation, and the Word of the Day discovery panel
- **Categories:** taxonomy explanation plus live browsable collections generated from the dictionary dataset
- **About:** project purpose, EpochLex pronunciation, Living Dictionary/edition model, current capabilities, transparency, and licensing
- **Contribute:** contribution guidance
- **Methodology:** editorial, provenance, sourcing, and maintenance process
- **Experiment:** public editorial case-study surface at `experiment/`, with a companion report reader at `experiment/report/`; linked contextually from About and Methodology and available under More in the installed PWA rather than added to permanent primary navigation

Each published term also has a stable dedicated URL at `terms/<slug>/` with definition, pronunciation, provenance, history, related terms, sources, and research status.

Word of the Day has a dedicated page at `word-of-the-day/` with the current daily term, pronunciation, definition, example, links to the canonical entry, sharing, and recent Word of the Day history.

EpochLex also has an installable Progressive Web App. The installed PWA uses the same EpochLex visual identity and content as the website but adopts a focused app shell when launched in standalone mode.

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

Category color is semantic, not decorative. The established semantic colors remain intentionally more distinct than the surrounding brand palette so readers can recognize category at a glance in both light and dark modes.

Light mode:

- **AI Culture & Slang:** muted violet `#8B6FBD`
- **AI Ways of Working:** muted teal `#4E9A8A`
- **AI Systems & Technical Concepts:** muted steel blue `#507EA6`
- **AI Risks, Safety & Governance:** muted clay/coral `#B56F61`
- **AI Organizations, Products & Models:** uses the restrained EpochLex system accent treatment established in the implementation rather than introducing a competing fifth decorative palette

Dark mode uses brighter counterparts for comparable recognition and contrast for the four established semantic category hues, while **AI Organizations, Products & Models** continues to use the implementation's system-accent treatment.

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

Secondary discovery actions, including Word of the Day links, should remain visually quieter than search and dictionary content. Where icons are used, they should clarify the action without turning secondary links into dominant call-to-action buttons.

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
- Organizations, Products & Models: organization/building or similarly restrained named-entity cue
- All Terms: collection/grid

Icons inherit their semantic/system accent and remain secondary to the label.

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

## Word of the Day

Word of the Day is a discovery feature layered onto the dictionary rather than a separate editorial brand or promotional landing page.

On Browse:

- it appears after the primary hero/search/filter area and before Browse A-Z;
- it must not displace search as the primary interaction;
- the daily term, definition, pronunciation, category, date, and compact navigation actions should remain visually subordinate to the main dictionary hero;
- action links should be restrained, icon-led where useful, and avoid oversized filled buttons.

On the dedicated Word of the Day page:

- the selected term should be the dominant headline;
- the page-level “Word of the Day” label should not compete with the term;
- definition, pronunciation, part of speech, category, example, canonical-entry link, sharing, and recent-word history may be shown;
- recent words should preserve the same reference-site hierarchy and theme behavior rather than becoming a dashboard or activity feed.

Word of the Day uses the normal EpochLex light/dark system and should not introduce a separate color palette, decorative AI illustration, or promotional visual identity.

## Mobile app shell and installed PWA

The **EpochLex PWA Showcase** is the visual and interaction reference for both the mobile-browser experience and the installed standalone experience.

On phone-size viewports, the public website and installed PWA share the same app-like shell: compact branded header, persistent bottom navigation, compact content treatments, and the More sheet. The installed PWA remains the installable form of the same canonical site rather than a separate content product.

Established standalone behavior:

- phone-size browser views use the same app-like navigation shell as the installed PWA, while desktop and larger browser layouts retain the reference-site navigation;
- responsive testing in desktop developer tools continues to show the normal mobile website unless the browser is actually emulating/running standalone display mode;
- the normal primary navigation and mobile hamburger menu are hidden in standalone mode;
- the installed app uses a compact branded header with the EpochLex lockup and theme control;
- a persistent bottom navigation provides **Browse**, **Categories**, **Word**, **About**, and **More**;
- **Word** links directly to the dedicated Word of the Day experience;
- **More** opens an app-style secondary sheet for lower-frequency destinations such as **Contribute** and **Methodology**;
- the active section is clearly indicated without oversized tabs, heavy fills, or dashboard styling;
- iconography uses restrained line icons consistent with the site's existing system;
- bottom navigation and sheets respect device safe areas and remain usable in both light and dark themes;
- the normal site footer may be omitted in standalone mode because the persistent app navigation becomes the installed experience's primary shell;
- standalone navigation should remain keyboard accessible and expose appropriate navigation/dialog semantics.

The shared mobile/PWA shell must not fork content or create app-only editorial pages. It is an application-like frame over the same canonical EpochLex site.

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
- use the same interaction model on Browse, Word of the Day, and dedicated term pages;
- use explicit speech overrides for acronyms or terms browser voices commonly misread;
- fail gracefully when speech synthesis is unsupported.

EpochLex itself uses the explicit speech form **“epoch lex.”**

Curated audio files may be added later for unusual or consistently unreliable pronunciations, but are not required for the static architecture.

## Category browsing

The Categories page has two responsibilities:

1. explain the five editorial categories;
2. provide live, browsable term collections sourced from `data/terms.json`.

Category counts and membership should never be maintained in a second manual dataset.

## Responsive behavior

Desktop and tablet layouts should preserve the editorial reference feel. Mobile should simplify controls without removing core discovery capability.

Current mobile-browser behavior includes:

- native `<details>/<summary>` primary navigation;
- compact search/filter treatment;
- horizontally scrollable A-Z navigation;
- single-column term layouts where necessary;
- responsive category collections and related-term cards;
- responsive Word of the Day cards and compact icon-led actions.

Phone-size browser views and installed standalone views use the shared app shell defined above rather than the hamburger-navigation pattern. The Experiment publication keeps its compact card surfaces and swipeable content groups, but uses the same global EpochLex bottom navigation as the rest of the mobile site.

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
- category collection navigation;
- Word of the Day discovery, recent-word history, and sharing;
- installable PWA behavior, standalone app navigation, and offline-aware caching where supported.

Push notifications are not a current interaction capability.

## Publishing and metadata

EpochLex is a reference site and should remain indexable by default.

Current publishing behavior includes:

- canonical URLs using `https://epochlex.justathoughtblog.org/` as the public base;
- Open Graph and Twitter/X metadata;
- Schema.org `DefinedTermSet` on home;
- Schema.org `DefinedTerm` on term pages;
- sitemap and robots directives;
- noindex behavior for the 404 page.

The custom domain is the current canonical public base. Publishing changes should keep canonical URLs, sitemap URLs, social URLs, redirects, and GitHub Pages configuration aligned with it.

## Dates and living status

The homepage **Updated** date is a Living Dictionary freshness indicator, not a deployment timestamp. It records the most recent date on which published EpochLex dictionary content received a substantive reader-facing change.

Advance the date when a published change materially affects the dictionary itself, including:

- adding a new published term;
- materially revising a definition, example, category, status, alias, or other reader-facing entry content;
- adding or materially revising provenance, origin, first-known-use, history, sources, or research status for a published entry when that changes what readers can learn from the entry;
- making a substantive corpus correction that changes meaning or classification.

Do **not** advance the date for UI or PWA changes, code refactoring, documentation-only changes, SEO or metadata maintenance, build/cache/deployment work, or purely typographic/copyediting fixes that do not materially change dictionary content.

The value is maintained manually in `index.html` and should be updated in the same change that introduces the qualifying Living Dictionary content update. Display it as a human-readable full date such as **September 8, 2026**. The **Living** status is conceptually separate from this date.

Word of the Day uses the EpochLex calendar date in Pacific Time and changes at midnight Pacific Time.

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
