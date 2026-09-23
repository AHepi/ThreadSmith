# W16-atria-L3-s2 - the content of the reply, as extracted by program

Extracted by send_w16.py from `W16-atria-L3-s2.record.json` (the record's `message.content`), unchanged below the rule. Family atria, lens L3, send 2. Verdict under plan W16 section 4.3: answer (HTTP 200, content not empty, finish reason 'stop'). The reply's `reasoning_content`, if any, is kept in the record and is not reproduced here.

---

## L3: what stage B licenses

**Point 1**

**Target:** W15 section 8, "It certifies": *"Those sixteen, and no others, may carry an arm difference when stage C's reports are marked in stage D: P4.1 and PA.3 over all sixteen; P4.2 and P4.3 over the eleven of section 6.1; P4.4 over the four (or the seven as written) of section 6.3; and P4.5 over the certified fields of the sort each of its clauses names."* And section 6.1: *"The cross-step fields that certified may carry an arm difference in stage C."*

**Claim:** The licence is granted for "stage C's reports" — kinds none of the 96 reports had — and the sentence that grants it is placed under "It certifies", as though stage B certified the licence. Stage B certified agreement on 96 reports of other kinds; the plan grants the licence. The reach limit is in W15, but three paragraphs later, under "It does not certify", and section 6.1, the section that derives the eleven-field list, carries no limit at all.

**Evidence:** (seen) W15 section 8, "It does not certify": *"The instrument beyond the kinds of report it was tested on. Under the qualified Derivation 3 (\"faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not\"), the certification holds for these 96 reports' kinds:"*, followed by *"Stage C's reports are all file-33 reports under arms. So what these fields would do on them is unconstrained by stage B in both directions."* (seen) W15, "Whose cases": *"No report was written under file 33, and none was handed a question."* (seen) W15 section 6.1, the whole licensing paragraph, contains no kind limit. (claimed) That stage C's reports are all file-33 reports under arms rests on W10 section 4, which is not among the documents given.

**What would settle it:** List the kinds of report stage C will produce (from the stage C plan, not in these documents) and check them against the two kind lists W15 gives in section 8. If no stage-C kind matches a tested kind, the licence sentence should carry the limit inside it and should separate "the plan licenses these fields" from "stage B certified agreement on these 96 reports". If a stage-C kind does match a tested kind, the limit should name which kinds are covered.

---

**Point 2**

**Target:** W15 section 8, "It certifies": *"The markers were Sonnet 5 at effort high, each armed with seven of the skill's eight files and the qualified Derivation 3."*

**Claim:** Two conditions of the certification are asserted here as fact. The documents show the markers read seven files; they do not show the served model, and they do not show the markers were given the qualified form of Derivation 3. The seven files include `word-list.md`, which states Derivation 3 without the qualification; the qualification comes from Semantics file 11, which is not one of file 33's eight files.

**Evidence:** (seen) W15 section 9: *"The model each marker was served. The workflow asks for `sonnet`, and neither the returns nor the audit records a model id. \"Sonnet 5\" is claimed."* (seen) W15 section 2, item 2: *"All 192 markers read exactly those seven."* (seen) W15 section 6.4: *"All 192 prompts have only the sections \"THE FIELDS\", \"THE REPORT\" and \"END OF THE REPORT\"."* (seen) W14 section 1 says the markers were *"told to read the skill (HV file 33, all eight files, with the qualified Derivation 3 stated)"* — told, by a plan whose instruction already omitted one file. (seen) `word-list.md` maps *"held only where it was tested"* to Derivation 3 without the qualification. (claimed) The qualification itself is from Semantics file 11, Part XVI, not among the eight files and not among these documents. (seen) `comparison.md`'s head uses the exact phrase *"armed with HV file 33 (all eight files) and the qualified Derivation 3"* — of the comparison worker, not of the markers; W15 appears to carry it across.

**What would settle it:** Read one marker prompt in full (`stage-B/w10/marking1/prompts/M001.txt`) and the stage-B workflow's instruction lines. If neither states the qualification, the markers met Derivation 3 only in `word-list.md`'s unqualified form and the phrase should be cut or sourced. Separately, grep `returns.json`, `returns_M085_rerun.json` and `tool_audit.json` for a served model id; if there is none, "Sonnet 5" stays a claim and the certification block should say so, as section 9 already does.

---

**Point 3**

**Target:** W15 section 6.3: *"After stage B no certified field records a part's mark: marks_per_part is struck."* followed by *"So P4.4, as this rule leaves it, reaches the marks only through test_remove. The other three certified fields are the report's shape, the modules the reader says it opened, and the attributions."*

**Claim:** The second sentence contradicts the first. `test_remove` does not record a part's mark; it records whether the remove test was applied. So under the four certified within-step fields P4.4 reaches no part's mark at all — stronger than W15 states, and it sharpens the question W15 puts to the owner.

**Evidence:** (seen) `criteria.json`, `test_remove`: `"kind": "enum"`, `"values": ["RAN", "NAME ONLY", "ABSENT", "CANNOT"]`, and its criterion is about taking a part away and saying what happens. (seen) `criteria.json`, `marks_per_part`: `"kind": "map_enum"`, values the eight marks, `"per": "part"` — the field that records a part's mark. (seen) `stage_b_record96.json`: `marks_per_part` `"certified": false`. (seen) W15 section 6.3 itself, quoting marking plan section 10: *"P4.4 \"is about the within-step *marks*, not about the vocabulary\"."* (claimed) Marking plan section 10 is outside the excerpt given here, so what P4.4 is about cannot be read directly.

**What would settle it:** Read marking plan section 10 (not in the excerpt). If P4.4 is about the eight marks on parts, then W15's sentence should read that P4.4 reaches no part's mark at all under the four-field reading, and the owner's question stands unanswered either way. If "within-step marks" means the test verdicts, then `test_remove` does reach them and the sentence should say "the test verdicts", not "the marks".

---

**Point 4**

**Target:** W15 section 6.1: *"P4.2 and P4.3 are read over 11 fields: those twelve less test_patches, which `affordance.json` records as afforded by no arms document (marking plan sections 13.4 and 15.2). The eleven are test_flip, test_reverse, test_hunt, test_addjob, test_rival, test_pull, test_inside, turned_own_test, same_explanation, pairs_that_pull and remove_in_groups."*

**Claim:** The licence names the fields but not that the instrument's own gauge for whether such a field has anything behind it on the arms — the "never varies" flag — is unimplemented, so a field taking one value on every run of every arm could carry P4.2 and P4.3. No step of stage B could test this (stage C's runs do not exist), but W15's section 9, whose job is to say what was not tested, does not name it, and HF2 covers only section 6's consequences.

