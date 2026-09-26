# S98 — The line-up of edits and recommendations, by part of the semantics

*Log S98, 26 September 2026, under decision S30 and the specification `../group/grouping and structure, chosen.md`. Inputs, all in `../group/`: `anchored.jsonl` (md5 41752268722000a376a15e7de2bde76e); `sentence index of the latest text.jsonl` (md5 fdaf069a0c1d71be4e17b38d2f6bce82); `proposal by place - scripts/sections.json` (md5 c4f53beacd7f699a930191e2cb95f9fe); `proposal by place - scripts/assignment.jsonl` (md5 2b57aec91e82dec64aaa9686ca3ca377); `proposal by idea - assignment.jsonl` (md5 921b4ceb5a918f5fb30425c1068c6ff5). Made by program (`scripts/build.py`, checked by `scripts/check.py`), nothing committed.*

## How it is lined up

- The thing lined up is the unit of the latest text (`tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md`): 756 units, each a sentence, a heading, a displayed formula or a list item.
- The units fall into 134 sections, and the sections into sixteen groups: fifteen named by the theory's own Part titles (G02 to G15 for Parts II to XV, G01 for the document as a whole), and G16 for vocabulary changes that run across the text.
- A section of Part 0, Part I or Part XVI that treats the matter of another Part is filed with that Part's group; it stays whole and keeps its own Part label.
- Each group file shows its sections, each section all its units in text order, and under each unit every record that touches it, oldest first, with the records of one change kept together as one entry.
- A record on several sentences is shown in full once, under its home sentence, with a pointer line at each other sentence; a vocabulary record is shown in full under every sentence it touches.
- A record with no sentence in the latest text stands in a block at the end of its section, or at the end of its group under its Part.
- Only the wording is shown, never the grounds given for a change; the source file and source reference on each record line are the one pointer to them.

## How to read an entry

