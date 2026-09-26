# Ruling: s90_xexam_mimo_C, item 2, R07 (W45.1)

*A fresh Claude checker, 24 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3) and "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (§2 item 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*What it read:*
- *the whole reply, `parts/s90_xexam_mimo_C.response.txt` (the file the task names, with the call description in place of `.response`, does not exist; this is the one reply of this tag). 1,321 words by `wc -w`. The receipt shows it was accepted: pass 2, attempt 1 (the only attempt of the pass), status 200, finish "stop", 0 bad chunks, `accepted: true`, and the last line is END OF REPORT. The response sha256 9ea0342f… matches the receipt. Pass 1 of this tag ended on the dead proxy with no reply (rerun note §1); nothing of it was read.*
- *the R07 section and tasks (a)–(d) of the part C brief (md5 2183faa5…), to see what the reply was given;*
- *the S90 rule, the S90 Parts rule and the rerun note; the batch 1 and batch 2 readings and the rulings folder, for any earlier ruling on this entry. There is none.*
- *the change-list entry W45.1, the worklist's W45, the plan's row W45 and the revision note's row R2-07, for the entry's history;*
- *Atria C's point 5 on R07, which the orchestrator pointed to. It is read as another reader's view and is not counted (Parts rule 1).*
- *The S87 rules (05, 05b, 05c) govern S87 rows, not S90 parts, and are not applied here. No reasoning file was opened.*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (as of 587eebf);*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the S81 case book (md5 4f488d14…), the S89 candidate book (md5 b2e53577…) and D3-T's `final.md`.*

## 1. The entry and its checkers' history

