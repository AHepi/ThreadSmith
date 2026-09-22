# Premise check - L82 Test plan, Arm B, twelfth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, twelfth version.md`. Hashed: the first sixteen digits are `214a41da2cf67590`, as the coordinator said. Confirmed. Read whole. The tree is clean at `c2f7739`.

`Language/tools/translate_via_api_2.py` was re-read at its new hash `b92bfe0a4bf4bf46`. Everything else is unchanged at the hash the eleventh version recorded: the caller `d1d55e43543d4dcd`, the runner `f3a5b90189f378f0`, the three first-version tools, both drivers, `sameness_2.py`, `consequences_2.py`, `PAIRS.txt`, the briefs, the guide, 39, L80, L81, the sixteen passages and the two sealed maps. No map was opened.

**What differs from the eleventh version.** Six lines of the plan — the title, the preamble, P3, P4, P9 and B9 — and three lines of the translator. The expectations table is byte-identical apart from B9, and the marking rule and the probes' exposure section are byte-identical, each checked by diff.

---

## Part 1. The premises

Ten are FOUND. **P3 is FOUND WITH A DIFFERENCE**, on the ground it gives for one rule, and that difference is what stops the freeze.

### The tool change — verified

`translate_via_api_2.py` differs in exactly three lines: one sentence of the docstring, a new `CAP = {"atria": 65536, "mimo": 100000}` at line 22 with the reason in a comment, and `str(CAP[provider])` in place of `"100000"` at line 121. Nothing else moved, so the validation function P9 describes is untouched and everything verified about it before still holds.

### P9 — FOUND

"Calls `ask_model_2.py` with a completion cap of 65,536 for Atria and 100,000 for Mimo" is exactly the `CAP` dict and exactly what line 121 passes.

### P4 — FOUND

The second run's record is right in every particular I could check against the outputs.

The receipts under `results/L82 Arm B outputs - second run, stopped 20:25 ...` show status 400 on one attempt, `"failed": true`, not retried; the request files carry `max_tokens: 100000`; and the error file holds the JSON P4 quotes verbatim — `{"error":{"message":"max_tokens must be an integer between 1 and 65536.","type":"atria_api_error","code":"invalid_request"}}`. Two attempt files per text are the translator's two validation attempts, which is what "not retried" at the HTTP level plus one validation retry produces. All sixteen texts were reached, consistent with eight lanes and an immediate refusal. The Mimo side holds prompts and requests only, as P4 says.

The attempt history for those 400s reads `{"attempt": 1, "status": 400, "seconds": 1.8, "finish": null, "chunks": 0}` — which is also the first production confirmation that the tenth version's per-attempt reset works: a refusal that produced no stream records zeros rather than carrying anything forward.

The cap probes are real and are honestly described. `scratchpad/captest` holds `atria65536` with `max_tokens: 65536` finishing `stop`, and `mimo100000` with `max_tokens: 100000` finishing `stop`. P4 calls them "short calls, both answered", which is the accurate claim: they establish that the caps are *accepted*, not that they are *sufficient*.

P4's arithmetic is right, and it takes up the correction I recorded last round: "a 65,536-token Atria call takes about 20 minutes at its observed 54 tokens a second; a 100,000-token Mimo call about 50 at the probes' 33". 65,536 ÷ 54 is 1,214 s; 100,000 ÷ 33 is 3,030 s. Dropping the old "bounds its calls at about 97,000 tokens" inference is also right, because at 65,536 the cap now binds well before Atria's 1802-second cut.

### P3 — FOUND WITH A DIFFERENCE

The hashes and every behavioural clause carried over from the eleventh version were re-checked and hold. P3 no longer carries the justification for the `-4` rule; it says only "an empty answer whose finish reason is `length` is not retried, status -4". The justification now lives only in the caller's docstring, at the hash P3 records:

> an empty answer whose finish reason is `length` is not retried **(the same cap gives the same answer)** and is recorded as status -4

**The project's own probe record refutes that parenthesis.** Two long Atria calls were made on B01's prompt, at the same cap of 60,000 and at the same settings the run will use:

- `stream_probe.py`, whose request body is `{"model": "Atria-Dawn-Preview", messages, "max_tokens": 60000, "temperature": 0.2, "stream": true}` — no `reasoning_effort`, which is the run's own configuration. Its log ends `DONE t=1075s chunks=21999 reasoning=246591 content=0 finish=length usage={... 'completion_tokens': 60000 ...}`. The cap was exhausted and nothing was produced.
- `ask_model_2.py` at the provider's default effort, same cap. Its receipt reads finish `stop`, 39,997 completion tokens, 34,505 of them reasoning. It answered, and the answer validated as a 20-line ledger.

Same model, same prompt, same effort, same temperature, same cap: one call burned the whole budget on reasoning and returned nothing, the other answered using two-thirds of it. The same cap did not give the same answer.

This matters more in this version than it did in any earlier one, because Atria's ceiling is now a **hard provider limit**. 65,536 is what the API will accept and no more; it is 9 per cent above the 60,000 that was exhausted in the probe above. When an Atria call exhausts 65,536, the caller does not retry; the translator makes its single validation retry; if that call also exhausts, the text is dropped with no ledger. On this evidence a further attempt had a real chance of answering — the call that did answer did so on its fifth attempt, after three cuts and a 502.

