# Prompt Template: Fix a Bug

Use this template to investigate and correct a reproducible EpochLex problem.

## Prompt

Help me investigate and fix the following EpochLex bug.

### Problem

[Describe what is wrong.]

### Expected behavior

[Describe what should happen, citing an issue, documentation, or known prior behavior when available.]

### Reproduction information

[Steps, browser/device, URL, screenshots, console output, error text, affected term/page, or other useful evidence.]

### Relevant context

[Paste or reference relevant files, issue discussion, recent changes, or documentation.]

### Requested output

[For example: root-cause analysis + minimal fix + validation steps.]

### EpochLex instructions

Use the repository and provided project documentation as the source of truth. Reproduce or trace the problem from available evidence before changing code.

Do not assume that nearby code is incorrect merely because it could be written differently. Preserve unrelated working behavior and avoid broad refactors unless the root cause requires one.

Separate:

- observed behavior;
- confirmed root cause;
- hypotheses that still need validation;
- the proposed fix.

Make the smallest coherent correction that addresses the root cause. Check for regressions in functionality directly affected by the change, including relevant responsive, keyboard, accessibility, no-JavaScript fallback, data-integrity, or URL behavior where applicable.

Do not invent new EpochLex requirements while fixing the bug. If expected behavior is not actually established, identify that as an open product decision instead of presenting your preference as the correct fix.

At the end, report the files changed, why they changed, how the fix was validated, and any remaining uncertainty.