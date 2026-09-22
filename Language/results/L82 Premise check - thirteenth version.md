# Premise check - L82 Test plan, Arm B, thirteenth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, thirteenth version.md`. Hashed: the first sixteen digits are `f2980f606ad46a85`, as the coordinator said. Confirmed. Read whole. The tree is clean at `163d5cf`.

`Language/tools/ask_model_2.py` was re-read at its new hash `9dbfd37f61a97c6b`. Everything else is unchanged at the hash the twelfth version recorded: the translator `b92bfe0a4bf4bf46`, the runner `f3a5b90189f378f0`, the three first-version tools, both drivers, `sameness_2.py`, `consequences_2.py`, `PAIRS.txt`, the briefs, the guide, 39, L80, L81, the sixteen passages and the two sealed maps. No map was opened.

**What differs from the twelfth version.** Six lines of the plan — the title, the preamble, P3, P4, B9 and "Not tested" — and in the caller, one executable line and a passage of the docstring. The expectations table is byte-identical apart from B9; the marking rule and the probes' exposure section are byte-identical; each checked by diff.

---

## Part 1. The premises

Ten are FOUND. **P4 is FOUND WITH A DIFFERENCE**, on one count, and that is the only thing outstanding.

### The caller's change — verified, and correct

The executable change is one line. `final = status in (400, 401, 403, 404, 413, 422, -4)` has become `final = status in (400, 401, 403, 404, 413, 422)`, with the reason in a comment. I compared the two files after stripping the module docstring: 105 lines each, two changed lines, both the one above. Nothing else in the body moved.

Traced through: a `length` exhaustion is still labelled `-4` at line 110 and recorded in the history with its own seconds, finish reason and chunk count; `final` is now false for it, so line 114 falls through to the backoff and it is retried like any other failure. That is my first item from the twelfth version, answered.

### P3 — FOUND

"An empty answer whose finish reason is `length` is recorded as status -4 and retried like any other failure, since the same prompt at the same cap has answered on one attempt and exhausted the cap on another (P4)." That is what the code now does, and the count it gives — one answer, one exhaustion — is the count the evidence supports.

### P4 — FOUND WITH A DIFFERENCE

Everything about the ceiling is right, and it is the part I asked for. P4 now says the caps were probed "as accepted, not as sufficient", and that "Atria's 65,536 is a ceiling its API enforces and cannot be raised", and it draws the consequence: "a text that needs more than 65,536 tokens from Atria cannot be translated by it through this pipeline, and a text near that size gets its answer, if at all, on a retry." "Not tested" carries the same, tied to B5. That is my second item, answered well.

**The difference is a count.** P4 says the ceiling is "nine per cent above the 60,000 that Atria exhausted on B01 at the run's own settings **on two probe calls while answering on a third** with 39,997".

I enumerated every Atria request body in the probes folder to check it. On B01 there are four Atria calls, and their bodies are:

| call | max_tokens | reasoning_effort | reasoning extra | outcome |
| --- | --- | --- | --- | --- |
| `stream_probe.py` | 60,000 | none | none | exhausted, finish `length`, no content |
| `default and medium effort/B01.atria` | 60,000 | none | none | answered, 39,997 tokens, valid ledger |
| `B01.atria.medium` | 60,000 | `medium` | none | exhausted |
| `B01.atria.budget30k` | 60,000 | none | `{"max_tokens": 30000}` | exhausted |

The run's own settings are no `reasoning_effort` and no `reasoning` extra — `stream_probe.py`'s body is `{"model": "Atria-Dawn-Preview", messages, "max_tokens": 60000, "temperature": 0.2, "stream": true}`, which is the run's shape exactly. Only the first two calls are at those settings, and of them **one exhausted and one answered**. The answering call took five HTTP attempts — three clean cuts, a 502, then the answer — and none of those attempts was a `length` exhaustion.

So at the run's settings there are two calls, not three, and one exhaustion, not two. Reading "the run's own settings" loosely, to mean the same model, prompt and cap while ignoring the reasoning knobs, gives three exhaustions and one answer across four calls — which is not the stated shape either. The sentence does not match the record on any reading.

The conclusion P4 draws from it is nonetheless right, and nothing rests on the inflated number: one exhaustion and one answer on the same prompt at the same cap is already enough to refute "the same cap gives the same answer", which is what the retry change needed. The plan states the correct count in its other three places — the preamble ("a valid ledger on one call, all tokens on reasoning on another"), P3 ("answered on one attempt and exhausted the cap on another") and the caller's docstring ("39,997 tokens and a valid ledger on one call, all 60,000 on reasoning and no content on another"). P4 is the outlier, and it is the most circumstantial of the four, so it is the one a later reader would take as authoritative.

