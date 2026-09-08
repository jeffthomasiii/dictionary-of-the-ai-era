# EpochLex Corpus Audit — September 2026

This audit applies the editorial model established on September 8, 2026: a dictionary entry may be publishable before its dedicated provenance review is complete. The four labels below are **planning dispositions for this audit**, not new permanent editorial lifecycle states.

## Audit rules

- **Publish** — documented usage and distinct reader value are strong enough to draft a human-reviewed core dictionary entry now; provenance may remain `pending`.
- **Alias** — the phrase is useful for discovery but does not currently add enough distinct reader value for a separate page.
- **Research Further** — plausible candidate, but boundaries, durability, evidence, or relationship to existing entries still need work.
- **Exclude or Observe** — too generic, too overlapping, too volatile, or insufficiently useful as a separate entry today; retain only when future usage may change the decision.

Any candidate in `CORPUS-CANDIDATES.md` that is not explicitly listed as Publish, Alias, or Exclude/Observe below is classified **Research Further** by default. That makes the full inventory classified without pretending that hundreds of unresolved candidates have received a deeper research pass.

## Publish — Batch A (published in this change)

### Artificial Intelligence

**Why publish:** The broad field of creating machine-based systems that can perform tasks associated with human intelligence, such as perception, learning, reasoning, language use, decision-making, or goal-directed action.

