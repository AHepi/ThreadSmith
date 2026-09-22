# Premise check - L82 Test plan, Arm B, second version

The plan checked is `Language/tests/L82 Test plan - Arm B, sixteen reported arguments, two API translators, old rig and new, second version.md`, SHA-256 `b82f7447452b72a0848fae7f2b48a4cd9c04231afdac6c79c0f966fea9c26a57`. The first sixteen digits are `b82f7447452b72a0`, as the instruction said they would be. Confirmed.

Read whole. Background read: `Language/authority/L81 Calibration - what Arm B measures, in file 11's terms, and when a vague translation is acceptable, second version.md`; every file in `Language/tests/L82 Arm B corpus brief/`; and in `Language/results/L82 Corpus - sixteen reported arguments/` the sixteen passage files, TEXTS.md, TEXTS2.md and MANIFEST.json. The two `.enc` files were hashed but not opened.

Everything below is by hand against the files. Hashes are sha256sum, first sixteen hex digits.

---

## Part 1. The premises

### P1. The sixteen passages, their hashes, the sealed maps, the sentence counts — FOUND

Every one of the sixteen hashes in P1 is the hash of the file on disk, and is also what MANIFEST.json records. Taken in order: B01 `27046e03f0c42d30`, B02 `37329dd4d77218c9`, B03 `b202d2275f73e9be`, B04 `62f118ddc1b3e48d`, B05 `380c9632a55c4ae6`, B06 `d7d42c45615c801a`, B07 `07cf5365e915b17a`, B08 `0a2b900f8dbc6363`, B09 `4fdc992609a91208`, B10 `0ad68f74f5f62201`, B11 `feb219f622289852`, B12 `b2aea43bf1e890a3`, B13 `6f11a1f2f97a3bcb`, B14 `c4466e8bb79184a2`, B15 `4a17af24e235410f`, B16 `593fd9bac4c98749`. All sixteen match.

`MAP.enc` on disk is `4dce17f60633fa79`, as P1 says; `MAP2.enc` is `5e9a35e2e80e7c00`, as P1 says. The two sealed-plaintext hashes P1 gives, `d25711c96eee17f3` for MAP.json and `1aaaf06963ea6de8` for MAP2.json, are copied correctly out of MANIFEST.json. They cannot be checked against anything, because checking them would mean opening the seal; what is confirmed is that the plan quotes the manifest faithfully. The manifest's own note repeats that the orchestrator has not read MAP.json.

Sentence counts, splitting on sentence-final punctuation: B01 4, B02 5, B03 5, B04 4, B05 5, B06 5, B07 5, B08 4, B09 4, B10 5, B11 5, B12 4, B13 4, B14 4, B15 4, B16 4. Every one agrees with P1. Each passage is a single line of text, so no count depends on a judgement about paragraph breaks, and no passage contains an abbreviation that could split wrongly.

### P2. The connectives and the three diffs — FOUND

Case-insensitive search of each file gives exactly the sets P2 states, with nothing left over and nothing missing.

"since" appears in B01, B04, B08 and B16 and nowhere else. "because" appears in B03, B05, B06, B10, B11, B12, B13 and B15 and nowhere else; B05 and B10 carry it twice each, once in the claim and once in the denial, which P2's membership list does not contradict. "so that" appears in B04, B09 and B14 and nowhere else. "always" appears in B01 and B06 and nowhere else. "did not think" appears in B05 and B10 and nowhere else. " may " with spaces either side appears in B12 and nowhere else. None of the six appears in B02 or in B07.

The three diffs P2 asks for, taken sentence by sentence:

B16 against B08 — exactly one sentence differs, the **third**. B16 has "The foreman added, from what he saw himself, that no grass remained in the lower field."; B08 has "...that the lower field was empty of grass." The other three sentences are byte-identical.

B11 against B03 — exactly one sentence differs, the **third**. B11 has "The log went on to list who had crewed the boat and how much the catch had weighed."; B03 has "The log went on to record the names of the crew and the weight of the catch." The other four are byte-identical.

B14 against B09 — exactly one sentence differs, the **fourth**. B14 has "The last line told the day staff to chart his medication at six."; B09 has "They ended with a reminder to chart his medication at six." The other three are byte-identical.

Two further diffs the expectations lean on were run as well and also hold: B01 against B08 differs only in the second sentence, B06 against B03 only in the second, B04 against B09 only in the second, B10 against B05 only in the fourth, and B12 against B15 only in the second. So B3's parenthesis ("the second sentence of B01/B08, B03/B06, B04/B09; the fourth of B05/B10") is right.

One wording point, in the plan's prose rather than in P2. The section "The texts, by observable features" says B12 and B15 "differ in one word". They differ in a phrase: "the valve **may have** been left open" against "the valve **had** been left open". The observable feature is real and the pair is a hedged pair; the count of words is wrong. In the same sentence B10 is described as differing from B05 in "what is denied", which is true, but the two sentences also differ in that B05 says "the rise in attendance" where B10 says "the rise". Neither changes any expectation; both should be corrected because the plan is about to be frozen on this prose.

### P3. The tools, the drivers, the translators' materials, the briefs, the runner — FOUND WITH A DIFFERENCE

Twelve of the thirteen items are at their stated hashes:

`tools/ask_model.py` `31ec591f2e2a3d02`; `tools/translate_via_api.py` `0053f66020414e31`; `tools/sameness_2.py` `e66a9d314a0227b6`; `tools/consequences_2.py` `d04f6dfd08268ce7`; `rigs/rig 1 - arguments/patched/run_check.py` `eff1dee15bebc977`; `run_check_2.py` `9a4b21cf771b1208`; `authority/39 Prompt - translate a text into the ledger language.md` `dcfbed45d4e94861`; `authority/L80 The ledger language - complete definition, second version.md` `ec16e220a433e24a`; the encoding guide `afe860e1509caf09`; the reader brief `ddeba43abbbc1dba`; the prose reader brief `888a45f49248fba3`; `PAIRS.txt` `6da2ec538b581a22`. The four example files named beside the encoding guide — `example_T10D.json`, `example_P14.json`, `example_A.json`, `example_A.pl` — are all present in the brief folder.

PAIRS.txt holds eight pairs and they are the eight P3 describes: `B08 B01`, `B03 B06`, `B09 B04`, `B05 B10` (the four matched pairs, F-side first, and B08, B03, B09 and B05 are indeed the F-sides), then `B12 B15` (the hedged pair), then `B08 B16`, `B03 B11`, `B09 B14` (each rewording against its original). Correct.

