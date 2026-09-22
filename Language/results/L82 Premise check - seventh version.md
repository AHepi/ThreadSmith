# Premise check - L82 Test plan, Arm B, seventh version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, seventh version.md`. Hashed: the first sixteen digits are `20c65a52afe3c879`, as the coordinator said. Confirmed. Read whole. The tree is clean at `31b27e3`.

The two changed files were re-read at their new hashes and both are as named: `Language/tools/L82_run.sh` at `d43d3798e21b1367` and `Language/tools/ask_model.py` at `0d0db0299fa3ced5`. Every other artefact in P3 was re-hashed and is unchanged, as were the sixteen passages, `MAP.enc` and `MAP2.enc`. No map was opened.

**What differs from the sixth version.** Six lines: the title, the preamble, P3, P4, P11, B1 and B9. P1, P2, P5, P6, P7, P8, P9 and P10, the marking rule section, and every other row of the table are byte-identical to the sixth version.

---

## Part 1. The premises, P1 to P11

Nine are FOUND. **P4 and P11 are FOUND WITH A DIFFERENCE**, and P11's difference is the one that stops the freeze.

### P1, P2, P5, P6, P7, P8, P9, P10 — FOUND

All eight are byte-identical to the sixth version, and the files they rest on were re-hashed and are unchanged: the sixteen passages and the two sealed maps; `translate_via_api.py` at `284be80d1703b60f`; `sameness_2.py`, `consequences_2.py`, both drivers, 39, L80, the encoding guide, the two briefs, `PAIRS.txt` and L81, each at the hash P3 records. The facts in them were verified in full on earlier checks — P1's sentence counts, P2's connective sets and eight diffs, P5's templates and OUTCOMES accounting and the standing-prefix clause, P6's line numbers and the old driver's actual-ledger reach, P7's verbatim quotations from L81, P8's six headings and five-bucket partition, P9's validation list, P10's two brief formats — and they stand on unchanged files.

### P3. The tools — FOUND

Every hash re-taken at the current tree and every one matches, including `ask_model.py` at `0d0db0299fa3ced5` and `L82_run.sh` at `d43d3798e21b1367`.

The new clause is true of the code: "every receipt carries `attempt_history`, the status and seconds of each HTTP attempt, beside `seconds`, which is the successful attempt's alone". Line 56 initialises `history`, line 70 appends `{"attempt", "status", "seconds"}` after every HTTP call, and both the failure receipt (line 80) and the success receipt (line 90) carry it. That is a real improvement on the receipts I complained about last time, where two Atria attempts were visible only as a count.

Two things about it to know, neither a misstatement by P3:

The history's `status` is the **transport** status, captured at line 70 before line 75 relabels a 200 with empty content to `-2` and a 200 with no choices to `-3`. So an attempt rejected for empty content and retried is recorded as `status: 200`, indistinguishable in the history from a success. That is the commonest retry cause in this pipeline — it is what Mimo did on B99 and almost certainly what Atria did twice in the second pilot — so the history shows that a retry happened and how long it took, but not why, in exactly the case the plan cares about. Recording the labelled status instead would cost nothing.

And "`seconds`, which is the successful attempt's alone" is true of the success receipt; in the failure receipt `seconds` is `time.time() - started`, the whole call. Defensible, since a failed call has no successful attempt, but the two receipts use the same key for different quantities.

### P4. The pilot — FOUND WITH A DIFFERENCE

Everything about the two pilots' substance is right, including the new disclosure I asked for. What is wrong is a time, and it is wrong in a way the seventh version itself made visible.

**What is right.** The first pilot's figures are unchanged and were verified on earlier checks. The second pilot's figures were re-verified against the receipts and validation files under `out_stopped_1515`: B98 Atria 6 lines, B98 Mimo 6 lines and 109 s, B99 Atria 11 lines with 12,842 reasoning tokens of 15,311, B99 Mimo empty content after 651 s with `finish_reason` `length` and 24,003 reasoning tokens against the 24,000 cap. The new sentence answers my item 4 exactly and honestly: "each after two HTTP attempts (`"attempts": 2` in both receipts; the first attempt's failure is not recorded by the caller at that hash, and the receipts' 73 s and 269 s are the successful attempt's alone)". Both receipts do carry `"attempts": 2`, the caller at that hash wrote no error file for a non-final failure, and `seconds` is indeed the successful attempt's.