- **Entry header:** the change id (`CH-…`, one change seen in one or more sources), the number of its records shown there, their statuses, and the marks *vocabulary* (a record of the change has scope `term` or `whole text`), *form only* (the idea proposal files the change under punctuation, emphasis, pointers and labels) and *also at* (the other units where records of the change are shown, its entry not in the latest text, or its entry in G16).
- **Record line:** record id · round · kind (`edit`: a change made to a theory text; `recommendation`: a proposed change) · status · whether the wording stands · written against (the text and line the change is written against) · carried by (the text that carries it) · source file — source reference.
- **Wording:** *Before* is the old sentence (or the old wording when no sentence is given), *After* the new sentence (or the new wording). *Old wording* and *New wording* are added when a span differs from its sentence. All wording is verbatim, LaTeX included.
- **Displays:** *in full* (under the record's home sentence); *pointer line* (at each other sentence the record touches, with a link to where it is in full); *vocabulary line* (a vocabulary record, in full under every sentence it touches); *block* (a record with no sentence in the latest text: removed, never applied or not locatable).
- **Statuses:** applied, not applied, declined, superseded, open for the owner, unknown, as the collectors recorded them.
- **Wording stands** means the record's new wording is in the latest text; **wording not in the latest text** means it is not; nothing is shown where the question does not arise.
- **Same wording:** records of one change whose four wording fields are byte for byte the same are listed together, and the wording is shown once.
- **Nearest latest-text sentence (a lead, not a place):** for a record with no sentence, the sentence sharing most content words with it; it is a lead for the reader, not where the record is filed.

## The groups

| group | Parts drawn from | units (touched / all) | changes placed here | records shown here in full | pointer lines | vocabulary lines | records in blocks | applied | not applied | declined | superseded | open for the owner | unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [G01 The document as a whole](groups/01%20The%20document%20as%20a%20whole.md) | FM, 0, I, XVI | 29 / 46 | 86 | 62 | 2 | 37 | 52 | 55 | 1 | 2 | 4 | 0 | 0 |
| [G02 Organizations and their changes](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md) | II, 0, XVI | 27 / 66 | 52 | 51 | 28 | 24 | 7 | 35 | 2 | 5 | 8 | 0 | 1 |
| [G03 Questions](groups/03%20Questions%20%28Part%20III%29.md) | III, 0, XVI | 39 / 56 | 74 | 80 | 1 | 50 | 25 | 63 | 4 | 6 | 7 | 0 | 0 |
| [G04 Layers, transports, and provenance](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md) | IV, 0, I, XVI | 68 / 98 | 118 | 139 | 17 | 85 | 34 | 111 | 1 | 10 | 11 | 6 | 0 |
| [G05 Account](groups/05%20Account%20%28Part%20V%29.md) | V, I, XVI | 52 / 68 | 153 | 130 | 15 | 81 | 42 | 95 | 9 | 10 | 16 | 0 | 0 |
| [G06 Work, routes, and interference](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md) | VI | 61 / 67 | 143 | 157 | 107 | 157 | 23 | 102 | 16 | 14 | 14 | 11 | 0 |
| [G07 Exact constructions](groups/07%20Exact%20constructions%20%28Part%20VII%29.md) | VII, 0 | 32 / 48 | 42 | 55 | 4 | 25 | 2 | 46 | 1 | 4 | 4 | 0 | 0 |
| [G08 Transport results](groups/08%20Transport%20results%20%28Part%20VIII%29.md) | VIII, XVI | 21 / 27 | 37 | 44 | 9 | 37 | 4 | 28 | 2 | 4 | 10 | 0 | 0 |
| [G09 Criticism, use, and usable arguments](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md) | IX, 0, I | 40 / 51 | 65 | 70 | 9 | 48 | 1 | 60 | 2 | 1 | 6 | 1 | 0 |
| [G10 Understanding, construction, and origin](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md) | X, XVI | 49 / 80 | 105 | 119 | 9 | 59 | 34 | 92 | 14 | 6 | 7 | 0 | 0 |
| [G11 Repair, created explanation, and appraisal](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md) | XI, 0 | 26 / 27 | 77 | 81 | 6 | 46 | 29 | 63 | 3 | 8 | 5 | 2 | 0 |
| [G12 The physical module](groups/12%20The%20physical%20module%20%28Part%20XII%29.md) | XII, I | 23 / 35 | 50 | 49 | 6 | 16 | 12 | 46 | 0 | 2 | 1 | 0 | 0 |
| [G13 Recursion and universality](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md) | XIII, I | 7 / 14 | 22 | 16 | 0 | 11 | 22 | 14 | 1 | 0 | 1 | 0 | 0 |
| [G14 The class collected](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md) | XIV, 0, XVI | 50 / 55 | 116 | 141 | 24 | 144 | 19 | 114 | 11 | 9 | 6 | 1 | 0 |
| [G15 What would rule this class out](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md) | XV, 0 | 16 / 18 | 89 | 115 | 12 | 43 | 3 | 90 | 1 | 21 | 3 | 0 | 0 |
| [G16 Vocabulary across the text](groups/16%20Vocabulary%20across%20the%20text.md) | — | — | 46 | 88 | 1 | — | — | 50 | 0 | 1 | 32 | 5 | 0 |

In G16 the records shown in full are its vocabulary records and its records with no sentence; its units are those of G01 to G15.

## The text in order

Every section of the latest text, in text order, with the group file that shows it.

| Part | section | lines | group | units (touched / all) | records shown |
| --- | --- | --- | --- | --- | --- |
| Front matter | Opening of the Part | lines 1–2 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L1-2) | 4 / 8 | 6 |
| Front matter | A structural class of explanatory creativity, with selected and constructed correspondence | line 3 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L3-3) | 0 / 1 | 0 |
| Part 0 | Opening of the Part | line 7 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L7-7) | 0 / 1 | 0 |
| Part 0 | Two words, as used here | line 8 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L8-8) | 7 / 9 | 9 |
| Part 0 | What this document claims | lines 9–17 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L9-17) | 13 / 19 | 41 |
| Part 0 | What this document does not claim | lines 19–27 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L19-27) | 10 / 13 | 37 |
| Part 0 | What is imported, what is an index, and what is defined | lines 29–31 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L29-31) | 5 / 5 | 38 |
| Part 0 | Grievances, anticipated / introduction | lines 33–35 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L33-35) | 1 / 2 | 17 |
| Part 0 | Grievances, anticipated / 1. "Without declared kinds you cannot tell a cause from a correlation." | line 37 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L37-37) | 2 / 4 | 4 |
| Part 0 | Grievances, anticipated / 2. "So this is operationalism: a thing is what you can do to it." | line 39 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L39-39) | 2 / 5 | 4 |
| Part 0 | Grievances, anticipated / 3. "If correspondences are selected, you have made fidelity a matter of survival." | line 41 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L41-41) | 4 / 4 | 12 |
| Part 0 | Grievances, anticipated / 4. "Then everything is relative to a contract of admitted changes, and nothing is independent of the modeller." | line 43 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L43-43) | 5 / 5 | 19 |
| Part 0 | Grievances, anticipated / 5. "This is teleosemantics, structural realism or functionalism with new words." | line 45 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L45-45) | 3 / 5 | 5 |
| Part 0 | Grievances, anticipated / 6. "You have replaced explanation with evolution." | line 47 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L47-47) | 3 / 3 | 17 |
| Part 0 | Grievances, anticipated / 7. "Mathematics has no interventions." | line 49 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L49-49) | 5 / 5 | 14 |
| Part 0 | Grievances, anticipated / 8. "Where is aesthetics?" | line 51 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L51-51) | 3 / 3 | 12 |
| Part 0 | Grievances, anticipated / 9. "'Selected' is as much a stipulation as 'is a cause'." | line 53 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L53-53) | 3 / 3 | 6 |
| Part 0 | Grievances, anticipated / 10. "Freezing the question for assessment while letting questions change across episodes is having it both ways." | line 55 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L55-55) | 3 / 4 | 7 |
| Part 0 | Grievances, anticipated / 11. "Kinds exist. A rule is not a cause." | line 57 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L57-57) | 3 / 3 | 5 |
| Part 0 | Where to attack this | lines 59–61 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L59-61) | 2 / 4 | 20 |
| Part I | Opening of the Part | line 65 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L65-65) | 0 / 1 | 0 |
| Part I | Faithfulness without assessors | line 67 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L67-67) | 2 / 2 | 11 |
| Part I | Fallibility without error-as-work | line 69 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L69-69) | 3 / 3 | 10 |
| Part I | Conjecture, criticism, action | line 71 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L71-71) | 3 / 3 | 4 |
| Part I | Recursive scrutiny with operative return | line 73 | [G13](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md#sec-L73-73) | 1 / 1 | 1 |
| Part I | Substrate independence with physical conditions | line 75 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L75-75) | 6 / 7 | 20 |
| Part I | Two provenances, not one | line 77 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L77-77) | 0 / 3 | 0 |
| Part II | Opening of the Part | line 81 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L81-81) | 0 / 1 | 0 |
| Part II | Organizations | lines 83–105 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L83-105) | 1 / 18 | 5 |
| Part II | Roles are defined, not supplied | lines 107–109 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L107-109) | 2 / 6 | 4 |
| Part II | Kinds are edit-signatures | lines 111–127 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L111-127) | 11 / 21 | 34 |
| Part III | Opening of the Part | line 131 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L131-131) | 0 / 1 | 0 |
| Part III | Contracts | lines 133–147 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L133-147) | 3 / 10 | 5 |
| Part III | The respect is the query | lines 149–151 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L149-151) | 7 / 8 | 35 |
| Part III | Contracts have provenance | lines 153–155 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L153-155) | 4 / 7 | 7 |
| Part III | Scope, and a question that can be in error | lines 157–161 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L157-161) | 10 / 13 | 41 |
| Part IV | Opening of the Part | line 165 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L165-165) | 0 / 1 | 0 |
| Part IV | Occurrences and contents | lines 167–169 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L167-169) | 0 / 4 | 0 |
| Part IV | The object layer and the simulation layer | lines 171–179 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L171-179) | 4 / 8 | 11 |
| Part IV | Transports | lines 181–189 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L181-189) | 2 / 5 | 2 |
| Part IV | Three provenances | lines 191–201 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L191-201) | 13 / 17 | 29 |
| Part IV | Representation is defined, not supplied | lines 203–213 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L203-213) | 6 / 9 | 27 |
| Part IV | Prediction, surprise, violation | lines 215–225 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L215-225) | 11 / 15 | 48 |
| Part V | Opening of the Part | lines 229–231 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L229-231) | 4 / 5 | 20 |
| Part V | Component fidelity | lines 233–245 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L233-245) | 6 / 8 | 21 |
| Part V | Question fidelity | lines 247–253 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L247-253) | 0 / 3 | 0 |
| Part V | Non-circular dependence | line 255 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L255-255) | 4 / 4 | 19 |
| Part V | Non-vacuity | line 257 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L257-257) | 3 / 3 | 7 |
| Part V | The conjunction (E) | lines 259–265 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L259-265) | 0 / 4 | 0 |
| Part V | What (E) excludes, and what it does not | lines 267–277 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L267-277) | 14 / 14 | 50 |
| Part V | Why there is no counterpart-kind condition | lines 279–281 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L279-281) | 5 / 6 | 10 |
| Part VI | Opening of the Part | lines 285–303 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L285-303) | 7 / 12 | 30 |
| Part VI | Finite monotone claim | line 305 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L305-305) | 5 / 5 | 15 |
| Part VI | Redundant routes | line 307 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L307-307) | 5 / 5 | 19 |
| Part VI | Interference | line 309 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L309-309) | 2 / 2 | 2 |
| Part VI | Infinitary routes | line 311 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L311-311) | 1 / 2 | 9 |
| Part VI | Commitments that do no work | line 313 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L313-313) | 3 / 3 | 21 |
| Part VI | Rivals | line 315 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L315-315) | 21 / 21 | 61 |
| Part VI | Problems | line 317 | [G06](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#sec-L317-317) | 17 / 17 | 73 |
| Part VII | Opening of the Part | line 321 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L321-321) | 1 / 1 | 3 |
| Part VII | Production and direction | lines 323–325 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L323-325) | 4 / 8 | 9 |
| Part VII | Identification | lines 327–331 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L327-331) | 6 / 10 | 14 |
| Part VII | Obstruction | lines 333–335 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L333-335) | 2 / 4 | 8 |
| Part VII | Explanations that remove structure | lines 337–339 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L337-339) | 4 / 6 | 16 |
| Part VII | Odd-order skew-symmetric matrices | lines 341–343 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L341-343) | 7 / 10 | 11 |
| Part VII | Constitutive rules | lines 345–347 | [G07](groups/07%20Exact%20constructions%20%28Part%20VII%29.md#sec-L345-347) | 3 / 4 | 1 |
| Part VIII | Opening of the Part | line 351 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L351-351) | 0 / 1 | 0 |
| Part VIII | Functional transport | line 353 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L353-353) | 3 / 4 | 7 |
| Part VIII | Relational transport | lines 355–361 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L355-361) | 0 / 4 | 0 |
| Part VIII | Approximate transport | line 363 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L363-363) | 4 / 4 | 11 |
| Part VIII | Recoding | line 365 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L365-365) | 2 / 2 | 7 |
| Part VIII | Historical index | line 367 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L367-367) | 2 / 2 | 5 |
| Part VIII | A failed answer stays failed | line 369 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L369-369) | 6 / 6 | 27 |
| Part IX | Opening of the Part | line 373 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L373-373) | 1 / 1 | 3 |
| Part IX | Histories | line 375 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L375-375) | 3 / 3 | 5 |
| Part IX | Bearing | lines 377–383 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L377-383) | 5 / 6 | 15 |
| Part IX | Reason use | line 385 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L385-385) | 1 / 2 | 7 |
| Part IX | Usability | lines 387–393 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L387-393) | 5 / 6 | 19 |
| Part IX | What a test rules out | line 395 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L395-395) | 1 / 1 | 8 |
| Part IX | Arguments | line 397 | [G09](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#sec-L397-397) | 14 / 20 | 38 |
| Part X | Opening of the Part | line 401 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L401-401) | 0 / 1 | 0 |
| Part X | Deployment | line 403 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L403-403) | 3 / 4 | 15 |
| Part X | Construction | line 405 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L405-405) | 5 / 5 | 23 |
| Part X | Representation in use; construction is not selection | lines 407–411 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L407-411) | 2 / 15 | 6 |
| Part X | Newness | lines 413–417 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L413-417) | 2 / 4 | 5 |
| Part X | Origin | lines 419–423 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L419-423) | 1 / 2 | 2 |
| Part X | What a new content may be | line 425 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L425-425) | 3 / 3 | 3 |
| Part X | Ownership | line 427 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L427-427) | 4 / 4 | 17 |
| Part X | Episodes | line 429 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L429-429) | 4 / 4 | 20 |
| Part XI | Opening of the Part | line 433 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L433-433) | 1 / 1 | 4 |
| Part XI | Repair | lines 435–439 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L435-439) | 3 / 3 | 10 |
| Part XI | The aims of a repair | line 441 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L441-441) | 6 / 6 | 33 |
| Part XI | Created explanation | lines 443–451 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L443-451) | 4 / 4 | 16 |
| Part XI | Result, and the index of (EX) | line 453 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L453-453) | 4 / 5 | 10 |
| Part XI | Appraisal | line 455 | [G11](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#sec-L455-455) | 5 / 5 | 36 |
| Part XII | Opening of the Part | line 459 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L459-459) | 0 / 1 | 0 |
| Part XII | Tasks | line 461 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L461-461) | 4 / 6 | 8 |
| Part XII | Retained realization | lines 463–469 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L463-469) | 1 / 3 | 4 |
| Part XII | Retention fixed point | line 471 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L471-471) | 0 / 2 | 0 |
| Part XII | System boundary and continuity | line 473 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L473-473) | 4 / 4 | 8 |
| Part XII | Owned capability | line 475 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L475-475) | 1 / 3 | 8 |
| Part XII | Achievement | line 477 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L477-477) | 1 / 2 | 1 |
| Part XII | Tolerances | line 479 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L479-479) | 3 / 4 | 11 |
| Part XII | Selection in the physical module | line 481 | [G12](groups/12%20The%20physical%20module%20%28Part%20XII%29.md#sec-L481-481) | 3 / 3 | 7 |
| Part XIII | Opening of the Part | line 485 | [G13](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md#sec-L485-485) | 0 / 1 | 0 |
| Part XIII | Scrutinizability | line 487 | [G13](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md#sec-L487-487) | 0 / 2 | 0 |
| Part XIII | Recursive capacity | lines 489–493 | [G13](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md#sec-L489-493) | 0 / 2 | 0 |
| Part XIII | Barriers | line 495 | [G13](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md#sec-L495-495) | 3 / 3 | 12 |
| Part XIII | Universality | lines 497–509 | [G13](groups/13%20Recursion%20and%20universality%20%28Part%20XIII%29.md#sec-L497-509) | 3 / 5 | 14 |
| Part XIV | Opening of the Part | line 513 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L513-513) | 0 / 1 | 0 |
| Part XIV | Imports | lines 515–518 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L515-518) | 3 / 3 | 16 |
| Part XIV | What everything else is defined from | line 520 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L520-520) | 8 / 8 | 13 |
| Part XIV | Declared inputs | line 522 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L522-522) | 3 / 3 | 33 |
| Part XIV | Indices, not imports | line 524 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L524-524) | 4 / 4 | 9 |
| Part XIV | Dependence order | line 526 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L526-526) | 18 / 18 | 62 |
| Part XIV | Membership | line 528 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L528-528) | 2 / 6 | 5 |
| Part XV | Opening of the Part | lines 532–534 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L532-534) | 4 / 4 | 17 |
| Part XV | (Suff) Sufficiency | line 536 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L536-536) | 3 / 3 | 29 |
| Part XV | (Nec) Necessity | line 538 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L538-538) | 2 / 2 | 18 |
| Part XV | (Elim) Reinstatement of kinds | line 540 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L540-540) | 2 / 2 | 20 |
| Part XV | (Prov) Genesis | line 542 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L542-542) | 1 / 1 | 27 |
| Part XV | (QF) Question-finding | line 544 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L544-544) | 1 / 1 | 19 |
| Part XV | A mathematical error | line 546 | [G15](groups/15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#sec-L546-546) | 1 / 1 | 7 |
| Part XVI | Opening of the Part | line 550 | [G01](groups/01%20The%20document%20as%20a%20whole.md#sec-L550-550) | 1 / 1 | 3 |
| Part XVI | 1. Kind preservation needs no condition of its own | lines 552–558 | [G02](groups/02%20Organizations%20and%20their%20changes%20%28Part%20II%29.md#sec-L552-558) | 6 / 8 | 13 |
| Part XVI | 2. Same counterparts, one account | lines 560–568 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L560-568) | 9 / 11 | 29 |
| Part XVI | 3. Selected transports are underdetermined on unseen changes their population leaves open | lines 570–576 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L570-576) | 11 / 13 | 35 |
| Part XVI | 4. Surprise requires an incomplete history | lines 578–584 | [G04](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#sec-L578-584) | 8 / 8 | 17 |
| Part XVI | 5. Question-finding is representable | lines 586–592 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L586-592) | 8 / 11 | 34 |
| Part XVI | 6. There are two imports | lines 594–600 | [G14](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#sec-L594-600) | 7 / 7 | 33 |
| Part XVI | 7. The frozen assessment and the moving question are consistent | lines 602–608 | [G03](groups/03%20Questions%20%28Part%20III%29.md#sec-L602-608) | 7 / 8 | 18 |
| Part XVI | 8. Equivariance under structure-preserving recoding | lines 610–612 | [G08](groups/08%20Transport%20results%20%28Part%20VIII%29.md#sec-L610-612) | 4 / 4 | 6 |
| Part XVI | 9. Output descriptions do not determine accounts | lines 614–616 | [G05](groups/05%20Account%20%28Part%20V%29.md#sec-L614-616) | 2 / 5 | 5 |
| Part XVI | 10. A two-layer episode, in exact form | lines 618–632 | [G10](groups/10%20Understanding%2C%20construction%2C%20and%20origin%20%28Part%20X%29.md#sec-L618-632) | 17 / 27 | 53 |

## Records open for the owner

The 26 records whose status is `open for the owner`.

| record | change | round | group | shown in full at |
| --- | --- | --- | --- | --- |
| C-131 | CH-0504 | S90 | G04 | [L205.s1](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L205-s1) |
| C-156 | CH-0529 | S93 | G06 | [L315.s13](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s13) |
| C-157 | CH-0530 | S93 | G06 | [L315.s21](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s21) |
| C-158 | CH-0531 | S93 | G06 | [L315.s21](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s21) |
| C-159 | CH-0532 | S93 | G06 | [L315.s14](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s14) |
| C-160 | CH-0533 | S93 | G06 | [L315.s1](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s1) |
| C-161 | CH-0534 | S93 | G09 | [L397.s13](groups/09%20Criticism%2C%20use%2C%20and%20usable%20arguments%20%28Part%20IX%29.md#L397-s13) |
| E-12 | CH-1239 | S94 | G06 | [L315.s1](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s1) |
| E-13 | CH-1240 | S94 | G06 | [L315.s7](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s7) |
| E-14 | CH-1241 | S94 | G14 | [L526.s15](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#L526-s15) |
| E-27 | CH-1239 | S94 | G06 | [L315.s1](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s1) |
| E-28 | CH-1240 | S94 | G06 | [L315.s7](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L315-s7) |
| D-591 | CH-1132 | S95 | G16 | [L31.s4](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#L31-s4) |
| D-698 | CH-1132 | S95 | G16 | [L528.s3](groups/14%20The%20class%20collected%20%28Part%20XIV%29.md#L528-s3) |
| D-763 | CH-1199 | S95 | G04 | [L221.s1](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L221-s1) |
| D-764 | CH-1200 | S95 | G16 | [L215.s1](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L215-s1) |
| D-765 | CH-1201 | S95 | G04 | [L215.s1](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L215-s1) |
| D-766 | CH-1202 | S95 | G16 | [L223.s5](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L223-s5) |
| D-775 | CH-1206 | S95 | G11 | [L455.s1](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#L455-s1) |
| D-785 | CH-1199 | S95 | G04 | [L221.s1](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L221-s1) |
| D-786 | CH-1200 | S95 | G04 | [L223.s5](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L223-s5) |
| D-787 | CH-1201 | S95 | G04 | [L215.s1](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L215-s1) |
| D-788 | CH-1202 | S95 | G16 | [L223.s5](groups/04%20Layers%2C%20transports%2C%20and%20provenance%20%28Part%20IV%29.md#L223-s5) |
| D-841 | CH-1206 | S95 | G11 | [L455.s1](groups/11%20Repair%2C%20created%20explanation%2C%20and%20appraisal%20%28Part%20XI%29.md#L455-s1) |
| D-873 | CH-1210 | S96 | G06 | [L317.s1](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L317-s1) |
| D-875 | CH-1211 | S96 | G06 | [L317.s1](groups/06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L317-s1) |

## Files and rerun

- `groups/01 … 16 *.md`: one file per group.
- `by idea.md`: the idea proposal's twenty ideas as a cross-index, with links to where each change is shown.
- `data/records.jsonl`: the 1850 records, each once, every field of `anchored.jsonl` first, then the `lineup_…` fields.
- `data/tree.json`: groups, sections, units and entries, by reference.
- `data/by sentence.csv`: one row per showing of a record, in the order of the views.
- `scripts/build.py`, `scripts/check.py`: the builder and its checks.
- Rerun from this folder: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build.py && PYTHONDONTWRITEBYTECODE=1 python3 scripts/check.py`.
