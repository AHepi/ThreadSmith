# Premise check - L82 Test plan, Arm B, eleventh version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, eleventh version.md`. Hashed: the first sixteen digits are `7f5faefafeec74b0`, as the coordinator said. Confirmed. Read whole. The tree is clean at `6a84d6d`.

`Language/tools/ask_model_2.py` was re-read at its new hash `d1d55e43543d4dcd`. Everything else is unchanged at the hash the tenth version recorded: `translate_via_api_2.py` `9496d3923ae367c2`, `L82_run_2.sh` `f3a5b90189f378f0`, the three first-version tools, both drivers, `sameness_2.py`, `consequences_2.py`, `PAIRS.txt`, the briefs, the guide, 39, L80, L81, the sixteen passages and the two sealed maps. No map was opened.

**What differs from the tenth version.** Three lines of the plan — the title, the preamble and P3 — and the caller's docstring. The expectations table, the marking rule section and "The probes' exposure, beside the rows it touches" are byte-identical, each checked by diff.

---

## Part 1. The one change

### P3 — FOUND

My single item from the tenth version is answered, and answered in both places it needed to be.

P3 now reads: "an empty answer whose finish reason is `length` is not retried, status -4; an empty answer with no finish reason (a stream that carried chunks and then closed cleanly, which is Atria's cut in P4) or with any finish reason other than `length` is retried, -2; a 200 whose stream yields no parsable chunk -3; a raised exception 0, which is a connection closed without any response (the first run's `RemoteDisconnected`), a reset, or silence for `--idle` seconds."

Checked clause by clause against the code at its new hash:

- Line 107, `if status == 200 and not chunks: status = -3` — a 200 whose stream yields no parsable chunk is `-3`.
- Line 108, `elif status == 200 and not content.strip(): status = -4 if finish == "length" else -2` — an empty answer is `-4` when the finish reason is `length` and `-2` otherwise, which covers both a finish reason of `None` and any other value. That is exactly what P3 now says, and it is what the old clause did not say.
- Lines 98 to 103 — an HTTPError takes the provider's code; a `socket.timeout` or `TimeoutError` takes `0`, which is the silence case; any other exception takes `0`, which is where a connection closed without a response and a reset land. "A raised exception 0" with those three instances named is right.

The two attributions are right as well, and I checked both against the evidence rather than the prose. Atria's cut is recorded in `results/L82 Probes .../default and medium effort/B01.atria.receipt.json` as `-2` at 377.0, 1802.3 and 1802.4 seconds with 1,487, 8,597 and 8,974 chunks and no finish reason — a stream that carried chunks and then closed cleanly, exactly as P3 now describes it, and the events P4 calls "the stream closed ... and no finish reason". The first run's failures are recorded as status `0` with `RemoteDisconnected('Remote end closed connection without response')` in the error file — a connection closed without any response. The two labels that were crossed now point at the events they belong to, each with the record that establishes it.

The caller's docstring carries the same sentence, in the same terms.

### The two label sets in P3 are both correct, and are not a contradiction

P3 describes two callers: the second version, which the run will use, and the first version, which is kept beside it and is what the first run used. Their label sets differ, and a quick reading could take that for an inconsistency, so I checked both against their own tools.

The second-version caller has no `-1`: parsing happens per chunk with the failure skipped, so a body yielding nothing parsable arrives with zero chunks and is `-3`. The first-version caller does have `-1` — line 73, `except Exception: status = -1` — because it parses one whole body; and its `-3` means a 200 with no choices, line 76, not a stream with no chunks. P3's "for the record" description of the old caller, "0 for an exception, -1 unparsable, -2 empty content, -3 no choices", is accurate for that file, and the new description is accurate for the new one. Keeping both, clearly separated, is right, and nothing here needs changing.

### Everything else in P3, and the other ten premises — FOUND

The rest of P3 is byte-identical to the tenth version and was verified against the code then: the streamed request, the `--idle` read timeout, `--attempts` with backoff 10, 20, 40, 80, 120, the six statuses not retried, the per-attempt reset, the receipt's contents, and `--effort` and `--extra` recorded and unused. P1, P2, P4 to P11 are byte-identical to the tenth version and rest on files that are unchanged at their hashes; their contents were verified in full over the ninth and tenth rounds, including P4's first-run receipts and probe figures, which I checked to the tenth of a second and the token.

---

## Part 2. The expectations, and the marking rule

All thirteen rows, the marking rule section and the probes' exposure section are byte-identical to the tenth version, confirmed by diff rather than by eye. They stand as checked and found sound over the fourth to tenth rounds. Nothing in this version's change reaches them: no row reads an attempt status.

---

## Part 3. The run spec

`L82_run_2.sh` and `translate_via_api_2.py` are unchanged at their hashes and were read line by line on the ninth round. The caller's change cannot reach them, because it is confined to a docstring — which I established rather than assumed.

**How that was established, including two false starts.** My first check diffed both files from a fixed line offset, and my second compared compiled constant tables. Both reported a difference, and both were wrong: the new docstring is two lines longer than the old, so a fixed offset lands in different places in the two files, and a code object's line numbers shift with it. Parsing each file and taking everything after the module docstring gives the honest comparison:

```
old body: 105 lines, sha256 2afdeab272c8970b
new body: 105 lines, sha256 2afdeab272c8970b
EXECUTABLE BODY IDENTICAL: True
docstring: 23 lines -> 25 lines; 6 changed lines in the file, all inside it
```

So "docstring only; the code is unchanged from `6de5bd9f4c6a81e2`" is verified. I record the false starts because the same shape of mistake — a test whose subject is not in the state the test assumes — is what let the seventh version's start guard through, and because a check that reports a difference it cannot explain should not be left in the record unexplained.

---

## Verdict

**FREEZE.**

All eleven premises are found at their hashes, every hash re-taken at the current tree. The single item from the tenth version is answered in both the premise and the tool that premise describes, with the evidence for each label attached — Atria's clean cut to `-2`, the first run's `RemoteDisconnected` to `0`. The executable code is unchanged and I proved it rather than accepting it. The expectations table, the marking rule and the probes' exposure section are byte-identical to the version whose soundness I have already established row by row.

**Nothing must change before the freeze.**

Three things I have recorded along the way and would carry into the run rather than into another draft:

1. Eight concurrent Atria streams, each possibly open for half an hour, is a concurrency the probes never exercised. Nothing claims otherwise and no premise rests on it, so it is not a defect; it is the kind of unknown the 301-second wall turned out to be, and it will show in the first minutes of step 1 if it shows at all.
2. B9's prose-reader arithmetic uses Mimo at 37 tokens a second, which comes from the earlier pilot; the three probe calls give 32.8, 33.4 and 34.0. The budgets are bracketed either way and B9 is sound, but the true figure is nearer 33 and the margin is correspondingly smaller than the cell implies.
3. The start guard cannot see a caller in its own process group. This is now written into "Not tested" with the operating instruction that follows from it, which is where it belongs.

This is the eleventh version. I have raised thirty-nine items across nine checks; all are answered, and the plan is in a state I would mark against.
