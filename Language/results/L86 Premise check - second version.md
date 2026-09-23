# PREMISE CHECK - L86 Test plan, second version

Checked 23 September 2026 by the same fresh Opus agent at extra effort, by hand against the files.
No repository file was edited; no git command that writes was run. Runs were made only in a scratch
copy under `.../scratchpad/premise_check_l86/`.

**The plan's SHA-256** of
`Language/tests/L86 Test plan - the driver's third version, which names the general lines it examined under a JUMP and a NO CONNECTION, second version.md`
is `78a9cd24054b3e11956d5d149e28d90ca5dc89cf9e363f3fd3a68a18e1c0f7e6`.
First sixteen **`78a9cd24054b3e11`** — matches.

Sixteen of my seventeen items are answered, several of them well. Two new faults have been
introduced, one of which voids an expectation under the plan's own rule.

---

## Part 1. The premises, P1 to P11

### P1 `run_check_2.py` — FOUND, no difference
Hash `9a4b21cf771b1208` ✓; `checker_rules.pl` `7f10c6f40f8618d1` ✓, line 30 exactly
`holds(F) :- produced(F).` ✓. **Every quotation verbatim and every line number correct**, including
the ones v2 added: 314 (the JUMP text; v1's off-by-one "313" is fixed), 316-318, 320 (`abduce = ...`),
328, 329, 351, 353-355, 359, 222-230 with the side effects at 224 (`slowest[0]`), 225 (the raw log),
226 (`RAN OUT OF TIME on the question:`), 228 (`first_raw`), 229 (`out_of_time`), 111 (`run_query`),
114-115 (the removals), 133 (`sorted(set(...), key=str)`), 141-145, 153, 176 (`indented`),
200-202 (`general_lines`), 603 (the count line), 620 (the gauge printing `slowest[0]`).

### P2 the four rule ledgers — hashes ✓, quotations ✓, **two negative claims false**
All eight hashes match. Every quoted clause is verbatim at the line P2 gives (B06 Atria 58, 59, 37,
52; B06 Mimo 39, 40-42, 18, 29; B01 Atria 31, 33, 35, 25, 27, 29; B01 Mimo 35, 31, 33, 37), and
every mark and sentence is confirmed against the JSONs.

But:
- **B06 Atria.** P2 says "no clause has a head with `at_harbour` or `loaded_boat` (the strings occur
  only in `general`'s two clauses)". `loaded_boat` occurs at lines 48, 49 and 50, and **line 49 is
  `kind(loaded_boat, loaded_boat) :- line(loaded_boat).` — a clause whose head contains
  `loaded_boat`.** The `at_harbour` half is true; the `loaded_boat` half and the parenthetical are false.
- **B06 Mimo.** P2 says "no clause has a head with `loaded`, `at_harbour` or `turns_before_dawn`".
  **Lines 40 and 42 are `depends(crossed_bar_early(X), turns_before_dawn(tide)) :- ...` and
  `depends(crossed_bar_early(X), at_harbour(X)) :- ...` — heads containing both**; `loaded` is in the
  heads at lines 33 and 34.

What E1 needs is nonetheless true — I re-ran every goal (below) and all seven return no answer — but
E1's "Would count against" cell points at P2, and P2 as written is false.

### P3 the four second-version reports — FOUND, no difference (unchanged from v1, re-verified)

### P4 Arm A — FOUND, no difference
`MANIFEST.json` `f1c217a47f806a24` ✓ and `RUN SUMMARY.md` `f919bf23500e64d7` ✓. The manifest holds
389 hashes; **I recomputed all 389: 389 match, 0 bad, 0 missing**, and **all 76 `.new.txt` reports
are in it**. Counts 36 + 8 + 23 + 9 = 76 ✓, and **every one of the 76 `.pl` has its `.json` beside
it** (0 missing), which is what `L86_run.sh` needs. `RUN SUMMARY.md` line 37 is exactly
`| NEW driver, `patched/run_check_2.py`, all 76 | 110.0 |` ✓ and line 51 the `A1 HOLDS` sentence ✓.
"36 and 40 files" ✓. Ledger E's four clauses are verbatim at file lines 6-9, and
`holds(quoted(jon, letter)) :- line(3).` at line 5 ✓; its report's lines 4, 9 (empty
`  Effect's direct lines:`), 10 and 11 are verbatim ✓. Ledger A's line-5 clause is verbatim (at file
line 10; "line 5" is the ledger line id, which is right) ✓.

