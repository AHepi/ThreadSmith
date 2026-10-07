# S100 — Strong candidates and the most altered sections

*Log S100, 26 September 2026, under decision S31. Made by program (`S100 Strong candidates and the most altered sections - script.py`), from the S98 ledger (`results/S98 Ledger of edits and recommendations/`) and the ten theory texts from file 10 to the latest text; nothing in them was changed. One agent (decision S22). Sentences are quoted byte for byte; no reason given for any change or proposal is copied.*

## What was asked

The owner, 26 September 2026, answering Claude's suggestion "For your 'strong candidates', I'd start with the sentences that came through many rounds without being touched, while the sentences around them kept changing.": "Yup do that. Also collect the sections that are most altered. Because they might tell me what isn't well understand, what's difficult to express in prose or whatever." Earlier, the aim: to "isolate the strong candidates, See what else they depend on and maybe even figure out, for example, whether values should be part of the theory, or separate."

## In short

- **The unit** is the ledger's: a sentence, heading, displayed formula or list item of the latest text (756). Headings (55) and the dated note on how the text was made (7 sentences, line 2) are left out of the candidate lists; 694 units remain.
- **Untouched in substance:** 327 of the 694 have no criticism-driven change, no owner-directed change and no replaced wording in the ledger, and no change between versions that the ledger has no record of; 260 of them have been in the text since file 10.
- **Thresholds:** in all ten versions (since file 10, through all 22 rounds), and neighbours that averaged at least 1.21 substantive changes each, the upper quartile over all 694 units.
- **Strong candidates:** 36, of which 7 were **challenged and kept** (a proposal was made against the sentence and not taken) and 29 were **never challenged** (no proposal ever touched the sentence alone; it may simply never have been examined).
- **Most altered:** the ten sections with the most criticism-driven changes per unit are (Prov) Genesis (6 per unit); (QF) Question-finding (4 per unit); (Nec) Necessity (4 per unit); (Elim) Reinstatement of kinds (4 per unit); (Suff) Sufficiency (4 per unit); Declared inputs (2 per unit); Grievances, anticipated / introduction (2 per unit); What is imported, what is an index, and what is defined (1.8 per unit); Ownership (1.75 per unit); Grievances, anticipated / 6. "You have replaced explanation with evolution." (1.67 per unit).
- **Where the most altered stand:** 5 of those ten are items of the theory's own list of what would rule it out (group G15), 2 are about what the theory imports, takes as input or defines (group G14), and the other 3 are Grievances, anticipated / introduction; Ownership; Grievances, anticipated / 6. "You have replaced explanation with evolution.". Owner-directed passes account for at most 15% of any one's churn.
- **Wordings that came back:** 1 unit holds a wording that repeats an earlier one after a different wording between (1 exactly, 0 all but a few characters); 34 phrases were added and later taken out, or taken out and later put back.

## 1. How the measures were made

### 1.1 Versions and rounds

Each unit of the latest text was followed back through the chain file 10 → file 11 → drafts 1 to 5 → scrubbed copy → repaired copy → latest text, one step at a time, by program: the ledger's line maps (`group/line maps.json`) name the earlier line or lines; on them, the same sentence in any wording is the one with the same text, or failing that the most similar one (similarity at least 0.5 on the whole sentence, and at least 0.45 once formula markup is set aside, unless 0.65 or more), or one that holds the unit as a part (a split); failing those, a sentence anywhere in the earlier text with similarity at least 0.6 (moved). The first version reached is where the unit first stands. Links made: moved 8, part of 2, reworded 538, same 5178.

| first in | file 10 | file 11 | draft 1 | draft 2 | draft 3 | draft 4 | draft 5 | scrubbed copy | repaired copy | latest text |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| units (all 756) | 516 | 53 | 49 | 15 | 1 | 26 | 1 | 29 | 55 | 11 |
| units (694, no headings, no note) | 463 | 52 | 49 | 14 | 1 | 26 | 1 | 25 | 52 | 11 |

"Rounds" are the ledger's 22 rounds of edits and proposals, in its order (file 20 and R2 to S97). A unit in file 10 came through all 22; one first in file 11 through the ten from S81; one first in a draft of revision 2 through those from the round that read that draft (S90 read drafts 1 and 2, S91 and S93 draft 4, S94 and S95 draft 5, S96 the scrubbed copy, S97 the repaired copy).

### 1.2 What each record of the ledger counts as

A record touches a unit when the unit is among its sentences in the latest text (`latest_sentences`: its home sentence, its pointer sentences and, for a vocabulary record, every sentence it names). Records with no sentence in the latest text (319) are counted only for their section (§4). Every record is one of three classes:

- **Vocabulary only** (515 records): what the ledger marks as vocabulary, scope `term` or `whole text`, and the scrub's edits that its own list marks `swap` (265 of the 300 edits of `S95 Scrub - scripts/replacements.json`).
- **Owner-directed** (76 records): the scrub's other edits (its 33 marked `rewording` and the two lines it filled, lines 2 and 8); the S96 repair of physical possibility, conflict and premises (groups P, C, F and G of `S96 Repair - scripts/replacements.json`, on decisions S23 to S27, and its rewrite of the dated note); the S28 wording points (group O of `replacements_stage3.json`, and every entry whose ruling names S28) and the note of that stage (group N).
- **Criticism-driven** (1303 records): everything else — the readers' and auditors' proposals, the rulings, the errata and the defects, the change list of revision 2, the repairs the S95 readings asked for (group R of the S96 repair, applied with the owner-directed pass but found by readers), the second stage after the two readings of the first, and the S97 rulings on the outside cross-examination (group X).

Changes are counted once each (the ledger's `change_id`), not once per record: a change with an applied record, other than one applied only in a note, is an **applied change** of the unit, classed vocabulary only if all its applied records are, owner-directed if any is, and criticism-driven otherwise. 64 applied records changed only a note (the revision note, the revision record, the note of sources) and are not counted as changes. A change with no applied record and at least one proposal (a recommendation, or an edit declined or not applied) is a **proposal** of the unit, with the first of these outcomes among its records: open for the owner, declined, not applied, superseded, unknown. A **replaced wording** is a distinct wording of a record whose status is superseded (applied in a draft or in the S96 stage-1 text and later changed, or proposed and replaced by a later wording).

- **Substantive changes** of a unit: criticism-driven changes + owner-directed changes + replaced wordings other than vocabulary ones.
- **Total churn:** criticism-driven + owner-directed + vocabulary-only changes + all replaced wordings.
- **Neighbours:** the other units of its section and the units within two either side in text order (headings included, the dated note left out). **Neighbour churn** is the mean of their substantive changes.
- **Changes in the texts the ledger does not hold:** each step between versions where the unit's text differs is marked *layout* (only emphasis or spacing, or a unit joined with or split from its neighbour), *vocabulary* (after draft 5, on a unit whose only applied changes are vocabulary only), *recorded* (the unit has a substantive change in the ledger) or *unrecorded* (none of these).

Owner-directed passes add to churn by design: they touched sentences because the owner asked for a change of words or of what the theory says, not because a reader found a fault there. Every count below gives them apart.

## 2. Distributions, and where the cuts fall

### 2.1 Substantive changes per unit

| substantive changes | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| units | 331 | 194 | 92 | 39 | 17 | 8 | 9 | 2 | 1 | 1 |

331 of 694 units have none. 4 of those have a change in the texts that the ledger holds for no record on them, and are left out of the lists (§3.4). That leaves 327 units untouched in substance, which are allowed vocabulary-only changes and layout: 199 of them have no change of any kind in any version.

### 2.2 How long the untouched units have stood

| versions carried | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| all 694 units | 11 | 52 | 25 | 1 | 26 | 1 | 14 | 49 | 52 | 463 |
| untouched in substance | 0 | 16 | 13 | 0 | 13 | 0 | 6 | 18 | 1 | 260 |

The untouched units fall into two clumps: 260 have stood in all ten versions, since file 10, and 48 are no older than draft 1; between them stand only 19 (in 9 versions, since file 11, or 8, since draft 1). The cut is taken at all ten versions: those units came through all 22 rounds. The 4 of 8 or 9 versions that pass every other test are listed apart (§3.3).

### 2.3 Neighbour churn

| quantile | 0 | 0.1 | 0.25 | 0.5 | 0.75 | 0.9 | 1 | mean |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| all 694 units | 0 | 0.18 | 0.46 | 0.84 | 1.21 | 1.6 | 7.25 | 0.95 |
| untouched, in all ten versions (260) | 0 | 0.11 | 0.25 | 0.5 | 1 | 1.33 | 2.75 | 0.66 |

Untouched units in all ten versions, by neighbour churn (steps of 0.25; the last column is 3 or more):

| neighbour churn from | 0 | 0.25 | 0.5 | 0.75 | 1 | 1.25 | 1.5 | 1.75 | 2 | 2.25 | 2.5 | 2.75 | 3 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| units | 62 | 40 | 49 | 34 | 40 | 21 | 6 | 3 | 2 | 1 | 1 | 1 | 0 |

How many candidates each cut would give:

| neighbour churn at least | 0.5 | 0.75 | 1 | 1.21 | 1.5 | 2 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| candidates | 158 | 109 | 75 | 36 | 14 | 5 |
| of them challenged and kept | 23 | 21 | 14 | 7 | 5 | 1 |

The cut is the upper quartile of neighbour churn over all 694 units, 1.21: a candidate's neighbours changed more than those of three units in four. Half of all units have neighbours with fewer than 0.84 substantive changes each. The distribution has no gap to cut at; the quartile is a plain, stated line, and the table above shows what a lower or higher line would give.

## 3. Strong candidates

Each unit: its wording now, where it stands, how long it has stood, what changed in it (vocabulary only, if anything), its neighbours' churn, the proposals it came through (list 1 only), the terms it uses (the ledger's term list, matched as the ledger matched them) and what the dependence order of the latest text says those terms depend on. The dependence order names conditions by their tags; the match from a unit's words to a tag is by program (for example "account" to (E), "question" to (Q)) and is a lead, not a reading.

| list | units | by group |
| --- | ---: | --- |
| challenged and kept | 7 | G05 1, G09 1, G11 3, G14 1, G15 1 |
| never challenged | 29 | G01 1, G02 9, G03 3, G04 7, G05 1, G06 1, G09 4, G11 1, G12 1, G14 1 |

### 3.1 Challenged and kept

Proposals were made against these units and were declined, not applied, replaced by a later wording, or are open; each unit stands with no change in substance.

| unit | section | since | neighbour churn | proposals (outcome) | vocabulary-only changes |
| --- | --- | --- | ---: | --- | ---: |
| L546.s1 | A mathematical error | file 10 | 2.5 | 1 declined | 5 |
| L255.s1 | Non-circular dependence | file 10 | 1.8 | 1 not applied | 0 |
| L441.s4 | The aims of a repair | file 10 | 1.8 | 1 declined | 0 |
| L51.s1 | Grievances, anticipated / 8. "Where is aesthetics?" | file 10 | 1.75 | 1 not applied | 2 |
| L517.s1 | Imports | file 10 | 1.5 | 1 declined | 2 |
| L389.s1 | Usability | file 10 | 1.33 | 1 not applied | 1 |
| L437.s1 | Repair | file 10 | 1.25 | 1 declined | 0 |

**L546.s1** · sentence · Part XV · A mathematical error (line 546) · group G15 What would rule this class out

> **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 5 vocabulary-only changes (the ledger marks them); the ledger's vocabulary records on it: "A counterexample to the finite monotone theorem," → "A counterexample to the finite monotone claim," (D-242, S95); "Derivations" → "Arguments" (D-243, S95); "Derivation 1–10; Derivations" → "Argument 1–10; Arguments" (D-518, S95); "theorem; Corollary" → "claim; Consequence" (D-520, S95); "Derivation 1–10; "Derivations" → Argument 1–10; "Arguments"" → "Needs row 13's general definition." (D-581, S95); "**Derivation 1–10**; Part XVI title "Derivations"; "Derivations 1–3" (Part XV)" → "**Argument 1–10**; "Arguments"; "Arguments 1–3"" (D-649, S95).
- Earlier wording:
  - file 10 to draft 5:
    > **A mathematical error.** A counterexample to the finite monotone theorem, (I2), (O1), (T2), (CT2), or Derivations 1–3 under their stated assumptions.
- Neighbours (4: the other units of its section and the units within two either side): 2.5 substantive changes each on average (criticism-driven alone: 2.5).
- Proposals it came through (1):
  - A-23 · file 20 (before log 25) · edit · declined · written against file 10 · source: results/S62 Stage D and report - return/07 Quotations.md — XV-earlier-6 (earlier) / XV-revised-8 (revised), earlier sentence 1-1, revised sentence 1-1 · placed by the line it was written against, not by its own words
    > **A mathematical error.** A counterexample to the finite monotone theorem, (I2), (O1), (T2), (CT2), or Derivations 1–3 and 8 under their stated assumptions.
