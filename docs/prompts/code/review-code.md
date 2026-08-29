# Prompt Template: Review Code

Use this template to review a proposed EpochLex code change before it is merged.

## Prompt

Review the following EpochLex code change.

### Change to review

[Provide the diff, pull request, branch, commit, or changed files.]

### Intended outcome

[Describe what the change is supposed to accomplish or paste the relevant issue/requirement.]

### Relevant context

[Provide applicable architecture, design, editorial, QA, or contribution documentation.]

### Requested output

Provide a focused code review with findings prioritized by impact.

### EpochLex instructions

Use the repository, documented requirements, and intended outcome as the basis for the review. Do not review against standards that EpochLex has not adopted.

Look for concrete issues such as:

- behavior that does not satisfy the stated requirement;
- regressions to existing functionality;
- data integrity or schema problems;
- broken URLs or fallback content;
- accessibility or keyboard regressions;
- responsive/mobile regressions;
- duplicated sources of truth;
- unsafe assumptions about terminology or provenance data;
- maintainability problems introduced by the change;
- documentation that no longer matches implementation.

Do not treat personal style preferences as defects. Do not recommend unrelated refactors simply because you would structure the code differently.

For each finding, explain the observable risk, where it occurs, and what should be corrected. Clearly label recommendations that are optional improvements rather than defects.

If the change appears sound within the provided scope, say so and identify any validation you could not perform from the available material.