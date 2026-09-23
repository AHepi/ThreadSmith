# BUILD REVIEW - run_check_3.py, against L86 plan (fourth version)

Reviewer: fresh Opus agent, extra effort. 23 September 2026.

## Identities confirmed

| file | SHA-256 |
| --- | --- |
| `Language/tests/L86 Test plan ... fourth version.md` | `32a064ccbfe543597799aa35a3a21c16cb7044a8f482948eb692b0cf73d8e222` |
| `Language/rigs/rig 1 - arguments/patched/run_check_3.py` | `dc82e68bc30997de28b0c43b77a84da793253d5f366b739a013325845a2ab8f2` |
| `Language/rigs/rig 1 - arguments/patched/run_check_2.py` | `9a4b21cf771b12086562a733b2edeb3a4018abe051d243bb473a8636aedad55d` |

All three begin as the brief states. `git status --porcelain` is empty at the end of the
review: no repository file was edited and no writing git command was run. All running was
done in `/tmp/claude-0/-home-user-ThreadSmith/10bc3818-55b7-5ba7-b992-fc651a944425/scratchpad/l86review/`
from a copy of `patched/`.

---

## Part 1. The diff

`diff -u run_check_2.py run_check_3.py`: 636 lines become 811. Four hunks. Thirteen items.
Twelve are pure additions; exactly **one existing line is modified**.

| # | what is added or changed | lines in v3 | licensed by |
| --- | --- | --- | --- |
| 1 | header block naming this plan's hash `32a064ccbfe54359`, the source hash `9a4b21cf771b1208`, and D1 to D8 each with its give-up line | 1-48 | "What is built": *its header names this plan's hash and each D with its give-up line* |
| 2 | `BLOCK_HEAD` regex | 149 | D7 (the strip rule) |
| 3 | `strip_blocks` | 151-158 | D7 |
| 4 | `split_top` | 160-169 | D1 (*body goals are the body split at commas outside parentheses*), D2 |
| 5 | `parse_term` | 171-178 | D2 |
| 6 | `render` | 180-183 | D2 (*printed as the checker prints it*) |
| 7 | `unify` | 185-193 | D2 |
| 8 | `general_clauses` | 195-212 | D1 |
| 9 | `apply_bindings` | 214-222 | D2, D4 |
| 10 | `inner_term` | 224-226 | D6 |
| 11 | `peek`, `goal_lines`, `general_block`, `routes_block` (inside `battery`) | 362-404 | D3, D4, D5, D6 |
| 12 | `text += general_block("produce", effect, direct)` | 490 | D5 |
| 13 | `text += routes_block(...)` and `text += general_block("reach", ..., reason=reason)` | 528-529 | D6 |
| 14 | **modified**: `would_go = len([f for f in blocks + inside if f not in blocks_again + inside_again])` becomes a two-line form that strips the blocks from both sides | 777-778 | D7 |

Verified absent: any other edit. `grep -n "general_block\|routes_block\|strip_blocks\|peek("` shows
calls at 490, 528, 529 and 777-778 only. `ask`, `run_query`, `listed_lines`, `describe_lines`,
`indented`, `world_body`, the OUTCOMES block, the gauge and every other check are byte-for-byte
the second version's.

**Nothing D1 to D8 requires is missing.** Each clause of each D maps onto code:

- D1's comment rule → `re.sub(r"%[^\n]*", "", ledger_text)`; its full-stop rule → `re.split(r"\.(?:\s|$)", text)`;
  its join-across-line-breaks → `" ".join(clause.split())`; its head test → `^(produced|holds)\((.*)\)$`;
  its body test → `if not ids or not others: continue`; MAKES/SHOWS → the `m.group(1) == "produced"` ternary;
  its removed-line rule → `if str(line_id) in {str(x) for x in excluded}`.
- D2's term grammar, unification, and "printed as written ... with each bound variable replaced" →
  `parse_term`, `unify`, `render`, `apply_bindings`.
- D3's `peek(query, removed)` → `run_query(ledger_text, query, removed, world_removed)` with no `extra`.
- D4's four branches, in D4's order → `goal_lines`.
- D5's heading, entry, goal lines, SHOWS note, `(none)` case and placement → `general_block` plus line 490.
- D6's route block, its `(none)`/`(no route)` cases, the `reach` verb, the suppressed SHOWS note and
  the reason's-atom line → `routes_block`, `general_block(..., reason=...)`, lines 528-529.
