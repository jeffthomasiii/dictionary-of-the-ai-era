# EpochLex Contributor Prompt Templates

These prompt templates are baseline starting points for people using AI assistance while contributing to EpochLex. They are intended to help contributors provide useful context, respect existing project decisions, and produce work that is easier to review.

They are **not mandatory workflows**, and they are not an exhaustive catalog of contribution types. Adapt them to the task and to the AI tool you use.

## Before using a template

Read [`CONTRIBUTING.md`](../../CONTRIBUTING.md) and the project document relevant to your change. Depending on the task, that may include:

- [`docs/ARCHITECTURE.md`](../ARCHITECTURE.md) for technical boundaries;
- [`docs/ROADMAP.md`](../ROADMAP.md) for current priorities;
- [`PROVENANCE.md`](../../PROVENANCE.md) for terminology research and sourcing;
- [`DESIGN.md`](../../DESIGN.md) for interface and interaction guidance;
- [`BRAND.md`](../../BRAND.md) for naming and identity;
- [`AI-TRANSPARENCY.md`](../../AI-TRANSPARENCY.md) for AI-assisted contribution expectations.

When possible, give the AI assistant access to the repository or paste the relevant files, issue, discussion, or documentation into the prompt.

## Shared principle

All templates follow the same baseline:

> Use the EpochLex repository and provided project documentation as the source of truth. Preserve established decisions and working functionality. Do not infer or manufacture EpochLex requirements that are not documented. If the task exposes an unresolved project decision, identify it rather than silently choosing a standard. Clearly distinguish existing behavior, proposed changes, and open questions.

AI output should be reviewed by a human contributor. AI output is not evidence for factual, historical, terminology, origin, usage, or attribution claims.

## Templates

### Code

- [`code/implement-feature.md`](code/implement-feature.md) — implement a defined feature or enhancement.
- [`code/fix-bug.md`](code/fix-bug.md) — investigate and correct a reproducible problem.
- [`code/review-code.md`](code/review-code.md) — review a proposed code change without rewriting unrelated functionality.

### Design

- [`design/design-ui.md`](design/design-ui.md) — propose or implement an interface change within the existing EpochLex system.
- [`design/review-ui.md`](design/review-ui.md) — evaluate an interface for usability, consistency, responsive behavior, and documented design constraints.

### Research

- [`research/research-ai-term.md`](research/research-ai-term.md) — research terminology, usage, provenance, and supporting evidence without treating research as automatic approval for publication.
- [`research/research-product-decision.md`](research/research-product-decision.md) — investigate technical or product options before EpochLex adopts a new approach.

### Documentation

- [`documentation/write-documentation.md`](documentation/write-documentation.md) — draft or update repository or public-facing documentation from established project facts.
- [`documentation/review-documentation.md`](documentation/review-documentation.md) — review documentation for accuracy, clarity, stale claims, audience fit, and consistency with implementation.

## How to use a template

1. Open the template that best matches your task.
2. Replace the bracketed fields with the issue, task, files, constraints, and requested output.
3. Provide the relevant EpochLex documentation or repository context to the AI assistant.
4. Review the result against the repository and source material before submitting it.
5. Disclose material AI assistance in accordance with [`AI-TRANSPARENCY.md`](../../AI-TRANSPARENCY.md) and [`CONTRIBUTING.md`](../../CONTRIBUTING.md).

If none of these templates fits, use the shared principle above as a starting point rather than forcing a task into the wrong template.