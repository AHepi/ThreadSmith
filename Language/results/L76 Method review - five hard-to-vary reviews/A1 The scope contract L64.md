# A1. The scope contract L64, tested as an explanation

Reviewer A1, 22 September 2026. Subject: `Language/authority/L64 Scope - the contract the language claims, second version.md` (190 lines), accepted by the owner without strikes (Decisions L7) on 21 September, before L65, L66, L71 and L72 were run.

**How I know things.** I ran nothing. I read files, including program source. So no claim below is tagged **seen** in the strict sense of a printed output I watched; where a printed output matters I name the file that holds it and tag the claim **read**. Tags used: **read** (I read it, file and line named), **worked out** (my reasoning from read things), **assumed**. Line numbers are from `cat -n` on the file named.

---

## 1. The question, frozen

L64 is a design document, not a diagnosis. So the question it answers is *does it achieve its purpose?* — and its purpose is set by its own line 5:

> "to say, in one place and in advance, which texts the language claims to handle, which changes the checker claims to track, which findings it promises, what it leaves out and how anyone would see it leaning on the leftovers" (L64:5).

Range: prose of the kinds in section 3, at the lengths in section 1, run through 38/39 and the two rigs. What is asked: whether each clause of L64 is held in place by something — an owner's job, a run in the record, or a result now in hand — or whether a near neighbour of that clause would serve the contract just as well.

I hold this question still throughout. I am not asking whether the language is good, whether the findings are true, or whether the owner should accept the contract.

---

## 2. Its jobs, and whether the tags are right (question a)

L64's section 2 lists sixteen jobs with tags. Checked row by row against `Language/records/Language - Decisions.md` and `Language/records/Checked reasoning language - Decisions.md` (**read**).

**Tags that are right.** Rows at L64:38 (Decision 1), :39 (Decision 5), :41 (Decision 12), :42 (Decision 13), :43 (Decision 16), :47 (decision L6), and the six rows tagged *added* at :48–:53 all match the owner's words as recorded. Row :44 and :45 are the owner's words at Decisions L4, correctly *given*.

**Five things are wrong or loose.**

**(i) Lesson L3's own fix was not applied in the file that was made to apply it.** Lesson L3 (`Language - Lessons.md`:10) says: *"a job marked 'given' quotes the owner's words beside it; a paraphrase is marked as Claude's until the owner has read it; L64 corrects the file"*. L64's jobs table quotes no owner's words in any row: the Where column gives a decision number and the Job column gives Claude's paraphrase (L64:36–53). The lesson was written because a paraphrase reversed the owner's meaning; the correction reproduces the form that allowed it. **read**.

**(ii) The meaning-preservation job is circular.** L64:46 states the job as *"the ledger commits the writer to what the prose commits them to, **as the contract says it must**"*, tagged given. The owner's words at Decision L6 are *"meaning preservation is as essential as the contract says it is"* (`Language - Decisions.md`:14). The owner deferred to the contract; the contract cites the owner. The content of this job is therefore set by L64 itself, not by the owner. By the skill's *hunt the answer in the starting points*, the job is the part under another name. The operative content — *"faithful on the admitted changes, not the same words"*, and the variation test at L64:143 — is Claude's, and should be tagged **added**, not given. **worked out**.

**(iii) "An honest attempt over correctness" is tagged fixed, and it is a permission, not a requirement.** Decision 3 reads *"Correctness isn't a priority. An honest attempt is perfectly acceptable"* (`Checked reasoning language - Decisions.md`:9). The skill's *fixed* means the owner made it a requirement that is not up for test. A relaxation marked fixed cannot hold any part in place, and it can absorb any failure: every miss in sections 3 and 4 can be answered "correctness isn't a priority". This is a catch-all at the level of the job list, and it has no gauge. It also pulls directly against the job at L64:46 (meaning preserved, essential), and that pair is not among the pairs that pull at L64:154–157. **worked out**.