**Evidence:** (seen) Marking plan 15.2: *"the gauge on all twelve is unchanged: a field that takes one value on every run of every arm is flagged \"never varies\" and carries no arm difference."* (seen) Marking plan 13.4's fourth ask of the harness, unchanged through 15: *"`agreement.py` must read `instrument/affordance.json` ... and flag a field that never varies across every run of every arm as \"never varies\" ... a field so flagged carries no arm difference."* (seen) Marking plan 14.6: *"until it is made, `agreement.py` builds its cross-step set from `sort` alone and P4.2 and P4.3 can be carried by a field with nothing behind it."* (seen) `criteria.json`, `remove_in_groups`: *"No report in either folder removes in groups, so RAN is untested here and the field is at risk of being uninformative"* — a live candidate. (seen) W15 HF2 names that no program applies section 6's consequences; the never-varies flag is an ask of the harness, not a section 6 consequence. (seen) W15 section 9 lists what was not tested, from *"Which marker is right"* to *"Whether a marker agrees with itself"*; the never-varies gauge is not among them.

**What would settle it:** Grep `code/agreement.py` for the never-varies flag; if it is absent, W15's licence for P4.2 and P4.3 should say that the gauge the instrument wrote for that licence is not yet made. Once stage C's runs exist, take each of the eleven fields' values across every run of every arm and check for constancy; a field constant throughout carries nothing and should be flagged.

---

**Point 5**

**Target:** W15 section 8, "It does not certify": *"Anything across model families. Stage C's reader is Sonnet 5 as well (W10 section 4), so in stage D a model will be marking its own family's reports. Stage E's examiners of other families are the only check on that, and the DeepSeek examiners wait on the key (decision W17)."*

