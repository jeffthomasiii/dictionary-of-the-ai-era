# AI Transparency

## Why AILex is vibe coded

AILex did not begin as a vibe-coding experiment. The dictionary came first.

The project began as a personal attempt to catalog the new language emerging around artificial intelligence. After the idea had already grown from a term list into a searchable dictionary with provenance research, another thought changed the development approach:

> **“Wouldn't it be cool if the Dictionary of the AI Era was actually built using AI?”**

That question became a second experiment inside the project.

AILex would not only document the language of the AI era. It would also explore what it looks like to build and maintain a serious public reference project through human-directed AI collaboration.

The full project origin is documented in [`docs/ORIGIN.md`](docs/ORIGIN.md).

## This project is intentionally AI-assisted

**AILex is intentionally and substantially developed through an AI-assisted, vibe-coding workflow.** AI is not only a subject documented by this project; it is materially involved in how the project itself is built.

Jeff Thomas III provides the project direction, product requirements, editorial judgment, testing, review, and final decisions. AI tools assist with activities that may include brainstorming, research support, architecture, code generation, debugging, documentation, definition drafting, copy editing, QA, and implementation.

The project does not present AI-assisted work as though it were created without AI involvement. The use of AI is intentional, material, and disclosed as part of the project's development process.

## What "vibe coded" means here

For AILex, vibe coding does **not** mean blindly accepting whatever an AI system produces. It describes a human-directed development process in which goals, constraints, desired behavior, and review feedback are expressed conversationally, AI systems generate or modify significant portions of implementation, and the human project owner evaluates, tests, redirects, accepts, or rejects the results.

A concise description of the development model is:

> **Vibe coded · Human-directed · AI-assisted · Human-reviewed**

The experiment is not whether AI can produce code at all. It is how far AI collaboration can responsibly support the full lifecycle of a public project while human judgment remains accountable for what ships and what the dictionary says.

## How AI may be used

AI tools may assist with:

- brainstorming features, terminology, and information architecture;
- drafting and revising HTML, CSS, JavaScript, JSON, documentation, and configuration;
- architecture and implementation planning;
- debugging and regression investigation;
- researching candidate terminology and identifying possible sources;
- drafting plain-English definitions and usage examples;
- organizing provenance, related concepts, and metadata;
- reviewing consistency, accessibility, maintainability, and documentation drift;
- preparing validation logic, release notes, contribution guidance, and QA plans.

Different AI products or models may be used over time. The principles matter more than preserving one permanent toolchain.

## What remains human-controlled

Human review and decision-making remain responsible for:

- project purpose, scope, priorities, and product direction;
- editorial policy and inclusion criteria;
- accepting, revising, deferring, or rejecting candidate terms;
- approving published definitions and examples;
- evaluating source credibility and whether evidence supports a claim;
- choosing attribution language such as coined, introduced, formalized, or popularized;
- determining categories and status;
- reviewing UX and design decisions;
- testing and approving software behavior;
- deciding whether AI-generated implementation is acceptable;
- merge, release, and publication decisions.

Human review is a control in the workflow, not a decorative disclaimer added after AI output is produced.

## AI research is assistance, not authority

AI-generated research, summaries, definitions, citations, and historical claims must not be treated as authoritative merely because an AI system produced them. Claims that depend on external evidence should be verified against appropriate sources before publication.

The editorial workflow is conceptually:

```text
Candidate term discovered
        ↓
AI-assisted research and drafting
        ↓
Source verification
        ↓
Human editorial review
        ↓
Accept, revise, defer, or reject
        ↓
Published dictionary entry
```

AI may help discover, compare, organize, and prepare material. It does not independently decide what becomes part of the dictionary.

## Validation is part of the experiment

AI-assisted development can produce useful work quickly, but it can also produce regressions, incorrect assumptions, malformed data, stale documentation, or browser-specific behavior that looks correct in code and fails in use.

AILex has already encountered examples such as:

- mobile navigation that required redesign after real testing;
- acronym pronunciations that browser speech engines guessed incorrectly;
- staging-data mistakes caught before publication by validation;
- documentation that became inaccurate as the product evolved quickly.

The goal is not to present the AI-assisted process as frictionless. Testing, validation, spot checking, correction, and revision are part of the development model.

When practical, repeatable validation should be added around high-risk or high-volume changes, particularly corpus/provenance parity, relationship integrity, generated term pages, metadata, and shared behavior.

## Why open source matters to the experiment

AILex is intended to remain open source.

Open source makes the dictionary inspectable, but it also makes the experiment inspectable. The public repository exposes the code, editorial datasets, standards, documentation, changes, fixes, and contribution history rather than asking people to trust a description of how the project was made.

Outside contributions are welcome whether they involve code, term research, sources, corrections, pronunciation, accessibility testing, design, QA, or documentation. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Tools and workflow may change

This document describes the development and editorial principles rather than attempting to maintain a forensic log of every prompt, conversation, model version, or generated line of code.

When a particular AI tool or workflow materially changes the project's methodology, risk profile, editorial process, or architecture, that change should be documented where it is useful to contributors and maintainers.

## Why disclose this

A project documenting the language of the AI era should be transparent about its own relationship with AI.

The goal is neither to minimize AI involvement nor to imply that AI independently authored or governs the project. The goal is to make the division of labor visible, learn from the process in public, and preserve human accountability for what AILex ultimately publishes and ships.
