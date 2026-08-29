# Prompt Template: Implement a Feature

Use this template when a feature or enhancement has already been defined well enough to implement.

## Prompt

Help me implement the following change in EpochLex.

### Task

[Describe the feature or enhancement.]

### Relevant context

[Paste or reference the issue, requirement, discussion, file paths, or documentation that defines the change.]

### Constraints

[List known constraints, or write "None provided."]

### Requested output

[Describe whether you want an implementation plan, code changes, tests/validation, review notes, or a combination.]

### EpochLex instructions

Use the EpochLex repository and provided project documentation as the source of truth. Inspect the existing implementation before proposing or making changes.

Preserve established decisions, architecture, data structures, URLs, accessibility behavior, responsive behavior, and unrelated working functionality unless the task explicitly requires changing them.

Do not infer or manufacture EpochLex requirements that are not documented. If the requested feature depends on an unresolved product, editorial, design, or technical decision, identify that dependency before silently choosing a standard.

Keep the implementation scoped to the requested change. Avoid opportunistic refactors or unrelated feature additions.

When proposing the implementation:

1. summarize the existing behavior relevant to the task;
2. identify the files and components that need to change;
3. distinguish documented requirements from your recommendations;
4. implement the smallest coherent change that satisfies the task;
5. identify validation appropriate to the affected functionality;
6. report assumptions, unresolved questions, and any behavior intentionally left unchanged.

Follow `CONTRIBUTING.md`, `docs/ARCHITECTURE.md`, and other relevant EpochLex documentation. If your proposal conflicts with existing documentation or implementation, call out the conflict rather than silently overriding it.