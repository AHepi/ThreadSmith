# Premise check - L82 Test plan, Arm B, fourth version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, fourth version.md`. Hashed: the first sixteen digits are `524e70daa51893c5`, as the coordinator said. Confirmed. Read whole.

The two changed files were re-read at their new hashes and both are as named: `Language/tools/L82_run.sh` at `e52f9478c5bde4cd` and `Language/tools/ask_model.py` at `e00b8b6cedb81b79`. Every other artefact in P3 was re-hashed and is unchanged, as were the sixteen passages, `MAP.enc` and `MAP2.enc`. No map was opened.

Method as before: every fact checked by hand against the file it names. Hashes are sha256sum, first sixteen hex digits.

---

## Part 1. The premises, P1 to P11

**All eleven are FOUND.** That is the first time in four versions. What follows records what was checked rather than arguing a case.

### P1. The passages, the sealed maps, the sentence counts — FOUND

All sixteen hashes match the files and match MANIFEST.json, and `MAP.enc` (`4dce17f60633fa79`) and `MAP2.enc` (`5e9a35e2e80e7c00`) match too. The corpus is byte-identical to the corpus I checked on the second and third versions, where I counted the sentences of all sixteen passages by hand twice; the counts P1 lists are those counts. The caveat that the two sealed-plaintext hashes are copied from the manifest and cannot be checked without opening the seal is still there and still right.

### P2. The connectives and the diffs — FOUND

Unchanged text over an unchanged corpus. The six connective sets, the note that "because" falls twice each in B05 and B10, and all eight sentence-by-sentence diffs were verified by hand on the second and third versions and hold: B16 from B08 in the third sentence, B11 from B03 in the third, B14 from B09 in the fourth, B01 from B08 in the second, B06 from B03 in the second, B04 from B09 in the second, B10 from B05 in the fourth, B12 from B15 in the second, each differing in exactly one sentence and byte-identical elsewhere.

### P3. The tools, the drivers, the materials, the briefs, the calibration — FOUND

All fourteen hashes match: `ask_model.py` `e00b8b6cedb81b79`; `translate_via_api.py` `0053f66020414e31`; `sameness_2.py` `e66a9d314a0227b6`; `consequences_2.py` `d04f6dfd08268ce7`; `L82_run.sh` `e52f9478c5bde4cd`; `run_check.py` `eff1dee15bebc977`; `run_check_2.py` `9a4b21cf771b1208`; `39` `dcfbed45d4e94861`; `L80` `ec16e220a433e24a`; the encoding guide `afe860e1509caf09`; the reader brief `ddeba43abbbc1dba`; the prose reader brief `888a45f49248fba3`; `PAIRS.txt` `6da2ec538b581a22`; L81 `c8ff6244676b3c0e`. The four example files are present, and PAIRS.txt holds exactly the eight pairs in the order P3 quotes.

The behavioural clauses attached to the caller are all true of the file at that hash, including the three that are new:

- "a 400, 401, 403, 404, 413 or 422 is not retried **and the error file and the message say how many attempts were made**". The old `attempts = 6` trick is gone, replaced by a `final` flag, and both the error file and the stderr line now read `status %s after %d attempt(s)` with ` (not retried)` appended. A rejected request now reports one attempt, not six.
- "a well-formed answer with empty content is retried like a failure". The break condition now requires `((data["choices"][0].get("message") or {}).get("content") or "").strip()`, and an empty answer sets `status = -2` and falls through to the retry. Whitespace-only content counts as empty, which is the right reading.
- "a failed call leaves `<tag>.error.txt` **and a receipt with `"failed": true`**". It does, carrying the status, the true attempt count, the elapsed seconds, the tag and the user file.

Timeout 2400 s, backoff 10/20/40/80/120, one lock per provider in `$ASK_MODEL_LOCKDIR` when set, and the gap at 60/rpm plus a tenth are all unchanged and all as stated.

### P4. The pilot — FOUND

Unchanged from the third version and re-checked against the files, which are unchanged: Atria on T10-D `"attempts": 1`, `"seconds": 263.3`, six lines, validation file beginning `rebuilt from ...`; Mimo `"attempts": 1`, `"seconds": 355.0`, six lines, `attempt 1` / `VALID`; the two quoted old-driver strings verbatim; the two stopped T11-B calls, each leaving a prompt and a request file and nothing else; both made by the caller at `31ec591f2e2a3d02` with a 900-second timeout; reasoning tokens 1,908 of 3,593 and 10,800 of 12,258.

