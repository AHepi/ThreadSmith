# PREMISE CHECK - L86 Test plan, the driver's third version

Checked 23 September 2026 by a fresh Opus agent at extra effort, by hand against the files.
No repository file was edited; no git command that writes was run. The second driver was run
only on a scratch copy under
`/tmp/claude-0/-home-user-ThreadSmith/10bc3818-55b7-5ba7-b992-fc651a944425/scratchpad/premise_check_l86/`.

**The plan's SHA-256** of
`Language/tests/L86 Test plan - the driver's third version, which names the general lines it examined under a JUMP and a NO CONNECTION.md`
is `104dba892bebdf6cb95893f37fb2bb6ff65fce9b367c2d2dd51c0d6f892cd6e4`.
First sixteen digits **`104dba892bebdf6c`** — matches the orchestrator's record.

s(CASP) 1.1.4 on SWI-Prolog 9.0.4 at `/home/claude/sCASP/scasp`, as the runs below used.

---

## Part 1. The premises, P1 to P7

### P1. `rigs/rig 1 - arguments/patched/run_check_2.py` — FOUND, no difference

Hash on disk `9a4b21cf771b12086562a733b2edeb3a4018abe051d243bb473a8636aedad55d`; first sixteen
`9a4b21cf771b1208` — matches. 636 lines.
`checker_rules.pl` on disk `7f10c6f40f8618d1be5bcfb...`; first sixteen `7f10c6f40f8618d1` — matches.

Every quotation is verbatim, and every line number P1 gives is right:

| P1's quotation | claimed | actual |
| --- | --- | --- |
| `text = head + "\nJUMP. Even granting the stated cause, nothing in the ledger produces %s." % effect` | 313-318 | line 314, verbatim |
| `listed_lines(meta, "Claim line", [n])` | " | line 316 (also 353) |
| `listed_lines(meta, "Cause's lines", cause_lines, "(no line supports the cause)")` | " | line 317 |
| `listed_lines(meta, "Effect's direct lines", direct)` | " | line 318 |
| `A single line that would close the jump, which nobody wrote:` | (the abduction) | line 328 |
| `text = head + "\nNO CONNECTION. Nothing in the ledger leads from the reason to what is expected."` | 351-359 | line 351, verbatim |
| the three `listed_lines` blocks (`Claim line`, `Reason's lines`, `Expected's direct lines`) | " | lines 353, 354, 355 |
| `text += "\nIt would take a line nobody wrote, of this kind: a general line saying that someone who %s does %s." % (reason, expected)` | " | line 359, verbatim |
| `direct` | 283, 340 | lines 283 and 340, and it is the set of single-line answers to `holds(<effect>)` / `holds(<expected>)` as described |
| `reason_lines` | 341 | line 341, answers of at most two lines, as described |
| `ask(query, removed=(), extra="")` | 222 | line 222, verbatim |
| `listed_lines` printing `\n  <title>:\n` | 153 | `def listed_lines` at 153; the format literal at 160 |
| `describe_lines` rows `  - line <id> [<mark>, sentence <N>]: <text>` | 141 | `def describe_lines` at 141; the row literal `'  - line %s [%s, sentence %s]: %s'` at 145 |
| `holds(F) :- produced(F).` in `checker_rules.pl` | 30 | line 30, exactly |

Two loosenesses, neither a difference: "built at lines 313 to 318" includes line 313
(`verdicts[n] = "JUMP"`), which prints nothing, and line 315, a comment; and "(line 141)" points
at the definition of `describe_lines`, not at the row literal on line 145.

### P2. The four rule ledgers — FOUND, no difference

All eight hashes match on disk:
`ledger_B06_atria.pl` `51cdd4bab55de28a` · `ledger_B06_mimo.pl` `05ea456f7207287f` ·
`ledger_B01_atria.pl` `324eee2584b9bd3f` · `ledger_B01_mimo.pl` `8cf7589251d64bee` ·
JSON `3030413ed8ddb5f8`, `26de0fb9b5f11af3`, `176439d37fa3b61b`, `5b20ff9341dd9e6e`.

