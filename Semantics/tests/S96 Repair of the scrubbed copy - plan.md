# S96 Repair of the scrubbed copy - plan

*Log S96, 26 September 2026. Agent 10 of the owner's 15 for this task (decisions S22, S24). Written by `tests/S96 Repair - scripts/plan_build.py` from `replacements.json` beside it, so every change listed here is the change the build applies. Not yet committed. Line numbers are the scrubbed copy's; the repaired copy keeps them, line for line.*

**Input.** `tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md` (log S95, md5 2517ef4ec1f274e8de2bfb7e6661ef94), unchanged. Draft 5 and the change list are unchanged.

**Output.** `tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md`, md5 c1eecbd1587e5aec91fd0ba7d46e1469, built by `tests/S96 Repair - scripts/repair_apply.py`, which refuses unless the input's md5 matches and refuses any span that is missing, occurs more than once on its line, or overlaps another.

**Decisions applied.** S20, S21, S23, S25, and S26 and S27 (recorded in commit da91472, 26 September 2026).

**Counts.** 77 entries (P 21, C 2, G 2, F 2, R 50) and the dated note at l. 2 replaced whole; 14 entries change what a sentence claims. 58 lines differ from the scrubbed copy; both have 632 lines (wc -l). Words: 13427 in the scrubbed copy, 15292 repaired. These counts describe the work; they put no order on anything (S20).

## 1. The reading, against the owner's words

The five points of the reading were compared with the owner's words (a), (b) and (d) in decisions S26 and S27. Where a point goes beyond them:

- **Point 1** (that the thing explained itself fixes whether a candidate meets the requirements, whether or not anyone knows it) is not in the owner's words. It follows from S25 ("It has nothing to do with explanation") as refined by S26, and it restates the relation of the S95 hard case 1, which is still the owner's question. The list of kinds of target in point 1 is Claude's.
- **Point 2(i)**: the owner said "This is correct" of the sentence "Physical possibility comes in only when something is instantiated or transformed", and asked for examples; the list of ways (held, copied, taught, tested, built, performed) comes from Claude's five examples, which the owner answered with footnotes "so your agents aren't led astray", not with a reading of each. **Point 2(ii)** joins "not strictly nothing" to the footnote's "'perpetual motion is impossible' is enough to trigger a conflict"; that these are the only two ways physical possibility enters is Claude's.
- **Point 3**: "responding needs more" and "creative work (Parts X-XI)" are Claude's; the owner says only that the bare claim "is not enough for a creative agent to do anything about it".
- **Point 4**: the owner says a system that must contain the whole explanation first can be designed ("nothing is stopping one") and that this is "a detail that exists outside the process". "The theory must not require it" reads that as: the process the theory describes leaves it out, and the theory does not forbid such a design either. The text says both.
- **Point 5**: the owner's example is a conflict (an explanation that implies perpetual motion), and it is about the world ("you don't have to compare your explanation directly to the world"). The files 93-94 first choice was about a failure found by examining a candidate, that it assumes its own answer. That case is not a conflict between explanations; carrying S27 over to it is Claude's step. It also follows from the owner's definition of argument (S23), which names no records.

## 2. What the repair does, in brief

- **(P)** Draft 5 and the scrubbed copy define a question's range as a subset of "the physically admitted changes" (l. 159, l. 257), fail an account whose contrast "no physically admitted edit realizes" (l. 275), and read conflict through "the relations the adopted physics admits" (l. 315, l. 526); Part XV speaks of a "physically admitted contract" (l. 536, l. 538). The repair puts **the changes the target admits** (Part II's set A of the target organization) where "physically admitted" was: those are the changes the question asks about, in whatever the target is. Conflict between candidates ranges over **relations of the target's components on their footprints**, not over relations a physics admits. Physical possibility stays where a content is instantiated in a carrier or transformed (Parts IV, X to XIII), and it comes back in as the content of claims a candidate can conflict with (C). One sentence at l. 75 says this for the whole text, and l. 461 says it for Part XII.
- **What is kept from the old "adopted physics".** For a physical target, what the target itself is and does still fixes whether a candidate meets (E) (l. 159, l. 317: "fixed by the candidate, the question and its target"). What a physics excludes still bears on two candidates: where a claim excludes every relation that would let both meet (F1), (F2) and (A), they "conflict there given" that claim (l. 315), and that argument lapses with the claim.
- **The worked example at l. 343** (odd-order skew-symmetric matrices) now comes out an account on the new wording, conjunct by conjunct: (F1), (F2) and (A) as before; non-circular dependence at the two contrasts; non-vacuity because Sol_D(1,b_0) is not empty and the target's edits outside the contract (the field arithmetic, the link between determinant and invertibility) are left out by the stated scope; and nothing asks that an edit be physical. Conflict, where a rival is offered, ranges over relations on the matrix organization's footprints, which exist for a mathematical target.
- **A melody or a philosophical claim** can be a target: l. 49 names the edits (a note or chord changed; a premise or a distinction dropped), l. 159 names the kinds of target, and l. 275 says a contrast no one could produce is still a contrast of its question when the target admits the edit.
- **(C)** At the end of the Rivals paragraph (l. 315), a new relation, **conflict with a claim**, beside conflict between rivals, which is kept as it was. A bare claim, including one about what is possible, is enough for a conflict; the conflict is found by argument, with no test; it rules the candidate out for an assessor who can use the argument (on a pair of C), and it does not say which to drop: that is the person's choice (S21), and responding is construction and repair (Parts X, XI).
- **(G)** In Part IX (l. 397), **premises taken as given**: a premise may be a claim tentatively accepted, even with no thought, by someone who holds no explanation of it; nothing in the semantics asks that the person represent the premise's explanation. The gamble is named in the owner's words and not measured. A system that must hold the whole explanation first can be designed; the semantics does not require it. Then **a premise that is the denial**: an argument whose premises include the very denial of what it would rule out rules nothing out; the person may still drop the claim, which is a choice, not a ruling out, and the claim stays not ruled out and any problem stays.
- **(F)** The text now says, at l. 8, l. 317 and l. 397, that an argument need not cite a test, and that a failure found by argument rules a candidate out for whoever can use the argument, on a question about the world as on any other.
- **(R)** Every S95 break, residue item and changed-claim repair is applied, superseded or left to the owner, item by item in section 8.

## 3. Words

The one-word-one-thing rule and the S95 vocabulary are kept. New terms: **conflict with a claim** (l. 315), **premise taken as given** and **a premise that is the denial** (l. 397), and \(X_j(\psi)\) for the S95 \(R_j(\psi)\), R being the repertoire. "Carrier" at l. 51 meant a relation and now says so. "World" as the thing a candidate answers to becomes "target" where it was a definition (l. 41, l. 211, l. 317), since a target need not be physical; l. 11, l. 57 and l. 608 keep "world" in passing. "Admit" keeps its S95 senses, each fixed by its subject: an organization or its target admits edits (Part II); a population admits a survivor (Argument 3); an assessor admits an inference form (Form_j, declared tentative); the semantics admits an operation (l. 608). "Physically admitted" is left only in Part XII, of constructions and variation operators. Every new sentence was run through the S95 residue scan (section 9).

## 4. (P) The physical ties