### P5. What the new driver does and prints — FOUND

The clause I marked false last time is repaired, and repaired with the evidence attached. P5 now says the world name "also appears unquoted in every named line's printed text, because the guide fixes a line's `text` field as `[<standing>] <the line>`, so a told line reads `[TOLD in world <name>] ...` and a supposed line `[SUPPOSED in case <name>] ...` (`example_T10D.json` shows it on all six lines); P11 blinds both places." Checked: the guide's line 19 does fix the field that way, `example_T10D.json` does carry `[TOLD in world account_world]` on all six lines, and the runner does blind both places. A live ledger in the second pilot shows the same thing from the other side — its `denied` line's text reads `[CLAIMED] NOT [line returned BECAUSE line burning]; ...`, and its world name `inspector_world` appears both in the quoted heading and in the GAUGE's bin quotation.

Two additions are also correct. "The because verdicts are FOLLOWS, CIRCLE, FOLLOWS ONLY IF THE CAUSE IS GRANTED and JUMP" — those are exactly the four `verdicts[n]` assignments in check 2. "`reading()` returns `ran out of time` first, whenever a query exceeded the driver's 20-second limit" — `reading()`'s first test is `if out_of_time.get(name)`, `out_of_time` is set whenever a query times out, and `TIME_LIMIT_SECONDS = 20`.

Everything carried over from the third version was re-checked and still holds: the check list with the what-ifs excluded by `if world is None`, all five quoted finding templates with their tails, and the OUTCOMES accounting at twelve names in the actual ledger and eleven inside a world with the five forms.

One small imprecision, noted and not counted as a difference because the clause that follows repairs it: "every named line's printed text" is not literally every line the report names. A CLAIMED or GIVEN line's prefix carries no world name, and the CLAIM AND DENY sentence names two lines by id without printing their texts. The point P5 is making — that the standing prefix is printed and carries the world name for told and supposed lines — is true and is the point that matters.

### P6. The old driver's silence, and its actual-ledger reach — FOUND

Unchanged and re-verified. Line 69 sets `WORLD_REMOVED[:] = all_case_lines` before every check; lines 313 to 320 are the world's removal, the single `contradiction(F)` ask and the `INSIDE '<name>' ... no contradiction.` print; line 327 restores it; check 2's comment is at line 95 and its head at line 99 is `BECAUSE-claim on line %s: "%s".` without the mark-and-sentence bracket. The second pilot's B99 report is a fresh instance of the second half: the old driver reached an actual-ledger `DENIED BECAUSE` and printed `Fine.` while saying only `no contradiction` inside the told world.

### P7. L81 section 3, the marking rule, section 5 — FOUND

Unchanged from the third version, where I compared every quotation against L81 at `c8ff6244676b3c0e`. The four cases are verbatim with case 3 carrying both halves; the marking rule is verbatim including the prose-reader limb and the sentence explaining why the role exists; the variation list, the hedge sentence and the whole of section 5 are verbatim.

### P8. The sameness buckets and the partition — FOUND

Re-read and re-run on `ledger_A.json` against `ledger_A2.json`. The six headings printed exactly as P8 quotes them, each with its count and in that order, followed by `BIN ENTRIES: first 0, second 0 (compare by reading)`. The partition over five buckets, with SAME CONTENT, DIFFERENT STANDING re-listing BOTH SAY pairs and `partition_or_stop` enforcing the rest, is as stated.

### P9. What the translator tool validates — FOUND

Unchanged and re-verified against the tool at its hash: the six required fields and the per-line fields; the guard check on the body after `:-` with the bare-fact consequence recorded; every sentence in a line or the bin; the old driver run in a temporary copy of the rig; one retry with the failures; `paragraph` by `setdefault` and `whose` to the provider, neither printed by either driver; the model's own line ids in the built `.pl`; and the validation file's two-line head. The second pilot's `B99.atria.validation.txt` is a live instance: `attempt 1` then `VALID`.

### P10. The briefs' answer formats — FOUND

Unchanged from the third version, where both briefs were compared line by line against the premise. The reader's four parts and three rules and its `READER:` / `READING COMPLETE` envelope, and the prose reader's four part-1 answers with their parenthetical instructions, its parts 2, 3 and 4 and its `PROSE READER:` / `READING COMPLETE` envelope, are all quoted accurately.

