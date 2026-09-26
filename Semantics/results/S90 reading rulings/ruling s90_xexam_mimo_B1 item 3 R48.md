# Ruling: s90_xexam_mimo_B1, item 3, R48 (W7.5)

*A fresh Claude checker, 23 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*What it read:*
- *the reply's point 3 (R48) and its closing lines. The receipt shows the reply was accepted (finish "stop", accepted, response sha256 b67c7207… matching), and the last line is END OF REPORT;*
- *the change list's W7.5, W7.4, W7.6 and W3.2 entries, and its "Findings carried forward" (finding 9);*
- *batch 1's reading, for any earlier ruling on this entry;*
- *R48 as the part B1 brief gives it (brief md5 130a5eace514ebb02b736d12a311ade2, lines 880–898).*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e, as of 587eebf;*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923;*
- *the S81 case book (md5 4f488d14…) and the S89 case book (md5 b2e53577…).*

*It opened no other S90 return and no reasoning file.*

## 1. The entry and its checkers' history

W7.5, "L518 s9–s11: Ownership, owned capability, ProducedBy and the obligations".
- **Place:** Part XIV, "Dependence order", file-11 L518, revised L520. The sentences on Build, (N) and (G), and (P) and (EK).
- **Group, item and reason word:** GROUP B1, ITEM W7, REASON WORD erratum. STATUS applied.
- **Its neighbours in the same paragraph:** W7.4 (R47) changes s1. W3.2 (record only) declares the last sentence, which is kept word for word. The two sentences "(E) depends on those." and "(S), (B), (D) depend on (E)." are left free for W20. No anchor overlaps.

- **OLD:** `Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy.`
- **NEW:** `Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, and ProducedBy on histories and their active routes.`
- **KIND:** CLAIM.
- **DECLARATION:** "Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, and (P) on ProducedBy and the declared obligations with their occasions, and ProducedBy on histories and their active routes."
- **CHECK:** "check 1, SOUND. The order still omits Result, ProducesVia, Cap and Enable (B1 finding 9)."
- **REASON, "Not corrected":** "'(P), (EK) depend on (G), (E), Deploy' is kept, although (P)'s definition does not use (G), (E) or Deploy. As a dependence it is an over-statement and does not harm well-foundedness. Correcting it lies outside W7."
- **Findings carried forward, finding 9:** "The dependence order is still a summary … After W7.4–W7.5 it omits (K2), receipts, (K3), (CA), (CT2)–(CT4), Barriers, Enable, Scrutinizability, Membership, Result, ProducesVia and Cap. '(P), (EK) depend on (G), (E), Deploy' over-states (P)'s dependence and is kept." (EK)'s dependence on (P) is not in that list.
- **CASES AT RISK:** O49 and O37 stay AGREE; O35 and O38 rest on L514's unchanged input; the boundary rows are as in W7.3; "No N-case cites the dependence order."
- **The paired proof:** W7.6 (R53) rewrites Derivation 6's proof to "By the dependence order of Part XIV, which lists the declared indices and the declared inputs with the definitions that rest on them, following each definition to its base in the primitives, the indices and the inputs." Its REASON: "The proof now cites the order as W7.4 and W7.5 extend it."

**Other readers:**
- The single S90 call (C43) failed and supports nothing (S90 rule 4).
- Atria (s90_xexam_atria_B1) gives "R48: STANDS". Batch 1's reading lists R48 among the changes its points 2–9 test and find standing, with no undeclared change of claim or moved verdict named. Not contested there.
- **Batch 1 made no ruling on this entry.** There is nothing to reconcile.

## 2. The reply's argument

The closing line is "R48: STANDS". Point 3 is headed "R48 (task a, task c) — the modified passage over-attributes dependencies to (P)." It makes two claims and a repair.

**First, the over-statement for (P), now in a new form.**

