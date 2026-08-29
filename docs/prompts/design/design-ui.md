# Prompt Template: Design or Improve an EpochLex Interface

Use this template when proposing or implementing an interface, interaction, or visual change.

## Prompt

Help me design or improve the following EpochLex interface.

### Task

[Describe the screen, component, interaction, or design problem.]

### Relevant context

[Provide screenshots, current files, issue/discussion, user problem, or applicable documentation.]

### Constraints

[List known constraints, or write "None provided."]

### Requested output

[For example: design recommendation, implementation approach, mockup direction, CSS/HTML changes, or reviewable alternatives.]

### EpochLex instructions

Use the current EpochLex implementation, `DESIGN.md`, `BRAND.md`, and provided approved assets as the source of truth for established visual and interaction decisions.

Preserve the reference-first character of EpochLex and existing working behavior unless the task explicitly requires changing it. Account for light and dark themes, desktop/tablet/mobile behavior, keyboard access, visible focus, and meaning that does not depend on color alone where relevant to the component.

Do not invent a new brand system, design token system, component standard, semantic relationship, or accessibility requirement and describe it as an existing EpochLex rule. If the repository does not establish a needed design decision, identify the gap and present your recommendation as a proposal.

Before proposing changes:

1. describe the current interface and the specific problem being addressed;
2. identify applicable documented constraints;
3. preserve existing information architecture and data semantics unless change is part of the task;
4. explain the proposed design and why it addresses the stated problem;
5. identify effects on responsive, light/dark, keyboard, and accessibility behavior;
6. distinguish required changes from optional refinements.

Avoid redesigning unrelated parts of EpochLex simply to make the requested component match a new personal aesthetic.