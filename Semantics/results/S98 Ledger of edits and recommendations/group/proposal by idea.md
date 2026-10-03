# S98 — a proposal for lumping the ledger: by idea

*Log S98, 26 September 2026, under the owner's instruction of that day (decision S30). This is one proposal for the grouping step of the ledger. It reads the 1850 records of `anchored.jsonl` (1275 changes after the anchor step joined duplicates) and places each change in the idea of the semantics that its sentences carry, across Parts. Nothing in `anchored.jsonl`, `collect/` or any theory text was changed, and nothing was committed. The page and `proposal by idea - assignment.jsonl` were written by `proposal by idea - scripts/write_proposal.py`, from `group_by_idea.py`, `ideas.py` (the lens as first tried) and `ideas_v2.py` (the one adjustment).*

## The metric

A change goes to the idea its sentences carry. The idea of a sentence is read by program from two things: the words it uses that name an idea of the theory (the defined terms, tagged conditions and their near words, each weighted by how rare it is in the ledger's sentences and the latest text), and the heading or run-in label it stands under in the latest text. A change's sentences are its records' old and new sentences, its own old and new wording, and the latest-text sentences it is placed on, and the idea with the most weight over them is its group. Sizes below count changes; records are given beside them.

## The groups

The ideas follow the order in which the theory first takes them up. *Also* counts the changes of the group whose sentences give a second idea at least half the weight of the first; *where its changes stand* counts each change once, by the Part of its first latest-text sentence (or the Part its source names when it has none).

| # | idea | rule | changes | records | also | where its changes stand |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **The document's frame: title, claims, sources and departures** (`frame`) | sentences about the document itself: its title, what it claims and does not claim as a whole, its note of sources and departures, its revision notes | 21 | 28 | 8 | Part 0 11, Front 6, Part VIII 2, Part XIV 1, no Part 1 |
| 2 | **Organizations, roles and kinds** (`organization`) | sentences about organizations, their components and ports, roles, kinds as edit-signatures, levels, and substrate | 63 | 80 | 29 | Part II 24, Part 0 11, Part XVI 7, Part V 6, Part I 6 … |
| 3 | **Questions, contracts and scope** (`question`) | sentences about questions, contracts of admitted changes, the respect as the query, scope, and a question that can be in error | 76 | 113 | 49 | Part III 22, Part V 14, Part 0 12, Part XVI 11, Part VIII 5 … |
| 4 | **Layers, transports and representation** (`layers`) | sentences about occurrences and contents, the object and simulation layers, transports and their results, recoding, and representation | 61 | 86 | 36 | Part IV 19, Part VIII 13, Part XVI 10, Part 0 7, Part II 4 … |
| 5 | **Provenance: selected, constructed and declared correspondence** (`provenance`) | sentences about where a correspondence comes from: selection, construction, declaration, their traces, and genesis | 45 | 89 | 34 | Part 0 17, Part IV 10, Part XVI 6, Part X 5, Part XII 2 … |
| 6 | **Prediction, surprise and violation** (`surprise`) | sentences about prediction, expectation, violation and surprise | 34 | 57 | 17 | Part IV 25, Part XVI 7, Part 0 1, no Part 1 |
| 7 | **What an account requires** (`account`) | sentences about the conditions of (E) on an account: component and question fidelity, non-circular dependence, non-vacuity, and what (E) excludes | 129 | 194 | 71 | Part V 76, Part XVI 15, Part 0 12, Part VI 7, no Part 3 … |
| 8 | **Work, routes and commitments that do no work** (`work`) | sentences about routes, criticality, interference, redundant and infinitary routes, and commitments that do no work (easy to vary) | 69 | 97 | 17 | Part VI 57, Part V 9, Part IX 2, Part XII 1 |
| 9 | **Rivals, conflict and problems** (`rivals`) | sentences about rivals, conflict between candidates, and the problems two rivals pose | 33 | 43 | 22 | Part VI 26, Part VII 3, Part 0 3, no Part 1 |
| 10 | **Ruling out and tentative acceptance** (`ruling`) | sentences about what an assessor rules out or leaves not ruled out, tentative acceptance, and the words for how a claim is held | 57 | 83 | 40 | Part 0 18, Part VI 18, Part I 10, Part VIII 3, Part IX 2 … |
| 11 | **Exact constructions and mathematics** (`constructions`) | sentences about the exact constructions: production and direction, identification, obstruction, removing structure, skew-symmetric matrices, constitutive rules, and mathematics | 33 | 43 | 15 | Part VII 16, Part 0 6, Part III 6, Part V 3, Part XIII 1 … |
| 12 | **Arguments, premises and tests** (`argument`) | sentences about what an argument is (why this and not that), its steps, premises and record leaves, bearing, usability, reason use, and tests | 114 | 175 | 65 | Part IX 38, Part VI 24, Part 0 12, Part IV 7, Part V 5 … |
| 13 | **Criticism, error and repair** (`criticism`) | sentences about criticism and its use, error and defects, recognized difficulties, aims and repair | 71 | 96 | 42 | Part XI 33, Part IX 10, Part I 7, Part XVI 5, Part III 3 … |
| 14 | **Creativity, understanding and origin** (`creativity`) | sentences about understanding, deployment, construction, newness, origin, ownership, episodes, created explanation and question-finding | 87 | 135 | 52 | Part X 39, Part 0 12, Part XVI 10, Part XI 9, Part IV 4 … |
| 15 | **Aims, values and appraisal** (`appraisal`) | sentences about the appraisal relation, values and aesthetics, and how aims are appraised | 46 | 65 | 10 | Part XI 21, Part 0 15, Part XVI 5, Part V 2, Part VII 2 … |
| 16 | **Physical possibility and the physical module** (`physical`) | sentences about the physical module, what is physically possible or admitted, tasks, retention, boundary and continuity, capability, tolerances | 47 | 74 | 18 | Part XII 28, Part 0 6, Part XIII 4, Part X 4, Part I 2 … |
| 17 | **Recursion, scrutiny and universality** (`recursion`) | sentences about scrutinizability, recursive capacity, barriers and universality | 12 | 18 | 7 | Part XIII 11, Part I 1 |
| 18 | **Imports, declared inputs and the dependence order** (`inputs`) | sentences about the two imports, declared inputs and indices, what is defined from what, the dependence order and membership of the class | 127 | 192 | 76 | Part XIV 68, Part 0 31, Part XVI 17, Part VIII 3, Part III 2 … |
| 19 | **What would rule the class out** (`ruleout`) | sentences stating the cases that would rule the class out (sufficiency, necessity, reinstatement of kinds, genesis, question-finding) and where to attack it | 73 | 105 | 60 | Part XV 66, Part 0 4, Part VII 2, no Part 1 |
| 20 | **Form only: punctuation, emphasis, pointers and labels** (`form`) | changes that alter no wording of an idea: punctuation, bold or italics, a Part or Argument pointer, a tag number, or the labels `Derivation` and `Proof` renamed | 77 | 77 | 0 | Part 0 21, Part XVI 21, Part XV 7, Part V 6, Part VI 6 … |
| | **all** | | 1275 | 1850 | 668 | |

## How a change that touches several places is placed

Every change has one group. Its weight is summed over all its sentences: the mean idea profile of its records' sentences, plus the mean profile of the latest-text sentences it stands on (each carrying the idea of its heading or label), plus half the profile of its own old and new wording. A vocabulary entry (scope `term`) has no sentence of its own, so its own wording counts three times the weight of its places. The group is the idea with the most weight; every other idea with at least half that weight (and at least 0.15 of the whole) is listed in *also* in the assignment, so a reader of one idea can find the changes it shares with another. Two exceptions come first. A change all of whose sentences stand in a place that speaks of the other ideas as a whole (the front matter; Part 0, *What is imported, what is an index, and what is defined*; Part XIV; Part XV) goes to that place's idea, and the idea its words name goes to *also*. A change that alters only punctuation, emphasis, a pointer, a tag number or a label goes to *Form only*, with the idea of its sentence in *also*. A change with no place in the latest text uses the sentence named in `latest_nearest`, if any, and the idea of the Part its source names, at equal weight. The records of one change stay together; `records_alone` in the assignment file gives the group each record would take by itself.

## How the lens was tried and adjusted once

**First try (version 1).** Nineteen ideas, each with a list of words and a home among the headings and labels of the latest text (the examples in the task, with the Part 0 grievances, the Part I commitments and the numbered arguments of Part XVI sent to the idea each discusses). Measured on all 1275 changes:

- changes with a second idea at half the weight of the first or more: 747 (1061 records); near ties, a second idea at three quarters or more: 387;
- changes whose first idea has under 0.30 of the weight: 156;
- changes placed by their place alone, their wording naming no idea: 45; by nothing at all: 0;
- three faults a reader following the theory would meet. The words the theory now uses everywhere ("argument", "rules out", "record", "contract", "declared") pulled sentences about rivals, problems and prediction into *Arguments* and *Ruling out*. The old words the S95 scrub replaced (`true`, `established`, `fits`, `proves` …) stood in sentences of every idea, so a scrub edit went to *Ruling out* whatever its sentence said. The sentences that speak of the ideas as a whole (the dependence order of Part XIV, the cases of Part XV) were scattered over the ideas they name: only 18 of the 78 changes standing in Part XV reached *What would rule the class out*, and 38 of the 77 in Part XIV reached *Imports, declared inputs and the dependence order*. Pointer and punctuation edits sat in whichever idea their sentence had, among edits of wording.

**The adjustment (version 2), made once, in four parts** (`ideas_v2.py`):

1. Each word's weight is scaled by how rare it is (the logarithm of the number of sentences over the number holding it, divided by the median, kept between 0.4 and 1.6). The first word of each idea, the one that names it, keeps at least its full weight.
2. The list of old scrub words in *Ruling out* is narrowed to the ones about ruling out and holding a claim (`refute`, `reject`, `verdict`, `justification`, `certify`).
3. The places that speak of the ideas as a whole carry their own idea with double weight, and a change standing only there goes to that idea.
4. A twentieth group, *Form only*, takes the changes that alter no wording of an idea.

Version 2 moved 271 changes. The largest moves: argument → form 27, organization → form 15, account → ruleout 11, appraisal → inputs 10, ruling → ruleout 9, provenance → ruleout 8, creativity → ruleout 7, creativity → inputs 7.

| idea | v1 changes | v2 changes |
| --- | --- | --- |
| The document's frame: title, claims, sources and departures | 18 | 21 |
| Organizations, roles and kinds | 84 | 63 |
| Questions, contracts and scope | 88 | 76 |
| Layers, transports and representation | 63 | 61 |
| Provenance: selected, constructed and declared correspondence | 54 | 45 |
| Prediction, surprise and violation | 30 | 34 |
| What an account requires | 143 | 129 |
| Work, routes and commitments that do no work | 69 | 69 |
| Rivals, conflict and problems | 38 | 33 |
| Ruling out and tentative acceptance | 78 | 57 |
| Exact constructions and mathematics | 33 | 33 |
| Arguments, premises and tests | 149 | 114 |
| Criticism, error and repair | 75 | 71 |
| Creativity, understanding and origin | 110 | 87 |
| Aims, values and appraisal | 58 | 46 |
| Physical possibility and the physical module | 49 | 47 |
| Recursion, scrutiny and universality | 12 | 12 |
| Imports, declared inputs and the dependence order | 98 | 127 |
| What would rule the class out | 26 | 73 |
| Form only: punctuation, emphasis, pointers and labels | 0 | 77 |

## Measures of the final lens

- **Groups:** 20. Sizes from 12 to 129 changes; the two middle sizes are 61 and 63.
- **In more than one group.** None by assignment: each change has one group. 668 changes (964 records) name a second idea in *also* at half the weight or more, and 302 are near ties (three quarters or more). The theory's sentences often carry two ideas at once (a conflict defined through (F1), (F2) and (A); an argument about kinds), and *also* keeps that visible.
- **In no group.** None: every change is placed. 49 changes have wording that names no idea and are placed by where they stand alone; 7 have no place and no Part (notes and whole-text changes) and are placed by their wording alone. 95 changes placed by weight give their first idea under 0.30 of the whole: these are the first to read when reviewing.
- **Rules used:** most weight 1112, place that speaks of the ideas as a whole 86, form only 77.
- **Changes of several records:** 281. In 78 of them the records, placed one by one, would go to more than one idea (178 records would leave their change's group). The large chains the anchor step flagged cross ideas in this way:

| change | records | group | the records placed alone |
| --- | --- | --- | --- |
| CH-0152 | 18 | account | question 7, account 6, constructions 4, argument 1 |
| CH-1018 | 15 | argument | creativity 4, criticism 3, account 3, argument 3, physical 2 |
| CH-0244 | 14 | provenance | provenance 7, ruleout 4, form 1, appraisal 1, layers 1 |
| CH-0148 | 13 | account | account 8, argument 2, criticism 2, physical 1 |
| CH-0997 | 13 | ruleout | ruleout 11, ruling 1, layers 1 |
| CH-0143 | 12 | provenance | provenance 8, ruleout 4 |
| CH-1131 | 11 | inputs | question 3, inputs 2, account 2, ruling 1, layers 1, appraisal 1, provenance 1 |
| CH-0437 | 10 | surprise | surprise 6, criticism 2, provenance 1, layers 1 |

- **Does each group read as one part of the semantics?** Read by sampling changes of each group with their sentences (ten for most groups; all 77 of *Form only*). Groups that come out as one idea: *Organizations, roles and kinds*, *Questions, contracts and scope*, *Prediction, surprise and violation*, *What an account requires*, *Work, routes and commitments that do no work*, *Exact constructions*, *Creativity, understanding and origin*, *Aims, values and appraisal*, *Physical possibility*, *Recursion*, *Imports, declared inputs and the dependence order*, *What would rule the class out*, *Form only*. Groups with a seam: *Arguments, premises and tests* holds both what an argument is (Part IX) and scrub edits that put arguments into sentences about rivals and problems (24 changes stand in Part VI); *Ruling out and tentative acceptance* and *Rivals, conflict and problems* share the sentences of Part VI that define each through the other, which is where most near ties fall; *Provenance: selected, constructed and declared correspondence* has the lowest mean weight share of the groups placed by weight (0.41), because its sentences also speak of layers, transports and construction. A few strays sit in each group, most often scrub vocabulary entries whose new words name one idea while their places stand in another.

## Strengths

- It follows what a sentence says, not where it stands: a grievance in Part 0, a commitment in Part I, the numbered arguments of Part XVI and the dependence order's sentences each join the idea they discuss, so a reader of one idea sees every change to it across the text in one place.
- It is made by program from the sentences only, with no use of the reasons in the sources, and every choice leaves its weights in the assignment file (`shares`, `also`, `near_tie`, `rule`), so any placement can be reread and moved by hand.
- The records that never reached a text (collector A's proposals against file 20, notes) still get an idea from their own wording, where a grouping by place has only the Part their source names.
- *Form only* keeps 77 pointer, punctuation and label edits out of the idea groups, and *also* shows where one sentence carries two ideas instead of hiding it.

## Weaknesses

- The word lists are Claude's reading of the theory's vocabulary; a different reader would draw some lines elsewhere, most of all between *Ruling out*, *Arguments* and *Rivals*, whose sentences in Part VI define each idea through the others.
- Many changes carry two ideas (668 have a second at half weight or more), so a one-group assignment hides part of what they touch unless *also* is read.
- A change is placed as a whole. Where the anchor step joined a chain of restatements (CH-0152, CH-1018, CH-1131), its records sit in one idea although, read alone, they spread over several; these chains would be split before the line-up.
- Changes with no place in the latest text (181: 82 with a nearest sentence, 92 with only the Part their source names, 7 with neither) are placed by their own wording and a Part, and are the least sure; 141 of them are collector A's, most of these proposals against file 20. Some requirements on an account written with the word *question* went to *Questions* rather than *What an account requires*.
- The exceptions for Part XIV and Part XV make those two groups mostly Part-shaped; a reader who wants a Part XV case under the idea it tests must use *also*.

## Files and rerun

- `proposal by idea - assignment.jsonl`: one line per change: `change_id`, `group`, `group_name`, `also`, `near_tie`, `rule`, `shares` (the four heaviest ideas and their shares), `records`, `records_alone`, `placed_by`, `place`, `latest_sentences`, `parts`, `statuses`, `kinds`.
- `proposal by idea - scripts/`: `ideas.py` (the lexicon and the homes), `ideas_v2.py` (the adjustment), `group_by_idea.py` (the placing and the measures), `write_proposal.py` (this page).
- Rerun: `PYTHONDONTWRITEBYTECODE=1 python3 write_proposal.py` in the scripts folder; the output is the same bytes.
- Inputs read: `anchored.jsonl` md5 41752268722000a376a15e7de2bde76e; `sentence index of the latest text.jsonl` md5 fdaf069a0c1d71be4e17b38d2f6bce82.

## The assignment: change → group

In change order. *Idea* is the group's number and key from the table above; *also* lists the second ideas; *sentences* gives up to three latest-text sentences the change stands on (`—` when it has none; then *Part* is the one its source names).

| change | idea | also | records | Part | sentences |
| --- | --- | --- | --- | --- | --- |
| CH-0001 | 7 `account` | question, criticism | A-1 | Part 0 | L43.s4 |
| CH-0002 | 7 `account` | question, inputs | A-2 | Part XI | L453.s5 |
| CH-0003 | 14 `creativity` | question | A-3 | Part X | L425.s1, L425.s2 |
| CH-0004 | 13 `criticism` | — | A-4 | Part XI | L441.s2 |
| CH-0005 | 19 `ruleout` | argument | A-5 | Part XV | L536.s2 |
| CH-0006 | 7 `account` | — | A-6 | Part V | L269.s2 |
| CH-0007 | 7 `account` | question, constructions | A-7 | Part V | L271.s2 |
| CH-0008 | 19 `ruleout` | appraisal | A-8 | Part XV | L536.s1 |
| CH-0009 | 19 `ruleout` | account | A-9 | Part XV | L536.s2 |
| CH-0010 | 19 `ruleout` | — | A-10 | Part XV | L538.s1 |
| CH-0011 | 19 `ruleout` | — | A-11 | Part XV | L540.s1 |
| CH-0012 | 5 `provenance` | frame, layers | A-12 | Part 0 | — |
| CH-0013 | 19 `ruleout` | creativity | A-13 | Part XV | L544.s1 |
| CH-0014 | 19 `ruleout` | physical | A-14 | Part XV | L544.s1 |
| CH-0015 | 19 `ruleout` | account, layers | A-15 | Part XV | L536.s1 |
| CH-0016 | 19 `ruleout` | — | A-16 | Part XV | L536.s1 |
| CH-0017 | 19 `ruleout` | physical | A-17 | Part XV | L538.s1 |
| CH-0018 | 19 `ruleout` | — | A-18 | Part XV | L538.s2 |
| CH-0019 | 19 `ruleout` | account | A-19 | Part XV | L540.s1 |
| CH-0020 | 19 `ruleout` | ruling, layers, provenance | A-20 | Part XV | L540.s1, L540.s2 |
| CH-0021 | 19 `ruleout` | provenance, argument, creativity | A-21 | Part XV | L542.s1 |
| CH-0022 | 19 `ruleout` | provenance | A-22 | Part XV | L544.s1 |
| CH-0023 | 20 `form` | ruleout | A-23 | Part XV | L546.s1 |
| CH-0024 | 19 `ruleout` | — | A-24 | Part XV | L544.s1 |
| CH-0025 | 19 `ruleout` | account, question | A-25 | Part XV | L542.s1 |
| CH-0026 | 7 `account` | organization | A-26 | Part V | L281.s3 |
| CH-0027 | 7 `account` | question | A-27 | Part V, Part 0 … | — |
| CH-0028 | 7 `account` | — | A-28 | Part V | — |
| CH-0029 | 3 `question` | account | A-29 | Part V | — |
| CH-0030 | 7 `account` | — | A-30 | Part V | — |
| CH-0031 | 13 `criticism` | account | A-31 | Part V | — |
| CH-0032 | 3 `question` | account | A-32 | Part V | — |
| CH-0033 | 7 `account` | criticism, question | A-33 | Part V | — |
| CH-0034 | 15 `appraisal` | account | A-34 | Part V | — |
| CH-0035 | 7 `account` | — | A-35 | Part V | — |
| CH-0036 | 7 `account` | appraisal, question | A-36 | Part V | — |
| CH-0037 | 7 `account` | question, inputs | A-37 | Part V | — |
| CH-0038 | 7 `account` | — | A-38 | Part V | — |
| CH-0039 | 7 `account` | inputs, question | A-39 | Part V | — |
| CH-0040 | 13 `criticism` | account | A-40 | Part V | — |
| CH-0041 | 7 `account` | — | A-41 | Part V | — |
| CH-0042 | 7 `account` | — | A-42 | Part V | — |
| CH-0043 | 7 `account` | inputs, question | A-43 | Part V | — |
| CH-0044 | 12 `argument` | — | A-44 | Part V | — |
| CH-0045 | 12 `argument` | account, work | A-45 | Part V | — |
| CH-0046 | 8 `work` | — | A-46 | Part V | — |
| CH-0047 | 7 `account` | physical, work | A-47 | Part V | — |
| CH-0048 | 8 `work` | account | A-48 | Part V | — |
| CH-0049 | 11 `constructions` | account | A-49 | Part V | — |
| CH-0050 | 2 `organization` | account | A-50 | Part V | — |
| CH-0051 | 3 `question` | — | A-51 | Part V | — |
| CH-0052 | 7 `account` | physical, appraisal | A-52 | Part V | — |
| CH-0053 | 7 `account` | constructions, argument, provenance | A-53 | Part V | — |
| CH-0054 | 4 `layers` | account, question | A-54 | Part V | — |
| CH-0055 | 3 `question` | account | A-55 | Part V | — |
| CH-0056 | 3 `question` | — | A-56 | Part V | — |
| CH-0057 | 7 `account` | — | A-57 | Part V | — |
| CH-0058 | 7 `account` | — | A-58 | Part V | — |
| CH-0059 | 2 `organization` | account | A-59 | Part V | — |
| CH-0060 | 7 `account` | — | A-60 | Part V | — |
| CH-0061 | 7 `account` | — | A-61 | Part V | — |
| CH-0062 | 7 `account` | — | A-62 | Part V | — |
| CH-0063 | 7 `account` | work | A-63 | Part V | — |
| CH-0064 | 7 `account` | work | A-64 | Part V | — |
| CH-0065 | 7 `account` | — | A-65 | Part V | — |
| CH-0066 | 7 `account` | — | A-66 | Part V | — |
| CH-0067 | 2 `organization` | — | A-67 | Part II | — |
| CH-0068 | 2 `organization` | — | A-68 A-164 | Part II | — |
| CH-0069 | 2 `organization` | — | A-69 | Part II | — |
| CH-0070 | 4 `layers` | organization | A-70 | Part II | — |
| CH-0071 | 3 `question` | organization | A-71 | Part II | — |
| CH-0072 | 2 `organization` | — | A-72 | Part II | — |
| CH-0073 | 6 `surprise` | layers | A-73 | Part IV | — |
| CH-0074 | 4 `layers` | — | A-74 A-75 A-165 A-166 A-167 | Part IV | — |
| CH-0075 | 4 `layers` | — | A-76 | Part IV | — |
| CH-0076 | 4 `layers` | — | A-77 A-168 A-169 | Part IV | — |
| CH-0077 | 4 `layers` | — | A-78 | Part IV | — |
| CH-0078 | 4 `layers` | — | A-79 A-80 A-170 | Part IV | — |
| CH-0079 | 4 `layers` | frame, surprise | A-81 A-171 | Part IV | — |
| CH-0080 | 6 `surprise` | layers | A-82 | Part IV | — |
| CH-0081 | 12 `argument` | — | A-83 | Part IV, Part X | — |
| CH-0082 | 2 `organization` | provenance | A-84 A-172 A-173 | Part IV, Part X | — |
| CH-0083 | 16 `physical` | provenance, layers, creativity | A-85 | Part IV, Part X | — |
| CH-0084 | 4 `layers` | creativity | A-86 | Part IV, Part X | — |
| CH-0085 | 14 `creativity` | — | A-87 A-89 A-174 A-175 A-176 A-177 A-178 | Part X | L405.s1 |
| CH-0086 | 14 `creativity` | layers, criticism | A-88 A-179 A-180 | Part IV, Part X | — |
| CH-0087 | 14 `creativity` | provenance, argument | A-90 | Part IV, Part X | — |
| CH-0088 | 14 `creativity` | — | A-91 A-92 A-181 | Part IV, Part X | — |
| CH-0089 | 18 `inputs` | — | A-93 | Part XIV, Part XVI | — |
| CH-0090 | 4 `layers` | inputs, argument, creativity | A-94 A-95 A-182 A-183 | Part XIV, Part XVI | — |
| CH-0091 | 16 `physical` | — | A-96 A-184 | Part XIV, Part XVI | — |
| CH-0092 | 5 `provenance` | inputs, layers | A-97 A-188 | Part XIV, Part XVI | — |
| CH-0093 | 18 `inputs` | layers, argument | A-98 A-100 A-185 A-186 | Part XIV, Part XVI | — |
| CH-0094 | 12 `argument` | layers, inputs | A-99 | Part XIV, Part XVI | — |
| CH-0095 | 1 `frame` | inputs, argument, layers | A-101 A-187 | Part XIV, Part XVI | — |
| CH-0096 | 14 `creativity` | — | A-102 A-189 | Part XIV, Part XVI | — |
| CH-0097 | 8 `work` | — | A-103 A-190 | Part VI | — |
| CH-0098 | 8 `work` | — | A-104 A-191 | Part VI | — |
| CH-0099 | 8 `work` | — | A-105 | Part VI | — |
| CH-0100 | 8 `work` | organization, ruling | A-106 A-107 A-192 | Part VI | — |
| CH-0101 | 12 `argument` | physical, work | A-108 | Part VI | — |
| CH-0102 | 8 `work` | argument, layers | A-109 A-193 A-194 | Part VI | — |
| CH-0103 | 12 `argument` | work | A-110 A-195 | Part VI | — |
| CH-0104 | 12 `argument` | work | A-111 A-196 | Part VI | — |
| CH-0105 | 3 `question` | organization, account, creativity | A-112 A-197 | Part XVI, Part III | — |
| CH-0106 | 3 `question` | — | A-113 | Part XVI, Part III | — |
| CH-0107 | 13 `criticism` | question, argument, creativity | A-114 A-198 | Part XVI, Part III | — |
| CH-0108 | 3 `question` | — | A-115 A-116 A-199 | Part XVI, Part III | — |
| CH-0109 | 3 `question` | — | A-117 A-118 A-200 A-201 A-202 | Part XVI, Part III | — |
| CH-0110 | 3 `question` | — | A-119 A-203 | Part III | — |
| CH-0111 | 14 `creativity` | appraisal, criticism | A-120 | Part X | — |
| CH-0112 | 14 `creativity` | — | A-121 A-204 A-205 | Part X | — |
| CH-0113 | 14 `creativity` | criticism | A-122 A-123 A-206 | Part X | — |
| CH-0114 | 14 `creativity` | criticism | A-124 | Part X | — |
| CH-0115 | 14 `creativity` | — | A-125 A-126 A-207 | Part X | — |
| CH-0116 | 14 `creativity` | — | A-127 A-208 A-210 | Part X | — |
| CH-0117 | 14 `creativity` | frame | A-128 A-209 | Part X | — |
| CH-0118 | 13 `criticism` | — | A-129 A-211 A-212 | Part XI | — |
| CH-0119 | 13 `criticism` | — | A-130 A-131 A-213 | Part XI | — |
| CH-0120 | 14 `creativity` | criticism | A-132 A-214 | Part XI | — |
| CH-0121 | 14 `creativity` | criticism, account | A-133 A-135 A-215 | Part XI | — |
| CH-0122 | 13 `criticism` | account | A-134 A-216 | Part XI | — |
| CH-0123 | 13 `criticism` | — | A-136 A-217 | Part XI | — |
| CH-0124 | 13 `criticism` | appraisal, inputs | A-137 | Part XI | — |
| CH-0125 | 13 `criticism` | — | A-138 A-218 | Part XI | — |
| CH-0126 | 15 `appraisal` | — | A-139 A-219 | Part XI | L455.s5 |
| CH-0127 | 16 `physical` | — | A-140 A-220 | Part XII | — |
| CH-0128 | 16 `physical` | creativity, organization | A-141 A-221 A-222 | Part XII | — |
| CH-0129 | 8 `work` | physical | A-142 | Part XII | — |
| CH-0130 | 16 `physical` | — | A-143 A-223 | Part XII | — |
| CH-0131 | 16 `physical` | — | A-144 A-224 | Part XII | — |
| CH-0132 | 14 `creativity` | recursion | A-145 A-146 A-225 | Part XIII | — |
| CH-0133 | 12 `argument` | recursion, layers, question | A-147 A-226 | Part XIII | — |
| CH-0134 | 17 `recursion` | — | A-148 A-227 | Part XIII | — |
| CH-0135 | 17 `recursion` | creativity | A-149 A-150 A-228 | Part XIII | — |
| CH-0136 | 11 `constructions` | recursion | A-151 | Part XIII | — |
| CH-0137 | 16 `physical` | recursion | A-152 | Part XIII | — |
| CH-0138 | 17 `recursion` | — | A-153 A-229 | Part XIII | — |
| CH-0139 | 12 `argument` | recursion | A-154 A-230 | Part XIII | — |
| CH-0140 | 17 `recursion` | — | A-155 | Part XIII | — |
| CH-0141 | 8 `work` | — | A-156 A-231 A-232 | Part VI | L299.s2 |
| CH-0142 | 4 `layers` | physical, criticism | A-157 A-158 A-233 | Part VIII | — |
| CH-0143 | 5 `provenance` | — | A-159 A-160 A-234 A-235 A-299 A-302 A-303 A-316 A-318 A-319 A-320 A-321 | Part XVI, Part 0 … | L572.s2, L41.s3, L576.s1 +1 |
| CH-0144 | 18 `inputs` | argument, creativity | A-161 A-236 | Part XVI | — |
| CH-0145 | 12 `argument` | — | A-162 | Part XVI | — |
| CH-0146 | 18 `inputs` | argument | A-163 A-237 | Part XVI | — |
| CH-0147 | 7 `account` | — | A-238 | Part V | — |
| CH-0148 | 7 `account` | — | A-239 A-240 A-241 A-246 A-247 A-248 A-249 A-250 A-251 A-252 A-259 A-283 A-304 | Part V, Part 0 … | — |
| CH-0149 | 3 `question` | — | A-242 | Part V, Part III | — |
| CH-0150 | 3 `question` | account | A-243 | Part V, Part III | — |
| CH-0151 | 12 `argument` | — | A-244 | Part V, Part III | — |
| CH-0152 | 7 `account` | question, constructions | A-245 A-253 A-254 A-255 A-256 A-257 A-258 A-260 A-261 A-262 A-263 A-264 A-265 A-266 A-267 A-282 A-284 A-305 | Part V, Part III … | — |
| CH-0153 | 14 `creativity` | criticism | A-268 | Part X | — |
| CH-0154 | 14 `creativity` | appraisal | A-269 | Part X | — |
| CH-0155 | 13 `criticism` | — | A-270 A-271 A-293 | Part XI | L441.s6 |
| CH-0156 | 14 `creativity` | argument, criticism | A-272 A-273 A-274 A-294 A-310 | Part XI, Part IX … | — |
| CH-0157 | 12 `argument` | creativity | A-275 A-276 A-277 A-297 A-315 | Part XIII, Part 0 … | — |
| CH-0158 | 13 `criticism` | — | A-278 A-279 A-280 A-295 A-311 | Part XI | — |
| CH-0159 | 3 `question` | account | A-281 | Part V | — |
| CH-0160 | 5 `provenance` | layers, rivals | A-285 A-306 | Part IV, Part X | — |
| CH-0161 | 14 `creativity` | — | A-286 A-309 | Part X | L405.s5 |
| CH-0162 | 4 `layers` | provenance, argument | A-287 | Part IV, Part IX | — |
| CH-0163 | 4 `layers` | — | A-288 | Part VIII | — |
| CH-0164 | 8 `work` | creativity | A-289 A-313 | Part VI, Part V | — |
| CH-0165 | 8 `work` | argument | A-290 A-312 | Part VI | — |
| CH-0166 | 3 `question` | — | A-291 | Part III | — |
| CH-0167 | 14 `creativity` | question | A-292 | Part III | L161.s5 |
| CH-0168 | 16 `physical` | creativity | A-296 A-314 | Part X, Part XII … | — |
| CH-0169 | 8 `work` | argument, appraisal | A-298 | Part VI | — |
| CH-0170 | 16 `physical` | argument | A-300 | Part XII, Part XIV … | — |
| CH-0171 | 18 `inputs` | argument | A-301 | Part XIV, Part XVI | — |
| CH-0172 | 14 `creativity` | — | A-307 | Part 0, Part X | — |
| CH-0173 | 12 `argument` | — | A-308 | Part IX | — |
| CH-0174 | 5 `provenance` | — | A-317 | Part XVI | L576.s1 |
| CH-0175 | 1 `frame` | — | B-1 | — | — |
| CH-0176 | 18 `inputs` | argument, creativity | B-2 | — | — |
| CH-0177 | 12 `argument` | ruling | B-3 | — | — |
| CH-0178 | 19 `ruleout` | question | B-4 | — | — |
| CH-0179 | 7 `account` | — | B-5 | — | — |
| CH-0180 | 2 `organization` | — | B-6 | Part 0 | L11.s2 |
| CH-0181 | 20 `form` | organization | B-7 | Part 0 | L11.s4 |
| CH-0182 | 4 `layers` | frame, inputs | B-8 | Part 0 | L13.s1 |
| CH-0183 | 5 `provenance` | criticism | B-9 | Part 0 | L13.s3 |
| CH-0184 | 1 `frame` | — | B-10 | Part 0 | L13.s4 |
| CH-0185 | 3 `question` | — | B-11 | Part 0 | L15.s2 |
| CH-0186 | 14 `creativity` | — | B-12 | Part 0 | L15.s3 |
| CH-0187 | 12 `argument` | frame | B-13 | Part 0 | L17.s4 |
| CH-0188 | 18 `inputs` | — | B-14 | Part 0 | L25.s2 |
| CH-0189 | 14 `creativity` | — | B-15 | Part 0 | L25.s3 |
| CH-0190 | 7 `account` | frame | B-16 | Part 0 | L23.s2 |
| CH-0191 | 20 `form` | argument | B-17 | Part 0 | L23.s3 |
| CH-0192 | 15 `appraisal` | — | B-18 | Part 0 | L25.s1 |
| CH-0193 | 14 `creativity` | frame | B-19 | Part 0 | L25.s3 |
| CH-0194 | 20 `form` | frame | B-20 | Part 0 | L27.s1 |
| CH-0195 | 18 `inputs` | — | B-21 | Part 0 | L29.s1 |
| CH-0196 | 18 `inputs` | appraisal, physical | B-22 | Part 0 | L31.s1 |
| CH-0197 | 18 `inputs` | question, physical | B-23 | Part 0 | L31.s2 |
| CH-0198 | 18 `inputs` | argument | B-24 | Part 0 | L31.s3 |
| CH-0199 | 18 `inputs` | argument | B-25 | Part 0 | L31.s4 |
| CH-0200 | 1 `frame` | — | B-26 | Part 0 | L35.s1 |
| CH-0201 | 2 `organization` | — | B-27 | Part 0 | L37.s3 |
| CH-0202 | 2 `organization` | account | B-28 | Part 0 | L37.s4 |
| CH-0203 | 20 `form` | organization | B-29 | Part 0 | L39.s2 |
| CH-0204 | 2 `organization` | — | B-30 | Part 0 | L39.s4 |
| CH-0205 | 5 `provenance` | layers | B-31 | Part 0 | L41.s3 |
| CH-0206 | 5 `provenance` | layers, account | B-32 | Part 0 | L41.s2 |
| CH-0207 | 5 `provenance` | layers, argument | B-33 | Part 0 | L41.s3 |
| CH-0208 | 7 `account` | — | B-34 | Part 0 | L43.s4 |
| CH-0209 | 20 `form` | question | B-35 | Part 0 | L43.s3 |
| CH-0210 | 16 `physical` | provenance | B-36 | Part 0 | L45.s1 |
| CH-0211 | 3 `question` | provenance | B-37 | Part 0 | L45.s5 |
| CH-0212 | 20 `form` | provenance | B-38 | Part 0 | L47.s1 |
| CH-0213 | 1 `frame` | — | B-39 | Part 0 | — |
| CH-0214 | 5 `provenance` | layers | B-40 | Part 0 | L47.s1 |
| CH-0215 | 10 `ruling` | provenance, creativity | B-41 | Part 0 | L47.s3 |
| CH-0216 | 20 `form` | constructions | B-42 | Part 0 | L49.s1 |
| CH-0217 | 11 `constructions` | — | B-43 | Part 0 | L51.s3 |
| CH-0218 | 20 `form` | organization | B-44 | Part 0 | L49.s2 |
| CH-0219 | 20 `form` | constructions | B-45 | Part 0 | L49.s3 |
| CH-0220 | 11 `constructions` | — | B-46 | Part 0 | L49.s1 |
| CH-0221 | 15 `appraisal` | — | B-47 | Part 0 | L51.s2 |
| CH-0222 | 15 `appraisal` | — | B-48 | Part 0 | L51.s3 |
| CH-0223 | 5 `provenance` | — | B-49 | Part 0 | L53.s1 |
| CH-0224 | 5 `provenance` | — | B-50 | Part 0 | — |
| CH-0225 | 20 `form` | provenance | B-51 | Part 0 | L53.s1 |
| CH-0226 | 2 `organization` | provenance | B-52 | Part 0 | L53.s3 |
| CH-0227 | 5 `provenance` | — | B-53 | Part 0 | L51.s3 |
| CH-0228 | 3 `question` | — | B-54 | Part 0 | L55.s1 |
| CH-0229 | 3 `question` | — | B-55 | Part 0 | L55.s3 |
| CH-0230 | 20 `form` | organization | B-56 | Part 0 | L57.s2 |
| CH-0231 | 3 `question` | organization | B-57 | Part 0 | L57.s3 |
| CH-0232 | 19 `ruleout` | provenance | B-58 | Part 0 | L61.s2 |
| CH-0233 | 10 `ruling` | argument, criticism | B-59 | Part 0 | L61.s1 |
| CH-0234 | 20 `form` | ruleout | B-60 | Part XV | L536.s1, L536.s2, L536.s3 |
| CH-0235 | 19 `ruleout` | question, layers, account | B-61 | Part XV | L536.s1 |
| CH-0236 | 19 `ruleout` | account | B-62 | Part XV | L534.s2 |
| CH-0237 | 19 `ruleout` | argument | B-63 | Part XV | L536.s2 |
| CH-0238 | 20 `form` | ruleout | B-64 | Part XV | L538.s1, L538.s2 |
| CH-0239 | 19 `ruleout` | organization, question, layers | B-65 | Part XV | L538.s1 |
| CH-0240 | 19 `ruleout` | work, account | B-66 | Part XV | L538.s2 |
| CH-0241 | 20 `form` | ruleout | B-67 | Part XV | L540.s1 |
| CH-0242 | 19 `ruleout` | organization, work | B-68 | Part XV | L540.s1 |
| CH-0243 | 19 `ruleout` | inputs, argument | B-69 | Part XV | L540.s2 |
| CH-0244 | 5 `provenance` | — | B-70 B-161 B-162 B-163 B-165 B-168 B-169 B-170 B-171 B-172 B-173 B-174 B-175 B-277 | Part XV, Part XVI | L542.s1, L540.s2, L540.s1 +9 |
| CH-0245 | 4 `layers` | provenance, frame | B-71 | Part 0 | — |
| CH-0246 | 20 `form` | ruleout | B-72 | Part XV | L544.s1 |
| CH-0247 | 19 `ruleout` | creativity | B-73 | Part XV | L544.s1 |
| CH-0248 | 20 `form` | criticism | B-74 | Part I | L67.s2 |
| CH-0249 | 20 `form` | question | B-75 | Part I | L73.s1 |
| CH-0250 | 20 `form` | organization | B-76 | Part II | L105.s1 |
| CH-0251 | 2 `organization` | — | B-77 | Part II | L119.s6 |
| CH-0252 | 20 `form` | constructions | B-78 | Part II | L121.s1 |
| CH-0253 | 2 `organization` | — | B-79 | Part II | L127.s4 |
| CH-0254 | 2 `organization` | account | B-80 | Part II | L127.s5 |
| CH-0255 | 20 `form` | organization | B-81 | Part III | L141.s3 |
| CH-0256 | 11 `constructions` | — | B-82 | Part III | L151.s1 |
| CH-0257 | 11 `constructions` | surprise, question | B-83 | Part III | L151.s7 |
| CH-0258 | 3 `question` | — | B-84 | Part III | L159.s1 |
| CH-0259 | 3 `question` | account, inputs | B-85 | Part III | L159.s4 |
| CH-0260 | 13 `criticism` | question | B-86 | Part III | L159.s5 |
| CH-0261 | 3 `question` | — | B-87 | Part III | L157.s1 |
| CH-0262 | 14 `creativity` | question | B-88 | Part III | L161.s5 |
| CH-0263 | 20 `form` | organization | B-89 | Part IV | L175.s1 |
| CH-0264 | 12 `argument` | provenance | B-90 | Part IV | L195.s6 |
| CH-0265 | 12 `argument` | layers, provenance | B-91 | Part IV | L211.s4 |
| CH-0266 | 12 `argument` | provenance, layers, surprise | B-92 | Part IV | L223.s4 |
| CH-0267 | 6 `surprise` | — | B-93 | Part IV | L223.s3 |
| CH-0268 | 12 `argument` | — | B-94 | Part IV | L223.s2 |
| CH-0269 | 20 `form` | organization | B-95 | Part V | L245.s4 |
| CH-0270 | 3 `question` | — | B-96 | Part V | L269.s3 |
| CH-0271 | 3 `question` | account | B-97 | Part V | L271.s2 |
| CH-0272 | 7 `account` | — | B-98 | Part V | L267.s1 |
| CH-0273 | 20 `form` | account | B-99 | Part V | L269.s1 |
| CH-0274 | 7 `account` | — | B-100 | Part V | L269.s2 |
| CH-0275 | 20 `form` | constructions | B-101 | Part V | L271.s1 |
| CH-0276 | 7 `account` | criticism | B-102 | Part V | L273.s2 |
| CH-0277 | 7 `account` | — | B-103 | Part V | L277.s2 |
| CH-0278 | 7 `account` | question | B-104 | Part V | L277.s3 |
| CH-0279 | 7 `account` | frame | B-105 | Part 0 | L19.s1 |
| CH-0280 | 7 `account` | — | B-106 | Part V | L277.s3 |
| CH-0281 | 7 `account` | — | B-107 | Part V | L277.s4 |
| CH-0282 | 20 `form` | organization | B-108 | Part V | L281.s1 |
| CH-0283 | 8 `work` | — | B-109 | Part VI | L299.s2 |
| CH-0284 | 8 `work` | — | B-110 | Part VI | L305.s5 |
| CH-0285 | 8 `work` | — | B-111 | Part VI | L307.s5 |
| CH-0286 | 20 `form` | work | B-112 | Part VI | L307.s2 |
| CH-0287 | 20 `form` | ruleout | B-113 | Part VII | L339.s4 |
| CH-0288 | 4 `layers` | — | B-114 | Part VIII | L365.s1 |
| CH-0289 | 4 `layers` | — | B-115 | Part VIII | L365.s1 |
| CH-0290 | 1 `frame` | layers | B-116 | Part VIII | L365.s2 |
| CH-0291 | 8 `work` | — | B-117 | Part IX | L375.s3 |
| CH-0292 | 12 `argument` | — | B-118 | Part IX | L397.s1 |
| CH-0293 | 20 `form` | provenance | B-119 | Part X | L403.s1 |
| CH-0294 | 14 `creativity` | physical | B-120 | Part X | L403.s4 |
| CH-0295 | 5 `provenance` | rivals, layers, argument | B-121 | Part X | L405.s4 |
| CH-0296 | 5 `provenance` | creativity | B-122 | Part X | L405.s5 |
| CH-0297 | 7 `account` | creativity, organization | B-123 | Part X | L425.s3 |
| CH-0298 | 14 `creativity` | — | B-124 | Part X | L427.s1 |
| CH-0299 | 3 `question` | creativity, physical | B-125 | Part X | L427.s1 |
| CH-0300 | 14 `creativity` | work, physical | B-126 | Part X | L427.s2 |
| CH-0301 | 14 `creativity` | physical | B-127 | Part X | L427.s4 |
| CH-0302 | 13 `criticism` | — | B-128 | Part XI | L441.s1 |
| CH-0303 | 15 `appraisal` | criticism | B-129 | Part XI | L441.s1 |
| CH-0304 | 13 `criticism` | work, constructions | B-130 | Part XI | L441.s5 |
| CH-0305 | 13 `criticism` | account | B-131 | Part XI | L441.s6 |
| CH-0306 | 15 `appraisal` | — | B-132 | Part XI | L455.s5 |
| CH-0307 | 13 `criticism` | appraisal | B-133 | Part XI | L455.s1 |
| CH-0308 | 15 `appraisal` | — | B-134 | Part XI | L455.s2 |
| CH-0309 | 15 `appraisal` | — | B-135 | Part XI | L455.s4 |
| CH-0310 | 15 `appraisal` | — | B-136 | Part XI | L455.s3 |
| CH-0311 | 15 `appraisal` | — | B-137 | Part XI | L455.s5 |
| CH-0312 | 16 `physical` | — | B-138 | Part XII | L473.s1 |
| CH-0313 | 16 `physical` | — | B-139 | Part XII | L473.s1 |
| CH-0314 | 16 `physical` | — | B-140 | Part XII | L473.s2 |
| CH-0315 | 14 `creativity` | inputs, physical | B-141 | Part XII | L473.s3 |
| CH-0316 | 16 `physical` | creativity | B-142 | Part XII | L475.s3 |
| CH-0317 | 4 `layers` | provenance, creativity | B-143 | Part XII | L481.s3 |
| CH-0318 | 18 `inputs` | appraisal | B-144 | Part XIV | L518.s1 |
| CH-0319 | 18 `inputs` | appraisal | B-145 | Part XIV | L518.s1 |
| CH-0320 | 20 `form` | inputs | B-146 | Part XIV | L520.s6 |
| CH-0321 | 18 `inputs` | — | B-147 | Part XIV | L522.s1 |
| CH-0322 | 18 `inputs` | question, criticism | B-148 | Part XIV | L522.s1 |
| CH-0323 | 18 `inputs` | — | B-149 | Part XIV | L522.s2 |
| CH-0324 | 20 `form` | inputs | B-150 | Part XIV | L520.s1 |
| CH-0325 | 18 `inputs` | creativity, account | B-151 | Part XIV | L526.s18 |
| CH-0326 | 19 `ruleout` | ruling, argument | B-152 | Part XV | L534.s1 |
| CH-0327 | 19 `ruleout` | account, question | B-153 | Part XV | L536.s2 |
| CH-0328 | 19 `ruleout` | account | B-154 | Part XV | L536.s3 |
| CH-0329 | 19 `ruleout` | layers, account | B-155 | Part XV | L536.s1, L536.s2, L536.s3 |
| CH-0330 | 19 `ruleout` | account, question, layers | B-156 | Part XV | L536.s1 |
| CH-0331 | 19 `ruleout` | — | B-157 | Part XV | L536.s1, L536.s2, L536.s3 |
| CH-0332 | 19 `ruleout` | layers, account | B-158 | Part XV | L538.s2 |
| CH-0333 | 19 `ruleout` | — | B-159 | Part XV | L538.s1, L538.s2 |
| CH-0334 | 19 `ruleout` | organization | B-160 | Part XV | L538.s2 |
| CH-0335 | 19 `ruleout` | provenance, creativity | B-164 | Part XV | L542.s1 |
| CH-0336 | 19 `ruleout` | provenance, creativity | B-166 | Part XV | L542.s1 |
| CH-0337 | 19 `ruleout` | frame | B-167 | Part XV | L534.s2 |
| CH-0338 | 20 `form` | layers | B-176 | Part XVI | L584.s2 |
| CH-0339 | 15 `appraisal` | — | B-177 | Part XVI | L592.s3 |
| CH-0340 | 18 `inputs` | — | B-178 | Part XVI | L596.s1 |
| CH-0341 | 20 `form` | creativity | B-179 | Part XVI | L620.s2 |
| CH-0342 | 5 `provenance` | surprise, layers | B-180 | Part XVI | L626.s3 |
| CH-0343 | 20 `form` | organization | B-181 | Part XVI | L626.s4 |
| CH-0344 | 20 `form` | creativity | B-182 | Part XVI | L628.s1 |
| CH-0345 | 1 `frame` | — | B-183 B-184 B-185 B-212 B-213 B-262 C-1 | Part 0 | — |
| CH-0346 | 15 `appraisal` | inputs | B-186 B-199 C-4 | Part 0 | L25.s2, L25.s1 |
| CH-0347 | 7 `account` | criticism | B-187 C-22 | Part V | L273.s2 |
| CH-0348 | 15 `appraisal` | — | B-188 B-200 C-47 C-48 | Part XI | L455.s2, L455.s3 |
| CH-0349 | 18 `inputs` | — | B-189 C-64 | Part XVI | L598.s2 |
| CH-0350 | 6 `surprise` | layers, account, provenance | B-190 B-204 C-65 | Part XVI | L626.s3 |
| CH-0351 | 5 `provenance` | layers, physical | B-191 B-192 C-52 | Part XII | L481.s1, L481.s3 |
| CH-0352 | 4 `layers` | creativity | B-193 C-63 | Part XVI | L572.s3 |
| CH-0353 | 18 `inputs` | — | B-194 B-196 B-197 B-198 B-201 C-5 C-55 C-56 | Part 0, Part XIV | L31.s3, L31.s2, L524.s1 +1 |
| CH-0354 | 18 `inputs` | — | B-195 C-54 | Part XIV | L520.s2, L520.s1 |
| CH-0355 | 18 `inputs` | — | B-202 | Part XVI | L596.s1 |
| CH-0356 | 18 `inputs` | — | B-203 C-57 | Part XIV | L526.s4, L526.s1 |
| CH-0357 | 19 `ruleout` | creativity, question, argument | B-205 | Part XV | L544.s1 |
| CH-0358 | 14 `creativity` | — | B-206 | Part XVI | L592.s1 |
| CH-0359 | 15 `appraisal` | — | B-207 | Part XVI | L592.s3 |
| CH-0360 | 19 `ruleout` | — | B-208 | Part 0 | L61.s2 |
| CH-0361 | 14 `creativity` | — | B-209 C-41 | Part X | L427.s2 |
| CH-0362 | 8 `work` | — | B-210 C-24 | Part VI | L299.s2 |
| CH-0363 | 18 `inputs` | argument | B-211 C-6 | Part 0 | L31.s1, L31.s4 |
| CH-0364 | 3 `question` | criticism | B-214 B-297 C-12 | Part III | L159.s5 |
| CH-0365 | 14 `creativity` | physical | B-215 C-42 C-50 | Part X, Part XII | L427.s2, L473.s3, L473.s4 |
| CH-0366 | 2 `organization` | — | B-216 C-11 | Part II | L119.s6, L119.s7, L119.s8 |
| CH-0367 | 15 `appraisal` | — | B-217 | Part 0 | L25.s1 |
| CH-0368 | 14 `creativity` | — | B-218 | Part 0 | L25.s3 |
| CH-0369 | 18 `inputs` | appraisal, physical | B-219 | Part 0 | L31.s1 |
| CH-0370 | 1 `frame` | — | B-220 | Part 0 | L35.s1 |
| CH-0371 | 2 `organization` | — | B-221 | Part II | L127.s4 |
| CH-0372 | 11 `constructions` | surprise, question | B-222 | Part III | L151.s7 |
| CH-0373 | 13 `criticism` | question | B-223 | Part III | L159.s5 |
| CH-0374 | 14 `creativity` | question | B-224 | Part III | L161.s5 |
| CH-0375 | 12 `argument` | provenance | B-225 | Part IV | L195.s6 |
| CH-0376 | 4 `layers` | argument, provenance | B-226 | Part IV | L211.s4 |
| CH-0377 | 12 `argument` | provenance, layers, surprise | B-227 | Part IV | L223.s4 |
| CH-0378 | 7 `account` | — | B-228 | Part V | L269.s2 |
| CH-0379 | 7 `account` | criticism | B-229 | Part V | L273.s2 |
| CH-0380 | 7 `account` | — | B-230 | Part V | L277.s1 |
| CH-0381 | 7 `account` | question | B-231 | Part V | L277.s3 |
| CH-0382 | 8 `work` | — | B-232 | Part VI | L299.s2 |
| CH-0383 | 8 `work` | — | B-233 C-26 | Part VI | L307.s5 |
| CH-0384 | 4 `layers` | — | B-234 | Part VIII | L365.s1 |
| CH-0385 | 1 `frame` | layers | B-235 | Part VIII | L365.s2 |
| CH-0386 | 8 `work` | — | B-236 | Part IX | L375.s3 |
| CH-0387 | 12 `argument` | — | B-237 | Part IX | L397.s1 |
| CH-0388 | 14 `creativity` | physical | B-238 | Part X | L403.s4 |
| CH-0389 | 5 `provenance` | rivals, layers | B-239 | Part X | L405.s4 |
| CH-0390 | 14 `creativity` | provenance | B-240 C-38 | Part X | L405.s5 |
| CH-0391 | 14 `creativity` | account, organization | B-241 | Part X | L425.s3 |
| CH-0392 | 14 `creativity` | physical | B-242 C-40 | Part X | L427.s2 |
| CH-0393 | 13 `criticism` | — | B-243 | Part XI | L441.s1 |
| CH-0394 | 15 `appraisal` | criticism | B-244 | Part XI | L441.s3 |
| CH-0395 | 13 `criticism` | work, constructions | B-245 | Part XI | L441.s5 |
| CH-0396 | 13 `criticism` | account | B-246 | Part XI | L441.s6 |
| CH-0397 | 15 `appraisal` | — | B-247 | Part XI | L455.s2 |
| CH-0398 | 15 `appraisal` | — | B-248 | Part XI | L455.s5 |
| CH-0399 | 16 `physical` | — | B-249 C-49 | Part XII | L473.s1, L473.s2, L473.s3 |
| CH-0400 | 16 `physical` | creativity | B-250 | Part XII | L475.s3 |
| CH-0401 | 4 `layers` | provenance, creativity | B-251 | Part XII | L481.s3 |
| CH-0402 | 18 `inputs` | appraisal | B-252 | Part XIV | L518.s1 |
| CH-0403 | 18 `inputs` | — | B-253 | Part XIV | L522.s1 |
| CH-0404 | 18 `inputs` | creativity, account | B-254 C-59 | Part XIV | L526.s18 |
| CH-0405 | 19 `ruleout` | account | B-255 | Part XV | L536.s3 |
| CH-0406 | 15 `appraisal` | — | B-256 | Part XVI | L592.s3 |
| CH-0407 | 18 `inputs` | — | B-257 | Part XVI | L596.s1 |
| CH-0408 | 6 `surprise` | layers, provenance | B-258 | Part XVI | L626.s3 |
| CH-0409 | 4 `layers` | — | B-259 B-260 B-261 B-271 B-274 B-282 C-33 | Part VIII | L363.s4, L363.s2 |
| CH-0410 | 7 `account` | — | B-263 B-273 B-279 C-62 | Part XVI | L560.s1 |
| CH-0411 | 2 `organization` | — | B-264 B-280 C-10 C-72 C-100 | Part II | L119.s2, L119.s5 |
| CH-0412 | 7 `account` | organization | B-265 B-281 C-66 | Part XVI | L630.s3 |
| CH-0413 | 7 `account` | work, physical | B-266 | Part V | L255.s4 |
| CH-0414 | 2 `organization` | work, layers | B-267 | Part V | L231.s1 |
| CH-0415 | 16 `physical` | — | B-268 | Part V | L255.s2 |
| CH-0416 | 7 `account` | organization | B-269 B-275 B-284 C-20 | Part V | L255.s4 |
| CH-0417 | 2 `organization` | — | B-270 | Part V | L255.s1, L255.s2, L255.s3 +1 |
| CH-0418 | 7 `account` | — | B-272 | Part XVI | L562.s1 |
| CH-0419 | 8 `work` | — | B-276 B-285 C-18 C-102 | Part V | L231.s1, L231.s2 |
| CH-0420 | 5 `provenance` | layers, appraisal | B-278 | Part XVI | L572.s2 |
| CH-0421 | 4 `layers` | — | B-283 | Part VIII | L363.s2 |
| CH-0422 | 8 `work` | physical | B-286 C-23 | Part VI | L287.s2 |
| CH-0423 | 7 `account` | work, physical | B-287 | Part V | L255.s4 |
| CH-0424 | 18 `inputs` | physical | B-288 | Part XIV | L524.s1 |
| CH-0425 | 8 `work` | physical | B-289 | Part VI | L287.s2 |
| CH-0426 | 18 `inputs` | question, criticism | B-290 | Part XIV | L522.s1 |
| CH-0427 | 16 `physical` | frame | B-291 B-292 B-293 C-2 C-107 C-176 | Part 0, Part XII | — |
| CH-0428 | 8 `work` | — | B-294 C-28 | Part VI | L313.s3, L313.s2 |
| CH-0429 | 13 `criticism` | work | B-295 C-8 | Part I | L69.s2 |
| CH-0430 | 8 `work` | — | B-296 C-27 | Part VI | L313.s3, L313.s1 |
| CH-0431 | 8 `work` | — | B-298 | Part VI | L313.s3 |
| CH-0432 | 16 `physical` | — | B-299 | Part XII | — |
| CH-0433 | 13 `criticism` | inputs, argument | B-300 | Part XI | — |
| CH-0434 | 5 `provenance` | criticism, layers | B-301 C-3 C-91 C-92 C-115 | Part 0 | L13.s3 |
| CH-0435 | 12 `argument` | organization, question, inputs | B-302 | Part III, Part XIV | — |
| CH-0436 | 18 `inputs` | physical, account | B-303 C-19 | Part V | L255.s2 |
| CH-0437 | 6 `surprise` | layers | B-304 B-308 C-14 C-15 C-16 C-17 C-43 C-94 C-101 C-106 | Part IV, Part X … | L223.s1, L429.s1, L429.s2 +6 |
| CH-0438 | 13 `criticism` | argument | B-305 | — | — |
| CH-0439 | 14 `creativity` | provenance | B-306 C-37 | Part X | L405.s1, L405.s2, L405.s3 +2 |
| CH-0440 | 19 `ruleout` | account | B-307 C-31 | Part VII | L339.s4, L339.s5 |
| CH-0441 | 5 `provenance` | — | B-309 | Part IV | L195.s1, L195.s2, L195.s3 +3 |
| CH-0442 | 2 `organization` | physical | B-310 C-9 | Part I | L75.s1, L75.s4 |
| CH-0443 | 5 `provenance` | ruleout, layers | C-7 | Part 0 | L61.s2 |
| CH-0444 | 4 `layers` | provenance, inputs | C-13 | Part IV | L195.s2, L195.s3 |
| CH-0445 | 7 `account` | — | C-21 | Part V | L269.s2 |
| CH-0446 | 8 `work` | layers | C-25 | Part VI | L307.s3 |
| CH-0447 | 9 `rivals` | account, constructions | C-29 C-103 | Part VII, Part VI | L321.s1, L315.s2 |
| CH-0448 | 11 `constructions` | — | C-30 C-104 | Part VII | L325.s5 |
| CH-0449 | 4 `layers` | — | C-32 C-97 | Part VIII | L353.s1, L353.s2 |
| CH-0450 | 18 `inputs` | layers | C-34 | Part VIII | L367.s2 |
| CH-0451 | 13 `criticism` | question | C-35 C-98 | Part IX | L377.s2 |
| CH-0452 | 13 `criticism` | — | C-36 | Part IX | L383.s2 |
| CH-0453 | 14 `creativity` | — | C-39 | Part X | L413.s1 |
| CH-0454 | 13 `criticism` | — | C-44 | Part XI | L435.s1 |
| CH-0455 | 13 `criticism` | — | C-45 | Part XI | L441.s1 |
| CH-0456 | 13 `criticism` | account, work, question | C-46 | Part XI | L453.s2 |
| CH-0457 | 16 `physical` | — | C-51 | Part XII | L479.s2 |
| CH-0458 | 17 `recursion` | physical | C-53 | Part XIII | L495.s3 |
| CH-0459 | 18 `inputs` | rivals | C-58 C-105 | Part XIV | L526.s15 |
| CH-0460 | 19 `ruleout` | frame | C-60 | Part XV | L534.s2 |
| CH-0461 | 19 `ruleout` | account | C-61 | Part XV | L536.s3 |
| CH-0462 | 14 `creativity` | — | C-67 | Part XVI | L632.s2 |
| CH-0463 | 1 `frame` | — | C-68 | Part 0 | — |
| CH-0464 | 1 `frame` | — | C-69 | Part 0 | — |
| CH-0465 | 5 `provenance` | layers, criticism | C-70 | Part 0 | L13.s3 |
| CH-0466 | 13 `criticism` | work | C-71 | Part I | L69.s2 |
| CH-0467 | 2 `organization` | — | C-73 C-93 | Part II | L119.s2, L119.s3 |
| CH-0468 | 6 `surprise` | question, layers | C-74 | Part IV | L217.s1 |
| CH-0469 | 6 `surprise` | provenance, layers, argument | C-75 | Part IV | L223.s4 |
| CH-0470 | 6 `surprise` | layers, provenance | C-76 C-95 | Part IV | L223.s4, L223.s5 |
| CH-0471 | 8 `work` | organization, layers | C-77 | Part V | L231.s1 |
| CH-0472 | 8 `work` | — | C-78 C-96 | Part V | L231.s1, L231.s2 |
| CH-0473 | 8 `work` | account | C-79 | Part VI | L313.s2 |
| CH-0474 | 8 `work` | — | C-80 | Part VI | L313.s2 |
| CH-0475 | 11 `constructions` | — | C-81 | Part VII | L321.s1 |
| CH-0476 | 4 `layers` | — | C-82 | Part VIII | L353.s2 |
| CH-0477 | 13 `criticism` | question | C-83 | Part IX | L377.s2 |
| CH-0478 | 18 `inputs` | creativity | C-84 | Part XIV | L526.s12 |
| CH-0479 | 18 `inputs` | creativity | C-85 C-99 | Part XIV | L526.s12, L526.s13 |
| CH-0480 | 2 `organization` | — | C-86 | Part II | L119.s1, L119.s2, L119.s3 +5 |
| CH-0481 | 7 `account` | — | C-87 | Part V | L231.s1, L231.s2, L231.s3 +1 |
| CH-0482 | 4 `layers` | — | C-88 | Part VIII | L363.s1, L363.s2, L363.s3 +1 |
| CH-0483 | 3 `question` | account | C-89 C-108 | Part VII | L339.s5 |
| CH-0484 | 15 `appraisal` | — | C-90 C-109 C-110 | Part XI | L455.s2, L455.s3 |
| CH-0485 | 6 `surprise` | layers | C-111 | Part IV | L223.s5 |
| CH-0486 | 4 `layers` | organization | C-112 | Part II | L119.s1, L119.s2, L119.s3 +5 |
| CH-0487 | 4 `layers` | — | C-113 | Part II | L119.s3 |
| CH-0488 | 8 `work` | — | C-114 | Part V | L231.s2 |
| CH-0489 | 5 `provenance` | layers | C-116 | Part IV | L195.s1, L195.s2, L195.s3 +3 |
| CH-0490 | 7 `account` | — | C-117 | Part V | L255.s4 |
| CH-0491 | 11 `constructions` | — | C-118 | Part VII | L343.s5 |
| CH-0492 | 13 `criticism` | argument | C-119 | Part IX | L377.s2 |
| CH-0493 | 7 `account` | argument | C-120 | Part XVI | L630.s3 |
| CH-0494 | 7 `account` | organization | C-121 | Part XVI | L568.s1 |
| CH-0495 | 15 `appraisal` | — | C-122 | Part XI | L455.s1, L455.s2, L455.s3 +2 |
| CH-0496 | 15 `appraisal` | inputs | C-123 | Part XI | L455.s3 |
| CH-0497 | 18 `inputs` | — | C-124 | Part 0 | L31.s4 |
| CH-0498 | 18 `inputs` | argument | C-125 | Part 0 | L31.s4 |
| CH-0499 | 18 `inputs` | work | C-126 | Part XIV | L526.s13 |
| CH-0500 | 18 `inputs` | question, ruling | C-127 | Part III | L159.s7 |
| CH-0501 | 18 `inputs` | — | C-128 | Part 0 | L31.s3 |
| CH-0502 | 14 `creativity` | question, layers | C-129 | Part X | L413.s1 |
| CH-0503 | 3 `question` | layers, creativity, account | C-130 | Part X | L413.s1 |
| CH-0504 | 4 `layers` | question | C-131 | Part IV | L205.s1 |
| CH-0505 | 5 `provenance` | layers, argument | C-132 | Part XVI | L572.s3 |
| CH-0506 | 6 `surprise` | layers | C-133 | Part IV | L221.s1 |
| CH-0507 | 3 `question` | — | C-134 | Part IV | — |
| CH-0508 | 3 `question` | — | C-135 | Part IV | L219.s1 |
| CH-0509 | 6 `surprise` | layers | C-136 | Part IV | L223.s5 |
| CH-0510 | 2 `organization` | layers | C-137 | Part I | L75.s4 |
| CH-0511 | 4 `layers` | constructions | C-138 | Part X | L409.s5 |
| CH-0512 | 12 `argument` | — | C-139 | Part X | L409.s5 |
| CH-0513 | 14 `creativity` | argument, provenance | C-140 | Part X | L405.s5 |
| CH-0514 | 6 `surprise` | layers | C-141 | Part IV | L223.s5 |
| CH-0515 | 7 `account` | question | C-142 | Part VII | L339.s5 |
| CH-0516 | 15 `appraisal` | — | C-143 | Part 0 | L51.s1 |
| CH-0517 | 18 `inputs` | — | C-144 | Part XIV | L526.s1, L526.s2, L526.s3 +15 |
| CH-0518 | 1 `frame` | — | C-145 | Part 0 | — |
| CH-0519 | 2 `organization` | — | C-146 | Part II | L119.s3 |
| CH-0520 | 2 `organization` | — | C-147 | Part II | L119.s4 |
| CH-0521 | 6 `surprise` | layers, provenance | C-148 | Part IV | L223.s5 |
| CH-0522 | 6 `surprise` | layers | C-149 | Part IV | L223.s5 |
| CH-0523 | 8 `work` | — | C-150 | Part V | L231.s2 |
| CH-0524 | 8 `work` | organization, inputs | C-151 | Part V | L231.s2 |
| CH-0525 | 2 `organization` | account | C-152 | Part V | L245.s4 |
| CH-0526 | 8 `work` | — | C-153 | Part VI | L299.s2 |
| CH-0527 | 2 `organization` | — | C-154 | Part XVI | L558.s1 |
| CH-0528 | 8 `work` | — | C-155 | Part V | L231.s2 |
| CH-0529 | 12 `argument` | ruling | C-156 | Part VI | L315.s13 |
| CH-0530 | 12 `argument` | rivals, ruling, account | C-157 | Part VI | L315.s21 |
| CH-0531 | 9 `rivals` | ruling, argument, question | C-158 | Part VI | L315.s21 |
| CH-0532 | 12 `argument` | creativity, ruling | C-159 | Part VI | L315.s14 |
| CH-0533 | 12 `argument` | — | C-160 | Part VI | L315.s1, L315.s2, L315.s3 +18 |
| CH-0534 | 12 `argument` | — | C-161 | Part IX | L397.s13 |
| CH-0535 | 9 `rivals` | account, argument | C-162 | Part VI | L317.s13 |
| CH-0536 | 9 `rivals` | argument, layers | C-163 | Part VI | L315.s5 |
| CH-0537 | 18 `inputs` | rivals | C-164 | Part XIV | L526.s15 |
| CH-0538 | 18 `inputs` | physical | C-165 | Part XIV | L526.s13 |
| CH-0539 | 18 `inputs` | physical | C-166 | Part XIV | L526.s13 |
| CH-0540 | 10 `ruling` | — | C-167 | Part VI | L317.s1 |
| CH-0541 | 2 `organization` | constructions | C-168 | Part VII | L325.s5 |
| CH-0542 | 7 `account` | question | C-169 | Part VIII | L369.s6 |
| CH-0543 | 12 `argument` | ruling | C-170 | Part VIII | L369.s5 |
| CH-0544 | 6 `surprise` | — | C-171 | Part XVI | L582.s2 |
| CH-0545 | 20 `form` | frame | C-172 | Part 0 | — |
| CH-0546 | 20 `form` | frame | C-173 | Part 0 | — |
| CH-0547 | 20 `form` | frame | C-174 | Part 0 | — |
| CH-0548 | 1 `frame` | — | C-175 | Part 0 | — |
| CH-0549 | 18 `inputs` | — | C-177 | Part XIV | L522.s2 |
| CH-0550 | 11 `constructions` | account | C-178 | Part VII | — |
| CH-0551 | 7 `account` | — | C-179 | Part V | L245.s1, L245.s2, L245.s3 +1 |
| CH-0552 | 2 `organization` | layers | C-180 | Part IV | L189.s1, L189.s2 |
| CH-0553 | 12 `argument` | — | C-181 | Part IX | L389.s1 |
| CH-0554 | 12 `argument` | inputs | C-182 | Part XVI | L598.s1, L598.s2 |
| CH-0555 | 9 `rivals` | — | C-183 | Part VI | L315.s1, L315.s2, L315.s3 +18 |
| CH-0556 | 18 `inputs` | question | C-184 | Part XIV | L522.s1, L522.s2, L522.s3 |
| CH-0557 | 18 `inputs` | work | C-185 | Part VI | L299.s1, L299.s2, L299.s3 |
| CH-0558 | 18 `inputs` | ruling | C-186 | Part XIV | L522.s1 |
| CH-0559 | 17 `recursion` | — | C-187 | Part XIII | L497.s1 |
| CH-0560 | 2 `organization` | — | C-188 | Part II | L119.s3 |
| CH-0561 | 18 `inputs` | — | C-189 | Part XIV | L526.s5 |
| CH-0562 | 13 `criticism` | — | C-190 | Part XI | L441.s2 |
| CH-0563 | 18 `inputs` | appraisal | C-191 | Part XIV | L522.s2 |
| CH-0564 | 18 `inputs` | — | C-192 | Part XIV | L522.s3 |
| CH-0565 | 5 `provenance` | — | C-193 | Part 0 | L61.s2 |
| CH-0566 | 7 `account` | — | C-194 | Part V | L269.s2 |
| CH-0567 | 16 `physical` | — | C-195 | Part XII | L473.s2 |
| CH-0568 | 15 `appraisal` | — | C-196 | Part XVI | L572.s2 |
| CH-0569 | 5 `provenance` | — | C-197 | Part XII | L481.s3 |
| CH-0570 | 13 `criticism` | layers, organization | C-198 | Part IX | L383.s2 |
| CH-0571 | 11 `constructions` | — | C-199 | Part VII | — |
| CH-0572 | 19 `ruleout` | — | C-200 | Part XV | — |
| CH-0573 | 2 `organization` | account, constructions | C-201 | Part V | L255.s3 |
| CH-0574 | 4 `layers` | — | C-202 | Part VIII | L363.s2 |
| CH-0575 | 8 `work` | — | C-203 | Part VI | L313.s3 |
| CH-0576 | 2 `organization` | account, rivals | C-204 | Part VI | L315.s11 |
| CH-0577 | 11 `constructions` | — | C-205 | Part V | L255.s3 |
| CH-0578 | 4 `layers` | — | C-206 | Part X | L405.s4 |
| CH-0579 | 7 `account` | organization, question | C-207 | Part III | L151.s2 |
| CH-0580 | 7 `account` | organization | C-208 | Part II | L121.s1 |
| CH-0581 | 13 `criticism` | constructions | C-209 | Part XI | L437.s1 |
| CH-0582 | 12 `argument` | organization, layers | D-1 | Part 0 | L11.s1 |
| CH-0583 | 20 `form` | organization | D-2 | Part 0 | L11.s4 |
| CH-0584 | 18 `inputs` | layers | D-3 | Part 0 | L13.s1 |
| CH-0585 | 14 `creativity` | inputs | D-4 | Part 0 | L13.s7 |
| CH-0586 | 20 `form` | argument | D-5 | Part 0 | L15.s2 |
| CH-0587 | 4 `layers` | physical | D-6 | Part 0 | L17.s1 |
| CH-0588 | 10 `ruling` | argument | D-7 | Part 0 | L17.s3 |
| CH-0589 | 12 `argument` | frame, provenance, creativity | D-8 | Part 0 | L21.s1, L21.s2 |
| CH-0590 | 20 `form` | argument | D-9 | Part 0 | L23.s3 |
| CH-0591 | 15 `appraisal` | — | D-10 | Part 0 | L25.s1 |
| CH-0592 | 15 `appraisal` | — | D-11 | Part 0 | L25.s2 |
| CH-0593 | 14 `creativity` | — | D-12 | Part 0 | L25.s3 |
| CH-0594 | 1 `frame` | — | D-13 | Part 0 | L27.s1 |
| CH-0595 | 18 `inputs` | — | D-14 | Part 0 | L29.s1 |
| CH-0596 | 18 `inputs` | — | D-15 | Part 0 | L31.s1 |
| CH-0597 | 18 `inputs` | appraisal | D-16 | Part 0 | L31.s1 |
| CH-0598 | 18 `inputs` | criticism, question, physical | D-17 | Part 0 | L31.s2 |
| CH-0599 | 18 `inputs` | — | D-18 | Part 0 | L31.s3 |
| CH-0600 | 18 `inputs` | — | D-19 | Part 0 | L31.s4 |
| CH-0601 | 18 `inputs` | appraisal | D-20 | Part 0 | L31.s1 |
| CH-0602 | 20 `form` | inputs | D-21 | Part 0 | L31.s4 |
| CH-0603 | 2 `organization` | — | D-22 | Part 0 | L37.s3 |
| CH-0604 | 2 `organization` | — | D-23 | Part 0 | L39.s2 |
| CH-0605 | 5 `provenance` | account, layers | D-24 | Part 0 | L41.s1 |
| CH-0606 | 4 `layers` | provenance | D-25 | Part 0 | L41.s2 |
| CH-0607 | 20 `form` | provenance | D-26 | Part 0 | L41.s3 |
| CH-0608 | 3 `question` | — | D-27 | Part 0 | L43.s1 |
| CH-0609 | 3 `question` | account | D-28 | Part 0 | L43.s3 |
| CH-0610 | 3 `question` | account, argument | D-29 | Part 0 | L43.s5 |
| CH-0611 | 16 `physical` | — | D-30 | Part 0 | L45.s4 |
| CH-0612 | 5 `provenance` | creativity | D-31 | Part 0 | L47.s2 |
| CH-0613 | 10 `ruling` | provenance | D-32 | Part 0 | L47.s3 |
| CH-0614 | 5 `provenance` | layers | D-33 | Part 0 | L47.s1 |
| CH-0615 | 2 `organization` | argument, account, constructions | D-34 | Part 0 | L49.s2 |
| CH-0616 | 11 `constructions` | argument | D-35 | Part 0 | L49.s3 |
| CH-0617 | 15 `appraisal` | rivals | D-36 | Part 0 | L51.s3 |
| CH-0618 | 15 `appraisal` | — | D-37 | Part 0 | L51.s1 |
| CH-0619 | 10 `ruling` | physical | D-38 | Part 0 | L53.s2 |
| CH-0620 | 12 `argument` | ruling | D-39 | Part 0 | L55.s4 |
| CH-0621 | 2 `organization` | — | D-40 | Part 0 | L57.s1 |
| CH-0622 | 10 `ruling` | argument, inputs | D-41 | Part 0 | L61.s1 |
| CH-0623 | 10 `ruling` | — | D-42 | Part 0 | L61.s1 |
| CH-0624 | 10 `ruling` | account, physical | D-43 | Part I | L67.s1 |
| CH-0625 | 10 `ruling` | — | D-44 | Part I | L67.s1 |
| CH-0626 | 13 `criticism` | — | D-45 | Part I | L67.s2 |
| CH-0627 | 13 `criticism` | work | D-46 | Part I | L69.s1 |
| CH-0628 | 3 `question` | account, criticism, work | D-47 | Part I | L69.s3 |
| CH-0629 | 7 `account` | question, work, criticism | D-48 | Part I | L69.s3 |
| CH-0630 | 10 `ruling` | — | D-49 | Part I | L71.s1 |
| CH-0631 | 15 `appraisal` | — | D-50 | Part I | L71.s3 |
| CH-0632 | 2 `organization` | physical | D-51 | Part I | L75.s1 |
| CH-0633 | 16 `physical` | ruling, organization | D-52 | Part I | L75.s2 |
| CH-0634 | 2 `organization` | — | D-53 | Part I | L75.s4 |
| CH-0635 | 2 `organization` | argument | D-54 | Part II | L105.s1 |
| CH-0636 | 2 `organization` | — | D-55 | Part II | L107.s1 |
| CH-0637 | 2 `organization` | — | D-56 | Part II | L119.s3 |
| CH-0638 | 2 `organization` | — | D-57 | Part II | L119.s4, L119.s5 |
| CH-0639 | 20 `form` | organization | D-58 | Part II | L119.s4, L119.s5 |
| CH-0640 | 20 `form` | organization | D-59 | Part II | L119.s4, L119.s5 |
| CH-0641 | 2 `organization` | account | D-60 | Part II | L127.s5 |
| CH-0642 | 13 `criticism` | — | D-61 | Part III | L147.s1 |
| CH-0643 | 11 `constructions` | question | D-62 | Part III | L151.s4 |
| CH-0644 | 3 `question` | surprise, constructions | D-63 | Part III | L151.s7 |
| CH-0645 | 5 `provenance` | — | D-64 | Part III | L155.s1 |
| CH-0646 | 3 `question` | provenance | D-65 | Part III | L155.s6 |
| CH-0647 | 14 `creativity` | question, provenance | D-66 | Part III | L155.s4 |
| CH-0648 | 3 `question` | — | D-67 | Part III | L157.s1 |
| CH-0649 | 3 `question` | criticism | D-68 | Part III | L159.s5 |
| CH-0650 | 3 `question` | inputs, ruling | D-69 | Part III | L159.s7 |
| CH-0651 | 4 `layers` | — | D-70 | Part IV | L171.s1 |
| CH-0652 | 4 `layers` | organization | D-71 | Part IV | L175.s1 |
| CH-0653 | 6 `surprise` | — | D-72 | Part IV | L177.s2 |
| CH-0654 | 4 `layers` | — | D-73 | Part IV | L189.s2 |
| CH-0655 | 20 `form` | argument | D-74 | Part IV | L195.s6 |
| CH-0656 | 14 `creativity` | provenance, organization | D-75 | Part IV | L197.s1 |
| CH-0657 | 5 `provenance` | layers, surprise | D-76 | Part IV | L201.s1 |
| CH-0658 | 4 `layers` | provenance | D-77 | Part IV | L201.s1 |
| CH-0659 | 4 `layers` | — | D-78 | Part IV | L203.s1 |
| CH-0660 | 4 `layers` | — | D-79 | Part IV | L211.s1, L211.s2 |
| CH-0661 | 4 `layers` | provenance, argument | D-80 | Part IV | L211.s4 |
| CH-0662 | 6 `surprise` | — | D-81 | Part IV | L215.s1 |
| CH-0663 | 6 `surprise` | — | D-82 | Part IV | L219.s1 |
| CH-0664 | 6 `surprise` | — | D-83 | Part IV | L223.s4, L223.s5 |
| CH-0665 | 20 `form` | argument | D-84 | Part IV | L223.s3 |
| CH-0666 | 5 `provenance` | — | D-85 | Part IV | L225.s3 |
| CH-0667 | 7 `account` | — | D-86 | Part V | L231.s3 |
| CH-0668 | 7 `account` | organization | D-87 | Part V | L233.s1 |
| CH-0669 | 7 `account` | — | D-88 | Part V | L245.s1, L245.s2 |
| CH-0670 | 7 `account` | organization | D-89 | Part V | L245.s4 |
| CH-0671 | 20 `form` | account | D-90 | Part V | L245.s4 |
| CH-0672 | 11 `constructions` | — | D-91 | Part V | L255.s3 |
| CH-0673 | 7 `account` | — | D-92 | Part V | L257.s3 |
| CH-0674 | 7 `account` | — | D-93 | Part V | L269.s2 |
| CH-0675 | 3 `question` | account | D-94 | Part V | L269.s3 |
| CH-0676 | 7 `account` | — | D-95 | Part V | L269.s2 |
| CH-0677 | 7 `account` | criticism | D-96 | Part V | L273.s2 |
| CH-0678 | 7 `account` | — | D-97 | Part V | L277.s1 |
| CH-0679 | 7 `account` | — | D-98 | Part V | L277.s2 |
| CH-0680 | 7 `account` | question, ruling | D-99 | Part V | L277.s3 |
| CH-0681 | 3 `question` | account | D-100 | Part V | L277.s3 |
| CH-0682 | 12 `argument` | account, constructions | D-101 | Part V | L277.s4 |
| CH-0683 | 7 `account` | constructions, argument | D-102 | Part V | L277.s4 |
| CH-0684 | 7 `account` | organization | D-103 | Part V | L279.s1 |
| CH-0685 | 7 `account` | organization | D-104 | Part V | L281.s2 |
| CH-0686 | 20 `form` | argument | D-105 | Part V | L281.s5 |
| CH-0687 | 8 `work` | — | D-106 | Part VI | L285.s1 |
| CH-0688 | 8 `work` | — | D-107 | Part VI | L299.s2 |
| CH-0689 | 8 `work` | — | D-108 | Part VI | L305.s1 |
| CH-0690 | 8 `work` | — | D-109 | Part VI | L305.s3 |
| CH-0691 | 8 `work` | — | D-110 | Part VI | L305.s5 |
| CH-0692 | 20 `form` | argument | D-111 | Part VI | L305.s2 |
| CH-0693 | 8 `work` | — | D-112 | Part VI | L307.s3 |
| CH-0694 | 8 `work` | criticism | D-113 | Part VI | L307.s4 |
| CH-0695 | 8 `work` | — | D-114 | Part VI | L307.s5 |
| CH-0696 | 20 `form` | work | D-115 | Part VI | L307.s2 |
| CH-0697 | 8 `work` | criticism, account | D-116 | Part VI | L309.s1, L309.s2 |
| CH-0698 | 8 `work` | — | D-117 | Part VI | L311.s1 |
| CH-0699 | 8 `work` | — | D-118 | Part VI | L311.s1 |
| CH-0700 | 8 `work` | — | D-119 | Part VI | L313.s2 |
| CH-0701 | 8 `work` | — | D-120 | Part VI | L313.s2 |
| CH-0702 | 8 `work` | — | D-121 | Part VI | L313.s3 |
| CH-0703 | 7 `account` | rivals | D-122 | Part VI | L315.s2 |
| CH-0704 | 12 `argument` | ruling | D-123 | Part VI | L315.s6 |
| CH-0705 | 20 `form` | layers | D-124 | Part VI | L315.s5 |
| CH-0706 | 20 `form` | argument | D-125 | Part VI | L315.s9 |
| CH-0707 | 9 `rivals` | ruling | D-126 | Part VI | L317.s1 |
| CH-0708 | 12 `argument` | rivals, ruling, account | D-127 | Part VI | L317.s4 |
| CH-0709 | 12 `argument` | account, ruling | D-128 | Part VI | L317.s7 |
| CH-0710 | 9 `rivals` | — | D-129 | Part VI | L317.s11 |
| CH-0711 | 9 `rivals` | account, question | D-130 | Part VI | L317.s13 |
| CH-0712 | 9 `rivals` | ruling | D-131 | Part VI | L317.s14 |
| CH-0713 | 9 `rivals` | argument | D-132 | Part VI | L317.s14 |
| CH-0714 | 9 `rivals` | ruling | D-133 | Part VI | L317.s15 |
| CH-0715 | 9 `rivals` | ruling | D-134 | Part VI | L317.s16 |
| CH-0716 | 9 `rivals` | criticism | D-135 | Part VI | L317.s17 |
| CH-0717 | 20 `form` | rivals | D-136 | Part VI | L317.s13 |
| CH-0718 | 11 `constructions` | — | D-137 | Part VII | L325.s7 |
| CH-0719 | 11 `constructions` | layers, question | D-138 | Part VII | L331.s3 |
| CH-0720 | 15 `appraisal` | — | D-139 | Part VII | L335.s2 |
| CH-0721 | 10 `ruling` | question | D-140 | Part VII | L335.s3 |
| CH-0722 | 9 `rivals` | — | D-141 | Part VII | L339.s3 |
| CH-0723 | 19 `ruleout` | account | D-142 | Part VII | L339.s4 |
| CH-0724 | 11 `constructions` | account | D-143 | Part VII | L343.s5 |
| CH-0725 | 11 `constructions` | argument | D-144 | Part VII | L343.s9 |
| CH-0726 | 11 `constructions` | account, organization | D-145 | Part VII | L343.s3 |
| CH-0727 | 11 `constructions` | — | D-146 | Part VII | L343.s4 |
| CH-0728 | 3 `question` | layers | D-147 | Part VIII | L353.s2 |
| CH-0729 | 20 `form` | argument | D-148 | Part VIII | L353.s3 |
| CH-0730 | 3 `question` | argument, layers | D-149 | Part VIII | L363.s2 |
| CH-0731 | 20 `form` | layers | D-150 | Part VIII | L365.s1 |
| CH-0732 | 3 `question` | — | D-151 | Part VIII | L369.s2 |
| CH-0733 | 10 `ruling` | argument | D-152 | Part VIII | L369.s3 |
| CH-0734 | 12 `argument` | ruling | D-153 | Part VIII | L369.s4 |
| CH-0735 | 13 `criticism` | argument | D-154 | Part IX | L373.s1 |
| CH-0736 | 4 `layers` | work, inputs | D-155 | Part IX | L375.s2 |
| CH-0737 | 13 `criticism` | argument | D-156 | Part IX | L377.s1 |
| CH-0738 | 13 `criticism` | — | D-157 | Part IX | L383.s2 |
| CH-0739 | 12 `argument` | criticism | D-158 | Part IX | L385.s2 |
| CH-0740 | 12 `argument` | — | D-159 | Part IX | L387.s1 |
| CH-0741 | 12 `argument` | — | D-160 | Part IX | L389.s1 |
| CH-0742 | 12 `argument` | — | D-161 | Part IX | L393.s1 |
| CH-0743 | 12 `argument` | ruling | D-162 | Part IX | L395.s1 |
| CH-0744 | 12 `argument` | — | D-163 | Part IX | L397.s1 |
| CH-0745 | 12 `argument` | — | D-164 | Part IX | L397.s2 |
| CH-0746 | 12 `argument` | ruling | D-165 | Part IX | L397.s6 |
| CH-0747 | 12 `argument` | — | D-166 | Part IX | L397.s16 |
| CH-0748 | 5 `provenance` | physical, creativity, layers | D-167 | Part X | L403.s1 |
| CH-0749 | 16 `physical` | provenance | D-168 | Part X | L403.s1 |
| CH-0750 | 14 `creativity` | — | D-169 | Part X | L403.s3 |
| CH-0751 | 14 `creativity` | — | D-170 | Part X | L403.s4 |
| CH-0752 | 14 `creativity` | organization, layers | D-171 | Part X | L405.s1 |
| CH-0753 | 5 `provenance` | creativity, layers | D-172 | Part X | L405.s2 |
| CH-0754 | 12 `argument` | creativity, provenance | D-173 | Part X | L409.s5 |
| CH-0755 | 16 `physical` | provenance, creativity | D-174 | Part X | L411.s3 |
| CH-0756 | 14 `creativity` | — | D-175 | Part X | L427.s3 |
| CH-0757 | 14 `creativity` | physical | D-176 | Part X | L427.s4 |
| CH-0758 | 14 `creativity` | argument | D-177 | Part X | L429.s3 |
| CH-0759 | 13 `criticism` | — | D-178 | Part X | L429.s2 |
| CH-0760 | 13 `criticism` | — | D-179 | Part X | L429.s2 |
| CH-0761 | 15 `appraisal` | — | D-180 | Part XI | L433.s1 |
| CH-0762 | 13 `criticism` | — | D-181 | Part XI | L435.s2 |
| CH-0763 | 13 `criticism` | — | D-182 | Part XI | L435.s2 |
| CH-0764 | 13 `criticism` | — | D-183 | Part XI | L441.s2 |
| CH-0765 | 15 `appraisal` | criticism | D-184 | Part XI | L441.s3 |
| CH-0766 | 13 `criticism` | work, constructions | D-185 | Part XI | L441.s5 |
| CH-0767 | 7 `account` | criticism | D-186 | Part XI | L441.s6 |
| CH-0768 | 13 `criticism` | — | D-187 | Part XI | L441.s1 |
| CH-0769 | 14 `creativity` | — | D-188 | Part XI | L443.s1 |
| CH-0770 | 14 `creativity` | work, criticism | D-189 | Part XI | L445.s1 |
| CH-0771 | 14 `creativity` | — | D-190 | Part XI | L445.s1 |
| CH-0772 | 14 `creativity` | — | D-191 | Part XI | L445.s1 |
| CH-0773 | 13 `criticism` | work | D-192 | Part XI | L453.s2 |
| CH-0774 | 18 `inputs` | account, question | D-193 | Part XI | L453.s5 |
| CH-0775 | 15 `appraisal` | — | D-194 | Part XI | L455.s1, L455.s2 |
| CH-0776 | 15 `appraisal` | — | D-195 | Part XI | L455.s5 |
| CH-0777 | 16 `physical` | — | D-196 | Part XII | L461.s2 |
| CH-0778 | 7 `account` | physical, inputs | D-197 | Part XII | L469.s1 |
| CH-0779 | 16 `physical` | creativity | D-198 | Part XII | L475.s3 |
| CH-0780 | 2 `organization` | creativity, physical | D-199 | Part XII | L477.s1 |
| CH-0781 | 16 `physical` | — | D-200 | Part XII | L479.s1 |
| CH-0782 | 16 `physical` | — | D-201 | Part XII | L479.s2 |
| CH-0783 | 16 `physical` | — | D-202 | Part XII | L479.s2 |
| CH-0784 | 16 `physical` | — | D-203 | Part XII | L479.s2 |
| CH-0785 | 16 `physical` | — | D-204 | Part XII | L479.s4 |
| CH-0786 | 16 `physical` | — | D-205 | Part XII | L481.s2 |
| CH-0787 | 17 `recursion` | ruling | D-206 | Part XIII | L495.s2 |
| CH-0788 | 16 `physical` | — | D-207 | Part XIII | L495.s3 |
| CH-0789 | 17 `recursion` | argument | D-208 | Part XIII | L509.s1 |
| CH-0790 | 18 `inputs` | — | D-209 | Part XIV | L515.s1 |
| CH-0791 | 18 `inputs` | physical, organization | D-210 | Part XIV | L517.s1 |
| CH-0792 | 18 `inputs` | appraisal | D-211 | Part XIV | L518.s1 |
| CH-0793 | 18 `inputs` | appraisal | D-212 | Part XIV | L518.s1 |
| CH-0794 | 18 `inputs` | — | D-213 | Part XIV | L520.s1 |
| CH-0795 | 18 `inputs` | creativity, recursion | D-214 | Part XIV | L520.s8 |
| CH-0796 | 18 `inputs` | — | D-215 | Part XIV | L522.s1 |
| CH-0797 | 18 `inputs` | question | D-216 | Part XIV | L522.s1 |
| CH-0798 | 18 `inputs` | creativity | D-217 | Part XIV | L522.s1 |
| CH-0799 | 18 `inputs` | appraisal | D-218 | Part XIV | L522.s2, L522.s3 |
| CH-0800 | 18 `inputs` | criticism | D-219 | Part XIV | L522.s1 |
| CH-0801 | 18 `inputs` | — | D-220 | Part XIV | L524.s1 |
| CH-0802 | 18 `inputs` | criticism | D-221 | Part XIV | L524.s2 |
| CH-0803 | 18 `inputs` | — | D-222 | Part XIV | L526.s1 |
| CH-0804 | 18 `inputs` | rivals | D-223 | Part XIV | L526.s15 |
| CH-0805 | 18 `inputs` | — | D-224 | Part XIV | L526.s16 |
| CH-0806 | 18 `inputs` | creativity, account | D-225 | Part XIV | L526.s18 |
| CH-0807 | 18 `inputs` | — | D-226 | Part XIV | L526.s13 |
| CH-0808 | 18 `inputs` | criticism | D-227 | Part XIV | L526.s13 |
| CH-0809 | 18 `inputs` | — | D-228 | Part XIV | L526.s13 |
| CH-0810 | 18 `inputs` | physical | D-229 | Part XIV | L528.s1 |
| CH-0811 | 18 `inputs` | creativity, ruleout | D-230 | Part XIV | L528.s3 |
| CH-0812 | 19 `ruleout` | ruling | D-231 | Part XV | L534.s1 |
| CH-0813 | 19 `ruleout` | appraisal, inputs, ruling | D-232 | Part XV | L534.s3 |
| CH-0814 | 19 `ruleout` | account | D-233 | Part XV | L536.s1 |
| CH-0815 | 19 `ruleout` | organization | D-234 | Part XV | L538.s1 |
| CH-0816 | 19 `ruleout` | inputs, ruling, argument | D-235 | Part XV | L540.s2 |
| CH-0817 | 19 `ruleout` | provenance, ruling, creativity | D-236 | Part XV | L542.s1 |
| CH-0818 | 19 `ruleout` | provenance, argument, creativity | D-237 | Part XV | L542.s1 |
| CH-0819 | 19 `ruleout` | provenance, layers | D-238 | Part XV | L542.s1 |
| CH-0820 | 20 `form` | ruleout | D-239 | Part XV | L542.s1 |
| CH-0821 | 19 `ruleout` | creativity, argument | D-240 | Part XV | L544.s1 |
| CH-0822 | 19 `ruleout` | creativity | D-241 | Part XV | L544.s1 |
| CH-0823 | 19 `ruleout` | work, physical, argument | D-242 | Part XV | L546.s1 |
| CH-0824 | 20 `form` | ruleout | D-243 | Part XV | L546.s1 |
| CH-0825 | 20 `form` | argument | D-244 | Part XVI | L550.s1 |
| CH-0826 | 2 `organization` | — | D-245 | Part XVI | L552.s1 |
| CH-0827 | 2 `organization` | account | D-246 | Part XVI | L554.s1 |
| CH-0828 | 20 `form` | argument | D-247 | Part XVI | L556.s1 |
| CH-0829 | 2 `organization` | account, question | D-248 | Part XVI | L558.s1 |
| CH-0830 | 7 `account` | — | D-249 | Part XVI | L560.s1 |
| CH-0831 | 7 `account` | organization | D-250 | Part XVI | L562.s3 |
| CH-0832 | 7 `account` | — | D-251 | Part XVI | L562.s1 |
| CH-0833 | 2 `organization` | account, argument | D-252 | Part XVI | L564.s3 |
| CH-0834 | 20 `form` | argument | D-253 | Part XVI | L564.s1 |
| CH-0835 | 7 `account` | work | D-254 | Part XVI | L566.s1 |
| CH-0836 | 20 `form` | argument | D-255 | Part XVI | L566.s1 |
| CH-0837 | 20 `form` | argument | D-256 | Part XVI | L566.s2 |
| CH-0838 | 7 `account` | question | D-257 | Part XVI | L568.s1 |
| CH-0839 | 7 `account` | question | D-258 | Part XVI | L568.s1 |
| CH-0840 | 7 `account` | question | D-259 | Part XVI | L568.s1 |
| CH-0841 | 12 `argument` | layers | D-260 | Part XVI | L572.s3 |
| CH-0842 | 20 `form` | argument | D-261 | Part XVI | L574.s1 |
| CH-0843 | 5 `provenance` | physical, argument | D-262 | Part XVI | L576.s4 |
| CH-0844 | 4 `layers` | — | D-263 | Part XVI | L576.s2 |
| CH-0845 | 6 `surprise` | — | D-264 | Part XVI | L582.s3 |
| CH-0846 | 20 `form` | argument | D-265 | Part XVI | L582.s1 |
| CH-0847 | 4 `layers` | provenance, surprise | D-266 | Part XVI | L584.s2 |
| CH-0848 | 14 `creativity` | — | D-267 | Part XVI | L588.s2 |
| CH-0849 | 20 `form` | argument | D-268 | Part XVI | L590.s1 |
| CH-0850 | 14 `creativity` | — | D-269 | Part XVI | L592.s1 |
| CH-0851 | 15 `appraisal` | — | D-270 | Part XVI | L592.s3 |
| CH-0852 | 18 `inputs` | — | D-271 | Part XVI | L594.s1 |
| CH-0853 | 18 `inputs` | — | D-272 | Part XVI | L596.s1 |
| CH-0854 | 18 `inputs` | — | D-273 | Part XVI | L598.s2 |
| CH-0855 | 20 `form` | argument | D-274 | Part XVI | L598.s1 |
| CH-0856 | 18 `inputs` | — | D-275 | Part XVI | L600.s2 |
| CH-0857 | 14 `creativity` | question | D-276 | Part XVI | L604.s1 |
| CH-0858 | 4 `layers` | inputs, ruling | D-277 | Part XVI | L606.s2 |
| CH-0859 | 7 `account` | inputs | D-278 | Part XVI | L606.s4 |
| CH-0860 | 20 `form` | argument | D-279 | Part XVI | L606.s1 |
| CH-0861 | 20 `form` | question | D-280 | Part XVI | L606.s3 |
| CH-0862 | 18 `inputs` | question | D-281 | Part XVI | L608.s2 |
| CH-0863 | 4 `layers` | — | D-282 | Part XVI | L610.s1 |
| CH-0864 | 4 `layers` | — | D-283 | Part XVI | L612.s1 |
| CH-0865 | 20 `form` | argument | D-284 | Part XVI | L612.s2 |
| CH-0866 | 14 `creativity` | — | D-285 | Part XVI | L616.s4 |
| CH-0867 | 20 `form` | argument | D-286 | Part XVI | L616.s2 |
| CH-0868 | 4 `layers` | physical | D-287 | Part XVI | L620.s1 |
| CH-0869 | 6 `surprise` | — | D-288 | Part XVI | L624.s3 |
| CH-0870 | 20 `form` | argument | D-289 | Part XVI | L624.s4 |
| CH-0871 | 20 `form` | argument | D-290 | Part XVI | L626.s6 |
| CH-0872 | 14 `creativity` | physical | D-291 | Part XVI | L628.s1 |
| CH-0873 | 13 `criticism` | account, creativity, surprise, question | D-292 | Part XVI | L628.s2 |
| CH-0874 | 13 `criticism` | — | D-293 | Part XVI | L628.s2 |
| CH-0875 | 3 `question` | organization | D-294 | Part XVI | L630.s4 |
| CH-0876 | 13 `criticism` | question | D-295 | Part XVI | L630.s5 |
| CH-0877 | 20 `form` | account | D-296 | Part XVI | L630.s3 |
| CH-0878 | 20 `form` | account | D-297 | Part XVI | L630.s3 |
| CH-0879 | 14 `creativity` | — | D-298 | Part XVI | L632.s1, L632.s2 |
| CH-0880 | 1 `frame` | argument | D-299 | Front | L2.s2 |
| CH-0881 | 10 `ruling` | argument | D-300 | Part 0 | L8.s6 |
| CH-0882 | 2 `organization` | physical, ruling | D-301 | Part I | L75.s2 |
| CH-0883 | 17 `recursion` | — | D-302 | Part I | L75.s5 |
| CH-0884 | 3 `question` | — | D-303 | Part 0 | L43.s1 |
| CH-0885 | 7 `account` | question, criticism | D-304 | Part 0 | L43.s4 |
| CH-0886 | 7 `account` | question | D-305 | Part 0 | L43.s5 |
| CH-0887 | 4 `layers` | provenance | D-306 | Part 0 | L41.s2 |
| CH-0888 | 11 `constructions` | argument, frame | D-307 | Part 0 | L49.s4 |
| CH-0889 | 15 `appraisal` | — | D-308 | Part 0 | L51.s2 |
| CH-0890 | 3 `question` | — | D-309 | Part III | L159.s3 |
| CH-0891 | 6 `surprise` | — | D-310 | Part IV | L223.s3 |
| CH-0892 | 3 `question` | — | D-311 | Part V | L257.s2 |
| CH-0893 | 7 `account` | — | D-312 | Part V | L275.s2 |
| CH-0894 | 7 `account` | rivals | D-313 | Part VI | L315.s2 |
| CH-0895 | 3 `question` | rivals | D-314 | Part VI | L317.s14 |
| CH-0896 | 11 `constructions` | — | D-315 | Part VII | L343.s6, L343.s7 |
| CH-0897 | 16 `physical` | — | D-316 | Part XII | L461.s3 |
| CH-0898 | 18 `inputs` | rivals | D-317 | Part XIV | L526.s15 |
| CH-0899 | 19 `ruleout` | question | D-318 D-728 D-817 | Part XV | L536.s1 |
| CH-0900 | 19 `ruleout` | — | D-319 D-730 D-819 | Part XV | L538.s1 |
| CH-0901 | 3 `question` | surprise | D-320 | Part XVI | L580.s1 |
| CH-0902 | 4 `layers` | — | D-321 | Part IV | L211.s2 |
| CH-0903 | 9 `rivals` | provenance | D-322 | Part VI | L315.s9 |
| CH-0904 | 9 `rivals` | ruling | D-323 D-725 D-802 | Part VI | L317.s16 |
| CH-0905 | 10 `ruling` | argument, rivals, account | D-324 | Part VI | L317.s7, L317.s8 |
| CH-0906 | 10 `ruling` | argument | D-325 | Part 0 | L8.s6, L8.s7 |
| CH-0907 | 12 `argument` | — | D-326 D-718 D-720 D-824 D-825 | Part IX | L397.s2, L397.s3, L397.s5 +1 |
| CH-0908 | 12 `argument` | frame | D-327 D-734 D-813 | Part IX | L393.s1 |
| CH-0909 | 12 `argument` | ruling | D-328 D-719 D-779 | Part 0 | L8.s2, L8.s5 |
| CH-0910 | 10 `ruling` | question | D-329 D-727 | Part 0 | L17.s2 |
| CH-0911 | 14 `creativity` | — | D-330 D-778 D-806 | Part 0 | L25.s3 |
| CH-0912 | 18 `inputs` | — | D-331 D-364 D-740 D-821 | Part 0, Part XIV | L31.s4, L526.s16 |
| CH-0913 | 10 `ruling` | provenance | D-332 D-751 D-781 | Part 0 | L47.s3 |
| CH-0914 | 10 `ruling` | — | D-333 D-752 D-782 | Part 0 | L61.s1 |
| CH-0915 | 3 `question` | constructions, surprise | D-334 D-737 D-793 | Part III | L151.s7 |
| CH-0916 | 3 `question` | account, argument | D-335 D-739 D-794 | Part III | L159.s6 |
| CH-0917 | 3 `question` | — | D-336 D-755 D-783 | Part III | L161.s4 |
| CH-0918 | 5 `provenance` | layers | D-337 D-771 D-795 | Part IV | L201.s1 |
| CH-0919 | 5 `provenance` | layers | D-338 D-762 D-784 | Part IV | L211.s4 |
| CH-0920 | 6 `surprise` | — | D-339 D-340 D-356 D-767 D-768 D-789 D-790 | Part IV, Part XI | L221.s1, L223.s5, L443.s1 |
| CH-0921 | 7 `account` | — | D-341 D-726 D-796 | Part V | L277.s1 |
| CH-0922 | 8 `work` | — | D-342 D-735 D-797 | Part VI | L299.s2 |
| CH-0923 | 8 `work` | — | D-343 D-807 | Part VI | L305.s5 |
| CH-0924 | 8 `work` | — | D-344 D-736 D-798 | Part VI | L307.s3 |
| CH-0925 | 8 `work` | — | D-345 D-808 | Part VI | L311.s1 |
| CH-0926 | 12 `argument` | ruling | D-346 D-721 D-799 | Part VI | L315.s6 |
| CH-0927 | 10 `ruling` | argument | D-347 D-723 D-800 | Part VI | L317.s5 |
| CH-0928 | 10 `ruling` | argument, rivals | D-348 D-724 D-801 | Part VI | L317.s7, L317.s8 |
| CH-0929 | 7 `account` | question | D-349 D-371 D-777 D-840 | Part VI, Part XVI | L317.s13, L568.s1 |
| CH-0930 | 15 `appraisal` | constructions, question | D-350 D-738 D-803 | Part VII | L331.s3 |
| CH-0931 | 14 `creativity` | question, ruling | D-351 D-753 D-804 | Part VII | L335.s3 |
| CH-0932 | 12 `argument` | ruling | D-352 D-722 D-805 | Part VIII | L369.s4 |
| CH-0933 | 12 `argument` | — | D-353 D-773 D-837 | Part IX | L385.s2 |
| CH-0934 | 14 `creativity` | argument, ruling | D-354 D-774 D-838 | Part X | L429.s4 |
| CH-0935 | 13 `criticism` | work | D-355 D-744 D-823 | Part XI | L441.s5 |
| CH-0936 | 3 `question` | account, inputs | D-357 D-750 D-835 | Part XI | L453.s5 |
| CH-0937 | 16 `physical` | — | D-358 D-756 D-816 | Part XII | L461.s1 |
| CH-0938 | 16 `physical` | — | D-359 D-745 D-830 | Part XII | L479.s1 |
| CH-0939 | 17 `recursion` | ruling | D-360 D-754 D-809 | Part XIII | L495.s2 |
| CH-0940 | 18 `inputs` | appraisal | D-361 D-761 D-814 | Part XIV | L518.s1 |
| CH-0941 | 18 `inputs` | ruling, argument | D-362 D-731 D-827 | Part XIV | L522.s1 |
| CH-0942 | 18 `inputs` | — | D-363 D-732 D-828 | Part XIV | L526.s7, L526.s8 |
| CH-0943 | 18 `inputs` | account, creativity, argument | D-365 D-760 D-820 | Part XIV | L526.s18 |
| CH-0944 | 19 `ruleout` | — | D-366 D-757 D-815 | Part XV | L532.s1 |
| CH-0945 | 19 `ruleout` | ruling, account | D-367 D-729 D-818 | Part XV | L536.s3 |
| CH-0946 | 19 `ruleout` | ruling, inputs, argument | D-368 D-748 D-833 | Part XV | L540.s2 |
| CH-0947 | 19 `ruleout` | provenance, creativity, layers | D-369 D-758 D-810 | Part XV | L542.s1 |
| CH-0948 | 19 `ruleout` | creativity | D-370 D-759 D-811 | Part XV | L544.s1 |
| CH-0949 | 14 `creativity` | — | D-372 D-776 D-839 | Part XVI | L592.s1 |
| CH-0950 | 18 `inputs` | — | D-373 D-733 D-829 | Part XVI | L598.s2 |
| CH-0951 | 18 `inputs` | layers | D-374 D-741 D-822 | Part XVI | L600.s1 |
| CH-0952 | 18 `inputs` | — | D-375 D-749 D-834 | Part XVI | L600.s3 |
| CH-0953 | 4 `layers` | provenance, physical | D-376 D-746 D-831 | Part XVI | L620.s1 |
| CH-0954 | 13 `criticism` | question | D-377 D-747 D-832 | Part XVI | L630.s5 |
| CH-0955 | 1 `frame` | argument | D-378 | Front | L2.s3 |
| CH-0956 | 1 `frame` | criticism, argument | D-379 | Front | L2.s2 |
| CH-0957 | 12 `argument` | ruling | D-380 D-848 | Part 0 | L8.s3 |
| CH-0958 | 7 `account` | physical, question | D-381 D-862 | Part 0 | L49.s5 |
| CH-0959 | 10 `ruling` | argument, rivals | D-382 D-845 | Part 0 | L55.s4 |
| CH-0960 | 2 `organization` | rivals, physical | D-383 D-851 | Part I | L75.s2, L75.s3 |
| CH-0961 | 16 `physical` | layers | D-384 D-865 D-866 | Part I | L75.s6 |
| CH-0962 | 3 `question` | physical, organization | D-385 D-852 | Part III | L159.s3 |
| CH-0963 | 7 `account` | — | D-386 D-863 | Part V | L275.s1 |
| CH-0964 | 12 `argument` | rivals, ruling | D-387 D-842 | Part VI | L315.s13 |
| CH-0965 | 10 `ruling` | argument | D-388 D-856 | Part VI | L315.s14, L315.s15, L315.s16 |
| CH-0966 | 12 `argument` | rivals, ruling | D-389 D-850 D-864 | Part VI | L315.s14, L315.s15, L315.s16 +1 |
| CH-0967 | 13 `criticism` | rivals | D-390 D-872 | Part VI | L315.s18, L315.s19 |
| CH-0968 | 9 `rivals` | ruling | D-391 D-843 D-857 | Part VI | L315.s20, L315.s21 |
| CH-0969 | 10 `ruling` | rivals | D-392 D-870 | Part VI | L317.s8 |
| CH-0970 | 9 `rivals` | ruling | D-393 D-847 | Part VI | L317.s14 |
| CH-0971 | 10 `ruling` | argument | D-394 D-854 | Part IX | L393.s2 |
| CH-0972 | 12 `argument` | — | D-395 D-868 | Part IX | L397.s7 |
| CH-0973 | 14 `creativity` | criticism, physical, argument | D-396 D-869 | Part IX | L397.s11 |
| CH-0974 | 12 `argument` | — | D-397 D-846 | Part IX | L397.s12 |
| CH-0975 | 12 `argument` | — | D-398 D-859 | Part IX | L397.s16 |
| CH-0976 | 12 `argument` | ruling | D-399 D-860 D-861 | Part IX | L397.s18, L397.s19, L397.s20 |
| CH-0977 | 12 `argument` | creativity, ruling | D-400 D-871 | Part X | L429.s4 |
| CH-0978 | 16 `physical` | rivals | D-401 D-867 | Part XII | L461.s4 |
| CH-0979 | 16 `physical` | — | D-402 D-853 | Part XIII | L497.s1 |
| CH-0980 | 18 `inputs` | ruling, argument | D-403 D-855 | Part XIV | L522.s1 |
| CH-0981 | 18 `inputs` | rivals | D-404 D-858 | Part XIV | L526.s15 |
| CH-0982 | 18 `inputs` | account, ruling, creativity | D-405 D-874 | Part XIV | L526.s18 |
| CH-0983 | 19 `ruleout` | ruling, inputs, argument | D-406 D-844 | Part XV | L540.s2 |
| CH-0984 | 1 `frame` | — | D-407 | Front | L2.s1 |
| CH-0985 | 1 `frame` | criticism | D-408 | Front | L2.s2 |
| CH-0986 | 1 `frame` | criticism, argument | D-409 | Front | L2.s4 |
| CH-0987 | 10 `ruling` | argument | D-410 | Part 0 | L8.s7, L8.s8, L8.s9 |
| CH-0988 | 2 `organization` | rivals, argument | D-411 | Part VI | L315.s3 |
| CH-0989 | 13 `criticism` | rivals, question | D-412 | Part VI | L315.s18 |
| CH-0990 | 9 `rivals` | ruling | D-413 | Part VI | L317.s9, L317.s10 |
| CH-0991 | 12 `argument` | ruling | D-414 D-910 | Part VI | L317.s4, L317.s5 |
| CH-0992 | 10 `ruling` | rivals | D-415 | Part VI | L317.s14 |
| CH-0993 | 12 `argument` | ruling | D-416 | Part IX | L397.s7, L397.s8 |
| CH-0994 | 3 `question` | layers | D-417 | Part VIII | L369.s6 |
| CH-0995 | 4 `layers` | inputs | D-418 | Part XVI | L606.s2 |
| CH-0996 | 14 `creativity` | — | D-419 D-901 | Part 0 | L15.s3 |
| CH-0997 | 19 `ruleout` | — | D-420 D-426 D-427 D-451 D-471 D-474 D-475 D-477 D-478 D-879 D-880 D-887 D-939 | Part 0, Part VII … | L17.s1, L17.s2, L61.s2 +6 |
| CH-0998 | 18 `inputs` | — | D-421 D-469 D-485 D-935 D-936 | Part 0, Part XIV … | L31.s3, L520.s1, L596.s1 |
| CH-0999 | 3 `question` | — | D-422 D-432 D-433 D-443 D-891 D-892 D-893 | Part 0, Part III … | L43.s1, L155.s2, L159.s1 +3 |
| CH-1000 | 5 `provenance` | layers | D-423 D-878 | Part 0 | L47.s1 |
| CH-1001 | 11 `constructions` | — | D-424 D-428 D-452 D-899 D-900 | Part 0, Part II … | L49.s3, L105.s1, L343.s9 +1 |
| CH-1002 | 16 `physical` | ruling | D-425 D-886 | Part 0 | L53.s2 |
| CH-1003 | 2 `organization` | — | D-429 D-898 | Part II | L109.s4 |
| CH-1004 | 2 `organization` | — | D-430 D-905 | Part II | L119.s3 |
| CH-1005 | 11 `constructions` | — | D-431 D-897 | Part III | L151.s4, L151.s5, L151.s1 |
| CH-1006 | 5 `provenance` | layers | D-434 D-436 D-915 D-916 | Part IV | L193.s1, L205.s1 |
| CH-1007 | 5 `provenance` | layers, creativity | D-435 D-437 D-913 D-914 | Part IV | L197.s1, L211.s2, L197.s2 |
| CH-1008 | 7 `account` | work | D-438 D-444 D-882 D-917 D-918 D-919 | Part V, Part VI | L231.s3, L231.s4, L257.s3 +2 |
| CH-1009 | 7 `account` | organization | D-439 D-440 D-479 D-883 D-884 | Part V, Part XVI | L233.s1, L235.s1, L556.s2 |
| CH-1010 | 7 `account` | organization | D-441 D-912 | Part V | L245.s4 |
| CH-1011 | 7 `account` | organization | D-442 D-909 | Part V | L255.s4 |
| CH-1012 | 8 `work` | — | D-445 D-920 | Part VI | L305.s1 |
| CH-1013 | 8 `work` | — | D-446 D-921 | Part VI | L311.s1 |
| CH-1014 | 5 `provenance` | constructions, organization | D-447 D-877 | Part VII | L325.s1, L325.s2 |
| CH-1015 | 11 `constructions` | — | D-448 D-449 D-876 D-885 D-931 | Part VII | L329.s5, L329.s6, L331.s1 +1 |
| CH-1016 | 9 `rivals` | account | D-450 D-932 D-934 | Part VII | L339.s3, L339.s4 |
| CH-1017 | 12 `argument` | ruling, account | D-453 D-929 | Part VIII | L369.s5 |
| CH-1018 | 12 `argument` | creativity | D-454 D-455 D-456 D-457 D-459 D-460 D-461 D-462 D-463 D-922 D-923 D-924 D-925 D-926 D-927 | Part IX, Part X … | L375.s1, L377.s2, L379.s1 +8 |
| CH-1019 | 3 `question` | creativity | D-458 D-928 | Part X | L413.s2, L413.s1 |
| CH-1020 | 15 `appraisal` | — | D-464 D-465 D-930 | Part XI | L455.s3 |
| CH-1021 | 16 `physical` | recursion | D-466 D-467 D-468 D-942 D-943 | Part XIII | L495.s3, L497.s1, L505.s1 |
| CH-1022 | 18 `inputs` | ruling | D-470 D-950 | Part XIV | L526.s17, L526.s18 |
| CH-1023 | 19 `ruleout` | ruling | D-472 D-473 D-938 | Part XV | L536.s1, L536.s3 |
| CH-1024 | 19 `ruleout` | ruling, inputs, argument | D-476 D-948 | Part XV | L540.s2 |
| CH-1025 | 7 `account` | organization | D-480 D-949 | Part XVI | L562.s3 |
| CH-1026 | 7 `account` | question | D-481 D-937 | Part XVI | L568.s1, L568.s2 |
| CH-1027 | 6 `surprise` | layers | D-482 D-489 D-941 | Part XVI | L582.s2, L582.s3, L582.s4 +1 |
| CH-1028 | 2 `organization` | creativity, question | D-483 D-484 D-946 | Part XVI | L588.s1, L590.s3, L588.s2 |
| CH-1029 | 18 `inputs` | — | D-486 D-951 | Part XVI | L600.s2, L600.s3 |
| CH-1030 | 18 `inputs` | question | D-487 D-952 | Part XVI | L608.s2, L608.s1 |
| CH-1031 | 4 `layers` | argument | D-488 D-947 | Part XVI | L612.s1, L612.s2, L612.s3 |
| CH-1032 | 3 `question` | organization | D-490 D-944 | Part XVI | L626.s8 |
| CH-1033 | 3 `question` | — | D-491 D-945 | Part XVI | L630.s4, L630.s5 |
| CH-1034 | 10 `ruling` | argument | D-492 | Part VI, Part VIII … | L315.s6, L315.s7, L317.s1 +7 |
| CH-1035 | 10 `ruling` | argument | D-493 | Part VI, Part XIV | L315.s7, L317.s4, L317.s17 +1 |
| CH-1036 | 10 `ruling` | — | D-494 | Part 0, Part I | L8.s6, L8.s7, L67.s1 |
| CH-1037 | 10 `ruling` | — | D-495 | Part I | L75.s2 |
| CH-1038 | 12 `argument` | — | D-496 | Part VI, Part VIII … | L315.s6, L369.s4, L369.s5 +3 |
| CH-1039 | 12 `argument` | ruling | D-497 | Part IX | L397.s5, L397.s12 |
| CH-1040 | 12 `argument` | — | D-498 | — | — |
| CH-1041 | 10 `ruling` | — | D-499 | Part 0, Part VI … | L47.s3, L61.s1, L317.s4 +8 |
| CH-1042 | 7 `account` | organization | D-500 | Part V | L245.s1, L245.s2, L245.s3 +1 |
| CH-1043 | 12 `argument` | ruling | D-501 | Part III | L159.s6 |
| CH-1044 | 10 `ruling` | — | D-502 | Part 0, Part VI … | L17.s3, L17.s4, L315.s6 +2 |
| CH-1045 | 12 `argument` | — | D-503 | Part V | L269.s3 |
| CH-1046 | 2 `organization` | — | D-504 | Part II | L127.s5 |
| CH-1047 | 12 `argument` | — | D-505 | Part 0, Part VI … | L25.s3, L315.s6, L315.s7 +15 |
| CH-1048 | 12 `argument` | ruling | D-506 | Part 0, Part XI … | L25.s3, L441.s1, L441.s2 +2 |
| CH-1049 | 12 `argument` | ruling | D-507 | Part VI | L317.s1, L317.s2, L317.s3 +14 |
| CH-1050 | 10 `ruling` | argument, account | D-508 | Part VI | L317.s1, L317.s2, L317.s3 +14 |
| CH-1051 | 10 `ruling` | argument | D-509 | Part VI | L317.s4 |
| CH-1052 | 9 `rivals` | ruling | D-510 | Part VI | L317.s9 |
| CH-1053 | 12 `argument` | — | D-511 | Part IX | L373.s1, L387.s1 |
| CH-1054 | 12 `argument` | — | D-512 | Part IX, Part XVI | L393.s4, L608.s2 |
| CH-1055 | 13 `criticism` | — | D-513 | Part IX | L383.s2 |
| CH-1056 | 12 `argument` | — | D-514 D-579 D-646 | Part IX | L385.s2 |
| CH-1057 | 10 `ruling` | appraisal, rivals | D-515 | Part I | L71.s1, L71.s2, L71.s3 |
| CH-1058 | 10 `ruling` | — | D-516 | Part III, Part XIV … | L159.s7, L522.s2, L534.s3 |
| CH-1059 | 18 `inputs` | — | D-517 | Part 0, Part XIV | L25.s2, L522.s2, L522.s3 |
| CH-1060 | 12 `argument` | — | D-518 | Part XV, Part XVI | L546.s1, L550.s1 |
| CH-1061 | 12 `argument` | — | D-519 | Part 0, Part II … | L49.s3, L105.s1, L277.s4 +15 |
| CH-1062 | 12 `argument` | — | D-520 | Part VI, Part XV … | L305.s1, L305.s5, L542.s1 +3 |
| CH-1063 | 12 `argument` | recursion | D-521 | Part XIII, Part XV | L495.s2, L542.s1, L544.s1 |
| CH-1064 | 12 `argument` | — | D-522 | Part X | L429.s1, L429.s2, L429.s3 +1 |
| CH-1065 | 11 `constructions` | provenance, creativity, argument | D-523 | Part 0, Part III … | L47.s2, L155.s1, L155.s4 +14 |
| CH-1066 | 18 `inputs` | — | D-524 | Part 0, Part IV … | L13.s1, L29.s1, L31.s1 +19 |
| CH-1067 | 4 `layers` | inputs | D-525 | Part 0, Part IV … | L47.s1, L171.s1, L175.s1 +4 |
| CH-1068 | 18 `inputs` | argument | D-526 | Part IV, Part VII | L211.s4, L325.s7 |
| CH-1069 | 18 `inputs` | — | D-527 | Part XIV, Part XVI | L526.s17, L526.s18, L598.s2 |
| CH-1070 | 7 `account` | organization | D-528 | Part II, Part V … | L119.s3, L119.s5, L233.s1 +13 |
| CH-1071 | 14 `creativity` | argument | D-529 | Part X, Part XII | L427.s4, L475.s3 |
| CH-1072 | 12 `argument` | — | D-530 | Part 0 | L49.s2 |
| CH-1073 | 3 `question` | inputs | D-531 | Part XVI | L608.s2 |
| CH-1074 | 18 `inputs` | criticism | D-532 | Part 0, Part XIV | L31.s2, L524.s2 |
| CH-1075 | 7 `account` | ruling | D-533 | Part I, Part VIII … | L75.s4, L369.s2, L369.s4 +1 |
| CH-1076 | 11 `constructions` | account | D-534 | Part III, Part V … | L151.s4, L255.s3, L606.s2 +1 |
| CH-1077 | 13 `criticism` | question, work | D-535 | Part I, Part III … | L67.s2, L69.s1, L69.s3 +6 |
| CH-1078 | 13 `criticism` | account | D-536 | Part 0 | L41.s1, L41.s4 |
| CH-1079 | 7 `account` | ruling | D-537 | Part 0 | L43.s3 |
| CH-1080 | 3 `question` | — | D-538 | Part 0 | L43.s1, L43.s5 |
| CH-1081 | 10 `ruling` | account, physical | D-539 | Part I | L67.s1 |
| CH-1082 | 3 `question` | — | D-540 | Part VI, Part XVI | L317.s4, L630.s4 |
| CH-1083 | 6 `surprise` | account, organization | D-541 | Part 0, Part V … | L39.s2, L245.s2, L528.s1 +1 |
| CH-1084 | 19 `ruleout` | argument, account | D-542 | Part XV | L538.s1, L538.s2 |
| CH-1085 | 3 `question` | argument, account | D-543 | Part III | L159.s5, L159.s6 |
| CH-1086 | 12 `argument` | — | D-544 | Part 0 | L37.s3 |
| CH-1087 | 2 `organization` | argument | D-545 | Part 0, Part XV | L17.s4, L57.s1, L536.s1 |
| CH-1088 | 16 `physical` | — | D-546 | Part 0 | L13.s7 |
| CH-1089 | 14 `creativity` | — | D-547 | Part XI | L443.s1 |
| CH-1090 | 14 `creativity` | surprise | D-548 | Part XI | L443.s1 |
| CH-1091 | 13 `criticism` | — | D-549 | — | — |
| CH-1092 | 13 `criticism` | physical | D-550 | Part 0, Part I | L45.s4, L75.s1 |
| CH-1093 | 6 `surprise` | — | D-551 | Part IV, Part XVI | L177.s2, L201.s1, L215.s1 +4 |
| CH-1094 | 9 `rivals` | appraisal | D-552 | Part 0 | L51.s3 |
| CH-1095 | 15 `appraisal` | — | D-553 | Part 0, Part XI … | L25.s2, L31.s1, L51.s1 +5 |
| CH-1096 | 15 `appraisal` | — | D-554 | Part 0 | L25.s1, L25.s2 |
| CH-1097 | 15 `appraisal` | criticism | D-555 | Part XI | L455.s1 |
| CH-1098 | 15 `appraisal` | — | D-556 | Part 0, Part VI … | L25.s1, L317.s9, L441.s3 +1 |
| CH-1099 | 7 `account` | — | D-557 | Part V | L277.s2 |
| CH-1100 | 7 `account` | — | D-558 | — | — |
| CH-1101 | 10 `ruling` | — | D-559 | Part V | L277.s3 |
| CH-1102 | 7 `account` | — | D-560 | Part XII | L469.s1 |
| CH-1103 | 16 `physical` | — | D-561 | Part XII | L479.s4 |
| CH-1104 | 13 `criticism` | appraisal | D-562 | Part XI | L433.s1 |
| CH-1105 | 14 `creativity` | — | D-563 | Part XV, Part XVI | L544.s1, L592.s1 |
| CH-1106 | 14 `creativity` | layers | D-564 | Part 0, Part VI … | L25.s3, L307.s4, L427.s3 +2 |
| CH-1107 | 18 `inputs` | argument | D-565 | Part 0, Part XV | L61.s1, L534.s1 |
| CH-1108 | 10 `ruling` | argument | D-566 | Part VIII | L369.s4 |
| CH-1109 | 17 `recursion` | physical | D-567 | Part XIII | L497.s1 |
| CH-1110 | 8 `work` | — | D-568 D-622 | Part VI, Part VII … | L285.s1, L299.s2, L305.s1 +14 |
| CH-1111 | 10 `ruling` | — | D-569 D-623 | Part VI, Part VIII … | L315.s6, L315.s7, L317.s1 +7 |
| CH-1112 | 10 `ruling` | — | D-570 D-624 | Part VI, Part XIV | L315.s7, L317.s4, L317.s15 +2 |
| CH-1113 | 10 `ruling` | — | D-571 D-625 D-626 | Part VI, Part VIII | L315.s6, L315.s7, L369.s4 +24 |
| CH-1114 | 19 `ruleout` | ruling | D-572 D-627 | Part XV | L534.s1 |
| CH-1115 | 10 `ruling` | argument | D-573 D-630 | Part VI | L317.s4 |
| CH-1116 | 9 `rivals` | ruling | D-574 D-634 | Part VI | L317.s9 |
| CH-1117 | 12 `argument` | — | D-575 D-635 | Part VI, Part VIII … | L315.s6, L369.s4, L369.s5 +3 |
| CH-1118 | 12 `argument` | ruling | D-576 D-638 D-639 | Part IX | L397.s5, L397.s12 |
| CH-1119 | 12 `argument` | ruling | D-577 D-643 D-644 | Part IX, Part XVI | L393.s4, L608.s2 |
| CH-1120 | 13 `criticism` | argument | D-578 D-645 | Part IX, Part XII | L383.s2, L377.s1, L475.s3 |
| CH-1121 | 10 `ruling` | argument | D-580 D-647 | Part IX | L395.s1 |
| CH-1122 | 12 `argument` | frame | D-581 D-649 | Part XV, Part XVI | L546.s1, L550.s1 |
| CH-1123 | 12 `argument` | — | D-582 D-650 | — | — |
| CH-1124 | 2 `organization` | — | D-583 D-652 | Part XVI | L552.s1 |
| CH-1125 | 10 `ruling` | recursion, argument | D-584 D-656 D-657 D-659 D-660 | Part XIV, Part V … | L526.s15, L526.s18, L277.s4 +7 |
| CH-1126 | 18 `inputs` | — | D-585 D-661 D-662 | Part 0, Part II … | L29.s1, L13.s1, L31.s1 +33 |
| CH-1127 | 18 `inputs` | — | D-586 D-663 D-664 D-665 D-666 D-667 | Part IV, Part 0 … | L211.s4, L31.s1, L31.s2 +25 |
| CH-1128 | 7 `account` | — | D-587 D-673 | Part II, Part V … | L119.s3, L119.s5, L233.s1 +12 |
| CH-1129 | 3 `question` | inputs | D-588 D-677 D-678 D-679 D-680 D-681 D-685 | Part VIII, Part 0 … | L369.s2, L369.s4, L31.s1 +34 |
| CH-1130 | 7 `account` | layers, ruling | D-589 D-687 | Part 0, Part IV | L43.s3, L211.s1, L223.s4 |
| CH-1131 | 18 `inputs` | — | D-590 D-688 D-689 D-690 D-691 D-692 D-693 D-694 D-695 D-696 D-697 | Part III, Part XIII … | L159.s1, L159.s2, L159.s3 +54 |
| CH-1132 | 15 `appraisal` | frame | D-591 D-698 | Part 0, Part XI … | L31.s4, L433.s1, L443.s2 +5 |
| CH-1133 | 10 `ruling` | — | D-592 D-703 D-704 | Part I, Part 0 | L67.s1, L17.s1, L17.s2 +2 |
| CH-1134 | 7 `account` | — | D-593 D-706 D-707 | Part XII, Part VI … | L469.s1, L307.s5, L309.s1 +6 |
| CH-1135 | 15 `appraisal` | — | D-594 D-709 D-710 D-711 D-712 D-713 D-714 | Part V, Part XI … | L277.s1, L277.s3, L277.s4 +19 |
| CH-1136 | 14 `creativity` | rivals, question | D-595 D-716 | Part XV, Part XVI | L544.s1, L592.s1, L592.s2 +1 |
| CH-1137 | 7 `account` | argument | D-596 D-654 D-655 | Part V, Part 0 | L245.s1, L245.s2, L245.s3 +2 |
| CH-1138 | 12 `argument` | — | D-597 | — | — |
| CH-1139 | 3 `question` | account, constructions | D-598 | Part VII | L331.s3 |
| CH-1140 | 16 `physical` | — | D-599 | Part X | — |
| CH-1141 | 14 `creativity` | criticism, argument | D-600 | Part 0, Part VII | L25.s3, L335.s2 |
| CH-1142 | 7 `account` | — | D-601 | Part 0 | L41.s1 |
| CH-1143 | 12 `argument` | — | D-602 | Part 0 | L49.s2 |
| CH-1144 | 3 `question` | inputs | D-603 | Part III | L159.s7 |
| CH-1145 | 10 `ruling` | argument, account | D-604 | Part VI | L317.s7 |
| CH-1146 | 14 `creativity` | physical, argument | D-605 | Part X | L427.s4 |
| CH-1147 | 15 `appraisal` | — | D-606 | Part XI | L441.s3 |
| CH-1148 | 14 `creativity` | physical | D-607 | Part XII | L475.s3 |
| CH-1149 | 18 `inputs` | argument, account | D-608 | Part XIV | L526.s18 |
| CH-1150 | 3 `question` | inputs | D-609 | Part XVI | L608.s2 |
| CH-1151 | 3 `question` | organization | D-610 | Part XVI | L630.s4 |
| CH-1152 | 14 `creativity` | — | D-611 | Part I, Part XVI | L75.s2, L632.s2 |
| CH-1153 | 11 `constructions` | — | D-612 | Part VII | L343.s1 |
| CH-1154 | 12 `argument` | account | D-613 | Part VI | L317.s14 |
| CH-1155 | 18 `inputs` | argument | D-614 | Part 0, Part XV | L61.s1, L534.s1 |
| CH-1156 | 14 `creativity` | — | D-615 | Part XVI | L592.s1 |
| CH-1157 | 10 `ruling` | argument | D-616 | Part VIII | L369.s4 |
| CH-1158 | 3 `question` | account | D-617 | Part V | L277.s3 |
| CH-1159 | 7 `account` | — | D-618 | Part 0, Part XV | L17.s4, L536.s1 |
| CH-1160 | 2 `organization` | — | D-619 | Part 0 | L57.s1 |
| CH-1161 | 14 `creativity` | inputs, frame | D-620 | Part 0 | L13.s7 |
| CH-1162 | 10 `ruling` | account, physical | D-621 | Part I | L67.s1 |
| CH-1163 | 2 `organization` | — | D-628 | Part II, Part VI | L127.s5, L317.s1 |
| CH-1164 | 12 `argument` | — | D-629 | Part VI | L317.s4, L317.s5, L317.s7 +2 |
| CH-1165 | 10 `ruling` | — | D-631 | — | — |
| CH-1166 | 10 `ruling` | rivals | D-632 | — | — |
| CH-1167 | 7 `account` | question | D-633 | Part VI | L317.s11 |
| CH-1168 | 12 `argument` | — | D-636 | Part IX | L397.s1 |
| CH-1169 | 12 `argument` | — | D-637 | Part IX | L397.s1 |
| CH-1170 | 12 `argument` | ruling | D-640 | Part IX | L397.s1 |
| CH-1171 | 12 `argument` | criticism | D-641 | Part IX | L373.s1 |
| CH-1172 | 12 `argument` | — | D-642 | Part IX | L387.s1 |
| CH-1173 | 10 `ruling` | appraisal, rivals | D-648 | Part I | L71.s1, L71.s2, L71.s3 |
| CH-1174 | 8 `work` | — | D-651 | Part VI, Part XV | L305.s1, L542.s1 |
| CH-1175 | 12 `argument` | — | D-653 | Part XVI | L558.s1 |
| CH-1176 | 12 `argument` | creativity | D-658 | Part X | L429.s1, L429.s2, L429.s3 +1 |
| CH-1177 | 18 `inputs` | creativity | D-668 | Part 0, Part XVI | L13.s7, L598.s2 |
| CH-1178 | 18 `inputs` | — | D-669 | Part XVI | L598.s1, L598.s2 |
| CH-1179 | 18 `inputs` | — | D-670 | Part XIV | L526.s17 |
| CH-1180 | 18 `inputs` | creativity, physical, layers, ruling | D-671 | Part XIV | L526.s1, L526.s2, L526.s3 +15 |
| CH-1181 | 4 `layers` | inputs | D-672 | Part 0, Part IV … | L47.s1, L171.s1, L175.s1 +4 |
| CH-1182 | 5 `provenance` | creativity, argument | D-674 | Part III, Part IV … | L155.s4, L197.s1, L225.s3 +4 |
| CH-1183 | 7 `account` | constructions | D-675 | Part VII, Part XVI | L343.s5, L343.s6, L632.s1 |
| CH-1184 | 5 `provenance` | argument | D-676 | Part IV | L211.s1, L211.s2, L211.s3 +1 |
| CH-1185 | 13 `criticism` | question | D-682 | Part I, Part IV … | L69.s3, L211.s2, L403.s3 |
| CH-1186 | 13 `criticism` | work, ruling | D-683 | Part I | L69.s1 |
| CH-1187 | 7 `account` | — | D-684 | Part I, Part III … | L67.s2, L157.s1, L245.s1 |
| CH-1188 | 11 `constructions` | — | D-686 | Part IX | L393.s4 |
| CH-1189 | 13 `criticism` | — | D-699 | Part XI | L443.s2, L443.s3 |
| CH-1190 | 6 `surprise` | — | D-700 | Part IV, Part XVI | L177.s1, L177.s2, L223.s5 +2 |
| CH-1191 | 6 `surprise` | — | D-701 | Part IV | L201.s1, L201.s2, L201.s3 +1 |
| CH-1192 | 9 `rivals` | appraisal | D-702 | Part 0 | L51.s3 |
| CH-1193 | 10 `ruling` | inputs | D-705 | Part I | L75.s2 |
| CH-1194 | 16 `physical` | — | D-708 | Part XII | L479.s1 |
| CH-1195 | 13 `criticism` | — | D-715 | Part 0, Part I … | L45.s4, L75.s1, L147.s1 +10 |
| CH-1196 | 17 `recursion` | physical | D-717 | Part XIII | L497.s1 |
| CH-1197 | 12 `argument` | ruling | D-742 D-826 | Part IX | L397.s16 |
| CH-1198 | 12 `argument` | — | D-743 | Part IX | L397.s7 |
| CH-1199 | 6 `surprise` | — | D-763 D-785 | Part IV | L221.s1 |
| CH-1200 | 6 `surprise` | — | D-764 D-786 | Part IV, Part XI … | L215.s1, L221.s1, L223.s1 +10 |
| CH-1201 | 6 `surprise` | — | D-765 D-787 | Part IV | L215.s1 |
| CH-1202 | 13 `criticism` | — | D-766 D-788 | Part IV, Part VI … | L223.s5, L317.s17, L429.s1 +1 |
| CH-1203 | 16 `physical` | question | D-769 D-791 | Part 0 | L43.s2 |
| CH-1204 | 3 `question` | account, argument | D-770 D-792 | Part 0 | L43.s5 |
| CH-1205 | 14 `creativity` | — | D-772 D-836 | Part X | L403.s3 |
| CH-1206 | 13 `criticism` | appraisal | D-775 D-841 | Part XI | L455.s1 |
| CH-1207 | 10 `ruling` | argument | D-780 | Part 0 | L17.s3 |
| CH-1208 | 12 `argument` | frame, ruling | D-812 | Part IX | L393.s1 |
| CH-1209 | 2 `organization` | rivals, layers, account | D-849 | Part VI | L315.s11 |
| CH-1210 | 9 `rivals` | — | D-873 | Part VI | L317.s1, L317.s2, L317.s3 +14 |
| CH-1211 | 12 `argument` | — | D-875 | Part VI | L317.s1, L317.s2, L317.s3 +14 |
| CH-1212 | 7 `account` | — | D-881 | Part VI | L301.s1 |
| CH-1213 | 3 `question` | provenance | D-888 | Part III | L147.s2 |
| CH-1214 | 3 `question` | provenance | D-889 | Part III | L155.s6 |
| CH-1215 | 18 `inputs` | question, physical | D-890 | Part 0 | L31.s2 |
| CH-1216 | 19 `ruleout` | provenance | D-894 | Part 0 | L61.s2 |
| CH-1217 | 19 `ruleout` | — | D-895 | Part XV | L536.s1, L536.s2, L536.s3 |
| CH-1218 | 3 `question` | organization | D-896 | Part III | L141.s3 |
| CH-1219 | 20 `form` | organization | D-902 | Part 0 | L11.s4 |
| CH-1220 | 20 `form` | argument | D-903 | Part 0 | L15.s2 |
| CH-1221 | 4 `layers` | argument | D-904 | Part VI | L315.s5 |
| CH-1222 | 18 `inputs` | — | D-906 | Part 0 | L31.s4 |
| CH-1223 | 7 `account` | — | D-907 | Part 0 | L43.s3 |
| CH-1224 | 7 `account` | — | D-908 | Part V | L257.s3 |
| CH-1225 | 9 `rivals` | — | D-911 | Part VI | L317.s1, L317.s2, L317.s3 +14 |
| CH-1226 | 11 `constructions` | question, organization | D-933 | Part VII | L347.s1, L347.s2, L347.s3 |
| CH-1227 | 6 `surprise` | — | D-940 | Part XVI | L580.s1 |
| CH-1228 | 9 `rivals` | — | E-1 | Part VI | L317.s16 |
| CH-1229 | 9 `rivals` | ruling | E-2 | Part VI | L317.s16 |
| CH-1230 | 2 `organization` | — | E-3 E-30 | Part VI | L299.s3 |
| CH-1231 | 7 `account` | — | E-4 E-31 | Part VI | L301.s1 |
| CH-1232 | 18 `inputs` | — | E-5 E-32 | Part XIV | L526.s5 |
| CH-1233 | 2 `organization` | account, physical | E-6 | Part VI | L301.s1 |
| CH-1234 | 12 `argument` | rivals, account, ruling | E-7 | Part VI | L317.s4 |
| CH-1235 | 14 `creativity` | rivals, argument, criticism | E-8 | Part X | L429.s2 |
| CH-1236 | 14 `creativity` | rivals | E-9 | Part X | L429.s1 |
| CH-1237 | 12 `argument` | — | E-10 E-23 | Part VI | L315.s11 |
| CH-1238 | 12 `argument` | ruling | E-11 E-24 | Part VI | L315.s14 |
| CH-1239 | 9 `rivals` | — | E-12 E-27 | Part VI | L315.s1 |
| CH-1240 | 10 `ruling` | — | E-13 E-28 | Part VI | L315.s7 |
| CH-1241 | 18 `inputs` | rivals | E-14 | Part XIV | L526.s15 |
| CH-1242 | 3 `question` | argument, physical, organization | E-15 E-22 | Part III | L159.s6 |
| CH-1243 | 13 `criticism` | — | E-16 E-19 | Part XI | L441.s4 |
| CH-1244 | 9 `rivals` | — | E-17 | Part VI | L317.s11 |
| CH-1245 | 9 `rivals` | — | E-18 | Part 0 | L25.s3 |
| CH-1246 | 14 `creativity` | rivals, argument, criticism | E-20 | Part X | L429.s2 |
| CH-1247 | 10 `ruling` | rivals, account, argument | E-21 | Part VI | L317.s4 |
| CH-1248 | 12 `argument` | — | E-25 | Part IX | L379.s1 |
| CH-1249 | 18 `inputs` | ruling | E-26 | Part XIV | L517.s1 |
| CH-1250 | 9 `rivals` | — | E-29 | Part VI | L317.s11 |
| CH-1251 | 13 `criticism` | rivals | E-33 | — | — |
| CH-1252 | 9 `rivals` | — | E-34 | — | — |
| CH-1253 | 7 `account` | — | E-35 | — | — |
| CH-1254 | 4 `layers` | organization | E-36 | Part II | L119.s1, L119.s2, L119.s3 +5 |
| CH-1255 | 6 `surprise` | frame, rivals | E-37 | — | — |
| CH-1256 | 4 `layers` | inputs, question | E-38 | Part VIII | L367.s1, L367.s2 |
| CH-1257 | 12 `argument` | criticism, question | E-39 E-44 | Part III | L159.s4 |
| CH-1258 | 8 `work` | — | E-40 | Part VI | L313.s2 |
| CH-1259 | 7 `account` | — | E-41 | Part V | L277.s1 |
| CH-1260 | 8 `work` | account | E-42 | Part VI | L313.s1, L313.s2, L313.s3 |
| CH-1261 | 4 `layers` | question, inputs | E-43 | Part VIII | L367.s1, L367.s2 |
| CH-1262 | 8 `work` | — | E-45 | Part VI | L313.s2 |
| CH-1263 | 8 `work` | — | E-46 | Part VI | L313.s3 |
| CH-1264 | 8 `work` | — | E-47 | Part VI | L313.s1, L313.s2, L313.s3 |
| CH-1265 | 12 `argument` | criticism | E-48 | Part VIII | L369.s2 |
| CH-1266 | 8 `work` | account, question | E-49 | Part VI | L293.s2 |
| CH-1267 | 8 `work` | — | E-50 | Part VI | L313.s3 |
| CH-1268 | 8 `work` | — | E-51 | Part VI | L313.s1, L313.s2, L313.s3 |
| CH-1269 | 18 `inputs` | layers | E-52 | Part VIII | L367.s1, L367.s2 |
| CH-1270 | 8 `work` | — | E-53 | Part VI | L313.s2 |
| CH-1271 | 11 `constructions` | — | E-54 | Part VII | L321.s1 |
| CH-1272 | 18 `inputs` | layers | E-55 | Part VIII | L367.s2 |
| CH-1273 | 1 `frame` | — | E-56 | Part 0 | — |
| CH-1274 | 7 `account` | work, argument | E-57 | Part VI | — |
| CH-1275 | 8 `work` | — | E-58 | Part VI | — |