- Terms it uses (the ledger's term list): (CT2), argument, Finite monotone claim.

**L255.s1** · sentence · Part V · Non-circular dependence (line 255) · group G05 Account

> **Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (5: the other units of its section and the units within two either side): 1.8 substantive changes each on average (criticism-driven alone: 0.6).
- Proposals it came through (1):
  - B-270 · S88 · recommendation · not applied · written against file 11 · source: results/S88 Claude's checks of the three defects/02 Derivation 2 and non-circular dependence.md — §2.8, 'Keep in either option', third bullet: 'If \(\tau\)'s role needs stating once, restore 00:176's bridge.' · placed by the line it was written against, not by its own words
    > [no wording given] restore file 00 line 176's bridge (the role of \(\tau\)), if it needs stating once
- Terms it uses (the ledger's term list): Non-circular dependence.

**L441.s4** · sentence · Part XI · The aims of a repair (line 441) · group G11 Repair, created explanation, and appraisal

> Losses outside \(P\) must be exposed.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (5: the other units of its section and the units within two either side): 1.8 substantive changes each on average (criticism-driven alone: 1.2).
- Proposals it came through (1):
  - E-16 · S94 · recommendation · declined · written against file 13 draft 5, theory text · source: tests/Revision 2 - the owner's statement on choosing, against draft 5, 25 September.md — the owner's statement file (log S94), section 9, "Not proposed", first item (reader A, finding A4), and section 10.5 (A4): the L441 rewording is dropped
    > A repair claim exposes its losses outside \(P\).
  - E-19 · S94 · recommendation · declined · written against file 13 draft 5, theory text · source: tests/working files/S94 owner statement on choosing/reader A-text.md — S94 working file, reader A, finding A4, "Proposed change": the optional L441 reading; dropped in the statement file (section 9 and 10.5)
    > A repair claim exposes its losses outside \(P\)
- Terms it uses (the ledger's term list): none on the list.

**L51.s1** · sentence · Part 0 · Grievances, anticipated / 8. "Where is aesthetics?" (line 51) · group G11 Repair, created explanation, and appraisal

> **8. "Where is aesthetics?"** In Part XI, as a declared appraisal relation.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 2 vocabulary-only changes (the ledger marks them); a change of layout only (file 10 to file 11); the ledger's vocabulary records on it: "normative relation." → "appraisal relation." (D-37, S95); "normative relation" → "appraisal relation" (D-553, S95).
- Earlier wordings:
  - file 10:
    > In Part XI, as a declared normative relation.
  - file 11 to draft 5:
    > **8. "Where is aesthetics?"** In Part XI, as a declared normative relation.
- Neighbours (4: the other units of its section and the units within two either side): 1.75 substantive changes each on average (criticism-driven alone: 1.25).
- Proposals it came through (1):
  - C-143 · S90 · recommendation · not applied · written against file 13 draft 2 · source: results/S90 Reading of the replies - batch 1 (Mimo A1, Mimo A2, Atria B1).md — S90 batch 1, Atria B1 R39 ruling, "Loose end, not ruled": revised L51 is the one place left that calls N "declared"; passed to the orchestrator; carried forward after S90 ("Revised L51") · placed by the line it was written against, not by its own words
    > [no wording given] L51 still calls the normative relation "declared"; no entry changes it
- Vocabulary proposals that passed over it (term-wide, not about this sentence alone): CH-1135 (superseded).
- Terms it uses (the ledger's term list): Appraisal, appraisal relation, declared.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - appraisal relation (import 2): "2. The **appraisal relation** \(\mathcal N\), when a question invokes an appraisal. It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance."

**L517.s1** · list item · Part XIV · Imports (lines 515–518) · group G14 The class collected

> 1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation, resources, tolerances, and \(\operatorname{Org}_\ell\), the organization a physical occurrence instantiates at a grain.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 2 vocabulary-only changes (the ledger marks them); the ledger's vocabulary records on it: "resources, accuracy grades, and" → "resources, tolerances, and" (D-210, S95); ""credit", "credits", "credited"" → ""attribution" / "attributes": "ProducedBy attributes a repair to the contributions …"; "th…" (F-42, S95).
- Earlier wording:
  - file 10 to draft 5:
    > 1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation, resources, accuracy grades, and \(\operatorname{Org}_\ell\), the organization a physical occurrence instantiates at a grain.
- Neighbours (4: the other units of its section and the units within two either side): 1.5 substantive changes each on average (criticism-driven alone: 1.5).
- Proposals it came through (1):
  - E-26 · S94 · recommendation · declined · written against file 13 draft 5, theory text · source: tests/working files/S94 owner statement on choosing/reader B-scope.md — S94 working file, reader B, finding B8, "Proposed change (optional, for a checker)": at L517, after the description of the physical module; the statement file's section 9, "Not proposed", second item · placed by the line it was written against, not by its own words
    > It is the physics adopted, and is itself conjectural: a verdict that turns on what it admits is given with it.
- Terms it uses (the ledger's term list): occurrence, physical module, Tolerances.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (O): "**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined."
  - declared indices and inputs: the same sentence as above.
  - physical module (import 1): "1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation, resources, tolerances, and \(\operatorname{Org}_\ell\), the organization a physical occurrence instantiates at a grain."

**L389.s1** · display · Part IX · Usability (lines 387–393) · group G09 Criticism, use, and usable arguments

> \[
> \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}
> \]

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 1 vocabulary-only change (the ledger marks it); the ledger's vocabulary records on it: "\operatorname{Lic}_j(u)" → "\operatorname{Form}_j(u)" (D-160, S95).
- Earlier wording:
  - file 10 to draft 5:
    > \[
    > \operatorname{Usable}_j(u)\iff\operatorname{Lic}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}
    > \]
- Neighbours (6: the other units of its section and the units within two either side): 1.33 substantive changes each on average (criticism-driven alone: 0.67).
- Proposals it came through (1):
  - C-181 · S93 · recommendation · not applied · written against file 13 draft 4, theory text · source: results/S93 reading rulings/ruling S93 X17 W7.5.md — S93 ruling X17 (W7.5), finding 1; carried forward after S93 · placed by the line it was written against, not by its own words
    > [no wording given] define (K2)'s Lic_j, Scope_j and Live_j (L390 only)
- Terms it uses (the ledger's term list): none on the list.

**L437.s1** · display · Part XI · Repair (lines 435–439) · group G11 Repair, created explanation, and appraisal

> \[
> \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}(\Delta,\xi,\xi';O). \tag{P}
> \]

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (4: the other units of its section and the units within two either side): 1.25 substantive changes each on average (criticism-driven alone: 1.25).
- Proposals it came through (1):
  - C-209 · S90 · recommendation · declined · written against file 11 · source: tests/Revision 2 - worklist, draft of 23 September.md — worklist item W48 (L962), new claim: adopt (AC) and define ProducedBy by it (12:451); decision D5 of the change list ("The decisions D1-D11") · placed by the line it was written against, not by its own words
    > [no wording given] adopt (AC) and define ProducedBy by it, as "(AC) applied to the repair as result" (12:451); defer the pre-emption episode
- Terms it uses (the ledger's term list): Repair.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (P), (EX): "(P), (EX) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared aims with their occasions, (EX) also on (P), and ProducedBy on histories and their active routes."

### 3.2 Never challenged

No proposal ever touched these units alone. That may mean no reader ever examined them; it does not mean they came through an attack.

| unit | section | since | neighbour churn | vocabulary-only changes |
| --- | --- | --- | ---: | ---: |
| L311.s2 | Infinitary routes | file 10 | 2.75 | 0 |
| L47.s2 | Grievances, anticipated / 6. "You have replaced explanation with evolution." | file 10 | 2.25 | 3 |
| L383.s1 | Bearing | file 10 | 2.17 | 0 |
| L443.s2 | Created explanation | file 10 | 2 | 2 |
| L41.s4 | Grievances, anticipated / 3. "If correspondences are selected, you have made fidelity a matter of survival." | file 10 | 1.6 | 1 |
| L273.s1 | What (E) excludes, and what it does not | file 10 | 1.54 | 0 |
| L225.s4 | Prediction, surprise, violation | file 10 | 1.5 | 0 |
| L471.s2 | Retention fixed point | file 10 | 1.5 | 0 |
| L520.s7 | What everything else is defined from | file 10 | 1.5 | 0 |
| L113.s2 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L115.s1 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L123.s1 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L124.s1 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L125.s1 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L127.s1 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L127.s2 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L127.s3 | Kinds are edit-signatures | file 10 | 1.45 | 0 |
| L161.s1 | Scope, and a question that can be in error | file 10 | 1.42 | 0 |
| L161.s2 | Scope, and a question that can be in error | file 10 | 1.42 | 0 |
| L161.s3 | Scope, and a question that can be in error | file 10 | 1.42 | 0 |
| L113.s1 | Kinds are edit-signatures | file 10 | 1.38 | 0 |
| L217.s2 | Prediction, surprise, violation | file 10 | 1.29 | 0 |
| L219.s1 | Prediction, surprise, violation | file 10 | 1.29 | 2 |
| L220.s1 | Prediction, surprise, violation | file 10 | 1.29 | 0 |
| L225.s1 | Prediction, surprise, violation | file 10 | 1.29 | 0 |
| L393.s4 | Usability | file 10 | 1.29 | 3 |
| L375.s2 | Histories | file 10 | 1.25 | 1 |
| L385.s1 | Reason use | file 10 | 1.25 | 0 |
| L27.s2 | What this document does not claim | file 10 | 1.21 | 1 |

**L311.s2** · sentence · Part VI · Infinitary routes (line 311) · group G06 Work, routes, and interference

> (B) records the collective contribution.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (4: the other units of its section and the units within two either side): 2.75 substantive changes each on average (criticism-driven alone: 1.25).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (S), (B), (D): "(S), (B), (D) depend on (E)."

**L47.s2** · sentence · Part 0 · Grievances, anticipated / 6. "You have replaced explanation with evolution." (line 47) · group G04 Layers, transports, and provenance

> Construction is a separate provenance with a separate trace, and every creative attribution requires it.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 3 vocabulary-only changes (the ledger marks them); the ledger's vocabulary records on it: "Construction is a separate provenance with a separate witness," → "Construction is a separate provenance with a separate trace," (D-31, S95); "witness (construction); witness (mathematics)" → "trace; instance" (D-523, S95); ""credit", "credits", "credited"" → ""attribution" / "attributes": "ProducedBy attributes a repair to the contributions …"; "th…" (F-42, S95).
- Earlier wording:
  - file 10 to draft 5:
    > Construction is a separate provenance with a separate witness, and every creative attribution requires it.
- Neighbours (4: the other units of its section and the units within two either side): 2.25 substantive changes each on average (criticism-driven alone: 2).
- Terms it uses (the ledger's term list): provenance.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - provenance: "Provenance, from physical history (Parts IV, XII)."

**L383.s1** · sentence · Part IX · Bearing (lines 377–383) · group G09 Criticism, use, and usable arguments

> A criticism occurrence can exist when (K1) fails.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (6: the other units of its section and the units within two either side): 2.17 substantive changes each on average (criticism-driven alone: 1).
- Terms it uses (the ledger's term list): (K1), occurrence.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K1), (K2), (K3): "(K1) depends on (E)."

**L443.s2** · sentence · Part XI · Created explanation (lines 443–451) · group G11 Repair, created explanation, and appraisal

> An explanatory aim requires an account, or the correction of a use through one, to be deployable.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 2 vocabulary-only changes (the ledger marks them); the ledger's vocabulary records on it: "epistemic obligation, O_ep" → "explanatory aim, O_ex" (D-699, S95); "**obligation**: claimed obligations O, protected obligations P, epistemic obligations" → "**aim**: claimed aims O, protected aims P, explanatory aims O_ex" (D-715, S95).
- Earlier wording:
  - file 10 to draft 5:
    > **Created explanatory knowledge.** An epistemic obligation requires a correct account, or the correction of a use through one, to be deployable.
- Neighbours (4: the other units of its section and the units within two either side): 2 substantive changes each on average (criticism-driven alone: 0.75).
- Vocabulary proposals that passed over it (term-wide, not about this sentence alone): CH-1132 (open for the owner); CH-1131 (superseded).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (E): "(E) depends on those."

**L41.s4** · sentence · Part 0 · Grievances, anticipated / 3. "If correspondences are selected, you have made fidelity a matter of survival." (line 41) · group G04 Layers, transports, and provenance

> Survival is how the transport got there; fidelity is what it is.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 1 vocabulary-only change (the ledger marks it); the ledger's vocabulary records on it: "truth (objection, l. 41)" → "fidelity" (D-536, S95); its own wording is the same in every version (the vocabulary change stands on words it shares with a record placed on it).
- Neighbours (5: the other units of its section and the units within two either side): 1.6 substantive changes each on average (criticism-driven alone: 1).
- Terms it uses (the ledger's term list): transport.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (F1), (F2), (A): "(F1), (F2), (A) depend on (O), (Q), (K)."

**L273.s1** · sentence · Part V · What (E) excludes, and what it does not (lines 267–277) · group G05 Account

> "\(p\) because \(p\)" fails non-circular dependence.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (13: the other units of its section and the units within two either side): 1.54 substantive changes each on average (criticism-driven alone: 1.15).
- Vocabulary proposals that passed over it (term-wide, not about this sentence alone): CH-1131 (superseded).
- Terms it uses (the ledger's term list): Non-circular dependence.

**L225.s4** · sentence · Part IV · Prediction, surprise, violation (lines 215–225) · group G04 Layers, transports, and provenance

> Only the second can be originative under Part X.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (16: the other units of its section and the units within two either side): 1.5 substantive changes each on average (criticism-driven alone: 0.62).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (N), (G): "(N), (G) depend on Deploy and Build."

**L471.s2** · sentence · Part XII · Retention fixed point (line 471) · group G12 The physical module

> \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (4: the other units of its section and the units within two either side): 1.5 substantive changes each on average (criticism-driven alone: 1.25).
- Terms it uses (the ledger's term list): (CT2).

**L520.s7** · sentence · Part XIV · What everything else is defined from (line 520) · group G14 The class collected

> Account, from fidelity under change (E).

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (8: the other units of its section and the units within two either side): 1.5 substantive changes each on average (criticism-driven alone: 1.25).
- Vocabulary proposals that passed over it (term-wide, not about this sentence alone): CH-1127 (superseded).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (F1), (F2), (A): "(F1), (F2), (A) depend on (O), (Q), (K)."
  - (E): "(E) depends on those."

**L113.s2** · sentence · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> The **signature** of component \(j\) on \(C\) is

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): signature.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K): "(K) depends on (O) and a contract."

**L115.s1** · display · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> \[
> \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}
> \]

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): none on the list.

**L123.s1** · list item · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> - a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): causal assignment, observation, output, signature.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K): "(K) depends on (O) and a contract."

**L124.s1** · list item · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): measurement, signature.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K): "(K) depends on (O) and a contract."

**L125.s1** · list item · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): rule application, signature.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K): "(K) depends on (O) and a contract."

**L127.s1** · sentence · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> These are descriptions of patterns in (K), not additional data.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K): "(K) depends on (O) and a contract."

**L127.s2** · sentence · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> The semantics never asks whether a component "is" a cause.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): none on the list.

