# S90: verification of draft 3

*Written on 24 September 2026 by a Claude subagent for the orchestrator. It is an independent check of draft 3 of revision 2, as committed at 99e9cd0. The writer did not draft, assemble, check or apply the change list, and wrote no ruling. It read:*
- *the S90 rule, the Parts rule and the rerun note;*
- *the three batch readings and every file in `results/S90 reading rulings/`;*
- *the change list before the pass (3deee3e, md5 a5c92adc9f1e3806c0f9c6394cffde1e, the text the rulings read) and after it (99e9cd0, md5 1488a9cd41c4a284be78769019acf7ca);*
- *the theory texts of draft 2 and draft 3;*
- *the revision note, the S81 case book, and D3-T's `final.md`.*

*It opened no S90 reply, receipt, reasoning file or attempt file. It wrote only this file and its check script, `results/S90 Verification of draft 3 - check script.py`. The script reads and never writes, and it runs checks 1, 2 and 4. Nothing was written into `authority/`.*

## Result

| check | result | in short |
|---|---|---|
| 1. Every FIX carries exactly the ruled text, and draft 3 contains it | **PASS** | All 29 fenced FIX texts are in their ruling files and in their entries. The 8 changed NEWs are in draft 3. The 18 FIX texts the readings give inline are present, and the 6 superseded texts are absent. One cosmetic note: a capital letter in W20.1's CHECK. |
| 2. Draft 2 against draft 3: every hunk is a FIX | **PASS** | Draft 2, with the old NEW of the 8 changed entries replaced by the new NEW, equals draft 3 byte for byte. There is no other difference. |
| 3. The apply tool's self-test | **PASS** | Exit 0. The figures are as reported, and both planted edits were refused. |
| 4. File 11 unchanged; `authority/` untouched | **PASS** | md5 5e494c1095d920d128b9a79de378f923. No commit since 49cc31b (22 September) touches `authority/`, and the working tree there is clean. |
| 5. O35, O45, O48, O24, O46 and D3-T against draft 3 | **PASS** | No verdict moves away from its fixed verdict. O45 holds on firmer text. The other five hold as before. |

The check script reports PASS 106, FAIL 0.

## 1. The ruled texts

**How it was checked.** The script takes every fenced block from the three batch readings (52 in all) and places each one by its section and label.

- **Each FIX text is checked twice.**
  - It must occur in the ruling file it came from. 28 of the 29 occur byte for byte. The one exception is W37.1's four-line record sentence. Batch 3 prints it without the ruling file's two-space indent, so it matches the ruling file once indentation is ignored. The change list carries the ruling file's indented lines byte for byte.
  - It must also occur in its change-list entry:
    - NEW and OLD must equal the entry's fenced block byte for byte;
    - DECLARATION must equal the field byte for byte;
    - REASON, CHECK and CASES AT RISK texts must be contained in the field.
- **Every changed NEW** must also occur in draft 3's theory text, and not in draft 2's.

| entry (R) | ruling files | NEW | DECLARATION | other ruled fields |
|---|---|---|---|---|
| W37.1 (R01) | mimo_A1 R01; atria_A1 item 1 R01 | = b1 and b3 (identical); in draft 3 | none, with the fallback line as ruled | REASON WORD clarification; KIND ORDER; b3's record sentence, byte for byte as in the ruling file; b3's CHECK line; GAIN drops "in the same word as file 10"; LOSS adds file 10's word |
| W19.1 (R08) | mimo_A1 R08 | = b1; in draft 3; grows from 84 to 131 words, as recorded | unchanged | WHERE "Three sentences are inserted"; LOSS as b1 gives it; KIND CLAIM |
| W35.1 (R12) | mimo_C item 1 R12 | = b3; in draft 3 | = b3 | CHECK line byte for byte; LOSS from the ruling's "what is lost" |
| W35.2 (R13) | mimo_C item 4 R13; atria_C item 1 R13 | = Mimo C item 4; in draft 3 | = Mimo C item 4 | CHECK line and the recorder's sentence; REASON adds Atria C item 1's paragraph, byte for byte; LOSS as in the Mimo C item 4 ruling file (L121); Atria C's NEW and DECLARATION absent, as reconciled |
| W20.1 (R15) | mimo_A1 R15 | = b1; in draft 3 | = b1 | the ruled line in REASON (byte for byte) and in CHECK (see note); CASES AT RISK O45 as ruled |
| W40.1 (R25) | atria_C item 5 R25 | unchanged | = Atria C item 5 | CHECK line and the recorder's sentence; CASES AT RISK N22 sentence; Mimo C item 5's KEEP line absent, as reconciled |
| W24.1 (R26) | mimo_A2 R26 | = b1; in draft 3 | none | REASON sentence byte for byte; KIND WORDING |
| W22.1 (R28) | mimo_A2 R28 | = b1; in draft 3 | = b1 | CHECK line byte for byte |
| W6.3 (R39) | atria_B1 R39; mimo_B1 item 2 R39 | unchanged | = b1 = b2 | KIND CLAIM; b2's REASON sentence, in place of "can be dropped without harm"; b2's CHECK after "check 1, SOUND"; b1's superseded REASON and CHECK texts absent |
| W7.5 (R48) | mimo_B1 item 3 R48 | = b2; in draft 3; OLD = b2 | = b2 | REASON paragraph, "Not corrected" sentence and CHECK line, byte for byte; GAIN sentence |

