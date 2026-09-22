# W10 marking plan — the instrument, frozen before any report is read

Written 22 September 2026 by A4 of stage A, plan W10, before any run of this round exists and before any report of this round is read. The machine-readable form is `criteria.json` beside this file; where the two differ, this file is the instrument and the JSON is wrong. Once stage B starts this file stays as it is; a change is an addendum that names the finding that forced it and says what it gives up.

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

Three things, small, and the second is shown to bite.

1. `first_marker.py` builds its marking prompt from every field in the criteria. The four fields whose source is the run record (`modules_served`, `requests`, `request_text_saved`, `ports_set`) must be left out of the prompt and filled at collect from the run record; otherwise every marker returns null on them and four fields are unreadable on every report. Confirmed by building a prompt from these criteria in memory: it asks the marker for all four, and `modules_served` is the one P4.6 is read on.
2. `agreement.py` reads P4.1 to P4.5 over every comparable field. It must read them over fields with `certified_candidate: true` only. Shown: in a dry run where arm (e) moved nothing but `modules_served`, P4.4 came out `holds=True` carried by `modules_served` alone — a read-out with no marker in it passing the emission-port prediction.
3. `first_marker.py validate` should check two things this file fixes and the code cannot know: that `shape` follows from `shape_elements` by the rule in section 4.2, and that every key of `marks_per_part` appears in the report.

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
