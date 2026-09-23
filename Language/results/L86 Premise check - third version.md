# PREMISE CHECK - L86 Test plan, third version

Checked 23 September 2026 by the same fresh Opus agent at extra effort. No repository file was
edited; no git command that writes was run. This time I did not only read `L86_run.sh` — I **ran
it end to end on all 112 ledgers** in a scratch root, with `run_check_2.py` copied in as a stub
`run_check_3.py`. That run found a defect that reading had missed, in both the second version and
this one.

**The plan's SHA-256** is `b6086057413da27dffdbac80d494ae65908f2063e94f2ab77f5936a03a6746be`;
first sixteen **`b6086057413da27d`** — matches.
`L86_run.sh` `8c87900efac4a44f` ✓, `L86_compare.py` `0e9e2e6c866bdf33` ✓ (unchanged),
`L86_strip.py` `b58d1550cff950f1` ✓ (unchanged).

**All eleven of my items are closed.** One new defect, which predates this version, must be fixed.

---

## Part 1. The eleven items

I diffed the second and third versions whole. **Exactly the eleven items changed and nothing else**:
the preamble, D3, D4, D6, D7, "The instruments", P2, P6, P9, the table header's quotation rule, and
the Lesson L12 list. No expectation row's text moved.

**1. P6's eight mock hashes — CLOSED.** All eight now match the files on disk exactly:
`mock_none.json 7cc6924fb963a4f5`, `mock_none.pl a5941efaf5dfc4a0`,
`mock_fires.json 8358ad844038ea20`, `mock_fires.pl b9cc553f2cd7a09f`,
`mock_open.json 172b72eebc4f7674`, `mock_open.pl b286d2533e4d8e6c`,
`mock_reason_in.json 16c77ac1245314f3`, `mock_reason_in.pl 4dd5d8dbd83f5c83`. P6 now records that
they were computed by `sha256sum` and not typed, and Lesson L18 holds the reason. E5 is no longer
voided.

**2. P2's two negative claims — CLOSED.** Both are rewritten as what E1 needs, and I checked every
clause head in both ledgers programmatically:
- B06 Atria: `kind(trawler, trawler) :- line(trawler).` (line 37) is **the trawler's only kind
  clause** ✓; **no clause has head `kind(trawler, loaded_boat)`** ✓; line 49 is
  `kind(loaded_boat, loaded_boat) :- line(loaded_boat).` ✓ exactly as quoted; **no `produced` or
  `holds` clause has head term `at_harbour(...)`** ✓.
- B06 Mimo: `kind(trawler, trawler) :- line(trawler).` (line 18) ✓; **no clause has head
  `kind(trawler, boat)`** ✓; **no `produced` or `holds` clause has head term `loaded(...)`,
  `at_harbour(...)` or `turns_before_dawn(...)`** ✓; and the three `depends` clauses at 40-42 do
  carry those terms as second arguments, exactly as P2 now says ✓.

**3. The runner's compare chain — CLOSED.** Lines 16-17 are now
`if [ -n "$old" ]; then o=...; if [ -f "$old/$o" ]; then python3 L86_compare.py ... ; else echo "no old report" >> NO_OLD.txt; fi; fi`
— the comparison runs only inside the `if [ -f ]` and its exit code is not read. I ran the new lines
verbatim against a deliberately differing report: `compare.txt` reads `DIFFERENT at line 23:` and
**`NO_OLD.txt` is absent** ✓. The full 112-ledger run wrote 108 `.compare.txt` files with
`NO_OLD.txt` empty throughout ✓.

**4. `FAILED.txt`, `SKIPPED.txt`, `NO_OLD.txt` in the summary — CLOSED.** Line 32 emits one count
line each across all six set directories. Tested with all three lists absent: each prints `0`
cleanly (`grep -c .` on empty input exits 1, but the value is captured and `set -e` is not on) ✓.
The real run printed `FAILED.txt entries across all sets: 0`, and the same for the other two.

**5. The Lesson L12 list — CLOSED.** It now names the five Arm A ledgers that carry a supposed case
(H, K06, K09, N25B, P18), cites P1's header lines 88 and 89 — which read exactly "Of the 76 ledgers
only H, K06, K09, N25B and P18 carry a supposed case" ✓ — and says ledger H's case carries NO
CONNECTION findings, so E4's comparison exercises the path and only the *string* is unexercised.
That is now true and precise.