Every quoted clause is verbatim, at these lines of the `.pl`:
B06 Atria — `produced(crossed_bar(B)) :- line(general), ...` line 58; the `depends` clause line 59;
`kind(trawler, trawler)` line 37; `holds(turned(tide)) :- line(tide_turned).` line 52.
B06 Mimo — `produced(crossed_bar_early(X)) :- line(rule1), ...` line 39; the three `depends`
clauses lines 40-42; `kind(trawler, trawler)` line 18; `holds(turned(tide)) :- line(turn1).` line 29.
B01 Atria — `al1` line 31, `lo1` line 33, `al2` line 35, `go1` line 25, `si1` line 29.
B01 Mimo — `gate_rule` line 35, `gate_stood_open` line 33, `since1` line 37. P2's two negative
claims hold: the only clause with head `holds(in(flock, top_field))` is `:- line(flock_top).`
(line 31, no further goal), and nothing yields `left_open_by(shepherd, gate)`.

Every mark and sentence P2 gives is confirmed against the JSON: `general` filled in / 2;
`rule1` filled in / 2; `al1` said, `lo1` filled in, `al2` filled in, all sentence 2; `gate_rule` said.
The JSONs carry `prolog_clauses`, as D1 assumes.

*Gap, not a falsehood.* P2 does not state the **absence** facts that E1's seven `no line says so`
statuses need (that nothing yields `at_harbour`, `loaded`, `turns_before_dawn`, and that
`kind(trawler, loaded_boat)` and `kind(trawler, boat)` fail). I confirmed all of them by running the
checker (below), but under L13 they should be premised.

### P3. The four second-version reports — FOUND, no difference

Hashes match: `bf7715d87c5cdbf1`, `32717236c2ef6f44`, `15c36d91068a04c6`, `8583c44319ee2ff9`.
Every quoted string is verbatim: the JUMP head and `Cause's lines` = `tide_turned`,
`Effect's direct lines` = `crossing` inside `harbourmaster_world` (report lines 17-26); the Mimo
JUMP on `crossed_bar_early(trawler)` inside `log_world`; the Atria NO CONNECTION inside
`note_world` with `go1` / `fi1` and, at line 26, exactly
`  It would take a line nobody wrote, of this kind: a general line saying that someone who open(gate) does in_field(flock,top_field).`;
the Mimo one inside `shepherd_world` with `gate_stood_open` / `flock_top` and
`... someone who gate_open(gate) does in(flock,top_field).`
"None of the four contains the string `General lines that could`" — confirmed, and extended:
**none of the 108 second-version reports contains either `General lines that could` or
`Reached without the reason:`.**

### P4. Arm A's 76 ledgers and outputs — FOUND, correct

L79's P14 reads "36 `.pl` files at the top level of `rigs/rig 1 - arguments/`; 8 in
`results/45 Reruns by the orchestrator/`; 23 in `results/L69 Return .../`; 9 in
`results/L72 Return - Astra Ultra/...`. 76 files" — as L86's P4 says. The output folders hold
exactly 36 / 8 / 23 / 9 `ledger_<name>.new.txt` under `results/L79 Arm A outputs/{rig1,r45,l69,l72}/`.
`RUN SUMMARY.md` line 51 is exactly
`None. The normaliser printed `A1 HOLDS` on all 76 ledgers.` — correct.
*Looseness:* P4 carries no hash for `RUN SUMMARY.md` or for the 76 reports E4 compares against.

### P5. The 32 Arm B ledgers — FOUND, no difference

32 `.pl`, 32 `.json`, 32 `.new.txt`, all present. `MANIFEST.json` holds 1198 entries; I recomputed
**all 1198** against disk: 1198 match, 0 mismatched, 0 missing. All 96 files P5 names are covered.

### P6. The four mocks — FOUND, no difference

All eight hashes match: `mock_none.json 7cc6924fb963a4f5`, `mock_none.pl a5941efaf5dfc4a0`,
`mock_fires.json 8358ad844038ea20`, `mock_fires.pl b9cc553f2cd7a09f`,
`mock_open.json 172b72eebc4f7674`, `mock_open.pl b286d2533e4d8e6c`,
`mock_reason_in.json 16c77ac1245314f3`, `mock_reason_in.pl 4dd5d8dbd83f5c83`.

I ran all four on the second driver in the scratch copy
(`python3 patched/run_check_2.py <mock>.pl <raw log>`). They print exactly what P6 says, in that
order: `mock_none` — `JUMP.` and `NO CONNECTION.`, and neither report contains `General lines`;
`mock_fires` — `FOLLOWS, using:`; `mock_open` — `JUMP.` with
`A single line that would close the jump, which nobody wrote: wick_of(wick,lamp)` (byte-for-byte);
`mock_reason_in` — `NO CONNECTION.`. **P6 holds.**