### P11. The runner — FOUND

Both descriptions I flagged are corrected and the new behaviour is described accurately.

The gate now reads "whose validation file has `VALID` alone on one of its first two lines (`head -2 | grep -qx`; P9 puts it on the second)" — which is what the code does and where P9 says the word lands. The prose reader directory now reads "with each prompt (named by ledger, no key needed)", which is right; there is no key there and none is wanted.

The new clauses are all true of the file: the blinding "replaced through placeholders in two passes (so a world already named `world_k` cannot collide with another's neutral name)"; "after the words `world` or `case` in line texts"; `name_still_present` listed "after the bin cut, and before the neutral names go in"; `FAILED.txt` taking "calls that exited non-zero, or returned an empty answer, recorded as exit 99" and the prose reader's "`FAILED.txt` and `SKIPPED.txt` on the same rules"; and "Its header says no other caller of either provider may run alongside it." All verified line by line in Part 3.

---

## Part 2. The expectations, B1 to B13, and the marking rule

Eleven of the thirteen rows are sound on all six questions. Two are not, and they share one defect.

**On the map — sound, unchanged.** No expectation needs MAP.json or MAP2.json. Every named instance is reachable from features I confirmed in the texts: the F-sides and S-sides by shared openings and the added rule, route or differently-denied cause; the controls by the absence of all six connectives; the hedged pair by "may have been" against "had been"; B13 by being the only passage with no reporting verb; the rewordings by their single-sentence diffs.

### B2 the S-sides — now sound

The wording is fixed in the way I asked and better. "B06 the because gets FOLLOWS or FOLLOWS ONLY IF THE CAUSE IS GRANTED (no JUMP)" names the met verdicts instead of naming one and implying the rest, and the against now adds the fourth verdict with its own charge: "a CIRCLE on B06 (the rule line runs through the conclusion, L81 case 3: charged to the translation, listed, and that ledger is unmarkable here)". All four of check 2's verdicts are now on a side.

The other three clauses were already exhaustive and I confirmed why. The since check has exactly two outcomes, `TO BE EXPECTED, using: ...` and `NO CONNECTION`, so "the since connects (no NO CONNECTION)" covers both. The plan clause is written as a complement. The denial clause names `Fine.` with no flag as met and both the CLAIM AND DENY line and `YOU DENY A CAUSE ...` as against, with a missing denied-because line unmarkable.

### B4 controls — now sound

`ran out of time` is bracketed: "a query over the driver's 20-second limit, recorded against the pipeline, listed, and that line is neither met nor against". With that, all five of `reading()`'s forms are accounted for — the two "not asked" forms meet the row, `asked, nothing found` counts against with its charge, `asked, N found` is a finding, and the fifth is recorded. The no-world case and the B13 precedence clause carry over from the third version.

### B7 the two translators agree in kind — now sound

The denominator is now principled rather than arbitrary: "Per text of the thirteen that carry a reported argument (all but B02, B07 and B13)", with "misses on at most 3 of the markable texts (13 if all are)" against "Misses on 4 or more markable texts". Exhaustive, and the three excluded texts are disposed of explicitly: "On B13 the kinds in the actual ledger are compared and recorded, not counted; the controls are B4's". That is the right disposal — B13 has no world by design and the controls are already B4's business.

### B11 the narrator's own — now sound

Every because verdict on B13 is on a side, and each is charged by its cause rather than by its name: "a FOLLOWS or a FOLLOWS ONLY IF THE CAUSE IS GRANTED from a said rule line is a rule the passage does not state (L81, a claim the reported person never made), from a filled-in or usual-case line an added line supplying the answer (L81 case 3), and a CIRCLE a route through the conclusion (case 3): each charged to the translator and listed, and the drivers' half is then unmarkable". That distinction — a said rule line against a filled-in or usual-case one, two different limbs of L81 — is finer than I asked for and is correct.

### B3, B5, B6, B8, B9, B12, B13 — sound, as before

B3's brackets and its unmarkable clause; B5's denominator of 14 of 16 with the TOLD requirement scoped to the thirteen texts that carry an argument; B6's band at two misses and three, with an invented sentence number charged to the reader and not the report; B8's two-sided simplicity resting on a P6 that now says what the code does; B12's order and its L81 section 5 charge; B13's coverage of all four prose-reader answers with B4 governing on controls. All were checked again and none has moved.