What that costs is not confined to B5. A dropped Atria ledger counts toward B5's "13 or fewer valid for either provider", and B5's unmarkable clause then removes that text from B1 to B4, B6, B7 and B10 to B13. The rule that was adopted to save time on a deterministic failure will, on the plan's own data, spend the arm's yield on the one provider whose cap cannot be raised.

I am reporting the refuted ground rather than prescribing the fix. Either a `length` exhaustion is retried like any other failure, which is the only lever left once the cap is fixed by the provider, or the rule stands and the docstring says what is actually true — that a retry may answer and the rule trades that chance for time — with the consequence recorded.

### P1, P2, P5, P6, P7, P8, P10, P11 — FOUND

All are byte-identical to the eleventh version and rest on files unchanged at their hashes; their contents were verified in full over earlier rounds.

---

## Part 2. The expectations, and the marking rule

Twelve rows, the marking rule and the probes' exposure section are byte-identical to the eleventh version, confirmed by diff. They stand as checked and found sound over the fourth to eleventh rounds.

### B9 — sound, with one number left inconsistent

The tail now reads "six streamed attempts of up to 50 minutes each", which is the Mimo bound at the probes' 33 tokens a second and takes up the correction I recorded last round. For Atria an attempt is now bounded at about 20 minutes by the cap, which arrives before the 1802-second cut, so the Mimo figure covers both. Two texts a lane inside five hours remains the right order, and the tail is bracketed as before.

One number was left behind: the prose-reader clause of the same cell still says "about 13 minutes at Mimo's observed 37 tokens a second". At the 33 the rest of the plan now uses, a capped prose-reader call is about 15 minutes and four rounds about 60, against a 90-minute budget — still sound, so nothing turns on it, but one cell should not quote two rates for one model.

### B5 — unchanged, and correctly bracketed for what may now happen

B5 is untouched and still brackets both sides: at least 14 of 16 per provider, 13 or fewer counts against, charged to the translator or the guide, with a text that fails both attempts listed and the run continuing without it. If Atria loses texts to the cap, B5 fires and the marking rule removes them from every row that counts them. The row works; what the plan does not say is that this is now a foreseeable outcome rather than a remote one.

---

## Part 3. The run spec

`L82_run_2.sh` is unchanged at `f3a5b90189f378f0` and was read line by line on the ninth round; `ask_model_2.py` is unchanged at `d1d55e43543d4dcd` and was verified on the tenth and eleventh. The translator's change cannot reach either: the runner invokes the translator by name and reads its exit code, and the caller receives `--max-tokens` as a string either way.

The one thing worth restating about what a failed text leaves, because the cap makes it newly likely: an Atria text that exhausts 65,536 produces an empty answer with finish `length`, recorded as `-4` with its own chunk count and seconds, no retry, an error file, a reasoning file and a failure receipt; the translator's second validation attempt does the same; no validation file is written, so the gate skips the text and it is absent from both drivers, consequences, both sameness runs, the reader and the prose reader. That chain is intact and was verified before. It is efficient, and on this evidence it may be triggered by texts that a third call would have answered.

---

## Verdict

**DO NOT FREEZE YET.**

The change this version makes is right and I verified it: the per-provider cap is three lines, both values are probed as accepted, P9 and P4 describe them accurately, the second run's record matches its receipts to the token and the error string, and B9's translation arithmetic now uses the corrected Mimo rate. The preamble's admission that the 100,000 cap "had been probed on neither provider" is the right lesson to write down.

What stops the freeze is not that change but what this version's hard ceiling does to a rule inherited from the ninth. The caller declines to retry a `length` exhaustion on the ground that "the same cap gives the same answer", and the plan's own probes show the same prompt, cap and settings exhausting 60,000 with no content in one call and answering at 39,997 in another. With Atria now fixed at 65,536 — nine per cent above the cap that was exhausted — that rule will drop Atria ledgers the evidence says were obtainable, and each one is removed from B1 to B4, B6, B7 and B10 to B13 by B5's unmarkable clause.

What must change:

1. **Revisit the `-4` no-retry rule, and correct the ground given for it.** `ask_model_2.py`'s docstring says a `length` exhaustion "is not retried (the same cap gives the same answer)". The probe record refutes it: on B01's prompt, with no `reasoning_effort` set and a 60,000 cap, `stream_probe.py` ended `finish=length ... completion_tokens: 60000, content=0`, while `ask_model_2.py` at default effort and the same cap ended finish `stop` with 39,997 completion tokens and a ledger that validated. Either retry a `length` exhaustion like any other failure — the only lever left now that Atria's cap is fixed by the provider — or keep the rule and say truthfully that it trades a real chance of an answer for time.

2. **Record that Atria's 65,536 is a hard provider ceiling and what follows from it.** P4 says the caps were "probed as accepted (short calls, both answered)", which is honest as far as it goes, but nothing in the plan says the cap was not probed as *sufficient*, that it is nine per cent above a cap Atria has been seen to exhaust at the run's own settings, or that a text needing more cannot be run at all and will be listed under B5 and removed from nine other rows. This belongs with the plan's other recorded limits — the 1802-second cut, the blinding's reach, the guard's process group — and the plan has always been better for stating them.

3. **Tidy B9's second rate.** The cell now uses Mimo at 33 tokens a second for the translations and still at 37 for the prose reader. At 33 the prose-reader worst case is about 60 minutes against 90, so the row stays sound; one cell should not carry two rates for one model.
