# Premise check - L82 Test plan, Arm B, third version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, third version.md`, SHA-256 `f9402a14ff9850c90530a0f89b2db8067d9f8341f4166323f764270f1da8105e`. The first sixteen digits are `f9402a14ff9850c9`, as the coordinator said. Confirmed. Read whole.

The two changed files were re-read at their new hashes and both are as named: `Language/tools/L82_run.sh` at `47774a3437d81efd` and `Language/tools/ask_model.py` at `0a7f66febbc3b908`. Everything else in P3 was re-hashed and is unchanged. The sixteen passages, `MAP.enc` and `MAP2.enc` were re-hashed and are unchanged. No map was opened.

Method as before: every fact checked by hand against the file it names. Hashes are sha256sum, first sixteen hex digits.

---

## Part 1. The premises, P1 to P11

They are now in order, P1 through P11, which was item 15 on the last list. Done.

### P1. The passages, the sealed maps, the sentence counts — FOUND

All sixteen hashes match the files and match MANIFEST.json: B01 `27046e03f0c42d30`, B02 `37329dd4d77218c9`, B03 `b202d2275f73e9be`, B04 `62f118ddc1b3e48d`, B05 `380c9632a55c4ae6`, B06 `d7d42c45615c801a`, B07 `07cf5365e915b17a`, B08 `0a2b900f8dbc6363`, B09 `4fdc992609a91208`, B10 `0ad68f74f5f62201`, B11 `feb219f622289852`, B12 `b2aea43bf1e890a3`, B13 `6f11a1f2f97a3bcb`, B14 `c4466e8bb79184a2`, B15 `4a17af24e235410f`, B16 `593fd9bac4c98749`. `MAP.enc` is `4dce17f60633fa79` and `MAP2.enc` is `5e9a35e2e80e7c00`, both as stated.

The premise now carries its own caveat — "the two sealed hashes are copied from the manifest and cannot be checked without opening the seal" — which is exactly right and answers the point I raised last time. The two sealed-plaintext hashes are faithfully copied from MANIFEST.json.

Sentence counts re-checked by splitting on sentence-final punctuation: B01 4, B02 5, B03 5, B04 4, B05 5, B06 5, B07 5, B08 4, B09 4, B10 5, B11 5, B12 4, B13 4, B14 4, B15 4, B16 4. Every one agrees. The added parenthesis "each passage is one line of text" is true of all sixteen, and it is worth having, because it is why no count turns on a judgement about paragraph breaks.

### P2. The connectives and the diffs — FOUND

Re-run case-insensitively over each file. "since" in B01, B04, B08, B16 and nowhere else. "because" in B03, B05, B06, B10, B11, B12, B13, B15 and nowhere else, twice each in B05 and B10 — the new parenthesis "(twice each in B05 and B10: the claim and the denial)" is correct, and correct in its reading: in both passages one occurrence is the head teacher's claim and one is her denial. "so that" in B04, B09, B14. "always" in B01, B06. "did not think" in B05, B10. " may " in B12 only. None of the six in B02 or B07.

All eight sentence-by-sentence diffs the premise now lists were run and all eight hold, each differing in exactly one sentence and byte-identical elsewhere: B16 from B08 in the third; B11 from B03 in the third; B14 from B09 in the fourth; B01 from B08 in the second; B06 from B03 in the second; B04 from B09 in the second; B10 from B05 in the fourth; B12 from B15 in the second. Promoting the last five out of the prose and into the premise was the right move, because B3 and B12 mark against those sentence numbers.

The two wording corrections I asked for are made. "The texts, by observable features" now says B12 and B15 "differ in one phrase of their second sentence" rather than one word, and it now names B05's and B10's second difference ("the rise in attendance" against "the rise"). Both are accurate.

### P3. The tools, the drivers, the materials, the briefs, the calibration — FOUND

Every one of the fourteen hashes matches the file on disk:

`tools/ask_model.py` `0a7f66febbc3b908`; `tools/translate_via_api.py` `0053f66020414e31`; `tools/sameness_2.py` `e66a9d314a0227b6`; `tools/consequences_2.py` `d04f6dfd08268ce7`; `tools/L82_run.sh` `47774a3437d81efd`; `run_check.py` `eff1dee15bebc977`; `run_check_2.py` `9a4b21cf771b1208`; `39` `dcfbed45d4e94861`; `L80` `ec16e220a433e24a`; the encoding guide `afe860e1509caf09`; the reader brief `ddeba43abbbc1dba`; the prose reader brief `888a45f49248fba3`; `PAIRS.txt` `6da2ec538b581a22`; and, newly cited, `authority/L81 Calibration ... second version.md` `c8ff6244676b3c0e`. The four example files named beside the encoding guide are all present.

The runner's hash, which was the first item on my last list, is now the hash of the file that exists, and the file that exists is the four-lane one the plan's prose describes. Giving L81 a path and a hash closes the other half of that item, because P7 now cites a file at a hash rather than a memory.

PAIRS.txt is quoted in full and in order in the premise, and the file holds exactly that: `B08 B01`, `B03 B06`, `B09 B04`, `B05 B10`, `B12 B15`, `B08 B16`, `B03 B11`, `B09 B14`. F-side first on the four matched pairs, original before rewording on the last three, as stated.

The behavioural clauses P3 now attaches to `ask_model.py` are all true of the file at that hash. Request timeout 2400 s (`urlopen(req, timeout=2400)`). At most six attempts with backoff `min(120, 5 * 2 ** attempts)`, which for attempts 1 to 5 gives exactly 10, 20, 40, 80, 120 seconds as the premise says. A 400, 401, 403, 404, 413 or 422 is not retried. One lock file per provider in `$ASK_MODEL_LOCKDIR` when set, else in the output directory. The gap is `60.0 / rpm * 1.1`, sixty over the rate plus a tenth. Every call leaves `<tag>.request.json` and then `.response.txt`, `.reasoning.txt` and `.receipt.json`, or `.error.txt` on failure.

