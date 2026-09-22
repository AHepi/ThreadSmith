# Written by OpenAI Codex under L66. New files only; originals remain immutable.
from pathlib import Path
import json,hashlib,copy,re
R=Path('/workspace/scratch/984d5d85cc67/return_L66')
receipts=[]
def read(p):
 base=R/'rigs/rig 1 - arguments'/f'ledger_{p}'
 return json.loads(base.with_suffix('.json').read_text()),base.with_suffix('.pl').read_text()
def add(m,pl,id,s,text,clauses,mark='said',standing='CLAIMED'):
 m['lines'][id]=dict(mark=mark,sentence=s,standing=standing,text=f'[{standing}] {text}')
 return pl+f'\n% {id} | {standing} | {mark} | sentence {s} | {text}\nline({id}).\n'+ '\n'.join(x.replace('$',f'line({id})') for x in clauses)+'\n'
def finish(p,m,pl,why,rig2=False):
 stem=f'ledger_{p}_correction1'
 m['paragraph']=p+' correction 1';m['author_note']+=' Correction 1 by OpenAI Codex; original files and original runs remain beside this correction.';m['correction_reason']=why;m['corrects']=f'ledger_{p}.json'
 m['leftover']=[f'Sentence {x["sentence"]}: “{x["words"]}” — {x["reason"]}' for x in m['bin_entries']]
 counts={k:sum(l['mark']==k for l in m['lines'].values()) for k in ['said','filled in','usual case']};counts['sentences_losing_to_bin']=len(set(x['sentence'] for x in m['bin_entries']));m['counts']=counts
 pl='% Correction 1 written by OpenAI Codex under L66. Originals retained.\n'+pl
 data=json.dumps(m,ensure_ascii=False,indent=2)+'\n'
 md=[f'# {p} — blind translation, correction 1','Written by OpenAI Codex under L66. This is a new correction file; the original is unchanged.',f'Correction, worked out: {why}',(R/'corpus'/f'{p}.txt').read_text(),'## 1. The ledger','','| Number | Standing | Content | Source mark | Sentence |','| --- | --- | --- | --- | --- |']
 md += [f'| {id} | {v["standing"]} | {v["text"].split("] ",1)[1]} | {v["mark"]} | {v["sentence"]} |' for id,v in m['lines'].items()]
 md += ['','## 2. The bin','','\n\n'.join(m['leftover']) or 'Nothing in the bin.','','## 3. Words I split','','\n\n'.join(m['words_split']) or 'No split.','','## 4. Readings I chose','','\n\n'.join(m['readings']),'','## 5. The count','',f'Lines said: {counts["said"]}. Lines filled in: {counts["filled in"]}. Lines usual case: {counts["usual case"]}. Sentences that lost something to the bin: {counts["sentences_losing_to_bin"]}.','','TRANSLATION COMPLETE.']
 files={R/'rigs/rig 1 - arguments'/f'{stem}.json':data,R/'rigs/rig 1 - arguments'/f'{stem}.pl':pl,R/'translations'/f'{p}_OpenAI_Codex_translation_correction1.md':'\n'.join(md)+'\n'}
 if rig2:
  two=copy.deepcopy(m);two['rig']='rig 2 - causes'
  files[R/'rigs/rig 2 - causes'/f'{stem}.json']=json.dumps(two,ensure_ascii=False,indent=2)+'\n';files[R/'rigs/rig 2 - causes'/f'{stem}.pl']=pl
 for path,text in files.items():
  with path.open('x') as f:f.write(text)
 receipts.append(dict(author='OpenAI Codex',passage=p,reason=why,original=f'rigs/rig 1 - arguments/ledger_{p}.json',correction=f'rigs/rig 1 - arguments/{stem}.json',files={str(k.relative_to(R)):hashlib.sha256(v.encode()).hexdigest() for k,v in files.items()}))
 print(p,counts)
