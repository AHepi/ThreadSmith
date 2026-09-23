# SECOND MARKING - Arm B (plan L82, fourteenth version)

Marker: second marker, independent. Marked by hand against the plan's own words (its
expectations table, its "The marking rule, and where it lives" section, and its "The probes'
exposure, beside the rows it touches" section), on evidence quoted from the files.

**Plan hash confirmed.** `sha256sum` of
`Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, fourteenth version.md`
returns `8c1b4473fb5284b4a8a0291bc27adefa2e70be17b9e1832e981e7e35e5372989` — the first sixteen
hex digits are `8c1b4473fb5284b4` as the brief requires. Nothing in the repository was edited and
no writing git command was run.

**What I read.** The plan whole; `Language/results/L82 Arm B outputs.run.log`; every file under
`Language/results/L82 Arm B outputs/` that a row turns on (32 validation files, `ledgers/COUNTS.txt`,
the 32 built `.pl`/`.json` ledgers where a cell needed them, all 64 driver reports, all 32 sameness
files, all 64 reader answers by `reader/KEY_report_names.json`, all 32 prose-reader answers, the
translation receipts, `MANIFEST.json`); and the sixteen passage files in
`Language/results/L82 Corpus - sixteen reported arguments/`. I did not open `MAP.enc` or `MAP2.enc`.
`Language/tools/L82_mark_aid.py` was run once as a reading aid; every mark below rests on the
underlying file, quoted.

---

## B1 — the F-sides, inside the world