B9 gains the overlap clause: "No other caller of either provider runs while the runner runs (the lock is shared within one run only, P11); the pilot runs are finished before the run starts", against "a second caller found running alongside the run is recorded against the pipeline". That answers item 10 as a stated precondition with a consequence. The arithmetic behind the four budgets is unchanged and still works: 64 reader calls in eight lanes is eight rounds, 32 prose-reader calls is four rounds, sixteen texts in four lanes is four per lane, against 90, 60 and 180 minutes.

### B1 the F-sides — **a wrong kind of finding inside the world is still on neither side**

This is the one substantive thing left, and it is the same defect that was just fixed in B2 and B11 and not carried across to B1.

B1 expects a named finding of a named kind on each of four F-sides: a JUMP on B03's because line, a NO CONNECTION on B08's since line, CANNOT TELL on B09's plan line, and YOU CLAIM AND DENY THE SAME CAUSE on B05. Its against has two branches: "Silence on any markable ledger, charged to the driver", and two unmarkable cases — a claim in the actual ledger or absent, and a claim in a form the guide does not name.

But each of those four checks can print something that is neither the expected finding nor silence:

- **B03.** Check 2 has four verdicts. FOLLOWS, FOLLOWS ONLY IF THE CAUSE IS GRANTED and CIRCLE are all reachable on a ledger whose translator supplied a rule the passage does not state. None is a JUMP; none is silence.
- **B08.** Check 2b has exactly two verdicts, and the other one is `TO BE EXPECTED, using: ...`. B08 is the F-side with the rule removed, so nothing should lead from the open gate to the flock in the top field — but a translator who writes an implicit general line gets TO BE EXPECTED. Not a NO CONNECTION; not silence.
- **B09.** Check 3 has three outcomes. Besides CANNOT TELL it can print "The action does touch something the goal depends on, using: ..." or `KIND MISTAKE (the plan cannot work as written)`. Neither is CANNOT TELL; neither is silence.
- **B05.** Patch 14 prints a DENIED BECAUSE block with `Fine.` or `YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY`, and appends the CLAIM AND DENY sentence only when the claimed effect and cause match the denied ones. A ledger that writes the two with different terms gets the block without the sentence. Not the expected finding; not silence.

Read literally, none of these falls on a side, and the row's own table header promises that every outcome does. Read loosely — treating "silence" as "the expected finding did not appear" — the row charges the driver for what is in most of these cases the translator's added line, which is precisely the mis-assignment B2's new CIRCLE clause and B11's new verdict clause exist to prevent. Either way the row needs a sentence, and B11's is the model for it: name the other verdicts, and charge them by their cause under L81 rather than by the driver's silence.

### B10 the hedge — the same gap, and a mis-assignment with it

B10 expects "a JUMP inside the world on the because line of both" B12 and B15, and its against says: "No JUMP on a B12 ledger whose because claim is in a told world as a bare fact: charges the driver (as B1)", and the same for B15.

Neither B12 nor B15 states a rule — both read only "the cellar had flooded because the valve may have been / had been left open" — so a FOLLOWS or a FOLLOWS ONLY IF THE CAUSE IS GRANTED on either can only come from a line the translator added. Under L81 case 3, or under L81's "a claim the reported person never made" if the added line is a said one, that is the translator's; B10 charges the driver. And a CIRCLE on either is on no side at all.

B10 imports B1's rule by name ("as B1"), so fixing B1 fixes most of this; but B10 should also carry B11's carve-out, because the hedged pair is exactly where an added rule line is most tempting to a translator trying to make the cause work.

### The marking rule, and where it lives

Unchanged from the third version, where I checked it against P7 in detail. It still resolves all three things it was added to resolve, and still consistently with P7.

**The B12 / L81 section 5 order** is stated once, before the table, for every row with a sameness half and a report half, and is L81 section 5's own rule. **B4 over B13 on the controls** is stated with both branches spelled out, so the outcome that produced two charges in the second version now produces one. **B10's hedge override** is stated with its ground and, importantly, with its limit — it reaches only a hedge the language sends to the bin. Each is cross-referenced from the cells that need it, and a trap is set against marking B10 by the default rule.

On consistency with P7: the section opens by restating P7's rule faithfully. The override is not a departure from it, because L81 decides that a hedge made a fact counts as an error and the plan decides which layer wears it; L81 section 3, which P7 quotes, attributes the cause to "the language's silence on modality" itself. Item 3 has the same shape. The closing clause on thin or absent ledgers — removed from numerator and denominator of every row that counts them, each row saying what it was marked on — still does the work of keeping the shifting denominators honest.

