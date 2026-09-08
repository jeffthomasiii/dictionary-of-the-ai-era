#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D='2026-09-08'
RECORDS={
'artificial-intelligence':{
'researchStatus':'researched',
'origin':'The term “artificial intelligence” is documented in the August 31, 1955 proposal for the Dartmouth Summer Research Project on Artificial Intelligence, authored by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon. The proposal framed a proposed 1956 study around the conjecture that aspects of learning and intelligence could be described precisely enough for machines to simulate them. EpochLex treats that proposal as the earliest documented use established by the current research pass, while avoiding a stronger claim about any undocumented earlier spoken use.',
'firstKnownUse':{'date':'1955-08-31','precision':'day','note':'The dated Dartmouth proposal uses “artificial intelligence” in the title and body and is the earliest documented use established in the current EpochLex research pass.'},
'history':[{'date':'1955-08-31','event':'McCarthy, Minsky, Rochester, and Shannon dated their proposal for the Dartmouth Summer Research Project on Artificial Intelligence.'},{'date':'1956','event':'The Dartmouth summer research project convened and became a foundational event in the development of artificial intelligence as a research field.'}],
'sources':[{'id':'dartmouth-ai-proposal-1955','type':'primary','publisher':'AI Magazine / Association for the Advancement of Artificial Intelligence','title':'A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence, August 31, 1955','published':'1955-08-31','url':'https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904/0','supports':['origin','firstKnownUse','history','definition']},{'id':'dartmouth-ai-history','type':'primary','publisher':'Dartmouth College','title':'Artificial Intelligence (AI) Coined at Dartmouth','published':None,'url':'https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth','supports':['history','origin','usage']},{'id':'nist-ai-glossary','type':'reference','publisher':'National Institute of Standards and Technology','title':'artificial intelligence - Glossary','published':None,'url':'https://csrc.nist.gov/glossary/term/artificial_intelligence','supports':['definition','usage']}]
},
'workslop':{
'researchStatus':'researched',
'origin':'“Workslop” entered documented workplace-AI discourse in 2025 as a label for AI-generated work that appears polished but shifts substantive thinking, verification, or cleanup onto the recipient. BetterUp Labs and the Stanford Social Media Lab published research using the term in September 2025. The current evidence establishes that research as an important early documented use and popularization point, but does not establish that the researchers were the first people ever to coin the word.',
'firstKnownUse':None,
'history':[{'date':'2025-09-22','event':'Harvard Business Review published research by BetterUp Labs and Stanford Social Media Lab researchers describing AI-generated “workslop” and its productivity costs.'},{'date':'2026-01-16','event':'A follow-up Harvard Business Review article examined why people create workslop and how organizations can reduce it, showing continued uptake of the term in workplace-AI discourse.'}],
'sources':[{'id':'betterup-workslop-2025','type':'primary','publisher':'BetterUp Labs / Stanford Social Media Lab','title':'Workslop: The Hidden Cost of AI-Generated Busywork','published':'2025','url':'https://www.betterup.com/workslop','supports':['definition','usage','history']},{'id':'hbr-workslop-2025','type':'primary','publisher':'Harvard Business Review','title':'AI-Generated “Workslop” Is Destroying Productivity','published':'2025-09-22','url':'https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity','supports':['definition','usage','history']},{'id':'hbr-workslop-2026','type':'primary','publisher':'Harvard Business Review','title':'Why People Create AI “Workslop”—and How to Stop It','published':'2026-01-16','url':'https://hbr.org/2026/01/why-people-create-ai-workslop-and-how-to-stop-it','supports':['usage','history']}]
},
'ai-literacy':{
'researchStatus':'researched',
'origin':'“AI literacy” does not have a single coinage established by the current evidence. The concept developed from broader digital, data, and computational-literacy traditions and has been used in education and policy to describe the knowledge, skills, values, and judgment needed to understand and use AI responsibly. UNESCO’s 2024 AI competency framework gave the concept a prominent global education-policy framing while explicitly extending beyond narrow tool-use literacy.',
'firstKnownUse':None,
'history':[{'date':'2024-08-08','event':'UNESCO published its AI Competency Framework for Students, defining a global competency framework spanning a human-centred mindset, ethics of AI, AI techniques and applications, and AI system design.'}],
'sources':[{'id':'unesco-ai-competency-students-2024','type':'primary','publisher':'UNESCO','title':'AI competency framework for students','published':'2024-08-08','url':'https://www.unesco.org/en/articles/ai-competency-framework-students','supports':['definition','usage','history']},{'id':'unesco-tvet-ai-literacy','type':'reference','publisher':'UNESCO-UNEVOC','title':'TVETipedia Glossary — AI literacy','published':None,'url':'https://connect.unevoc.unesco.org/home/TVETipedia%2BGlossary/lang%3De/show%3Dterm/term%3DAI%2Bliteracy','supports':['definition','usage']}]
},
'responsible-ai':{
'researchStatus':'researched',
'origin':'“Responsible AI” is a broad governance and development concept rather than a term with a single established inventor. It is used for approaches that aim to design, develop, deploy, and use AI in ways that account for safety, fairness, privacy, transparency, accountability, reliability, and other human and societal considerations. By the early 2020s, the phrase was embedded in major institutional frameworks and engineering practices.',
'firstKnownUse':None,
'history':[{'date':'2023-01-26','event':'NIST released AI RMF 1.0 to promote trustworthy and responsible development and use of AI systems through a voluntary risk-management framework.'},{'date':'2023-03-29','event':'NIST published The Language of Trustworthy AI, a glossary intended to support common understanding around trustworthy and responsible AI.'}],
'sources':[{'id':'nist-ai-rmf-2023','type':'primary','publisher':'National Institute of Standards and Technology','title':'Artificial Intelligence Risk Management Framework (AI RMF 1.0)','published':'2023-01-26','url':'https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10','supports':['definition','usage','history']},{'id':'nist-trustworthy-responsible-ai','type':'primary','publisher':'National Institute of Standards and Technology','title':'Trustworthy and responsible AI','published':None,'url':'https://www.nist.gov/trustworthy-and-responsible-ai','supports':['definition','usage']},{'id':'microsoft-responsible-ai','type':'primary','publisher':'Microsoft','title':'Responsible AI Principles and Approach','published':None,'url':'https://www.microsoft.com/en-us/ai/principles-and-approach','supports':['definition','usage']}]
},
'agentic-workflow':{
'researchStatus':'researched',
'origin':'“Agentic workflow” does not have a single coinage established by the current evidence. The phrase emerged as practitioners distinguished structured multi-step AI workflows from more autonomous agents. Anthropic’s 2024 engineering guidance formalized a closely related distinction between workflows, where LLMs and tools follow predefined code paths, and agents, where the model dynamically directs tool use and process execution.',
'firstKnownUse':None,
'history':[{'date':'2024-12-19','event':'Anthropic published Building effective agents, distinguishing predefined workflows from more autonomous agent systems and documenting reusable workflow patterns such as routing, parallelization, and evaluator-optimizer loops.'}],
'sources':[{'id':'anthropic-building-effective-agents-2024','type':'primary','publisher':'Anthropic','title':'Building effective agents','published':'2024-12-19','url':'https://www.anthropic.com/engineering/building-effective-agents','supports':['definition','usage','history']},{'id':'anthropic-agent-guide-2026','type':'primary','publisher':'Anthropic','title':'Building Effective AI Agents: Architecture Patterns and Implementation Frameworks','published':'2026','url':'https://resources.anthropic.com/building-effective-ai-agents','supports':['definition','usage']}]
},
'ai-memory':{
'researchStatus':'researched',
'origin':'Memory as a computing and AI concept predates modern generative AI, and the current evidence does not support assigning “AI memory” to a single coinage. In contemporary agent and assistant systems, the phrase refers to mechanisms that retain and recall information across interactions so prior information can influence later behavior, personalization, continuity, or task performance.',
'firstKnownUse':None,
'history':[{'date':'2026-06-22','event':'Microsoft Security published guidance defining AI memory as the retention and recall of information across interactions and describing memory as both a capability and a security-sensitive persistent state.'}],
'sources':[{'id':'microsoft-guarding-ai-memory-2026','type':'primary','publisher':'Microsoft Security','title':'Guarding AI memory','published':'2026-06-22','url':'https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/','supports':['definition','usage','history','risk']}]
},
'local-ai':{
'researchStatus':'researched',
'origin':'“Local AI” is a descriptive deployment term rather than a coinage that the current evidence ties to one inventor. It refers to AI models or workloads executed on a user-controlled local device or localized infrastructure instead of relying entirely on a remote public-cloud service. Current usage commonly emphasizes privacy, lower latency, offline operation, cost control, and local access to data.',
'firstKnownUse':None,
'history':[{'date':'2025','event':'Intel and LLMWare documented enterprise local AI workflows that run inference on AI PCs or local servers and keep data inside the enterprise rather than sending it to the public cloud.'},{'date':'2026-06-09','event':'Intel published a technical overview explicitly describing local AI as running models directly on a device or within localized infrastructure instead of relying on cloud servers.'}],
'sources':[{'id':'intel-local-ai-2025','type':'primary','publisher':'Intel','title':'Local AI—No Code, More Secure with AI PCs and the Private Cloud','published':'2025','url':'https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-05/llmware-intel-solution-brief-local-ai-private-cloud.pdf','supports':['definition','usage','history']},{'id':'intel-local-ai-architecture-2026','type':'primary','publisher':'Intel','title':'Local AI and the Compute Architecture That Makes It Work','published':'2026-06-09','url':'https://community.intel.com/t5/Blogs/Tech-Innovation/Edge-5G/Local-AI-and-the-Compute-Architecture-That-Makes-It-Work/post/1750535','supports':['definition','usage','history']},{'id':'qualcomm-gpt4all-local-ai-2025','type':'primary','publisher':'Qualcomm','title':'Nomic GPT4ALL and Embeddings: Fast, local AI inference for devices powered by Snapdragon X Series','published':'2025-03-21','url':'https://www.qualcomm.com/developer/blog/2025/03/nomic-gpt4all-fast-local-ai-inference-for-snapdragon-x-series','supports':['usage']}]
},
'hybrid-search':{
'researchStatus':'researched',
'origin':'“Hybrid search” is an established information-retrieval label rather than a generative-AI coinage. In current AI and retrieval-augmented-generation usage, it commonly refers to combining lexical or full-text retrieval with semantic or vector retrieval and then combining the result signals or rankings. The current research pass does not establish a single first use of the phrase.',
'firstKnownUse':None,
'history':[],
'sources':[{'id':'microsoft-hybrid-search-2026','type':'primary','publisher':'Microsoft','title':'Hybrid Search Overview - Azure AI Search','published':'2026-08-31','url':'https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview','supports':['definition','usage','technical-definition']},{'id':'pinecone-hybrid-search','type':'primary','publisher':'Pinecone','title':'Hybrid search','published':None,'url':'https://docs.pinecone.io/guides/search/hybrid-search','supports':['definition','usage','technical-definition']}]
},
'open-weight-model':{
'researchStatus':'researched',
'origin':'“Open-weight model” is a descriptive openness label rather than a term with a single coinage established by the current evidence. It generally means that a trained model’s weights are publicly available for download or use, while other components needed for full reproducibility or open-source status—such as training data, training code, or complete development documentation—may remain unavailable. The term became especially important as the AI community distinguished open weights from the broader requirements of Open Source AI.',
'firstKnownUse':None,
'history':[{'date':'2025','event':'The Open Source Initiative published guidance explaining that access to trained weights alone does not necessarily make an AI system Open Source AI.'}],
'sources':[{'id':'osi-open-weights','type':'primary','publisher':'Open Source Initiative','title':'Open Weights: not quite what you’ve been told','published':'2025','url':'https://opensource.org/ai/open-weights','supports':['definition','usage','history']},{'id':'openai-open-weight-models','type':'primary','publisher':'OpenAI','title':'OpenAI open-weight models (gpt-oss)','published':None,'url':'https://help.openai.com/en/articles/11870455-openai-open-weight-models','supports':['definition','usage']}]
},
'agent-to-agent-a2a':{
'researchStatus':'researched',
'origin':'Google introduced the Agent2Agent (A2A) protocol on April 9, 2025 as an open protocol for interoperability among AI agents built by different vendors or frameworks. On June 23, 2025, Google transferred the specification, SDKs, and related tooling to a new Linux Foundation project for vendor-neutral stewardship.',
'firstKnownUse':{'date':'2025-04-09','precision':'day','note':'Google publicly announced the Agent2Agent (A2A) protocol on April 9, 2025.'},
'history':[{'date':'2025-04-09','event':'Google announced the Agent2Agent (A2A) protocol for communication and collaboration across heterogeneous AI-agent systems.'},{'date':'2025-06-23','event':'Google donated A2A to the Linux Foundation, which launched the Agent2Agent project for vendor-neutral governance.'},{'date':'2026-04-09','event':'The Linux Foundation reported that A2A had reached production-ready status with support from more than 150 organizations and adoption across major cloud platforms.'}],
'sources':[{'id':'google-a2a-launch-2025','type':'primary','publisher':'Google Developers Blog','title':'Announcing the Agent2Agent Protocol (A2A)','published':'2025-04-09','url':'https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/','supports':['origin','firstKnownUse','definition','history','usage']},{'id':'linux-foundation-a2a-2025','type':'primary','publisher':'Linux Foundation','title':'Linux Foundation Launches the Agent2Agent Protocol Project to Enable Secure, Intelligent Communication Between AI Agents','published':'2025-06-23','url':'https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents','supports':['origin','history','usage']},{'id':'a2a-spec-1-0','type':'primary','publisher':'Agent2Agent Project / Linux Foundation','title':'Agent2Agent (A2A) Protocol','published':'2026','url':'https://a2a-protocol.org/v1.0.0/','supports':['definition','technical-definition','usage']},{'id':'linux-foundation-a2a-year-one-2026','type':'primary','publisher':'Linux Foundation','title':'A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year','published':'2026-04-09','url':'https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year','supports':['history','usage']}]
}
}
pp=R/'data/provenance.json'; prov=json.loads(pp.read_text())
for slug,record in RECORDS.items():
    assert slug in prov, slug
    assert prov[slug].get('researchStatus')=='pending', (slug,prov[slug].get('researchStatus'))
    related=prov[slug].get('relatedTerms',[])
    record['relatedTerms']=related
    prov[slug]=record