**Mark: MET. Charge: nothing fires** (the row charges "the rig (driver); the translation or the
guide for the listed ledgers"; no limb fired).

The row expects, on each F-side ledger whose claim sits in a told world in a form the guide names:
"B03 a JUMP on the because line; B08 a NO CONNECTION on the since line; B09 CANNOT TELL on the plan
line; B05 YOU CLAIM AND DENY THE SAME CAUSE naming the claim and the denial (and a JUMP on the
claim). Expected on every such ledger: 8 of 8 if all eight are markable."

All eight are markable: B5 lists no ledger (see B5 below), and every one of the eight puts its claim
in a told world (`ledgers/COUNTS.txt`).

**8 of 8 came as stated.**

B03 — a JUMP on the because line, in the world, on both:

- `reports/ledger_B03_atria.new.txt`:
  `INSIDE 'log_world' (a told world, looked at alone): no contradiction.` /
  `  BECAUSE-claim on line because2 [said, sentence 2]: "[TOLD in world log_world] line cross BECAUSE line turn".` /
  `  JUMP. Even granting the stated cause, nothing in the ledger produces crossed(trawler,bar).`
- `reports/ledger_B03_mimo.new.txt`:
  `  BECAUSE-claim on line cause1 [said, sentence 2]: "[TOLD in world log_world] line cross1 BECAUSE line turned1".` /
  `  JUMP. Even granting the stated cause, nothing in the ledger produces crosses(trawler,bar).`

B08 — a NO CONNECTION on the since line, in the world, on both:

- `reports/ledger_B08_atria.new.txt`:
  `  SINCE-claim on line since1 [said, sentence 2]: "[TOLD in world note_world] line flock_in SINCE line gate_open". (A reason to expect, not a cause.)` /
  `  NO CONNECTION. Nothing in the ledger leads from the reason to what is expected.`
- `reports/ledger_B08_mimo.new.txt`:
  `  SINCE-claim on line since1 [said, sentence 2]: "[TOLD in world shepherd_world] line flock_top SINCE line gate_open". (A reason to expect, not a cause.)` /
  `  NO CONNECTION. Nothing in the ledger leads from the reason to what is expected.`

B09 — CANNOT TELL on the plan line, in the world, on both:

- `reports/ledger_B09_atria.new.txt`:
  `  PLAN on line w9 [said, sentence 2]: "[TOLD in world notes_world] PLAN: sister moves the patient toward the desk SO THAT the patient's breathing is easier to monitor".` /
  `  CANNOT TELL whether the plan can work. The ledger says nothing about what the action changes.`
- `reports/ledger_B09_mimo.new.txt`:
  `  PLAN on line pl [said, sentence 2]: "[TOLD in world notes_world] Do move(sister, patient toward desk) SO THAT [goal: line mg]".` /
  `  CANNOT TELL whether the plan can work. ...`

B05 — the CLAIM AND DENY sentence naming both lines, and a JUMP on the claim, on both:

- `reports/ledger_B05_atria.new.txt` (inside `'meeting'`):
  `  BECAUSE-claim on line mbecause [said, sentence 2] ...` / `  JUMP. ...` /
  `  DENIED BECAUSE on line mdenied [said, sentence 4] ...` / `  Fine. ...` /
  `  YOU CLAIM AND DENY THE SAME CAUSE: line mbecause [said, sentence 2] claims rose(attendance) BECAUSE reaches(bus_route,estate), and line mdenied [said, sentence 4] denies it.`
- `reports/ledger_B05_mimo.new.txt` (inside `'minutes_world'`):
  `  YOU CLAIM AND DENY THE SAME CAUSE: line because1 [said, sentence 2] claims rose(attendance) BECAUSE reached(bus_route,estate), and line denial [said, sentence 4] denies it.`

No "finding of another kind" fired on any of the eight: no FOLLOWS, no FOLLOWS ONLY IF THE CAUSE IS
GRANTED, no CIRCLE, no `TO BE EXPECTED, using:`, no `The action does touch ...` and no KIND MISTAKE
appears in any of the eight reports, and no B05 report printed a DENIED BECAUSE without the CLAIM
AND DENY sentence. No ledger's claim sat in the actual ledger or was absent, and none was "out of
reach". Nothing is listed.

**Probes' exposure (the plan names B1).** The probed ledger here is Mimo's B03 (Mimo translated B03
in the probes, P4). Mimo's B03 ledger **sits with the others**: it gives the same JUMP inside the
same kind of world, on a because line of sentence 2, as Atria's unprobed B03 does, and as the seven
other F-side ledgers give their own expected kind. The row does not fire only on a probed text.

---

## B2 — the S-sides, the near miss

**Mark: MET on the texts where the row is markable (B04 on Atria; B10 on both). B01 and B06 fall on
neither side of the cell and are recorded, not scored. Charge: nothing fires; B04 Mimo is listed to
the translator as unmarkable.**

The row expects "B06 the because gets FOLLOWS or FOLLOWS ONLY IF THE CAUSE IS GRANTED (no JUMP);
B01 the since connects (no NO CONNECTION); B04 the plan gets a verdict other than CANNOT TELL; B10
DENIED BECAUSE reads `Fine.` and no CLAIM AND DENY flag. Expected on at least one translator's
ledger for each of B06, B01 and B04, and on both for B10."

### B04 — met, on Atria (`reports/ledger_B04_atria.new.txt`)

`  PLAN on line t7 [said, sentence 2]: "[TOLD in world notes_world] PLAN: sister plans to move the patient toward the desk SO THAT the patient's breathing is easy to monitor".`
`  The action does touch something the goal depends on, using:`
`    - line t10 [filled in, sentence 2]: ... moving the patient toward the desk changes whether the bed is near the desk ...`
`    - line t8 [filled in, sentence 2]: ... the patient's breathing being easy to monitor DEPENDS ON the bed being near the desk ...`

A verdict other than CANNOT TELL, as the cell asks. The route lines are in the ledger
(`ledgers/ledger_B04_atria.pl`: `changes(move(patient, toward(desk)), near(bed, desk)) :- line(t10).`
and `depends(easy_to_monitor(breathing(patient)), near(bed, desk)) :- line(t8).`). **Met.**

Mimo's B04 gave `CANNOT TELL whether the plan can work.` (`reports/ledger_B04_mimo.new.txt`). That
is the "against" word, but the against limb requires a ledger "that holds the rule or route as a
general line pointing at the right facts", and Mimo's B04 ledger holds no route at all: grepping
`ledgers/ledger_B04_mimo.pl` shows `claim_plan(plan, move_toward(patient, desk), monitored(breathing))`
with no `changes(...)` line and no `depends(monitored(breathing), ...)` line. So this is the cell's
other limb — "an S-side ledger with no rule or route line (B01, B06, B04) ... is the translator's
and is unmarkable here". **Listed, translator's, unmarkable, not counted.**

### B10 — met, on both

- `reports/ledger_B10_atria.new.txt`, inside `'headteacher_world'`:
  `  DENIED BECAUSE on line h_denied [said, sentence 4]: "[TOLD in world headteacher_world] NOT [line h_rise BECAUSE line h_repaint]".` /
  `  Fine. Nothing in the ledger makes repainted(entrance_hall) produce rose(attendance). The effect itself still stands; only the cause is denied.`
  No CLAIM AND DENY sentence appears anywhere in the file.
- `reports/ledger_B10_mimo.new.txt`, inside `'head_teacher_says'`:
  `  DENIED BECAUSE on line h_denial [filled in, sentence 4]: "[TOLD in world head_teacher_says] NOT [line h_rise BECAUSE line h_repaint]; ..."` /
  `  Fine. Nothing in the ledger makes repainted(school,entrance_hall) produce risen(attendance). ...`
  Again no CLAIM AND DENY, although the claim `h_because` and the denial `h_denial` sit in **the
  same world** here — exactly the near miss the plan says must not fire, and it did not.

**Met on both.** (The B10 ledgers do hold a denied-because line for the fourth sentence, so the
unmarkable limb does not apply.)

### B01 and B06 — on neither side of the cell; recorded

Both texts got the opposite of what the row expects:

- `reports/ledger_B01_atria.new.txt`: `NO CONNECTION. Nothing in the ledger leads from the reason to what is expected.`
- `reports/ledger_B01_mimo.new.txt`: `NO CONNECTION. ...`
- `reports/ledger_B06_atria.new.txt`: `JUMP. Even granting the stated cause, nothing in the ledger produces crossed_bar(trawler).`
- `reports/ledger_B06_mimo.new.txt`: `JUMP. Even granting the stated cause, nothing in the ledger produces crossed_bar_early(trawler).`

The cell's "against" limb charges the driver only for a JUMP/NO CONNECTION/CANNOT TELL "on an S-side
ledger that holds the rule or route **as a general line pointing at the right facts**". Reading the
built ledgers, **in all four the general line exists but points at atoms the ledger never asserts**:

- `ledgers/ledger_B06_atria.pl`:
  `produced(crossed_bar(B)) :- line(general), kind(B, loaded_boat), holds(at_harbour(B)), holds(turned(tide)).`
  The trawler is `kind(trawler, trawler)`, never `loaded_boat`, and no line asserts `at_harbour(trawler)`.
- `ledgers/ledger_B06_mimo.pl`:
  `produced(crossed_bar_early(X)) :- line(rule1), kind(X, boat), holds(loaded(X)), holds(at_harbour(X)), holds(turns_before_dawn(tide)).`
  The trawler is `kind(trawler, trawler)`; `loaded(trawler)`, `at_harbour(trawler)` and
  `turns_before_dawn(tide)` are all absent (the because claim names `turned(tide)` instead).
- `ledgers/ledger_B01_atria.pl`: the reason the since claim names is `open(gate)`
  (`claim_since(si1, in_field(flock, top_field), open(gate))`), while the rule is keyed to a
  different atom: `holds(driven_through(flock, gate)) :- line(al1), holds(left_open(shepherd, gate)).`
  The driver's own words: `It would take a line nobody wrote, of this kind: a general line saying
  that someone who open(gate) does in_field(flock,top_field).`
- `ledgers/ledger_B01_mimo.pl`: `holds(driven_through(flock, gate)) :- line(gate_rule), holds(left_open_by(shepherd, gate)).`
  — the second step (driven through ⇒ in the top field) is simply not written.

So the against limb does not fire. But the cell's unmarkable limb is keyed to "an S-side ledger with
**no** rule or route line", and here there **is** a rule line — it just binds nothing. **This outcome
falls on neither side of the cell as written**, and I record it rather than score it. If a marker
instead read these rules as "pointing at the right facts", B2 would be NOT MET against the driver on
four ledgers; I do not read them that way, because in every case it is the translator's own choice
of predicate or class that broke the match, which is the translator's layer, not the rig's. I note
both readings so the difference is visible.

**Probes' exposure (the plan names B2).** The probed ledger is Atria's B01. It **sits with the
others**: Atria's B01 and Mimo's unprobed B01 both printed NO CONNECTION on the since line of
sentence 2, and both wrote a rule the driver could not use. No difference of shape between the
probed and the unprobed ledger.

---

## B3 — variation, F1 and F2

**Mark: NOT MET. Charge: the translator — both of them.**

The row expects "8 pair-comparisons (2 translators × 4 pairs) with no ONLY or OPPOSITE line on an
unchanged sentence". The against cell: "Any ONLY or OPPOSITE line on an unchanged sentence: that
translator's ledger moved where the prose did not (L81 case 1), charged to the translator; counted
per translator."

The differing sentence is the second for B01/B08, B03/B06 and B04/B09, and the fourth for B05/B10
(plan, "The texts, by observable features"; P2). Reading all eight `sameness/pair_*.txt` files, the
ONLY buckets carry lines on unchanged sentences in **every one of the eight**. OPPOSITE is `0` in
all eight files (e.g. `sameness/pair_B08_B01_atria.txt`: `OPPOSITE (0, a near pair with NOT on one
side only):`), so the failure is entirely in the ONLY buckets.

Counted by hand from the files (ONLY+OPPOSITE lines / of those, lines whose printed sentence number
is **not** the pair's differing sentence):

| comparison | Atria | Mimo |
| --- | --- | --- |
| B08/B01 (diff. sentence 2) | 16 lines, **10** on unchanged sentences (1, 3, 4) | 13 lines, **8** on unchanged (1, 3, 4) |
| B03/B06 (diff. sentence 2) | 10 lines, **5** on unchanged (1) | 30 lines, **15** on unchanged (1, 4, 5) |
| B09/B04 (diff. sentence 2) | 19 lines, **7** on unchanged (1, 4) | 27 lines, **10** on unchanged (1) |
| B05/B10 (diff. sentence 4) | 17 lines, **11** on unchanged (1, 2, 3, 5) | 27 lines, **22** on unchanged (1, 2, 3, 5) |
| **total** | **33** on unchanged | **55** on unchanged |

Quoted evidence, `sameness/pair_B08_B01_atria.txt` (B08 and B01 differ only in sentence 2):

```
ONLY THE FIRST SAYS (7):
  line foreman [[CLAIMED]; usual case; sentence 1] foreman is a person; it answers a press as heavy and standing
  line rounds [[CLAIMED]; said; sentence 1] rounds are rounds; response to a press not stated
  line notes [[CLAIMED]; said; sentence 1] notes are notes; response to a press not stated
  line s1fact [[CLAIMED]; said; sentence 1] foreman kept notes on the rounds
  ...
  line grass [[TOLD in world note_world]; said; sentence 3] grass is grass; response to a press not stated
  line s4fact [[GIVEN]; said; sentence 4] the rounds finished
ONLY THE SECOND SAYS (9):
  line f1 [[CLAIMED]; said; sentence 1] foreman is a farm_foreman; it answers a press as not stated
  ...
  line e1 [[CLAIMED]; said; sentence 4] note ended
```

and `sameness/pair_B05_B10_mimo.txt` (differ only in sentence 4), where nine ONLY-lines carry
sentence 1 alone, e.g.

```
ONLY THE SECOND SAYS (17):
  line head_teacher [[GIVEN]; said; sentence 1] head_teacher is a person; it answers a press as heavy and standing
  line m_rise [[TOLD in world minutes_note]; said; sentence 1] attendance has risen
  line m_explanation [[TOLD in world minutes_note]; said; sentence 1] explanation is an explanation; ...
```

The row's second half — "every unchanged sentence that has a line on one side has a matched line on
the other" — fails in the same files and for the same reason.

No comparison is unmarkable (B5 lists no ledger). **0 of 8 comparisons clean.** Charged to the
translator, and counted per translator as the cell says: Atria 4 of 4 comparisons fired, Mimo 4 of 4.

**A note the marking must carry.** The tool's own header says
`(wording compared, not meaning; near matches and only-lines need a reader)`
(`sameness/pair_B08_B01_atria.txt`, line 2), and a great many of these ONLY lines are pure wording —
`foreman is a person` against `foreman is a farm_foreman`, `rounds are rounds` against
`rounds is a rounds` — the very thing L81 section 3 calls variation and the plan's "Traps" warn
against scoring. The cell as written nevertheless charges them ("**Any** ONLY or OPPOSITE line on an
unchanged sentence"), so I mark it as the plan wrote it. I record, under "What the plan did not
predict", that the row as drafted cannot be passed by two independently prompted models, because a
string-overlap matcher puts ordinary rewording into ONLY.

**Probes' exposure (the plan names B3).** The probed comparisons are B08/B01 for Atria and B03/B06
for Mimo. Both **sit with the others**: both fired, with 10 and 15 lines on unchanged sentences,
inside the same range as the unprobed comparisons (5 to 22). Nothing distinguishes the probed pairs.

---

## B4 — controls

**Mark: MET. Charge: nothing fires.**

The row: "On B02 and B07, both translators, both drivers: no finding of any kind; and the new
driver's OUTCOMES lines `because claims`, `since claims` and `plans` read `not asked, ...` (in every
world the ledger has, and in the actual ledger when the ledger has no world; a told world is not
required on a control)."

**No finding of any kind, all eight control reports.** Grepping the four control ledgers' eight
reports for every finding word the plan names (`JUMP`, `NO CONNECTION`, `CANNOT TELL`, `DENIED`,
`CLAIM AND DENY`, `TO BE EXPECTED`, `FOLLOWS`, `CIRCLE`, `KIND MISTAKE`) returns nothing. The four
old reports read only `NO FAULT FOUND in the lines that were checked.`
(`reports/ledger_B02_atria.old.txt`, `ledger_B02_mimo.old.txt`, `ledger_B07_atria.old.txt`,
`ledger_B07_mimo.old.txt`), with `INSIDE '<name>' (a told world, looked at alone): no contradiction.`
where the ledger has a world.

**The three OUTCOMES lines.** In every block of every control new-driver report:

- `reports/ledger_B02_atria.new.txt` (the ledger has no world — `ledgers/COUNTS.txt`:
  `ledger_B02_atria: ... TOLD 0, SUPPOSED 0; worlds: (none)`), the actual ledger's block:
  `  because claims: not asked, no line of that kind` /
  `  since claims: not asked, no line of that kind` /
  `  plans: not asked, no line of that kind`
- `reports/ledger_B02_mimo.new.txt`: the same three lines in the actual ledger's block **and**
  inside `'notebook_world'`.
- `reports/ledger_B07_atria.new.txt`: the same three lines in the actual ledger's block and inside
  `'shopkeeper_world'`.
- `reports/ledger_B07_mimo.new.txt`: the same three lines in the actual ledger's block and inside
  `'telling'`.

No `asked, nothing found` and no `asked, N found` on any of the three names, on any control. No
`ran out of time` line anywhere in the 64 reports (grep over `reports/` returns no file). The
plan's note that "a told world is not required on a control" is borne out: Atria's B02 has none and
Mimo's B02 has one, and both pass.

---

## B5 — validity and size

**Mark: MET. Charge: nothing fires.**

"Each provider returns a ledger that validates within two attempts on at least 14 of 16 texts (read
from the validation files' first two lines, P9)."

All 32 `translations/*.validation.txt` files read `attempt 1` or `attempt 2` on the first line and
`VALID` on the second — **16 of 16 for each provider**, well over the 14 required. Six needed the
second attempt: `B01.atria`, `B03.atria`, `B07.atria`, `B04.mimo`, `B06.mimo`, `B13.mimo` (e.g.
`translations/B01.atria.validation.txt`: `attempt 2` / `VALID`). No text failed both attempts, so
nothing is listed under that limb. The run log agrees: `valid ledgers: 32`
(`Language/results/L82 Arm B outputs.run.log`).

"every valid ledger has at least 3 said lines" — the smallest said count in `ledgers/COUNTS.txt` is
`ledger_B14_mimo: 10 lines; said 10`. All 32 clear 3.

"every valid ledger of B01, B03 to B06, B08 to B12 and B14 to B16 has at least one TOLD line" — from
`ledgers/COUNTS.txt`, the TOLD counts on those 26 ledgers run from 4 (`ledger_B14_mimo: ... TOLD 4`)
to 18 (`ledger_B10_mimo: ... TOLD 18`); none is 0.

"on B02, B07 and B13 the TOLD count is recorded, not required" — recorded here:
`ledger_B02_atria ... TOLD 0 ... worlds: (none)`; `ledger_B02_mimo ... TOLD 6 ... worlds: notebook_world`;
`ledger_B07_atria ... TOLD 14 ... worlds: shopkeeper_world`; `ledger_B07_mimo ... TOLD 13 ... worlds: telling`;
`ledger_B13_atria ... TOLD 0 ... worlds: (none)`; `ledger_B13_mimo ... TOLD 0 ... worlds: (none)`.

**No ledger is unmarkable under B5.** Every other row is marked on the full set.

---

## B6 — read-back

**Mark: MET. Charge: nothing fires.**

Read by `reader/KEY_report_names.json`, which maps the neutral codes to the reports. The eight
new-driver F-side reports are R23 (B08 atria), R48 (B08 mimo), R42 (B03 atria), R55 (B03 mimo),
R61 (B09 atria), R15 (B09 mimo), R53 (B05 atria), R64 (B05 mimo).

"on the markable new-driver F-side reports (8 if all are markable) it names the finding inside the
world and, in part 2, the sentence number the report prints, with at most 2 misses" — **0 misses of
8**:

- `reader/R23.response.txt`: "The checker found no connection in the ledger from that reason to what
  is expected" inside `world_1`; part 2: "All of the findings point at sentence 2".
- `reader/R48.response.txt`: "Inside the told world world_1, it found a since-claim"; part 2:
  "Sentence 2."
- `reader/R42.response.txt`: "Inside the told world "world_1", one because-claim was found ... The
  report attaches a "jump" note to it"; part 2: "all printed as sentence 2 (inside world_1)".
- `reader/R55.response.txt`: "Inside world_1 it found one BECAUSE-claim ... it printed a jump";
  part 2: "The report prints sentence 2 for the BECAUSE-claim".
- `reader/R61.response.txt`: "Inside world_1, one plan was found ... The checker could not tell
  whether that plan can work"; part 2: "The plan finding points at sentence 2, printed as line w9."
- `reader/R15.response.txt`: "Inside the told world world_1, the checker found one plan ... could not
  tell whether that plan can work"; part 2: "The plan is reported at sentence 2 (line pl, "said,
  sentence 2")."
- `reader/R53.response.txt`: "that same cause is both claimed and denied"; part 2: "The first
  finding points at sentence 2 ... The second finding points at sentence 2 for the claim and sentence
  4 for the denial."
- `reader/R64.response.txt`: "It also found (sentence 4) a denial of that same cause"; part 2: "The
  because-claim finding points at sentence 2; the denied-because finding points at sentence 4."

Every sentence number given is one the report prints (`[said, sentence 2]`, `[said, sentence 4]` in
the corresponding files under `reports/`).

"on the old-driver F-side reports it reports nothing found in all" — the eight are R25, R62, R28,
R57, R27, R43, R26, R44, and each answers nothing found, e.g. `reader/R25.response.txt`:
`1. The checker found no fault in the lines it checked, and no contradiction inside the told world
'world_1'.` and `reader/R43.response.txt`: `Nothing was found`.

"on the control reports (old and new) nothing found in all" — the eight are R14, R39, R46, R41
(B02) and R12, R24, R16, R49 (B07), and each answers nothing found, e.g.
`reader/R14.response.txt`: `The checker found nothing: contradictions and exceptions were asked and
came up empty`; `reader/R49.response.txt`: `The checker found no fault in the lines it checked`.

"A reader call in `FAILED.txt` or `SKIPPED.txt` is a miss" — both files are zero bytes, and the run
log says `reader: 64 reports, 64 calls, 0 failed, 0 skipped`.

"a sentence number given that the report does not print (recorded against the reader ...)" — I
checked every one of the 64 answers against the sentence numbers its own report prints. The single
apparent hit is `reader/R26.response.txt`, whose part 2 says `The report does not say — it prints no
sentence numbers`, and whose part 4 then offers a hypothetical wording: `One added sentence — for
example, "The lines checked were sentences 1 through 5, and each passed" — would settle it.` That is
not a sentence number given for a finding; the reader is quoting the sentence it wishes the report
had. **Nothing is recorded against the reader.**

---

## B7 — the two translators agree in kind

**Mark: MET. Charge: the translator layer, recorded per text — one miss, B04.**

"Per text of the thirteen that carry a reported argument (all but B02, B07 and B13), where both
ledgers are markable: the two translators' new-driver reports show the same set of finding kinds
inside the world ... with misses on at most 3 of the markable texts (13 if all are)." All 13 are
markable (B5 lists none).

Set of finding kinds inside the worlds, read from the reports:

| text | Atria | Mimo | agree? |
| --- | --- | --- | --- |
| B01 | NO CONNECTION | NO CONNECTION | yes |
| B03 | JUMP | JUMP | yes |
| **B04** | **NO CONNECTION + `The action does touch ...`** | **NO CONNECTION + CANNOT TELL** | **no** |
| B05 | JUMP + DENIED BECAUSE `Fine.` + CLAIM AND DENY | same three | yes |
| B06 | JUMP | JUMP | yes |
| B08 | NO CONNECTION | NO CONNECTION | yes |
| B09 | CANNOT TELL | CANNOT TELL | yes |
| B10 | JUMP + `Fine.` | JUMP + `Fine.` | yes |
| B11 | JUMP | JUMP | yes |
| B12 | JUMP | JUMP | yes |
| B14 | CANNOT TELL | CANNOT TELL | yes |
| B15 | JUMP | JUMP | yes |
| B16 | NO CONNECTION | NO CONNECTION | yes |

The one miss, quoted: `reports/ledger_B04_atria.new.txt`
`  The action does touch something the goal depends on, using:` against
`reports/ledger_B04_mimo.new.txt` `  CANNOT TELL whether the plan can work.`

**1 miss of 13 markable texts**; the against limb is "Misses on 4 or more markable texts". Met.

"On B13 the kinds in the actual ledger are compared and recorded, not counted" — recorded: both are
`JUMP` on the because claim (`reports/ledger_B13_atria.new.txt`,
`reports/ledger_B13_mimo.new.txt`). They agree.

**Probes' exposure (the plan names B7).** The probed texts are B01 (Atria) and B03 (Mimo), "one per
translator, which is the axis B7 measures". Both **sit with the others**: B01 and B03 both agree in
kind, as 11 of the other 12 texts do. The single miss, B04, is on neither probed text.

---

## B8 — the old driver's silence

**Mark: MET. Charge: nothing fires** (the row charges "the premise (P6)", and the premise held).

"On every ledger whose claim sits in a told world, the old driver prints no BECAUSE, SINCE or PLAN
finding (P6)."

Grepping all 32 `reports/*.old.txt` for `BECAUSE-claim on `, `SINCE-claim on ` and `PLAN on ` returns
exactly two files: `reports/ledger_B13_atria.old.txt` and `reports/ledger_B13_mimo.old.txt`. B13 is
precisely the ledger whose claim does **not** sit in a told world — `ledgers/COUNTS.txt` records
`ledger_B13_atria: ... TOLD 0, SUPPOSED 0; worlds: (none)` and the same for `ledger_B13_mimo` — and
the old report prints `BECAUSE-claim on line k: "[CLAIMED] line i BECAUSE line j".` with the standing
`[CLAIMED]`, i.e. the actual ledger. That is P6's own second sentence at work
("a because claim in the actual ledger, as B13's is expected to be, is reached by the old driver"),
not an exception to the row.

So on all 30 ledgers whose claim sits in a told world, the old driver printed nothing of the three
kinds — a clean run of the near-miss case the plan lists under "Near-miss cases that must not fire".

---

## B9 — time

**Mark: MET. Charge: nothing fires** (the row charges "the pipeline").

All four budgets, read from `Language/results/L82 Arm B outputs.run.log`:

| budget | plan | run log | |
| --- | --- | --- | --- |
| all 32 translations | 5 hours | `translations took 13989 s` = 3 h 53 m 09 s | under |
| reader calls (64 at most) | 120 minutes | `reader took 907 s` = 15 m 07 s | under |
| prose-reader calls (32 at most) | 90 minutes | `prose reader took 1914 s` = 31 m 54 s | under |
| the rig (drivers and consequences together) | 15 minutes | `rig (drivers and consequences) took 381 s` = 6 m 21 s | under |

The run ran end to end without a stop: `run started 2026-09-22T20:36:40Z` ... `done 01:23:12`. No
text exhausted six streamed attempts — the longest attempt history in `translations/*.receipt.json`
is four (`B01.atria.attempt2.receipt.json`: `"attempts": 4`), so nothing is listed under B5 on this
head and no single call ate the budget.

"No other caller of either provider runs while the runner runs (the runner refuses to start while one
is running, P11); the pilot runs are finished before the run starts." The run reached step 1 and
completed, which is what the guard permits; nothing in the outputs records a second caller. I cannot
positively verify a caller started from the same shell after the run began (the plan itself puts that
under Not tested), so I mark this limb on the evidence available: no second caller is recorded
against the pipeline.

---

## B10 — the hedge

**Mark: MET. Charge: the language (scope), as the cell states.**

"On B12 and B15, both translators: the new driver reports a JUMP inside the world on the because line
of both ...; the prose reader answers "hedged in the passage" for B12's finding and "claimed as a
fact in the passage" for B15's, on both translators' reports. Expected: 4 of 4 JUMPs, 4 of 4
prose-reader answers as stated."

**4 of 4 JUMPs**, all inside `report_world`:

- `reports/ledger_B12_atria.new.txt`: `  BECAUSE-claim on line wbecause [said, sentence 2]: "[TOLD in world report_world] line wflood BECAUSE line wopen".` / `  JUMP. ...`
- `reports/ledger_B12_mimo.new.txt`: `  BECAUSE-claim on line b1 [said, sentence 2]: "[TOLD in world report_world] line f_flooded BECAUSE line f_valve_open".` / `  JUMP. ...`
- `reports/ledger_B15_atria.new.txt`: `  BECAUSE-claim on line n [said, sentence 2] ...` / `  JUMP. ...`
- `reports/ledger_B15_mimo.new.txt`: `  BECAUSE-claim on line cause1 [said, sentence 2] ...` / `  JUMP. ...`

**4 of 4 prose-reader answers as stated:**

- `prose_reader/ledger_B12_atria.response.txt`:
  `- BECAUSE-claim on line wbecause (said, sentence 2): hedged in the passage — "the valve may have been left open".`
- `prose_reader/ledger_B12_mimo.response.txt`:
  `- BECAUSE-claim on line b1 [said, sentence 2]: hedged in the passage — "because the valve may have been left open".`
- `prose_reader/ledger_B15_atria.response.txt`:
  `1. "BECAUSE-claim on line n [said, sentence 2]" — claimed as a fact in the passage: "the cellar had flooded because the valve had been left open" (no may, might, or seemed).`
- `prose_reader/ledger_B15_mimo.response.txt`:
  `- BECAUSE-claim on line cause1 [said, sentence 2]: claimed as a fact in the passage — the surveyor "wrote that the cellar had flooded because the valve had been left open".`

**The override applies, and only it.** The cell's escape — "A B12 ledger that keeps the hedge out of
the world's claim by some other means (the claim hedged, absent, or in the bin)" — did not happen on
either B12 ledger. Both wrote the cause as a flat fact inside the world and put the modal in the bin,
which is exactly the language's silence L81 section 3 names:

- `ledgers/ledger_B12_atria.json`, bin: `{"sentence": 2, "words": "may have been", "reason": "Modal possibility; outside the language. The cause is recorded at line wopen without the uncertainty, marked filled in."}`
- `ledgers/ledger_B12_mimo.json`, bin: `{"sentence": 2, "words": "may have been", "reason": "A modal of possibility; the language has no form for may, must, should, can. The report allows its cause as possible only, so line f_valve_open (filled in) states more than the report does."}`

No B15 ledger lacks a because line; no prose-reader answer of "claimed as a fact" on B12 or "hedged"
on B15 (the near miss the plan lists as one that must not fire — and it did not); no "not made" or
"cannot tell" on either B12 or B15 **because claim**.

So, in the cell's own words: "If all four JUMPs and all four answers come as expected, **the language
is charged with the false finding L81 section 3 and 5 name, and C is short a change** (marking rule,
1)." That is the charge, and it is not the translators' and not the driver's.

---

## B11 — the narrator's own

**Mark: MET. Charge: nothing fires.**

"On B13, both translators: the because claim is in the actual ledger, not a world; both drivers
report a JUMP on it (P6); the prose reader answers "claimed as a fact in the passage"."

**In the actual ledger, not a world**, on both: `ledgers/COUNTS.txt` —
`ledger_B13_atria: 17 lines; said 16 ... TOLD 0, SUPPOSED 0; worlds: (none)` and
`ledger_B13_mimo: 16 lines; said 16 ... TOLD 0, SUPPOSED 0; worlds: (none)`. The reports print the
claim with the standing `[CLAIMED]`. The against limb "A world holding the claim on B13" did not
fire.

**Both drivers report a JUMP**, on both ledgers — four reports:

- `reports/ledger_B13_atria.new.txt`: `  BECAUSE-claim on line k [said, sentence 2]: "[CLAIMED] line i BECAUSE line j".` / `  JUMP. Even granting the stated cause, nothing in the ledger produces left(train,station).`
- `reports/ledger_B13_atria.old.txt`: `BECAUSE-claim on line k: "[CLAIMED] line i BECAUSE line j".` / `JUMP. Even granting the stated cause, nothing in the ledger produces left(train,station).`
- `reports/ledger_B13_mimo.new.txt`: `  BECAUSE-claim on line p [said, sentence 2] ...` / `  JUMP. ...`
- `reports/ledger_B13_mimo.old.txt`: `BECAUSE-claim on line p: "[CLAIMED] line k BECAUSE line l".` / `JUMP. Even granting the stated cause, nothing in the ledger produces left_station_late(train,station).`

Neither "the old driver silent while the new reports a JUMP" nor "both silent" happened. Both
ledgers hold a because line for B13's claim, so the translator limb does not fire. No because verdict
other than JUMP appears — no FOLLOWS, no FOLLOWS ONLY IF THE CAUSE IS GRANTED, no CIRCLE.

**The prose reader answers "claimed as a fact in the passage"**, on both:

- `prose_reader/ledger_B13_atria.response.txt`:
  `- BECAUSE-claim on line k [said, sentence 2] "[CLAIMED] line i BECAUSE line j": claimed as a fact in the passage — "The train left the station late because the signal failed at the junction."`
- `prose_reader/ledger_B13_mimo.response.txt`:
  `- BECAUSE-claim on line p (sentence 2) — claimed as a fact in the passage: "The train left the station late because the signal failed at the junction."`

Neither "hedged" nor "not made" (prose reader's charge) nor "cannot tell" (recorded against the
report) on the because claim itself. **Recorded, not scored:** the two answers each gave a second,
separate answer for the JUMP *verdict* — Atria's report drew `claimed as a fact in the passage` and
Mimo's drew `cannot tell from the report; ... the jump complaint is about the ledger, which the
report does not show`. The cell's answers are keyed to "the because claim", which both got right, so
this does not fire B11; it is part of the pattern I record under B13 and in the closing list.

---

## B12 — the rewordings

**Mark: NOT MET. Charge: the translator — both of them. The report half is recorded, not charged.**

The marking rule, point 2, is explicit about order: "Where a row has a sameness half and a report
half, the sameness half is read first and decides the charge of the report half: clean sameness with
differing report kinds charges the driver (L81 section 5); unclean sameness charges the translator and
the report half is recorded, not charged." The Traps repeat it: "Charging the translator for a
differing report kind before reading the sameness half (B12)."

### The sameness half, read first — unclean in all six

The reworded sentence is the third for B16/B08 and B11/B03, the fourth for B14/B09 (P2). Every one of
the six `sameness/pair_*` comparisons carries ONLY lines on unchanged sentences; OPPOSITE is `0` in
all six:

| comparison | Atria | Mimo |
| --- | --- | --- |
| B08/B16 (reworded sentence 3) | 7 ONLY lines, **5** on unchanged (1, 2) | 13 ONLY lines, **10** on unchanged (1, 2, 4) |
| B03/B11 (reworded sentence 3) | 13 ONLY lines, **9** on unchanged (1, 2, 5) | 18 ONLY lines, **14** on unchanged (1, 2, 4, 5) |
| B09/B14 (reworded sentence 4) | 16 ONLY lines, **15** on unchanged (1, 2, 3) | 11 ONLY lines, **8** on unchanged (1, 2) |

Quoted, `sameness/pair_B08_B16_atria.txt` (B16 differs from B08 only in sentence 3):

```
ONLY THE FIRST SAYS (3):
  line foreman [[CLAIMED]; usual case; sentence 1] foreman is a person; it answers a press as heavy and standing
  line since1 [[TOLD in world note_world]; said; sentence 2] line flock_in SINCE line gate_open
  ...
ONLY THE SECOND SAYS (4):
  line rounds [[GIVEN]; said; sentence 1] foreman made rounds
  line wrote [[CLAIMED]; said; sentence 2] foreman wrote the note
  line since1 [[TOLD in world shepherd_world]; said; sentence 2] line flocktop SINCE line gateopen
  ...
```

and `sameness/pair_B09_B14_atria.txt` (reworded sentence 4), where eight ONLY-lines carry sentence 1:

```
ONLY THE FIRST SAYS (12):
  line n1 [[GIVEN]; said; sentence 1] nurse is a person, incoming
  line n2 [[GIVEN]; usual case; sentence 1] nurse answers a press as heavy and standing
  line n4 [[GIVEN]; said; sentence 1] sister is a person, the night sister
  ...
```

**0 of 6 comparisons clean.** Charged to the translator, counted per translator: Atria 3 of 3 fired,
Mimo 3 of 3.

### The report half — recorded, not charged

Because the sameness half is unclean, the cell puts the report half on record only. For the record,
**the report kinds inside the world are identical on all six pairs**, which is what the row wanted:

- B08 `NO CONNECTION` / B16 `NO CONNECTION`, Atria (`reports/ledger_B08_atria.new.txt`,
  `reports/ledger_B16_atria.new.txt`) and Mimo (`ledger_B08_mimo.new.txt`, `ledger_B16_mimo.new.txt`).
- B03 `JUMP` / B11 `JUMP`, Atria and Mimo.
- B09 `CANNOT TELL` / B14 `CANNOT TELL`, Atria and Mimo.

No comparison is unmarkable (B5 lists no ledger).

**Probes' exposure (the plan names B12).** The probed comparison is B03/B11 for Mimo. It **sits with
the others**: it fired like the other five, with 14 ONLY-lines on unchanged sentences, the highest of
the six but inside the same shape; and its report half is identical (`JUMP` on both), like the other
five. Nothing distinguishes it.

---

## B13 — the prose reader on every report

**Mark: NOT MET. Charge: mainly the rig, on the part-2 half; the first half's answers fire the cell's
words but not its reasoning, and I record rather than charge them.**

The row has three clauses. Read on the 32 new-driver reports (all markable under B5), except that one
has no answer at all — see the unpredicted outcome below.

### (a) "no finding answered "not made in the passage"" — fires 17 times, but not for the cell's reason

Reading findings proper only (the BECAUSE-claim, SINCE-claim, PLAN, DENIED BECAUSE and CLAIM AND DENY
lines **and their verdicts**, not OUTCOMES rows and not GAUGE notes), a "not made in the passage"
answer appears on 17 of the 27 answerable non-control reports: B01 atria, B01 mimo, B03 mimo, B05
atria, B06 atria, B06 mimo, B08 mimo, B09 atria, B11 atria, B12 atria, B12 mimo, B14 atria, B14 mimo,
B15 atria, B15 mimo, B16 atria, B16 mimo.

**Every single one of the seventeen lands on a driver verdict, never on a claim line.** Quoted:

- `prose_reader/ledger_B06_atria.response.txt`:
  `- JUMP on the effect line crossing, sentence 2 (nothing in the ledger produces crossed_bar(trawler)): "not made in the passage" — the crossing itself is stated as a fact ("the trawler crossed the bar"), but nobody in the passage claims the cause fails to produce it.`
  — while the *claim* on the same report drew
  `- BECAUSE-claim on line because [said, sentence 2] ...: "claimed as a fact in the passage" — "the trawler crossed the bar early because the tide had turned".`
- `prose_reader/ledger_B16_atria.response.txt`:
  `- NO CONNECTION on line since1 — not made in the passage: the shepherd claims the link, not its absence ("since the gate stood open").`
- `prose_reader/ledger_B14_mimo.response.txt`:
  `- "CANNOT TELL whether the plan can work" — not made in the passage: the passage gives only the aim ("so that his breathing would be easier to monitor") and never claims the move would work.`
- `prose_reader/ledger_B12_atria.response.txt`:
  `- JUMP on line wbecause (sentence 2): not made in the passage — nobody there claims the flood fails to follow from the stated cause; the surveyor asserts the link herself.`

The cell's against limb reads: "A "not made" answer on a non-control: **the translator invented a
claim** (L81, "a claim the reported person never made"), charged to that translation and listed." On
the plan's literal words this half is not met, 17 times. But **not one of the seventeen shows a
translator inventing a claim**: in each, the prose reader is saying, correctly, that a checker's
verdict about the ledger is not something the passage's reported person asserted. Applying the charge
as drafted would charge the translations for the driver's own prose. **I therefore record all
seventeen and decline to charge any translation on them**, and I list under "What the plan did not
predict" that the cell does not distinguish a finding's claim line from the driver's verdict on it.

Of the ten answerable non-control reports with no "not made" on a finding proper, the same verdicts
mostly drew `cannot tell from the report` instead (e.g. `prose_reader/ledger_B05_mimo.response.txt`:
`- JUMP on line because1: cannot tell from the report — it turns on "nothing in the ledger produces
rose(attendance)", and I do not see the ledger.`), which the cell records against the report and
counts "neither for nor against the first half". The split between "not made" and "cannot tell" on
the same verdict, across the same translator pairs, is itself unpredicted.

**"A "hedged in the passage" answer outside B12":** these occur — e.g.
`prose_reader/ledger_B01_atria.response.txt`
`- SINCE-claim on line si1 [said, sentence 2] — hedged in the passage ("the shepherd had concluded the flock must be in the top field, since the gate stood open": hedges "had concluded", "must").`
and `prose_reader/ledger_B05_atria.response.txt`
`- DENIED BECAUSE on line mdenied (said, sentence 4): hedged in the passage — "she said she did not think the rise in attendance was because of the new bus route."`
The cell then asks me to read the quoted hedge against the passage. I did: `B01.txt` does read "the
shepherd **had concluded** the flock **must** be in the top field" and `B05.txt` does read "she said
she **did not think**". These are real hedges in the passages, so under the cell's words they would
charge the translator ("a real hedge the ledger made a fact charges the translator") rather than the
prose reader. I record them: on B01 the reported person's conclusion is written flat as
`holds(in_field(flock, top_field))` (`ledgers/ledger_B01_atria.pl`), and on B05 the denial is written
flat as `NOT [line mrise BECAUSE line mreach]`. But both are the same modality gap L81 section 3
calls "a false finding produced by the language's silence on modality" and the marking rule's
point 1 takes off the translator — an override the plan scopes to B12 only. **This is a second place
where the outcome falls on neither side of the cell**, and I record it without charging.

### (b) "part 2 answers "nothing" on every non-control passage" — fails, 21 of 27

Part 2 of the prose reader brief asks for "Anything argued in the passage that the report does not
mention: quote the passage's words, or write 'nothing'" (P10). Only six answerable non-control
reports answered nothing: B03 mimo (`2. nothing ...`), B04 atria (`2. nothing`), B10 atria
(`2. nothing.`), B10 mimo (`2. nothing`), B11 mimo (`2. nothing`); and B12 atria in prose
(`2. Nothing argued in the passage is left out of the report`). The other twenty-one quote passage
words. Examples:

- `prose_reader/ledger_B06_atria.response.txt`:
  `2. "she added that a loaded boat at that harbour always crosses the bar early once the tide turns before dawn" — the report only calls it "the general line's condition" and never checks it ("two usually lines: not asked").`
- `prose_reader/ledger_B01_atria.response.txt`:
  `2. "the shepherd always left that gate open only once the flock had been driven through it"`
- `prose_reader/ledger_B16_atria.response.txt`:
  `2. "no grass remained in the lower field", added "from what he saw himself" — the report never names it as a claim, and never offers it as the very bridge its NO CONNECTION finding asks for.`
- `prose_reader/ledger_B13_atria.response.txt`:
  `2. "The morning was cold and the platform was nearly empty."; "Two porters carried the mailbags to the far end of the platform."; ...`

The cell: "A part 2 quotation on a non-control: the report missed an argument the passage carries,
**charged to the translation if the ledger lacks the line and to the driver if it has it**." I checked
the built ledgers for every quoted item I could pin to a line, and **in every case the ledger has the
line**, so the charge falls on the driver:

- B01 atria's rule: `ledgers/ledger_B01_atria.pl` holds it —
  `holds(driven_through(flock, gate)) :- line(al1), holds(left_open(shepherd, gate)).` → **driver**.
- B06 atria's and mimo's rule: `ledgers/ledger_B06_atria.pl` `line(general)` and
  `ledgers/ledger_B06_mimo.pl` `line(rule1)` → **driver**. (Mimo's own answer says so: "the report
  names line rule1 but raises no finding on it".)
- B16 atria's grass line: the ledger holds `line nograss ... NOT [grass remained in the lower field]`
  (`sameness/pair_B08_B16_atria.txt`) → **driver**.
- B01 mimo's lower field: `ledgers/ledger_B01_mimo.pl` `holds(empty_of_grass(lower_field)) :- line(field_empty).` → **driver**.
- B13's cold morning and porters: `ledgers/ledger_B13_atria.pl` `holds(cold(morning)) :- line(c).`;
  `ledgers/ledger_B13_mimo.pl` `holds(carried(porters, mailbags, toward(end_of_platform))) :- line(m).` → **driver**.
- B11 atria's crew, count and repairs: `ledgers/ledger_B11_atria.pl` `holds(lists(log, crew_of(boat)))`,
  `holds(tied_up(boats))`, `holds(concerns(entry, repairs))` → **driver**.

**The charge under (b) is the rig**: the new driver names, in its findings, only the lines a check
fires on, so lines the ledger carries — including the reported person's own general rule on B01 and
B06, the one thing that would answer the NO CONNECTION and the JUMP — never reach the report at all.
That is the substantive finding of this row.

I record, however, that most of the twenty-one quotations are **not arguments** but recorded facts
("the names of the crew", "his temperature had been normal at midnight", "the time the rounds had
finished"). The brief asks for "anything **argued**"; the prose reader answered with anything the
report failed to mention. The genuinely argued misses are B01 atria's rule and B06's rule on both
translators — three of the twenty-one.

### (c) "on controls part 1 reports no findings" — met, 4 of 4

`prose_reader/ledger_B02_atria.response.txt`, `ledger_B02_mimo.response.txt`,
`ledger_B07_atria.response.txt` and `ledger_B07_mimo.response.txt` list only OUTCOMES rows and bin
entries in part 1; not one names a BECAUSE-claim, SINCE-claim, PLAN, DENIED BECAUSE or CLAIM AND DENY.
E.g. `prose_reader/ledger_B02_mimo.response.txt`:
`- OUTCOMES kinds (contradictions, exceptions, and the rest): no findings to judge — the report says "contradictions: asked, nothing found" ...`
The marking rule's point 3 ("On a control, B4 governs") is not needed, because no "not made" answer
on a control attaches to a finding.

### The report with no answer

`prose_reader/ledger_B04_mimo.response.txt` contains, in full:
`The request was rejected because it was considered high risk`
and `prose_reader/ledger_B04_mimo.receipt.json` records
`"finish_reason": "content_filter"`, `"attempts": 1`, `"attempt_history": [{"attempt": 1, "status": 200, ...}]`.
The call returned 200 with non-empty content, so the caller did not retry it, and it is in neither
`prose_reader/FAILED.txt` nor `prose_reader/SKIPPED.txt` (both zero bytes); the run log reads
`prose reader: 32 calls, 0 failed, 0 skipped`. **B13's only unmarkable limb is keyed to those two
files**, so on the plan's words this report is not unmarkable — yet there is no answer to read.
**Unmarkable in fact, on neither side of the cell**; I have excluded it from the counts above and
record it as the plan's clearest gap.

---

# Closing table

| Row | Mark | Charge | Evidence, one line |
| --- | --- | --- | --- |
| B1 the F-sides, inside the world | **MET** | none fires (row would charge the rig, or the translation/guide) | 8 of 8: e.g. `reports/ledger_B05_atria.new.txt` `YOU CLAIM AND DENY THE SAME CAUSE: line mbecause [said, sentence 2] claims rose(attendance) BECAUSE reaches(bus_route,estate), and line mdenied [said, sentence 4] denies it.` |
| B2 the S-sides, the near miss | **MET** on its markable texts (B04 Atria, B10 both); **B01 and B06 on neither side**, recorded | none fires; B04 Mimo listed to the translator as unmarkable | `reports/ledger_B04_atria.new.txt` `The action does touch something the goal depends on, using:`; but `ledgers/ledger_B06_atria.pl` `produced(crossed_bar(B)) :- line(general), kind(B, loaded_boat), holds(at_harbour(B)), ...` — a rule whose antecedents the ledger never asserts, so neither "points at the right facts" nor "no rule line" |
| B3 variation, F1 and F2 | **NOT MET** | the translator, both (Atria 4/4 comparisons fired, Mimo 4/4) | `sameness/pair_B08_B01_atria.txt` `ONLY THE FIRST SAYS (7): line s1fact [[CLAIMED]; said; sentence 1] foreman kept notes on the rounds` — sentence 1 is unchanged; 33 such lines for Atria, 55 for Mimo |
| B4 controls | **MET** | none fires | `reports/ledger_B07_mimo.new.txt` inside `'telling'`: `because claims: not asked, no line of that kind` / `since claims: not asked, no line of that kind` / `plans: not asked, no line of that kind`, and no finding word in any of the eight control reports |
| B5 validity and size | **MET** | none fires | all 32 `translations/*.validation.txt` read `attempt 1`or`attempt 2` then `VALID` — 16 of 16 per provider; smallest said count `ledger_B14_mimo: 10 lines; said 10`; no required TOLD line missing |
| B6 read-back | **MET** | none fires | 0 misses of 8: `reader/R53.response.txt` `The second finding points at sentence 2 for the claim and sentence 4 for the denial.`; all 16 old-F-side and control answers report nothing found; `FAILED.txt`/`SKIPPED.txt` empty |
| B7 the two translators agree in kind | **MET** | the translator layer, recorded per text — 1 miss (B04) | `reports/ledger_B04_atria.new.txt` `The action does touch something the goal depends on` against `reports/ledger_B04_mimo.new.txt` `CANNOT TELL whether the plan can work.`; 12 of 13 texts agree |
| B8 the old driver's silence | **MET** | none fires (premise P6 held) | only `reports/ledger_B13_*.old.txt` print a BECAUSE/SINCE/PLAN finding, and B13's claim is `[CLAIMED]` in the actual ledger (`ledgers/COUNTS.txt`: `worlds: (none)`) |
| B9 time | **MET** | none fires | `L82 Arm B outputs.run.log`: `translations took 13989 s` (<5 h), `reader took 907 s` (<120 min), `prose reader took 1914 s` (<90 min), `rig (drivers and consequences) took 381 s` (<15 min) |
| B10 the hedge | **MET** | **the language (scope)** — C is short a change | `prose_reader/ledger_B12_mimo.response.txt` `BECAUSE-claim on line b1 [said, sentence 2]: hedged in the passage — "because the valve may have been left open"` against `prose_reader/ledger_B15_mimo.response.txt` `claimed as a fact in the passage`; 4 JUMPs, 4 answers, and both B12 bins hold `"words": "may have been"` |
| B11 the narrator's own | **MET** | none fires | `reports/ledger_B13_mimo.old.txt` `BECAUSE-claim on line p: "[CLAIMED] line k BECAUSE line l". JUMP.` — and `prose_reader/ledger_B13_atria.response.txt` `claimed as a fact in the passage — "The train left the station late because the signal failed at the junction."` |
| B12 the rewordings | **NOT MET** (sameness half read first) | the translator, both (Atria 3/3, Mimo 3/3); report half recorded, not charged | `sameness/pair_B09_B14_atria.txt` `ONLY THE FIRST SAYS (12): line n1 [[GIVEN]; said; sentence 1] nurse is a person, incoming` — sentence 1 unchanged (reworded sentence is 4); report kinds identical 6 of 6 |
| B13 the prose reader on every report | **NOT MET** | the **rig** on the part-2 half (the ledger holds every quoted line); the 17 "not made" answers recorded, not charged, since each lands on a driver verdict | `prose_reader/ledger_B06_atria.response.txt` `2. "she added that a loaded boat at that harbour always crosses the bar early once the tide turns before dawn" — the report only calls it "the general line's condition" and never checks it` while `ledgers/ledger_B06_atria.pl` holds `line(general)`; 21 of 27 answerable non-control reports quote in part 2 |

---

# What the plan did not predict

1. **A provider content filter that returns 200.** `prose_reader/ledger_B04_mimo.response.txt` is the
   single line `The request was rejected because it was considered high risk`, and its receipt records
   `"finish_reason": "content_filter"` on a `status: 200` first attempt. Because the answer is not
   empty, P3's caller neither labelled it -2 nor retried it; the run log says `0 failed, 0 skipped`
   and both `FAILED.txt` files are empty. B13's only unmarkable limb is keyed to those files, so the
   plan has no way to name a report whose prose-reader answer exists but says nothing. One of the 32
   reports is unmarkable in fact and markable on the plan's words.

2. **`content_filter` on translation calls too, silently costing a validation attempt.**
   `translations/B04.mimo.attempt1.receipt.json` and `translations/B13.mimo.attempt1.receipt.json`
   both record `"finish_reason": "content_filter"` with status 200; both ledgers then needed a second
   validation attempt (`translations/B04.mimo.validation.txt`: `attempt 2`). The plan's P3 and P9 name
   `length`, empty answers and HTTP codes, never a content filter.

3. **Mimo cuts its stream as often as Atria does.** P4 records the irregular cut as Atria's
   ("Atria also cuts a stream at irregular points"). In the run, `-2` attempts are everywhere on both
   providers: 29 of the 38 translation receipts carry at least one `-2`, including
   `B02.mimo` `[-2, -2, 200]`, `B05.mimo` `[-2, -2, -2, 200]`, `B07.mimo` `[-2, -2, -2, 200]`,
   `B08.mimo` `[-2, -2, -2, 200]`. The thirteenth version's retry provision carried the run; without
   it almost nothing would have translated.

4. **The `length` exhaustion the plan feared on Atria happened on Mimo.**
   `translations/B06.mimo.attempt1.receipt.json` `hist=[-4, -2, -2, 200]` and
   `translations/B09.mimo.attempt1.receipt.json` `hist=[-2, -4, 200]` are the only `-4`s in the run.
   P4's whole discussion of exhaustion, and the "Not tested" note, are about Atria's 65,536 ceiling;
   no Atria call exhausted its cap.

5. **A 200 with no finish reason at all.** `translations/B01.atria.attempt1.receipt.json` and
   `B07.atria.attempt1.receipt.json` record `"finish_reason": null` on the successful attempt. P3's
   label set does not name a successful answer with no finish reason.

6. **B3 and B12 as drafted cannot be passed.** `sameness_2.py`'s own header says
   `(wording compared, not meaning; near matches and only-lines need a reader)`, and its ONLY buckets
   are therefore full of pure rewording — `rounds are rounds` against `rounds is a rounds`,
   `foreman is a person` against `foreman is a farm_foreman`. L81 section 3 and the plan's own Traps
   call that variation and forbid scoring it, yet B3 and B12 charge "**Any** ONLY or OPPOSITE line on
   an unchanged sentence". Every one of the 14 comparisons fired, with 0 OPPOSITE lines anywhere: the
   rows measured the matcher, not the translators' movement. A threshold (or a restriction to
   OPPOSITE and to lines the NEAR bucket does not cover) is what the rows needed.

7. **The prose reader answers the driver's verdicts as if they were the passage's claims.** All 17
   "not made in the passage" answers on findings proper attach to a JUMP, a NO CONNECTION or a
   CANNOT TELL, never to a claim line — e.g. `prose_reader/ledger_B12_atria.response.txt`
   `JUMP on line wbecause (sentence 2): not made in the passage — nobody there claims the flood fails
   to follow from the stated cause`. B13's cell reads any "not made" as "the translator invented a
   claim", a charge none of the seventeen supports. The brief's four labels need a fifth for "this is
   the checker's verdict, not anyone's claim", or the cell needs to say that only a claim line's
   answer counts.

8. **The same verdict drew different labels across translators on the same text.** On B03 the JUMP
   drew `claimed as a fact in the passage` from Atria's report and `not made in the passage` from
   Mimo's; on B05 it drew `not made` from Atria's and `cannot tell from the report` from Mimo's; on
   B09 the CANNOT TELL drew `not made` from Atria's and `hedged in the passage` from Mimo's. The plan
   treats the prose reader as a fixed instrument and has no cell for its own inconsistency across a
   pair.

9. **"Hedged in the passage" answers outside B12 are real hedges, and the override does not reach
   them.** `prose_reader/ledger_B01_atria.response.txt` quotes `"had concluded", "must"` and
   `prose_reader/ledger_B05_atria.response.txt` quotes `"she said she did not think"` — both genuine
   hedges the ledgers wrote flat (`holds(in_field(flock, top_field))`, `NOT [line mrise BECAUSE line
   mreach]`). B13's cell would charge the translator; the marking rule's hedge override is scoped to
   B12 alone. The same modality gap B10 charges to the language would, outside B12, be charged to the
   translators.

10. **The new driver never mentions a general line that fires no check.** This is what B13's part-2
    half actually found, and no cell names it: on B01 (Atria) and B06 (both) the reported person's own
    rule is in the ledger (`line(al1)`, `line(general)`, `line(rule1)`) and the report prints a JUMP
    or NO CONNECTION saying `It would take a line nobody wrote` — while the line the prose reader
    points at sits unnamed in the same ledger. The plan's B1, B2 and B12 all read report kinds; none
    reads what the report leaves out.

11. **A rule line that binds nothing is neither of B2's two cases.** In all four B01/B06 ledgers the
    translator wrote the rule but keyed it to a class or a fact the ledger never asserts
    (`kind(B, loaded_boat)` for a `kind(trawler, trawler)`; `holds(at_harbour(B))`, `holds(loaded(X))`,
    `holds(turns_before_dawn(tide))`, `holds(left_open(shepherd, gate))` against a reason written
    `open(gate)`). B2 brackets only "a general line pointing at the right facts" (driver) and "no rule
    or route line" (translator, unmarkable). This third state decided four of the row's eight ledgers.

12. **Part 2 answers named recorded facts, not arguments.** The brief asks for "anything **argued**";
    18 of the 21 part-2 quotations are plain records — "the names of the crew", "his temperature had
    been normal at midnight", "The morning was cold". B13's cell reads every quotation as "the report
    missed an argument the passage carries", which overstates 18 of them.

13. **Two reader answers drop the opening label.** `reader/R12.response.txt` and
    `reader/R50.response.txt` begin at `1. **What the checker found**` with no `READER:` line, though
    P10 records that the answer "begins `READER:`". Both end `READING COMPLETE` and both are otherwise
    complete; nothing scores the format.

14. **The prose reader's part 3 said "no" on two reports, and nothing reads it.** 
    `prose_reader/ledger_B16_atria.response.txt` `3. No — the report puts the argument in
    'shepherd_world' and leaves 'note_world' with 0 findings, while the passage puts the argument
    inside the foreman's note` and `prose_reader/ledger_B13_atria.response.txt` `3. No.` Part 3 is the
    one question the brief asks about world placement, and no row in the table reads it.

15. **The hedged pair is compared by `sameness_2` and by nothing else.** `PAIRS.txt` includes
    `B12 B15`, so `sameness/pair_B12_B15_atria.txt` and `pair_B12_B15_mimo.txt` exist (5 and 7 ONLY
    lines on the first side, 5 each on the second, OPPOSITE 0). B3 scores the four matched pairs and
    B12 the three rewordings; no row reads these two files.

16. **An extra output directory.** `Language/results/L82 Arm B outputs/scratch/` (68 entries,
    including `scratch/frozen/run_check.py`, `checker_rules.pl` and `fingerprints.txt`, plus a copy of
    every built ledger) is not among the outputs P11 lists. Harmless, but it is in `MANIFEST.json`'s
    1198 hashed files and the plan does not name it.

17. **The cross-translator OPPOSITE lines that no row scores.** `sameness/across_B04.txt` and
    `across_B10.txt` each carry `OPPOSITE (1, ...)` — on B10 it is
    `A: line h_denied ... NOT [line h_rise BECAUSE line h_repaint]` against
    `B: line h_because ... line h_rise BECAUSE line h_reaches`, i.e. the two translators put a denial
    and a claim at the same place. The plan's "What is scored and what is only recorded" sends these to
    the diagnostic, so they are recorded here: the two translators differ at the exact point B2 tests.

18. **`Expected's direct lines:` printed empty.** `reports/ledger_B04_atria.new.txt` and
    `ledger_B04_mimo.new.txt` both print the NO CONNECTION block's `Expected's direct lines:` heading
    with nothing under it, because neither ledger asserts the expected fact outright. P5 describes the
    block but not the empty case, and no cell reads it.
