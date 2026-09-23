# Ruling: s90_xexam_mimo_B1, item 1, R04 (W58(ii).1)

*A fresh Claude checker, 23 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*What it read:*
- *the reply's point 1 (R04) and its closing lines. The receipt shows the reply was accepted: attempt 2 finished "stop" and was accepted, the response sha256 b67c7207… matches, and the last line is END OF REPORT;*
- *batch 1's reading, for any earlier ruling on this entry;*
- *03 §7.6 and §8, and its row M6.*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e, as of 587eebf;*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923;*
- *the revision note, draft of 23 September;*
- *the S81 case book (md5 4f488d14…) and the S89 case book (md5 b2e53577…).*

*It opened no other S90 return and no reasoning file.*

## 1. The entry and its checkers' history

W58(ii).1, "L33 s4: no such predicate is primitive or depended on".
- **Place:** Part 0, "What is primitive, what is an index, and what is derived". It is file-11 L33 s4, revised L31.
- **Group and reason word:** GROUP B1. REASON WORD clarification.
- **Its neighbour:** W7.1 (R03) changes s3 of the same paragraph. The two anchors do not overlap.

- **OLD:** `No predicate meaning "really explains", "is a cause" or "is knowledge" appears anywhere (Derivation 6).`
- **NEW:** `No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive, and no definition depends on one (Derivation 6).`
- **KIND:** WORDING.
- **DECLARATION:** "none (WORDING, after check 1: ORDER against L518 and L590; listed in the record)".
  - It has a fallback line, ready: "Part 0 now says that no predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive or depended on by any definition, where it said that none appears anywhere."

**How the entry got its kind:**
- **As drafted it was CLAIM.** The reason given: the entry closes a reading that is literally false, because file 11 mentions "is a cause" at L55, L123 and L129. Under plan 1.1, closing an open reading is CLAIM.
- **Check 1 changed the kind only: FIX, CLAIM → WORDING.** Its reason: 03 ruled L33 s2–s4 ORDER (M6, upheld). 03 also read "appears anywhere" as L590's "no residual predicate" (03 §8 item 11). So the new words say what the old ones meant.
- **The REASON field** explains why the skeleton's "is defined or presupposed" was not used: "defined" contradicts L586, (EK) and Part II's causal assignment.
- **CASES AT RISK:** none.
- **The revision note** lists the entry among "Entries not declared, whose ruling a checker may raise to CLAIM".

**Other readers:**
- Atria (s90_xexam_atria_B1, point 2) tested R04 under task (b) and found it standing. It did not contest it.
- **Batch 1 made no ruling on this entry.** There is nothing to reconcile.
- Batch 1's ruling on R39 concerns a different entry, and its ground does not carry over (see §3, point 7).

## 2. The reply's argument

The closing line is: "R04: FALLS — weaker claim in WORDING guise ("not primitive, not depended on" ≠ "appears nowhere")". Point 1 argues this in three steps.

**First, the new wording is weaker than the old.**

> "The old wording rules out every such predicate—derived or underived. The new wording rules out only (i) its being primitive and (ii) its being used in any definition's definiens. A predicate meaning "explains" that some definition *introduces* (as its definiendum) and that no other definition *uses* satisfies both new conditions while violating the old wording. … The new wording therefore permits orphan derived predicates the old wording forbade."

**Second, the pointer supports the old wording, not the new.**

> "On the natural reading of "residual" (present in the theory after the derivation), this supports the *old*, stronger wording—not the new, weaker one. On the weaker reading of "residual" (underived), Derivation 6 supports "not taken as primitive" but says nothing about "no definition depends on one"; that claim is supported by Part XIV's dependence order …, which R04 does not cite."

**Third, a repair.**

> "Reclassify R04 as CLAIM with declaration: *"Part 0 no longer claims that no such predicate appears anywhere; it now claims only that none is taken as primitive and that no definition depends on one."* Alternatively, keep WORDING and strengthen the wording to match Derivation 6: *"No predicate meaning 'really explains', 'is a cause' or 'is knowledge' exists in the theory (Derivation 6)."*"

The reply names no case.

## 3. The texts

**1. The quotations are found (S90 rule 8).**
- OLD and NEW are found, and match the brief byte for byte.
- The Derivation 6 Consequence is found at revised L594 and file-11 L590. The reply's "594–595" is one line off, because L595 is blank.
- "Nothing depends on a predicate meaning "really explains," "is a cause," or "is knowledge."" is found at revised L520 and file-11 L518.

**2. On the reply's reading, the old sentence is false against file 11 itself.**

The reply reads "a predicate meaning 'explains' / 'is knowledge'" as covering *derived* predicates. File 11 has such predicates, in five places:
- **L13:** "An explanation is a **question-relevant organization of dependencies** …". This defines explanation.
- **L51:** "A proof explains, relative to a question, when its components respond to those edits as the target structure does".
- **L125–129:** "What ordinary language calls a cause … are families of signatures: a **causal assignment** has a signature …". Then: "These are descriptions of patterns in (K), not additional data. The semantics never asks whether a component "is" a cause."
- **L512:** "Representation, from fidelity and provenance (R). … Account, from fidelity under change (E). Understanding, …, knowledge, …, from those."
- **L55** quotes "is a cause" in a grievance.

