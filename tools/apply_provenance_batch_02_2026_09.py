#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
RECORDS={
'natural-language-processing':{
'researchStatus':'researched',
'origin':'Natural language processing grew out of earlier work in machine translation, computational linguistics, information retrieval, and artificial intelligence rather than from a single established coinage. In modern usage, NLP refers to computational methods for analyzing, understanding, and generating human language in text or speech. The current research pass does not establish a defensible first use of the exact phrase “natural language processing.”',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'ibm-nlp-overview','type':'reference','publisher':'IBM','title':'What Is NLP (Natural Language Processing)?','published':None,'url':'https://www.ibm.com/think/topics/natural-language-processing','supports':['definition','usage']},
{'id':'sparck-jones-nlp-history','type':'secondary','publisher':'Association for Computational Linguistics archive','title':'Natural language processing: a historical review','published':None,'url':'https://aclanthology.org/www.mt-archive.info/Zampolli-1994-Sparck-Jones.pdf','supports':['history','usage']}
]},
'tokenization':{
'researchStatus':'researched',
'origin':'Tokenization is a general text-processing concept that predates modern large language models. In current language-model systems, it is the process of converting input into discrete tokens that a model can process. Modern tokenization often uses subword units rather than whole words, helping systems represent rare and previously unseen forms efficiently. The current evidence does not support assigning the general term to one inventor.',
'firstKnownUse':None,
'history':[{'date':'2016','event':'Sennrich, Haddow, and Birch published influential work applying byte-pair encoding to subword segmentation for neural machine translation, helping establish subword tokenization as a practical default in modern NLP systems.'}],
'sources':[
{'id':'google-ml-tokenizer-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary','published':None,'url':'https://developers.google.com/machine-learning/glossary','supports':['definition','usage']},
{'id':'sennrich-subword-2016','type':'primary','publisher':'Association for Computational Linguistics','title':'Neural Machine Translation of Rare Words with Subword Units','published':'2016','url':'https://aclanthology.org/P16-1162/','supports':['history','usage','technical-definition']}
]},
'ground-truth':{
'researchStatus':'researched',
'origin':'“Ground truth” predates machine learning and is used across scientific and engineering fields for observations or reference information treated as the closest available representation of reality. In machine learning it is the reference outcome or label against which predictions are trained or evaluated. The term does not imply that the reference data is infallible, and the current research pass does not assign it a single AI-era origin.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-ground-truth-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary — ground truth','published':None,'url':'https://developers.google.com/machine-learning/glossary','supports':['definition','usage','limitations']},
{'id':'google-data-quality-ground-truth','type':'reference','publisher':'Google for Developers','title':'Data quality and interpretation','published':None,'url':'https://developers.google.com/machine-learning/guides/data-traps/quality','supports':['definition','limitations','usage']}
]},
'sampling':{
'researchStatus':'researched',
'origin':'Sampling is a long-established statistical and computational concept rather than a generative-AI coinage. In generative models, sampling refers to selecting a next token or other output from a probability distribution rather than always choosing the single highest-probability option. Parameters such as temperature and top-p alter how that sampling distribution is used. The current evidence does not establish a single origin for the AI usage.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-genai-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary: Generative AI','published':None,'url':'https://developers.google.com/machine-learning/glossary/generative','supports':['definition','usage']},
{'id':'google-ml-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary','published':None,'url':'https://developers.google.com/machine-learning/glossary','supports':['definition','usage']}
]},
'loss-function':{
'researchStatus':'researched',
'origin':'Loss functions come from a broader mathematical and statistical tradition of optimization and estimation rather than from one machine-learning coinage. In machine learning, a loss function computes a numerical measure of prediction error or model performance that training procedures can minimize. Different tasks use different loss functions, and the current research pass does not attempt to assign the general concept to a single origin.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-loss-function-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary — loss function','published':None,'url':'https://developers.google.com/machine-learning/glossary','supports':['definition','usage','technical-definition']}
]},
'gradient-descent':{
'researchStatus':'researched',
'origin':'Gradient descent is an optimization method with roots that predate modern machine learning. In ML training, it updates model parameters in the direction that reduces a loss function, using gradients to determine how changes in parameters affect loss. EpochLex does not claim a machine-learning-era coinage or first use for the term.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-gradient-descent-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary — gradient descent','published':None,'url':'https://developers.google.com/machine-learning/glossary/fundamentals','supports':['definition','usage','technical-definition']}
]},
'backpropagation':{
'researchStatus':'researched',
'origin':'The mathematics underlying reverse-mode differentiation and multilayer-network training predates the modern deep-learning era, so EpochLex does not claim that backpropagation was invented in 1986. Rumelhart, Hinton, and Williams nevertheless provided a landmark 1986 demonstration and popularization of back-propagation for learning internal representations in multilayer neural networks.',
'firstKnownUse':None,
'history':[{'date':'1986-10-09','event':'Nature published Rumelhart, Hinton, and Williams’s “Learning representations by back-propagating errors,” a landmark paper that helped popularize backpropagation for training multilayer neural networks.'}],
'sources':[
{'id':'rumelhart-hinton-williams-1986','type':'primary','publisher':'Nature','title':'Learning representations by back-propagating errors','published':'1986-10-09','url':'https://www.nature.com/articles/323533a0','supports':['definition','history','usage']},
{'id':'google-backprop-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary: ML Fundamentals','published':None,'url':'https://developers.google.com/machine-learning/glossary/fundamentals','supports':['definition','usage','technical-definition']}
]},
'overfitting':{
'researchStatus':'researched',
'origin':'Overfitting is an established statistics and machine-learning concept rather than a recent AI term. It describes a model fitting the training data so closely that performance fails to generalize to new data. The concept has a long prehistory in statistical modeling, and the current research pass does not establish a defensible first use of the exact term.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-overfitting-course','type':'reference','publisher':'Google for Developers','title':'Overfitting','published':None,'url':'https://developers.google.com/machine-learning/crash-course/overfitting/overfitting','supports':['definition','usage','limitations']},
{'id':'google-overfitting-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary — overfitting','published':None,'url':'https://developers.google.com/machine-learning/glossary','supports':['definition','usage']}
]},
'underfitting':{
'researchStatus':'researched',
'origin':'Underfitting is the complementary model-fitting concept to overfitting. It describes a model that has not captured enough of the structure or complexity of its training data to make good predictions even on that data, and therefore also tends to perform poorly on new data. The current research pass does not establish a single origin or first known use for the term.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-underfitting-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary — underfitting','published':None,'url':'https://developers.google.com/machine-learning/glossary/fundamentals','supports':['definition','usage','limitations']},
{'id':'google-overfitting-course','type':'reference','publisher':'Google for Developers','title':'Overfitting','published':None,'url':'https://developers.google.com/machine-learning/crash-course/overfitting/overfitting','supports':['definition','usage']}
]},
'unsupervised-learning':{
'researchStatus':'researched',
'origin':'Unsupervised learning is an established machine-learning category rather than a modern generative-AI coinage. It refers to methods that learn patterns, structure, or representations from data without task labels supplied as target answers. Clustering and dimensionality-reduction methods are common examples. The current research pass does not establish a defensible first use of the exact phrase.',
'firstKnownUse':None,
'history':[],
'sources':[
{'id':'google-unsupervised-glossary','type':'reference','publisher':'Google for Developers','title':'Machine Learning Glossary: ML Fundamentals','published':None,'url':'https://developers.google.com/machine-learning/glossary/fundamentals','supports':['definition','usage']},
{'id':'sklearn-unsupervised','type':'reference','publisher':'scikit-learn','title':'Unsupervised learning: seeking representations of the data','published':None,'url':'https://scikit-learn.org/stable/tutorial/statistical_inference/unsupervised_learning.html','supports':['definition','usage','examples']}
]}
}
pp=R/'data/provenance.json'
prov=json.loads(pp.read_text())
for slug,record in RECORDS.items():
    assert slug in prov, slug
    assert prov[slug].get('researchStatus')=='pending', (slug,prov[slug].get('researchStatus'))
    record['relatedTerms']=prov[slug].get('relatedTerms',[])
    prov[slug]=record
