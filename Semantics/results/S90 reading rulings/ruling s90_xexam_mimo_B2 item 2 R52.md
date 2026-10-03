# Ruling: s90_xexam_mimo_B2, item 2, R52 (W17.3)

*A fresh Claude checker, 24 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rules 1–5) and by "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling items 3–5: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*The file name the task gave ("ruling " + the whole call description + " item 2 R52.md") has 338 bytes, which is more than the 255-byte file-name limit. The file is therefore named in the pattern of the existing rulings.*

*What it read:*
- *the reply, all of it: the pass-2 reply `parts/s90_xexam_mimo_B2.response.txt`. Its receipt shows pass 2, attempt 1, status 200, finish "stop", `saw_done`, 0 bad chunks, response sha256 bbee0da8d374… matching the file, 805 words by `wc -w`, and END OF REPORT on the last line. Pass 1's two rejected replies (`content_filter`; `length` with no content) are recorded with pass 1 and were not opened;*
- *the change list's W17.3, W17.2 and W17.1 entries, and the revision note's row and line for R2-52;*
- *batch 1's and batch 2's readings, and the committed ruling files, for any earlier ruling on this entry;*
- *R52 as the part B2 brief gives it (brief md5 d214f495e0b9fcac4f423d522bee0d37, lines 860–880);*
- *Atria B2's point 2 and closing line, only because the task handed them to this checker. They are not weighed as a reply contesting R52, since Atria does not contest it.*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e, unchanged since 587eebf;*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923 (read only);*
- *the S81 case book (md5 4f488d14…), the S89 case book (md5 b2e53577…) and D3-T's `final.md`.*

*It opened no reasoning file.*

## 1. The entry and its checkers' history

W17.3, "L562 s3: Derivation 3's condition in the two defined terms".
- **Place:** Part XVI, Derivation 3, **Claim**, file-11 L562 s3, revised L566, from "it must be" to the end.
- **Group, item and reason word:** GROUP B2, ITEM W17, REASON WORD clarification. STATUS applied.
- **OLD:** `it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\).`
- **NEW:** `it must be a member of \(\mathcal T\), a transport the physics and the stated construction admit (Part XII), and it must survive on \(H\) (Part IV).`
- **KIND:** CLAIM.
- **DECLARATION:** "Derivation 3's claim now requires the differing transport to be a member of the population, a transport the physics and the stated construction admit, that survives on H. This replaces the list "admitted, realizable, a member of the population, and a survivor of H"."
- **CHECK:** "check 1, SOUND. CLAIM is defensible; a checker may rule it WORDING, given W17.1 and L473." The revision note (line 146) lists W17.3 among the declared entries a checker may rule down to WORDING.
- **REASON (not sent):** "The old sentence lists four conditions. Two of them, "admitted" and "realizable", are what L473 says membership is. "A survivor of H" was the ambiguous phrase that W17.1 now defines."
- **CASES AT RISK:** O48 and O24 stay AGREE; D3-T is secured, as for W17.1; N5 is as for W17.2. LOSS: none.
- **Its companion:** W17.2 (R42) changes L473 s1 from "a population of realized transports" to "a population of candidate transports". Its CHECK reads ""Realizable" alone suggests physics alone, the reading under which O48's wired arrangement is a member." Its declaration and LOSS state that the population is no longer described as realized transports only.

**Other readers and earlier rulings:**
- The single S90 call (C46) failed and supports nothing (S90 rule 4).
- Atria (s90_xexam_atria_B2) gives "R52: STANDS". Its point 2 says "Dropping "realizable" from the old list loses nothing, since Part XII makes physics-and-construction admission a condition of membership in \(\mathcal T\)." It does not contest R52.
- **No ruling in batch 1 or batch 2 is on this entry.** Batch 2 and the two R51 ruling files cite Derivation 3 "(L566, W17.3)" as unchanged support for O24. That agrees with the ruling below, so there is nothing to reconcile.

## 2. The reply's argument

The closing line is "R52: STANDS". Point 2 is headed "R52, task (a) — the declaration does not name the dropped condition "realizable."" It says:

> "The old list has four conditions; the new wording has three phrases, but Part XII already defines the population as "the set of transports the physics and the stated construction admit," so "a member of \(\mathcal T\)" and "a transport the physics and the stated construction admit" state one condition. The net replacement is four conditions down to two. The item "realizable" has no counterpart."

> "By displaying both lists, the declaration lets a careful reader see the drop. But it does not say that "realizable" is removed as a separate requirement or absorbed into "admitted." If "realizable" denoted a genuine physical condition—having a retained realization in the sense of (CT1), say—dropping it weakens Derivation 3's hypothesis and broadens its underdetermination conclusion. A one-line fix exists: append to the declaration "—the separate realizability condition is dropped.""

> "This point does not survive as a fatal defect, because the declaration does display both lists and the change is visible from them."

It names no case.

## 3. The texts

**1. The quotations are found (S90 rule 8).**
- OLD is file-11 L562 s3 and NEW is revised L566 s3, byte for byte as the reply quotes them.
- "the set of transports the physics and the stated construction admit" is at revised L475 (file-11 L473), last sentence, the same in both texts.
- (CT1) is revised L457–461 (file-11 L455–459).
- "requires three things" is the reply's paraphrase of the declaration, not a quotation. The declaration's words are as given in section 1.

**2. The reply's count is right.** Revised L475 says "The population is the set of transports the physics and the stated construction admit". So "a member of \(\mathcal T\)" and "a transport the physics and the stated construction admit" are one condition. Revised L195 (W17.1) makes survival include membership: "A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\)". So the NEW's whole condition comes down to "survives on \(H\)".