**Also confirmed by the script.**
- **The KEEP entries.** Each of the 14 kept entries has its CHECK text. That is 16 fenced texts, among them W19.2's two lines and its O36 note. All but one are byte for byte. W21.1's reconciled append is nested one level deeper, so only its indentation differs. W19.2's N25 note is present too. The superseded texts are absent: Mimo B2's own R31 append and Mimo C's own R30 line.
- **One S90 line each.** Each of the 24 ruled entries has exactly one line beginning "S90 cross-examination:", labelled FIX or KEEP as ruled. No other entry has one.
- **Which entries changed.** Exactly the 24 ruled entries differ between 3deee3e and 99e9cd0.
- **Which fields changed.**
  - DECLARATION changed in W37.1 (the fallback line only), W35.1, W35.2, W20.1, W40.1, W22.1, W6.3 and W7.5.
  - REASON WORD changed only in W37.1, and KIND only in W6.3.
  - That is what the report says.

**Note (cosmetic, not a failure).** In W20.1's CHECK (change list L780) the ruled line "settled wording (F3, block 2) with one clause added …" opens a sentence, so it reads "Settled wording …". In W20.1's REASON it is byte for byte.

## 2. Draft 2 against draft 3

- **The md5s.** Draft 2 (`tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`) has md5 9aecf2f30ce0b4523606b2b8409fdf37, and draft 3 has 403c4f2fb3e5d57bb48a5647011c9f91.
- **The NEWs.** Eight entries changed their NEW: W37.1, W19.1, W35.1, W35.2, W20.1, W24.1, W22.1 and W7.5. Each old NEW occurs once in draft 2, and each new NEW occurs once in draft 3.
- **The rebuild.** Replacing the one with the other in draft 2 gives draft 3 byte for byte.
- **The hunks.** With no context lines there are eight one-line hunks, one per FIX that changes NEW:

| revised line | entry | change |
|---|---|---|
| 13 | W37.1 | "blind" deleted |
| 119 | W19.1 | typing sentence inserted before the two settled sentences |
| 217 | W35.1 | "a transport to the simulation layer \(S\), with contract \(C\)" |
| 223 | W35.2 | "for every transport to the simulation layer"; "a constructed one" |
| 231 | W20.1 | ", whether or not anyone has described their work" |
| 349 | W24.1 | "for every admitted generator \(a\)" |
| 371 | W22.1 | \(\mathcal E_c\) "the criticism's connection from \(g\) to \(\delta\), interpreted as …" |
| 520 | W7.5 | "(EK) also on (P), " |

`diff -u` shows seven hunks, because L217 and L223 fall in one context window. W6.3 and W40.1 change no text: each NEW is unchanged and occurs in draft 3. **No other difference.**

## 3. The apply tool's self-test

`python3 Semantics/tools/s89_apply_changes.py <scratch> --theory-output <scratch> --self-test` exited 0. It reported:
- 63 entries parsed: 58 applied (55 theory and 3 meta), 5 record-only and 0 held;
- CLAIM 49, ORDER 2 and WORDING 4;
- every OLD, locator and anchor once in file 11, with no overlap;
- N = 49 of M = 55, and K = 42;
- 54 diff hunks, each inside an entry;
- the cut of the meta blocks gives back the theory text;
- both planted edits refused, and the clean draft passed.

**The outputs.**
- The theory output has md5 403c4f2fb3e5d57bb48a5647011c9f91, the same as the committed draft 3.
- Rebuilt with `--date "draft of 24 September 2026, not frozen"`, the full draft has md5 e33624e73da8c31e33a8e8df222931af and 26,026 words by the runner's count, as the change list states. By `wc -w` it has 25,984, and the theory text 11,546.

**The note.** The built note block occurs whole in `tests/Revision 2 - revision note, draft of 23 September.md`, with all 49 declaration lines. Its row R2-01 reads "clarification".

## 4. File 11 and `authority/`

- **File 11.** `authority/11 … revision 1.md` has md5 5e494c1095d920d128b9a79de378f923, and the tool checks this too.
- **Commits.** `git log -- Semantics/authority` shows 49cc31b (22 September 2026) as the last commit to touch the folder. 99e9cd0 changes only the three files in `tests/`.
- **Working tree.** `git status` shows nothing in `authority/`.

## 5. The six cases, worked through draft 3

This check was made by reading, not by a test round. For each case it asks whether any of the eight changed places moves the fixed verdict away. Line numbers are draft 3's.

- **O24, the unused joint setting.** Fixed verdict: two arrangements, not yet chosen between; one reachable setting is enough.
  - **Where draft 3 rests it.** The second arrangement is buildable and reachable, so it is in the population (L475). It agrees on the history, so it survives on \(H\) (L195). Derivation 3 then leaves the value at the joint setting underdetermined (L566).
  - **Derivation 2.** On a contract that contains the setting, the two arrangements answer differently, so they are different candidates (L554–562).
  - **The changed places.**
    - W19.1's sentence (L119) only types the notation that Derivation 2's comparison across candidates uses.
    - W35.1 and W35.2 (L217, L223) concern expectation, which O24 does not raise.
  - **Holds AGREE.**
