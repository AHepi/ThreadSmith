# S90: how the cross-examination of the revision 2 draft will be read

*Written by a Claude subagent for the orchestrator on 23 September 2026, from 18:59 UTC, before anything was sent, and committed in the same commit as the brief. When it was written, the folder `results/S90 Cross-examination - revision 2 draft - returns/` did not exist, and no S87 or S88 return was opened.*

## What is sent

- **The brief.** `tests/S90 Cross-examination - revision 2 draft, the first 48 changes.md`: md5 a7cfeb263f11c27f7f781b701eeabeeb, sha256 9c830d355bfc2e73c09ffe85bbce7ec59c38eea4071526d72a162034362dde0d, 25,790 words by `wc -w` (25,874 by the runner's count). The budget was 26,000. It is sent whole, as the one user message.
- **To Atria only.** The job list is `tools/s90_jobs - revision 2 draft, Atria.json`, run by `tools/s87_run.py`. It holds one job, `s90_xexam_atria`: effort medium (the map's "audit" for Atria), ladder 65,536 and 65,536, 6 attempts, `max_rejects` 3, `max_pass` 1. Its returns go to `results/S90 Cross-examination - revision 2 draft - returns/`. A dry run of the list was checked and sent nothing.
- **Mimo is not sent now**, because its slots are busy. If it is sent later, it gets the same brief unchanged, its reply is read under this rule, and the two replies are read independently.

## The number

LEGEND gives a new entry the shared sequence's next number at the time of writing. This session's Semantics work holds S87, S88 and S89. The Language log reaches L86, and no Language or HV Skill log entry above 86 exists on any branch (H88 and H90 occur only as the names of cases). So 90 is the next free number, and S90 is used as expected.

## Sources, each checked by md5 when the brief was built

- **The revised text** (section 2 of the brief) is the draft theory text: scratchpad `rev2/file13_draft_theory_only.md`, md5 dd2741b0d5a18617d845b19b874943f4. The block between the brief's marker lines is byte-identical to it. For the record, it is committed as `tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md`, with the same md5. It is a draft, not an authority, and nothing was written into `authority/`.
  - It is the theory text that `tools/s89_apply_changes.py --theory-output` writes: the 48 applied theory entries applied to file 11, and file 11's note (L5) cut with the blank line after it. The build script checked this again when it built the brief, and it located every NEW in the draft.
- **File 11**: `authority/11 … revision 1.md`, md5 5e494c1095d920d128b9a79de378f923, read only. "The current text" in the brief is file 11 with its note cut, as S81 sent it.
- **The change list**: `tests/Revision 2 - change list, draft of 23 September.md`, md5 f50930771cb582fd49311b9e66daae9c, as committed at 12e73da. It has 48 theory entries (CLAIM 41, WORDING 5, ORDER 2), 3 meta entries, 5 record-only entries and 3 held entries.
- **The draft note**: `tests/Revision 2 - revision note, draft of 23 September.md`, md5 6a5ea301e14a540da8fd9c0f5801fbbe. It was read and is not sent.
- **The case books**: the S81 book (md5 4f488d149e44669240d5db546c8e946a) and the S89 candidate book (md5 b2e535777976a511935430bd089ba500).

## What the brief carries and what it withholds

- **Section 1** introduces a theory of explanation, "the current text" and "the revised text", and the three kinds. It names no model, file number, record or round. The only name of a model in the whole brief is the theory's own title inside the revised text, which the S87 and S88 briefs also carried.
- **Section 3** gives each of the 48 theory entries in file-11 order, as follows.
  - The id C01–C48.
  - The Part and heading, in the words the program uses for layer 1 of the record.
  - The revised-text line or lines of NEW.
  - KIND and REASON WORD.
  - The DECLARATION for the 41 CLAIM entries. The 7 WORDING and ORDER entries get "none", and their drafted fallback lines are not sent.
  - OLD and NEW, byte for byte.
  - The section-5 cases among those the entry's CASES AT RISK names, as ids only.
- **Withheld**:
  - every W-number;
  - the entries' REASON, CHECK, GAIN and LOSS, and the direction the drafters expect on each case;
  - decisions D1–D11;
  - the meta entries W1.1, W38.1 and W1.2 (the note, the sources note and the record);
  - the record-only entries W3.1–W3.5;
  - the held placeholders W19, W20 and W31. The brief says only that three repairs are drafted separately, names their places (Derivation 2, (T2), how Γ is typed in non-circular dependence), and asks the reader to leave them out unless a listed change depends on one of them or makes it worse.
- **Words.** The brief was checked for the withheld marker words ("Revision 2", "revision record", "file 13", "Deutsch", "Marletto"). It was also checked for W-numbers, file numbers, log numbers and model names outside the revised text. None occurs.

## The ids

C*nn* numbers the theory entries in file-11 order, as R2-*nn* in the revision record the program writes does, so C*nn* = R2-*nn*.

| id | entry | file-11 line | revised-text line | kind | cases given in section 5 |
|---|---|---|---|---|---|
| C01 | W37.1 | 15 | 13 | ORDER | O11, N11 |
| C02 | W6.1 | 27 | 25 | CLAIM | O6, O8, O12, O21, O27, O35, O40, O50, N11 |
| C03 | W7.1 | 33 | 31 | CLAIM | O12, O35 |
| C04 | W58(ii).1 | 33 | 31 | WORDING | — |
| C05 | W8.1 | 63 | 61 | ORDER | O48 |
| C06 | W36.1 | 71 | 69 | CLAIM | O2, O8, O15, N1, N2, N3, N7, N8, N17, N22, N25 |
| C07 | W45.1 | 77 | 75 | CLAIM | O14, N24 |
| C08 | W30.1 | 121 | 119 | CLAIM | O10, N17 |
| C09 | W57.1 + W32(b).1 | 161 | 159 | CLAIM | O8, N2, N5, N7 |
| C10 | W17.1 | 197 | 195 | CLAIM | O11, O48, N5, N18 |
| C11 | W35.1 | 219–223 | 217–221 | CLAIM | O3, O11, O48, N18 |
| C12 | W35.2 | 225 | 223 | CLAIM | O3, O23, N18 |
| C13 | W35.4 | 227 | 225 | WORDING | O3, N18 |
| C14 | W39.1 | 257 | 255 | CLAIM | O2, N2, N3, N8, N25 |
| C15 | W11.1 | 271 | 269 | CLAIM | O2, N17 |
| C16 | W9.1 | 275 | 273 | WORDING | O2, N1 |
| C17 | W58(i).1 | 301 | 299 | CLAIM | O45, N1 |
| C18 | W28.1 | 309 | 307 | CLAIM | O45, N1, N2, N23, N25 |
| C19 | W34.1 | 315 | 313 | CLAIM | N4, N5 |
| C20 | W33.1 | 315 | 313 | CLAIM | O2, O8, O45, N1, N2, N7, N25 |
| C21 | W40.1 | 337 | 335 | CLAIM | N8, N22, N25 |
| C22 | W24.1 | 351 | 349 | WORDING | — |
| C23 | W22.1 | 373 | 371 | CLAIM | O27, O40, O50, N11 |
| C24 | W22.2 | 379 | 377 | CLAIM | O3, O27, O40, O50, N11 |
| C25 | W41.1 | 401 | 399–403 | CLAIM | O3, O11, O14, O15, O18, O23, O31, O32, N13, N15, N21 |
| C26 | W21.1 | 405 | 407 | CLAIM | O3, O11, O15, O18, O27, O31, N4, N10, N15, N21 |
| C27 | W13.1 | 419 | 421 | CLAIM | O30, O51 |
| C28 | W13.2 + W12.2 | 419 | 421 | CLAIM | O21, O27, O30, O40, O50, N11, N13, N15 |
| C29 | W35.3 | 421 | 423 | CLAIM | O12, O21, O27, O35, O40, O50, N18, N19 |
| C30 | W23.1 | 427 | 429 | CLAIM | O26, N10, N19 |
| C31 | W5.1 | 433 | 435 | CLAIM | O26, O35, N18, N19 |
| C32 | W23.2 | 445 | 447 | CLAIM | O32, N10 |
| C33 | W6.2 | 447 | 449 | CLAIM | O12, O35 |
| C34 | W6.3 | 447 | 449 | WORDING | — |
| C35 | W12.1 | 465 | 467 | CLAIM | O3, O14, O18, O21, O30, O31, O40, O50, O51, N11, N13, N15, N21 |
| C36 | W25.1 | 471 | 473 | CLAIM | N24 |
| C37 | W17.2 | 473 | 475 | CLAIM | O11, O48, N5 |
| C38 | W25.2 | 487 | 489 | CLAIM | N24 |
| C39 | W7.2 | 512 | 514 | CLAIM | O12 |
| C40 | W6.4 + W14.1 | 514 | 516 | CLAIM | O3, O6, O8, O12, O14, O18, O21, O26, O27, O30, O31, O32, O35, O40, O50, O51, N11, N23 |
| C41 | W7.3 | 516 | 518 | CLAIM | O3, O8, O10, O14, O18, O21, O30, O31, O51, N11, N13, N15, N21 |
| C42 | W7.4 | 518 | 520 | CLAIM | — |
| C43 | W7.5 | 518 | 520 | CLAIM | O35 |
| C44 | W15.1 | 526 | 528 | CLAIM | O12, O21, O27, O35, O48, O50 |
| C45 | W11.2 | 528 | 530 | CLAIM | O2, N17 |
| C46 | W17.3 | 562 | 564 | CLAIM | O48, N5 |
| C47 | W7.6 | 588 | 590 | CLAIM | — |
| C48 | W10a.1 | 616 | 618 | CLAIM | O48 |

## The cases in section 5

- **Which cases.** The pool is every case named in the CASES AT RISK field of the 48 entries. O53–O75 are read as the N-cases they will become under D8. N6 and N14 (set aside, D8) and D3-T (O76, not yet agreed) are not given.
- **The order they were added in.** Each case was ranked first by the number of entries with a sentence on it that speaks of a possible move: "toward", "away", "watched", "may move" or "could move", SPLIT, "→" or "risk", but not "no move is expected". It was ranked next by the number of entries that name it. Cases were added in that order while the brief stayed within 25,900 words by the runner's count. All 42 cases that have any such sentence fit. The first case left out was O49, which nine entries name and none speaks of moving.
- **Given (42).** O2, O3, O6, O8, O10, O11, O12, O14, O15, O18, O21, O23, O26, O27, O30, O31, O32, O35, O40, O45, O48, O50, O51; N1, N2, N3, N4, N5, N7, N8, N10, N11, N13, N15, N17, N18, N19, N21, N22, N23, N24, N25.
- **Named and not given (30).** O49, O13, O1, O24, O17, O20, O38, O39, O5, O36, O41, O52, O4, O7, O25, O33, O37, O42, O43, O44, N16, O19, O22, O34, O46, O47, N9, O28, N12, N20.
- **How they are given.** The O-cases are the S81 book's entries byte for byte, each with its title, situation and thoughtful person's verdict. The N-cases take their title, **Situation**, **Question(s)** and **Verdict** word for word from the S89 candidate book, with the verdict under the heading "Thoughtful person's verdict". Confidence and open notes are left out. Following the rule of the plan draft's section 3.3, words that only report how a verdict was agreed are cut, and each cut is marked […]. The cuts in the given cases are:
  - N4: "(R2 A1)"; "Both round-1 authors said the same, and the reconciled proposal expected this answer."
  - N5: "The authors differ only in emphasis. A2 calls the seasons reading "a sensible first guess". A1 says only an understanding from outside the rule could tell him to sow in April or May. Both agree that the rule alone cannot settle it." The verdict's finding, that the rule alone cannot tell him which reading to trust, stands in the sentence before the cut.
  - N17: "(A1)"; "Round 1 was disputed on the old wording: A1 said both explain, at different levels, and A2 said only B, as given. Round-1 A2 had already said that a full A "would be a real physical account ... an explanation of a sort", which is where round 2 lands."
  - N18: "Round 1 was disputed on Dov's surprise because the sketch did not say what Dov expected or knew. The rewrite supplies both."
  - N21: "Both round-1 authors leaned this way, and the reconciled proposal expected it."
  - N22: "This is the answer the reconciled proposal expected. Round 1 was disputed only on the old question, which asked whether either theorist had explained why people "seem" to have inner experiences."
  - N23: "(R2 A1, A2)".

## How the reply will be read

This rule was written and committed before the brief was sent.

1. **The reply is evidence, not a result.** Neither its OVERALL line nor its STANDS and FALLS lines settle anything by themselves.
2. **What is re-examined.** Every change the reply says FALLS is re-examined from the texts. So is every undeclared change of claim and every moved verdict the reply names, whatever line it gives that change, and whether or not it lists the change. The re-examiner is a fresh Claude checker, one that did not draft, assemble or check the change list. For each change the checker works in this order:
   - first, it states the change entry: its OLD, NEW, KIND and DECLARATION, and its checkers' verdict (the entry's CHECK field);
   - then, it states the reply's argument;
   - then, it rules: **keep** (the entry stands as drafted), **fix with new wording** (the exact new OLD or NEW, KIND or DECLARATION, with the reason), or **drop**.
3. **Every resulting edit is made in the change list.** It goes in the entry itself, with its reason and the note that it came after the cross-examination, and in the list of what the checks changed. The counts, the note's N and M, and the record follow by program when the draft is rebuilt. A ruling of keep is recorded in the entry's CHECK field.
4. **A failed call supports nothing.** A reply the runner does not accept (it must finish "stop" with END OF REPORT on its last line) counts neither for nor against any change. Its attempt files are kept and not read for arguments. The call is not rerun without a new note written before sending.
5. **Silence is not support.** A change the reply does not list is not thereby confirmed.
6. **The three held repairs are cross-examined separately, later**, once drafted: Derivation 2 (W19), (T2) (W31), and non-circular dependence with the typing of Γ (W20). A point the reply makes about them is passed on to that cross-examination and is not ruled here, unless it bears on one of the 48 changes.
7. **Fixed verdicts are not in question.** A point that disputes a fixed verdict is noted and not ruled here.
8. **Quotations are checked.** Each quotation the reply relies on is checked against the revised text or the old wording. Where one is not found, that is recorded, and the point is ruled on what the texts say.

Dated 23 September 2026.