### P1, P2, P5 to P11 — FOUND

All are byte-identical to the twelfth version and rest on files unchanged at their hashes; their contents were verified in full over earlier rounds, including P9's per-provider caps against the `CAP` dict and P11's runner line by line.

---

## Part 2. The expectations, and the marking rule

Twelve rows, the marking rule and the probes' exposure section are byte-identical to the twelfth version, confirmed by diff. They stand as checked over the fourth to twelfth rounds.

### B9 — sound, and the last rate is fixed

The prose-reader clause now reads "about 15 minutes at Mimo's observed 33 tokens a second, four rounds about 60 minutes", against a 90-minute budget. 30,000 ÷ 33 is 909 seconds, and thirty-two calls in eight lanes is four rounds. The cell now carries one rate for Mimo throughout. My third item, answered.

**One consequence of the retry change that B9 already brackets but which is worth seeing plainly.** Before this version, an Atria text that exhausted the cap cost two calls — one per validation attempt — and was dropped in about forty minutes. Now it costs up to six calls per validation attempt, so up to twelve calls and roughly four hours, at about twenty minutes a capped Atria call. With eight lanes and two texts a lane, a handful of such texts makes B9's five hours a good deal more exposed than it was. The row says "a text that exhausts six streamed attempts of up to 50 minutes each could alone take longer; it is listed under B5, and the budget is still charged", so the outcome is bracketed and the row is sound. It is the right trade — the retry is the only way left to get a ledger out of Atria near its ceiling — but B9 is now more likely to fire, and for a reason the plan has chosen.

---

## Part 3. The run spec

`L82_run_2.sh` is unchanged at `f3a5b90189f378f0` and `translate_via_api_2.py` at `b92bfe0a4bf4bf46`; both were read line by line on earlier rounds. The caller's change cannot reach them: the runner and translator read an exit code and a set of output files whose names and meanings are unchanged.

What a failed text leaves is unchanged in kind and longer in duration. An Atria text that exhausts its cap now produces up to six `-4` entries per validation attempt, each with its own seconds, finish reason and chunk count, then an error file, a reasoning file and a failure receipt; the translator's second validation attempt does the same; no validation file is written, so the gate skips the text and it is absent from both drivers, consequences, both sameness runs, the reader and the prose reader, listed under B5 and removed from every row that counts it. That chain was verified before and is intact.

---

## Verdict

**DO NOT FREEZE YET** — for one sentence in P4, and nothing else.

All three items from the twelfth version are answered, and the first two are answered exactly as the evidence required. The `-4` rule is reversed in one line, with the probe record given as its ground in both the code comment and the docstring; Atria's ceiling is now recorded as provider-enforced and probed as accepted rather than sufficient, with the consequence carried into "Not tested" and tied to B5; and B9 carries one rate for Mimo.

What is left is that P4 describes the evidence for the reversal as two exhausting calls and a third that answered, when the record holds two calls at the run's settings, one exhausting and one answering. The reversal is right regardless, and the preamble, P3 and the caller's docstring all state the count correctly — which is what makes P4's version worth correcting rather than letting stand, since a premise is frozen for other people to read and this is the one of the four that carries the detail.

What must change:

1. **Correct P4's count of the Atria probes.** It reads "the 60,000 that Atria exhausted on B01 at the run's own settings on two probe calls while answering on a third with 39,997". At the run's own settings — no `reasoning_effort`, no `reasoning` extra, which is `stream_probe.py`'s body and the default-effort `ask_model_2.py` call — there are two calls on B01: one exhausted 60,000 with no content, and one answered with 39,997 tokens and a ledger that validated, on its fifth HTTP attempt after three cuts and a 502, with no `length` exhaustion among those attempts. The other two Atria calls on B01 set `reasoning_effort: medium` and `reasoning: {"max_tokens": 30000}` and are not at the run's settings; counting them gives three exhaustions and one answer across four calls, which is not the stated shape either. The wording used in the preamble, P3 and the docstring — one call answered, another exhausted — is the one the record supports.

One thing I would record rather than change: now that a `length` exhaustion is retried, an Atria text that cannot fit its ceiling costs up to twelve calls and about four hours instead of two calls and forty minutes. B9 brackets that and the trade is the right one, but the row is materially more likely to fire than it was, and it will be worth watching Atria's first capped text in the run rather than discovering the cost at the end.