pp.write_text(json.dumps(prov,ensure_ascii=False,indent=2)+'\n')

tp=R/'data/terms.json'; terms=json.loads(tp.read_text())
for t in terms:
    if t['slug'] in RECORDS: t['lastReviewed']=D
tp.write_text(json.dumps(terms,ensure_ascii=False,separators=(',',':'))+'\n')

rp=R/'docs/ROADMAP.md'; r=rp.read_text(); r=r.replace('- 122 researched provenance records and 243 pending provenance records in the current published corpus;','- 132 researched provenance records and 233 pending provenance records in the current published corpus;'); rp.write_text(r)

qp=R/'docs/PROVENANCE-REVIEW-QUEUE-2026-09.md'; q=qp.read_text(); q=q.replace('EpochLex currently has **365 published entries**, including **122 researched** provenance records and **243 pending** records.','EpochLex currently has **365 published entries**, including **132 researched** provenance records and **233 pending** records after provenance Batch 01.')
q=q.replace('The first milestone is to complete 61 pending records, which would move the corpus to **183 researched / 182 pending** without adding new entries.','The first milestone remains **183 researched / 182 pending** without adding new entries. Provenance Batch 01 completed 10 of the 61 Wave 1 records, leaving **51 Wave 1 reviews** to reach that milestone.')
q=q.replace('## First provenance research batch — 10 entries','## Provenance Batch 01 — completed September 8, 2026')
q=q.replace('This first batch deliberately mixes foundational, differentiating, practical, and fast-moving concepts so the workflow can be tested across several kinds of provenance research before scaling to the rest of Wave 1.','This first batch deliberately mixed foundational, differentiating, practical, and fast-moving concepts so the provenance workflow could be tested across several kinds of research. All ten records completed the initial human-reviewed provenance pass and now use `researchStatus: "researched"`.')
q=q.replace('1. Complete the first 10-entry research batch and verify that the provenance-review workflow is producing useful, appropriately cautious records.','1. **Completed:** Provenance Batch 01 reviewed the first 10 entries and validated the cautious, claim-specific research workflow.')
qp.write_text(q)

# Validation
terms=json.loads(tp.read_text()); prov=json.loads(pp.read_text()); slugs={t['slug'] for t in terms}
assert len(terms)==365
assert set(prov)==slugs
assert sum(1 for p in prov.values() if p.get('researchStatus')=='researched')==132
assert sum(1 for p in prov.values() if p.get('researchStatus')=='pending')==233
for slug in RECORDS:
    p=prov[slug]
    assert p['researchStatus']=='researched'
    assert p['sources']
    assert all(s.get('url') and s.get('supports') for s in p['sources'])
    for rel in p.get('relatedTerms',[]): assert rel in slugs,(slug,rel)
print(json.dumps({'published':365,'researched':132,'pending':233,'batch':list(RECORDS)},indent=2))