**6. The quotation rule — CLOSED** (one wording slip, item 2 of the list below). The header now
excepts `<its text>`, `<mark>`, `<N>`, `<text>`, `...` and the `A single line that would close the
jump` prefix. I enumerated every quotation in E1, E2, E5 and E7: all are covered.

**7. D6's `- lines` separator — CLOSED**: "the ids in the checker's order, joined by `, `".

**8. D3 carries no `extra` — CLOSED**: "with no `extra` (so a JUMP's supposed cause is not granted
to the goals)".

**9. Which `removed` the peeks copy — CLOSED**: D3 names `removed=direct` for D5's goal peeks
(P1 lines 284 and 310), for D6's goal peeks (line 342) and for D6's route peek; D4 now writes
`peek("<goal>", direct)`.

**10. The blocks in both `battery` runs — CLOSED**: D7 says they are built in both, stripped before
the comparison, and names the cost.

**11. The Arm A total and the per-report table — CLOSED**: line 25 sets `TA` and line 31 writes
`armA, all four sets together: N s`; "The instruments" and E3 now say E3 reads its 32 Arm B rows and
E4 its 76 Arm A rows off the per-report table, "since the aggregate spans all 112 reports" — and
4 + 32 + 76 = 112 ✓.

---

## Part 2. The end-to-end run, and what it found

I built a scratch root (symlinks to `tools`, `tests`, `results`; a copy of the rig with
`run_check_2.py` copied in as `run_check_3.py`) and ran `L86_run.sh` for real. What it printed:

```
run started 2026-09-23T02:22:42Z; run_check_3.py 9a4b21cf771b1208
mocks: 4 ledgers, 4 s
armB: 32 ledgers, 59 s
armA/rig1: 36 ledgers, 39 s
armA/r45: 8 ledgers, 7 s
armA/l69: 23 ledgers, 25 s
armA/l72: 9 ledgers, 9 s
armA, all four sets together: 80 s
FAILED.txt entries across all sets: 0
SKIPPED.txt entries across all sets: 0
NO_OLD.txt entries across all sets: 0
reports: 0; compared SAME: 0; DIFFERENT: 0 (-); not compared: 0
block counts off (...): 0 (-)

| report | JUMP. | NO CONNECTION. | General lines blocks | Reached blocks | compare |
| --- | --- | --- | --- | --- | --- |
```

**`reports: 0`, and an empty table — although 112 `.third.txt` and 108 `.compare.txt` files were
written to disk.** Every other line reads like a clean, healthy run.

**The cause.** Line 37 of the summary block is
`if "/scratch" in root or "armA_src" in root: continue` — a substring test against the **whole
absolute path**, not against the path relative to `OUT`. My `OUT_DIR` lay under
`.../scratchpad/premise_check_l86/v3/out`, and **`scratchpad` contains the substring `/scratch`**,
so `os.walk` skipped every directory in the tree.

**Proof.** I copied the same outputs to a path with no "scratch" in it and re-ran the identical
summary block:

```
reports: 112; compared SAME: 108; DIFFERENT: 0 (-); not compared: 4
block counts off (blocks != JUMP + NO CONNECTION heads, or Reached != NO CONNECTION): 50 (...)
```

which is the truth: 108 stored reports compared, the 4 mocks correctly "not compared", and the count
invariant correctly flagging the 50 reports that carry a JUMP or a NO CONNECTION while my stub
prints no blocks, and correctly leaving the 62 that carry neither.

**Why this is a blocker.** E3 and E4 read that table. The failure is silent and points the wrong
way: `DIFFERENT: 0`, `block counts off: 0 (-)`, no FAILED/SKIPPED/NO_OLD entries, all set timings
present. A marker reading `RUN SUMMARY.md` would mark E3 and E4 **held on zero rows**. It is worse
than the second version's `NO_OLD.txt` fault, which only wrote a spurious line. And the project's own
convention puts scratch work under `.../scratchpad/...`, so the path that triggers it is the likely
one.

**This defect is mine to have missed.** Line 37 is unchanged from the second version; I read the
runner then and did not see it, because I could not run it. It is not new to the third version.

### What the run also established, in the plan's favour

