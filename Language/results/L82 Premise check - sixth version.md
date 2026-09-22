# Premise check - L82 Test plan, Arm B, sixth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, sixth version.md`. Hashed: the first sixteen digits are `67d2a9ba58035bc8`, as the coordinator said. Confirmed. Read whole.

A note on how this check ran. I began on the fifth version and had read it whole and analysed its table when the working tree moved underneath me: `translate_via_api.py` no longer hashed to the `0053f66020414e31` that the fifth version's P3 recorded, and the git log showed a sixth version raising the token caps. The coordinator's next message confirmed it. So this report is a full check of the sixth version, and it carries forward the analysis of the fifth's table, which the sixth leaves byte-identical.

**What actually differs between the fifth version and the sixth.** Six lines: the title, the preamble, P3, P4, P9 and P11. P1, P2, P5, P6, P7, P8, P10, the marking rule section, every row of the expectations table, and the closing sections are byte-identical to the fifth version, which was itself identical to the fourth except P3, P11, B1, B9 and B10.

Everything below was checked by hand against the files at the tree's current state, which is clean at `d275f87`. No map was opened.

---

## Part 1. The premises, P1 to P11

**All eleven are FOUND.**

### P1 and P2 — FOUND

Both are byte-identical to the fourth and fifth versions, and the corpus was re-hashed: all sixteen passages, `MAP.enc` and `MAP2.enc` are unchanged from the files whose sentence counts, connective sets and eight sentence-by-sentence diffs I verified by hand on the second and third checks. The facts stand on an unchanged corpus.

### P3. The tools — FOUND

Every hash was re-taken at the current tree and every one matches, including the two that moved:

`ask_model.py` `bdd97f6b4e0ed5ba`; **`translate_via_api.py` `284be80d1703b60f`**; `sameness_2.py` `e66a9d314a0227b6`; `consequences_2.py` `d04f6dfd08268ce7`; **`L82_run.sh` `098551a71093682e`**; `run_check.py` `eff1dee15bebc977`; `run_check_2.py` `9a4b21cf771b1208`; `39` `dcfbed45d4e94861`; `L80` `ec16e220a433e24a`; the encoding guide `afe860e1509caf09`; the reader brief `ddeba43abbbc1dba`; the prose reader brief `888a45f49248fba3`; `PAIRS.txt` `6da2ec538b581a22`; L81 `c8ff6244676b3c0e`. The four example files are present and PAIRS.txt holds the eight pairs in the order quoted.

The two new parentheses are true of the code. "`tools/translate_via_api.py` 284be80d1703b60f (max tokens 60,000 per translation call)" — line 114 passes `--max-tokens 60000`. "the runner `tools/L82_run.sh` 098551a71093682e (P11; 30,000 max tokens per reader and prose-reader call)" — lines 112 and 143 both pass `--max-tokens 30000`.

The `-2` / `-3` clause is also exact. Line 75 of the caller reads `if status == 200: status = -2 if data.get("choices") else -3`, with the comment "-2: an answer with no content; -3: a 200 with no choices; both retried". Neither label is in the `final` list, so both are retried, as P3 says. This answers the note I left on the fourth version, where both cases were labelled -2 and a malformed response was described in the error file as an empty one.

Everything else P3 attaches to the caller was re-verified against the file at its new hash: timeout 2400 s; six attempts with backoff `min(120, 5 * 2 ** attempts)` giving 10, 20, 40, 80, 120; the six statuses not retried with the true attempt count in both the error file and the message; a failed call leaving an error file and a receipt with `"failed": true`; one lock per provider in `$ASK_MODEL_LOCKDIR` when set; the gap at `60.0 / rpm * 1.1`.

### P4. The pilot — FOUND, and it is the most carefully checked premise in the plan

The first pilot's figures are unchanged and were re-verified on earlier checks. The second pilot is new to this version, and every number in it was checked against the receipts and validation files under `scratchpad/l82_pilot2/out_stopped_1515/`:

