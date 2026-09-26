# Ruling: s90_xexam_atria_C, item 6, R30 (W41.1)

*A fresh Claude checker, 24 September 2026.*

*This checker did not draft, assemble or check the change list, and did not write the part briefs. It follows three rules:*
- *the S90 rule;*
- *"S90 Parts - how they will be read, written before sending.md" (rules 1-3);*
- *"S90 and S87 - seven calls rerun after the container restart - written before sending.md" (section 2, item 4: the pass-2 reply stands where the pass-1 reply would have stood).*

*File name.* The task names a file with the full call description in it. That name is over the file system's 255-byte limit. This file follows the naming of the other Atria C rulings in this folder.

*What it read:*
- *The whole reply, `parts/s90_xexam_atria_C.response.txt`.*
  - *The file the task names, with the call description in place of `.response`, does not exist. This is the one reply of this tag.*
  - *It has 1,227 words by `wc -w`, and END OF REPORT is its last line.*
  - *The receipt shows pass 2, finish "stop" and 0 bad chunks. Attempts 1-5 had status 0; attempt 6 had status 200.*
  - *The response sha256 bd51b785... matches the receipt.*
  - *The pass-1 error file and the reasoning file were not opened.*
- *The R30 section and tasks (a)-(d) of the part C brief (md5 2183faa5...). The brief numbers lines by the revised text, with the title line as line 1.*
- *The S90 rule, the S90 Parts rule and the rerun note.*
- *Batch 1 and batch 2, and the rulings folder. None of them rules on R30, W41.1 or C25.*
- *The change-list entry W41.1 (list md5 a5c92adc...); worklist W41; the worklist's case-table rows for N12, N13 and N21.*
- *The revised text (md5 9aecf2f3...), L191-205, L367-405 and L475.*
- *File 11 (md5 5e494c10..., read only), L397-405.*
- *The S81 case book (O14, O15, O18, O23, O32); the S89 case book (N13, N21); D3-T's `final.md`.*
- *The S81 determination 01, its row and section on O15.*
- *Mimo C's reply, for its R30 point, to which the orchestrator pointed.*
- *The sibling checker's ruling on Mimo C item 3 (R30), in the scratch rulings and not committed. This ruling is reconciled with it into one ruling.*
- *The S87 rules (05, 05b, 05c) govern S87 rows, not S90 parts, and are not applied.*

## 1. The entry and its checkers' history

W41.1, "Part X: inexplicit representation, and a witness identified by use, with the relay guard".
- **Place.** Part X, "Construction". File-11 L401 becomes revised L399-403.
- **Group:** C. **Reason word:** clarification. **KIND:** CLAIM.
- **OLD:** `A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.`
- **NEW:** the OLD sentence, kept byte for byte as the anchor. Two paragraphs follow it, revised L401 and L403, each checked byte for byte against the entry.
  - L401: "An inexplicit representation is not an absent one. [pianist; geometer; investigator] None of (R), Deploy and Build asks whether the relevant distinctions and transformations are written in a particular format: what they ask is whether those distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked."
  - L403: "A system's realization can use a partial, distributed, or temporally extended representation. ... A construction witness may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it: by responses that preserve its role bindings, send content-preserving recodings to the same transition and content changes to the changes the binding specifies, and lie on an active route, as reason use asks of an objection (Part IX). Use does not by itself construct: received content used as it was received keeps its inherited provenance. A carrier that passes content on without such use has relayed it, and relay is not construction."