W45.1, "Part I: substrate independence holds relative to the physics' interoperability".
- **Place:** Part I, "Substrate independence with physical obligations". File-11 L77, revised L75. Two sentences are added after s2; s1 ("Any carrier may bear an organization.") and s2 are unchanged.
- **Group:** C. **Reason word:** change of claim. **KIND:** CLAIM.
- **OLD:** `Every attribution of an organization to a physical system must be permitted by the adopted physics.`
- **NEW:** `Every attribution of an organization to a physical system must be permitted by the adopted physics. Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are fixed by the adopted physics, and substrate independence holds so far as that physics lets contents pass between media. Where two media cannot exchange what they bear, the contents that only one of them can bear form, for a system built of the other, a barrier in the sense of Part XIII.`
- **DECLARATION:** "Part I's substrate independence now holds only so far as the adopted physics lets contents pass between physical media; where two media cannot exchange what they bear, the contents only one of them can bear form a barrier, in Part XIII's sense, for a system built of the other."
- **CHECK (its checkers' verdict):** "check 2, FIX. "Kind of carrier" used "kind", a defined, contract-relative word of the theory (L13; attack (C) in Part XV). NEW reads "physical medium". The sources note follows." Group C went to check 2 only; the fix changed wording, not the declaration.
- **REASON** (not sent) says the added sentences "make substrate independence relative to the adopted physics, which L77 s2 already makes the judge of every attribution".
- **CASES AT RISK:** N24 toward; no O-case moves (O28, O42, O43, O44 checked; O14 and O49 not affected). Part C gave O14 only.
- **Revision note:** row R2-07, W45.1, C07, L77, change of claim, CLAIM, declared "yes". Plan row W45: "Take … change of claim (narrowed commitment) → CLAIM", N24, none on O-cases.
- **Earlier rulings:** batch 1 and batch 2 made none on R07 or W45.1, and no ruling file on it exists. The single S90 call (C07) failed and supports nothing. Nothing to reconcile.
- **Other reader:** Atria C (point 5; closing line "R07: STANDS") calls the barrier sentence "the limiting case of Part XIII's definition", "a genuine change of claim, as declared", and finds O14 untouched. Not counted.

## 2. The reply's argument

Closing line: "R07: FALLS — declaration misses the claim that physics fixes what carriers can bear". Point 2, task (a):

> "Three claims result. The declaration captures the second ("substrate independence now holds only so far as …") and the third (barrier). It omits the first: that *which organizations a carrier can bear* and *whether contents can pass between media* are **fixed** by the adopted physics. This is stronger than the unchanged sentence immediately before — "Every attribution of an organization to a physical system must be permitted by the adopted physics" — which imposes a one-sided constraint (attributions may not outrun the physics), whereas "fixed by" asserts that the physics determines the complete set of bearable organizations and the complete pattern of inter-medium transfer. The declaration is therefore incomplete: a reader who relied on it would not know that the change also asserts physical determinacy of bearability."

> "**Repair.** Add to the declaration: "and that which organizations a carrier can bear and whether contents pass between media are determined by the adopted physics.""

It names no case for R07.

**Quotations checked (S90 rule 8).** The quotation of the new wording matches revised L75 byte for byte apart from the bold and the ellipsis; the old s2 matches file-11 L77 and revised L75; the declaration's words match. The reply places the new wording at "lines 75–77"; it stands on line 75 alone. Nothing turns on that.

## 3. Reading

**What the reply gets right.** The new wording does make the clause the reply calls the first claim, and the declaration does not state it in those words. Task (b) of the brief asks, of the parts of a CLAIM change that its declaration does not mention, whether they change a claim. So the question is whether "Which organizations a carrier can bear, and whether … can pass …, are fixed by the adopted physics" lets a reader conclude something file 11 left unconcluded, beyond what the declaration already says. It does not.

**1. That bearability is the physics' to fix is file 11's own position.**
- Part 0 (file-11 L33, revised L31): the semantics has two primitives, "the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain", and the normative relation.
- Part IV (file-11 L215, revised L213): "The one thing (R) takes from outside is \(\operatorname{Org}_\ell(o)\): which organization a physical occurrence instantiates at a grain. That is supplied by the physical module, not by the semantics."
- Part XIV, declared input 1 (file-11 L509, revised L511): \(\Theta\) comprises "substrate state spaces, attributes, admitted processes, … and \(\operatorname{Org}_\ell\)".
- Part XII (file-11 L453, revised L455): "Possibility is the absence of a law-imposed limit …; The physical module adopts a task-based formulation of physics".
Which organizations a carrier *can* bear is the range of \(\operatorname{Org}_\ell\) over the states the admitted processes can bring the carrier into. Every ingredient is \(\Theta\)'s, and file 11 says in terms that it is supplied "by the physical module, not by the semantics". "The adopted physics" of L77 is that module's physics (L455). The new clause restates this in Part I; it adds no determiner and removes none.

**2. The reply's contrast mixes two subjects.** s2's "must be permitted by the adopted physics" constrains *attributions*, what a modeller says a system bears. The new clause speaks of *bearability*, what a carrier can bear. The one-sidedness the reply finds in s2 is that attributions must lie inside the permitted set; the permitted set itself is, in s2, already the physics' to give ("permitted by"). "The complete set of bearable organizations" is that permitted set, so "fixed by" asserts no determinacy that s2 with L213 and L511 does not already carry. The drafters' REASON reads it the same way ("which L77 s2 already makes the judge of every attribution").

**3. The passage half is inside the declaration.** The declaration says substrate independence holds "only so far as the adopted physics lets contents pass between physical media". That the physics lets or does not let contents pass is what "whether … can pass … [is] fixed by the adopted physics" says. The declaration also names "the contents only one of them can bear", which is the only consequence of media-relative bearability the new sentences draw. What the declared narrowing of s1 rests on is declared; what is left over is file 11.

**4. The proposed repair would make the declaration less exact.** A declaration is meant "to say exactly what changes in what is claimed", and task (a) asks whether it "describe[s] the current text correctly". Adding "and that which organizations a carrier can bear and whether contents pass between media are determined by the adopted physics" would present as new a position file 11 states at L33, L215 and L509, and would say of file 11 that it left bearability undetermined by the physics, which it does not.

**5. Grain.** "Fixed by the adopted physics" is read, like every claim, relative to the declared grain (revised L31: "every claim is relative to them"), as \(\operatorname{Org}_\ell\) is. The clause does not make bearability grain-free, and the reply does not say it does.

**Cases worked.**
- **O14** (the only case part C gave): Kofi's phrasebook skill turns on Deploy's narrow retained use, not on media. Neither the declared sentences nor the clause the reply names touches it. No move (Atria agrees).
- **N24** (named by the entry, not given in part C): the move toward comes from the barrier sentence and the situation's stated fact that "some calculations can be carried out only in the first sort of matter, and some only in the second" — the declared "contents only one of them can bear". The situation itself supplies the physics, so the "fixed by" clause adds nothing N24 needs. The declared move stands; no undeclared move.
- **O28, O42, O43, O44** (transfers between carriers): each situation states that the transfer took place, so the physics permits it; the clause cannot unsettle them. **O49**: no carrier question. No move.
- **D3-T** (two controller designs, one discarded): no carrier, medium or bearability question. Not touched.

## 4. Ruling

**KEEP.** W45.1 stands as drafted: OLD, NEW, KIND (CLAIM) and DECLARATION unchanged.

**Reason.** The clause the reply finds undeclared ("Which organizations a carrier can bear, and whether … can pass …, are fixed by the adopted physics") changes no claim. Bearability being the physical module's to fix, not the semantics', is file 11 (L33, L215, L453, L509; revised L31, L213, L455, L511). Whether contents pass is already in the declaration's "so far as the adopted physics lets contents pass". "Fixed by" is not stronger than s2 in substance: s2 bounds attributions by a permitted set the physics already fixes. The proposed addition would declare as new what file 11 already holds. No case moves beyond the declared N24.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Mimo said FALLS (the declaration omits that bearability and passage between media are "fixed by the adopted physics"); Atria said STANDS. Ruled KEEP after the cross-examination: bearability is the physical module's to fix already in file 11 (L33, L215, L509; Part XII L453), and passage is in the declaration's "so far as the adopted physics lets contents pass", so the clause changes no claim and the declaration is exact."
