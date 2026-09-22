"""OpenAI Codex: compose L66 draft and gauge from immutable saved receipts/reports."""
from pathlib import Path
import json,re
from collections import Counter
B=Path(__file__).resolve().parents[1]
C={1,3,7,10,14}
def key(i):return f'P{i:02}'+('_correction1' if i in C else '')
def link(label,path):
 assert (B/path).exists(),path
 return f'[{label}](<{path}>)'
def cell(s):return str(s).replace('|','\\|').replace('\n','<br>')
def code(s):return '`'+s.replace('`','\\`')+'`'
def report_links(kind,k):
 return ' / '.join(link(label,f'evidence/{kind}/{k}_OpenAI_Codex.{ext}') for label,ext in [('report','report.txt'),('raw','raw.txt'),('receipt','receipt.json')])
def report_body(kind,k):
 t=(B/f'evidence/{kind}/{k}_OpenAI_Codex.report.txt').read_text().split('GAUGE:')[0]
 t='\n'.join(t.splitlines()[1:]).strip()
 return '<br>'.join(code(x.strip()) for x in t.splitlines() if x.strip()) if t else 'No finding text printed before GAUGE.'
rows=[]
shape_text=(B/'rigs/rig 2 - causes/patched/laws.pl').read_text()
shapes=set(re.findall(r'shape\((\w+),',shape_text))
for i in range(1,19):
 p=f'P{i:02}';k=key(i);j=json.loads((B/f'rigs/rig 1 - arguments/ledger_{k}.json').read_text())
 pl=(B/f'rigs/rig 1 - arguments/ledger_{k}.pl').read_text()
 # These ledgers use simple atomic arguments for did/5; keep actual lexical forms.
 events=re.findall(r'^did\((\w+),\s*\w+,\s*(\w+),\s*\w+,\s*\w+\)',pl,re.M)
 actual={v for _,v in events}; unshaped=sorted(actual-shapes);shaped=sorted(actual&shapes)
 other=sorted({x['verb'] for x in j.get('verb_inventory',[]) if not x.get('has_shape')} - actual)
 tr=f'translations/{p}_OpenAI_Codex_translation'+('_correction1' if i in C else '')+'.md'
 r2k='P13_correction1' if i==13 else k
 r2exists=(B/f'evidence/rig2/{r2k}_OpenAI_Codex.receipt.json').exists()
 if i==13:assert r2exists,'Wait for P13 rig2 correction before writing final draft.'
 findings='Rig 1: '+report_body('rig1',k)+'<br>'+report_links('rig1',k)
 if r2exists:findings+='<br>Rig 2: '+report_body('rig2',r2k)+'<br>'+report_links('rig2',r2k)
 else:findings+='<br>Rig 2: no run for this passage.'
 cr=(B/f'evidence/consequences/{k}_OpenAI_Codex.report.txt').read_text()
 ds=cr.split('DERIVED, ON THE FULL LEDGER:')[1].split('WHAT CHANGES WHEN ONE LINE IS TAKEN OUT:')[0].strip()
 der='<br>'.join(code(x.strip()) for x in ds.splitlines()) if ds else 'No entries printed under DERIVED, ON THE FULL LEDGER.'
 der+='<br>'+report_links('consequences',k)
 binids=sorted({x['sentence'] for x in j['bin_entries']})
 marks=Counter(x['mark'] for x in j['lines'].values())
 assert marks['said']==j['counts']['said'] and marks['filled in']==j['counts']['filled in'] and marks['usual case']==j['counts']['usual case']
 assert len(binids)==j['counts']['sentences_losing_to_bin']
 receipt=json.loads((B/f'evidence/rig1/{k}_OpenAI_Codex.receipt.json').read_text());assert receipt['exit_code']==0
 rows.append(dict(i=i,p=p,k=k,j=j,tr=tr,findings=findings,der=der,binids=binids,marks=marks,events=events,unshaped=unshaped,shaped=shaped,other=other,r2k=r2k,r2exists=r2exists))

