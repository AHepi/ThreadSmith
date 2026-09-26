# Ruling: s90_xexam_mimo_A1, R15 (W20.1)

Checker: a fresh Claude checker. It did not draft, assemble or check the change list, and did not write the S90 briefs. Rules applied: the S90 reading rule, 2, 3, 7 and 8, as extended by the S90 Parts rule, 1 to 4.

Why it is contested: the reply's line is "R15: STANDS", but its point 2 names a moved verdict on O45, conditional on one reading of the new phrase (Parts rule 2).

The call was accepted: the receipt says `accepted: true`, finish "stop", and the reply's last line is END OF REPORT.

Map: R15 = R2-15 = W20.1, file-11 L233, draft-2 L231 (the note's section 5 row; the Parts rule table, R15 row).

Texts read: the change list, unchanged since 587eebf (`git diff 587eebf HEAD` on it is empty); the draft 2 theory text, md5 9aecf2f30ce0b4523606b2b8409fdf37; file 11. Of the reply, only point 2 and the verdict lines were read.

## 1. The entry

- **OLD:** `and an identified set \(\Gamma\) of active commitments in \(E\).`
- **NEW:** `and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.`
- **KIND:** CLAIM. The reason word is "clarification".
- **DECLARATION:** Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, and the organization's boundary values and its other components, including any that assigns an input, belong to the named background of Part VI.
- **The checkers' verdict (CHECK field):**
  - The entry was not put to check 1 or check 2, which ran before S88 was settled.
  - Its text is the settled S88 wording (F3, block 2), copied byte for byte.
  - It was checked by its drafter only. No outside reader had seen the wording, and X1 must carry it.
- **Its own CASES AT RISK:** "O45: watched, with a risk away." The entry says:
  - A reader who takes "offers as doing the work" to need a description of the work puts the second spring in the named background, and "It was already a route" moves from AGREE to SPLIT.
  - The AGREE is held by L309 s3, W28.1 and W58(i).1.
  - "X1 should test this row."
- **The drafter's check** (the change list, L168 and L190) repeats this watch.

## 2. The reply's argument (point 2, "R15, tasks (a) and (c)")

> "The phrase admits two readings: (i) "identifies as part of the explanatory mechanism, whether or not their work has been described" and (ii) "explicitly describes as contributing." Under (ii), the second spring in O45 — "never described as doing anything until the first is deleted" — falls outside \(\Gamma\). The fixed verdict says it "was in the account from the start." Reading (ii) moves the theory's verdict away from the fixed one."
>
> "The body resolves the ambiguity toward (i). Part VI states: "A route already present in the candidate is a route whether or not anyone has described its work," and "the supports assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out." A careful reader who reaches Part VI adopts (i) and the verdict is preserved. But R15's declaration repeats the ambiguous phrase without resolving it, and the text forces only the ambiguity, not the resolution."
>
> "*Proposed repair.* Replace "those the candidate offers as doing the work" with "those the candidate identifies as active, whether or not their work has been described.""

**The quotations were checked (rule 8).** All are found:

- the R15 sentence at draft L231;
- "A route already present … described its work" at draft L307, Part VI, Redundant routes, s3;
- "the supports assessed … set them out" at draft L299;
- O45 in the S81 case book. The reply clips "… until the first is deleted from the account"; the clipping changes nothing. "was in the account from the start" is verbatim.

The reply's side points agree with the entry and are not contested:

- It takes "including any that assigns an input" on the second reading. The entry says the named verdicts are the same on both readings.
- O7 holds.
- R20 (W20.3, L287) is consistent with R15.

## 3. The texts and the case

**O45** (S81 case book):

- **Situation.** Two springs are in the account, both connected, both sufficient. The second is "never described as doing anything until the first is deleted".
- **Fixed verdict.** The second spring "was in the account from the start … It was already a route. That nobody said it did work does not make it a later addition."

**The membership question is the one that split O45 before.**

- In S87 part P3 (the O45 section), file 10's O45 is ruled SPLIT on "Reading 2". That reading says: "If the candidate as written identified only the described spring, the second spring was background. It became an active commitment, a route in Part VI's sense, only when the author named it after the deletion."
- File 11's AGREE rests on L309 s3 (draft L307) alone.
- The residual of 04c, recorded in the same place, says: "L309 s3's subject ("A route") could be read as presupposing membership in \(\Gamma\)."
- So the Part VI sentences that the reply relies on speak of routes and supports, and both are subsets of Γ. They say that description does not matter once a component is in Γ. They do not say that an undescribed component is in Γ.

**What W20.1 adds.** W20.1 is the first text that gives a rule of membership: "those the candidate offers as doing the work".

- To offer something as doing a thing is, in plain English, to put it forward as doing it. O45 stipulates that the second spring was never put forward as doing anything.
- So reading (ii) is not strained. It is arguably the natural reading in place, and it revives file 10's Reading 2 at the definition itself.
- Worked through on (ii):
  1. Γ = {spring 1}, and spring 2 is named background.
  2. By L299, spring 2 is in no support ("not a support someone could write with commitments outside Γ"), so it is not a route.
  3. Under W20.2, deleting G = {spring 1} leaves spring 2 fixed in the background, and the door still returns. The contrast is not lost, so on this reading the candidate may fail (E) outright.
  4. The verdict "It was already a route" moves away.

**What resolves it toward (i).** The rest of the text supports (i), but only by coherence:

- L307 s3 and L299 ("whether or not anyone has …");
- L265, "None inspects a label", which governs the conjuncts of (E), not the identification of Γ;
- L127, "Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording", which is about measurement against production, not membership.

None of these states that a component can be offered as doing the work without its work being described. Given 04c's residual, "a careful reader adopts (i)" holds, but the text does not force it. The reply's claim is correct: the new sentence opens the risk, and only an inference from later text closes it.

**Other rows.** The fix below only removes "a description of the work" as a condition of membership. Membership stays the candidate's identification. So:

- **N1 (O53):** the sun-god sentence is offered, with its work described ("keeps the tilt steady"). No effect.
- **O2:** Carla offers both parts. No effect.
- **O7, Part VII's production case and the skew-symmetric case:** these turn on input-assigning and held-fixed components, not on description. No effect.
- **O36, O46 and O47:** supports stay subsets of the written Γ. A reassigned cable is still a new candidate (L307 s3, second clause). No effect.
- **The S89 N-cases:** none turns on an undescribed component. D3-T is not reached.
- **The LOSS stands.** "A candidate that leaves out of Γ a component that does the work has it fixed as background" is unchanged, because leaving a component out is not the same as leaving its work undescribed.

## 4. Ruling: FIX

The argument succeeds against the sentence as drafted, but not as a moved verdict on the whole text. The reply itself grants that the verdict is preserved on (i). The drafter pre-registered exactly this risk and asked X1 to test the row. X1 confirms that the membership rule, read in place, admits the reading that moves O45, and that the only rescue is Part VI text whose subject presupposes membership. The definition should carry the answer itself.

**The reply's own wording is declined.**

- "Identifies as active" brings back "active", which the settled S88 position declined because it is undefined. The change list's findings still record it as undefined.
- It would also make Γ circular: Γ is the "active commitments", which would be "those the candidate identifies as active".

**Only its second half is taken, in the theory's own words from L307 s3.**

- **OLD:** unchanged.
- **NEW (exact):**
````text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
````
- **KIND:** CLAIM, unchanged. The reason word stays "clarification".
- **DECLARATION (exact):** Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, whether or not anyone has described their work, and the organization's boundary values and its other components, including any that assigns an input, belong to the named background of Part VI.
- **Record as after the cross-examination**, in the CHECK and REASON fields: "settled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined)".
- **Change O45's CASES AT RISK** from "watched, with a risk away" to "holds AGREE, on firmer text (W20.1 now states that membership does not wait on a description; L309 s3, W28.1 and W58(i).1 agree)".
- **Follow-on edits** in the same list, which are not conflicts:
  - the drafter's check line "Watched, with a risk away: O45 under W20.1 …" (the change list, L168);
  - the carried-forward finding "O45 against W20.1's …" (L190).

**Conflicts with other entries.** None found.

- W20.1 is the only entry at file-11 L233, and its OLD is unchanged, so the applier's anchor holds.
- The following agree with the new clause: W28.1; W3.5 (layer 2, row L2-17, L309 s3, unchanged); W58(i).1 (L301); W20.2 (S3 and the deletion rider); W20.3 (L289, "the commitments of \(E|W\) are \(W\)"); and L2-05 (L129, what an account offers is not settled by its wording).
- The new clause adds no term and no symbol.
- The note's R2-15 line and the counts follow by program when the draft is rebuilt.
- If another reply's checker rules on R15 with other wording at L231, the two rulings must be reconciled.