**(iv) One row mixes two of the skill's word lists.** L64:52 tags the shape book job *"added, borrowed"*. *Borrowed* is one of the eight marks, not a job tag. Log L75 caught the same error in section 7 (where *Borrowed* heads a provenance list) and called it "a relabel for L64's next version"; it did not catch this one, in the jobs table. **read**, `Language - project story.md` L75.

**(v) A given job is narrowed without saying so.** Decision 1 ends *"Basically anything that will aid in reasoning"* (`Checked reasoning language - Decisions.md`:7). L64:38 keeps the four named fault kinds and drops the open clause. Section 4 then makes the list of findings closed. This narrowing is what lets finding 1 below sit outside the promises. By the skill a narrowed range is a part like any other and needs its own reason inside the explanation; none is given. **worked out**.

**One more, smaller.** L64:39 marks the external checker *fixed*. The shared record's own open list says *"Whether to reopen decision 5 (external checker essential) ... Not reopened by Claude"* (`Checked reasoning language - Decisions.md`:54). A job the owner has left reopenable is marked by L64 as outside the test, with no note. **read**.

---

## 3. Part by part (question b)

Marks are the skill's eight. Provenance is in its own column. Nothing is added up.

| # | Part (L64 line) | Mark | What holds it, or what would settle it | Provenance |
|---|---|---|---|---|
| 1 | Target: everyday reasoning prose, one writer, one level deep (:13) | held | job at :42 (given, Decision 13); every §3 row names a case run | fitted |
| 2 | The length limit, "about a dozen sentences ... Longer: **unknown**" (:13) | unknown | a growth-of-error test. L66's longest passage was 11 sentences (`Gauge_OpenAI_Codex.md`), so nothing in hand reaches it | built |
| 3 | Two queries, faults and consequences (:16–:17) | held | jobs at :38 and :44 (both given) | asserted |
| 4 | The six admitted changes (:20–:25) | held | each row names the run that forced it | fitted |
| 5 | "These are the whole of what 'consequence' means here" (:19) | unknown | run the consequences mode under the other five changes. L65:28 and L71:42 both say only removal was run | built |
| 6 | Grain rule (:28) | borrowed | rests on file 10, Derivation 2, not tested here | built |
| 7 | "This is the level; it is not a loss" (:28) | loose | a neighbour does every job and more: "two commitments the changes cannot separate are *recorded as not separated, and counted*". As written the clause can re-describe F15 (a BECAUSE and its exact denial raising no contradiction) as a level, not a failure | asserted |
| 8 | The jobs table and its tags (:36–:53) | held if | held only by the owner's words, which it does not quote (section 2 above); settle by putting the quotes in and asking the owner | asserted |
| 9 | §3 rows other than :72 (:65–:77) | held | each names a case in the log | fitted |
| 10 | §3 :72, texts with a story/report told inside | held if | its witness is log 37, the orchestrator's own ledgers, which L72:31 says did not follow 39's told-world rule; settle by re-translating T05 and T07-B under 39 and re-running | fitted |
| 11 | §4 rows with a case, other than :90 (:87–:107) | held | each names a case | fitted |
| 12 | §4 :90, "Jump, with candidate missing lines ... T10-D" | held if | same defect as #10, and sharper: L72 E5 (L72:40) reports that under 39 the T10-D BECAUSE "sits inside the told world and is never tested". The witness for the JUMP promise was produced by a translation that broke 39's rule 30 | fitted |
| 13 | §4 :108–:109, the two "promised and failing" rows | held | the stated rule that a promise stays listed until patched; F15 and F09 are what it is for | built |
| 14 | §4 :110, consequences | unknown | says so itself. L65 and L71 have since run; the row has not been re-marked, because L64 is never edited | built |
| 15 | §5 exclusion row :123, "Who believes, knows or wants what ... the content as TOLD **only when the text presents it as told**" | loose | 39:30 says *"Who believes, wants or concludes what. Send the attribution to the bin, and write the content as TOLD in that person's world"* — a different set (concludes, not knows) and no guard. The two documents disagree exactly where finding 1 lives (T11-B is "the inspector's reason for **concluding**") | built |
| 16 | The bin gauge, "bin entries per sentence" (:120) | loose | two better gauges are already in the same file: the count of findings leaning on filled-in lines (:155) and the count of "filled in" readings (:128). See question d | built |
| 17 | The bin threshold, "more than a third of sentences" (:120, :134) | idle | it fires on 18 of 18 L66 passages (L66:38), so it tells no text from another; and setting it would void the findings of the run that tested it. See question d | built |
| 18 | Unshaped-verb gauge and threshold (:130) | held | it discriminates: the worker's table flags P07, P09, P10, P13, P17 under it and not the rest (`Gauge_OpenAI_Codex.md`) | fitted |
| 19 | "Cannot tell" gauge (:131) | held | printed; fired once in eighteen (P16) | fitted |
| 20 | Length note (:132) | idle | nothing in hand reaches the length; removable today with no loss | built |
| 21 | The four-layer table (:140–:145) | held if | held only where an "error that is not" cell names the failure. Two of the four forced findings have no such cell. See question e | built |
| 22 | "Which layer failed ... is a fresh choice" (:147) | loose | a neighbour constrains and does every job the sentence does: "the layer whose cell names the failure; where two cells name it, say which was chosen and why". The table already does more than the sentence admits | asserted |
| 23 | Pairs that pull (:154–:157) | held if | the first pair (more consequences against exact read-back) was tested and found not real at 27 lines (L65:21; L71:39), so it holds nothing; the pull the runs did find — 39's told-world rule against §4's promised findings — is not on the list | built |
| 24 | The catch-all roster (:159) | loose | replace with a roster that includes told worlds and "a query never asked". See question d | built |
| 25 | Where the parts came from (:161–:165) | held | it does say which parts to check first, and L66/L72 bore that out (the borrowed shape book and the fitted patches are where the trouble is) | built |
| 26 | §8, what would show this scope is wrong (:170–:174) | idle | none of the five can fire on what actually went wrong, and one cannot fire at all. See question f | built |
| 27 | The freeze rule (:5 and :186) | loose | the file contradicts itself — :5 "the owner's strikes make **L65**", :186 "Strikes and changes make **L64**" (copied unchanged from L63:185). And L65 was taken the same day by the consequences prototype, so :5 cannot be honoured under the never-overwrite rule | asserted |

