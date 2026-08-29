# EpochLex Provenance & Sourcing Standard

EpochLex is intended to document not only what AI-era terms mean, but also where those meanings come from and how confidently their histories can be described.

This standard governs the research layer stored separately from the core dictionary entries in `data/provenance.json`.

## Core principle

A source that supports a definition does not automatically establish a term's origin.

EpochLex separates:

- **Meaning:** evidence supporting what a term means.
- **Origin:** evidence about who introduced, coined, formalized, or popularized a term.
- **First known use:** the earliest use EpochLex can responsibly document. This may remain unknown.
- **History:** dated events that help explain how a term entered or changed within AI-era usage.
- **Related terms:** editorially useful connections to other EpochLex entries.
- **Research status:** whether the provenance review for an entry is still pending or has received an initial human-reviewed research pass.

## Research statuses

### `pending`

The term is published in EpochLex, but its provenance record has not yet received a dedicated sourcing review. Empty provenance fields must not be interpreted as claims that no origin or history exists.

### `researched`

The provenance record has received an initial human-reviewed research pass with sources sufficient to support the claims currently recorded. This status does not mean research is permanently complete.

Future statuses may include `needs-review`, `contested`, and `revised` if the editorial workflow requires them.

## Source types

Each source is classified by its relationship to the claim it supports.

- **Primary:** original paper, announcement, specification, post, documentation, transcript, or other first-party material.
- **Secondary:** reporting, analysis, historical discussion, or commentary based on primary evidence.
- **Reference:** dictionary, encyclopedia, standards reference, or similar reference work.

Primary sources are preferred for origin, first-use, technical-definition, and release-date claims when they are available.

## Source object

```json
{
  "id": "anthropic-mcp-2024",
  "type": "primary",
  "publisher": "Anthropic",
  "title": "Introducing the Model Context Protocol",
  "published": "2024-11-25",
  "url": "https://www.anthropic.com/news/model-context-protocol",
  "supports": ["origin", "definition", "history"]
}
```

The `supports` array identifies the claims for which the source was selected. A source should not be treated as evidence for unrelated fields simply because it appears in the record.

## Origin language

Origin claims must distinguish among different kinds of evidence:

- **coined by** — use only when evidence supports that a person or organization introduced the term itself;
- **introduced by** — appropriate when a source publicly launches or names a new technical concept or standard;
- **formalized by** — appropriate when existing language or a known phenomenon is given a rigorous research formulation;
- **popularized by** — appropriate when evidence shows meaningful spread but not necessarily invention;
- **associated with** — useful when attribution is real but stronger origin wording is not justified.

When the evidence is uncertain, the prose should say so.

## First-known-use rules

`firstKnownUse` should only be populated when EpochLex has evidence for a reasonably defensible earliest documented use within the meaning being described.

It is acceptable and preferable to use `null` when:

- the term predates modern AI and its true first use is outside the project's current research scope;
- multiple earlier uses may exist;
- the available source establishes importance but not priority;
- the term evolved gradually rather than appearing in a single naming event.

A date may use `year`, `month`, or `day` precision. The `precision` value should reflect the evidence actually available.

## History entries

History is not intended to become a complete chronology. Add events only when they materially help readers understand the term's emergence, formalization, adoption, change in meaning, or entry into broader usage.

Each history event contains:

```json
{
  "date": "2024-11-25",
  "event": "Anthropic publicly introduced MCP."
}
```

## AI-assisted research

AI may help discover candidate sources, compare terminology, organize evidence, and draft provenance notes. AI-generated claims are never themselves sources.

Before publication of a researched provenance record, a human reviewer should verify that:

1. the cited source exists and is accessible;
2. the source actually supports the claim assigned to it;
3. origin wording is no stronger than the evidence permits;
4. dates are represented at an appropriate level of precision;
5. quotations, if ever used, comply with copyright and attribution requirements;
6. disagreements or uncertain histories are represented rather than flattened into false certainty.

## Relationship to dedicated term pages

`data/provenance.json` is intentionally separate from `data/terms.json` during this phase. The core dictionary remains lightweight while the research model develops.

Future dedicated term pages can combine both datasets to display definition, pronunciation, source citations, origin, history, related terms, research status, and review dates without forcing every field into the current browse interface.