- D7's indentation, the both-runs build and the stripped count line → the literal `"\n  "`, `"\n    - "`,
  `"\n        "` prefixes and lines 777-778.
- D8 → no third call site.

### One change the plan does not name (not a defect)

Line 385, inside `general_block`:

```python
entry = "\n    - line %s [%s, sentence %s]: %s" % (...) if line_id in meta["lines"] else "\n    - line %s" % line_id
```

D5 gives the entry unconditionally as "the `describe_lines` row". The `else` arm is a guard the
plan does not license. I scanned all 112 ledgers: **0** general-clause line ids are absent from
their `.json` `lines` map, so the arm is unreachable on every input in scope and can change no
output. Recorded, not charged.

---

## Part 2. D1 to D8, read against the code and exercised

### D1. A general clause

`general_clauses` (195-212). Read line by line, every clause of D1 is present. Exercised:

| edge case | input built | result |
| --- | --- | --- |
| a clause spanning lines | `produced(out(L)) :-\n line(g),\n kind(L, lamp),\n holds(pair(L, deep(L, tail))).` (`edge/x1.pl`) | listed; goals joined and printed `kind(lamp, lamp)`, `holds(pair(lamp, deep(lamp, tail)))` |
| a `%` comment holding a full stop | `% x1.pl - a comment with a full stop. And a second sentence. produced(bogus(z)) :- line(zz), holds(q).` | comment wholly removed; the fake clause inside it is not examined; the clause after it parses correctly |
| a clause of a line the world removed | `edge/x2.pl`: `produced(out(L)) :- line(gen), ...` with `gen` outside the told world | inside `note_world` the block reads `General lines that could produce out(lamp): (none)` |
| a bare fact / another head | `denied(read(P, letter)) :- line(u3), ...` (ledger_E line 10); `depends(crossed_bar(B), ...)` (B06 Atria, P2); `line(1). line(2)...` | none examined — confirmed in the reports |

Across the 112 ledgers the function finds **89 general clauses in 50 ledgers**; 0 heads it cannot
parse, 0 quoted atoms containing `%` or `.`, 0 clauses with more than one `line(...)` goal.
The give-up lines therefore bite on nothing in hand, as the plan says.

### D2. Terms and matching

`parse_term` / `unify` / `render` / `apply_bindings` (171-222).

| edge case | input | result |
| --- | --- | --- |
| a head with a constant that differs from the effect's | `produced(out(torch)) :- line(g1), kind(torch, torch).` against effect `out(lamp)` (`x1`) | not listed. Unit: `unify(out(lamp), out(torch)) = False`, arity mismatch `False`, nested mismatch `f(g(a))/f(g(b))` `False` |
| a variable appearing twice in a head | `produced(pair(X, X)) :- line(g), holds(twin(X)), holds(link(Y, Z, X)).` (`x4`) | matches `pair(lamp,lamp)` with X=lamp everywhere; does **not** match `pair(lamp,torch)` — the second occurrence is checked against the first (`unify` line 188) |
| a head variable bound to a compound | `produced(out(L)) :- line(g), holds(needs(L, tail)).` against `out(deep(a,b))` (`x5`) | `holds(needs(deep(a,b), tail))` — the goal's own spacing kept, the sub-term printed as the checker prints it |
| a body goal with a nested term holding a variable | ledger_E `holds(told(Q, P))`, `holds(read(P, letter))` | `holds(told(Q, jon))`, `holds(read(jon, letter))` |