**Pairs held only together.** #16 and #17 are *held, jointly with* each other in the negative sense: neither the gauge nor the threshold does its job without the other, and L64's own trap says so — *"Reading the gauge without the threshold. A number with no line is decoration"* (:188). No line is in force today (section 9 leaves the thresholds to the owner, :179), so by its own trap the bin gauge is decoration as things stand. **read**.

---

## 4. Whole-explanation checks

### Flip

Had L66 come back clean on all eighteen passages, L64 would have covered it: twelve NO FAULT FOUNDs are already read as the contract working. Had it come back failing, L64 covers that too, through :120 — every passage is over the proposed threshold, so *"its clean report means nothing"*. Both outcomes are absorbed, and by the same clause. That is the flip failing, and it fails on the threshold, not on the body of the contract. **worked out** from L64:120 and L66:38.

### Reverse: poke the cause, then the effect

Poke the contract: nothing in `rigs/` or `tools/` names L64 (grep over `tests results tools rigs` returns hits only in plans, handoffs and returns; **read**). Change L64 and no run changes. Poke the effect: the gauge line the threshold would be read off, `run_check.py`:331, was written before L64 and is not derived from it. So the contract is downstream of the rig, describing it, not upstream controlling it. That is allowed for a contract, but it means no test of the rig is a test of L64 unless someone carries the number across by hand — which is what L66's E6 did, and what L71 did not do at all.

### Add a job