### P4. The pilot — FOUND

Every claim checked against the files in the scratchpad, which are unchanged since my last reading except for the two lock files' timestamps.

Atria on T10-D: `T10D.atria.attempt1.receipt.json` records `"attempts": 1` and `"seconds": 263.3`; the gauge in the validation file reads six said lines; the validation file's first line is `rebuilt from /tmp/.../T10D.atria.attempt1.response.txt`, not `attempt 1`. The premise now says all of this, including the rebuild, which was the small correction I asked for. Mimo on T10-D: `"attempts": 1`, `"seconds": 355.0`, six lines, validation file `attempt 1` then `VALID`. The two strings quoted from the old driver's report on Atria's ledger are in the file verbatim: `NO FAULT FOUND in the lines that were checked.` and `INSIDE 'account_world' (a told world, looked at alone): no contradiction.`

The reasoning-token figures are right: Atria 1,908 reasoning of 3,593 completion tokens; Mimo 10,800 of 12,258.

The T11-B correction is made and is accurate. Both calls are named, Atria's sent 14:14 and Mimo's 14:21, and the directory holds for each exactly a `.prompt.txt` and an `.attempt1.request.json` and nothing else — no response, no reasoning, no receipt, no error file. The premise's statement that the orchestrator stopped both at 14:44 is corroborated by the lock files: `.rate_atria` was last written at 14:44 and `.rate_mimo` at 14:37, which is what a 900-second timeout followed by a retry produces from send times of 14:14 and 14:21. The premise's note that both were made by the caller at its earlier hash `31ec591f2e2a3d02` with a 900-second timeout is correct — that is the hash I confirmed on the second version.

Saying plainly that the pilot lives in the scratchpad and is not in the repository, and quoting the receipts into the premise, is the right way to carry evidence that a later reader cannot re-hash.

### P5. What the new driver does and prints — FOUND WITH A DIFFERENCE

Everything in this premise is right except its last clause, and the last clause is wrong in a way that matters to the blinding.

What is right. The check list is exact, including the exclusion: `battery` runs checks 1, 2, 2b, 3, 4, 5, the chain and patches 8, 9, 10 and 14 inside a told world, and patches 11 and 13, the what-ifs, are guarded by `if world is None:` at line 506. The printed strings are now quoted with their tails and all match the templates: the JUMP text `JUMP. Even granting the stated cause, nothing in the ledger produces ...`; the SINCE head with `. (A reason to expect, not a cause.)`, which was the shortening I noted; `NO CONNECTION. Nothing in the ledger leads from the reason to what is expected.`; `CANNOT TELL whether the plan can work. The ledger says nothing about ...`; the denial head and both continuations; and the claim-and-deny line. The `Claim line:` and `Plan line:` blocks exist under those names. The OUTCOMES accounting is exact: twelve names in the actual ledger, eleven inside a world where `what-ifs` is dropped by the comprehension, and the five forms `ran out of time`, `not asked, nothing to ask`, `not asked, no line of that kind`, `asked, nothing found`, `asked, N found` are precisely the five branches of `reading()`.

**The difference.** P5 ends: "World headings quote the world's name in single quotes (`INSIDE '<name>' (a told world, looked at alone): ...`), and the name appears nowhere else in the report unquoted."

The first half is right — the driver prints the world name in single quotes in three places, the two `INSIDE '<name>'` forms and the `%d findings inside '<name>' would not stand ...` line, and the old driver likewise. The second half is false. The report also prints the **text** of every line it names, in the head (`BECAUSE-claim on line <id> [...]: "<text>"`) and in `describe_lines`. The encoding guide's line 19 fixes the shape of that field: `"text": "[<standing>] <the line in the language's words>"`, and the guide's own first example, `example_T10D.json`, has every told line's text beginning `[TOLD in world account_world]`. So the world name appears in the report unquoted, once per named line, in the standing prefix the translator wrote.

This is not a small slip, because P11 blinds exactly that: its second substitution replaces the name "after the word `world` in line texts (the guide's `[TOLD in world <name>]` prefix)". So P5 and P11 contradict each other, and P5 is the one that is wrong. A marker who took P5 at its word would conclude that blinding the quoted headings was enough, and would not look at the line texts at all.

### P6. The old driver's silence, and its actual-ledger reach — FOUND

Both halves check out, and the line numbers are now accurate.

Line 69 is `WORLD_REMOVED[:] = all_case_lines`, and it stands before every check: check 1, check 2 (the comment `# ---- check 2: "because" claims` is at line 95, as the premise says), check 2b, the chain, check 3, checks 4 and 5 and patches 8, 9, 10 and 14. So every line of a told world is out of the program when those questions are asked. Lines 313 to 320 are the world's `WORLD_REMOVED` assignment, the single `ask("contradiction(F)")` and the `INSIDE '<name>' (a told world, looked at alone): no contradiction.` print — which is what the premise says they are. Line 327 is `WORLD_REMOVED[:] = all_case_lines` and restores the removal. Correct throughout.

Two points of precision, neither material. The told-world loop's header is at line 311, not 313; 313 to 320 is its body up to the no-contradiction print, and the contradiction block runs on to 326. The premise's description of what those lines do is accurate; only the word "loop" is placed two lines low.

The second half — "Its check 2 runs over the actual ledger's BECAUSE claims with only the case lines removed and prints `BECAUSE-claim on line <id>: "..."` and a JUMP from the same template as the new driver's" — is correct, and it is the premise B11 was missing last time. Line 99 is `head = 'BECAUSE-claim on line %s: "%s".'`, and the premise is careful to quote it without the `[mark, sentence N]` bracket that the new driver's `named_line` adds. That distinction is right and easy to get wrong.

