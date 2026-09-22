# Premise check - L82 Test plan, Arm B, tenth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, tenth version.md`. Hashed: the first sixteen digits are `8bce76e0fbc30fdb`, as the coordinator said. Confirmed. Read whole. The tree is clean at `a0a0648`.

`Language/tools/ask_model_2.py` was re-read at its new hash `6de5bd9f4c6a81e2`. `translate_via_api_2.py` at `9496d3923ae367c2` and `L82_run_2.sh` at `f3a5b90189f378f0` are unchanged, as are the three first-version tools at the hashes the ninth version recorded, the drivers, `sameness_2.py`, `consequences_2.py`, the briefs, the guide, 39, L80, L81, `PAIRS.txt`, the sixteen passages and the two sealed maps. No map was opened.

**What differs from the ninth version.** Five places: the title, the preamble, the translators' entry under "Who does what", P3, a new section inserted after the table, and the "Not tested" paragraph. All thirteen rows of the expectations table are byte-identical and so is the marking rule section — both checked by diff.

---

## Part 1. The premises, and the blindness clause

Ten are FOUND. **P3 is FOUND WITH A DIFFERENCE**, on one clause, and it is the only thing outstanding in the plan.

### The blindness clause — corrected

My first item is answered, and answered exactly. The translators' entry now reads: "Neither sees the other's work, the plan, the map, or, **within the run**, any earlier ledger of these texts. Two earlier ledgers exist, made by the probes after the first run failed (P4): Atria's of B01 and Mimo's of B03, kept in `results/L82 Probes ...`. Each call is fresh and no probe output enters the run, so nothing carries over from them; the exposure is asymmetric (Atria saw B01, Mimo saw B03) and is stated beside the rows it touches, below the table."

The false "(there are none)" is gone. "Within the run" is the right narrowing — it is true, and it is the claim the design actually needs. The two ledgers are named with their owners and their location, and I re-confirmed them: `ledger_B01_atria.json`, twenty lines, `whose` `atria, under L82`; `ledger_B03_mimo.json`, twenty-three lines, `whose` `mimo, under L82`; both validating. The asymmetry is stated where a marker will meet it.

### The new section — sound, and its facts check out

"The probes' exposure, beside the rows it touches" names five rows, and every attribution in it is correct against the corpus and `PAIRS.txt`:

- **B1**, "B03 is an F-side; Mimo's B03 ledger" — B03 is one of the four F-sides, and Mimo is the translator that probed it.
- **B2**, "B01 is an S-side; Atria's B01 ledger" — B01 is one of the four S-sides, probed by Atria.
- **B3**, "the pairs B08/B01 for Atria and B03/B06 for Mimo compare a probed text against an unprobed partner within one translator" — both are PAIRS lines, and in each the probed member is the one that translator saw. This is the sharpest statement of the risk in the section, and it is the right one.
- **B7**, "B01 and B03 are two of the thirteen texts, one per translator, which is the axis B7 measures" — both are among the thirteen that carry a reported argument, and B7 compares the two translators per text, so a one-sided exposure lands on its axis.
- **B12**, "B03/B11 for Mimo" — a rewording pair in PAIRS, probed member B03, probed by Mimo.

The handling is right too: "No expectation changes; the marker lists, for each of these rows, whether the probed ledger sits with or against the others, and if a row fires only on a probed text the record says so and the charge stands with that note." That weakens nothing — the charge stands — and it gives the marker a definite diagnostic and a definite obligation. It is the treatment the plan has given every other known limit.

### Not tested — now carries both

The paragraph now adds "Whether an earlier call on the same text affects a fresh call (the probes' exposure, above)", and, answering the recommendation I have carried since the eighth round, "The runner's start guard cannot see a caller in its own process group (P11), so the run is started from a launcher whose shell has launched none; a caller started from the same shell after the run began would not be seen." Both are accurate, and the second adds the operating instruction and the second limit — a caller started after the run begins — that I had not asked for and that is correct.

### P3 — FOUND WITH A DIFFERENCE