- **B98 Atria**: validation file reads `attempt 1` / `VALID`, the ledger has 6 lines, the receipt records `"seconds": 73.4`. P4 says "B98 6 lines, 73 s". Correct.
- **B98 Mimo**: `attempt 1` / `VALID`, 6 lines, `"seconds": 108.9`. P4 says "6 lines, 109 s". Correct.
- **B99 Atria**: `attempt 1` / `VALID`, 11 lines, `"seconds": 269.1`, `completion_tokens` 15311 with `reasoning_tokens` 12842. P4 says "11 lines, 269 s, 12,842 reasoning tokens of 15,311". Correct to the token.
- **B99 Mimo**: no ledger and no validation file; the receipt records `"finish_reason": "length"`, `"seconds": 651.2`, `completion_tokens` 24000 and `reasoning_tokens` 24003. P4 says "returned empty content after 651 s with `finish_reason` `length` and 24,003 reasoning tokens against the 24,000 cap". Correct, including the provider's own oddity of reporting three more reasoning tokens than completion tokens, which P4 reproduces rather than tidying.
- **"the pilot was stopped at 15:17 during its second attempt"**: `B99.mimo.attempt2.request.json` exists with no response, reasoning, receipt or error file beside it. Correct.
- The runner and translator hashes P4 names for that pilot, `c3bb0b60d85de057` and `0053f66020414e31`, are the hashes those two files had at commits `0951768` and `d3cbe17`, which I confirmed with `git show`.

The arithmetic P4 draws from this also checks out: Mimo produced 24,000 completion tokens in 651 s, about 37 tokens a second, so a 60,000-token call takes about 1,626 s — "about 27 minutes, inside the 2,400 s timeout", as P4 says.

**One thing the premise does not record, and should.** Both Atria receipts in the second pilot carry `"attempts": 2`. That is the caller's own HTTP attempt count, not the validation attempt, so P4's "Atria valid on the first attempt on both" is right — the tags are `attempt1` and the validation files say `attempt 1`. But it means Atria's first HTTP call failed retryably on **both** texts and the retry carried it. Two consequences follow, and they bear on B9. First, the receipt's `seconds` field is set inside the retry loop and records only the attempt that succeeded, so 73 s and 269 s understate the wall-clock those calls actually took. Second, an Atria retry rate of two out of two in this pilot is a fact about the provider that B9's translation budget is silent on. Neither is fatal — four texts a lane at even double 269 s is 36 minutes against a three-hour budget — but P4 says "B9's budgets are set from these numbers", and these numbers are per-attempt.

### P5, P6, P7, P8, P10 — FOUND

All five are byte-identical to the fourth version, where each was checked in full against its source: P5's check list, its five quoted finding templates with their tails, the OUTCOMES accounting, the standing-prefix clause corroborated in `example_T10D.json` and in a live pilot ledger, the four because verdicts, and `reading()` returning `ran out of time` first at the driver's 20-second limit; P6's line numbers 69, 95, 313 to 320 and 327 and the old driver's actual-ledger reach; P7's quotations from L81, verbatim, with both halves of case 3 and the prose-reader limb; P8's six headings, the five-bucket partition and the `BIN ENTRIES` line, re-run on two rig ledgers; P10's two brief formats.

### P9. What the translator tool validates — FOUND

The tool moved to `284be80d1703b60f`, so P9 was re-checked against the new file rather than carried forward. The only change in the file is the token cap on line 114; the validation function is untouched. Every clause holds: the six required top-level fields and the four per-line fields with `mark` restricted, `sentence` an integer and `case` with `case_kind` for TOLD or SUPPOSED; the guard check on the clause body after `:-`, with the bare-fact consequence recorded; every sentence in a line or the bin; the old driver run in a temporary copy of the rig; one retry with the failures; `paragraph` by `setdefault` and `whose` to the provider, neither printed by either driver; the model's own line ids; and the two-line head of the validation file, which the second pilot's four files show in both forms.

The new opening clause, "calls the caller with 60,000 max tokens", is line 114 exactly.

### P11. The runner — FOUND

The runner moved to `098551a71093682e`. I diffed it against `c3bb0b60d85de057`, the version I read line by line on the fifth-version pass, and the difference is exactly four lines: two header lines recording the token caps and their reason, and the two `--max-tokens` values in the reader and prose-reader subprocess calls. Nothing else changed, so everything P11 says that I verified line by line still holds, and the one new clause — "eight lanes each (`ThreadPoolExecutor`), 30,000 max tokens per call" — is lines 112 and 143.

