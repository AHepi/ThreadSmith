# SECOND MARKING — L79 Arm A

Independent second marker. I marked from the frozen plan, the frozen normaliser and the
outputs folder alone. I did not read the project's log, records, results files outside the
outputs folder, or any other marker's report. Beyond the outputs folder I opened only the
ledger `.json` files the expectations name (A2, A7) and the first few lines of the four new
files the plan says were built, to confirm they exist and carry a header.

## Hashes confirmed

| File | SHA-256 (full) | Plan's first 16 |
| --- | --- | --- |
| `Language/tests/L79 Test plan - Arm A, the ledgers in hand on the old rig and the new, third version.md` | `2e97300690dc39f797412ca4f343b67fff4ed7989e8a953f77c1665e506d4050` | `2e97300690dc39f7` — matches |
| `Language/tools/L79_normalise.py` | `ca62f449cef91a3b0f75980f586c52b43152f93520349b2e650cc2ccfc5ce7b4` | `ca62f449cef91a3b` — matches |

Outputs folder: 389 files besides `MANIFEST.json` — 76 `.old.txt`, 76 `.new.txt`, 76 `.a1.txt`,
156 `.err.txt`, 4 `.consequences_2.txt`, `RUN SUMMARY.md`. Per-subfolder: rig1 36, r45 8,
l69 23, l72 9 = 76 ledgers, as plan P14 states.

The four new files the plan says were built exist and carry a header (headers only; I did not
judge their code):

- `/home/user/ThreadSmith/Language/rigs/rig 1 - arguments/patched/run_check_2.py`, 636 lines, line 1 `# run_check_2.py`
- `/home/user/ThreadSmith/Language/authority/L80 The ledger language - complete definition, second version.md`, 156 lines, line 1 `# The ledger language`, line 3 `**Second version.** ...`
- `/home/user/ThreadSmith/Language/tools/consequences_2.py`, 196 lines, line 2 `"""Consequences, second version: ...`
- `/home/user/ThreadSmith/Language/tools/sameness_2.py`, 180 lines, line 3 `# sameness_2.py - the sameness test, second version.`

The old files are still present and untouched in place: `patched/run_check.py`,
`tools/consequences.py`, `tools/sameness.py`.

---

## A1 regression — MET

No entry of the "would count against" cell fired.

**Re-run, not the saved files.** I ran the frozen normaliser myself on every one of the 76
pairs (`L79_normalise.py <base>.old.txt <base>.new.txt`), not on the saved `.a1.txt`:

```
pairs=76 HOLDS=76 FAILS=0
```

All 76 printed `A1 HOLDS` on their first line and exited 0. The 76 saved `.a1.txt` files agree:
every one holds exactly `A1 HOLDS` (e.g. `/home/user/ThreadSmith/Language/results/L79 Arm A outputs/l69/ledger_P01.a1.txt` line 1:
`A1 HOLDS`), and all 76 have the same SHA-256, so none was edited.

**The two copies of ledger A.** Compared directly:

- `rig1/ledger_A.consequences_2.txt` and `l72/ledger_A.consequences_2.txt` — byte-identical.
- `rig1/ledger_A.old.txt` and `l72/ledger_A.old.txt` differ at one line only, line 28:
  - `rig1/ledger_A.old.txt:28`: `GAUGE: 11 lines said, 1 filled in, 1 usual case; 0 of 4 sentences went to the leftover bin (not checked). Slowest question: 0.07 seconds.`
  - `l72/ledger_A.old.txt:28`: `... Slowest question: 0.09 seconds.`
- `rig1/ledger_A.new.txt` and `l72/ledger_A.new.txt` differ at one line only, line 42:
  - `rig1/ledger_A.new.txt:42`: `GAUGE: 11 lines said, 1 filled in, 1 usual case; 0 bin entries over 4 sentences (not checked). Slowest question: 0.07 seconds.`
  - `l72/ledger_A.new.txt:42`: `... Slowest question: 0.08 seconds.`

The sole difference is the machine-timing string. No finding, line id, verdict, world, gauge
mark or gauge count differs. I also ran the normaliser across the copies
(`rig1/ledger_A.old.txt` vs `l72/ledger_A.new.txt`, and the reverse): both printed `A1 HOLDS`.
I read this as the two copies agreeing. It is flagged below as unpredicted, because the plan's
"must agree with itself" (P14) is not satisfied byte for byte.

