# Ruling S93 X06 (W20.1): the commitments Γ of a candidate

*Written by a fresh Claude checker on 25 September 2026. The checker did not draft, assemble or check the change list, did not write the S93 briefs, and has read no S93 reply other than the two named below. It follows the S93 reading rule (rules 4, 5, 6, 9, 10, 11 and 12), decision S20 and lesson S26.*

**Texts read, in this order.**
- The S93 reading rule.
- Decision S20 and lesson S26.
- From the tabulation, only four parts: §2.2's X06 entry, §3.4, the X06 row of §6.3, and X06's entry in §7.
- The two replies. `s93_xexam_atria_H.response.txt` has md5 2e7241d50943d5945345ef41d4eca21f. `s93_xexam_mimo_H.response.txt` has md5 c74f416e38510d5fbc3e4ed3d4f6c2d1. Both finished "stop" on pass 1, with END OF REPORT as the last line.
- The part H brief (md5 4be1172e57216bd67a9a9dce66ba2040).
- From the change list (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40), W20.1 and the findings it carries forward.
- The draft-4 theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17).
- For background only:
  - the S90 ruling on R15;
  - `S90 Verification of draft 3.md`;
  - the S88 settled position on F3;
  - the F3 reading's models 1a and 1b.

I opened no other checker's ruling, no other item's section of the tabulation, and no other S93 reply.

**Rule 10.** No point on X06 disputes a fixed verdict.

**Rule 11.** No point on X06 was raised outside part H (tabulation §3.4).

## The entry

- **Place.** Part V, opening paragraph, draft 4 L231 (file 11 L233). The entry inserts one sentence after sentence 1. The NEW occurs once in draft 4, at L231 (checked by program).
- **OLD:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\).
````
- **NEW:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
````
- **KIND:** CLAIM. **REASON WORD:** clarification.
- **DECLARATION:** Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, whether or not anyone has described their work, and the organization's boundary values and its other components, including any that assigns an input, belong to the named background of Part VI.
- **CHECK field**, verbatim: "not put to check 1 or check 2, which ran before S88 was settled. The text is the settled wording (F3, block 2), copied byte for byte. Checked by its drafter as W19.1 was. No outside reader has seen this wording; X1 must carry it." Below it: "S90 cross-examination: s90_xexam_mimo_A1, point 2 (R15 STANDS, naming a move away on O45 on one reading) — FIX, after the cross-examination. Settled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined). The declaration follows the new clause. O45 moves from "watched, with a risk away" to "holds AGREE, on firmer text". Atria (s90_xexam_atria_A1, pass 2, point 5) read O45's second spring as a route "whether or not anyone described its work" and gave STANDS, which agrees."
- **CASES AT RISK, in brief.**
  - O45 holds AGREE, on firmer text.
  - O7 holds AGREE, and the entry says "The component that spreads or sweeps the salt assigns an input and is named background".
  - O5 holds.
  - Part VII's production case holds "under W20.2 on both identifications (models 1a and 1b)".
  - The skew-symmetric case holds.
  - O2 holds.
  - N1 is watched both ways, as W33.1 records.
  - O36, O46 and O47 hold.
- **LOSS**, verbatim: "Membership is the candidate's identification, not a test. A candidate that leaves out of Γ a component that does the work has it fixed as background, and non-circular dependence then has only the listed commitments to witness it."
- **What the drafters left open.** The change list carries two findings forward:
  - "W20.1's "including any that assigns an input" has two readings. On one, every component that assigns an input is outside Γ. On the other, any such component that the candidate leaves out of Γ is named background. The named verdicts are the same on both".
  - "'Active' is still undefined".

  S88's settled position says of the sentence that "the candidate's identification decides" membership. The F3 reading's model 1b is "the input-assigning components in Γ".

## Atria's argument

**Point 1 (T1): the input-assigner counterexample, reported as failing.**

*The argument.* Atria builds a component \(j\) that determines \(v\) from \(u\). \(A\) contains an edit \(a_v\) that sets \(v\) directly, so \(j\) "assigns an input". \(C\) never uses \(a_v\), and the answer depends on \(j\). Atria reads X06 as putting \(j\) outside Γ, so (F1) never checks \(j\) and (B) never records it. It then says the attack fails, for four reasons:
- L103 makes such a contribution "provisional";
- L255 forbids resting the answer on a value assigned to a settable port;
- (F2) still checks the assembled organization;
- "The exclusion is the theory's own, carried by unchanged lines; X06 only states it."

It adds that no listed situation turns on this.