**The difference.** P4 now says two things that cannot both be true: "the pilot was stopped at **15:17** during its second attempt", and "The pilot was restarted at **15:15** UTC on the runner at 098551a71093682e". A run cannot be stopped two minutes after its replacement started.

The filesystem settles it against 15:17. The last write anywhere under `out_stopped_1515` is at **15:03:17** — `B99.mimo.attempt2.request.json` and `.rate_mimo`, the moment the second attempt's request went out; nothing in that tree is newer, and a search for anything written after 15:04 returns nothing. The restarted pilot's first files, the four Atria lane logs, are stamped **15:15:18**. And the plan's own directory name for the stopped run is `out_stopped_1515`. So the stop was at about 15:15, immediately before the restart, and "15:17" is wrong.

The error is inherited from the sixth version, where I checked that the `attempt2` request file existed with nothing beside it but had no second time to check it against. The seventh version's new restart time is what makes the contradiction visible, which is the system working; it should now be corrected rather than frozen.

One clause in P4 I could not verify: "the caller was edited while it ran (attempt history added), so its receipts carry `attempt_history` from the point of the edit and not before." The restarted pilot has produced no receipts yet — its `translations` directory holds sixteen files, all prompts and request bodies, with no response, reasoning or receipt for any of the four calls. The statement is plausible and is the right kind of thing to disclose; it simply has nothing behind it yet.

### P11. The runner — FOUND WITH A DIFFERENCE

P11's guard sentence reads: "It refuses to start (exit 2, OUT_DIR left empty) while any `ask_model.py`, `translate_via_api.py` or `L82_run.sh` process other than itself and its ancestors is alive, a translator between calls included, since the lock is shared within one run only".

That describes the intent, and the pattern and the ancestor filter are in the file. But the file does not behave that way: it refuses **always**, including on an idle machine, for the reason set out in Part 3. A premise that says the runner refuses under a condition, when the runner refuses under every condition, is not found as stated.

Everything else in P11 was re-verified. I diffed the runner against `098551a71093682e`, the version I read line by line on the sixth-version pass, and the only change is the guard and its two header lines. So the outputs, the gate, COUNTS.txt, the blinding through placeholders, the exit-99 checks, the shuffle, the eight lanes, the 30,000-token cap, the stop when no ledger validates and the six timings all stand as previously checked. The clause "OUT_DIR left empty" is also right: `mkdir -p "$2"` is at line 33, the guard at 34 to 37, and the subdirectories at line 38, so a refusal leaves the directory existing and empty and the next attempt passes the emptiness check.

---

## Part 2. The expectations, and the marking rule

Every row but B1 and B9 is byte-identical to the sixth version, where twelve of thirteen were sound. **Both changed rows are now sound.** The marking rule section is unchanged and still resolves the B12/L81 order, B4 over B13 and B10's bounded override, consistently with P7.

### B1 — now sound

My first item is properly answered, and answered by the method I asked for rather than by patching the symptom. The cell now reads: "Charged by what the passage states, as B10 is: B03, B08 and B09 state no rule and no route (those are in B06, B01 and B04), so a FOLLOWS, a FOLLOWS ONLY IF THE CAUSE IS GRANTED, a TO BE EXPECTED or `The action does touch ...` can rest only on a line the translator added ... each the translator's, listed, and the ledger unmarkable here".

The factual claim carries the row, so I checked it against the texts. B03 states no rule; its rule is the clause B06 adds. B08 states no rule; its rule is the clause B01 adds. B09 states no route; its route is the clause B04 adds. The pairing and the order in the parenthesis are both correct. With that, `FOLLOWS ONLY IF THE CAUSE IS GRANTED` no longer needs to print anything for the marker to charge it, which was the whole defect.

My second item is answered too, and the blocks are demoted from being the basis of the charge to being recorded with it: "the blocks such a verdict prints (`using`, `Lines in the circle`, `Lines used`, the list under `YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY`) are recorded with it where there are any, and FOLLOWS ONLY IF THE CAUSE IS GRANTED prints none." Those are exactly the four blocks the alternatives print, and the note about FOLLOWS ONLY IF is exactly right — line 312 of the driver prints that verdict with no `describe_lines` call at all.

