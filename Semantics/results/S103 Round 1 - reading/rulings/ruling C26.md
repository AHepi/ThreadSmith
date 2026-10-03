# S103 Round 1 — ruling on C26 (L393)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it goes. Not committed. This file obeys decision S23 except where it quotes the text, a reader, a record or the owner.*

**Ruling: KEEP.** The sentence stands as it is.

- **Old (L393, last sentence of the line):** `Withdrawing a premise makes the step unusable; it does not rule the conclusion out.`
- **New:** `Withdrawing a premise makes the step unusable; it does not rule the conclusion out.` (unchanged)
- **Easy to vary on this reading (rule 5):** yes, in the plain sense the brief asks about, and recorded as such. Mimo's rival, `Withdrawing a premise makes the step unusable and rules out no claim.`, is a rewording that changes nothing the theory needs from the sentence: its second clause covers the conclusion, and what it says beyond the conclusion the text already says at L315 and L397. It is not clearer than the text's wording (reasons below), so the ruling is KEEP, not FIX.

## What was read

- The text under review, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): L1–L60, L300–L319, L360–L399 (the end of Part VIII and Part IX whole), and the whole file searched by program for "withdr", "ceases to be live", "lapses" and the quotations below.
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`, whole.
- The part 3 brief, `tests/S103 Round 1 - trying to vary the strong candidates - part 3, Parts V to XIV.md` (md5 44ef4fbdb179963c3e76fcdaf60ecf27): the C26 entry of section 3 (brief lines 127–144).
- The tabulation, `results/S103 Round 1 - reading/tabulation.md` (md5 51e752c3e26ab822e69daf8e9ec9f387): its opening (lines 1–60), C26's section (lines 2572–2672) and the note that names C26 (line 3040).
- The replies: `s103_vary_mimo_3.response.txt` (md5 a1491ae7b541cf691c5760cf07c93d44) lines 161–190 and `s103_vary_glm_3.response.txt` (md5 540429867c7029b78bcb9ad72c1af834) lines 74–88. All six replies were searched for "C26" and "withdraw"; there is no hit outside those two sections. No reasoning file was opened.
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md` (md5 71459192867b1ebcf1bae914c9297129).
- For ties to cases and history: the S98 ledger, group 09, entry L393.s4 (and L393.s1, which holds the S95 rewording), with `data/by sentence.csv` and `data/records.jsonl` searched for "L393.s4" and "Withdrawing a premise"; `results/S96 Check of the repaired copy - cases.md`, searched for "l. 393", "withdr", "(K2)", "usable", "live" and "lapses"; the S81 case book of 52 cases and the S89 candidate cases N1 to N25, searched for "withdr", "retract", "usable", "K2", "premise" and "live".

## The sentence and where it stands

L393 defines the three conjuncts of (K2), whose display is L390: `\operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}`. L387 introduces it: "For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:". The clause the sentence reads off is on L393 itself:

> \(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it

The sentence then says two things: what withdrawing does to the step (it fails (K2), since the withdrawn premise is no longer live), and what it does not do to the step's conclusion (rule it out).

The terms it uses: a step "rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form" (L397; the same at L8); "A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out" (L315); "An argument is usable by \(j\) when each of its steps is (K2)" (L397).

**History (S98 ledger, L393.s1 and L393.s4).** Draft 5 read "Withdrawing a premise removes a license; it does not make the conclusion false." The S95 scrub replaced it with the present wording (record D-161, "TRUTH-OR-FOUNDATION"; D-644 and D-686: "it does not make the conclusion false" to "it does not rule the conclusion out"). The second clause has always been about the conclusion: it blocks the move from a lost premise to the conclusion's denial.

## What the theory needs from the sentence

1. That withdrawing a premise makes the step unusable: the local reading of (K2) with the Live clause, which L369 applies ("If a premise about them ceases to be live, the argument is not usable (K2)"), L315 applies ("uses \(\chi\) as a premise and lapses with it") and L317 presupposes ("stays ruled out on \(p\) for as long as the argument stays usable (Part VIII)").
2. That the withdrawal is not itself a ruling out of the conclusion: when the step lapses, its conclusion is left only not ruled out by it. This is what L8 says of any claim ("A claim that no argument rules out is only not ruled out, and gets nothing from that"), what L397 says of an absence ("Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\).") and what L369 says of candidates ("those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (E)").
3. Both said where (K2) is defined, so that a reader of the Live clause meets both halves at once.

## Each side's argument (rule 7)

**Mimo (VARIES).** Rival: `Withdrawing a premise makes the step unusable and rules out no claim.` (reply line 166). "The second clause covers the first: the conclusion is a claim, so the guarded misreading is blocked, and the wider statement matches L8" (line 169). Variations said to break something: `Withdrawing a premise leaves the step usable.` (breaks L390 and the Live clause of L393; line 177); `Withdrawing a premise rules the conclusion out.` (breaks L8 and L315; line 183); dropping the second clause "leaves the step's collapse unseparated from the conclusion's standing", against L369 (line 185). Step 3: "The unqualified "a premise" is read in the section's context as one of \(\operatorname{Prem}(u)\) … The text forces the essential-premise reading only." (line 187).

**GLM (HOLDS).** Dropping the second half: "nothing in Part IX then says that withdrawal is not itself a ruling-out", and L8 and L369 "need the complement stated: un-usable ≠ ruled out" (line 80). Against `Withdrawing a premise makes the step unusable and rules nothing out.` (line 81): "ambiguous between "the step rules nothing out" (trivial once unusable) and "the withdrawal rules nothing out" (too broad); it loses the named claim at stake, the step's conclusion, which L315's definition of "ruled out" is about." Against `Withdrawing a premise undermines the step; the conclusion is not thereby refuted.` (line 82): S23 language; "rule out" is the defined term. Against `… it does not rule the conclusion out either way.` (line 83): the added words do no work. Fault search: "Withdrawal removes Live … so (K2) fails: correct. The second half holds because an unusable argument rules out nothing" (line 85).

**Where they differ.** Both readers agree on the sentence's work, on the variations that break it, and that the sentence has no fault. They differ on one thing: whether a wording that widens the second clause from "the conclusion" to every claim works as well. GLM's line 81 wording is not Mimo's, but it is close enough ("rules nothing out" against "rules out no claim") that GLM's three objections to it are weighed against Mimo's rival here.

**GLM's three objections, weighed against Mimo's wording.**

- *Ambiguity.* In Mimo's wording the two verbs share one subject, "Withdrawing a premise", by coordination: "[Withdrawing a premise] makes the step unusable and rules out no claim". The reading "the step rules out no claim" would need "the step" as the subject of "rules out", which the grammar does not give. The objection does not hold against Mimo's wording (and holds little against GLM's own, which has the same shape).
- *Too broad.* GLM names no claim that a withdrawal rules out, and the text gives none. By L315 only an argument usable by \(j\) rules a claim out for \(j\), and a withdrawal is not an argument; L397 says the same of dropping a claim: "A person may still drop the claim, for whatever reason (Part 0): that is the person's choice, not a ruling out, and it leaves the claim not ruled out". Nor can a withdrawal bring a ruling out about indirectly: it removes a premise from the Live clause's second disjunct, so it can only make steps unusable, never usable, and the arguments usable by \(j\) that rule out a claim can only lose members. So the wider clause says nothing the text does not already hold. The objection does not hold.
- *Loses the named conclusion.* This holds, as a point about what the sentence puts before the reader, not about content. The conclusion is a claim, so Mimo's clause still covers it (Mimo's point); L315's definition is about any claim, not about conclusions, so no definition loses its object. What is lost is the name of the one claim the guarded misreading bears on. That is weighed under clarity below.

**GLM's claim that the sentence is "the local anchor" for L8 and L369.** Looser than GLM puts it: L8 and L369 come before L393 and rest on (K2) and on L315's definition, not on this sentence; the sentence states at (K2)'s own definition what L369 applies to candidates. The point it serves (item 3 above) stands.

## Is the rival a rewording or a different claim?

Against items 1–3 above:

- Item 1: kept word for word ("Withdrawing a premise makes the step unusable").
- Item 2: kept. "Rules out no claim" covers the conclusion; by instance, the withdrawal does not rule the conclusion out.
- Item 3: kept; the rival stands in the same place.
- What the rival adds, that the withdrawal rules out no other claim either, is already held by L315 and L397 (above). It adds no claim to the theory.

**Dependents under the rival.** L369, L315 ("lapses with it"), L317, L397 and L522 ("the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX)") read as before; no case moves (below).

**The owner's words.** The rival has no word or idea S23 forbids; it says what the withdrawal does in the semantics, not what must happen (S21); it lists and counts nothing (S20); it brings in no physical possibility (S25–S27); it settles nothing (S28).

So the rival makes no different claim and is not weighed as a challenge; the sentence is easy to vary on this reading, and that is recorded. (Weighed as a challenge anyway, it shows no defect in the sentence: nothing it says is missing from the text.)

## Is the rival clearer?

**For the rival.**

1. It names every claim, so a reader cannot take the text's naming of the conclusion to hint that a withdrawal might rule out some other claim. In context the hint is faint: no other claim is in view at L393, and L315 and L397 close it.
2. It drops the pronoun. In the text's wording "it" may be read as the withdrawal (intended) or as the step; the coordination fixes the subject. Both readings of the text's "it" give what the text holds (a step never rules out its own conclusion, and the withdrawal does not either), so nothing turns on it.

**Against the rival.**

1. It loses the name of the claim at stake. The misreading the clause blocks is a move from a lost premise to the step's own conclusion: its denial is what a reader might take the lapse to leave standing, as draft 5's wording shows ("it does not make the conclusion false", S98 ledger, D-161). Nobody is tempted to take the withdrawal as ruling out an unrelated claim. The text puts the one claim in danger in front of the reader; the rival makes the reader find it by instance from "no claim".
2. It loses the contrast. The text's semicolon sets the step's lapse against the conclusion's standing, the same two halves L369 gives for candidates ("the argument is not usable (K2) and those candidates are no longer ruled out by it … no candidate becomes an account by that (E)"). The rival's "and" joins two effects, the second a general remark about withdrawals that belongs with L315's definition.
3. "Rules out no claim" can be heard as "leaves no claim ruled out", a reading the text's wording does not invite; other arguments usable by \(j\) may still rule claims out.

Weighed together, the rival is not clearer. What holds in Mimo's challenge is that the sentence can be reworded without loss, not that the text falls short; the smallest change that meets that is none. KEEP.

## The variations that change the claim, and what each breaks

Each is weighed on its own argument; none is a repair of a fault in the sentence, and none is taken.

- `Withdrawing a premise leaves the step usable.` (Mimo, line 174). Against (K2) with the Live clause: a premise \(j\) has withdrawn is not live by the second disjunct, and (K2) asks that every \(d\in\operatorname{Prem}(u)\) be live. Real, as Mimo says (with the proviso in the last section, which does not help the variation: in the ordinary case it breaks (K2)).
- `Withdrawing a premise rules the conclusion out.` (Mimo, line 180). Makes a withdrawal a ruling out, against L315 (only an argument usable by \(j\) rules a claim out) and L8 ("A claim that no argument rules out is only not ruled out, and gets nothing from that"); against L369 it would make a candidate whose ruling out lapses ruled out the other way, where L369 says "no candidate becomes an account by that (E)". Real.
- Dropping the second clause (both readers, described without wording). The text would still hold item 2 at L8, L369 and L397, so nothing becomes inconsistent; what goes is item 3, the statement of the second half where (K2) is defined, and so the guard against reading the lapse as counting against the conclusion at the place a reader meets the Live clause. A loss, not a break, and neither reader proposes it.
- `Withdrawing a premise undermines the step; the conclusion is not thereby refuted.` (GLM, line 82). "Refute" is a word the S95 scrub replaced by "rule out" throughout (S98 ledger, D-499: "refute, refutes, refutation" to "rule out, rules out, what would rule it out"); it reads as the absolute falsification S23 excludes ("Anything that could be interpreted as needing verification or falsification in any absolute sense"). "Undermines" is not a term the semantics defines, and it loses the pointer to (K2). Not taken, as GLM says.
- `Withdrawing a premise makes the step unusable; it does not rule the conclusion out either way.` (GLM, line 83). "Either way" could be heard as "neither the conclusion nor its denial"; for the denial that is already the first clause (an unusable step rules nothing out) with L397 ("neither \(\phi\) nor \(\neg\phi\)"), and otherwise the words have no object. Idle, as GLM says.

## Failures of the sentence itself

None shown by either reader. Sought:

- **"A premise", unqualified (Mimo, step 3).** A step may cite premises its inference form does not use (L387's "essential" implies it), and withdrawing one of those leaves the step usable. The text forces the essential reading, as Mimo says: the sentence picks up the Live clause's "and not withdrawn it" on the same line, and that clause is \(\operatorname{Live}_j(d;u)\) for \(d\in\operatorname{Prem}(u)\) under (K2)'s quantifier. Not a fault.
- **Contradiction.** With L369, L315 ("lapses with it"), L317 ("for as long as the argument stays usable"), L397 and L522: none found; each uses the same pair of facts.
- **Vacuity, or a part doing no work.** The first clause states (K2)'s consequence at its definition, which L315, L317 and L369 use; the second blocks the move from a lost premise to the conclusion's denial (history above). Each part works.
- **The owner's words.** S23: no forbidden word or idea; "rule … out" is the defined term, and the second clause is the S95 scrub's own replacement for "make the conclusion false". S21 and S28: "withdrawing" is the person's act, and the sentence says what follows in (K2), not what the person must do; it leaves the conclusion only not ruled out, which settles nothing (L8; S28, "A theory is never settled."). S20: no list, count or grade. S25–S27: no physical possibility. S33–S34: nothing about what hard to vary covers; nothing here is parked.

## Cases

No fixed case verdict moves under this KEEP, and none would have moved under Mimo's rival.

- **S98 ledger.** L393.s4's records (CH-1054, CH-1119, CH-1188: D-512, D-577, D-643, D-644, D-686) and L393.s1's D-161 are vocabulary and scrub records; none ties the sentence to a case.
- **S96 cases.** O27 ("The test that fitted neither"), with O40 and O50, is the case that turns on a premise ceasing to be live: the S96 check reads it on L317 and L369 ("when such a premise ceases to be live, "the argument is not usable and those candidates are no longer ruled out by it""). Its fixed verdict, "The expert framed the choice. The robot found the answer. The achievement is mostly the robot's, because the decisive step was its own reinterpretation of the test.", turns on who withdrew the sensor premise and what was found after; the sentence's first clause (the test's argument lapses) is kept word for word, and its second (the lapse does not rule a candidate out) is kept. O40's and O50's verdicts turn on attribution in the same situation and do not move.
- **The S81 case book and the S89 candidate cases.** No other case speaks of withdrawing a premise or of usability. O36 ("A premise both routes use") and O47 ("One more commitment") concern premises in routes (Part VI), not (K2).

## Dependents (named for the record; none is affected by a KEEP)

- L393, the Live clause the sentence reads off: "\(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it".
- L369: "If a premise about them ceases to be live, the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (E)." (the same two halves, for candidates).
- L315: "an argument that rules out their both meeting (F1), (F2) and (A) there uses \(\chi\) as a premise and lapses with it." (the first half, for a claim taken as given).
- L317: "an answer that such an argument rules out stays ruled out on \(p\) for as long as the argument stays usable (Part VIII)" (the first half, for a test).
- L397: "Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\)." (the second half, in general).
- L522: "the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX)" (withdrawal among the declared inputs).

## Outside this item's challenge (not ruled here)

For the orchestrator and the next round only; nothing in this ruling rests on it, and no wording is applied.

- **A premise that is live twice over.** The Live clause has two disjuncts. Where a premise \(d\) of \(u\) is a claim \(j\) took up and is also "the conclusion of a step of the same argument as \(u\) that is usable by \(j\)" (L393), withdrawing \(d\) removes only the second disjunct; \(d\) stays live by the first, and \(u\) stays usable. In that configuration the sentence's first clause, read without restriction, says more than (K2) gives. The configuration is narrow (an argument tree that has the same claim as a leaf and as a step's conclusion), and neither reader raised it, so it is not ruled here and not repaired: under the task a FIX meets only what holds in the challenge. It is a point for the next round's readers to try. L369's own wording, "If a premise about them ceases to be live", states the condition (K2) uses, and is noted only as material for that round.
- **File name.** Rule 11 of the reading rule names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; the task named `results/S103 Round 1 - reading/rulings/ruling C26.md`, and that path was used. No second copy was written.