The new hash is right and the reset clause is true of the file. P3 says the caller's "stream variables are reset at the top of every attempt, so each history entry is that attempt's own". Line 93, immediately after `attempts += 1` and before the rate-limit wait and the `try`, is `content = reasoning = ""; finish = last = rid = None; chunks = 0; text = ""   # each attempt starts clean`. That is the top of every attempt.

I checked the fix against the failure it was written for rather than only reading it. Running the loop's exact discipline twice, with a stub that returns a clean cut on attempt 1 (empty content, 8,974 chunks) and raises a 502 on attempt 2:

```
NINTH (no reset)      attempt 1: status -2, chunks 8974, reasoning 16 chars
                      attempt 2: status 502, chunks 8974, reasoning 16 chars
TENTH (reset at top)  attempt 1: status -2, chunks 8974, reasoning 16 chars
                      attempt 2: status 502, chunks 0,    reasoning 0 chars
```

The first reproduces the defect I found in `B01.atria.receipt.json`, where a 502 lasting 2.3 seconds was recorded with attempt 3's 8,974 chunks. The second cannot. The failure receipt's `reasoning.txt` and character counts are now the last attempt's too, since they are written inside the loop after the reset. My second item is fixed.

The docstring corrections are in as well, and both are right. `stream()` is now documented as returning six values with their correct names and as raising rather than returning a status; and the unreachable `-1` is gone, replaced by an explanation of why an unparsable body becomes `-3` — "a chunk that does not parse is skipped, so an unparsable body arrives as no chunks", which is exactly what line 105 does. My third item is fixed.

Everything else in P3 was re-verified at the new hash and holds: the streamed request, the `--idle` read timeout, `--attempts` with backoff 10, 20, 40, 80, 120, the six statuses not retried, `-4` for an empty answer with finish `length` and not retried, the receipt's `attempt_history`, `seconds`, `total_seconds`, `stream: true`, finish reason, chunk count and the usage the last chunk reports, and `--effort` and `--extra` recorded and unused.

**The difference is one clause: the two kinds of closed connection carry two labels, and P3 assigns the phrase to the wrong one.**

P3's labels read: "an empty answer with another finish reason is retried, -2; a 200 whose stream yields no parsable chunk -3; an exception, **a closed connection** or silence 0".

There are two closed-connection events in this pipeline, and the plan has evidence of both.

The first is a connection closed before any response arrives. That is the first run's signature — `RemoteDisconnected('Remote end closed connection without response')`, twenty times across four texts, each at about 301 s. It raises, and the caller labels it **0**. P3's clause fits it.

The second is a stream that carries data and then closes cleanly, with no `[DONE]`, no finish reason and no content. That is Atria's cut, which P4 itself describes as "attempts one to three ended with **the stream closed** at 377, 1802 and 1802 s and no finish reason". It does not raise: the line iterator simply ends, `stream()` returns normally with a large chunk count, and line 106 labels it **-2**. The probe receipt shows exactly that: `-2` at 377.0 s with 1,487 chunks, `-2` at 1802.3 s with 8,597, `-2` at 1802.4 s with 8,974.

So the run's most frequent Atria failure is a closed connection recorded as `-2`, while P3 tells the reader that a closed connection is `0` and that `-2` means "an empty answer with another finish reason" — and these answers have no finish reason at all, which is not "another" one. The two labels that will dominate this run's diagnostics are crossed in the premise that defines them, and the same sentence stands in the caller's own docstring.

The code is correct and unambiguous; only the descriptions are. The fix is one clause in each: `-2` is an empty answer with no finish reason or any finish reason other than `length`, which is what a stream closed cleanly mid-flight produces; `0` is a raised exception — a connection closed without a response, a reset, or silence for `--idle` seconds.

### P1, P2, P4, P5, P6, P7, P8, P9, P10, P11 — FOUND

All are byte-identical to the ninth version except P3, and every file they rest on was re-hashed and is unchanged. Their contents were verified in full on the ninth round and before: P4's first-run receipts and probe figures, which I checked to the tenth of a second and the token; P9's translator at an unchanged hash; P11's runner at an unchanged hash, whose twenty-seven changed lines I read individually last round; and the seven premises about the corpus, the drivers, the language, the calibration and the briefs, which have stood unchanged for several rounds on unchanged files.