**Usage evidence:**
- [NIST AI glossary](https://csrc.nist.gov/glossary/term/artificial_intelligence)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Ground Truth

**Why publish:** The reference information treated as the correct or verified answer when training, testing, or evaluating an AI or machine-learning system, even though the reference itself can contain measurement, labeling, or judgment errors.

**Usage evidence:**
- [Google Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)
- [IBM: Ground truth](https://www.ibm.com/think/topics/ground-truth)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Hybrid Search

**Why publish:** A search approach that combines two or more retrieval methods—commonly keyword or full-text search with vector or semantic search—and merges their results into one ranked set.

**Usage evidence:**
- [Elastic hybrid search documentation](https://www.elastic.co/docs/solutions/search/hybrid-search)
- [Microsoft Azure AI Search hybrid search overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Natural Language Processing

**Why publish:** A field of artificial intelligence and computer science focused on enabling computers to analyze, understand, generate, and otherwise work with human language in text or speech.

**Usage evidence:**
- [IBM: What is NLP?](https://www.ibm.com/think/topics/natural-language-processing)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Open-Weight Model

**Why publish:** An AI model whose trained weights are made available for others to download and run. Open weights do not by themselves establish that the training data, source code, development process, or license satisfies a broader definition of open-source AI.

**Usage evidence:**
- [OpenAI open-weight models overview](https://help.openai.com/en/articles/11870455-openai-open-weight-models)
- [OpenAI gpt-oss model card](https://openai.com/index/gpt-oss-model-card/)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Responsible AI

**Why publish:** An approach to designing, developing, deploying, and governing AI with explicit attention to trustworthiness and societal impacts such as fairness, safety, privacy, transparency, accountability, and human oversight.

**Usage evidence:**
- [NIST trustworthy and responsible AI glossary](https://www.nist.gov/publications/language-trustworthy-ai-depth-glossary-terms)
- [Microsoft Responsible AI](https://www.microsoft.com/en/ai/responsible-ai)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Tokenization

**Why publish:** The process of converting text or other input into tokens that a model can represent and process, often by splitting text into words, subwords, characters, bytes, or other learned units and mapping them to token IDs.

**Usage evidence:**
- [Hugging Face tokenization pipeline](https://huggingface.co/docs/tokenizers/main/pipeline)
- [Hugging Face tokenization algorithms](https://huggingface.co/docs/transformers/main/tokenizer_summary)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

### Workslop

**Why publish:** Low-effort AI-generated work that appears polished but lacks the context, substance, or judgment needed to be useful, shifting cleanup or thinking work onto the recipient.

**Usage evidence:**
- [BetterUp Labs / Stanford Social Media Lab workslop research](https://www.betterup.com/workslop)
- [Harvard Business Review, Why People Create AI Workslop](https://hbr.org/2026/01/why-people-create-ai-workslop-and-how-to-stop-it)

**Provenance state:** `pending` — the entry is useful as a dictionary definition now; origin/first-known-use/history research remains open.

## Publish — Batch B (published September 8, 2026)

### AI Literacy

**Why publish:** The knowledge and skills needed to understand, use, evaluate, and make informed decisions about artificial intelligence, including awareness of its capabilities, limitations, and risks.

**Usage evidence:** [European Commission: AI talent, skills and literacy](https://digital-strategy.ec.europa.eu/en/policies/ai-talent-skills-and-literacy)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Indirect Prompt Injection

**Why publish:** A prompt-injection attack in which malicious or conflicting instructions reach an AI system through external content such as a webpage, document, message, or retrieved data rather than directly from the user.

**Usage evidence:** [OWASP GenAI Security Project: LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Data Poisoning

**Why publish:** An attack in which an adversary manipulates or inserts data used for training or adaptation so the resulting AI model learns unwanted behavior, loses performance, or develops a hidden vulnerability.

**Usage evidence:** [NIST: Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/glossary/term/data_poisoning)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Model Card

**Why publish:** A structured document that accompanies an AI or machine-learning model and describes information such as its intended uses, evaluation results, performance characteristics, limitations, and relevant context for responsible use.

**Usage evidence:** [Google Research: Model Cards for Model Reporting](https://research.google/pubs/model-cards-for-model-reporting/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### System Card

**Why publish:** A document published about an AI system or major model release that summarizes evaluations, identified risks, safety measures, limitations, and other information relevant to understanding how the system was assessed and deployed.

**Usage evidence:** [OpenAI: GPT-5.5 System Card](https://openai.com/index/gpt-5-5-system-card/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Agentic Workflow

**Why publish:** A multi-step AI workflow that uses agentic behavior such as model-directed decisions, tool use, routing, iteration, or delegation to move a task toward a goal.

**Usage evidence:** [Anthropic: Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Agent Loop

**Why publish:** A recurring cycle in which an AI agent observes its current state or results, decides what to do next, takes an action or uses a tool, evaluates the outcome, and repeats until it reaches a stopping condition.

**Usage evidence:** [Anthropic: Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### AI Companion

**Why publish:** An AI system, often conversational, designed or used for ongoing social interaction, companionship, emotional support, or a simulated interpersonal relationship.

**Usage evidence:** [Stanford University: AI companions may worsen loneliness for vulnerable users](https://news.stanford.edu/stories/2026/08/ai-companions-chatbots-loneliness-research)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Human-AI Collaboration

**Why publish:** A way of working in which people and AI systems contribute to a shared task or goal, with each providing capabilities, information, judgment, or actions that shape the combined result.

**Usage evidence:** [NIST: Economic Research and Analysis of the National Need for Technology Infrastructure to Support the Internet of Things (IoT)](https://nvlpubs.nist.gov/nistpubs/gcr/2025/NIST.GCR.25-059.pdf)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Sampling

**Why publish:** A generation method in which an AI model selects among possible next tokens according to a probability distribution rather than always choosing only the single highest-probability option.

**Usage evidence:** [Hugging Face: How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Publish — Batch C (published September 8, 2026)

### Top-p

**Why publish:** A sampling method that limits the next-token choices to the smallest set of likely tokens whose cumulative probability reaches a chosen threshold p, then samples from that set.

**Usage evidence:** [Hugging Face: How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Speech-to-Text

**Why publish:** An AI speech-recognition capability that converts spoken audio into written text or a text transcription.

**Usage evidence:** [Google Cloud: Cloud Speech-to-Text documentation](https://docs.cloud.google.com/speech-to-text/docs)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Text-to-Speech

**Why publish:** An AI speech-synthesis capability that converts written text into spoken audio, often using generated voices.

**Usage evidence:** [Google Cloud: Cloud Text-to-Speech documentation](https://docs.cloud.google.com/text-to-speech/docs)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Text-to-Video

**Why publish:** A generative AI task or model capability that creates video from a text prompt or description.

**Usage evidence:** [Hugging Face: Text-to-Video](https://huggingface.co/tasks/text-to-video)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Loss Function

**Why publish:** A mathematical function that measures how far a model’s predictions are from desired or reference outcomes, producing a loss value that training commonly seeks to minimize.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Gradient Descent

**Why publish:** An optimization method that iteratively adjusts model parameters in directions that reduce a loss function.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Backpropagation

**Why publish:** The algorithm used in neural-network training to calculate how changes in model parameters affect loss, allowing gradients to be propagated backward through the network so the parameters can be updated.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Overfitting

**Why publish:** A training failure in which a model fits its training data so closely that it performs poorly on new or unseen data.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Underfitting

**Why publish:** A training failure in which a model does not capture enough of the structure or complexity in the training data to make useful predictions.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Unsupervised Learning

**Why publish:** A machine-learning approach that trains on data without supplied target labels in order to discover patterns, structure, groupings, or useful representations.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Publish — Batch D (published September 8, 2026)

### Latent Space

**Why publish:** A learned representation space in which an AI or machine-learning model encodes features or concepts as numerical positions or directions, so items with related learned characteristics may be represented near one another.

**Usage evidence:** [Google for Developers: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### AI Assurance

**Why publish:** The practice of gathering and evaluating evidence that an AI system performs as intended within defined conditions and that relevant risks, trustworthiness properties, and safeguards have been assessed.

**Usage evidence:** [NIST: The Path to Consensus on Artificial Intelligence Assurance](https://www.nist.gov/publications/path-consensus-artificial-intelligence-assurance)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Subagent

**Why publish:** A specialized AI agent or agent-like worker delegated a narrower task by a primary agent or orchestration process, often with its own context, instructions, tools, or permissions.

**Usage evidence:** [Anthropic: Create custom subagents - Claude Code Docs](https://code.claude.com/docs/en/subagents)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Autonomous Agent

**Why publish:** An AI agent designed to pursue tasks or goals with a comparatively high degree of independent decision-making and action, requiring less step-by-step human direction than an assistant or tightly scripted workflow.

**Usage evidence:** [Microsoft: AI Agent FAQ: Definitions and Explanations](https://www.microsoft.com/en-us/microsoft-365-copilot/agents/ai-agents-faq)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### AI Fluency

**Why publish:** The practical ability to work with AI effectively, critically, responsibly, and safely, including knowing what to delegate, how to communicate with AI, how to evaluate its outputs, and when human judgment is required.

**Usage evidence:** [Anthropic: AI Fluency: The AI Fluency Framework](https://www.anthropic.com/ai-fluency/overview)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Publish — next qualified group

The previously qualified queue has now been published through Batches A–D. No additional candidates are prequalified for publication in this audit; future Publish promotions should come from fresh evidence-based review of the Research Further inventory.

## Alias

These should currently improve discovery through an existing entry rather than create a duplicate page:

- **Function Calling** → **Tool Calling**
- **Model Evaluation** → **Eval**
- **Few-Shot Prompting** → **Few-Shot**
- **Zero-Shot Prompting** → **Zero-Shot**
- **Chain-of-Thought Prompting** → **Chain-of-Thought**
- **Vector Embedding** → **Embedding**
- **Vector Store** → **Vector Database**
- **Retrieval-Augmented Generation** → **RAG**
- **Knowledge Distillation** → **Distillation**
- **Re-ranking** → **Reranking**
- **Model Parameters** → **Parameters**
- **Weights** → **Model Weights**
- **Training Dataset** → **Training Data**
- **System Message** → **System Prompt**
- **Developer Message** → **Developer Prompt**
- **User Message** → **User Prompt**
- **Model-as-a-Judge** → **LLM-as-a-Judge**
- **LLM Judge** → **LLM-as-a-Judge**
- **AI Jailbreak** → **Jailbreak**
- **LLM Jailbreak** → **Jailbreak**
- **Jailbreaking** → **Jailbreak**
- **AI Red Teaming** → **Red Teaming**
- **Prompt Injection Attack** → **Prompt Injection**
- **Artificial Neural Network** → **Neural Network**
- **ANN** → **Neural Network**
- **Supervised Machine Learning** → **Supervised Learning**
- **Low-Rank Adaptation** → **LoRA**
- **Parameter-Efficient Fine-Tuning** → **PEFT**
- **One-Shot Prompting** → **One-Shot**

## Exclude or Observe

These are not recommended as separate entries now. Some are generic business phrases; others are unstable culture labels, narrow subtypes, or phrases whose reader value is not yet distinct enough. Observation does not mean permanent rejection.

- AI Boom
- AI Bubble
- AI Gold Rush
- AI Race
- AI Hype
- AI Hype Cycle
- AI Arms Race
- AI Delusion
- AI Psychosis
- AI Girlfriend/Boyfriend
- AI Friend
- AI Therapist
- AI Employee
- Synthetic Employee
- AI Clone
- AI Twin
- Digital Clone
- AI-Enabled
- AI-Assisted
- AI-First
- AI Adoption
- AI Transformation
- AI Upskilling
- AI Reskilling
- AI Workforce
- AI Exceptionalism
- AI Maximalist
- AI Booster
- Decelerationism
- AI Skeptic
- AI Skepticism
- AI Optimism
- AI Anxiety
- AI Fatigue
- Model Roulette
- Model Hopping
- Cyborg Workflow
- Vibe Debugging

## Research Further

All remaining unpublished candidates in `CORPUS-CANDIDATES.md`, including the newly added September 2026 expansion pool, are classified **Research Further** unless later promoted. This is intentionally conservative: candidate status records possible reader value, while publication requires actual evidence and human editorial judgment.

### Highest-priority research clusters

1. **Agent and agentic systems:** AI Memory, Browser Use, Subagent, Agent Skills, Agentic Commerce, Agent Observability, agent permissions/authorization, and MCP-era interaction concepts.
2. **Safety and governance:** AI Literacy, Indirect Prompt Injection, Data Poisoning, AI Assurance, Frontier Model, High-Risk AI, AI safety cases, and deployment safeguards.
3. **Evaluation:** Model Card, System Card, faithfulness/groundedness, calibration, benchmark contamination, agent evaluation, and long-context evaluation.
4. **Local/open deployment:** Local AI, open-source/open-model distinctions, NPUs, AI PCs, edge inference, model runtimes, and quantized deployment.
5. **Reasoning and post-training:** reasoning effort, inference-time scaling, verifiable rewards, DPO/GRPO/RLVR-adjacent terminology, and reward/specification failure modes.
6. **Retrieval:** hybrid and agentic retrieval, query routing, rerankers, retrieval fusion, RRF, and RAG evaluation.

## Expansion result

This audit has now published 33 candidates across Batches A, B, C, and D and added 172 new research candidates. The candidate inventory is intentionally broader than the publication queue; the goal is useful coverage without treating every AI-adjacent phrase as a dictionary entry.

## Follow-up

- Close or update candidate issues whose outcome is now established (for example, Function Calling → Tool Calling alias).
- Promote the next Publish group in coherent batches while leaving provenance `pending` where the core definition is ready but historical research is not.
- Keep Alias mappings discoverable in canonical term records when they are adopted.
- Revisit Exclude/Observe terms only when new evidence shows durable, distinct usage.