**MANIFEST.json.** Far more than the ten asked for: I verified all 389 entries.

```
declared files: 389 entries: 389
mismatched: 0
missing on disk: 0
on disk not in manifest: 0
```

**The instrument is not vacuous.** I injected four faults into copies of real outputs and the
frozen normaliser failed each:

- a dropped `JUMP.` verdict line → `A1 FAILS` / `missing from new: ('', 'BECAUSE', '3', 'JUMP')`
- a changed head line id (`line 3` → `line 9`) → `A1 FAILS` / `added outside any world (not listed): ('', 'BECAUSE', '9', 'JUMP')`
- an unlisted sentence outside a world → `A1 FAILS` / `unlisted text in new: ('text', 'SOMETHING NOBODY PREDICTED about the ledger.')`
- a deleted `Fine.` prose line → `A1 FAILS` / `unlisted text in new: ('dropped from new', 'Fine. Nothing in the ledger makes ...')`

**Supporting checks.** `NO FAULT FOUND` appears in 39 old reports and in 0 new ones (D5).
`bin entries over` appears in all 76 new reports and `went to the leftover bin` in all 76 old
ones (D7). The gauge marks prefix (`N lines said, M filled in, K usual case`) is identical old
to new on all 76. The list of world headings is identical old to new on all 76.

## A2 sentences — MET

No entry of the "would count against" cell fired.

Exactly eight findings across the five reports of P8 — 2, 2, 2, 1, 1, as P8 says. Each is
followed by the `Claim line:` (or `Plan line:`) block, each printed line carries
`[mark, sentence N]`, and every N equals that line's `sentence` field in the ledger:

| Finding (path and line) | Block line quoted | Ledger field |
| --- | --- | --- |
| `l69/ledger_P01_correction1.new.txt:4` `NO CONNECTION. ...` | `:6` `  - line g [filled in, sentence 5]: [CLAIMED] line e SINCE line f; ...` | P01c1 `g`: mark `filled in`, sentence `5` |
| `l69/ledger_P01_correction1.new.txt:14` `NO CONNECTION. ...` | `:16` `  - line s [filled in, sentence 10]: [CLAIMED] line q SINCE line h; ...` | P01c1 `s`: `filled in`, `10` |
| `l69/ledger_P07_correction1.new.txt:4` `NO CONNECTION. ...` | `:6` `  - line g [filled in, sentence 5]: ...` | P07c1 `g`: `filled in`, `5` |
| `l69/ledger_P07_correction1.new.txt:14` `NO CONNECTION. ...` | `:16` `  - line s [filled in, sentence 10]: ...` | P07c1 `s`: `filled in`, `10` |
| `l69/ledger_P09.new.txt:4` `JUMP. ... produces increase(trees).` | `:6` `  - line p [said, sentence 6]: [CLAIMED] line m BECAUSE line o` | P09 `p`: `said`, `6` |
| `l69/ledger_P09.new.txt:13` `JUMP. ... produces yield(trees,fruit).` | `:15` `  - line q [said, sentence 6]: [CLAIMED] line n BECAUSE line o` | P09 `q`: `said`, `6` |
| `l69/ledger_P14_correction1.new.txt:4` `JUMP. ... produces spreads(helping).` | `:6` `  - line h [filled in, sentence 8]: [CLAIMED] line g BECAUSE line f; ...` | P14c1 `h`: `filled in`, `8` |
| `l69/ledger_P16.new.txt:4` `CANNOT TELL whether the plan can work. ...` | `:6` `  - line b [filled in, sentence 3]: [CLAIMED] Do [make life counter-friction] SO THAT [government stops]; ...` | P16 `b`: `filled in`, `3` |

The supporting lines inside the same blocks also match the ledgers' fields: P01c1/P07c1
`f` said/5, `e` said/5, `h` said/6, `q` said/10; P09 `o` said/6, `m` said/6, `n` said/6;
P14c1 `f` said/8, `g` said/8. (Ledgers read from
`/home/user/ThreadSmith/Language/results/L69 Return - L66 run by OpenAI Codex/rigs/rig 1 - arguments/*.json`,
whose `lines` is a dict keyed by line id.)

The five old reports contain 0 lines beginning `  - line`, as P8 states, so these blocks are
wholly new. Beyond the five, all 42 `JUMP` / `NO CONNECTION` / `CANNOT TELL` findings across
all 76 new reports carry their D4 label set (16 JUMP, 23 NO CONNECTION, 3 CANNOT TELL, 0
missing a label), and no other verdict word is followed by one.

