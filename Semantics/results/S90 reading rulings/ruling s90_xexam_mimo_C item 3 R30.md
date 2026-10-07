# Ruling: s90_xexam_mimo_C, item 3, R30 (W41.1)

*A fresh Claude checker, 24 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3) and "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (§2 item 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*What it read:*
- *the whole reply, `parts/s90_xexam_mimo_C.response.txt`. The file the task names, with the call description in place of `.response`, does not exist; this is the one reply of this tag. It has 1,321 words by `wc -w`. The receipt shows pass 2, status 200, finish "stop", 0 bad chunks, and END OF REPORT on the last line. The response sha256 9ea0342f… matches the receipt. Pass 1 of this tag ended on the dead proxy with no reply (rerun note §1), and nothing of it was read.*
- *the R30 section and tasks (a)–(d) of the part C brief (md5 2183faa5…), to see what the reply was given. The brief numbers lines by the revised text, title line = 1.*
- *the S90 rule, the S90 Parts rule and the rerun note; batch 1 and batch 2 and the rulings folder, for any earlier ruling on this entry. There is none.*
- *the change-list entry W41.1; the worklist's W41; the plan's row W41 (with its relay guard, 1.2); the revision note's row R2-30; W3.1 (the anchor sentence); and file 00's lines 855–861, the source of the restored text (read only).*
- *Atria C's point 3 and closing line on R30, which the orchestrator pointed to. It is read as another reader's view and is not counted (Parts rule 1). No other reply names R30.*
- *The S87 rules (05, 05b, 05c) govern S87 rows, not S90 parts, and are not applied here. No reasoning file was opened.*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (as of 587eebf, unchanged since);*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the S81 case book (md5 4f488d14…), the S89 candidate book (md5 b2e53577…) and D3-T's `final.md`.*

## 1. The entry and its checkers' history

W41.1, "Part X: inexplicit representation, and a witness identified by use, with the relay guard".
- **Place:** Part X, "Construction". File-11 L401, revised L399–403. Two new paragraphs follow L401's last sentence, which is kept byte for byte as the anchor and is W3.1's declared sentence. L403 of file 11 ("Construction is not selection") follows unchanged.
- **Group:** C. **Reason word:** clarification. **KIND:** CLAIM.
- **OLD:** `A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.`
- **NEW:** the OLD sentence, then:
  - revised L401: "An inexplicit representation is not an absent one. A pianist can imagine a passage without playing it. A geometer can manipulate a spatial relation without naming every component. An investigator can notice an inconsistency before articulating its premises. None of (R), Deploy and Build asks whether the relevant distinctions and transformations are written in a particular format: what they ask is whether those distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked."
  - revised L403: "A system's realization can use a partial, distributed, or temporally extended representation. The relevant bindings can be available through memory, imagery, action rehearsal, or interaction with an artifact. Not every representation must be simultaneously explicit. Retaining a critical target can consist in being able to re-present the relevant distinction, not in storing a complete verbal transcript. A construction witness may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it: by responses that preserve its role bindings, send content-preserving recodings to the same transition and content changes to the changes the binding specifies, and lie on an active route, as reason use asks of an objection (Part IX). Use does not by itself construct: received content used as it was received keeps its inherited provenance. A carrier that passes content on without such use has relayed it, and relay is not construction."
