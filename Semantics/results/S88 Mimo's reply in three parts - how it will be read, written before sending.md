# S88: Mimo's reply in three parts, and how it will be read

*Written by a Claude subagent for the orchestrator on 23 September 2026, from 17:46 UTC, before any part was sent. When it was written, the folder `results/S88 Cross-examination - three defects - returns/Mimo in three parts/` did not exist.*

## Why three parts

Mimo's single call on the S88 brief, `s88_xexam_mimo`, failed. The only sources for this are its receipt and error file, committed at 48236c7. Its reasoning files were not opened.

- **Three attempts came back, and none was accepted.** After three rejected returns the runner stopped, because that call's limit was 3 (`max_rejects` 3 of 6 attempts). Every attempt was sent with max_tokens 131,072 and returned status 200, and none wrote any reply text (`content_chars` 0).

| attempt | seconds | finish | why it was rejected |
|---|---|---|---|
| 1 | 2,674.8 | "length" | it ran to the 131,072-token limit |
| 2 | 2,266.6 | "length" | it ran to the 131,072-token limit |
| 3 | 1,397.0 | none | the stream ended with no finish reason and no reply |

- **Correction to the brief for this note.** It said "three attempts ran to 131,072 tokens". Only attempts 1 and 2 did. Attempt 3 ended earlier: its reasoning file is about half the size of the other two.
- **Under R1 of the S88 rule, the failed call supports nothing.** It counts for and against no finding, and its attempt files are kept and not read for arguments.

At medium effort, Mimo's reasoning on the full S88 task used up the 131,072-token ceiling, or stopped, before any reply was written. The S81 audit of tester A failed in the same way, and the fix there was to split the task. There, two of the four parts came back with a reply (parts 3 and 4) and two failed (parts 1 and 2), so splitting is no guarantee. Each call here carries a smaller task:

- **one finding instead of three.** Each part asks two things of its finding: try to refute it, and judge its repair. The full brief asked those two things for each of three findings and then asked for a hunt for further counterexamples.
- **No hunt.** Atria's reply already did the hunt, and its items were read under R4 in `results/S88 Reading of Atria's reply - the three defects.md`. The hunt adds reasoning load.

## The three texts

| part | tag | brief, in `tests/` | words | sha256 (first 12) |
|---|---|---|---|---|
| F1 | `s88_xexam_mimo_F1` | `S88 Cross-examination - part F1, Derivation 2.md` | 10,307 | 45e210160953 |
| F2 | `s88_xexam_mimo_F2` | `S88 Cross-examination - part F2, (T2).md` | 9,721 | 9c24e62f7ef1 |
| F3 | `s88_xexam_mimo_F3` | `S88 Cross-examination - part F3, non-circular dependence.md` | 10,422 | 370ba7cb2f64 |

Each part is built from the committed S88 brief. That brief's sha256 is 8485bb425b21…, the `user_sha256` of both the failed Mimo call and Atria's accepted call. It has 13,510 words. Each part differs from it only as follows.

- **The theory text is kept byte for byte.** It is the text between the BEGIN THEORY TEXT and END THEORY TEXT lines, md5 3a8cd7c8ca6f3ad3b8a85ab9984d850e in the brief and in all three parts. Theory line numbers are therefore unchanged.
- **Only that part's finding section is kept, byte for byte.** It keeps its counter-instances, the arguments in the theory's defence with the replies, and the proposed repair. For F3, option A is kept too.
- **Only the predecessor passage the finding needs is kept (from file 00).** F2 keeps passage 1 (approximate transport) and F3 keeps passage 2 (non-circular dependence). F1 cites neither, so it keeps neither. The heading and the sentence that introduces the passage are put in the singular.
- **Only the notation that the finding uses is kept.** F1 keeps the sentence on \(\mathrm{do}(x{=}c)\), F3 keeps the sentence naming S1, S2 and S3, and F2 keeps neither.
- **The introduction changes in three sentences.**
  - The job sentence now says the text carries only that finding, with the other two examined in separate texts. It drops "and to look independently for further defects of the same kind".
  - The layout sentence speaks of one finding.
  - The sentence on predecessor passages is put in the singular, or dropped for F1.
  - The list of the three findings is kept, as is the rest of the introduction.
- **The tasks section is replaced.** It asks the reader to:
  - try to refute the finding (the full brief's task 1, reworded for one finding);
  - judge the proposed repair (the full brief's task 2, with the same checklist, plus O33 and O5 for F3);
  - number the points, most serious first;
  - close with one verdict line (F<n>: UPHELD, F<n>: PARTLY UPHELD or F<n>: REFUTED), with the full brief's definitions of the three verdicts;
  - keep the reply under about 3,000 words, where the full brief allowed about 6,000 for four sections;
  - end with END OF REPORT.
- **No part names any model.**

## The parts carry the wordings sent to Atria

Each part's finding and repair are word for word as sent to Atria in the S88 brief. Since then, Atria's reading has changed some of them:

- F1's repair premise was tightened, and its conclusion was qualified;
- F2's erratum gained a scope clause;
- F3 was narrowed, and option B was reworded.

**So a reply may argue against wording that has since been tightened.**

The briefs were left as sent so that Mimo is asked the same question Atria was asked. Rebuilding them with the later wordings would make the text Mimo tests depend on Atria's reply.

The reader handles such an argument in this order:

1. The reader checks the argument against the wording the part carries, as R3 requires.
2. The reader then says whether the argument also holds against the current wording below.
3. If the argument bears only on wording that has already changed, it is recorded as that. It neither reopens the change nor counts as support for it.

## How each part's reply will be read

Each part's reply is read under the rule committed at cc87b45: `results/S88 How the cross-examination will be read - written after Atria's reply arrived, before it was opened.md`. The rule is applied part by part, as follows.

