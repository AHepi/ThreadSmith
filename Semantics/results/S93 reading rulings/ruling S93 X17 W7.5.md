# Ruling S93 X17 · W7.5 · Part XIV, "Dependence order", L526 · CLAIM · part K

*A fresh Claude checker, 25 September 2026, under rules 4, 5, 9, 11 and 12 of "S93 How the cross-examination of draft 4 will be read - written before sending.md". It did not draft, assemble or check the change list, did not write the briefs, and has read no S93 reply other than those named below. A first checker for this item was lost in a restart before it wrote anything; this one started from scratch.*

*What it read:*
- *the reading rule (all of it);*
- *in "S93 Tabulation of the replies, before any ruling.md": only §2.2's entry for X17, §3.9 (X17's digest) and X17's entry in §7;*
- *the two replies §7 names, `s93_xexam_atria_K.response.txt` and `s93_xexam_mimo_K.response.txt`, whole (both end "END OF REPORT"; their X16 points were read only as context and are not ruled here);*
- *the brief, "S93 Cross-examination - draft 4 - part K, the normative relation, and the dependence order.md" (sections 1, 2, 4, 5, 6 and 7, and the excerpts it prints);*
- *the part A and part B replies (`s93_xexam_atria_A`, `s93_xexam_mimo_A`, `s93_xexam_atria_B`, `s93_xexam_mimo_B`, `.response.txt`), searched for points on the dependence order (see "Points from other parts");*
- *the change list (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40): W7.5, with W7.4, W7.6 and W3.2 beside it, W59.1's REASON on "established", finding 9 ("The dependence order is still a summary"), "Found in draft 4" and "Carried forward after S90";*
- *for background, the S90 ruling on R48 ("ruling s90_xexam_mimo_B1 item 3 R48.md") and the W7.5 rows of "S90 Verification of draft 3.md";*
- *the draft-4 theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), L29–L31, L65–L77, L285–L317, L351–L369, L373–L531 and L594–L600, and file 11's L518 (md5 5e494c1095d920d128b9a79de378f923).*

*It opened no other checker's ruling, no other item's section of the tabulation, no reasoning or attempt file, and not the scratchpad key file.*

## The entry

W7.5, "L518 s9–s11: Ownership, owned capability, ProducedBy and the obligations". STATUS applied; GROUP B1; ITEM W7; FILE-11 LINE 518; REASON WORD erratum. Draft 4 places it in Part XIV, "Dependence order", L526. Draft 4 left it as draft 3 has it, after the S90 fix.

- **OLD:**
````text
Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy.
````
- **NEW:**
````text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, (EK) also on (P), and ProducedBy on histories and their active routes.
````
- **KIND:** CLAIM.
- **DECLARATION:** "Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, (P) on ProducedBy and the declared obligations with their occasions, (EK) on (P), and ProducedBy on histories and their active routes."
- **CHECK:** "check 1, SOUND. The order still omits Result, ProducesVia, Cap and Enable (B1 finding 9)." Then: "S90 cross-examination: s90_xexam_mimo_B1, point 3 (R48 STANDS, naming an undeclared change of claim on one reading) — FIX, after the cross-examination. After the cross-examination (Mimo B1, point 3): FIX, '(EK) also on (P)' added; the over-statement for (P) kept."

What the entry says about the order, beside those fields:
- REASON, "Not corrected": "(P), (EK) depend on (G), (E), Deploy" is kept as a harmless over-statement.
- REASON, after S90: the clause "(EK) also on (P)" was added because the order "left (EK) ... with no route" to the declared obligations, and "Derivation 6's proof as W7.6 words it follows each definition to the declared inputs through this order".
- GAIN: "Derivation 6's proof has an order that reaches the declared inputs and the definitions that rest on them. (EK) reaches the declared obligations through (P)."
- CASES AT RISK: O49 and O37 stay AGREE; O35 and O38 rest on the unchanged input; "No N-case cites the dependence order. This was checked."
- Finding 9 (change list, "Findings carried forward"): "The dependence order is still a summary". After W7.4–W7.5 it omits "(K2), receipts, (K3), (CA), (CT2)–(CT4), Barriers, Enable, Scrutinizability, Membership, Result, ProducesVia and Cap".
- "Found in draft 4": "The dependence order does not place the new terms", which it says are defined "with no new primitive or declared input, so Derivation 6 still holds". It offers candidate words at the free sentence "(S), (B), (D) depend on (E).", which lies outside W7.5.

The draft-4 line as it stands (L526), for reference: the order runs from "(O) and (Q) depend on nothing" through W7.5's sentences to "(RC), (U1)–(U3) depend on all of the above", then "Nothing depends on a predicate meaning ...", then the well-foundedness sentence (W3.2, record only). No entry touches "(RC), (U1)–(U3) depend on all of the above." (checked in the change list; only W7.4, W7.5 and W3.2 name file-11 L518).

## Atria's argument

The receipt was not opened; the reply ends "END OF REPORT" and its closing line is `X17: UPHELD — every added dependence is supported by Parts X–XII, the declaration matches the new wording clause for clause, no verdict moves, and the order's silence on Part VI's rival/problem terms is a pre-existing incompleteness, not a falsity X17 introduces.` It makes five points on X17, each an attack it reports as failing.