*Quotations (rule 9).*
- "including any that assigns an input" is found at L231.
- The sentence ending "does not discharge this" is found at L255. The text puts "law" in double quotes.
- The cited places also check: L109, L103, (F1) at L233, (B) at L296, L287, and (F2) at L242.

*What the texts say.* The counterexample is sound on the strict reading, but the rescue is not in the texts:
- L103 says how an edit acts: it "replaces the component assigning that port". It says nothing about membership in Γ. On a contract that never uses the edit, it does not make the component's contribution provisional.
- L255 bars *the target's answer* from appearing "as an unanalysed boundary input or as a component". It does not bar an answer that depends on a component whose output port some admitted edit sets.
- (F2) is fidelity of the whole. It gives \(j\) no place in (S) or (B), and \(j\) cannot witness non-circular dependence.
- No unchanged line says that a component which assigns an input cannot be a commitment. The drafters' own record calls the clause two-way, and S88 settled that the candidate's identification decides.

So Atria's \(j\) shows the reverse of its conclusion. On the strict reading, a working component that the candidate offers as doing the work is inside Γ by the sentence's first half and outside it by the second half. That is Mimo's contradiction, with a better instance than Mimo's (ruling 1).

**Point 2 (T2): the kind is CLAIM, and the declaration is exact.**

*Quotations.* "an identified set \(\Gamma\) of active commitments in \(E\)" and "those the candidate offers as doing the work, whether or not anyone has described their work" are both found at L231. "identified active commitment" is Atria's own words.

*What the texts say.* Atria is right that the offer criterion and the clause about description change what a reader can conclude: O45's second spring is a commitment from the start. Mimo agrees that CLAIM is the kind (its point 4). But the declaration repeats both phrases that are faulted below, so it must follow any FIX of the NEW.

**Point 3 (T3): the "named background" is not circular, with an optional phrase.**

*Quotations.* "the named background of Part VI" is found at L231. "with the named background fixed" is found at L287. L231 and L287 are the phrase's only occurrences in draft 4.

*What the texts say.* Atria is right on the texts. L287 uses the background, and L231 now says what it contains. The optional phrase is "what Part VI calls the named background" (ruling 3).

**Point 4 (T4): verdict moves.**

*Quotations.* L307 is found, where the text opens "A route …" with a capital. "an unsupported belief riding along with a good explanation, not a part of it" and "Yes, Tomas explains the seasons" are found in brief H §7 (N1).

*What the texts say.*
- On O45, Atria agrees with the S90 fix and with the CASES AT RISK.
- On N1, Atria calls the sun-god sentence "squarely a commitment that does no work". That is one of the readings the change list keeps watched, both ways, under W33.1. X06 does not settle it, and Atria shows no move away from the fixed verdict.
- The other rows are correct.

**(d): RIGHT.**

*Quotations.*
- L315's "at some admitted edit–boundary pair … in \(C\) or outside it" is found.
- L317's "a conflict between ideas that what the assessor has established has not settled" is found.
- "two discovered variations that fit" is not found verbatim. The owner's words (brief H §2, line 28) read "If two discovered variations fit, that constitutes a problem". The paraphrase keeps the sense.
- The citations of L159, L562, L339 and L612 say what Atria uses them for. L159 is paraphrased.

## Mimo's argument

**Point 1 (T1): the two halves contradict, with a whole replacement proposed.**

*The argument.* Read strictly, the second half puts every component that assigns an input outside Γ, while the first half makes Γ exactly what the candidate offers as doing the work. Mimo's instance is Part VII's stipulation "Set \(b_B=0\)" at L331. Mimo says it is offered as the support and assigns the bias port, which calibration edits set. As background it would sit in every \(E|W\), no \(G\subseteq\Gamma\) could delete it, and "its support is circular" would have no object. Mimo's proposed repair adds "except that a component that assigns an input is never one of them", and replaces "boundary values" and the pointer.

*Quotations.*
- The L231 passages are found.
- L109 and L103 are found.
- L331 is found. The text puts the stipulation in double quotes, and the reply uses single quotes.
- "an independent calibration can" is found at L329. The reply cites L330, which is a blank line.
- L287 and (S) at L290 are found.

*What the texts say.* The logical point holds on the strict reading (ruling 1). The instance does not hold, for three reasons:
- L329 to L331 never say that \(A\) contains an edit setting \(b_B\) directly. "an independent calibration can" completes "Repeating rows changes no kernel": a calibration adds an independent reading, which changes the kernel. It is not an edit that sets \(b_B\).
- The stipulation is not given as a component of any candidate's \(E\) for a question \(p\).
- "its support is circular" speaks of the reason offered for the stipulation ("because it gives the mass I favour"), and L331 sets that against "an inference from the readings". That is support in the ordinary sense, the reasons for adopting something, which (E) leaves to Part IX (L277). It is not \(\mathsf S_{E,p}\), so "would have no object" does not follow.