> "The addition of ProducedBy and the obligations is correct: (P) (Repair, line 438) is defined as "∃o∈O[¬o(ξ) ∧ o(ξ')] ∧ ∀r∈P[r(ξ) ⇒ r(ξ')] ∧ ProducedBy(Δ,ξ,ξ';O)"—it uses only the obligations and ProducedBy. But the unchanged clause "(P), (EK) depend on (G), (E), Deploy" attributes (G) (Origin), (E) (Account), and Deploy to (P). … The composite claim—(P) depends on five things, three of which it does not use—contradicts (P)'s definition."

> "R48's declaration … does not mention the (G), (E), Deploy attribution. … It says in both texts what it said before, but in the *combined* new sentence it now reads as the baseline from which (P)'s "also" dependencies are added, giving the error a form it did not have before ("(P) also on…" presupposes the prior list is correct for (P))."

**Second, (EK)'s dependence on (P) is never stated.**

> "Additionally, (EK) uses Repair (line 443: "∧ Repair_{O,P}(ξ,ξ';Δ)"), so (EK) depends on (P). The grouping "(P), (EK) depend on…" never says this. The passage R48 is rewriting as erratum carries two structural errors; R48 fixes neither."

**Its own weighting, and a repair.**

> "This is partly pre-existing, which is why R48 does not fall on it alone. But the repair should accompany the change. **Suggested repair** for the shared clause: "(EK) depends on (G), (E), Deploy and (P). (P) depends on ProducedBy and on the declared obligations with their occasions, and ProducedBy on histories and their active routes.""

The point names no case.

## 3. The texts

**1. The quotations are found (S90 rule 8); three line numbers are wrong.**
- The NEW sentence is found at revised L520, byte for byte as the reply quotes it.
- (P)'s definiens is found at revised **L432** (tag (P)), not "line 438". Rendered from its LaTeX it reads as the reply quotes it.
- "Attempt ∧ New ∧ Build" is (G) at revised **L416**, not "line 371" (L371 is "Bearing"; "Histories" is L369).
- "∧ Repair_{O,P}(ξ,ξ';Δ)" is in (EK) at revised **L441**, not "line 443" (L443 is (EK)'s last line: Account, Result, Deploy, ProducesVia).
- The declaration phrase is found in the brief's declaration, which is the entry's.
- The quotations hold on their content. The wrong line numbers change nothing.

**2. The definitions (revised text).**
- (P), L432: `Repair_{O,P}(ξ,ξ';Δ) ⇔ ∃o∈O[¬o(ξ)∧o(ξ')] ∧ ∀r∈P[r(ξ)⇒r(ξ')] ∧ ProducedBy(Δ,ξ,ξ';O)`. L435: the obligations are declared inputs, stated conditions over stated occasions; "ProducedBy holds when an active route (Part IX) runs from Δ to the repair". (P)'s definiens names neither (G) nor (E) nor Deploy.
- (EK), L440–444: `CreativeCriticalEpisode ∧ Repair_{O,P}(ξ,ξ';Δ) ∧ ∃o∈O_ep ∃c,p_c,e_c [e_c ⪯_h e ∧ ¬o(ξ) ∧ o(ξ') ∧ Origin(…) ∧ Account(c,p_c) ∧ c∈Result(Δ) ∧ Deploy(s,c,ξ';U_c) ∧ ProducesVia(…)]`. So (EK) uses (P) by name, uses the obligations directly (O_ep ⊆ O), and uses (G), (E) and Deploy.
- Active route, L369: "a connected subnetwork of actual occurrences joining a **represented** input to an operative result, whose components satisfy the applicable relations and which has nonconstant dependence on the **represented** distinction under the declared contrasts."
- Epistemic obligation, L437: "An epistemic obligation requires a correct account, or the correction of a use through one, to be deployable." An obligation in O can therefore be a condition stated with Account and Deploy.

**3. File 11 around the change.** File-11 L518 has "(P), (EK) depend on (G), (E), Deploy." and nothing else on (P) or (EK). The order there names no declared input and no ProducedBy. Derivation 6's proof (file-11 L588) reads "By the dependence order of Part XIV, following each definition to its base."

**4. The first claim names no change of claim.**
- The clause "(P), (EK) depend on (G), (E), Deploy" is word for word the same in both texts, and says in both that (P) depends on (G), (E) and Deploy. The reply grants this: "It says in both texts what it said before".
- "(P) also on …" adds ProducedBy and the obligations, which is exactly what the declaration names. It asserts nothing about (G), (E) or Deploy that the old sentence did not.
- "A form it did not have before" is a point about emphasis, not content. The revised text neither starts nor stops claiming anything about (P)'s place after (G), (E) and Deploy.
- **So, on this claim, the reply names no undeclared change of claim under Parts rule 2 (S90 rule 2).** The over-statement is pre-existing, and the entry records it twice ("Not corrected" and finding 9).

**5. The over-statement is only partly an over-statement, and deleting it would trade it for an under-statement.**
- **(G)** is plainly spurious for (P): nothing in (P) or in ProducedBy uses Attempt, New or Build.
- **(E) and Deploy** are not in (P)'s definiens, but they are not idle in the order:
  - ProducedBy rests on active routes, and L369 defines an active route through a *represented* input and a *represented* distinction. That reaches (R). In the order as R48 drafts it, (P) reaches (R) only through (E) and Deploy ("(E) depends on those", "(R) depends on (F1)–(F2)…", "Deploy depends on (R) and (CT1)"). "ProducedBy on histories and their active routes" does not reach (R) by itself.
  - An obligation in O may be epistemic (L437), a condition stated with Account and Deploy. (P) evaluates o(ξ) and o(ξ′) for every o in O.
- **The reply's repair** ("(P) depends on ProducedBy and on the declared obligations with their occasions, and ProducedBy on histories and their active routes") drops (G), (E) and Deploy from (P) and adds nothing in their place. (P) would then no longer reach (R) in the order. Derivation 6's proof follows "each definition to its base". An over-statement does not hurt that; an under-statement does. The repair would trade a harmless over-statement for a possible under-statement that no reply has examined.
- **So the first half of the repair is not taken.** The entry's decision stands: the over-statement is kept and recorded. What active routes depend on is carried forward (section 5), not ruled here.

**6. The second claim is a real gap, and R48 opens it.**
- **(EK) rests directly on a declared input.** Its definiens has Repair_{O,P} and ∃o∈O_ep with ¬o(ξ)∧o(ξ′). L514 lists "the obligations O and P of a repair, with the occasions each covers" among the declared inputs.
- **In the order as R48 drafts it, (EK) never reaches the obligations.** Its stated bases are (G), (E) and Deploy. (G) reaches Deploy, Build, Ownership, a declared boundary, histories and (E). Deploy reaches (R) and (CT1). None of these reaches O, P or ProducedBy. Only (P) is now tied to them, and (EK) is not tied to (P).
- **In file 11 this lost nothing.** (P) and (EK) had the same stated bases, so (EK)'s list covered all of (P)'s. The order named no declared input and no ProducedBy for either. R48 gives (P) further bases and does not give them to (EK), so for the first time (EK)'s stated bases do not cover (P)'s.
- **R48 and R53 together say more than the order gives.** R53's proof now says the order "lists the declared indices and the declared inputs with the definitions that rest on them, following each definition to its base in the primitives, the indices and the inputs". (EK) is in the order and rests on the declared obligations, but following it in the order does not reach them. W7's own ground is XR6 ("the order lists none of the definitions that rest on one"), and R48 exists to close it. It closes it for (P) and leaves (EK), in the same sentence, open.
- **Finding 9 does not cover this.** It admits the omission of Result and ProducesVia, (EK)'s own conjuncts, but not of (EK)→(P). The dependence is the one that carries (EK) to the declared inputs.
- **The repair is one true clause.** "(EK) also on (P)" is (EK)'s definition read off (L441). It adds a base, so it cannot under-state anything. It creates no circle, since (P) does not use (EK), so the last sentence of L520 (well-foundedness, M49) is untouched.

**7. The cases.**
- The reply names none. The entry names O35, O37, O38 and O49, and the brief gives O35 and O37.
  - **O35** ("Four seconds") and **O38** ("Written on the job sheet") turn on how a protected condition covers its occasions (L435, and L514's list), not on where (P) or (EK) sits in the order.
  - **O37** ("The uncited textbook") turns on L520's last sentence, which is unchanged.
  - **O49** ("Owned means capable") turns on Ownership before owned capability and on the last sentence. Both are unchanged by the fix.
- The S81 book was searched for "depends on", "dependence" and "repair". The hits are O32 ("the pressure depends on the second pump") and O44 ("Most of the copy depends on the source"). Both are about dependence in a history, not the order.
- The S89 book was searched for "depend", "well founded", "in a circle" and "repair". No case cites the dependence order.
- **No mark moves under the fix,** in either direction.

**8. W20 is not touched.** The fix is in the (P)/(EK) sentence. The two sentences left free for W20's rider ("(E) depends on those." and "(S), (B), (D) depend on (E).") and L520's last sentence stay as they are.

## 4. Ruling: FIX (NEW and DECLARATION; OLD and KIND unchanged)

**On Parts rule 2.**
- The reply's first claim does not name an undeclared change of claim. The objected clause says the same thing in both texts, and what R48 adds is declared.
- The reply's second claim names a gap that R48 opens in the order it declares, together with R53's proof. It is fixed in the entry itself, with a declared clause.

**OLD** (unchanged):
````text
Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy.
````

**NEW** (corrected):
````text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, (EK) also on (P), and ProducedBy on histories and their active routes.
````
The only change to the drafted NEW is the inserted clause "(EK) also on (P), ", after "with their occasions," and before "and ProducedBy".

**KIND:** CLAIM (unchanged).

**DECLARATION** (corrected):
> Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, (P) on ProducedBy and the declared obligations with their occasions, (EK) on (P), and ProducedBy on histories and their active routes.

**Reason** (for the entry, marked as after the cross-examination): (EK) uses Repair_{O,P} and the obligations O_ep ⊆ O (L440–443). As drafted, the order gave (P) its bases in ProducedBy and the declared obligations and left (EK), in the same sentence, with no route to them. Derivation 6's proof as W7.6 words it follows each definition to the declared inputs through this order. The clause states a dependence (EK)'s definition already has. It moves no case, touches neither W20's two free sentences nor the last sentence, and creates no circle (Mimo, s90_xexam_mimo_B1, point 3).

**Not taken: the reply's rewording for (P).** Removing "(G), (E), Deploy" from (P) would leave (P) no route in the order to (R), which active routes (L369, "a represented input … the represented distinction") and epistemic obligations (L437) bring in. It would trade a recorded over-statement that is harmless to Derivation 6 for an under-statement that is not. The REASON's "Not corrected" and finding 9 stay. "Not corrected" gains one sentence: "Kept after the cross-examination: only (G) is plainly idle for (P), and (E) and Deploy carry (P)'s route to (R) through active routes and epistemic obligations."

## 5. What follows, and what is carried forward

**In the change list:**
- W7.5's NEW and DECLARATION as above.
- CHECK: add "After the cross-examination (Mimo B1, point 3): FIX, '(EK) also on (P)' added; the over-statement for (P) kept."
- REASON: add the reason above, and the one sentence under "Not corrected".
- CASES AT RISK: no change. GAIN: add "(EK) reaches the declared obligations through (P)." LOSS: none.
- The list of what the checks changed gets one line.
- Finding 9 is unchanged in substance. It may add that (EK)→(P) is now stated.

**By program:** the revision note's row R2-48 stays CLAIM ("yes"). N, M and K are unchanged. The note's line for R2-48 follows the new declaration when the draft is rebuilt. The new NEW occurs once in the rebuilt draft and overlaps no other entry.

**Carried forward, not ruled:** what an active route depends on. L369 defines it through a represented input and a represented distinction "under the declared contrasts". The order does not place active routes, and L514 does not list declared contrasts. This is the same summary looseness as finding 9, and no reply raised it.