But P6's *description* of `mock_reason_in` ("a since claim whose reason's atom is a condition of a
general clause reaching the expectation") is not true under D3 as D3 is written — see E5 below.
The mock is built correctly; D3's rule is the thing that is wrong.

### P7. `tools/L86_strip.py` — FOUND, **one difference**

Hash `b58d1550cff950f1a8ea47ec...`; first sixteen `b58d1550cff950f1` — matches.

**Difference: the plan says the instrument is "twelve lines". The file is thirteen lines**
(shebang, a three-line docstring, and nine statements). Both the last paragraph of "What is built"
and, by reference, P7 carry the wrong count.

Its behaviour is exactly as described. Its mock holds: applied to the four mock reports and the
four P3 reports, all eight come back **byte-identical** to the input.

On hand-made third-version inputs it round-trips exactly, in all four shapes D2/D3 produce:
a base-level JUMP block; a told-world JUMP block (heading 4, rows 6, goals 10 after `indented()`);
a told-world NO CONNECTION with both blocks; and the `(none)` / `(no route)` forms. **All four PASS.**

Behaviours the plan does not state, found by test:
- a blank line inside a block ends the strip early and leaves the rest of the block behind (so D2/D3
  must forbid a blank line inside the block);
- a line indented deeper than the heading that immediately follows a block is eaten. I checked the
  insertion point at **every one of the 63 JUMP/NO CONNECTION findings in the 108 reports**: the
  line after the direct-lines block is never indented deeper than the heading would be, so this
  cannot bite on this corpus — but "removes exactly the two blocks and nothing else" is not true in
  general;
- indentation is counted in spaces only, so a tab-indented row would not be removed;
- a heading appearing inside a described line's `<text>` is correctly ignored;
- input without a trailing newline round-trips.

---

## Part 2. The expectations, E1 to E7

I ran, in the scratch copy, every query E1 and E2 turn on, with `world_removed` set as
`run_check_2.py` sets it for a told world (every line outside the case).

| query, in its world | answers | lines |
| --- | --- | --- |
| `kind(trawler, loaded_boat)` · harbourmaster_world | none | — |
| `holds(at_harbour(trawler))` · harbourmaster_world | none | — |
| `holds(turned(tide))` · harbourmaster_world | one | `tide_turned` |
| `kind(trawler, boat)` · log_world | none | — |
| `holds(loaded(trawler))` · log_world | none | — |
| `holds(at_harbour(trawler))` · log_world | none | — |
| `holds(turns_before_dawn(tide))` · log_world | none | — |
| `holds(driven_through(flock, gate))` · note_world | **one** | **`al1`, `lo1`** |
| `holds(in_field(flock,top_field))`, removed `fi1` · note_world | **one** | **`al1`, `al2`, `lo1`** |
| `holds(open(gate))` · note_world | one | `go1` |
| `holds(in(flock,top_field))`, removed `flock_top` · shepherd_world | none | — |

So **yes**: the second driver's `ask` inside a told world can answer such a goal;
`ask("holds(driven_through(flock, gate))")` on Atria's B01 returns exactly one answer whose lines are
exactly `al1` and `lo1`, in that order. The order is `sorted(set(...), key=str)` — ascending string
sort, `run_check_2.py` line 133. E1's and E2's statuses all follow from D2 and D3 as written, and
the route E2 names contains no `go1` and does not meet `reason_lines = [go1]`, as D3 requires.

### The six questions, row by row

**E1 the B06 blocks.** Both sides bracketed — yes (missing/absent *and* "a line named that is not a
general line"; the latter is a real guard, since `holds(crossed_bar(trawler)) :- line(crossing).`
also matches the effect but is not general under D1). Markable under every outcome — yes.
Names an instance no premise establishes — **yes**: the seven `no line says so` statuses and
`holds (line tide_turned)` are established by no premise (I verified them). Rests on a differenced
premise — no. Layer — correct (D1, D2). Decidable from the outputs — yes, **but only as
substrings**: E1 quotes the goal lines with no indentation while D2 fixes eight spaces (ten inside a
told world), and the row `- line general [filled in, sentence 2]: ...` likewise. A marker comparing
whole lines would mark E1 against a correct build.