**L127.s3** · sentence · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> It asks what its signature is.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (20: the other units of its section and the units within two either side): 1.45 substantive changes each on average (criticism-driven alone: 0.8).
- Terms it uses (the ledger's term list): signature.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (K): "(K) depends on (O) and a contract."

**L161.s1** · sentence · Part III · Scope, and a question that can be in error (lines 157–161) · group G03 Questions

> A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (12: the other units of its section and the units within two either side): 1.42 substantive changes each on average (criticism-driven alone: 0.92).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (Q): "**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined."

**L161.s2** · sentence · Part III · Scope, and a question that can be in error (lines 157–161) · group G03 Questions

> Its formulation is still an event.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (12: the other units of its section and the units within two either side): 1.42 substantive changes each on average (criticism-driven alone: 0.92).
- Terms it uses (the ledger's term list): none on the list.

**L161.s3** · sentence · Part III · Scope, and a question that can be in error (lines 157–161) · group G03 Questions

> Exposing the defect is another question with its own contract.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (12: the other units of its section and the units within two either side): 1.42 substantive changes each on average (criticism-driven alone: 0.92).
- Terms it uses (the ledger's term list): contract.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (Q): "**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined."
  - declared indices and inputs: the same sentence as above.

**L113.s1** · sentence · Part II · Kinds are edit-signatures (lines 111–127) · group G02 Organizations and their changes

> Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (21: the other units of its section and the units within two either side): 1.38 substantive changes each on average (criticism-driven alone: 0.76).
- Terms it uses (the ledger's term list): contract.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (O): "**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined."
  - declared indices and inputs: the same sentence as above.

**L217.s2** · sentence · Part IV · Prediction, surprise, violation (lines 215–225) · group G04 Layers, transports, and provenance

> For an edit–boundary pair \((a,b)\in C\) actually occurring:

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (14: the other units of its section and the units within two either side): 1.29 substantive changes each on average (criticism-driven alone: 0.64).
- Terms it uses (the ledger's term list): none on the list.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - declared indices and inputs: "**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined."

**L219.s1** · list item · Part IV · Prediction, surprise, violation (lines 215–225) · group G04 Layers, transports, and provenance

> - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 2 vocabulary-only changes (the ledger marks them); the ledger's vocabulary records on it: "the **expectation** is" → "the **prediction** is" (D-82, S95); "expectation, expects, expected" → "prediction, predicts, usual" (D-551, S95).
- Earlier wording:
  - file 10 to draft 5:
    > - the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- Neighbours (14: the other units of its section and the units within two either side): 1.29 substantive changes each on average (criticism-driven alone: 0.64).
- Vocabulary proposals that passed over it (term-wide, not about this sentence alone): CH-0508 (declined).
- Terms it uses (the ledger's term list): prediction.

**L220.s1** · list item · Part IV · Prediction, surprise, violation (lines 215–225) · group G04 Layers, transports, and provenance

> - a **violation** occurs when fidelity fails at \((a,b)\);

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (14: the other units of its section and the units within two either side): 1.29 substantive changes each on average (criticism-driven alone: 0.64).
- Terms it uses (the ledger's term list): violation.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (F1), (F2), (A): "(F1), (F2), (A) depend on (O), (Q), (K)."

**L225.s1** · sentence · Part IV · Prediction, surprise, violation (lines 215–225) · group G04 Layers, transports, and provenance

> Two responses to a violation are distinguished.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (14: the other units of its section and the units within two either side): 1.29 substantive changes each on average (criticism-driven alone: 0.64).
- Terms it uses (the ledger's term list): violation.

**L393.s4** · sentence · Part IX · Usability (lines 387–393) · group G09 Criticism, use, and usable arguments

> Withdrawing a premise makes the step unusable; it does not rule the conclusion out.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 3 vocabulary-only changes (the ledger marks them); the ledger's vocabulary records on it: "Lic_j(u), license" → "Form_j(u): the inference form of u is one j admits [Claude's reading, marked in the text]" (D-512, S95); "Lic_j(u), license" → ""Form_j(u): u's inference form is one j admits." Keep "makes the step unusable". Mark as C…" (D-577, S95); ""it does not make the conclusion false" (l. 393)" → ""it does not rule the conclusion out"" (D-686, S95).
- Earlier wording:
  - file 10 to draft 5:
    > Withdrawing a premise removes a license; it does not make the conclusion false.
- Neighbours (7: the other units of its section and the units within two either side): 1.29 substantive changes each on average (criticism-driven alone: 0.71).
- Terms it uses (the ledger's term list): none on the list.

**L375.s2** · sentence · Part IX · Histories (line 375) · group G09 Criticism, use, and usable arguments

> An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 1 vocabulary-only change (the ledger marks it); the ledger's vocabulary records on it: "satisfy" → "meet" (D-155, S95).
- Earlier wording:
  - file 10 to draft 5:
    > An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components satisfy the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.
- Neighbours (4: the other units of its section and the units within two either side): 1.25 substantive changes each on average (criticism-driven alone: 0.75).
- Terms it uses (the ledger's term list): active route, declared, input, occurrence, route.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (R): "(R) depends on (F1)–(F2) and physical provenance."

**L385.s1** · sentence · Part IX · Reason use (line 385) · group G09 Criticism, use, and usable arguments

> **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Changes: none of any kind; the same wording in every version.
- Neighbours (4: the other units of its section and the units within two either side): 1.25 substantive changes each on average (criticism-driven alone: 0.75).
- Terms it uses (the ledger's term list): active route, content, Reason use, Recoding, route.
- What the dependence order of the latest text (Part XIV) says of what it names:
  - (O): "**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined."
  - (R): "(R) depends on (F1)–(F2) and physical provenance."
  - roles: "Roles, from admitted edits (Part II)."

**L27.s2** · sentence · Part 0 · What this document does not claim (lines 19–27) · group G01 The document as a whole

> It defines the classes.

- In the text since file 10: 10 of 10 versions; came through 22 of the 22 rounds of edits and proposals.
- Allowed changes: 1 vocabulary-only change (the ledger marks it); the ledger's vocabulary records on it: ""It does not prove that any human, machine, institution or lineage belongs to the classes …" → ""It does not decide whether any human, machine, institution or lineage belongs to the clas…" (D-660, S95); its own wording is the same in every version (the vocabulary change stands on words it shares with a record placed on it).
- Neighbours (14: the other units of its section and the units within two either side): 1.21 substantive changes each on average (criticism-driven alone: 1).
- Terms it uses (the ledger's term list): none on the list.

### 3.3 Near the age cut: untouched since file 11 or draft 1

These pass every test but have stood in eight or nine versions, not ten.

| unit | section | since | versions | neighbour churn | list it would join |
| --- | --- | --- | ---: | ---: | --- |
| L534.s3 | Opening of the Part | draft 1 | 8 | 4.2 | never challenged |
| L441.s3 | The aims of a repair | file 11 | 9 | 1.8 | challenged and kept |
| L427.s3 | Ownership | draft 1 | 8 | 1.75 | never challenged |
| L441.s2 | The aims of a repair | draft 1 | 8 | 1.5 | challenged and kept |

- **L534.s3**:
  > A case whose assessment turns on an input the case does not state, where the input is one of the declared inputs Part XIV lists or the appraisal relation, is a case with a missing input, not an argument that rules a claim out.
- **L441.s3**:
  > Their declaration makes no appraisal of the aims, and (P) puts no order on alternatives.
- **L427.s3**:
  > Contribution of content and ownership of a process are different attributions: a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution.
- **L441.s2**:
  > In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).

### 3.4 Left out: changed in the texts with no record on them

These have no substantive change in the ledger, but their text changed between versions in a way the ledger places on another sentence or does not hold. They are not candidates.

- **L479.s3** (file 11 to draft 1):
  - file 10 to file 11:
    > **Grades.** \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\); \(\mathsf{Cap}^\infty=\bigcap_{q,r}\mathsf{Cap}^{q,r}\subseteq\mathsf{Poss}_\Theta\).
  - draft 1 to latest text:
    > Then \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\); \(\mathsf{Cap}^\infty=\bigcap_{q,r}\mathsf{Cap}^{q,r}\subseteq\mathsf{Poss}_\Theta\).
- **L520.s8** (file 10 to file 11):
  - file 10:
    > Understanding, construction, newness, origin, repair, knowledge, capability, recursion, universality — from those.
  - file 11 to draft 5:
    > Understanding, construction, newness, origin, repair, knowledge, capability, recursion, universality, from those.
  - scrubbed copy to latest text:
    > Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.
- **L526.s11** (file 11 to draft 1):
  - file 10 to file 11:
    > Build depends on histories and (E).
  - draft 1 to latest text:
    > Build depends on histories, Ownership and (E).
- **L562.s1** (draft 1 to draft 2):
  - file 10 to draft 1:
    > **Claim.** Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2), and (A) on \(C\) are one account at grain \(C\): their components are pairwise of one kind on \(C\) and their answer profiles coincide.
  - draft 2 to draft 5:
    > **Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\).
  - scrubbed copy to latest text:
    > **Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both meet (F1), (F2) and (A) on \(C\).

## 4. The most altered

Per section (the ledger's 134, less the dated note), distinct changes over its units and the records in its not-in-the-latest-text block (removed sentences, proposals never applied). Per unit = divided by the number of units in the section (headings included, as the ledger counts them). Sections of one or two units swing most; the counts are given beside the rates.

Columns: **crit** criticism-driven changes; **owner** owner-directed; **vocab** vocabulary only; **repl** replaced wordings (of them from owner-directed passes); **decl** proposals declined; **n.a.** not applied; **open** open for the owner; **block** records with no sentence in the latest text.

### 4.1 Sections, most criticism-driven changes per unit first (the first 20)

| # | section | group | units | crit per unit | total per unit | crit | owner | vocab | repl (owner) | decl | n.a. | open | block | owner-directed share of churn |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Part XV · (Prov) Genesis (line 542) | G15 | 1 | 6 | 21 | 6 | 0 | 15 | 0 (0) | 2 | 0 | 0 | 0 | 0% |
| 2 | Part XV · (QF) Question-finding (line 544) | G15 | 1 | 4 | 12 | 4 | 0 | 6 | 2 (0) | 4 | 1 | 0 | 0 | 0% |
| 3 | Part XV · (Nec) Necessity (line 538) | G15 | 2 | 4 | 6.5 | 8 | 2 | 1 | 2 (0) | 3 | 0 | 0 | 0 | 15% |
| 4 | Part XV · (Elim) Reinstatement of kinds (line 540) | G15 | 2 | 4 | 6.5 | 8 | 0 | 4 | 1 (0) | 3 | 0 | 0 | 0 | 0% |
| 5 | Part XV · (Suff) Sufficiency (line 536) | G15 | 3 | 4 | 6 | 12 | 1 | 3 | 2 (0) | 6 | 0 | 0 | 0 | 6% |
| 6 | Part XIV · Declared inputs (line 522) | G14 | 3 | 2 | 8.33 | 6 | 1 | 12 | 6 (0) | 0 | 4 | 0 | 0 | 4% |
| 7 | Part 0 · Grievances, anticipated / introduction (lines 33–35) | G01 | 2 | 2 | 8 | 4 | 0 | 0 | 12 (0) | 0 | 0 | 0 | 15 | 0% |
| 8 | Part 0 · What is imported, what is an index, and what is defined (lines 29–31) | G14 | 5 | 1.8 | 5.6 | 9 | 1 | 11 | 7 (0) | 4 | 1 | 1 | 0 | 4% |
| 9 | Part X · Ownership (line 427) | G10 | 4 | 1.75 | 3.25 | 7 | 0 | 5 | 1 (0) | 0 | 0 | 0 | 2 | 0% |
| 10 | Part 0 · Grievances, anticipated / 6. "You have replaced explanation with evolution." (line 47) | G04 | 3 | 1.67 | 5.33 | 5 | 0 | 10 | 1 (0) | 0 | 0 | 0 | 0 | 0% |
| 11 | Part XI · Appraisal (line 455) | G11 | 5 | 1.6 | 4 | 8 | 1 | 8 | 3 (0) | 2 | 1 | 1 | 0 | 5% |
| 12 | Part 0 · Where to attack this (lines 59–61) | G15 | 4 | 1.5 | 3.25 | 6 | 0 | 6 | 1 (0) | 3 | 0 | 0 | 2 | 0% |
| 13 | Part VIII · Recoding (line 365) | G08 | 2 | 1.5 | 2.5 | 3 | 0 | 1 | 1 (0) | 0 | 0 | 0 | 1 | 0% |
| 14 | Part 0 · Grievances, anticipated / 8. "Where is aesthetics?" (line 51) | G11 | 3 | 1.33 | 3.67 | 4 | 1 | 5 | 1 (0) | 0 | 1 | 0 | 0 | 9% |
| 15 | Part 0 · Grievances, anticipated / 9. "'Selected' is as much a stipulation as 'is a cause'." (line 53) | G04 | 3 | 1.33 | 2 | 4 | 0 | 1 | 1 (0) | 0 | 0 | 0 | 0 | 0% |
| 16 | Part XV · Opening of the Part (lines 532–534) | G15 | 4 | 1.25 | 3.5 | 5 | 0 | 8 | 1 (0) | 0 | 0 | 0 | 0 | 0% |
| 17 | Part XII · System boundary and continuity (line 473) | G12 | 4 | 1.25 | 1.75 | 5 | 0 | 1 | 1 (0) | 0 | 0 | 0 | 0 | 0% |
| 18 | Part 0 · Grievances, anticipated / 7. "Mathematics has no interventions." (line 49) | G07 | 5 | 1.2 | 2.6 | 6 | 0 | 5 | 2 (1) | 0 | 0 | 0 | 0 | 8% |
| 19 | Part V · What (E) excludes, and what it does not (lines 267–277) | G05 | 14 | 1.07 | 2.64 | 15 | 2 | 14 | 6 (1) | 4 | 1 | 0 | 2 | 8% |
| 20 | Part XIV · Imports (lines 515–518) | G14 | 3 | 1 | 4.33 | 3 | 0 | 8 | 2 (0) | 1 | 0 | 0 | 0 | 0% |

### 4.2 Sections, most total churn per unit first (the first 20)

| # | section | group | units | crit per unit | total per unit | crit | owner | vocab | repl (owner) | decl | n.a. | open | block | owner-directed share of churn |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Part XV · (Prov) Genesis (line 542) | G15 | 1 | 6 | 21 | 6 | 0 | 15 | 0 (0) | 2 | 0 | 0 | 0 | 0% |
| 2 | Part XV · (QF) Question-finding (line 544) | G15 | 1 | 4 | 12 | 4 | 0 | 6 | 2 (0) | 4 | 1 | 0 | 0 | 0% |
| 3 | Part XIV · Declared inputs (line 522) | G14 | 3 | 2 | 8.33 | 6 | 1 | 12 | 6 (0) | 0 | 4 | 0 | 0 | 4% |
| 4 | Part 0 · Grievances, anticipated / introduction (lines 33–35) | G01 | 2 | 2 | 8 | 4 | 0 | 0 | 12 (0) | 0 | 0 | 0 | 15 | 0% |
| 5 | Part IX · What a test rules out (line 395) | G09 | 1 | 0 | 8 | 0 | 1 | 5 | 2 (0) | 1 | 0 | 0 | 0 | 12% |
| 6 | Part XV · (Nec) Necessity (line 538) | G15 | 2 | 4 | 6.5 | 8 | 2 | 1 | 2 (0) | 3 | 0 | 0 | 0 | 15% |
| 7 | Part XV · (Elim) Reinstatement of kinds (line 540) | G15 | 2 | 4 | 6.5 | 8 | 0 | 4 | 1 (0) | 3 | 0 | 0 | 0 | 0% |
| 8 | Part XV · (Suff) Sufficiency (line 536) | G15 | 3 | 4 | 6 | 12 | 1 | 3 | 2 (0) | 6 | 0 | 0 | 0 | 6% |
| 9 | Part 0 · What is imported, what is an index, and what is defined (lines 29–31) | G14 | 5 | 1.8 | 5.6 | 9 | 1 | 11 | 7 (0) | 4 | 1 | 1 | 0 | 4% |
| 10 | Part 0 · Grievances, anticipated / 6. "You have replaced explanation with evolution." (line 47) | G04 | 3 | 1.67 | 5.33 | 5 | 0 | 10 | 1 (0) | 0 | 0 | 0 | 0 | 0% |
| 11 | Part VI · Commitments that do no work (line 313) | G06 | 3 | 0.67 | 5 | 2 | 0 | 4 | 9 (0) | 5 | 0 | 0 | 0 | 0% |
| 12 | Part I · Faithfulness without assessors (line 67) | G05 | 2 | 0.5 | 5 | 1 | 0 | 9 | 0 (0) | 0 | 0 | 0 | 0 | 0% |
| 13 | Part XV · A mathematical error (line 546) | G15 | 1 | 0 | 5 | 0 | 0 | 5 | 0 (0) | 1 | 0 | 0 | 0 | 0% |
| 14 | Part XIV · Imports (lines 515–518) | G14 | 3 | 1 | 4.33 | 3 | 0 | 8 | 2 (0) | 1 | 0 | 0 | 0 | 0% |
| 15 | Part XI · Appraisal (line 455) | G11 | 5 | 1.6 | 4 | 8 | 1 | 8 | 3 (0) | 2 | 1 | 1 | 0 | 5% |
| 16 | Part III · The respect is the query (lines 149–151) | G03 | 8 | 0.62 | 3.88 | 5 | 0 | 3 | 23 (0) | 1 | 0 | 0 | 21 | 0% |
| 17 | Part XI · The aims of a repair (line 441) | G11 | 6 | 1 | 3.83 | 6 | 0 | 12 | 5 (0) | 3 | 0 | 0 | 0 | 0% |
| 18 | Part 0 · Grievances, anticipated / 8. "Where is aesthetics?" (line 51) | G11 | 3 | 1.33 | 3.67 | 4 | 1 | 5 | 1 (0) | 0 | 1 | 0 | 0 | 9% |
| 19 | Part XV · Opening of the Part (lines 532–534) | G15 | 4 | 1.25 | 3.5 | 5 | 0 | 8 | 1 (0) | 0 | 0 | 0 | 0 | 0% |
| 20 | Part VI · Infinitary routes (line 311) | G06 | 2 | 1 | 3.5 | 2 | 0 | 4 | 1 (0) | 0 | 0 | 0 | 0 | 0% |

### 4.3 Sections of five units or more, most criticism-driven changes per unit first (the first 10)

| # | section | group | units | crit per unit | total per unit | crit | owner | vocab | repl (owner) | decl | n.a. | open | block | owner-directed share of churn |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Part 0 · What is imported, what is an index, and what is defined (lines 29–31) | G14 | 5 | 1.8 | 5.6 | 9 | 1 | 11 | 7 (0) | 4 | 1 | 1 | 0 | 4% |
| 2 | Part XI · Appraisal (line 455) | G11 | 5 | 1.6 | 4 | 8 | 1 | 8 | 3 (0) | 2 | 1 | 1 | 0 | 5% |
| 3 | Part 0 · Grievances, anticipated / 7. "Mathematics has no interventions." (line 49) | G07 | 5 | 1.2 | 2.6 | 6 | 0 | 5 | 2 (1) | 0 | 0 | 0 | 0 | 8% |
| 4 | Part V · What (E) excludes, and what it does not (lines 267–277) | G05 | 14 | 1.07 | 2.64 | 15 | 2 | 14 | 6 (1) | 4 | 1 | 0 | 2 | 8% |
| 5 | Part XI · The aims of a repair (line 441) | G11 | 6 | 1 | 3.83 | 6 | 0 | 12 | 5 (0) | 3 | 0 | 0 | 0 | 0% |
| 6 | Part XVI · 6. There are two imports (lines 594–600) | G14 | 7 | 1 | 2.71 | 7 | 0 | 11 | 1 (0) | 0 | 3 | 1 | 1 | 0% |
| 7 | Part VI · Redundant routes (line 307) | G06 | 5 | 0.8 | 2.8 | 4 | 0 | 8 | 2 (0) | 0 | 1 | 0 | 2 | 0% |
| 8 | Part X · Construction (line 405) | G10 | 5 | 0.8 | 2.6 | 4 | 0 | 4 | 5 (0) | 1 | 1 | 0 | 0 | 0% |
| 9 | Part 0 · What this document does not claim (lines 19–27) | G01 | 13 | 0.77 | 2.23 | 10 | 1 | 14 | 4 (0) | 0 | 2 | 0 | 1 | 3% |
| 10 | Part III · Scope, and a question that can be in error (lines 157–161) | G03 | 13 | 0.77 | 2 | 10 | 2 | 8 | 6 (1) | 1 | 3 | 0 | 2 | 12% |

### 4.4 Units, most substantive changes first (the first 15)

| # | unit | section | since | crit | owner | vocab | repl (owner) | decl | open | substantive | total |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | L536.s1 | (Suff) Sufficiency | file 10 | 7 | 1 | 3 | 2 (0) | 4 | 0 | 10 | 13 |
| 2 | L536.s3 | (Suff) Sufficiency | file 11 | 7 | 0 | 0 | 1 (0) | 1 | 0 | 8 | 8 |
| 3 | L522.s1 | Declared inputs | file 11 | 5 | 0 | 8 | 3 (0) | 0 | 0 | 7 | 16 |
| 4 | L538.s1 | (Nec) Necessity | file 10 | 4 | 2 | 1 | 2 (0) | 2 | 0 | 7 | 9 |
| 5 | L542.s1 | (Prov) Genesis | file 11 | 6 | 0 | 15 | 0 (0) | 2 | 0 | 6 | 21 |
| 6 | L538.s2 | (Nec) Necessity | file 10 | 6 | 0 | 1 | 1 (0) | 1 | 0 | 6 | 8 |
| 7 | L540.s2 | (Elim) Reinstatement of kinds | file 10 | 5 | 0 | 4 | 1 (0) | 1 | 0 | 6 | 10 |
| 8 | L536.s2 | (Suff) Sufficiency | file 11 | 5 | 0 | 0 | 1 (0) | 3 | 0 | 6 | 6 |
| 9 | L119.s3 | Kinds are edit-signatures | draft 3 | 3 | 0 | 3 | 3 (0) | 3 | 0 | 6 | 9 |
| 10 | L405.s5 | Construction | file 11 | 3 | 0 | 0 | 3 (0) | 1 | 0 | 6 | 6 |
| 11 | L119.s2 | Kinds are edit-signatures | file 10 | 2 | 0 | 0 | 4 (0) | 1 | 0 | 6 | 6 |
| 12 | L313.s2 | Commitments that do no work | draft 1 | 1 | 0 | 3 | 6 (0) | 3 | 0 | 6 | 10 |
| 13 | L231.s1 | Opening of the Part | file 10 | 1 | 0 | 0 | 5 (0) | 1 | 0 | 6 | 6 |
| 14 | L526.s18 | Dependence order | file 11 | 4 | 0 | 6 | 3 (0) | 0 | 0 | 5 | 13 |
| 15 | L299.s2 | Opening of the Part | file 11 | 4 | 0 | 2 | 2 (0) | 1 | 0 | 5 | 8 |

### 4.5 The ten sections with the most criticism-driven changes per unit: pattern and wordings

Each section: its counts, the share of its churn from owner-directed passes, a pattern line per unit found by program (words per wording; longer or shorter; wordings that came back; words swapped; phrases added and taken out; splits), and the run of wordings the unit held, oldest first. A run lists the unit's text in each version where it differs from the version before, with the S96 stage-1 wordings (never kept as a file) in their place. Units with a single wording are named only.

#### 1. Part XV · (Prov) Genesis (line 542)

Group G15 What would rule this class out · 1 unit · criticism-driven 6, owner-directed 0, vocabulary-only 15, replaced wordings 0 (0 from owner-directed passes), declined 2, open 0 · owner-directed share of churn 0%.

**Pattern, in plain words:** One sentence, in the text since file 11, four wordings of about 90 words each. The scrub swapped eight words or phrases in it at once ("Derivation" to "Argument", "theorem" to "claim", "a demonstration" and "a showing" to "an argument", "witness" to "trace", "primitive layer" to "object layer"). The repaired copy then rewrote the second and third of its three clauses, taking out one "an argument" the scrub had put in ("an argument that every construction trace can be rewritten" became "a method that rewrites every construction trace"); the latest text renamed its label, "(D)" to "(Prov)". Length stayed flat.

- **L542.s1** (sentence; crit 6, owner 0, vocab 15, replaced 0): 4 wordings, 88 → 92 → 90 → 90 words; words swapped: "Derivation" → "Argument" (scrubbed copy); "theorem's" → "claim's" (scrubbed copy); "a demonstration" → "an argument" (scrubbed copy); "witness" → "trace" (scrubbed copy); "a showing" → "an argument" (scrubbed copy); "primitive" → "object" (scrubbed copy) and 2 more; "an argument" added (scrubbed copy) and taken out again (repaired copy).
  - file 11 to draft 5:
    > **(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation); a demonstration that every construction witness can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or a showing that the primitive layer of Part IV is not what explanation operates on.
  - scrubbed copy:
    > **(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); an argument that every construction trace can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that the object layer of Part IV is not what explanation operates on.
  - repaired copy:
    > **(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV.
  - latest text:
    > **(Prov) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV.

#### 2. Part XV · (QF) Question-finding (line 544)

Group G15 What would rule this class out · 1 unit · criticism-driven 4, owner-directed 0, vocabulary-only 6, replaced wordings 2 (0 from owner-directed passes), declined 4, open 0 · owner-directed share of churn 0%.

**Pattern, in plain words:** One sentence since file 10, five wordings. Its opening changed at nearly every step: an instruction ("Show that ...") became a noun ("A showing that ..."), then "An argument that ...", then, in the repaired copy, two cases ("A case of finding a new question that ... fails to capture; or an episode that is not creative which that treatment counts as creative"). "Genuine" and "the right question" went out in the scrubbed copy ("a new question"). The label was renamed, "(E)" to "(QF)".

- **L544.s1** (sentence; crit 4, owner 0, vocab 6, replaced 2): 5 wordings, 42 → 44 → 43 → 50 → 50 words; words swapped: "Show" → "A showing" (file 11 to draft 5); "A showing" → "An argument" (scrubbed copy); "the right" → "a new" (scrubbed copy); "Derivation" → "Argument" (scrubbed copy); "A showing" added (file 11 to draft 5) and taken out again (scrubbed copy); "An argument" added (scrubbed copy) and taken out again (repaired copy).
  - file 10:
    > **(E) Question-finding.** Show that treating a contract as a content — something that can be constructed, be new, and be the originative contribution of an episode — either trivializes creativity or fails to capture some genuine case of finding the right question.
  - file 11 to draft 5:
    > **(E) Question-finding.** A showing that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, either trivializes creativity or fails to capture some genuine case of finding the right question (against Derivation 5).
  - scrubbed copy:
    > **(E) Question-finding.** An argument that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, either trivializes creativity or fails to capture some case of finding a new question (against Argument 5).
  - repaired copy:
    > **(E) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5).
  - latest text:
    > **(QF) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5).

#### 3. Part XV · (Nec) Necessity (line 538)

Group G15 What would rule this class out · 2 units · criticism-driven 8, owner-directed 2, vocabulary-only 1, replaced wordings 2 (0 from owner-directed passes), declined 3, open 0 · owner-directed share of churn 15%.

**Pattern, in plain words:** The first sentence has five wordings and three labels ("An explanation without a faithful transport", then "(B) Necessity", then "(Nec) Necessity"). What would count moved from "A genuine explanation" (file 10 to draft 5) to "An explanation, argued to be one and not a non-explanation by an argument that does not use (E)" (scrubbed copy), to "A candidate that an argument not using (E) rules out as a non-explanation" (repaired copy), to "A candidate such that an argument not using (E) rules out the claim that it is a non-explanation" (latest text). "Under any physically admitted contract" became "under any contract on its target" in an owner-directed pass. The second sentence kept one wording.

- **L538.s1** (sentence; crit 4, owner 2, vocab 1, replaced 2): 5 wordings, 20 → 16 → 31 → 27 → 32 words; grew longer overall; words swapped: "A genuine" → "An" (scrubbed copy); "use" → "using" (repaired copy).
  - file 10:
    > **An explanation without a faithful transport.** A genuine explanation whose organization no transport can preserve under any physically admitted contract.
  - file 11 to draft 5:
    > **(B) Necessity.** A genuine explanation whose organization no transport can preserve under any physically admitted contract.
  - scrubbed copy:
    > **(B) Necessity.** An explanation, argued to be one and not a non-explanation by an argument that does not use (E), whose organization no transport can preserve under any physically admitted contract.
  - repaired copy:
    > **(B) Necessity.** A candidate that an argument not using (E) rules out as a non-explanation, whose organization no transport can preserve under any contract on its target.
  - latest text:
    > **(Nec) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, whose organization no transport can preserve under any contract on its target.
- One wording throughout: L538.s2.

#### 4. Part XV · (Elim) Reinstatement of kinds (line 540)

Group G15 What would rule this class out · 2 units · criticism-driven 8, owner-directed 0, vocabulary-only 4, replaced wordings 1 (0 from owner-directed passes), declined 3, open 0 · owner-directed share of churn 0%.

**Pattern, in plain words:** The first sentence changed once, in file 11 (the instruction "Produce a case in which ..." became "A case where ..."), and then only its label ("(C)" to "(Elim)"). The second grew from 9 to 26 words over five wordings, each naming what the case would rule out a little differently: "This refutes Derivation 1", "Such a case would rule out Argument 1", "... the Claim of Argument 1", "An argument that exhibits such a case would rule out the Claim of Argument 1, for whoever can use it", "... the Consequence of Argument 1".

- **L540.s1** (sentence; crit 4, owner 0, vocab 0, replaced 0): 3 wordings, 21 → 23 → 23 words; words swapped: "Produce" → "A case where" (file 11 to repaired copy); "does discriminating work" → "distinguishes two accounts" (file 11 to repaired copy); "C" → "Elim" (latest text).
  - file 10:
    > **(C) Reinstatement of kinds.** Produce a case in which a declared kind-label does discriminating work that no admitted change can do.
  - file 11 to repaired copy:
    > **(C) Reinstatement of kinds.** A case where a kind-label distinguishes two accounts that no admitted change distinguishes, and the distinction does explanatory work.
  - latest text:
    > **(Elim) Reinstatement of kinds.** A case where a kind-label distinguishes two accounts that no admitted change distinguishes, and the distinction does explanatory work.
- **L540.s2** (sentence; crit 5, owner 0, vocab 4, replaced 1): 5 wordings, 9 → 14 → 17 → 26 → 26 words; grew longer overall; words swapped: "reinstates" → "make" (scrubbed copy); "as primitive" → "an import again" (scrubbed copy); "Claim" → "Consequence" (latest text).
  - file 10 to draft 5:
    > This refutes Derivation 1 and reinstates correspondence as primitive.
  - scrubbed copy:
    > Such a case would rule out Argument 1 and make correspondence an import again.
  - the S96 stage-1 text (not kept):
    > Such a case would rule out the Claim of Argument 1 and make correspondence an import again.
  - repaired copy:
    > An argument that exhibits such a case would rule out the Claim of Argument 1, for whoever can use it, and make correspondence an import again.
  - latest text:
    > An argument that exhibits such a case would rule out the Consequence of Argument 1, for whoever can use it, and make correspondence an import again.

#### 5. Part XV · (Suff) Sufficiency (line 536)

Group G15 What would rule this class out · 3 units · criticism-driven 12, owner-directed 1, vocabulary-only 3, replaced wordings 2 (0 from owner-directed passes), declined 6, open 0 · owner-directed share of churn 6%.

**Pattern, in plain words:** The first sentence has five wordings, and its ending went back and forth: "plainly explains nothing" (file 10), "plainly provides no account" (file 11 to draft 5), "nonetheless explains nothing" (scrubbed copy: the words of file 10 came back), "an argument not using (E) rules out as an explanation of what its question asks" (repaired copy), "an argument not using (E) rules out the claim that it is an explanation of what its question asks" (latest text). "On a physically admitted contract" became "on a contract of its question" (owner-directed), and "a non-declared transport" became "a transport whose provenance is not declared (Part IV)"; it went from 28 words in file 10 to 47. The third sentence, new in file 11, grew at every change and took the same new ending. The second sentence has kept one wording since file 11, when it took the place of an earlier sentence.

- **L536.s1** (sentence; crit 7, owner 1, vocab 3, replaced 2): 5 wordings, 28 → 24 → 23 → 36 → 47 words; grew longer overall; words swapped: "Produce a" → "A" (file 11 to draft 5); "that satisfies" → "meeting" (file 11 to draft 5); "Part V" → "E" (file 11 to draft 5); "explains nothing" → "provides no account" (file 11 to draft 5); "A" → "Suff" (latest text); "provides no account" added (file 11 to draft 5) and taken out again (scrubbed copy); "nonetheless explains nothing" added (scrubbed copy) and taken out again (repaired copy); "explains nothing" taken out (file 11 to draft 5) and put back (scrubbed copy).
  - file 10:
    > **(A) Sufficiency.** Produce a candidate that satisfies all four conditions of Account (Part V) on a physically admitted contract, with a non-declared transport, and that plainly explains nothing.
  - file 11 to draft 5:
    > **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that plainly provides no account.
  - scrubbed copy:
    > **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that nonetheless explains nothing.
  - repaired copy:
    > **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks.
  - latest text:
    > **(Suff) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.
- **L536.s3** (sentence; crit 7, owner 0, vocab 0, replaced 1): 4 wordings, 32 → 34 → 40 → 43 words; grew longer at every change; words swapped: "explain" → "explains" (draft 1 to scrubbed copy).
  - file 11:
    > A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing.
  - draft 1 to scrubbed copy:
    > A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and still explains nothing.
  - repaired copy:
    > A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and such an argument rules it out as an explanation.
  - latest text:
    > A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and such an argument rules out the claim that it is an explanation.
- One wording throughout: L536.s2.

#### 6. Part XIV · Declared inputs (line 522)

Group G14 The class collected · 3 units · criticism-driven 6, owner-directed 1, vocabulary-only 12, replaced wordings 6 (0 from owner-directed passes), declined 0, open 0 · owner-directed share of churn 4%.

**Pattern, in plain words:** All three sentences grew at every change. The list of declared inputs gained an item in draft 1 (a weighting of credit among contributions) and another in the repaired copy (an assessor's inference forms, scope and premises), and the words "tentatively accepts" joined that item in the repaired copy; the first sentence went from 57 to 111 words. The scrub swapped "primitives", "obligations", "verdict", "unsettled", "normative relation" and "worth" across the three.

- **L522.s1** (sentence; crit 5, owner 0, vocab 8, replaced 3): 5 wordings, 57 → 77 → 85 → 108 → 111 words; grew longer at every change; words swapped: "primitives" → "imports" (scrubbed copy); "obligations" → "aims" (scrubbed copy); "restriction appropriate" → "wider one" (scrubbed copy); "credit" → "attribution" (scrubbed copy).
  - file 11:
    > **Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII).
  - draft 1 to draft 5:
    > **Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII); a weighting of credit among several contributions to one achievement, beyond any division of credit its history contains (Part XI).
  - scrubbed copy:
    > **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
  - the S96 stage-1 text (not kept):
    > **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
  - repaired copy to latest text:
    > **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
- **L522.s2** (sentence; crit 1, owner 1, vocab 3, replaced 3): 3 wordings, 37 → 47 → 49 words; grew longer at every change; words swapped: "A verdict" → "An assessment" (scrubbed copy to latest text); "normative" → "appraisal" (scrubbed copy to latest text); "worth" → "an appraisal" (scrubbed copy to latest text); "a verdict" → "an assessment" (scrubbed copy to latest text); "verdict" → "assessment" (scrubbed copy to latest text); "unsettled" → "left open" (scrubbed copy to latest text) and 1 more.
  - file 11:
    > A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.
  - draft 1 to draft 5:
    > A verdict that depends on one of these, or on the normative relation where a claim invokes worth, is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.
  - scrubbed copy to latest text:
    > An assessment that depends on one of these, or on the appraisal relation where a claim invokes an appraisal, is an assessment given the input; where the input is missing, the assessment is left open and the semantics says so rather than choosing the input from the assessment wanted.
- **L522.s3** (sentence; crit 0, owner 1, vocab 2, replaced 2): 2 wordings, 23 → 24 words; words swapped: "unsettled" → "left open" (scrubbed copy to latest text).
  - draft 1 to draft 5:
    > The semantics supplies no probability of truth, no merit function and no ranking of thinkers, and a claim that needs one is unsettled.
  - scrubbed copy to latest text:
    > The semantics supplies no probability on claims and no function that orders explanations or thinkers, and a claim that needs one is left open.

#### 7. Part 0 · Grievances, anticipated / introduction (lines 33–35)

Group G01 The document as a whole · 2 units · criticism-driven 4, owner-directed 0, vocabulary-only 0, replaced wordings 12 (0 from owner-directed passes), declined 0, open 0 · owner-directed share of churn 0%.

**Pattern, in plain words:** Its two units kept one wording each. The churn is elsewhere in the section: a chain of twelve proposed wordings of a clause on narrowed claims (round 4 to S70), whose last wording (S72) the ledger marks applied but cannot place in the latest text, all standing in the section's block, placed there by the section their source names; and two fragments removed in file 11. The sentence that stands was added in file 11.

- One wording throughout: L33.s1, L35.s1.
- Records with no sentence in the latest text, in the section's block: 15, in 3 changes (never applied 1, removed 2).

#### 8. Part 0 · What is imported, what is an index, and what is defined (lines 29–31)

Group G14 The class collected · 5 units · criticism-driven 9, owner-directed 1, vocabulary-only 11, replaced wordings 7 (0 from owner-directed passes), declined 4, open 1 · owner-directed share of churn 4%.

**Pattern, in plain words:** Three of its five units grew, two at every change. "Everything else is derived." (4 words, file 10) became a 30-word sentence over five wordings, adding in turn "in the order Part XIV states", "from the two primitives, the declared indices and the declared inputs", and "the structural vocabulary of (O) and (Q)". The sentence naming the predicates "really explains", "is a cause" and "is knowledge" has five wordings; "is a created explanation" was put in by the scrub and taken out in the repaired copy, which added "(EX) is a defined relation of an episode, not such a predicate". The heading and the word pairs "primitive"/"import", "derived"/"defined" were swapped by the scrub.

- **L29.s1** (heading; crit 1, owner 0, vocab 3, replaced 1): 2 wordings, 12 → 12 words; words swapped: "primitive" → "imported" (scrubbed copy to latest text); "derived" → "defined" (scrubbed copy to latest text).
  - file 11 to draft 5:
    > ## What is primitive, what is an index, and what is derived
  - scrubbed copy to latest text:
    > ## What is imported, what is an index, and what is defined
- **L31.s1** (sentence; crit 2, owner 0, vocab 6, replaced 6): 2 wordings, 35 → 36 words; words swapped: "primitives" → "imports" (scrubbed copy to latest text); "normative" → "appraisal" (scrubbed copy to latest text); "worth" → "an appraisal" (scrubbed copy to latest text).
  - file 11 to draft 5:
    > The semantics has two primitives: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **normative relation** \(\mathcal N\), taken as an input wherever a question invokes worth.
  - scrubbed copy to latest text:
    > The semantics has two imports: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **appraisal relation** \(\mathcal N\), taken as an input wherever a question invokes an appraisal.
- **L31.s2** (sentence; crit 2, owner 0, vocab 2, replaced 4): 3 wordings, 16 → 29 → 29 words; grew longer overall; words swapped: "could be true" → "a case meets" (scrubbed copy to latest text); "false" → "fails" (scrubbed copy to latest text); made from an earlier sentence that also gave rise to another sentence (a split).
  - file 10:
    > Every claim is relative to them; none is a predicate that could be true or false.
  - file 11 to draft 5:
    > Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them, and none is a predicate that could be true or false.
  - scrubbed copy to latest text:
    > Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them, and none is a predicate that a case meets or fails.
- **L31.s3** (sentence; crit 3, owner 0, vocab 3, replaced 5): 5 wordings, 4 → 10 → 21 → 23 → 30 words; grew longer at every change; words swapped: "primitives" → "imports" (scrubbed copy to repaired copy).
  - file 10:
    > Everything else is derived.
  - file 11:
    > Everything else is derived, in the order Part XIV states.
  - draft 1 to draft 5:
    > Everything else is derived from the two primitives, the declared indices and the **declared inputs**, in the order Part XIV states.
  - scrubbed copy to repaired copy:
    > Everything else is defined in terms of the two imports, the declared indices and the **declared inputs**, in the order Part XIV states.
  - latest text:
    > Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the **declared inputs**, in the order Part XIV states.
- **L31.s4** (sentence; crit 3, owner 1, vocab 3, replaced 5): 5 wordings, 14 → 15 → 23 → 33 → 41 words; grew longer at every change; words swapped: "meaning" → "that says" (scrubbed copy); "knowledge" → "a created explanation" (scrubbed copy); "primitive" → "an import" (scrubbed copy); "Derivation" → "Argument" (scrubbed copy); "a created explanation" added (scrubbed copy) and taken out again (repaired copy to latest text); made from an earlier sentence that also gave rise to another sentence (a split).
  - file 10:
    > Nothing depends on a predicate meaning "really explains," "is a cause," or "is knowledge."
  - file 11:
    > No predicate meaning "really explains", "is a cause" or "is knowledge" appears anywhere (Derivation 6).
  - draft 1 to draft 5:
    > No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive, and no definition depends on one (Derivation 6).
  - scrubbed copy:
    > No predicate that says "explains" without a question and a contract, or "is a cause", or "is a created explanation", is taken as an import, and no definition depends on one (Argument 6).
  - repaired copy to latest text:
    > No undefined predicate that says "explains" without a question and a contract, or "is a cause", is taken as an import, and no definition depends on one (Argument 6); (EX) is a defined relation of an episode, not such a predicate.

#### 9. Part X · Ownership (line 427)

Group G10 Understanding, construction, and origin · 4 units · criticism-driven 7, owner-directed 0, vocabulary-only 5, replaced wordings 1 (0 from owner-directed passes), declined 0, open 0 · owner-directed share of churn 0%.

**Pattern, in plain words:** Small changes on long sentences: one word taken out in draft 1 ("the system's own today" became "the system's own"), "Credit for content" became "Contribution of content", and "the capability it is meant to ground" became "the capability attributed through it". A proposal in the section's block was never applied.

- **L427.s2** (sentence; crit 3, owner 0, vocab 0, replaced 0): 2 wordings, 56 → 55 words.
  - file 11:
    > Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing.
  - draft 1 to latest text:
    > Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing.
- **L427.s3** (sentence; crit 0, owner 0, vocab 2, replaced 0): 2 wordings, 33 → 33 words; words swapped: "Credit for" → "Contribution of" (scrubbed copy to latest text).
  - draft 1 to draft 5:
    > Credit for content and ownership of a process are different attributions: a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution.
  - scrubbed copy to latest text:
    > Contribution of content and ownership of a process are different attributions: a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution.
- **L427.s4** (sentence; crit 1, owner 0, vocab 3, replaced 0): 2 wordings, 14 → 12 words.
  - file 11 to draft 5:
    > Ownership is not defined by the capability it is meant to ground (Part XII).
  - scrubbed copy to latest text:
    > Ownership is not defined by the capability attributed through it (Part XII).
- One wording throughout: L427.s1.
- Records with no sentence in the latest text, in the section's block: 2, in 1 change (never applied 1).

#### 10. Part 0 · Grievances, anticipated / 6. "You have replaced explanation with evolution." (line 47)

Group G04 Layers, transports, and provenance · 3 units · criticism-driven 5, owner-directed 0, vocabulary-only 10, replaced wordings 1 (0 from owner-directed passes), declined 0, open 0 · owner-directed share of churn 0%.

**Pattern, in plain words:** Two of the three sentences grew, one at every change. The answer to the grievance was qualified in the latest text ("Selection appears once, at the bottom" became "Selection appears at the bottom: in the arrangement Part IV describes, as one possibility and not a requirement, ..."), and its last sentence was reworded three times ("the semantics forbids that reduction in Part IV"; "Part IV forbids the reduction and Part XV names its refutation"; "... names what would rule it out"; "Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out"). The middle sentence changed only "witness" to "trace".

- **L47.s1** (sentence; crit 3, owner 0, vocab 5, replaced 1): 4 wordings, 17 → 25 → 25 → 37 words; grew longer overall; words swapped: "things-with-persistence" → "persistent things" (file 11 to draft 5); "primitive" → "object" (scrubbed copy to repaired copy).
  - file 10:
    > Selection appears once, at the bottom, to produce the primitive layer of things-with-persistence that explanation operates on.
  - file 11 to draft 5:
    > **6. "You have replaced explanation with evolution."** Selection appears once, at the bottom, to produce the primitive layer of persistent things that explanation operates on.
  - scrubbed copy to repaired copy:
    > **6. "You have replaced explanation with evolution."** Selection appears once, at the bottom, to produce the object layer of persistent things that explanation operates on.
  - latest text:
    > **6. "You have replaced explanation with evolution."** Selection appears at the bottom: in the arrangement Part IV describes, as one possibility and not a requirement, it produces the object layer of persistent things that explanation operates on.
- **L47.s2** (sentence; crit 0, owner 0, vocab 3, replaced 0): 2 wordings, 15 → 15 words; words swapped: "witness" → "trace" (scrubbed copy to latest text).
  - file 10 to draft 5:
    > Construction is a separate provenance with a separate witness, and every creative attribution requires it.
  - scrubbed copy to latest text:
    > Construction is a separate provenance with a separate trace, and every creative attribution requires it.
- **L47.s3** (sentence; crit 2, owner 0, vocab 2, replaced 0): 4 wordings, 15 → 18 → 21 → 33 words; grew longer at every change; words swapped: "forbids" → "keeps" (repaired copy to latest text).
  - file 10:
    > Nothing about construction is reduced to selection; the semantics forbids that reduction in Part IV.
  - file 11 to draft 5:
    > Nothing about construction is reduced to selection; Part IV forbids the reduction and Part XV names its refutation.
  - scrubbed copy:
    > Nothing about construction is reduced to selection; Part IV forbids the reduction and Part XV names what would rule it out.
  - repaired copy to latest text:
    > Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out.

### 4.6 The fifteen units with the most substantive changes: pattern and wordings

#### 1. L536.s1 · Part XV · (Suff) Sufficiency (line 536)

Criticism-driven 7, owner-directed 1, vocabulary-only 3, replaced wordings 2 (0 from owner-directed passes), proposals declined 4, open 0; 1 of its changes and 0 of its replaced wordings came from the owner-directed passes.

Pattern: 5 wordings, 28 → 24 → 23 → 36 → 47 words; grew longer overall; words swapped: "Produce a" → "A" (file 11 to draft 5); "that satisfies" → "meeting" (file 11 to draft 5); "Part V" → "E" (file 11 to draft 5); "explains nothing" → "provides no account" (file 11 to draft 5); "A" → "Suff" (latest text); "provides no account" added (file 11 to draft 5) and taken out again (scrubbed copy); "nonetheless explains nothing" added (scrubbed copy) and taken out again (repaired copy); "explains nothing" taken out (file 11 to draft 5) and put back (scrubbed copy).

- file 10:
  > **(A) Sufficiency.** Produce a candidate that satisfies all four conditions of Account (Part V) on a physically admitted contract, with a non-declared transport, and that plainly explains nothing.
- file 11 to draft 5:
  > **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that plainly provides no account.
- scrubbed copy:
  > **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that nonetheless explains nothing.
- repaired copy:
  > **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks.
- latest text:
  > **(Suff) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.
- Proposed and replaced by a later wording (never held by the text):
  - F-23 · S90 · recommendation:
    > [no wording given] L528 s3 changed in step

#### 2. L536.s3 · Part XV · (Suff) Sufficiency (line 536)

Criticism-driven 7, owner-directed 0, vocabulary-only 0, replaced wordings 1 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: 4 wordings, 32 → 34 → 40 → 43 words; grew longer at every change; words swapped: "explain" → "explains" (draft 1 to scrubbed copy).

- file 11:
  > A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing.
- draft 1 to scrubbed copy:
  > A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and still explains nothing.
- repaired copy:
  > A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and such an argument rules it out as an explanation.
- latest text:
  > A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and such an argument rules out the claim that it is an explanation.
- Proposed and replaced by a later wording (never held by the text):
  - F-23 · S90 · recommendation:
    > [no wording given] L528 s3 changed in step

#### 3. L522.s1 · Part XIV · Declared inputs (line 522)

Criticism-driven 5, owner-directed 0, vocabulary-only 8, replaced wordings 3 (0 from owner-directed passes), proposals declined 0, open 0; none of its changes came from the owner-directed passes.

Pattern: 5 wordings, 57 → 77 → 85 → 108 → 111 words; grew longer at every change; words swapped: "primitives" → "imports" (scrubbed copy); "obligations" → "aims" (scrubbed copy); "restriction appropriate" → "wider one" (scrubbed copy); "credit" → "attribution" (scrubbed copy).

- file 11:
  > **Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII).
- draft 1 to draft 5:
  > **Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII); a weighting of credit among several contributions to one achievement, beyond any division of credit its history contains (Part XI).
- scrubbed copy:
  > **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
- the S96 stage-1 text (not kept):
  > **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
- repaired copy to latest text:
  > **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
- Proposed and replaced by a later wording (never held by the text):
  - D-827 · S95 · recommendation:
    > Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) tentatively accepts, the scope \(j\) declares and the premises \(j\) has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).

#### 4. L538.s1 · Part XV · (Nec) Necessity (line 538)

Criticism-driven 4, owner-directed 2, vocabulary-only 1, replaced wordings 2 (0 from owner-directed passes), proposals declined 2, open 0; 2 of its changes and 0 of its replaced wordings came from the owner-directed passes.

Pattern: 5 wordings, 20 → 16 → 31 → 27 → 32 words; grew longer overall; words swapped: "A genuine" → "An" (scrubbed copy); "use" → "using" (repaired copy).

- file 10:
  > **An explanation without a faithful transport.** A genuine explanation whose organization no transport can preserve under any physically admitted contract.
- file 11 to draft 5:
  > **(B) Necessity.** A genuine explanation whose organization no transport can preserve under any physically admitted contract.
- scrubbed copy:
  > **(B) Necessity.** An explanation, argued to be one and not a non-explanation by an argument that does not use (E), whose organization no transport can preserve under any physically admitted contract.
- repaired copy:
  > **(B) Necessity.** A candidate that an argument not using (E) rules out as a non-explanation, whose organization no transport can preserve under any contract on its target.
- latest text:
  > **(Nec) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, whose organization no transport can preserve under any contract on its target.
- Proposed and replaced by a later wording (never held by the text):
  - D-939 · S96 · recommendation:
    > **(B) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, while no transport can preserve its organization under any contract on its target. Eliminative explanation (Part VII) is the exposed case.

#### 5. L542.s1 · Part XV · (Prov) Genesis (line 542)

Criticism-driven 6, owner-directed 0, vocabulary-only 15, replaced wordings 0 (0 from owner-directed passes), proposals declined 2, open 0; none of its changes came from the owner-directed passes.

Pattern: 4 wordings, 88 → 92 → 90 → 90 words; words swapped: "Derivation" → "Argument" (scrubbed copy); "theorem's" → "claim's" (scrubbed copy); "a demonstration" → "an argument" (scrubbed copy); "witness" → "trace" (scrubbed copy); "a showing" → "an argument" (scrubbed copy); "primitive" → "object" (scrubbed copy) and 2 more; "an argument" added (scrubbed copy) and taken out again (repaired copy).

- file 11 to draft 5:
  > **(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation); a demonstration that every construction witness can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or a showing that the primitive layer of Part IV is not what explanation operates on.
- scrubbed copy:
  > **(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); an argument that every construction trace can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that the object layer of Part IV is not what explanation operates on.
- repaired copy:
  > **(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV.
- latest text:
  > **(Prov) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV.

#### 6. L538.s2 · Part XV · (Nec) Necessity (line 538)

Criticism-driven 6, owner-directed 0, vocabulary-only 1, replaced wordings 1 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: one wording throughout.

- file 10 to latest text:
  > Eliminative explanation (Part VII) is the exposed case.

#### 7. L540.s2 · Part XV · (Elim) Reinstatement of kinds (line 540)

Criticism-driven 5, owner-directed 0, vocabulary-only 4, replaced wordings 1 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: 5 wordings, 9 → 14 → 17 → 26 → 26 words; grew longer overall; words swapped: "reinstates" → "make" (scrubbed copy); "as primitive" → "an import again" (scrubbed copy); "Claim" → "Consequence" (latest text).

- file 10 to draft 5:
  > This refutes Derivation 1 and reinstates correspondence as primitive.
- scrubbed copy:
  > Such a case would rule out Argument 1 and make correspondence an import again.
- the S96 stage-1 text (not kept):
  > Such a case would rule out the Claim of Argument 1 and make correspondence an import again.
- repaired copy:
  > An argument that exhibits such a case would rule out the Claim of Argument 1, for whoever can use it, and make correspondence an import again.
- latest text:
  > An argument that exhibits such a case would rule out the Consequence of Argument 1, for whoever can use it, and make correspondence an import again.

#### 8. L536.s2 · Part XV · (Suff) Sufficiency (line 536)

Criticism-driven 5, owner-directed 0, vocabulary-only 0, replaced wordings 1 (0 from owner-directed passes), proposals declined 3, open 0; none of its changes came from the owner-directed passes.

Pattern: one wording throughout.

- file 11 to latest text:
  > Part V says which of the four each classic attempt fails: a table of observed answers fails (F1); a reversed calculation fails (F2) under the production contract; conclusion-as-premise fails non-circular dependence.
- Proposed and replaced by a later wording (never held by the text):
  - F-23 · S90 · recommendation:
    > [no wording given] L528 s3 changed in step

#### 9. L119.s3 · Part II · Kinds are edit-signatures (lines 111–127)

Criticism-driven 3, owner-directed 0, vocabulary-only 3, replaced wordings 3 (0 from owner-directed passes), proposals declined 3, open 0; none of its changes came from the owner-directed passes.

Pattern: 3 wordings, 47 → 47 → 50 words; words swapped: "anchor" → "counterpart" (scrubbed copy to repaired copy).

- draft 3 to draft 5:
  > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV).
- scrubbed copy to repaired copy:
  > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
- latest text:
  > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\pi\) translates valuations, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
