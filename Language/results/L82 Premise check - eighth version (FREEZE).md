# Premise check - L82 Test plan, Arm B, eighth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, eighth version.md`. Hashed: the first sixteen digits are `f1ccf374b4f93c37`, as the coordinator said. Confirmed. Read whole. The tree is clean at `ea44d1a`.

The two changed files were re-read at their new hashes and both are as named: `Language/tools/L82_run.sh` at `59084b21d61230d1` and `Language/tools/ask_model.py` at `6736ac6793471387`. Every other artefact in P3 was re-hashed and is unchanged, as were the sixteen passages, `MAP.enc` and `MAP2.enc`. No map was opened.

**What differs from the seventh version.** Five lines: the title, the preamble, P3, P4 and P11. Every row of the expectations table, the marking rule section, P1, P2, P5, P6, P7, P8, P9, P10 and the closing sections are byte-identical to the seventh version.

---

## Part 1. The premises, P1 to P11

**All eleven are FOUND.**

### P1, P2, P5, P6, P7, P8, P9, P10 — FOUND

All eight are byte-identical to the seventh version, and every file they rest on was re-hashed at the current tree and is unchanged: the sixteen passages and the two sealed maps; `translate_via_api.py` at `284be80d1703b60f`; `sameness_2.py`, `consequences_2.py`, both drivers, 39, L80, the encoding guide, the two briefs, `PAIRS.txt` and L81. Their contents were verified in full on earlier rounds — P1's sentence counts, P2's connective sets and eight diffs, P5's templates, OUTCOMES accounting, standing-prefix clause and four because verdicts, P6's line numbers and the old driver's actual-ledger reach, P7's verbatim quotations from L81, P8's headings and five-bucket partition, P9's validation list, P10's two brief formats — and they stand on unchanged files.

### P3. The tools — FOUND

Every hash re-taken at the current tree and every one matches, including the two that moved.

The new caller clause is exact. P3 says: "every receipt, success or failure, carries `attempt_history` (each attempt's labelled status, 200 for the success, an HTTP code, 0 for an exception, -1 unparsable, -2 empty content, -3 no choices, with its seconds), `seconds` (the last attempt's) and `total_seconds` (the whole call's)". Checked clause by clause against the file:

- The append now happens **after** the relabel, which was my fourth item. The success path appends at line 75, inside the break condition, with status 200. Every other path falls through to line 77, which appends the status as it stands after line 73's `-1` for unparsable JSON and line 76's `-2` for empty content and `-3` for no choices. So a retried empty answer now reads `-2` in the history and can be told from a success, which it could not before.
- All six labels are reachable and correctly named: 200 on the success; `e.code` for an HTTPError; 0 for any other exception, which is where a timeout lands; -1 when the body will not parse; -2 for a well-formed answer with empty content; -3 for a 200 with no choices.
- `seconds` is the last attempt's in **both** receipts now — line 82 for the failure receipt and line 92 for the success receipt — where before the failure receipt used the same key for the whole call. That inconsistency was the second half of my fourth item and it is gone.
- `total_seconds` is `time.time() - started` in both, and `started` is set before the loop, so it is the whole call's.

Everything else P3 attaches to the caller was re-verified at the new hash: the 2400-second timeout, six attempts with backoff 10, 20, 40, 80, 120, the six statuses not retried with the true attempt count in the error file and the message, the failure receipt with `"failed": true`, one lock per provider in `$ASK_MODEL_LOCKDIR`, and the gap at `60/rpm × 1.1`.

### P4. The pilot — FOUND

The contradiction I raised is resolved, and resolved in the better of the two ways available: rather than simply changing the number, P4 now carries the evidence. It reads "the pilot was stopped at about 15:15 during its second attempt (the last write under `out_stopped_1515` is 15:03:17, the restarted pilot's first files 15:15:18)".

Both file times were re-checked and both are right: the newest file anywhere under `out_stopped_1515` is `B99.mimo.attempt2.request.json` at 15:03:17, and the restarted run's first files, the Atria lane logs, are stamped 15:15:18. "About 15:15" is the correct reading of those two facts, and a later reader can now check it without me.