**3. "Realizable" is entailed by membership in both texts, so no condition is lost.**
- "Realizable" occurs once in file 11, at L562, and is defined nowhere. It occurs nowhere in the revised text.
- **In file 11**, L473 s1 calls the population "a population of realized transports". A realized transport is realizable, so "realizable" added nothing to "a member of \(\mathcal T\)".
- **In the revised text**, a member is "a transport the physics and the stated construction admit" (L475). In Part XII's terms, what the physics admits is what is physically possible: "Possibility is the absence of a law-imposed limit short of perfection on performance and retention" (Tasks, L455; file-11 L453). That is what "realizable" says in its plain sense. The drafters' own check on W17.2 reads "realizable" as "physics alone", which is weaker than physics together with the stated construction. On either reading, membership entails it.
- **So the NEW does not weaken Derivation 3's hypothesis, and it does not broaden its conclusion.** With the population read as each text gives it, every \(t'\) the old list admitted as a witness is a witness under the new wording, and every witness under the new wording meets all four old conditions. The one difference in who counts as a member, realized or only admitted, is made at L475 by R42, not here. "Realizable" was never a separate condition of the claim. It was one of the words for membership that W17 set out to make one.

**4. The reply's hypothetical reading has no footing in the texts.**
- **(CT1) is typed on something else.** RetReal\((\pi,T,C;\chi)\) takes a protocol, a task, a constructor attribute and enabling conditions (L457–461). Part XII uses it for what a system owns and retains: owned capability (L469), and deployment "as a retained capability" (L397). A population member \(t'\) of a selection history is not a protocol for a task. Nothing in file 11 ties "realizable" at L562 to (CT1).
- **A realized-only reading contradicts Derivation 3 in both texts.** Its proof (file-11 L564; revised L568) uses a transport "with \(L_{j}(a,b)\) altered to another admitted relation for one \((a,b)\notin H\)", that is, a hypothetical alternative. Its Consequence (file-11 L566; revised L570) speaks of "wherever its population admits an alternative". A condition that the witness have a retained realization would make the proof's witness fail the claim's own hypothesis.
- **Where file 11 did describe members as realized, the change is R42's, and R42 declares it.** Its declaration reads "Part XII now describes the population of a selection history as candidate transports, as Part IV does, not realized ones." Its LOSS says "A selection claim is no longer described as being about realized alternatives only." That is where the realized reading goes, and it is declared.

**5. The declaration is accurate.** Its first sentence is true of the NEW, clause by clause. Its second quotes the old list, correctly. The NEW claims no more and no less than the declaration says, because the one old item with no counterpart in the NEW (the reply's own finding) is one that membership already entails.

**6. The reply's fix would mis-declare.** "—the separate realizability condition is dropped" tells the reader that a condition of Derivation 3 has gone. That is the weakening that, by item 3, does not happen. It would also invite the (CT1) reading that item 4 finds unsupported. It is not taken.

**7. The cases.** The reply names none. The entry names O24, O48, N5 and D3-T. The S81 and S89 books were searched for "realiz" and "realis", and neither book uses either.
- **O48** ("every device in the stated population is built without that wire"; "The different response is imaginable and is not available"): the wired arrangement is excluded by membership, through the stated construction, in both texts. "Realizable" never excluded it, since the wire is physically possible. It stays AGREE.
- **O24** ("The setting is reachable by hand"): the second arrangement is a member and survives on \(H\). It is realizable on any reading. It stays AGREE.
- **N5** (the months reading and the seasons reading of the village rule): both readings are admitted transports that survive the home history. Whether they are "realizable" adds nothing. It stays as W17.2 leaves it.
- **D3-T** ("Both can be built"): the discarded design fails at a tested setting, so it does not survive on \(H\). Realizability is not what excludes it. The verdict stays No.
- **No mark moves** in either direction.

## 4. Ruling: KEEP

**On Parts rule 2.** The reply contests R52 by naming a possible undeclared change of claim: the loss of "realizable" as a separate condition. No such change exists. "Realizable" is entailed by membership in \(\mathcal T\) under file 11's L473 and under the revised L475. So the NEW keeps Derivation 3's hypothesis as it was, and the declaration, which quotes both lists, describes the change correctly.

OLD, NEW, KIND (CLAIM) and DECLARATION stay as drafted, and no text changes. The reply does not raise whether W17.3 should be WORDING, so that question is not ruled here.

**The CHECK-field note** (to append to W17.3's CHECK):

> After the cross-examination (S90, Mimo B2, point 2, R52 STANDS): the claim that the declaration does not say whether "realizable" is dropped was re-examined and ruled KEEP. "Realizable" is entailed by membership in both texts: file 11's population is of realized transports (L473 s1), and the revised text's population is what the physics and the stated construction admit (L475), which is physical possibility in Part XII's sense (Tasks) together with the construction. No condition of Derivation 3 is lost, and the declaration shows both lists. The reply's suggested addition ("the separate realizability condition is dropped") is not taken, because it would declare a weakening the new text does not make. (CT1) is typed on protocols and tasks, not on population members, and the realized-only reading belongs to W17.2, which declares it.

## 5. What follows

- **In the change list:** only the CHECK note above. There is no change to NEW, KIND, DECLARATION, CASES AT RISK, GAIN or LOSS. Being a KEEP, it adds nothing to the list of what the checks changed.
- **By program:** R2-52 stays CLAIM ("yes"), and N, M and K are unchanged.
- **Carried forward, not ruled:** nothing.
