# Written by OpenAI Codex under L66. Inventory and integrity, not semantic scores.
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((R/'corpus/MANIFEST.json').read_text());checked=[]
for name,expected in manifest['corpus_files'].items():
 p=R/'corpus'/name;assert sha(p)==expected,name;checked.append(name)
order=[json.loads(x) for x in (R/'evidence/translation_order.jsonl').read_text().splitlines()]
assert [x['passage'] for x in order]==[f'P{i:02}' for i in range(1,19)]
for x in order:assert sha(R/'translations'/f'{x["passage"]}_OpenAI_Codex_translation.md')==x['translation_sha256']
ledgers=[]
for rig in ['rig 1 - arguments','rig 2 - causes']:
 for jp in sorted((R/'rigs'/rig).glob('ledger_P*.json')):
  m=json.loads(jp.read_text());p=m['paragraph'][:3]
  assert m['whose']=='OpenAI Codex, under L66, from the sealed corpus'
  expected=dict(re.findall(r'(?m)^(\d+)\. (.*)$',(R/'corpus'/f'{p}.txt').read_text()))
  assert m['sentences']==expected,jp
  assert m['rig']==rig,jp
  pp=jp.with_suffix('.pl');assert pp.is_file()
  pl=pp.read_text();ids=re.findall(r'^line\((\w+)\)\.',pl,re.M)
  assert len(ids)==len(set(ids)) and set(ids)==set(m['lines']),(jp,ids)
  assert {str(x['sentence']) for x in m['lines'].values()}|{str(x['sentence']) for x in m['bin_entries']}==set(expected),jp
  for id,v in m['lines'].items():
   assert v['mark'] in ['said','filled in','usual case'] and v['text'].startswith('['+v['standing']+'] '),(jp,id)
  for mark in ['said','filled in','usual case']:assert m['counts'][mark]==sum(x['mark']==mark for x in m['lines'].values())
  assert m['counts']['sentences_losing_to_bin']==len({x['sentence'] for x in m['bin_entries']})
  ledgers.append(str(jp.relative_to(R)))
for p in (R/'translations').glob('*.md'):
 text=p.read_text();assert 'OpenAI Codex' in text and text.rstrip().endswith('TRANSLATION COMPLETE.'),p
 for h in ['1. The ledger','2. The bin','3. Words I split','4. Readings I chose','5. The count']:assert '## '+h in text,p
assert len(ledgers)==29,len(ledgers)
assert len(list((R/'translations').glob('*.md')))==23
assert len(list((R/'evidence/rig1').glob('*.report.txt')))==23
assert len(list((R/'evidence/consequences').glob('*.report.txt')))==23
assert len(list((R/'evidence/rig2').glob('*.report.txt')))==6
assert len(list((R/'evidence/sameness').glob('*.stdout.txt')))==4
for folder in ['rig1','rig2','consequences']:
 for raw in (R/'evidence'/folder).glob('*.raw.txt'):
  assert raw.stat().st_size and 'timed out: True' not in raw.read_text(),raw
 for stderr in (R/'evidence'/folder).glob('*.stderr.txt'):assert stderr.stat().st_size==0,stderr
for file in ['RETURN_README.md','DRAFT L66 - what the run showed.md','Gauge_OpenAI_Codex.md']:assert (R/file).is_file(),file
assert not (R/'corpus/KEY.enc').exists()
result=dict(author='OpenAI Codex',knowledge='seen by local validation; counts are inventory only',checks='passed',corpus_hashes_checked=checked,original_completion_hashes_unchanged=True,original_order=[x['passage'] for x in order],ledger_pairs=len(ledgers),five_section_translations=23,rig1_reports=23,rig2_reports=6,consequences_outputs=23,sameness_outputs=4,no_timeouts=True,stderr_empty=True,key_returned=False,limits='This checks completeness, metadata agreement and byte integrity. It does not establish semantic fidelity or correctness of the writers or the theory.')
out=R/'evidence/Final_integrity_validation_OpenAI_Codex.json'
with out.open('x') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