**E2 the B01 blocks.** Both sides bracketed — yes. Markable — yes. Names an instance no premise
establishes — **yes**: `holds (line al1, lo1)`, the route `al1, al2, lo1`, and "the checker's
order". All three are true (verified above), but the plan carries no premise for them, and "the
checker's order" is defined nowhere in the plan. Rests on a differenced premise — no. Layer —
charged to "the build (D3)", though the goal statuses are D2's machinery; minor. Decidable — yes,
with the same substring caveat, and with one string E2 does not quote at all: D3's
`    - lines <ids>` fixes no separator, so E2 cannot be marked on the route row's exact text.

**E3 Arm B regression. — THE ROW CANNOT BE MARKED HELD UNDER ANY OUTCOME THE BUILD AND RUN CAN
PRODUCE.** The second driver's GAUGE ends `Slowest question: %.2f seconds.` — wall clock, two
decimals (built at `run_check_2.py` lines 618-620 from `slowest[0]`, raised at line 224 by every
`ask`). I re-ran the **unchanged** second driver on ten Arm B ledgers and compared with the stored
`.new.txt`:

```
SAME     B01_atria          DIFFERS  B05_atria  0.07 -> 0.05
DIFFERS  B01_mimo  0.08 -> 0.10    DIFFERS  B06_atria  0.06 -> 0.07
DIFFERS  B02_atria 0.05 -> 0.06    DIFFERS  B06_mimo   0.06 -> 0.09
DIFFERS  B03_atria 0.05 -> 0.06    DIFFERS  B08_atria  0.07 -> 0.05
DIFFERS  B04_mimo  0.05 -> 0.06    SAME     B16_mimo
```

Eight of ten differ, and with that one field normalised the residual diff is **zero lines on all
ten**. So "equals the second-version report byte for byte" fails for a reason that has nothing to do
with the build or with the strip; and because the block adds one `ask` per goal, each a fresh draw
on a running maximum, the third version's value is stochastically no smaller than the second's.
*Layer — wrong.* The cell charges "the build (D4), or the strip instrument (P7)"; the layer that
moved is the clock in the second driver's own gauge, which the cell does not name.
Rests on a differenced premise — yes, P7 (the line count, harmless in itself).

Three further leaks that D4's "Nowhere else" does not cover and the strip does not remove, all from
routing the block's goal queries through the in-scope `ask`, which D2's give-up line ("one `ask` per
body goal (time)") implies: `slowest[0]` rises (line 224 → the GAUGE); a timeout appends
`RAN OUT OF TIME on the question: <query>` to `report` at column 0 (line 226); and `out_of_time`
is set (line 229), which rewrites an OUTCOMES row to `ran out of time` (line 578).

What *is* sound in E3, and verified: the count invariant. Across the 108 second-version reports
`JUMP.` occurs 32 times and every one is a head — the three `... whose verdict above is JUMP).`
lines in `ledger_K22b`, `ledger_P14`, `ledger_P14_correction1` do not match — and `NO CONNECTION.`
occurs 31 times, all heads, the 18 chain rows `->  NO CONNECTION` carrying no period.
32 + 31 = 63, which is exactly the number of blocks D2/D3 would print (I counted matching general
clauses per finding: 51 findings would print `(none)`, 11 would name one clause, 1 would name three).

**E4 Arm A regression.** As E3, with the same verdict and the same misassigned layer; and its 76
targets carry no hashes (P4).

**E5 the mocks.** Both sides bracketed — yes. Markable — **no, for `mock_reason_in`.** D3 fixes the
test as "textual identity after bindings" between the reason's atom and the clause's conditions.
On `mock_reason_in` the reason's atom is `out(lamp)` (confirmed: the second-version report prints
`... someone who out(lamp) does dark(room).`), and the conditions of
`holds(dark(room)) :- line(g), holds(out(lamp)), holds(closed(shutters)).`, as D1 splits a body at
top-level commas, are the goals `holds(out(lamp))` and `holds(closed(shutters))`. `out(lamp)` is
textually identical to neither, so **a correct build following D3 prints
`is not among these conditions` and E5 fires on it.** D3 must say the comparison is against the
goal's inner term (a `holds(` wrapper stripped), or the mock and E5 must change.
Second, `open (<variable>)`: D2 gives three statuses with no precedence and does not say whether "a
variable stays unbound" is judged before or after the ask. On `mock_open`,
`holds(wick_of(W, lamp))` returns no answer *and* leaves `W` unbound, so `no line says so` and
`open (W)` both apply; `holds(burned_down(W))` returns an answer (line `b`) although `W` was unbound
beforehand. Two builders print different things and E5 cannot then be marked.
Names an instance no premise establishes — yes (as above). Layer — "the build", but for
`mock_reason_in` the fault is D3's or the mock's, not the build's. Decidable — yes.

