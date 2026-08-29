# Prompt Template: Write or Update Documentation

Use this template to create or revise EpochLex documentation from established project information.

## Prompt

Help me write or update the following EpochLex documentation.

### Document or section

[Name the file, page, or documentation topic.]

### Audience

[Readers, contributors, developers, researchers, maintainers, or another defined audience.]

### Purpose

[What should someone understand or be able to do after reading it?]

### Source material

[Provide repository files, implementation details, issue/PR discussion, research, or existing documentation that supports the content.]

### Requested output

[New Markdown, replacement section, targeted edits, etc.]

### EpochLex instructions

Ground the documentation in the supplied sources and current repository. Do not invent EpochLex features, history, standards, workflows, governance, maturity, adoption, or future commitments to make the document sound more complete.

Use EpochLex as the current project name. When relevant, preserve the distinction between EpochLex as a searchable AI terminology reference and a conventional static glossary.

Respect the repository's documentation boundary:

- public website documentation should primarily help readers understand and use EpochLex;
- repository documentation may address architecture, contribution work, detailed standards, development practices, roadmap, release mechanics, and the open-source AI experiment.

If implementation and documentation conflict, identify the discrepancy rather than silently choosing whichever version is easier to write.

Clearly distinguish:

- implemented/current behavior;
- historical context;
- planned or roadmap work;
- recommendations or proposals that have not been adopted.

Prefer clear, concrete language over promotional claims. Preserve useful existing detail unless the task explicitly calls for restructuring or shortening it.