- Proposed and replaced by a later wording (never held by the text):
  - C-86 · S90 · recommendation:
    > [no wording given] held under D2: nothing drafted; the placeholder names the S88 candidate wordings then in view for file-11 lines 121, 554, 620
  - C-188 · S90 · recommendation:
    > (Parts IV and V)
  - D-905 · S96 · recommendation:
    > where \(\pi\) translates ports, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with \(\pi\) restricted to its ports (Part IV).

#### 10. L405.s5 · Part X · Construction (line 405)

Criticism-driven 3, owner-directed 0, vocabulary-only 0, replaced wordings 3 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: one wording throughout.

- file 11 to latest text:
  > A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.
- Proposed and replaced by a later wording (never held by the text):
  - A-286 · S70 (log S71) · recommendation:
    > A small newly constructed binding keeps its own origin while the rest of the received content keeps its inherited provenance.
  - F-29 · S90 · recommendation:
    > [no wording given] restore the first two paragraphs of 00:855–861 after Build
  - F-30 · S90 · recommendation:
    > a witness may identify a binding by its use (reason use, Part IX); a carrier that delivers content it does not use that way has relayed it, and relay is not construction

#### 11. L119.s2 · Part II · Kinds are edit-signatures (lines 111–127)

Criticism-driven 2, owner-directed 0, vocabulary-only 0, replaced wordings 4 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: one wording throughout.