### Contradictory marks between rows

None found, as in the third version. The rows that touch one ledger are cross-referenced rather than left to collide: B10 imports B1 for B12 and B15, B11 imports B1 for a wrongly-opened world on B13, B13 yields to B4 on controls, B12's halves are ordered, and B7 now hands the controls to B4 and B13's actual-ledger kinds to a recorded-not-counted line.

---

## Part 3. The run spec at `e52f9478c5bde4cd`

Read line by line. Steps 1 to 4 (lines 20 to 69) and step 7 are unchanged from the version I checked line by line last time and were re-read to confirm it. All six fixes are in, and all six are done properly.

### The blinding — all three defects fixed

**The collision (item 6) is fixed, and fixed at the root.** Line 91 builds a placeholder per case, `"\x00W%d\x00" % i`. Lines 92 to 95 replace each case name with its placeholder; line 100, after everything else, replaces each placeholder with its neutral name. Because the placeholders are NUL-delimited tokens that cannot occur in a report, a case already named `world_1` can no longer be caught by a later iteration's pattern and collapsed into another world's name. This is the right fix rather than a guard against the symptom.

Two details worth recording because they were easy to get wrong and were got right. Line 94 now uses a lambda, `lambda m: m.group(1) + h`, instead of a `\g<1>`-style replacement template, so nothing in the replacement is re-interpreted as an escape. And `\b` boundaries still behave around the placeholders, because NUL is a non-word character.

**The `case <name>` prefix (item 8) is covered.** Line 94's pattern is now `(\b(?:world|case)\s+)%s\b`, which catches both the guide's `[TOLD in world <name>]` and its `[SUPPOSED in case <name>]`.

**`name_still_present` (item 7) is computed in the right place.** Line 97 cuts the bin quotations, line 99 computes the leak list, line 100 puts the neutral names in. So the list is taken after the cut and while the placeholders are still standing, which means a hit is a genuine occurrence the blinding did not reach rather than an artefact of either. A name containing an underscore or a digit is replaced everywhere by line 95 and so can never appear in the list; a plain-word name can, and is recorded for the marker. That is the honest treatment and matches what "Not tested" already says.

### The empty answer — fixed twice over

**Item 9 is answered in both places.** The caller now retries an empty-content answer like any other failure and, if all six attempts come back empty, writes an error file and a receipt with `"failed": true` and exits non-zero. The runner adds a second guard: lines 109 to 111 in the reader and 140 to 142 in the prose reader check, on a zero exit, that the response file exists and is not blank, and set the code to 99 if it is not. Both `FAILED.txt` files record it, and B6 and B13 both count a FAILED.txt entry.

**This is not hypothetical, and there is live evidence.** The second pilot under `scratchpad/l82_pilot2/` has a `B99.mimo.attempt1.response.txt` of zero bytes written beside a receipt — a successful call with no content, made by the caller at its previous hash, which exited zero and wrote a success receipt. The tool has since moved to `B99.mimo.attempt2`, because `translate_via_api.py` could not find a JSON block and retried. That is exactly the failure mode both new guards close.

### The overlap precondition — stated, not enforced

**Item 10 is answered in the header.** Lines 17 and 18 read: "No other caller of either provider may run while this script runs: the lock is shared within one run only." P11 says the header says so, and it does, and B9 now makes it a condition with a consequence.

It is stated in three places and enforced in none. The script does not look for another caller, so the condition rests on the orchestrator remembering. It would cost one line at the top — a `pgrep` for `ask_model.py` that is not this run's, refusing to start if one is found — and it would turn B9's "a second caller found running alongside the run" from something somebody has to notice into something the run refuses to do. This matters today rather than in principle: the second pilot is still running as I write, working through B99 on both providers with its own lock directory, so at this moment the precondition does not hold.

### The header comment is stale

The runner's line 2 says it is "kept with the outputs", so its header is part of the record. Lines 10 to 13 still describe the third version's blinding: "every world name replaced by world_1, world_2, ... in order of first appearance (in the driver's quoted headings, after "world" in line texts, and everywhere for a name with an underscore or a digit; a plain-word name left elsewhere is listed in the key)". It does not mention `case`, and it does not mention the two-pass placeholder scheme; only line 90's inline comment does. P11 now describes the code more accurately than the file's own header does, which is the wrong way round for a file that travels with the outputs.