L64 gives itself a job at :5: *"Every later test is run against a version of this file and says which."* Of the four tests now in hand, L65, L66 and L72 name L64 in their plans; **L71's plan does not name it** (grep of `tests/*.md`; **read**). One in four fails the job the contract set for itself, four days after it was accepted.

### The answer hidden in the starting points

Two places. The meaning-preservation job (section 2 (ii)). And the grain rule's closing clause (#7): whatever the contract's changes cannot separate is defined as one commitment, so a failure to separate can never appear as a failure. F15 is a live case of exactly that shape.

### Look inside

Matching the results is not matching the workings. I read the driver rather than trusting the reports.

- Finding 2 is confirmed at the code: `run_check.py`:276–281, `results_tied_to(fact)` collects, for every `claim_because(N, E, C)` whose cause is the changed fact, the lines that state the effect, and sets them aside. It never consults `produced`. The report prints only *"Set aside, because your ledger says they came from what was changed"* (`run_check.py`:297). Astra Pro's finding D is right at the mechanism, not just at the output. **read (code)**.
- Finding 3 is not exactly as log L75 states it. `describe_lines` prints `line %s [%s, sentence %s]` for every line it lists (`run_check.py`:47), and it is called by the CONTRADICTION, FOLLOWS, CIRCLE, DEPARTURE, PLAN, WHAT-IF and supposition branches. What lacks a sentence is the *head* of a claim-based finding (`'BECAUSE-claim on line %s'`, :99; `'SINCE-claim on line %s'`, :145) and the two branches that list no lines at all: JUMP (:124–:138) and NO CONNECTION (:158 onward). That is precisely the set L66 E7 could not trace — seven jumps and no-connections, sentence traced on none (L66:39) — and precisely why the contradiction criterion was unmarkable: no contradiction occurred, and a contradiction would have carried its sentences. The fix is still one change, but it belongs on the two heads and the two branches, not on "the driver in general". **read (code), worked out**.

### Pairs that pull

The one L64 names first (consequences against read-back) has been tested twice and found not real at this size (L65:21, L71:39). The one the runs found is not on the list: **39's told-world rule against section 4's promised findings**. Making the translator more faithful to attribution (39:30) makes more of the writer's reasoning unreachable by the checker (patch 12). That is a joint failure of two parts that each pass alone, which is what the skill says to look for in a design.

A second, unnamed: **Decision 3 (honest attempt over correctness, tagged fixed) against L64:46 (meaning preserved, essential)**.

### Check the patches

The bin threshold at :120 is a patch made in advance, in the skill's exact sense: it is a rule written before the run that can absorb any failure after it. Its bill has already arrived. P14 is a text of a kind section 3 admits (:65, an argument that something produced something), and finding 2 is a failure of a promise section 4 makes (:103, "A what-if holds, fails, or cannot be run"). But under :120 P14 is over the threshold, *"reported as outside scope, and its clean report means nothing"* — so the strongest L66 finding is voided by the contract's own patch. The owner has not set the threshold, so this has not happened yet; it would happen the moment the number at :120 is adopted as written. **worked out** from L64:120, L64:103, L66:33–38.

### Rivals

The best rival to L64 is a contract identical to it with **no section 3 and no section 4** — a scope document that says only what is excluded and what the gauges are. Can any change in the change list tell the two apart? Yes, and only one that has been run: L66 E7 and L72 E5 turn on whether a promised finding was reached, which the rival cannot state. So sections 3 and 4 are the part of L64 doing real work, and sections 5, 8 and 9 are the parts that survive every change made so far.

### The change list — what it leaves out

L64's change list is section 1's six admitted changes. It leaves out, without saying so, **every change to the report's wording** — and that is where three of the four forced findings live (2, 3, and the told-world wording fault of L72:50). The non-vacuity condition at :116 covers only excluded *changes*: *"every excluded change is excluded by a stated scope, never silently."* It says nothing about an excluded *query* or an excluded *report line*. That is the hole finding 1 falls through.

### The natural swap test, already run by the record