- **DECLARATION:** "Part X now says that an inexplicit representation is not an absent one; that (R), Deploy and Build ask for no particular format, only whether the relevant distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked; that a representation can be partial, distributed or extended in time and need not be explicit all at once; that retaining a critical target can consist in being able to re-present the relevant distinction; that a construction witness may identify a constructed binding by its use, in the manner of reason use; that use does not by itself construct, so received content used as received keeps its inherited provenance; and that a carrier that passes content on without such use has relayed it."
- **CHECK:** "check 2, FIX. 'The realization' had no antecedent ... The relay sentence put O18's 'The rest is relay' at risk; NEW adds 'Use does not by itself construct ...'. The declaration is completed. Cases: as drafted, plus O18 guarded, O11 and O15 toward, O23 watched ..., N4 Q2 and N12 (Mr Okafor) watched."
- **CASES AT RISK:**
  - N21: toward.
  - N13 holds AGREE (the guard).
  - N12 and N15 hold.
  - O14 holds and is watched.
  - O23 is watched and holds.
  - O19 holds.
  - "O3, O11, O15, O18, O31, O43, O44 and O49 hold."
  - "O32 holds, and moves toward if anything."
- **Worklist W41:** "Gained. N21 (a tacit rule she formed herself) can be reached."
- **Earlier rulings.**
  - Batch 1 and batch 2 made none on R30.
  - The single S90 call (C25) failed and supports nothing.
  - The sibling ruling on Mimo C item 3 is KEEP. It is reconciled with this one in section 4.

## 2. The replies' arguments

**Atria C** closes with "R30: STANDS". Point 3, task (d), says "declared moves toward the fixed verdicts; none away":

> "R30 (lines 399-403) on N21: 'she knows it, tacitly' (an inexplicit representation is not an absent one; no format is required) and 'her grasp of it was not handed to her' (a witness may identify the binding by its use; the heard examples were incoming carriers, the binding hers, and the rest keeps its inherited provenance). On O15 the same clauses keep the arrows' provenance a hole in the diagrams rather than a hole in Sam's own construction."

The reply names moved verdicts, so the change is contested under Parts rule 2, whatever line it gives the change.

**Quotations checked (rule 8).**
- "she knows it, tacitly" is in N21's verdict ("Yes, she knows it, tacitly").
- "her grasp of it was not handed to her" is N21's second bullet heading, with a lower-case "h".
- "lines 399-403" is right.
- The glosses rest on text that is there:
  - "An inexplicit representation is not an absent one" (L401);
  - "incoming carriers" and "keeps its inherited provenance" (L399);
  - "by its use rather than by a statement of it" (L403).
- The O15 gloss is a paraphrase. It gives the verdict's first sentence and the first half of its second. It leaves out "and it is a hole in his account, because his cut followed them", but does not deny it.

**Mimo C** (given to the checker) closes with "R30: FALLS — identification criteria diverge from Part IX's reason use while the text and declaration present them as its own". Its three points:
- the binding, not "the operative deliberative rule", specifies the changes;
- there is no "structural map from the represented objection into the response suborganization";
- the text says "lie on" where Part IX says "lands on".

It proposes two repairs: copy Part IX word for word, or write "in a manner modelled on reason use". It names no case for R30.

## 3. Reading

**N21 (given; declared toward): Atria is right.**
- **Question 1, "she knows it".** Deploy asks for a representation by (R) that is faithful, has provenance, and is used in problem-directed activity as a retained capability (L397).
  - Ngozi's ordering of phrases she has never heard is faithful on its contract, and she retains it.
  - L401 says Deploy asks for no format, so her inability to state the rule no longer blocks "she knows it, tacitly".
- **Question 2, "formed it herself".** Build's witness must identify "the bindings constructed" (L399). Under file 11 a tacit binding could not be shown by a statement; that was the gap (worklist W41). Under L403 her use identifies it:
  - each class of adjective keeps its slot (role bindings preserved);
  - the same adjectives in another phrase go to the same order;
  - new adjectives go to the order the binding specifies;
  - all of this lies on the active route of her speaking.
- **Not received.** The rule is in no sentence she heard. So it is not "received content used as it was received", and not a composition of content-preserving transfers.
  - The heard examples are the incoming carriers.
  - "Reconstruction by a learner is construction" (L399) covers "rebuilt rather than invented".
- **Declared.** Both halves of the move are in the declaration:
  - "(R), Deploy and Build ask for no particular format";
  - "a construction witness may identify a constructed binding by its use".