**E6 time.** Both sides bracketed — **no**, only the upper: a run that produced nothing in two
seconds would pass E6. Markable — yes. Names an instance no premise establishes — **yes, and one of
the two figures is wrong.** The 110 s is real: `results/L79 Arm A outputs/RUN SUMMARY.md`, the
Timings table, "NEW driver, `patched/run_check_2.py`, all 76 | 110.0". The 80 s is **not the second
version**: `results/L82 Arm B outputs.run.log` line 6 reads `drivers took 80 s`, and step 2 of
`tools/L82_run_2.sh` (lines 66-69) runs **both** `run_check.py` and `run_check_2.py` over every
ledger inside that timer. Neither figure is carried by a premise at a hash. Layer — correct.
Decidable from the outputs the plan says the run leaves — **no**: the plan names no output that
records the elapsed time of a 108-ledger pass; the GAUGE records only the slowest single question.

**E7 the prose reader's finding.** Both sides bracketed — no, only "2 or fewer". Markable — yes, by
judgement. The brief is found at
`tests/L82 Arm B corpus brief/PROSE READER BRIEF for the API prose reader.md`,
`888a45f49248fba34c513f70...` — first sixteen `888a45f49248fba3`, matches; the receipts confirm the
prose reader is Mimo (`mimo-v2.6-pro`). Names an instance no premise establishes — yes: the Arm B
baseline "three of four" sits in the plan's opening prose and in no premise. I checked it and it is
true: part 2 quotes the rule on B01 Atria, B06 Atria and B06 Mimo, and not on B01 Mimo (which quotes
"the lower field was empty of grass" instead). Layer — correct. Decidable — yes, by a reader's
judgement over the four responses; no fixed string is involved.
*A risk the plan does not flag.* On B01 Atria the rule the reader quoted is `al1`
("the shepherd always left that gate open only once the flock had been driven through it"), but
D3's block lists only clauses whose **head** matches the expectation, so it names `al2` and mentions
`al1` only as an id inside `holds (line al1, lo1)`. On B01 Mimo the block is `(none)` and can do
nothing at all. E7 therefore rests on the two B06 reports doing the work — and "at least 3 of 4"
needs two of the three flips, since B01 Mimo already counts.

---

## Part 3. D1 to D4 as a build instruction

**Would two builders build the same thing? No.** Ten underdeterminations, six of them exercised by
the corpus in hand.

1. **The clause parser (D1).** "Clauses are read up to the full stop that ends them" says nothing
   about `%` comments. **All 68 ledger `.pl` files I checked open with a `%` comment containing full
   stops**, e.g. `% ledger_B01_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.`
   A builder taking D1 literally mis-parses the first "clause" of every ledger. D1 must say comments
   are stripped first, and should say whether a full stop inside a term ends a clause.
2. **Unifying a head with an effect (D2).** D2 says "the head's inner term and the effect's atom
   unify, variables in the head binding by position; a mismatched functor or arity does not match".
   It never says a mismatched **constant** does not match, so one builder rejects
   `crossed_bar(other_boat)` against `crossed_bar(trawler)` and another accepts it with no bindings.
   It never says the effect's atom must be **parsed as a term at all** — and it must be: the effect
   comes from an s(CASP) binding with no spaces (`in_field(flock,top_field)`) while the head comes
   from the `.pl` with spaces (`in_field(flock, top_field)`), so a textual comparison finds no match
   and prints `(none)` on B01 Atria, failing E2. Nothing is said about a head whose inner term is a
   bare variable, or about nested arguments.
3. **"The checker's order" of ids.** Used by E2, defined nowhere in the plan. In `run_check_2.py`
   it is `sorted(set(re.findall(...)), key=str)`, line 133 — ascending string sort. A builder could
   as easily read it as the order of first appearance in the justification tree. They agree on
   `al1, lo1` by coincidence. D2 must name it.