- **DECLARATION:** "Part X now says that an inexplicit representation is not an absent one; that (R), Deploy and Build ask for no particular format, only whether the relevant distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked; that a representation can be partial, distributed or extended in time and need not be explicit all at once; that retaining a critical target can consist in being able to re-present the relevant distinction; that a construction witness may identify a constructed binding by its use, in the manner of reason use; that use does not by itself construct, so received content used as received keeps its inherited provenance; and that a carrier that passes content on without such use has relayed it."
- **CHECK (its checkers' verdict):** "check 2, FIX. "The realization" had no antecedent (NEW: "A system's realization"). The paraphrase of what (R) asks dropped fidelity and provenance (NEW states them). The relay sentence put O18's "The rest is relay" at risk; NEW adds "Use does not by itself construct: received content used as it was received keeps its inherited provenance." The declaration is completed. Cases: as drafted, plus O18 guarded, O11 and O15 toward, O23 watched (the shared word "investigator"), N4 Q2 and N12 (Mr Okafor) watched." Check 2 did not touch the witness clause's four criteria or its pointer to Part IX.
- **REASON** (not sent) says that the witness's use "is spelled out in the four clauses of reason use (L381), which are what separate use from recitation". It also says that L401 of the NEW restores 00:856–857 with two edits, and L403 restores 00:858 word for word and adds the plan's relay guard. File 00 has no witness-by-use sentence; the four criteria are the drafters' own.
- **CASES AT RISK:** N21 toward; N13 holds AGREE (the guard); N12 and N15 hold; O14 holds and is watched; O23 is watched and holds; O19 holds; O3, O11, O15, O18, O31, O43, O44 and O49 hold; O32 holds, "and moves toward if anything". Part C gave O14, O15, O23, O32 and N21.
- **Revision note:** row R2-30, W41.1, C25, L401, clarification, CLAIM, declared "yes". Plan row W41: "Take, with a relay guard … a witness may identify a binding by its use (reason use, Part IX)". Guards: N13, O14, N12.
- **Earlier rulings:** batch 1 and batch 2 made none on R30, W41.1 or C25, and no ruling file on it exists. The ruling on R31 (Mimo B2 item 1) mentions W41.1 only to say that it adds text at L399–403 and does not touch L407. The single S90 call (C25) failed and supports nothing. There is nothing to reconcile.
- **Other reader:** Atria C (point 3, task (d); closing line "R30: STANDS") reads R30 as a declared move toward the fixed verdicts on N21 ("she knows it, tacitly"; "her grasp of it was not handed to her") and O15 ("the same clauses keep the arrows' provenance a hole in the diagrams rather than a hole in Sam's own construction"). It is not counted, and it is checked in section 3.

## 2. The reply's argument

Closing line: "R30: FALLS — identification criteria diverge from Part IX's reason use while the text and declaration present them as its own". Point 3, tasks (a) and (c):

> "Part IX (line 364) says reason use requires "a **structural map from the represented objection into the response suborganization** … sends content changes to **the changes specified by the operative deliberative rule**, and **lands** on an active route." At least three clauses diverge:
> - **Source of specification.** R30: "the changes the binding specifies." Part IX: "the changes specified by the operative deliberative rule." For a structural binding — the text's own flagship example is "the binding of a persistence component to a continuity subnetwork" (Derivation 10) — "the changes the binding specifies" are structural changes between components, while the "operative deliberative rule" governs how a response to an objection is generated. These are different in kind.
> - **Structural map.** Part IX requires "a structural map from the represented objection into the response suborganization." R30 omits this and attributes preservation directly to "responses."
> - **Lie vs. land.** "lie on an active route" (a state) vs. "lands on an active route" (a transition).
>
> The phrase "as reason use asks of an objection (Part IX)" asserts that these are Part IX's criteria. Part IX does not say what the change says it says. The declaration — "in the manner of reason use" — inherits the inaccuracy: the manner is *modelled on* reason use with at least one substantive substitution, not reason use's own manner.
>
> The criteria themselves are stated in full and are usable without Part IX, so the text is not self-contradictory; but the pointer is misleading and the declaration misdescribes the claim."

> "**Repair.** Either copy Part IX's clause verbatim ("content changes to the changes specified by the operative deliberative rule"), or replace the pointer with "in a manner modelled on reason use (Part IX)" and change the declaration to "in a manner modelled on reason use.""

The reply names no case for R30.

**Quotations checked (S90 rule 8).**
- The quotation of R30's clause matches revised L403 byte for byte, apart from the added bold.
- The quotation of Part IX matches revised L379 (file-11 L381) byte for byte, apart from the bold and the ellipsis.
- "in the manner of reason use" matches the declaration.
- "the binding of a persistence component to a continuity subnetwork" is at revised L622 (Derivation 10).
- The reply's line numbers are off. It puts Part IX's reason use at "line 364", but it is at L379. It puts R30's clause at "lines 404–405", but it is at L403. Nothing turns on this, since every quotation is found.

## 3. Reading

**What the reply gets right.** The witness clause does not repeat Part IX word for word. It names the binding, not "the operative deliberative rule", as what specifies the changes. It makes "responses", not "a structural map from the represented objection into the response suborganization", the subject of the four criteria. And it says "lie on" where Part IX says "lands on". The question is whether any of these makes the pointer "as reason use asks of an objection (Part IX)" say something that Part IX does not say, or makes the declaration misdescribe the claim. None does.

**1. The specifier has to change, and the pointer marks the change.**
- The pointer says the criteria are asked "as reason use asks" them "*of an objection*". The thing whose use is tested here is a binding, and the clause says so ("its role bindings", "the changes the binding specifies"). So the pointer offers a parallel with the ask Part IX makes of another object. It does not say that Part IX states these words.
- In reason use, the objection does not itself fix the response to a change in its content; the operative deliberative rule does. A binding is itself the relation that fixes what a change of content should become. Putting "the binding" where Part IX has "the operative deliberative rule" is the substitution the parallel needs. It is not a drift away from it.
- The reply's first repair would be harmful. Copying "the changes specified by the operative deliberative rule" into the witness clause would ask a tacit or structural binding for a deliberative rule it does not have. The term is used only at L379 and is not defined elsewhere. That would make the clause fail for N21's adjective order and for Derivation 10's persistence-continuity binding, which the reply itself calls the flagship example. The clause exists to reach exactly these cases (worklist W41: "Gained. N21 … can be reached").

**2. Leaving out the structural map does not weaken what is claimed.**
- In R30, "responses that … send content-preserving recodings to the same transition and content changes to the changes the binding specifies" are the responses taken as a map from variants of what the binding governs to transitions. That is the shape of Part IX's map. The pointer directs the reader to Part IX's statement of it.
- Part IX's map starts from "the represented objection", which the witness does not have in hand: the paragraph is about a binding that may be "partial, distributed, or temporally extended" and is to be identified "by its use rather than by a statement of it". So Part IX's wording could not be copied here unchanged.
- What the structural map guards stays guarded by the unchanged conditions and by the new L401:
  - "preserve its role bindings" is structural;
  - "lie on an active route" reads the route from the history (Part IX: "whether a route is active is read from the history, not from the result");
  - the binding identified must still be instantiated "with the fidelity and provenance (R) requires" (L401), and Build's own conditions (L399: a nontrivial binding construction, "not a composition of content-preserving transfers") still have to hold.
- The witness clause says only how a constructed binding "may" be identified. It does not construct anything, and the next sentence says so: "Use does not by itself construct".

**3. "Lie on" and "lands on" put the same condition.** An active route is "a connected subnetwork of actual occurrences joining a represented input to an operative result" (L369). In Part IX, the map's image lands on such a route. In R30, the responses lie on one, which means they are among its occurrences. The difference is grammatical: the subject is a map in one sentence and occurrences in the other. No case or clause turns on it.

**4. The declaration is exact.**
- "In the manner of reason use" already says what the reply's repair says, "in a manner modelled on reason use". It claims the manner, not identity of wording.
- Every other clause of the declaration matches the NEW (task (a)).
- The declaration does not say that file 11 already had a witness by use, so it describes the current text correctly. File 11 has none: its Build witness "identifies … the bindings constructed" by no stated means.
- The reply's second repair would change words and no claim. That is not a defect to fix under the S90 rule.

**5. Coherence (task (c)).**
- Revised L379 (reason use) is unchanged, and R30 neither contradicts it nor makes it idle.
- "Use does not by itself construct" agrees with L361 ("A section of a carrier filled from another source keeps that other source's history") and with the anchor sentence.
- "relay is not construction" repeats L399's "relay is not". The new text adds when a carrier has relayed.
- No symbol is new, and no letter is re-bound.

**Cases worked** (those part C gave, those the entry names, and D3-T).
- **N21** (given): toward, as the entry says.
  - Ngozi's orderings of phrases she never heard preserve the role bindings, meaning each adjective's class keeps its slot.
  - The same adjectives in another phrase go to the same order. A change of adjectives goes to the order the binding specifies. The orderings lie on the active route of her speaking.
  - The binding is in no sentence she heard, so it is not a composition of content-preserving transfers.
  - This gives "she knows it, tacitly" and "formed her grasp of it herself".
  - Under the reply's first repair, with "the operative deliberative rule" in place of the binding, there is no deliberative rule here, so the clause would not reach N21. The move toward would be lost. Under its second repair nothing changes.
- **N13** (named, not given): holds AGREE.
  - A rephrased question gets "another of its sentences, or … a squawk". That fails the clause about recodings going to the same transition.
  - "Had the lectures been recipes, it would have repeated those just as readily": its responses do not follow content changes. So it has "relayed" the sentences.
  - This holds under every wording discussed here, and the structural map is not needed to exclude the parrot.
- **N12** (named): holds. Ms Varga's use is Deploy and passes the criteria; Mr Okafor "answers each question by reciting the list again", which fails the content-change clause. **N15** (named): holds. Her correction is a small constructed binding (the anchor sentence).
- **O14** (given): holds.
  - Kofi's retained phrases are received content used as received, and "Use does not by itself construct".
  - Asked for a new sentence, "he has nothing to say": no content change goes to a specified change, so no language binding is identified by use.
  - The verdict ("a narrow skill by his own effort"; "yet to understand the language") turns on Deploy's narrow retained use (L397).
- **O15** (given): holds, toward if anything.
  - The arrows are received and followed as received, so "received content used as it was received keeps its inherited provenance". The gap in where they came from passes into his account "because his cut followed them".
  - His own work, which is the cutting, is fully recorded: "Sam's account of his own work is complete".
  - File 11 already reached this through L361 and the anchor sentence, so R30 at most reinforces it.
  - Atria's gloss ("a hole in the diagrams rather than a hole in Sam's own construction") agrees with the verdict's first sentence. The entry itself says "holds" under CASES AT RISK and "toward" under CHECK; both are consistent with this reading. There is no move away.
- **O23** (given): holds. The passing mention of the seal is not made an inexplicit dimension: L401 asks whether a distinction is "instantiated … and used where use is asked", and L419 (file-11 L417) makes a dimension a port only when the account admits changes to it. The shared word "investigator" (L401) does no work in the case.
- **O32** (given): holds. The dependence was found aloud and minuted, so it is witnessed by a statement. R30 adds a second route (use) and removes none.
- **O18, O31** (named): hold. The one tooth and the corrected line are constructed bindings; "the rest is relay" / "the received content stays received" is given directly by "Use does not by itself construct".
- **O19** (named): holds. The diagram "did no work", so it lies on no active route.
- **O3, O11, O43, O44, O49** (named): no binding is identified by use in a way that changes any of them. No move.
- **D3-T** (the discarded controller): this is a case about selection by a tester (Derivation 3). It has no construction, binding, use or relay, and R30 does not touch it.

## 4. Ruling

**KEEP.** W41.1 stands as drafted: OLD, NEW, KIND (CLAIM) and DECLARATION unchanged.

**Reason.**
- The pointer "as reason use asks of an objection (Part IX)" offers a parallel, and "of an objection" marks it as one.
- The one substantive substitution, "the changes the binding specifies" for "the changes specified by the operative deliberative rule", is what applying reason use's four clauses to a binding requires. Copying Part IX word for word would ask a tacit binding for a deliberative rule, and would lose N21 and Derivation 10's binding.
- Dropping the structural map weakens nothing claimed. Fidelity and provenance under (R) (L401), Build's conditions (L399) and the active-route clause still hold, and the clause only says how a binding may be identified.
- "Lie on" and "lands on" put the same condition.
- The declaration's "in the manner of reason use" already means "modelled on", so the reply's second repair changes words and no claim.
- No case moves away. N21 moves toward as declared; N13, N12, O14, O18, O19, O23, O31 and O32 hold; O15 holds or moves toward.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Mimo said FALLS (the witness criteria differ from Part IX's reason use: "the changes the binding specifies" for "the changes specified by the operative deliberative rule", no structural map, "lie on" for "lands on", while the pointer and the declaration present them as reason use's); Atria said STANDS (declared moves toward on N21 and O15). Ruled KEEP after the cross-examination. "As reason use asks of an objection" is a marked parallel, and the binding must replace the deliberative rule as specifier when the thing used is a binding: a verbatim copy would fail N21 and Derivation 10's binding. The structural map's guard is kept by (R)'s fidelity and provenance (L401), Build (L399) and the active-route clause. "In the manner of" already means modelled on. No case moves away; O15 holds, toward if anything."