Re-verified in the file at its new hash: the three arguments with OUT_DIR made absolute and required new or empty; `ASK_MODEL_LOCKDIR` exported; the gate at `head -2 | grep -qx 'VALID'`; COUNTS.txt's nine fields; the report, consequences and sameness outputs; the reader's key with the world map and the cut flag; `FAILED.txt` at exit 99 for an empty answer and `SKIPPED.txt` for an empty report, in both reader directories; the manifest; the blinding through NUL-delimited placeholders in two passes, covering the quoted headings, `world` or `case` in line texts, and any name with an underscore or a digit, with `name_still_present` taken after the bin cut and before the neutral names go in; the shuffle at `random.Random(82)`; the stop when no ledger validates; and the six printed timings.

The refusal clause is also accurate: line 33 is `if pgrep -f "ask_model.py" > /dev/null 2>&1; then echo ...; exit 2; fi`, and the header says so. It is well placed — after `mkdir -p "$2"` but before the subdirectories are made, so a refused start leaves OUT_DIR existing and empty, which passes the emptiness check on the next attempt instead of poisoning it. That placement looks deliberate and is right.

---

## Part 2. The expectations, B1 to B13, and the marking rule

Every row is byte-identical to the fifth version, which I analysed in full. Twelve of thirteen are sound on all six questions. **B1 is not**, and the defect is narrow and specific.

**On the map — sound.** No expectation needs the sealed maps; every named instance is reachable from features confirmed in the texts.

### What the fifth version got right, and the sixth inherits

**B10 is now clean, and it is clean for the right reason.** Its cell brackets silence ("no because verdict printed on the line") to the driver, and then brackets every other verdict — FOLLOWS, FOLLOWS ONLY IF THE CAUSE IS GRANTED, CIRCLE — to the translator, with this parenthesis doing the work: "(B12 and B15 state no rule, so no such verdict can come from lines the passage states)". That closes the case by reasoning from the **passage**, which the marker can read, rather than from what the report happens to print. It is the right shape, and it needs nothing further.

**B9's narrowing is honest.** Its against now reads "a second caller **started** alongside the run", not "found running alongside". That matches what the guard can actually do — it checks once, at start — so the row no longer promises a check nobody makes.

**B2, B3, B4, B5, B6, B7, B8, B11, B12, B13 and the marking rule** are unchanged from the fourth version, where each was checked against the six questions and found sound: B2's four because verdicts on B06 with the CIRCLE branch; B3's brackets and unmarkable clause; B4's five OUTCOMES readings including `ran out of time`; B5's 14 of 16 with the TOLD requirement scoped to the thirteen texts that carry an argument; B6's band at two misses and three with an invented number charged to the reader; B7's denominator of thirteen with B13 recorded-not-counted and the controls handed to B4; B8's two-sided simplicity; B11's enumeration of all four because verdicts on B13, each charged by its cause; B12's order and its L81 section 5 charge; B13's coverage of all four prose-reader answers. The marking rule still resolves the B12/L81 order, B4 over B13, and B10's bounded override, and is still consistent with P7. No contradictory pair of rows remains.

### B1 — the new rule routes through the report, and one verdict prints no lines

B1's against now brackets the other verdicts, and it names them correctly. I checked all four against the driver: on B03, check 2's other three verdicts are FOLLOWS, CIRCLE and FOLLOWS ONLY IF THE CAUSE IS GRANTED; on B08, check 2b has exactly one other verdict, `TO BE EXPECTED, using: ...`; on B09, check 3's others are the positive "The action does touch ..." and `KIND MISTAKE`; on B05, the DENIED BECAUSE block without the appended CLAIM AND DENY sentence. The enumeration is complete and exact.

The charging rule is where it breaks. It reads: "The marker reads the lines the verdict names (the `using`, `Claim line`, `Plan line` and circle blocks): where any is a filled-in or usual-case line, an added line supplied the answer (L81 case 3); where any is a said line stating a rule, route or fact the passage does not state, a claim the reported person never made ... Where every line the verdict names is a said line the passage states and the atoms match, the verdict is the driver's and counts against."

**`FOLLOWS ONLY IF THE CAUSE IS GRANTED` names no lines at all.** Line 312 of the driver prints `head + "\nFOLLOWS ONLY IF THE CAUSE IS GRANTED. Nothing else in the ledger supports: %s." % cause` — no `describe_lines`, no block of any kind. The only line the block names is the claim line in its own head, and on B03 that is a said line stating what the passage does state. So B1's rule falls through to its last sentence and charges the **driver**, and the verdict counts against.