**The difference is the runner.** P3 records `tools/L82_run.sh` at `a28248c7e19249b7`. The file on disk hashes to `ff20943b245f1422`. The working tree is clean, so this is not an uncommitted edit. `a28248c7e19249b7` is the runner as it stood at commit `9eaf7f6` ("prose reader brief, Arm B runner script (draft)"); `ff20943b245f1422` is the runner as it stands at commit `43aeae7` ("L82 runner in four lanes per provider"). The difference between the two is precisely the change from one lane per provider to four.

This matters more than a stale hash usually would, because the plan's own prose describes the newer file. "Who does what" says "translations in parallel lanes per provider", and P4 says "the run uses four parallel lanes per provider and B9 allows for it". The file at the hash P3 records does **not** run four lanes; it runs one. So P3 names a version of the runner that contradicts two other statements in the same plan. The plan's closing rule — "A premise the checker cannot find at its hash voids the expectation that rests on it" — would, read literally, void every expectation, since every expectation needs the runner's outputs. The hash must be corrected to `ff20943b245f1422` before the freeze.

### P4. The pilot — FOUND WITH A DIFFERENCE

What P4 asserts about T10-D is confirmed, and one thing it asserts about T11-B is now out of date.

Confirmed. Atria returned a ledger that validated, six lines, 263 seconds: `T10D.atria.validation.txt` reads VALID, the gauge in it reads "6 lines said, 0 filled in, 0 usual case", and `T10D.atria.attempt1.receipt.json` records `"seconds": 263.3` and `"attempts": 1`. Mimo likewise: `T10D.mimo.validation.txt` reads "attempt 1 / VALID", the same six-line gauge, and the receipt records `"seconds": 355.0`, `"attempts": 1`. The two strings P4 quotes from the old driver's report on Atria's ledger are in the file verbatim: `NO FAULT FOUND in the lines that were checked.` and `INSIDE 'account_world' (a told world, looked at alone): no contradiction.` T10-D is indeed the guide's first example — `example_T10D.json` is in the brief folder and `translate_via_api.py` sends it in every prompt — so P4's own caveat that the pilot shows the pipeline rather than the models is well placed.

The differences. First, small: P4 says Atria's ledger "validated on the first attempt". The receipt does say one attempt, but the Atria validation file does not; its first line is "rebuilt from .../T10D.atria.attempt1.response.txt", meaning the record on disk was regenerated through the `--rebuild` path rather than written by the live run. Mimo's file does say "attempt 1". The claim is true; the evidence for it is in the receipt, not in the validation file, and the plan should say so.

Second, and more substantive: P4 says "Atria's call on T11-B had not returned after fifteen minutes". **Two** calls on T11-B are outstanding, not one. The directory holds `T11B.atria.prompt.txt` and `T11B.atria.attempt1.request.json` (both stamped 14:14) and `T11B.mimo.prompt.txt` and `T11B.mimo.attempt1.request.json` (both stamped 14:21), and for neither provider is there a `.response.txt`, a `.reasoning.txt`, a `.receipt.json` or an `.error.txt`. Both calls went out and neither came back.

What is in the pilot directory now, in full: the two rate-limiter lock files `.rate_atria` and `.rate_mimo`; for T10-D and each provider a prompt, a request, a response, a reasoning file, a receipt, a translation and a validation file; for T10-D and each provider a built `ledger_T10D_<provider>.json` and `.pl`; and for T11-B and each provider a prompt and a request and nothing else. Twenty-four files.

### P5. What the new driver does and prints — FOUND

Read against `run_check_2.py` at `9a4b21cf771b1208`.

The list of checks is exactly right, including the omission. The function `battery` holds check 1 (contradictions), check 2 (because), check 2b (since), the chain under patch 7, check 3 (plans), check 4 (exceptions), check 5 (likeness), and patches 8, 9, 10 and 14; a told world runs the same battery. Patches 11 and 13, the what-ifs, are guarded by `if world is None:` with the comment "D2: what-ifs are not run inside a case", which is why P5's list leaves them out. Correct.

The printed strings. `named_line` returns `line <id> [<mark>, sentence <N>]`, so the heads read as P5 quotes them. A because head is `'BECAUSE-claim on %s: "%s".'` and a JUMP follows as `JUMP. Even granting the stated cause, nothing in the ledger produces ...`, with a block titled `Claim line`. A since head is `'SINCE-claim on %s: "%s". (A reason to expect, not a cause.)'` and a NO CONNECTION follows as `NO CONNECTION. Nothing in the ledger leads from the reason to what is expected.` — P5 quotes the head without its "(A reason to expect, not a cause.)" tail, which is a shortening, not an error, but a marker matching on exact strings should know the tail is there. The plan verdict prints `CANNOT TELL whether the plan can work. The ledger says nothing about ...` with a block titled `Plan line`. The denial head is `'DENIED BECAUSE on %s: "%s".'` followed by `Fine. Nothing in the ledger makes ...` or by `YOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY. ...`, and the claimed-and-denied line reads `YOU CLAIM AND DENY THE SAME CAUSE: <named line> claims <E> BECAUSE <C>, and <named line> denies it.` All as quoted.

The OUTCOMES block is printed once for the actual ledger and once per world, headed `OUTCOMES:` with one indented line per name. P5 names three of those lines — "because claims", "since claims", "plans" — and does not claim the list is exhaustive; in fact there are twelve names, eleven inside a world, since "what-ifs" is dropped there. The five forms P5 points at are the five that `reading()` can return: "ran out of time"; "not asked, nothing to ask"; "not asked, no line of that kind"; "asked, nothing found"; "asked, N found". Five, as stated.

### P6. The old driver's silence — FOUND WITH A DIFFERENCE

The substance holds and the citation does not.

The substance. In `run_check.py` the module global `WORLD_REMOVED` is set to every case line before any check runs, and it stays that way through check 1, check 2 (because), check 2b (since), the chain, check 3 (plans), checks 4 and 5, and patches 8, 9, 10 and 14. Every line belonging to a told world is therefore taken out of the program before those questions are asked, so a claim sitting in a told world cannot produce a BECAUSE, a SINCE or a PLAN finding. The told-world section that follows asks one question only, `contradiction(F)`, and prints either `INSIDE '<case>' (a told world, looked at alone): no contradiction.` or a contradiction block. So the old driver does ask a told world only for contradictions, and it does print no BECAUSE, SINCE or PLAN finding on such a ledger. Confirmed, and the pilot's Atria report shows exactly this shape.