Every alternative is now on a side: FOLLOWS, FOLLOWS ONLY IF, CIRCLE, TO BE EXPECTED and the plan's positive verdict to the translator; KIND MISTAKE by its own two-way clause; B05's missing CLAIM AND DENY sentence by whether the atoms match; silence to the driver; the expected verdict met; and the two unmarkable cases listed. B05's clause is executable from the report alone, because the denial's cause and effect atoms are printed in the `Fine.` continuation and the claim's in the because verdict's text.

One observation, not a defect. The KIND MISTAKE clause allows a "driver's, against" branch where "the kinds it names are the kinds the passage's own words give the things". On B09 that branch looks unreachable: a KIND MISTAKE requires both a `changes` and a `depends_on` line, the guide says to write each only "if the text says", and B09's prose says neither what moving the patient changes nor what monitoring the breathing depends on — so any KIND MISTAKE on B09 rests on added lines and is the translator's by the row's own first rule. A vacuous branch leaves no outcome unbracketed, so it costs nothing; it may simply never be used.

### B9 — now sound

The budgets are raised and the arithmetic is in the cell: the reader gets 120 minutes and the prose reader 90, with "at the 30,000-token cap a call that runs to the cap takes about 13 minutes at Mimo's observed 37 tokens a second, four rounds about 54 minutes, and the pilot showed Atria needing a second HTTP attempt twice".

The arithmetic checks out. Mimo produced 24,000 completion tokens in 651 s, about 37 a second, so a 30,000-token call is about 811 s or 13.5 minutes; thirty-two calls in eight lanes is four rounds, about 54 minutes, now against 90 rather than 60. Atria produced 15,311 tokens in 269 s, about 57 a second, so a capped reader call is about 526 s; sixty-four calls in eight lanes is eight rounds, about 70 minutes, against 120 rather than 90. Both now have room for the retried round that the second pilot suggests is likely, which was the point of the item. The row's against is unchanged and still exhaustive.

---

## Part 3. The run spec at `d43d3798e21b1367`

The only change from the version I read line by line is the start guard and its header lines, so this part is about the guard.

### The guard is wider, and it is broken

The intent is right and answers my third item: the pattern now covers the parent processes, so a `translate_via_api.py` sitting in `validate()` between calls — copying the rig and running the old driver, with no `ask_model.py` child alive — is caught, which the old child-only pattern missed.

The implementation refuses unconditionally.

```
ANC=""; q=$$; while [ "$q" -gt 1 ] 2>/dev/null; do ANC="$ANC $q"; q=$(ps -o ppid= -p "$q" ...); ...; done
OTHERS=$(pgrep -f 'ask_model\.py|translate_via_api\.py|L82_run\.sh' 2>/dev/null | while read -r pid; do case " $ANC " in *" $pid "*) ;; *) echo "$pid";; esac; done)
if [ -n "$OTHERS" ]; then ... exit 2; fi
```

`ANC` holds the script's own pid and its **ancestors**. But the line that computes `OTHERS` forks two **descendants** of the script: the command substitution `$(...)`, and the right-hand side of the pipeline, the `while read` loop. Both are forks of the running shell, so each has the script's own argv and each `/proc/<pid>/cmdline` contains `L82_run.sh`. Both are alive while `pgrep` scans. Neither is an ancestor, so neither is filtered out. `OTHERS` is therefore never empty and the script always exits 2.

**Demonstrated, not inferred.** I copied those three lines verbatim into a scratch script, changing only the pattern to the scratch script's own unique name so that nothing else on the machine could match, and ran it twice:

```
ANC   =[ 4802 4799 102 85 81]      OTHERS=[4818 4820 ]     RESULT: would REFUSE
ANC   =[ 4824 4799 102 85 81]      OTHERS=[4840 4842 ]     RESULT: would REFUSE
```

Two pids each time, neither in the ancestor chain, on a pattern that only that script's own processes could match. They are its command-substitution and pipeline subshells. The real runner reproduces this because its invocation — `sh Language/tools/L82_run.sh ...`, or the script by path — puts `L82_run.sh` in the argv its subshells inherit.