So "appears anywhere", read the reply's way, is contradicted by the text around it. 03 recorded exactly this (§8 item 11: it "must mean L590's 'no residual predicate'"). 03 also ruled that file 11's introduction of that sentence was ORDER against file 10's "no residual predicate" (M6, upheld under adversarial verification). In doing so it held against the readers, Mimo among them, who marked s4 CLAIM (03 §7.6).

**3. "Residual" means "left undefined", not "present".**
- Derivation 6's Claim is that every predicate in Parts II–XIII is *defined* from the primitives, indices and inputs. A Consequence of that Claim can only say that no such predicate is left over undefined.
- The Consequence's own list includes "represents". Part XIV derives representation from (R) (file-11 L512; revised L514). So on the reply's "natural reading", Derivation 6 would contradict Part XIV.
- The Consequence ends: "Neither is a semantic primitive about explanation."
- So "no residual predicate" is "none is taken as primitive". This is NEW's first half.

**4. The second half copies L518, in L518's own sense.**
- File-11 L518 already says "Nothing depends on a predicate meaning "really explains," "is a cause," or "is knowledge."" NEW's "no definition depends on one" says the same, at the same or narrower scope. That makes this half ORDER, which counts with WORDING.
- On the reply's reading of "depends on" (used in a definiens), L518 would itself be false in file 11:
  - (S), (B), (D), (K1), Build and (EK) depend on (E), which is the theory's account of explaining (L13, L512);
  - "(RC), (U1)–(U3) depend on all of the above", which includes (EK).
- So in L518, and in NEW, which borrows L518's words, "a predicate meaning 'really explains'" names the *unanalyzed* predicate. The quotation marks and "really" mark it as such, and L127's "never asks whether a component "is" a cause" confirms this.

**5. So the two wordings say the same thing.** On the one reading the text can bear, both sentences say that no unanalyzed predicate of explaining, causing or knowing is a primitive or sits in the dependence order.
- **Everything a reader can conclude from NEW can be concluded from the current text.** L33 s1 and L510 give two primitives, L590 gives "no residual", and L518 gives "nothing depends".
- **The one extra thing the old words seemed to allow is refuted by the current text.** That is that no predicate of that meaning, derived or not, is present. L13, L51, L125–129 and L512 refute it.
- **The reply's "orphan derived predicate" is already in file 11.** The causal assignment of L125 is defined and is used by no other definition (it occurs only at L125 in file 11 and at L123 in the revised text). NEW is true of it. OLD, read literally, was false of it.
- Closing a reading the text itself refutes is not closing an *open* reading, so plan 1.1's CLAIM rule does not apply. Nothing is dropped, narrowed or widened. This meets 03's WORDING test and the brief's: "the new wording says what the old wording said".

**6. The pointer is sound.**
- Derivation 6 supports the first half (see point 3).
- Its proof (revised L592) runs "By the dependence order of Part XIV, …", and that order is where the second half stands (L520).
- The sentence just before, L31 s3, also says "in the order Part XIV states".
- So "which R04 does not cite" is literally true, but the pointer reaches L520 through Derivation 6's proof, and no reader is misdirected.

**7. Both repairs are refused.**
- **"Exists in the theory (Derivation 6)"** would be false against revised L11, L49, L121–127 and L514, which define explanation, a proof's explaining, the causal assignment, and knowledge.
- **The CLAIM declaration** would say Part 0 withdraws a claim that no reading consistent with the text ever made. It would also imply that file 11 denied any derived predicate of knowledge or representation, against file-11 L512. And it would reverse 03's upheld M6 ruling, in the opposite direction, without new ground.
- **The R39 precedent in batch 1 does not carry over.** There, old s3 let a reader conclude something the text used as a working category ("declared input"). Here, the old conclusion is one the text refutes in four places.

**8. Cases.**
- The reply names none, and CASES AT RISK is "None".
- A search of the S81 and S89 case books for "is a cause", "primitive", "predicate", "residual" and "really explain" finds nothing.
- 03 records M6 as touching no case.
- No verdict moves.

## 4. Ruling: KEEP

The entry stands as drafted, byte for byte: OLD, NEW, KIND WORDING, DECLARATION none, and its CLAIM fallback line kept as it is.

**Append to CHECK:** "After the cross-examination (s90_xexam_mimo_B1, point 1, R04 FALLS: 'weaker claim in WORDING guise'): KEEP.
- The reply reads 'a predicate meaning …' and L590's 'residual' as covering derived predicates. On that reading, both OLD and L518 are false in file 11 itself, which defines explanation (L13), a proof's explaining (L51), the causal assignment (L125–129) and knowledge and representation (L512), and whose (RC) depends on (EK) and (E).
- On the only reading the text bears, the unanalyzed predicate, OLD and NEW say the same thing. The second half copies L518.
- Derivation 6's proof reaches L518/L520.
- Atria (s90_xexam_atria_B1, point 2) found the entry standing."

**No other field changes.** Nothing follows by program: the counts, the note's N and M, and record row R2-04 are unchanged. The entry stays in the note's list "Entries not declared, whose ruling a checker may raise to CLAIM".

**Conflicts:** none.
- W7.1 (R03, L31 s3) is untouched. Its "in the order Part XIV states" supports the pointer.
- W7.6 (R53, Derivation 6's proof) is what makes the proof cite Part XIV's dependence order together with the indices and inputs. It agrees with this entry.
