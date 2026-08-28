# Dictionary of the AI Era

A living, searchable dictionary of the language emerging around artificial intelligence.

The project catalogs technical concepts, new ways of working, emerging slang, and terminology related to AI risk, safety, and governance.

## Current MVP

- Plain-English dictionary entries
- Pronunciation for every term
- Definition + natural usage example
- Instant client-side search
- Category filters
- A–Z browsing
- Shareable term anchors
- Structured JSON source data
- GitHub Pages-ready static site
- No database, framework, build step, or API required

## Repository structure

```text
dictionary-of-the-ai-era/
├── index.html
├── 404.html
├── data/
│   └── terms.json
├── assets/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Data model

Each entry in `data/terms.json` follows this structure:

```json
{
  "term": "Vibe Coding",
  "slug": "vibe-coding",
  "pronunciation": "vybe KOH-ding",
  "partOfSpeech": "noun",
  "definition": "A plain-English definition.",
  "example": "A natural example sentence.",
  "categories": ["AI Culture & Slang", "AI Ways of Working"],
  "aliases": [],
  "status": "Established emerging term",
  "added": "2026-08-28",
  "lastReviewed": "2026-08-28",
  "sources": []
}
```

## Editorial principle

This project is intended to be a dictionary, not a list of AI buzzwords. Terms should have documented real-world usage and definitions should distinguish between established technical vocabulary, emerging terminology, slang, research language, and contested concepts.

AI can assist with identifying and researching candidate terms, but inclusion and wording should remain human-reviewed.

## Categories

1. AI Culture & Slang
2. AI Ways of Working
3. AI Systems & Technical Concepts
4. AI Risks, Safety & Governance

## Running locally

Because the app loads `data/terms.json` with `fetch`, serve the folder over a local web server instead of double-clicking `index.html`.

With Python:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## GitHub Pages

The project is intentionally static. Once the MVP is merged:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose `main` and `/ (root)`.
4. Save.

No build process is required.

## Next milestones

- Source citations and provenance for individual terms
- Dedicated term detail pages
- Related-term relationships
- Emerging-term lifecycle
- AI-language timeline
- Submission workflow
- Editorial review status
- Automated candidate-term discovery with human approval

## License

Code is available under the MIT License. Dictionary content may need a separate content license before accepting external contributions.