### P7. L81 section 3, the marking rule, section 5 — FOUND

Every quotation was compared character by character against L81 second version at `c8ff6244676b3c0e`.

The four cases are quoted verbatim, and case 3 now carries **both halves**: "an added line whose content is the conclusion (patch 10, 'added lines alone give the conclusion'; 38 line 113's note); and there must exist an admitted change under which the answer changes, so a ledger whose findings survive every admitted change has no dependence to report." The silent drop is repaired.

The marking rule is quoted whole and verbatim, including the limb that was missing: "counts as an error only under one of the four, **or on a prose reader's verdict that the ledger commits the writer to what the prose does not (a hedge made a fact; a claim the reported person never made)**", and the sentence that explains why the role exists. B10, B11 and B13 now have a premise to stand on.

The variation list is accurate with its elisions. The hedge sentence is verbatim: "A translation that writes the hedged clause as a fact is wrong about the prose even though the hedge is marked in the bin ... This is a false finding produced by the language's silence on modality". Section 5 is quoted whole and verbatim, including the sentence B12 now turns on: "Or a text where the variation test passes on both ledgers and the reports still disagree in kind: then the report, not the translation, is the variable, and the driver is charged."

The premise now has a path and a hash, through P3. Item 2 on the last list is fully answered.

### P8. The sameness buckets and the partition — FOUND

`sameness_2.py` was re-read and re-run on `ledger_A.json` against `ledger_A2.json`. It printed exactly the six headings the premise now quotes, each with its count, in the order given: `BOTH SAY (12):`, `ONLY THE FIRST SAYS (0):`, `ONLY THE SECOND SAYS (0):`, `SAME CONTENT, DIFFERENT STANDING (0):`, `NEAR, JUDGE BY HAND (1, overlap >= 0.50):`, `OPPOSITE (0, a near pair with NOT on one side only):`, then `BIN ENTRIES: first 0, second 0 (compare by reading)`. The `BIN ENTRIES` line the old premise omitted is now named.

The partition is now stated correctly: five of the six partition the lines, and SAME CONTENT, DIFFERENT STANDING re-lists pairs already counted under BOTH SAY. The file says so in its header comment and in the docstring of `partition_or_stop`, which places lines from those five buckets only and exits with a message if they do not cover both ledgers. The premise's parenthesis about `partition_or_stop` stopping the tool is accurate.

### P9. What the translator tool validates — FOUND

Re-read against `translate_via_api.py` at `0053f66020414e31`. Every clause holds: the six required top-level fields; the four per-line fields with `mark` restricted to the three values, `sentence` required to be an integer, and `case` with `case_kind` required for a TOLD or SUPPOSED standing; the guard check on the clause body after `:-`; every sentence in a line or the bin; the old driver run on the built ledger in a temporary copy of the rig with the raw log searched for three spellings of a syntax error; and one retry with the failures appended.

The premise now records the bare-fact consequence I noted last time — "a clause written as a bare fact has no body and is always reported as unguarded" — which is true of the code and is a plausible cause of a first-attempt failure that B5 counts.

The blinding-relevant clauses are right: `paragraph` is set by `setdefault` and `whose` to the provider; neither driver reads `meta["whose"]`; the `.pl` header comment that names the provider is fed to s(CASP) and never reaches the report. And the validation file's shape is as stated — first line `attempt 1` or `attempt 2`, or `rebuilt from ...` on the rebuild path, second line `VALID` or the first problem — which is what the runner's gate now reads.

### P10. The briefs' answer formats — FOUND

This premise did not exist before; it was item 5 on my list. Both briefs were compared against it.

The reader brief does say "Answer in exactly these four numbered parts", and the four are quoted accurately, including part 2's "give the sentence number the report prints for it, or write 'the report does not say'" and part 3's question about the named world and about anything found outside it. The three rules are verbatim: "guess at nothing about the passage; do not judge whether the writer was right; do not invent a sentence number the report does not print". The answer does begin `READER:` and end `READING COMPLETE`.

The prose reader brief's part 1 does offer exactly the four answers quoted, with the parenthetical instructions attached to three of them, including the hedge list "may, might, perhaps, possibly, seemed, thought, and the like". Part 2, part 3 and part 4 are quoted accurately, and the answer does begin `PROSE READER:` and end `READING COMPLETE`.

Four expectations are marked against these strings, and they are now premised.

### P11. The runner — FOUND WITH A DIFFERENCE

The runner was read line by line at `47774a3437d81efd`, and the premise describes it accurately in every substantive respect. The outputs, the gate, COUNTS.txt's contents, the sameness file names, the key's three recorded fields, FAILED.txt and SKIPPED.txt, the shuffle at `random.Random(82)` over the sorted report names, the eight lanes through `ThreadPoolExecutor`, the stop when no ledger validates, and the six printed timings are all as stated and all present.

Two differences, both small, and one runner defect that makes a third clause not quite true.

First, "`prose_reader/` likewise". The prose reader directory does get prompts, the caller's files, FAILED.txt and SKIPPED.txt, but it has no key file — and it needs none, because nothing there is blinded. "Likewise" invites a marker to look for a key that will not be there.

Second, the gate. P11 says ledgers are copied "for ledgers whose validation file's second line is `VALID`". The code is `head -2 "$v" | grep -qx 'VALID'`, which matches a whole line equal to `VALID` in either of the first two lines. Because the first line is always `attempt N` or `rebuilt from ...`, the effect is the second line, so the premise is right about what happens; it is not quite right about what the code says.

Third, and this is a defect in the runner rather than a misdescription: P11 says "every world name replaced by `world_k`". That is true except in one collision, set out in Part 3, where the substitutions can rewrite their own output and give two different worlds the same neutral name.