- **R1. The receipt comes first.** A part is read only if its receipt shows finish "stop" and its reply's last line is END OF REPORT. **A failed part supports nothing:**
  - its finding is reported as "not examined by Mimo";
  - its attempt files are kept and not read for arguments;
  - it counts neither for nor against the finding or the repair.
- **R2. The verdict line is evidence, not a result.** Only an argument that survives R3's check changes anything.
- **R3. A fresh reader takes the four steps for that part's one finding.** The steps are the current position, the reply's argument, the check against the theory text, and the ruling: UPHELD, NARROWED or WITHDRAWN. The theory text is the one between the part's marker lines, which is byte for byte the S88 brief's and file 10's.
- **R4. Any further counterexample is checked.** The parts ask for no further counterexamples. If a reply offers one anyway, it is checked the same way. It is added as a new finding if it holds, or recorded as not holding.
- **R5. Each part is read on its own.** Each part's reply is read without Atria's reply and without the other parts. The reader of a part does not open:
  - Atria's reply or its reasoning;
  - `S88 Reading of Atria's reply - the three defects.md`;
  - the other parts' replies or their readings.
  The readings are put side by side, with Atria's reading and with each other, only after all of them are written. Where two readings rule differently on one finding, both rulings are recorded, and the difference is resolved in writing from the theory text.
- **R6. Changes to the repairs are recorded with their reasons.** Each change names the part that prompted it, and records that it came after this cross-examination.
- **R7. The rule was not late for these parts.** It was committed at 15:36 UTC, and no part has been sent. So R7's late-rule statement does not go with these readings.

### The positions each reader starts from: a change to R3 and R5

As committed, R3 step 1 and R5 have every reader start from the positions frozen in the rule at 15:35 UTC. R5 also requires that Mimo's reader has read "neither Atria's reply nor its reading". **This note changes that for the three parts.** Each part's reader starts from Claude's current positions, which are the positions after Atria's reading and are set out below. The change is recorded here, before any part is sent, and is dated from now (lesson S2).

- **Why.** A ruling on a part should test what Claude now holds. Positions frozen at 15:35 are no longer held in their frozen form.
- **What it costs.** The reader learns where the positions moved, and so learns in outline what Atria's reading concluded. R5's independence is kept only in a narrower sense: the reader sees these positions as conclusions, and does not see Atria's arguments or the reading's checks.
- **What it costs later.** When the readings are put side by side, Atria's reading will have started from the frozen positions and these readings from the revised ones. The comparison must say so.

The current positions, which the reader copies into step 1:

- **F1: UPHELD.** The component half of Derivation 2 is false under its stated assumptions, and the answer-profile half is true. The repair is "Same anchors, one account", a recorded change of claim, with the premise tightened and the conclusion qualified:

  > **Claim.** Let ℰ, ℰ′ be candidates for the same p that both satisfy (F1), (F2) and (A) on C. (i) Their answer profiles coincide on C. (ii) If a bijection φ of their active components gives each k and φ(k) one anchor, the same subnetwork of D with port translations onto the same ports of D, then k and φ(k) are of one kind on C for every k; so far as (F1), (F2) and (A) reach, the two are one account on C.

  The sentence "Without the premise of (ii) nothing more follows …", the Consequence, the sentence after (K) and the Derivation 10 wording are as in the part's brief. The smaller alternative wording is not adopted as it stands.