L63 and L64 differ in exactly five hunks (`diff`; **read**). One of them **reverses a central given job**: L63:46 said *"Meaning preservation is not the priority here"*; L64:46–47 says the opposite. Sections 1, 3, 4, 5, 8 and 9 are word for word unchanged, and L64:3 says so: *"The jobs table, section 6 and section 7 are corrected; nothing else is changed."*

So: the texts claimed, the findings promised, the exclusions, the gauges, the thresholds and the list of what would refute the contract all survive a reversal of one of the contract's own given jobs. By the skill, those parts are not held by that job. This is the single strongest result in this review, and the project produced it itself without noticing what it was.

---

## 5. Do the four forced findings fall under the contract's promises? (question c)

| Finding | Where it falls | Verdict |
|---|---|---|
| 1. A reported BECAUSE or SINCE is never tested (L72, T10-D and T11-B) | §3:72 admits the text kind: *"A story, note or report told inside the text, one level \| Nora's story (T07-B); the note (T05) \| seen, log 37"*. §4:90 promises *"Jump, with candidate missing lines \| A, T10-D \| seen"*. But §4:105 promises only *"Inside a told world: a contradiction, or none"*, and 38:111 promises the same | **Partly inside, and the contract does not say which.** The text kind is in scope and the JUMP is promised, but the only promise L64 makes *about* told worlds is contradiction. L64 nowhere says whether the promised findings apply inside a told world. So the failure can be called a refutation or an unstated exclusion at will — which is the easy-to-vary property itself. Note also that §4:90's witness is void (part #12), so the JUMP promise has no surviving told-world case at all |
| 2. A what-if HOLDS on a BECAUSE the same run judged a JUMP (L66, P14) | §4:103 promises *"A what-if holds, fails, or cannot be run"*, seen on K21, K22, N25-B. §6:144 names the error under the checker layer: *"a what-if that holds when the ledger cannot say (F09)"* | **Squarely inside.** The contract promises the verdict and names this error kind, under a layer, as one that is not acceptable. It refutes the promise at :103. The only escape is the threshold at :120 (see "Check the patches") |
| 3. The sentence number is missing from JUMP and NO CONNECTION findings (L66 E7) | Not in §3 or §4 at all. §4 lists findings, not their traceability. It falls under §6:145: error that is not — *"Any finding a reader cannot trace to a sentence"*; success — *"A reader given the report alone names the finding and points at the sentence"* | **Outside sections 3 and 4; inside section 6.** The read-back row names the failure and its success test exactly, and the test was run and failed |
| 4. `consequences.py` pools told and supposed lines with the actual ledger (L72, T07-B) | Not in §3 or §4. §4:110 marks consequences **unknown**, so nothing was promised. It falls under §1:25, the admitted change *"Open a told world and look at it alone (**seen**, patch 15)"* | **Outside sections 3 and 4; inside section 1's change list.** The tool breaks an admitted change. It cannot refute a promise that was never made |

Two of four fall under sections 3 and 4; and of those two, one (finding 1) falls under a promise whose witness no longer stands.

---

## 6. The bin threshold and its gauge (question d)

**Is it a catch-all without a gauge in the skill's sense? Yes.** The skill's gauge is *"something that can be measured and that would show the catch-all is swallowing a job."* Three separate defects, each with a location:

1. **The gauge column and the threshold column measure different quantities.** L64:118–120 gives the gauge as *"bin entries per sentence"* and the threshold as *"a text where more than a third of **sentences lose something** to the bin"*. Entries per sentence and sentences that lost something are not the same number.
2. **The driver prints a third quantity, mislabelled.** `run_check.py`:331–332 prints `len(meta["leftover"])` as *"%d of %d sentences went to the leftover bin (not checked)"*. The worker says so in its own words: *"the rig-1 driver's printed gauge counts `len(leftover)`, which need not equal distinct source sentence IDs. The original P01 report prints 9 of 10 because it has nine leftover entries; they concern eight distinct sentences"* (`Gauge_OpenAI_Codex.md`). The parenthetical "(not checked)" asserts the strong reading the number cannot carry.
3. **It does not measure jobs swallowed.** Both outside agents said so independently. Astra Pro: *"'Every sentence has an excluded fragment' and 'no sentence was checked' cannot be treated as equivalent"*, and, decisively, *"the decisive support for a conclusion may be in an excluded fragment even when surrounding facts remain represented. P01 explicitly leaves the mathematical and probabilistic support around sentence 6 unexecuted"* (`L66_AUDIT.md`:63–67). A count of fragments is insensitive to whether the fragment was load-bearing, which is the only thing a gauge here is for.