scope=link('L64 scope contract','scope/L64 Scope - the contract the language claims, second version.md')
g=['# L66 gauge — OpenAI Codex','',
'Written by OpenAI Codex. **Read:** the supplied source sentences, ledger metadata, generated Prolog, shape book and '+scope+'. **Seen:** the linked checker reports and raw query evidence. **Worked out:** the inventory below by distinct source sentence IDs, line marks and literal verb names. Counts are inventory, not scores or evidence of truth.',
'',
'The primary ledger is correction 1 for P01, P03, P07, P10 and P14; it is the original for the other passages. P13 uses the separate corrected rig-2 adapter, with its original rig-1 ledger unchanged. The draft records original outputs separately. The said/filled-in/usual-case columns count rig-1 ledger lines once; matching rig-2 copies are not counted again.',
'',
'“Bin sentences” counts distinct `bin_entries[].sentence` IDs, not the length of `leftover`. “Actual unshaped verbs” counts distinct verbs in executable `did(...)` clauses absent from the unchanged shape book. “Other listed verbs” records distinct unshaped verb names from the JSON manual inventory after removing those actual verbs; these include generic, intransitive, figurative, supposed or binned uses and are not additional checked happenings. This preserves the difference between a zero event inventory and successful checking.',
'',
'| Passage and primary translation | Source sentences | Bin sentences and IDs | Said | Filled in | Usual case | Actual unshaped verbs (distinct types; event lines) | Actual shaped verbs | Other listed verbs (distinct types, not actual did events) | CANNOT TELL findings |',
'| --- | ---: | --- | ---: | ---: | ---: | --- | --- | --- | --- |']
for r in rows:
 actual=(str(len(r['unshaped']))+': '+', '.join(code(v)+' (line'+('s ' if sum(v==v2 for _,v2 in r['events'])>1 else ' ')+', '.join(e for e,v2 in r['events'] if v==v2)+')' for v in r['unshaped'])) if r['unshaped'] else '0; no actual did event'
 shaped=str(len(r['shaped']))+(' — '+', '.join(r['shaped']) if r['shaped'] else '')
 other=str(len(r['other']))+(': '+', '.join(code(x) for x in r['other']) if r['other'] else '')
 ct='1 — rig 1, plan b: '+code('CANNOT TELL whether the plan can work.') if r['i']==16 else '0 printed; not coverage'
 g.append('| '+' | '.join(map(cell,[link(r['p'],r['tr']),len(r['j']['sentences']),f"{len(r['binids'])} / {len(r['j']['sentences'])}; IDs "+', '.join(map(str,r['binids'])),r['marks']['said'],r['marks']['filled in'],r['marks']['usual case'],actual,shaped,other,ct]))+' |')
g += ['',
'**Seen and worked out:** the rig-1 driver’s printed gauge counts `len(leftover)`, which need not equal distinct source sentence IDs. The original P01 report prints 9 of 10 because it has nine leftover entries; they concern eight distinct sentences. The requested gauge above counts those eight sentence IDs. Every printed gauge remains unchanged in its saved report. Original evidence: '+report_links('rig1','P01')+'.',
'',
'**Seen, separate from CANNOT TELL:** P03 correction 1, rig 2, line m prints '+code("FINE, BUT IT RESTS ON SOMETHING NOBODY STATED: 'MAKES' only fits if they were not already heading that way.")+' This is an unstated-tendency warning, not a CANNOT TELL finding. The ledger supplies no prior tendency; the report is conditional on an addition the writer did not state. '+report_links('rig2','P03_correction1')+'.',
'',
'**Seen, separate from CANNOT TELL:** P13 rig 2, line d prints '+code("NOT CHECKED. The verb 'bears' is not in the shape book, so the checker cannot tell what kind of happening it is.")+' The category is NOT CHECKED even though the explanatory sentence uses “cannot tell”. P07 `produced`, P09 `yield`/`pass`, P10 `bestows` and P17 `supplanted` likewise have no shape in the machine inventory; their absence from individual finding text does not turn them into checked events. '+report_links('rig2','P13_correction1')+'.',
'',
'**Read and worked out, conditional threshold:** L64 labels its thresholds “proposed for the owner”. No approval was supplied. Every row above loses something from more than one third of its sentences to the bin. If that proposed threshold is adopted, every passage in this run would be reported as outside scope under that bin rule. This is a conditional implication of the inventory, not an approved classification or a judgment that every remaining line is uncheckable.',
'',
'**Read and worked out, conditional shape threshold:** if L64’s proposed “unshaped outnumber shaped” test is applied to actual `did` verb types, it flags P07, P09, P10, P13 and P17 as outside the laws. Zero actual shaped and zero actual unshaped verbs in another passage means the physical-event comparison has no event sample; it does not mean the prose is physically verified. The broader manual inventory shows additional language left outside shape checking. P03’s explicit MAKES slot is checked separately from did/shape events.',
'',
'**Seen and worked out:** P04 and P18 rig-2 reports contain no finding before their gauges. Their zero actual-event inventories, uninstantiated general rules and large bins explain why these reports cannot support a claim of full coverage. No passage exceeds twelve source sentences, but that length inventory alone is not a measured error-growth guarantee.',
'']
(B/'Gauge_OpenAI_Codex.md').write_text('\n'.join(g))

