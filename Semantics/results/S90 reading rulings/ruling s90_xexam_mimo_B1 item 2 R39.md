# Ruling: s90_xexam_mimo_B1, item 2, R39 (W6.3)

*A fresh Claude checker, 23 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*What it read:*
- *the reply's point 2 (R39), and its other points only where they name R39, \(\mathcal N\) or "declared" (points 1 and 5 do not bear on R39); its closing lines. The receipt shows the reply was accepted: attempt 1 finished "length" and was rejected, attempt 2 finished "stop" and was accepted, the response sha256 b67c7207… matches, and the last line is END OF REPORT;*
- *batch 1's reading and its ruling file on this entry, "S90 reading rulings/ruling s90_xexam_atria_B1 R39.md" (md5 71e79d6308a363a77e014f82b206af47).*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e, as of 587eebf;*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923;*
- *batch 1's reading, md5 56219a1d3bf20e22ea241cb18ff8a426;*
- *the S81 case book (md5 4f488d14…) and the S89 case book (md5 b2e53577…).*

*It opened no other S90 return and no reasoning file.*

## 1. The entry, its checkers' history, and batch 1's ruling

W6.3, "L447 s3: 'declared as' becomes 'taken as'".
- **Place:** Part XI, "Worth, and the normative relation", file-11 L447 s3, last clause; revised L449.
- **Group and reason word:** GROUP B1. REASON WORD erratum.
- **OLD:** `declared as a substantive input when aesthetic value is claimed.`
- **NEW:** `taken as a substantive input when aesthetic value is claimed.`
- **KIND:** WORDING.
- **DECLARATION:** "None, because the entry is WORDING. It is listed in the record."
- **KIND AS DRAFTED:** WORDING, given W6.2 and W6.4, with a fallback ready: "If W6.4's clause on the normative relation is dropped, rule this entry CLAIM and declare it as: 'Part XI no longer calls the aesthetic normative relation a declared input.'"
- **REASON** ends: "This entry goes one sentence past that scope, for the same reason, and it can be dropped without harm to any other entry."
- **CHECK:** "check 1, SOUND." No earlier FIX.
- **CASES AT RISK:** None ("aesthet" and "beaut" searched).
- **Its neighbour:** W6.2 (R38), s2 of the same paragraph, KIND CLAIM, DECLARATION "Part XI now names the normative relation as primitive 2 of Part XIV, taken as an input where a claim invokes worth, and no longer calls it a declared input." The two OLDs are disjoint.

**Batch 1 already ruled on this entry** (Atria B1, point 1): **FIX**.
- KIND WORDING → CLAIM. REASON WORD erratum, unchanged. OLD and NEW unchanged, byte for byte.
- DECLARATION: `Part XI no longer calls the aesthetic normative relation a declared input: it is taken as a substantive input when aesthetic value is claimed.`
- REASON: the clause "and it can be dropped without harm to any other entry." is replaced by a sentence saying it cannot be dropped, and why.
- CHECK: "check 1, SOUND. After the cross-examination (s90_xexam_atria_B1, R39 FALLS): FIX. KIND WORDING → CLAIM, declaration added; OLD and NEW unchanged."
- It refused Atria's two repairs: "fold into R38" (it would renumber R2-39 onward and merge two disjoint OLDs), and "R38's declaration" (it says "primitive 2", which R39's NEW does not).
- It passed revised L51, "In Part XI, as a declared normative relation", to the orchestrator as a loose end.

## 2. The reply's argument

Closing line: `R39: FALLS — reclassifies 𝒩 ("declared" → "taken") while typed WORDING`. Point 2 (task b):

> "The single word carries classificatory weight. Throughout the text, "declared" is a term of art: Part XIV has a section titled **"Declared inputs"** (*"stated inputs that the semantics records and does not supply"*), Part 0 and Part XIV have **"declared indices,"** and Part IV has **"Declared"** as a provenance type. To say 𝒩 is *"declared as a substantive input"* places it in the declared-input category. … A reader of the old wording can conclude 𝒩 is a declared input; a reader of the new wording can no longer conclude this and can now conclude the opposite. That is a change of claim."