**Point 2 (T3): the repairs Mimo proposes at L245, L299 and L558.**

*Quotations.* L245 ("every component of \(E\)"), L233 and L554 ("every active component \(k\) of \(E\)"), L299 ("commitments outside \(\Gamma\)") and L558 ("each component must anchor to a component of the same kind") are all found.

*What the texts say.*
- **L245.** The gap between L245's "every component of \(E\)" and the "every active component" of (F1) and Derivation 1 is real if "active component" means a member of Γ. But it predates X06:
  - L233 and L245 are unchanged;
  - "active" is undefined, as the change list records;
  - \(E\) already had components outside Γ (in Part VII's production case, \(H:=U_H\) and \(\theta:=U_\theta\), by the change list).

  X06 defines no "active", so its wording does not make L245 false. It makes the gap visible.
- **L299.** "commitments outside \(\Gamma\)" means what a support that someone could write would use and the written Γ lacks. In O36 that is a premise nobody has written, which is not a component of \(E\) at all. X06 types this candidate's commitments and leaves that phrase meaningful. Mimo's "components outside \(\Gamma\)" would narrow L299 to \(E\)'s background and lose the O36 sense.
- **L558.** The same holds as for L245.

**Point 3 (T3): "boundary values" is undefined, and the pointer does not deliver.**

*Quotations.* L91, L119, L189, L255 (twice), L231 and L287 are all found.

*What the texts say.* The first half of the point holds (ruling 2):
- "boundary values" occurs nowhere in draft 4 but L231;
- the datum is \(B\), "a set of boundary conditions", whose members are the "boundary \(b\)" of L91;
- elsewhere "values" is what ports take in a valuation or a solution (L91, L105, and L119's "not from the values its ports take in a solution");
- "boundary" also names the declared index \(\beta\) (L524).

The second half does not hold (ruling 3).

**Point 4 (T2): the kind is right, and a new declaration is proposed.**

*Quotations.* L231 and L255 are found.

*What the texts say.* The kind is agreed with Atria. Mimo's declaration follows Mimo's NEW, which is not taken, so the declaration follows ruling 1 instead.

**Point 5 (T4): no move away.**

*Quotations.* L307 (both passages), L313 and L273 are found.

*What the texts say.* This is agreed. Mimo reads N1 in two ways: the sun god is "either a no-work commitment or, if it assigns an input, background". Under the FIX the second branch no longer applies to a sentence that Tomas offers as keeping the tilt steady. That is how the change list's N1 note already reads it.

**(d): RIGHT, WITH A LOSS.**

*Quotations.*
- L11 is found.
- The three passages from L315 are found.
- L250, L568 and L612 check.
- "the sun god, who approves" is found in brief H §7 (N1).
- "the sun god, who is indifferent" is not found. It is Mimo's own variant.
- The owner's sentence is found at brief H §2, line 28.

## Rulings

### 1. The input-assigner clause (Mimo point 1 against Atria point 1): FIX, with a third wording

**The two sides.**
- **Mimo:** on the strict reading, the sentence contradicts itself for an offered component that assigns an input. It repairs this with an explicit exception: such a component is "never" a commitment.
- **Atria:** the exclusion is the theory's own (L103, L255, (F2)), no listed situation turns on it, and the entry is upheld.

The number of replies on each side decides nothing.

**The ruling.**
1. **The clause has two live readings.** "Any" ranges most naturally over "the components of \(E\) outside \(\Gamma\)", and on that reading nothing contradicts. But the strict reading is live:
   - both replies took it;
   - the change list records it as one of two readings;
   - one of the drafters' own carried-forward notes writes it that way ("puts the components that assign inputs in the named background").
2. **On the strict reading the sentence contradicts itself, for candidates the theory's own definitions produce.** A port is an input when \(A\) contains an edit that sets it directly (L109). The component that assigns that port is the one the edit replaces (L103). So any component whose output port an admitted edit sets "assigns an input", and Atria's \(j\) is one. The same holds for a causal assignment as L123 identifies it: its signature "changes under intervention on its output port", and it shows that change on \(C\) only when \(C\subseteq A\times B\) (L113) contains the intervention. On the strict reading, the first half puts such a component in Γ when the candidate offers it as doing the work, and the second half puts it out. That is incoherence, not a matter of emphasis. The production case even describes such an edit ("An intervention on \(L\) replaces its component", L325), while the change list puts the law in Γ.
3. **Atria's rescue is not in the texts** (see its point 1).
4. **Mimo's repair removes the contradiction the wrong way.** "Never one of them" turns the strict reading into a rule, and the edits \(A\) admits then override the offer criterion. Every component whose output some admitted edit sets would be fixed as background: every causal assignment identified on a contract that intervenes on its output, and O45's springs too, if the door's contract admits setting the door directly. Such a component cannot be deleted in non-circular dependence (L255) and is in no support (L287, L290). This would:
   - widen the declared LOSS from "a candidate that leaves out of Γ a component that does the work" to every candidate;
   - overturn S88's settlement that the candidate's identification decides;
   - exclude the F3 reading's model 1b;
   - put the production case at risk if \(A\) contains the intervention on \(L\) that L325 describes.

   It is a change of claim beyond the declaration, and it is not taken.
5. **The smallest change is "including any of them that assigns an input".** "Them" can only be the components of \(E\) outside Γ. The clause then says only that a component which assigns an input and which the candidate does not offer is named background, which is what S88 settled. The first half decides membership for every component, and no contradiction is left. The clause is kept, not deleted, because it answers S88 finding F3's question in place. Under the FIX, Atria's \(j\) is a commitment when the candidate offers it. It falls into the background only when the candidate leaves it out, which is the declared LOSS.

### 2. "boundary values" (Mimo point 3, first half): FIX

The sentence that gives every part of \(E\) a class uses a term that is never defined. The term points two ways: to port values, and to the index \(\beta\). The defined term is at hand ("\(B\) is a set of boundary conditions", L91; "its independent boundary conditions", L255). The smallest change is one word: "boundary values" becomes "boundary conditions". Mimo's added "(its \(B\), Part II)" is not needed, because "the boundary conditions of \(E\)" already names \(E\)'s \(B\) by L91.

### 3. "the named background of Part VI" (Mimo point 3, second half; Atria point 3 and its optional phrase): KEEP

"Of Part VI" says whose background this is: the one Part VI holds fixed in \(E|W\) (L287). The sentence itself says what the background contains. Nothing here is false, circular or misleading, and before X06, L287's "named" had nothing to name.

Atria's optional phrase, "what Part VI calls the named background", is ruled KEEP: the present wording stands without it. Mimo's "that Part VI holds fixed in \(E|W\)" is not taken either.

### 4. Kind and declaration (Atria point 2; Mimo point 4): KIND CLAIM is kept, and the declaration follows the FIX

**Does the FIX change what the theory claims?** Not on the reading the drafters settled, on which the CASES AT RISK and models 1a and 1b were written: it states that reading. It removes the other reading, so a reader can no longer conclude that no component which assigns an input can be a commitment. The declaration carries both faulted phrases, so it must change in the same two places to say exactly what the NEW says. The REASON WORD stays "clarification". Mimo's declaration is not taken.

### 5. Verdicts (Atria point 4; Mimo point 5), and the FIX's CASES AT RISK: no fixed verdict moves

- **O45** holds AGREE. The springs are contained, connected and sufficient, so they are offered, and "whether or not anyone has described their work" stands. The FIX removes a reading on which, under a contract that sets the door directly, both springs would be barred from Γ.
- **O46** holds: reassignment makes a new candidate (L307).
- **O36** holds: supports are subsets of the written Γ (L299).
- **O47** holds: interference (L309).
- **O2** holds: Carla offers both parts.
- **O5** holds (W20.2).
- **O7** holds on both identifications of the spreading component. Offered, its deletion leaves the salt port with the full relation and loses the contrast. Not offered, it is background, and the salt's action is the witness (W20.2; models 1a and 1b).
- **N1** is as the change list's note already reads it: the sun-god sentence is a commitment wherever it is a component, and W33.1's watch is unchanged.
- **Part VII's production case** holds on both identifications. **The skew-symmetric case** is untouched.
- "Boundary conditions" moves nothing.

### 6. The repairs at L245, L299 and L558 (Mimo point 2): not part of this FIX

X06's own wording does not make them necessary.
- **L245 and L558** go to a later entry (Findings, 1).
- **L299** is not taken (Mimo's argument, point 2).

### 7. (d), a choice for the owner (rule 6): not ruled KEEP, FIX or DROP

**Does the present wording state the matter truly?** Yes. L315 says openly what it requires and what it excludes:
- rivalry needs an offer "in place of the other" and a conflict "at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it";
- candidates that differ only in how they are written, and candidates that some admitted relations let both meet (F1), (F2) and (A), "conflict at no pair";
- "a candidate that nobody has offered is no one's rival".

Each loss Mimo names is a consequence the text states, not one it hides. The FIX leaves L315 unchanged.

**The two reasons, for the owner's word.**
- **Atria (RIGHT).** Only admitted pairs can be tested, and where there is no conflict there is nothing to settle. "Or outside it" is needed, because otherwise the second kind of problem, and with it "easy to vary", could never arise for two accounts. Recodings and inert parts correctly fall outside. What is given up follows from the owner's rule against grading and counting.
- **Mimo (RIGHT, WITH A LOSS).** The condition keeps mechanism rivals and correctly drops recodings and inert parts. But two discovered variations that both fit and differ only where no admitted change reaches pose no problem, although the owner's words read "If two discovered variations fit, that constitutes a problem". An offer "in place of" another is required where the owner makes discovery enough. And a pair that only one transport translates is never a conflict.

### The FIX, exact

- **OLD:** unchanged.
````text
and an identified set \(\Gamma\) of active commitments in \(E\).
````
- **NEW:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.
````
- **KIND:** CLAIM, unchanged. **REASON WORD:** clarification, unchanged.
- **DECLARATION:**
````text
Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, whether or not anyone has described their work, and the organization's boundary conditions and its other components, including any of them that assigns an input, belong to the named background of Part VI.
````
- **CHECK line (rule 12):**

  > S93 cross-examination: s93_xexam_mimo_H, points 1, 3 and 4, and s93_xexam_atria_H, points 1–4 — FIX, after the S93 cross-examination. "including any that assigns an input" becomes "including any of them that assigns an input", so that the candidate's offer decides membership for every component, as S88 settled and model 1b has it, and the reading on which the sentence contradicts itself for an offered component that assigns an input is gone. "boundary values" becomes "boundary conditions", the term of L91. Mimo's exception ("never one of them"), its declaration and its repairs at L245, L299 and L558 are not taken. Atria's optional phrase is not taken, and the pointer to Part VI is kept. The declaration follows. No fixed verdict moves.

- **Record edits that go with it:**
  - the carried-forward finding "W20.1's "including any that assigns an input" has two readings" is closed, and so is REASON's matching bullet under "Read in place";
  - in the carried-forward finding on "active", "puts the components that assign inputs in the named background" becomes "puts the components outside Γ, including any that assign inputs, in the named background";
  - in O7's CASES AT RISK, after "assigns an input and is named background", add "where the candidate does not offer it as doing the work; offered, it is a commitment, and O7 holds on both identifications (W20.2)".

  GAIN and LOSS are unchanged.

## Findings for later entries

1. **L245 and L558, and L281's argument, against (F1).** L245 says "every component of \(E\)" and L558 says "each component", while (F1) and Derivation 1 say "every active component" (L233, L554), and "active" is undefined.
   - If "active" means a member of Γ, L245 is false for the named background.
   - The Corollary's "adds nothing to (F1)" would then hold only for active components, even though \(\lambda\) gives every component of \(E\) an anchor (L189).

   This predates X06, and the change list already carries it ("'Active' is still undefined"). Candidate repairs:
   - Mimo's wording for L245 ("By (K), (F1) entails that every active component of \(E\) has the signature of its anchor; there is no further condition about kinds to state (Derivation 1)."), which says what Derivation 1 proves;
   - "each active component" at L558;
   - or a definition of "active component".

   Whether an anchoring condition on named-background components would then add something to (F1) and (F2) needs its own check, which is why this belongs to a later entry and not to this FIX.
2. **L325.** "\(L\) is an output, by Part II" stands next to "An intervention on \(L\) replaces its component". By L109, \(L\) is also an input if \(A\) contains that intervention. After the FIX no verdict turns on this, because the law is a commitment when it is offered either way. It is noted only. This checker has not read X11's material, which concerns the next sentence of L325.

## For the owner

- **(d) on X06.** The present wording of L315 states its condition and its exclusions truly. Two questions are the owner's choice, and both replies' reasons are set out in ruling 7:
  - whether "offered … in place of the other" renders the owner's "discovered" well enough;
  - whether "A variation is a competitor" should reach variations that no admitted change separates.
- **The choice in the FIX.** The FIX keeps what S88 settled: the candidate's offer decides membership, including for a component that assigns an input. Mimo proposed the opposite rule, that such a component is never a commitment. That rule is ruled out here as a change of claim that would fix working components as background. If the owner wants it, it needs a new declaration and a fresh check of Part VII's production case and O45.
- **The LOSS.** The declared LOSS stands: membership is the candidate's identification, not a test.

X06: FIX