d=['# DRAFT L66 — what the run showed','',
'Written by OpenAI Codex under L66. This is the returned draft for the owner, not a change to any project record. **Read:** the supplied instructions, authorities 38 and 39, '+scope+', source passages and translation choices. **Seen:** the saved reports and raw queries linked below. **Worked out:** the limitations and parked questions, kept separate from printed findings. Nothing here judges the truth of a passage or the quality of its writer.',
'',
'The per-passage table uses correction 1 for P01, P03, P07, P10 and P14, and the original rig-1 ledger for all others. For P13 alone, its separate rig-2 correction 1 is the reported rig-2 execution. Original ledgers, translations and outputs remain beside corrections and are linked separately below. Quoted findings and DERIVED entries are transcribed from the selected saved reports; the reports themselves are unchanged.',
'',
'## Per-passage observed results','',
'| Passage | What the rigs printed, with named lines and evidence | What consequences printed as DERIVED, with support IDs | Choices made in the translation (read), with exact translation |',
'| --- | --- | --- | --- |']
for r in rows:
 choices='<br>'.join(r['j'].get('readings',[]))+'<br>'+link('five-section translation',r['tr'])+' / '+link('ledger JSON',f"rigs/rig 1 - arguments/ledger_{r['k']}.json")+' / '+link('ledger Prolog',f"rigs/rig 1 - arguments/ledger_{r['k']}.pl")
 d.append('| '+' | '.join(map(cell,[r['p'],r['findings'],r['der'],choices]))+' |')
