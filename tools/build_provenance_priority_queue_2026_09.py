#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

R=Path(__file__).resolve().parents[1]
terms=json.loads((R/'data/terms.json').read_text())
prov=json.loads((R/'data/provenance.json').read_text())
by_slug={t['slug']:t for t in terms}
pending={s for s,p in prov.items() if p.get('researchStatus')=='pending'}
assert len(pending)==243, len(pending)

# Working prioritization only — not an editorial standard.
W1={
'Foundational model & AI concepts':[
'Artificial Intelligence','Natural Language Processing','Tokenization','Ground Truth','Open-Weight Model','Sampling','Loss Function','Gradient Descent','Backpropagation','Overfitting','Underfitting','Unsupervised Learning','Latent Space','Byte-Pair Encoding (BPE)','Autoregressive Model','Encoder','Decoder','Cross-Attention','Softmax','Logit','Perplexity','Multimodal Model','FlashAttention','Model Serving','Top-p'],
'Retrieval & RAG backbone':['Hybrid Search','BM25','HNSW','Dense Retrieval','Sparse Retrieval','Cross-Encoder','Bi-Encoder','Reranker','Retrieval Pipeline','RAG Pipeline'],
'Agents & protocols':['Agentic Workflow','Agent Loop','Autonomous Agent','AI Memory','Agent Skills','Browser Use','Agent Security','Agent Handoff','Agent Planning','Agent-to-Agent (A2A)'],
'Governance, safety & trust':['Responsible AI','AI Assurance','High-Risk AI','AI Safety Case','Frontier AI','General-Purpose AI','AI Act','Human Oversight','AI Accountability','Trustworthy AI'],
'EpochLex differentiators & practical AI':['AI Literacy','Workslop','Local AI','On-Device AI','Local Inference','AI Companion']
}
wave1_names=[n for g in W1.values() for n in g]
assert len(wave1_names)==61, len(wave1_names)
name_to_slug={t['term'].casefold():t['slug'] for t in terms}
missing=[n for n in wave1_names if n.casefold() not in name_to_slug]
assert not missing, missing
wave1_slugs={name_to_slug[n.casefold()] for n in wave1_names}
not_pending=[by_slug[s]['term'] for s in wave1_slugs if s not in pending]
assert not not_pending, not_pending

first10=['Artificial Intelligence','Workslop','AI Literacy','Responsible AI','Agentic Workflow','AI Memory','Local AI','Hybrid Search','Open-Weight Model','Agent-to-Agent (A2A)']
assert all(name_to_slug[n.casefold()] in wave1_slugs for n in first10)

# Relationship centrality is used only to order items within a wave.
inbound=Counter()
for p in prov.values():
    for rel in p.get('relatedTerms',[]): inbound[rel]+=1

def degree(slug): return inbound[slug]+len(prov[slug].get('relatedTerms',[]))
def cats(slug): return by_slug[slug].get('categories',[])
def term(slug): return by_slug[slug]['term']

def wave_for(slug):
    if slug in wave1_slugs: return 1
    n=term(slug).casefold()
    c=' '.join(cats(slug)).casefold()
    fast_words=('mcp','agent','security','risk','governance','oversight','compliance','regulation','policy','incident','approval','permission','systemic','prohibited','accountability','audit','safety')
    if any(w in n for w in fast_words) or 'risks, safety & governance' in c:
        return 2
    return 3

waves={1:[],2:[],3:[]}
for s in pending: waves[wave_for(s)].append(s)
for w in waves: waves[w].sort(key=lambda s:(-degree(s),term(s).casefold()))
assert sum(map(len,waves.values()))==243
assert len(waves[1])==61

lines=[]
lines += ['# EpochLex Pending Provenance Review Queue — September 2026','',
'**Status:** Working prioritization for the current provenance-consolidation phase. This is an operational planning document, not a permanent editorial standard or lifecycle taxonomy.','',
'## Why this queue exists','',
'EpochLex currently has **365 published entries**, including **122 researched** provenance records and **243 pending** records. The current corpus-growth pause shifts attention from bulk publication to deeper provenance review. The first milestone is to complete 61 pending records, which would move the corpus to **183 researched / 182 pending** without adding new entries.','',
'The queue prioritizes four practical considerations: broad reader importance, value to EpochLex’s identity and differentiation, volatility or likelihood of meaning changing quickly, and the value of documenting provenance/history rather than leaving a useful definition without its research layer. These considerations guide this working queue only; they do not change `PROVENANCE.md` or `CONTRIBUTING.md`.','',
'## Review waves','',
'- **Wave 1 — Majority milestone (61):** highest-priority mix of foundational concepts, EpochLex differentiators, fast-moving agent/protocol terms, and governance/safety anchors. Completing this wave crosses the majority-researched milestone.','- **Wave 2 — Time-sensitive and governance/security:** remaining fast-moving protocols, agent concepts, security, regulation, oversight, and governance entries where current sourcing matters especially strongly.','- **Wave 3 — Technical and workflow backbone:** all other pending systems, retrieval, evaluation, deployment, and ways-of-working concepts. These remain important, but the current evidence suggests they are generally less time-sensitive than Wave 2.','',
'Within Waves 2–3, relationship centrality in the current published corpus is used only as a practical ordering aid; it is not a measure of editorial importance.','',
'## First provenance research batch — 10 entries','',
'This first batch deliberately mixes foundational, differentiating, practical, and fast-moving concepts so the workflow can be tested across several kinds of provenance research before scaling to the rest of Wave 1.','']
for i,n in enumerate(first10,1): lines.append(f'{i}. **{n}**')
lines += ['','## Wave 1 — Majority milestone (61)','']
for group,names in W1.items():
    lines += [f'### {group} ({len(names)})','']
    for n in names:
        s=name_to_slug[n.casefold()]
        lines.append(f'- **{n}** — relationship links: {degree(s)}')
    lines.append('')

for w,title in [(2,'Wave 2 — Time-sensitive and governance/security'),(3,'Wave 3 — Technical and workflow backbone')]:
    lines += [f'## {title} ({len(waves[w])})','']
    for s in waves[w]:
        cs=', '.join(cats(s)) or 'Uncategorized'
        lines.append(f'- **{term(s)}** — {cs}; relationship links: {degree(s)}')
    lines.append('')

lines += ['## Working review sequence','',
'1. Complete the first 10-entry research batch and verify that the provenance-review workflow is producing useful, appropriately cautious records.','2. Continue through the rest of Wave 1 until EpochLex reaches at least **183 researched / 182 pending**.','3. Reassess the queue after the majority milestone rather than assuming the remaining order is permanent.','4. Continue accepting candidate terminology, but do not resume systematic bulk publication unless an entry is important enough to interrupt the consolidation phase.','5. After substantial consolidation, reassess whether a roughly two-thirds-researched corpus is the appropriate point to reopen broader publication work.','',
'## Research completion rule','',
'A record moves from `pending` to `researched` only after the initial human-reviewed provenance pass required by `PROVENANCE.md`. Unknown origin or first-known-use information may remain unresolved; `null` is preferable to invented precision. Meaning evidence, origin evidence, first-known use, history, and related-term judgments remain distinct claims.','']

out='\n'.join(lines)+'\n'
(R/'docs/PROVENANCE-REVIEW-QUEUE-2026-09.md').write_text(out)
print(json.dumps({'pending':len(pending),'wave1':len(waves[1]),'wave2':len(waves[2]),'wave3':len(waves[3]),'first_batch':first10},indent=2))
