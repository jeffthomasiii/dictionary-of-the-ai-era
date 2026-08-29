# Prompt Template: Research a Product or Technical Decision

Use this template when EpochLex needs evidence before choosing a new feature, dependency, architecture, workflow, or implementation approach.

## Prompt

Research the following product or technical decision for EpochLex.

### Decision to investigate

[State the question or choice.]

### Why it is being considered

[Describe the problem, opportunity, issue, or limitation prompting the research.]

### Known EpochLex constraints

[Provide relevant architecture, roadmap, design, editorial, hosting, licensing, maintenance, or other documented constraints.]

### Options already identified

[List known options, or write "None yet."]

### Requested output

[For example: comparison, recommendation, proof-of-concept plan, risks, or decision brief.]

### EpochLex instructions

Start by separating established EpochLex constraints from assumptions and preferences. Use the repository and project documentation as the source of truth for current behavior.

Research viable options without assuming that the most feature-rich or fashionable option is best. Consider the effect on the project's existing architecture, maintainability, accessibility, performance, data integrity, contributor experience, publishing model, and user experience where relevant.

For each serious option, identify:

- what it would solve;
- how it fits or conflicts with current EpochLex architecture;
- implementation complexity;
- new dependencies or operational requirements;
- migration or regression risk;
- maintenance implications;
- meaningful tradeoffs.

Do not describe a recommendation as an adopted EpochLex requirement. Clearly separate:

1. established current state;
2. research findings;
3. recommendation;
4. alternatives considered;
5. open questions requiring a project decision.

Prefer a focused recommendation that solves the stated problem over expanding the project scope simply because additional capabilities are available.