**The scan.** A program listed every line of the scrubbed copy with physic*, admit*, adopt*, carrier*, instantiat*, possib*/impossib* or task*: 175 words on 81 lines. Most are "admitted" in the organization sense (Part II's admitted edits), which is not physical possibility. The table gives each line's decision: rewritten where physical possibility or an adopted physics defined a question, its range, non-vacuity, a conflict or Part XV's contracts; kept, with which kind, where it concerns instantiation or transformation, the content of a possibility claim, or a sense of "admit" that is not physical.

| line | words in the scrubbed copy | decision |
| --- | --- | --- |
| 11 | admits, admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 15 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 17 | admit, physical | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and (iv) 'physical realization' of explanatory creativity: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 21 | Physics, instantiates | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 31 | physical, physical, instantiates, admitted | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; and 'the contract of admitted changes': organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 39 | admitted, admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 41 | admits | REWRITTEN (P): 'The world' presumes a physical target; the target is whatever is explained (point 1). What stays: population sense: what a selection population contains (Argument 3), not physical possibility |
| 43 | admitted, physical, possible, physically, possible, physics | REWRITTEN (P): Draft 5 answered grievance 4 by making the contract a subset of the physically possible changes, which S25 takes out of explanation; Same universe as the new first sentence: the target's changes, not the physically possible ones; Point 1 of the reading: whether a candidate meets the requirements is fixed by the thing explained itself. What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 45 | physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 49 | admitted, physical | REWRITTEN (P): The task asks that a melody or a philosophical claim could be a target; this grievance is where the text already says an admitted change need not be physical. What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and the statement of where physical possibility enters and where it does not (S25-S27) |
| 51 | carriers | REWRITTEN (P): 'Carrier' is a physically located occurrence (Part IV); here it meant a relation, which the next sentence and Part XI call them |
| 53 | physical, physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 57 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 61 | admits | KEPT: population sense: what a selection population contains (Argument 3), not physical possibility |
| 75 | physical, carrier, physical, possible, adopted, physics, adopt, carrier, carriers, physical, carriers, adopted, physics, physics | REWRITTEN (P): Instantiation stays physical (S25, S26), but 'must be possible under the adopted physics' and 'fixed by the adopted physics' made a tentatively adopted theory the last word; the adopted physics is now a claim an attribution can conflict with (S26 'not strictly nothing', S27); States S25 as refined by S26 and S27 once, in the Commitments, so every later place can point here. What stays: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; the content of a claim about what is possible or impossible (point 2(ii)) (the adopted physics as a claim an attribution can conflict with); the statement of where physical possibility enters and where it does not (S25-S27); 'adopt' in the sense declared at l. 75, to take tentatively |
| 91 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 105 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 109 | admits | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 141 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 159 | physically, admitted, adopted | REWRITTEN (P): The definition of a question's range. What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; the statement of where physical possibility enters and where it does not (S25-S27) (for a physical target, what the target itself is and does); and 'a narrowing adopted': 'adopt' in the sense declared at l. 75, to take tentatively |
| 169 | physically, carrier | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 175 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 177 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 179 | physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 193 | physical, physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 201 | physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 205 | instantiates, physical, admits | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; and 'admits a transport': the organization has one, not physical possibility |
| 211 | carrier, carrier, carrier, carrier | REWRITTEN (P): A theory in error need not be about the physical world (a mathematical structure, a melody). What stays: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 213 | physical, instantiates, physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 223 | admit | REWRITTEN (P): 'The world must admit' tied the contract to what the world allows; surprise needs only a contract larger than the history and an occurring pair outside it, as its definition at l |
| 257 | physically, admitted, physically, admitted | REWRITTEN (P): Non-vacuity defined through physically admitted edits; now through the target's own admitted edits (Part II's A). What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 269 | admitted, admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 275 | physically, admitted | REWRITTEN (P): Draft 5 made a contrast no physical edit realizes a failure of (E). What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 315 | admitted, adopted, physics, admits, admitted | REWRITTEN (P): Conflict read through 'the relations the adopted physics admits' failed the worked example (l. What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; the statement of where physical possibility enters and where it does not (S25-S27) ('does not turn on what any physics admits'); the content of a claim about what is possible or impossible (point 2(ii)) ('perpetual motion is impossible') |
| 317 | admitted, admitted | REWRITTEN (P): Point 1: fixed by the thing explained itself, of whatever kind. What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 325 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 329 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 353 | admitted, admitted, admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 365 | carrier, carrier | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 375 | physical, instantiated | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 393 | admits | KEPT: the assessor admits an inference form (Form_j; the S95 vocabulary's word, declared tentative) |
| 403 | task | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 405 | carriers | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 407 | instantiated | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 409 | carrier | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 411 | physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 425 | admits | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 459 | physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 461 | Tasks, physical, task, Possibility, task, task, physical, adopts, task, physics | REWRITTEN (P): Marks Part XII as the place S25 names, and says what it does not do. What stays: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; the statement of where physical possibility enters and where it does not (S25-S27); and 'adopts': 'adopt' in the sense declared at l. 75, to take tentatively |
| 463 | task | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 469 | admitted, task | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 475 | physically, admitted | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 477 | task | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 479 | physical, admitting, Admit, tasks, physically, tasks, Admit, tasks, possibility, Tasks, Admit, possibility | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 481 | physical, physical, physically, admitted, physical, physics, admit | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 487 | admitted | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 492 | admitted | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 495 | admitted, admitted, task | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 517 | physical, admitted, physical, instantiates | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 520 | admitted, physical | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and 'physical history' of provenance: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 526 | physical, adopted, physics, admits | REWRITTEN (P): Dependence order follows the new conflict definition and adds conflict with a claim. What stays: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII ('physical provenance' of (R)) |
| 528 | physical, physical | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 536 | physically, admitted, admitted | REWRITTEN (P): Part XV's 'physically admitted contract' goes (S25); the rest is S95 B6 (range 2 repair 8). What stays: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 538 | physically, admitted | REWRITTEN (P): 'Physically admitted contract' goes (S25); the rest is S95 B6 (range 2 repair 8), which drops the argued-FOR form |
| 540 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 542 | admits | KEPT: population sense: what a selection population contains (Argument 3), not physical possibility |
| 568 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 572 | physics, admit | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII (the selection population, a physical history) |
| 574 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 576 | admits, possible, physical | KEPT: population sense: what a selection population contains (Argument 3), not physical possibility; and 'a physical relation' that may fix a selected value: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 580 | admits | REWRITTEN (P): Argument 4 needs only H strictly inside C; 'changes the world admits' tied C to what the world allows |
| 590 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 608 | admits | KEPT: 'an operation the semantics admits': the S95 word for draft 5's 'licensed', not physical possibility |
| 612 | carriers | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 620 | admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 626 | admits | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 630 | admits, admitted | KEPT: organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 632 | instantiates | KEPT: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |

**The changes (P).**

- **l. 75** (S25-S27; supersedes nothing). **Claim changed.** Instantiation stays physical (S25, S26), but 'must be possible under the adopted physics' and 'fixed by the adopted physics' made a tentatively adopted theory the last word; the adopted physics is now a claim an attribution can conflict with (S26 'not strictly nothing', S27).
  - old: `` Every attribution of an organization to a physical system must be possible under the adopted physics; here and throughout, to adopt something is to take it tentatively, open to replacement. Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are fixed by the adopted physics, and substrate independence reaches as far as that physics lets contents pass between media. ``
  - new: `` Every attribution of an organization to a physical system is a claim that the system instantiates it, and whether a system can is a matter of physics; here and throughout, to adopt something is to take it tentatively, open to replacement, and an attribution that the adopted physics excludes conflicts with it, as a candidate can conflict with a claim (Part VI). Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are matters of physics as well, and substrate independence reaches as far as contents can pass between media. ``
- **l. 75** (S25-S27 (the one statement of where physics enters)). **Claim changed.** States S25 as refined by S26 and S27 once, in the Commitments, so every later place can point here.
  - old: `` a barrier in the sense of Part XIII. ``
  - new: `` a barrier in the sense of Part XIII. Physical possibility enters the semantics in two ways only: where a content is instantiated in a carrier or transformed, as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), and as the content of claims that a candidate can conflict with (Part VI). It does not define a question, its range of changes, an account or a conflict between candidates (Parts III, V, VI). ``
- **l. 43** (S25; supersedes S95 R7). **Claim changed.** Draft 5 answered grievance 4 by making the contract a subset of the physically possible changes, which S25 takes out of explanation. R7 only renamed 'the physical theory' to 'the adopted physical theory' and is superseded.
  - old: `` The physical theory fixes which changes are possible at all. A contract is a declared subset of those. ``
  - new: `` A contract is a declared subset of the changes its target admits (Part II), which are changes in whatever the target is, a garden, a mathematical structure or a melody, and not only those anyone could carry out. ``
- **l. 43** (S25). Same universe as the new first sentence: the target's changes, not the physically possible ones.
  - old: `` A contract that quietly excludes physically possible changes to protect an account ``
  - new: `` A contract that quietly excludes changes its target admits to protect an account ``
- **l. 43** (S25; supersedes S95 R7). Point 1 of the reading: whether a candidate meets the requirements is fixed by the thing explained itself. R7's 'the world the adopted physics describes' is superseded.
  - old: `` What is independent of the modeller lies in the physics and in fidelity; ``
  - new: `` What is independent of the modeller lies in the target and in fidelity; ``
- **l. 41** (point 1). 'The world' presumes a physical target; the target is whatever is explained (point 1).
  - old: `` turns on the transport and the world alone ``
  - new: `` turns on the transport and the target alone ``
- **l. 49** (S25, point 1). The task asks that a melody or a philosophical claim could be a target; this grievance is where the text already says an admitted change need not be physical.
  - old: `` A mathematical argument explains, relative to a question, when its components respond to those edits as the target structure does (Part VII). ``
  - new: `` A mathematical argument explains, relative to a question, when its components respond to those edits as the target structure does (Part VII). The same goes for a melody, where changing a note or a chord is an edit, and for a philosophical claim, where dropping a premise or a distinction is one. Whether anyone could carry an edit out in a physical system bears on testing and building (Part XII), not on whether a candidate meets (E) at it. ``
- **l. 51** (one word, one thing). 'Carrier' is a physically located occurrence (Part IV); here it meant a relation, which the next sentence and Part XI call them.
  - old: `` get three distinct carriers ``
  - new: `` get three distinct relations ``
- **l. 159** (S25; B-scope finding B2 (L159)). **Claim changed.** The definition of a question's range. It keeps what the theory needed from the old 'adopted physics' (for a physical target, what the target itself does) without letting physical possibility define the range (point 1).
  - old: `` A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one. ``
  - new: `` A contract is a declared subset of the changes its target admits (Part II), and a stated scope is what makes it one. Those are the changes the question asks about, in whatever the target is: a garden, a mathematical structure, a melody or a philosophical claim. For a physical target they are changes in what the target itself is and does; whether anyone could carry a change out, or whether it could come about, is a matter of instantiation and transformation (Part XII), which bears on testing and building and does not by itself put a change in a contract or keep it out. ``
- **l. 223** (S25). 'The world must admit' tied the contract to what the world allows; surprise needs only a contract larger than the history and an occurring pair outside it, as its definition at l. 221 says.
  - old: `` Surprise requires an incomplete selection history: the world must admit changes the system's correspondence was never shaped against (Argument 4). ``
  - new: `` Surprise requires an incomplete selection history: the contract must contain changes the system's correspondence was never shaped against, and one of them must occur (Argument 4). ``
- **l. 257** (S25; B-scope finding B2 (L257)). **Claim changed.** Non-vacuity defined through physically admitted edits; now through the target's own admitted edits (Part II's A).
  - old: `` The contract \(C\) is a declared subset of the physically admitted edits, and every physically admitted edit excluded from \(C\) is excluded by a stated scope, not silently. ``
  - new: `` The contract \(C\) is a declared subset of the edits the target admits, and every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. ``
- **l. 275** (S25; B-scope finding B2 (L275)). **Claim changed.** Draft 5 made a contrast no physical edit realizes a failure of (E). A clash can stand where no test can reach it (S26 context, example 3); what fails is only a contrast outside the target's own edits, and then non-circular dependence, which needs a pair of C with the contrast, is what fails.
  - old: `` An account whose only substantive contrast is one that no physically admitted edit realizes fails non-vacuity by having a silently narrowed contract. ``
  - new: `` An account whose only substantive contrast is one that no edit the target admits realizes has no pair of \(C\) at which the contrast appears, and fails non-circular dependence. A contrast that no one could produce, or that could not come about, is still a contrast of its question when the target admits the edit that realizes it; whether it can be produced bears on testing (Part XII), not on (E). ``
