# PREMISE CHECK - L86 Test plan, fourth version

Checked 23 September 2026 by the same fresh Opus agent at extra effort. No repository file was
edited; no git command that writes was run. As in the third check I **ran** the runner rather than
only reading it — twice, and on the exact path that broke the third version.

**The plan's SHA-256** is `32a064ccbfe543597799aa35a3a21c16cb7044a8f482948eb692b0cf73d8e222`;
first sixteen **`32a064ccbfe54359`** — matches.
`L86_run.sh` **`a84d58af6b305d74`** ✓; `L86_compare.py` `0e9e2e6c866bdf33` ✓ and
`L86_strip.py` `b58d1550cff950f1` ✓, both unchanged.

**All three of my items are closed, and verified by running.** Nothing new is wrong.

---

## Part 1. The three items

I diffed the third and fourth versions whole. **Exactly the claimed changes and nothing else**: the
preamble's new paragraph, a new P12, P9's hash and description, the quotation rule's `...` gloss,
and E3's "against" and "charges" cells. No D, no other premise, and no other expectation moved.

### Item 1 — the summary's directory filter. CLOSED, and tested where it failed before.

Lines 37-38 of the runner are now

```python
rel = os.path.relpath(root, OUT)
if rel in ("scratch", "armA_src") or rel.startswith(("scratch" + os.sep, "armA_src" + os.sep)): continue
```

which is the component test I asked for, and line 49 adds
`reports found: %d of 112 expected` with ` -- SHORT: the table below is incomplete` when the count
is not 112.

**The test the coordinator asked for.** I re-ran `L86_run.sh` end to end on all 112 ledgers, with
`run_check_2.py` standing in for `run_check_3.py`, into
`.../scratchpad/premise_check_l86/v4out` — an absolute path containing `scratchpad`, and therefore
the substring `/scratch` that emptied the third version's table. It printed:

```
mocks: 4 ledgers, 4 s
armB: 32 ledgers, 61 s
armA/rig1: 36 ledgers, 38 s      armA/r45: 8 ledgers, 7 s
armA/l69: 23 ledgers, 24 s       armA/l72: 9 ledgers, 10 s
armA, all four sets together: 81 s
FAILED.txt entries across all sets: 0
SKIPPED.txt entries across all sets: 0
NO_OLD.txt entries across all sets: 0
reports found: 112 of 112 expected
reports: 112; compared SAME: 108; DIFFERENT: 0 (-); not compared: 4
block counts off (...): 50 (...)
```

**`reports found: 112 of 112 expected`, with the full table under it.** Where the third version
silently reported zero on this same path, the fourth reports everything. Item 1 is closed.

Three further tests on that run's output:

| test | result |
| --- | --- |
| (a) decoy `.third.txt` files planted in `scratch/`, `scratch/deeper/`, `armA_src/` and `armA_src/rig1/` | still `reports found: 112 of 112 expected` — all four skipped, at any depth, so the fix does not over-include |
| (b) one report deleted | `reports found: 111 of 112 expected -- SHORT: the table below is incomplete` ✓ exactly as P9 and E3 say |
| (c) the table's rows | **112 rows: 32 beginning `armB/`, 76 beginning `armA/`, 4 mocks** — precisely what E3 and E4 read; all 32 Arm B and all 76 Arm A rows read `SAME`; the four mock rows carry `-` in the compare column, correct, since no stored report exists for them |

### Item 2 — the `...` gloss. CLOSED.
The table header now reads "`...` for the rest of the line", dropping "as the second version prints
it". That fits the two block-row quotations, `- line g ...` (E5) and `- line u2 ...` (E7), which the
second version never prints.

### Item 3 — `NO_OLD.txt` in E3's cell. CLOSED.
E3's "Would count against" is now "Any `DIFFERENT`; any count off; any `FAILED.txt`, `SKIPPED.txt`
or `NO_OLD.txt` entry; a `reports found` line under 112", and its "Charges" adds "or the runner (P9)
on a short count". Both the entry counts and the `reports found` line are things the summary prints,
so both are decidable where E3 says it reads.

---

## Part 2. The premises

**Every hash in the plan verifies.** I recomputed all 29 named files in one pass — the driver and
the checker rules; the four rule ledgers' `.pl` and `.json`; the four second-version reports; the
L79 manifest and RUN SUMMARY; all eight mocks; the three instruments; the prose-reader brief and its
caller — **29 checked, 0 mismatches**.