---

## Part 2. The expectations, B1 to B13

Each read against the six questions. The table's own header now promises what I was checking for — "each 'against' brackets both sides; every outcome falls on one side or is named unmarkable" — and for the most part it delivers.

**On the map, again — sound.** Nothing in B1 to B13 needs MAP.json or MAP2.json. Every named instance is reachable from features I confirmed in the texts: the four F-sides and four S-sides by shared openings and the added rule, route or differently-denied cause; the two controls by the absence of all six connectives; the hedged pair by "may have been" against "had been" in the second sentence; B13 by being the only passage with no reporting verb; the three rewordings by their single-sentence diffs. The seal still checks the writer's intent, not the marker's blindness.

### B1 the F-sides — sound

Both sides are bracketed and, new this version, the third outcome I said was missing is now named: "a ledger whose claim sits in the world in a form the guide does not name (recorded as 'out of reach', charged to the translation if the guide names a form for that claim and to the guide if it does not)". The charges column now reads "the rig (driver); the translation or the guide for the listed ledgers", which matches. The qualifying phrase in the expectation — "in a form the guide names (a because line, a since line, a plan line, a denied because)" — corresponds to the guide's `claim_because`, `claim_since`, `claim_plan` and `denied_because`, which are also four of the six keys in the driver's `CHECK_PREDICATE`. Every outcome now falls somewhere. No premise it rests on is in doubt.

### B2 the S-sides — one ambiguity of wording

The gap I named is closed: "a B10 ledger with no denied-because line for the fourth sentence" is now listed as unmarkable, and the row adds "if neither translator's ledger is markable for a text, the row is unmarkable for that text and says so". The B10 against is also sharpened correctly — a `CLAIM AND DENY` flag cannot fire when the denied cause differs from the claimed one, because the driver requires `claimed_effect == effect and claimed_cause == cause`, and a `YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY` would need the ledger's own lines to make the entrance hall produce the rise, which B10's prose does not say. Charging the driver for either is right.

**What remains is an ambiguity, not a hole.** The row says "B06 the because FOLLOWS (no JUMP)" and "B01 the since connects (no NO CONNECTION)". The new driver's because check has four verdicts, not two: `FOLLOWS`, `CIRCLE`, `FOLLOWS ONLY IF THE CAUSE IS GRANTED` and `JUMP`. Read as "the verdict is FOLLOWS", a `CIRCLE` or a `FOLLOWS ONLY IF THE CAUSE IS GRANTED` on B06 is neither met nor against. Read as the parenthesis suggests, "not a JUMP", both count as met, and the against cell — which names only a JUMP as charging the driver — supports that reading. Two markers could reasonably differ. The plan clause is written the other way round, "a verdict other than CANNOT TELL", and is unambiguous; the because and since clauses should be written the same way, or should list which verdicts count as met.

### B3 variation within pairs — sound

Unchanged in substance and still exhaustive. The unmarkable clause for a B5-listed ledger is added. The sentence numbers it marks against are now carried by P2 and I confirmed all of them. Charged to the translator, which is right for a line that moves where the prose did not.

### B4 controls — one outcome still unbracketed

Two of the three things I raised are fixed. The no-world case is provided for: the OUTCOMES lines are read "in every world the ledger has, and in the actual ledger when the ledger has no world; a told world is not required on a control", and the observable-features section now says the same. The OUTCOMES half now has an against: "An OUTCOMES line reading `asked, nothing found`: the ledger holds a line of that kind where the text carries none, charged to the translator and listed; `asked, N found` is a finding, above." And "B4 governs over B13 on the controls" settles the clash.

**What remains.** The row treats the OUTCOMES line as having three possible readings — `not asked, ...` (met), `asked, nothing found` (against), `asked, N found` (a finding). There is a fourth. `reading()` tests `out_of_time` first and returns `ran out of time`, and `out_of_time[current[0]]` is set whenever a query exceeds `TIME_LIMIT_SECONDS`, which is 20. A `because claims: ran out of time` on a control falls on neither side. It is not a remote possibility: the pilot's slowest question was 0.47 seconds, but these are unseen ledgers from two models, and a twenty-second ceiling is the kind of thing that bites once in sixty-four reports. The same fourth reading is available to any row that reads an OUTCOMES line.

### B5 validity and size — sound

The denominator is fixed and is now right: at least 14 of 16 per provider, against at 13 or fewer, which is exhaustive. The TOLD requirement is now scoped to the thirteen texts where a told world is expected — B01, B03 to B06, B08 to B12, B14 to B16 — and recorded but not required on B02, B07 and B13, which is the correct exclusion: the two controls carry no argument and B13's belongs in the actual ledger. The row now names where each number is read: the validation files' first two lines, which P9 describes, and `ledgers/COUNTS.txt`, which P11 describes and which the runner writes. Both exist. "A text that fails both attempts is listed and the run continues without it" matches what the runner does.

### B6 read-back — sound

The band is closed: at most 2 misses met, 3 or more against. The layer mis-assignment is fixed and fixed explicitly — an invented sentence number is now "recorded against the reader, which invented it, and not against the report", with the reason given. The charges column carries both layers. A reader call in FAILED.txt or SKIPPED.txt now counts as a miss and is listed, which ties the row to files the runner actually writes.

One consequence of the runner, noted under Part 3 and item 9 below: a call that returns successfully with empty content lands in neither file, so it is not a miss under this row and the marker would have to notice the empty response by hand.

### B7 the two translators agree in kind — one thing still unsaid

The band is closed (at most 4 misses; 5 or more against) and the denominator is now 16, not 10. Both were on the list.