## A3 the tie — MET

No entry of the "would count against" cell fired.

P14 correction 1 (`l69/ledger_P14_correction1.new.txt`):

```
14:  Set aside, because your ledger says they came from what was changed: line(s) g.
15:  Set aside: line g [said, sentence 8] (tied by line h [filled in, sentence 8], whose verdict above is JUMP).
16:  NOTE: leans on lines you did not write: h.
17:  Your what-if HOLDS.
```

The verdict is unchanged (`l69/ledger_P14_correction1.old.txt:9` `  Your what-if HOLDS.`). `g` is
named as set aside; `h`'s verdict is printed as `JUMP`, matching the head at
`l69/ledger_P14_correction1.new.txt:4`; `h` is marked `filled in`, so the NOTE is due and present.

P11 (`l69/ledger_P11.new.txt:5` `  Your what-if HOLDS.`; old `:7` the same) and P13
(`l69/ledger_P13.new.txt:5` `  Your what-if FAILS.`; old `:7` the same). Neither new report
contains any `Set aside` line or any `NOTE:` line — I grepped both files for
`Set aside` and `NOTE: leans on` and got nothing.

## A4 worlds in consequences — MET

No entry of the "would count against" cell fired, on the reading given below.

**Ultra's T07-B**, `l72/ledger_T07B.consequences_2.txt`. No `contradiction(` anywhere in the
file — in particular the actual section (lines 3–24) has none, against P5's record of the old
tool printing `  contradiction(open(door))   <- lines actualshut, storyopen`. The world section
is present and named `nora_story` with the story's facts:

```
26:INSIDE 'nora_story' (a told world, looked at alone): WHAT FOLLOWS FROM THE WORLD'S OWN LINES
29:    holds(open(door))   <- lines storyopen
31:    kind(door,door)   <- lines storydoor
```

**Mine**, `rig1/ledger_T07B.consequences_2.txt`. No `contradiction(` anywhere. World section
named as P3 says mine names it:

```
15:INSIDE 'Nora's story' (a told world, looked at alone): WHAT FOLLOWS FROM THE WORLD'S OWN LINES
18:    holds(open(door))   <- lines 2
```

**Ledger A**, `rig1/ledger_A.consequences_2.txt` (and `l72/...`, byte-identical). The derived
list is exactly eight entries, at lines 4, 7, 12, 15, 18, 20, 24, 28:

```
 4:  changes(move(thermometer),reading(thermometer))   <- lines 4, k1
 7:  contradiction(dies(door_plant))   <- lines 2, 5, 7, 9
12:  depends(dies(balcony_plants),reached(the_cold,balcony_plants))   <- lines 1, 5
15:  depends(dies(door_plant),reached(the_cold,door_plant))   <- lines 2, 5
18:  depends_on(reading(thermometer),reached(the_cold,thermometer))   <- lines 11
20:  holds(dies(door_plant))   <- lines 2, 5, 7
24:  produced(dies(balcony_plants))   <- lines 1, 5, 6
28:  produced(dies(door_plant))   <- lines 2, 5, 7
```

The two facts P15 names as appearing under both heads —
`depends(dies(balcony_plants),reached(the_cold,balcony_plants))` and
`depends(dies(door_plant),reached(the_cold,door_plant))` — are present once each, under
`depends`, and their `depends_on` twins are gone. Ten minus two is eight, and the header at
line 1 says `8 derived (not stated by any line)`.

**Two scoping notes I record rather than fire on.** (i) The "would count against" phrase
"A `contradiction(` in an actual section" cannot be meant to reach ledger A, whose actual
section must keep `contradiction(dies(door_plant))` (line 7) if its list is to be "the old ten
with the two `depends_on` twins gone: exactly otherwise identical", and whose report is a
contradiction report by P9. I read that phrase as belonging to the T07-B sentence it follows.
(ii) "otherwise identical" is checkable here only against P15's own words, since the L65
baseline file is outside the outputs I may open and `RUN SUMMARY.md:26` records
`consequences.py (old) runs | 0 -- its baseline exists (plan P5, P15)` — no fresh old-tool run
sits in these outputs. On P15's words the eight are exactly right.

## A5 inside worlds — MET

No entry of the "would count against" cell fired.