- **l. 315** (S25; B-scope finding B2 (L315); feeds C). **Claim changed.** Conflict read through 'the relations the adopted physics admits' failed the worked example (l. 343) and made physics define conflict. It now ranges over relations on the target's footprints; what a physics excludes comes in as a claim (conflict with a claim, C).
  - old: `` or when each of them could meet (F1), (F2) and (A) there under some relations of the target that the adopted physics admits (Part I) and no such relations let both, as none do when two of their active components with one counterpart have different relations there. ``
  - new: `` or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both, as none do when two of their active components with one counterpart have different relations there. Whether two candidates conflict is fixed by their organizations and transports and by the target's ports and components; it is found by argument, with no test, and it does not turn on what any physics admits (Part I). ``
- **l. 317** (point 1). Point 1: fixed by the thing explained itself, of whatever kind.
  - old: `` fixed by the candidate, the question and the world, ``
  - new: `` fixed by the candidate, the question and its target, ``
- **l. 343** (S25; B-scope finding B2 (L343, the worked example)). Makes the worked example come out an account on the new wording, with both clauses of non-vacuity read.
  - old: `` Non-vacuity is met: any nonzero odd skew matrix is an instance. ``
  - new: `` Non-vacuity is met: any nonzero odd skew matrix is an instance, and the edits the target admits outside the contract, to the field arithmetic and to the link between determinant and invertibility, are left out by the stated scope. No edit here is a physical one, and none needs to be: the contract is a set of changes to the mathematical target (Part III). ``
- **l. 461** (S25-S27, Part XII's role). Marks Part XII as the place S25 names, and says what it does not do.
  - old: `` The physical module adopts a task-based formulation of physics for this purpose. ``
  - new: `` The physical module adopts a task-based formulation of physics for this purpose. It is where physical possibility enters the semantics as instantiation and transformation; the only other way it enters is as the content of claims a candidate can conflict with (Part VI). The module says which organizations a carrier can instantiate, and which transformations of a content, such as holding, copying, teaching, testing, building or performing it, can be carried out. It does not define a question, an account or a conflict between candidates (Parts III, V, VI). ``
- **l. 526** (S25; B-scope finding B2 (L526, dependence order)). **Claim changed.** Dependence order follows the new conflict definition and adds conflict with a claim.
  - old: `` In Part VI, conflict depends on (F1), (F2), (A) and the relations the adopted physics admits, rivals on conflict ``
  - new: `` In Part VI, conflict depends on (F1), (F2), (A) and the target's ports and components (Part II), conflict with a claim on those and on the claim, rivals on conflict ``
- **l. 536** (S25; with B6). **Claim changed.** Part XV's 'physically admitted contract' goes (S25); the rest is S95 B6 (range 2 repair 8).
  - old: `` **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that nonetheless explains nothing. ``
  - new: `` **(A) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks. ``
- **l. 538** (S25; with B6). **Claim changed.** 'Physically admitted contract' goes (S25); the rest is S95 B6 (range 2 repair 8), which drops the argued-FOR form.
  - old: `` **(B) Necessity.** An explanation, argued to be one and not a non-explanation by an argument that does not use (E), whose organization no transport can preserve under any physically admitted contract. ``
  - new: `` **(B) Necessity.** A candidate that an argument not using (E) rules out as a non-explanation, whose organization no transport can preserve under any contract on its target. ``
- **l. 580** (S25). Argument 4 needs only H strictly inside C; 'changes the world admits' tied C to what the world allows.
  - old: `` strictly smaller than the contract \(C\) of changes the world admits. ``
  - new: `` strictly smaller than its contract \(C\). ``
- **l. 211** (point 1). A theory in error need not be about the physical world (a mathematical structure, a melody).
  - old: `` the content's transport to the world fails ``
  - new: `` the content's transport to its target fails ``

## 5. (C) Conflict at the level of explanation

Placed at the end of the Rivals paragraph (l. 315), after "ruled out" and "not ruled out" are defined, since it uses them; the rivals definition is kept word for word except for the P change to its conflict clause and R13. l. 317's list of what the text says of candidates now includes it, and the dependence order (l. 526) gives it a place. What it says, in the theory's vocabulary:
- a candidate conflicts with a claim \(\chi\) at a pair its transport translates when \(\chi\) excludes the candidate's answer there, or every relation of the target's components under which it could meet (F1), (F2) and (A) there;
- \(\chi\) need not be an explanation; a bare claim about what is possible, such as that perpetual motion is impossible, is enough for a conflict;
- the conflict is found by argument, with no test against the target;
- on a pair of \(C\), the argument rules out that the candidate meets (E) for any assessor who can use it (so for whom \(\chi\) is live); outside \(C\) it rules out only what the organization gives there;
- it does not say which to drop: the candidate, \(\chi\), or another premise; which one the person goes on with is the person's choice (Part 0, S21), and using \(\chi\) gives \(\chi\) nothing;
- it is not enough to do anything about it: a response is construction and repair (Parts X, XI), and \(\chi\) alone does not say where the candidate is in error.

- **l. 315** (S27 first footnote; points 2(ii) and 3). **Claim changed.** Point 3: explanations conflict at the level of explanation, found by argument, with no test; a bare claim is enough to trigger a conflict and not enough to do anything about it. Placed where rivals and conflict are defined; the rivals definition is kept. The last sentence keeps what draft 5's 'relations the adopted physics admits' did, as a conflict relative to a claim.
  - old: `` whatever rivals anyone offers. ``
  - new: `` whatever rivals anyone offers. **Conflict with a claim.** A candidate can conflict with a claim as well as with a rival. A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there. \(\chi\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion. Such a conflict is found by argument, with no test against the target: an argument that the candidate gives there what \(\chi\) excludes (Part IX). Where the pair is in \(C\), that argument rules out that the candidate meets (E) for any assessor \(j\) who can use it, and so for whom \(\chi\) is a live premise (K2); outside \(C\) it rules out what the candidate's organization gives there, not its meeting (E) on \(p\). The conflict does not by itself say which to drop, the candidate, \(\chi\) or another premise of the argument: which one the person goes on with is the person's choice (Part 0), and using \(\chi\) as a premise gives \(\chi\) nothing. Nor is the conflict enough to do anything about it: a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI), and \(\chi\) alone does not say where the candidate is in error. Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\): the argument that they conflict uses \(\chi\) as a premise and lapses with it. ``
- **l. 317** (S95 R15 (B4), widened for C). Applies R15 (the old sentence did not agree with its own paragraph) and adds the new relation so the sentence stays exhaustive.
  - old: `` Nothing here counts rivals or orders candidates: of one candidate, the only thing said is whether it is ruled out for an assessor; of two, whether they conflict. ``
  - new: `` Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict; of a candidate and a claim, whether they conflict. ``

## 6. (G) Premises taken as given, and S95 B12 (the range 2 reader's B4) reconsidered

**Premises taken as given** (l. 397, and l. 393 for Live_j). An argument may use a claim tentatively accepted as given by someone who holds no explanation of it. (K2) asks of a premise only that it be live; Live_j is read as "j has not withdrawn d, whether or not j holds an explanation of d". The owner's "costly gamble" is quoted and not measured. A system that must hold the whole explanation first "can be designed", and "the semantics does not require it".

**B12 in this light.** S95 found that stated-assumption leaves let an assessor rule a candidate out by stating that it fails (E), which would dissolve "not ruled out", a problem for p, and S21's choice. The S95 repair ("neither does a stated assumption of the claim, or of a claim that contains it") could catch a premise taken as given, since "perpetual motion is impossible" can be read as containing the denial of a candidate that implies perpetual motion. The repair draws the line elsewhere:
- a **premise taken as given** is used through steps: the argument finds that the candidate gives what the premise excludes. It rules the candidate out for whoever can use it;
- **a premise that is the denial** (alone or joined by "and", read structurally, as non-circular dependence reads identity, not by logical equivalence alone) puts the conclusion among the premises, as "p because p" does. Such an argument rules nothing out for anyone. The same goes for an argument whose record leaf was made from the claim.

**What the theory does with the latter, without forbidding a choice.** It does not count it as ruling out. The person may still drop the claim, "for whatever reason" (Part 0): that is the person's choice (S21), not a ruling out, and the claim stays not ruled out, and a problem it poses stays a problem for that assessor (Part VI). Nothing forbids the choice; the text only declines to call it an argument.

**Arguments 1 to 10** remain arguments: their stated assumptions are hypotheses of conditional claims, and no claim's denial is among their premises.