**A1 · T3, the directed question (reply lines 3–9).**
- *Attack.* Part VI now defines rivals, conflict, established, fits and a problem for \(p\) (L315, L317). The order places none of them: its Part VI entry is only "(S), (B), (D) depend on (E)". So Derivation 6's claim (L596), proved "By the dependence order of Part XIV" (L598), "is not carried by the order as written".
- *Why Atria says it fails against X17.* X17's span neither adds nor removes a placement for these terms, and its declaration claims nothing about them. "The gap predates X17 and belongs to the items that introduced lines 315/317."
- *Its answer to the question.* The order "stays true". No entry X17 adds is contradicted by the new terms. "(RC), (U1)–(U3) depend on all of the above" claims dependence on the listed items only. The "Nothing depends on ..." sentence "does not touch rivals". "The order is incomplete, not untrue; the incompleteness is not X17's."
- *Quotation check (rule 9).* "(S), (B), (D) depend on (E)": found, L526. The L596 claim: found, rendered from its LaTeX. "By the dependence order of Part XIV": found, L598. X17's span: found, L526. "(P) also on ProducedBy and on the declared obligations with their occasions": found, L526. The L441 sentence on \(r(\xi')\) and "ProducedBy holds when an active route (Part IX) runs from Δ to the repair": found, L441, rendered. "the obligations O and P of a repair, with the occasions each covers": found, L522. "(RC), (U1)–(U3) depend on all of the above": found, L526. The "Nothing depends on ..." sentence: found, L526; the reply uses single inner quotation marks where the text has double. All found.

**A2 · T1 (line 13–15).**
- *Attack.* "Build depends on histories, Ownership and (E)" is imprecise. Build (L405) needs a represented organization, hence (R), which the order puts on "(F1)–(F2) and physical provenance", not on (E) as a whole. And (EK) separately needs Account.
- *Why it fails.* "(E)" is carried over verbatim from the old wording; X17 declares only the added Ownership. "for explanatory use of \(c\)" and "the resulting representation" (L405) read on Part V and on the fidelity conditions. Every addition is supported: Ownership (L427, L473, L475), owned capability (L475), (P) (L438), (EK) on (P) (L447, where Repair\(_{O,P}\) is a conjunct), ProducedBy (L375, L441). There is no cycle: histories, boundary and continuity are base items, and capability comes after Ownership.
- *Quotation check.* The L405 fragments, "(F1)–(F2) and physical provenance" (L526), the Can sentence (L475, rendered) and "nor do the declared indices and the declared inputs, which are stated, not derived" (L526): all found. The reply puts Account\((c,p_c)\) at "line 448"; it stands at L449. The slip changes nothing.

**A3 · T2 (lines 17–21).**
- *Attack.* The declaration's "Build on Ownership" leaves out histories and (E).
- *Why it fails.* A declaration reports what changes, and histories and (E) are kept. CLAIM is the right kind: the new wording lets a reader conclude that (EK) depends on (P), owned capability on Ownership, and ProducedBy on histories and active routes.
- *Quotation check.* "Build on Ownership": found in the brief's declaration (brief l.615). "(EK) also on (P)" and "(P), (EK) depend on (G), (E), Deploy": found, L526.

**A4 · T4 (lines 23–35).** No move on O49, O35, O38 or O37.
- O49 is already carried by L475 ("'owned because it can, and can because owned' grounds neither") and by the unchanged well-foundedness sentence.
- O35 and O38 are fixed by (P)'s unchanged reading at L441.
- O37 rests on the unchanged well-foundedness sentence.
- *Quotation check.* L475: found. The well-foundedness fragment: found at L526, which has a comma after "each other" that the reply drops. "a separate proof that would supply it counts only when the account uses it": found, L526. "owned means capable": the case title, brief l.691.

**A5 · (a), as a point (line 39).** Faithful. X17 adds no record or log. The anti-record wording stands at L369, "with no record of which candidates failed before or of how any was changed", found.

## Mimo's argument

The receipt was not opened; the reply ends "END OF REPORT" and its closing line is `X17: CHALLENGED — (EK)'s entry omits the declared obligations with their occasions and ProducesVia, which (EK) uses directly and not only through (P)`. Its X17 points are 1, 2, 3, 4, 5 and 9.