> "R38 (correctly typed CLAIM) already declares the reclassification … R39 performs the same reclassification at the second mention of 𝒩 in the same paragraph but is typed WORDING with no declaration. If R39 is part of R38's change, it should be merged into R38 or retyped."

> "**Repair:** Retype R39 as CLAIM with declaration: *"𝒩 is now 'taken as' rather than 'declared as' a substantive input in the aesthetic case, consistent with its status as primitive 2."*"

The reply names no case.

## 3. The texts

**1. Quotations (S90 rule 8).**
- OLD is found at file-11 L447; NEW at revised L449. Both match the entry.
- "**Declared inputs.**" and "stated inputs that the semantics records and does not supply": found, file-11 L514, revised L516.
- "declared indices": found in Part 0 (revised L31) and Part XIV (revised L518).
- "It is taken as an input and never derived": found, primitive 2, revised L512 (file-11 L510).
- R38's "no longer calls it a declared input": found in W6.2's DECLARATION.
- **Not found as stated:** "Part IV has "Declared" as a provenance type". The provenance value \(\text{declared}\) is a contract's provenance, at revised L155, in Part III ("A **declared** contract is stipulated by the modeller"); Part IV has only "A declared transport" (revised L211). The point does not rest on it: the "Declared inputs" paragraph carries it alone.

**2. The old clause used the term of art.** File-11 L447 s2 says "takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV)", and s3, one sentence later, says of the aesthetic \(\mathcal N\) "declared as a substantive input". Read after s2 and its pointer to Part XIV, s3 places the aesthetic \(\mathcal N\) in the category L514 names. The drafter's REASON reads it the same way: left in place, the clause "would bring back, one sentence after W6.2, the category that W6.2 removes". "Declared" has other, ordinary uses in the text (a declared contract, L155; a declared transport, L211; "Their declaration", L435), but none of them is one sentence after "a declared input".

**3. The change is CLAIM by the list's own test.** The record's test (change list L2184): CLAIM "when a reader can conclude from one of the two texts something the other leaves unconcluded"; WORDING "when both texts assert the same thing and every conclusion drawn from one can be drawn from the other".
- From old s3 a reader concludes that the aesthetic \(\mathcal N\) is a declared input.
- From the revised text no reader can: s2 (W6.2) no longer says it, L516 keeps "Besides the two primitives", L512 says "taken as an input and never derived; the aesthetic relation of Part XI is one instance", and new s3 now uses primitive 2's own verb.
- W6.4's clause (revised L516, "or on the normative relation where a claim invokes worth") gives \(\mathcal N\) the same missing-input consequence, which is why the drafter chose WORDING. But the same consequence reached by a different route is not the same assertion. And the loss is exactly the one W6.2 declares as CLAIM for s2: one removal cannot be a claim change in s2 and a paraphrase in s3.
- The reply's "can now conclude the opposite" holds only with L512 and L516; s3 alone does not state it. That does not affect the ruling.

**4. The change is needed; the REASON's "can be dropped without harm" is false.** Without it, revised L449 would say "(primitive 2, Part XIV) as an input" in s2 and "declared as a substantive input" in s3, against L512 and L516, and W6.2's declaration ("no longer calls it a declared input") would be false of Part XI.

**5. Related text, searched in both texts.** Every other mention of \(\mathcal N\) in the revised text agrees with the NEW: L25 ("a claim of worth or of aesthetic value takes the normative relation as an input"), L31 ("taken as an input wherever a question invokes worth"), L512, L516, L528 ("one of the declared inputs Part XIV lists or the normative relation") and L590. File 11's L27 ("takes it as a **declared input**") and L447 s2 are the other old places, and W6.1 and W6.2 change them. Revised L51 (file-11 L53, which no entry touches) still reads "In Part XI, as a declared normative relation." It does not say "declared input", so the declaration below and W6.3's GAIN ("No sentence calls \(\mathcal N\) a declared input") stay literally true. It is batch 1's loose end, already passed to the orchestrator, and this ruling leaves it there.

**6. Cases.** The reply names none. The S81 and S89 case books contain no "aesthet", "beaut" or "artist" (searched, 0 hits each). The only worth case is O12 ("its merit is real", S81 case book L75), a claim of worth, not of aesthetic value. It falls under s2 (W6.2) and L516 (W6.4), not under s3, and it stays SILENT. No verdict moves. CASES AT RISK "None" stands.