- **l. 397** (S27 second footnote (point 4); S95 B1 (range 2 repair 12), B12 (range 2 B4, repair 13) reconsidered; F; rename R_j to X_j). **Claim changed.** B1: what a whole argument rules out is defined (results file wording). Rename R_j to X_j, R being the repertoire. F: an argument with no record leaf counts, on a question about the world too, and B12's owner marker is dropped because S27 answers it. G: premises taken as given, not contained, not required; the gamble noted, not measured; the fuller system is outside the process. B12 reconsidered: a premise taken as given is distinguished from a premise that is the very denial; the latter rules nothing out, and the person's choice to drop the claim stays the person's (S21). The watch on 'A record ... does not rule out' (O16) is met by saying 'an argument whose record leaf was made from a claim'.
  - old: `` **Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions. For \(\psi\), \(R_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\). Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\). A record reconstructed from a claim does not rule out that claim's denial. ``
  - new: `` **Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions. Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (\(\operatorname{Form}_j\)), while that form stays admitted. An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below). For \(\psi\), \(X_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\). Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\). An argument need not cite a test: one with no record leaf that finds, by examining a candidate, that it assumes its own answer, or that it gives what a claim excludes (Part VI, conflict with a claim), rules the candidate out for whoever can use it, on a question about the world as on any other. **Premises taken as given.** A premise may be a claim taken as given: tentatively accepted, for whatever reason, even with no thought given to it, by someone who holds no explanation of it. As to its premises, (K2) asks only that they be live for the person using the step; neither it nor anything else in the semantics asks that the person represent (R) a premise's explanation, or any part of it, before using the premise to find an error. Using a claim so is, in the owner's words, "a costly gamble for all creative agents"; without it, "error correction could become impossibly costly to perform". The semantics records the gamble and puts no measure on it. A system can be designed that must hold the whole explanation of a premise before using it; that is a detail outside the process the semantics describes, and the semantics does not require it. **A premise that is the denial.** What a stated premise cannot do is stand in for the steps. An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial. Such an argument's conclusion is among its premises, as in "\(p\) because \(p\)", and it rules nothing out for anyone. A person may still drop the claim, for whatever reason (Part 0): that is the person's choice, not a ruling out, and it leaves the claim not ruled out and any problem it poses as it was (Part VI). A premise taken as given differs from such a premise in that the argument has steps from it to what it rules out: it finds that the candidate gives what the premise excludes. ``
- **l. 393** (S95 B7 (optional readings) and B1 (tentative admitting); G pointer). B7's optional readings of Scope_j and Live_j, applied; Live_j is read so that a premise taken as given is live (G); admitting a form is declared tentative (R1's point, stated where Form_j is).
  - old: `` [Claude's reading; draft 5 names this predicate and does not define it]. ``
  - new: `` [Claude's reading; draft 5 names this predicate and does not define it]. \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it; \(\operatorname{Live}_j(d;u)\): \(j\) has not withdrawn \(d\), whether or not \(j\) holds an explanation of \(d\) [Claude's readings]. Admitting a form, like accepting a claim, is tentative (Part 0). ``

## 7. (F) The first choice of files 93-94

The owner's footnote answers it for conflict: "you don't have to compare your explanation directly to the world". The text says so where it bears: in the definition of argument (l. 8, a pointer), in Problems (l. 317: either kind of problem can be solved with no test, by an argument that rules out that one rival meets (E) on C), and in Part IX (l. 397: an argument with no record leaf rules a candidate out for whoever can use it, "on a question about the world as on any other"). S95's provisional marker (B12) is therefore not added. The extension from conflict to a candidate that assumes its own answer is Claude's (section 1).

- **l. 317** (S27; files 93-94 first choice; point 5). **Claim changed.** A failure found by argument, not by looking at the world, counts, for questions about the world as for others (S27; answers file 93's (c2) and file 94's first question).
  - old: `` and where both meet (E) on \(C\) both are accounts of \(p\). ``
  - new: `` and where both meet (E) on \(C\) both are accounts of \(p\). Either kind of problem can also be solved with no test, by an argument usable by that assessor that rules out that one of the rivals meets (E) on \(C\): one that finds, by examining it, that it assumes its own answer, or that at a pair of \(C\) it gives what a claim the assessor tentatively accepts excludes (conflict with a claim, above; Part IX). ``
- **l. 8** (S27; points 4 and 5 (pointer from the definition of argument)). Points the owner's definition of argument at the two S27 points, where it is defined.
  - old: `` and the semantics never defines accepting by the arguments someone holds. ``
  - new: `` and the semantics never defines accepting by the arguments someone holds. A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX). ``

## 8. (R) The S95 repairs, item by item

| S95 item | where | what happened here |
| --- | --- | --- |
| B1 (whole-argument rule-out undefined) | l. 8, l. 397 | applied: R1 at l. 8 (one clause added to agree with G); the results-file wording at l. 397; R_j renamed X_j |
| B2 (l. 315 and l. 369 disagree) | l. 315, l. 369 | applied: R13, R18 |
| B3 (test solves "for that assessor") | l. 317 | applied: R14 (i) and (ii) |
| B4 (l. 317 last sentence at odds with its paragraph) | l. 317 | applied: R15, widened by C with "of a candidate and a claim, whether they conflict" |
| B5 (l. 277 empty head) | l. 277 | applied: R11 |
| B6 (defeaters and Part XV (A)/(B)) | l. 17, l. 536, l. 538 | applied: the results-file wording (R2 superseded); "physically admitted contract" also removed by P |
| B7 (assessor inputs, Argument 6) | l. 393, l. 522, l. 526, l. 598 | applied, with "admits"; the optional readings of Scope_j and Live_j applied at l. 393, Live_j read for G |
| B8 (route used before defined) | l. 299, l. 307 | applied: R12 |
| B9 (faithful outside its definition) | l. 151, l. 331 | applied: R8, R16 |
| B10 (l. 159 said nothing) | l. 159 | applied: R9 |
| B11 (refused predicate against (EX)) | l. 31, l. 526, l. 600 | applied |
| B12 (stated-assumption leaves; the range 2 reader's B4) | l. 397 | reconsidered under G and F: the owner marker is dropped (S27 answers it); range 2 repair 13 superseded by the premise-that-is-the-denial wording |
| B13 (ProducedBy widened) | l. 441 | applied |
| B14 (tolerance order presumed a chain) | l. 479 | applied |
| B15 (small breaks) | l. 453, 540, 600, 620, 630 | applied |
| residue l. 47, l. 61 (R3) | l. 47, l. 61 | applied |
| residue l. 161 (R4) | l. 161 | applied |
| residue l. 211 (R5) | l. 211 | applied |
| residue: attitude words (R6) | l. 221, 223, 443 | option B applied (mark, not decide); option A is the owner's |
| borderline l. 43 (R7) | l. 43 | superseded by P |
| borderline l. 201 (R10) | l. 201 | applied |
| residue l. 335 (R17) | l. 335 | applied |
| residue l. 461 ("permitted") | l. 461 | applied ("specified") |
| residue l. 495 | l. 495 | applied, extended so that only an argument rules out |
| residue l. 518 (N indefinable) | l. 518 | applied |
| residue l. 526 ("a separate argument") | l. 526 | applied ("a separate definition") |
| residue l. 532 (heading) | l. 532 | applied |
| residue l. 542, l. 544 (reasons-FOR form) | l. 542, l. 544 | applied |
| changed claim l. 25 (R19) | l. 25 | applied |
| changed claim l. 385 | l. 385 | applied |
| changed claim l. 429 | l. 429 | applied |
| changed claim l. 568 and l. 317 (repair 22) | l. 568, l. 317 | applied at both |
| changed claim l. 592 (repair 21) | l. 592 | applied |
| optional clarity l. 305, l. 311 | l. 305, l. 311 | applied |
| optional l. 403 (repair 18) | l. 403 | not applied (see below) |
| optional l. 455 (repair 23, worth) | l. 455 | not applied: the owner's question 4 |
| watch l. 522 ("any function that orders explanations") | l. 522 | a watch, no repair proposed; unchanged |
| watch l. 526 ("defined only by its own construction") | l. 526 | a watch, no repair proposed; unchanged |
| watch l. 397 ("A record ... does not rule out", O16) | l. 397 | met: "an argument whose record leaf was made from a claim" |
| hard case 1 | l. 67, l. 317 | the owner's question 1; the relation is kept, now "fixed by the candidate, the question and its target" |

**Not applied, or superseded, with the reason.**

- **R2 (l. 17)**: superseded by B6's l. 17 wording, which the results file chose (section 7, B6).
- **R7 (l. 43)**: superseded by P at l. 43: the contract is no longer a subset of what any physics says is possible.
- **range 2 repair 4 (l. 393, Form_j as 'tentatively accepts')**: superseded by B1's choice of 'admits', declared tentative (results file, B1).
- **range 2 repair 14 with 'tentatively accepts'**: applied with 'admits' instead, per B1.
- **B12's marker (the owner's open question on arguments with no record leaf)**: superseded by F: decision S27 answers it; l. 397 now says such an argument counts, on a question about the world as on any other.
- **range 2 repair 13 (l. 397, 'neither does a stated assumption of the claim, or of a claim that contains it')**: superseded by G: 'a claim that contains it' could catch a premise taken as given such as 'perpetual motion is impossible'; the new wording names the premise that is the denial, alone or joined by 'and', read structurally.
- **R6 option A (rename surprise and recognized difficulty)**: the owner's call (S95 question 3); option B, which marks and does not decide, is applied.
- **range 2 repair 18, optional (l. 403, 'a theory that is not an account of its question')**: not applied: l. 211 uses 'a theory in error' for the same idea, and one idea keeps one wording.
- **range 2 repair 23, optional (l. 455, worth)**: the owner's call (S95 question 4).
- **hard case 1 (the assessor-free 'meets (E)')**: the owner's call (S95 question 1); the text keeps the relation, now said to be fixed by the candidate, the question and its target.

**The changes (R).**

- **l. 8** (B1 (R1)). B1: Part 0's step clause now points at a definition Part IX gives; admitting a form is tentative; a claim whose denial is ruled out gets nothing more. One clause added to R1 ('and the claim's denial is not one of its premises'), to agree with G at l. 397.
  - old: `` Each of its steps rules out the case in which the step's premises are met and its conclusion fails (Part IX). An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2); a claim that no argument rules out is only not ruled out, and gets nothing from that. ``
  - new: `` Each of its steps is of an inference form that the person using it admits (\(\operatorname{Form}_j\), Part IX), and admitting a form, like accepting a claim, is tentative; for that person, while the form stays admitted, the step rules out the case in which its premises are met and its conclusion fails. An argument rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not one of its premises (Part IX). An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2). A claim that no argument rules out is only not ruled out, and gets nothing from that; a claim whose denial an argument rules out gets nothing more than that ruling out. ``