`apply_bindings`'s `\b[A-Z_]\w*\b` does not mistake an upper-case letter inside a name for a
variable (`holds(at_Harbour(B))` leaves `at_Harbour` alone) because `_` is a word character and
kills the boundary. `unify` rejects `None` before binding, so a head the parser cannot read can
never crash `render` (D2's give-up).

### D3. Peeking without leaking — the decisive check

```python
def peek(query, removed=()):
    answers, _, timed_out, _ = run_query(ledger_text, query, removed, world_removed)
    return answers, timed_out
```

No `extra`; `world_removed` from the closure; `slowest`, `report`, `first_raw`, `out_of_time`,
`current` and `log` are untouched by reading. Proved by running:

1. **Raw logs.** I ran `run_check_2.py` and `run_check_3.py` on **all 112 ledgers** and compared
   their raw logs after normalising only the wall-clock field (`| N.NNs |`), s(CASP)'s own
   `Answer n (N.NNN sec)` and the random temp-file paths. **0 content differences, 0 query-count
   differences, 112 of 112.** The peeks are absent from the raw logs.
   `ledger_H` makes 14 peeks (10 route peeks, 4 goal peeks) and its log still holds the second
   version's 117 `ask` queries, in the same order, with the same s(CASP) output; the query
   `holds(is_suggestion(monday))` appears 8 times in both logs although v3 peeks it.
2. **The gauge.** For all 112 reports, `Slowest question: N.NN` equals the maximum of the seconds
   recorded in that report's own raw log. No peek reaches `slowest[0]`.
3. **A forced timeout.** I monkey-patched `run_query` so the single goal `holds(twin(lamp))` times
   out, and ran `check()` on `x4.pl`. Result: the block reads
   `holds(twin(lamp)): the checker ran out of time`; `RAN OUT OF TIME` does **not** appear in the
   report; the fake output does **not** appear in the raw log; the gauge still reads
   `Slowest question: 0.07 seconds` (not 20.00); OUTCOMES shows no `ran out of time`.
   This also exercises the string Lesson L12 lists as unexercised.

The three removal lists are as D3 names them: D5's goal peeks `removed=direct` (line 386 via
`general_block(..., direct)`), D6's goal peeks `removed=direct` (line 529), D6's route peek
`removed=direct` (line 397).

### D4. The goal line

`goal_lines` (367-377) judges in D4's order: variables left → timed out → answers → none. All four
branches observed (`open (W)` in `mock_open`, the forced timeout above, `holds (line tide_turned)`
in B06 Atria, `no line says so` throughout). The ids come from `answers[0]["lines"]`, which
`run_query` already sorts `sorted(set(...), key=str)` (P1, line 133), joined by `", "`. Two
variables print in order of first appearance: `holds(link(Y, Z, lamp)): open (Y, Z)` (`x4`) —
another string Lesson L12 lists as unexercised.

### D5. Under a JUMP

Placement: line 490, immediately after `listed_lines(meta, "Effect's direct lines", direct)` and
before the abduction. Order of entries is ledger-text order; a line with several matching clauses
gets one entry per clause with the same `- line` header — ledger_E prints `u1`, `u2`, `u2`.
The SHOWS note is appended after the goal lines and only when `reason is None` (i.e. only under a
JUMP). `(none)` wording verified on `mock_none` and 33 other blocks. No blank line inside any
block on any of the 112 reports (checked programmatically).

### D6. Under a NO CONNECTION