**Ultra's T10-D**, `l72/ledger_T10D.new.txt`:

```
17:INSIDE 'account_world' (a told world, looked at alone): no contradiction.
18:  BECAUSE-claim on line because [said, sentence 1]: "[TOLD in world account_world] line dry BECAUSE line opening".
19:  JUMP. Even granting the stated cause, nothing in the ledger produces stayed_dry(letter).
26:  0 findings inside 'account_world' would not stand if the actual ledger's general lines were available.
```

The actual section (lines 3–15) holds only the `OUTCOMES:` block: no world finding printed
there. P1 records the old report's `because` string as absent; `l72/ledger_T10D.old.txt` has no
`because` line, and the new one has it inside the world only.

**Ultra's T11-B**, `l72/ledger_T11B.new.txt`:

```
20:INSIDE 'inspector_world' (a told world, looked at alone): no contradiction.
21:  SINCE-claim on line since [said, sentence 1]: "[TOLD in world inspector_world] line toldreturn SINCE line toldburning". (A reason to expect, not a cause.)
22:  NO CONNECTION. Nothing in the ledger leads from the reason to what is expected.
35:  0 findings inside 'inspector_world' would not stand if the actual ledger's general lines were available.
```

The DENIED BECAUSE block of P2 is in the actual section and unchanged in its text:

```
3:DENIED BECAUSE on line notbecause [said, sentence 2]: "[CLAIMED] NOT [line return BECAUSE line burning]".
4:Fine. Nothing in the ledger makes burning(lamp) produce returned(visitor). The effect itself still stands; only the cause is denied.
```

against `l72/ledger_T11B.old.txt:5-6`, which carry the same two lines. The head gains only the
`[said, sentence 2]` token D4 licenses; line 4 is character-for-character the old line.

**Ultra's T07-B**, `l72/ledger_T07B.new.txt`. The world section holds no finding — it is the
heading, the count line and the outcomes block and nothing else:

```
17:INSIDE 'nora_story' (a told world, looked at alone): no contradiction.
18:  0 findings inside 'nora_story' would not stand if the actual ledger's general lines were available.
19:  OUTCOMES:
```

and every line of that world's outcomes block reads `asked, nothing found`,
`not asked, no line of that kind` or `not asked, nothing to ask` (lines 20–30).

**Ultra's T07-D**, `l72/ledger_T07D.new.txt`. The D6 heading, naming the same two lines as the
old report, and not moved out of the world:

```
17:INSIDE 'nora_description' (a told world, looked at alone): CONTRADICTION about open(door,described_moment), which the world's own lines give.
18:  - line notopen [said, sentence 1]: [TOLD in world nora_description] NOT [door is open at stage described_moment], in the same context and respect as line open
19:  - line open [said, sentence 1]: [TOLD in world nora_description] door is open at stage described_moment
20:  Every line needed is inside the world.
21:  0 findings inside 'nora_description' would not stand if the actual ledger's general lines were available.
```

Old, `l72/ledger_T07D.old.txt:3-5`, names `notopen` and `open` — the same two lines — under
`UNDER THE SUPPOSITION 'nora_description': CONTRADICTION about open(door,described_moment), which arises only once the supposed lines are added.`
The three supposition phrases are gone from this told case (`THE SUPPOSITION UNDOES ITSELF` at
old line 6 is replaced by `Every line needed is inside the world.`), as D6 requires. Its actual
outcomes block reads `contradictions: asked, nothing found` (line 4) and the world's reads
`contradictions: asked, 1 found` (line 23), so the finding is counted where it sits.

All four outside counts read `0`.

## A6 F15 and F09 — MET

No entry of the "would count against" cell fired.

N18-A, `r45/ledger_N18A.new.txt`:

```
13:Fine. Nothing in the ledger makes fleaming_happened produce opening_happened. The effect itself still stands; only the cause is denied.
14:YOU CLAIM AND DENY THE SAME CAUSE: line 3 [said, sentence 1] claims opening_happened BECAUSE fleaming_happened, and line 4 [said, sentence 1] denies it.
```

Lines 3 and 4 are the pair P11 records (`claim_because(3, opening_happened, fleaming_happened)`
and `denied_because(4, ...)`), the flag sits after the DENIED BECAUSE block, and the `Fine.`
line is kept, character for character against `r45/ledger_N18A.old.txt:7`.

