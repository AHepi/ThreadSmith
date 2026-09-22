# Premise check - L82 Test plan, Arm B, ninth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, ninth version.md`. Hashed: the first sixteen digits are `0e7f42698df80480`, as the coordinator said. Confirmed. Read whole. The tree is clean at `831aae3`.

The three new tools were read whole at their hashes and all three are as named: `ask_model_2.py` at `ef2e39b165218be4`, `translate_via_api_2.py` at `9496d3923ae367c2`, `L82_run_2.sh` at `f3a5b90189f378f0`. The three first-version tools are unchanged at the hashes the eighth version froze — `ask_model.py` `6736ac6793471387`, `translate_via_api.py` `284be80d1703b60f`, `L82_run.sh` `59084b21d61230d1` — as are the drivers, `sameness_2.py`, `consequences_2.py`, the briefs, the guide, 39, L80, L81, `PAIRS.txt`, the sixteen passages and the two sealed maps. No map was opened.

**What differs from the eighth version.** Seven lines: the title, the preamble, the translators' and runner's entries under "Who does what", P3, P4, P9, P11 and B9. The expectations table is byte-identical apart from B9, and the marking rule section is byte-identical — both checked by diff, not by eye.

---

## Part 1. The premises

Nine are FOUND. **P3 is FOUND WITH A DIFFERENCE.** And one statement outside the numbered premises, in "Who does what", is now false.

### P1, P2, P5, P6, P7, P8, P10 — FOUND

Byte-identical to the eighth version, and every file they rest on was re-hashed and is unchanged. Their contents were verified in full on earlier rounds.

### P3. The tools — FOUND WITH A DIFFERENCE

All four hashes match, and the plan is right to keep the first-version tools beside the second and to say they are what the first run used.

Checked clause by clause against `ask_model_2.py`, and all but one hold: the streamed request with `stream: true` (line 83); the read timeout of `--idle` seconds, which for a streamed response really is a silence timeout, because a socket timeout in Python is per read and the clock restarts on every chunk (line 51); at most `--attempts` HTTP attempts with backoff 10, 20, 40, 80, 120 (lines 109, 117); the six statuses not retried (line 108); an empty answer with finish `length` not retried as `-4`, on the sound ground that the same cap gives the same answer (lines 105, 108); an empty answer with another finish reason retried as `-2`; a 200 with no chunks as `-3` (line 104); an exception as `0` (lines 99-102); `--effort` and `--extra` recorded in the request body and passed by nothing in the run, which I confirmed by searching both the runner and the translator.

P3 is also more accurate than the tool's own docstring, which claims a status `-1` for an unparsable body. In the streamed caller `-1` is unreachable: parsing happens per chunk with `except: continue`, so a body that yields nothing parsable arrives at line 104 with `chunks` at zero and becomes `-3`. P3 correctly omits it.

**The difference.** P3 says "every receipt carries `attempt_history` with each attempt's status, seconds, finish reason and chunk count". The chunk count and the finish reason are not always that attempt's.

`content`, `reasoning`, `finish`, `last`, `chunks` and `rid` are initialised once at line 90, before the retry loop, and reassigned only at line 96, on a *successful return* from `stream()`. When `stream()` raises — an HTTPError, a silence timeout, a disconnect — the handlers at lines 97 to 102 set `status` and `text` and leave those six alone. Line 106 then records the previous attempt's `finish` and `chunks` against the attempt that raised.

This is not a hypothetical. It has already happened, in the probe record the plan itself quotes. `results/L82 Probes .../default and medium effort/B01.atria.receipt.json` reads:

```
attempt 1: status -2    seconds 377.0    finish None   chunks 1487
attempt 2: status -2    seconds 1802.3   finish None   chunks 8597
attempt 3: status -2    seconds 1802.4   finish None   chunks 8974
attempt 4: status 502   seconds 2.3      finish None   chunks 8974
attempt 5: status 200   seconds 705.2    finish stop   chunks 14690
```

