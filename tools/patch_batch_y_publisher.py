from pathlib import Path
p=Path('tools/apply_corpus_batch_y_2026_09.py')
s=p.read_text()
s=s.replace("if t and label in t.get('aliases',[]): cleanup.append(label)","if t and any(a.casefold()==label.casefold() for a in t.get('aliases',[])): cleanup.append(label)")
s=s.replace("for label in [b['term'] for b in B]+cleanup: text=re.sub", "candidate_labels=[('Flash Attention' if b['slug']=='flashattention' else b['term']) for b in B]\nfor label in candidate_labels+cleanup: text=re.sub")
p.write_text(s)