d += ['',
'## What the runs establish, and where they stop','',
'**Seen:** the one-line-removal consequences outputs are preserved in full at every consequences report link. An empty DERIVED section means that this program printed no newly classified fact for that ledger and its queried predicates. It does not establish that the prose has no consequences. In P04 no facts were found; the ledger consists of generic rules/restrictions without an instantiated case. In P18 the supposed universal has no ground specimen: “no new contradiction” therefore does not amount to testing every possible instance.',
'',
'**Seen and worked out:** P10 prints `depends_on(our_bliss,blamed_conditions)   <- lines g`, although line g already directly states the dependency as `depends(...)`. This is the program’s derived classification for a predicate-level consequence, not a newly discovered substantive claim. P11 and P14’s three `groups_selected(...)` facts apply their filled-in descriptive general line m to explicitly supplied examples n/o/p. P13’s `holds(yields(void))` applies its filled-in generic line g to h. These consequences are conditional on those marked translation readings.',
'',
'**Seen:** P11’s what-if HOLDS queries `holds(spreads(helping))` after f is removed. Its raw proof cites only g, the already-given spread fact. **Worked out:** the result shows retention of that baseline fact under the driver’s change procedure, not an independently supplied mechanism proving spread would persist. Its denied-BECAUSE finding likewise says only that no productive connection is present in this ledger. '+report_links('rig1','P11')+'.',
'',
'**Seen:** P13’s rig-1 what-if FAILS queries `holds(moves(atoms,down))` after e is removed, and the proof cites only d. The corrected rig-2 adapter really swaps the source decline clause for its explicit denial; the original rig-2 adapter did not execute this change because it supplied an unsupported metadata field. **Worked out:** preserving baseline d still makes the positive downward-motion query succeed; the negative what-if therefore prints FAILS without a shaped law for `bears`. The NOT CHECKED movement finding and this what-if output concern different questions and must be retained together. '+report_links('rig1','P13')+'; corrected rig 2 '+report_links('rig2','P13_correction1')+'.',
'',
'**Seen:** P14’s h prints JUMP because no ledger rule produces `spreads(helping)` after the asserted effect g is removed. Its what-if nevertheless prints HOLDS after f and g are set aside; the raw changed query has no models. **Worked out:** the driver matches the claimed negative outcome to the absence of a positive proof after dependency-based deletion. It has not supplied the missing productive mechanism or a separate explicit proof that spread stops. The coexistence of JUMP and HOLDS is evidence about these two procedures, not a vindication of the causal statement. '+report_links('rig1','P14_correction1')+'.',
'',
'**Seen:** P03 correction 1 has an unstated-tendency report on its explicit social MAKES line m. **Worked out:** the report applies the MAKES slot test to a marked pronoun reading; it does not show that a government and a remedy are physical bodies or that the presumed tendency is a stated fact. No tendency was inserted to obtain a clean report. '+report_links('rig2','P03_correction1')+'.',
'',
'**Read and seen:** the supplied instructions explain that generic driver questions can print “predicate does not exist” when a ledger contains none of the queried kind. Those errors remain in raw logs. Empty answers and “NO FAULT FOUND in the lines that were checked” are read with each ledger’s populated predicates and bin, not promoted to full coverage or truth. P16 demonstrates this directly: the report prints NO FAULT FOUND and also CANNOT TELL whether plan b can work. No missing route was supplied.',
'',
'**Seen in the sameness runs; worked out in the hand decisions:** the two qualifying source pairs each share nine of ten numbered sentences. Primary P01/P07 '+link('exact output','evidence/sameness/P01_correction1_P07_correction1_primary_OpenAI_Codex.stdout.txt')+' and '+link('hand decisions','evidence/sameness/P01_correction1_P07_correction1_primary_hand_decisions_OpenAI_Codex.md')+' distinguish real production polarity from annotation-only differences and predicate encoding asymmetry. Primary P11/P14 '+link('exact output','evidence/sameness/P11_P14_correction1_primary_OpenAI_Codex.stdout.txt')+' and '+link('hand decisions','evidence/sameness/P11_P14_correction1_primary_hand_decisions_OpenAI_Codex.md')+' retain opposite causal claims and opposite removal expectations. These lexical comparisons and hand rulings are not independent proof that the translations preserve every commitment.',
'',
'## What could not be translated, and why','',
'This table summarizes the bins; exact quoted words, source sentence IDs and reasons remain in section 2 of every linked translation and in the JSON `bin_entries`. No binned material was silently removed from the returned evidence. '+link('Gauge_OpenAI_Codex.md','Gauge_OpenAI_Codex.md')+' counts distinct affected sentences and distinguishes the proposed L64 threshold from an approved boundary.',
'',
'| Passage | Material left out of executable commitments, and reason |',
'| --- | --- |']
bins={
1:'Probability comparisons, likelihood-weighted cost/benefit arithmetic, relative speed, modal rewriteability, purpose and location. Their restricted conclusions cannot be made unconditional; the redescription remains an opaque relation.',
2:'Mentioned mottos, belief/desire, degree, most/sometimes, normative or possible objections, institutional imagery, purpose, liability, timing and counterfactual consent. The supplied “cannot” is retained, not repaired.',
3:'Questions, attributed thought and obligation, majority and timing, blame wording and rhetorical images. Correction 1 retains the qualitative worse-than relation and explicit MAKES; it does not turn questions into assertions or add a prior tendency.',
4:'Motion/dissolution possibility, total annihilation modality, qualifications about violence/strength, restriction-until wording, and questions about hypothetical events. Generic laws have no invented actual object on which to run the physical laws.',
5:'Command, attitude, degree, permission, exception-like evaluative exclusivity, names/renaming, imagery and relations of duty/convention. Marked categorical and only-ways readings do not calculate moral values.',
6:'Imperatives and purpose, degree, spatial imagery, modality, long enumerations as imagery and chain-length examples. A figurative chain is not asserted to be a physical object with a pressure response.',
7:'The same probabilistic, quantitative, modal, temporal and spatial restrictions as the independently translated passage describes, plus “not merely” emphasis. The asserted writer’s PRODUCED event remains unshaped; showing is not denied.',
8:'Command and obligation, withdrawal imagery, conditional/modally qualified consequences, comparisons of time and moral weight, and a temporally framed reclassification. “Would not be lost” is preserved as supplied.',
9:'Location, openings, degree, speed, modal claims and questions; a generic load tendency is not a specified response to a press. Water/food/voice and other source verbs are preserved without substituting push/hit, and the BECAUSE claims do not create their own production rules.',
10:'Questions, amounts and metaphysical scale, figurative cosmic body/soul and paradoxes, purpose, ignorance/attitudes, and uninstantiated universals. Figurative identities and bestowal readings are marked; no bodily mechanism or inverse identity rules are inferred.',
11:'Selection criteria combining variation, inheritance and descendant numbers; joint causes, greater/smaller reproductive success, possibility, variation magnitudes, and sameness of spread trajectory. The what-if only queries continued truth of spread, not “as before” in amount or manner.',
12:'Greatest/best comparisons, degree, absence of doubt, predicted agreement/belief, qualified deprivation, and causal ranking. Qualifiers are not silently converted into an unqualified sufficient cause or an actual animal specimen.',
13:'Spatial magnitude, timing, modal collision/creation claims and questions, material or weight comparisons and generic yielding qualifications. The supplied “would not ... fall” is retained; unshaped bears does not determine physical response.',
14:'The quantified selection criteria and comparisons, combined contributors, modal group possibility and amount-dependent outcome, plus timing/cessation, attribution and accounting. The claim of stopping is represented only as the admitted negative spread query after removal, not a duration model.',
15:'Images, command, modal inability, question, amount/scale, unbounded time and attribution. The printed “To be great is not to be misunderstood” is not repaired; the selected categorical reading supplies no unstated greatness of named people.',
16:'Commands, machine imagery, perhaps/may and obligation, comparative evaluation, intended avoidance, lack of knowledge, excessive duration and future life ending. The explicit plan retains its aim but the route remains unstated.',
17:'Quantitative contrasts of individual and tribal advantage, numbers and degrees, readiness/purpose, hypothetical victory over most tribes, and unbounded time/place. Supplanted is retained; no actual victorious hypothetical tribe or sufficient morality-causes-success law is invented.',
18:'Belief/knowledge, modality, possibility under supposition, spatial/seasonal timing, hidden-power and birth imagery, questions, and purposive or quantified consequences. Generic origin descriptions remain distinct; no ground creation instance or unstated modal bridge is added.'}
for r in rows:d.append('| '+link(r['p']+' bin',r['tr'])+' | '+bins[r['i']]+' |')
d += ['',
'## Original results and corrections retained separately','',
'**Read and seen:** these corrections repair the translation or runner metadata in new files. They do not edit the saved original evidence, source passages, authorities, or checker code.',
'',
'| Passage | What changed and why (worked out) | Original evidence retained | Correction evidence used above |',
'| --- | --- | --- | --- |']
corrections={1:'The original SINCE s asked about positive selected(group) and adds_own_cause(group), contrary to the negative source lines. Correction 1 supplies line-gated neg(...) aliases and changes c from denied(faithfully_copied(group)) to the stated denied(copied(group)). The printed final conclusion now names neg(selected(group)); g and s still print NO CONNECTION.',3:'The original retained only unjust-laws a and overbinned the qualitative comparison and explicit MAKES. Correction 1 retains w and m, with the needed named referents but no tendency. Rig 1 still prints NO FAULT FOUND; a new rig-2 run prints the unstated-tendency finding.',7:'The original machine already used the negative SINCE aliases, but the human ledger text did not explicitly state the negative content. Correction 1 changes c from denied(faithfully_copied(group)) to the stated denied(copied(group)), aligns the text, and records the alias reading and distinct bin-sentence count; its printed inference outcomes remain NO CONNECTION.',10:'The same referent was split between whole and divine_whole. Correction 1 consistently uses whole; the adjective divine does not create another thing. Its printed DERIVED entry is unchanged.',14:'The original weakened “not a way of speaking” to “not merely a way of speaking”. Correction 1 retains the exact source denial, while its JUMP, what-if and groups-selected consequence outputs remain as printed above.'}
for i in sorted(C):
 p=f'P{i:02}'
 orig=link('translation',f'translations/{p}_OpenAI_Codex_translation.md')+'; rig 1 '+report_links('rig1',p)+'; consequences '+report_links('consequences',p)
 new=link('correction translation',f'translations/{p}_OpenAI_Codex_translation_correction1.md')+'; rig 1 '+report_links('rig1',p+'_correction1')+'; consequences '+report_links('consequences',p+'_correction1')
 if i==3:new+='; rig 2 '+report_links('rig2',p+'_correction1')
 d.append('| '+' | '.join(map(cell,[p,corrections[i],orig,new]))+' |')