pp.write_text(json.dumps(prov,indent=2,ensure_ascii=False)+'\n')
terms=json.loads((R/'data/terms.json').read_text())
published={t['slug'] for t in terms}
assert set(prov)==published
for slug,p in prov.items():
    for rel in p.get('relatedTerms',[]):
        assert rel in published,(slug,rel)
researched=sum(p.get('researchStatus')=='researched' for p in prov.values())
pending=sum(p.get('researchStatus')=='pending' for p in prov.values())
assert len(terms)==365
assert researched==142, researched
assert pending==223, pending
for slug in RECORDS:
    assert prov[slug]['researchStatus']=='researched'
    assert prov[slug]['sources']
    for src in prov[slug]['sources']:
        assert src.get('supports'),(slug,src)
# update roadmap counts
rp=R/'docs/ROADMAP.md'; road=rp.read_text()
road=road.replace('132 researched provenance records and 233 pending provenance records','142 researched provenance records and 223 pending provenance records')
rp.write_text(road)
# update review queue progress and add completed batch section before Wave 1
qp=R/'docs/PROVENANCE-REVIEW-QUEUE-2026-09.md'; q=qp.read_text()
q=q.replace('including **132 researched** provenance records and **233 pending** records after provenance Batch 01.', 'including **142 researched** provenance records and **223 pending** records after provenance Batch 02.')
q=q.replace('Provenance Batch 01 completed 10 of the 61 Wave 1 records, leaving **51 Wave 1 reviews** to reach that milestone.', 'Provenance Batches 01–02 completed 20 of the 61 Wave 1 records, leaving **41 Wave 1 reviews** to reach that milestone.')
marker='## Wave 1 — Majority milestone (61)'
section='''## Provenance Batch 02 — completed September 8, 2026\n\nThis batch concentrated on foundational machine-learning and language-processing concepts. All ten records completed the initial human-reviewed provenance pass and now use `researchStatus: "researched"`.\n\n1. **Natural Language Processing**\n2. **Tokenization**\n3. **Ground Truth**\n4. **Sampling**\n5. **Loss Function**\n6. **Gradient Descent**\n7. **Backpropagation**\n8. **Overfitting**\n9. **Underfitting**\n10. **Unsupervised Learning**\n\n'''
assert marker in q
q=q.replace(marker,section+marker,1)
qp.write_text(q)
print(json.dumps({'published':len(terms),'researched':researched,'pending':pending,'batch':list(RECORDS)},indent=2))