- **l. 17** (B6 (results file wording; supersedes R2)). **Claim changed.** B6: the defeaters rested on the bare 'explains nothing', the predicate l. 31 refuses, and a case, not an argument, ruled out.
  - old: `` An explanatory achievement that these four cannot represent would rule out the conjecture; so would a candidate that meets all four and explains nothing. Part XV lists what would rule it out. ``
  - new: `` A candidate that an argument not using these four rules out as a non-explanation of its question, and that these four cannot represent, would conflict with the conjecture; so would a candidate that meets all four and that such an argument rules out as an explanation on its question and contract. An argument that exhibits either rules the conjecture out for whoever can use it, while it stays usable. Part XV lists what such an argument would have to exhibit. ``
- **l. 25** (R19). R19: 'attribution' is the vocabulary's word.
  - old: `` It does not divide an achievement among contributors beyond what a history contains (Part XI). ``
  - new: `` It does not attribute an achievement to contributors beyond what a history contains (Part XI). ``
- **l. 31** (B11). B11: the refused predicate collided with the defined (EX).
  - old: `` No predicate that says "explains" without a question and a contract, or "is a cause", or "is a created explanation", is taken as an import, and no definition depends on one (Argument 6). ``
  - new: `` No undefined predicate that says "explains" without a question and a contract, or "is a cause", is taken as an import, and no definition depends on one (Argument 6); (EX) is a defined relation of an episode, not such a predicate. ``
- **l. 47** (R3). R3: 'forbids', on the S95 residue list, and a rule-out with no argument.
  - old: `` Nothing about construction is reduced to selection; Part IV forbids the reduction and Part XV names what would rule it out. ``
  - new: `` Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out. ``
- **l. 61** (R3). R3: only an argument rules out.
  - old: `` are stated exactly in Part XV together with what would rule out each. ``
  - new: `` are stated exactly in Part XV together with what an argument would have to exhibit to rule out each. ``
- **l. 151** (B9 (R8)). B9: 'faithful' is defined for transports only.
  - old: `` A measure that identifies an outcome, with a prediction from it that is faithful on the contract, answers the identification question; ``
  - new: `` A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; ``
- **l. 159** (B10 (R9)). B10: the old reading said nothing, the question asked having the restricted contract.
  - old: `` Meeting the conditions of an account (Part V) on the restricted contract leaves open whether the restriction drops changes the question asked contains. ``
  - new: `` Meeting the conditions of an account (Part V) on the restricted contract leaves open why the claim is made on this restriction and not on a wider one. ``
- **l. 161** (R4). R4: 'prohibited' is on the S95 residue list.
  - old: `` What is prohibited is changing \(C\) or \(\mathcal Q\) during an assessment without recording that the claim has changed. ``
  - new: `` An assessment is an event with a frozen contract (Part 0, grievance 10): a change to \(C\) or \(\mathcal Q\) during it, left unrecorded, makes the record name a claim other than the one assessed. ``
- **l. 201** (R10). R10: an unargued claim about frequency.
  - old: `` that is the usual arrangement, not a requirement. ``
  - new: `` that is one arrangement, not a requirement. ``
- **l. 211** (R5). R5: an independent second trace, on the S95 residue list.
  - old: `` and a later record made from the carrier is not a second, independent trace of its history. ``
  - new: `` and a later record made from the carrier carries that provenance, not a second, independent one. ``
- **l. 221** (R6 option B (owner question 3 still open)). R6: option B, which marks and does not decide; option A (renaming) is the owner's call.
  - old: `` - **surprise** is a violation of a selected transport at \((a,b)\notin H\). ``
  - new: `` - **surprise** is a violation of a selected transport at \((a,b)\notin H\) (the name is provisional; see the marker in Part XI). ``
- **l. 223** (R6 option B). R6 option B for 'recognized difficulty' at its first use.
  - old: `` a violation the system represents can be a recognized difficulty (Part X). ``
  - new: `` a violation the system represents can be a recognized difficulty (Part X; the name is provisional, as in Part XI). ``
- **l. 277** (B5 (R11)). B5: the first sentence had an empty head.
  - old: `` (E) does not exclude a mechanism that meets (E) whatever led anyone to guess it; how it came to be taken up is assessed elsewhere (Part IX). ``
  - new: `` (E) has no condition on how a mechanism came to be guessed: a mechanism meets (E) or fails it whatever led anyone to guess it, and how it came to be taken up is assessed elsewhere (Part IX). ``
- **l. 299** (B8 (R12)). B8: 'route' used before it is defined.
  - old: `` Criticality is relative to the route \(W\) it is assessed in: ``
  - new: `` Criticality is relative to the route \(W\) it is assessed in, a **route** of the candidate being a member of \(\mathsf S_{E,p}\) (not an active route of a history, Part IX): ``
- **l. 305** (range 1 optional clarity). Optional clarity, no change of claim; applied.
  - old: `` Deletion of \(d\) from \(\Gamma\) leaves a route exactly when a minimal route omits \(d\). ``
  - new: `` Deletion of \(d\) from \(\Gamma\) leaves \(\Gamma\setminus\{d\}\) a route exactly when a minimal route omits \(d\). ``
- **l. 307** (B8 (R12)). B8: the definition now sits at l. 299.
  - old: `` Here a route of the candidate is a member of \(\mathsf S\), and is a route whether or not any history runs it; ``
  - new: `` A route of the candidate is a route whether or not any history runs it; ``
- **l. 311** (range 1 optional clarity). Optional clarity, no change of claim; applied.
  - old: `` no minimal route and no singleton instance exists ``
  - new: `` no minimal route, and no route of one commitment, exists ``
- **l. 315** (B2 (R13)). B2: 'ruled out' defined for claims, so l. 369 can apply it to an answer.
  - old: `` A candidate is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules out that the candidate meets (E); ``
  - new: `` A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is; ``
- **l. 317** (B3 (R14, kind i)). B3: the test must solve the problem for that assessor.
  - old: `` is a **test** that solves the problem whatever it records, since an argument from what it records rules out at least one of them for as long as that argument stays usable; an answer it rules out stays ruled out on \(p\) for as long as the argument that rules it out stays usable (Part VIII). ``
  - new: `` is a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live for that assessor (K2, K3): an argument from what it records then rules out at least one of them for that assessor, while it stays usable; an answer that such an argument rules out stays ruled out on \(p\) for as long as the argument stays usable (Part VIII). ``
- **l. 317** (B3 (R14, kind ii)). B3/residue: only an argument rules out, not a test.
  - old: `` a test inside \(C\) can rule out one of them without the other only for a failure of its own; ``
  - new: `` an argument from a test inside \(C\) can rule out one of them without the other only for a failure of its own; ``
- **l. 317** (range 2 repair 22 (l. 317 side)). The contrastive restatement no longer follows by definition (changed-claims list, l. 317 and 568).
  - old: `` as a claim that one assignment of counterparts, and not the other, is the target's must (Argument 2, Consequence). ``
  - new: `` as a claim that the target pairs its components one way and not the other must (Argument 2, Consequence). ``
- **l. 331** (B9 (R16)). B9: 'faithful' outside its definition.
  - old: `` it is circular, though its content might be faithful on the contract. ``
  - new: `` it is circular, though the value it sets might be the target's. ``
- **l. 335** (R17). R17: 'rule out' with no argument.
  - old: `` permitting division changes the state space and does not rule out the scoped result. ``
  - new: `` permitting division changes the state space and makes a new question (Part III); the scoped result on its own question is as it was. ``
- **l. 369** (B2 (R18)). B2: l. 315 and l. 369 agree, and the step from y to the candidates goes through (A).
  - old: `` Here "ruled out" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out \(y\) as the target's answer at \((a,b)\), and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses. ``
  - new: `` Here "ruled out" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out the claim that \(y\) is the target's answer at \((a,b)\); joined to a candidate's own answer \(y\) there and to (A), it rules out that the candidate meets (E); and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses. ``
- **l. 385** (range 2 repair 19). Changed claim: 'gives it no bearing' read as taking bearing away.
  - old: `` Using an objection gives it no bearing (K1) and makes no argument from it usable (K2). ``
  - new: `` Using an objection does not give it bearing (K1) or make any argument from it usable (K2). ``
- **l. 429** (range 2 repair 20). Changed claim: read as saying arguments play no part, against S21.
  - old: `` Closing an episode is a choice, not an argument. ``
  - new: `` Closing an episode is a choice: an argument can rule out some ways of closing it, but no argument makes the choice. ``
- **l. 441** (B13 (range 2 repair 11)). B13: widened attribution, against l. 307.
  - old: `` it attributes the repair to each contribution the history contains, and where two sufficient contributions both ran, ``
  - new: `` it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, ``
- **l. 443** (R6 option B (the marker)). R6: 'recognized' was marked nowhere.
  - old: `` as are "understanding" (Part X) and "surprise" (Part IV); ``
  - new: `` as are "understanding" (Part X), "surprise" (Part IV) and "recognized difficulty" (Parts IV, X); ``
- **l. 453** (B15 (range 2 repair 17)). B15: 'its' had no clear referent.
  - old: `` A later narrowing of that contract to rescue its meeting (E) ``
  - new: `` A later narrowing of that contract to rescue \(c\)'s meeting (E) ``
- **l. 461** (residue (range 2 repair 7)). Residue ('permitted'); with 'specified' a task can be possible or impossible, as Admit and Poss require.
  - old: `` a task a permitted input-to-output attribute transformation ``
  - new: `` a task a specified input-to-output attribute transformation ``
- **l. 479** (B14 (range 2 repair 15)). B14: the order presumed a chain.
  - old: `` each admitting no performance the one before it excludes, and short of exact; ``
  - new: `` in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact; ``