The difference. P6 cites "`run_check.py` lines 311 to 320". Lines 311 to 320 are the head of the told-world loop and its contradiction query — that is where the *one* question is asked, but it is not where the silence comes from. The silence comes from the single statement that sets `WORLD_REMOVED` to all case lines, which stands well before the checks, and from the fact that patch 14's DENIED BECAUSE block also sits under it. A reader sent to lines 311 to 320 to verify P6 will not find the mechanism there. The citation should name both places.

### P7. L81 section 3, the four conditions — FOUND WITH A DIFFERENCE

P7 is the one premise with no path and no hash. It is a paraphrase of L81 second version, section 3, and the paraphrase loses two things.

What matches. L81's "Not acceptable" list has four cases, and P7's first, second and fourth are faithful: F2 and F1 where it can be seen, under an admitted change; a claim the question asks about put where no query reaches it; a sentence reaching neither a line nor the bin. P7's list of what counts as variation — wording, the form of a line, standing where the text does not settle it, extra Thing lines — is L81's list word for word.

First loss. L81's third case is headed "Non-circular dependence, **both halves**" and has two halves: an added line whose content is the conclusion, *and* the requirement that "there must exist an admitted change under which the answer changes, so a ledger whose findings survive every admitted change has no dependence to report". P7 renders the case as "an added line supplying the answer" and drops the second half in silence. This is the same fault L81's own preamble records against the first version of L81, which "misquoted L64's six admitted changes and dropped one silently".

Second loss, and the heavier one. L81's marking rule for Arm B is not four conditions. It reads: "A difference between two translators, or between a translation and the prose, counts as an error only under one of the four, **or on a prose reader's verdict that the ledger commits the writer to what the prose does not (a hedge made a fact; a claim the reported person never made)**." P7 says "only under one of four conditions" and leaves the prose reader's limb out entirely. That limb is the whole reason the prose reader role exists — L81 says so directly: "A shared error of the two translators shows only in the prose reader's verdict, never in the comparison between them; that is why the role exists." Three expectations, B10, B11 and B13, charge errors on the prose reader's verdict. As P7 is written, none of them has a premise to stand on.

P7 should also be given a path and a hash like every other premise.

### P8. The sameness buckets and the partition — FOUND WITH A DIFFERENCE

`sameness_2.py` was read and then run once, on `Language/rigs/rig 1 - arguments/ledger_A.json` against `ledger_A2.json`.

The six headings P8 names are all printed, in this order: `BOTH SAY (12):`, `ONLY THE FIRST SAYS (0):`, `ONLY THE SECOND SAYS (0):`, `SAME CONTENT, DIFFERENT STANDING (0):`, `NEAR, JUDGE BY HAND (1, overlap >= 0.50):`, `OPPOSITE (0, a near pair with NOT on one side only):`. Each heading carries its count, which P8 does not mention. A seventh line follows that P8 does not name at all: `BIN ENTRIES: first 0, second 0 (compare by reading)`.

The difference is the partition. P8 says the six buckets are such that "every line appears in exactly one of them". The file says the opposite about one of the six, twice over. Its header comment: "SAME CONTENT, DIFFERENT STANDING ... re-lists matched pairs whose standing differs, and it is not one of the buckets that partition the lines. The buckets that partition are BOTH SAY, ONLY THE FIRST SAYS, ONLY THE SECOND SAYS, NEAR and OPPOSITE." And the docstring of `partition_or_stop`, the function that enforces it: "SAME CONTENT, DIFFERENT STANDING re-lists pairs already counted under BOTH SAY and is not one of the buckets." The enforcement code places lines from five buckets only and exits with a message if they do not cover both ledgers.

So the partition is over **five** buckets, not six, and P8 as written is false. The run bears this out: twelve pairs under BOTH SAY, zero under SAME CONTENT DIFFERENT STANDING, one near pair, and every line of both ledgers accounted for by the five. The practical damage is nil for B3 and B12, which read only the ONLY and OPPOSITE buckets, but the premise is wrong and a marker who relied on it would double-count standing differences.

### P9. What the translator tool validates — FOUND

Read against `translate_via_api.py` at `0053f66020414e31`. Every clause of P9 is in the code.

Required fields: `paragraph`, `sentences`, `lines`, `bin`, `leftover`, `whatifs` are each checked for presence, and each line is checked for `mark`, `sentence`, `standing` and `text`, with `mark` restricted to said / filled in / usual case, `sentence` required to be an integer, and a TOLD or SUPPOSED standing required to carry `case` and `case_kind`. Every clause guarded by its own `line(<id>)`: the check takes the clause body after `:-` and requires `line(<id>)` in it. Every sentence in a line or the bin: the covered set is built from the lines' sentence numbers and the bin's, and any sentence outside it is reported as "reaches neither a line nor the bin". The old driver running without a Prolog syntax error: the rig is copied to a temporary directory, `patched/run_check.py` is run on the built ledger, a non-zero return code is a problem, and the raw log is searched for "syntax error", "Syntax error" and "syntax_error". One retry with the failures: the loop runs at most twice and the second prompt appends "===== YOUR PREVIOUS ANSWER DID NOT VALIDATE =====" with the problems listed.

P9's last sentence also holds. `build_pl` writes `line(<lid>).` using the model's own line ids, and the drivers' report heads print those ids through `named_line`.

One observation, not a contradiction. The guard check inspects only the body after `:-`. A clause written as a bare fact, with no `:-`, has an empty body and will always be reported as unguarded. That is a strict reading of 39 and the encoding guide, both of which tell the translator that every clause's first body goal is `line(<id>)`, so it is probably intended; it is worth knowing, because it is a plausible reason for a first-attempt validation failure and B5 counts those.

---

## Part 2. The expectations

Read against six questions each: are both sides of the "against" cell bracketed; can the row be marked under every outcome the run can produce; does it name an instance no premise establishes; does it rest on a premise marked with a difference; is the layer it charges the one that would have moved; and is it stated by observable features rather than by the map.

