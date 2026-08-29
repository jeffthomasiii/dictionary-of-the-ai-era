# EpochLex Named-Entity Expansion Backlog

This backlog tracks the first wave of organizations, products, model families, and model lines to research and add under the taxonomy established in `docs/TAXONOMY.md`.

It is a planning document, not evidence for dictionary claims. Each published entry still requires claim-specific research, provenance, human review, and the normal publication surfaces required by `CONTRIBUTING.md`.

## Priority 1 — Core distinctions readers routinely encounter

- OpenAI — `organization`
- ChatGPT — `product`
- GPT — `model-family`
- Anthropic — `organization`
- Claude — `product`
- Google — `organization`
- Gemini — `product`
- Meta — `organization`
- Llama — `model-family`
- Microsoft — `organization`
- Microsoft Copilot — `product`
- GitHub — `organization`
- GitHub Copilot — `product`
- Copilot — existing generic `term`; preserve and explicitly distinguish from named products

## Priority 2 — Major model lines and additional organizations/products

- Claude Opus — `model-family`
- Claude Sonnet — `model-family`
- Claude Haiku — `model-family`
- xAI — `organization`
- Grok — `product`
- Mistral AI — `organization`
- Mistral — `model-family`
- DeepSeek — `organization`

## DeepSeek naming note

`DeepSeek` is used publicly as the organization name and as the consumer-facing brand for its web/app experience, while released models use more specific names such as DeepSeek-R1, DeepSeek-V3, and DeepSeek-V4. Research should determine whether EpochLex needs a separate product entry or whether the organization entry plus significant model-family/model entries gives readers clearer value.

Do not create two indistinguishable entries both titled simply `DeepSeek`.

## Version policy

Do not add every released model version automatically. Specific versioned entries should be proposed only when they independently satisfy EpochLex's distinct-reader-value standard. Routine releases should normally be represented in the history/provenance of the appropriate model-family or product entry.

## Research sequence

For each candidate:

1. establish the durable identity of the entry and its `entryType`;
2. identify real-world usage and reader value;
3. prefer first-party sources for naming, launch, technical definition, and release claims;
4. distinguish product identity from the model family or model that powers it;
5. draft a plain-language definition that explains rather than promotes;
6. create the matching provenance record with claim-specific source descriptions;
7. add related-term targets without inventing typed relationship semantics;
8. create/update the dedicated term page, sitemap, search surfaces, pronunciation behavior, and validation requirements.

## Current research notes

Initial first-party verification supports several important distinctions:

- OpenAI introduced ChatGPT as a conversational product in November 2022; current ChatGPT releases can use models from the GPT family, so ChatGPT and GPT should not be treated as synonyms.
- Anthropic uses Claude as the broader assistant/model brand and has maintained Opus, Sonnet, and Haiku as recognizable model lines across multiple generations.
- Google uses Gemini both as a consumer-facing AI brand and for a continuing family of models, so the entry should clearly explain that dual usage.
- Meta's current branding is `Llama`; the original 2023 release was styled `LLaMA`, short for Large Language Model Meta AI. The modern canonical entry title should therefore be `Llama`, with `LLaMA` retained as an alias/historical styling.
- The existing generic EpochLex entry `Copilot` should remain separate from `Microsoft Copilot` and `GitHub Copilot`.
- Mistral AI publishes multiple model lines under the Mistral name; the generic model-family entry should avoid implying that `Mistral` identifies one permanent model version.
- DeepSeek publishes named model lines such as DeepSeek-R1, DeepSeek-V3, and DeepSeek-V4; the organization/product/model distinction needs to be explicit before publication.
