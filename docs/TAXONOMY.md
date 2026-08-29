# EpochLex Taxonomy

EpochLex uses two complementary classification layers: **editorial categories** and **entry types**.

Editorial categories answer: **What area of AI-era language does this entry help a reader understand?**

Entry types answer: **What kind of thing is this entry?**

Keeping these dimensions separate prevents organizations, products, and model names from being forced into subject categories that do not accurately describe them.

## Editorial categories

EpochLex currently uses five reader-facing editorial categories:

1. **AI Culture & Slang** — language, expressions, memes, informal usage, and cultural terminology that emerge around AI.
2. **AI Ways of Working** — practices, workflows, methods, roles, and patterns for using or working with AI.
3. **AI Systems & Technical Concepts** — models, architectures, mechanisms, system concepts, technical capabilities, and implementation terminology.
4. **AI Risks, Safety & Governance** — terminology concerning harms, limitations, safety, policy, oversight, security, accountability, and governance.
5. **AI Organizations, Products & Models** — named organizations, AI products, model families, and individual models whose names provide meaningful context for understanding the AI era.

Entries may belong to more than one editorial category when doing so materially improves reader understanding.

The fifth category is not intended to turn EpochLex into a company directory, product catalog, or exhaustive model-release tracker. It provides a reader-facing home for named entities that meet the inclusion principle below.

## Entry types

Each published entry should identify one primary `entryType`.

Initial vocabulary:

- `term` — a general AI-era term, concept, practice, technique, acronym, or expression that is not primarily a named organization, product, model family, or individual model;
- `organization` — a named company, laboratory, nonprofit, research organization, or other organization materially associated with AI-era terminology;
- `product` — a named AI product, assistant, service, application, or branded AI experience;
- `model-family` — a named family or continuing line of related AI models;
- `model` — a specific named or versioned AI model that warrants its own reference entry.

`entryType` describes the entry itself. Editorial categories describe the subject areas through which readers may discover it. The two fields should not be treated as substitutes for one another.

## Named-entity inclusion principle

Named AI organizations, products, model families, and individual models may qualify for EpochLex when understanding the name provides meaningful context for understanding AI-era terminology, technology, history, or culture.

Inclusion is **not automatic** merely because an organization develops AI, a product uses AI, or a model has been released.

A named entity should still satisfy the general EpochLex inclusion baseline: it should have documented real-world usage and provide distinct reader value. A separate entry should not be created merely to produce exhaustive vendor or version coverage.

Factors that can support inclusion include:

- the name is commonly encountered in AI discussion, documentation, reporting, research, or everyday use;
- readers benefit from understanding the distinction between the organization, product, model family, and model;
- the entity has historical, technical, cultural, or terminology significance beyond a routine release identifier;
- the entry resolves a recurring ambiguity, naming collision, or relationship that would otherwise make AI-era terminology harder to understand.

A current example is **Copilot**. EpochLex already defines the generic AI-era use of *copilot* as an assistant that works alongside a person. **Microsoft Copilot** and **GitHub Copilot** are distinct named products and should therefore be represented separately rather than replacing or redefining the generic term.

Likewise, **ChatGPT** and **GPT** should remain distinguishable: ChatGPT is a named product, while GPT refers to the Generative Pre-trained Transformer name and OpenAI model lineage. Product names and the model families that power them should not be treated as interchangeable merely because they are closely associated.

## Model variants and release granularity

A model family does not require a separate EpochLex entry for every released version, size, tier, or dated snapshot.

Individual-model entries are appropriate when the specific model provides distinct reader value, for example because it is widely referenced by name, marks an important technical or historical change, introduces terminology that readers are likely to encounter independently, or cannot be adequately explained through the parent model-family entry.

Routine version churn should normally be documented in provenance/history or represented within the parent family entry rather than generating permanent dictionary entries automatically.

## Relationships

This taxonomy does not establish typed relationship semantics.

EpochLex may surface related entries such as an organization, its product, and an associated model family through the existing related-term system, but a related-term connection alone does not formally mean `developed by`, `owned by`, `powers`, `successor to`, or any other typed relationship unless the data model is later expanded to encode and source those claims explicitly.

## Initial named-entity expansion

The first planned expansion under this taxonomy includes entries covering the following organizations, products, and model families where research supports distinct reader value:

- OpenAI
- ChatGPT
- GPT
- Anthropic
- Claude
- Claude Opus
- Claude Sonnet
- Claude Haiku
- Google
- Gemini
- Meta
- Llama
- xAI
- Grok
- Mistral AI
- Mistral
- DeepSeek
- Microsoft
- Microsoft Copilot
- GitHub
- GitHub Copilot

Specific current model versions should be evaluated individually rather than automatically added as permanent entries.

## Editorial maintenance

Named product and model information can change quickly. Definitions should focus on durable identity and reader value rather than transient benchmark rankings, pricing, context-window sizes, or marketing claims unless those details are necessary to explain the term and are appropriately sourced.

Primary sources should be preferred for organization identity, naming events, model introductions, product releases, and technical definitions when available. Historical and contested claims should continue to follow `PROVENANCE.md`.