**On the map, for all thirteen at once — sound.** Not one expectation needs MAP.json or MAP2.json to be marked. B1, B2, B4, B6 and B12 name passages by the S-side / F-side / control / rewording classes, and every one of those classes is defined in "The texts, by observable features" by shared openings, added rules, added routes, differing denials and the absence of connectives — all of which I confirmed by reading and diffing the texts. B10 names the hedged pair, which is visible as "may have been" against "had been". B11 names B13, which is visible as the only passage with no reporting verb in it. B3's differing-sentence numbers are visible by diff. The seal therefore does what the plan says it does: it checks the writer's intent at marking, not the marker's blindness. This is the strongest part of the plan and should be kept as it stands.

### B1, the F-sides inside the world — brackets complete, one outcome unprovided for

The "against" cell brackets both sides: 8 of 8 expected, 7 or fewer counts against, and the cell separately says silence charges the driver while a claim placed in the actual ledger or absent altogether charges the translation and is recorded rather than counted. The denominator is right: four F-sides times two translators is eight.

The outcome it cannot be marked under is a ledger that **does** put the claim in a told world but writes it in a form the driver never asks about — a because relation expressed as something other than `claim_because`, for instance. The cell's carve-outs cover "in the actual ledger" and "absent"; they do not cover "present, in the world, in a shape no query reaches". That outcome charges the encoding guide or the language, not the driver, and the row as written would score it against the driver.

It names no instance no premise establishes: P5 establishes that the driver prints those four finding kinds, and the observable features establish that B03, B08, B09 and B05 carry a because, a since, a plan and a claimed-and-denied cause respectively.

It rests on P3, which I marked with a difference.

### B2, the S-sides, the near miss — brackets complete, B10 unprovided for

Both sides are bracketed, and the row is unusually careful: it names the driver as the charge when a JUMP, NO CONNECTION or CANNOT TELL fires on a ledger that holds the rule as a general line pointing at the right facts, and it makes the row unmarkable when the translator wrote no rule line.

The gap is B10. B10's S-side feature is not a rule or a route; it is a *differently denied cause*. The unmarkability clause is written only for "an S-side ledger with no rule line", so if a translator writes no `denied_because` line for B10 at all, the row gives the marker no instruction: there is nothing to read "Fine." on, and nothing to say the ledger is unmarkable. Since B10 is also the one text for which B2 expects both translators rather than one, this gap bites.

The layer is correctly left open ("the rig, or the translator, as stated"). Rests on P3.

### B3, variation within pairs — brackets complete, markable throughout

Expected: eight pair-comparisons with no ONLY or OPPOSITE line on an unchanged sentence. Against: any such line, charged to that translator, counted per translator. Exhaustive — every comparison either has such a line or does not.

The sentence numbers it names are right; I confirmed by diff that the differing sentence is the second for B01/B08, B03/B06 and B04/B09 and the fourth for B05/B10.

It rests on P8, which I marked with a difference, but the difference does not reach it: B3 reads only the ONLY and OPPOSITE buckets, and those two are genuine partition buckets in the code. It also rests on P3.

The charge — the translator — is right. A ledger line that moves where the prose did not move is the transport's doing, and this is L81's case 1.

### B4, the controls — the OUTCOMES half is not bracketed, and one outcome cannot be marked

The finding half is bracketed cleanly: no finding of any kind is expected, any finding counts against, and the cell splits the charge between translator and driver by whether the ledger holds a claim line the text does not state.

The OUTCOMES half has no against at all. B4 expects the world OUTCOMES to read "because claims: not asked, ...", "since claims: not asked, ...", "plans: not asked, ...". If no finding fires but those three lines read "asked, nothing found" instead, the row is met on its first half and silent on its second. That distinction is exactly what L79 D5 was built to draw — a ledger that carries a line of that kind and produces nothing is a different state from a ledger that carries no such line — so leaving it unbracketed wastes the row.

The outcome it cannot be marked under: **a control ledger with no told world at all**. B02 and B07 contain no argument; nothing in 39 or the encoding guide forces a translator to open a told world for a passage that merely lists samples or deliveries, and 39's attribution rule is about attributed belief and reported argument. If a translator writes B02 with no `case` at all, the driver prints no world section, and "the new driver's world OUTCOMES" do not exist. B4 says nothing about that outcome. It should either say the actual-ledger OUTCOMES are read instead, or make the row unmarkable and say so.

Rests on P3 and P5.

### B5, validity and size — the denominator is wrong

Both sides are bracketed: at least 8 of 10 expected, fewer than 8 for either provider counts against, and the row also says what happens to a thin ledger (unmarkable for B1 to B4 and B6, and listed). The listing clause is good design; it is what keeps the other rows' denominators honest.

**"8 of 10" is stale.** The corpus is sixteen passages. The plan's own "Who does what" speaks of 32 translations, and B9 says 32. B5 is a leftover from the first version, which had ten passages. As written, a provider that validates ten of sixteen meets the row.

The row also asks for something no output computes: "at least 3 said lines and at least one TOLD line". The said count is readable off the GAUGE line of either driver's report. The TOLD count is not in any report; it is in the ledger JSON's `standing` fields and in `sameness_2`'s line display. The marker can get it, but the runner produces no count, and the row should say where to read it.

The layer — "the translator, or the guide" — is right.

### B6, read-back — a band falls between the two sides

The row names three things and brackets two of them exhaustively: any fault "found" on an old-driver report or on a control report counts against, and so does a sentence number the report does not print. Those are clean.

The first clause is not bracketed. Expected: the finding and the sentence number traced on **at least 7** of the 8 new-driver F-side reports. Against: **5 or fewer** of 8. **Six of eight falls in neither.** The row can be neither met nor counted against on its main clause, which is the one clause it exists for.

The layer it charges is "the report (read-back layer)". For two of its three triggers that is right. For the third — a sentence number the report does not print — the thing that moved is the *reader*, which invented a number; charging the report for the reader's invention misplaces it. Since Atria is a fixed instrument here and "Not tested" says a reader other than Atria is out of scope, the row cannot separate the two, and it should say so rather than assign the charge silently.

One further note, not a defect in the row but a limit on it. The old and new drivers print visibly different reports — the old one opens "NO FAULT FOUND in the lines that were checked." and has no OUTCOMES block; the new one has an OUTCOMES block and four extra gauge counts. The reader can tell old from new by shape even under neutral names. That does not break B6, whose two halves expect different things of the two, but it means the shuffle does not make them exchangeable, and the marker should not read the reader's silence on an old report as blind silence.

Rests on P3 and P5.

### B7, the two translators agree in kind — the denominator is wrong and a band falls between

