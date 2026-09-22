# W10 marking plan — the instrument, frozen before any report is read

Written 22 September 2026 by A4 of stage A, plan W10, before any run of this round exists and before any report of this round is read. The machine-readable form is `criteria.json` beside this file; where the two differ, this file is the instrument and the JSON is wrong. Once stage B starts this file stays as it is; a change is an addendum that names the finding that forced it and says what it gives up. **Section 13 is that addendum**, written 22 September 2026 in the fix round before stage B: four criteria changed under the reviewer's faults 3, 4, 5 and 18, and `affordance.json` added beside this file. Where section 13 and an earlier section differ, section 13 is the later text and is the instrument; the earlier sections carry a line at the point where they differ. **Section 14** is round 2's addendum (faults 4 and 25) and **section 15** is round 3's (fault 28), under the same rule: the later section wins where they differ, and the earlier one carries a line where it does.

It answers the question W10 stage A4 sets: how the reports of stage C are marked, so that a difference between arms is a difference in the emission and not a difference between markers.

Sources it is built from, all quoted below where they do work: plan 52 (`HV Skill/tests/52 Marking plan - frozen before the corpus is read.md`), plan H63 and results H64, W3 section 5 (phases 3 and 4) and section 7, W8 parts B4, C4, A3, A10, B10 and section 5, and file 11 where the theory decides something. The reports it was tested against are in `HV Skill/rigs/plan 49 rig - DeepSeek on outside papers/runs_sonnet5/` (Sonnet 5, file 30) and `runs_repeat/` (DeepSeek V4.1 Flash, file 30): twenty-four reports on two documents, P3 (Bostrom, *Are You Living in a Computer Simulation?*) and F4 (Wells, *The Time Machine*).

---

## 1. What is measured, and what is not

Plan 52 said it for the corpus round and it holds here: **truth is not marked.** The documents of this round are outside documents no run in the record has read, and nobody here knows which of their explanations are true.

What is marked in *this* round is narrower still than plan 52's. Plan 52 marked the skill. W10 marks the **arrangement**: what changes in the emission when the arrangement around one reader is changed — one agent carrying its own history, fresh calls handed a transcript, a summary, a carry-over note, a partition, a prefilled skeleton, a withheld change list, a criticism in the context, a name exchange. W10 section 1: "One claim under test: model W8".

So a field earns its place here only if some part of W8 needs it. Fields plan 52 carried that no part of W8 needs are dropped, and section 10 says which and why.

Three things are never done with these marks. They are never added up. They are never summed across fields, arms or readers. A count falsifies a prediction and settles nothing about a part of the model: W10 section 12 lists "moving a mark on a count alone" among the traps, and W8 part A7 is the part that forbids it.

## 2. The three layers, kept apart

Plan 52, quoted whole, because it is the rule and not a paraphrase:

> A report can be wrong in three places, and the marks must say which. 1. **The document.** What it actually says. Checked against the text. 2. **The skill.** What its words told the reader to do. 3. **The reader.** DeepSeek V4.1 Flash, which may simply be careless. A finding contradicted by the document is the reader's fault unless the skill's wording pushed it there; only then is it the skill's. The marker must name which, in one line, every time.

Two things change for this round and nothing else.

- The reader is not only DeepSeek. Stage C's reader is Sonnet 5 through the subagent transport, with DeepSeek V4.1 Flash as a second reader when the key arrives, never summed with the first (W10 section 4). Layer 3 is whichever reader made the report.
- Layer 2 is read as **the thing under test**: the skill's words (file 33) together with the arrangement the arm sets around them. That is what W10 varies, and it is the layer a fault must be charged to if it is to bear on W8 at all.

Every report carries `layer_at_fault` (the document, the thing under test, the reader, or none) and `layer_at_fault_line`, one line saying what the fault is and why it sits there. Where the layer is the thing under test, the line quotes the sentence of file 33 that pushed the reader there. Plan 52's trap is kept: "Recording a break without quoting the line of the skill that caused it."

`layer_at_fault` carries no arm difference. It is the marker's own attribution, and a difference on it between arms would be a difference between markers wearing an arm's coat.

**Tested on two reports.** `runs_repeat/F4-m1-r1.json` writes "| P7 | fixed | the owner set it." — the layer is *the thing under test*, because H64 traced this to the skill's wording and not to the reader's care: "the eight part-marks (held, held if, ..., borrowed, fixed, unknown) and the provenance words (fitted, built, asserted) are two closed lists in the same style, and 'nothing in the skill says the two vocabularies must not be mixed'". Both markers of H63 judged this use of *fixed* improper. `runs_repeat/F4-m2-r2.json` writes "P8 the Psychologist's \"presentation below the threshold… diluted presentation\"" — the layer is *the reader*, because the document gives that phrase to the Time Traveller (H64: "'diluted presentation' is the Time Traveller's phrase handed to the Psychologist") and no line of file 33 pushes a reader to move a quotation from one speaker to another. Those two reports are fitting for this criterion.

## 3. Within-step and cross-step: the sorting, and where the line is drawn

W8 part B4, quoted:

