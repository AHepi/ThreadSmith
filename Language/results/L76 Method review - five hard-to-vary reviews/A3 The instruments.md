# A3 — The measuring instruments, tested as instruments

Reviewer A3. Skill applied: `hard-to-vary` (SKILL.md, `building.md`, `testing-against-cases.md`, `reporting.md`).
How I know each thing is tagged **read** (a file and line), **seen** (a printed output I produced or that is in the repository), **worked out**, **assumed**.
All runs of mine were made on a scratch copy at `scratchpad/method_review/scratch/`. Nothing in `/home/user/ThreadSmith` was written or modified.

---

## 1. The question, frozen

**What is being explained.** The Language project claims that five instruments give readings of five named things: how much two ledgers of one text say in common; what follows from a ledger and what changes under an admitted change; how much of a text went unchecked; whether a report can be read back to the sentences it is about; whether a fault planted in prose is caught.

**Over what range.** The runs on record: L62, L65, L66/L69, L71, L72/L73, L74. Rig 1 patched, `checker_rules.pl` as frozen, s(CASP) 1.1.4, SWI-Prolog 9.0.4.

**What is asked.** Two kinds of question, kept apart:
- *Does it achieve its purpose?* — does each instrument's reading move with the thing its plan names?
- *What can we tell from what we see?* — given a reading, which of the four layers of L64 section 6 (scope, translator, checker, read-back) does it bear on?

**Frozen for this report.** I do not ask whether the language is right, whether a translation is right, or whether the checker's findings are true. I ask only what the instruments measure.

**Something to explain, not a non-event.** The contrast is real: L72 read 4 of my 21 lines as shared where the hand read 21 (**read**, `Language/results/L72 Test results - two translators on the eight texts of plan 37.md` line 36); L66 read every one of eighteen passages over the scope threshold (**read**, `Language/results/L66 Test results - the blind run on a lyrical and a contested corpus.md` line 38). Those are readings that parted from the thing read, and they are what is to be explained.

---

## 2. The jobs, and where each came from