- **l. 495** (range 2 repair 1, extended). Repair 1 kept 'one bypass rules out', a rule-out with no argument; extended so only an argument rules out (the vocabulary's one sense).
  - old: `` A finite list of failures is not an argument that no bypass exists; one bypass rules out a proposed barrier. ``
  - new: `` A finite list of failures does not rule out a bypass; an argument that exhibits one bypass rules out a proposed barrier for whoever can use it. ``
- **l. 518** (residue (range 2 repair 5)). Residue: the old wording said N cannot be defined.
  - old: `` It is taken as an input and never defined in terms of anything else; ``
  - new: `` It is taken as an input and the semantics does not define it; ``
- **l. 522** (B7 (with 'admits', per B1)). B7: the assessor's inputs are declared, closing the gap in Argument 6.
  - old: `` the system boundary and continuity of an attribution (Part XII); ``
  - new: `` the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) has not withdrawn (K2, Part IX); ``
- **l. 526** (B7). B7: (K2) and (K3) take their place in the order.
  - old: `` (K1) depends on (E). ``
  - new: `` (K1) depends on (E). (K2) depends on the assessor's declared inputs (Part XIV, above); (K3) on (K2). ``
- **l. 526** (B11 (range 2 repair 10)). B11.
  - old: `` Nothing depends on a predicate that says "explains" without a question and a contract, or "is a cause," or "is a created explanation." ``
  - new: `` Nothing depends on an undefined predicate that says "explains" without a question and a contract, or "is a cause"; (EX) is a defined relation of an episode, not such a predicate. ``
- **l. 526** (residue (range 2 repair 9)). A definition's job is meant; 'an argument that X' was the reasons-FOR form.
  - old: `` and a separate argument that would supply it is part of the account only when the account uses it. ``
  - new: `` and a separate definition that would supply it is part of the account only when the account uses it. ``
- **l. 532** (residue (range 2 repair 6)). The heading's 'defeats' is on the S95 residue list.
  - old: `` # Part XV — What defeats this class ``
  - new: `` # Part XV — What would rule this class out ``
- **l. 536** (B6 (range 2 repair 8, end of (A))). B6.
  - old: `` it is a counterexample only if it fails none of the four and still explains nothing. ``
  - new: `` it is a counterexample only if it fails none of the four and such an argument rules it out as an explanation. ``
- **l. 540** (B15 (range 2 repair 17)). B15: claims are ruled out, arguments are not.
  - old: `` Such a case would rule out Argument 1 and make correspondence an import again. ``
  - new: `` Such a case would rule out the Claim of Argument 1 and make correspondence an import again. ``
- **l. 542** (residue (range 2 repair 2)). 'An argument that X', the reasons-FOR form.
  - old: `` ; an argument that every construction trace can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that the object layer of Part IV is not what explanation operates on. ``
  - new: `` ; a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV. ``
- **l. 544** (residue (range 2 repair 3)). 'An argument that X', the reasons-FOR form.
  - old: `` **(E) Question-finding.** An argument that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, either trivializes creativity or fails to capture some case of finding a new question (against Argument 5). ``
  - new: `` **(E) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5). ``
- **l. 568** (range 2 repair 22). The contrastive restatement no longer follows by definition.
  - old: `` a claim that one assignment, and not the other, is the target's is a claim that some admitted change separates them, and must supply it. ``
  - new: `` a claim that the target pairs its components one way and not the other is a claim that some admitted change separates them, and must supply it. ``
- **l. 592** (range 2 repair 21). 'Finding' must mean owned construction, as (G) has it.
  - old: `` Finding a new question is a creative act, as answering one is. ``
  - new: `` Finding a new question, by an owned construction (G), is a creative act, as answering one is. ``
- **l. 598** (B7). B7: the walk back never reached (O) and (Q).
  - old: `` following each definition back until it reaches the imports, the indices or the declared inputs. ``
  - new: `` following each definition back until it reaches the imports, the indices, the declared inputs, or (O) and (Q), which depend on nothing. ``
- **l. 600** (B11 (range 2 repair 10)). B11.
  - old: `` There is no residual predicate meaning "explains," "represents," "is a cause," or "is a created explanation." ``
  - new: `` There is no residual, undefined predicate meaning "explains," "represents," or "is a cause"; (EX) is defined (Part XI). ``
- **l. 600** (B15 (range 2 repair 17)). B15.
  - old: `` Neither is a predicate about explanation taken as an import. ``
  - new: `` Neither is a predicate about explanation. ``
- **l. 620** (B15 (range 2 repair 16)). B15: article.
  - old: `` Stipulate a object layer ``
  - new: `` Stipulate an object layer ``
- **l. 630** (B15 (range 2 repair 16)). B15: a category slip, a contract contains changes.
  - old: `` That is not a defect of \(S_1\); it is what the contract contains: identity, at this grain, is exhausted by trajectory. ``
  - new: `` That is not a defect of \(S_1\): the contract contains no change that separates the two things except by their trajectories, so identity, at this grain, is exhausted by trajectory. ``

## 9. The build and the scans

- `python3 "tests/S96 Repair - scripts/replacements_source.py"` compares every span with the scrubbed copy and writes `replacements.json`; `python3 "tests/S96 Repair - scripts/repair_apply.py" --scan --physical` builds the repaired copy and runs both scans; this plan is written by `plan_build.py`.
- **md5** of the repaired copy: c1eecbd1587e5aec91fd0ba7d46e1469.
- **The S95 residue scan** (the families and `scan()` of `tests/S95 Scrub - scripts/scrub_apply.py`, imported unchanged), with S95's BORDERLINE notes and 10 S96 notes: 63 hits, 63 noted BORDERLINE, **0 unexplained**. By family: {'accept': 10, 'hold': 13, 'logical joint': 8, 'more/less + adjective': 1, 'real/reality': 3, 'adopt': 4, 'surprise': 14, 'progress/advance/elegant/appropriate': 2, 'correct': 2, 'understand': 5, 'show': 1}. The S96 notes cover a tentative "accept" (S23), "hold" as possession, and the owner's quoted "error correction". Stale S95 notes, for words the repair removed: l. 75 'adopted', l. 315 'adopted', l. 461 'permitted', l. 526 'adopted'.
- The owner's own list (fit, support, verif-, corroborat-, prove, proof, disprove, reason to, belief, better, worse, true, truth, establish, authority, foundation, derive, derivation) finds, by program, nothing in the repaired copy.

**Every remaining physical-tie word, with why it stays** (186 words on 79 lines):