Attempt 4 is a 502 that lasted 2.3 seconds and is recorded with 8,974 chunks — attempt 3's count, to the chunk. A 502 returns an error body, not a stream; it produced no chunks at all.

The same staleness reaches further on a final failure: line 112 writes `<tag>.reasoning.txt` from whatever `reasoning` holds, and the error file reports `%d reasoning chars, %d content chars` from the same stale variables, so a call that ends on a raised attempt can leave a reasoning file belonging to an earlier attempt. Given that the probes document Atria cutting streams and returning 429s and 502s, and that the whole point of these fields is to diagnose exactly that, the record should not be able to misattribute them. One line at the top of the loop, resetting the six, fixes it.

What is *not* affected: `.response.txt` is written at line 118 only on success and only from the successful attempt's content, so no ledger is touched, and `seconds` is measured per attempt at lines 94 and 103 and is always that attempt's.

### P4. The pilot, the first run and the probes — FOUND

This is the longest premise in the plan and the most heavily evidenced, and every figure in it that I could check is right.

**The first run.** P4 says four Atria texts failed after six attempts each, every attempt ending at 300.9 to 301.5 s with `RemoteDisconnected('Remote end closed connection without response')`, three 429s and one 502 among them each under 3 s; no Mimo call returned within the 2400 s timeout; the second attempts were stopped with the run. The four receipts under `results/L82 Arm B outputs - first run, stopped 17:27/translations` give:

```
B01  0@301.4 0@301.1 429@2.1 0@301.4 0@301.5 0@301.1
B02  0@301.4 0@301.4 0@301.0 0@301.1 0@301.2 0@301.4
B03  0@301.2 0@301.2 429@2.8 0@301.3 0@300.9 0@301.2
B04  0@301.4 0@301.2 429@2.3 0@301.3 502@2.4 0@301.3
```

Twenty disconnects, all between 300.9 and 301.5 s; three 429s and one 502, all under 3 s. The error file carries the quoted exception verbatim. The Mimo side holds prompts and request bodies and nothing else, and `B0x.atria.attempt2.request.json` exists with no receipt, which is the second validation attempt the run was stopped in. The run log confirms the 16:33:49 start and that nothing past step 1 was reached. Only four texts appear because four lanes were each stuck on their first text.

**The probes.** Every number matches its receipt to the tenth of a second and the token. Atria on B01 at default effort answered on its fifth attempt in 705.2 s with 34,505 reasoning of 39,997 completion tokens, after cuts at 377.0, 1802.3 and 1802.4 s with no finish reason and a 502; Mimo on B03 answered on its first attempt in 1613.5 s with 48,597 reasoning of 54,866; at `reasoning_effort: medium` Atria ran to 60,000 in 1103.0 s after a cut at 1802.1 s and Mimo to 60,000 in 1831.0 s; with a 30,000-token reasoning budget Atria ran to 60,000 after cuts at 1802.4, 728.0 and 999.3 s and Mimo to 60,000 in 1798.8 s. The two answers are in the repository as ledgers of 20 and 23 lines, both validating.

The arithmetic P4 draws is sound: 100,000 tokens at Atria's 54 a second is about 31 minutes and at Mimo's 37 about 45; 1802 s at 54 a second is about 97,000 tokens, which is the honest and important observation that Atria's cut, not the 100,000 cap, is what bounds its calls.

Two small things, neither a misstatement. "Every attempt ending at 300.9 to 301.5 s ... (three 429s and one 502 among them, each under 3 s)" reads as if the parenthesis contradicts the clause it qualifies; the numbers behind it are exactly right, and a semicolon would settle it. And Mimo's 37 tokens a second comes from the earlier pilot; the three probe calls give 32.8, 33.4 and 34.0, so the 45-minute figure is mildly optimistic and 50 would be safer. B9 brackets the outcome either way.

### P9 — FOUND