**What remains.** The row compares "the same set of finding kinds **inside the world**", "per text where both ledgers are markable", over sixteen texts. But three of the sixteen are expected to have no world at all: B13's argument belongs in the actual ledger by the plan's own reading of 39, and the controls B02 and B07 carry no argument, with the plan saying in two places that a told world is not required on them. For those three, "the set of finding kinds inside the world" has no referent. The row does not say whether the comparison moves to the actual ledger, or whether those texts drop out and the denominator becomes 13. As written a marker must invent the rule.

### B8 the old driver's silence — sound

Unchanged, and now resting on a P6 that says exactly what the code does. Expected none, against any: exhaustive. The charge to the premise rather than to a layer is still the right one, because a finding there falsifies P6 and nothing else.

### B9 time — sound, with a tension the plan names

The four budgets are all readable from numbers the runner actually prints: translations, reader, prose reader, and "rig (drivers and consequences)" — the last was the gap I found, and the runner now prints both the parts and the sum. Against at "over any of the four": exhaustive.

The arithmetic now works, which it did not before. Sixty-four reader calls in eight lanes is eight rounds; at the pilot's Atria latency of 263 seconds on a prompt six times longer than a reader prompt, that is about thirty-five minutes against a ninety-minute budget. Thirty-two prose-reader calls in eight lanes is four rounds; at Mimo's 355 seconds that is about twenty-four minutes against sixty. Sixteen texts in four lanes is four per lane; at 355 seconds that is twenty-four minutes against three hours. All three have real margin.

The tension the plan names honestly: raising the timeout from 900 to 2400 seconds rescues a slow call that would have been abandoned, but it raises the worst case for one text to six attempts at 2400 seconds plus 270 seconds of backoff, about four hours, which alone exceeds B9's three and blocks the three texts behind it in that lane. The row says so — "a text that exhausts six attempts at 2400 s each could alone take longer; it is listed under B5, and the budget is still charged". Given that the pilot saw T11-B hang on both providers, this is not hypothetical; the plan has chosen to let B9 fire in that case rather than to complicate the budget, and having stated it, that is a decision and not a defect.

### B10 the hedge — sound

Both gaps are closed. The B15 side is now bracketed on both counts: no JUMP on a B15 ledger whose claim is in a told world charges the driver, as B1; a B15 ledger with no because line charges the translator and makes the row unmarkable there. The two prose-reader answers outside the expected pair — "not made" and "cannot tell" — are now recorded against the report and marked unmarkable here, which uses all four of P10's options. The override is stated in the marking rule as well as in the cell, and the row's phrasing of the prose reader's answers now matches the brief's exact strings, "hedged in the passage" and "claimed as a fact in the passage".

It still does the thing that makes it the most interesting row in the table: it names what a clean success charges. If all four JUMPs and all four answers come as expected, the language is charged and the contract is short a change. That is L81 sections 3 and 5 used as they were written, and P7 now quotes both.

### B11 the narrator's own — one outcome still unbracketed

Three of the four things I raised are fixed. Both drivers silent is bracketed ("or both silent ... driver, both drivers if both are silent"). No because line for B13's claim is bracketed. "Cannot tell" from the prose reader is bracketed. And the claim about the old driver reaching actual-ledger because claims, which had no premise last time, is now P6's second half and is true of the code.

The row also adds something good that was not there before: a FOLLOWS on B13 produced by a filled-in or usual-case line that supplies the missing rule is charged to the translator under L81 case 3, an added line supplying the answer. That is the right reading of P7's case 3.

**What remains.** B13's prose gives no rule, so the driver's because check can return any of four verdicts on it. The row brackets JUMP (met) and FOLLOWS-from-an-added-line (translator). It does not bracket `CIRCLE`, or `FOLLOWS ONLY IF THE CAUSE IS GRANTED`, or a FOLLOWS produced by a **said** line rather than a filled-in or usual-case one — a translator could write the rule as a said line, which is a different charge from an added line under L81 case 3. Any of those three leaves the row unmarked.

### B12 the rewordings — sound

The charge is fixed and fixed in the right direction. "Report kinds that differ within a pair whose sameness half is clean: the driver (L81 section 5)" is now what L81 section 5 says, and P7 quotes that sentence. The order is stated both in the cell and in the marking rule, and the cell also says what happens to the report half when the sameness half is unclean: recorded, not charged. The charges column reads "the translator, or the driver, as the order states". The unmarkable clause for a B5-listed ledger is added. The reworded sentence numbers it marks against are carried by P2 and I confirmed all three.

### B13 the prose reader on every report — sound

All four of P10's part-1 answers are now accounted for. "Not made" on a non-control charges the translation; on a control, B4 governs. "Cannot tell" is recorded against the report and is explicitly neither for nor against the first half. And "hedged in the passage" outside B12 gets a rule that did not exist before and is well judged: the marker reads the quoted hedge against the passage, a real hedge made a fact charges the translator under L81's limb, and words that are no hedge charge the prose reader. A failed or skipped prose-reader call makes that report unmarkable and is listed.

### The marking rule, and where it lives

This section is new, and it does what it was added to do.

**Does it resolve the B12 / L81 section 5 order?** Yes. Item 2 states the order once, for every row that has both halves: "the sameness half is read first and decides the charge of the report half: clean sameness with differing report kinds charges the driver (L81 section 5); unclean sameness charges the translator and the report half is recorded, not charged." B12's cell repeats it and B11's cell is cross-referenced. The rule is stated where a marker will find it before reaching the table, which was the point.

**Does it resolve B4 over B13?** Yes, and it resolves it in the direction that makes the two rows coherent. Item 3: "On a control, B4 governs: the ledger, not the prose reader's answer, decides the layer." It then spells out both branches — where the ledger holds the unstated claim line the prose reader's answer confirms B4's translator charge, and where it does not the finding is the driver's and the prose reader's answer is "recorded as agreeing with the ledger's reading, not as a second charge". B4's and B13's cells both point at it. The outcome that produced two charges last time now produces one.