Everything else in P4 is unchanged and was verified on earlier rounds: the first pilot's figures; the second pilot's B98 and B99 results including Mimo's empty content at 651 s with `finish_reason` `length` and 24,003 reasoning tokens against the 24,000 cap; the two HTTP attempts on both Atria calls with the note that the caller at that hash did not record the first attempt's failure and that 73 s and 269 s are the successful attempt's alone.

### P11. The runner — FOUND

The guard sentence now describes the code as built: "It refuses to start (exit 2, OUT_DIR left empty) while any `ask_model.py`, `translate_via_api.py` or `L82_run.sh` process outside its own process group (its subshells and the shell that launched it) and its ancestry is alive, a translator between calls included". That is what lines 36 to 42 do, and the parenthesis is an honest statement of the scope rather than a claim of completeness.

P11 also records the test: "Tested in a scratch copy with the pattern replaced by a unique name: on an idle machine it passed the guard and began step 1; with one foreign process of that name alive it refused with exit 2 and an empty OUT_DIR." I reproduced both halves independently rather than taking them on trust, and both hold — see Part 3.

I diffed the runner against `d43d3798e21b1367` and the only change is the guard and its header lines, so everything else in P11 stands as verified line by line on earlier rounds: the outputs, the gate, COUNTS.txt, the blinding through placeholders with `name_still_present` taken after the bin cut, the exit-99 checks, the 30,000-token caps, the shuffle, the eight lanes, the stop when no ledger validates and the six timings. "OUT_DIR left empty" is still right: `mkdir -p "$2"` is at line 33, the guard at 34 to 42, the subdirectories at 43.

---

## Part 2. The expectations, and the marking rule

Every row and the marking rule section are byte-identical to the seventh version. **All thirteen rows are sound**, and I have nothing to add to the checks already made.

For the record, the state each row is in and where it was settled: B1 charges its other verdicts by what the passage states, with the four blocks listed correctly and demoted to a record, and every alternative on a side with the right layer (seventh version, verified against the texts and the driver). B2's four because verdicts on B06 with the CIRCLE branch, B4's five OUTCOMES readings including `ran out of time`, B5's 14 of 16 with the TOLD requirement scoped to the thirteen texts that carry an argument, B6's band at two misses with an invented number charged to the reader, B7's denominator of thirteen with B13 recorded-not-counted and the controls handed to B4, B11's four because verdicts each charged by its cause, B12's order and its L81 section 5 charge, B13's coverage of all four prose-reader answers (fourth version). B3 and B8 have been sound throughout. B9's budgets at 120 and 90 minutes with the arithmetic shown, which I recomputed (30,000 ÷ 37 tokens a second ≈ 13.5 minutes, four rounds ≈ 54 against 90; 30,000 ÷ 57 ≈ 8.8 minutes, eight rounds ≈ 70 against 120), and B10's carve-out reasoning from the passage (fifth and seventh versions).

Every "against" brackets both sides; every outcome falls on a side or is named unmarkable; each row names the layer that would have moved; no row needs the sealed maps, and I have checked each named instance against observable features of the texts; no two rows give contradictory charges on one outcome, the three former collisions being settled by the marking rule, which remains consistent with P7.

---

## Part 3. The run spec at `59084b21d61230d1`

The only change is the start guard. Last round it refused unconditionally; the question this round is whether it now refuses exactly when it should. I tested it four ways rather than reading it and hoping.

### The guard as built

```
ANC=""; q=$$; while ...; do ANC="$ANC $q"; q=$(ps -o ppid= -p "$q" ...); done
PG=$(ps -o pgid= -p $$ | tr -d ' '); OTHERS=""
for pid in $(pgrep -f 'ask_model\.py|translate_via_api\.py|L82_run\.sh' 2>/dev/null); do
  pg=$(ps -o pgid= -p "$pid" 2>/dev/null | tr -d ' '); [ -n "$pg" ] || continue; [ "$pg" = "$PG" ] && continue
  case " $ANC " in *" $pid "*) continue;; esac; OTHERS="$OTHERS $pid"
done
```

Three changes from the broken version: the pipeline is gone, so the loop body runs in the main shell; every matching pid in the script's own process group is skipped, which is what removes the self-match; and a pid whose `ps` lookup comes back empty is skipped, which handles a process that exits between the `pgrep` and the inspection.

### What the tests showed