### P5 the 32 Arm B ledgers — FOUND, no difference
32 `.pl`, 32 `.json`, 32 `.new.txt`, all name-matched. `results/L82 Arm B outputs.run.log` line 6 is
`drivers took 80 s` ✓, and it does cover both drivers: `tools/L82_run_2.sh` lines 66-69 run
`run_check.py` and `run_check_2.py` on each ledger in one loop ✓. **This closes my item 13.**

### P6 the mocks — **ALL EIGHT HASHES WRONG**

| file | P6 (second version) says | on disk | P6 (first version) said |
| --- | --- | --- | --- |
| mock_none.json | `3ab6ec6d2ba7bd5b` | `7cc6924fb963a4f5` | `7cc6924fb963a4f5` |
| mock_none.pl | `64a8ec87d1ea2dd4` | `a5941efaf5dfc4a0` | `a5941efaf5dfc4a0` |
| mock_fires.json | `60f1c5c7d24f6bff` | `8358ad844038ea20` | `8358ad844038ea20` |
| mock_fires.pl | `39c6b9dd6e47bbdf` | `b9cc553f2cd7a09f` | `b9cc553f2cd7a09f` |
| mock_open.json | `8f4fd9d4c34f1c19` | `172b72eebc4f7674` | `172b72eebc4f7674` |
| mock_open.pl | `9d3da8ce0c3f2e3a` | `b286d2533e4d8e6c` | `b286d2533e4d8e6c` |
| mock_reason_in.json | `8b4ab5d8bfbcb3fa` | `16c77ac1245314f3` | `16c77ac1245314f3` |
| mock_reason_in.pl | `8a3b1f83a4f1bac2` | `4dd5d8dbd83f5c83` | `4dd5d8dbd83f5c83` |

The mock files are **byte-identical to the ones the first version named**, and the first version's
eight hashes were all correct. The second version's eight are new strings that match nothing on
disk. That it is a transcription slip rather than a change of file is confirmed by P6's own prose,
which describes each mock's clauses **correctly**: `mock_none` none; `mock_fires`
`produced(out(L)) :- line(g), kind(L, lamp), holds(burned_down(wick)).` with `kind(lamp, lamp) :- line(k).`
and `holds(burned_down(wick)) :- line(b).`; `mock_open`
`produced(out(L)) :- line(g), kind(L, lamp), holds(wick_of(W, L)), holds(burned_down(W)).`;
`mock_reason_in` `holds(dark(room)) :- line(g), holds(out(lamp)), holds(closed(shutters)).` with
`claim_since(e, dark(room), out(lamp))` and no clause for `closed(shutters)`. All four match the
files exactly. P6's behaviour claim (what the second driver prints, in order) I confirmed by running
in the first check and it holds.

**Under the plan's own rule — "A premise the checker cannot find at its hash voids the expectation
that rests on it" — this voids E5.**

### P7 `L86_strip.py` — FOUND, no difference
Hash ✓; **"thirteen lines" is now correct** (my item 14 closed); the description matches the code;
the round-trip on the four P3 reports and four mock reports returns each unchanged (re-verified).

### P8 `L86_compare.py` — FOUND, no difference. **My item 1 is closed.**
Hash `0e9e2e6c866bdf33` ✓. Read line by line, and tested.

### P9 `L86_run.sh` — FOUND at its hash; **two defects in the file** (below)