Placement: 528-529, after `Expected's direct lines` and before `It would take a line nobody
wrote`, route block first. Routes: `peek("holds(<expected>)", direct)`, answers whose lines
intersect `reason_lines` dropped, duplicate id-tuples collapsed, `sorted(routes)` ("the order of
their joined strings"), `(no route)` when empty. No SHOWS note. The reason's-atom test uses
`inner_term` on each goal **after** the bindings are applied:

| edge case | input | result |
| --- | --- | --- |
| goal is `produced(...)` | `holds(dark(room)) :- line(g6), produced(out(lamp)), kind(room, room).`, reason `out(lamp)` (`x3`) | `the reason's atom, out(lamp), is among these conditions` |
| goal is `kind(...)` | same clause | `kind(room, room)` correctly not read as an inner term |
| goal is neither holds nor produced ("the whole goal otherwise") | `holds(cold(room)) :- line(g7), frost(pane), holds(open(window)).`, reason `frost(pane)` (`x3`) | `the reason's atom, frost(pane), is among these conditions` |

### D7. Indentation and the world

Measured over all 112 reports: block headings sit at indent 2 (57) or 4 (43); entries at 4 or 6;
goal, SHOWS and reason lines at 8 or 10. That is D7's two / four / eight, plus `indented()`'s two
inside a world section, and nothing else.

The blocks are printed inside told worlds (B06, B01, x2) and inside supposed cases (ledger_H's
`UNDER THE SUPPOSITION 'Monday is gone'`, five blocks at indent 4), and the goal peeks there use
the world's `world_removed` (x2's `(none)` proves the world's removal reaches `general_clauses`).

**The count line.** `strip_blocks` is byte-for-byte the loop of `tools/L86_strip.py`, same regex.
It is applied to both sides before the comparison. I built `edge/x2.pl`, a told world whose two
`battery` runs differ **only** in the block (the restored run gains an entry for the actual
ledger's ALWAYS line `gen`, which still does not close the jump), and ran three drivers:

| driver | count line |
| --- | --- |
| `run_check_2.py` | `0 findings inside 'note_world' would not stand ...` |
| `run_check_3.py` as built | `0 findings inside 'note_world' would not stand ...` |
| `run_check_3.py` with `strip_blocks` neutered (control) | `1 findings inside 'note_world' would not stand ...` |

So D7's strip is present, correct and necessary; it keeps the second version's meaning.

### D8. Nowhere else

Only two call sites. Over all 112 reports, per report:
`General lines that could` headings **=** `JUMP.` heads **+** `NO CONNECTION.` heads, and
`Reached without the reason:` headings **=** `NO CONNECTION.` heads — **0 violations on 112 of 112**
(totals: 34 JUMP, 33 NO CONNECTION, 67 general headings, 33 route headings; the 32/31 of P12 plus
the mocks' 2/2). Every `produce` heading sits immediately after an `Effect's direct lines:` block,
every `reach` heading immediately after a `Reached without the reason:` block, and every route
heading immediately after an `Expected's direct lines:` block. No block under FOLLOWS (mock_fires
contains the string `General lines that could` zero times), CIRCLE, TO BE EXPECTED, CANNOT TELL, a
plan verdict, a what-if, or an OUTCOMES block.

### An independent re-derivation

To take nothing on trust I wrote my own term parser, unifier and clause splitter (`sweep/independent.py`,
`sweep/independent2.py`), independent of the build's code, and re-derived from the `.pl` and `.json`
sources, for **all 67 JUMP and NO CONNECTION findings on all 112 ledgers**: which general clauses
should be listed and in what order, the SHOWS notes, the 29 goal lines with their statuses (using
the *second* version's `run_query`, which is not under review), the 8 reason's-atom lines, and the
33 route blocks. **Every one agrees with what `run_check_3.py` printed.** (Two reported
"mismatches" are my extractor over-running the end of a finding on the two B06 reports, where the
block is the last thing printed; the goal lines themselves are identical.)

### An observation on D4 that is not a defect of the build

`armA/ledger_G.third.txt` line 26 reads

```
        not exception(5, the_wedding): holds (line )
```

The goal is proved by negation as failure using no ledger line, so the first answer's id list is
empty and D4's own template `holds (line <ids>)` yields `holds (line )`. My independent
implementation of D4 produces the same string, so this is the spec's shape, not a coding slip: the
build does exactly what D4 says. D4 simply has no empty-id case. The string is invisible to E1, E2,
E5 and E7, and to `L86_compare.py` (the block is stripped), so no expectation fires. Recorded for a
future version of the plan; the plan is frozen and no code change is warranted.

---

## Part 3. The expectations as strings

### E1 — the B06 blocks

`ledger_B06_atria.third.txt`, inside `harbourmaster_world`, immediately after the
`Effect's direct lines:` block of the JUMP, leading spaces removed:

```
General lines that could produce crossed_bar(trawler), and what each needs:
- line general [filled in, sentence 2]: [TOLD in world harbourmaster_world] ALWAYS MAKES: when a loaded boat is at that harbour and the tide turns, then the loaded boat crosses the bar; the MAKES kind is the translator's choice, the content is the harbourmaster's
kind(trawler, loaded_boat): no line says so
holds(at_harbour(trawler)): no line says so
holds(turned(tide)): holds (line tide_turned)
```

In that order, with nothing between them and nothing after them before the next finding (this JUMP
prints no abduction line). `ledger_B06_mimo.third.txt`, inside `log_world`:

```
General lines that could produce crossed_bar_early(trawler), and what each needs:
- line rule1 [filled in, sentence 2]: [TOLD in world log_world] ALWAYS MAKES: when a boat is loaded and is at that harbour and the tide turns before dawn, then the boat crosses the bar early; the strength always and the words are said, MAKES is the translator's choice
kind(trawler, boat): no line says so
holds(loaded(trawler)): no line says so
holds(at_harbour(trawler)): no line says so
holds(turns_before_dawn(tide)): no line says so
```

All eight goal lines present, in order, with the stated status. No line is named that is not a
general line of the ledger: the `depends` clauses of both ledgers (P2) are not examined. **E1 met.**

### E2 — the B01 blocks

`ledger_B01_atria.third.txt`, inside `note_world`, after `Expected's direct lines:`:

```
Reached without the reason:
- lines al1, al2, lo1
General lines that could reach in_field(flock,top_field), and what each needs:
- line al2 [filled in, sentence 2]: [TOLD in world note_world] ALWAYS SHOWS: when the flock has been driven through the gate, the flock is in the top_field
holds(driven_through(flock, gate)): holds (line al1, lo1)
the reason's atom, open(gate), is not among these conditions
It would take a line nobody wrote, of this kind: a general line saying that someone who open(gate) does in_field(flock,top_field).
```

The route matches P10 exactly (`al1, al2, lo1`, containing no `go1`) and so does the goal's answer
(`al1, lo1`, in that order). `al1` is not named as reaching the expectation — its head is
`holds(driven_through(flock, gate))`, which does not unify with `in_field(flock,top_field)`.
`ledger_B01_mimo.third.txt`, inside `shepherd_world`:

```
Reached without the reason: (no route)
General lines that could reach in(flock,top_field): (none)
```

`gate_rule` is not named. **E2 met.**

### E5 — the mocks

| mock | required | printed |
| --- | --- | --- |
| `mock_none` | `General lines that could produce out(lamp): (none)`, `Reached without the reason: (no route)`, `General lines that could reach dark(room): (none)`, no goal line | all three present (lines 11, 21, 22); no goal line anywhere |
| `mock_fires` | `FOLLOWS, using:` and no block heading anywhere | line 4; `grep -c "General lines that could"` = 0 |
| `mock_open` | `holds(wick_of(W, lamp)): open (W)` and `holds(burned_down(W)): open (W)` under `- line g ...`, with `kind(lamp, lamp): holds (line k)` before them | lines 13, 14, 15 in that order under `- line g [said, sentence 2]: ...` |
| `mock_reason_in` | under `- line g ...`: `holds(out(lamp)): holds (line a)`, `holds(closed(shutters)): no line says so`, `the reason's atom, out(lamp), is among these conditions` | lines 14, 15, 16 in that order |

The second driver's order of verdicts on the four mocks (P6) is unchanged. **E5 met.**

### E7 — ledger E

`armA/rig1/ledger_E.third.txt`, under the JUMP, lines 10 to 18:

```
General lines that could produce knows_words(jon), and what each needs:
- line u1 [usual case, sentence 3]: someone who quotes a letter word for word knows its words
    holds(quoted(jon, letter)): holds (line 3)
    a SHOWS clause: it shows knows_words(jon) and does not produce it
- line u2 [usual case, sentence 4]: you come to know a letter's words by reading it, or by being told by someone who knows them
    holds(read(jon, letter)): no line says so
- line u2 [usual case, sentence 4]: you come to know a letter's words by reading it, or by being told by someone who knows them
    holds(told(Q, jon)): open (Q)
    holds(knows_words(Q)): open (Q)
```

then line 19, `A single line that would close the jump, which nobody wrote: ...`. Exactly E7's
order and statuses, including the two separate `u2` entries with the same header. **E7 met.**

### The comparison instrument

`tools/L86_compare.py OLD NEW` on the five named ledgers against their stored second-version
reports: **SAME** on all five. On ten further ledgers (`ledger_H`, `ledger_K06`, `ledger_K09`,
`ledger_A`, `ledger_D`, `ledger_B02_atria`, `ledger_B02_mimo`, `ledger_B09_atria`,
`ledger_B12_mimo`, `ledger_B16_atria`): **SAME** on all ten.

I then ran the whole corpus rather than stopping at ten:

| set | ledgers | seconds | compare |
| --- | --- | --- | --- |
| Arm B | 32 | 63 | 32 SAME |
| Arm A `rig1` | 36 | 41 | 36 SAME |
| Arm A `r45` + `l69` + `l72` | 40 | 41 | 40 SAME |
| mocks | 4 | — | no stored second-version report |
| **total** | **112** | Arm B 63 s, four Arm A sets 82 s | **108 SAME, 0 DIFFERENT, 0 FAILED, 0 empty-stderr exceptions** |

(The seconds are well inside E6's 300 s per side, though E6 is marked off `RUN SUMMARY.md`, which
is the runner's business, not this review's.)

### The raw logs (D3)

Read and compared as described in Part 2, D3: **the peeks are absent from all 112 third-version
raw logs**, which are content-identical to the second version's.

---

## Verdict

**BUILD MEETS THE PLAN**

No defect found. Two items are recorded above for the record and neither is charged against the
build:

- the unreachable `else` arm at line 385 (`general_block`), a guard D5 does not name, dead on all
  112 ledgers;
- `holds (line )` at `armA/ledger_G.third.txt` line 26, which is D4's own template applied to an
  empty id list — a gap in D4, faithfully implemented, invisible to every expectation.