**Claim:** This names the cross-family limit but not the mirror-image one: the case stage D will actually present — a Sonnet 5 marker on Sonnet 5 reports — was tested on only 24 of the 96, all on two documents, while 72 of the 96 are DeepSeek-family reports. The per-set certification the licence rests on is mostly the cross-family case stage D will not have.

**Evidence:** (seen) W15 section 8's own kind list: *"p52: DeepSeek V4.1 Flash on 16 outside documents"* and *"The repeat set: DeepSeek and Sonnet 5 readers on two documents (P3, F4) in modes 1 and 2, under skill files 30 and 31."* (seen) `stage-B/independent-check/README.md` section 1: *"The sets are p52 48; rep, rep31, son and son31 12 each."* (seen) `criteria.json` names the record folders `runs_sonnet5/`, `runs_repeat/`, `runs_sonnet5_31/` and `runs/`. Worked out from those: son and son31 are the Sonnet 5 folders, so 24 of 96 reports are Sonnet-written and 72 (p52 48, rep 12, rep31 12) are DeepSeek-written; the repeat set of 48 mixes 24 of each, and only that set tests same-family marking. (seen) W15 section 9 does not name this split.

**What would settle it:** Using the marks and the closed mapping, split each of the sixteen certified fields' repeat-set counts into son+son31 (24) and rep+rep31 (24) and compare. If the Sonnet 24 agree much as the DeepSeek 24, the licence's evidence for the stage D case is as the per-set counts suggest and the point is recorded; if not, the licence's same-family reach is thinner than the per-set counts show and W15 should say on how many reports the stage D case was tested.

---

**Point 6**

**Target:** W15 section 6.3: *"So swap's failure is held by the close set's report kinds, and poke's is not."* And section 8: *"**That the kind of report doesn't matter.** The evidence says it does. Several struck fields fail mostly on p52's mode-0 reports, where the reader had no skill: test_swap: 5 of its 8 disagreements; shape_elements: 9 of 13 in p52; marks_per_part: 9 of 11 in p52; test_addjob: 7 of its 9 in p52."*

**Claim:** The disagreement pattern is read as held in place by report kind. The rival — that the repeat set agrees more on nearly every field, so swap's 48 of 48 there is what that set gives anyway — is not named in section 6.3, though W15 names exactly this rival for a different claim in section 5. And the numbers that would separate the two, p52's mode-1 and mode-2 counts on the same documents and the same reader, are in neither the counts file nor the independent's output.

**Evidence:** (seen) W15 section 5, for W10.16: *"**The rival:** set composition and small numbers. 16 of read set A's 20 reports are in the repeat set, which agrees more on nearly every field."* (seen) W15 section 6.3: *"test_swap's 8 disagreements are all in p52, and 5 of them are p52's mode-0 reports ... The repeat set agrees 48 of 48."* (claimed) The "5 of 8", "9 of 13", "9 of 11" and "7 of 9" splits come from `results-w15/output.txt` section 7, which is not among these documents. (seen) The independent's E3 gives the mode-0 agreement counts: *"There shape_elements is 7/16, marks_per_part 7/16, test_addjob 9/16, and test_swap, test_patches and rivals_built 11/16 each"* and *"rivals_built is also low in p52 mode 2 (11/16), so mode 0 is not the whole story."* (seen) E3's separating check is a different one: *"compare rep+son with rep31+son31 ... No difference is larger than 4 of 24"* — skill version, not mode. Neither program reports p52 mode 1 against mode 2.

**What would settle it:** From the marks, compute per-field agreement within p52 split by mode (0, 1, 2) — same 16 documents, same reader, differing only in whether the skill was present. If modes 1 and 2 agree far more than mode 0 on test_swap, shape_elements, marks_per_part and test_addjob, the kind reading stands and the claim should still name the rival. If modes 1 and 2 agree as little as mode 0, the separation fails: the difference is p52 against repeat, not skill against no skill, and section 8's "The evidence says it does" should be withdrawn.

---

**On the two remaining questions in this lens:** I found no place where W15 reads marker agreement as a field measuring what it is meant to measure, and no place where a count is read as a score; section 8 states both limits expressly (*"Agreement between two markers is not validity"*) and section 10 lists the score reading as a trap. I also found no claim narrower than the evidence supports in the licensing sections — the under-claims I checked (the in-place run re-testing no rule, the audit being claimed, question_identity being untested) are all stated by W15 itself.