m,pl=read('P01')
pl=pl.replace('denied(faithfully_copied(group)) :- line(c).','denied(copied(group)) :- line(c).')
pl=pl.replace('denied(adds_own_cause(group)) :- line(h).','denied(adds_own_cause(group)) :- line(h).\nholds(neg(adds_own_cause(group))) :- line(h).')
pl=pl.replace('denied(selected(group)) :- line(q).','denied(selected(group)) :- line(q).\nholds(neg(selected(group))) :- line(q).')
pl=pl.replace('claim_since(s, selected(group), adds_own_cause(group))','claim_since(s, neg(selected(group)), neg(adds_own_cause(group)))')
m['lines']['s']['text']='[CLAIMED] line q SINCE line h; chosen referent of therefore, with explicit negative content'
m['bin_entries']=[x for x in m['bin_entries'] if not (x['sentence']==10 and x['words']=='therefore')]
m['readings']=[x if not x.startswith('Sentence 10.') else 'Sentence 10. Open readings: therefore points to the whole paragraph or the immediately preceding causal rejection. Chosen: h is my reason pointer. In the corrected execution, neg(...) aliases are gated by the same negative source lines h/q; no positive selection/cause inference is tested.' for x in m['readings']]
finish('P01',m,pl,'Correct the copied predicate and the signed SINCE execution. The original tested positive propositions despite negative ledger wording; this correction uses source-gated negative aliases.')
m,pl=read('P07');pl=pl.replace('denied(faithfully_copied(group)) :- line(c).','denied(copied(group)) :- line(c).')
finish('P07',m,pl,'Align the machine denial with the source and ledger wording: not copied, rather than the narrower not faithfully copied.')
m,pl=read('P10');pl=pl.replace('same_whole_changed_manifestation(divine_whole)','same_whole_changed_manifestation(whole)')
m['lines']['f']['text']='[CLAIMED] whole changes in manifestation while remaining the same whole; divine describes this same referent'
m['readings'].append('Correction 1: whole and divine_whole had denoted the same referent. Use whole everywhere; divine is descriptive, not a second entity.')
finish('P10',m,pl,'Use one machine name, whole, for the referent called divine whole in the original reading; no new thing is introduced.')
m,pl=read('P14');pl=pl.replace('merely_way_of_speaking(group_selection_account)','way_of_speaking(group_selection_account)')
m['lines']['i']['text']='[CLAIMED] NOT [this group-selection account is a way of speaking]'
for x in m['bin_entries']:
 if x['sentence']==8:x['reason']='The source denial of being a way of speaking is retained without adding merely. Stopping time/cessation are not modelled: j asks whether spread remains true after removal. No production law is added from the BECAUSE claim alone.'
m['readings'].append('Correction 1: sentence 8 says not a way of speaking. Retain that exact denial, without weakening it to not merely a way of speaking.')
finish('P14',m,pl,'Remove the unmarked merely qualification from the denial and align its predicate with the source.')
m,pl=read('P03')
pl=add(m,pl,'g',4,'government is a government; response to a press not stated',['kind(government, government) :- $.','body(government, not_stated) :- $.'],standing='GIVEN')
pl=add(m,pl,'r',4,'remedy is a remedy; response to a press not stated',['kind(remedy, remedy) :- $.','body(remedy, not_stated) :- $.'],standing='GIVEN')
pl=add(m,pl,'w',4,'remedy is worse than evil; qualitative comparison without a measured degree',['holds(worse_than(remedy,evil)) :- $.'])
pl=add(m,pl,'m',5,'government MAKES remedy [worse than evil]; pronouns resolved as government/remedy',['social(m, makes, government, remedy, worse_than_evil) :- $.'],'filled in')
m['bin_entries']=[x for x in m['bin_entries'] if x['sentence']!=5]
for x in m['bin_entries']:
 if x['sentence']==4:
  x['words']='the fault of the government itself';x['reason']='Blame/responsibility wording is preserved here, without a moral adjudication. The qualitative worse-than effect is retained as w, and the following explicit MAKES is m; no numerical degree or prior tendency is invented.'
m['readings']=[x for x in m['readings'] if not x.startswith('Sentence 4.') and not x.startswith('Sentence 5.')]
m['readings']+=['Sentence 4. Open readings: worse-than as a measurable amount or an opaque qualitative relation. Chosen in correction 1: retain the qualitative relation under Fact; no amount or ranking computation. The original overbinned that relation.','Sentence 5. Open readings: it denotes government or remedy. Chosen: government MAKES remedy worse, marked filled in for pronoun resolution. No prior tendency is inferred from MAKES.']
finish('P03',m,pl,'Retain the qualitative worse-than effect under Fact and the explicit MAKES line; the original binned too much. Add a rig-2 run to expose the unstated-tendency boundary.',rig2=True)
with (R/'evidence/corrections_OpenAI_Codex.json').open('x') as f:json.dump(dict(author='OpenAI Codex',corrections=receipts),f,indent=2)