**7. The reply's two repairs.**
- **Merge into R38: refused**, as in batch 1. It would renumber R2-39 onward in the record and in the S90 id maps, and turn two disjoint OLDs (s2 and s3) into one, for no gain. The reply offers it only as an alternative to retyping.
- **The reply's declaration: refused, in favour of batch 1's.**
  - It states the edit, not the claim. "'taken as' rather than 'declared as'" quotes the two verbs. It does not say which conclusion is lost, namely that the aesthetic \(\mathcal N\) is a declared input. Batch 1's declaration says so in the list's form ("Part XI no longer …").
  - "consistent with its status as primitive 2" is not something R39 changes. R39's NEW does not name primitive 2; W6.2 (s2) does, and W6.2's declaration already says it. Putting it in R39's declaration would give R39 content its NEW does not carry. This is batch 1's reason for refusing "R38's declaration", in milder form.
  - Batch 1's declaration is exact against OLD and NEW, and it is the drafter's own fallback with its positive half added.

## 4. Ruling: FIX (kind and declaration; OLD and NEW unchanged). One reconciled ruling for Atria B1 point 1 and Mimo B1 point 2

Mimo's point on KIND agrees with batch 1's FIX. Its repairs add nothing batch 1 did not weigh, so batch 1's ruling stands. The only change is that the entry's REASON, CHECK and "What the checks changed" row now name both calls.

- **OLD:** unchanged: `declared as a substantive input when aesthetic value is claimed.`
- **NEW:** unchanged: `taken as a substantive input when aesthetic value is claimed.`
- **KIND:** CLAIM (was WORDING). **REASON WORD:** erratum (unchanged).
- **DECLARATION (exact, as batch 1):**

````text
Part XI no longer calls the aesthetic normative relation a declared input: it is taken as a substantive input when aesthetic value is claimed.
````

- **REASON, last clause, replace** "and it can be dropped without harm to any other entry." **with** the sentence below; the sentence before it then ends "… for the same reason." This is batch 1's sentence, with the second call added.

````text
It cannot be dropped: without it, s3 would still call \(\mathcal N\) declared one sentence after W6.2, W6.2's declaration would be false of Part XI, and the paragraph would pull against L510 and L514. After the cross-examination (s90_xexam_atria_B1, point 1; s90_xexam_mimo_B1, point 2) it is ruled CLAIM, with the declaration drafted above as its fallback.
````

- **CHECK (exact; replaces batch 1's CHECK line):**

````text
check 1, SOUND. After the cross-examination (s90_xexam_atria_B1, point 1, and s90_xexam_mimo_B1, point 2; both R39 FALLS): FIX. KIND WORDING → CLAIM, declaration added; OLD and NEW unchanged. Both replies' repairs refused: folding into W6.2 (R38) would renumber the record and merge disjoint OLDs; W6.2's declaration, and Mimo's "consistent with its status as primitive 2", give R39 a content its NEW does not carry.
````

- **"What the checks changed":** batch 1's W6.3 row names both calls and points: s90_xexam_atria_B1 point 1 and s90_xexam_mimo_B1 point 2.
- **Follows by program, unchanged from batch 1's pending edit 6** (made once, not twice): CLAIM 48 → 49, WORDING 5 → 4, B1 CLAIM 13 → 14 of 15; the note reads "49 of the 55 changes" and gains a second line for file-11 L447, after W6.2's; W6.3 leaves the note's list "Entries not declared, whose ruling a checker may raise to CLAIM"; record row R2-39 becomes CLAIM, declared.
- **Loose end, not ruled here:** revised L51, "as a declared normative relation". It is batch 1's item, already with the orchestrator, and this ruling does not change it.

**Conflicts.** None. W6.2 (R38): its declaration overlaps this one and agrees with it, and its OLD is disjoint. W6.1 (R02), W6.4 + W14.1 (R45), W15.1 (R49) and W7.2/W7.3 each send \(\mathcal N\) to "an input" outside the declared-input category, as this declaration does.
