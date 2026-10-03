# S95 Does the semantics hold without verificationist words

*Log S95, on decision S23. Written on 26 September 2026 by a Claude subagent, from the files of this workflow, all in `Semantics/` and each named below. Draft 5 (`tests/Revision 2 - file 13 draft 5, theory text.md`, md5 7f1d8ad02adf96e27622593bd263252e) is unchanged and stays the current draft; the change list and the earlier drafts are untouched. The scrubbed text is an experiment on a copy. Line numbers are draft 5's; the scrubbed text keeps them, line for line. No book is quoted here. The plain-words answer to the owner is `plain words/95 Without verificationist words - does the theory still hold, in plain words.md`.*

## 1. The answer

**The semantics holds with repairs, on one condition that is the owner's to decide.**

**Why it holds.** In draft 5 the positive status did one job. A result was "established" for an assessor who held a usable receipt for it, and a candidate "fit" when nothing established showed it failing a condition of (E). Every use of the pair in Parts VI, VIII and IX went through its negative side. So the scrubbed text keeps one status, **ruled out for j** (an argument usable by j rules out that the candidate meets (E)), and its absence, **not ruled out**, and these pick out the same candidates as "fails to fit" and "fits" did (range 1 reader, l. 315). With them the text still states rival, conflict, a problem as two rivals neither of which is ruled out for an assessor, the two kinds of problem, the test that solves a problem of the first kind, easy to vary, and "A failed answer stays failed". What makes a test separate two rivals was never the assessor's status. It is (E) and (A): where two candidates conflict at a pair, at most one of them can meet (E) there, and that is fixed by the candidates, the question and the world (l. 317). The scrub leaves this untouched. The two levels now come apart cleanly. At the world level, by (A), a candidate whose answer at a pair differs from the target's is no account of p, with no assessor and no record. At the assessor level, a candidate is ruled out only while an argument usable by that assessor rules it out, and when the argument lapses no candidate becomes an account (l. 369). Arguments 1–10 (draft 5's Derivations) keep every step, each headed "Why this and not its denial.". Part IX's one set R_j(ψ) replaces P_j and N_j and loses nothing (P_j(φ) is R_j(¬φ), N_j(φ) is R_j(φ)). Nowhere does the scrubbed text say that anything counts for a claim.

**Why only with repairs.** It did not survive by swapping words alone:
- Some claims changed (section 9).
- Some things broke (section 7): chiefly, what it is for a whole argument to rule out a claim is never defined, and several pointers and sentences no longer agree with the new definitions.
- Some residue remains (section 8): "rule out" still has a case, a test or a condition as its subject in six places, which is falsification in the absolute sense, and "forbids", "prohibited" and "an argument that X" are left.

Every break and every piece of residue has a repair in the new words, all local. None needs the positive status back.

**The condition (hard case 1).** The scrubbed text keeps one relation with no assessor in it: a candidate meets (E) on C or fails it, fixed by the candidate, the question and the world (l. 67, l. 317). The scrub removed "true", "fact" and "fact of the matter" from it, but the idea stays. If the owner counts this as truth "in any absolute sense", it must go, and then the semantics does not hold as built. "Account" would become what an assessor tentatively accepts. A test would no longer solve a problem of the first kind, because nothing would make at most one of two conflicting rivals an account. The world-level half of "A failed answer stays failed" would go, and "in error" (l. 211) would lose its sense. Claude reads the owner's "It must match reality, but not by some fixed infallible metric." (decision S21) as keeping the relation: it is a relation to reality, and no one has a metric that reads it off infallibly, since every assessor reaches it only through arguments that can lapse. That reading is Claude's.

**One change of claim that touches an open question (Claude's finding in this answer; no second reader has read it).** Draft 5's receipts were trees over evidence leaves. Whether a failure found by examining a candidate, with no test, counts as established is the owner's open question: file 93's (c2), put again in file 94 as whether the myth about winter is to count as no longer fitting for someone who sees by argument that it assumes its own answer. The scrubbed l. 397 lets an argument's leaves be "stated assumptions and definitions". The sceptic required this so that Arguments 1–10 fall inside the definition of argument. With it, an argument that finds, by examining a candidate alone, that it assumes its answer is an argument usable by j that rules out that the candidate meets (E). So the candidate is ruled out for j. The scrubbed text therefore answers (c2) "yes" by definition, where draft 5 left it open. The owner's definition of argument ("something that can be strung together into a coherent structure to decide why this and not another") names no records, and S21 bears on (c2) for non-scientific theories. Neither settles it for a question about the world. Until the owner answers, the repair is to mark the place (section 7, B12).

## 2. The instruction

The owner, 25 September 2026 (decision S23), verbatim:

> Next step. Get rid of all words that imply verificationism and see if the semantics still holds. Forbidden words and phrases.
>
> Fits, supports, supported, verifies, verified, corroborates, corroborated, proves, proved, disproves, disproved, reason to believe, reason to reject. In fact, anything belief related at all must be scrubbed. Better than, worse than, true, not true, more true, established, authority, foundation, foundational, derived, derived from. Anything that could imply some sort of foundational truth or authority. Anything that could be interpreted as needing verification or falsification in any absolute sense. Anything that is accepted is always tentatively, and mean anywhere that "accept" or "accepted" is used.
>
> Also, argument is short hand for: reasons why this and not that. Not reasons for this and not that. An argument is merely something that can be strung together into a coherent structure to decide why this and not another.

Claude's reading is in decision S23 (commit 2603e65). A replacement may not be a synonym that brings the same idea back: for example "confirmed", "validated", "justified", "warranted", "grounded", "secure", "certain", "credence", "evidence for", "vindicated", "well-founded", "basis", "rests on", or "primitive" in a foundational sense.

## 3. What was done

1. **Register.** A program (`tests/S95 Scrub - scripts/register.py`) listed every occurrence in draft 5 of the owner's words, the task's synonyms, and further words that carry a listed idea back in. Its output is `tests/S95 Scrub - register of words in draft 5.md` (a table), with the same data in `.json`.
2. **Proposed vocabulary.** `tests/S95 Scrub - vocabulary, proposed.md` gives a replacement for each family and six hard cases.
3. **Sceptic's rulings.** `tests/S95 Scrub - vocabulary, sceptic's rulings.md` rules KEEP, CHANGE or OWNER on each row of the proposal, lists missed words, and makes two findings that cut across many rows. (a) "Tentatively accept" must not be a defined status: defining acceptance as holding an argument gives it the justificationist shape, and S21 leaves acceptance with the person. (b) "Rule out" must have one sense: an argument usable by someone. A condition's exclusion is said by the condition, and logical compatibility is said with "leaves open".
4. **Rewrite.** The replacements are written in `replacements_source.py`, built into `replacements.json` and applied to draft 5 by `scrub_apply.py`, all in `tests/S95 Scrub - scripts/`. The program checks draft 5's md5 and refuses a span that is missing, occurs more than once, or overlaps another. The result is `tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md` (md5 2517ef4ec1f274e8de2bfb7e6661ef94). The words, with the reason for each, are in `tests/S95 Scrub - vocabulary, as used.md`. For this answer the program was run again at 00:14 UTC on 26 September. It rewrote the scrubbed text with the same md5, and its residue scan reported 57 hits, all BORDERLINE with a stated reason, and none unexplained.
5. **Three readers**, each a Claude subagent. The two range readers say that they wrote neither the vocabulary nor the scrubbed text; the cases reader does not say:
   - `results/S95 Scrub - check of the opening note, the note of sources and departures, and Parts 0 to VIII.md` covers lines 1–372.
   - `results/S95 Scrub - check of Parts IX to XV and every derivation, proof or argument after them.md` covers lines 373–632.
   - `results/S95 Scrub - cases re-read on the scrubbed text.md` covers 20 cases chosen because their draft-5 reading turns on a rewritten line.
6. **This answer**, which brings the three readings together. Where two readers' repairs differ, it chooses between them and says so.

## 4. The counts

| | |
| --- | --- |
| Draft 5, register | 436 occurrences on 148 lines. By category: LISTED 122, BELIEF 34, TRUTH-OR-FOUNDATION 175, RANKING 47, ACCEPT 8, BORDERLINE 50. By source: the owner's list 129, the task's lists 91, words that carry a forbidden idea back in 216. 206 of them sit inside a defined technical term. |
| Largest families | derive/Derivation 44; hold (satisfaction or possession) 26; establish 24; primitive 23; support 21; prove/proof 19; anchor 17; obligation 17; witness 17. |
| Listed words not in draft 5 at all | verify, corroborate, disprove, reason to believe, reason to reject, better than, worse than, not true, more true, authority, foundation, and the belief words believe, belief, credence, confidence, credible, warrant, trust, certain, sure, doubt. Among the synonyms: confirm, validate, basis, basic, secure, sound, falsify. Among the ranking words: better, worse, best, worst, superior, inferior, good. |
| Sceptic | 53 rows: 29 KEEP, 23 CHANGE, 1 OWNER ("knowledge"). |
| Rewrite | 298 replacements: 224 written by hand and 74 made by 12 mechanical rules. 33 are marked as rewordings, 4 as changes of claim (l. 315, 317, 397, 538), and 14 as using the provisional name (EX). By category: TRUTH-OR-FOUNDATION 132, LISTED 92, BELIEF 28, MISSED 23, RANKING 21, ACCEPT 2. |
| Lines | Both files have 632 lines. 158 of draft 5's lines are changed, and lines 2 and 8, blank in draft 5, are filled (the dated note and the Part 0 definitions): 160 lines differ. |
| Words (wc -w) | Draft 5 12,622; scrubbed 13,399 (+777). 267 of the added words are in the two new paragraphs. The body grew by 510, mostly at l. 315, 317, 369 and 397, l. 43, and l. 159 and 522. |
| Residue scan | Across the register's families and the ones the sceptic added, draft 5 has 511 hits and the scrubbed text 57, all BORDERLINE: surprise 14, hold (possession, "held fixed") 9, logical joints 8, adopt 7, accept 5 (the definition at l. 8 and the person's act at l. 67), understand 5, real/realism 3, elegance and advanceable 2, "more admitted" 1, correction 1, permitted 1, shows (display) 1. |
| Owner's own list in the scrubbed text | A search for fit, support, verif-, corroborat-, prove, proof, disprove, reason to, belief, better, worse, true, truth, establish, authority, foundation, derive, derivation finds nothing. "Accept" occurs only at l. 8 (its definition) and l. 67 ("tentatively accepts"). |
| Cases | 20 read again: 19 SAME, 1 NOW SILENT (N10, O61). |

These counts describe the work done. They grade nothing (decision S20, lesson S26).

## 5. The vocabulary as used

The whole table is in `tests/S95 Scrub - vocabulary, as used.md`. The words that carry the semantics are these:

- **Argument** (Part 0, l. 8, the owner's words): "reasons why this and not that": "something that can be strung together into a coherent structure to decide why this and not another". Part IX (l. 397) defines it: "an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions". An argument is never a reason *for* a claim. It rules out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2).
- **Tentatively accept** (l. 8): "a person's choice to go on with it, made, in the owner's words, 'for whatever reason'". The semantics never defines accepting by the arguments someone holds. Its one other use is l. 67.
- **Ruled out for j / not ruled out** (l. 315) replace "established" and "fits". "Rule out" is meant only for an argument usable by someone. A condition's exclusion is said by the condition ("no component … whose signature differs from its counterpart's meets (F1)", l. 245), and logical compatibility by "leaves open" (l. 159, l. 509).
- **R_j(ψ)** (l. 397) is the arguments usable by j that rule out ψ, and replaces the receipts for and against. "Where no argument usable by j rules out φ, that absence rules out nothing, neither φ nor ¬φ."
- **Usability, argument step, Form_j(u)** replace standing, argument application and Lic_j(u). Form_j is read as "the inference form of u is one j admits" and marked in the text as Claude's reading.
- **Premise** replaces grounds. **Record** and **recording** replace "establish" for a test; **record leaf** replaces evidence leaf.
- **Argument 1–10**, **claim**, **Consequence**, and *Why this and not its denial.* replace Derivation, theorem, Corollary and *Proof.*
- **Import(s)** replaces primitive(s). **Object layer** replaces primitive layer. **Defined (in terms of)** and **set by** replace derived (from). "No cycle and no endless descent" replaces "well founded".
- **Counterpart** replaces anchor. **Trace** replaces a construction's witness, and **instance** a mathematical one.
- **Meets / fails** replace satisfies, holds (satisfaction) and true or false. **In error** replaces false and wrong. **Fidelity relation** replaces fidelity fact. **Faithfulness without assessors** replaces the title "Explanatory realism".
- **Aim** replaces obligation (O_ex, explanatory aim, for O_ep). **Prediction** replaces expectation. **Appraisal relation** replaces normative relation, and worth is dropped. **Tolerances** replace accuracy grades. **Repair** replaces progress. **Attribution** replaces credit. **Assessment** replaces verdict. **Left open** replaces unsettled. **A new question** replaces the right question.
- **Adopt** is kept, with one declaration at l. 75: "here and throughout, to adopt something is to take it tentatively, open to replacement".
- **Created explanation (EX)** replaces (EK), created explanatory knowledge. It is provisional and marked at l. 443, and the marker also names "understanding" and "surprise" (the OWNER row).

Where the rewrite departs from the sceptic, each time with its reason in the vocabulary file:
- l. 317, the test sentence: "an argument from what it records" in place of "what it records", because (K2) makes steps usable, not records;
- l. 317, case (ii): "no argument from an answer recorded in C", because the sceptic's wording would contradict the next clause;
- l. 277, the elegance sentence: "draws no line between two candidates", because "separate" is the theory's word for an admitted change;
- l. 269: "fixes nothing" in place of "decides";
- l. 37: "asks about" in place of "tests".

Where it departs from the proposal:
- l. 455: "says nothing about how anyone appraises";
- l. 628: "the displacements that occur", not "observed".

## 6. The verdicts

- **Lines 1–372** (title, the note, Part 0 and Parts I–VIII): **HOLDS_WITH_REPAIRS**. No listed word is left. Organizations, kinds, questions, contracts, provenance, representation, (E), routes and criticality, rivals and problems, the exact constructions and the transport results all still work, and the mathematical arguments keep every step. Nothing in the range needed the positive status. There are 19 repairs, with exact wording.
- **Lines 373–632** (Parts IX–XV and Arguments 1–10): **HOLDS_WITH_REPAIRS**. (K1)–(K3), (P), (EX), (CT1)–(CT4), (RC), (U1)–(U3), the dependence order and the conditions under which the class would be ruled out all survive. Arguments 1–5 and 7–10 go through as written. Argument 6 goes through once one repair is made (B7 below).
- **Cases**: of the 20 re-read, **19 SAME**. Where draft 5 reached the fixed verdict, the scrubbed text reaches it from the same lines, and where draft 5 was silent (O1's "retreat", O27's "mostly") the scrubbed text is silent in the same place. The verdicts come from content the scrub only renamed: (E), (A), the conflict relation, Argument 3's population, the dependence order and active routes. **N10 (O61), the burned notebook, is NOW SILENT**: draft 5 gave it through (EK), and the name "knowledge" is gone pending the owner. If the owner rules that knowledge is (EX), both of its questions come back the same, the second pulling away from the verdict because the name now points at the explanation, not at whoever holds it. No case moved away from or toward its verdict. The re-read cases were O1, O2, O16, O24, O27, O36, O37, O45, O46, O48, O52, D3-T (O76), N1 (O53), N2 (O54), N3 (O55), N4 (O56), N5 (O57), N7 (O58), N10 (O61) and N25 (O75).
- **Watches**, wordings that open a reading draft 5 did not have, though none moves a verdict on the text as it stands:
  - l. 397's stated-assumption leaves (O24, N5);
  - l. 441's widened attribution (O52);
  - l. 522's refusal of "any function that orders explanations", wider than "merit function" (N7's "fuller");
  - l. 526's "defined only by its own construction", which no longer echoes O37's "justifies";
  - l. 397's "A record … does not rule out", which is true of every record once only arguments rule out (O16).

## 7. What broke, and the repairs

The repairs are given in the scrubbed text's words. "R" numbers are the range 1 reader's. Where both readers proposed wording for the same place, the choice made here is marked.

**B1. What it is for a whole argument to rule out a claim is not defined** (l. 8, 315, 317, 369, 397). Both readers found this. l. 8 says each step "rules out the case in which the step's premises are met and its conclusion fails (Part IX)", but Part IX does not say so. (K2) defines usability for steps only, so "an argument usable by j" is undefined. *Repair, combining both readers:*
- At l. 397 add: "Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (Form_j), while that form stays admitted. An argument is usable by j when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion."
- At l. 8, replace the step sentence with R1: "Each of its steps is of an inference form that the person using it admits (Form_j, Part IX), and admitting a form, like accepting a claim, is tentative; …; a claim that no argument rules out is only not ruled out, and gets nothing from that; a claim whose denial an argument rules out gets nothing more than that ruling out."
- Rename R_j(ψ) to X_j(ψ), because R is already the repertoire R_{β,l} (l. 403) and R_{<e} (l. 413).

*Choice made here:* the range 2 reader proposed Form_j as "one j tentatively accepts". R1 keeps "admits" and declares admitting tentative. R1 is chosen: the sceptic keeps "accept" for a person's choice of a claim, and "admit" is draft 5's word for a declared inclusion that can be withdrawn.

**B2. l. 315 and l. 369 no longer agree.** l. 369 says "ruled out" is "meant as in Part VI", but l. 315 now defines it only for a candidate, and l. 369 applies it to an answer. The step from y to the candidates also needs (A) and the candidate's own answer. *Repair:*
- R13 (l. 315): "A claim is **ruled out** for an assessor j when an argument usable by j (Part IX) rules it out, and a candidate is ruled out for j when the claim that it meets (E) is;"
- R18 (l. 369): "Here 'ruled out' is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out the claim that y is the target's answer at (a,b); joined to a candidate's own answer y there and to (A), it rules out that the candidate meets (E); and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses."

**B3. l. 317 (i): the test no longer solves the problem "for that assessor".** The argument from the record is not said to be usable by that assessor. Draft 5 had this inside "establishing it". *Repair, R14:* "…is a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live for that assessor (K2, K3): an argument from what it records then rules out at least one of them for that assessor, while it stays usable; an answer that such an argument rules out stays ruled out on p for as long as the argument stays usable (Part VIII)." In (ii): "…an argument from a test inside C can rule out one of them without the other only for a failure of its own…"

**B4. l. 317's new last sentence is false of its own paragraph.** "Of one candidate, the only thing said is whether it is ruled out" cannot stand, because the paragraph also says of one candidate whether it is an account of p. *Repair, R15:* "Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict."

**B5. l. 277's first sentence has an empty head.** *Repair, R11:* "(E) has no condition on how a mechanism came to be guessed: a mechanism meets (E) or fails it whatever led anyone to guess it, and how it came to be taken up is assessed elsewhere (Part IX)."

**B6. The conjecture's defeaters and Part XV (A)/(B) no longer match** (l. 17, 31, 536, 538). With "genuine" and "plainly" dropped, l. 17 and (A) rest on a bare "explains nothing", which is the predicate that l. 31 and l. 526 now refuse. (B) already names the outside judgement, an argument that does not use (E). *Repair, reconciled here from R2 and the range 2 reader*, whose (A)/(B) form avoids "argued to be one", which that reader calls the argued-FOR form:
- l. 17: "A candidate that an argument not using these four rules out as a non-explanation of its question, and that these four cannot represent, would conflict with the conjecture; so would a candidate that meets all four and that such an argument rules out as an explanation on its question and contract. An argument that exhibits either rules the conjecture out for whoever can use it, while it stays usable. Part XV lists what such an argument would have to exhibit."
- l. 536 (A): "A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks." (A) ends: "…it is a counterexample only if it fails none of the four and such an argument rules it out as an explanation."
- l. 538 (B): "A candidate that an argument not using (E) rules out as a non-explanation, whose organization no transport can preserve under any physically admitted contract."

This l. 17 wording is Claude's reconciliation, and no reader has read it.

**B7. Assessor inputs are neither defined nor declared, which leaves a gap in Argument 6** (l. 390–391, 522, 526, 598). Form_j, Scope_j and Live_j are not defined in terms of the imports, indices and inputs, nor listed among Part XIV's declared inputs, yet Argument 6 claims that every predicate in Parts II–XIII is. The gap was already in draft 5 (Lic_j, Live_j), and the reading "j admits" makes it explicit. Also already in draft 5: Argument 6's walk back never reaches (O) and (Q), which depend on nothing. *Repair (range 2 reader):*
- l. 522, after "(Part XII);": "for an assessor j, the inference forms j admits, the scope j declares and the premises j has not withdrawn (K2, Part IX);" (with "admits" for "tentatively accepts", per B1);
- l. 526, after "(K1) depends on (E).": "(K2) depends on those inputs of the assessor; (K3) on (K2).";
- l. 598: "…following each definition back until it reaches the imports, the indices, the declared inputs, or (O) and (Q), which depend on nothing.";
- optionally, at l. 391: "Scope_j(u): u is applied within the contract, grain and boundary j has declared for it; Live_j(d;u): j has not withdrawn d [Claude's readings]."

**B8. "Route" is used before it is defined, in two senses** (l. 299, 307). *Repair, R12:* "Criticality is relative to the route W it is assessed in, a **route** of the candidate being a member of S_{E,p} (not an active route of a history, Part IX): …". At l. 307, "Here a route of the candidate is a member of S" then becomes "A route of the candidate".

**B9. "Faithful" is applied outside its definition** (l. 151, l. 331). Fidelity is defined for transports only (l. 189). *Repair:*
- R8 (l. 151): "A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; …"
- R16 (l. 331): "…is not an inference from the readings; it is circular, though the value it sets might be the target's."

**B10. l. 159's reading of "appropriate" says nothing.** The question asked has the restricted contract, so the answer is always no, and the syntax is a garden path. *Repair, R9:* "Meeting the conditions of an account (Part V) on the restricted contract leaves open why the claim is made on this restriction and not on a wider one."

**B11. The refused predicate collides with the defined (EX)** (l. 31, 526, 600, against l. 443–450 and l. 528). Draft 5 kept the refused "is knowledge" apart from the defined CreateEK, and the provisional rename merges them. *Repair (range 2 reader):*
- l. 526, with l. 31 to match: "Nothing depends on an undefined predicate that says 'explains' without a question and a contract, or 'is a cause'; (EX) is a defined relation of an episode, not such a predicate."
- l. 600, if the name stays: "…no residual, undefined predicate meaning 'explains,' 'represents,' or 'is a cause'; (EX) is defined (Part XI)."

**B12. Stated-assumption leaves** (l. 397). Nothing stops j from ruling out ψ by assuming ¬ψ, so "not ruled out" (Part VI), "a problem for p" and S21's choice could all be dissolved by stipulation. The present block covers only "a record reconstructed from a claim". The same widening answers (c2) (section 1). *Repair:*
- (range 2 reader) the last sentence of l. 397 becomes "A record reconstructed from a claim does not rule out that claim's denial, and neither does a stated assumption of the claim, or of a claim that contains it."
- (this answer) add: "[Whether an argument with no record leaf can rule out that a candidate meets (E) is the owner's open question (logs S93, S94); this definition answers yes, and is provisional.]"

No reader has read the second sentence against Arguments 1–10. Their stated assumptions are the hypotheses of conditional claims, not the claims themselves, so the block should not catch them, but this is untested.

**B13. l. 441: ProducedBy is widened.** It "attributes the repair to each contribution the history contains", where l. 307 of the same text says "the contributions whose active routes ran to it". *Repair:* "…it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both…"

**B14. The tolerance order presumes a chain** (l. 479), while Q_Θ is declared a directed preorder. *Repair:* "The tolerances of the physical module (Part XIV) form a directed preorder Q_Θ, in which q precedes q′ when q′ admits no performance q excludes; none of them is exact."

**B15. Small breaks** (range 2 reader). *Repairs:*
- l. 620: "Stipulate an object layer".
- l. 630, a category slip, since a contract contains changes: "That is not a defect of S_1: the contract contains no change that separates the two things except by their trajectories, so identity, at this grain, is exhausted by trajectory."
- l. 540, since claims are ruled out and arguments are not: "Such a case would rule out the Claim of Argument 1 and make correspondence an import again."
- l. 600: "Neither is a predicate about explanation."
- l. 453: "to rescue c's meeting (E)".

## 8. Residue, and the repairs

**"Rule out" with no assessor: falsification in the absolute sense.**
- l. 8, the step clause, is repaired by B1.
- l. 17, where a case and not an argument rules out, and more strongly than draft 5's "counts against", is repaired by B6.
- l. 47, "Part XV names what would rule it out". *Repair, R3:* "Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out."
- l. 61. *Repair, R3:* "…are stated exactly in Part XV together with what an argument would have to exhibit to rule out each."
- l. 317, with a test as subject, is repaired by B3.
- l. 335, "does not rule out the scoped result". *Repair, R17:* "…permitting division changes the state space and makes a new question (Part III); the scoped result on its own question is as it was."
- l. 495. *Repair:* "A finite list of failures does not rule out a bypass; one bypass rules out a proposed barrier."

**Authority words.**
- l. 47 "forbids" is repaired by R3 above.
- l. 161 "What is prohibited is changing C or Q during an assessment …". *Repair, R4:* "An assessment is an event with a frozen contract (Part 0, grievance 10): a change to C or Q during it, left unrecorded, makes the record name a claim other than the one assessed."
- l. 461, a task as "a permitted input-to-output attribute transformation", kept as BORDERLINE by the rewrite. *Repair:* "…a task a specified input-to-output attribute transformation with explicit resources and side effects." The range 2 reader notes a fault already in draft 5 here: Admit and Poss in the same Part need tasks that can be impossible.
- l. 532, the heading "What defeats this class", uses the vocabulary of defeasible justification. *Repair:* "# Part XV — What would rule this class out".

**"An argument that X", the reasons-FOR form.**
- l. 542: "…; a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV."
- l. 544: "**(E) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5)."
- l. 538, "argued to be one", is repaired by B6.
- l. 526, "a separate argument that would supply it". A definition's job is meant. *Repair:* "…a separate definition that would supply it is part of the account only when the account uses it."

**Foundational residue.** l. 518 says N is "taken as an input and never defined in terms of anything else", which claims N cannot be defined. *Repair:* "It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance."

**Corroboration residue.** l. 211, "a second, independent trace", still carries the idea of an independent witness. *Repair, R5:* "A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one."

**Belief and attitude words (the owner's call).** "Surprise" and "surprised" (Part IV, l. 215–223), "recognized difficulty" (l. 223, 317, 429) and "understand"/"understanding" (Part X) are each defined with no attitude in them, but in ordinary use each is a belief word. The l. 443 marker names "surprise" and "understanding", but nothing at l. 215–223 points to it, and "recognized" is marked nowhere. *Repair, R6, two options.* Option A:
- l. 221: "- an **unshaped violation** is a violation of a selected transport at (a,b)∉H.";
- at l. 223, "surprised"/"surprise" become "has no unshaped violation"/"unshaped violation";
- the heading at l. 215 becomes "## Prediction and violation";
- "recognized difficulty" becomes "registered difficulty" at l. 223, l. 317, l. 429 and in Part X.

Option B: add "(the name is provisional; see the marker in Part XI)" at l. 221, and the same pointer for "recognized difficulty" at l. 223.

**Borderline.**
- l. 43: "The physical theory fixes which changes are possible at all" reads, without l. 75, as the physics having the last word. *Repair, R7:* "The adopted physical theory says which changes are possible at all." and "What is independent of the modeller lies in the world the adopted physics describes and in fidelity; what the modeller chose to leave out lies in the stated scope, and so in the record."
- l. 201: "the usual arrangement" is an unargued claim about frequency. *Repair, R10:* "…that is one arrangement, not a requirement."
- l. 8: "rule out a claim's denial" equals proving the claim in classical logic. It is acceptable only if the claim gets nothing from it, and B1's last clause says so.
- Kept without repair: l. 403 "a theory in error", l. 481 "testable", l. 497 "advanceable". Optional: l. 403 "A system may understand a theory that is not an account of its question."

## 9. Changed claims

Both readers compared every changed line with draft 5. **INTENDED** means the verificationist commitment is gone and the claim otherwise stands, or changed only as the owner's instruction requires. **MORE** means the claim changed beyond that.

**MORE than intended, each with its repair in section 7 or 8:**
- l. 17: a weight ("counts against") became an exclusion with no assessor, and the defeater no longer has to be judged independently of the conjecture (B6).
- l. 31: "No predicate that says 'explains' without a question and a contract" makes l. 17's "explains nothing" the refused predicate (B6, B11).
- l. 151 and l. 331: "faithful" is used outside its definition (B9).
- l. 159: "appropriate" is narrowed to a reading that says nothing (B10).
- l. 277: the first sentence is wider (any origin of the guess) and empty at its head (B5).
- l. 317: the step from the record to "for that assessor" is weaker (B3), and the added clause about one candidate is false (B4).
- l. 385: "Using an objection gives it no bearing (K1) and makes no argument from it usable (K2)" widens to all objections, and "gives it no bearing" can be read as taking bearing away. *Repair:* "Using an objection does not give it bearing (K1) or make any argument from it usable (K2)."
- l. 390–391: Form_j is new content, an assessor-relative logic (B1, B7).
- l. 397: the widened leaves (B12), and with them the answer "yes" to (c2) (section 1).
- l. 429: "a choice, not an argument" can be read as saying arguments play no part in closing, against S21. *Repair:* "Closing an episode is a choice: an argument can rule out some ways of closing it, but no argument makes the choice."
- l. 441: widened attribution (B13).
- l. 455: worth, a property of the aim, becomes a relation to appraisers, which leans toward a person-relative reading. *Optional repair:* "Repairing an aim repairs it and says nothing about any appraisal of the aim, or of the question that led to it; an appraisal, where one is invoked, is itself a claim open to criticism."
- l. 479: a loose description became a chain-shaped inclusion claim (B14).
- l. 518: N is now said to be indefinable (section 8).
- l. 526: the refused "is a created explanation" collides with (EX) (B11).
- l. 536: the marker of outside judgement is gone (B6).
- l. 544 and l. 592: "finding a new question" covers every finding of a new question. This matches (G) and exposes more to defeat; "finding" must mean owned construction. *Repair:* l. 592, "Finding a new question, by an owned construction (G), is a creative act, as answering one is."
- l. 568, and l. 317: the contrastive restatement of "right" now follows almost by definition. *Repair:* "a claim that the target pairs its components one way and not the other is a claim that some admitted change separates them, and must supply it."
- l. 630: a category slip (B15).

**INTENDED:**
- l. 2 and l. 8 are new: the dated note, and the definitions of argument and tentatively accept.
- l. 13: "permitted" became "used".
- l. 25: the refusal now also covers ordering explanations. "Divide an achievement" is not "divide the credit". *Repair, R19:* "It does not attribute an achievement to contributors beyond what a history contains (Part XI)."
- l. 27: "does not decide whether", which also disclaims ruling membership out.
- l. 39, l. 51 and l. 55: "Argument 7 rules out a conflict between them".
- l. 41, 43 and 57: the objections are restated in the text's vocabulary.
- l. 67: "Faithfulness without assessors … tentatively accepts".
- l. 71: "with no argument that rules out its rivals … an appraisal that no argument has decided".
- l. 75: conditions, "possible under", and the declaration for "adopt".
- l. 201: "usual" (see section 8).
- l. 211: fidelity relation, theory in error, trace.
- l. 245: stated as what (F1) excludes, the contrapositive of the same claim.
- l. 277: the elegance sentence, now exact: both meet (E) or both fail it.
- l. 285–313: support became route, theorem became claim, "Why this and not its denial", instance.
- l. 315: the positive status is removed, and the same candidates are picked out.
- l. 317: permanence at the assessor's level is removed. The contrastive restatements replace "right/wrong", and "orders" replaces "grades … ranks".
- l. 325–365: renamings with the same claims.
- l. 369: the positive status is removed and the lapse made tentative. The pointer is repaired in B2.
- l. 373–395: usable arguments, Usability, premise, and (K3) as "an argument usable by j that rules out O rules out T∧B∧I together for j, and nothing narrower".
- l. 397: one set R_j with no information lost (leaves aside).
- l. 403–411: suffices, theory in error, trace.
- l. 427 and l. 441: contribution, "attributed through", aims, "account", "order".
- l. 443–453: (EX), provisional.
- l. 461 and l. 469: performed, admitted.
- l. 475: "defined".
- l. 481: "testable".
- l. 495: argument, and "rules out".
- l. 509: "leaves open", "suffice for".
- l. 515–526: imports, "defined", "no cycle and no endless descent".
- l. 522: assessment, left open, "probability on claims", "function that orders explanations or thinkers".
- l. 524: "a case meets or fails".
- l. 528: "typing as declared".
- l. 534: "the claims the rest depends on", "rule out".
- l. 538: "genuine" became the argument that would have to be given, which is stricter.
- l. 540: "would rule out Argument 1" (repaired in B15).
- l. 568: "and not the other, is the target's".
- l. 572: "leaves open whether", which is slightly stronger and still holds.
- l. 576 and l. 620: object layer, and "claim" for guarantee.
- l. 582 and l. 624: prediction.
- l. 606: "E can meet (E) on C and fail it on C′".
- l. 608: "admits".
- l. 610: "structure-preserving".
- l. 628: "that occur", and "an account".
- l. 632: "instantiates it", a stronger disclaimer.

## 10. Losses and gains

**Losses.**
- *A positive status for an assessor.* The text can no longer say that a candidate that survived tests differs from one never tested, since both are only "not ruled out". Nothing in the text needed the status. The loss is intended, per S21.
- *Permanence of an exclusion at the assessor's level* (l. 317, 369, 495). It was an absolute the owner asked to remove. The world-level permanence by (A) stays.
- *Worth.* The appraisal relation has no slot for an aim or a question being worth having apart from someone's appraisal. "How anyone appraises" leans toward a person-relative reading that the sources' objective, criticizable values do not share.
- *"Knowledge"*, pending the owner. The rename loses the direct bridge to the sources' non-belief sense of the word and causes B11 and N10's silence.
- *The critics' own words.* Objections 3, 4 and 11 (l. 41, 43, 57) are restated in the text's words, so an opponent who holds them in terms of truth or objectivity no longer sees them quoted and answered.
- *The names* "Explanatory realism" and "scope-honesty", and with them the explicit tie to the sources' realism. The content stays.
- *"The right question".* The text now says only that finding a new question is creative. Draft 5 never formalized "right", so there is no formal loss.
- *The explicit point* that a mechanism guessed for bad reasons is not disqualified (l. 277), until R11.
- *Draft 5's broader "appropriate restriction"* (l. 159), until R9.

**Gains.**
- *The owner's definitions are in the text.* l. 8 states the owner's definition of argument and makes acceptance a person's tentative choice, kept out of the semantics: the semantics supplies "ruled out", and the choosing is the person's (S21).
- *Only exclusions, all tentative.* "Not ruled out … gets nothing from that" removes draft 5's asymmetry, under which a candidate fit what was established. Every exclusion is tied to an argument someone can use, and lasts while it stays usable.
- *Two levels made visible.* At the world level a candidate meets or fails (E), with no assessor. At the assessor level it is ruled out for j. Draft 5 mixed "established", "fits", "refuted" and "right". l. 43 ("no assessor appears in (E)") and l. 67 say where independence lies without the word "fact".
- *Contrastive statements throughout*, in the owner's "why this and not that": "one of them and not the other", "on this restriction and not on a wider one", "Why this and not its denial".
- *Part IX.* One set replaces two sets and an exchange rule, and "that absence rules out nothing, neither φ nor ¬φ" says exactly what "missing evidence stays missing" gestured at. (K3) keeps the Duhem point, relative to the assessor and to usability.
- *Precision elsewhere.* l. 385 names both senses that "valid" left unsaid. "Import" says where Θ and N come from, not what standing they have, and "no cycle and no endless descent" is the exact content of well-foundedness without the metaphor. l. 245 states what (F1) excludes. Argument 7 now says how the two claims coexist. Argument 10's disclaimer no longer implies that verification is the missing step. (B) says what an outside judgement must be, an argument not using (E). Tolerances read as inclusion remove the merit reading of "grades" (lesson S26), once B14 is repaired.

## 11. For the owner

1. **Hard case 1, on which the answer depends.** May the theory keep the assessor-free relation "a candidate meets (E) on C or fails it, fixed by the candidate, the question and the world"? If yes, the semantics holds with the repairs above. If not, Part VI's test, the world level of "A failed answer stays failed", and "in error" must be rebuilt, and the semantics as built does not hold (section 1).
2. **An argument with no record in it.** The scrubbed definition of argument lets a pure argument, such as finding by examination that a candidate assumes its own answer, rule a candidate out for whoever can use it. That answers file 93's first question, and file 94's, "yes". Is that what the owner means by argument, for questions about the world as well as for non-scientific ones?
3. **"Knowledge"** (the one OWNER ruling). Rename it (the provisional "created explanation"), or keep the sources' sense and add their condition that the created explanation tends to keep itself in being in its environment; do not keep the word alone. The same question, smaller, applies to "understanding", "surprise" and "recognized difficulty".
4. **Worth.** Is dropping it for "someone's appraisal" acceptable, given that the sources treat values as objective and open to criticism? Keeping "worth" inside a declared appraisal was the other option; the sceptic dropped it.
5. **The critics' words.** May an objection be quoted in its author's words (truth, objectivity) when the text answers it in its own?

The questions of logs S93 and S94 are still open. The second above changes the first of them.

## 12. What was not tested

- **No outside cross-examination.** Atria and Mimo have not seen the scrub, the vocabulary or this answer. Every register, proposal, ruling, rewrite and reading is by a Claude subagent, of the family that wrote the theory.
- **Only the most exposed cases were read again**: 20 of the 76 (O1–O52, the candidates O53–O75 and D3-T as O76), chosen because their draft-5 reading turns on a rewritten line. The exclusions and their reasons are in the cases file.
- **No repair is applied or read.** The repairs above are proposals. Where two readers' repairs differed, this answer chose between them (B1, B6, B7); B6's l. 17 wording and B12's marker are Claude's and unread by anyone else.
- **One reader per range**, each read once. The mathematical steps of Arguments 1–10 were read by one reader.
- **The scrubbed text was not run through draft 5's verification program** (`results/S93 Verification of draft 5 - check script.py`). It was checked only by the rewrite's own refusals and residue scan and the readers' programs.
- **The sources.** The sceptic checked the proposal's two book quotations against the books. No reader compared the scrubbed text's new claims (on knowledge, values or appraisal) with the sources.
- **The plain-words files 91–94 still use the old words** ("established", "fits", "receipt", "judge"), and so do the change list, the records, the earlier results and the decisions' readings. File 92 renders draft 4.
- **The change list is untouched.** The scrub is an experiment on a copy of draft 5, not a change-list entry with a declaration.
- **Not decided**: whether the scrubbed text, repaired, becomes the working draft in place of draft 5.

## 13. Next step

The owner's answer to question 1 in section 11: whether the theory may keep saying, with no assessor, that a candidate meets (E) or fails it. Everything else waits on it: question 2, the name, and then applying the repairs to the scrubbed copy and putting it, split by part, to a checker and to Atria and Mimo.