And the threshold as a test fails the skill's rule for tests: run it on the thing it is meant to catch and on that thing's nearest innocent neighbour. It fires on both — 18 of 18, ten from every sentence, P09 at 11 of 11 with 26 said lines (L66:38). A test that fires on everything is measuring something else.

**What gauge would do the job.** Three candidates, in order of how much is already in hand. The first two need no new instrument.

- **Sentences with no said line at all.** The worker's table already has the column: P04, P06 and P18 have `Said = 0` (`Gauge_OpenAI_Codex.md`). Three of eighteen. This fires exactly where the checker had nothing of the writer's to work on and stays quiet on P09, which the bin gauge condemns. It discriminates, and it names a job swallowed: no commitment of the writer entered the ledger.
- **Filled-in lines against said lines**, and the count of findings leaning on filled-in lines. L64 already names this gauge twice (:128, :155) and did not draw its threshold on it. On the worker's table it fires on P04, P05, P06, P08, P10, P16, P18 — seven of eighteen. A finding that leans on a line the writer did not write is already flagged in the report (`run_check.py`:113, 154, 199, 213, 325), so the count is free.
- **The gauge that actually matches the words "swallowing a job": per sentence, whether what went to the bin was load-bearing for a finding the contract promises.** Concretely: does the bin entry hold a connective (BECAUSE, SINCE, SO THAT, ALWAYS, USUALLY, NOT) or the sentence's main predicate, as against a fragment of an excluded kind (amount, time, place, modality, manner, figure)? Only the first kind can take a promised finding with it. This needs one new field on each bin entry and nothing else, and Astra Pro's P01 sentence 6 is the case that would validate it. Pair it with Lesson L2's owed fix (list the kinds of claim the ledger had none of) and the two together answer "which questions were never asked", which is what a gauge here is for.

The hostile test L64:171 owes would then have something to bite on. As things stand it cannot be run: see question f.

---

## 7. Does the four-sources table decide the layer? (question e)

The closing sentence says it does not: *"**Which layer failed** is never read off a failed run ... It is a fresh choice"* (:147). But the table's "Error that is not" cells do constrain, so the sentence understates the document. Poking each forced finding against the table:

| Finding | Does a cell name it? | Layer |
|---|---|---|
| 1. Reported BECAUSE/SINCE never tested | **No cell names it.** The scope row's nearest is *"a change excluded without being written here"* (:142) — but no *change* was excluded; a *query* was. The translator row's cells do not bite: 39 was followed exactly (L72:31, :70). The checker row names *"a clash that passes"*, not a question never asked | **Unconstrained.** Two candidates (scope, checker) with nothing to choose between them. This is the finding that most needs a layer and gets none |
| 2. What-if HOLDS on an unestablished BECAUSE | **Yes**, exactly: *"a what-if that holds when the ledger cannot say (F09)"* (:144) | **Checker.** One layer, named. The table works here |
| 3. No sentence on JUMP and NO CONNECTION | **Yes**: *"Any finding a reader cannot trace to a sentence"* (:145) | **Read-back for the error, checker for the fix.** The table names where the failure shows; the change is one in `run_check.py`, which is the checker layer. The table has no way to say that, and :147's promise that *"the cost of a wrong choice shows at once through the other jobs of the layer changed"* assumes error-layer and change-layer are the same |
| 4. `consequences.py` pools worlds | **No cell names it**, and no row covers the tool. The checker row's provenance is *"constructed: built with cases in view, criticised, sixteen patches"* (:144) — that is the rig driver. `consequences.py` was written at L65, after the table | **Unconstrained.** The four sources came from the owner's four (Decisions L4). A new tool is a fifth thing, or silently the third; the table does not say |