4. **Which answer, and how ids are joined (D2, D3).** "when `ask("<goal>")` returns an answer (the
   ids are that answer's lines)" — with several answers D2 does not say which. No join is fixed for
   `holds (line <ids>)`, for `    - lines <ids>`, or for `open (<the unbound variables>)` when more
   than one variable stays unbound. D3 also does not say whether two routes with the same line set
   are printed twice.
5. **Precedence among the three statuses (D2).** No answer *and* an unbound variable satisfies both
   `no line says so` and `open (...)`; an answer that binds a previously unbound variable satisfies
   both `holds (line ...)` and — on the before-the-ask reading — `open (...)`. `mock_open` hits this,
   and so does `ledger_E` (item 6).
6. **The order of several matching clauses, and a line carrying two (D2). Exercised by the corpus.**
   `rigs/rig 1 - arguments/ledger_E.pl` lines 7-9 carry three general clauses with head
   `knows_words/1` — `u1` (a `holds` head) and **two on the same line `u2`** — and `ledger_E`'s JUMP
   is on `knows_words(jon)` (its report line 4). D2 says "listing every general clause" with no
   order, so `    - line u2 [usual case, sentence 4]: ...` is printed twice with nothing to say
   which goal list comes first. This is the only plural block in the whole 108 and no mock covers it.
   It also exercises the `open (...)` form: `produced(knows_words(P)) :- line(u2), holds(told(Q, P)), holds(knows_words(Q)).`
   leaves `Q` unbound.