- **O35, four seconds.** Fixed verdict: the protected condition held; the interruption is on the record and is not a loss.
  - **Where draft 3 rests it.** L435 is unchanged from draft 2. A protected condition is a stated condition over stated occasions, and it is lost exactly when it fails on an occasion it covers. With the condition stated over draws, which is the input the verdict states, the four seconds hold no occasion.
  - **The changed places.**
    - W7.5 (L520) adds only "(EK) also on (P)" to the dependence order, and says nothing about occasions.
    - W35.1 and W35.2 now scope expectation and violation to transports to the simulation layer, which is narrower than draft 2's "every transport". So they cannot newly call the tap's stop a violation.
  - **Holds, as before:** AGREE given the stated input.
- **O45, the spring nobody mentioned.** Fixed verdict: the second spring was in the account and a route from the start.
  - **W20.1's fix (L231)** now says that \(\Gamma\) is the components the candidate offers as doing the work, "whether or not anyone has described their work". So the connected second spring is a commitment from the start.
  - **Part VI agrees.** L299 assesses subsets of the written \(\Gamma\) "whether or not anyone has set them out". L307 gives redundant routes, and "a route … whether or not anyone has described its work".
  - **Holds AGREE, on firmer text.** The fix closes the one reading on which draft 2 could move it away. That is a move toward, not away.
- **O46, the cable that used to be a spring.** Fixed verdict: a new account with a cable; the spring account did not survive.
  - **L307** says that a component reassigned to a new target after a deletion belongs to a new candidate, whose success is not the old one's.
  - **L560** says that candidates that anchor different subnetworks are different candidates.
  - **The changed places.**
    - W19.1's typing, "\(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor", makes the reassignment a change of candidate.
    - W20.1's clause is about which components of a written candidate are its commitments. It cannot carry the reassigned component back into the old account.
  - **Holds AGREE.**
- **O48, the forbidden wire.** Fixed verdict: there is no alternative in that population; the premise is not met.
  - **L475's last sentence** excludes any transport that needs a part every member of the population is built without.
  - **Derivation 3 (L566)** requires the differing transport to be a member of the population.
  - **The changed places.** Neither line is among them. L570's "why surprise is possible" reads the same under W35.1 and W35.2.
  - **Holds AGREE.**
- **D3-T, the discarded lamp controller.** Fixed verdict: No.
  - **Derivation 3 (L566)** needs a differing transport that is a member of the population and survives on \(H\). L195 defines survival.
  - **The discarded design** fails at a tried setting (A on, B off), so it does not survive and cannot be that transport. With two designs and one passing, "the population fixes it" (L568).
  - **The changed places.** None of the eight touches L195, L475 or L566–570.
  - **Holds (No).**

## Discrepancies and observations

**Discrepancies against the five checks: none.** The cosmetic capital letter in W20.1's CHECK is recorded under check 1.

**Observations.** None of these bears on a ruled text or on the theory text.
- **W33.1's housekeeping is not done.** The cumulative list, item 23, asks for W33.1's CASES AT RISK to be reconciled with its CHECK. The O2 item still ends "This derives L275 s2's rule" (L1137), and O19 is not named. The pass lists this under "Options the rulings left open, not taken in this pass" (L241) instead of making it. The R24 ruling called it a record point outside the ruling. It is record-only and in a KEEP entry.
- **Drafter's text left as history.**
  - W37.1's REASON (L377) still begins with the drafter's "The added words pin 'blind' to the body's sense". The S90 bullets that follow it say "blind" is deleted.
  - W20.1's CHECK (L779) still says "No outside reader has seen this wording; X1 must carry it."
  - The list's rule that CHECK governs keeps both unambiguous. A later tidy could mark them as history.
- **Confirmed as reported.** Three things the pass did beyond the literal instruction are confirmed:
  - W19.2's O36 and N25 notes, which cumulative list item 7 asks for;
  - W37.1's new title, which both R01 rulings offer;
  - the LOSS notes on W35.1, W35.2 and W22.1. Each follows its ruling's "what is lost", and W35.2's is taken from its ruling file.
- **Frame edits confirmed.** The header reads "DRAFT 3 — after the S90 cross-examination by Atria and Mimo; not frozen". The counts are CLAIM 49, WORDING 4 and ORDER 2, with groups A 14 of 18, B1 14 of 15, B2 11 of 11 and C 10 of 11. The S90 table of "What the checks changed" has 10 rows and names both calls where two ruled. The findings on Part II's forward notation and on O45 are closed. "Carried forward after S90" lists every item that the three readings passed on.
- **R13 and R25 are not re-ruled here.** They rest on the batch-3 recorder's reconciliation, not on a third checker, as the change list says. This verification checks only that the texts chosen are the ones applied.

Dated 24 September 2026.