| line | words in the repaired copy | why it stays |
| --- | --- | --- |
| 2 | physical, possibility, instantiated | the dated note, saying what the repair did with physical possibility |
| 8 | admits, admitting, admitted | the assessor admits an inference form (Form_j; the S95 vocabulary's word, declared tentative) |
| 11 | admits, admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 15 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 17 | admit, physical | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and (iv) 'physical realization' of explanatory creativity: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 21 | Physics, instantiates | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 31 | physical, physical, instantiates, admitted | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; and 'the contract of admitted changes': organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 39 | admitted, admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 41 | admits | population sense: what a selection population contains (Argument 3), not physical possibility |
| 43 | admitted, admits, admits | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 45 | physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 49 | admitted, physical, physical | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and the statement of where physical possibility enters and where it does not (S25-S27) |
| 53 | physical, physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 57 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 61 | admits | population sense: what a selection population contains (Argument 3), not physical possibility |
| 75 | physical, carrier, physical, instantiates, physics, adopt, adopted, physics, carrier, carriers, physical, carriers, physics, Physical, possibility, instantiated, carrier | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; the content of a claim about what is possible or impossible (point 2(ii)) (the adopted physics as a claim an attribution can conflict with); the statement of where physical possibility enters and where it does not (S25-S27); 'adopt' in the sense declared at l. 75, to take tentatively |
| 91 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 105 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 109 | admits | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 141 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 159 | admits, physical, instantiation, adopted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; the statement of where physical possibility enters and where it does not (S25-S27) (for a physical target, what the target itself is and does); and 'a narrowing adopted': 'adopt' in the sense declared at l. 75, to take tentatively |
| 169 | physically, carrier | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 175 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 177 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 179 | physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 193 | physical, physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 201 | physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 205 | instantiates, physical, admits | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; and 'admits a transport': the organization has one, not physical possibility |
| 211 | carrier, carrier, carrier, carrier | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 213 | physical, instantiates, physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 257 | admits, admits | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 269 | admitted, admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 275 | admits, admits | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 315 | admitted, physics, admits, admitted, admitted, possible, impossible, impossible | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; the statement of where physical possibility enters and where it does not (S25-S27) ('does not turn on what any physics admits'); the content of a claim about what is possible or impossible (point 2(ii)) ('perpetual motion is impossible') |
| 317 | admitted, admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 325 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 329 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 343 | admits, physical | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and the statement of where physical possibility enters and where it does not (S25-S27) ('No edit here is a physical one') |
| 353 | admitted, admitted, admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 365 | carrier, carrier | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 375 | physical, instantiated | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 393 | admits, Admitting | the assessor admits an inference form (Form_j; the S95 vocabulary's word, declared tentative) |
| 397 | admits, admitted, impossibly | the assessor admits an inference form (Form_j; the S95 vocabulary's word, declared tentative); and 'impossibly costly' is the owner's quoted words about cost, not physical possibility |
| 403 | task | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 405 | carriers | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 407 | instantiated | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 409 | carrier | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 411 | physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 425 | admits | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 459 | physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 461 | Tasks, physical, task, Possibility, task, task, physical, adopts, task, physics, physical, possibility, instantiation, carrier, instantiate | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII; the statement of where physical possibility enters and where it does not (S25-S27); and 'adopts': 'adopt' in the sense declared at l. 75, to take tentatively |
| 463 | task | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 469 | admitted, task | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 475 | physically, admitted | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 477 | task | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 479 | physical, admits, Admit, tasks, physically, tasks, Admit, tasks, possibility, Tasks, Admit, possibility | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 481 | physical, physical, physically, admitted, physical, physics, admit | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 487 | admitted | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 492 | admitted | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 495 | admitted, admitted, task | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 517 | physical, admitted, physical, instantiates | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 520 | admitted, physical | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility; and 'physical history' of provenance: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 522 | admits | the assessor admits an inference form (Form_j; the S95 vocabulary's word, declared tentative) |
| 526 | physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII ('physical provenance' of (R)) |
| 528 | physical, physical | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 536 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 540 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 542 | admits | population sense: what a selection population contains (Argument 3), not physical possibility |
| 568 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 572 | physics, admit | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII (the selection population, a physical history) |
| 574 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 576 | admits, possible, physical | population sense: what a selection population contains (Argument 3), not physical possibility; and 'a physical relation' that may fix a selected value: instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 590 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 608 | admits | 'an operation the semantics admits': the S95 word for draft 5's 'licensed', not physical possibility |
| 612 | carriers | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |
| 620 | admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 626 | admits | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 630 | admits, admitted | organization sense: the edits an organization or its target admits (Part II's A), not physical possibility |
| 632 | instantiates | instantiation or transformation (point 2(i)): a carrier, an occurrence, a physical history, a capability, Part XII |

**Every remaining physic*, admitted or adopted, in short:** l. 2 physical; l. 8 admitted; l. 11 admitted; l. 15 admitted; l. 17 physical; l. 21 Physics; l. 31 physical, physical, admitted; l. 39 admitted, admitted; l. 43 admitted; l. 45 physical; l. 49 admitted, physical, physical; l. 53 physical, physical; l. 57 admitted; l. 75 physical, physical, physics, adopted, physics, physical, physics, Physical; l. 91 admitted; l. 105 admitted; l. 141 admitted; l. 159 physical, adopted; l. 169 physically; l. 175 admitted; l. 177 admitted; l. 179 physical; l. 193 physical, physical; l. 201 physical; l. 205 physical; l. 213 physical, physical; l. 269 admitted, admitted; l. 315 admitted, physics, admitted, admitted; l. 317 admitted, admitted; l. 325 admitted; l. 329 admitted; l. 343 physical; l. 353 admitted, admitted, admitted; l. 375 physical; l. 397 admitted; l. 411 physical; l. 459 physical; l. 461 physical, physical, physics, physical; l. 469 admitted; l. 475 physically, admitted; l. 479 physical, physically; l. 481 physical, physical, physically, admitted, physical, physics; l. 487 admitted; l. 492 admitted; l. 495 admitted, admitted; l. 517 physical, admitted, physical; l. 520 admitted, physical; l. 526 physical; l. 528 physical, physical; l. 536 admitted; l. 540 admitted; l. 568 admitted; l. 572 physics; l. 574 admitted; l. 576 physical; l. 590 admitted; l. 620 admitted; l. 630 admitted.

## 10. Open points

1. **Point 1 and hard case 1.** The text keeps the assessor-free relation "a candidate meets (E) on C or fails it", now "fixed by the candidate, the question and its target". That is still the owner's question 1 of S95; S26 and S27 do not answer it.
2. **A premise that is the denial, taken as given.** If someone takes "this candidate is in error" as given, on another's say-so, the repair counts it as a choice to drop the candidate, not a ruling out, because no step leads from it to what it excludes. Whether the owner means S27's "accepted it as a given" to reach that far is open.
3. **Circularity found by examination** (a candidate that assumes its own answer) is carried over from S27's conflict case by Claude (section 1).
4. **"Only two ways in."** l. 75 and l. 461 say physical possibility enters in two ways only. The owner said "not strictly nothing" and gave the perpetual-motion claim; "only" is Claude's.
5. **Relations on footprints.** Conflict between candidates now ranges over every relation on the target's component footprints. Two candidates that only a physically excluded arrangement would let both meet the conditions no longer conflict outright; they conflict given the claim that excludes it. This is intended (S25), and it narrows outright conflict.
6. **R6 option A, worth, the critics' words, "knowledge"** (S95 questions 3 to 5) stay the owner's.
7. **Nothing here has been read by a second reader** or by Atria or Mimo; the repaired copy is an experiment, not yet a draft of file 13.

## 11. Stage 2: the two readers' repairs

The two readings (`results/S96 Check of the repaired copy - whole text.md`, W, and `results/S96 Check of the repaired copy - cases.md`, K) read the stage-1 text described above (md5 c1eecbd1587e5aec91fd0ba7d46e1469). Their repairs are written once in `replacements_stage2_source.py`, which writes `replacements_stage2.json`; `repair_apply.py` applies them to the stage-1 text by the same rules and writes the final text. The Output line and section 8 above give the stage-1 figures; the final text's are here.

- **Final text:** `tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md`, md5 8bb4d19d5aad53de2492b2193fd23ff1.
- **Stage 2:** 28 entries (W 26, K 1, the dated note 1); 9 change what a sentence claims; 17 lines differ from the stage-1 text, 60 from the scrubbed copy; 632 lines, none added or removed. Words: 15979.
- **Not applied or not text:** 5 items, below.

### Applied

- **l. 2** (N the dated note, Claude's). The note says how the text was made; it now names the second stage and the two readings.
  - old: `` with the S96 repairs applied, made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` beside it), ``
  - new: `` with the S96 repairs applied in two stages, the second after two readings of the first (`results/S96 Check of the repaired copy - whole text.md` and `- cases.md`), made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` and `replacements_stage2.json` beside it), ``
- **l. 8** (W R-6, adapted). l. 8 and l. 397 said the denial block two ways; l. 8 now points to l. 397's structural reading. Worded without the reader's doubled '(Part IX)'.
  - old: `` and the claim's denial is not one of its premises (Part IX). ``
  - new: `` and the claim's denial is not among its premises, in the structural sense of Part IX. ``
- **l. 49** (W B-5, as worded). (E) is defined on a contract, not at an edit.
  - old: `` not on whether a candidate meets (E) at it. ``
  - new: `` not on whether a candidate meets (F1), (F2) and (A) there, or (E) on a contract that contains it. ``
- **l. 55** (W R-3, as worded). Ruling out is always for someone who can use the argument (l. 8, S23).
  - old: `` Argument 7 rules out a conflict between them. ``
  - new: `` Argument 7 rules out a conflict between them, for whoever can use it. ``
- **l. 75** (W P-2, adapted). **Claim changed.** Without this, an attribution to the Earth and Sun whose organization admits 'axis upright' would conflict with physics, and physical possibility would bound a physical target's range again, through the attribution (S25). The reader's '(Part III)' widened to Parts II and III: admitted edits are Part II's, contracts Part III's.
  - old: `` as a candidate can conflict with a claim (Part VI). ``
  - new: `` as a candidate can conflict with a claim (Part VI). That an organization admits an edit is not a claim that the edit can be carried out or can come about, so an attribution does not conflict with a physics that excludes carrying out an edit the attributed organization admits (Parts II and III). ``
- **l. 75** (W O-1, as worded). **Claim changed.** 'In two ways only' was Claude's: the owner wrote 'This is correct.' of the instantiation sentence (S26) and added the content of claims (S27), and closed no list. The list of ways stays, introduced by 'as when', as illustration.
  - old: `` Physical possibility enters the semantics in two ways only: where a content is instantiated in a carrier or transformed, as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), and as the content of claims that a candidate can conflict with (Part VI). ``
  - new: `` Physical possibility enters the semantics where a content is instantiated in a carrier or transformed, as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), and it also enters as the content of claims that a candidate can conflict with (Part VI). ``
- **l. 159** (W P-2, adapted). **Claim changed.** Same gap as at l. 75, closed where the range is defined: the target's own admitted edits, not the edits physics lets anyone carry out. '(Part I)' in the reader's wording changed to Part II, where admitted edits are defined.
  - old: `` For a physical target they are changes in what the target itself is and does; ``
  - new: `` For a physical target they are changes in what the target itself is and does, as its attributed organization admits them (Part II), and admitting a change is not a claim that it can be carried out or come about; ``
- **l. 275** (W B-6, as worded). An account meets (E) by definition, so 'an account ... fails' contradicted itself.
  - old: `` An account whose only substantive contrast ``
  - new: `` A candidate whose only substantive contrast ``
- **l. 315** (W R-1, as worded). 'An argument that X' is a reasons-for form (S23); an argument rules out.
  - old: `` an argument that the candidate gives there what \(\chi\) excludes (Part IX). ``
  - new: `` an argument that rules out, for whoever can use it, that what the candidate gives there is something \(\chi\) allows (Part IX). ``
- **l. 315** (W B-1, as worded). Goes with the new reading of Live_j at l. 393: a premise is live for j only if j has taken it up.
  - old: `` and so for whom \(\chi\) is a live premise (K2) ``
  - new: `` and so who tentatively accepts \(\chi\) (K2) ``
- **l. 315** (W B-7 and P-1, B-7 as worded; P-1 adapted). **Claim changed.** B-7: what the candidate gives is a matter of the candidate; what is ruled out is that the target gives it. P-1: without the premise, 'perpetual motion is impossible' would rule out every candidate for a question about an edit no one could carry out, which S25 forbids. Adapted: the reader also narrowed the definition of conflict with a claim; that part is not applied (see not applied), and the missing premise is named where the ruling out is, so the owner's 'that's a conflict' stands.
  - old: `` outside \(C\) it rules out what the candidate's organization gives there, not its meeting (E) on \(p\). ``
  - new: `` outside \(C\) it rules out that the target gives there what the candidate's organization gives, not the candidate's meeting (E) on \(p\). Either way the argument needs the premise that \(\chi\) speaks of the target under that pair's edit. Where the edit is itself one that \(\chi\) excludes, as when a question asks what a pendulum does with its friction component deleted, the target so edited may itself give a motion that never stops, and without that premise the argument rules out no candidate there; the candidate still conflicts with \(\chi\). ``
- **l. 315** (W O-6, adapted). **Claim changed.** The owner: a bare claim is 'enough to trigger a conflict', and an agent 'uses it to identify flaws'. Without this, a represented conflict with a claim could not be a recognized difficulty (l. 429 names aims only). Worded like the last sentence of l. 317 rather than the reader's 'keeping both'. Recognizing a difficulty is not yet a response, so 'not enough ... to do anything about it' stands.
  - old: `` and \(\chi\) alone does not say where the candidate is in error. ``
  - new: `` and \(\chi\) alone does not say where the candidate is in error. A conflict with a claim that a system represents can be a recognized difficulty (Part X), as when keeping the candidate meets a claimed aim only by dropping the claim, where keeping the claim is among the protected aims (Part XI). ``
- **l. 315** (W R-1 and B-2, R-1 as worded; B-2 adapted). **Claim changed.** R-1: the second reasons-for form. B-2: 'conflict given chi' was defined and used nowhere; now two such candidates pose a problem for an assessor who tentatively accepts chi. The reader's clause on which kind of problem is left out: the kinds follow from where the rivals conflict (l. 317), and the clause was in error when they conflict given chi both inside and outside C.
  - old: `` conflict there given \(\chi\): the argument that they conflict uses \(\chi\) as a premise and lapses with it. ``
  - new: `` conflict there given \(\chi\): an argument that rules out their both meeting (F1), (F2) and (A) there uses \(\chi\) as a premise and lapses with it. Two candidates offered one in place of the other that conflict at a pair given \(\chi\) are **rivals given \(\chi\)**: for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account. ``
- **l. 317** (W O-4, adapted). Reading 'not enough ... to do anything about it' as 'does not say where or how to repair' is Claude's; the text now says what solving here is and is not. Cross-reference changed from 'Part VI' to 'above', since l. 317 is in Part VI.
  - old: `` (conflict with a claim, above; Part IX). ``
  - new: `` (conflict with a claim, above; Part IX). Solving a problem so rules one rival out for that assessor while the claim stays live for that assessor; it is not a response to the conflict with the claim, which does not say where the rival is in error, and what the person goes on with stays the person's choice (conflict with a claim, above). ``
- **l. 317** (W R-5, adapted). The assessor-free relation does the work 'true' did; S26 and S27 do not answer hard case 1, so it is marked open, not closed.
  - old: `` or by whether anyone has tested the candidate on it (Parts I and V). ``
  - new: `` or by whether anyone has tested the candidate on it (Parts I and V) [whether this relation, which names no assessor, stays in the theory is the owner's open question (S95, hard case 1)]. ``
- **l. 393** (W B-1, adapted). **Claim changed.** Most serious break found: with 'j has not withdrawn d', a premise j never took up was live, so any contingent claim and its denial were ruled out for every assessor, and 'not ruled out', problems and S21's choice became empty. 'The same argument' made 'the same argument as u', since u is a step.
  - old: `` \(\operatorname{Live}_j(d;u)\): \(j\) has not withdrawn \(d\), whether or not \(j\) holds an explanation of \(d\) [Claude's readings]. ``
  - new: `` \(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\) [Claude's readings]. ``
- **l. 397** (W O-2, as worded). Carrying S27 over from conflict to circularity is Claude's step, and is now marked so.
  - old: `` rules the candidate out for whoever can use it, on a question about the world as on any other. ``
  - new: `` rules the candidate out for whoever can use it, on a question about the world as on any other [Claude's reading: the owner's words (S27) speak of a conflict; that a candidate found by examination to assume its own answer is ruled out in the same way is read from the owner's definition of argument (S23)]. ``
- **l. 397** (W O-3, as worded). The owner calls 'that property', being able to use an explanation to find errors without containing it, the gamble; the text had moved the subject to the using. The second quotation is now whole.
  - old: `` Using a claim so is, in the owner's words, "a costly gamble for all creative agents"; without it, "error correction could become impossibly costly to perform". ``
  - new: `` That a person can use a claim so, without containing its explanation, is, in the owner's words, "a costly gamble for all creative agents"; and "If this weren't possible, then error correction could become impossibly costly to perform." ``
- **l. 397** (W R-4, as worded). 'Records' suggested a ledger; S20 calls a record redundant.
  - old: `` The semantics records the gamble and puts no measure on it. ``
  - new: `` The semantics names the gamble and puts no measure on it. ``
- **l. 397** (W B-3, as worded). The definition blocks only that one claim; 'rules nothing out for anyone' said more.
  - old: `` Such an argument's conclusion is among its premises, as in "\(p\) because \(p\)", and it rules nothing out for anyone. ``
  - new: `` Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because \(p\)", and does not rule that claim out for anyone. ``
- **l. 397** (W B-3 and B-4, as worded). **Claim changed.** B-3: 'cannot stand in for the steps' said more than the block catches; the text now says what it catches. B-4: premises taken 'without any thought whatsoever' (S27) make inconsistent premises a case to reckon with; the text now says what follows, and leaves the dropping to the person (S21).
  - old: `` it finds that the candidate gives what the premise excludes. ``
  - new: `` it finds that the candidate gives what the premise excludes. The block catches only a premise that is the claim's denial, read structurally; a premise from which a step leads to the denial, as one does from \(r\) and "if \(r\), this candidate fails (E)", is a premise taken as given, and using it is the gamble above, not a circular argument. Where the premises \(j\) tentatively accepts are inconsistent, arguments from them can rule out, for \(j\), a claim and its denial alike; the semantics then says only that \(j\)'s premises conflict, and which of them \(j\) drops, if any, is \(j\)'s choice (Part 0). ``
- **l. 429** (W O-5, adapted). S21: 'sees no option', not 'has no option'. The text never said what a ruling out is for the person choosing. Worded for the case the owner describes (one way left), not 'one not ruled out' in general. The owner's words were said 'In the case of non scientific theories'; the bracket marks their use for every episode as Claude's.
  - old: `` Closing an episode is a choice: an argument can rule out some ways of closing it, but no argument makes the choice. ``
  - new: `` Closing an episode is a choice: an argument can rule out some ways of closing it for the person choosing, and where it leaves one way not ruled out, the person, in the owner's words, "sees no option" but that one, which is not to say the person "has no option" [the owner said this of non-scientific theories (S21); using it for every episode is Claude's reading]; no argument makes the choice. ``
- **l. 461** (W O-1, as worded). **Claim changed.** As at l. 75: the list is not closed at two.
  - old: `` the only other way it enters is as the content of claims a candidate can conflict with (Part VI). ``
  - new: `` it also enters as the content of claims a candidate can conflict with (Part VI). ``
- **l. 497** (W P-3, as worded). The index Theta read as if the physical module fixed which contents are explanatory; it belongs to holding a content (instantiation, S26).
  - old: `` With \(\mathfrak E_\Theta\) the explanatory contents and ``
  - new: `` With \(\mathfrak E_\Theta\) the explanatory contents that some carrier can hold under the physical module (whether a content is explanatory on its question is fixed by (E), Part V; \(\Theta\) says only which of them a carrier can hold) and ``
- **l. 522** (W B-1, as worded). Goes with l. 393.
  - old: `` the premises \(j\) has not withdrawn ``
  - new: `` the premises \(j\) tentatively accepts and has not withdrawn ``
- **l. 526** (W B-2, as worded). Goes with l. 315: the new relation gets its place in the order.
  - old: `` rivals on conflict and on the offer of one in place of the other, ``
  - new: `` rivals on conflict and on the offer of one in place of the other, rivals given a claim on conflict given that claim and on the same offer, ``
- **l. 526** (K O37, as worded). Case O37: read strictly, 'a separate definition' left the case's fixed answer ('The textbook proof would break the circle') unreachable; this keeps O49's reading and restores O37's.
  - old: `` and a separate definition that would supply it is part of the account only when the account uses it ``
  - new: `` and a separate definition that would supply it, or a separate argument that rules out the denial of the result it is defined through without using it, is part of the account only when the account uses it ``
- **l. 540** (W R-2, as worded). A case does not rule out; an argument does, for whoever can use it (l. 17, l. 495).
  - old: `` Such a case would rule out the Claim of Argument 1 and make correspondence an import again. ``
  - new: `` An argument that exhibits such a case would rule out the Claim of Argument 1, for whoever can use it, and make correspondence an import again. ``

### Not applied, or no text proposed

- **W P-1, first part (l. 315): define conflict with a claim only 'when chi, as a claim about the target under that pair's edit and boundary, excludes' what the candidate gives**: The owner: 'If it can be shown that your explanation implies perpetual motion, then that's a conflict', with no restriction. Narrowing the definition would make the frictionless-pendulum candidate conflict with nothing. The gap the reader found is in the ruling out, not in the conflict, and the adapted second part names the missing premise there.
- **W B-2, the clause 'of the first kind where the pair is in C and of the second where it is not'**: The kinds follow from where the rivals conflict (l. 317); the clause was in error for two candidates that conflict given chi both inside and outside C. 'As rivals do' carries it.
- **W O-7 (point 1 of the reading goes beyond the owner's words)**: No text of its own: R-5 marks the assessor-free relation at l. 317 as the owner's open question.
- **K l. 317 (N5, O24): point the no-test sentence back to 'does not by itself say which to drop'**: Proposed as an owner question, not a text change. O-4 now says that solving a problem by a claim is not a response to the conflict with the claim; whether the owner's 'not enough ... to do anything about it' reaches a choice between rivals stays the owner's.
- **K l. 275 (N25)**: The reader proposed no text change: what a target such as 'the universe and what holds it up' admits is S95 hard case 1 in another form.