So: the table is not "a fresh choice", and it is not a decision procedure either. It bites on two of four, half-bites on one, and has no cell for the finding the orchestrator calls the strongest (L72:48). The gap has a shape: every cell names an error in what a layer *produces*; none names an error of *omission* — a query not asked, a world not separated, a line not printed. Three of the four forced findings are omissions.

---

## 8. What would show this scope is wrong: has any of it happened? (question f)

| §8 item (line) | Happened? |
|---|---|
| *"A text of a kind in section 3 that the checker mishandles, and no patch fixes without breaking a job in section 4"* (:170) | **Half.** T10-D and T11-B are texts of the kind at :72, mishandled (L72:48). The second clause has not been reached: no patch was tried. And the clause cannot be discharged by any run — "no patch fixes it" can always be answered "the right patch has not been tried". As worded, item 1 cannot fire on a test; only on an exhausted search. Worth noting: the obvious patch (L72:60, ask BECAUSE and SINCE inside the world alone) has a cost 38 already names — *"A told world ... is looked at alone, so general lines from the actual ledger are not available inside it"* (38:149) — so inside-world BECAUSE checks would mostly return JUMP. That give-up is not yet logged anywhere |
| *"A gauge that reads under threshold on a text built to hide a contradiction in the bin. (A hostile test owed; none run.)"* (:171) | **No, and it now cannot.** The gauge reads *over* threshold on every text tried (18 of 18, L66:38). While that holds, no text can read under it, so this refuting condition is dead by the behaviour of the instrument it names. Still owed |
| *"A finding in section 4 that is never reached on any text the owner brings, over a season"* (:172) | **No.** One day has passed. The clock is long enough that nothing in hand can bear on it. I note that many §4 rows have been reached only on forcing cases built here, never on a text the owner brought |
| *"Consequences that a reader cannot use: the filter swallows the ones that would have caught the writer out"* (:173) | **Not as worded; yes in substance.** There is no filter (:154, "when it exists"). But a swallow happened by another mechanism: L71's first finding, *"Stated facts hide derived ones ... a consequences report is blind to a general line whose only work is to derive something the writer also asserts"* (L71:37), and Astra Pro's F, *"A zero single-line delta does not show a line does no work"* (L66:51). The condition named one mechanism and the swallow came by another, so the condition did not fire |
| *"Two ledgers of one text, by translators who have read no ledger, that differ in said-content on a text inside section 3"* (:174) | **Not as worded, and the test could not have fired.** L72 is this test. Its premise fails on both sides: Astra Ultra read six example ledgers (L72:57, *"the two 'independent' translators are not independent of the examples"*), and the other translator is the author of the contract. And the outcome is out of the condition's reach: by hand all 21 lines matched in content (L72:36); what differed was *standing* on 9 of 21, which the project's own instrument classes as *"same content, different standing"* (L72:29) — not said-content. Yet the difference that matters did occur: the checker's report differs on two of eight texts (L72:40). The condition is worded to a quantity that misses it |

**The answer to (f): none of the five has fired. Two of the five cannot fire (items 1 and 2). Two nearly fired and were worded to the wrong mechanism (items 4 and 5). One has no clock yet (item 3). Meanwhile four findings the orchestrator judges refuting (L75) passed straight through the list.** A "what would show this is wrong" list that misses every actual failure is the clearest sign in this review that the contract is easy to vary: it was written to be refutable and is not refutable by anything that has happened.

---

## 9. What would make it harder to vary

Two changes, in order.