`translate_via_api_2.py` differs from the first version in four places only, which I confirmed by diff: the file name in the docstring and in the built `.pl` header comment, a new give-up paragraph, and the call at line 120, which now invokes `ask_model_2.py` with `--max-tokens 100000 --idle 600 --attempts 6`. P9 records exactly that, and the validation function it goes on to describe is byte-identical to the one verified on earlier rounds.

### P11 — FOUND

`L82_run_2.sh` differs from `L82_run.sh` in 27 lines, and I read every one: the header and its give-up paragraph, the usage string, the root check, the guard pattern, the lane loop, and the three tool names. Nothing else moved — the gate, COUNTS.txt, the blinding through placeholders, the exit-99 checks, the eight-lane readers, the timings and the manifest are as verified line by line before.

The two substantive changes check out. Translations now run in eight lanes per provider, `for k in 0 1 2 3 4 5 6 7` with `i % 8`, which over sixteen texts is two per lane as B9 says. The start guard's pattern is now `ask_model(_2)?\.py|translate_via_api(_2)?\.py|L82_run(_2)?\.sh`, valid extended regex, so a first-version caller left running would still be caught — the right choice, since both versions are now on disk.

Eight lanes per provider do not threaten the request limits: the per-provider lock is unchanged and serialises every lane at `60/rpm × 1.1`, which is at most 27 Atria and 91 Mimo starts a minute against 30 and 100. What eight lanes do change is concurrency — eight Atria streams held open for up to half an hour each. Nothing in the probes speaks to a concurrent-connection limit, and nothing in the plan claims to know; it is simply something this run will discover, and worth watching in the first minutes rather than at the end.

### The statement outside the premises that is now false

"Who does what", the translators' entry, still ends: "Neither sees the other's work, the plan, the map, or **any earlier ledger of these texts (there are none)**."

There are now two. `Language/results/L82 Probes - streaming, reasoning size, effort and budget/the two answers rebuilt as ledgers/` holds `ledger_B01_atria.json`, twenty lines, `paragraph` `B01`, `whose` `atria, under L82`, validating; and `ledger_B03_mimo.json`, twenty-three lines, `paragraph` `B03`, `whose` `mimo, under L82`, validating. They are earlier ledgers of two of the sixteen corpus texts, made by the two translators the run will use, and they are in the repository.

The preamble records the exposure and argues it: "each call is fresh and no probe output enters the run, so nothing carries over, and it is recorded here." As an argument about mechanism that is sound, and I want to be clear that I am not disputing it — the calls carry no conversation, the runner builds every prompt from the corpus and the briefs, and no probe file is read by anything in step 1. What is wrong is that the sentence a marker will read to learn what the translators are blind to says the opposite of the fact, two paragraphs after the fact is recorded.

There is also something the preamble's argument does not reach, and which belongs with the rows rather than in the preamble. The exposure is **asymmetric**: Atria was given B01 and Mimo was given B03, not both models both texts. B01 is an S-side and B03 an F-side, and between them they carry: B1's expected JUMP on B03; B2's B01; B3's matched pairs B08/B01 and B03/B06, each of which compares a probed text against an unprobed partner *within one translator*; B12's rewording pair B03/B11, the same shape; and B7, which compares the two translators per text and is therefore measured on exactly the axis the exposure is asymmetric along. If a probe effect existed at all it would present as a ledger moving where the prose did not, which is precisely what B3 and B12 charge to the translator. I think the effect is very unlikely; that is a reason to record it beside those rows, not a reason to leave it in the preamble alone.

---

## Part 2. The expectations, and the marking rule

The table is byte-identical to the eighth version except B9, and the marking rule section is byte-identical; both confirmed by diff. So B1 to B8 and B10 to B13 stand exactly as checked and found sound over the fourth to eighth rounds, and I have nothing to add to them.

### B9 — sound