7. **Placement (D2).** "before the `A single line that would close the jump` line" — that line is
   absent from both B06 reports (E1's own cases) and from 51 of the 63 findings; and D2 never
   mentions `Lines that would also close it but are ruled out, because the ledger denies them:`
   (line 329), which `ledger_E` prints. "Immediately after the `Effect's direct lines` block, with no
   blank line" would settle it — and the "no blank line" matters, because a blank line inside a block
   ends the strip early (tested).
8. **Indentation, absolute or relative (D2, D3).** D2 fixes 2 / 4 / 8 spaces. Inside a world
   `indented()` (lines 176-178) adds two to every line, so the builder must write 2 / 4 / 8 and let
   the world add two. D2 never says so; a builder who reads the indents as what the reader sees
   writes 4 / 6 / 10 inside a world and produces different bytes, breaking E1 and E2.
9. **The told-world case (D4).** Three things unsaid.
   (a) D1's source is "the ledger's `.pl` text", the whole file, while a told world has removed most
   lines; a general clause carried by a removed line would still be listed, printing
   `- line <id> [...]` for a line the world does not have. **No ledger in hand exercises it** — I
   checked all 108 — so under L15 the negative case of that gate would go untested.
   (b) Each world runs `battery` **twice** (line 602), the second with the actual ledger's general
   lines restored, and `would_go` (line 603) counts findings whose **strings** differ between the two
   runs. In the third version those strings contain the block, whose goal statuses change when
   general lines come back, so the line
   `  N findings inside 'X' would not stand if the actual ledger's general lines were available.`
   can move although no verdict moved. It is not inside a block and the strip does not remove it.
   **Again no ledger in hand exercises it** (no ledger has both an actual-ledger general line and a
   JUMP or NO CONNECTION inside a world), so D4's "nothing else" is not guaranteed and nothing tests
   it.
   (c) D2/D3 write `ask("<goal>")` with no `removed`, so a condition can be reported as met by the
   very `direct` line the verdict set aside. Deliberate or not, the spec should say.
   Note that D4's supposed-case clause *is* exercised by a real ledger: `ledger_H`'s case
   "Monday is gone" carries five NO CONNECTION findings. No mock has a supposed case.
10. **What contradicts `run_check_2.py` as it stands.**
    - **The name "general line" is already taken.** `run_check_2.py` lines 200-202 define
      `general_lines` as the lines with no `case` whose JSON text contains "ALWAYS" or "USUALLY", and
      that set drives the sentence at line 612. D1 defines a different "general line" from the `.pl`
      clause shape. The two disagree (B01 Atria's `al1` and `al2` are general under D1 and
      ALWAYS-texted, but sit in a case, so they are not in `general_lines`). The plan must say the
      D1 notion is new and does not touch line 612's count.
    - **Routing the block's asks through `ask` contradicts D4 and Trap 2**, which says the goal asks
      "add nothing to `report` but the block". They add to `slowest[0]` (line 224, printed in the
      GAUGE), can append `RAN OUT OF TIME on the question: ...` to `report` at column 0 (line 226),
      and can set `out_of_time` (line 229), rewriting an OUTCOMES row (line 578). The spec must
      either have the block's queries call `run_query` directly with the world's removals, or name
      and exempt those side effects.
    - **D3 re-issues `ask("holds(<expected>)", removed=direct)`**, which line 342 has already
      computed and filtered. A second call is a second s(CASP) run per NO CONNECTION — time, and
      another draw on `slowest`. The spec should say to reuse the answers in hand.

---

## Lesson L12: every exact string the spec fixes, and what exercises it

L12 requires that "the mock suite contains one case for every exact string the spec fixes and every
world kind the ledgers in hand contain, and the premise checker lists the strings the mocks do not
exercise."

**Exercised** (mock, or real ledger, verified by running or by reading the report):
`General lines that could produce <effect>, and what each needs:` — B06 Atria, B06 Mimo, `mock_open`;
`General lines that could produce <effect>: (none)` — `mock_none`;
`General lines that could reach <expected>, and what each needs:` — B01 Atria;
`General lines that could reach <expected>: (none)` — B01 Mimo, `mock_none`;
`    - line <id> [<mark>, sentence <N>]: <text>` — B06 Atria/Mimo, `mock_open`, `ledger_E`;
`holds (line <ids>)` with one id — B06 Atria, `mock_open`; with two ids — B01 Atria;
`no line says so` — B06 Atria (two goals), B06 Mimo (four);
`open (...)` — `mock_open`, `ledger_E`;
`Reached without the reason:` with one route — B01 Atria;
`Reached without the reason: (no route)` — B01 Mimo, `mock_none`, `mock_reason_in`;
`is not among these conditions` — B01 Atria;
a told world — B01, B06; a supposed case — `ledger_H` only.

**Not exercised, or exercised by something the spec contradicts:**
1. `the reason's atom, <reason>, is among these conditions` — its only mock, `mock_reason_in`, prints
   the **negative** under D3's "textual identity" rule. No ledger prints it either. **L12 fails here.**
2. A block naming two or more clauses, and a line carrying two matching clauses — only `ledger_E`,
   which reaches the marker only through E4, the expectation that cannot be marked held. No mock.
3. A supposed case — only `ledger_H`, again only through E4. No mock, although L12 names "every
   world kind the ledgers in hand contain".
4. `Reached without the reason:` with more than one route, and the separator in `    - lines <ids>`.
5. The exact rendering of `open (...)`, since its precedence and its multi-variable join are undefined.
6. A JUMP or NO CONNECTION inside a told world on a ledger that also carries actual-ledger general
   lines — the `would_go` path of item 9(b). Nothing in hand.

---

## DO NOT FREEZE YET

1. **E3 and E4 cannot be met by any build.** The second driver's GAUGE ends
   `Slowest question: %.2f seconds.`, a wall-clock value; re-running the unchanged second driver on
   ten Arm B ledgers reproduced the stored report on two and differed on eight, in that field alone.
   Replace "equals the second-version report byte for byte" with a comparison that normalises or
   exempts the `Slowest question:` field (or that compares against a freshly re-run second-version
   report with that field normalised), and correct the "Would count against" cell, which today
   charges the build or the strip for a difference neither produced.
2. **Say where the block's goal queries are made, and stop them leaking outside the block.** Routing
   them through `run_check_2.py`'s `ask` raises `slowest[0]` (line 224, printed in the GAUGE), can
   append `RAN OUT OF TIME on the question: <query>` to `report` at column 0 (line 226), and can set
   `out_of_time` (line 229), which rewrites an OUTCOMES row (line 578). D4's "Nowhere else" and Trap
   2's "add nothing to `report` but the block" are both false as the spec stands. Either call
   `run_query` directly with the world's removals, or name each side effect and exempt it from E3/E4.
3. **Fix D3's reason's-atom test.** "Textual identity after bindings" between the reason's atom and
   the clause's conditions makes `mock_reason_in` print `is not among these conditions`, since the
   atom is `out(lamp)` and the condition goal is `holds(out(lamp))`. A correct build then fires E5,
   and the one string E5 fixes has no case that prints it (L12). Say the comparison is against the
   goal's inner term with a `holds(` wrapper stripped, or change the mock and E5.
4. **Give D2's three statuses a precedence, and define `open (...)`.** Say which wins when a goal
   returns no answer *and* leaves a variable unbound, say whether "stays unbound" is judged before or
   after the ask, and fix how several unbound variables are rendered. `mock_open` and `ledger_E` both
   sit on the ambiguity.
5. **Fix D2's matching rule.** Say that a mismatched constant does not match, that the effect's atom
   is parsed as a term before comparison (the effect prints without spaces, the head with them:
   `in_field(flock,top_field)` against `in_field(flock, top_field)`), and what a head whose inner
   term is a bare variable does.
6. **Fix which answer and how ids are joined.** Say which answer's lines are used when `ask` returns
   several; fix the separator for `holds (line <ids>)`, for `    - lines <ids>`, and for
   `open (...)`; say whether two routes with the same line set are printed twice; and define "the
   checker's order" (it is `sorted(set(...), key=str)`, `run_check_2.py` line 133) in D2 rather than
   only in E2.
7. **Fix the order of several matching clauses, and the repeated-line case.**
   `rigs/rig 1 - arguments/ledger_E.pl` lines 7-9 give `knows_words/1` three general clauses, two of
   them on line `u2`, and `ledger_E`'s JUMP is on `knows_words(jon)`. Say the order, and say what a
   line carrying two matching clauses prints. Add a mock for it.
8. **Fix D1's parser.** Say `%` comments are stripped before clauses are read: all 68 ledger `.pl`
   files open with a `%` comment containing full stops.
9. **Fix the placement and the indentation.** Say "immediately after the `Effect's direct lines`
   block, with no blank line inside the block" (a blank line ends the strip early, tested), say where
   the block goes relative to `Lines that would also close it but are ruled out, ...` (line 329,
   printed by `ledger_E`), and say that D2's 2 / 4 / 8 spaces are written before `indented()` adds
   two inside a world.
10. **Settle the told-world questions of D4.** Say whether a general clause carried by a line the
    world has removed is listed; say what happens to `would_go` (line 603) when the block's text
    differs between a world's two `battery` runs, since the line
    `  N findings inside 'X' would not stand ...` is not inside a block and is not stripped; and say
    whether the goal asks remove `direct`. Neither of the first two is exercised by any of the 108
    ledgers, so add mocks or record them as untested under L15.
11. **Say that D1's "general line" is not `run_check_2.py`'s `general_lines`** (lines 200-202, by
    "ALWAYS"/"USUALLY" in the JSON text of an uncased line), which drives the existing sentence at
    line 612, and that the new notion does not change that count.
12. **Say whether E1's and E2's quoted strings are whole lines or substrings.** They are quoted with
    no indentation while D2 fixes eight spaces (ten inside a told world), so a whole-line marker would
    mark a correct build against.
13. **Correct E6 and make it decidable.** "the second version took 80 s" is wrong: the 80 s in
    `results/L82 Arm B outputs.run.log` line 6 covers **both** drivers, because step 2 of
    `tools/L82_run_2.sh` (lines 66-69) runs `run_check.py` and `run_check_2.py` over every ledger
    inside that timer; only the 110 s (`results/L79 Arm A outputs/RUN SUMMARY.md`, Timings table) is
    the second version alone. Carry both as premises at their hashes, say what output records the
    elapsed time of the 108-ledger pass, and bracket the lower side of the cell.
14. **Correct P7 and "What is built": `tools/L86_strip.py` is thirteen lines, not twelve.**
15. **Add the premises the expectations lean on.** The absence facts behind E1's seven
    `no line says so` statuses; E2's answer lines (`al1, lo1`) and route (`al1, al2, lo1`); the two
    E6 baselines; E7's Arm B "three of four" (true — part 2 quotes the rule on B01 Atria, B06 Atria
    and B06 Mimo, not on B01 Mimo); and hashes for P4's `RUN SUMMARY.md` and its 76 reports.
16. **Record E7's mechanism honestly.** On B01 Atria the rule the reader quoted is `al1`, and D3's
    block names only `al2`, mentioning `al1` merely as an id inside `holds (line al1, lo1)`; on B01
    Mimo the block is `(none)`. E7 rests on the two B06 reports.
17. **List, in the plan, the strings the mocks do not exercise** (L12 requires it of the premise
    check, and the plan should carry the list): `is among these conditions`; a plural block and a
    repeated line; a supposed case; a multi-route `Reached without the reason:`; the id separators;
    the `open (...)` rendering; and the told-world `would_go` path.