**Why the testing did not catch it.** The coordinator reports the guard was "tested against the running pilot, it refused with exit 2 and left OUT_DIR empty". That is the one test that cannot distinguish a working guard from a self-blocking one: the pilot was running, so a refusal was the expected answer either way. The guard has been exercised only in the case where it is meant to say no.

**The shape of a fix.** Excluding descendants as well as ancestors is awkward, because they are created by the very command that looks for them. Comparing process groups is simpler and correct: the subshells share the script's process group, while a separately started pilot or runner has its own, so dropping every pid whose `pgid` equals the script's removes the self-match without weakening the check. Whatever is chosen, the guard needs one test on an idle machine before it is recorded in a premise.

### Everything else

Unchanged from `098551a71093682e` and previously verified line by line: the argument and repository-root checks, the absolute paths, the fresh-directory requirement, the `head -2 | grep -qx 'VALID'` gate and the consistent exclusion of invalid ledgers from every later step, the driver return-code messages, the six timings, COUNTS.txt, the blinding through NUL-delimited placeholders in two passes with `name_still_present` taken after the bin cut, the exit-99 checks in both reader steps, the 30,000-token caps, the manifest's exclusions, and the rate limiting at `60/rpm × 1.1`, which permits at most 28 Atria and 91 Mimo starts in any sixty-second window against limits of 30 and 100.

---

## Verdict

**DO NOT FREEZE YET** — the runner cannot start.

The plan itself has come a long way in this version. B1 is now charged by what the passage states, which is the right method and the one B10 already used, and every alternative verdict on all four F-sides is on a side with the correct layer; the block list is corrected and demoted to a record. B9's budgets are raised with the arithmetic shown, and both now have room for the retry the pilot suggests is likely. P4 discloses the two HTTP attempts and what `seconds` measures, which is exactly what I asked for. The caller now carries an attempt history in every receipt. Nine premises are found at their hashes and eleven of thirteen rows were already sound and remain so.

But the fix to my third item introduced a hard fault: the start guard matches its own subshells and refuses on an idle machine, so `L82_run.sh` at this hash will not run at all. P11 records behaviour the file does not have, and a plan frozen on that premise would be frozen on a runner that cannot produce a single output. And P4, in gaining the restart time, has acquired two times that contradict each other.

What must change:

1. **Fix the start guard; it refuses unconditionally.** `OTHERS` is computed by a command substitution containing a pipeline, and both of those forks inherit the script's argv, so both match `L82_run\.sh` and neither is in the ancestor list. I reproduced it twice with the pattern narrowed to a scratch script's own name: two foreign pids on an otherwise idle machine. Excluding the script's process group rather than only its ancestors would fix it without weakening the check. Then test it once with nothing else running — the only test so far was against the running pilot, which would refuse either way.

2. **Correct P4's stop time.** P4 says the second pilot "was stopped at 15:17" and also "was restarted at 15:15 UTC", which cannot both hold. The last write anywhere under `out_stopped_1515` is 15:03:17, the restarted pilot's first files are stamped 15:15:18, and the plan's own directory name is `out_stopped_1515`. The stop was about 15:15.

3. **Bring P11's guard sentence to what the file does**, once item 1 is settled. As written it promises a conditional refusal that the file does not implement, and it is the sentence a marker would rely on to explain why a run produced nothing.

4. **Record the labelled status in `attempt_history`.** The history appends at line 70, before line 75 relabels a 200 with empty content to `-2` and a 200 with no choices to `-3`, so a retried empty-content attempt reads as `status: 200` and cannot be told from a success. That is the commonest retry cause here — Mimo's B99, and probably both of Atria's two-attempt calls — so the history shows that a retry happened and how long it took but not why, in the case the plan added it for. While there, note that `seconds` in a failure receipt is the whole call, not an attempt, unlike the success receipt.

Two smaller observations, not requiring change. B1's KIND MISTAKE clause keeps a "driver's, against" branch that looks unreachable on B09, since a KIND MISTAKE needs both a `changes` and a `depends_on` line and B09's prose gives neither; a vacuous branch leaves nothing unbracketed. And P4's statement that the restarted pilot's receipts carry `attempt_history` from the point of the edit could not be checked: that run has produced sixteen files, all prompts and request bodies, and no receipt yet.
