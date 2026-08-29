# Prompt Template: Review Documentation

Use this template to check EpochLex documentation against the repository, implementation, and intended audience.

## Prompt

Review the following EpochLex documentation.

### Documentation to review

[Provide the file, section, branch, diff, or draft.]

### Intended audience and purpose

[Describe who it is for and what it should accomplish.]

### Source material

[Provide relevant implementation, project documents, issues, PRs, or research.]

### Requested output

Provide a prioritized documentation review and, where useful, proposed corrections.

### EpochLex instructions

Review the documentation against the supplied sources and current repository rather than general assumptions about how an AI dictionary or open-source project should operate.

Check for:

- claims that are unsupported by the implementation or project documentation;
- stale future-state language for features that are already implemented;
- implemented behavior still described as merely planned;
- invented standards, governance, workflows, or capabilities;
- incorrect EpochLex naming or historical framing;
- broken or misleading internal links;
- public-facing documentation that exposes unnecessary repository mechanics;
- repository documentation that omits technical detail necessary for contributors;
- ambiguity between established decisions, proposals, and open questions;
- unnecessary promotional or exaggerated language.

Do not rewrite accurate documentation merely to impose a different writing style. Prioritize factual correctness, clarity, audience fit, and consistency with the project.

For each substantive finding, identify the problematic passage or claim, explain why it conflicts with the source of truth, and propose a correction. If the available sources do not resolve a question, mark it as unresolved rather than inventing an answer.