N18-B, `r45/ledger_N18B.new.txt`: no `YOU CLAIM AND DENY` line anywhere in the file. It keeps
its DENIED BECAUSE block (`:3`, `:4`) unchanged apart from the D4 token.

N25-A, `r45/ledger_N25A.new.txt:5` `  Your what-if HOLDS.` — the same verdict as
`r45/ledger_N25A.old.txt:7`; no `Set aside` line anywhere in the file.
N25-B, `r45/ledger_N25B.new.txt:5` `  Your what-if FAILS.` — the same as
`r45/ledger_N25B.old.txt:5`, and its supposition contradiction is intact at `:21`.

## A7 outcomes and gauge — MET

No entry of the "would count against" cell fired. All six numbers checked, each against the
ledger the plan names.

| Number | Output line | Ledger evidence |
| --- | --- | --- |
| my T10-B | `rig1/ledger_T10B.new.txt:24` `  sentences with no line: 1` | `rigs/rig 1 - arguments/ledger_T10B.json`: 3 sentences, lines on 1 and 2 → 3 has none = 1 |
| my T05-B | `rig1/ledger_T05B.new.txt:19` `  sentences with no line: 1` | `rigs/rig 1 - arguments/ledger_T05B.json`: 3 sentences, lines on 2 and 3 → 1 has none = 1 |
| Ultra's T05-B | `l72/ledger_T05B.new.txt:19` `  sentences with no line: 0` | Ultra's `ledger_T05B.json`: 3 sentences, lines on 1, 2 and 3 → 0 |
| ledger A, copy 1 | `rig1/ledger_A.new.txt:44` `  sentences with no line: 0` | `rigs/rig 1 - arguments/ledger_A.json`: 4 sentences, lines on 1, 2, 3, 4 → 0 |
| ledger A, copy 2 | `l72/ledger_A.new.txt:44` `  sentences with no line: 0` | Ultra's `ledger_A.json`: same → 0 |
| T10-D outcomes | `l72/ledger_T10D.new.txt:5` `  because claims: not asked, no line of that kind` and `:29` `    because claims: asked, 1 found` | the BECAUSE claim is a world line, not an actual one |

The two T10-D lines are the strings A7 quotes; the world one carries four leading spaces
rather than two, because D2 indents the whole world section by two. Noted below, not fired on.

The ledgers also bear out D7's `bin sentences` line: Ultra's T05-B and T10-D carry a structured
`bin` and print `  bin sentences: 1`; my T10-B, my T05-B and both ledger A copies have only
`leftover` and print `  bin sentences: not recorded (free-text bin)` with
`  sentences with no line and no bin entry: not recorded`.

**Outcomes-block coverage, all 76 reports and all 11 world sections.** Every one of the 76 new
reports has an actual `OUTCOMES:` block; every one of the 11 world sections has its own
`OUTCOMES:` block and its outside-count line. Checked mechanically: the actual blocks carry
the twelve D5 names in D5's order, the world blocks carry the same eleven with `what-ifs`
absent, and all 1033 outcome values (76 × 12 actual + 11 × 11 world) are one of D5's five forms. No `contradictions:` or
`exceptions:` line anywhere reads `not asked`, and `not asked, nothing to ask` appears only on
`the chain`, `two usually lines`, `added lines` and `what-ifs`, exactly as D5 sets out. No line
reads `ran out of time`.

The 11 world sections are: `l69/ledger_P18.new.txt:17`, `l72/ledger_T07B.new.txt:17`,
`l72/ledger_T07D.new.txt:17`, `l72/ledger_T10D.new.txt:17`, `l72/ledger_T11B.new.txt:20`,
`r45/ledger_N25B.new.txt:21`, `rig1/ledger_H.new.txt:92`, `rig1/ledger_K06.new.txt:22`,
`rig1/ledger_K09.new.txt:17` and `:32`, `rig1/ledger_T07B.new.txt:17`.

## A8 time — MET

No entry of the "would count against" cell fired.

The only clock in the outputs is the runner's, `RUN SUMMARY.md`:

```
36:| OLD driver, `patched/run_check.py`, all 76 | 97.0 |
37:| NEW driver, `patched/run_check_2.py`, all 76 | 110.0 |
38:| Both passes together | 207.0 |
```

207.0 s is 3 min 27 s, inside the 10 minutes. The container is the one the plan names:

```
44:- `swipl --version`: `SWI-Prolog version 9.0.4 for x86_64-linux`
45:- `/home/claude/sCASP/scasp --version`: `% s(CASP): version 1.1.4 on SWI-Prolog 9.0.4`
```