### P10 — correct; it restates my own verified finding.

### P11 the prose reader — FOUND, no difference
All four part-2 quotations are **verbatim** in
`results/L82 Arm B outputs/prose_reader/ledger_<id>_<provider>.response.txt`. The brief
`888a45f49248fba3` ✓ and `tools/ask_model_2.py` `9dbfd37f61a97c6b` ✓. The prompt shape is exactly
what `L82_run_2.sh` builds (lines 144-155): brief + passage + `===== THE REPORT =====` + the report
with its first line replaced by `REPORT for the passage above` ✓, and the Arm B call used
`--max-tokens 30000 --temperature 0.1` ✓ — which is what E8 specifies, and necessary, since
`ask_model_2.py`'s default temperature is 0.2 (line 75).

---

## The two new tools, read line by line

### `L86_compare.py` — sound
**Does its strip equal the strip tool's rule?** Yes. The `HEAD` regex on line 7 is byte-identical to
`L86_strip.py` line 6, and the loop body on lines 9-14 is the strip tool's lines 7-12 verbatim,
wrapped in `def strip(text)` reading from `text` instead of `open(sys.argv[1]).read()` and returning
`"\n".join(out)`. I also compared their **output** on three inputs (two hand-made third-version
reports and a real second-version report): **byte-identical in all three.**

`norm` (line 16) replaces `Slowest question: \d+\.\d+ seconds\.` — the driver writes `%.2f`, so the
pattern always matches — in **both** old and new, as "The instruments" says. Tested end to end:

| test | result |
| --- | --- |
| stored B06 Atria report vs a fresh second-driver run (differing only in the timing field) | `SAME`, exit 0 |
| stored report vs the same report with a told-world block inserted | `SAME`, exit 0 |
| stored report vs that plus a real regression (`[said,` → `[filled in,`) | `DIFFERENT at line 23:` with both lines, exit 1 |

So E3 and E4 can now be met by a correct build. **My item 1 is closed.**

### `L86_run.sh` — finds everything it must, with two defects