The row now reads "all 32 translations within 5 hours wall clock in eight lanes per provider, two texts per lane (a text that exhausts six streamed attempts of up to 45 minutes each could alone take longer; it is listed under B5, and the budget is still charged)". Sixteen texts in eight lanes is two per lane, matching the runner. The 45-minute figure is P4's 100,000 tokens at Mimo's 37 a second, and the tail is bracketed exactly as before.

Against the observed numbers the budget is plausible rather than generous. Atria's answered B01 probe took 377 + 1802 + 1802 + 2 + 705 seconds, about 78 minutes for one text in one validation attempt; two texts a lane is about two and a half hours, and a second validation attempt could roughly double it. Mimo's B03 took 27 minutes. So five hours is the right order and the row brackets the overrun either way.

### B5 — reached by the tool change, and still sound

The coordinator asked me to look at B5's attempt wording, since "attempts" now has two senses: the caller's six HTTP attempts and the translator's two validation attempts. B5 says "validates within two attempts on at least 14 of 16 texts (read from the validation files' first two lines, P9)". The parenthesis pins it to the validation file, whose first line is `attempt 1` or `attempt 2` and which P9 describes; the translator's loop is unchanged. So B5 is anchored and unambiguous where it is marked, even though P3 uses the other sense. No change needed.

The rest of B5 is untouched and still reads from `ledgers/COUNTS.txt`, which the second-version runner still writes.

---

## Part 3. The run spec at `f3a5b90189f378f0`

Read line by line against the first version, which I had read line by line before. Twenty-seven lines differ and I checked each.

**Lanes.** `for p in atria mimo; do for k in 0 1 2 3 4 5 6 7; do ( i=0; for t in $TEXTS; do if [ $((i % 8)) -eq $k ] ...` — sixteen background subshells, two texts each, one `wait`. Consistent with B9 and with P11.

**The guard.** The pattern covers both versions of all three names and the process-group and ancestor filters are unchanged from the version I tested four ways on the eighth round, where it passed on an idle machine, refused with exit 2 against a foreign process in its own process group, and caught the live pilot. The one documented limit stands: a caller sharing the runner's process group — one launched from the same shell — is skipped. I raised that last round as a thing to record rather than a defect, and it is still unrecorded; with two versions of every tool now on disk and a pilot habit established, it is worth the line it would cost.

**The streamed caller's failure modes, and what a failed text leaves.** This is the part worth spelling out, because the run's first step is where the last attempt died.

A streamed attempt can end five ways. It can finish with content, which breaks the loop and writes a response, a reasoning file and a receipt. It can end with the stream closing cleanly and no content and no finish reason, which is what Atria's cuts at 377, 728, 999 and 1802 s actually look like — `stream()` returns normally, `chunks` is large, `content` is empty, and line 105 labels it `-2` and retries. It can end with finish `length` and no content, labelled `-4` and not retried, which is the right call and is what both models did at the 60,000 cap. It can raise an HTTPError, as the 429s and the 502 did. Or it can raise on silence, if no byte arrives for 600 s, which is the case the first run's 301-second disconnects would now fall into only if the connection stalled rather than closed.

When six attempts are used up, the caller writes `<tag>.error.txt`, `<tag>.reasoning.txt` and a receipt with `"failed": true`, and exits 1. The translator treats a non-zero return as a failed attempt, sets its feedback to "the call failed", and goes round once more, writing a second prompt and request; if that fails too it returns 1 and leaves no ledger and no validation file. The runner's gate then finds no validation file for that text, skips it, and the text is absent from `ledgers/`, from both drivers, from consequences, from both sameness runs, from the reader and from the prose reader — the same consistent exclusion verified before. B5 lists it, and the marking rule removes it from the numerator and denominator of every row that counts it. That chain is intact and is what the first run's outputs show: four texts with error files and receipts, no ledgers, and empty `ledgers/`, `reports/`, `sameness/`, `reader/` and `prose_reader/` directories.