Corroboration, such as it is: the old pass at 97.0 s sits against the plan's own "100 s for all
76, as the checker timed it"; the per-ledger `Slowest question:` figures in the gauge lines
(76 old, 76 new; max 0.14 s old, 0.15 s new) are consistent with a fast pass, though they
measure one query each and cannot be summed into a wall clock; and when I first listed the
folder the file times ran 11:35 to 11:38 across old, new, `.a1` and `consequences_2`, a span of
about four minutes for the whole run.

I mark this MET, with the limit stated plainly: the deciding figure is self-reported by the
runner and the outputs carry no independent total clock. A marker cannot re-time a run from
saved text. (Note also that the file mtimes were uniform at 11:41:52 when I checked them a
second time in this read-only session, so mtimes are not sound evidence here; I rely on the
summary.)

---

## What the outputs hold that the plan did not predict

Nothing here changes a mark. Each is something a reader of the plan would want to know.

**1. D4's `  - (none)` is never printed; nine D4 labels head an empty list.** D4 says
"`  Effect's direct lines:` then the lines that alone state the effect, or `  - (none)`". The
string `- (none)` occurs nowhere in any of the 76 new reports. Instead the label is printed
with nothing after it:

- `rig1/ledger_E.new.txt:9` `  Effect's direct lines:` — next line is `:10` `A single line that would close the jump, ...`
- `rig1/ledger_J.new.txt:9` and `:17` `  Effect's direct lines:` — next line blank
- `rig1/ledger_K14.new.txt:9` `  Effect's direct lines:` — next line blank
- `l69/ledger_P01.new.txt:17` `  Reason's lines:` — next line is `:18` `  Expected's direct lines:`, itself empty, next line `:19` `It would take a line nobody wrote, ...`
- `rig1/ledger_H.new.txt:43`, `:62`, `:159` `  Reason's lines:` — each followed immediately by `Expected's direct lines:`

The sibling placeholder D4 also names, `  - (no line supports the cause)`, *is* printed, at
`rig1/ledger_E.new.txt:8`, `rig1/ledger_J.new.txt:8` and `rig1/ledger_J.new.txt:16`. So one of
D4's two placeholders was built and the other was not. None of the nine sits in A2's five
reports, so A2 is untouched; A1 is untouched because the normaliser classes the bare label as
"D4 searched lines".

**2. The two copies of ledger A are not byte-identical.** P14 says "the duplicate ledger A is
run twice and must agree with itself", and A1's "would count against" cell names "the two
copies of ledger A disagreeing". They differ, in one respect only, in each of the two report
files: `rig1/ledger_A.old.txt:28` ends `Slowest question: 0.07 seconds.` against
`l72/ledger_A.old.txt:28` `... 0.09 seconds.`, and `rig1/ledger_A.new.txt:42` `... 0.07 seconds.`
against `l72/ledger_A.new.txt:42` `... 0.08 seconds.` I did not fire on it: the difference is
the machine's clock, not the ledger's reading, and the normaliser does not see it (it keeps only
the marks prefix of the gauge line). But the plan's words, read literally, are not met, and a
second marker should not silently decide that for the record.

**3. One line inside a world section is not indented, and it closes the section for the
instrument.** `r45/ledger_N25B.new.txt:24` reads

```
24:It cannot stand together with line(s) m1 that you claim outright.
```

with no leading spaces, between the indented described lines (`:22`, `:23`) and the indented
count line (`:25`) and world outcomes block (`:26`–`:37`). It is the only line in any of the 11
world sections that is not indented; `rig1/ledger_H.new.txt:96-97` shows the same kind of
trailing prose (`THE SUPPOSITION UNDOES ITSELF ...`, `NOTE: ...`) correctly indented inside its
supposed case. This matters beyond looks: the frozen normaliser treats a non-indented,
non-world-head line as closing a world (its line 91), so for N25-B it books the world's count
line and the world's outcomes block as if they stood outside the world. A1 still holds on
N25-B, because both are listed extra kinds either way, but the instrument's world tracking is
wrong on this one file and would not notice a world finding that followed line 24.

**4. Ledger A's consequences_2 header does not add up, and one derived entry contradicts the
tool's own stated rule.** `rig1/ledger_A.consequences_2.txt:1`:

```
LEDGER A tomato: 13 lines; 9 facts stated directly; 19 facts found; 8 derived (not stated by any line)
```

9 + 8 = 17, not 19. The gap of two is presumably the two `depends_on` twins folded into
`depends` — which is what A4 wants — but the header reports them as found and then in neither
column. The other three consequences_2 headers do add up (`l72/ledger_T07B...:1` 7 = 7 + 0;
`rig1/ledger_T07B...:1` 2 = 2 + 0).

Separately, the entry at `rig1/ledger_A.consequences_2.txt:18`:

```
18:  depends_on(reading(thermometer),reached(the_cold,thermometer))   <- lines 11
```

is the only entry in the DERIVED list cited to exactly one line. The plan's own description of
`consequences_2.py` says "a found fact is 'stated' when some justification for it uses exactly
one line" — so by that rule this fact is stated, not derived, and should not be in a list headed
"not stated by any line". And the removal block shows both forms exist for this fact:

```
76:      no longer: depends(reading(thermometer),reached(the_cold,thermometer))
77:      no longer: depends_on(reading(thermometer),reached(the_cold,thermometer))
```

so by the plan's other rule — "a fact under both `depends` and `depends_on` is printed once, as
`depends`" — the entry should read `depends(...)`, not `depends_on(...)`. It looks wrong to me
on both counts. A4 still holds, because P15 records the old ten as containing this same
`depends_on` entry and not its `depends` twin, so the eight are "the old ten with the two
twins gone"; the oddity is inherited, not introduced.

**5. A7's world-block string is quoted at the wrong indent.** A7 asks for
"the `account_world` block has `  because claims: asked, 1 found`" (two spaces). The built
report gives four, `l72/ledger_T10D.new.txt:29`, because D2 indents the whole world section by
two and D5's own form already carries two. Every world outcomes line in every report is
four-space indented. The plan's two expectations are consistent with each other; only A7's
quoted string is not.

**6. D3's tie block also fires on ledgers the plan never mentions, once with a verdict the
plan's examples do not show.** Besides P14 correction 1, the `Set aside:` line appears at
`l69/ledger_P14.new.txt:15` (the uncorrected P14, with the same `h [filled in, sentence 8]`
tie and the same NOTE at `:16`), at `rig1/ledger_K22b.new.txt:24` (verdict `JUMP`), and at
`rig1/ledger_K22.new.txt:12`:

```
12:  Set aside: line 2 [said, sentence 1] (tied by line 3 [said, sentence 1], whose verdict above is FOLLOWS).
```

`FOLLOWS` is on D3's list of five, so this is inside the rule; the plan simply never shows it.
`rig1/ledger_H.new.txt:97` gains an indented D3-form NOTE inside the supposed case. None of
these is a ledger any expectation names, and A1 holds on all of them.

**7. D8 has no outcomes line of its own.** N18-A's flag at `r45/ledger_N18A.new.txt:14` is
counted nowhere in the outcomes block at `:16`–`:28` — `because claims: asked, 1 found`,
`denied because: asked, 1 found`, and nothing for F15. D5's list of twelve names has no slot
for it, so this follows the plan; it means the outcomes block is not a complete tally of what
the report prints.

**8. `sameness_2.py` was built but nothing in the outputs exercises it.** The plan's "What is
built" section builds `tools/sameness_2.py` (present, 180 lines), and the builders' smoke case
is T07-D's pair, but no expectation A1 to A8 mentions it and the outputs folder holds no
sameness output of any kind. Its change is untested by this arm. `RUN SUMMARY.md:25-26` records
`consequences_2.py` runs as 4 and old `consequences.py` runs as 0.

**9. Small things in the built reports that are the plan's own template, recorded so no one
reads them as faults later.** `l69/ledger_P16.new.txt:22` reads `GAUGE: 1 lines said, ...` and
`:26` `  filled in against said: 2/1` — a ledger with more filled-in lines than said ones;
`l72/ledger_T10D.new.txt:40` reads `1 bin entries over 1 sentences`. Both are D7's wording
applied literally.

**10. RUN SUMMARY.md's counts are all reproducible.** 76 ledgers (36/8/23/9), 76 old, 76 new,
76 comparisons, 76 `A1 HOLDS`, 0 `A1 FAILS`, 4 `consequences_2.py` runs, 0 non-empty stderr —
I confirmed each against the folder. All 156 `.err.txt` files are zero bytes.
