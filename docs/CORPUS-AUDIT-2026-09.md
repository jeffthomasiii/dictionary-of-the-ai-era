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

## Research Further promotion pass 5 — Batch I (published September 8, 2026)

This batch is the fifth evidence-based promotion from **Research Further**. Promotion records an audit decision for these entries; it does not create a permanent lifecycle state or automatic promotion rule.

### Inference Server

**Why promote and publish:** Server software that loads one or more trained AI models and exposes an interface, often an API, for receiving requests and running model inference.

**Usage evidence:** [Hugging Face: Serve CLI](https://huggingface.co/docs/transformers/serve-cli/serving)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Model Serving

**Why promote and publish:** The deployment and operation of a trained AI model so applications or users can send inference requests and receive outputs, typically through managed endpoints or inference servers.

**Usage evidence:** [Hugging Face: Serve Models on Jobs](https://huggingface.co/docs/hub/jobs-serving)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### GGUF

**Why promote and publish:** A single-file model format used with GGML-compatible inference engines that stores model tensors together with standardized metadata and supports multiple quantized data types.

**Usage evidence:** [Hugging Face: GGUF](https://huggingface.co/docs/transformers/main/quantization/gguf)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### 4-Bit Quantization

**Why promote and publish:** A model-compression approach that represents model weights or other numerical values using 4-bit precision, substantially reducing memory requirements while potentially changing accuracy or performance.

**Usage evidence:** [Hugging Face: Bitsandbytes](https://huggingface.co/docs/transformers/main/quantization/bitsandbytes)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Safetensors

**Why promote and publish:** A tensor serialization format designed to store model weights and other tensors safely and efficiently without relying on executable pickle-based serialization.

**Usage evidence:** [Hugging Face: Safetensors](https://huggingface.co/docs/safetensors/index)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Reranker

**Why promote and publish:** A model or component that takes an existing set of retrieved candidates and reorders them according to their estimated relevance to a query or task.

**Usage evidence:** [Cohere: Cohere’s Rerank Model](https://docs.cohere.com/docs/rerank)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Safety Evaluation

**Why promote and publish:** The systematic testing of an AI model or system for safety-relevant behaviors, risks, safeguards, and failure modes under defined conditions or scenarios.

**Usage evidence:** [NIST: AI Metrology Center](https://airc.nist.gov/metrology/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Pass@k

**Why promote and publish:** An evaluation metric estimating whether at least one successful solution appears among k independently sampled model outputs for the same task, commonly used in code-generation evaluation.

**Usage evidence:** [OpenAI researchers: Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Group Relative Policy Optimization

**Why promote and publish:** A reinforcement-learning post-training method in which a model generates groups of candidate completions, receives rewards for them, and updates its policy using advantages computed relative to other completions in the group.

**Usage evidence:** [Hugging Face: GRPO Trainer](https://huggingface.co/docs/trl/grpo_trainer)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Model Registry

**Why promote and publish:** A managed catalog for recording model versions and associated metadata, evaluation information, lifecycle status, approvals, or deployment references so models can be governed and promoted through operational workflows.

**Usage evidence:** [AWS: Model Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Research Further promotion pass 4 — Batch H (published September 8, 2026)

This batch is the fourth evidence-based promotion from **Research Further**. Promotion records an audit decision for these entries; it does not create a permanent lifecycle state or automatic promotion rule.

### Agent Sandbox

**Why promote and publish:** An isolated or constrained execution environment that limits what an AI agent can access or change, reducing the potential impact of unsafe, unintended, or compromised actions.

**Usage evidence:** [Anthropic: Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Agent Permission

**Why promote and publish:** A configured rule or grant that determines which resources, tools, commands, data, or actions an AI agent is allowed to access or use.

**Usage evidence:** [Anthropic: How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/engineering/claude-code-auto-mode)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Tool Approval

**Why promote and publish:** A human or policy-controlled checkpoint that must authorize an AI system or agent before it invokes a particular tool or performs a tool-mediated action.

**Usage evidence:** [Anthropic: Getting Started with Custom Connectors Using Remote MCP](https://support.anthropic.com/en/articles/11175166-about-custom-integrations-using-remote-mcp)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### MCP Server

**Why promote and publish:** A server-side implementation of the Model Context Protocol that exposes tools, resources, prompts, or other supported capabilities for MCP clients to discover and use.

**Usage evidence:** [Model Context Protocol: MCP Server](https://java.sdk.modelcontextprotocol.io/latest/server/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### MCP Resource

**Why promote and publish:** A URI-identified item of data or context that an MCP server exposes for clients to discover or read, such as a file, schema, document, or application-specific resource.

**Usage evidence:** [Model Context Protocol: Resources](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### MCP Apps

**Why promote and publish:** An MCP extension that lets servers provide interactive user interfaces to host applications by linking UI resources with MCP tools and enabling communication between the embedded interface and the host.

**Usage evidence:** [Model Context Protocol: MCP Apps: Extending servers with interactive user interfaces](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### MCP Tasks

**Why promote and publish:** An MCP extension for representing and tracking longer-running server work through task handles and task lifecycle operations such as getting status, updating, or cancelling work.

**Usage evidence:** [Model Context Protocol: The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### On-Device AI

**Why promote and publish:** AI processing in which a model runs directly on an end-user device rather than sending each inference request to a remote cloud service.

**Usage evidence:** [Apple: Integrating on-device AI models in your app with Core AI](https://developer.apple.com/documentation/CoreAI/integrating-on-device-ai-models-in-your-app-with-core-ai)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### QLoRA

**Why promote and publish:** A parameter-efficient fine-tuning technique that keeps a pretrained model quantized, commonly at 4-bit precision, while training low-rank adapter weights instead of updating the full model.

**Usage evidence:** [Hugging Face: bitsandbytes](https://huggingface.co/docs/transformers/main/quantization/bitsandbytes)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Direct Preference Optimization

**Why promote and publish:** A post-training method that fine-tunes a language model directly on preferred and rejected response pairs without first training a separate explicit reward model.

**Usage evidence:** [Hugging Face: DPO Trainer](https://huggingface.co/docs/trl/dpo_trainer)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Research Further promotion pass 3 — Batch G (published September 8, 2026)

This batch is the third evidence-based promotion from **Research Further**. Promotion records an audit decision for these entries; it does not create a permanent lifecycle state or automatic promotion rule.

### Content Credentials

**Why promote and publish:** Cryptographically verifiable provenance information attached to or associated with digital content to record claims about its origin, edits, and processing history using the C2PA standard.

**Usage evidence:** [C2PA: Content Credentials: C2PA Technical Specification 2.4](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Context Caching

**Why promote and publish:** A technique for reusing computation associated with previously processed context so repeated or shared prompt prefixes do not have to be fully recomputed for every generation.

**Usage evidence:** [Hugging Face: Cache strategies](https://huggingface.co/docs/transformers/main/kv_cache)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### MCP Authorization

**Why promote and publish:** The authorization mechanisms used with Model Context Protocol connections to control whether an MCP client may access protected MCP servers or capabilities on behalf of a resource owner.

**Usage evidence:** [Model Context Protocol: The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### MCP Tool

**Why promote and publish:** A callable capability exposed by a Model Context Protocol server, described with a name and input schema and invoked by an MCP client through the protocol’s tool-calling methods.

**Usage evidence:** [Model Context Protocol: The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Grader

**Why promote and publish:** A rule, metric, program, or model used in an AI evaluation to score, label, compare, or otherwise judge a model or system output against defined criteria.

**Usage evidence:** [OpenAI: Graders](https://platform.openai.com/docs/api-reference/graders)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Long-Context Evaluation

**Why promote and publish:** Evaluation designed to measure how well a model uses, retrieves from, reasons over, or summarizes information across very long input contexts rather than merely accepting a large context window.

**Usage evidence:** [Stanford CRFM: HELM Long Context](https://crfm.stanford.edu/helm/long-context/latest/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Structured Output

**Why promote and publish:** Model-generated output constrained to follow a specified machine-readable structure or schema so downstream software can reliably parse and use it.

**Usage evidence:** [OpenAI: Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Speculative Decoding

**Why promote and publish:** An inference technique that speeds generation by having a faster helper produce candidate tokens that a larger model verifies in fewer expensive forward passes.

**Usage evidence:** [Hugging Face: Assisted decoding](https://huggingface.co/docs/transformers/main/assisted_decoding)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### KV Cache

**Why promote and publish:** A key-value cache that stores attention-layer key and value states for previously processed tokens so an autoregressive model can reuse them during later generation steps instead of recomputing them.

**Usage evidence:** [Hugging Face: Caching](https://huggingface.co/docs/transformers/cache_explanation)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### General-Purpose AI

**Why promote and publish:** In the EU AI Act context, AI with significant generality that can competently perform a wide range of distinct tasks and be integrated into varied downstream systems or applications; the Act separately defines general-purpose AI models and systems.

**Usage evidence:** [European Commission AI Act Service Desk: Guidelines on the scope of the obligations for general-purpose AI models](https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-07/guidelines_on_the_scope_of_the_obligations_for_generalpurpose_ai_models_established_by_regulation_1cx2atxgq79us4n3x8jfgyy1qlm_118340-3.pdf)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Research Further promotion pass 2 — Batch F (published September 8, 2026)

This batch is the second evidence-based promotion from **Research Further**. Promotion records an audit decision for these entries; it does not create a permanent lifecycle state or automatic promotion rule. **Frontier Model** is treated as an alias of **Frontier AI** rather than a separate entry in this pass.

### Agentic Commerce

**Why promote and publish:** Online commerce in which AI agents help discover, compare, select, or purchase products and services on behalf of a user, potentially carrying a transaction from expressed intent through checkout.

**Usage evidence:** [Stripe: Agentic commerce](https://docs.stripe.com/agentic-commerce)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Agent Evaluation

**Why promote and publish:** The systematic testing of an AI agent across tasks or scenarios using defined success criteria, repeated trials, graders, traces, or outcome checks to measure how well the agent behaves and completes work.

**Usage evidence:** [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Groundedness

**Why promote and publish:** An evaluation property describing whether a generated response is supported by the supplied or retrieved context rather than introducing claims that are not grounded in that context.

**Usage evidence:** [Microsoft Learn: Develop a RAG Solution on Azure - Large Language Model End-to-End Evaluation Phase](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-llm-evaluation-phase)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Benchmark Contamination

**Why promote and publish:** A condition that weakens an AI benchmark when a model has already been exposed to benchmark questions, answers, or closely related test material before evaluation, making the resulting score less trustworthy as a measure of unseen performance.

**Usage evidence:** [Google DeepMind: Piloting the world’s first double-blind AI evaluations](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Inference-Time Scaling

**Why promote and publish:** An approach to improving AI performance by allocating more computation during inference, such as allowing a reasoning model or agent to spend more effort, samples, or search steps on a task before producing a result.

**Usage evidence:** [OpenAI: BrowseComp: a benchmark for browsing agents](https://openai.com/index/browsecomp/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Edge Inference

**Why promote and publish:** Running a trained AI model to make predictions or generate outputs on computing infrastructure near the data source or end device rather than sending the workload to a distant centralized cloud service.

**Usage evidence:** [NVIDIA: Accelerating LLM and VLM Inference for Automotive and Robotics with NVIDIA TensorRT Edge-LLM](https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### RAG Evaluation

**Why promote and publish:** The evaluation of a retrieval-augmented generation system across retrieval and answer quality, using measures such as relevance, groundedness, completeness, correctness, retrieval quality, or end-to-end task performance.

**Usage evidence:** [Microsoft Learn: Develop a RAG Solution on Azure - Large Language Model End-to-End Evaluation Phase](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-llm-evaluation-phase)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Calibration

**Why promote and publish:** The degree to which a model’s predicted probabilities or confidence levels correspond to observed outcomes; a well-calibrated model’s stated confidence matches how often predictions at that confidence are actually correct.

**Usage evidence:** [scikit-learn: Probability calibration](https://scikit-learn.org/stable/modules/calibration.html)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### AI Safety Case

**Why promote and publish:** A structured argument, supported by evidence, that an AI system is acceptably safe within a specified training, deployment, or operating context.

**Usage evidence:** [UK AI Security Institute: Safety cases at AISI](https://www.aisi.gov.uk/blog/safety-cases-at-aisi)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Frontier AI

**Why promote and publish:** A relative term for highly capable general-purpose AI models at or near the leading edge of current capabilities. What counts as frontier AI changes as the state of the art advances, so the term does not imply a fixed capability threshold.

**Usage evidence:** [UK Department for Science, Innovation and Technology: A pro-innovation approach to AI regulation: government response to consultation](https://assets.publishing.service.gov.uk/media/65c1e41663a23d000dc8224f/a-pro-innovation-approach-to-ai-regulation-amended-governement-response-print-ready.pdf)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

## Research Further promotion pass 1 — Batch E (published September 8, 2026)

This batch is the first set promoted directly from **Research Further** after the original prequalified Publish queue was exhausted. Promotion reflects fresh evidence and reader value review; it does not create a new permanent editorial status or automatic promotion rule.

### Agent Skills

**Why promote and publish:** A packaging approach for giving AI agents reusable procedural knowledge through organized instructions, scripts, and resources that can be discovered and loaded when relevant to a task.

**Usage evidence:** [Anthropic: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Agent Observability

**Why promote and publish:** The methods and instrumentation used to inspect, monitor, trace, and evaluate the behavior and internal activity of AI agents, including model interactions, tool use, latency, errors, and execution paths.

**Usage evidence:** [Google Cloud: Agent observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### AI PC

**Why promote and publish:** A personal computer designed with dedicated hardware for running artificial-intelligence workloads locally, typically combining a CPU and GPU with a neural processing unit or other specialized AI accelerator.

**Usage evidence:** [Intel: What is an AI PC?](https://www.intel.com/content/www/us/en/support/articles/000099561/processors/intel-core-ultra-processors.html)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### NPU

**Why promote and publish:** A neural processing unit: a specialized processor or accelerator optimized for neural-network and other AI workloads, often designed to perform highly parallel AI computations efficiently and at relatively low power.

**Usage evidence:** [Microsoft: All about neural processing units (NPUs)](https://support.microsoft.com/en-us/windows/experience/compatibility/all-about-neural-processing-units-npus)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### High-Risk AI

**Why promote and publish:** A regulatory classification under the European Union AI Act for certain AI systems that meet specified product or use-case criteria and are therefore subject to enhanced requirements and obligations. The term does not simply mean any AI system that seems dangerous.

**Usage evidence:** [European Commission AI Act Service Desk: Article 6: Classification rules for high-risk AI systems](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Reasoning Effort

**Why promote and publish:** A configurable setting that controls how much reasoning computation a supported AI model uses before producing an answer, allowing developers or users to trade off response quality, latency, and token use.

**Usage evidence:** [OpenAI: Introducing GPT-5 for developers](https://openai.com/index/introducing-gpt-5-for-developers/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Reciprocal Rank Fusion

**Why promote and publish:** A rank-fusion method that combines multiple ranked result lists by assigning each result a score based on its reciprocal rank in each list and summing those contributions into one final ranking.

**Usage evidence:** [Elastic: Reciprocal rank fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Browser Use

**Why promote and publish:** An AI capability that lets a model or agent work with websites through a web browser by opening pages, reading content, navigating links or tabs, and taking permitted browser actions.

**Usage evidence:** [OpenAI: Using the built-in browser in the ChatGPT desktop app](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### AI Memory

**Why promote and publish:** Mechanisms that let an AI system retain, retrieve, or reuse information beyond the immediate turn so prior facts, preferences, events, or learned state can influence later interactions or agent behavior.

**Usage evidence:** [Microsoft Security: Guarding AI memory](https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

### Local AI

**Why promote and publish:** Running AI models and inference on a user-controlled device or local infrastructure rather than relying on a remote public-cloud AI service for the computation.

**Usage evidence:** [Microsoft Learn: Choose between cloud-based and local AI models](https://learn.microsoft.com/en-us/windows/ai/cloud-ai); [Intel: Local AI and the Compute Architecture That Makes It Work](https://community.intel.com/t5/Blogs/Tech-Innovation/Edge-5G/Local-AI-and-the-Compute-Architecture-That-Makes-It-Work/post/1750535)

**Provenance state:** `pending` — meaning/usage evidence is recorded; origin, first-known-use, and fuller history research remain open.

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

This audit has now published 83 candidates across Batches A–I and added 172 new research candidates. The candidate inventory is intentionally broader than the publication queue; the goal is useful coverage without treating every AI-adjacent phrase as a dictionary entry.

## Follow-up

- Close or update candidate issues whose outcome is now established (for example, Function Calling → Tool Calling alias).
- Promote the next Publish group in coherent batches while leaving provenance `pending` where the core definition is ready but historical research is not.
- Keep Alias mappings discoverable in canonical term records when they are adopted.
- Revisit Exclude/Observe terms only when new evidence shows durable, distinct usage.