- file 10 to latest text:
  > A kind is an equivalence class of components under this relation.
- Proposed and replaced by a later wording (never held by the text):
  - B-264 · S88 · recommendation:
    > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivations 1 and 2 use kinds in this sense.
  - C-72 · S90 · edit:
    > A kind is an equivalence class of components under this relation. A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
  - C-73 · S90 · edit:
    > A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
  - C-86 · S90 · recommendation:
    > [no wording given] held under D2: nothing drafted; the placeholder names the S88 candidate wordings then in view for file-11 lines 121, 554, 620

#### 12. L313.s2 · Part VI · Commitments that do no work (line 313)

Criticism-driven 1, owner-directed 0, vocabulary-only 3, replaced wordings 6 (0 from owner-directed passes), proposals declined 3, open 0; none of its changes came from the owner-directed passes.

Pattern: 3 wordings, 52 → 58 → 58 words; words swapped: "the candidate" → "it" (draft 4 to draft 5); "support" → "route" (scrubbed copy to latest text); "support" → "route" (scrubbed copy to latest text); "support" → "route" (scrubbed copy to latest text); "support" → "route" (scrubbed copy to latest text).

- draft 1 to draft 3:
  > A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B).
- draft 4 to draft 5:
  > A commitment \(d\) of a candidate that has a support does no work by itself in it when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B).