- **F2: UPHELD.** (T2) omits h1 to h3, and this is a drafting omission, fixed by an erratum. The erratum now carries the scope clause:

  > **Approximate transport.** With one-step discrepancy d(πSz, Tπz) ≤ ε at every state z of the stated scope and an L-Lipschitz represented next-step map T, the discrepancy after n steps from one state z, e_n = d(πSⁿz, Tⁿπz) (so e₀ = 0), satisfies e_n ≤ ε Σ_{k<n} L^k whenever z, Sz, …, S^{n−1}z lie in that scope. (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

  The unequal-start clause stays optional.
- **F3: NARROWED.** The finding now reads: "Γ in non-circular dependence is untyped. On the mechanism-only reading R-τ-mech, O5's fixed verdict flips on a narrowed contract with no edit that removes a mechanism commitment, and Part VII's forward organization fails S3 on its production contract. O33's fixed verdict does not flip. Of the brief's two repairs, option B is preferred over option A." Option B is still a change of claim, and it now names the translation:

  > "There exist (a,b) ∈ C and a nonempty block G ⊆ Γ such that the answer profile at (a,b) differs from its value at (1,b₀), or is not determined there in the claimed way, and in E|(Γ∖G), evaluated at (τ(a),σ(b)) and at (1,σ(b₀)) with the named background fixed, that difference is lost or the answer ceases to be determined."

  Line 246 gains a sentence that types Γ: "The commitments Γ are components of E; the boundary values of E belong to the named background of Part VI." Option A is unchanged, as the alternative.

Atria's reading also added F4, on file 10's Derivation 3. No part puts F4 to Mimo, so these readings say nothing about it.

## Confounds, stated before the data

- **Each part is a different call from the single call.** Each part sees the whole theory but only one finding. It cannot draw on work done on the other findings, and it is not asked to hunt for further counterexamples.
- **Word limits.** Each part allows about 3,000 words for one finding. The single call allowed about 6,000 words for three findings and a hunt.
- **Selection by the ceiling.** A part is accepted only if its reasoning fits within 131,072 tokens. The accepted parts are the runs that happened to fit.
- **Wording since tightened.** See the section above on the wordings sent to Atria.
- **Timing and order.** The parts are sent after Atria's reply and its reading. Mimo does not see either.

## Settings

- **The call.** Thinking is on, with `reasoning_effort` medium, from `s80_common.effort_for("audit", "mimo")` under decision S17. max_tokens is 131,072 on both rungs ([131072, 131072], Mimo's ceiling), and the temperature is 0.7. There is no system message: the part's text is the one user message.
- **Attempts.** Each part may make up to 6 attempts, and at most 3 of them may come back and fail. Each part goes one pass only (`max_pass` 1), so a part that fails is never sent again.
- **Acceptance.** A part is accepted only if it finishes with "stop" and the last line of its reply is END OF REPORT.
- **Runner.** The parts are sent by `tools/s87_run.py` with `tools/s88_jobs - Mimo in three parts.json` (sha256 8ccde401cdeb…). At most three Mimo calls are in flight across every process, through the shared slot lock. The returns go to `results/S88 Cross-examination - three defects - returns/Mimo in three parts/`, and their file names follow `tools/s80_call.py`.
- **Dry run.** The runner's dry run on this job list shows all three parts to go as pass 1 of at most 1, with no files already in place.

## Who decided, and when

Claude decided this under decision S18 on 23 September 2026. The decision came after two things: the single call's failure, known only from its receipt and error file (finish reasons, token limits, times and file sizes), and Atria's reading. It came before any part was sent. No reply text from Mimo existed to be read, and the failed call's reasoning was not opened.

## Files

- `tests/S88 Cross-examination - part F1, Derivation 2.md`, `… part F2, (T2).md` and `… part F3, non-circular dependence.md`: the three texts, exactly as they will be sent.
- `tools/s88_jobs - Mimo in three parts.json`: the job list. For each part it gives provider mimo, effort medium, ladder [131072, 131072], 6 attempts, at most 3 rejected and `max_pass` 1.
- `results/S88 Cross-examination - three defects - returns/Mimo in three parts/`: written by the runner when the parts are sent.