Expected at least 7 of 10 texts; against 5 or fewer. **Two faults.** "Of 10" is stale in the same way B5 is; the corpus is sixteen. And 6 of the denominator falls between the two sides, so the row has an unmarkable band, exactly as B6 does.

The layer — the translator layer, with the note that 39 leaves room — is right, and the Traps section reinforces it correctly.

Rests on P3 and P5.

### B8, the old driver's silence — sound

Expected: no BECAUSE, SINCE or PLAN finding on any ledger whose claim sits in a told world. Against: any such finding. Exhaustive; there is no third outcome.

It is the one row that charges a premise rather than a layer, and that is the right charge: a finding there would falsify P6, which is what the row is for. P6 I marked with a difference, but the difference is in the citation, not in the behaviour, and the behaviour is what B8 tests. The row survives.

### B9, time — bracketed, but the run will almost certainly fire it, and for the wrong reason

Four budgets, and "over any of the four" counts against. Exhaustive.

The run cannot meet two of them as the script is written, which is set out in Part 3. In short: steps 5 and 6 are strictly sequential, so the 64 reader calls and the 32 prose-reader calls each go out one at a time, against pilot latencies of 263 seconds for Atria and 355 seconds for Mimo. Thirty-two sequential Mimo calls will not finish in 60 minutes on any plausible reading of those numbers. A row that is nearly certain to fire is not testing anything; it is recording a decision already taken. Either the budgets or the script has to change.

The layer charged is "the pipeline", which is right as far as it goes, but the pipeline's constraint here is a scripting choice (no lanes in steps 5 and 6), not a provider limit — Mimo's 100 requests a minute would allow all 32 calls to be in flight at once.

Rests on P3, which is the runner, and on P4's timings.

### B10, the hedge — the best-built row in the table; one outcome unprovided for

