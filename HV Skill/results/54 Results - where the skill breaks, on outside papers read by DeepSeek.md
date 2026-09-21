# 54 Results - where the skill breaks, on outside papers read by DeepSeek V4.1 Flash

Phases 3 and 4 of plan 49, 21 September 2026. Marking under plan 52, frozen before any report was read. Reader: DeepSeek V4.1 Flash. Marker: Claude, who wrote the skill and chose the corpus; that flaw is stated in plan 52 and is not repaired here.

## The short answer
On sixteen outside documents, 48 reports, the skill's words did work in a reader that had never seen them, and they broke in two places. Both breaks are in the skill's wording and both are small. The larger finding is not a break: one of the eleven tests, *look inside*, has almost no purchase on a single document, and the skill does not say so.

## What was marked
- **Close marking:** sixteen sources drawn before the run (two per domain), three modes each, 48 reports, mode labels hidden. Per report: the shape; each of the eleven tests as RAN (applied with a concrete change), NAME ONLY, ABSENT, or CANNOT; five claims about the document checked against its text by search and marked SUPPORTED, MISREAD or OUTSIDE; breaks, with the skill's line quoted; two yes-or-no marks.
- **Light marking by program:** all 147 reports (file 53).
- **Conversation mode:** twelve dialogues, read for the questioning, not marked under plan 52, which did not cover it.

## The table, condensed
Per mode, over the sixteen sources. Not a score: plan 52 forbids adding these up into a verdict, and the counts below are read box by box in `marking/close_marks_restored.json`.

| | Mode 0, no skill | Mode 1, skill pasted whole | Mode 2, router live |
|---|---|---|---|
| Reports in the method's form | 0 of 16 | 16 of 16 | 16 of 16 |
| Test slots RAN / NAME ONLY / ABSENT / CANNOT (of 176) | 18 / 2 / 156 / 0 | 148 / 4 / 24 / 0 | 140 / 5 / 31 / 0 |
| Claims SUPPORTED / MISREAD / OUTSIDE (of 80) | 73 / 0 / 7 | 75 / 3 / 2 | 77 / 0 / 3 |
| Breaks | 0 | 2 | 0 |
| Controls left standing (R1, D2) | 2 of 2 | 2 of 2 | 2 of 2 |
| Reached a finding by testing the text | 14 of 16 | 16 of 16 | 16 of 16 |

Which tests ran, by mode, out of sixteen reports: flip, hunt-the-answer, pull and check-the-patches ran in every skill-mode report; remove, swap, add-a-job and rival in 12 to 15; poke in 11 to 12; reverse in 12 to 15; **look inside in 3 (mode 1) and 0 (mode 2)**. In mode 0, only poke (6) and rival (7) appeared at all.

## Where the skill breaks

**Break 1. The flip test fires on a derived conclusion.** Bostrom's paper concludes a disjunction that follows from a count. One skill-mode reader (P3, mode 1) applied "Flip the outcome: had the opposite happened, could the same explanation have covered it? If yes, it explains nothing" and called the disjunction's covering every outcome "the weakest joint". A theorem covers every outcome because it is a theorem. The by-domain proofs section has the right tool (remove a condition, show a counter-case), but the main file's flip fired first. The other skill-mode reader on the same paper (mode 2) read it correctly: "the argument partitions rather than absorbs. It passes." The mode 0 reader also read it correctly. So the skill permits this error rather than forcing it, and one run each cannot say how often.

**Break 2. Two vocabularies for a design choice.** The design section of `by-domain.md` marks decisions held, free or inherited; `reporting.md` maps "free is loose and harmless; inherited is fitted" in one line beside the eight marks. One reader (F4, mode 1) marked the time machine's two levers, a free design choice, as **fixed**, which the skill reserves for an owner's untested requirement. The mapping line is easy to miss.

**Not a break, but the skill's largest gap on this corpus: look inside.** The skill says "matching the results is not matching the workings ... use changes that reach inside." With one document in hand there is nothing to reach inside, and the readers said so by silence: the test ran with content only where the document itself replicated a calculation (Herndon on Reinhart and Rogoff) or named two mechanisms for one job (David on QWERTY). The skill gives a reader with a single text nothing to do at this step and does not say that the right mark is *unknown, with the test named*.

**No CANNOT marks.** Not one report said a test had no purchase. On the rule cases the readers wrote "you cannot poke the world; you rewrite the rule"; on the history and astrophysics cases, "the change list is made of comparisons"; on the proofs, changes to conditions. That is the domain file working, not an edge. Either this corpus never met the skill's edge, or the reader adapts silently where a person would stop. The second cannot be ruled out from these reports.

## Where the reader broke, and what the skill did about it
Three MISREAD claims, all in mode 1, none in mode 2 or mode 0:
- R1: "serve tomatoes as dessert; the opinion says they would then be fruit." The opinion says fruits are generally served as dessert. The reader's inference was put in the court's mouth.
- F4: the Psychologist "explains" the vanishing as too fast to see. The Time Traveller offers it and the Psychologist assents.
- F6: "left a fake parcel at the sweet shop to be forwarded to Westminster." The real cross went to Westminster; Flambeau held the dummy.

All three arose inside a test (poke, reverse, part-listing), not in the frozen question. The skill's step 3 asks for the parts "in the owner's own words"; the misreads happened where the reader paraphrased. The mode 0 reader on the same story got the parcels right. Nothing in the skill catches a misread; it has no step that sends the reader back to the text with a quotation.