**P12 is new and accurate.** It records the third check's end-to-end run: "all 108 stored reports
compared `SAME`, no `NO_OLD.txt`, `SKIPPED.txt` or `FAILED.txt` entry, 32 `JUMP.` and 31
`NO CONNECTION.` heads by the runner's regexes, 59 s on Arm B and 80 s on the four Arm A sets."
That is exactly what my third report recorded, and **this fresh run reproduces it** (61 s and 81 s,
within noise; 108 SAME; all three lists empty).

**P9's new description matches the file**: the summary "skips the `scratch` and `armA_src`
directories by path component relative to OUT_DIR and prints `reports found: N of 112 expected`,
with `SHORT` when N is under 112" — verified above, clause by clause.

**P6's Lesson L18 discipline is applied.** L18 exists in `records/Language - Lessons.md` and reads
"Plan L86's second version listed eight mock hashes that matched no file: they were typed into the
premise instead of computed... Fix: a hash in a premise is written by the script that computes it."
P6 now says "hashes computed by `sha256sum` on 23 September, not typed", and all eight match.

---

## Part 3. The D-spec and the expectations

D1 to D8 are byte-identical to the third version, which I passed: the term parser and constant
matching, D4's precedence and joins, D5's clause order and SHOWS note, D6's inner-term reason test
and `- lines` separator, D7's indentation, count line and both-battery-runs rule, D3's `peek(query,
removed)` with no `extra` and its named `removed=direct`. Nothing in them contradicts
`run_check_2.py`. E1, E2, E5, E6, E7 and E8 are unchanged; only E3's two right-hand cells moved.

The corpus facts they rest on all still hold, re-confirmed by this run: 32 `JUMP.` and 31
`NO CONNECTION.` heads over the 108; the mocks at 1+1, 1+0, 0+1 and 0+0; and the count invariant
proven by a proper negative test — with a stub that prints no blocks it flags exactly the 50 reports
carrying a JUMP or a NO CONNECTION and leaves the 62 that carry neither.

**E6 has ample room.** The second driver takes 61 s on Arm B and 81 s on the four Arm A sets against
a 300 s budget each: roughly five times and nearly four times the head-room the third version needs
for one checker run per goal across 63 findings.

---

## Two things to record, not to change

Neither can make a correct build look wrong or a wrong build look right, and no expectation rests on
either. **I list them as warnings rather than blockers, because fixing them now costs another full
check round, and fixing them *after* the freeze would be worse** — see the caution below.

- **The plan says "Lessons L10 to L17 apply" while its own preamble cites Lesson L18**, which exists
  and is the highest lesson, created by this episode. The plan in fact follows L18 (P6's hashes are
  computed, not typed); it just does not list it in the range.
- **`L86_run.sh` line 38 ends with the comment "(the pilot's manifest lesson, L84)". There is no
  Lesson L84.** The Lessons file runs L1 to L18, none of which is about substring-versus-component
  matching; L84 is an Arm B results-and-marking entry (`L84 Test results - Arm B ...`). The comment
  is inert — P9 describes the summary's behaviour, not its comments, and I verified that behaviour
  directly.

**Caution for after the freeze.** P9 pins the runner at `a84d58af6b305d74`. Tidying that comment
later would change the file's hash, make P9 false, and void E3 and E4 under the plan's own rule
("A premise the checker cannot find at its hash voids the expectation that rests on it"). So either
correct both now and re-cut the plan, or freeze as it stands and leave the tool alone. I recommend
the latter and a line in the log.

---

## FREEZE

Nothing must change first. The numbered list is empty.

All three items from the third check are closed and were verified by running the instrument, not by
reading it: the summary's filter now skips by path component and reports `112 of 112 expected` on
the very path that silently emptied the table before; the `SHORT` warning fires when a report is
missing; decoys inside `scratch/` and `armA_src/` are still skipped at any depth; the table carries
the 32 Arm B and 76 Arm A rows E3 and E4 read. Every one of the 29 files the plan names verifies at
its hash. The diff shows exactly the claimed changes and nothing else. The D-spec is unchanged from
the version I already passed and is buildable twice over, and the run shows the comparison
instrument holding all 108 stored reports byte-identical after normalisation, with time to spare
against E6.

The two Lesson citations above should be recorded in the log as known warts of the frozen text, and
the tool must not be edited afterwards without re-cutting the plan.