**The live pilot is caught.** I copied lines 36 to 42 verbatim into a scratch script, keeping the real pattern, and ran it while the pilot was working. It listed four pilot processes at process group 3992 against its own group 5338 and refused. It also matched my own invoking shell, pid 5335, and correctly skipped it through the ancestor filter — so both filters did real work in the same run.

**Idle: it passes.** With the pattern narrowed to a scratch script's own unique name, so that nothing else on the machine could match, the guard passed and would have gone on to step 1. This is the case that failed last round, twice, and it is the case the previous testing could not see. Fixed.

**A foreign process in its own process group: it refuses.** With a long-lived process of that unique name running under `setsid`, the guard reported that pid alone and exited 2. The listing in that run is the clearest evidence the fix works: four pids matched, three of them the checker's own shell and subshells at its own process group, and only the foreign one at its own group was reported.

I record one false start in my own testing: my first attempt at this case used `sleep 40 --name`, which `sleep` rejects, so the "foreign" process was already dead and the guard passed for the wrong reason. I redid it with a real sleeper. Worth saying, because it is the same shape of mistake that let the seventh version's guard through — a test whose subject was not in the state the test assumed.

**A sibling in the same process group is invisible.** Launching the "pilot" and then the "runner" from one shell, as an orchestrator might, puts both in the launching shell's process group, and the guard passes. This is the deliberate cost of skipping the group: the file's own comment names the group as "its subshells and the shell that launched it", and P11 repeats it. It does not touch the real case — I demonstrated that the actual pilot, launched separately, is caught — but it is the one way B9's precondition could be broken without the guard noticing, and the consequence would be a quietly doubled request rate rather than anything visible in the outputs.

### Everything else

Unchanged from `d43d3798e21b1367` and previously verified line by line: the argument and repository-root checks, the absolute paths, the fresh-directory requirement, the `head -2 | grep -qx 'VALID'` gate and the consistent exclusion of invalid ledgers from the drivers, consequences, both sameness runs, the reader and the prose reader; the driver return-code messages; the six timings including the rig sum; COUNTS.txt's nine fields; the blinding through NUL-delimited placeholders in two passes, covering the quoted headings, `world` or `case` in line texts and any name with an underscore or a digit, with `name_still_present` taken after the bin cut and before the neutral names go in; the exit-99 checks in both reader steps; the 30,000-token caps, both present; the manifest's exclusions; and the rate limiting at `60/rpm × 1.1`, which permits at most 28 Atria and 91 Mimo starts in any sixty-second window against limits of 30 and 100.

---

## Verdict

**FREEZE.**

All eleven premises are found at their hashes, every hash re-taken at the current tree this round. All thirteen expectations bracket both sides, every outcome falls on a side or is named unmarkable, each names the layer that would have moved, none is stated by the map, and none contradicts another. The marking rule resolves the three places two rows once met on one outcome and is consistent with P7. The runner produces every output the expectations and P11 name, blinds the two channels that reached the reader, excludes a failed ledger consistently from every later step, shuffles reproducibly, respects both request limits, has budgets with real headroom — and now starts.

The four items from the seventh version are all answered, and three of them are answered better than asked. The stop time was not merely corrected but given the two file times that establish it. The attempt history now records the labelled status, so the empty-content retry that this pipeline actually produces is legible, and `seconds` and `total_seconds` mean the same thing in both receipts. And the guard was rebuilt around the process group and tested in both directions, which is the test that was missing last time; I reproduced both halves independently, and added a third against the live pilot.

**Nothing must change before the freeze.** One thing is worth recording, and one operating instruction follows from it:

1. **Record that the guard cannot see a caller in its own process group, and start the runner from a shell that has not launched one.** P11 already names the scope — "outside its own process group (its subshells and the shell that launched it)" — so the premise is accurate and nothing in it is wrong; what is missing is the consequence spelled out, in the plan's own habit of naming its limits under "Not tested" and in B9. I confirmed the behaviour: a pilot and a runner launched from one shell share that shell's process group and the pilot is skipped. It does not affect the run as actually arranged — the live pilot, launched separately, is caught, and I watched the guard catch it — so this is a note to keep the record complete and to fix the launch habit, not a defect that voids anything.

I have raised thirty-five items across seven rounds and this is the first version in which none of them is outstanding. The plan is in a state I would freeze and mark against.