- scrubbed copy to latest text:
  > A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no route (B).
- Proposed and replaced by a later wording (never held by the text):
  - C-79 · S90 · edit:
    > **Hard-to-vary.** For explanatory jobs \(F\subseteq F'\), \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), where \(\operatorname{Pres}(F)=\{v\in\mathcal V:\forall f\in F,\operatorname{Account}(E_v,f)\}\). The **reach** of \(E\) is the set of jobs \(f\) with \(\operatorname{Account}(E,f)\); it is fixed by \(E\) and the world, not by which jobs anyone has checked.
  - C-80 · S90 · edit:
    > More reach constrains variation; the containment need not be strict; counting jobs is not a warrant. (E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support). How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing.
  - E-53 · S91 · recommendation:
    > (E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support).
  - E-45 · S91 · recommendation:
    > What the measure bears on is correction: a commitment that does no work cannot absorb a failure, and a part varied or added to absorb one is recorded (Part VIII).
  - E-51 · S91 · recommendation:
    > **Correction in a common family.** Let a later organization \(E_1\), with commitments \(\Gamma_1\), be declared with a family \(\mathcal V\) of organization edits that has a member \(v_0\) with \(E_{1,v_0}=E_0\): the earlier candidate's organization, each component it keeps with its earlier anchor, and the named background fixed. Where \(E_1\) only adds a block \(B\), \(E_0=E_1|(\Gamma_1\setminus B)\). Where it changes a component, \(v_0\) restores it. Let \(\operatorname{Account}(E_0,f)\) for every \(f\in F\), and \(\neg\operatorname{Account}(E_0,f^*)\). By (A), every job whose contract holds a pair at which \(E_0\) answers otherwise than the target is such an \(f^*\). Then
    > \[
    > v_0\in\operatorname{Pres}(F)\setminus\operatorname{Pres}(F\cup\{f^*\}),\qquad\text{so}\qquad\operatorname{Pres}(F\cup\{f^*\})\subsetneq\operatorname{Pres}(F).\tag{H\(^*\)}
    > \]
    > If also \(\operatorname{Account}(E_1,f^*)\) and \(E_0=E_1|(\Gamma_1\setminus B)\), then \(\operatorname{CriticalBlock}(B;\Gamma_1,f^*)\). *Proof.* (H) gives the containment. \(v_0\) is in \(\operatorname{Pres}(F)\) by the first hypothesis and not in \(\operatorname{Pres}(F\cup\{f^*\})\) by the second. For the block, \(\Gamma_1\in\mathsf S_{E_1,f^*}\) and \(\Gamma_1\setminus B\notin\mathsf S_{E_1,f^*}\) (B). ∎
    >
    > The same argument, with the identity edit as the witness, covers a narrowing. If \(E\) is an account on every job of \(F\) and not on \(f^*\), then \(\operatorname{Pres}(F)\supsetneq\operatorname{Pres}(F\cup\{f^*\})\). This holds whether \(f^*\) was held at an earlier index and dropped after a failure, or was never claimed. Which of the two it was is read from the historical index (Part VIII), not from \(\operatorname{Pres}\).
    >
    > (H\(^*\)) says what \(f^*\) excludes and nothing more.
    > (i) A member of \(\operatorname{Pres}(F\cup\{f^*\})\) may answer as \(E_0\) does at a pair where \(E_0\) answers otherwise than the target, whenever no job of \(F\cup\{f^*\}\) holds that pair in its contract.
    > (ii) For any \(\mathcal V_0\subseteq\mathcal V\), \(\operatorname{Pres}_{\mathcal V_0}(F)=\operatorname{Pres}_{\mathcal V}(F)\cap\mathcal V_0\). So where the earlier organization's own family sits inside \(\mathcal V\), the later organization is never the harder to vary on the same jobs.
    > (iii) Two members of \(\mathcal V\) that are both accounts on \(F\cup\{f^*\}\) both belong to \(\operatorname{Pres}(F\cup\{f^*\})\). Only a job on which one is an account and the other is not separates them, and that is (A) on that job, not variation.
    > (iv) If no member of \(\mathcal V\) gives \(E_0\), (H\(^*\)) does not apply, and the containment may be non-strict.
    >
    > (H\(^*\)) relates two subsets of one family of one organization under one interpretation, which is the premise of (H). It orders no candidates. It uses no fact about who wrote \(E_1\) or when. It holds for every declared \(\mathcal V\) that has the member \(v_0\).

#### 13. L231.s1 · Part V · Opening of the Part (lines 229–231)

Criticism-driven 1, owner-directed 0, vocabulary-only 0, replaced wordings 5 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: one wording throughout.

- file 10 to latest text:
  > An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\).
- Proposed and replaced by a later wording (never held by the text):
  - B-276 · S88 · recommendation:
    > The commitments Γ are components of E; the boundary values of E belong to the named background of Part VI.
  - C-77 · S90 · edit:
    > An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
  - C-78 · S90 · edit:
    > An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
  - C-87 · S90 · recommendation:
    > [no wording given] held under D2: nothing drafted; the placeholder names the S88 candidate wordings then in view for file-11 lines 233, 257, 518, 518
  - F-35 · S90 · recommendation:
    > \(\Gamma\) is a set of components of \(E\): those the candidate offers as doing the work

#### 14. L526.s18 · Part XIV · Dependence order (line 526)

Criticism-driven 4, owner-directed 0, vocabulary-only 6, replaced wordings 3 (0 from owner-directed passes), proposals declined 0, open 0; none of its changes came from the owner-directed passes.

Pattern: 5 wordings, 46 → 55 → 55 → 74 → 67 words; grew longer overall; words swapped: "justified" → "defined" (scrubbed copy); "justified" → "each defined" (scrubbed copy); "each" → "the" (scrubbed copy); "proof" → "argument" (scrubbed copy); "argument" → "definition" (the S96 stage-1 text (not kept)); "it , and" → "the order ;" (latest text) and 3 more; "has no cycle and no endless descent" added (scrubbed copy) and taken out again (latest text); "argument" added (scrubbed copy) and taken out again (the S96 stage-1 text (not kept)); made from an earlier sentence that also gave rise to another sentence (a split).