- **No move away.** Whether a child's acquisition is selection rather than construction (L201, L405) is a question about unchanged text, and it pulls the same way under file 11. L401's "inexplicit ... not absent" allows the tacit represented target that construction needs (L197).

**O15 (given): holds at AGREE and does not move.**
- File 11 is already AGREE, with the passage SAME (S81 determination 01: "F11 AGREE ... Ruling: passage SAME"). No mark can move toward.
- R30's "received content used as it was received keeps its inherited provenance" adds support:
  - Sam followed the arrows as received, so their unrecorded origin stays theirs;
  - his cut is his, so "Sam's account of his own work is complete";
  - the arrows lie on the active route of his cut, so the hole passes into his account.
- Atria's gloss agrees with this but states only the first half. Nothing in R30 keeps the hole out of his account.
- The entry's CHECK says "O15 toward", and its CASES AT RISK says "O15 ... hold". Read against S81 01, "holds" is the mark, and "toward" can only mean support for the passage. This is recorded in the CHECK text below and needs no edit to the entry's text.

**Mimo's point, reconciled with the sibling ruling, which is upheld.**
- **The pointer is true of Part IX.** L379 asks these four things of an objection, so "as reason use asks of an objection (Part IX)" is true. "Of an objection" marks the pointer as a parallel applied to a binding.
- **The substitution is the one the parallel needs.** When the thing used is a binding, the binding fixes what a content change becomes. Copying "the changes specified by the operative deliberative rule" would ask a tacit binding for a deliberative rule it lacks, and N21 would be lost.
- **Leaving out the map weakens nothing claimed.**
  - "Responses that preserve its role bindings" is structural.
  - (R)'s fidelity and provenance are still required (L401).
  - Build's conditions still hold (L399).
  - The clause only says how a binding "may" be identified.
  - "Use does not by itself construct".
- **"Lie on" and "lands on"** put the same condition (L369).
- **"In the manner of"** already says "modelled on". Mimo's second repair changes words and no claim.

**Other cases.**
- **N13** holds AGREE. The parrot answers a rephrasing with a squawk or another sentence, and it would have repeated recipes just as readily. The content-change clause fails, so it has "relayed".
- **O14** holds. Kofi's phrases are received content used as it was received. Asked for a new sentence, he has no content change that goes to a specified change.
- **O18** holds. The tooth is a constructed binding. "The rest is relay" follows from "Use does not by itself construct".
- **O23** holds. A distinction must be "instantiated ... and used", and a passing mention is neither.
- **O32** holds. The finding was stated aloud and minuted. R30 adds a second route and removes none.
- **D3-T** is about selection by a tester and has no construction, binding or relay. R30 does not touch it.

## 4. Ruling

**KEEP.** W41.1 stands as drafted: OLD, NEW, KIND (CLAIM) and DECLARATION are unchanged. This is one reconciled ruling with the sibling ruling on Mimo C item 3, which also keeps the entry.

**Reason.**
- Atria's named moves are toward the fixed verdicts, and the declaration accounts for them:
  - N21 moves toward on both questions;
  - O15 holds at file 11's AGREE, and R30 only adds support.
- Mimo's pointer objection fails for the reasons given in section 3.
- No case moves away.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Atria said STANDS (declared moves toward on N21, 'she knows it, tacitly' and 'her grasp of it was not handed to her'; O15 kept a hole in the diagrams, not in Sam's construction). Mimo said FALLS (the witness criteria differ from Part IX's reason use: the binding for 'the operative deliberative rule', no structural map, 'lie on' for 'lands on'). Ruled KEEP after the cross-examination. N21 moves toward on both questions, as declared (no format for Deploy; a witness by use for Build). O15 holds at AGREE, which is file 11's mark (S81 01): R30 only supports the passage, and 'toward' above means no more than that. 'As reason use asks of an objection' is a marked parallel. The binding must replace the deliberative rule as specifier, because a verbatim copy would fail N21. (R)'s fidelity and provenance (L401), Build (L399) and the active-route clause keep the map's guard. 'In the manner of' already means 'modelled on'. No case moves away."