**Does it resolve B10's override?** Yes, and it bounds it, which the cell alone did not. Item 1 states the charge (the language, not the translation), gives the ground (39 and L80 give no way to keep a modal hedge; L64 sends "may" to the bin), and limits the reach: "The override reaches only a hedge the language sends to the bin; a translator that keeps the hedge out of the world's claim by some other means is recorded, charged to nothing." The Traps section adds a fourth trap against marking B10 by the default rule.

**Is it consistent with P7?** Yes, on all three. The section opens by restating P7's rule faithfully — an error only under one of the four cases or on the prose reader's verdict, everything else variation, recorded and not scored. Item 2 is L81 section 5 verbatim in effect, and P7 quotes that section. Item 1 looks at first like a departure, because L81's limb makes a hedge made a fact an error and the plan declines to charge the translation for it; but L81 section 3, which P7 also quotes, says in its own words that this is "a false finding produced by the language's silence on modality". L81 decides that the difference counts as an error; the plan decides which layer wears it. Those are different questions and the plan answers the second without contradicting the first. Item 3 is the same shape: P7's limb makes the difference an error, and item 3 assigns the layer. No inconsistency.

The closing paragraph on thin or absent ledgers — removed from both numerator and denominator of every row that counts them, with each row saying what it was marked on — is the piece that keeps all the shifting denominators honest, and it belongs where it now is.

### Contradictory marks between rows

I could not find a pair that gives contradictory charges on one outcome. The two I found last time are both settled by the marking rule. The places where two rows touch the same ledger are now cross-referenced rather than left to collide: B10 imports B1's rule for B12 and B15 ("charges the driver (as B1)"); B11 imports B1's reading for a B13 ledger that wrongly opens a world ("read inside the world as B1 reads it"); B13 yields to B4 on controls; B12's two halves are ordered. B1 covers the four F-sides only, and a driver failure on one of the three rewordings is caught by B12 instead and charged to the driver when the sameness half is clean, which is consistent.

---

## Part 3. The run spec at `47774a3437d81efd`

Read line by line against P11, the expectations, and the faults I reported last time.

### What was fixed

All four script faults from the last list are fixed, and fixed properly rather than papered over.

Paths are made absolute at the top: the corpus at line 22, the pairs file at line 24, and the output directory at line 26, each through `cd ... && pwd`. The `cd "$OUT/scratch"` at line 44 can no longer strand the redirections, and it carries `|| exit 1`. The usage comment says paths may be relative because they are made absolute, which is now true.

`lines[0]` is guarded in both steps. Line 82 and line 123 test `if not lines or not body.strip()` and record the report as skipped instead of raising. An empty report no longer aborts the whole step.

Driver and tool return codes are reported: lines 46, 47 and 51 each carry `|| echo "... failed on ..."`, and the reader and prose reader capture the return code in `call` and write FAILED.txt.

Step 3 is timed, and so is the sum B9 asks for: line 52 prints both "consequences took N s" and "rig (drivers and consequences) took N s".

Beyond the list, three more things were tightened. The output directory must be new or empty (line 25), with the reason given — the drivers append to their raw logs, which was the append-mode point I raised. The empty-glob case is guarded at line 39. And the run stops if nothing validated (line 42), instead of carrying on to produce nothing.

**The VALID gate is genuinely better.** It was a bare `grep -q '^VALID'` over a file with the old driver's whole report appended below the verdict. It is now `head -2 "$v" | grep -qx 'VALID'`: the report below is out of scope, and `-x` requires the whole line, so no line that merely begins with those letters can flip it. The fragile anchor is gone.

### Does it produce every output the expectations and P11 name?

Yes, with one qualification.

Step 1 writes the translations and four lane logs per provider. Step 2 writes `ledger_<id>_<provider>.old.txt` and `.new.txt` with a `.raw.txt` and `.err.txt` beside each — the 64 reports B6 counts, when all 32 ledgers validate. Step 3 writes the consequences. Step 4 writes `pair_<a>_<b>_<provider>.txt` for each of the eight PAIRS lines and each provider, which covers B3's four matched pairs, B12's three rewordings and B10's hedged pair, and `across_<id>.txt` per text for the cross-translator diagnostic L81 asks for. Step 4 also writes `ledgers/COUNTS.txt`, whose row carries the line count, said, filled in, usual case, TOLD, SUPPOSED, the world names, bin entries and sentences — every number B5 reads, and the world names a marker needs beside the reader's key. Step 5 writes the reader's prompts, the caller's files, `KEY_report_names.json`, FAILED.txt and SKIPPED.txt. Step 6 writes the prose reader's, with its own FAILED.txt and SKIPPED.txt. Step 7 writes the manifest, skipping the scratch rig and the rate-lock files.

The qualification: B5 wants "at least 3 said lines" and "at least one TOLD line", and COUNTS.txt now gives both, which closes last time's gap. But the *validation attempt count* B5 also reads is in the per-text validation files in `translations/`, not in COUNTS.txt; the row points at the right place (P9, first two lines) so this is a matter of the marker looking in two files, not a missing output.

### Does the blinding close the channels I found, and what remains open?

It closes the two I named, and it opens one small new risk of its own.

**The world name.** Step 5 now replaces every case name with `world_1`, `world_2`, ... in order of first appearance, in three passes: the driver's single-quoted headings (line 89), which catches all three quoted sites in the new driver and both in the old; the standing prefix in line texts (line 90), matching `world <name>`; and, for a name containing an underscore or a digit, every word-boundary occurrence (line 91). The second pass is the one that matters most and the plan was right to add it: the guide fixes the `text` field as `"[<standing>] <the line ...>"` and its own example has every told line reading `[TOLD in world account_world] ...`, and the driver prints that text in every finding head and in `describe_lines`. A plain-word name that survives elsewhere is recorded in the key as `name_still_present` rather than silently left, which is the honest way to handle a case named `log` in a passage about a log.