- file 11 to draft 5:
  > The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it.
- scrubbed copy:
  > The order has no cycle and no endless descent: a representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in it, and a separate argument that would supply it is part of the account only when the account uses it.
- the S96 stage-1 text (not kept):
  > The order has no cycle and no endless descent: a representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in it, and a separate definition that would supply it is part of the account only when the account uses it.
- repaired copy:
  > The order has no cycle and no endless descent: a representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in it, and a separate definition that would supply it, or a separate argument that rules out the denial of the result it is defined through without using it, is part of the account only when the account uses it.
- latest text:
  > A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order; a separate definition that would supply that place, or a separate argument that rules out the denial of the result the definition goes through without using that result, is part of the account only when the account uses it.

#### 15. L299.s2 · Part VI · Opening of the Part (lines 285–303)

Criticism-driven 4, owner-directed 0, vocabulary-only 2, replaced wordings 2 (0 from owner-directed passes), proposals declined 1, open 0; none of its changes came from the owner-directed passes.

Pattern: 4 wordings, 44 → 54 → 53 → 73 words; grew longer overall; words swapped: "support" → "route" (scrubbed copy); "successful support" → "route" (scrubbed copy); "supports" → "routes" (scrubbed copy); "support" → "route" (scrubbed copy).

- file 11:
  > Criticality is relative to the support \(W\) it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are the ones actually written, not a support someone could write in their place.
- draft 1 to draft 5:
  > Criticality is relative to the support \(W\) it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out, not a support someone could write with commitments outside \(\Gamma\).
- scrubbed copy:
  > Criticality is relative to the route \(W\) it is assessed in: a commitment critical in one route need not be critical in the full candidate, and the routes assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out, not a route someone could write with commitments outside \(\Gamma\).
- repaired copy to latest text:
  > Criticality is relative to the route \(W\) it is assessed in, a **route** of the candidate being a member of \(\mathsf S_{E,p}\) (not an active route of a history, Part IX): a commitment critical in one route need not be critical in the full candidate, and the routes assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out, not a route someone could write with commitments outside \(\Gamma\).
- Proposed and replaced by a later wording (never held by the text):
  - F-32 · S90 · recommendation:
    > the supports assessed are subsets of the written Γ, not a support someone could write in its place

### 4.7 Every wording that came back

A later wording that repeats an earlier one of the same unit after a different wording between: a change that did not stick. *Exact* means the same once emphasis and spacing are set aside; *near* means a similarity of 0.97 or more with a different wording between.

| unit | section | kind | the wording of | came back in | pattern |
| --- | --- | --- | --- | --- | --- |
| L626.s3 | 10. A two-layer episode, in exact form | exact | file 10 | draft 1 to latest text | 3 wordings, 22 → 43 → 22 words; the wording of file 10 came back in draft 1 to latest text; ", and this is Derivation 3's qualification seen from the other side , a populati" added (file 11) and taken out again (draft 1 to latest text) |

- **L626.s3**:
  - file 10:
    > If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.
  - file 11:
    > If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric, and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change.
  - draft 1 to latest text:
    > If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.

Phrases added and later taken out, or taken out and later put back (34):

| unit | section | what happened | phrase | first step | second step |
| --- | --- | --- | --- | --- | --- |
| L13.s3 | What this document claims | taken out, then put back | blind | file 11 | draft 1 to draft 2 |
| L13.s3 | What this document claims | added, then taken out | blind | draft 1 to draft 2 | draft 3 to latest text |
| L17.s2 | What this document claims | added, then taken out | conflict with | repaired copy | latest text |
| L17.s4 | What this document claims | added, then taken out | rule it out | scrubbed copy | repaired copy to latest text |
| L31.s4 | What is imported, what is an index, and what is defined | added, then taken out | a created explanation | scrubbed copy | repaired copy to latest text |
| L49.s3 | Grievances, anticipated / 7. "Mathematics has no interventions." | added, then taken out | mathematical argument | scrubbed copy to repaired copy | latest text |
| L75.s2 | Substrate independence with physical conditions | added, then taken out | possible under | scrubbed copy | repaired copy to latest text |
| L159.s6 | Scope, and a question that can be in error | added, then taken out | drops changes the question asked contains | scrubbed copy | repaired copy to latest text |
| L211.s2 | Representation is defined, not supplied | added, then taken out | its target | repaired copy | latest text |
| L315.s6 | Rivals | added, then taken out | candidate | scrubbed copy | repaired copy to latest text |
| L315.s19 | Rivals | added, then taken out | is not ruled out either | scrubbed copy | repaired copy to latest text |
| L315.s19 | Rivals | added, then taken out | not ruled out | scrubbed copy | repaired copy to latest text |
| L317.s4 | Problems | added, then taken out | for that assessor | repaired copy | latest text |
| L317.s4 | Problems | added, then taken out | so long as the premises about the test's background and instruments are live for that assessor ( K2 , K3 ) : | repaired copy | latest text |
| L317.s4 | Problems | added, then taken out | assessor , while it | repaired copy | latest text |
| L317.s4 | Problems | added, then taken out | that such an argument | repaired copy | latest text |
| L343.s9 | Odd-order skew-symmetric matrices | added, then taken out | mathematical argument | scrubbed copy to repaired copy | latest text |
| L385.s2 | Reason use | added, then taken out | gives | scrubbed copy | repaired copy to latest text |
| L441.s5 | The aims of a repair | added, then taken out | contains | scrubbed copy | repaired copy to latest text |
| L518.s1 | Imports | added, then taken out | defined in terms of anything else | scrubbed copy | repaired copy to latest text |
| L526.s17 | Dependence order | added, then taken out | argument | scrubbed copy | repaired copy |
| L526.s17 | Dependence order | added, then taken out | is part of the account | scrubbed copy | latest text |
| L526.s17 | Dependence order | added, then taken out | , or a separate argument that rules out the denial of the result it is defined through without using it , | repaired copy | latest text |
| L526.s18 | Dependence order | added, then taken out | has no cycle and no endless descent | scrubbed copy | latest text |
| L526.s18 | Dependence order | added, then taken out | argument | scrubbed copy | the S96 stage-1 text (not kept) |
| L536.s1 | (Suff) Sufficiency | added, then taken out | provides no account | file 11 to draft 5 | scrubbed copy |
| L536.s1 | (Suff) Sufficiency | taken out, then put back | explains nothing | file 11 to draft 5 | scrubbed copy |
| L536.s1 | (Suff) Sufficiency | added, then taken out | nonetheless explains nothing | scrubbed copy | repaired copy |
| L542.s1 | (Prov) Genesis | added, then taken out | an argument | scrubbed copy | repaired copy |
| L544.s1 | (QF) Question-finding | added, then taken out | A showing | file 11 to draft 5 | scrubbed copy |
| L544.s1 | (QF) Question-finding | added, then taken out | An argument | scrubbed copy | repaired copy |
| L600.s1 | 6. There are two imports | added, then taken out | a created explanation | scrubbed copy | repaired copy to latest text |
| L600.s3 | 6. There are two imports | added, then taken out | taken as an import | scrubbed copy | repaired copy to latest text |
| L626.s3 | 10. A two-layer episode, in exact form | added, then taken out | , and this is Derivation 3's qualification seen from the other side , a population that admits no survivor at the new ch | file 11 | draft 1 to latest text |

## 5. The values group

The units of group G11 (Part XI, "Repair, created explanation, and appraisal", with grievance 8 filed there) and every unit elsewhere whose wording in any version speaks of worth, appraisal, aesthetics, the normative or appraisal relation \(\mathcal N\), merit, or an order of explanations or thinkers: 38 units.

| unit | section | since | crit | owner | vocab | repl | decl | open | substantive | neighbour churn | strong list |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| L25.s1 | What this document does not claim | file 10 | 2 | 1 | 2 | 2 | 0 | 0 | 3 | 0.75 |  |
| L25.s2 | What this document does not claim | file 11 | 2 | 0 | 4 | 2 | 0 | 0 | 2 | 0.83 |  |
| L31.s1 | What is imported, what is an index, and what is defined | file 11 | 2 | 0 | 6 | 6 | 0 | 0 | 4 | 2.6 |  |
| L51.s1 | Grievances, anticipated / 8. "Where is aesthetics?" | file 10 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 1.75 | challenged and kept |
| L51.s2 | Grievances, anticipated / 8. "Where is aesthetics?" | file 10 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 1.5 |  |
| L51.s3 | Grievances, anticipated / 8. "Where is aesthetics?" | file 10 | 3 | 0 | 3 | 0 | 0 | 0 | 3 | 1.5 |  |
| L71.s3 | Conjecture, criticism, action | file 10 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0.75 | untouched, below the neighbour cut |
| L433.s1 | Opening of the Part | file 10 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 1.75 |  |
| L435.s1 | Repair | draft 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1.25 |  |
| L435.s2 | Repair | file 10 | 1 | 0 | 3 | 0 | 0 | 0 | 1 | 1 |  |
| L437.s1 | Repair | file 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1.25 | challenged and kept |
| L441.s1 | The aims of a repair | file 11 | 3 | 0 | 4 | 0 | 0 | 0 | 3 | 1 |  |
| L441.s2 | The aims of a repair | draft 1 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 1.5 | untouched, younger than file 10 |
| L441.s3 | The aims of a repair | file 11 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 1.8 | untouched, younger than file 10 |
| L441.s4 | The aims of a repair | file 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1.8 | challenged and kept |
| L441.s5 | The aims of a repair | file 11 | 2 | 0 | 4 | 1 | 0 | 0 | 2 | 1.5 |  |
| L441.s6 | The aims of a repair | file 11 | 1 | 0 | 3 | 3 | 0 | 0 | 4 | 1 |  |
| L443.s1 | Created explanation | scrubbed copy | 1 | 1 | 2 | 0 | 0 | 1 | 2 | 1.6 |  |
| L443.s2 | Created explanation | file 10 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 2 | never challenged |
| L443.s3 | Created explanation | file 10 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | untouched, below the neighbour cut |
| L445.s1 | Created explanation | file 10 | 1 | 0 | 3 | 1 | 0 | 1 | 2 | 0.8 |  |
| L453.s1 | Result, and the index of (EX) | draft 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1.17 | untouched, younger than file 10 |
| L453.s2 | Result, and the index of (EX) | draft 1 | 1 | 0 | 1 | 2 | 0 | 0 | 2 | 1 |  |
| L453.s3 | Result, and the index of (EX) | latest text | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| L453.s4 | Result, and the index of (EX) | file 10 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1.2 |  |
| L453.s5 | Result, and the index of (EX) | file 10 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1.5 |  |
| L455.s1 | Appraisal | file 11 | 1 | 1 | 5 | 2 | 1 | 1 | 2 | 1.83 |  |
| L455.s2 | Appraisal | file 11 | 2 | 1 | 3 | 2 | 1 | 0 | 3 | 1.8 |  |
| L455.s3 | Appraisal | file 10 | 3 | 0 | 0 | 0 | 2 | 0 | 3 | 2 |  |
| L455.s4 | Appraisal | file 10 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 2 |  |
| L455.s5 | Appraisal | file 10 | 2 | 0 | 1 | 1 | 1 | 0 | 2 | 1.67 |  |
| L518.s1 | Imports | file 10 | 3 | 0 | 3 | 2 | 0 | 0 | 3 | 1 |  |
| L522.s2 | Declared inputs | file 11 | 1 | 1 | 3 | 3 | 0 | 0 | 3 | 2.5 |  |
| L522.s3 | Declared inputs | draft 1 | 0 | 1 | 2 | 2 | 0 | 0 | 2 | 3 |  |
| L534.s3 | Opening of the Part | draft 1 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 4.2 | untouched, younger than file 10 |
| L592.s3 | 5. Question-finding is representable | file 11 | 1 | 0 | 3 | 1 | 0 | 0 | 1 | 0.5 |  |
| L596.s1 | 6. There are two imports | file 10 | 2 | 0 | 1 | 0 | 0 | 0 | 2 | 1 |  |
| L600.s2 | 6. There are two imports | file 10 | 1 | 0 | 3 | 1 | 0 | 0 | 1 | 1 |  |

- Units: 38; substantive changes 57 in all, 1.5 per unit (all 694 units: 0.99). Criticism-driven 41, owner-directed 7, vocabulary-only 81.
- Strong candidates among them: L51.s1 (challenged and kept), L437.s1 (challenged and kept), L441.s4 (challenged and kept), L443.s2 (never challenged).
- Untouched in substance, not on the lists: L71.s3 (neighbour churn below the cut), L441.s2 (since draft 1), L441.s3 (since file 11), L443.s3 (neighbour churn below the cut), L453.s1 (since draft 1), L534.s3 (since draft 1).
- Proposals open for the owner on these units: CH-1132 on L433.s1; CH-1200 on L443.s1; CH-1132 on L443.s2; CH-1132 on L445.s1; CH-1206 on L455.s1.

**Pattern, in plain words.** From file 10 on, the text has taken values from outside it: file 10's second import reads "The **normative relation** \(\mathcal N\), when a question invokes one." That arrangement stands in every version; what changed is its name and the wording around it. The scrub renamed it ("normative relation" to "appraisal relation", "worth" to "an appraisal", "primitive" to "import"), the heading of Part XI went from "Progress, knowledge, and the normative" to "Repair, created explanation, and appraisal", and "obligations" became "aims". The sentences that say the semantics does not supply or define it grew: "The semantics does not derive \(\mathcal N\)." gained a clause in file 11 and its verb changed in the scrub; the import's own sentence grew from 11 to 34 words. The value units have 1.5 substantive changes each, against 0.99 for all units; 4 of the 38 are strong candidates. One proposal on the Appraisal paragraph is open for the owner (below).

Runs of wordings of the 20 units whose wording in some version speaks of worth, appraisal, aesthetics, the normative or appraisal relation, merit, or an order of explanations or thinkers (the repair units of Part XI without such words are in the table and the data file only):

- **L25.s1** (What this document does not claim): 3 wordings, 19 → 23 → 28 words; grew longer at every change.
  - file 10:
    > It does not supply an objective aesthetics, a probability of truth, a merit function, or a ranking of thinkers.
  - file 11 to draft 5:
    > It does not supply an objective aesthetics, a probability of truth, a merit function, a measure of worth, or a ranking of thinkers.
  - scrubbed copy to latest text:
    > It does not supply an aesthetics independent of any declared appraisal, a probability on claims, an appraisal of its own, or a function that orders explanations or thinkers.
- **L25.s2** (What this document does not claim): 3 wordings, 22 → 48 → 50 words; grew longer at every change; words swapped: "takes" → "does not supply" (draft 1 to draft 5); "normative" → "appraisal" (scrubbed copy to latest text); "unsettled" → "left open" (scrubbed copy to latest text).
  - file 11:
    > Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV).
  - draft 1 to draft 5:
    > Where a claim needs one of these, the semantics does not supply it and marks the place: a claim of worth or of aesthetic value takes the normative relation as an input (Parts XI, XIV), and a claim that needs any of the others is unsettled (Part XIV).
  - scrubbed copy to latest text:
    > Where a claim needs one of these, the semantics does not supply it and marks the place: a claim that invokes an appraisal or aesthetic value takes the appraisal relation as an input (Parts XI, XIV), and a claim that needs any of the others is left open (Part XIV).