## What the skill found that the bare reader did not
Findings present in a skill-mode report and absent from the mode 0 report on the same source. Each was checked against the text.
- **"The same explanation at this level."** Six sources drew this verdict from a skill-mode reader and none from mode 0: the court's test against the judges' own table manners (R1); "the market chose well" against "locked in wrongly" on David's evidence (E3b); an incremental update against a necessary one (I2); a conjuring trick against a time journey (F4); the trilemma's three arms (P3); learning-styles persistence against the label hung on a habit (S15).
- **Hunt the answer in the starting points, on the document's own admission.** Herndon and colleagues write that their initial results "closely resemble the results we ultimately present as correct"; the mode 2 reader read that as corrections fitted to a target already in view. Mode 0 did not.
- **Pairs that pull, inside one document.** Chalmers: the conceivability premise carries the gap while organizational invariance denies the conceivable case (found by both skill modes as P3 against P7 and as inverted spectra doing opposite work in adjacent sections). Englert and Bertrams: criticise figure tracing, then lean on it. Newton and Miah: "reassuring" and "pessimistic" readings of one number in one discussion.
- **Flip the origin.** The PRISMA survey asked whether to keep, modify or remove each item, so "a process that always outputs revise explains neither the timing nor the content."
- **Flip finds a symmetric mechanism.** On QWERTY: had the rival won, the same Polya-urn parts would explain it, so the mechanism explains that one standard locked in and cannot pick which.
- **Remove in groups.** "B and C: cut B alone and the job survives on C; cut both and it goes" (Smith v. United States). "Exclusions plus weighting together, about 1.9 points; neither alone" (Herndon).
- **Rename the held part.** "Grown in kitchen gardens" is a bystander; the held part is "eaten as part of the main meal" (R1). "Three duplicate ACKs" is fitted; the held part is "a small number above the reordering depth" (D2).

## What the bare reader had that the skill modes lacked
- **Recall.** Mode 0 faulted RFC 2001 with later RFCs, Smith with later cases, Chalmers with zombie arguments from elsewhere, and the Time Machine with Minkowski. The skill modes stayed inside the document. That is both a cost (a real weakness on the record goes unmentioned) and the point of the method.
- **Two right readings where a skill mode went wrong:** the parcels in The Blue Cross, and the trilemma.

## Mode 1 against mode 2
One run per box, so an observation, not a result. Mode 2 had no misreads and no breaks; mode 1 had three and two. Mode 2 ran slightly fewer tests with content (140 against 148) and opened the idea-in-depth and reporting modules in every run without being told to. On the tomato case mode 2 reached the same-explanation verdict and mode 1 did not; on Herndon, mode 2 found the target-in-view admission and mode 1 found the critical block. Two runs of the same box disagreed on whether RFC 2001's "much less than 1%" is a gauge or an unstated one, both reading the same sentence. Reader variance between runs looks as large as the difference between the two skill modes.

## Conversation mode, read but not marked
Twelve dialogues, six exchanges each, the author played by a second DeepSeek session holding the document. The skill's questioning half works in this reader: it turned the tests into questions in the skill's own forms ("give me both halves of a poke", "hand you the tool: give me a different reading that would work just as well", "add one job", "flip it", "for each part, was it forced, worked out, or written down", "build the strongest rival and name one change that separates them"), and the author conceded under them ("You've caught me. No experiment I can name would show (d) false. Concede: (d) is fixed, not fitted"). No trouble from the skill's negative wording was visible. Two departures from the skill: the readers asked three to five questions a turn against "one part and one change at a time", and one reader (E3b) wrote its full report in its sixth turn before being told the conversation was over, then wrote another.

## Against plan 52's failure conditions
- The skill is idle: **no**. Shape, tests and findings differ in every box.
- The skill is ritual: **no**. RAN 288 against NAME ONLY 9 across the skill modes.
- The skill makes a prosecutor: **no** on the two controls in the sample, which is too few to say much.
- The marking is noise: **partly**. Claim-checking by search worked, but the marker's first pass judged ten claims from the first search hit and got them wrong; all ten were corrected on a recheck that printed every hit. The remaining three MISREADs were confirmed by reading the passages.
- The corpus is the wrong shape: **cannot tell**. No CANNOT marks appeared anywhere, which is either no edge met or an edge crossed silently.

## Expectations from plan 49, marked
1. Recall carries the famous cases: **partly seen**. Mode 0 leaned on the record; the skill modes did not, even on ego depletion and debt.
2. The setups part where the criticism has to be built: **seen**, on the six same-explanation verdicts and the pulls.
3. Test over recall: **seen**. Every skill-mode report reached at least one finding by testing the text.
4. Controls: **seen** on two; the other six controls were not in the close sample.
5. The semantics adds little: **not tested**; the semantics was not given to the reader in this design.
6. The supporter's own pokes accepted as held: **seen once** (D2, the <1% figure taken as a gauge by one reader and as unstated by another).

## What this does not show
- Anything about the truth of any of the sixteen documents.
- Anything about repeatability: one run per box, and two runs on the same paper disagreed on the flip.
- Anything about 33 of the 49 sources beyond their shape.
- Anything about a second marker. The marker wrote the skill, chose the corpus, and got ten marks wrong on the first pass.
- Anything about the router beyond which modules it opened.

## Three changes to the skill, proposed and held out until tested
1. **Flip, one clause:** "A conclusion that is derived (a theorem; a disjunction that follows from a count) covers every outcome because it is derived. Test it with the proofs tests, not the flip."
2. **Design vocabulary, one line moved:** put "free is loose; inherited is fitted; a free choice is never *fixed*" into the design section of `by-domain.md`, where the reader is when it needs it.
3. **Look inside, one clause:** "With one document and no way to reach the workings, mark the part *unknown* and name the test; do not mark it held on matching results."

## One next step
Run P3 and F4 three more times each under modes 1 and 2, with the skill unchanged, and count how often the flip break and the *fixed* misuse recur. If they recur at all, apply changes 1 and 2 and run the same six again. That settles whether the two breaks are the skill's or the run's.