d.append('| P13, rig 2 only | The original rig-2 metadata supplied make_not_so, which this driver ignores. Its raw what-if query had removed: [] and swap: None; the claimed change was not executed there. The new adapter uses the supported swap field to deny the decline clause. Rig-1 ledger and five-section translation are unchanged; the corrected query still retains baseline movement d. | '+report_links('rig2','P13')+' | '+report_links('rig2','P13_correction1')+' |')
d += ['',
'## PARKED','',
'These are questions for later authorization or investigation. No proposed authority change is applied in this return.',
'',
'| Parked issue | Evidence or reason to retain it | Boundary of the present finding |',
'| --- | --- | --- |',
'| Approve, reject or revise the bin and shape thresholds | Read: L64 explicitly labels the thresholds proposed. Worked out: each passage exceeds the proposed bin fraction, and five have unshaped actual verbs with no shaped actual verb. | The gauge inventories loss; it does not convert an unapproved threshold into a verdict or add scope to 38/39. |',
'| Counterfactual persistence versus an independent route | Seen: P11 retains g and P13 retains d under the queried change; P14 deletes g from an unproved BECAUSE relation and then reports HOLDS for the negative expectation. | These are observations of the admitted driver operations. A different intervention semantics or dependence propagation rule would need its own separately authorized test. |',
'| Shared schema or validation for rig-1 and rig-2 what-if metadata | Seen: the original P13 rig-2 run ignored make_not_so; the append-only adapter correction supplies swap and preserves the original. | The correction fixes this input adapter only. No checker protocol or authority is changed. |',
'| Plain facts, generic/intransitive verbs and no-shape coverage | Seen: only did/5 verbs enter the machine shape inventory; generic free descriptions and producer-free movement can remain outside it. P04/P18 have no actual event to check. | A zero physical-event gauge is not proof of coverage. Deciding whether additional language forms should enter physical laws is parked. |',
'| Explicit MAKES without a stated prior tendency in nonphysical prose | Seen: P03 m reaches rig 2 and prints an unstated-tendency warning; its reading resolves pronouns but adds no tendency. | No inference that the remedy was or was not already worsening is licensed by this return. Extension or restriction of MAKES needs a separate question. |',
'| Generic rule-level support and quantified argument chains | Read: bins preserve arguments about probabilities, descendant counts, multiple contributors and universal rules; no ground specimen or sufficient bridge is invented. | A richer rule-pointer or quantitative language would expand the current contract. Its absence explains missing executable material but is not a fault in the writer. |',
'| Consequences tool and world isolation | Read in supplied consequences.py: it calls run_query directly without the check() initialization of WORLD_REMOVED for SUPPOSED/TOLD lines. Seen: P18’s supposed rule c has no kind instances and its DERIVED section is empty. | No leakage was observed in this run; the source-level limitation is parked without a patch or an invented successful isolation test. |',
'| Meaning of “derived” across predicate encodings | Seen: P10 depends_on is printed as derived from g even though g states dependency as depends. | The report is kept verbatim. A future semantic-normalization policy would need to distinguish restatement at another predicate from a new claim. |',
'| Conditional and figurative readings | Read: all selected alternatives are in each translation; e.g. P09 BECAUSE attachment, P10 cosmic identities, P15 categorical reading of not misunderstood, P16 counter-friction plan. | Findings dependent on filled-in readings remain conditional. No external textual repair or authorial-intent verdict is made. |',
'']
(B/'DRAFT L66 - what the run showed.md').write_text('\n'.join(d))
print('OpenAI Codex wrote gauge and draft from selected saved evidence.')