**Does it produce every output E3, E4, E6 and E7 read?** Per ledger: `<name>.third.txt`,
`.raw.txt`, `.err.txt` and `<name>.compare.txt` (lines 13, 15); `RUN SUMMARY.md` with one
`<set>: N ledgers, S s` line per set (line 17) and, from the Python block (lines 29-48), the
aggregate `compared SAME / DIFFERENT / not compared` line, the `block counts off` line, and a
per-report table of `JUMP.` heads, `NO CONNECTION.` heads, `General lines that could` headings,
`Reached without the reason:` headings and the compare verdict. E7 reads
`armA/rig1/ledger_E.third.txt`, which line 27 produces ✓. E6 reads the seconds lines ✓ (**this
closes my item 13's "no timing output"**). The counting regexes on lines 37-38 are anchored
`(?m)^\s*`, which is right: across the 108 second-version reports every `JUMP.` and every
`NO CONNECTION.` head starts its line, while the three `... whose verdict above is JUMP).` lines and
the eighteen chain rows `->  NO CONNECTION` do not.

**Does it find all 76 Arm A ledgers with their `.json`, and compare against the right reports?**
Yes. I checked name by name:

```
rig1  ledgers=36  reports=36   unmatched: none
r45   ledgers= 8  reports= 8   unmatched: none
l69   ledgers=23  reports=23   unmatched: none
l72   ledgers= 9  reports= 9   unmatched: none      TOTAL 76, 0 unmatched either way
Arm B ledgers=32, all matched;  mocks: the four .pl, each with its .json
```

The four tags on line 24 are `rig1`, `r45`, `l69`, `l72` and the pattern is `%s.new.txt` ✓, so
`ledger_X.pl` in each place is compared with `results/L79 Arm A outputs/<tag>/ledger_X.new.txt` ✓.
Both copies of ledger A (rig1 and l72) are run and each has its own stored report ✓ (E4's "including
both copies"). Every `.pl` has its `.json`, so line 12's `cp` never falls to `SKIPPED.txt`.

**Defect A — line 15 mislabels every genuine regression.**
```
[ -f "$old/$o" ] && python3 "$T/L86_compare.py" "$old/$o" "...third.txt" > "...compare.txt" 2>&1 || echo "$b: no old report $old/$o" >> "$OUT/$set_name/NO_OLD.txt"
```
`&&` and `||` are left-associative, and `L86_compare.py` **exits 1 on `DIFFERENT`**. So every real
difference also writes `<name>: no old report <path>` into `NO_OLD.txt`, although the old report
exists and was compared. I reproduced it exactly:

```
compare.txt first line: DIFFERENT at line 23:
NO_OLD.txt:             ledger_B06_atria: no old report .../reports/ledger_B06_atria.new.txt
```
(with a `SAME` comparison, `NO_OLD.txt` is correctly absent). The RUN SUMMARY counts are unaffected —
they read the `.compare.txt` first line — but the record is false, and a marker chasing a
`DIFFERENT` would be told the old report is missing. `NO_OLD.txt` is also not named in "The
instruments" (plan line 20).

**Defect B — `RUN SUMMARY.md` never reports `FAILED.txt`, `SKIPPED.txt` or `NO_OLD.txt`,** yet E3's
"Would count against" cell reads "any `FAILED.txt` or `SKIPPED.txt` entry" and E3 says it reads
`RUN SUMMARY.md`. The marker would have to open eight directories.

Two smaller notes: no combined Arm A total is printed, so E6's "the four Arm A sets together" must be
summed from four lines; and the aggregate `compared SAME: N` spans all 108 rows, so E3's "all 32 Arm
B reports `SAME`" must be read off the per-report table (which does carry it).

---

## E7 on ledger E — the expected strings follow from D1, D2, D4 and D5

`rigs/rig 1 - arguments/ledger_E.pl` has no cases, so `world_removed` is empty, and its
`Effect's direct lines` is empty, so `direct` — and hence D3's `removed` — is empty. I ran every
peek D4 prescribes:

| goal, after the head bindings (`P = jon`) | peek | D4 gives |
| --- | --- | --- |
| `holds(quoted(jon, letter))` | one answer, lines `['3']` | `holds (line 3)` |
| `holds(read(jon, letter))` | no answer | `no line says so` |
| `holds(told(Q, jon))` | `Q` still a variable | `open (Q)` |
| `holds(knows_words(Q))` | `Q` still a variable — **and it returns an answer, lines `['3','u1']`** | `open (Q)` |

The last row is the one that matters: **D4's stated precedence (open, then ran out of time, then
holds, then no line) is exactly what makes E7's `holds(knows_words(Q)): open (Q)` right**; without
it the line would read `holds (line 3, u1)`. My item 4 is closed and the mock/ledger that needed it
exists.

Order: D5 says "in the order the clauses stand in the ledger text… one entry per clause, each with
the same `- line` header", which gives u1 (file line 7), u2 (8), u2 (9) — E7's order ✓, and the
repeated `- line u2` header ✓ (my items 6 and 7 closed, with a real ledger behind them).

**SHOWS note placement.** u1's head is `holds(knows_words(P))`, so D1 makes it a SHOWS clause, and
D5 puts the note **after** the clause's goal lines: "one `\n        <goal line>` per body goal (D4),
and, for a SHOWS clause, one more line `\n        a SHOWS clause: it shows <effect> and does not
produce it`". E7 lists it after the goal line, with `<effect>` = `knows_words(jon)` ✓. Correct and
unambiguous.

**Placement.** D5 appends the block immediately after the `listed_lines(meta, "Effect's direct
lines", direct)` statement (line 318) and before the abduction (lines 320-329). Ledger E's report has
line 9 `  Effect's direct lines:` (nothing under it), line 10 `A single line that would close the
jump, ...` and line 11 `Lines that would also close it but are ruled out, ...`. The block therefore
sits between lines 9 and 10 ✓, which is what E7 says. My item 9 is closed, including the
"ruled out" line, which D5 now names.

No fourth clause matches: `denied(read(P, letter)) :- line(u3), ...` (file line 10) is excluded by
D1's give-up line, which names `denied` ✓. u1 is `usual case`, sentence 3; u2 `usual case`,
sentence 4 — E7 uses `<mark>` and `<N>` placeholders, consistent with the marks on file.

---

## E5's `mock_reason_in` strings now follow from D6

D6's test: "the reason's term equals, with spaces removed, the inner term of any body goal whose
goal is `holds(T)` or `produced(T)` (or the whole goal otherwise)". The reason is `out(lamp)`; the
body goal is `holds(out(lamp))`, of the form `holds(T)` with `T = out(lamp)`; the two are equal, so
the line is **`the reason's atom, out(lamp), is among these conditions`** ✓. **My item 3 is closed**
— the rule no longer compares an atom with a whole goal.

The rest of E5 also follows: `holds(out(lamp)): holds (line a)` (line `a` supplies it) and
`holds(closed(shutters)): no line says so` (no clause) ✓; `mock_open`'s
`kind(lamp, lamp): holds (line k)`, then `holds(wick_of(W, lamp)): open (W)` and
`holds(burned_down(W)): open (W)` — again by D4's open-first precedence, since
`holds(burned_down(wick))` exists but `W` is unbound ✓, and D2's "printed as written in the ledger's
clause, spaces and all" gives `holds(wick_of(W, lamp))` ✓; `mock_none`'s three `(none)` /
`(no route)` lines ✓; `mock_fires`'s `FOLLOWS, using:` with no block, by D8 ✓.

**E5 is nonetheless voided by P6's eight wrong hashes.**

---

## E1 and E2 re-checked under D3's `removed`

D3 makes the peeks use "the same `removed` list the check's `ask` used for its verdict", which for
these findings is `direct`. I re-ran every one with that removal:

| world, `removed` | goal | peek | D4 gives |
| --- | --- | --- | --- |
| harbourmaster_world, `['crossing']` | `kind(trawler, loaded_boat)` | no answer | `no line says so` |
| " | `holds(at_harbour(trawler))` | no answer | `no line says so` |
| " | `holds(turned(tide))` | `['tide_turned']` | `holds (line tide_turned)` |
| log_world, `['cross1']` | all four of E1's goals | no answer | `no line says so` ×4 |
| note_world, `['fi1']` | `holds(driven_through(flock, gate))` | one answer, `['al1','lo1']` | `holds (line al1, lo1)` |
| note_world, routes | `holds(in_field(flock,top_field))` | one answer, `['al1','al2','lo1']`, no `go1` | `- lines al1, al2, lo1` |
| shepherd_world, `['flock_top']` | `holds(in(flock,top_field))` | no answer | `(no route)`, and `(none)` |

No goal timed out. **Every string E1 and E2 quote follows from D1 to D6 as written.**

---

## Part 2 and Part 3 — what is left

Sixteen of seventeen items are answered. D2 now gives a term parser with "a constant equal only to
itself" and parses the checker's spaceless effect string (item 5); D4 fixes the precedence and the
multi-variable join (item 4); D4 and D6 fix the id join and route dedup and order (item 6); D5 fixes
clause order and the repeated line (item 7); D1 removes `%` comments first (item 8) and excludes
clauses of removed lines (item 10a); D5/D6 fix placement and D5 names the "ruled out" line (item 9);
D7 fixes the indentation and computes the count line on stripped findings (items 9, 10b); the plan
distinguishes its "general clause" from the code's `general_lines` (item 11); the table header fixes
the whole-line rule (item 12); P5 and E6 fix the baselines and the runner records the seconds
(item 13); P7 says thirteen (item 14); P2, P4, P10 and P11 add the missing premises (item 15); E8
records the mechanism honestly (item 16); and the L12 list exists (item 17). **Nothing in D1 to D8
now contradicts `run_check_2.py`.** Two builders would build very nearly the same thing.

What remains:

- **The table header says "a quoted string is a whole line once its leading spaces are removed", but
  several of the plan's own quotations are prefixes or carry placeholders**: `A single line that
  would close the jump` (E1, E7) is a prefix of `A single line that would close the jump, which
  nobody wrote: ...`; `It would take a line nobody wrote ...` (E2) ends in an ellipsis;
  `- line general [filled in, sentence 2]: <its text>`, `- line u1 [<mark>, sentence <N>]: <text>`,
  `- line u2 ...` and `- line g ...` carry placeholders. A marker applying the rule literally would
  mark a correct build against.
- **D6 does not fix the separator for `- lines <ids>`.** D4 fixes "joined by `, `" only for
  `holds (line <ids>)`; D6 says routes are "listed in the order of their joined ids" without saying
  what the join is. E2 writes `, `.
- **D3's `peek` signature omits `extra`**, so under a JUMP whose cause was supposed (`supposed`,
  line 309, passed at 310) the goal peeks do **not** grant the supposed cause: a condition the
  supposed cause would satisfy prints `no line says so`. That is a defensible choice and it does not
  change E1 or E7, but it should be said in words rather than left to the signature.
- **D3 says peek uses "the same `removed` list the check's `ask` used for its verdict", and a JUMP
  has several asks with different `removed`** (line 283 none, lines 284 and 310 `direct`). Naming
  the statement would close it.
- **D7 does not say whether the blocks are built in a world's second (`restored`) `battery` run.**
  Since the count line is computed on stripped findings, building them there is pure waste; the
  printed bytes are the same either way.
- **The Lesson L12 list contains a factual error.** It says "a supposed case with a JUMP or NO
  CONNECTION (only ledger H has a supposed case ...)". **Five ledgers carry a supposed case — H, K06,
  K09, N25B and P18** — and `run_check_2.py`'s own header, lines 88-89, which the plan cites as P1,
  says exactly that. Worse, the path is listed as *not exercised* when it **is**: ledger H's
  "Monday is gone" carries five NO CONNECTION findings, so the block will print inside a supposed
  case and E4 will compare it. The rest of the list checks out: no goal I peeked timed out; B01
  Atria has exactly one route; `mock_open` and ledger E each leave exactly one variable open; no
  ledger has both an actual-ledger general line and a JUMP or NO CONNECTION inside a world, so the
  D7 count line cannot move on this corpus.

---

## DO NOT FREEZE YET

1. **P6's eight mock hashes are all wrong.** Every one of `mock_none`, `mock_fires`, `mock_open`,
   `mock_reason_in` (`.json` and `.pl`) is on disk at the hash the **first** version named, and P6
   now gives eight different strings that match nothing. P6's prose descriptions of the four mocks
   match the files exactly, so the files are right and the hash list was mistyped. By the plan's own
   rule this voids E5. Restore the eight: `mock_none.json 7cc6924fb963a4f5`,
   `mock_none.pl a5941efaf5dfc4a0`, `mock_fires.json 8358ad844038ea20`,
   `mock_fires.pl b9cc553f2cd7a09f`, `mock_open.json 172b72eebc4f7674`,
   `mock_open.pl b286d2533e4d8e6c`, `mock_reason_in.json 16c77ac1245314f3`,
   `mock_reason_in.pl 4dd5d8dbd83f5c83`.
2. **P2's two negative claims about B06 are false.** B06 Atria line 49 is
   `kind(loaded_boat, loaded_boat) :- line(loaded_boat).`, a clause whose head contains
   `loaded_boat`, so "no clause has a head with ... `loaded_boat` (the strings occur only in
   `general`'s two clauses)" is wrong; B06 Mimo lines 40 and 42 are
   `depends(crossed_bar_early(X), turns_before_dawn(tide)) :- ...` and
   `depends(crossed_bar_early(X), at_harbour(X)) :- ...`, heads containing `turns_before_dawn` and
   `at_harbour`. Rewrite both as what E1 actually needs and what is true: **no clause has head
   `kind(trawler, loaded_boat)` or `kind(trawler, boat)`, and no `produced` or `holds` clause has a
   head term `at_harbour(...)`, `loaded(...)` or `turns_before_dawn(...)`** — which I confirmed by
   running all seven goals.
3. **Fix `L86_run.sh` line 15.** `L86_compare.py` exits 1 on `DIFFERENT`, and the
   `[ -f ] && python3 ... || echo "no old report" >> NO_OLD.txt` chain therefore writes a false
   "no old report" line for **every genuine regression** (reproduced). Test the file's existence in
   its own `if`, and let the compare's exit status alone. Name `NO_OLD.txt` in "The instruments"
   (plan line 20) while you are there.
4. **Have `RUN SUMMARY.md` report `FAILED.txt`, `SKIPPED.txt` and `NO_OLD.txt`.** E3's "Would count
   against" names the first two and E3 says it reads `RUN SUMMARY.md`, but the summary block
   (lines 43-47) writes only the SAME/DIFFERENT line, the block-counts line and the table.
5. **Correct the Lesson L12 list.** Five ledgers carry a supposed case — H, K06, K09, N25B and P18
   (`run_check_2.py` lines 88-89, the file P1 cites) — not only H; and the path "a supposed case with
   a JUMP or NO CONNECTION" **is** exercised, by ledger H's five NO CONNECTION findings inside
   "Monday is gone", which E4 will compare. Move it out of the not-exercised list, or say precisely
   that no *mock* exercises it.
6. **Reconcile the table header's whole-line rule with the plan's own quotations.** `A single line
   that would close the jump` (E1, E7) is a prefix; `It would take a line nobody wrote ...` (E2) ends
   in an ellipsis; `- line general [... ]: <its text>`, `- line u1 [<mark>, sentence <N>]: <text>`,
   `- line u2 ...` and `- line g ...` carry placeholders. Say that a quotation ending in `...` or
   containing a `<placeholder>` is matched as a prefix or pattern, not as a whole line.
7. **Fix the `- lines <ids>` separator in D6.** D4 fixes `, ` only for `holds (line <ids>)`; D6 uses
   `<ids>` and speaks of "their joined ids" without stating the join. E2 writes `, `.
8. **Say in D3 that the goal peeks do not carry `extra`,** so a JUMP's supposed cause is not granted
   and a condition it would satisfy prints `no line says so`. The signature implies it; the words
   should say it.
9. **Say in D3 which `ask`'s `removed` list the peeks copy.** A JUMP has several (line 283 with
   none, lines 284 and 310 with `direct`); name the statement.
10. **Say in D7 whether the blocks are built in a world's second (`restored`) `battery` run.** Since
    the count line is computed on stripped findings, building them there changes nothing and costs a
    checker run per goal; either decision is fine, but the builder should not have to guess.
11. **Have the runner print an Arm A total in seconds** (E6 reads "the four Arm A sets together"),
    and note that E3's "all 32 Arm B reports `SAME`" is read off the per-report table, since the
    aggregate `compared SAME: N` spans all 108 rows.

Items 1 and 3 are the only ones that would make a correct build look wrong or a wrong build look
right; items 2 and 5 are false statements in premises and in the Lesson L12 list; 6 to 11 are
wording. The instruments themselves are sound: `L86_compare.py` strips by exactly the strip tool's
rule and closes the wall-clock problem, and `L86_run.sh` finds all 76 Arm A ledgers with their
`.json` files and compares each against the right stored report.