That is the wrong layer, and demonstrably so. Reaching line 310 requires that nothing produced the effect without the supposition and that the CIRCLE test failed, which means `cause_routes` was empty and granting the cause made the effect produced — in other words the ledger carries a rule making the cause produce the effect while no line supports the cause. B03 states no such rule; the rule is in B06, its S-side partner. So the verdict can only arise from a line the passage does not state, which is the translator's under L81, and B1 would charge it to the rig. On the row the whole arm is built on, with the driver as its headline charge, that is the one direction the error must not run.

The fix is in the plan already: use B10's reasoning. The F-sides are the sides with the rule or route removed — B08 has no rule, B03 has no rule, B09 has no route — so on those three passages any verdict other than the expected one must rest on a line the passage does not state, whatever the report prints. B05's alternative is already handled by its own atom-mismatch clause, which needs no lines.

**A second, smaller fault in the same sentence.** The parenthesised list of blocks is wrong in both directions. `Claim line` is printed by JUMP and by NO CONNECTION, and `Plan line` by CANNOT TELL — all three are the *expected* verdicts, not the alternatives, so a marker will never meet those blocks in the case the rule is written for. And the list omits `Lines used:`, which is the block `KIND MISTAKE` prints at line 418 — an alternative B1 itself names on B09. A marker told to look for "the `using`, `Claim line`, `Plan line` and circle blocks" on a KIND MISTAKE will find none of them and may conclude the verdict names no lines when they are printed under another heading. The blocks that alternatives actually print are `using` (FOLLOWS, TO BE EXPECTED, and the plan's positive verdict), `Lines in the circle` (CIRCLE), `Lines used` (KIND MISTAKE), and, for `YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY`, an unheaded `describe_lines` list.

---

## Part 3. The run spec at `098551a71093682e`

The file differs from the one I read line by line only in the four lines recording and applying the token caps, so this part records what the caps change and what the one new guard does, and does not repeat what has already been checked and has not moved.

### The token caps

**They were raised for a good reason and the reason is recorded.** The second pilot showed Mimo hitting the old 24,000-token translation cap on B99 with `finish_reason: length` and returning empty content — a correctness failure, not a slow call, and one that the caller's empty-content retry would have repeated six times at the same cap. Raising the translation cap to 60,000 and the reader and prose-reader caps from 4,000 to 30,000 answers it, and P4 records the evidence and P3 and P11 record the values. The runner's header now carries the caps and their reason too, so the file that travels with the outputs says why it asks for what it asks for.

**What the raise costs, in B9's terms.** The old reader cap of 4,000 tokens was below Mimo's observed reasoning alone (10,800 on the first pilot), so the old value would have produced empty prose-reader answers throughout; raising it was necessary. But the new value has real timing consequences that B9's budgets absorb with little room:

- **Prose reader.** Mimo ran at about 37 tokens a second in the second pilot. A call that runs to the 30,000 cap takes about 810 s, or 13.5 minutes. Thirty-two calls in eight lanes is four rounds, so a worst case of about 54 minutes against B9's 60. That is about a tenth of headroom, and no allowance at all for the in-caller retry that both Atria calls needed in the second pilot; one retried round would put the row over.
- **Reader.** Atria ran at about 57 tokens a second. A 30,000-token call is about 526 s; sixty-four calls in eight lanes is eight rounds, about 70 minutes against B9's 90. Tighter than before, but sound.
- **Translations.** A 60,000-token Mimo call is about 27 minutes, as P4 says, and four per lane is under two hours against three. A text that also takes translate_via_api's validation retry doubles to about 54 minutes, and four of those would breach the budget — but B9's against is "Over any of the four", so that outcome is bracketed even if it fires.

B9 is exhaustively bracketed and explicitly accepts firing, so none of this is a hole in the row. It is a number the plan should know it is close to.

### The refusal to start

**The guard is real and correctly placed**, and it does what B9 and P11 say. It also has one gap.

`pgrep -f "ask_model.py"` matches the **child** process, not the parent. `translate_via_api.py` spends real time between calls inside `validate()`, which copies the whole rig with `copytree` and runs the old driver with a 600-second allowance; during that window the parent is very much alive and no `ask_model.py` process exists, so the guard would let the run start alongside it. The same is true of a runner between its own steps.

I probed for the window while the restarted pilot was running and did not catch it open — six samples all showed six `ask_model.py` and six `translate_via_api.py` processes, because a six-lane pilot almost always has a call in flight. That masks the gap rather than closing it: a one-lane caller, or the tail of any run, will show the window. The fix is to widen the pattern to cover `translate_via_api.py` and `L82_run.sh` as well.

Two smaller notes on the same line, neither worth changing. `pgrep -f` will also match an editor or a `grep` with the string in its command line, which refuses the run — conservative, and the right direction to fail. And the guard is a start-time check only, which B9 now states plainly.

### Everything else

Unchanged and previously verified: the argument and repository-root checks; the absolute paths; the fresh-directory requirement; the empty-glob guard; the `head -2 | grep -qx 'VALID'` gate and the consistent exclusion of an invalid ledger from the drivers, consequences, both sameness runs, the reader and the prose reader; the driver return-code messages; the six timings including the rig sum; COUNTS.txt; the blinding through placeholders with the leak list taken at the right moment; the exit-99 checks in both reader steps; the manifest's exclusion of the scratch rig and the rate files. The rate limiting is unchanged and still correct with margin — a gap of `60/rpm × 1.1` permits at most 28 Atria and 91 Mimo starts in any sixty-second window against limits of 30 and 100, with every lane of every step queueing on one lock per provider.

---

## Verdict

**DO NOT FREEZE YET** — for one wrong-layer charge in B1, plus three smaller things.

All eleven premises are found at their hashes, and P4 is now a genuinely good record: every figure in the second pilot matches its receipt to the token, including the empty-content failure at the old cap that caused this version to exist. The two tools that moved were re-read at their new hashes and the plan describes both correctly. Twelve of the thirteen rows are sound. B10, which was the twin of B1's defect one version ago, is now clean and clean for the right reason — it decides by what the passage states, not by what the report prints.

B1 did not get that treatment. It decides by the report, and one of the four verdicts it brackets prints no lines for the marker to read, so the rule falls through and charges the driver for a verdict that can only come from a rule the passage does not state. On the row the arm is built on, that would report a fault in the rig that belongs to the translation.

What must change:

1. **Charge B1's other verdicts by the passage, as B10 does.** B03, B08 and B09 are the sides with the rule or route removed — B08's rule is in B01, B03's in B06, B09's route in B04 — so any verdict other than the expected one must rest on a line the passage does not state, and is the translator's, listed, with the ledger unmarkable. As written, a `FOLLOWS ONLY IF THE CAUSE IS GRANTED` on B03 is charged to the driver, because line 312 of `run_check_2.py` prints that verdict with no block of lines at all, so B1's "read the lines the verdict names" finds only the claim line — a said line the passage does state — and the cell's last sentence sends it to the rig. The verdict can only arise when the ledger carries a rule producing the effect from a cause no line supports, which on an F-side is the translator's added rule.

2. **Correct B1's list of blocks.** "the `using`, `Claim line`, `Plan line` and circle blocks" names two blocks that belong to the *expected* verdicts (`Claim line` to JUMP and NO CONNECTION, `Plan line` to CANNOT TELL) and omits `Lines used:`, which is what `KIND MISTAKE` prints and which B1 names as an alternative on B09. The blocks an alternative can print are `using`, `Lines in the circle`, `Lines used`, and the unheaded list under `YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY`.

3. **Widen the start guard beyond the child process.** `pgrep -f "ask_model.py"` misses a `translate_via_api.py` or `L82_run.sh` that is alive between calls — inside `validate()`, which copies the rig and runs the old driver, no `ask_model.py` exists. Add both names to the pattern. I could not catch the window open against the running six-lane pilot, which always has a call in flight; a one-lane caller, or the tail of any run, will show it.

4. **Record what P4's seconds are, and note B9's prose-reader headroom.** Both Atria receipts in the second pilot carry `"attempts": 2`, so each of those calls took two HTTP attempts and the `seconds` field records only the one that succeeded; P4 quotes 73 s and 269 s and says B9's budgets are set from them. And at the new 30,000-token cap, a prose-reader call that runs to the cap takes about 13.5 minutes at Mimo's observed 37 tokens a second, so four rounds of eight lanes is about 54 minutes against B9's 60 — about a tenth of headroom, with no allowance for the retry that Atria needed twice in that same pilot. B9 brackets the outcome either way; the plan should know how close the number is.