---

## Part 2. The expectations, and the marking rule

All thirteen rows and the marking rule section are byte-identical to the ninth version, confirmed by diff rather than by eye. They stand exactly as checked and found sound over the fourth to ninth rounds, and the new section's "No expectation changes" is true of the file.

The one row the exposure section touches in substance is none of them — it adds a recording obligation to five rows without altering what any of them expects, counts against, or charges. That is the right shape: the plan has repeatedly chosen to state a limit and carry it into the marking rather than to weaken a row, and it has done so again.

---

## Part 3. The run spec

`L82_run_2.sh` is unchanged at `f3a5b90189f378f0` and `translate_via_api_2.py` at `9496d3923ae367c2`. I read both line by line last round: the eight lanes per provider with two texts each, the guard pattern covering both versions of all three tool names, the gate, COUNTS.txt, the blinding, the exit-99 checks, the timings, the manifest, and the translator's call with `--max-tokens 100000 --idle 600 --attempts 6`. Nothing has moved, so nothing needs re-checking, and the caller's change does not reach them: the runner and translator only read its exit code and its output files, whose names and meanings are unchanged.

The one consequence of this round's change for the run spec is a good one. What a failed text leaves is now an honest record: on a text that exhausts six attempts, `<tag>.error.txt`, `<tag>.reasoning.txt` and the failure receipt all describe the last attempt, and every history entry describes its own attempt. The exclusion chain behind that — no validation file, so no ledger, so the text is absent from both drivers, consequences, both sameness runs, the reader and the prose reader, listed under B5 and removed from every numerator and denominator by the marking rule — is unchanged and was verified before.

The two things I recorded last round as not blocking are now handled or unchanged: the guard's process-group limit is written into "Not tested" with an operating instruction, and eight concurrent Atria streams remain an untested concurrency that the first minutes of the run will settle.

---

## Verdict

**DO NOT FREEZE YET** — for one clause in P3, and nothing else.

All three items from the ninth version are answered, and two of them better than asked. The blindness clause is not merely corrected but correctly narrowed to "within the run", and the exposure is carried into a section that names the five rows, states the shape a probe effect would take, and gives the marker a definite obligation without weakening any expectation. The caller's reset is in the right place and I confirmed by simulation that the defect I found in the plan's own probe receipt can no longer occur. The docstring now describes the function it belongs to. And the guard limit I had been carrying since the eighth round is recorded, with the operating instruction and a second limit I had not asked for.

What is left is that P3 assigns "a closed connection" to status 0, while the closed connections in the plan's own evidence — Atria's cuts at 377, 1802 and 1802 s, which P4 calls "the stream closed ... and no finish reason" — are recorded as -2, and P3's gloss for -2, "an empty answer with another finish reason", does not describe an answer with no finish reason. The code is right; the description crosses the two labels that this run will produce most of. Nothing rests on it in the marking — no row reads an attempt status, B5 reads the validation files, B9 the printed timings, B6 and B13 the FAILED and SKIPPED files — so this touches the record rather than any mark. But the last two rounds of this plan's progress came from reading those labels correctly, and a frozen premise that crosses them would point the next diagnosis the wrong way.

What must change:

1. **Correct P3's status labels for a closed connection, and the same sentence in `ask_model_2.py`'s docstring.** Say that `-2` is an empty answer with no finish reason or any finish reason other than `length` — which is what a stream that carries data and then closes cleanly produces, and is how the probes' three Atria cuts are recorded — and reserve `0` for a raised exception: a connection closed without a response, as the first run's twenty `RemoteDisconnected` failures were, a reset, or silence for `--idle` seconds.

If the coordinator reads P3's "another finish reason" as already covering "none" and "a closed connection" as meaning only the without-response case, then the clause is a loose gloss rather than an error and the freeze follows at once; I have marked it a difference because the plan's own P4 uses the phrase "the stream closed" for the events P3 sends to the other label, and because a premise is frozen for other people to read.