1. **Say, in section 4, which promised findings apply inside a told world and inside a named case.** One column. It would have made finding 1 either a refutation or a written exclusion on the day L64 was accepted, instead of a thing that can be argued either way now. It would also settle the layer question in (e): a written exclusion makes it scope, an unwritten one makes it checker.
2. **Replace the bin threshold with a gauge of jobs swallowed** (section 6 above), and re-run it on the eighteen L66 passages before setting any number. If the new gauge also fires on all eighteen, the contract has learned something real about lyrical prose; if it fires on three or seven, the instrument was the fault, as both outside agents said.

A third, cheap: put the owner's words beside each *given* job, as Lesson L3 already requires.

---

## 10. Lessons

- I took log L75's finding 3 at its word ("the driver prints the sentence number only in what-if and plan headings") and began writing it up as read. Reading `run_check.py` showed `describe_lines`:47 prints the sentence for every line it lists, in seven branches. The real gap is narrower and better located: the two claim heads (:99, :145) and the two branches that list no lines (JUMP, NO CONNECTION). Fix for me: read the code before repeating a finding stated about code, even when three documents agree on it.

---

## Parts that never met a hard case

- The length limit (#2) and the length note (#20): nothing tried has reached the stated length.
- The closure clause on the admitted changes (#5): five of the six changes have never been run in the consequences mode (L65:28, L71:42).
- The grain rule (#6, #7): no test has turned on it; F15 is where it would first bite.
- §8's items 2 and 3: no hostile text, no season.
- The whole of section 9 (left to the owner): untouched since acceptance.

## Findings that fit no part of L64

- **Thing lines.** L72:52: *"The count of lines said, which the gauge and L64's thresholds use, moves by a factor of two on this convention alone."* L64 has no part that governs the unit its own gauges count.
- **The report's wording.** L72:50 (supposition wording for a told-world contradiction) and L66:47 / Lesson L2 (NO FAULT FOUND cannot distinguish answered from unaskable). L64's change list admits no change to wording, so no part of it can be right or wrong about this.
- **Tools that are not the rig.** `consequences.py` and `sameness.py` have no layer in section 6 and no row in sections 3 or 4.
- **The orchestrator as a translator.** L72:53, the dropped sentence 3 of T10-B. Section 6's translator row describes a language model given 39; it does not describe the orchestrator translating by hand, which is where half the L72 comparison came from.

## What I did not look at

The rig-2 driver and its patches; `checker_rules.pl`; the raw s(CASP) logs and the stored report files (I read summaries and program source, ran nothing); the eighteen L66 translations and the L72 translations line by line; file 11's Parts I, III, V, VI, IX, XV, which I took from L75's summary; `L63` beyond the diff; the Semantics project; the historical logs 01 to 58 beyond what the Decisions files carry. I did not test whether the owner agrees with any reading of their words.

## One next step

Before anything is changed in 38, 39 or the rigs: add one column to section 4 of the next scope version saying, for each promised finding, whether it is asked inside a told world and inside a named case. That single column decides finding 1's layer, decides whether L72 refuted the contract or found an unwritten exclusion, and is the cheapest thing on this list.

## What would change my mind

- **On section 2:** the owner saying that "meaning preservation is as essential as the contract says it is" was meant as an endorsement of a contract they had read closely, not a deferral. Then row :46 is given after all, and (ii) falls.
- **On the swap result (section 4, last):** a showing that sections 3, 4 and 5 were *re-derived* under the corrected job and came out identical, rather than left untouched. L64:3 says they were not; a note in the record saying they were re-checked would change the reading.
- **On the threshold (question d):** a run of the proposed gauge on a text built to hide a contradiction in the bin. If the gauge caught it, "fires on everything" would be the right behaviour for this corpus rather than a defect of the instrument.
- **On question e:** a line in section 6 saying that errors of omission belong to the scope layer by default. That would give findings 1 and 4 a layer, and the table would then decide three of four.
- **On question f:** the owner reading §8 item 5 as covering standing differences. Then L72 fired it, and the contract has been refuted by its own list once.