### What else was checked and is sound

The gate is unchanged and still right: `head -2 "$v" | grep -qx 'VALID'` reads only the first two lines, so the old driver's report appended below cannot flip it, and `-x` requires the whole line. The naming arithmetic still matches what `translate_via_api.py` writes, and an invalid ledger is still excluded consistently from the drivers, consequences, both sameness runs, the reader and the prose reader. The shuffle is still `random.Random(82)` over the sorted names with the order frozen into the key. The eight-lane executors, the six printed timings, the COUNTS file, `ASK_MODEL_LOCKDIR`, the absolute paths, the fresh-directory check, the empty-glob guard, the no-valid-ledger stop, the driver return-code messages and the manifest's exclusions are all as they were and all as P11 describes.

The rate limiting is unchanged and still correct with margin: a gap of `60/rpm × 1.1` gives 2.2 seconds for Atria and 0.66 for Mimo, permitting at most 28 and 91 starts in any sixty-second window against limits of 30 and 100, with every lane of every step queueing on one lock per provider through `ASK_MODEL_LOCKDIR`.

One small thing in the caller, not worth a numbered item: when a 200 parses but carries no `choices` at all, the code labels it `-2`, the code it uses for empty content, so the error file will describe a malformed response as an empty one. It is a label, not a behaviour.

---

## Verdict

**DO NOT FREEZE YET** — for one defect in two cells, plus two pieces of housekeeping.

All eleven premises are now found at their hashes, for the first time. All twelve items from the third version are answered, and most are answered better than asked: the placeholder scheme fixes the collision at the root rather than guarding the symptom; the empty answer is caught in the caller and again in the runner; B11 charges each of the four because verdicts by its cause under L81 rather than by its name; B7's denominator is now the thirteen texts that carry an argument rather than a round number. The marking rule still resolves all three collisions and is still consistent with P7. Eleven of thirteen rows are sound on all six questions.

What stops the freeze is that the verdict-enumeration fix applied to B2 and B11 was not carried across to B1, the row the whole arm is built on, or to B10, which imports B1's rule. On each of B1's four F-sides the driver can print a finding that is neither the expected kind nor silence, and B1's against provides only for silence and for two unmarkable cases. Read literally the outcome is on no side; read loosely it charges the driver for what is usually the translator's added line. It is one sentence in each of two cells.

What must change:

1. **Bracket a wrong kind of finding inside the world in B1.** Each of the four F-sides can produce one, and none is silence: on B03 a FOLLOWS, a FOLLOWS ONLY IF THE CAUSE IS GRANTED or a CIRCLE; on B08 a `TO BE EXPECTED, using: ...`, which is check 2b's only other verdict; on B09 "The action does touch something the goal depends on" or a `KIND MISTAKE`; on B05 a DENIED BECAUSE block without the CLAIM AND DENY sentence, which the driver appends only when the claimed effect and cause match the denied ones. Follow B11's pattern: name the verdicts and charge each by its cause under L81 — a rule the passage does not state from a said line, an added line supplying the answer from a filled-in or usual-case line, a route through the conclusion for a CIRCLE — rather than letting them fall under "silence, charged to the driver".

2. **Give B10 the same carve-out.** "No JUMP on a B12 ledger whose because claim is in a told world as a bare fact: charges the driver (as B1)" will, once B1 is fixed, inherit the right rule for a FOLLOWS; but B12 and B15 state no rule at all, so a FOLLOWS or a FOLLOWS ONLY IF THE CAUSE IS GRANTED on either can only come from a line the translator added, and a CIRCLE is on no side. Say so in the cell, as B11 does, so the hedged pair is not marked against the driver for a translator's rule.

3. **Bring the runner's header comment up to the code.** Lines 10 to 13 still describe the third version's blinding — "after 'world' in line texts", no mention of `case`, no mention of the two-pass placeholder scheme. The file says it is kept with the outputs, so its header travels with them, and P11 currently describes the code better than the file does.

4. **Make the no-overlap precondition self-enforcing.** It is stated in the runner's header, in P11 and in B9, and checked by nobody; B9's against requires that a second caller be "found". One `pgrep` at the top of the script, refusing to start when another `ask_model.py` is running, would close it. It is live rather than theoretical: the second pilot is still working through B99 on both providers, with its own lock directory, as this check is written.