> Fields whose work is done inside one step (a part's mark reached by remove, swap and poke) need only that step's material in the call's context. Fields whose object is the set of parts or the whole candidate (pairs that pull, the best rival, the same-explanation verdict, remove-in-groups) need a context that holds the parts together. The sorting is about what one call's context holds, not about whether a process persisted; it is written before any run and is not re-sorted on the reports that break it.

The line: **cross-step** is a field whose object is the set of parts of the explanation, or the whole candidate. **Within-step** is a field a call can reach from one part and one step's material. B4 names three within-step tests and W3's P3.5 confirms them: if swap and poke fail to certify "they are dropped from the within-step set for phase 4 and remove carries it alone".

Within-step: `test_remove`, `test_swap`, `test_poke`, `shape`, `shape_elements`, `marks_per_part`, `question_identity`, `modules_self_reported`, `modules_served`, `attributions`, and the record fields.
Cross-step: `test_flip`, `test_reverse`, `test_hunt`, `test_addjob`, `test_rival`, `test_pull`, `test_patches`, `test_inside`, `turned_own_test`, `same_explanation`, `pairs_that_pull`, `rivals_built`, `remove_in_groups`.

Eight of the eleven tests are cross-step because their object is the whole candidate: the flip asks whether the same explanation could have covered the opposite; reverse asks which of two questions the explanation answers; hunt asks whether the conclusion is in the starting points; add a job asks what else must be so; the rival is another whole explanation; pull takes the parts in pairs; the patches test asks about the claim's history; look inside asks about the workings of the whole.

**The pair that pulls, named, because W8 names it.** Section 6, builder B: "B4 against B12: the more fields called cross-step, the more arm (d) is predicted to lose, and the easier P4.3 passes for a reason other than partition; the line is drawn at fields phase 3 certified whose object is the set of parts." This instrument gives way to B4 twice, and says where.

- **Shape is within-step.** Its object is the report's form, not the set of parts: a final call handed a pile of answers can write all seven of its elements from that pile. What would show the line drawn in the wrong place: arm (d) losing shape while keeping every cross-step field. If that happens, shape is re-sorted in the *next* round's plan and not in this one, because B4 forbids re-sorting on the reports that break it.
- **`remove_in_groups` is carried apart from `test_remove`.** B4 names remove-in-groups among the cross-step fields and the eleven-test remove field is within-step; one field cannot be both. So the group removal is its own field.

## 4. The fields

`criteria.json` carries each field's exact words, its closed list, its layer, its sort and the example that fixes its boundary. This section gives the reasons and names the two reports of the record each criterion was tested against. Naming them is not praise of them: under the qualified Derivation 3 (file 11, Part XVI: "A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not"), a criterion tested on two reports is faithful on those two and, wherever the population admits another reading, unconstrained everywhere else. Section 11 says what that costs.

### 4.1 The eleven tests: RAN / NAME ONLY / ABSENT / CANNOT

Plan 52's general rule is kept word for word:

> **Each of the eleven tests**, one mark: **RAN** (applied with a concrete change or a named neighbour), **NAME ONLY** (mentioned with no content behind it), **ABSENT**, or **CANNOT** (the reader says, or the document shows, that the test has no purchase on a document of this kind).

Kept unchanged, because H64 found them reliable at or above forty of forty-eight: **flip** (46), **pull** (45), **rival** (44), **remove** (43), **hunt** (43), **patches** (41), **reverse** (40). Their per-test criteria in `criteria.json` say in plain words what the general rule already meant; nothing is added that could change a mark.

> **Changed since.** `test_pull` was reworded on 22 September 2026 under the reviewer's fault 3, because it had no value for a common report shape. **Section 13.1 is its criterion now**, and this paragraph is superseded for pull alone; the other six kept tests are untouched.

Reworded, because H64's own trap paragraph names them — "The disagreements sit on four tests (poke, add a job, swap, inside), and those are where the skill's wording is loosest by the second marker's own breaks":

- **swap (36 of 48).** RAN when the report puts a *named* near neighbour in the place of a *named* part and says what happens to a named job. The word "swap" need not appear. A class of replacements with no particular neighbour ("use a different observer-selection rule") is NAME ONLY.
- **poke (35 of 48).** RAN only when both halves are named for one named part: a change to the world the report says would alter the outcome, and one it says would not, the second next to the disputed line. One half alone is NAME ONLY. A report that only says whether the *document* offers a pair is NAME ONLY, however well it says it: this field records whether the reader made a change, and a reader who names no change has made none. What that gives up: a report that correctly finds the document affords no poke is marked NAME ONLY, which understates it. The escape is CANNOT, below.
- **add a job (35 of 48).** RAN only when the report names something else that must also be so if the explanation is right, not already in its own job list, and says whether the explanation covers it or which rival it rules out. A job tagged *added* in the job list is not this test. This is H64's break kind 4, quoted: "'Added' means two things: Step 2's provenance tag for a job the reader supplied, and Step 5's test 'Add a job'; readers wrote the tag and never ran the test."
- **look inside (38 of 48).** RAN when the report names a change that reaches past what comes out, into how the thing works, and says what that change would show. Naming a change and saying it cannot be made is NAME ONLY. This is H64's break kind 2: SKILL.md's whole-explanation-checks line "names no slot for *look inside* or *add a job*".

**CANNOT is tightened to file 33's own form.** File 33's report section: "A test that cannot bite on a document of this kind is named, with the sentence of the document that leaves it nothing to reach, and the part it would have settled is left *unknown* with that test named; it is never simply left out." So CANNOT needs three things: the test named, the sentence of the document quoted, and a part left unknown with that test named. Anything less is NAME ONLY. Both markers of H63 recorded zero CANNOT under plan 52's looser wording; W3's P4.7 predicts a count above zero under file 33's new instruction, and this is the form that count is made of.

**The two reports each test was tested against.** Values and quotations are in `criteria.json`; the pairs and what each pair fixes:

| Test | Fitting reports | What the pair fixes |
|---|---|---|
| remove | `runs_sonnet5/P3-m1-r1` (RAN), `runs_sonnet5/F4-m1-r2` (ABSENT) | a report full of swaps and marks can still take nothing away |
| swap | `runs_sonnet5/F4-m1-r1` (RAN), `runs_repeat/F4-m2-r2` (RAN) | the word "swap" appears nowhere in the second and the test is applied four times: absence of the word is not ABSENT |
| poke | `runs_sonnet5/P3-m1-r3` (RAN), `runs_sonnet5/F4-m2-r1` (NAME ONLY) | both halves named for one part, against a report that names the document's missing pair and no change of its own |
| flip | `runs_sonnet5/P3-m1-r1` (RAN), `runs_sonnet5/P3-m2-r1` (RAN) | "the core deduction (C) does not flip" is the redirection for a derived conclusion, not the test unrun |
| reverse | `runs_repeat/F4-m2-r1` (RAN), `runs_sonnet5/F4-m1-r2` (NAME ONLY) | poking both ends separately, against naming direction and poking neither |
| hunt | `runs_repeat/F4-m1-r1` (RAN), `runs_sonnet5/P3-m1-r1` (RAN) | an answer of "No" is the test run |
| add a job | `runs_repeat/P3-m1-r3` (RAN), `runs_sonnet5/P3-m1-r1` (ABSENT) | the tag *added* on a job is not the test |
| rival | `runs_sonnet5/F4-m1-r2` (RAN), `runs_repeat/F4-m1-r3` (NAME ONLY) | "the rival is not ruled out" is not a change that tells them apart |
| pull | `runs_repeat/F4-m1-r1` (RAN), `runs_sonnet5/F4-m1-r2` (RAN) | a pull between things that are not part labels is still the test run; the pair is what `pairs_that_pull` records |
| patches | `runs_repeat/P3-m2-r2` (RAN), `runs_sonnet5/P3-m1-r1` (RAN) | "no gauge is offered" is the test run, not the test skipped |
| look inside | `runs_repeat/F4-m1-r1` (NAME ONLY), `runs_sonnet5/P3-m1-r1` (ABSENT) | one sentence short of CANNOT: the change is named and nothing is shown |

Three values are untested by this record and are named as untested rather than left out. Swap is never ABSENT or CANNOT in these twenty-four reports; look inside is never RAN or CANNOT; `remove_in_groups` is never RAN. "Found nowhere" means unknown (`testing-against-cases.md`): it says what the twenty-four reports contain and nothing about the new corpus.

### 4.2 The three fields H64 struck, each with a written rule

H64: "Three fields are struck from further use as marked: shape's PART boundary (a written rule is needed), 'turned own test' (the criterion is reworded or dropped), the same-explanation verdict as a count (kept as quotes only)."

**Shape's PART boundary.** H64: "34 of 48 agree, and every disagreement is the second marker saying PART where the first said NONE (seven bare-reader reports) or FULL (seven skill-mode reports); the order never inverted, and no bare-reader report was called FULL." The disagreement was never about the order, only about where FULL stops. So the marker no longer judges the shape. It fills seven elements, each Y or N — E1 the question frozen; E2 the parts listed; E3 the jobs listed, apart from the parts; E4 the change list, or what it leaves out, in one place; E5 at least one test applied with a concrete change or a named neighbour; E6 a mark on every part in E2's list; E7 the method's seven report sections, present, in its order, each doing its work whatever it is called — and the shape follows by rule: all seven Y is FULL, one to six is PART, none is NONE. A disagreement is then locatable at one element instead of at a word.

*Tested on:* `runs_repeat/F4-m1-r1` is FULL, seven of seven, its jobs list quoted ("J1 why Time is thought different from Space (given — the Medical Man)…"). `runs_sonnet5/P3-m1-r1` is PART on one element only: it writes "**Where jobs came from.** The three-way disjunction is the paper's own stated job (given)" and lists no jobs. That is the second marker's own break kind 2 in H64 — the seven-heading report "gives no heading for the jobs list Step 2 requires" — now showing up as a countable element rather than as a marker's judgement. Those two reports are fitting for this criterion.

**"Turned one of the document's own tests back on it".** H64: "8 of 48, the first marker saying N in 47 and the second Y in 41; the criterion's words are read two ways and the field says nothing until they are fixed." The two readings are a strict one (the document aims a test somewhere else and the report turns it on the document) and a loose one (the report uses any check that appears in the document). The strict reading is taken, for the reason the skill gives for any test — "run it on the very thing it is meant to catch, and on that thing's nearest innocent neighbour. A test that both pass is measuring something else" — and because the loose reading was Y in forty-one of forty-eight and so separated nothing. Y needs three things: the document states a test, check, gauge or standard aimed at something other than the explanation under test; the report applies that same test to the explanation under test; the report says what the result was.

*Tested on:* `runs_repeat/F4-m1-r1` is Y — "The Psychologist offers a gauge — a spinning spoke, a flying bullet — and it fails: both are blurred, not invisible." The document's test is aimed at ordinary fast objects; the report aims it at the part under test and reports the result. `runs_sonnet5/P3-m1-r1` is N, and it is the nearest innocent neighbour: "A real swap test, done by the author, that survives." The author's own test on the author's own part, noted and not turned. Those two reports are fitting for this criterion.

**The same-explanation verdict.** H64: "38 of 48, every disagreement the second marker reading 'nothing tells them apart' as the verdict", and it was struck "as a count (kept as quotes only)". It returns as **presence on one document, with the sentence quoted**, never as a count across documents. PRESENT when the report says of two named candidates that no change on the change list tells them apart, in those words or in words that carry them; the sentence is copied into `same_explanation_quote`. A report that says a rival "is not ruled out" is ABSENT.

*Tested on:* `runs_sonnet5/F4-m1-r1` is PRESENT — "At this point in the story the two are, by the method's own rule, **the same explanation at this level**: no change on the list (only 'watch the table') tells them apart." `runs_repeat/F4-m1-r3` is ABSENT — "The rival is not ruled out." That is the exact wording the two markers of H63 split on. Those two reports are fitting for this criterion.

The theory's reason for keeping presence and dropping the count is file 11's Derivation 2 as W8 part A7 reads it: a report of "no separating change on this contract" is a fact about one document's change list, and adding such facts across documents makes no larger fact.

### 4.3 The three new fields (W3 P3.2)

> **Changed since.** All three were reworded on 22 September 2026 under the reviewer's faults 4 and 5: the part key and the pull between two groups in **section 13.2**, the rival's naming rule in **section 13.3**. Those sections are the rules now; what follows is the reason each field exists and the pairs it was tested on, and where the wording differs the later section wins.
>
> **Changed again**, the same day, in round 2 of the fix round: the reviewer held fault 4 open and returned fault 25. The part key's two further clauses are in **section 14.1** and `rivals_built`'s three further clauses in **section 14.2**, and those sections are the rules now, later than section 13 and later than this paragraph.

**`marks_per_part` — the eight marks, read by document.** One entry per part: the key is the report's own label, copied exactly; the value is the one of the eight marks the report gives it. Longest match first, so "held if" is read before "held". Extra words do not change a mark: "Held, but coarser than stated" is *held*; "Held, catch-all with a gauge" is *held*. A cell containing two or more different marks of the eight is **left out of the map** and copied into `quotes`; the field records marks and not the marker's reconciliation of two. W3 P3.2 requires the field be "read by document", and it is: the map belongs to one report on one document and is never summed.

*Tested on:* `runs_repeat/P3-m2-r2`, eleven rows, every one exactly one mark with words round it ("P10 DOOM / not-special | Held, catch-all with a gauge | The gauge is named: a giant meteor would show we had been exceptionally unlucky."). `runs_sonnet5/P3-m2-r1`, where four of six rows carry two marks each — "**Loose** on the exact numbers, **held** on the qualitative point"; "**Borrowed**, and **held if**"; "**Idle** for the core trilemma; **borrowed** as color"; "**Unknown / loose**" — all four left out and quoted. Those two reports are fitting for this criterion.

**`pairs_that_pull` — pairs, named.** One member per pair the report names, written `A|B`, where A and B are two different labels from the report's own part list. A tension named between things that are not in that list is not a member and goes in `quotes`; `test_pull` still records that the test ran. A part said to pull against itself is not a member. The empty set is a value and means the report names no pair; null is only for "I cannot tell".

*Tested on:* `runs_repeat/F4-m1-r1` gives `["P3|P8"]` from "(a) P3 against P8: the more the patch covers, the less the vanishing shows. (b) P9 against itself: pass through matter at speed, jam into it at zero." — two offered, one a member. `runs_sonnet5/F4-m1-r2` gives `[]` from "Two later-stated claims about the mechanism pull against each other…" — a real pull, neither side a label. Those two reports are fitting for this criterion, and the pair is chosen so that `test_pull` and `pairs_that_pull` come apart on one report, which is what shows they are two fields and not one.

**`rivals_built` — rivals, named.** A rival is *built* when the report states it in a sentence of its own and either names a change that would tell it from the explanation under test or says plainly that no change on the change list can. A rival only named is not a member.

*Tested on:* `runs_sonnet5/F4-m1-r2` gives `["some sleight-of-hand trick"]` — stated, with three changes named that would tell them apart. `runs_repeat/F4-m1-r3` gives `[]` — "A magic trick… The rival is not ruled out." Those two reports are fitting for this criterion.

### 4.4 The question-identity field

W10 section 4: "The same frozen question is handed to every arm; the question-identity field is recorded on every run." SAME when the question the report freezes has the same target as the one handed in and asks the same thing of it; MOVED otherwise; both questions copied into `question_frozen_quote`.

**The range is not compared, and here is why.** Arm (f) is arm (a) with the change list withheld, so the question handed to arm (f) is the same object with its range removed by design. A field that compared the range would read MOVED on every arm (f) run for that reason, and would be measuring the arm instead of the drift. It would also carry arm (f)'s whole result on its own, which is what W10 section 12 calls reading a difference by construction. So the comparison is target and what is asked, and nothing else.

`question_identity` records SAME or MOVED and nothing more, so two runs that moved to two *different* questions agree on this field. That is why `question_frozen_quote` exists: without the quotations the agreement would be empty. W3 fixes the highest of all its stage B thresholds here, P3.3 at 46 of 48, because "The record holds two drifts in twelve under identical framing (H62); a field that cannot record drift falsifies the instrument."

*Tested on:* no run in the record was handed a question — run.py's framing told each reader to freeze one itself ("freeze the question the document answers (where it answers several, take the one its title or opening makes central, and say so)"). So the two reports were marked against a **stand-in target**, written down before they were marked: *the explanation this document gives of why at least one of the three propositions must be true*, which is what the W10 harness's `question.py` would build for that document from the manifest. `runs_repeat/P3-m2-r2` is SAME — "I froze the one its abstract makes central: **at least one of three propositions is true**…". `runs_repeat/P3-m1-r2` is MOVED — "I take the title's question as central, reached by that disjunction" — the target is the title's yes-or-no about this reader and the disjunction is demoted to a route; ten of the twelve P3 runs in these two folders froze the disjunction, and this one and `runs_repeat/P3-m2-r3` did not. Those two reports are fitting for this criterion. What the record cannot test: whether a marker handed two *literal* questions side by side reads them the same way. Stage B tests that, on the reports in hand, against the questions the record's framing names.

### 4.5 The modules-opened fields, kept apart

W8 part C4 is the part under test and it is quoted in full in `criteria.json`. The two fields are never one:

- **`modules_served`** — filled by program from the transport's own record of the calls it served. File 11, Part IX: "whether a route is active is read from the history, not from the result." This is the read-out P4.6 is read on.
- **`modules_self_reported`** — marked from the report: what the reader itself says it opened. File 11, Part II: "a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was". The reader's list is a measurement of the opening, not the opening.

P4.9 is the count of runs where the two differ: "more than one difference means the self-reported field carries no arm difference and P4.6 is unreadable on it".

The marker's rule for `modules_self_reported`: a file named in prose counts ("the reporting file" is *reporting*, "the question bank" is *question-bank*, "the depth file" is *the-idea-in-depth*); a file named as **not** opened does not count; and an ordinary use of a word that is also a file name does not count.

*Tested on:* `runs_repeat/F4-m2-r1` — "The method's own map sent me to four modules: the depth file…, the domain file…, the reporting file…, and the question bank…", and the word list named as not opened. Four. The same run's record names five, including `word-list`. `runs_sonnet5/F4-m2-r1` — the only occurrence of a module word in the whole report is "the Time Traveller spends all of Chapter I **building** a case", ordinary prose. None. That run's record names three. Those two reports are fitting for this criterion, and they settle something for the harness: a program that scans the report's text for module names returns `['building']` on the second report — nought right, three missed, one invented — and on the first returns `['reporting']` only, because "question bank" is not "question-bank". Run against all twenty-four reports, such a scan invents or misses on every one of the four where it fires. The reader's own list is a marked field, not a scan.

### 4.6 The request-as-sent fields (PA.1)

W8 part A1's prediction PA.1: "every run's record carries the number of requests and the text of each request as sent. A1 predicts exactly one request per step in arms (b), (c), (c') and (d) and more than one in arm (a); any run of the first four with more than one request falsifies the arm's description." It is a compliance count on the phase's practice, and W8 labels it so.

`requests` and `request_text_saved` are filled by program from the run record and are **text, never compared between arms**. The number of requests differs by arm by design, so comparing it would make every arm differ from arm (a) on a within-step field: it would falsify P4.1 and pass P4.4 by construction. PA.1 is read from the run records by the harness's own `agreement.py records`, which is where a compliance count belongs.

*Tested on:* `runs_repeat/F4-m1-r1` carries `"api_calls": 1` and `"tool_calls": 0` — one request, one step, no tool loop. `runs_sonnet5/F4-m2-r1` carries `"usage_total": {}` and no request count at all: the subagent transport of the old rig counted nothing and saved no request text. Both fail `request_text_saved`, which is the point of a compliance count — it can fail, and on the record it does. Those two reports are fitting for this criterion.

### 4.7 The arm (e) fields

Two fields, two layers, two sources, because W8 part B10 makes two different claims.

- **`ports_set`** — which ports the skeleton set. Written by the harness from its own record of the skeleton, for arm (e) only; one line per port set and one per port not set. On the Sonnet transport the value is "none set; the skeleton was placed in the context", because B10 says "A harness that only adds passages to the context sets no such port: it is a change to what the call reads", which is why the Sonnet arm (e) is the control and not the test (W10 section 10). W3 section 8 requires the arm to name which ports it set, and this is where it is named. Text, never compared.
- **`marks_outside_closed_list`** — the number of parts whose mark cell contains none of the eight marks, or two or more. This is the **gauge** that shows whether the skeleton set the vocabulary it claims to set. It is not certified and carries no arm difference: the skeleton prints the eight marks into the emission before the reader writes anything, so a count going to zero under arm (e) is the port being set, not evidence about the within-step marks. Reading P4.4 on it would pass P4.4 by construction, which is what the skill means by a test that its target and its target's innocent neighbour both pass.

*Tested on, `ports_set`:* it cannot be. No run in either folder was given a skeleton, and W8 part B10's own holder says why: "Unknown until arm (e) runs: no test in the record has set an emission port, so nothing now holds this part." The test is named here, with the sentence that leaves it nothing to reach, and the field is left unknown until arm (e) runs — which is file 33's rule for a test that cannot bite, and not a field quietly left out.

*Tested on, `marks_outside_closed_list`:* `runs_sonnet5/P3-m2-r1` is 4 — the four two-mark rows listed in section 4.3. `runs_repeat/F4-m1-r1` is 0 — nine rows, each exactly one of the eight with words round it; "loose, catch-all, no working gauge" is one mark and a description, not two. Those two reports are fitting for this criterion.

### 4.8 The arm (x) field

W8 part A10 is the part under test and PA.3 the prediction: an arm handing the same document with two speakers' names exchanged, against arm (a) on the unexchanged document, with the emission predicted to move on at least one certified field on at least four of the eight documents.

`attributions` is the field the exchange is read on. One member per numbered item of the report's own part list or job list that the report attributes to a named speaker or agent of the document, written `name|label`. An item attributed to no name, or to the reader, or to a thing rather than a person, is not a member. Attributions outside the numbered lists go in `quotes`.

**Whether an attribution is right is not marked.** The arm is read against its own unexchanged arm (a) control on the same document, which is exactly why W8 A10 requires that control: "The unexchanged control is needed, since the record already holds attribution errors without any exchange."

*Tested on:* `runs_repeat/F4-m2-r2` gives `["the narrator|P11", "the psychologist|P8"]` — two of eleven parts carry a name; P10's "his" is not a name. H64 records that the P8 attribution is wrong in the document, which is the reason the control and not the marker decides what moved. `runs_repeat/F4-m1-r1` gives `["the medical man|J1", "the narrator|J4", "the psychologist|J4"]` from its job list; J3's "the demonstration" is not a name and J6 and J7 are the reader's own. Those two reports are fitting for this criterion.

One boundary the record fixes by refusing: the field needs a document with two named speakers. P3 (Bostrom) has none, and every P3 report in both folders returns the empty set. That is why W10's corpus must carry "at least six with two named speakers or agents whose names the re-identification arm can exchange" (W10 section 3, A2), and why arm (x) does not run on the other two.

## 5. Agreement, by field and by document

W3 section 7 fixes it and is quoted whole:

> A field agrees between two runs when the marker's record for the field is the same (RAN or not; the same mark on the same part; the same pairs named; the same rivals built; the same question kept) on the same document. Agreement is a count of documents, by field, never summed across fields or arms.

Per kind: enum, int and bool agree when equal; a set agrees when the sets are equal; a map agrees when the whole map is equal; text is never compared and is kept so a disagreement can be traced. A document where either side has no value is **unreadable and named**, never agreement — `testing-against-cases.md`: "'Found nowhere' means unknown. It shows neither 'unneeded' nor 'impossible'."

**The P4.1 baseline rule, as W3 fixes it, quoted:**

> **P4.1 (from M5 i).** For each certified field: the baseline is the number of documents on which any two of the three repeats of arm (a) disagree; the comparison is the number of documents on which any repeat of arm (a) disagrees with any repeat of arm (b). Falsified if, on any certified field, the comparison exceeds the baseline by more than two documents. A field whose baseline exceeds half the documents says nothing, and is reported so. Agreement, where found, settles nothing about what either arm instantiates.

All three (a)-to-(a) pairs are taken and a document counts as disagreeing when any pair disagrees. W10 section 5 fixes the numbers: n = 8 documents, three repeats per box, tolerance two documents, and **k = the arm's own (a)-to-(a) baseline on that field plus three** for a loss.

Why there is a baseline at all is W8 part A3's work, and the reason is worth keeping in sight while the counts are read: "A call realizes exactly one edit-boundary pair of the organization of A2, so it instantiates a valuation and not the organization; and the compatible valuations at one context may be several, so two calls on one context may emit differently." Its prediction PA.2 is that the baseline is above zero on at least one certified field; a baseline of zero everywhere falsifies A3 at this grain.

**What the predictions are read over.** P4.1 to P4.5 and PA.3 are read over certified fields only — the fields marked `certified_candidate: true` that stage B certified. P4.6 is read over `modules_served` alone. PA.1 and P4.9 are read from the run records and from no marker's field. Agreement between two markers is the same rule counted over reports, by field, never summed.

## 6. Stage B: what certifies a field, and what is struck if it does not

W10 stage B: "The 96 marked reports in hand re-marked by two blind Sonnet markers under A4's criteria; agreement by field computed; W3's P3.1 to P3.5 ticked. **No field carries an arm difference in stage C unless it agreed here.**"

The thresholds, all from W3 except the one marked added:

| Field | Threshold | Source |
|---|---|---|
| shape, turned_own_test, same_explanation | at least two of the three at 44 of 48 | W3 P3.1 |
| marks_per_part, pairs_that_pull, rivals_built | each 40 of 48, marks_per_part read by document | W3 P3.2 |
| question_identity | 46 of 48 | W3 P3.3 |
| test_swap, test_poke | each 42 of 48 | W3 P3.5 |
| the other eight tests, remove_in_groups, shape_elements, modules_self_reported, attributions | 39 of 48 | **added here** |
| any field | at most one second rewording across the whole instrument | W3 P3.4 |

The added number is 80 percent of 48, rounded up: the only number the record fixes for a test field, from H63's prediction 2, which H64 marked borne out at 84 percent of the 528 cells. It is named as the instrument's own addition and not as W3's. Without it a field agreeing on 20 of 48 could carry an arm difference, which is worse than a number that may be wrong. What would show it wrong: a field that agrees on 38 of 48 in stage B and on which every arm difference in stage C exceeds its own (a)-to-(a) baseline by more than the tolerance, which would mean a struck field was carrying real signal.

**What is struck.** A field below its threshold is struck from carrying an arm difference in stage C. It is still marked; its quotations are kept; it is named in the results file, with its number. Three consequences are fixed now, before any number exists:

- If fewer than two of the three struck-and-reworded fields reach 44 of 48, "the cross-step fields cannot carry an arm difference; phase 4 runs on the certified fields and the two marker-free read-outs (the tool audit; the modules-opened trace) alone, and says so" (W3 P3.1).
- If `test_swap` and `test_poke` fall below 42 of 48, they leave the within-step set and the within-step set becomes `test_remove`, `shape`, `shape_elements`, `marks_per_part`, `question_identity`, `modules_self_reported` and `attributions`. P4.4 is then read on those.
- If a second field needs a second rewording, the phase stops and reports the patches with what each gave up (W3 P3.4). `testing-against-cases.md` is the reason: tuning a home-made test until it passes is forbidden, and the count of patches is the gauge.

Stage C adds one rule that stage B cannot supply: a field whose (a)-to-(a) baseline in stage C exceeds half the documents says nothing, whatever stage B said about it.

## 7. The marker's conflicts, named

Not a disclaimer. Each of these is a way this instrument could be agreeing with itself.

1. **The marker and the reader are the same model.** Stage C's reader is Sonnet 5 and stage D's two markers are Sonnet 5. A model marking the emissions of its own family may read them more kindly, or more fluently, than a stranger would. The check that exists is stage E: five DeepSeek examiners re-mark a random half blind, and W10's W10.5 fixes what happens if they disagree — "fewer, and the instrument does not travel between readers and the Claude marks carry no cross-reader claim".
2. **In stage E a DeepSeek examiner may mark a DeepSeek reader's own report.** The examiner's sample must record, for every report it marks, whether the report came from the examiner's own model, and the agreement count must be reported split by that. Otherwise a model's agreement with itself is counted as agreement between readers.
3. **The criteria were written with the predictions in view.** A4 read W8's section 5 and W3's P3.1 to P4.9 before writing a single criterion, so the field list is the one the predictions need. W10 fixed the field list, which limits this; the *boundaries* are mine, and a boundary drawn to make a prediction readable is a boundary chosen by its answer. Two places where that pressure was strongest are marked in the file itself: the question-identity field's decision not to compare the range (which protects arm (f)'s result), and the decision to keep `marks_outside_closed_list` and the record fields out of the certified set (which makes P4.4 harder to pass, not easier).
4. **The criteria are fitted to twenty-four reports on two documents under skill file 30.** Under the qualified Derivation 3 they are faithful there and, wherever the population admits another reading, unconstrained on A2's twelve new documents, written under file 33, in domains neither P3 nor F4 belongs to. Stage B is the first test on 96 reports; the new corpus is untested by anything until stage C runs.
5. **This instrument's author also wrote the striking rules.** A rule that strikes a field is a rule that could quietly protect a prediction by removing the field that would have falsified it. Every threshold but one is W3's, fixed before this round; the one that is not is named as added in section 6, with what would show it wrong.
6. **Both markers carry the same skill.** Neither is blind to the fact that the report under its eye is a hard-to-vary report, and both read it with file 33 in hand. What that cannot catch is a fault that file 33 and both markers share.

## 8. What the instrument asks of the harness

Three things, small, and the second is shown to bite; a fourth was added in the fix round and is marked as added.

1. `first_marker.py` builds its marking prompt from every field in the criteria. The four fields whose source is the run record (`modules_served`, `requests`, `request_text_saved`, `ports_set`) must be left out of the prompt and filled at collect from the run record; otherwise every marker returns null on them and four fields are unreadable on every report. Confirmed by building a prompt from these criteria in memory: it asks the marker for all four, and `modules_served` is the one P4.6 is read on.
2. `agreement.py` reads P4.1 to P4.5 over every comparable field. It must read them over fields with `certified_candidate: true` only. Shown: in a dry run where arm (e) moved nothing but `modules_served`, P4.4 came out `holds=True` carried by `modules_served` alone — a read-out with no marker in it passing the emission-port prediction.
3. `first_marker.py validate` should check two things this file fixes and the code cannot know: that `shape` follows from `shape_elements` by the rule in section 4.2, and that every key of `marks_per_part` appears in the report.

4. **Added 22 September 2026** under the reviewer's fault 18 and addendum W11's decision D4: `agreement.py` must read `instrument/affordance.json`, read P4.2 and P4.3 over the cross-step fields that at least one of the eight arms documents affords, and flag a field that never varies across every run of every arm as "never varies" beside its "uninformative" flag. Section 13.4 says why and what the table holds.

None of these is a fault in A1's code, which was written before this file existed and says so. They are what the instrument needs from it.

## 9. What was dropped from plan 52, and why

Each drop is a part removed; the skill says to say what it cost.

- **Claim-checking (SUPPORTED / MISREAD / OUTSIDE, up to five claims per report).** Dropped. It is the most expensive field in plan 52 — the marker must reread the document with the report in hand — and no prediction of W3, W8 or W10 is read on it. What it gives up: no field in this round tells a reader's misreading of the document from an arm's effect. `attributions` is the near neighbour that survives, and the unexchanged control is what makes it readable; outside arm (x) a misreading is invisible to this instrument. If stage C's reports look wrong about their documents and nothing here can say so, that is the bill for this drop, and the results file must say so.
- **Breaks (the quoted line of the skill, what the reader did with it, why it is the skill's doing).** Dropped. W10 section 11 puts the skill's own faults outside this round: "the skill's own faults (held for HV)". What it gives up: this round produces no new break candidates for the HV project even though it will run more reports under file 33 than any round so far. `layer_at_fault` and `layer_at_fault_line` keep the minimum — the layer named, and the line of file 33 quoted when the layer is the thing under test — so a break found is recorded even though it is not a field.
- **The control mark (LEFT STANDING / FALSE ALARM).** Dropped, unless A2's corpus names controls. It tests whether the skill makes a prosecutor, which is plan 52's question and not W10's.
- **The verdict, recorded as given.** Dropped as a field. It is a summary of the marks, and the marks are recorded.
- **Light marking.** Not carried. Plan 52 light-marked ninety-nine reports because forty-nine sources were too many to mark closely; W10 stage D says "First marker and blind second marker over every report", so every report of stage C is close-marked. What that costs is marker time, and the count is large: eight documents, ten boxes, three repeats is 240 reports for one reader.

## 10. Self-falsification: what would show each decision wrong, what was looked for, what was found

Written before the marks exist, so that it cannot be tidied afterwards.

| Decision | What would show it wrong | Looked for | Found |
|---|---|---|---|
| The strict reading of *turned own test* | A report that is Y under the strict reading and where the strict reading is plainly the wrong question | Read all 24 for the strict pattern | One clean Y (`runs_repeat/F4-m1-r1`, the Psychologist's spoke) and the nearest neighbour N. Kept. The risk that survives: if the new corpus affords no such move, the field is N everywhere and says nothing, which stage B will show as agreement and stage C as an uninformative field |
| The poke rule (both halves, or NAME ONLY) | A report that finds correctly that the document affords no poke pair and is marked NAME ONLY, with no better mark available | Found one: `runs_sonnet5/F4-m2-r1` | **Restated.** CANNOT was tightened to file 33's three-part form so such a report has a mark to reach; the report quoted does not reach it, and is NAME ONLY. The cost is written into the criterion |
| Shape as seven countable elements | Two reports of obviously different completeness landing on the same value | Marked both fitting reports element by element | They separate (7 of 7 against 6 of 7) and differ on exactly the element H64's second marker named. Kept |
| Shape sorted within-step | Arm (d) losing shape while keeping the cross-step fields | Cannot be looked for before stage C | Untested. Named in section 3 as the thing that would show the line drawn in the wrong place, and B4 forbids re-sorting on the reports that break it |
| `pairs_that_pull` as part labels only | A report where the rule makes the set empty and the pull is real | Found one: `runs_sonnet5/F4-m1-r2` | **Kept, and the cost written in.** `test_pull` records the test ran, the sentence goes in `quotes`, and the two fields are shown coming apart on one report. Had the fields been merged, that report would have read as no pull at all |
| `marks_per_part` leaving two-mark cells out | A report where most cells carry two marks, so the map is nearly empty | Found one: `runs_sonnet5/P3-m2-r1`, four of six | **Kept, with the number said.** A report whose map is mostly empty is reported as such, not filled by the marker's judgement. If this happens on most of stage C's reports the field is uninformative and the results file says so |
| Comparing only target and query in question-identity | A run that keeps the target and quietly changes the range, and is marked SAME | Looked in the 24 | Not found there, because no run was handed a range. **Untested, and named.** `question_frozen_quote` keeps the range so it can be looked at later |
| `modules_self_reported` marked and not scanned | The scan agreeing with the marker on the record | Ran the scan on all 24 | The scan invents or misses on every one of the four reports where it fires. Decision kept, and the finding handed to the harness |
| Record fields as text, never compared | A prediction that needs them compared | Read W3 P4.1–P4.7 and W8 PA.1, P4.9 | PA.1 and P4.9 are computed from the run records, not from marker fields. Kept |
| `marks_outside_closed_list` outside the certified set | A reading of P4.4 that needs it | Read P4.4 in W3 and W8 B10 | P4.4 is about the within-step *marks*, not about the vocabulary. Kept, and the field kept as a gauge |
| The added 39-of-48 threshold | A field below it that carries real signal in stage C | Cannot be looked for yet | Untested. Named as added, with its falsifier |
| Every criterion tested on two reports | A criterion where the two reports agree for a reason other than the criterion | Chose pairs that straddle a boundary wherever the record afforded one | Three criteria could not be straddled on this record (swap's ABSENT, look inside's RAN, remove-in-groups' RAN) and one could not be tested at all (`ports_set`). All four are named as untested rather than left out |

**Dropped on this pass, and why.** A `breaks` field, because W10 section 11 puts the skill's faults outside this round. A claim-checking field, because no prediction reads it and it is the most expensive thing a marker does. A `verdict` field, because it restates the marks. A plan to compare the range in question-identity, because it would have made arm (f) pass by construction. An intention to fill `modules_self_reported` by program, because the scan was tested and failed.

## 11. What this instrument does not settle

- Which marker is right where two disagree. That needs a third reading, which stage B does not run and stage E only partly supplies.
- Whether a criterion carries to a document of a kind neither P3 nor F4 belongs to. The criteria are fitted to those two and are unconstrained elsewhere until stage B and stage C run.
- Anything about the reader's insides. Every field here is read from the emission, the report or the transport's record; W8 part A7 and file 11's Derivation 9 forbid reading a kind, an organization or a route off any of them.
- Whether the arms differ *because* of what W8 says they differ by. A count falsifies a prediction. It moves no mark on any part of W8 without quoted evidence (W10 section 6).
- The skill's own faults. Held for the HV project.

## 12. Traps this instrument can still fall into

- Summing fields, arms or readers. Nothing here is a total.
- Reading a DeepSeek examiner's disagreement as a verdict.
- Re-sorting a field into the other column after the reports come in. B4 forbids it; the sorting is in section 3 and stays there.
- Marking a report as wrong because its verdict about the document is unwelcome. Plan 52's first trap, kept.
- Letting a full report pass because it is well written. Plan 52's second trap, kept.
- Reading 84 percent, or any percent, as a pass mark. H64's own trap: the disagreements sat on four tests, and those were where the wording was loosest.
- Filling a field with a guess rather than null. A gap is reported as unreadable; a guess is counted as agreement that was never there.
- Reading the two fitting reports named under each criterion as evidence that the criterion is right. They show that a stranger could apply it to those two. Nothing more.

---

## 13. Addendum, 22 September 2026: the fix round, faults 3, 4, 5 and 18

Written in the fix round of plan W10 stage A, under addendum W11, before stage B and before any report of this round exists. It records four changes to the instrument and the fault number that forced each, because the frozen file above says a change is an addendum that names the finding that forced it and says what it gives up, and never a silent edit. Sections 1 to 12 stand as they were written; where this section and an earlier one differ, this section is later and wins, and says so in the line that differs. `criteria.json` carries the same four changes, each with its date and fault number in its own `addenda` block, and its `version` is now `W10-A4-2`, so a mark made under the fixed criteria can be told from one made under `W10-A4-1`. No mark exists under either.

The four faults are the reviewer's, numbered as `stage-A returns/A5-reviewer.json` numbers them. Faults 3, 4 and 5 block stage B; fault 18 blocks stage C and is taken as addendum W11's decision D4.

> **Held open.** The reviewer's second return kept **fault 4** open: the key rule of section 13.2 still gave one key to two different parts in seven of the record's ninety-six reports. **Section 14.1** is the key rule now. He also returned **fault 25**, new, on `rivals_built`'s naming rule of section 13.3; **section 14.2** is that rule now. Sections 13.2 and 13.3 stand as the record of what was fixed and what it cost, and are superseded where 14.1 and 14.2 differ.

Every change below was applied to the one report the reviewer names, `runs_sonnet5/F4-m2-r3.json` of the old rig — a report this instrument did not name before — and the value each fixed criterion now gives there is stated with it. That report is now a third fitting report on three fields. Naming it is not praise of it: it is the report the fault was found on, and a criterion tested on the case that forced it is tested on the case that forced it and nothing else (the qualification of Derivation 3 that section 4 states).

### 13.1 Fault 3 — `test_pull` had no value for a common report shape

**The fault.** RAN required the stronger-weaker clause *and* one of three further things; NAME ONLY required that neither side be named. A report that names both sides and says which gives way, with no stronger-weaker wording, fitted neither, and two markers would have marked it two ways.

**The change.** RAN now has two cases. Case (i) is plan 52's rule unchanged: the report says of two things in the explanation that making one stronger makes the other weaker, and says which gives way, or where the line is, or what would show the line drawn in the wrong place. Case (ii) is new: the report names both sides of a tension between two things in the explanation — two things it presents as pulling against each other, competing, or in tension over one job, and not merely as different — and says which gives way, or where the line is, or what would show the line drawn in the wrong place; the stronger-weaker wording need not appear. A report that says the line is *not* drawn has said where the line is, in the same way that "no gauge is offered" is the patches test run, and for the same reason: reporting that the thing the test asks for is missing is the test run, not the test skipped. NAME ONLY now also covers both sides named with none of the three said. ABSENT is stated: the report names no tension between two things in the explanation. CANNOT keeps file 33's three-part form. So every report shape reaches one of the four values, which is what the fault asked for.

**Why RAN and not NAME ONLY.** The skill's Step 5 asks three things of this test: name each pair that pulls, say which one gives way and where, and say what would show that the line was drawn in the wrong place. The stronger-weaker question is what a pull *is*; it is not a fourth thing the report must say in those words. A report that names the pair and says which gives way has done the two the question bank calls the good answer's first two parts. Marking it NAME ONLY would have put it with a report that asserts a tension and names nobody, which is the shape the mark exists for.

**What it gives up, written here because a patch has a bill.** RAN no longer tells a report that asked the stronger-weaker question from one that reported a contrast with a winner. The difference is still visible in two places and is not lost: `pairs_that_pull` records the pair, and `quotes` keeps the sentence. If stage C's reports turn out to be RAN on this field nearly everywhere, that is the bill for case (ii), and the field's own `(a)`-to-`(a)` baseline plus the uninformative rule is what would show it.

**On the report the reviewer names.** `runs_sonnet5/F4-m2-r3.json` — "**Pairs that pull.** A–C aim at credibility through argument; D and G aim at it through checkable, sensory fact. The text shows which wins: Filby sits through the whole geometry lecture unmoved…, while the room goes quiet only once wounds appear." Under the fixed criterion: **RAN**, by case (ii). Under the criterion as frozen: no value.

**What did not change.** The two reports section 4.1 names as fitting for pull keep the values they were frozen with. `runs_repeat/F4-m1-r1` is RAN by case (i) ("the more the patch covers, the less the vanishing shows"). `runs_sonnet5/F4-m1-r2` is RAN because it says the line is not drawn ("Nothing marks where the vapour regime ends and the solid regime begins"), which is the clause added above; without that clause the fix would have moved a frozen value, and that is the first thing I looked for.

### 13.2 Fault 4 — the part key, and a pull between two groups

**The fault.** `marks_per_part` and `pairs_that_pull` keyed on "the report's own label for the part, copied exactly", and a report commonly labels its parts twice: once in the parts list of Step 3 and again in the part-by-part table. Two markers keying the two lists disagree on every part of the map, and a `map_enum` agrees only when the whole map is equal. The same report's one pull is between two *groups* of parts, which the member format `A|B` admitted neither as a member nor as anything else.

**The change, first half: one key by rule.** Take the part's label from the report's part-by-part section — the table or list that gives each part its mark — where there is one, and otherwise from the parts list. Then normalise: take the characters up to the first space, `(` or `[`; strip from each end of that token every character that is not a letter or a digit; use what is left as the key when it is label-shaped, that is at most two letters followed by at most two digits (`A`, `H`, `P3`, `P10`, `iv`); otherwise use the whole label as the report writes it, trimmed, with the same stripping at each end. A row that covers two parts under one label ("P3, P4 decomposition and ratio") is one entry under that label's normalised key.

Two things in that rule are not the reviewer's words and are here because the reviewer's own example list forced them. The stripping at each end is there because the two lists of the report the fault names are `- **A.** Time is a fourth dimension` and `| A (time = 4th dimension) |`: a rule that only cut at the first space would give `**A.**` from one and `A` from the other, and the fault would survive its own fix. The label-shaped test is there because the third form the fault lists is `Time is a fourth dimension`, whose leading token is `Time`, which is not a label and would collide with any other part whose label begins with that word; for such a label the key stays A4's original rule, the whole label as the report writes it.

**The change, second half: a pull between two groups.** A pull the report names between two groups of its own parts gives **one member per cross pair**, the left of each member taken from the side the report names first. A side written as a range (`A–C`, `P1-P3`, with any dash) means every part of the report's own list from the first named to the last named inclusive, in the order that list runs; a side written as a list ("D and G", "P2, P4") means the parts it names. A side that is not an explicit range or list of the report's own part labels — a description such as "the argument parts" — cannot be expanded: the pull is not a member, the sentence goes in `quotes`, and `test_pull` still records that the test ran.

**Why cross pairs and not "out of the set".** The reviewer allowed either. Out of the set would have made this report's set empty, and an empty set is what a report that names no pull at all returns. That reading merges a report that did the cross-step work with one that did none, and the difference between those two is exactly what P4.2 and P4.3 are read on: a field that cannot tell them apart cannot show arm (c) or arm (d) losing anything. The expansion is mechanical from the report's own parts list, which both markers have in front of them.

**What it gives up.** Two things. The key is no longer the report's own words, so a disagreement about a part can no longer be traced by the key alone; `quotes` keeps the cell. And the set grows with the size of the two groups — six members here — while a set field agrees only when the sets are equal, so one marker misreading one range makes the whole set disagree. The gauge for the second is that `quotes` keeps the sentence, so a disagreement traces to the range and not to the marker's judgement; if `pairs_that_pull` falls below its 40-of-48 threshold in stage B and the disagreements sit on group pulls, that is this patch's bill and section 6's striking rule collects it.

**On the report the reviewer names.** `marks_per_part` now gives `{A: held if, B: loose, C: idle, D: held, E: loose, F: idle, G: held}` — seven parts, seven single marks, E's cell "Loose, ungauged catch-all" and F's "**Idle**, as an explanation of what's actually shown" each carrying one of the eight with words around it. `pairs_that_pull` now gives `["A|D", "A|G", "B|D", "B|G", "C|D", "C|G"]`. Under the frozen criteria the first was two maps, one per list, and the second was undecided.

**What did not change.** The values of the two fitting reports of section 4.3 are the same marks under the same rule; only the keys are normalised (`P1 substrate-independence` → `P1`; `A. Substrate-independence` → `A`). `runs_repeat/F4-m1-r1`'s `["P3|P8"]` is untouched, and "P9 against itself" is still not a member.

### 13.3 Fault 5 — `rivals_built` had no naming rule

**The fault.** The field asked for "the report's own short name" for each rival, and a report that builds a rival properly often gives it none. It is a set needing exact agreement.

**The change.** A member is the report's own short name for the rival where it gives one, lowercased and trimmed, with any quotation marks round it removed and any punctuation at either end of what is left dropped; otherwise the first five words of the sentence that states the rival, lowercased and trimmed, each word as the report writes it, with punctuation at a word's edge dropped. The report gives a short name of its own when the sentence that states the rival carries a phrase that names the rival as a thing — a noun phrase, with no verb of its own inside it — in quotation marks or otherwise set off as the rival's name. A quoted phrase with a verb in it *states* the rival and does not name it, so the five-word rule applies to it.

The verb test is the part that is mine and not the reviewer's, and it is here because without it the rule is not decidable on the very report the fault was found on: that report puts the rival inside quotation marks, so a marker could read the quoted clause as the name and another could read the sentence, which is the disagreement the fault is about. One countable thing decides it: does the quoted phrase carry a verb of its own.

The dropped punctuation is a second patch on this rule, and it was not foreseen: running the rule as first written over the fitting report of section 4.3 returned `some sleight-of-hand trick.`, with the sentence's full stop inside the quotation marks, against the frozen value `some sleight-of-hand trick`. The fix would have moved a frozen value and left two markers two members, which is the fault it was meant to close. It is recorded here rather than tidied away, and it is the one thing the self-falsification pass of section 13.6 caught in this round.

**What it gives up.** A member that reads as a name. "drop the fourth-dimension argument for" is a handle, not a description of the rival, and a reader of the marks file learns nothing from it about what the rival was; `quotes` is where the rival is still readable. And two rivals stated in sentences with the same first five words would collide into one member, which would silently shorten the set; no report in the record does that, and I did not look outside it.

**On the report the reviewer names.** `runs_sonnet5/F4-m2-r3.json` builds one rival: "Drop the Fourth-Dimension argument for a bare "he built a machine, don't ask how" … At the level of *what makes the room believe him*, the two are the same explanation." It is built by the criterion's own test — stated in its own sentence, and the report says plainly that nothing separates the two — and the quoted phrase carries its own verbs, so it names nothing. Under the fixed criterion: **`["drop the fourth-dimension argument for"]`**. Under the criterion as frozen: two markers, two members.

**What did not change.** `runs_sonnet5/F4-m1-r2` keeps `["some sleight-of-hand trick"]`: the quoted phrase is a noun phrase with no verb, so it is a name and the five-word rule does not fire. `runs_repeat/F4-m1-r3` keeps `[]`: it is named and not built, so no member is written and no naming rule applies.

### 13.4 Fault 18, and addendum W11 decision D4 — what the corpus affords, and what P4.2 and P4.3 are read over

**The fault.** The cross-step set was never intersected with what the eight arms documents afford. Three cross-step fields have little or no purchase on the arms, so P4.2 and P4.3 rested on fewer fields than the criteria file implied, and a field that reads the same on every run of every arm cannot show a loss. A2 recorded the gap in `corpus/coverage.md`; it had not reached the instrument that will be read on it.

**The change: a table.** `instrument/affordance.json`, beside this file, names for every cross-step field of `criteria.json` which of the eight arms documents the corpus records as affording it, with one line of reason for every document named. It is built from `corpus/coverage.md` section 3 and from the `exercises` key of each entry of `corpus/sources.json`; the two were read and compared when the table was built, and they give the same eight-document list for all eleven tests, so the table rests on two records that agree and not on one.

| Cross-step field | Arms documents that afford it | From |
|---|---|---|
| `test_flip` | W8, W9, W12, W17 | coverage.md row "Flip the outcome" |
| `test_reverse` | W13 | row "Reverse"; coverage.md section 7 calls it thin, and W13 carries it as a question of law |
| `test_hunt` | W4, W7, W8 | row "Hunt the answer in the starting points" |
| `test_addjob` | W1, W4, W8, W13 | row "Add a job" |
| `test_rival` | W1, W7, W8, W12, W13, W17 | row "Build the best rival" |
| `test_pull` | W12, W13 | row "Pull" |
| `test_patches` | **none** | row "Check the patches"; coverage.md section 7 |
| `test_inside` | W1 | row "Look inside" |
| `pairs_that_pull` | W12, W13 | worked out: the same row as `test_pull` |
| `rivals_built` | W1, W7, W8, W12, W13, W17 | worked out: the same row as `test_rival` |
| `remove_in_groups` | W4, W7, W9, W13 | worked out, coarser: the "Remove" row, the nearest thing the corpus records |
| `turned_own_test` | **not recorded** | no row in coverage.md, no key in sources.json |
| `same_explanation` | W1, W7, W8, W12, W13, W17 | worked out: a verdict needs two candidates, so the rival row |
| `same_explanation_quote` | (follows `same_explanation`) | text; never compared, carries no arm difference |

How I know it, tagged: *worked out*, from A2's marks, which coverage.md section 2 itself tags as worked out and not as a reading of the whole document. Nobody on this round has read the eight documents and no text of them is in this repository. The table says what the corpus records, not what a reader will find.

**The rule this fixes in place.** **P4.2 and P4.3 are read over the cross-step fields that at least one arms document affords.** A field the corpus records as afforded by no arms document is not read: that is `test_patches`, and nothing else. A field the corpus records neither way is read — `turned_own_test` — because "found nowhere means unknown" and an exclusion needs evidence; a gap in A2's record is not a finding about the eight documents. The same sentence is in `criteria.json` under `agreement.cross_step_affordance`.

> **Round 3, fault 28.** The rule above is right and the table did not carry it. Version 1 of `affordance.json` gave `turned_own_test` a row with an empty `affords` list — the shape `test_patches` carries, which means the opposite thing — and `agreement.py` reads the list, so both came out excluded. The table now says the rule in its shape and not only in its prose: a field the corpus records neither way is not named in it at all. **Section 15** is that change. The `turned_own_test` row of the table above stands as the record of what the corpus holds, and has moved in the file to `fields_the_corpus_does_not_record`.

**A fourth ask of the harness**, which extends section 8 above: `agreement.py` must read `instrument/affordance.json`, read P4.2 and P4.3 over the cross-step fields at least one arms document affords, and flag a field that never varies across every run of every arm as "never varies" beside its "uninformative" flag; a field so flagged carries no arm difference. That is the harness half of decision D4 and it is A1's to make, not this file's; until it is made, `agreement.py` builds its cross-step set from `sort` alone and P4.2 and P4.3 can be carried by a field with nothing behind it.

**The known weakness, recorded as decision D4 requires.** Check the patches has no purchase in the arms. The five documents that give it purchase — W2, W11, W14, W16, W19 — are in the reserve or held out. The reserve is for the repeat under a new sorting (W3 section 8) and is not raided to give this field purchase. So this round says nothing about that test through the arms, and the results file must say so. Two thinner cases are recorded beside it and not fixed: `test_reverse` rests on one document of eight and `test_inside` on one, so a loss on either is read against n = 1, not n = 8, and W3's k rule has almost nothing to count.

**What the table does not do.** It does not say a test will pass or fail on a document. It does not reach the within-step fields, which P4.4 and P4.5 are read over unchanged. It does not re-sort anything: W8 part B4 forbids re-sorting a field, and no field moves between the two columns here. And it cannot show that a field with documents beside it will in fact vary — that is what the "never varies" flag is for.

### 13.5 The four patches together: what they cost, and the rewording count

`testing-against-cases.md` asks which layer each patch changed and what it gave up. All four changed the same layer — the instrument, which is the rig and not the thing under test — and none changed a document, a reader or an arm. None was made on a count: no mark exists under either version of the criteria, so nothing here was tuned until it passed. Each was forced by a fault a reviewer found by applying the frozen criterion to a report the instrument did not name, which is the one way a criterion of this kind can be caught out before stage B.

**The rewording count under W3 P3.4**, stated so that it can be collected against: P3.4 allows at most one field a *second* rewording. Before this addendum, A4 had reworded four test criteria (swap, poke, add a job, look inside) and three struck fields (shape, turned own test, same explanation) once each. This addendum is a first rewording for four more fields — `test_pull`, `marks_per_part`, `pairs_that_pull`, `rivals_built` — and touches none of the seven already reworded. So no field has yet been reworded twice, and **any further change to any of those eleven fields in stage B is that field's second rewording and stops the phase.** That makes P3.4 bite harder than it did this morning, not softer, and it is the gauge on this round's own patching.

One count is arguable and is written the stricter way. `rivals_built`'s new rule was corrected once inside this addendum, before it was frozen, when running it on a fitting report returned a member with a full stop on the end (section 13.3). Read as one rewording with a correction inside it, the count above stands. Read strictly, as two, **P3.4's single allowance is now spent on `rivals_built`, and a second rewording of any field at all stops the phase.** Take the stricter reading: it is the one that cannot be used to buy another patch.

**What all four give up together.** Three of the four move a field further from the report's own words — the pull's RAN, the part key, the rival's member — and the report's own words are what made a disagreement traceable. Each keeps a route back: `quotes` for the pull sentence and the rival sentence, and the mark cell for the part. If stage B's disagreements on these four fields turn out to sit on the quoted text rather than on the rule, the patches bought agreement at the price of meaning, and that is what to look for first in the stage B numbers.

### 13.6 Self-falsification of this addendum

Written before the marks exist, in the shape of section 10.

| Fix | What would show it does not fix the fault | What I ran | What I saw |
|---|---|---|---|
| Fault 3, `test_pull` case (ii) | The report the fault names still reaching no value, or reaching two; or a frozen fitting value moving | Applied all four values to `runs_sonnet5/F4-m2-r3.json` by hand, and re-applied the fixed criterion to the two fitting reports of section 4.1 | RAN, by case (ii) alone; ABSENT, NAME ONLY and CANNOT each ruled out by a clause I can point at. `runs_repeat/F4-m1-r1` stays RAN by case (i). `runs_sonnet5/F4-m1-r2` stays RAN **only** because of the "line not drawn" clause — without it the fix moved a frozen value, which is why the clause is in the criterion |
| Fault 4, the key rule | The rule giving two keys for the same part of the report the fault names, or a key colliding with another part's | Applied the rule to both lists of `F4-m2-r3`, to both lists of `runs_sonnet5/P3-m2-r1`, and to the eleven rows of `runs_repeat/P3-m2-r2` | One key per part in all three: `**A.**` and `A (time = 4th dimension)` both give `A`; `A. Substrate-independence (weak form)` and `A. Substrate-independence` both give `A`; the eleven rows give eleven distinct keys, `P3, P4 decomposition and ratio` keying as `P3` and `H, the count of pre-posthuman individuals` as `H`. No collision in any of the three |
| Fault 4, group pulls | The expansion being ambiguous: two markers reading the range or the list two ways | Expanded `A–C` and `D and G` against that report's own parts list | Six members, and the only judgement left is reading a dash as a range, which the criterion names. The alternative reading — groups out of the set — was tried and rejected in writing, because it gives the same empty set as a report that names no pull |
| Fault 5, the naming rule | A member that two markers would still write two ways on the report the fault names, or a frozen value moved | Wrote the rule as a program and ran it on `F4-m2-r3` and on the two fitting reports of section 4.3 | **Caught one.** The rule as first written returned `some sleight-of-hand trick.` on `F4-m1-r2`, against its frozen `some sleight-of-hand trick`: end punctuation was not dropped. The criterion was patched (section 13.3) and the run repeated: `drop the fourth-dimension argument for` and `some sleight-of-hand trick`, both matching. `F4-m1-r3` keeps the empty set |
| Fault 18, the table | The table disagreeing with the corpus it is drawn from, or leaving a cross-step field out | Built the table by reading `coverage.md` section 3 and `sources.json`'s `exercises` in one program and asserting they agree; then compared the table's field list against `criteria.json`'s cross-step set | The eleven rows of coverage.md and the seventeen `exercises` lists agree on all eleven tests for the arms eight. Fourteen cross-step fields in `criteria.json`, fourteen in the table, none missing, none extra |
| The four together | `criteria.json` no longer loading, or a quote no longer verbatim | `python3 -c "import json; json.load(open('criteria.json'))"`; `marks.load` through the harness's own `marks.py`; every `example` and `fitting` value against its closed list; every `quote` against the report it names; `first_marker.py prompts --dry` over the fixed criteria | Loads; 32 fields, 18 within-step, 14 cross-step, 25 comparable; 0 values outside a closed list; 82 quotes verbatim in the report named and 18 carrying `quote_from`, 0 problems; the marking prompt builds and carries the four fixed criteria |

> **What this table missed, found by the reviewer and kept here as it came.** The fault-4 row's falsifier is the right one — "the rule giving ... a key colliding with another part's" — and it was run on three reports, the three the criterion already named. Run over all ninety-six it fires on seven of them. The row is left as it was written; section 14.1 is what running it properly found.

**What I could not settle, and did not patch.** Whether `test_pull`'s case (ii) makes the field RAN nearly everywhere in stage C: it cannot be looked for before the runs, and the field's own baseline is what would show it. Whether two markers agree on a six-member expanded set: stage B is the first test. Whether `turned_own_test` has any purchase at all in the arms: the corpus does not record it, and nobody here has read the eight documents, so it stays unknown and is read.

---

## 14. Addendum, 22 September 2026: round 2 of the fix round, faults 4 and 25

Written in round 2 of the fix round of plan W10 stage A, under addendum W11, before stage B and before any report of this round exists. The reviewer's second return held **fault 4** open — the fix of section 13.2 did not make the part key unique, and the reviewer found that by running the rule as a program over all ninety-six reports of the record rather than over the three A4 had named — and returned **fault 25** new: `rivals_built`'s naming rule, written in section 13.3, is not decidable on reports neither A4 nor the reviewer had named. Both block stage B. Nothing else in the instrument is touched: section 13's other fixes stand, no field changed its sort (W8 part B4 forbids re-sorting), no threshold moved, and no field was added or removed.

Sections 1 to 13 stand as they were written. Where this section and an earlier one differ, this section is later and wins, and the line that differs says so. `criteria.json` carries the same two changes, each in its own `addenda` entry with its date and fault number, and its `version` is now **`W10-A4-3`**, so a mark made under these criteria can be told from one made under `W10-A4-2` or `W10-A4-1`. No mark exists under any of the three.

Both changes were applied to the report the reviewer names for every fix of this round, `runs_sonnet5/F4-m2-r3.json` of the old rig, and to the reports each fault's own evidence names, and the value each fixed criterion gives there is stated below. A criterion tested on the case that forced it is tested on the case that forced it and nothing else; what each fix was tested on beyond that case is stated too, because that is the whole of the reviewer's complaint about round 1.

### 14.1 Fault 4, held open — the key rule still gave one key to two different parts

**The fault, in the reviewer's count.** Of the ninety-six adapted reports, seventy-nine carry a part-by-part table; of those seventy-nine, seven have two or more rows whose labels normalise to the same key under the rule section 13.2 fixed. `marks_per_part` is `map_enum` and agrees only when the whole map is equal, and W3 P3.2 needs 40 of 48, so a report whose map silently loses a part is a report on which two markers cannot agree.

**What I ran before touching anything.** I wrote the round-1 rule as a program, word for word as the criterion words it, and ran it over the same ninety-six (regenerated with `record_adapter.py --out` into a folder outside the repository, because another agent's work had cleared `<rig>/dry/` while I read). It reproduced the reviewer's count exactly: seventy-nine of ninety-six carry a Part/Mark table, seven of the seventy-nine collide, and they are the seven he names, with the same duplicate keys — `rep31_P3-m2-r2` (11 rows → 9 keys, `B` and `E`), `rep_F4-m1-r2` (11 → 9, `a`), `rep_F4-m2-r1` (12 → 11, `I`), `rep_P3-m1-r3` (8 → 7, `P2`), `son31_F4-m1-r1` (10 → 9, `P6`), `son31_F4-m2-r1` (13 → 9, `A`, `B`, `F`, `H`) and `son_P3-m1-r1` (8 → 7, `P1`). The fault is reproduced before it is fixed, so that the fix has something to be measured against.

**The change, clause (1): a token is label-shaped only where it stands as an enumerator.** The label must not begin with a quotation mark of any kind, and what follows the token's last letter or digit inside the label must be at least one character that is not a letter or a digit — the separator — and then at least one more letter or digit — the rest of the label. `P3 the sum`, `**A.** Time is a fourth dimension`, `A (time = 4th dimension)`, `H, exact images` and `iv) the third premise` all key to their enumerator. `"a mathematical line... has no real existence"`, `"I don't, for certain, know which"` and `"To capture these advances… necessitated an update"` do not key to `a`, `I` and `To`; they keep the whole label. A label that is a bare token with nothing after it (`P1`, `A`) is not an enumerator either, and the whole-label rule gives back the same string, so nothing moves there.

**The change, clause (2): the key is unique within one report.** Where two or more rows of the part-by-part section still normalise to the same key, each of those rows — and only those rows — keeps its whole label as the report writes it, trimmed and end-stripped by the same stripping the rule already uses; a row that did not collide keeps its short key. `pairs_that_pull` uses these keys and inherits both clauses, and its criterion now says so: where a colliding row's key is a whole label, the member carries that whole label on that side.

**The one thing here that is mine and not the reviewer's, and the patch it cost.** The reviewer's words are "it is followed in the label by a separator and more text". A marker needs to know what counts as a separator. I first wrote it as a closed list of separator characters — full stop, comma, bracket, colon, dash, bar, space — and ran it: **it reverted 52 of the 750 rows**, including rows nobody would call ambiguous, `P4. “Known integer” means efficiently generatable/provable.` and `P2 +1 segment per ACK` and ``A `cwnd` `` among them, because a curly quotation mark, a plus sign and a backtick were not on the list. That is a closed list that has to be extended on every new report, which `testing-against-cases.md` names as the sign of a rule that is really a list — "If each new kind of case needs a new piece of rig, you have a list, one item per kind". So the separator is now **any run of characters that are not letters or digits**, which needs no list and is decidable by a marker with no program. Run again, it reverts **28 of 750 rows**, and every one of them is either a row in one of the seven colliding reports or one of exactly three quotation-led labels in reports that did not collide (`p52_I2-m2`'s `To`, `rep31_F4-m2-r1`'s `No`, `rep31_P3-m1-r2`'s `We`) — which is what clause (1)'s quotation-mark half exists for. This patch is recorded rather than tidied away: it was found by running, and the first form of the rule would have made the instrument worse on 24 rows that were never in doubt.

**What it gives up, written here because a patch has a bill.** Two things, and both are new costs of round 2.

- **A report's map now mixes two shapes of key.** On the seven reports where keys collided, the colliding rows carry long keys (`A, "jargon + named pushback`, `B′. The exact figures (10⁴², 10³³⁻³⁶ ops`) while their neighbours carry short ones (`C`, `D`, `E`, `G`, `I`). A marker must therefore read the whole part-by-part section before writing any key, and cannot write the map row by row.
- **A row's key now depends on the other rows.** Clause (2) makes one row's key a function of which other rows the marker read as belonging to the part-by-part section. Two markers who disagree about whether a summary row or a jobs row belongs to that section can now disagree about the key of a row neither of them disputes. The gauge is `quotes`, which keeps the cell: a disagreement of that kind traces to the section boundary and not to the mark. If `marks_per_part` falls below 40 of 48 in stage B and the disagreements sit on reports whose keys collide, that is this patch's bill and section 6's striking rule collects it.

**On the report the reviewer names.** `runs_sonnet5/F4-m2-r3.json`: its part-by-part rows are `A (time = 4th dimension)` through `G (bodily evidence on return)`, every one an enumerator, none colliding. `marks_per_part` gives **`{A: held if, B: loose, C: idle, D: held, E: loose, F: idle, G: held}`** and `pairs_that_pull` gives **`["A|D", "A|G", "B|D", "B|G", "C|D", "C|G"]`** — both unchanged from section 13.2, which is what a fix that reaches only the fault should do to a report the fault does not reach.

**On the report the fault was found on.** `runs_sonnet5_31/F4-m2-r1.json`, added to `criteria.json` as a fourth fitting report for `marks_per_part`: thirteen rows, nine keys under the round-1 rule, **thirteen keys now**. The four colliding pairs keep their whole labels — `A, specific 4-D content` (loose) beside `A, "jargon + named pushback` (held), `B, four *distinct* objections` (held) beside `B, Filby's red hair` (idle), `F, specific injuries (dirt, cut chin, torn socks` (loose) beside `F, visible bodily cost, independent of his say-so` (held), `H, exact images (rhododendrons, hail colour` (loose) beside `H, continuous escalating sensation` (held) — and the five rows that never collided keep `C`, `D`, `E`, `G`, `I`.

**What did not change.** The three fitting values of section 4.3 and 13.2 are untouched: `runs_repeat/P3-m2-r2` still gives `P1`, `P7`, `P10` (and eleven distinct keys in all), `runs_sonnet5/P3-m2-r1` still gives `A` and `C`, `runs_repeat/F4-m1-r1` still gives the nine bare keys `P1` to `P9` and its `pairs_that_pull` is still `["P3|P8"]`. Of the 750 rows in the seventy-nine part-by-part tables, 722 keep exactly the key the round-1 rule gave them.

### 14.2 Fault 25 — `rivals_built`'s naming rule was not decidable on a report neither of us had named

**The fault.** Section 13.3's rule says the member is "the report's own short name ... otherwise the first five words of the sentence that states the rival". Applied cold to four reports of the record neither A4 nor the reviewer had named, three things in it were undecided: where the sentence starts, when the report leads the passage with a bold tag (`- **Rival.**`, `**Rival explanation.**`); which sentence counts, when the rival is first put in a part-by-part cell; and what to do when one sentence states two rivals. `rivals_built` is a set and needs 40 of 48 in stage B.

**The change, three clauses.**

1. **Where the sentence starts.** A lead-in that names the test is not part of the sentence: any list marker, then any run set in bold, italics, brackets or parentheses whose text carries the word "rival" or "rivals", together with the punctuation and space that close it. The sentence's first word is the first word after that run.
2. **Which sentence.** "The first sentence in which the rival is put" is the first sentence of the report's own whole-explanation section — the section that runs file 33's whole-explanation checks — that states that rival. A mention in a part-by-part cell is not it: the cell goes in `quotes`, and a rival the report states only in a part-by-part cell and nowhere in the whole-explanation section is not a member.
3. **Two rivals in one sentence.** Each takes the report's own noun phrase for it as its name, written by the naming rule, whether or not that phrase is quoted or set off. Where the sentence gives no noun phrase for them, **the field is null for that report** and the sentence goes in `quotes`, rather than two rivals collapsing into one five-word member.

**What is mine and not the reviewer's.** Two things, both named in the criterion itself. The **decidable form of the lead-in** (a list marker, then an emphasised or bracketed run whose text carries "rival"), because "a bold or bracketed lead-in that names the test" has to be something a marker can point at; a run that does not carry the word is not a lead-in, so `- **Add a job.**` is left alone even where a rival is stated later in that bullet. And a **fallback for a report with no whole-explanation section**: the first sentence of the report outside the part-by-part section that states the rival. Without it clause (2) leaves such a report with no sentence at all, which is the same kind of hole fault 3 closed in `test_pull`.

**The four cold reports, marked cold under the fixed rule.** These are the four the reviewer applied the round-1 rule to; they are the test of the fix, not of the reports.

| Report | Under the round-1 rule | Under the fixed rule | Which clause did it |
|---|---|---|---|
| `runs/F4-m2.json` | `it was a trick answers`, or `rival`, or `the medical man names the` (from the P8 cell), or `nothing on the change list` | **`["it was a trick answers"]`** | (1) drops `- **Rival.**`; (2) makes the P8 cell `the Medical Man names the rival ("like that ghost you showed us last Christmas")` a quote and not the sentence |
| `runs/C5-m1.json` | one member, `benioff's machine and feynman's simulator`, or two names — the marker's choice | **`["benioff's machine", "feynman's simulator"]`** | (3): one sentence, two rivals, the report's own noun phrase for each |
| `runs/R2-m2.json` | one member `the dissent and phelps`, or two, with only `*Phelps*` set off | **`["the dissent", "phelps"]`** | (3), which does not ask whether a noun phrase is italicised |
| `runs/I1-m1.json` | `best rival`, or `the fix is editorial enforcement` | **`["that job kills the rival"]`**, with the best-rival sentence in `quotes` | (1) drops `- **Best rival.**`; the best-rival sentence is *named and not built* by the criterion's own built test, because the report says only that the document "never tests the two against each other", which is not a change named and is not "no change can"; the add-a-job line's rival is built, because the added job is the change that rules it out |

`runs/C5-m1.json` and `runs/F4-m2.json` are added to `criteria.json` as fitting reports, because they are the cases that forced clauses (3) and (2) and a criterion with no case for a clause has not been tested on it. `runs/R2-m2.json` and `runs/I1-m1.json` are recorded here and not in the file: the first repeats clause (3) and the second turns on the built test, which no fault of this round changed.

**What it gives up.** Three things.

- **A report that builds two rivals and names neither now makes the whole field null**, not one member. A null is reported unreadable and never as agreement, so such a report subtracts a document from `rivals_built`'s denominator in stage B rather than adding a wrong member. That is the trade the reviewer's clause (3) asks for, and it is the right way round — but if `rivals_built` comes back with a small readable count in stage B, this clause is the first place to look.
- **The whole-explanation section must be found before the field can be filled.** On a report that does not use file 33's report shape that is a judgement, and the fallback in clause (2) is where it lands.
- **A member can now come from a sentence that is not the report's rival bullet**, as `runs/I1-m1.json` shows: `that job kills the rival` is a handle and tells a reader of the marks file nothing about the rival. `quotes` is where the rival stays readable, as in section 13.3.

**On the report the reviewer names.** `runs_sonnet5/F4-m2-r3.json` keeps **`["drop the fourth-dimension argument for"]`**, the value section 13.3 froze — and it is now reached by a rule rather than by a judgement: clause (1) drops `**Rival explanation.**`, so the five words are counted from `Drop`, and a marker who counted the lead-in would have written `rival explanation drop the fourth-dimension`, which is exactly the disagreement the fault names. Clause (2) also settles this report's second candidate: the part-by-part cell for `A` states another rival, "some other force removes things from the present", and the cell goes in `quotes` rather than into the set.

**What did not change.** `runs_sonnet5/F4-m1-r2.json` keeps `["some sleight-of-hand trick"]` — the lead-in `- **Rivals.**` is dropped, the member comes from the quoted noun phrase and not from the five-word rule, and the "trickery" mentions in its part-by-part rows are quotes and not the sentence. `runs_repeat/F4-m1-r3.json` keeps `[]`: the lead-in `- **Rivals:**` is dropped, and the rival is still named and not built.

### 14.3 Decision D4, the instrument side, as it stands after round 2

D4 is unchanged by this round and nothing in it was reopened. It was made in round 1 (section 13.4) and the reviewer verified it by rebuilding the table himself. As it stands: `instrument/affordance.json` names, for each of `criteria.json`'s fourteen cross-step fields, which of the eight arms documents `corpus/coverage.md` and `corpus/sources.json` record as affording it, with a line of reason for every document named; **P4.2 and P4.3 are read over the cross-step fields that at least one arms document affords**, the same sentence standing in `criteria.json` under `agreement.cross_step_affordance`; `test_patches` is afforded by no arms document and is not read, and the known weakness is recorded — the five documents that give it purchase are in the reserve or held out, and the reserve is not raided. Re-checked by running, after this round's edits: fourteen cross-step fields in `criteria.json`, fourteen rows in the table, none missing and none extra, read by the harness's own `marks.affordance` from `<rig>/instrument/affordance.json`.

> **Round 3, fault 28.** That last check — fourteen fields, fourteen rows, none missing — is the check that let the fault through: it counts rows and cannot tell an exclusion from a gap in the corpus's record. The table now has thirteen rows and `turned_own_test` stands under `fields_the_corpus_does_not_record`; the check that replaces the row count is in **section 15.3**.

### 14.4 The rewording count under W3 P3.4 — a count that has now gone past its allowance

Section 13.5 wrote the count so that it could be collected against, and it is collected here.

Before this round: four test criteria and three struck fields reworded once each, and four more fields — `test_pull`, `marks_per_part`, `pairs_that_pull`, `rivals_built` — reworded once in section 13. Section 13.5 read `rivals_built`'s in-addendum correction the stricter of two ways, as a second rewording, and wrote: "P3.4's single allowance is now spent on `rivals_built`, and a second rewording of any field at all stops the phase."

**This round reworded three of those fields again**: `marks_per_part` and `pairs_that_pull` (fault 4) and `rivals_built` (fault 25). So the count is: `marks_per_part` twice, `pairs_that_pull` twice, `rivals_built` twice, or three times on section 13.5's stricter reading. **W3 P3.4 allows at most one field a second rewording. Three fields have now had one, and on the stricter reading one of them a third.** On the count as W3 writes it, P3.4 is falsified if it is read from A4's first draft.

I am not going to write a reading of P3.4 that makes this go away, because that is what the prediction is a gauge against. Two things are true and both are reported, and which of them governs is the plan owner's to say, not the instrument's:

- **The count has failed.** Read from A4's first draft, three fields have been reworded a second time and P3.4's falsifier has fired. If that is the reading, stage B does not start under this instrument, and W3 P3.4's own instruction applies: "the phase stops and reports the patches with what each gave up" — which sections 13 and 14 do, patch by patch.
- **What P3.4 is a gauge for has not happened.** Its falsifier is a count, but the thing it is a count of is the criteria "being tuned until they pass", which `testing-against-cases.md` forbids. Nothing here was tuned on a result: no mark exists under any version of the criteria, stage B has not run, and every change was forced by a reviewer who found the fault by running the frozen rule over reports the instrument had not named. That is the opposite of tuning until it passes — it is the rig being frozen after one case and then run against the others, which is what `testing-against-cases.md` asks for.

The strict rule this leaves in place, and it is stricter than section 13.5's: **from the moment stage B begins, any change to any field of this instrument stops the phase.** No further change is bought by anything written above.

### 14.5 Self-falsification of this addendum

Written before the runs, in the shape of sections 10 and 13.6. Everything in the last column was seen by running, not by reading.

| Fix | What would show it does not fix the fault | What I ran | What I saw |
|---|---|---|---|
| Fault 4, clause (1) and clause (2) | A key still colliding with another part's anywhere in the ninety-six — the same falsifier A4 wrote in round 1 and did not run past three reports | Wrote both rules as programs and ran them over all ninety-six adapted reports: the round-1 rule and the fixed rule, side by side | Round-1 rule: seventy-nine reports with a part-by-part table, **seven with colliding keys**, the reviewer's seven exactly, with his duplicate keys exactly. Fixed rule: **0 of 79** |
| Fault 4, the innocent neighbour | The fix firing on rows that were never in doubt, which would buy uniqueness by making every key a sentence | Counted, row by row, every key the fix changes, over all 750 rows of the seventy-nine tables | **Caught one, and it changed the rule.** With "separator" written as a closed list of characters, 52 of 750 rows reverted, including `P4. “Known integer” …` and `P2 +1 segment per ACK`. With "separator" written as any run of non-letters-and-digits, **28 of 750**, all of them either in the seven colliding reports or one of three quotation-led labels. The first form is recorded in 14.1 and not tidied away |
| Fault 4, the frozen values | A fitting value of section 4.3 or 13.2 moving | Re-derived the keys of `runs_repeat/P3-m2-r2`, `runs_sonnet5/P3-m2-r1`, `runs_sonnet5/F4-m2-r3` and `runs_repeat/F4-m1-r1` under the fixed rule | All four unchanged: eleven distinct keys, six distinct keys, `A` to `G`, and `P1` to `P9` with `pairs_that_pull` still `["P3|P8"]` |
| Fault 25, clause (1) | The member on the report the reviewer names changing, or a marker who read the lead-in still getting a second answer | Wrote the lead-in rule as a program and ran it on the seven rival passages named in 13.3 and 14.2 | `**Rival explanation.**`, `- **Rival.**`, `- **Rivals.**`, `- **Rivals:**` and `- **Best rival.**` are all dropped; `- **Add a job.**` is not. The member on `F4-m2-r3` is `drop the fourth-dimension argument for`, the frozen value; counting the lead-in would have given `rival explanation`, which is the fault |
| Fault 25, clauses (2) and (3) | A cold report still admitting two members | Applied the three clauses cold to the four reports the reviewer names, and computed the alternatives a marker could have written under the round-1 rule | One value each, given in the table in 14.2. The one judgement the fix does **not** remove is on `runs/I1-m1.json`, and it is the *built* test, not the naming rule: whether "It never tests the two against each other" is "no change can". That is fault 5's clause, which no fault of this round reopened, and it is recorded in 14.6 rather than patched |
| Both, together | `criteria.json` no longer loading, a quote no longer verbatim, a value outside a closed list, a field re-sorted, or the marking prompt no longer building | `python3 -c "import json; json.load(open('criteria.json'))"`; `marks.load` through the harness's own `marks.py`; every `example` and `fitting` quote against the report it names; every value against its closed list; `first_marker.py prompts --dry --criteria ../instrument/criteria.json`; `marks.affordance` against the cross-step set | Loads. `W10-A4-3`, 32 fields, 18 within-step, 14 cross-step, 25 comparable, 22 certified and comparable — every count the same as under `W10-A4-2`, so nothing was re-sorted. 85 quotes verbatim in the report named and 18 carrying `quote_from`, 0 problems. 0 values outside a closed list. The marking prompt builds, 6,138 words, and carries both fixed criteria in full. Fourteen cross-step fields, fourteen rows in the affordance table, none missing, none extra |

> **Round 3, fault 28.** The last cell of the table above — "Fourteen cross-step fields, fourteen rows in the affordance table, none missing, none extra" — is what was seen and is kept as it came. It is also the check that let fault 28 through: a row count cannot tell an exclusion from a gap in the corpus's record, because version 1 wrote both with an empty `affords` list. Section 15.3 is the check that replaces it.

### 14.6 What I could not settle, and did not patch

- **Whether two markers agree on a thirteen-key map with four long keys in it.** Stage B is the first test, and `marks_per_part`'s 40-of-48 threshold is where it shows.
- **Whether `runs/I1-m1.json`'s best-rival sentence is built.** The undecided thing is the *built* test of section 13.3 — "names a change that would tell it from the explanation under test or says plainly that no change on the change list can" — applied to a report that says the document never ran the comparison. No fault of this round names it; it is one case in ninety-six; and reopening the built test would be a third rewording of `rivals_built` bought by nothing. It is written here so the count in 14.4 is not the only record of it.
- **Whether the harness reads `turned_own_test` as the instrument says it should.** Section 13.4 and `affordance.json` both say a field the corpus records neither way is **read**, not excluded — "found nowhere means unknown". `affordance.json` carries that distinction in its `status` line ("NOT RECORDED by the corpus: unknown, and read") but gives the same empty `affords` list to `test_patches`, which the corpus records as afforded by nothing. `agreement.py` reads only the list, so it leaves both out. Seen by reading `agreement.py`'s own line (`afforded = ... bool(aff[f["name"]])`) and by the reviewer's own verified run, which reported both fields "left out ... no arms document affords it". This is a seam between the instrument's table and the harness's reader, not a fault either of us was given: no numbered fault names it, the reviewer verified fault 18 fixed on the table as it stands, and narrowing the table now would undo what he checked. What would settle it on the instrument side: a shape that tells "none" from "not recorded". What would settle it on the harness side: reading `status`, or treating a row with an empty `affords` and a `not recorded` basis as a field the table does not name. Its cost if nothing is done: P4.2 and P4.3 are read over twelve certified cross-step fields rather than thirteen, and the results file should say so.

  > **Settled in round 3: the reviewer returned this as fault 28 and forced one of the two moves named just above. The move made was the first, on the instrument side — the table stops naming such a field. Section 15.** Reading it out by running, rather than by eye: eleven certified cross-step fields were read before the fix and twelve after, because `same_explanation_quote` is `text` and is never compared, so thirteen of the fourteen cross-step fields carry a count at all.

---

## 15. Addendum, 22 September 2026: round 3 of the fix round, fault 28

Written in round 3 of the fix round of plan W10 stage A, under addendum W11, before stage B and before any report of this round exists. The reviewer's third return holds one fault against this instrument, **fault 28**, which blocks stage C: `affordance.json` said in its prose that a cross-step field the corpus records neither way is read, and said in its shape that it is excluded, and the harness reads the shape. Nothing else in the instrument is touched: no criterion changed, no field changed its sort (W8 part B4 forbids re-sorting), no threshold moved, no field was added or removed, and `criteria.json`'s `fields` array is byte-identical to `W10-A4-3`'s.

Sections 1 to 14 stand as they were written. Where this section and an earlier one differ, this section is later and wins, and the line that differs says so. `criteria.json` carries this change in its own `addenda` entry with the date and the fault number, and its `version` is now **`W10-A4-4`**, so a mark made under it can be told from one made under `W10-A4-3`, `W10-A4-2` or `W10-A4-1`. No mark exists under any of the four.

### 15.1 Fault 28 — the table said "unknown, and read" in its prose and "excluded" in its shape

**The fault, in the reviewer's own evidence.** `affordance.json`'s `turned_own_test` row read `"affords": [], "count": 0, "status": "NOT RECORDED by the corpus: unknown, and read"`. Its `test_patches` row read the same empty list with `"status": "afforded by NO arms document"`. `agreement.py` decides by the list alone — `afforded = bool(aff[name])` where the name is in the table — so both came out `False`, and P4.2 and P4.3 printed `cross_step_fields_left_out {"test_patches": "no arms document affords it", "turned_own_test": "no arms document affords it"}`. One shape was carrying two meanings, and the meaning the harness took was the one this instrument's own words deny. Section 14.6 of this file had already found the seam and left it, because no fault named it and the reviewer had verified fault 18 on the table as it stood; fault 28 is the reviewer returning it as a fault, which is what settles who fixes it.

**Why it matters, said as a count.** An exclusion is a claim about the corpus, and the skill's rule is that an exclusion needs evidence: "'Found nowhere' means unknown. It shows neither 'unneeded' nor 'impossible'." With `turned_own_test` excluded, P4.2 and P4.3 were read over **eleven** certified cross-step fields where the instrument's words say twelve, and the results file would have reported an exclusion on the corpus's authority that the corpus never made. (The reviewer writes the pair as twelve and thirteen; running it gives eleven and twelve, because `same_explanation_quote` is `text` and is never compared, so thirteen of the fourteen cross-step fields carry a count at all and `test_patches` is rightly one of the two left out.)

**The change, made in the shape and not in the prose.** `affordance.json` now keeps two lists, and the difference between them is the difference the fault named:

| In the file | What it means | Which fields | What the harness does with it |
|---|---|---|---|
| `fields`, row with a non-empty `affords` list | the corpus records these arms documents as affording the field | the other twelve cross-step fields | read in P4.2 and P4.3 |
| `fields`, row with an empty `affords` list | the corpus records that **no** arms document affords it — an exclusion, with `coverage.md` section 7 quoted behind it | `test_patches`, and nothing else | left out of P4.2 and P4.3, and the counts file says why |
| `fields_the_corpus_does_not_record`, no `affords` key at all | the corpus says **neither yes nor no** | `turned_own_test` | not named in the table, so read — the harness's standing rule, `code/README.md` and `code/CRITERIA-SCHEMA.md`: "A field the table does not name is read, not excluded" |

**Which of fault 28's two moves was made, and why this one.** The reviewer allowed either: `agreement.py` could read the row's `status` or `basis`, or the table could stop naming such a field. The table was changed and `agreement.py` was not. The reason is the fault itself: a reader rule that parses a prose status leaves the ambiguous shape standing and holds the fix by a form of words, so rewording the status to a near neighbour — "the corpus is silent about this one" — would bring the exclusion back, which is fault 28 again. The shape is held by the data instead: an exclusion needs a row, and there is no row. Both halves of that were run, not argued: see 15.3, rows F-D and F-E.

**What the counts file now says.** Fault 28 also requires the counts file to say which move was made. `affordance.json` carries one sentence, `note_to_the_counts_file`, and `marks.affordance` gained four lines that append it to the string the counts file already prints as `corpus_affordance_from` — at the head of the counts file and inside P4.2's and P4.3's own blocks, which is where the exclusions are reported. Those four lines carry no decision: no count, no exclusion and no field list depends on the note, and a table without one (A1's dry-run fixture) reads exactly as before. `agreement.py` is untouched. This is the one place where this round's work reaches outside `instrument/`, and it is named here because the counts file is not the instrument's to write.

**The report the reviewer names.** Applied to `runs_sonnet5/F4-m2-r3.json` of the old rig, the report every fix of this round is applied to, `turned_own_test` is **N** — the same value it had before this round, because no criterion changed. The route by rule: clause (i) can be granted (the document's excerpt does carry a gauge aimed elsewhere, the Psychologist's spinning spoke and flying bullet, which is what made `runs_repeat/F4-m1-r1` a Y), but clause (ii) fails — this report never applies it. It names part E, the "presentation below the threshold", as a "**Loose, ungauged catch-all**", says of it "The method calls for a gauge on any catch-all; none is given", and in section 5 asks for one the document does not contain: "Give E a gauge: some in-story test (someone tries to touch the blurring machine and fails in a specific, checkable way) rather than taking the Psychologist's word for it." A gauge the report asks for is not a test of the document turned back on the explanation, so (ii) and (iii) both fall and the value is N. The words "spoke" and "bullet" appear nowhere in the report. **What moved for this field is not its value but whether it is read:** under `W10-A4-3` it was left out of P4.2 and P4.3, and under `W10-A4-4` it is read.

**The rewording count (W3 P3.4) does not move.** P3.4 counts rewordings of a field's criterion. No criterion was reworded this round: `turned_own_test`'s words are what `W10-A4-1` froze. Section 14.4's count stands exactly as it was written, and so does the stricter rule it left in place: from the moment stage B begins, any change to any field of this instrument stops the phase.

### 15.2 What P4.2 and P4.3 are read over after this round

Read over, twelve certified comparable cross-step fields: `test_flip`, `test_reverse`, `test_hunt`, `test_addjob`, `test_rival`, `test_pull`, `test_inside`, `pairs_that_pull`, `rivals_built`, `remove_in_groups`, `same_explanation`, `turned_own_test`.

Left out, one, with the corpus's own evidence behind it: `test_patches`. The known weakness stands as decision D4 requires — the five documents that give that test purchase (W2, W11, W14, W16, W19) are in the reserve or held out, the reserve is not raided, and the results file says so.

Carrying no count at all: `same_explanation_quote`, kind `text`, never compared, kept so a disagreement can be traced.

And the gauge on all twelve is unchanged: a field that takes one value on every run of every arm is flagged "never varies" and carries no arm difference. That is what reading `turned_own_test` costs if the corpus turns out to afford it nothing — the field shows itself empty and is dropped by the flag, on evidence from the runs, rather than being dropped beforehand on evidence nobody has.

### 15.3 Self-falsification of this addendum

Every falsifier was written before it was run, in the shape of sections 10, 13.6 and 14.5. Everything in the last column was seen by running. The programs are in the session scratchpad outside the repository (`a4r3/affcheck.py`, `a4r3/falsify28.py`); the marks they run on are synthetic — eight documents, four arms, three repeats, values made up so that every field is readable — because no mark of this round exists, and they are used only to make the field lists computable.

| What would show the fix does not fix the fault | What I ran | What I saw |
|---|---|---|
| **F-A.** `turned_own_test` still excluded under the fixed table | `agreement.run_agreement` with the real `criteria.json` and the fixed `affordance.json` | `afforded=None`, `in_the_affordance_table=False`; `cross_step_fields_read` 12, including `turned_own_test`; `cross_step_fields_left_out {"test_patches": "no arms document affords it"}` |
| **F-B.** Something other than this change moved it | Put round 2's table back (a copy in the scratchpad) and ran the same gauge | 11 read; `turned_own_test` left out with "no arms document affords it" — the fault, reproduced, and the table is what moved it |
| **F-C.** The fix threw the real exclusion away with the false one | The same run, read on `test_patches` | Still `afforded=False`, still left out, with its reason — the exclusion the corpus records survives |
| **F-D.** The fix is held by a form of words, which is what it was chosen to avoid | Reworded every prose line of the retired row to a near neighbour ("the corpus is silent about this one", "no row anywhere", "nothing recorded either way") and deleted the note to the counts file | Unmoved: 12 read, `turned_own_test` among them. The reading does not rest on any sentence of the file. This is the row the harness-side move would have failed |
| **F-E.** The shape is not what holds it | Put `"affords": []` and `"count": 0` back on the retired row, keeping every word of its prose | Excluded again: 11 read, `turned_own_test` left out. So the shape, and nothing else, is what the harness reads |
| **F-F.** The table quietly lost a field | Checked every cross-step field of `criteria.json` against both lists | 14 cross-step fields; 13 in `fields`, 1 in `fields_the_corpus_does_not_record`, 0 in both, 0 in neither, 0 in the file that are not cross-step fields, 0 rows outside `fields` carrying an `affords` key. **This is the check that replaces "fourteen rows, none missing"** |
| **F-G.** The note to the counts file breaks a table that has none | `marks.affordance` on A1's dry-run fixture, which carries a table and no note | 4 rows, `where` = "the criteria file's `corpus_affordance` key", nothing appended, nothing raised |
| **Anything else in the instrument moved** | `json.load` on `criteria.json`; `marks.load`; the `fields` array compared object by object against the copy of `W10-A4-3`; `first_marker.py prompts --dry --criteria ../instrument/criteria.json`; `agreement.py --dry`; `python3 -m py_compile marks.py` | Loads. 32 fields, 18 within-step, 14 cross-step, 25 comparable, 22 certified and comparable — every count as under `W10-A4-3`. `fields` identical object for object, so no criterion, value, quote or sort moved and no quote sweep can have changed. The marking prompt builds. `agreement.py --dry` runs end to end. `marks.py` compiles |

### 15.4 What this does not settle, and what it gives up

- **What it gives up.** The table no longer has a row for every cross-step field, so a later editor who deletes a row by accident makes that field *read* rather than making the harness complain. F-F is the gauge against that, and it is written here as the check that replaces the row count: every cross-step field of `criteria.json` stands in exactly one of the two lists, and the only field outside `fields` is one the corpus records neither way.
- **Whether `turned_own_test` has any purchase in the arms.** Unchanged and still unknown: the corpus records it neither way, nobody on this round has read the eight documents, and no text of them is in this repository. Reading the field is not a claim that it will vary; the "never varies" flag is what would show it carried nothing.
- **A1's dry-run fixture.** `code/fixtures/criteria.example.json` gives its own stand-in table `"turned_own_test": []`, so `agreement.py --dry` prints that field as excluded. That fixture is A1's, is a stand-in for this table and not this table, and no fault names it; it is named here so that a reader of the dry run is not misled into thinking the instrument still excludes the field.
- **Who else reads the table.** Nothing but `marks.affordance` (grep over `code/`). So the shape change reaches P4.2 and P4.3 and nothing else.
