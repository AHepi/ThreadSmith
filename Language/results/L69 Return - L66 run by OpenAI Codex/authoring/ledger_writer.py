"""Written by OpenAI Codex under L66. Write once; manual translation data only."""
from pathlib import Path
import json,re,hashlib,datetime
BASE=Path('/workspace/scratch/984d5d85cc67/work/L66_blind_corpus')
OUT=Path('/workspace/scratch/984d5d85cc67/return_L66')
AUTHOR='OpenAI Codex'
class Ledger:
 def __init__(self,p):
  self.p=p; self.source=(BASE/'corpus'/f'{p}.txt').read_text(); self.sentences=dict(re.findall(r'(?m)^(\d+)\. (.*)$',self.source)); self.rows={}; self.pl=[]; self.bin=[]; self.readings=[]; self.splits=[]; self.verbs=[]; self.whatifs=[]; self.rig2=False
 def add(self,id,s,text,code,mark='said',standing='CLAIMED',**kw):
  assert id not in self.rows
  self.rows[id]=dict(mark=mark,sentence=s,standing=standing,text=f'[{standing}] {text}',**kw)
  self.pl+=['',f'% {id} | {standing} | {mark} | sentence {s} | {text}',f'line({id}).']+[c.replace('$',f'line({id})') for c in ([code] if isinstance(code,str) else code)]
 def fact(self,id,s,text,term,mark='said',standing='CLAIMED',neg=False):
  self.add(id,s,text,f'{"denied" if neg else "holds"}({term}) :- $.',mark,standing)
 def thing(self,id,s,name,kind,standing='GIVEN',response='not_stated',mark='said'):
  self.add(id,s,f'{name} is a {kind}; response to a press {response.replace("_"," ")}',[f'kind({name}, {kind}) :- $.',f'body({name}, {response}) :- $.'],mark,standing)
 def b(self,s,words,reason): self.bin.append(dict(sentence=s,words=words,reason=reason))
 def r(self,s,open_,taken): self.readings.append(f'Sentence {s}. Open readings: {open_}. Chosen: {taken}.')
 def v(self,verb,s,why): self.verbs.append(dict(verb=verb,sentence=s,reason=why,has_shape=verb in {'throw','toss','hurl','push','pull','lean_on','hit','drop','let_go_of','open_fist_on','hold','close_fist_on'}))
 def finish(self):
  assert all(str(x['sentence']) in self.sentences for x in self.rows.values())
  coverage={str(x['sentence']) for x in self.rows.values()}|{str(x['sentence']) for x in self.bin}
  assert coverage==set(self.sentences),(self.p,coverage,set(self.sentences))
  counts={m:sum(x['mark']==m for x in self.rows.values()) for m in ['said','filled in','usual case']}; counts['sentences_losing_to_bin']=len({x['sentence'] for x in self.bin})
  meta=dict(paragraph=self.p,whose=f'{AUTHOR}, under L66, from the sealed corpus',rig='rig 1 - arguments',sentences=self.sentences,leftover=[f'Sentence {x["sentence"]}: “{x["words"]}” — {x["reason"]}' for x in self.bin],bin_entries=self.bin,whatifs=self.whatifs,lines=self.rows,author_note=f'Written by {AUTHOR}. Actual-ledger fixture. No answer-key access. Body predicates in rig 1 are inert unless a queried rule uses them.',readings=self.readings,words_split=self.splits,verb_inventory=self.verbs,counts=counts,source_sha256=hashlib.sha256(self.source.encode()).hexdigest(),events={},names={})
  md=[f'# {self.p} — blind translation',f'Written by {AUTHOR}, under L66, from the sealed corpus. Knowledge: read from this passage; chosen encodings are worked out. No checker findings used to revise it.',self.source,'## 1. The ledger','| Number | Standing | Content | Source mark | Sentence |','| --- | --- | --- | --- | --- |']
  md += [f'| {i} | {x["standing"]} | {x["text"].split("] ",1)[1].replace("|","/")} | {x["mark"]} | {x["sentence"]} |' for i,x in self.rows.items()]
  md+=['','## 2. The bin','\n\n'.join(meta['leftover']) or 'Nothing left in the bin.','## 3. Words I split','\n\n'.join(self.splits) or 'No word was split into two ledger senses.','## 4. Readings I chose','\n\n'.join(self.readings) or 'No additional lexical reading beyond the standing and source marks shown.','## 5. The count',f'Lines said: {counts["said"]}. Lines filled in: {counts["filled in"]}. Lines usual case: {counts["usual case"]}. Sentences that lost something to the bin: {counts["sentences_losing_to_bin"]}.','TRANSLATION COMPLETE.']
  files={OUT/'translations'/f'{self.p}_OpenAI_Codex_translation.md':'\n\n'.join(md[:4])+'\n'+ '\n'.join(md[4:])+'\n',OUT/'rigs/rig 1 - arguments'/f'ledger_{self.p}.json':json.dumps(meta,ensure_ascii=False,indent=2)+'\n',OUT/'rigs/rig 1 - arguments'/f'ledger_{self.p}.pl':f'% Written by {AUTHOR}, under L66. {self.p}.\n'+'\n'.join(self.pl)+'\n',OUT/'corpus'/f'{self.p}.txt':self.source}
  if self.rig2:
   m=dict(meta,rig='rig 2 - causes',author_note=f'Written by {AUTHOR}. Same translation, also submitted to rig 2. Facts without a named producer remain facts, not invented results.')
   files[OUT/'rigs/rig 2 - causes'/f'ledger_{self.p}.json']=json.dumps(m,ensure_ascii=False,indent=2)+'\n'
   files[OUT/'rigs/rig 2 - causes'/f'ledger_{self.p}.pl']=files[OUT/'rigs/rig 1 - arguments'/f'ledger_{self.p}.pl']
  for path,content in files.items():
   with path.open('x') as f:f.write(content)
  with (OUT/'evidence/translation_order.jsonl').open('a') as f:f.write(json.dumps(dict(author=AUTHOR,passage=self.p,completed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),translation_sha256=hashlib.sha256(files[OUT/'translations'/f'{self.p}_OpenAI_Codex_translation.md'].encode()).hexdigest()))+'\n')
  print(self.p,counts,'COMPLETE')
