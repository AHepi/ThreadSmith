# Premise check - L82 Test plan, Arm B, fourteenth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, fourteenth version.md`. Hashed: the first sixteen digits are `8c1b4473fb5284b4`, as the coordinator said. Confirmed. Read whole. The tree is clean at `e5e5d72`.

**No tool changed.** Every artefact in P3 was re-hashed at the current tree and every one is at the hash the thirteenth version recorded: `ask_model_2.py` `9dbfd37f61a97c6b`, `translate_via_api_2.py` `b92bfe0a4bf4bf46`, `L82_run_2.sh` `f3a5b90189f378f0`, the three first-version tools, both drivers, `sameness_2.py`, `consequences_2.py`, `PAIRS.txt`, the briefs, the guide, 39, L80, L81, and the sixteen passages with the two sealed maps. No map was opened.

**What differs from the thirteenth version.** Three lines: the title, the preamble and P4. I checked the rest structurally rather than by eye — all thirteen rows of the expectations table are byte-identical, as are the marking rule, the probes' exposure section, "Not tested", "What is scored and what is only recorded", "Near-miss cases that must not fire" and "Traps", and so is every premise but P4.

---

## Part 1. P4 — FOUND

My single item from the thirteenth version is answered, and the corrected sentence is right in every clause. It now reads:

> Atria's 65,536 is a ceiling its API enforces and cannot be raised; it is nine per cent above the 60,000 that Atria exhausted on B01 at the run's own settings on one probe call (the first streamed probe, no effort or budget set) while answering on the other call at those settings with 39,997 (the caller's default-effort call, on its fifth HTTP attempt); the two further Atria calls on B01, with `reasoning_effort: medium` and with a reasoning budget, are not at the run's settings and both exhausted; so a text that needs more than 65,536 tokens from Atria cannot be translated by it through this pipeline, and a text near that size gets its answer, if at all, on a retry.

I re-enumerated every Atria call on B01 in the probes, reading each request body for the two settings that distinguish them and each receipt for the outcome:

| call | cap | `reasoning_effort` | reasoning budget | finish | completion | attempts |
| --- | --- | --- | --- | --- | --- | --- |
| `stream_probe.py` | 60,000 | none | none | `length` | 60,000 | 1 |
| `B01.atria` | 60,000 | none | none | `stop` | 39,997 | 5 |
| `B01.atria.medium` | 60,000 | `medium` | none | `length` | 60,000 | 2 |
| `B01.atria.budget30k` | 60,000 | none | `{"max_tokens": 30000}` | `length` | 60,000 | 4 |

Every clause of the sentence matches. The two calls at the run's own settings are the first two rows, and of them one exhausted and one answered with 39,997 on its fifth HTTP attempt. The two further calls are the third and fourth rows, each distinguished by exactly the setting P4 names, and both exhausted. The arithmetic holds too: 65,536 is 9.2 per cent above 60,000.

The sentence also now identifies each call by the thing that separates it, so a later reader can repeat the check without guessing which probe is which. That is the difference between a count that can be verified and one that has to be trusted, and it is the right way for a frozen premise to carry a number.

## Part 1 (continued). The other ten premises — FOUND

P1, P2, P3 and P5 to P11 are byte-identical to the thirteenth version and rest on files that are unchanged at their hashes, every one re-hashed this round. Their contents were verified in full when each last changed: P1's sentence counts and P2's connective sets and eight diffs against the corpus; P3's caller clauses against the code, including the `-4` retry and the labelled attempt history; P5's driver templates and OUTCOMES accounting; P6's line numbers; P7's verbatim quotations from L81; P8's buckets and partition, re-run; P9's per-provider caps against the `CAP` dict; P10's two brief formats; and P11's runner line by line.

---

## Part 2. The expectations, and the marking rule

All thirteen rows, the marking rule section and the probes' exposure section are byte-identical to the thirteenth version. They stand as checked and found sound over the fourth to thirteenth rounds: every "against" brackets both sides, every outcome falls on a side or is named unmarkable, each row names the layer that would have moved, none is stated by the map, and no two rows give contradictory charges on one outcome.

---

## Part 3. The run spec

`L82_run_2.sh`, `translate_via_api_2.py` and `ask_model_2.py` are all unchanged at their hashes and were each read line by line when they last changed. Nothing in this version reaches them.

---

## Verdict

**FREEZE.**

The single item from the thirteenth version is answered, and answered in the way that makes the premise checkable rather than merely corrected: P4 now names each probe call by the setting that distinguishes it, and I confirmed all four against their request bodies and receipts. Every other line of the plan is byte-identical to a version I have already checked, and every tool is at a hash I have already verified.

**Nothing must change before the freeze.**

Three things I would carry into the run rather than into another draft, all recorded in earlier reports:

1. **B9 is more likely to fire than it was.** Now that a `length` exhaustion is retried, an Atria text that cannot fit its 65,536 ceiling costs up to twelve calls and about four hours, against two calls and forty minutes before. The row brackets it and the trade is right — the retry is the only way left to get a ledger out of Atria near its ceiling — but it is worth watching Atria's first capped text during the run rather than discovering the cost at the end.
2. **Eight concurrent Atria streams, each possibly open for twenty minutes or more, is a concurrency the probes never exercised.** No premise rests on it, so it is not a defect; it is the kind of unknown the 301-second wall and the 65,536 ceiling both turned out to be, and it will show in the first minutes of step 1 if it shows at all.
3. **The start guard cannot see a caller in its own process group**, which "Not tested" records together with the operating instruction that follows from it.

This is the fourteenth version. Across eleven checks I have raised forty-three items; all are answered. Two of them were found only because the plan was run and failed, and three more because a premise was compared against the project's own evidence rather than against itself. The plan is in a state I would mark against.
