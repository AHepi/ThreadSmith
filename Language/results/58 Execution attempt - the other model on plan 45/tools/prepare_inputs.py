#!/usr/bin/env python3
"""Export existing tables and named case inputs. This does not run s(CASP)."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'sources' / 'original_audit' / 'Ledger_38_39_Audit'
COMMIT = 'ce30053e4369675e989ae4f21103132e5398cbe6'
CASE_IDS = ['T02-B', 'T02-D', 'L09', 'N03-A', 'N03-B', 'N05-A']
# This is a disclosed encoding of the old tables, not a new translation or
# an implementation of the missing sameness test.
TERMS = {
 'T02-B': {
  'k': ['kind(kingfisher, kingfisher)'],
  'f': ['kind(feathers, feathers)'],
  'o': ['holds(belong_to(feathers, kingfisher))'],
  'u': ['holds(unharmed(feathers))'],
  'd': ['holds(subject_of_colour_description(feathers, mara))']},
 'T02-D': {
  'k': ['kind(kingfisher, kingfisher)'],
  'f': ['kind(feathers, feathers)'],
  'o': ['holds(belong_to(feathers, kingfisher))'],
  's': ['kind(spark, spark)'],
  'p': ['did(p, spark, struck, feathers, none)'],
  'c': ['holds(caught_fire(kingfisher))'],
  'b': ['holds(burned(feathers))']},
 'L09': {},
 'N03-A': {
  'p': ['kind(pear, pear)'],
  'y': ['holds(has_yellow_skin(pear))'],
  'r': ['holds(has_red_colouring(pear))']},
 'N03-B': {
  'a': ['kind(painter, painter)'],
  'p': ['kind(pear, pear)'],
  'f': ['kind(finger, finger)'],
  'r': ['holds(red_stained(finger))'],
  't': ['did(t, painter, touched, pear, none)']},
 'N05-A': {}}
# These statements are frozen-plan expectations, not results of this attempt.
PLAN_ROWS = [
 ('F01','exception against ALWAYS',['N12-A'],'no run', '1'),
 ('F02','embedded content as TOLD',['N05-A','N06'],'Part A; no separate run','1'),
 ('F03','a chosen reading is not a resolved source',['T39','C03','N27'],'no run','1'),
 ('F04','a Result needs a producer',['N14-A','N15-A','N15-B'],'translation and current/frozen rigs','2'),
 ('F05','enabling is not achieving',['T21','N17'],'current/frozen rigs','3'),
 ('F06','MAKES with a prior tendency',['N16'],'current/frozen rigs','3 with owner decision'),
 ('F07','endpoint support and the offered route',['N19','N20'],'current/frozen rigs','1 for N19; 3 for N20'),
 ('F08','the added-lines test is silent',['N23-A','N23-B'],'current/frozen rigs','3'),
 ('F09','an actual observation in a what-if',['N25'],'current/frozen rigs','2'),
 ('F10','only-ways makes nothing',['T26','T27'],'current/frozen rigs','1'),
 ('F11','one event, several mentions',['N29'],'translation','3 with translator note'),
 ('F12','a mentioned goal',['N22'],'current/frozen rigs','1'),
 ('F13','a clean report is not coverage',['T61','T76'],'no run','1'),
 ('F14','a verb with no object',['N30'],'translation and rig','3'),
 ('F15','a BECAUSE and its exact denial',['N18-A','N18-B'],'current/frozen rigs','2')]

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def main() -> None:
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('original_validator', AUDIT/'tools/validate_package.py')
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Calling validate(), not main(), leaves the original result file untouched.
    result = mod.validate()
    (ROOT/'evidence/original_package_validation.json').write_text(json.dumps(result, indent=2)+'\n')
    corpus = {}
    for name in ('inputs.jsonl','late_challenges.jsonl','literary_probes.jsonl','new_60.jsonl'):
        for line in (AUDIT/'corpus'/name).read_text().splitlines():
            row=json.loads(line)
            assert row['id'] not in corpus
            corpus[row['id']]=row
    text=(AUDIT/'03_Worked_translations.md').read_text()
    sections=[s for s in re.split(r'(?m)^## ',text)[1:] if '### The ledger' in s]
    assert len(sections)==len(CASE_IDS)
    out=ROOT/'prepared/part_a_original_side'
    out.mkdir(parents=True,exist_ok=True)
    exports=[]
    for case, section in zip(CASE_IDS,sections):
        table=section.split('### The ledger',1)[1].split('### The bin',1)[0]
        rows=[]
        for line in table.splitlines():
            if not line.startswith('|'): continue
            cells=[x.strip() for x in line.strip('|').split('|')]
            if len(cells)==5 and cells[3] in {'said','filled in','usual case'}:
                rows.append(dict(zip(('id','standing','content','mark','sentence'),cells)))
        assert set(TERMS[case])=={r['id'] for r in rows}
        sentences={}
        for n,s in re.findall(r'\*\*Source (?:sentence|unit) (\d+)\.\*\* ([^\n]+)',section):
            sentences[n]=s
        assert sentences
        bin_text=section.split('### The bin',1)[1].split('### Words I split',1)[0].strip()
        # Keep each old section byte-for-byte within the new wrapper.
        (out/(case+'_original_translation.md')).write_text('## '+section)
        metadata={
            'paragraph':case,
            'whose':"Other model's original corpus/table; export prepared for plan 45, not a new Claude translation",
            'sentences':sentences,
            'leftover':[bin_text] if bin_text else [],
            'whatifs':[],
            'lines':{},
            'status':'PREPARED_NOT_EXECUTED',
            'origin_sha256':sha((AUDIT/'03_Worked_translations.md').read_bytes()),
            'source_text_sha256':sha(corpus[case]['text'].encode()),
            'export_limit':'JSON retains original bin verbatim as one entry. Native GAUGE counts entries, not the original lost-sentence count; do not equate them.',
            'original_source':corpus[case],
            'adapter_notes':[
                'Stable predicate spellings are encoding choices, not recovered original .pl bytes.',
                'No body/2 classification is invented for response not stated.',
                'The native missing-direction sentinel none is used for the two Happenings; it is not an asserted physical direction.',
                'STRuck and TOUCHED remain struck and touched, not hit.',
                'TOLD case and case_kind fields retain the old fixture-world convention. No CLAIMED/GIVEN projection is substituted.',
                'did/5 is native rig-2 notation; rig-1-alone findings do not certify physical checking or shape-book coverage.',
                'The exact original five-part row is in original_row. No new substantive line is inserted.'
            ]}
        pl=['% Prepared export of the original table for plan 45.',
            '% NOT an independent translation, NOT a comparison result.',
            '% No semantic checker or Prolog parser has run on this export.']
        for row in rows:
            assert row['standing'].startswith('TOLD in world ')
            world=row['standing'].split('TOLD in world ',1)[1]
            metadata['lines'][row['id']]={
                'mark':row['mark'],'sentence':int(row['sentence']),
                'text':f"[{row['standing']}] {row['content']}",
                'standing':'TOLD','case':world,'case_kind':'told',
                'original_row':row,'encoded_heads':TERMS[case][row['id']]}
            pl.append('line('+row['id']+').')
            for head in TERMS[case][row['id']]: pl.append(head+' :- line('+row['id']+').')
        compact=case.replace('-','')
        (out/('ledger_'+compact+'.json')).write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
        (out/('ledger_'+compact+'.pl')).write_text('\n'.join(pl)+'\n')
        exports.append({'case':case,'rows':len(rows),'status':'PREPARED_NOT_EXECUTED','translator':'original assistant table, not Claude','json':'prepared/part_a_original_side/ledger_'+compact+'.json','pl':'prepared/part_a_original_side/ledger_'+compact+'.pl'})
    (ROOT/'prepared/part_a_manifest.json').write_text(json.dumps(exports,indent=2)+'\n')
    resolved=[]; chosen=set()
    for f,title,refs,mode,pile in PLAN_ROWS:
        ids=[]
        for ref in refs:
            if ref in corpus: matches=[ref]
            else: matches=sorted(k for k in corpus if k.startswith(ref+'-'))
            assert matches, (f,ref)
            ids.extend(matches)
        chosen.update(ids)
        resolved.append({'finding':f,'title':title,'plan_references':refs,'resolved_input_ids':ids,'required_evidence':mode,'plan_predicted_pile':pile,'observed_pile':None,'semantic_run':False,'status':'NOT_ADJUDICATED','expansion_note':'A family name without a suffix is expanded to all supplied members for preparation only, not a claim that the plan requires every member to be executed.'})
    (ROOT/'prepared/part_b_manifest.json').write_text(json.dumps(resolved,indent=2)+'\n')
    with (ROOT/'prepared/part_b_inputs.jsonl').open('w') as h:
        for identifier in sorted(chosen):
            d=dict(corpus[identifier]);d['text_sha256']=sha(d['text'].encode());d['status']='SOURCE_INPUT_ONLY_NOT_A_LEDGER_OR_RUN'
            h.write(json.dumps(d,ensure_ascii=False)+'\n')
    print(json.dumps({'original_package_validation':result['status'],'original_manifest_files':result['manifest_files_verified'],'existing_tables_exported':len(exports),'table_rows_exported':sum(x['rows'] for x in exports),'part_b_finding_records':len(resolved),'part_b_inputs_resolved':len(chosen),'completed_semantic_runs':0,'part_a_native_comparisons':0},indent=2))

if __name__=='__main__': main()