- **L31.s1** (What is imported, what is an index, and what is defined): 2 wordings, 35 → 36 words; words swapped: "primitives" → "imports" (scrubbed copy to latest text); "normative" → "appraisal" (scrubbed copy to latest text); "worth" → "an appraisal" (scrubbed copy to latest text).
  - file 11 to draft 5:
    > The semantics has two primitives: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **normative relation** \(\mathcal N\), taken as an input wherever a question invokes worth.
  - scrubbed copy to latest text:
    > The semantics has two imports: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **appraisal relation** \(\mathcal N\), taken as an input wherever a question invokes an appraisal.
- **L51.s1** (Grievances, anticipated / 8. "Where is aesthetics?"): 3 wordings, 8 → 12 → 12 words; grew longer overall; words swapped: "normative" → "appraisal" (scrubbed copy to latest text).
  - file 10:
    > In Part XI, as a declared normative relation.
  - file 11 to draft 5:
    > **8. "Where is aesthetics?"** In Part XI, as a declared normative relation.
  - scrubbed copy to latest text:
    > **8. "Where is aesthetics?"** In Part XI, as a declared appraisal relation.
- **L51.s2** (Grievances, anticipated / 8. "Where is aesthetics?"): 3 wordings, 21 → 17 → 17 words; words swapped: "carriers" → "relations" (repaired copy to latest text).
  - file 10:
    > The semantics gives artistic effect, artistic purpose, and aesthetic reasons three distinct mathematical carriers and refuses to define any as another.
  - file 11 to scrubbed copy:
    > Artistic effect, artistic purpose and aesthetic reasons get three distinct carriers, and none is defined as another.
  - repaired copy to latest text:
    > Artistic effect, artistic purpose and aesthetic reasons get three distinct relations, and none is defined as another.
- **L51.s3** (Grievances, anticipated / 8. "Where is aesthetics?"): 3 wordings, 11 → 12 → 9 words; words swapped: "It" → "The semantics" (file 11 to draft 5).
  - file 10:
    > It does not pretend to know which aesthetic reasons are true.
  - file 11 to draft 5:
    > The semantics does not pretend to know which aesthetic reasons are true.
  - scrubbed copy to latest text:
    > The semantics does not decide between rival aesthetic reasons.
- **L71.s3** (Conjecture, criticism, action): 2 wordings, 10 → 12 words.
  - file 10 to draft 5:
    > A thinker may act on an appraisal without certifying it.
  - scrubbed copy to latest text:
    > A thinker may act on an appraisal that no argument has decided.
- **L433.s1** (Opening of the Part): 2 wordings, 9 → 9 words; words swapped: "Progress" → "Repair" (scrubbed copy to latest text); "knowledge" → "created explanation" (scrubbed copy to latest text); "the normative" → "appraisal" (scrubbed copy to latest text).
  - file 10 to draft 5:
    > # Part XI — Progress, knowledge, and the normative
  - scrubbed copy to latest text:
    > # Part XI — Repair, created explanation, and appraisal
- **L441.s3** (The aims of a repair): 2 wordings, 17 → 15 words; words swapped: "claim that" → "appraisal of" (scrubbed copy to latest text).
  - file 11 to draft 5:
    > Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives.
  - scrubbed copy to latest text:
    > Their declaration makes no appraisal of the aims, and (P) puts no order on alternatives.
- **L455.s1** (Appraisal): 2 wordings, 30 → 22 words; got shorter overall; words swapped: "obligation establishes that" → "aim repairs" (scrubbed copy to latest text); "whether" → "how anyone appraises" (scrubbed copy to latest text); "obligation" → "aim" (scrubbed copy to latest text).
  - file 11 to draft 5:
    > **Worth, and the normative relation.** Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having.
  - scrubbed copy to latest text:
    > **Appraisal.** Repairing an aim repairs it and says nothing about how anyone appraises the aim, or the question that led to it.
- **L455.s2** (Appraisal): 3 wordings, 23 → 24 → 25 words; grew longer at every change; words swapped: "a declared" → "an" (draft 1 to draft 5); "worth" → "an appraisal" (scrubbed copy to latest text); "normative" → "appraisal" (scrubbed copy to latest text); "primitive" → "import" (scrubbed copy to latest text).
  - file 11:
    > Where a claim invokes worth, the semantics takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV).
  - draft 1 to draft 5:
    > Where a claim invokes worth, the semantics takes the **normative relation** \(\mathcal N\) (primitive 2, Part XIV) as an input and marks the place.
  - scrubbed copy to latest text:
    > Where a claim invokes an appraisal, the semantics takes the **appraisal relation** \(\mathcal N\) (import 2, Part XIV) as an input and marks the place.
- **L455.s3** (Appraisal): 4 wordings, 44 → 43 → 43 → 68 words; grew longer overall; words swapped: "a normative relation" → "and" (file 11); "declared" → "taken" (draft 1 to repaired copy).
  - file 10:
    > **Artistic effect, purpose, and aesthetic reason.** An effect organization \(\mathcal R\subseteq A\times K\times F\); a purpose \(G\subseteq K\times F\); achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); a normative relation \(\mathcal N\subseteq A\times K\times\mathcal Rsn\times\mathcal V_A\) declared as a substantive input when aesthetic value is claimed.
  - file 11:
    > The aesthetic case is one such invocation: an effect organization \(\mathcal R\subseteq A\times K\times F\); a purpose \(G\subseteq K\times F\); achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq A\times K\times\mathcal Rsn\times\mathcal V_A\) declared as a substantive input when aesthetic value is claimed.
  - draft 1 to repaired copy:
    > The aesthetic case is one such invocation: an effect organization \(\mathcal R\subseteq A\times K\times F\); a purpose \(G\subseteq K\times F\); achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq A\times K\times\mathcal Rsn\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed.
  - latest text:
    > The aesthetic case is one such invocation: an effect organization \(\mathcal R\subseteq \mathit{Act}\times\mathit{Occ}\times\mathit{Eff}\); a purpose \(G\subseteq \mathit{Occ}\times\mathit{Eff}\); achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq \mathit{Act}\times\mathit{Occ}\times\mathsf{Rsn}\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed, where \(\mathit{Act}\) is a set of actions, \(\mathit{Occ}\) of occasions, \(\mathit{Eff}\) of effects, \(\mathsf{Rsn}\) of aesthetic reasons and \(\mathcal V_A\) of aesthetic values, the last two not further specified here.
- **L455.s5** (Appraisal): 3 wordings, 7 → 16 → 16 words; grew longer overall; words swapped: "derive" → "define" (scrubbed copy to latest text).
  - file 10:
    > The semantics does not derive \(\mathcal N\).
  - file 11 to draft 5:
    > The semantics does not derive \(\mathcal N\), and no aesthetics follows from achieving a stated effect.
  - scrubbed copy to latest text:
    > The semantics does not define \(\mathcal N\), and no aesthetics follows from achieving a stated effect.
- **L518.s1** (Imports): 4 wordings, 11 → 29 → 35 → 34 words; grew longer overall; words swapped: "normative" → "appraisal" (scrubbed copy); "worth" → "an appraisal" (scrubbed copy); "defined in terms of anything else" added (scrubbed copy) and taken out again (repaired copy to latest text).
  - file 10:
    > 2. The **normative relation** \(\mathcal N\), when a question invokes one.
  - file 11 to draft 5:
    > 2. The **normative relation** \(\mathcal N\), when a question invokes worth. It is taken as an input and never derived; the aesthetic relation of Part XI is one instance.
  - scrubbed copy:
    > 2. The **appraisal relation** \(\mathcal N\), when a question invokes an appraisal. It is taken as an input and never defined in terms of anything else; the aesthetic relation of Part XI is one instance.
  - repaired copy to latest text:
    > 2. The **appraisal relation** \(\mathcal N\), when a question invokes an appraisal. It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance.
- **L522.s2** (Declared inputs): 3 wordings, 37 → 47 → 49 words; grew longer at every change; words swapped: "A verdict" → "An assessment" (scrubbed copy to latest text); "normative" → "appraisal" (scrubbed copy to latest text); "worth" → "an appraisal" (scrubbed copy to latest text); "a verdict" → "an assessment" (scrubbed copy to latest text); "verdict" → "assessment" (scrubbed copy to latest text); "unsettled" → "left open" (scrubbed copy to latest text) and 1 more.
  - file 11:
    > A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.
  - draft 1 to draft 5:
    > A verdict that depends on one of these, or on the normative relation where a claim invokes worth, is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.
  - scrubbed copy to latest text:
    > An assessment that depends on one of these, or on the appraisal relation where a claim invokes an appraisal, is an assessment given the input; where the input is missing, the assessment is left open and the semantics says so rather than choosing the input from the assessment wanted.
- **L522.s3** (Declared inputs): 2 wordings, 23 → 24 words; words swapped: "unsettled" → "left open" (scrubbed copy to latest text).
  - draft 1 to draft 5:
    > The semantics supplies no probability of truth, no merit function and no ranking of thinkers, and a claim that needs one is unsettled.
  - scrubbed copy to latest text:
    > The semantics supplies no probability on claims and no function that orders explanations or thinkers, and a claim that needs one is left open.
- **L534.s3** (Opening of the Part): 2 wordings, 39 → 44 words; words swapped: "verdict" → "assessment" (scrubbed copy to latest text); "normative" → "appraisal" (scrubbed copy to latest text); "refutation" → "claim out" (scrubbed copy to latest text).
  - draft 1 to draft 5:
    > A case whose verdict turns on an input the case does not state, where the input is one of the declared inputs Part XIV lists or the normative relation, is a case with a missing input, not a refutation.
  - scrubbed copy to latest text:
    > A case whose assessment turns on an input the case does not state, where the input is one of the declared inputs Part XIV lists or the appraisal relation, is a case with a missing input, not an argument that rules a claim out.
- **L592.s3** (5. Question-finding is representable): 2 wordings, 12 → 14 words.
  - file 11 to draft 5:
    > That a question was found says nothing about its worth (Part XI).
  - scrubbed copy to latest text:
    > That a question was found says nothing about how anyone appraises it (Part XI).
- **L596.s1** (6. There are two imports): 4 wordings, 21 → 24 → 26 → 33 words; grew longer at every change; words swapped: "from" → "in terms of" (scrubbed copy to repaired copy).
  - file 10:
    > **Claim.** Every predicate in Parts II–XIII is defined from \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with declared indices.
  - file 11 to draft 5:
    > **Claim.** Every predicate in Parts II–XIII is defined from \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with declared indices and declared inputs.
  - scrubbed copy to repaired copy:
    > **Claim.** Every predicate in Parts II–XIII is defined in terms of \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with declared indices and declared inputs.
  - latest text:
    > **Claim.** Every predicate in Parts II–XIII is defined in terms of \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with the structural vocabulary of (O) and (Q), declared indices and declared inputs.
- **L600.s2** (6. There are two imports): 3 wordings, 18 → 18 → 18 words; words swapped: "primitives" → "imports" (scrubbed copy to repaired copy); "reasons" → "appraisal" (latest text).
  - file 10 to draft 5:
    > The two primitives are a theory of matter and, when a question requires it, a theory of reasons.
  - scrubbed copy to repaired copy:
    > The two imports are a theory of matter and, when a question requires it, a theory of reasons.
  - latest text:
    > The two imports are a theory of matter and, when a question requires it, a theory of appraisal.

Open proposal CH-1132 (a vocabulary proposal), on L433.s1, L443.s2, L445.s1:

- D-591 · S95 · recommendation · open for the owner · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 2, row 41 (OWNER), file line 65
  > Claude's recommendation: the rename, unless the owner wants Deutsch's sense; then add the condition, do not keep the word alone.

Open proposal CH-1200 (a vocabulary proposal), on L443.s1:

- D-764 · S95 · recommendation · open for the owner · source: results/S95 Does the semantics hold without verificationist words.md — section 8, belief words, R6 option A, l. 223
  > "has no unshaped violation"/"unshaped violation"

Open proposal CH-1206 (on this sentence), on L455.s1:

- D-775 · S95 · recommendation · open for the owner · source: results/S95 Does the semantics hold without verificationist words.md — section 9, MORE, l. 455 (optional)
  > Repairing an aim repairs it and says nothing about any appraisal of the aim, or of the question that led to it; an appraisal, where one is invoked, is itself a claim open to criticism.

The dependence order of the latest text does not name the appraisal relation; its list of imports (Part XIV) says:

> 2. The **appraisal relation** \(\mathcal N\), when a question invokes an appraisal. It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance.

## 6. What is unsure

- **Untouched may mean unexamined.** A unit no proposal touched may never have been read closely; list 2 says nothing about how it would fare.
- **The counts depend on how the ledger split and placed things.** A change is counted on the sentences the ledger placed it on; 603 records were placed by the line they were written against, not by their own words, and a change to one sentence may stand on its neighbour (§3.4 shows four such cases). R2's 137 proposals were written against file 20, which the repository does not hold, and read as amendments to file 10.
- **Following a unit back is by similarity.** A heavily reworded sentence can be taken for new (it then looks younger than it is), and two different sentences can, rarely, be taken for one (the unit then shows a change it never had, which keeps it off the lists).
- **A record that names several sentences counts on each.** A paragraph-wide edit, or the removal of a sentence listed with the sentences of its paragraph, adds a change to sentences whose own words did not change (L536.s2 has five changes and one wording since file 11). And the scrub recorded each word swap as its own change, so a long sentence can carry many vocabulary-only changes (15 on the Genesis item).
- **Owner-directed passes inflate churn.** The scrub touched 269 units and the S96 and S97 owner-directed stages 45; their counts are given apart everywhere, and the neighbour churn used for the cut includes them.
- **Which class a change falls in follows the definitions given**, not a reading of each change: the repairs the S95 readings asked for count as criticism-driven though they were applied with an owner-directed pass; draft 4's restatement of hard to vary followed the owner's decision S20 and counts as criticism-driven (4 changes on units of the latest text came from S91).
- **Per-unit rates swing for small sections**; §4.3 gives the sections of five units or more.
- **The thresholds are stated lines, not gaps in the data** (§2). A different line moves units on and off the lists.

## 7. Files and rerun

- This page; the data, one row per unit (756), `S100 Strong candidates and the most altered sections - data.csv`; the script, `S100 Strong candidates and the most altered sections - script.py`.
- Inputs, read only, each tested against its md5 by the script: `S98 Ledger of edits and recommendations/line-up/data/records.jsonl` (591a7cc8d07cc376dc324dd725a11579); `S98 Ledger of edits and recommendations/line-up/data/tree.json` (9a4a27438e68a77224c624319afd6b7b); `S98 Ledger of edits and recommendations/group/sentence index of the latest text.jsonl` (fdaf069a0c1d71be4e17b38d2f6bce82); `S98 Ledger of edits and recommendations/group/line maps.json` (0334e1504051e76d5622cdb67a97fde2); `S98 Ledger of edits and recommendations/group/anchor - scripts/step3 side data.json` (c0f85a845fdeff160881b3f57e78bd6e); `S98 Ledger of edits and recommendations/group/anchor - scripts/lib_anchor.py` (bc5411ae431dc51aac5860fd279bf8dc); and the ten theory texts, tested against the md5s the line maps name.
- Rerun from `results/`: `PYTHONDONTWRITEBYTECODE=1 python3 "S100 Strong candidates and the most altered sections - script.py"` (about two minutes).