The one gap in that record is the stale-variable problem set out under P3: on a text whose last attempt raised, the reasoning file and the error file's character counts describe an earlier attempt.

**Everything else** is unchanged from the file verified line by line: the argument and root checks, the absolute paths, the fresh-directory requirement, the `head -2 | grep -qx 'VALID'` gate, the driver return-code messages, the six timings, COUNTS.txt, the blinding through NUL-delimited placeholders with `name_still_present` taken after the bin cut, the exit-99 checks in both reader steps, the 30,000-token caps, and the manifest's exclusions.

---

## Verdict

**DO NOT FREEZE YET** — for one false statement about what the translators are blind to, one premise that misdescribes its tool, and one documentary defect.

The response to the failed run is the strongest work in this sequence. The diagnosis is right: a non-streaming request died at 301 s on every Atria attempt, streaming survives past it, and the probes then established the thing that actually matters — that both models reason 35,000 to 60,000 or more tokens on these prompts, that neither `reasoning_effort` nor a reasoning budget binds them, and that Atria cuts a stream at irregular points. The tools were versioned rather than edited, the first versions are kept at their hashes as what the first run used, and P4 records all of it to the tenth of a second. The expectations table and the marking rule were left alone, which is exactly right — nothing in the failure touched them.

What stops the freeze is small in each case and easy to fix.

1. **Correct the translators' entry: there are now two earlier ledgers of these texts, and record the exposure where it is marked.** "Who does what" still says "any earlier ledger of these texts (there are none)". `results/L82 Probes .../the two answers rebuilt as ledgers/` holds `ledger_B01_atria.json`, 20 lines, and `ledger_B03_mimo.json`, 23 lines, both valid, both by the translators the run will use. The preamble's argument that nothing carries over is sound and I do not dispute it — the calls are fresh and no probe output enters the run — but the blindness clause should not assert the opposite of a fact the same page records. While correcting it, add the exposure to "Not tested", where the plan collects its limits, and note beside B1, B2, B3, B7 and B12 that it is asymmetric: Atria saw B01 and Mimo saw B03, which is the axis B7 measures and the within-pair comparison B3 and B12 make, each pair holding one probed text and one unprobed partner.

2. **Reset the caller's stream variables between attempts, and bring P3 to what the tool does.** `content`, `reasoning`, `finish`, `last`, `chunks` and `rid` are initialised once before the loop and reassigned only on a successful return from `stream()`, so an attempt that raises records the previous attempt's finish reason and chunk count, and a call ending on a raised attempt writes an earlier attempt's reasoning to `<tag>.reasoning.txt` and counts its characters in the error file. It has already happened in the evidence P4 quotes: in `B01.atria.receipt.json`, attempt 4 is a 502 lasting 2.3 seconds recorded with 8,974 chunks, attempt 3's count exactly. P3's "each attempt's status, seconds, finish reason and chunk count" is therefore not true as built. One line at the top of the loop fixes the tool; P3 then needs no change.

3. **Correct two statements in `ask_model_2.py`'s own docstring.** It documents `stream()` as returning seven values, "(status, content, reasoning, finish, last_chunk, chunks, text_on_error)", where the function returns six and no status, and the call site unpacks six. And it documents a status `-1` for an unparsable body, which the streamed caller cannot produce: chunk parsing fails silently per chunk, so a body yielding nothing parsable arrives with zero chunks and is labelled `-3`. P3 is right on both counts and the file is wrong, which is the wrong way round for a tool kept at a hash as the record of its own give-up line.

Two things I would record but would not hold the freeze for. The guard's known limit — a caller in the runner's own process group is invisible — is still unrecorded a round after I first raised it, and now matters slightly more with two versions of every tool on disk. And eight concurrent Atria streams, each possibly open for half an hour, is a concurrency the probes never tested; nothing suggests it will fail, but it is the kind of thing the first run's 301-second wall turned out to be, and it will show in the first minutes if it shows at all.