**M1 · point 1, T1: the challenge (reply lines 3–27).**
- *Claim.* (EK) is placed on "(G), (E), Deploy" and "(P)", but its definiens tests \(\neg o(\xi)\land o(\xi')\) over \(O_{\mathrm{ep}}\subseteq O\). That is a direct use of the declared obligations and their occasions. It also uses ProducesVia (L453), which is not ProducedBy.
- *Its standard.* It reads the item's own standard from its reason word, "erratum". The old entry was wrong because (P) is defined with the obligations and ProducedBy, "So a condition's declared inputs and named predicates must appear in the order". On that standard "(EK) also on (P)" is "false read as an exhaustive entry".
- *Its model.* \(O=\{o_1,o_2\}\), with \(o_1(\xi)\) false, \(o_2(\xi)\) true, both true at \(\xi'\), and \(P\) and ProducedBy holding. Then Repair\(_{O,P}\) holds. With \(O_{\mathrm{ep}}=\{o_1\}\) (EK) can hold; with \(O_{\mathrm{ep}}=\{o_2\}\) its existential fails. "(P) is untouched."
- *Proposed wording.* It proposes a NEW and a declaration that add to (EK) "on the declared obligations with their occasions through \(O_{\mathrm{ep}}\), and on ProducesVia", and add "ProducesVia on those and on the binding of \(c\)". Both are printed in the tabulation, §3.9, X17.6, and in the reply, lines 17–25.
- *What it leaves unpressed.* Result and CreativeCriticalEpisode for (EK), Attempt for (G), the restriction operation for (S), \(\mathcal V\) for (D), called "coarseness the order has always had". It also notes that \(O_{\mathrm{ep}}\) "appears in no list of declared inputs".
- *Quotation check (rule 9).*
  - The block quotation of (EK) (reply line 7) is **not found word for word**. It is a condensed rendering of L446–L450 that drops the argument lists of CreativeCriticalEpisode, Origin and Deploy. Its conjuncts and their order are otherwise the text's, so the point is ruled on L446–L450 as they stand.
  - "With \(O_{\mathrm{ep}}\subseteq O\) the epistemic obligations": found, L443.
  - (P)'s definiens: found, L438.
  - "(P), (EK) depend on (G), (E), Deploy" and "(EK) also on (P)": found, L526.
  - "erratum": the brief's reason given, l.613.
- *The model checked.* On L438 and L447–L449 the model is right as to truth values. (P) needs some \(o\in O\) with \(\neg o(\xi)\land o(\xi')\), which \(o_1\) gives. (EK) needs such an \(o\) inside \(O_{\mathrm{ep}}\).

**M2 · point 2, T3, the directed question (lines 29–35).**
- *The bases it gives.* Conflict rests on (F1)–(A) and on the relations the adopted physics admits, that is, on \(\Theta\). Established rests on "a usable receipt for it (Part IX)" and on (K3). Fits rests on established and (E). Rivals rest on conflict and on acts of offering. Problems rest on rivals and fits.
- *(i) The order stays true.* No entry is contradicted, and nothing in Part VI feeds back into (O), (Q), (K), (F1)–(F2), (A) or (E). The closing clause survives. Nothing depends on a "really explains" predicate, since fitting is defined through the absence of an established failure of a condition of (E).
- *(ii) But the order does not place them.* Nor did it ever place (K2), (K3) or receipts, although L598 rests on the order "which lists the declared indices and the declared inputs with the definitions that rest on them". "If it is meant to be one, it needs: 'Rivals, conflict, problems and easy to vary rest on (E), on the relations the adopted physics admits, and on acts of offering; established and fits rest on receipts, (K2), (K3) and (E).'" It calls this "the same class of gap my point 1 presses at (EK)".
- *Quotation check.*
  - "relations of the target that the adopted physics admits (Part I)" and "a usable receipt for it (Part IX)": found, L315.
  - "A record reconstructed from the claim it is meant to support is not a receipt for that claim": found, L397.
  - The italic "*failure of a condition of (E)*" is **not found**. L315 has "shows it failing a condition of (E)". It is a paraphrase, and the point is ruled on L315.
  - The L598 clause: found.

**M3 · point 3, T2 (line 37).**
- CLAIM is right, not WORDING or ORDER. The old entry let a reader conclude "(P) rests only on (G), (E), Deploy" and "Build does not rest on Ownership". Both are the reply's own words for what the old entry allowed.
- The declaration matches clause for clause, but "repeats the incomplete (EK) clause".
- *Quotation check.* "an actual subhistory owned by \(s\)": found at L405 (the reply says L406).

**M4 · point 4, T4 (line 39).** No verdict moves on O38, O35, O37 or O49. The reasons match Atria's.
- *Quotation check.* L441's two sentences and "Losses outside \(P\) must be exposed": found. "runs at all times" (brief l.681) and "not a loss" (brief l.677): found. The L526 and L475 fragments: found.

**M5 · point 5, T1, second attack (line 41).**
- *Attack.* Ownership rests on "the system boundary and resource contract declared for \(s\)", and capability rests on "the same continuity and resource contract", but the entry names only "a declared boundary".
- *Why it fails.* L473 makes the boundary the declaration of "which processes and resources are the system's". Residual: "resource contract" has no place of its own in L522, "not this item's doing".
- *Quotation check.* Found at L427 (the reply says L428), L475 and L473.

**M9 · point 9, (a) (line 49).** Faithful. The entry adds grounding entries only, with no set, count, grade or record. ProducedBy and ProducesVia credit by active routes.
- *Quotation check.* The drafters' rule (brief l.38) and "A record is redundant" (brief l.28): found.

## Points from other parts

The four replies of parts A and B (Atria A, Mimo A, Atria B, Mimo B) were searched for points on the dependence order or L526. The search terms were "dependence order", "order", "XIV", "Derivation 6", "primitive", "declared input", "well founded", "depends on", "rests on", "placed", "526" and "598". Each hit was read. **None of the four makes a point on the dependence order.**
- The hits on "dependence" are all (E)'s "non-circular dependence".
- The one hit on "ORDER" (Atria A, line 21) is the kind ORDER for X09.
- One point bears on this ruling without being about the order: **Atria A, line 33 (T3 on X09), raised outside part K (rule 11).**
  - It checks the pointers the new Part VI sentences use. (K3) and the receipts are "correctly paraphrased", and "relations of the target that the adopted physics admits (Part I)" "rests on line 75".
  - It finds "Forward references to Parts VIII–IX ... used elsewhere in the same way" and "no sentence made false, stale or idle".
  - This supports two facts the ruling relies on: that "established" rests on Part IX's usable receipts, and that the relations quantified over are the adopted physics' (Part I). It says nothing about the order.
  - It does not count X17 as examined by Atria in part A.
- This agrees with the tabulation's §3.9: "No point on X17 was raised outside part K."
- By the orchestrator's instruction to this checker, the checkers of the other items have ruled that any repair for the missing placement of Part VI's new terms belongs at L526, in this entry's span, and not in W59.1. They also noted that the order never placed receipts, (K2) or (K3). This checker did not read those rulings. It takes the routing as given and rules the placement here on the texts.

## Rulings

### 0. Is the order meant to be complete? What L526 and the entry claim about it

**What L526 says of itself.**
- L526 is a run of "X depends on Y" entries. Its last three sentences are "(RC), (U1)–(U3) depend on all of the above", "Nothing depends on a predicate meaning ...", and the well-foundedness sentence, under which what is "justified only by" itself "has not supplied its place in it".
- Nothing in L526 says that it lists every predicate, or every direct dependence of the predicates it lists.
- Its entries summarize bases:
  - "(E) depends on those", although (E) also uses the named background.
  - "(R) depends on (F1)–(F2) and physical provenance".
- It has never placed the tagged conditions (T1), (T2), (K2), (K3), (CT2)–(CT4), (CA), (AR) and (I1)–(I4).
- Nor has it placed Result, ProducesVia, Cap, Enable, Scrutinizability, Barriers, Membership, receipts or active routes.
- The entry's own CHECK says "The order still omits Result, ProducesVia, Cap and Enable (B1 finding 9)". Finding 9 calls the order "a summary".

**What the rest of the text and the entry claim of it.**
- L31: "Everything else is derived from the two primitives, the declared indices and the declared inputs, in the order Part XIV states."
- L520: "Everything else is derived from the two primitives, the declared indices and the declared inputs (below)."
- L598, Derivation 6's proof: "By the dependence order of Part XIV, which lists the declared indices and the declared inputs with the definitions that rest on them, following each definition to its base in the primitives, the indices and the inputs."
- W7.5's GAIN: "Derivation 6's proof has an order that reaches the declared inputs and the definitions that rest on them. (EK) reaches the declared obligations through (P)."

**Ruling on the question.** The order is not an exhaustive list of predicates, or of each predicate's direct dependences. L526 does not claim to be one, and the entry records that it is not. What the text does rest on it is three things:
1. every entry it makes is true;
2. every definition it places reaches its bases through it. This is the standard the S90 checker applied to this entry: an over-statement does not hurt Derivation 6's proof, and an under-statement does;
3. Derivation 6's proof (L598) and L31 follow the order to show that everything else is derived from the primitives, the indices and the inputs.

Incompleteness is a defect only where it fails (1), (2) or (3) in a way the recorded summary does not already cover. A definition the order does not place at all is one that Derivation 6's proof does not follow. The change list accepts this for the finding-9 omissions. Each of those rests on items the order places, in or next to its own Part:
- Cap on owned capability;
- Enable, Barriers and Scrutinizability on Can and Ownership;
- Result and ProducesVia on Build and routes;
- Membership on the tags.

Whether the Part VI terms may be left out in the same way is ruling 2.

### 1. Mimo's challenge: (EK)'s entry and the declared obligations, \(O_{\mathrm{ep}}\) and ProducesVia (M1, with M3's rider) — **KEEP**

- **The clause is true.** (EK) has Repair\(_{O,P}(\xi,\xi';\Delta)\) as a conjunct (L447). "(EK) also on (P)" states a dependence (EK) has.
- **The exhaustive reading is not the order's.**
  - No entry in L526 says "only", and the entries are summaries (§0).
  - Mimo's own proposed wording would still be "false read as an exhaustive entry". It leaves out Result and CreativeCriticalEpisode, which (EK) also uses (L447–L449), and which the reply leaves "unpressed".
  - So the standard Mimo invokes is neither the one the order keeps nor one Mimo's wording meets.
- **The item's standard is reach, and (EK) meets it.** The entry's REASON and GAIN, and the S90 ruling that added the clause, set the standard that (EK) must reach the declared inputs it rests on.
  - *The declared obligations.* (EK) reaches the declared obligations with their occasions through (P) ("(P) also on ... the declared obligations with their occasions").
  - *\(O_{\mathrm{ep}}\) adds no base.* L443 makes the epistemic obligations the members of \(O\) that require "a correct account, or the correction of a use through one, to be deployable". They are read off the stated conditions in \(O\), which is the declared input the order already has.
  - *What Mimo's model shows.* Mimo's model (\(O=\{o_1,o_2\}\)) is right that (EK)'s truth turns on which obligations are epistemic, over and above (P). It does not show a base that (EK) fails to reach. The base is the same declared input, the obligations with their occasions.
  - *ProducesVia's bases are reached.* ProducesVia (L453) holds when "an active route that runs from Δ to the repair of \(o\) contains the relevant binding of \(c\)". (EK) reaches histories and active routes through (P) and ProducedBy. It reaches the binding of \(c\) through (G) and Build ("contains a nontrivial binding construction", L405), and through Deploy and (R).
  - *ProducesVia's own omission is recorded.* No base is missed. That ProducesVia is not placed as a node is the omission the entry's CHECK and finding 9 record, like Result and CreativeCriticalEpisode.
- **The proposed wording would add questions the entry need not settle.**
  - "On the binding of \(c\)" adds a base the order names nowhere else.
  - "Through \(O_{\mathrm{ep}}\)" reads \(O_{\mathrm{ep}}\) as a channel of declared input. Mimo's own residual says \(O_{\mathrm{ep}}\) "appears in no list of declared inputs".
  - Both lengthen the declaration for no gain in reach.
- **M3's rider** ("repeats the incomplete (EK) clause") falls with M1. The declaration says exactly what the (EK) clause says.
- **The disagreement (rule 5).** Atria finds "(EK) on (P)" supported (A2, L447) and the declaration exact (A3). Mimo finds the clause incomplete. On the texts, Atria's reading holds: the clause is true, the declaration matches it, and nothing (EK) rests on is left unreached. **Not upheld.**

### 2. Part VI's new terms, raised by both under the directed T3 question (A1; M2) — **FIX**

**The two sides.**
- *Atria (A1).* The order stays true. Its silence on the new terms is "incomplete, not untrue". The gap predates X17 and "belongs to the items that introduced lines 315/317". No wording.
- *Mimo (M2).* The order stays true, but it does not place the new terms, and it never placed (K2), (K3) or receipts, although L598 says it lists the definitions that rest on the indices and inputs. "If it is meant to be one", it needs the words Mimo offers.

**Where both are right: the order stays true.** Each sentence of L526 was read against L313–L317 and against the uses of the new terms at L69, L339 and L369.
- *No entry is contradicted.* No entry names a Part VI term, so none is contradicted.
- *"(RC), (U1)–(U3) depend on all of the above"* is about the items above it and is unaffected.
- *"Nothing depends on a predicate meaning 'really explains,' 'is a cause,' or 'is knowledge'"* is true of the new terms:
  - a result is established when an assessor "holds a usable receipt for it" (L315);
  - a candidate fits when no established result "shows it failing a condition of (E)";
  - rivals rest on an offer and a conflict at a pair;
  - a problem rests on two rivals that both fit.
- *Well-foundedness holds.* No base of a new term rests on a new term:
  - (F1), (F2), (A) and (E) are Part V's;
  - the relations quantified over are those "the adopted physics admits (Part I)", which is primitive 1;
  - an offer is an occurrence;
  - usable receipts (L390, L397) rest on (K2) and on leaves that refer to events;
  - (K3) speaks of "an established \(\neg O\)" (L395), so it rests on "established", not the reverse;
  - Part IX's (K1) meets "easy to vary" only as the content of a question \(p_\delta\) (L317: the criticism "must supply such a rival"), not in the definition of any receipt.

  There is no circle.

**Where they part: does the incompleteness matter now?** It does. The Part VI terms are not like the finding-9 omissions, for five reasons:
1. **The text claims coverage that the order does not give for them.**
   - L31 says everything else is derived "in the order Part XIV states". L598 says the order "lists ... the definitions that rest on them" and follows "each definition to its base".
   - The order's only Part VI entry is "(S), (B), (D) depend on (E)".
   - The new terms rest on things the order puts nowhere near Part VI: Part IX's usable receipts (a later Part), an offer, and the relations the adopted physics admits (Part I).
   - A reader who follows L31 to Part VI finds (E) and nothing else. Unlike Cap or Enable, the new terms' bases are not items the order places beside them.
2. **Draft 4 makes references run both ways across Parts.**
   - L315's "established" cites Part IX's receipts and (K3).
   - (K3) at L395 speaks of "an established \(\neg O\)".
   - L317 sends the easy-to-vary criticism to Part IX.
   - L369, in Part VIII, uses "established" "as in Part VI".

   Whether these run in a circle is what the order's last sentence exists to settle ("has not supplied its place in it"; O37's circle). They do not, but only the order can say so, and it is silent.
3. **"Established" is new as a defined term, and much now rests on it.**
   - Before draft 4, (K3)'s "established" was an undefined qualifier.
   - Now fits, a problem for \(p\), easy to vary and Part VIII's "A failed answer stays failed" rest on it.
   - It is the one new term a reader will test against the order's "Nothing depends on a predicate meaning ... 'is knowledge'" and against Derivation 6's Consequence (L600).
   - Placing it on usable receipts is what shows those sentences true of it.
4. **The owner's position turns on these terms.** The order is where the theory states what they rest on: offers, conflicts, receipts and (E). It is where it can be seen that nothing in them rests on a listed set, a count, a grade or a record.
5. **No other entry can take the repair.**
   - The checkers of W59.1's items route it to L526.
   - The free sentence "(S), (B), (D) depend on (E)." is outside W7.5 and is kept free (change list: "The two sentences B1 left free stay free").
   - No other entry names L518.

   Atria's "not X17's" would leave the gap with no entry to close it. W7.5 is the entry of the order's middle sentences.

So Atria is right that the order stays true, and wrong that its silence on these terms is harmless. Mimo is right about the gap. **Mimo's offered words are not taken:**
- *They under-state the bases of problems and easy to vary.* "Rivals, conflict, problems and easy to vary rest on (E), on the relations the adopted physics admits, and on acts of offering" places problems and easy to vary without fits. A problem is two rivals that "both fit what is established" (L317), and fits rests on what is established, which rests on usable receipts. Under the reach standard, the order must not under-state bases in this way.
- *They read as a circle, and put "established" on (E).* "Established and fits rest on receipts, (K2), (K3) and (E)" puts what is established on (K3). But (K3) speaks of "an established \(\neg O\)" (L395), so in the order this reads as the circle its last sentence rules out. It also puts what is established on (E), which L315 does not: a result is established by a usable receipt, whatever the result is about.

**Where the sentence goes.** It goes after "(RC), (U1)–(U3) depend on all of the above.", not before.
- *Before it*, the unchanged "all of the above" would newly say that (RC) and (U1)–(U3) depend on rivals, fits and problems. Their definitions (L487–L506) do not use them. That would make an unchanged sentence falser (T3).
- *After it*, that sentence stays as it was. The new sentence is still under "Nothing depends ..." and "The order is well founded", which follow it and speak of everything.
- *The cost is the same either way.* The theory text changes by exactly one inserted sentence in both places. Putting it after costs one unchanged sentence in OLD and NEW. No other entry touches "(RC), (U1)–(U3) depend on all of the above." (only W7.4, W7.5 and W3.2 name file-11 L518), and W3.2's locator, the last sentence, is not met.

**What is placed, and what is not.**
- **Placed:** conflict, rivals, what is established, fits, a problem for \(p\), easy to vary. Each is given the fewest bases that keep reach.
- **Not placed: "test"** (bold at L317). Its bases, what is established and a problem for \(p\), are placed. The word "test" is also used in a wider sense in (K3) and at L315 ("the test that yields it"). Placing "a test" on a problem would seem to put (K3)'s tests after problems, which rest on fits, which reads through (K3). That would be a circle in appearance.
- **Not placed: (K3), receipts and (K2).** They stay as finding 9 records them. "Usable receipts (Part IX)" is named as a base at the order's existing grain, as "histories" and "active routes" are.
- **Not placed: "does no work"** (L313). It rests on (S) and (B), which are placed, and neither reply raises it.
- **Two wording choices:**
  - *"In Part VI".* It keeps "conflict" and "problem" apart from their ordinary uses elsewhere (L429 "a conflict in which what the system holds ..."; L403 and L405 "problem").
  - *"The offer of one in place of the other" rather than "histories".* "Rivals on ... histories" could be read as rivals resting on a candidate's history of change, against L369 ("with no record ... of how any was changed") and the owner's "A record is redundant". The offer is the one event L315 uses ("one of them has been offered as an answer to \(p\) in place of the other").

**The FIX** (OLD, NEW and DECLARATION replaced; KIND unchanged). Ready to paste:

- **OLD:**
````text
Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy. (RC), (U1)–(U3) depend on all of the above.
````
- **NEW:**
````text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, (EK) also on (P), and ProducedBy on histories and their active routes. (RC), (U1)–(U3) depend on all of the above. In Part VI, conflict depends on (F1), (F2), (A) and the relations the adopted physics admits, rivals on conflict and on the offer of one in place of the other, what is established on usable receipts (Part IX), fits on what is established and (E), a problem for \(p\) on rivals and fits, and easy to vary on a problem for \(p\).
````
- **KIND:** CLAIM (unchanged). **REASON WORD:** erratum (unchanged). The order's coverage, which L31 and L598 claim, is corrected.
- **DECLARATION:**
````text
Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, (P) on ProducedBy and the declared obligations with their occasions, (EK) on (P), and ProducedBy on histories and their active routes; and it places Part VI's conflict on (F1), (F2), (A) and the relations the adopted physics admits, rivals on conflict and on the offer of one in place of the other, what is established on usable receipts (Part IX), fits on what is established and (E), a problem for \(p\) on rivals and fits, and easy to vary on a problem for \(p\).
````
- **Bookkeeping that goes with the new OLD:**
  - The heading becomes `### W7.5 — L518 s9–s12: Ownership, owned capability, ProducedBy and the obligations; Part VI's terms`.
  - WHERE becomes `- **WHERE:** Part XIV, "Dependence order", L518, the sentences on Build, (N) and (G), and (P) and (EK), and the sentence on (RC), (U1)–(U3), which is kept word for word and followed by the placement of Part VI's terms.`
  - FILE-11 LINE stays 518.

**The declaration must change.** The fix adds claims: what six Part VI terms depend on. So the declaration grows by the clause after the semicolon. Nothing else changes in what is claimed:
- the (RC) sentence is reproduced word for word;
- because the new sentence comes after it, (RC) and (U1)–(U3) are not newly said to depend on anything;
- the first part of the declaration is the S90 declaration byte for byte.

**The fix under the four tests and question (a).**
- **T1, true.** Each clause was read against L315–L317:
  - Conflict: "their answers there differ" (answers under (A)), or each could meet "(F1), (F2) and (A) there under some relations of the target that the adopted physics admits" and no such relations let both.
  - Rivals: "one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair".
  - What is established: "for an assessor who holds a usable receipt for it (Part IX)".
  - Fits: "no result established for that assessor shows it failing a condition of (E)".
  - A problem for \(p\): "Two rivals that both fit what is established".
  - Easy to vary: "when it and a rival pose a problem of the second kind".

  Every base named is one the definition uses. No base that keeps reach is left out: (K3)'s part in "shows it failing" adds no base beyond what is established, and "test" is covered as above.
- **T2, kind and declaration.** CLAIM, since a reader can now conclude where these terms stand in the order, which the current text left unconcluded. The declaration says exactly that and no more.
- **T3, coherent.**
  - There is no circle (above).
  - "Nothing depends on ..." stays true.
  - "(Part IX)" points to receipts and (K2) (L390, L397), which is what it says.
  - "In Part VI" names the Part where all six are defined (L315, L317).
  - L598's clause is now true of the Part VI terms at the order's grain. Receipts remain a named, unplaced base, as histories are.
  - The sentence restates W59.1's definitions and does not pull against them.
- **T4, verdicts.**
  - The entry's CASES AT RISK (O35, O38, O37, O49) turn on the unchanged input at L441 and L522, on Ownership before owned capability, and on the unchanged last sentence. The new sentence adds no circle and no condition, so all four stand as before.
  - The S81 case book, the S89 N-cases (N1–N25) and the D3-T files were searched for "dependence order" and "well founded", and none cites them.
  - The verdicts that rest on Part VI (the cases W59.1 names) rest on L315 and L317, which the sentence restates without change.
  - **No verdict moves, in either direction.**
- **(a), the owner's words and the drafters' rule.**
  - The sentence brings back no list, count, grade or record. Rivals rest on an offer (a discovered competitor) and a conflict. A problem rests on two rivals that both fit. Easy to vary rests on a problem. What is established rests on usable receipts, which L397 already keeps apart from a record reconstructed from the claim.
  - The sentence is faithful to "If two discovered variations fit, that constitutes a problem" and to the rule "state hard to vary through discovered rivals and the problems they make".
- **The self-test (rule 4).**
  - *How it was run.* A copy of the change list (md5 b6b2ea95…) was made in the scratchpad. The four replacements above (heading, WHERE, OLD, and NEW with DECLARATION) were applied to the copy. Then `python3 Semantics/tools/s89_apply_changes.py <scratch>/fixed_draft.md --change-list "<scratch>/change list with X17 fix.md" --theory-output <scratch>/fixed_theory.md --self-test` was run.
  - *What the tool reported.*
    - "entries parsed: 65 (applied 60, of which theory 57 and meta 3; record-only 5; held 0)"
    - "CLAIM 51, ORDER 2, WORDING 4"
    - "every OLD, locator and anchor occurs once in file 11; no applied OLDs overlap"
    - "N = 51 of M = 57 changes; layer 2: K = 42 places"
    - "55 diff hunks, each inside an entry"
    - "no withheld word in it; no slot left"
    - both planted edits were refused, and "the clean draft passed".
  - *Result.* Theory text md5 f7fb94d3ad26c089c6abbf60b83baf67, 12,639 words. The unfixed baseline gives the draft-4 md5 fc55b470… and 12,577 words.
  - *The diff against draft 4* is one line, L526, with the one new sentence inserted after "(RC), (U1)–(U3) depend on all of the above." and before "Nothing depends on ...".
  - The committed change list was not edited (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40 after the test).

### 3. The other attacks, reported by the replies as failing — **KEEP**

The fix leaves each as it was.
- **A2, "Build depends on histories, Ownership and (E)".** "(E)" is the old wording's, carried over, and the S90 checkers kept the over-statements of this sentence knowingly. The added "Ownership" is exact: Build is "an actual subhistory owned by \(s\)" (L405). Not upheld.
- **A3, the declaration omits histories and (E) from Build.** The declaration reports what is placed anew, and histories and (E) are kept. Not upheld.
- **A4 and M4, verdicts.** Both find no move on O35, O38, O37 or O49, and the texts agree (see T4 above).
- **A5 and M9, (a).** Both find the entry faithful, and it is. Under the fix it stays so (see (a) above).
- **M3, kind.** CLAIM is right, as both replies hold.
- **M5, "resource contract".** The attack fails as Mimo says, on L473: the declared boundary says "which processes and resources are the system's". The residual is recorded under "Findings for later entries".

**Summary.**

| challenge or attack | raised by | ruling |
|---|---|---|
| (EK) omits the declared obligations with their occasions, \(O_{\mathrm{ep}}\), and ProducesVia | Mimo K, point 1 (closing line), with point 3's rider | KEEP (not upheld) |
| the order does not place Part VI's new terms | Atria K, T3 (as an attack it reports failing against X17); Mimo K, point 2 (words offered) | FIX: OLD, NEW and DECLARATION as above; KIND unchanged |
| Build and (E); the declaration and Build; resource contract | Atria K, T1 and T2; Mimo K, point 5 | KEEP |
| verdicts; (a) | both | KEEP: no move; faithful |

**For the entry, when the rulings are applied (rule 12).** These lines are suggested. The orchestrator writes the entry.
- *CHECK, a new line:* "S93 cross-examination: X17 (Atria K UPHELD; Mimo K CHALLENGED on (EK)). Mimo's (EK) omissions: KEEP, since (EK) reaches the declared obligations through (P) and ProducesVia's bases through (P), (G) and Deploy. The placement of Part VI's terms, raised by both under T3: FIX. OLD is extended by the unchanged sentence on (RC), (U1)–(U3); one sentence placing conflict, rivals, what is established, fits, a problem for \(p\) and easy to vary follows it; the DECLARATION is extended to match."
- *REASON, a new bullet:* "After the S93 cross-examination: the order placed none of Part VI's new terms. Yet L31 and Derivation 6's proof (L598) rest on it, what is established rests on Part IX's usable receipts, and (K3) and Part VIII speak of what is established. The sentence goes after the (RC) sentence so that 'all of the above' does not newly cover them. 'Test' is not placed (its bases are). Receipts, (K2) and (K3) stay as finding 9 records them."
- *CASES AT RISK, a new line:* "S93: the Part VI sentence moves no case. No case cites the dependence order. The Part VI verdicts rest on L315 and L317, which it restates."
- *GAIN, added:* "Part VI's rivals and problems, and what is established, have their place in the order: Derivation 6's proof reaches them, and the order shows that they rest on offers, conflicts, usable receipts and (E), not on a list, count, grade or record."
- *LOSS, added:* "The order grows by one sentence of 62 words."
- *"Found in draft 4", first bullet:* can say that the placement is now made, in W7.5, after the (RC) sentence. The candidate at the free sentence is not taken, and the free sentence stays free.

## Findings for later entries

These are recorded and not ruled. None is part of the FIX.

1. **(K2)'s Lic\(_j\), Scope\(_j\) and Live\(_j\) are defined nowhere in the text** (L390 only).
   - Derivation 6's claim, that every predicate is defined from \(\Theta\), \(\mathcal N\), the indices and the inputs, therefore cannot be followed through receipts to the primitives.
   - This predates draft 4. The fix makes it more visible, because the Part VI terms now route through "usable receipts (Part IX)".
   - It is for the orchestrator or a later revision. It is not X17's.
2. **Receipts, (K2) and (K3) are still not placed** (finding 9).
   - If they are placed later, (K3) goes after "what is established", because it speaks of "an established \(\neg O\)" (L395). It is never a base of "what is established". Mimo's offered words would have made that a circle.
3. **L598's relative clause is still stronger than the order.**
   - The clause is "which lists the declared indices and the declared inputs with the definitions that rest on them".
   - It is still unmet for the finding-9 omissions.
   - Either the order grows, or the proof (W7.6's wording) says that it follows unplaced definitions through their own text to placed ones. That is W7.6's matter, not X17's.
4. **"(RC), (U1)–(U3) depend on all of the above" over-states.**
   - It covers (S), (B), (D), (EK) and others that (RC) and (U1)–(U3) do not use (L487–L506).
   - The fix is placed after it so as not to add to that. The over-statement is harmless to well-foundedness, and it is recorded here only.
5. **The X09 and X10 rulings.**
   - If either changes what rivals, conflict, what is established, fits or a problem for \(p\) rest on (for example the physics quantifier, "offered", or the receipt clause), the placement sentence must be re-read against the fixed L315/L317 before the edit is made.
   - This checker has not read those rulings.
6. **"Conflict" is used in two senses.** The defined sense is at L315. The ordinary sense is L429's recognized difficulty ("a conflict in which what the system holds meets a claimed obligation only by failing a protected one"), and L317's gloss "a conflict between ideas". The fix's "In Part VI" keeps the order's use to the defined sense. Whether the text should mark the difference is for the W35 and W59 items.
7. **Mimo's residuals.**
   - \(O_{\mathrm{ep}}\) is not a separate input: it is read off \(O\) (L443).
   - "Resource contract" (L427, L475) has no place of its own in L522. L473's boundary carries it.
   - Neither affects X17. The second is a candidate clause for L522 if the orchestrator wants the words to match.
8. **"Test" (bold, L317) and "does no work" (L313)** stay unplaced. Their bases are placed.
9. **Line-number slips in the replies:** Atria's "line 448" for Account (L449); Mimo's L406 (L405) and L428 (L427). They change nothing.

X17: FIX