**The bin quotations.** Line 96 cuts `(not checked): <entries>. Slowest question:` down to `(not checked). Slowest question:` and records whether it cut. The pattern is safe: the gauge occurs once, `.*?` is lazy, and when the bin is empty the text has no colon there and nothing is cut, which the key records as false. The pilot's Atria bin entry, which ran to three sentences and contained `account_world`, would be removed entirely.

**What remains open, and is acknowledged.** The reader still sees the line texts in the translator's words, which is unavoidable because B6 asks it to name the finding and its sentence. The "Not tested" section now says this, says the reader can tell an old report from a new one by shape, and says a bin entry or line text that names the passage would reach the reader. That is the right disclosure and it matches what the code does.

**What remains open and is not acknowledged.** Three things.

First, a **substitution collision**. Lines 88 to 91 loop over the names in order and rewrite `text` in place, so a later pattern can match an earlier pass's output. If a translator names one case `world_1` — not far-fetched, since the guide's own placeholder reads `TOLD in world <name>` — and another case sorts before it, the first case becomes `world_1` and then the second iteration's `re.sub(r"\bworld_1\b", "world_2", text)` rewrites both. Two different worlds reach the reader under one name, and the key records a mapping that does not match the prompt. The fix is one line: substitute in a single pass, or refuse a neutral name that collides with a case name.

Second, **`name_still_present` is computed too early**. Line 93 searches the text before line 96 cuts the bin quotations. A world name that occurred only inside the bin is reported as still present when it is not. This errs on the safe side — the key over-reports rather than under-reports — but it makes the key's own record inaccurate, and B6's marker reads that key.

Third, **line 90 handles `world <name>` but not `case <name>`**. `cases` at line 86 is built from every `case` field, told or supposed, and a supposed line's standing prefix is `[SUPPOSED in case <name>]`. A supposed case name without an underscore or digit is therefore missed by both line 90 and line 91 and survives in the line texts, recorded only as `name_still_present`. Arm B expects no suppositions, so this is a corner; it costs one alternation in the regex.

### Do the lanes and the lock respect 30 and 100 requests a minute?

Yes, with more margin than before, and the cross-step hole is closed.

The gap is now `60.0 / rpm * 1.1`: 2.2 seconds for Atria and 0.66 for Mimo. The sleep still happens while the exclusive `flock` is held, so waiting callers queue rather than wake together, and the timestamp is written just before the request is issued, so the spacing is between request starts. In any sixty-second window that permits at most 28 Atria starts and 91 Mimo starts, against limits of 30 and 100. The tenth over the minimum is exactly the margin I asked for and the code comment gives the reason.

The lock is now shared across the whole run: the runner exports `ASK_MODEL_LOCKDIR="$OUT"` at line 28, and `wait_for_slot` prefers that over the per-step output directory. So step 1's eight translation lanes, step 5's eight reader lanes and step 6's eight prose-reader lanes all queue on one `.rate_atria` and one `.rate_mimo`. Four lanes per provider in step 1 and eight in steps 5 and 6 all respect both limits; the lanes are never the binding constraint, latency is.

**One hazard remains, and it is live right now.** The lock is shared within a run, not across the machine. While I was checking, a second pilot was running: `translate_via_api.py` on a text `B99` under `scratchpad/l82_pilot2/`, calling both Atria and Mimo, with no `ASK_MODEL_LOCKDIR` set and therefore its own lock files in its own translations directory. If anything like that is in flight when the real run starts — a hand rerun of a failed text, a second pilot — the two callers will not see each other and the combined rate can exceed 30 a minute for Atria. The plan should say the run must not overlap another caller, or the lock should default to a fixed path rather than to the output directory.

### What breaks

Beyond the three blinding defects and the overlap hazard above, four things.

**An empty but successful response is invisible.** FAILED.txt catches a non-zero exit and SKIPPED.txt catches an empty *report*. A call that returns HTTP 200 with empty content writes an empty `.response.txt`, exits 0, and appears in neither file. B6 says "a reader call in FAILED.txt or SKIPPED.txt is a miss" and B13 says the same for the prose reader, so such a call is neither a miss nor an answer, and the marker would have to notice the empty file unaided. `mimo`'s pilot receipt shows `finish_reason: stop` with 12,258 completion tokens, so this is not the common case; but at `--max-tokens 4000` with a model that spent 10,800 reasoning tokens on the pilot, a truncated or empty content field is a real possibility, and it is worth one line in `call` to treat empty content as a failure.

**`ask_model.py` misreports the attempt count on a rejected request.** The no-retry rule is implemented by setting `attempts = 6` and falling into the existing `if attempts >= 6:` branch, so a 400 or a 401 prints "failed after 6 attempts: status 400" when one attempt was made, and writes `.error.txt` but no receipt, so the true count is recorded nowhere. P3 says "at most six attempts with backoff", which is true of the behaviour but not of the log. A separate branch, or a `tried = attempts` captured before the override, would keep the record honest.

**`wait_for_slot` does not create its lock directory.** It joins `ASK_MODEL_LOCKDIR` and opens the file; if the variable points at a directory that does not exist, it raises rather than falling back. The runner always creates `$OUT` first, so this cannot bite inside the run; it can bite anyone who sets the variable by hand.

**No `set -e`, still.** It matters much less now, because the things that used to fail silently are guarded explicitly — the argument count, the repository root, the corpus and pairs paths, the empty output directory, the empty glob, the no-valid-ledger stop, and the `|| echo` on each driver and on `consequences_2`. What is left is that a failure inside step 4 or step 7 will not stop the run. That is a tolerable choice for a script whose whole purpose is to produce as much of the output as it can and leave the rest to the manifest.