Marked **given** (the owner named it), **fixed** (the owner made it a requirement not up for test), **added** (Claude's, or mine).

| # | Job | Tag | Where |
|---|---|---|---|
| J1 | Two translators who have read no ledger, on unseen text, produce the same said-content, differences only in marked readings, standing set aside — **by the sameness test** | added (the instrument); serves the **given** job "meaning preserved" | L64 line 143 for the success condition; L64 line 46 for the given job; L64 line 50 lists "the sameness test" as added |
| J2 | Two ledgers of one text by translators who read no ledger, differing in said-content, would show the scope wrong | added | L64 line 174 |
| J3 | What follows from the writer's commitments | given | L64 line 17 (query 2), decision L4 |
| J4 | And what would follow under **each** admitted change — six are named | given | L64 lines 19–25 |
| J5 | Anyone can see the language leaning on the leftovers; the bin's gauge is bin entries per sentence; every gauge appears in every report | added (threshold "proposed for the owner", never struck) | L64 lines 5, 120, 159; file 38 line 113 |
| J6 | A reader given the report alone names the finding **and** points at the sentence; and a NO FAULT FOUND that does not say which questions were never asked is an unacceptable error | given (the fourth error source, decision L4) | L64 line 145 |
| J7 | The checker reports a fault on the planted sentence of a planted passage and stays silent on the unplanted ones | added (structure was Claude's; owner approved the proposal, decision L8) | `Language/tests/L66 Test plan ...` line 16 |

**Held-if warning, stated up front.** J1, J2, J5 and J7 are added jobs. Parts held only by them are *held if* those jobs are real. J5's threshold is Claude's own number and L64 line 120 says so.

---

## 3. Instrument by instrument

### 3.1 `Language/tools/sameness.py`

**Job given.** J1 and J2. It is the sole named arbiter of one of L64's five conditions that would show the scope wrong (**read**, L64 line 174).

**What the code measures** (**read**, `sameness.py`). For each line: strip a leading `[CLAIMED|GIVEN|SUPPOSED|TOLD ...]` bracket, or else take `info["standing"]` (lines 18, 26–27); lowercase the rest, replace every non-alphanumeric run with a space, delete thirteen words — *the, a, an, is, are, was, were, of, to, its, it, that, this* — and rejoin (lines 33–37). Two lines are "both say" when those strings are **equal** (line 51). Otherwise the best remaining partner by Jaccard on the token **sets** (lines 39–41) is printed as "near" if it scores at least 0.5 (line 45).

So: exact match is order-sensitive, the near score is order-blind, and no token carries more weight than any other.

| Part (its own words) | Mark | Provenance | Why |
|---|---|---|---|
| S1 "It compares the wording of lines, not their meaning" (lines 10–12, 64) | **held if** — held only by a hand step that L64 line 174 does not require | built | The disclaimer did its job inside L72 (results line 69 warns against reading the four matches as the result), but L64 line 174 still makes the program the arbiter of a refutation condition with no hand step written into it |
| S2 the standing stripper (lines 18, 26–27) | **held** by the poke below | built | Changing only the standing moved the line into "same content, different standing" and left "both say" whole (**seen**, my run) |
| S3 `norm`, the thirteen-word list (lines 33–37) | **loose** — a near neighbour that weights a polarity token would do as well or better; the project has already proposed one (Lesson L8) | asserted | Nothing in the record gives a reason for these thirteen words |
| S4 exact match = normalised string equality (line 51) | **loose** — comparing token multisets is the near neighbour and gives up nothing the tool claims | built, never tested on a reordering | **Seen** (my run): "the door is open" against "open is the door" scores 1.00 on the near test and is **not** in "both say"; it is printed in *both* "only" buckets and again as a near pair |
| S5 the near score, threshold 0.5 (lines 39–41, 45) | **loose** | asserted | I grepped the whole `Language/` tree for a reason for 0.5 and found none; the only mentions are after the fact, in L72 results lines 43 and 51 |
| S6 the "only" and "near" buckets, "for the reader to judge by hand" | **loose** (a catch-all whose only gauge covers one of its three buckets — see below) | built | See the catch-all paragraph |

**Where the job and the reading part, with a case.** L72, `results/L72 Test results ...` line 36: the program found 4 "both" in 21 and three texts with no match at all; the hand found all 21 matched. Line 29 names the cause: "The reason is form, not content" — Astra Ultra wrote "folding: ada folded note; direction not stated" where the earlier ledger wrote "Ada folded the note". **Seen** by me on the repository's own output, `results/L72 Reruns by the orchestrator/sameness/sameness_T05B.txt` lines 6–15: five lines on one side, two on the other, nothing shared, and the pair "Ada folded the note" / "folding: ada folded note; direction not stated" split across the two "only" buckets.

The instrument's reading therefore moves with the ledger's **line-writing convention**, which is the thing J1 says should be set aside, and not with said-content, which is the thing J1 says should be read.

One correction to how L72 explains this. L72 results line 26 says "File 38 allows them and does not say whether every named thing needs one". File 38 rule 3 does say: "Every thing in a happening has a thing line" (**read**, `authority/38 ...` line 119). "Ada folded the note" is a happening with two things in it. The 20 September ledgers have no thing line for either (**seen**, the sameness output above). So on T05-B the departure from 38 is on the earlier side, not on Astra Ultra's, and part of the 4-of-21 reading is a breach of rule 3 rather than an open convention.

**Catch-all and gauge.** The "near" and the two "only" buckets are the catch-all: everything the exact test misses goes there and is absorbed by a reader. The only gauge on it is L72's E8, "at most three near pairs across the eight need a hand decision" (**read**, `tests/L72 Test plan ...` line 18). **Seen** (L72 results line 43): E8 read two — under its line — while 17 of 21 lines sat in the "only" buckets and were resolved by hand. The gauge reads green while the catch-all swallows the job. That is the error L64 line 142 names as unacceptable for the scope layer, in L64's own words: "A gauge that stays green while the bin, 'cannot tell' or 'not checked' absorbs a job".

There is a second reason the counts cannot be read as a gauge at all. The near loop (lines 58–61) neither removes its A line from `only_a` nor consumes its B partner from `only_b`. **Seen** (my run): three A lines, two B lines, printed as 3 only-first, 2 only-second **and** 3 near pairs, with one B line named as the near partner of two different A lines. The buckets overlap and "near" is not a pairing.

**Swap test.** Nearest instrument that does J1 better: compare the two ledgers' **answers** rather than their words — run the driver and `consequences.py` on both and compare the report kinds and the derived-fact sets. This is licensed by L64's own grain rule (line 28: "Two commitments the contract's changes cannot separate are one commitment at this grain"). *What is given up:* it cannot tell "the same commitment in other words" from "two different commitments that happen to entail the same under this rule set"; it loses per-line pairing, so the hand can no longer check the tool line by line (the very thing L72 results line 69 says is the result); and it goes blind on any content the checker has no query for. The project already has half of this instrument and did not use it for J1.

**Poke.**
- *Should move the reading:* replace a line by its exact denial. **Seen** (my run): the pair leaves "both say" — the reading moves. Good. But it lands in "near" at 0.67, above the threshold, because NOT is one token in a union of three.
- *Should not move the reading:* change only the standing. **Seen** (my run): "both say" unchanged, the difference reported separately. Good.
- *The pair that settles it:* on the repository's own T07-D output (`sameness/sameness_T07D.txt` lines 17–20) the near test pairs "the same door at the same moment is NOT open" with "door is open at stage described_moment" at 0.50. I computed the alternative (**seen**): the true counterpart, "NOT [door is open at stage described_moment], in the same context and respect as line open", scores 0.4286 and therefore falls **below** the threshold and is never printed. The instrument did not merely tolerate a negation; it ranked the negation above the true match and hid the true match.

---

### 3.2 `Language/tools/consequences.py`

**Job given.** J3 and J4 (**read**, L64 line 17 and lines 19–25).

**What the code measures** (**read**, `consequences.py`). It loads `run_check.py` as a module and calls `run_query` directly (lines 20–22, 41). It asks ten fixed queries with a variable (lines 16–18), keeps every binding, subtracts the set `stated_facts` — clause heads whose **entire body** is `line(N)` (lines 24–29) — and prints the remainder as "derived (not stated by any line)" (lines 58–59). Then it removes one `line(N)` at a time and prints the difference (lines 64–72).

| Part | Mark | Provenance | Why |
|---|---|---|---|
| C1 "Uses the rig-1 driver's own `run_query` (same rules, flags, time limit)" (lines 4–5) | **loose** — the near neighbour is "reuse the driver's check-time state, not only its query function", and it does the job | fitted (to ledger A, which has no worlds) | The claim names three switches. There is a fourth: `WORLD_REMOVED`, set by `check()` at `run_check.py` line 69 and used at line 16. `consequences.py` never calls `check()`, so the list stays empty. Lesson L7 |
| C2 the ten queries (lines 16–18) | **unknown** — no run bears on whether these are the right ten; adding `claim_because`, `claim_since`, `claim_plan`, `exempt`, `exception_reason` and re-running would settle it | asserted | See the flip test below on L71's E5 |
| C3 `stated_facts` (lines 24–29) | **loose** — the near neighbour is already free: `answers[i]["lines"]` from the driver already gives the lines used, so "used exactly one line" is one comparison away | fitted, and patched once already (Lesson L4) | **Seen**, my run on ledger A: `depends(dies(balcony_plants),reached(the_cold,balcony_plants))` is printed as derived, though `ledger_A.pl` line 11 states it for every tomato plant. Its body is `line(5), kind(P, tomato_plant)`, two goals, so the regex misses it. The same for `changes(move(thermometer),reading(thermometer))` from line k1. Six of the ten "derived" facts on ledger A are of this kind |
| C4 derived = found − stated (line 58) | **loose** for J3 — the near neighbour is to print every found fact with an "also stated by line N" flag instead of subtracting | built | See the poke below. It measures what follows **and was not also written down** |
| C5 one line removed at a time (lines 64–72) | **held if** — held only by the assumption that a fact has one route; Astra Pro finding F and L71 finding 1 both show it false | built | L66 results line 51 records joint removal as "not built" |
| C6 "Nothing is written to the ledger or the rig" (line 10) | **held** | built | True as read; the tool only reads and shells out |

**Where the job and the reading part, with cases.**

1. *Worlds.* **Seen**, my run on `ledger_T07B.pl`: `consequences.py` prints "1 derived ... `contradiction(open(door))` <- lines 2, 3", where line 2 is `[TOLD, in Nora's story] the door is open` and line 3 is `[CLAIMED] in the room the door is NOT open`. The driver on the same ledger prints "NO FAULT FOUND" and "INSIDE 'Nora's story' (a told world, looked at alone): no contradiction." Two instruments, one ledger, opposite readings. Recorded at L72 results line 49 and Lesson L7.

2. *Six admitted changes, one implemented.* L64 lines 19–25 name six. `consequences.py` implements one (take out a line), and not even the "or a group of lines" half. L65 said so openly (plan line 13). But L66's E4 then asked the instrument for a divergence "under the change withdraw the group-structure line" (**read**, `tests/L66 Test plan ...` line 28), and L66 results line 36 records what happened: "taking out the group-structure line of P14 removes only itself ... the what-if MAKE NOT SO on the same line **does** set the spread aside". The plan asked an instrument for a change it does not make, and the sound answer came from a different instrument.

3. *One relation in two notations.* Astra Pro finding E, L66 results line 50: P10's derived fact restates line g as `depends_on` beside `depends`. `checker_rules.pl` line 22 derives one from the other; `stated_facts` subtracts only the written form.

**Catch-all and gauge.** The "derived" list **is** the catch-all: anything found and not recognised as stated goes in it. Its gauge is named in L64 line 159 — "The consequence filter, when it exists: derived lines shown against derived lines total" — and it does not exist. L65 results line 22 found the need and stopped: "A consequences report should show the first kind and keep the second behind it. **Worked out** from the list; not a rule yet." So: a catch-all, with its gauge named in the contract, unbuilt, and used in three tests since.

**Swap test.** The nearest instrument that does J3/J4 better is the driver's own what-if machinery (`run_check.py` lines 282–298): it sets the world list, sets aside results the ledger ties to the change, and prints a verdict. L66 results line 36 shows it gave the reading `consequences.py` could not. *What is given up:* the what-if only answers a question someone wrote into the ledger's `whatifs` list; it never says "here is what follows that nobody asked about", which is J3's whole point. The two are complements. The finding is that the project runs the faulty one as the instrument of record and treats the sound one as a side branch.

**Poke.**
- *Should move the reading:* remove the ALWAYS line. **Seen**, L65 results line 11: removing line 5 changes eight facts. It moves.
- *Should not move the reading:* have the writer **state outright** a fact the ledger already derives. What follows is unchanged; only what was written changes. **Seen**, my run: I added `holds(dies(door_plant)) :- line(13).` to ledger A. Derived fell from ten to nine, and the fact that vanished is exactly the one L65 plan line 23 called "the one deduction here a reader would want and the fault mode does not print". The contradiction's attribution also changed, from "lines 2, 5, 7, 9" to "lines 13, 9".

That second poke is the decisive one. By the skill's own rule — "A part that moves when you change only how it is read or reported is a measurement of the thing, and answers *what can we tell*. The thing that produces the outcome stays put under that change" — `consequences.py` measures the reporting, not the entailment. It answers "what follows that no single line happens to state", which is narrower than J3 and is not the question L64 line 17 asks. L71 finding 1 (results line 37) found the same thing from the other end and filed it as "a limit of the mode to put in the read-back brief, not a rule change".

---

### 3.3 The driver's printed report and its GAUGE (`run_check.py`)

**Job given.** J5. Also file 38 line 113: "Every report also carries: a note wherever a finding leans on a line the writer did not write; the count of lines said, filled in and usual case; **the verbs with no shape**; and the bin."

**What the code measures** (**read**, `run_check.py` lines 330–333). `len(meta["leftover"])` over `len(meta["sentences"])`, printed as "N of M sentences went to the leftover bin (not checked)". `leftover` is a list of free-text strings (**seen**, `ledger_P01.json`: nine strings, two of them about sentence 10). The numerator counts **entries**; the denominator counts **sentences**. They are not the same unit.

| Part | Mark | Provenance | Why |
|---|---|---|---|
| G1 the marks count, said / filled in / usual case (line 331) | **held** by J5 | built | It counts what it names |
| G2 the bin ratio and its wording (lines 331–333) | **loose** — the near neighbour is one line: `len({e["sentence"] for e in meta["bin_entries"]})`, and the field already exists in every ledger | asserted (L64 line 120 states the gauge; the code prints a different quantity) | See the two pokes |
| G3 the threshold, "more than a third" (L64 line 120) | **loose** | asserted | **Read**, L66 results line 38: every one of eighteen passages is over it, ten of them at every sentence. A line that every case measured falls on is not a line |
| G4 the NO FAULT FOUND header (lines 334–335) | **loose** — the near neighbour is a flag set where each finding is appended | built, fitted to the keyword list it was written against | The header is a keyword scan over the report's own prose. "FAILS" and "CANNOT TELL" are not in the list. **Seen**, `L69 Return .../evidence/rig1/P13_OpenAI_Codex.report.txt` lines 3 and 7: "NO FAULT FOUND in the lines that were checked." followed by "Your what-if FAILS." P16 does the same with CANNOT TELL |
| G5 the other two gauges L64 line 159 requires in every report | **idle** — they are absent | asserted | **Read**, grep of `run_check.py` for "shape" and "cannot tell": the only hit is the CANNOT TELL finding text at line 206. No unshaped-verb count, no cannot-tell count. Rig 2's `check2.py` line 136 does print "Verbs with no shape". So neither rig prints all three, and the two rigs print different gauges |

**Where the job and the reading part, with cases.**

1. *A whole sentence lost and the gauge reads zero.* **Seen**, my run of the unmodified driver on the repository's own `ledger_T10B.pl`:

   `GAUGE: 3 lines said, 0 filled in, 0 usual case; 0 of 3 sentences went to the leftover bin (not checked).`

   `ledger_T10B.json` has three sentences and no line and no bin entry for sentence 3, "The account gives no reason for its dryness" (**seen**). L72 results line 53 records the lapse; what I add is that the gauge, the one instrument whose job is to show what went unchecked, read zero on it.

2. *The numerator can exceed the denominator.* **Seen**, my run on a scratch copy of `ledger_T05B` with four bin entries: `GAUGE: ... 4 of 3 sentences went to the leftover bin`. A ratio that can exceed one is not a proportion, and L64 line 120's threshold is stated as a proportion.

3. *The gauge and the sentence anchor are both the translator's word.* `meta["lines"][l]["sentence"]` and `meta["leftover"]` are written by the translator and checked by nothing. The driver reprints them.

**Catch-all and gauge.** The bin is the one catch-all L64 names (line 134) and it does have a gauge — this one — so the form of the rule is met. The substance is not: the gauge cannot show the catch-all swallowing a job, because the one case on record where the catch-all swallowed a whole sentence read zero.

**Swap test.** Nearest better instrument: print two numbers — distinct sentences with at least one bin entry (already in `bin_entries[].sentence`; Astra Ultra computed it by hand in `L69 Return .../Gauge_OpenAI_Codex.md` line 30), and sentences with **no** line at all. *What is given up:* both still rest on the translator's own `sentence` fields, so a sentence mis-numbered rather than dropped still reads clean; and the second number will fire on sentences the language openly excludes, so it needs its own threshold. It is a few lines of code and it would have caught T10-B.

**Poke.**
- *Should move the reading:* a sentence wholly untranslated. **Seen**: it does not. T10-B reads 0 of 3.
- *Should not move the reading:* split one bin entry into two halves with the same words about the same sentence. **Seen**, my run on a scratch copy of `ledger_T05B`: 1 of 3 became 2 of 3 — from under L64's third to double it, with no change to what was binned.

Both halves of the pair fail. This is the clearest instrument failure in the set, and it is the instrument on which the whole scope contract's one quantitative limit rests.

---

### 3.4 The read-back test (L66 Reader brief; E7 of the L66 plan)

**Job given.** J6, both halves (**read**, L64 line 145).

**What it measures.** The brief gives the reader the printed reports and forbids everything else: "not the passages, not the ledgers the checker read, not the rules" (**read**, `tests/L66 Reader brief ...` line 3). It asks four things; the sentence trace is item 2 (line 7). E7 puts numbers on the trace only (**read**, `tests/L66 Test plan ...` line 31).

| Part | Mark | Provenance | Why |
|---|---|---|---|
| R1 the reader sees reports only (brief line 3) | **held, jointly with** R3, for the job "names the finding" | built | It is what stops the reader reconstructing the finding from the prose. The reader named all seven findings correctly (L66 results line 39) |
| R2 the sentence trace (brief line 7) | **loose** — the near neighbour is to split the test: the reader says what the report lets it say, and the orchestrator checks the printed number against the ledger and the ledger against the text | asserted (L64 line 165 lists "the exact read-back" as asserted) | The reader cannot check the number. Seen at work: Astra Pro, `ANSWERS_ChatGPT.md` under P13, "The what-if **f** is explicitly attached to **sentence 2**" — accepted as printed, as the design requires |
| R3 "guess at nothing ... say so rather than fill it in" (brief line 10) | **held** by the run | built | The reader refused seven times and said what one added sentence would settle each (L66 results line 39) |
| R4 E7's expectations | **unknown** for the second half of J6 | asserted | E7 sets a number for contradictions, jumps and consequences, and none for "a NO FAULT FOUND that does not say which questions were never asked". What would settle it: an expectation requiring the reader to name, for every clean report, the kinds of claim the ledger had none of — the fix Lesson L2 already wrote down |

**Where the job and the reading part, with a case.** The reading of E7 in the results is wrong in its diagnosis, and the error matters because the proposed remedy is sized from it.

L66 results line 39 says the four what-if and plan findings were traced "because the driver prints '[..., sentence 8 line j]' in those headings and nowhere else". Two corrections, both **seen** in the code and the data:

- The driver prints **no** sentence in a what-if heading. `run_check.py` line 296 is `'WHAT-IF [%s]: "%s"' % (w.get("whose", "?"), w["text"])`. The string "OpenAI Codex, L66, sentence 2 line f" is the value of `whose` in `ledger_P13.json` (**seen**) — the **translator** wrote the anchor into a free-text field meant for who asked the what-if. P16's `whatifs` list is empty (**seen**); its trace came from a bin entry that quotes the sentence.
- "and nowhere else" is false. `describe_lines` (line 47) prints `[mark, sentence N]` for every line it lists. **Seen**, my run of the driver on `ledger_A.pl`: the contradiction block, the BECAUSE-follows block and the plan block all print "sentence 3", "sentence 2", "sentence 1".

The true shape is narrower and different: the JUMP branch (lines 126–138) and the NO CONNECTION branch (lines 156–162) never call `describe_lines`, and neither do the head lines of BECAUSE, SINCE, PLAN and DENIED BECAUSE. On L66's corpus every finding but the what-ifs and P16's plan head was a JUMP or a NO CONNECTION, so the gap looked total. The proposed fix, "one line in the driver" (L66 results line 68, L75 finding 3), is under-sized: those two branches have no line list to describe, so the fix is to build one for each, plus a sentence on each head line.

So the read-back test measured that a number was **present**, not that it was **right**; and the instrument, by its own design (brief line 3), cannot measure the second. That is the half of J6 that matters, because the numbers it validates are the translator's unchecked assertion (see 3.3, case 3).

**Catch-all and gauge.** Brief item 4, "What you could not make out", is the catch-all: anything the reader cannot do goes there. It has no gauge, and in this run it swallowed the trace job seven times while E7's other rows read as predicted. That said, the reader's use of it is the most informative part of the whole package (L66 results lines 44–53), which is the sign of a catch-all doing a job that ought to have a part of its own.

**Swap test.** Nearest better instrument: two tests where there is now one. (a) *Report legibility*: reader, reports only, as now. (b) *Anchor correctness*: the orchestrator checks every printed sentence number against the ledger, and every ledger `sentence` field against the text. *What is given up:* (b) is not blind and is not cheap — it is a line-by-line read of the corpus — and it tests the translator and the driver, not the reader, so it cannot be marked on E7's scale. In exchange it is the only test in the set that could have caught T10-B.

**Poke.**
- *Should move the reading:* remove the sentence number from a finding. **Seen** across the corpus: seven findings with no number, traced with confidence on none (L66 results line 39).
- *Should not move the reading:* change a printed sentence number to a wrong one, leaving the finding alone. **Worked out** from brief line 3: the reader has no passage and no ledger, so a wrong number reads exactly as a right one. The reading does not move. It should.

---

### 3.5 The blind-plant method (L66)

**Job given.** J7: "Does the checker, on the worker's translation, report a fault on the planted sentence of a planted passage, and stay silent on the unplanted ones?" (**read**, `tests/L66 Test plan ...` line 16.)

**What it measures.** Six of twelve lyrical passages carry one sentence altered by a program, seed 45, "each alteration a negation or a reversed connective" (plan line 7). The reading is taken at the end of a two-stage pipeline — a model translates, then the driver runs — over six passages that differ from the twelve unaltered ones in author, length and argument form. There is no unaltered twin of any planted passage.

| Part | Mark | Provenance | Why |
|---|---|---|---|
| P1 the six program alterations (plan line 7) | **held if** — held only by J7, and J7 names no control | built | The alteration enters the prose; the reading is taken after the translator. Four of six never became lines (L66 results line 76: "the checker had nothing to check") |
| P2 the criterion "a fault on the planted sentence" | **loose** — it had no fixed meaning before the run | asserted | E1 named the kinds it expected: "a NO CONNECTION or JUMP in a SINCE chain" (plan line 25). The one hit was neither: P13's report reads "NO FAULT FOUND in the lines that were checked" and then "Your what-if FAILS" (**seen**, `P13_OpenAI_Codex.report.txt` lines 3, 7). What counts as a hit was settled after the run |
| P3 E1's band — 2 expected, "against" at 0 or at 5–6 | **loose** | asserted | A band that passes on anything from 1 to 4 out of 6 |
| P4 the flip pairs, P01/P07 and P11/P14 (plan line 7) | **held** by the run | built | Matched pairs of one text differing in one sentence. **Read**, L66 results line 37: "P01/P07 differ on the sentence-9 lines only ... everything else identical to the letter" |
| P5 a per-plant record of whether the altered clause became a line | **idle, because absent** — the reading exists in the worker's notes and is not part of the instrument | — | L66 results line 33 quotes four refusals to repair; none of them is a reading the test takes |

**Where the job and the reading part, with cases.**

1. *The instrument cannot separate two causes of silence.* On four of six plants the alteration never reached the checker. The instrument's reading is the same whether the checker is blind or the plant never arrived. L66 results line 59 concedes it: "The blind test as designed measures the translator more than the checker." The reading that would separate them — did the altered clause become a line? — sits in the return and is not taken.

2. *A finding on an unplanted sentence of a planted passage has no home.* **Seen**, `P09_OpenAI_Codex.report.txt` lines 3–7: two JUMPs, on lines p and q. **Seen**, `ledger_P09.json`: both are sentence 6. The plant is at sentence 4. So P09 produced exactly the finding kind E1 named, twice, in the wrong place. E1 counts by passage, and E2's false alarms are counted only over unplanted **passages**, so this outcome — the most common one — is scored by neither. The results file handled it in prose (line 33) and the expectations could not.

**Catch-all and gauge.** E1's two-sided band is the catch-all: the method survives every outcome between 1 and 4, and no reading distinguishes a checker hit from a translator catch. There is no gauge on it.

**Swap test.** The better instrument is already in the same corpus: the flip design. One text, two versions differing in one sentence, both translated by one worker, both run, the two ledgers and the two reports compared. *What is given up:* twice the translations; and the worker may spot the near-identical pair — L69 records that Astra Ultra did find the two pairs blind, which is a leak the plant design does not have. Against that, it is the only design in the run that separates the alteration from everything else, and it did.

**Poke.**
- *Should move the reading:* a plant that does produce the stated opposite of something already in the ledger. **Worked out** from L66 results line 33: P15's plant became a line, "ALWAYS SHOWS: a great person is NOT misunderstood", and raised nothing only because no one in the passage is called great. The reader named the one missing premise without seeing the passage (results line 53). So the instrument would move — but only on a plant chosen to have its instance present, which the program that made the plants does not check.
- *Should not move the reading:* re-shuffle the P-numbers, or change which unaltered passages sit in the corpus beside the planted ones. **Worked out**: the reading is a count over six passages taken one at a time, so it does not move. That is the trouble — it also means nothing in the corpus around a planted passage constrains its reading, which is what a control would do.

---

## 4. Whole-explanation checks

**Flip.** Take the instruments one at a time and ask whether the opposite result would have been read differently.
- `consequences.py`: L71's E5 predicted that no SINCE step would appear in the derived list, with "A SINCE step visible in the derived list" as what would count against (**read**, `tests/L71 Test plan ...` line 14). The queries list (lines 16–18) contains no `claim_since`, so the prediction follows from the code the same hand wrote. E5 was marked **met** (L71 results line 31). An expectation that can only fail if the instrument does more than it can was never a test of the instrument. This is the skill's "passing your own test", with all three layers — the thing, the rig and the inputs — in one hand.
- The gauge: the threshold fires on every one of L66's eighteen passages (**read**, L66 results line 38) and on three of L72's eight texts — T05-D 2 of 2, T07-D 1 of 1, T11-B 1 of 2 (**seen**, the ledgers' `leftover` and `sentences`). Neither reading was taken as a scope verdict: L66's was recorded as "against on its face ... with the instrument in question", and L72 never mentions the threshold. No outcome of the gauge would have been read as the gauge working.

**Reverse — poke the cause, then poke the effect.** Done per instrument in section 3. The one that reverses cleanly is `consequences.py`'s C4: poke the ledger's entailments (remove the ALWAYS line) and the reading moves; poke only the writing-down (assert a fact already entailed) and the reading also moves. A measurement of entailment should be still under the second poke. It is not (**seen**, my two runs on ledger A).

**The answer hidden in the starting points.** Three instruments take the translator's own metadata as their measurand and re-read it as a measurement of something else: the gauge reads `leftover` and `sentences`; the read-back reads `sentence` fields reprinted by the driver, and on the what-ifs reads a sentence number the translator wrote into the `whose` field; `sameness.py` reads line text written under a convention the translator chose. In each case the thing being measured supplies its own reading. That is why all three go quiet on T10-B.

**Where the jobs came from.** J1, J2, J5 and J7 are added — Claude's own. J3, J4 and J6 are given. Section 3 marks each part against its job; the parts held only by J1, J2, J5 or J7 are *held if*, and the report says so.

**Add a job.** One job that must also be so if these instruments measure what the plans say: *each instrument gives the same reading on a ledger that says the same thing in a different admissible form.* It survives on none of the three programs. **Seen**: sameness moves under a change of line form (L72 results line 29); the gauge moves under a split bin entry (my run); `consequences.py` moves under a fact restated (my run). The new job rules out the current version of all three and does not rule out the swaps proposed in section 3, so it did work.

**Look inside.** Matching the results is not matching the workings. On ledger A, `consequences.py` printed ten derived facts and L65 read the list as right (results line 9). Reading the mechanism instead: six of the ten are instantiations of two general lines whose clause bodies have two goals, which `stated_facts` cannot see. L65 results line 22 saw six as "the checker's bookkeeping" and proposed to hide them behind a line. Hiding them would have concealed the mechanism's fault behind a presentation rule.

**Pairs that pull.**
- *Blindness against checkability* (read-back). The more the reader is kept from, the more its "names the finding" answer is worth and the less its "points at the sentence" answer can be checked. The line is currently drawn at total blindness, and the second half of J6 is lost. What would show the line is wrong: a run in which a printed sentence number is deliberately wrong and the reader reports the finding as traced — which is what the design guarantees.
- *Cheap instrument against honest instrument* (gauge). `len(leftover)` is free; a coverage count needs a per-clause map nothing produces. The line is drawn at free, and the instrument reads 0 on a lost sentence.
- *One hand against a real test* (plants, and L71's E5). The corpus maker wrote the plants, the expectations and the plan (L66 plan line 13 says so). The flip pairs are the part of that corpus that survives the conflict, because a matched pair constrains the reading whoever wrote it.
- *Sameness's word test against the translator's freedom* (L64 line 156's "translator freedom against checker fixedness", seen from the other side). 38 rule 3 requires a thing line for every thing in a happening; 38 says nothing about the phrasing of a happening line. The wording test reads the unconstrained half.

**Check the patches.** Every patch so far has changed the thing measured, never the instrument. Lesson L4 patched `consequences.py`'s head regex and kept both runs; Lesson L7 and Lesson L8 are recorded as fixes owed, not made. What has never been patched is any expectation: E8's near-pair count, E1's band, E5's wording and E7's silence on the NO FAULT FOUND half all stand as written, and each of them read green or unmarked while the job it covers failed. The skill's rule for a patch — say what it gives up — has been kept for the rig (the "What each patch gave up" list in the project story is exemplary) and not kept for the instruments, because the instruments have not been patched.

**What the change list leaves out.** L64 lines 19–25 name six admitted changes. No instrument in this set makes changes 2 to 6 except the driver's what-if code, which is not counted as an instrument. So the change list under which the instruments are exercised has one item on it, and a list with one item cannot separate an instrument that tracks entailment from one that tracks a single removal.

**Rivals.** For each instrument the best rival is named in section 3's swap test, and in three of five the rival is already inside the project: the driver's what-if machinery (against `consequences.py`), the flip design (against the plants), and the variation test of L64 line 143 (against `sameness.py`). None was set beside its incumbent.

**Provenance.** Given beside each mark in section 3. In summary: the three parts that carry a threshold or a word list — `norm`'s thirteen words, the 0.5 near cut, the third of sentences — are all **asserted**, and I found no reason for any of the three anywhere in `Language/`. The parts that were **fitted** are `consequences.py`'s C1 and C3, both fitted to ledger A, and both of the two faults found since (Lesson L7 on a ledger with worlds, Astra Pro finding E on a ledger with two notations) are of the kind "a case it never met".

---

## 5. The whole-instrument question: language, translator, or instrument?

**No — not from any instrument's reading.** Every separation on record was made by a person or an agent reading a source file, and none by a reading moving.

The reason is structural and can be stated in one line: **every one of the five instruments takes the ledger as given.** `sameness.py` reads two ledgers. `consequences.py` reads a ledger. The gauge reads the ledger's `leftover` and `sentences`. The read-back reads a report built from a ledger. The plant test reads a report built from a ledger. Nothing in the set reads the text beside the ledger.

The flip test on the whole set: had the translator been wrong in a way that leaves the ledger self-consistent, every one of the five would have read exactly as it did. **Seen** on T10-B: a sentence dropped without a line or a bin entry; the gauge reads "0 of 3 ... (not checked)"; the report reads NO FAULT FOUND plus a CANNOT TELL; `consequences.py` reads whatever the three remaining lines give; the reader, had it been given that report, would have had nothing to notice. The lapse was found by a hand pairing of two ledgers (L72 results line 53), not by an instrument.

Four worked cases, each showing which reading actually did the separating:

| Case | What the instruments read | What separated the layers |
|---|---|---|
| T07-B | `consequences.py`: a contradiction. Driver: NO FAULT FOUND. (**seen**, my two runs) | Reading `consequences.py` for the missing world list — Astra Ultra read the program (L72 results line 49) |
| P14 | One report saying "JUMP" and "Your what-if HOLDS" from the same dependency (**seen**, `P14_correction1 ... report.txt`) | Astra Pro reading the report and noticing the two findings belong together (L66 results line 49). No instrument compares a report with itself |
| T10-D, T11-B | Reports with nothing to say: the BECAUSE and the SINCE sit in a told world and patch 12 asks a told world only for contradictions | Reading 39's attribution rule against `run_check.py` lines 311–320 (L72 results line 48). Every instrument was silent and correct to be |
| The six plants | One hit of six | The translator's own notes, refusing to repair four (L66 results line 33) |

So the instrument that does the separating in this project is **a fresh agent given the code and the reports and asked to read them**. On the record it works: Astra Pro's seven findings all checked out (L66 results lines 45–53), and Astra Ultra's four all checked out (L72 results line 54). It is a real instrument, it has produced more of the project's findings in the last week than the five named ones, and it appears in no plan, in no gauge, and nowhere in L64 section 5's table of catch-alls and their gauges.

**One consequence for the record's own sorting.** L75 sorts the recent findings into four that force a change and a remainder: "The rest are decisions or instruments, not refutations: the bin threshold and gauge (L66 E6), Thing lines (L72), the told-world wording (L72), the near score and NOT (Lesson L8), stated facts hiding derived ones (L71)." The line is drawn in the wrong place for at least the gauge. L75's own item (4) — `consequences.py` deriving a contradiction the checker refuses — is a tool giving a wrong reading, and it is counted as forcing a change. The gauge printing "0 of 3 sentences went to the leftover bin (not checked)" on a ledger with a sentence missing is a tool giving a wrong reading of the same kind (**seen**, my run), and it is counted as a decision. The difference offered — that one derives something false about the ledger and the other only mis-sorts for a human — does not hold here: the gauge's reading is the one quantity L64 attaches a scope limit to, and it read clean on a failure.

The deeper point is the skill's: a check is itself an explanation of why you now believe the result, and it takes the same measure. If an instrument's wrong reading is never a refutation, then no run of these instruments can count against anything, and the whole apparatus becomes easy to vary.

---

## 6. What would make it harder to vary

Two cuts and one job, in the order I would do them.

1. **Run the variation test.** It is already written down, at L64 line 143: "change the prose (drop a sentence, deny a clause, swap a name), translate again, and the ledger changes as the commitments do and nowhere else." I grepped the whole repository: it appears in L64, in L64's copies inside two return bundles, and in the L64 log entry. It has never been named in a plan or run. It is the only instrument named anywhere in the project that reads the **text beside the ledger**, and it is therefore the only one that can move when the translator is wrong and the ledger is self-consistent — the case in which all five current instruments are blind. It has in fact already run once, unnamed: L66's flip pairs are a variation test on the translator, and its reading is the cleanest in the record (L66 results line 37, "everything else identical to the letter"). That reading was taken under E5, whose job was to test the checker and the sameness program.

2. **Give every instrument the same-reading job of section 4.** For each: name one admissible reformulation of a ledger that must not change its reading, and run it. Three of the three programs fail it now; each swap in section 3 is chosen to pass it.

3. **Declare the sixth instrument and gauge it.** "A fresh agent reads the code and the reports" belongs in L64 section 5's table with the others. Its gauge is available and cheap: for every finding it returns, whether the finding was later confirmed against the code or the outputs, and — the reading that is missing — what it did **not** find that a later reader did. Without the second half it is a catch-all with no gauge, which is exactly what section 3 holds against the others.

---

## 7. Lessons (failures only)

- **A test whose three layers are one hand passes for that reason.** L71's E5 predicted the consequences program would show no SINCE step, with a SINCE step as what would count against; the queries list (consequences.py lines 16–18) makes that outcome certain, and the same hand wrote both. Marked met (L71 results line 31). Fix: an expectation about an instrument's silence is not an expectation; read the code and state it as a known limit, or add the query and make the expectation testable.
- **A gauge on one bucket of a three-bucket catch-all reads green while the catch-all swallows the job.** L72's E8 gauged near pairs only (plan line 18); near read two, and seventeen of twenty-one lines went to the "only" buckets and were resolved by hand (results lines 36, 43). Fix: the gauge on a catch-all counts everything the catch-all takes, not the smallest part of it.
- **A diagnosis written from a report's shape, not its code, sizes the remedy wrongly.** L66 results line 39 credits the driver with printing sentence numbers in what-if headings. `run_check.py` line 296 prints the ledger's `whose` field; the anchor was the translator's. And `describe_lines` (line 47) prints the sentence in every block it builds, so "nowhere else" is false. The "one line in the driver" fix (results line 68) is under-sized. Fix: before writing what a report does, grep the code for the string.
- **An instrument built on one ledger inherits that ledger's shape as a silent assumption.** `consequences.py` was built on ledger A, which has no worlds and whose two general lines it cannot see; both faults found since (Lesson L7; Astra Pro finding E) are cases ledger A does not contain. Lesson L7 already states the fix; it is stated for worlds and applies to general lines and to duplicate notations too.

---

## 8. Parts that never met a hard case

- `sameness.py` S2, the standing stripper: every ledger tested writes the standing either as a leading bracket or in the `standing` field. A ledger with the standing written inside the line has never been run against it.
- `consequences.py` C2, the ten queries: no run has varied the list.
- `consequences.py` C6, "nothing is written to the ledger or the rig": true as read, but the module-level `WORLD_REMOVED` is shared state that `check()` leaves set to the last ledger's case lines (`run_check.py` line 327, not to `[]`). No run has imported both entry points into one process. **Worked out**; it is latent, not live, because `load_driver` builds a fresh module each run.
- The plant method P1: no plant has ever been made whose stated opposite is already present in the passage. P15 came nearest and lacked its instance (L66 results line 33).
- The read-back R1 against a report containing a contradiction: none occurred in L66, so E7's contradiction criterion is unmarkable (L66 results line 39). The instrument has never met the finding kind the job was written around.

## 9. Findings that fit no part

- The one plant the record counts as caught sits under a "NO FAULT FOUND" header (`P13_OpenAI_Codex.report.txt` lines 3, 7). Neither the plant method nor the report has a part that notices a header contradicting its own body.
- P09's two JUMPs land on sentence 6 of a passage planted at sentence 4 (**seen**, report and `ledger_P09.json`). No expectation in L66 covers a finding on an unplanted sentence of a planted passage.
- The report is the only artefact in the project that contains two findings which, read together, refute one of them (P14: JUMP and HOLDS). Nothing in the set reads a report against itself.
- `sameness.py` prints counts for buckets that overlap, and prints one B line as the near partner of two A lines (**seen**, my run). No part of the method treats the tool's output as a partition or checks that it is one, yet L72's E1 and E8 are both read off those counts.

## 10. What was not looked at

Rig 2 and `check2.py` beyond its gauge line. `checker_rules.pl` beyond the clauses the instruments query. File 11 and the theory's Parts I, III, V, VI, IX, XV. The eighteen passages' texts (I read ledgers, reports and the key table, never a passage). Whether any checker finding is true. The other 72 corpus families. Rig 1's frozen driver and the three earlier `run_check_*` copies. The L62 return's 1,145 files beyond the sameness discussion in `45 Test results`.

## 11. One next step

Run the variation test named at L64 line 143 on the two texts where an instrument has already failed: take T10-B and T05-B, make three changes each (drop a sentence, deny a clause, swap a name), have one translator translate all eight versions blind to the pairing, and read the four instruments across each pair. It costs eight translations, it is the only design in the project that reads the text beside the ledger, and on the evidence of L66's flip pairs it will give a clean reading.

---

## What would change my mind

- **On the gauge.** A ledger where a sentence contributes nothing to the ledger and something to the bin, so that the numerator and the denominator do count the same thing. I did not find one: `bin_entries[].sentence` exists in every L66 ledger and is discarded by `run_check.py` line 332. If the owner's intent is that a bin entry is the unit and "sentences" is a slip of wording, then G2 is a naming fault and G3's threshold is stated in the wrong unit — but T10-B still reads zero, and that is the finding that would have to be answered another way.
- **On `sameness.py`.** A case where two translators who never saw each other's ledgers, and who both follow 38 rule 3, produce line text that the wording test matches. L62's Part A is not that case: the worker had read the other model's six ledgers before translating and says so (`45 Test results` line 22). If such a case exists, S4 and S5 are held on it and my "loose" is wrong.
- **On `consequences.py`.** A statement in the record that J3 was always meant as "what follows that no line states", not "what follows". L64 line 17 reads the wider way and L65's plan line 16 describes the subtraction as a means, not as the measurand. If the narrow reading is the owner's, C4 is *held* and the report's section 3.2 poke is a naming dispute.
- **On the read-back.** Evidence that the reader cross-checked a printed sentence number against something. Astra Pro did cross-check four against bin entries that quote the sentence's words (L66 results line 53), which is more than I credit; if the brief required that, R2 is held for those findings. The brief does not require it (`Reader brief` lines 5–10).
- **On the plants.** A record, written before the run, of what counts as "a fault reported on the planted sentence". If one exists outside the L66 plan and names the what-if FAILS, P2 is held and my "the criterion was settled after the run" is wrong.
- **On the whole.** One case where an instrument's own reading — not an agent reading code or reports — separated the language from the translator from the instrument. I looked through L62, L65, L66, L69, L71, L72 and L74 and did not find one. One would overturn section 5.