- **All 108 stored reports compared `SAME`.** With the second driver as the stub, every Arm A and
  Arm B report is byte-identical to its stored second-version report once `L86_compare.py`
  normalises `Slowest question:`. That is the whole corpus, not the ten ledgers of my first check:
  my original item 1 is closed as firmly as it can be.
- **The name mapping is right on every file**: 108 comparisons for 108 stored reports, `NO_OLD.txt`
  empty, `SKIPPED.txt` empty (so every one of the 76 Arm A ledgers had its `.json`), `FAILED.txt`
  empty.
- **E3's parenthetical is exact.** Using the runner's own regexes over the 108 Arm A + Arm B
  reports: **32 `JUMP.` heads and 31 `NO CONNECTION.` heads** — the numbers E3 quotes. The mocks give
  mock_none 1 + 1, mock_open 1 + 0, mock_reason_in 0 + 1, mock_fires 0 + 0, matching P6 and E5.
- **E6 has room.** The second driver took 59 s on Arm B and 80 s over the four Arm A sets on this
  machine (against the 110.0 s recorded in L79's `RUN SUMMARY.md` — a faster box). E6 allows 300 s
  each, so the third version has roughly five times the head-room on Arm B and nearly four on Arm A
  for its extra peeks. One checker run per goal, over 63 findings, will not come close.

---

## Part 3. The D-spec

Unchanged but for D3, D4, D6 and D7, all four in the direction I asked. Re-read whole against
`run_check_2.py`: **nothing in D1 to D8 contradicts the code**, and the four questions I raised last
time — whether the peeks carry `extra`, which `removed` they copy, the `- lines` separator, and the
blocks in the second `battery` run — are now all answered in the text. D3's `peek(query, removed)`
signature matches its uses in D4, D5 and D6.

I re-ran the checks that E1, E2, E5 and E7 turn on in the first and second reports and they stand
unchanged: E1's eight goal statuses, E2's `holds (line al1, lo1)` and the single route
`al1, al2, lo1`, E5's `mock_reason_in` line under D6's inner-term test, and E7's four ledger E goals
including the two `open (Q)` lines that D4's precedence decides. Nothing in this version moved them.

---

## DO NOT FREEZE YET

1. **Fix line 37 of `L86_run.sh`'s summary block: `if "/scratch" in root or "armA_src" in root:
   continue` tests a substring of the absolute path.** Any `OUT_DIR` whose path contains `/scratch`
   anywhere — including this project's own `.../scratchpad/...` — makes the walk skip every
   directory, so the per-report table is empty and the summary reads `reports: 0; compared SAME: 0;
   DIFFERENT: 0 (-); not compared: 0` with `block counts off: 0 (-)`, which looks exactly like a
   clean pass. I reproduced it on a real 112-ledger run that had in fact written 112 `.third.txt`
   and 108 `.compare.txt` files. Compare path components relative to `OUT` instead, e.g.
   `rel = os.path.relpath(root, OUT)` and skip when `rel` is `scratch` or `armA_src` or starts with
   either plus a separator. **While you are there, add a guard line** — the summary should print the
   report count against the expected 112 and say plainly when it is short, since E3 needs 32 Arm B
   rows and E4 needs 76 Arm A rows and neither can be read from an empty table. P9 says the runner
   is "as 'The instruments' says", and "The instruments" promises that table; as the file stands
   that promise holds only for some output paths, and E3 and E4 both rest on it.
2. **Correct one word in the quotation rule.** The header glosses `...` as "the rest of the line as
   the second version prints it", but two of the plan's own `...` quotations — `- line g ...` (E5)
   and `- line u2 ...` (E7) — are third-version block rows that the second version never prints.
   "the rest of the line" alone is right.
3. **Add `NO_OLD.txt` to E3's "Would count against" cell.** It names only `FAILED.txt` and
   `SKIPPED.txt`, but the runner and P9 now also produce `NO_OLD.txt` and the summary prints its
   count. A `NO_OLD.txt` entry means a ledger was never compared at all, which should count against
   E3 and E4 exactly as a missing report would.

Item 1 is the only blocker: a one-line fix in a tool, not in the D-spec or the premises. Items 2
and 3 are wording. Every one of my eleven items from the second check is closed, the premises all
verify at their hashes, the D-spec is now buildable twice over, and the run shows the comparison
instrument doing its job on the whole corpus with time to spare.