**Two things I checked and found sound.** The `head -2 | grep -qx 'VALID'` gate matches the naming `translate_via_api.py` actually uses (`ledger_B03_atria` is rewritten by the sed to `B03.atria`, and the tool writes `B03.atria.validation.txt`), and it correctly excludes an invalid ledger from every later step — the drivers, consequences, both sameness runs, the reader and the prose reader all draw from `ledgers/` or from the reports of ledgers that passed it. And the shuffle is reproducible: `sorted` then `random.Random(82)`, with the resulting order frozen into the key dictionary, whose insertion order Python preserves; a smaller set of reports shifts the whole assignment, but shifts it the same way every time.

---

## Verdict

**DO NOT FREEZE YET** — narrowly, and with a short list.

This version answers all fifteen items on the last one. The runner's hash is the runner that exists; P7 quotes L81 whole, with the prose-reader limb and both halves of case 3; the sameness partition is stated correctly; the pilot's two stopped calls are recorded; P10 gives the briefs' answer formats a premise and P6 gives B11's old-driver claim one; the stale denominators are gone; the bands in B6 and B7 are closed; five unprovided-for outcomes are provided for; the two contradictory pairs are settled by a marking rule that now lives outside the table and is consistent with P7; and the runner meets its own time budgets, blinds the two channels I found, and shares one lock per provider across the run.

What stops the freeze is one false premise clause, three expectation outcomes that can still be neither met nor counted against, one ambiguity of wording that two markers could resolve differently, and three defects in the blinding the plan does not know about. All are small and most are one line.

What must change:

1. **Correct P5's last clause.** "The name appears nowhere else in the report unquoted" is false: the report prints each named line's `text`, and the encoding guide fixes that field as `"[<standing>] <the line ...>"`, so a told line reads `[TOLD in world <name>] ...` — the name, unquoted, once per named line. `example_T10D.json` shows it on all six lines. As written P5 contradicts P11, which blinds exactly that prefix, and a marker trusting P5 would think the quoted headings were the whole exposure.

2. **Bracket `ran out of time` in B4.** `reading()` tests `out_of_time` before everything else and returns that string whenever a query exceeds `TIME_LIMIT_SECONDS`, which is 20. B4 reads the `because claims`, `since claims` and `plans` lines and provides for three readings; this is a fourth, and it falls on neither side. Say what it means for the row — most naturally, unmarkable and listed.

3. **Say what B7 compares on the three texts with no world.** The row counts "finding kinds inside the world" over sixteen texts, but B13's argument is expected in the actual ledger and the controls are expected to carry no argument, with the plan saying twice that a told world is not required on them. Either move the comparison to the actual ledger for those three, or exclude them and make the denominator 13.

4. **Resolve B2's wording on the because and since clauses.** "The because FOLLOWS (no JUMP)" reads two ways, and the driver has four because verdicts — `FOLLOWS`, `CIRCLE`, `FOLLOWS ONLY IF THE CAUSE IS GRANTED`, `JUMP`. Say which count as met, as the plan clause already does with "a verdict other than CANNOT TELL".

5. **Bracket B13's other because verdicts in B11.** The row provides for a JUMP and for a FOLLOWS from a filled-in or usual-case line. A `CIRCLE`, a `FOLLOWS ONLY IF THE CAUSE IS GRANTED`, or a FOLLOWS from a **said** line — a different charge under L81 case 3 from an added line — are all reachable on B13 and none is named.

6. **Fix the substitution collision in the runner's blinding.** Lines 88 to 91 rewrite `text` in place in a loop, so a later pattern can match an earlier pass's output; a case named `world_1` collapses two worlds into one neutral name and makes the key disagree with the prompt. Substitute in one pass, or refuse a neutral name that collides with a case name.

7. **Compute `name_still_present` after the GAUGE cut.** Line 93 runs before line 96, so a world name occurring only in the bin quotations is recorded in the key as still present when it has been removed. It errs safe, but B6's marker reads that key.

8. **Extend the standing-prefix substitution to `case <name>`.** Line 90 matches `world <name>` only; a supposed line's prefix is `[SUPPOSED in case <name>]`, and a plain-word supposed case name survives in the line texts. One alternation. Arm B expects no suppositions, so this is insurance.

9. **Treat an empty successful response as a failure.** A call returning HTTP 200 with empty content exits 0 and lands in neither FAILED.txt nor SKIPPED.txt, so it is neither a miss nor an answer under B6 and B13. Check the content length in `call`, or have B6 and B13 name the third case.

10. **Say that the run must not overlap another caller.** `ASK_MODEL_LOCKDIR` unifies the lock within one run only. A second pilot was in flight during this check — `translate_via_api.py` on a text `B99` under `scratchpad/l82_pilot2/`, against both providers, with its own lock directory. Two callers that do not share a lock can exceed 30 a minute for Atria between them. Either say so in "Who does what", or default the lock to a fixed path.

11. **Correct two small descriptions in P11.** "`prose_reader/` likewise" invites a marker to look for a key file that is not there and is not needed. And the gate is `head -2 ... | grep -qx 'VALID'`, which reads the first two lines; it behaves as the premise says because the first line is always `attempt N` or `rebuilt from ...`, but the premise describes the effect, not the code.

12. **Keep the attempt count honest in `ask_model.py`.** A 400, 401, 403, 404, 413 or 422 is not retried by setting `attempts = 6`, so the run log says "failed after 6 attempts" when one was made, and no receipt is written on failure, so the true count survives nowhere. P3's "at most six attempts" is true of the behaviour and false of the record.