Both sides are bracketed and the row does something the others do not: it names what a *success* charges. If all four JUMPs and all four prose-reader answers come as expected, the language is charged with the false finding L81 section 5 names, and the contract is declared short a change. That is L81 section 5 used exactly as written, and it is the only row that can move the calibration rather than a layer inside it. It also brackets the translator side (a translator that keeps the hedge out of the world's claim is recorded and the half goes unmarkable for that ledger) and the prose-reader side ("claimed as a fact" on B12, or "hedged" on B15, charges the prose reader).

The outcome not provided for is **no JUMP on B15**. B15 is the unhedged control for the hedge; if a translator's B15 ledger produces no JUMP either, the row's carve-out does not apply — that carve-out is written for B12 only — and a missing JUMP on B15 is the driver's or the translator's, not the language's. Nothing says which.

A wording point for the marker: the row says the prose reader answers "claimed as a fact", but the brief's option is "claimed as a fact **in the passage**". If the marking is done on exact strings, the row should quote the brief.

The instance it names is observable; the hedge is in the second sentence of B12 and nowhere else in the corpus.

It rests on P7, which I marked with a difference, and the difference is the one that matters: P7 drops L81's prose-reader limb, which is the limb B10's prose-reader half stands on.

### B11, the narrator's own — one outcome unprovided for, and one factual claim with no premise

Both sides are bracketed for three failures: a world on B13 charges the translator, the old driver silent while the new reports charges the driver, and a "hedged" or "not made" answer charges the prose reader.

The outcome not provided for is **both drivers silent on B13**. The row brackets the asymmetry (old silent, new reporting) but not the symmetric case, which would be a translation that wrote no because claim at all, or wrote one the driver cannot reach. Nothing says which layer that charges.

The parenthesis "the old driver checks actual-ledger BECAUSE claims" is a factual claim about the old driver that **no premise carries**. P6, the only premise about the old driver, says only what it does *not* do inside a told world. I checked the claim directly and it is true — `run_check.py` runs its because check with only the case lines removed, so an actual-ledger claim is reached, and a JUMP is printed from the same template as the new driver's. But the plan asserts it without a premise, which is the failure this check exists to catch. It should become a premise, or be folded into P6.

B11 also rests on P7's missing prose-reader limb, and on the prose reader brief's answer vocabulary, which no premise quotes (see below).

### B12, the rewordings — brackets complete, but the charge contradicts L81

Expected 6 of 6; against any ONLY or OPPOSITE line on an unchanged sentence, or a report kind that differs within a rewording pair. Exhaustive on both halves. The instances are observable, and I confirmed all three rewordings differ in exactly one sentence and are byte-identical elsewhere.

**The charge is wrong on the second half.** B12 charges "the translator" for both halves, citing L81 case 1. For the first half — a ledger line that moved where the prose did not — that is right. For the second half it is not. If the sameness run shows no ONLY or OPPOSITE line on an unchanged sentence, the two ledgers did *not* move, and a report kind that nevertheless differs between them is the driver's doing. L81 section 5 says this in so many words: "a text where the variation test passes on both ledgers and the reports still disagree in kind: then the report, not the translation, is the variable, and the driver is charged." As written, B12 would charge the translator in precisely the case L81 reserves for the driver.

The two halves also need to be read in order, and the row does not say so: whether the sameness half passed determines who the report-kind half charges.

It also rests on P8, though the difference in P8 does not reach it.

### B13, the prose reader on every report — one answer falls outside both sides

Both sides are bracketed for the two answers the row anticipates: a "not made" answer charges the translation and is listed; a part 2 quotation on a non-control charges the translation if the ledger lacks the line and the driver if it has it. That second split is well made.

The prose reader brief offers **four** answers in part 1: "claimed as a fact in the passage", "hedged in the passage", "not made in the passage", and "cannot tell from the report". B13 addresses one of them. "Cannot tell from the report" is unprovided for, and it is the answer most likely to arrive in bulk, because it is what a careful reader says when a report names a line id it cannot tie to any sentence. Nothing says whether a run full of "cannot tell" meets B13, fails it, or charges the report.

It rests on P7's missing prose-reader limb.

### A premise nobody wrote

Three rows — B6 on the reader, and B10, B11 and B13 on the prose reader — are marked by matching the model's answers against the vocabulary of the two briefs. P3 gives both briefs a hash, and both hashes are correct. **No premise quotes what is in them.** No premise records that the reader brief asks for four numbered parts, that part 2 is where the sentence number goes, or that part 3 is where the world goes; no premise records the prose reader's four part-1 options or that part 2 is the "anything missing" question. Four expectations are marked on strings that the premise list never states. This is the same gap as B11's unpremised parenthesis, and it should be closed by a new premise quoting both briefs' answer formats.

### Where two rows could give contradictory marks on the same outcome

**B4 against B13, on a control.** Suppose a finding fires on a B02 or B07 report and the prose reader answers "not made in the passage", but the ledger does *not* hold a claim line the text fails to state — the finding came out of some other line. B4 says: charge the driver, because the translator-side condition is not met. B13 says: charge the translator, because a "not made" answer means the translator invented a claim. Same outcome, two charges, two layers. Nothing in the plan orders the two rows.

**B12 against L81 section 5**, set out under B12 above: the same outcome — variation test clean, report kinds differing — is the translator's under B12 and the driver's under the calibration the plan is written to.

**B10 against the default marking rule.** A prose-reader verdict of "hedged in the passage" where the ledger's claim is bare is, under L81's marking rule, an error charged to the translation. B10 overrides that and charges the language, on the ground that the language offers no way to keep the hedge. That override is right and L81 section 3 supports it — but it is an override, and nothing outside B10's own cell says so. A marker working from L81 alone, or from P7, would charge the translator. The override should be stated where the marking rule is stated, not only inside one cell.

---

## Part 3. The run spec

Read line by line: `Language/tools/L82_run.sh`, the file on disk, hash `ff20943b245f1422`. The hash in P3 names a different, earlier file; see P3 above. Everything below describes the file that exists.

### Does it produce every output the expectations need?

Mostly yes. Step by step against "Who does what":

Step 1 translates, four lanes per provider, lane *k* taking every fourth text, eight background subshells and one `wait`. Sixteen texts, four per lane. This is the four-lane arrangement the plan's prose describes.

Step 2 runs both drivers on every valid ledger, writing `<ledger>.old.txt`, `<ledger>.new.txt`, a raw log and a stderr file for each. Sixteen texts times two translators times two drivers is the 64 reports the reader needs.

Step 3 runs `consequences_2.py` on every valid ledger.

Step 4 runs `sameness_2.py` twice over: once per pair per translator from PAIRS.txt, which gives the four matched pairs B3 needs and the three rewording pairs B12 needs and the hedged pair; and once per text across the two translators, which gives the cross-translator diagnostic L81 asks for. Both sets are produced.

Step 5 produces the reader's 64 calls under neutral names R01 upward, with `KEY_report_names.json` mapping each code to its report. The key exists, as the plan requires.

Step 6 produces the prose reader's 32 calls, each with the passage and the new-driver report in one prompt, and no ledger. The text id is recovered from the report filename by splitting on underscore, which works for ids of the form B03 and would break on any id containing an underscore; there are none.

Step 7 writes a manifest of every file under the output directory except the scratch rig, each with its SHA-256.

Timings are printed for step 1 (translations), step 2 (drivers), step 5 (reader) and step 6 (prose reader). Those are the four B9 budgets — except that B9's fourth is "the rig runs within 15 minutes" and step 3, `consequences_2` on every ledger, is untimed. If "the rig" means steps 2 and 3 together, the number B9 needs is not printed.

Two things the expectations need and the script does not produce. B5 wants a count of said lines and TOLD lines per ledger; nothing computes either, though the said count is on the GAUGE line and the TOLD count is in the ledger JSON. And no step summarises failures: `subprocess.run` return codes are discarded in steps 5 and 6, so a reader call that fails after six attempts leaves an `.error.txt` and no response, and the run reports nothing. B6 counts out of eight; a silently missing report would reduce the numerator with no record.

### Does it leak the translator's name, the ledger id or the text id into the reader's prompt?

**The translator's name: no leak found.** `translate_via_api.py` writes the provider into two places — the first line of the built `.pl` file, as a Prolog comment, and the `whose` field of the ledger JSON. Neither driver prints either. I checked: neither `run_check.py` nor `run_check_2.py` reads `meta["whose"]`, and neither echoes the `.pl` text into the report; the `.pl` goes to s(CASP) and the justification trees go to the raw log, which is a separate file the reader never sees.

**The ledger id: no leak found.** No report names the file it was built from.

**The text id: closed on the one line the script blinds, open elsewhere.** The report's first line is `REPORT for paragraph <meta["paragraph"]>`, and `translate_via_api.py` sets `paragraph` to the text id — though by `setdefault`, so a model that supplied its own value keeps it. Step 5 overwrites line 0 with "REPORT for a passage", which closes that line. But the blinding is **one line deep**, and two other channels carry model-authored free text straight through:

First, the world name. A told world's heading reads `INSIDE '<case name>' (a told world, looked at alone): ...`, and the case name is whatever the translator chose. The encoding guide constrains line ids ("short lower-case letters or words with no spaces") but places no constraint at all on case names. A translator that names the world after the file — `b03_log`, say — puts the text id into the reader's prompt, and the script will not catch it.

Second, the GAUGE line. It ends with the leftover bin's entries joined and quoted in full. The pilot shows how much that can be: Atria's bin entry on T10-D runs to three sentences of commentary. A bin entry that quotes the passage, or names it, reaches the reader verbatim.

Neither channel is the translator's name or the ledger id, so the strict question is answered no. But the plan says the reader "never sees a passage", and through the GAUGE the reader can see a good deal of one. Either the blinding should be deepened — strip the bin quotations, and rewrite case names to neutral tokens with a key — or the plan should say plainly that the reader sees whatever the translator wrote in the bin and in the world's name.

### Does the shuffling seed make the reader's order reproducible?

Yes. The report list is built with `sorted(...)`, shuffled by `random.Random(82)`, and the resulting order is frozen into the key dictionary, which Python iterates in insertion order. Given the same set of reports, the same codes go to the same reports and the calls go out in the same order every time. If a ledger fails validation the set is smaller and the whole assignment shifts, but it shifts reproducibly. The code format `R%02d` holds to 99, and the run needs 64.

### What happens when a ledger fails validation?

**It is excluded consistently, and the exclusion mechanism is sound.** The gate is one line: for each `ledger_*.json` in the translations directory, the corresponding validation file is checked for a line beginning "VALID", and only then is the pair of files copied into `ledgers/` and into the scratch rig. The filename arithmetic is right — `ledger_B03_atria` is rewritten to `B03.atria`, which is exactly the name `translate_via_api.py` writes. Everything downstream draws from those two directories: steps 2 and 3 iterate the scratch rig, step 4 guards each comparison with a file test against `ledgers/`, and steps 5 and 6 read the reports directory, which only ever held valid ledgers' reports. An invalid ledger is therefore absent from the drivers, from consequences, from both sameness runs, from the reader and from the prose reader. Consistent.

Three things to know about it. The test `grep -q '^VALID'` is run against a file that also contains the old driver's whole report appended below the verdict; no line the driver prints begins with "VALID", so it is safe today, but it is a one-line anchor on a file with foreign content below it, and a translator's quoted text beginning a line with that word would flip the gate. The validation file is overwritten each attempt, so its first line ("attempt 1" or "attempt 2") is where B5's "within two attempts" is read — that works, but only because the last attempt is the one on disk. And if a text fails both attempts, the ledger JSON and `.pl` from the losing attempt remain in the translations directory; only the gate keeps them out of the run, so anyone reading that directory by hand will find ledgers that were never used.

### Shell and script errors

**Sequential reader and prose reader, against B9.** Steps 5 and 6 each run a plain Python loop with blocking `subprocess.run`. Sixty-four Atria calls one after another, then thirty-two Mimo calls one after another. The pilot's measured latencies are 263 seconds for Atria and 355 seconds for Mimo on a 12,000-token prompt; reader prompts are shorter, but both providers spent most of their time on reasoning tokens (1,908 of 3,593 for Atria; 10,800 of 12,258 for Mimo), which does not shrink with the prompt. Even at a quarter of the pilot latency, 32 sequential Mimo calls exceed 60 minutes. B9's reader and prose-reader budgets cannot be met by this script, and nothing about the providers forces it: Mimo's own limit would allow all 32 calls concurrently. Step 1 gets four lanes; steps 5 and 6 get none. This is the single change that would most improve the run.

**The 900-second timeout against B9's three hours.** `ask_model.py` uses a 900-second socket timeout and retries up to six times. The pilot's T11-B calls had not returned after fifteen minutes — that is the timeout itself. A text that times out repeatedly costs up to six times 900 seconds plus backoff, roughly 95 minutes, for one text. With four texts per lane, one bad lane can exceed B9's three hours by itself. P4 notices the hanging call and says "B9 allows for it"; the arithmetic says it may not.

**`$OUT` must be absolute, and nothing enforces it.** Step 2 does `cd "$OUT/scratch"` and then, from inside that directory, writes to `"$OUT/reports/..."`. If the caller passed a relative output directory, those redirections resolve under the scratch directory, the target directories do not exist, every redirection fails, and — because the script sets `-u` but not `-e` — the loop runs to the end writing nothing. Step 3's `ln -sfn "$OUT/scratch/patched"` has the same exposure. The usage line says to run from the repository root but says nothing about the output path. It should either require an absolute path or convert it at the top.

**An empty report kills step 5 or step 6 outright.** Both steps do `lines = body.splitlines()` and then assign to `lines[0]`. If any driver produced an empty stdout — a crash, with the traceback captured to the separate `.err.txt` — `splitlines()` returns an empty list and the assignment raises IndexError. That is not a skipped report; it aborts the whole heredoc, so step 5 makes no reader calls at all, or step 6 makes no prose-reader calls at all, and the script carries on to the next step as though nothing had happened. One conditional fixes it.

**No `set -e`, and no check that step 1 produced anything.** If every translation fails, step 2 finds no `.pl` files, every later step produces nothing, and the script exits 0 having printed "valid ledgers: 0" somewhere in the middle. Nothing stops the run or flags it.

**The raw logs are opened in append mode.** Both drivers do `open(sys.argv[2], "a")`. A second run over the same output directory appends to the existing raw logs rather than replacing them. Harmless if the output directory is fresh each time; confusing if it is not.

**`ls`-derived text list.** `TEXTS` comes from `ls` filtered by `^B[0-9]+\.txt$`, which correctly picks the sixteen passages and skips MANIFEST.json, the two `.enc` files and the two `.md` files. Fine as long as no passage filename ever contains a space.

Two things that look like errors and are not: `cp` with two sources and a directory target in the gate line is correct, and `cp -r "$RIG/patched" "$OUT/scratch/patched"` creates the copy correctly because the target does not yet exist. Both drivers read `checker_rules.pl` from their own directory, which the scratch copy includes, and `SCASP` is an absolute path, so running the drivers from the scratch rig works.

### `ask_model.py`: the rate limiter, retries, and whether four lanes respect 30 and 100 a minute

**The limiter.** Before every attempt, `wait_for_slot` opens a lock file named for the provider, takes an exclusive `flock`, reads the timestamp of the last request, sleeps if less than 60/rpm seconds have passed, writes the current time, and releases. The sleep happens while the lock is held, so waiting processes queue behind it rather than all waking at once. The gap is 2.0 seconds for Atria at 30 a minute and 0.6 seconds for Mimo at 100.

**Four lanes: yes, with two caveats.** All four lanes of a provider call `translate_via_api.py` with the same output directory, and it passes that directory to `ask_model.py` as `--out`, so all four share one lock file per provider. The flock serialises them, and no two requests for one provider can start less than the gap apart, however many lanes there are. Four lanes respect 30 a minute for Atria and 100 a minute for Mimo.

The first caveat is arithmetic. The limiter enforces a minimum gap between request *starts*, which bounds the long-run rate at exactly the limit but permits 31 starts for Atria, or 101 for Mimo, inside a worst-aligned 60-second window. Providers that count in fixed windows may see that as one over. If the limits are hard, the gap should carry a small margin.

The second caveat is scope. The lock file lives in the output directory, not in a fixed place. Steps 1, 5 and 6 use three different output directories and therefore three different lock files — harmless, because those steps run one after another. It stops being harmless the moment anything else touches the same provider at the same time: a hand rerun of a failed text while the main run is going, or a second pilot, would not share the lock, and the limit could be breached without either process knowing. A per-provider lock in a fixed location would remove the hazard.

**Retries.** Up to six attempts, sleeping `min(120, 5 × 2^attempts)` between them — 10, 20, 40, 80, 120 seconds. It retries on any non-200, which covers 429 and 5xx; on any exception, which covers socket timeouts at the 900-second limit; on a 200 whose body does not parse as JSON; and on a 200 with no `choices`. That is the right set for the failures the pilot shows. It also retries six times on a 401 or a 400, which cannot succeed, wasting about four and a half minutes per bad call at the start of a run — worth a short-circuit on 4xx other than 408 and 429. Every attempt goes through the limiter, so retries cannot burst.

**Receipts.** Each call leaves a request body, a response, a reasoning file and a receipt carrying the provider, the model as the provider reported it, the request hash, the provider's response id, token counts, the wall-clock seconds and the attempt count. The pilot's receipts are complete and are where P4's 263 and 355 seconds come from. The plan's requirement that every call leave a receipt is met.

---

## Verdict

**DO NOT FREEZE YET.**

Nine of the thirteen expectations are well made, and the corpus is the strongest part of this plan: every passage is at its recorded hash, every sentence count is right, every connective set is right, all three rewordings differ in exactly one sentence, and not one expectation needs the sealed maps to be marked. What stops the freeze is four stale or incomplete premises, three expectations with bands that can be neither met nor counted against, two places where two rows would charge different layers for the same outcome, and a runner that cannot produce two of the four things B9 asks it to produce inside the time B9 allows.

What must change before the freeze:

1. **Correct P3's hash for the runner.** `tools/L82_run.sh` is `ff20943b245f1422`, not `a28248c7e19249b7`. The recorded hash is the previous commit's one-lane runner, which contradicts the plan's own statements in "Who does what" and P4 that the run uses four lanes per provider. Under the plan's own voiding rule, the stale hash currently voids every expectation.

2. **Repair P7.** Restore the second half of L81's third case — that there must exist an admitted change under which the answer changes — and, more importantly, restore L81's fifth limb: an error also counts "on a prose reader's verdict that the ledger commits the writer to what the prose does not". B10, B11 and B13 have no premise without it. Give P7 a path and a hash like every other premise.

3. **Correct P8's partition.** `sameness_2.py` partitions the lines over five buckets — BOTH SAY, ONLY THE FIRST SAYS, ONLY THE SECOND SAYS, NEAR and OPPOSITE. SAME CONTENT, DIFFERENT STANDING re-lists pairs already counted under BOTH SAY and is not a partition bucket; the file says so twice and enforces it in `partition_or_stop`. Note also the printed `BIN ENTRIES` line, which P8 omits.

4. **Correct P4 and P6.** P4: two T11-B calls are outstanding, Atria's and Mimo's, not one, and the Atria validation record on disk was produced by `--rebuild`, so the "first attempt" claim is carried by the receipt rather than by the validation file. P6: the citation to lines 311 to 320 points at the told-world contradiction query, not at the statement that removes every case line before the because, since and plan checks run; cite both.

5. **Add a premise for the two briefs' answer formats.** B6 is marked against the reader brief's four numbered parts, and B10, B11 and B13 against the prose reader's four part-1 options. P3 hashes both briefs but no premise states what is in them. Add one, quoting the reader's parts 2 and 3 and the prose reader's four options and part 2.

6. **Make B11's claim about the old driver a premise.** "The old driver checks actual-ledger BECAUSE claims" is true — I verified it — but no premise carries it. Fold it into P6 or give it its own number.

7. **Fix the stale denominators in B5 and B7.** Both say "of 10"; the corpus is sixteen passages and the plan elsewhere says 32 translations. B5 should read 13 or 14 of 16 per provider, or whatever the owner intends; B7 should read out of 16.

8. **Close the unmarkable bands in B6 and B7.** B6 expects at least 7 of 8 and counts against at 5 or fewer, leaving 6 in neither; B7 expects at least 7 of 10 and counts against at 5 or fewer, leaving 6 in neither. Move one boundary in each so that every outcome falls on one side.

9. **Provide for the outcomes four rows do not cover.** B4: a control ledger with no told world at all, so that "the world OUTCOMES" do not exist; and an OUTCOMES block that reads "asked, nothing found" rather than "not asked", which is currently neither met nor against. B2: a B10 ledger with no denied-because line, which the "no rule line" clause does not reach. B10: no JUMP on B15. B11: both drivers silent on B13. B13: a prose-reader answer of "cannot tell from the report", which is one of the brief's four options and falls outside both sides of the cell.

10. **Resolve the two contradictory charges.** B12's second half charges the translator for a report kind that differs within a rewording pair; where the sameness half is clean, L81 section 5 charges the driver. Say that the sameness half is read first and determines the charge. And order B4 against B13 for a control where a finding fires, the prose reader answers "not made", and the ledger holds no unstated claim line: B4 charges the driver, B13 charges the translator. State which governs — and, while there, state where the marking rule lives that B10's override of L81's default charge belongs to.

11. **Give steps 5 and 6 lanes, or change B9.** The 64 reader calls and the 32 prose-reader calls are issued one at a time by a blocking loop. Against pilot latencies of 263 and 355 seconds, neither 60-minute budget is reachable, and nothing about the providers requires it — Mimo's limit would allow all 32 at once, and the per-provider lock already makes lanes safe. Also reconsider B9's three hours for the translations against a 900-second timeout retried up to six times, which can cost 95 minutes for a single text.

12. **Deepen the reader's blinding, or say plainly what it does not cover.** Step 5 rewrites only the report's first line. The told world's name is model-authored free text printed verbatim in every world heading, and the GAUGE line quotes the leftover bin in full — the pilot shows a bin entry running to three sentences of the translator's commentary. Neither carries the translator's name or the ledger id, both of which are genuinely absent, but both can carry the passage to a reader the plan calls blind to it. Strip the bin quotations and neutralise case names with a key, or record in "Not tested" that the reader sees the bin and the world's name.

13. **Fix the four script faults.** Require an absolute output directory, or convert it at the top: step 2 does `cd "$OUT/scratch"` and then writes to `"$OUT/reports/..."`, which silently writes nothing if the path is relative. Guard `lines[0]` in steps 5 and 6, where an empty report raises IndexError and aborts the whole step rather than skipping one file. Check the return codes of the reader and prose-reader calls, so a call that fails after six attempts is recorded rather than silently reducing B6's numerator. And time step 3, so that B9's "the rig runs within 15 minutes" has a number to read.

14. **Correct two sentences in "The texts, by observable features."** B12 and B15 differ in a phrase, "may have been" against "had been", not in one word. B10 and B05 differ in the denied cause and also in "the rise" against "the rise in attendance". Neither changes an expectation; both are about to be frozen.

15. **Renumber the premises into order.** They are listed P1, P2, P3, P4, P5, P6, P7, P9, P8. In a document frozen by hash and cited by number, that should be tidied.
