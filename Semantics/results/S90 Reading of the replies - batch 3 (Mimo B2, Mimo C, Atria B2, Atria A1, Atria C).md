# S90: reading of the replies, batch 3 (Mimo B2, Mimo C, Atria B2, Atria A1, Atria C)

*Written on 24 September 2026 by a Claude subagent for the orchestrator, from about 03:00 UTC. It records the rulings of fresh Claude checkers on the changes that these five replies contest. With it, all ten S90 part calls (five parts, two models) have been read. The recorder wrote no ruling and did not draft, assemble or check the change list. In two places, two checkers in this batch ruled one entry differently: R13 (two FIX rulings in different words) and R25 (KEEP against FIX). There the recorder sets the two rulings side by side and records, from their own grounds, which text the pass uses (section "Reconciliation"). The recorder read the five replies named here and their receipts, the readings of batches 1 and 2, and every ruling file of all three batches. For the coverage table it also read the closing lines of the five replies read in batches 1 and 2. It opened no reasoning file and no attempt file, and it did not edit the change list. The edits are listed at the end, together with those of batches 1 and 2, to be made in one pass. Nothing was written into `authority/`.*

## The five calls, and the restart

- **These five calls were among the seven cut by the container restart** at about 23:30 UTC on 23 September. They were sent again as pass 2 at 23:45:32 under `results/S90 and S87 - seven calls rerun after the container restart - written before sending.md` (57482a5, faf91f6). Each went with the same brief bytes and settings as pass 1.
- **All five were accepted in pass 2.** The replies, receipts, requests and attempt files were committed as returned at 286d69c (01:58:22 UTC on 24 September).
- **The requests.** For each call, the pass-2 request is byte-identical to its pass-1 request, and its sha256 equals the receipt's `request_sha256`, as the rerun note expected. Each receipt's `user_sha256` is the sha256 of its part brief: A1 8e7b98f33710…, B2 55d498b3fcee…, C a94c8ef9ead3….
- **Rejected replies.**
  - Atria A1 had two in pass 2: attempts 3 and 4, each status 200, finish "length", with no content. Their files `s90_xexam_atria_A1.pass2.a3.*` and `.pass2.a4.*` are kept and were not opened. Two rejects are within `max_rejects` 3.
  - Mimo B2's two pass-1 rejected replies (`content_filter`, 60 characters; `length` with no content) stay on the record with pass 1 and were not read (rerun note, ruling 3). Pass 2 added none. So Mimo B2 had two rejected replies across the two passes, not the five the rerun note allowed for.
  - The other three calls had no rejected reply in pass 2.
- **Rerun note, ruling 4:** each pass-2 reply stands where the pass-1 reply would have stood, and it is read by the S90 rule and the S90 Parts rule.

| call | pass-2 attempts | accepted | seconds, pass 2 | ended (UTC, 24 Sep) | words (`wc -w`) | reasoning / completion tokens (ceiling) | response sha256 (matches receipt) |
|---|---|---|---|---|---|---|---|
| s90_xexam_mimo_B2 | 1 | attempt 1 | 2,066.3 | 00:19:58 | 805 | 79,970 / 81,425 (131,072) | bbee0da8… |
| s90_xexam_mimo_C | 1 | attempt 1 | 2,150.3 | 00:21:22 | 1,321 | 97,236 / 99,280 (131,072) | 9ea0342f… |
| s90_xexam_atria_B2 | 4: 1–3 status 0 | attempt 4 | 5,502.7 | 01:17:14 | 1,375 | 50,051 / 52,079 (65,536) | f965836a… |
| s90_xexam_atria_A1 | 5: 1–2 status 0; 3–4 rejected ("length", no content) | attempt 5 | 6,049.9 | 01:26:21 | 1,103 | 52,573 / 54,285 (65,536) | 3a6d3413… |
| s90_xexam_atria_C | 6: 1–5 status 0 | attempt 6 | 6,410.3 | 01:32:22 | 1,227 | 59,583 / 61,482 (65,536) | bd51b785… |

Each accepted attempt returned status 200, finish "stop" and 0 bad chunks, with END OF REPORT on the reply's last line.

## The rule followed

- **The rule** is the one batches 1 and 2 followed: `results/S90 How the cross-examination of the revision 2 draft will be read - written before sending.md`, as extended by `results/S90 Parts - how they will be read, written before sending.md`, with the rerun note for these five calls.
  - **Each reply is read on its own** (Parts rule 1).
  - **What counts as contested** (Parts rule 2). A change is contested when the reply says it FALLS, or when the reply names an undeclared change of claim or a moved verdict on it, whatever closing line it gives the change.
  - **Who rules** (Parts rule 3). Each contested change went to a fresh Claude checker, one that did not draft, assemble or check the change list and did not write the part briefs. Each checker stated the entry and its checkers' verdict, then each reply's argument, and then ruled keep, fix (with exact new wording) or drop.
  - **Edits are recorded as made after the cross-examination** (Parts rule 4). A keep goes in the entry's CHECK field.
  - **Silence is not support** (S90 rule 5). **Quotations are checked** (S90 rule 8). Each ruling records its own checks.
- **Reconciliation.**
  - With batches 1 and 2, where an entry was already ruled there. Only R01 was.
  - Within this batch, where two checkers ruled one entry. That happened for R31, R30, R13 and R25.
- **Ids.** R01–R55 map to entry ids through the table in the Parts note.
- **Sources**, the same for every ruling and the same as in batches 1 and 2:
  - the change list `tests/Revision 2 - change list, draft of 23 September.md` as of 587eebf (md5 a5c92adc9f1e3806c0f9c6394cffde1e, unchanged at HEAD);
  - the revised text `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md` (md5 9aecf2f30ce0b4523606b2b8409fdf37);
  - file 11, `authority/11 … revision 1.md` (md5 5e494c1095d920d128b9a79de378f923), read only;
  - the S81 case book (md5 4f488d149e44669240d5db546c8e946a), the S89 case book (md5 b2e535777976a511935430bd089ba500) and D3-T's `final.md`;
  - batch 1's reading (md5 56219a1d3bf20e22ea241cb18ff8a426) and batch 2's (md5 4579cec0541b1af1f4757c783e05f1cb).
- **The rulings** are copied byte for byte into `results/S90 reading rulings/`, one file per ruling, and each file's md5 is given below.
  - Several rulings record that the file name their task asked for was over the 255-byte limit. They used the short form of the committed rulings.
  - The five Mimo C rulings were written in the scratch folder under names that carry the whole call description ("ruling s90_xexam_mimo_C (part C, Mimo). Pass 2, attempt 1 of 1: … item N Rnn.md"). They are copied here under the short form "ruling s90_xexam_mimo_C item N Rnn.md".
  - The R24 ruling cites a brute-force check it ran, the scratch file `fin/r24_check.py`. It is copied as `ruling s90_xexam_atria_C item 4 R24 - check script.py` (md5 2a2d4e7bacf57bc221345edbfd18a9e1). Run again for this reading, it prints the ruling's counts: 16 families pass the test, and both consequences hold in all 16; in 65 families \(\{d\}\) is critical in no support while the test fails; and 0 families meet the E-standing form without passing the test.

## Summary

| call | accepted | OVERALL line | closing lines | contested, and why | rulings |
|---|---|---|---|---|---|
| s90_xexam_mimo_B2 (part B2) | yes, pass 2, attempt 1 of 1 | OVERALL: NEEDS REPAIR | R31 FALLS (two lines); R11, R22, R32, R33, R35, R36, R37, R40, R42, R52 STANDS | R31 (FALLS, point 1); R52 (point 2: the declaration does not say that "realizable" is dropped) | R31 KEEP; R52 KEEP |
| s90_xexam_mimo_C (part C) | yes, pass 2, attempt 1 of 1 | OVERALL: NEEDS REPAIR | R07, R12, R30 FALLS; R06, R13, R14, R21, R23, R24, R25, R34 STANDS | R12 (FALLS, point 1); R07 (FALLS, point 2); R30 (FALLS, point 3); R13 (point 4: an undeclared opening clause); R25 (point 5: an undeclared description of a bare denial) | R12 FIX; R07 KEEP; R30 KEEP; R13 FIX; R25 KEEP |
| s90_xexam_atria_B2 (part B2) | yes, pass 2, attempt 4 of 4 | OVERALL: SOUND | all 11 STANDS | R42 (point 1: moves toward on O24 and N5); R31 (point 3: moves toward on O11, O18, O31, N15 and N21); R32 and R33 (point 5: listed as not clearly contested) | R42 KEEP; R31 KEEP; R32 KEEP; R33 KEEP |
| s90_xexam_atria_A1 (part A1) | yes, pass 2, attempt 5 of 5 | OVERALL: NEEDS REPAIR | R01 FALLS; R05, R08, R09, R15, R16, R17, R19, R20 STANDS | R01 (FALLS, point 1); R17 (point 2: a move toward on O33) | R01 FIX; R17 KEEP |
| s90_xexam_atria_C (part C) | yes, pass 2, attempt 6 of 6 | OVERALL: NEEDS REPAIR | R13 FALLS; R06, R07, R12, R14, R21, R23, R24, R25, R30, R34 STANDS | R13 (FALLS, point 1); under point 3 (d), moves toward on R06 (N3), R21 (O45), R24 (N1), R25 (N22), R30 (N21, O15) and R34 (N19) | R13 FIX; R06 KEEP; R21 KEEP; R24 KEEP; R25 FIX; R30 KEEP; R34 KEEP |

**Totals, this batch.** There are 20 rulings on 16 entries, from 19 ruling files (one file rules R32 and R33 together): KEEP 15, FIX 5, DROP 0.
- **Four entries were ruled twice in this batch**, each once for each model's reply to the same part:
  - R31: KEEP and KEEP, joined in one CHECK append;
  - R30: KEEP and KEEP, joined in one CHECK append;
  - R13: FIX and FIX, in different words, reconciled to one text;
  - R25: KEEP and FIX, reconciled to the FIX.
- **After reconciliation**, 4 entries are fixed and 12 kept.
  - **Fixed (4):** W37.1 (R01), W35.1 (R12), W35.2 (R13) and W40.1 (R25). W37.1 was already fixed in batch 1, with the same text.
  - **Kept (12):** W21.1 (R31), W17.3 (R52), W45.1 (R07), W41.1 (R30), W17.2 (R42), W13.1 (R32), W13.2 + W12.2 (R33), W20.2 (R17), W36.1 (R06), W58(i).1 (R21), W33.1 (R24) and W35.3 (R34).
  - **Dropped:** none.

**Totals, batches 1–3.** There are 32 rulings on 24 entries: KEEP 19, FIX 13, DROP 0.
- **Entries fixed (10):** W37.1 (R01), W19.1 (R08), W20.1 (R15), W24.1 (R26), W22.1 (R28), W6.3 (R39), W7.5 (R48), W35.1 (R12), W35.2 (R13) and W40.1 (R25).
- **Entries kept (14):** W19.2 (R51), W58(ii).1 (R04), and the 12 above.
- **Entries dropped:** none.
- **No KIND changes in this batch.** R12, R13 and R25 stay CLAIM, and R01 stays ORDER. The counts after the pass are therefore those batch 1 gave for W6.3: CLAIM 49, WORDING 4, ORDER 2, and N = 49 of M = 55.

**Changes a reply says FALLS, in this batch:**
- **R31 (Mimo B2):** not upheld. KEEP. The reply's repair would change the claim.
- **R07 and R30 (Mimo C):** not upheld. KEEP.
- **R12 (Mimo C):** upheld on the typing point. It is repaired with the reply's first repair, naming the target. The \(\operatorname{Ans}_E\) alternative is refused.
- **R13 (Atria C):** upheld. It is repaired with the reply's first repair, "into the simulation layer", in the form "to the simulation layer" that R12's fix uses.
- **R01 (Atria A1):** upheld. It is repaired with the reply's first repair (delete "blind"), which is batch 1's FIX. The second repair, adding blindness to Part IV, is refused.

## Mimo, part B2 (s90_xexam_mimo_B2)

**The call is accepted.** It was accepted in pass 2, at attempt 1 of 1: status 200, finish "stop", 0 bad chunks. The response's sha256, bbee0da8…, matches the receipt. The last line is END OF REPORT. The reply is 805 words by `wc -w`. Pass 1 had two replies that came back and were rejected, first on `content_filter` and then on `length` with no content. They are recorded with pass 1 and were not read.

**OVERALL:** `OVERALL: NEEDS REPAIR`

**Unexamined changes:** none. All 11 changes of the part (R11, R22, R31, R32, R33, R35, R36, R37, R40, R42, R52) have a closing line.
- **One irregularity.** R31 has two FALLS lines.
  - The first comes right after the points: `R31: FALLS — definition of ≡_ℓ applies \(c\)'s contract to a transport from \(d\) to \(c\), where Part V's (F1) requires the source's edits; the relation is non-symmetric despite ≡ notation.`
  - The second is in the list: `R31: FALLS — definition of ≡_ℓ ill-typed and non-symmetric.`
- The reply names no case.

### R31 (W21.1), point 1: KEEP (one ruling with Atria B2's, below)

- **Why contested.** The reply says FALLS (tasks (a) and (c)).
- **The entry.** W21.1, "L405: ≡_ℓ is defined, and 00:746's first sentence is restored". Part X, **Newness**, file-11 L405, revised L407. KIND CLAIM. REASON WORD clarification. CHECK: "check 1, SOUND".
- **The reply.** (F1) checks fidelity on the source's edits, because \(\lambda(k)\) is a subnetwork of the source. So "both faithful on \(c\)'s contract" is ill-typed for the transport from d to c. The relation \(\equiv_\ell\) is not symmetric, though it is written \(\equiv\) and called "the equivalence", so the declaration's "The equivalence is structural at that grain" misleads. Its repair: "each faithful on the contract of its source at grain \(\ell\)", with the declaration reworded to match.
- **The checker.**
  - **Typing.** The transport from d to c is judged on c's contract as (R) judges a transport into c (L205–208). (R) is file-11 text that none of the 55 changes touches, and Deploy, and so (N)'s repertoire, already rest on it. The transport from c to d is typed as in Part V. Both are checked on the changes c commits to.
  - **The reply's "(R) at line 166–67" is wrong.** Those words are at revised L205.
  - **Symmetry.** The reply is right that the relation is not symmetric, but that is harmless. \(\equiv_\ell\) occurs only at L407 and in (N) at L410, and nothing uses symmetry. "Equivalence" is the file's own two-direction sense (L357).
  - **The declaration** states the definition word for word, so it does not mislead.
  - **The repair is refused.** "Each faithful on the contract of its source" would make c new whenever an earlier content commits beyond c. That changes the claim, goes against plan row W21, and could reopen N4 in the away direction.
  - **Cases.** The reply names none, and no verdict moves under NEW.
- **Text:** none changes. OLD, NEW, KIND CLAIM and DECLARATION stay byte for byte.
- **CHECK.** The checker drafted this append:

````text
After the cross-examination (s90_xexam_mimo_B2, point 1, R31 FALLS: 'ill-typed and non-symmetric'): KEEP.
- The transport from d to c is judged on c's contract as (R) judges a transport into c (L205–208, file-11 text unchanged, on which Deploy and so (N)'s repertoire rest). The transport from c to d is typed as in Part V. Both are checked on the changes c commits to.
- The relation is taken on the contract of the content whose newness is in question. (N) is its only use, and nothing uses symmetry. 'Equivalence' is the file's two-direction sense (L357).
- The declaration states the definition word for word.
- The proposed 'each faithful on the contract of its source' would make c new whenever an earlier content commits beyond c. That is a change of claim, against plan row W21, and it could reopen N4.
- Atria (s90_xexam_atria_B2, point 3) found the entry standing, on the same typing.
````

- It is replaced by the one reconciled append that the Atria B2 checker wrote, given under Atria B2, R31. That append contains this ruling's text word for word.
- **Noted for the owner, not ruled.** A sentence at Part IV (L189) or at (R) (L205–208) could say that a transport into c is faithful on c's contract when it is faithful on the pairs it carries into that contract. That would state in words the reading the file already needs. It concerns file-11 text outside the 55 changes.
- **Earlier rulings:** batches 1 and 2 have none on this entry.
- **Ruling file:** `ruling s90_xexam_mimo_B2 item 1 R31.md` (md5 405d2e895ce435b914beda407b45ca94).

### R52 (W17.3), point 2: KEEP

- **Why contested.** The reply's line is STANDS. Its point 2 (task (a)) says the change is under-declared. The old four-item list becomes two conditions, and "realizable" has no counterpart. The declaration shows both lists but does not say that "realizable" is dropped. If "realizable" was a real physical condition (the reply suggests a retained realization in the sense of (CT1)), dropping it weakens Derivation 3's hypothesis. The reply says the point "does not survive as a fatal defect", and it offers to append "—the separate realizability condition is dropped" to the declaration.
- **The entry.** W17.3, "L562 s3: Derivation 3's condition in the two defined terms". Part XVI, file-11 L562 s3, revised L566. KIND CLAIM. CHECK: "check 1, SOUND. CLAIM is defensible; a checker may rule it WORDING, given W17.1 and L473."
- **The checker.**
  - **Membership already implies "realizable" in both texts.** In file 11, L473 calls the population "realized transports". In the revised text, L475 makes a member a transport "the physics and the stated construction admit", and Part XII calls that physically possible, which is what "realizable" means. So dropping the word removes no condition from Derivation 3, and the declaration, which quotes both lists, is accurate.
  - **Mimo's count is right.** Four conditions do come down to two. All its quotations were found.
  - **The (CT1) reading fails.** (CT1) applies to a protocol for a task, not to a member of a population. A realized-only reading would also contradict Derivation 3's own proof (L568) and its Consequence (L570), which use alternatives that were never built. The change from realized to candidate is R42's, and R42 declares it.
  - **The proposed fix is not taken.** It would declare a weakening that the new text does not make.
  - **Cases.** The reply names none. O24, O48, N5 and D3-T were worked, and no verdict moves. Neither case book uses "realiz" or "realis".
- **Text:** none changes. OLD, NEW, KIND (CLAIM) and DECLARATION stay as drafted. Whether W17.3 should be WORDING was not raised, and it is not ruled.
- **CHECK (append, exact):**

````text
After the cross-examination (S90, Mimo B2, point 2, R52 STANDS): the claim that the declaration does not say whether "realizable" is dropped was re-examined and ruled KEEP. "Realizable" is entailed by membership in both texts: file 11's population is of realized transports (L473 s1), and the revised text's population is what the physics and the stated construction admit (L475), which is physical possibility in Part XII's sense (Tasks) together with the construction. No condition of Derivation 3 is lost, and the declaration shows both lists. The reply's suggested addition ("the separate realizability condition is dropped") is not taken, because it would declare a weakening the new text does not make. (CT1) is typed on protocols and tasks, not on population members, and the realized-only reading belongs to W17.2, which declares it.
````

- **Earlier rulings:** none on this entry. Batch 2 and the R51 ruling files cite Derivation 3 "(L566, W17.3)" as unchanged support for O24, and that agrees with this KEEP. Atria B2 (point 2) found that dropping "realizable" loses nothing. It did not contest R52.
- **Ruling file:** `ruling s90_xexam_mimo_B2 item 2 R52.md` (md5 c8cc0df57aad3a91f65d8cf64a1e53ab).

## Mimo, part C (s90_xexam_mimo_C)

**The call is accepted.** It was accepted in pass 2, at attempt 1 of 1: status 200, finish "stop", 0 bad chunks. The response's sha256, 9ea0342f…, matches the receipt. The last line is END OF REPORT. The reply is 1,321 words by `wc -w`. Pass 1's attempt 1 ended with no reply after 1,364.6 s. Every later attempt of pass 1 was refused by the dead proxy.

**OVERALL:** `OVERALL: NEEDS REPAIR`

**Unexamined changes:** none. All 11 changes of the part (R06, R07, R12, R13, R14, R21, R23, R24, R25, R30, R34) have a closing line. The reply names no case.

### R12 (W35.1), point 1: FIX

- **Why contested.** The reply says FALLS (tasks (a) and (c)).
- **The entry.** W35.1, "Part IV: expectation and violation for every transport; surprise kept for selected ones". File-11 L219–223, revised L217–221. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, SOUND. …" The drafter's REASON reads: "The expectation keeps \(\operatorname{Ans}_S\): S is the organization the transport serves in this section".
- **The reply.** The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) type-checks only when the transport's target is the simulation layer \(S\): \(\tau(a)\) is an edit of the target \(E\), and \(\operatorname{Ans}_S\) is defined on S's edits. So the declaration's "defines expectation and violation for every transport" is false for expectation, though true for violation. The new preamble drops the old implicit restriction without adjusting the definition. Its repairs: restrict the declaration to "every transport to the simulation layer", or change the expectation to \(\operatorname{Ans}_E(\tau(a),\sigma(b))\).
- **The other reply to part C.** Atria C makes the same typing point, but it puts the FALLS on R13 and says R12 stands, adding "the same repair must touch it".
- **The checker.**
  - **The typing point is right.** \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) names nothing for (R)'s carrier-to-content transports (L208) or for the transports of Part V candidates (L231).
  - **What R12 adds.** File 11 left the target to context and had the same latent gap. R12 drops "selected" and its declaration states the universal outright. The drafter's own REASON already says the transports here are the ones that serve \(S\).
  - **\(\operatorname{Ans}_E\) is not adopted.** A general \(E\) supplies no query, and unchanged L177 says "\(S\) is where expectation lives".
  - **Scoping only the expectation bullet is not adopted.** It would leave surprise defined for transports with no expectation, against Derivation 4's proof (L576).
  - **Quotations.** All are found. Mimo places the transport definition at "line 203", but it is at revised L183. "The selected \(P\)-to-\(S\) transport" is not in file 11; it is the reply's reading of the context.
  - **Cases.** N18 and O3 hold. O11, O48, O5, O24 and D3-T are not reached.
- **OLD:** unchanged (file-11 L219–223).
- **NEW (exact):**

````text
Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation of a selected transport at \((a,b)\notin H\).
````

- **KIND:** CLAIM, unchanged. **REASON WORD:** clarification, unchanged.
- **DECLARATION (exact):**

````text
Part IV now defines expectation and violation for every transport to the simulation layer, whatever its provenance, and keeps surprise for a violation of a selected one at a pair outside its history.
````

- **CHECK and the list of what the checks changed (exact):**

````text
S90, Mimo part C, R12 FALLS (Atria part C makes the same typing point but rules R12 STANDS and R13 FALLS); fresh checker FIX after the cross-examination. The preamble reads 'a transport to the simulation layer \(S\), with contract \(C\)', since \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only when \(t\)'s target is \(S\). The declaration reads 'for every transport to the simulation layer, whatever its provenance'. The \(\operatorname{Ans}_E\) alternative is not adopted: a general \(E\) supplies no query, and L177 keeps expectation at \(S\).
````

- **What is lost:** the unscoped "for every transport", which was false for expectation.
- **Conflicts.** W35.2 (R13) must follow this fix; see R13 and the Reconciliation section. W35.4 (R14) and W35.3 (R34) are unaffected. No other entry has an OLD in L219–223.
- **Earlier rulings:** none on R12, W35.1 or C11.
- **Ruling file:** `ruling s90_xexam_mimo_C item 1 R12.md` (md5 670a4e95a95fd4148de0b1fa2f5db289).

### R07 (W45.1), point 2: KEEP

- **Why contested.** The reply says FALLS (task (a)).
- **The entry.** W45.1, "Part I: substrate independence holds relative to the physics' interoperability". File-11 L77, revised L75. KIND CLAIM. REASON WORD change of claim. CHECK: "check 2, FIX". Check 2 changed only the wording ("kind of carrier" became "physical medium").
- **The reply.** The new L75 makes three claims, and the declaration covers two of them: that substrate independence holds only so far as the physics lets contents pass, and the barrier. It leaves out the claim that which organizations a carrier can bear, and whether contents pass between media, are "fixed by the adopted physics". The reply says that is stronger than the unchanged, one-sided "must be permitted by the adopted physics". Its repair: add that clause to the declaration.
- **The checker.**
  - **The reply file.** The file named in the task does not exist. The reply is `parts/s90_xexam_mimo_C.response.txt`, and its quotations match revised L75.
  - **The clause Mimo names changes no claim.** File 11 already says that the physical module, not the semantics, fixes what a carrier bears: L33, L215 ("supplied by the physical module, not by the semantics"), L509, and Part XII at L453. Whether contents pass between media is already in the declaration's own words, "so far as the adopted physics lets contents pass".
  - **"Fixed by" is not stronger than s2.** S2 limits what may be attributed to a system to what the physics permits, and that set is already the physics' to fix. Adding Mimo's clause would declare as new something file 11 already holds.
  - **Cases.** O14, O28, O42, O43, O44, O49 and D3-T do not move. N24 moves toward only through the declared barrier sentence.
  - **Atria C** (point 5) also finds R07 standing. The checker read it and did not count it.
- **Text:** none changes. OLD, NEW, KIND (CLAIM) and DECLARATION stay as drafted.
- **CHECK (append, exact):**

````text
Cross-examination of revision 2 (S90 part C): Mimo said FALLS (the declaration omits that bearability and passage between media are "fixed by the adopted physics"); Atria said STANDS. Ruled KEEP after the cross-examination: bearability is the physical module's to fix already in file 11 (L33, L215, L509; Part XII L453), and passage is in the declaration's "so far as the adopted physics lets contents pass", so the clause changes no claim and the declaration is exact.
````

- **Earlier rulings:** none on R07 or W45.1.
- **Ruling file:** `ruling s90_xexam_mimo_C item 2 R07.md` (md5 5b2d1637ea37a88d58375f63a70e634a).

### R30 (W41.1), point 3: KEEP (one ruling with Atria C's, below)

- **Why contested.** The reply says FALLS (tasks (a) and (c)).
- **The entry.** W41.1, "Part X: inexplicit representation, and a witness identified by use, with the relay guard". File-11 L401, revised L399–403. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, FIX". Check 2 did not touch the witness clause's four criteria or its pointer to Part IX.
- **The reply.** The clause "as reason use asks of an objection (Part IX)" presents the identify-by-use criteria as Part IX's own, but they differ from Part IX in three ways:
  - the new clause says "the changes the binding specifies", where Part IX says "the changes specified by the operative deliberative rule";
  - it drops Part IX's structural map from the represented objection into the response suborganization;
  - it says "lie on" where Part IX says "lands on".

  So the reply says both the pointer and the declaration's "in the manner of reason use" misdescribe the claim. Its repairs: copy Part IX's clause word for word, or write "in a manner modelled on reason use" in both the text and the declaration.
- **The checker.**
  - **Quotations.** All are found word for word. Reason use is at revised L379, not 364, and the clause is at L403, not 404–405.
  - **The specifier.** "As reason use asks of an objection" is a parallel, and "of an objection" marks it as one. Putting the binding where Part IX has the operative deliberative rule is the change the parallel needs. A word-for-word copy would ask a tacit binding for a deliberative rule it does not have, and would lose the move toward on N21 and Derivation 10's binding.
  - **The structural map.** Leaving it out weakens nothing. (R)'s fidelity and provenance (L401), Build's conditions (L399) and the active-route clause still guard it.
  - **"Lie on" and "lands on"** put the same condition.
  - **"In the manner of"** already means "modelled on", so the second repair changes words and no claim.
  - **Cases.** N21 moves toward, as declared. N13, N12, N15, O14, O18, O19, O23, O31 and O32 hold. O15 holds, or moves toward. D3-T is not touched.
- **Text:** none changes.
- **CHECK.** This ruling's own line is below. It is replaced by the one reconciled line that the Atria C checker wrote after reading this ruling (given under Atria C, R30).

````text
Cross-examination of revision 2 (S90 part C): Mimo said FALLS (the witness criteria differ from Part IX's reason use: "the changes the binding specifies" for "the changes specified by the operative deliberative rule", no structural map, "lie on" for "lands on", while the pointer and the declaration present them as reason use's); Atria said STANDS (declared moves toward on N21 and O15). Ruled KEEP after the cross-examination. "As reason use asks of an objection" is a marked parallel, and the binding must replace the deliberative rule as specifier when the thing used is a binding: a verbatim copy would fail N21 and Derivation 10's binding. The structural map's guard is kept by (R)'s fidelity and provenance (L401), Build (L399) and the active-route clause. "In the manner of" already means modelled on. No case moves away; O15 holds, toward if anything.
````

- **Earlier rulings:** none on R30, W41.1 or C25. The single S90 call (C25) failed and supports nothing.
- **Ruling file:** `ruling s90_xexam_mimo_C item 3 R30.md` (md5 dd2ffd6a178a29c438ba745db3d6e362).

### R13 (W35.2), point 4: FIX (reconciled with Atria C's FIX; this text is the one taken)

- **Why contested.** The reply's line is STANDS. Its point 4 (task (a)) names an undeclared claim: the declaration leaves out the new wording's opening clause, "Expectation and violation are defined for every transport, surprise only for a selected one". The reply grants that the clause largely restates R12 and is "not an independent new claim". It says the clause inherits R12's defect and is false as written. Its repair: add the clause to the declaration, with "(to the simulation layer)", tracking any repair of R12.
- **The other reply to part C.** Atria C makes R13 its FALLS on the same ground.
- **The entry.** W35.2, "Part IV: a constructed transport is violated, not surprised". File-11 L225, revised L223. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, FIX. …" The drafter's REASON says the opening clause is what the sentence is for: plan 1.2's "and said so".
- **The checker.**
  - **Mimo is right** that the declaration leaves out the opening clause, which the entry's own REASON names as the sentence's purpose.
  - **Atria is right** that the clause, as prose, states a false universal. This holds even if R12 were kept as drafted.
  - **The fix** scopes the clause to transports "to the simulation layer", as R12's fix does, and writes its instance as "a constructed one", parallel to "a selected one", so that "violated" stays inside that scope. The two fixes should be applied together.
  - **\(\operatorname{Ans}_E\), and cutting the clause,** are both refused.
  - **Quotations.** All are found. Atria's "~203" and "~179" are file-11 line numbers; the revised lines are L201 and L177.
  - **Cases.** N18 holds, and its Dov half stays watched. O23, O3 and D3-T are not reached.
- **OLD:** unchanged (file-11 L225).
- **NEW (exact):**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

- **KIND:** CLAIM, unchanged. **REASON WORD:** clarification, unchanged.
- **DECLARATION (exact):**

````text
Part IV now says, restating its definitions, that expectation and violation are defined for every transport to the simulation layer and surprise only for a selected one; that a constructed transport to the simulation layer that fails at a pair of its contract is violated, and the failure is not surprise; and that a violation the system represents can be a recognized difficulty.
````

- **CHECK and the list of what the checks changed (exact):**

````text
S90, Mimo part C point 4 (closing line R13 STANDS, but it names an undeclared clause) and Atria part C point 1 (R13 FALLS); fresh checker FIX after the cross-examination. The opening clause reads 'for every transport to the simulation layer', since \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only when \(t\)'s target is \(S\); its instance reads 'a constructed one', parallel to 'a selected one', so that 'violated' stays inside that scope. The declaration now includes the restated clause, which the REASON names as the sentence's purpose. Follows the R12 (W35.1) fix.
````

- **Earlier rulings:** none on R13, W35.2 or C12.
- **Ruling file:** `ruling s90_xexam_mimo_C item 4 R13.md` (md5 cacaa8ee869cf81aee7cbc5e93f34486).

### R25 (W40.1), point 5: KEEP (reconciled with Atria C's FIX: the pass takes the FIX)

- **Why contested.** The reply's line is STANDS. Its point 5 (task (a)) says the declaration drops the new wording's description of a bare denial, "which offers no component that responds to a change in what produces the appearance". It calls this "Minor, but the characterisation is part of the claim". Its repair: "of which a denial that offers no component responsive to changes in what produces the appearance is not an account".
- **The entry.** W40.1, "Part VII: why the absent structure appears is a separate question". File-11 L337, revised L335. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, FIX". Check 2 changed the placement and the wording, but not the declaration or the relative clause.
- **The checker.**
  - **The clause gives the reason the declared verdict holds**, and file 11 already supplies that reason in (E)'s terms: non-circular dependence (L257); the table with no component that responds to an intervention (L271); the account that only restates its answer (L275); and a production question, whose contract contains interventions on upstream ports (L153).
  - **The reach is the same.** The clause is non-restrictive, so it describes bare denials rather than defining a new class. On every kind of denial, the declaration and the new wording reach the same verdict. The declared first limb, "an account of the absence neither answers that question", covers argued denials that say nothing about the appearance.
  - **The repair is refused.** It would turn that description into a restrictive condition the text does not state, so the declaration would describe a sentence that is not there.
  - **N22** moves toward its fixed verdict, and the declaration accounts for the move. Wren's is a bare denial, so it is not an account. Yuri offers a component, and R25 leaves his candidate to (E).
  - **Quotations.** All match the texts.
- **Ruled:** KEEP, with this CHECK line (exact):

````text
Cross-examination of revision 2 (S90 part C): Mimo gave STANDS but said under (a) that the declaration omits the new wording's description of a bare denial ("which offers no component that responds to a change in what produces the appearance"); Atria gave STANDS and named the declared move toward N22. Ruled KEEP after the cross-examination: the clause gives the ground of the declared verdict in (E)'s terms, which file 11 already supplies (non-circular dependence L257; L271; L275; Part III L153), and on every kind of denial the declaration and the new wording agree, so the declaration is exact.
````

- **Reconciled.** Atria C's checker ruled FIX, declaration only, on the same entry. The pass takes that FIX (Reconciliation, item 4), so this KEEP line is not appended. Both rulings stay on the record.
- **Earlier rulings:** none on R25, W40.1 or C21.
- **Ruling file:** `ruling s90_xexam_mimo_C item 5 R25.md` (md5 9d43fc63ac8a9a69d95c111d5ab82a19).

## Atria, part B2 (s90_xexam_atria_B2)

**The call is accepted.** It was accepted in pass 2, at attempt 4 of 4. Attempts 1–3 had status 0, after 1,802.2, 1,802.3 and 833.4 s. Attempt 4 had status 200, finish "stop" and 0 bad chunks, after 924.8 s. The response's sha256, f965836a…, matches the receipt. The last line is END OF REPORT. The reply is 1,375 words by `wc -w`. In pass 1, attempt 1 had ended with no reply after 1,802.5 s, attempt 2 was in flight at the cut, and attempts 3–6 were refused.

**OVERALL:** `OVERALL: SOUND`

**Unexamined changes:** none. All 11 changes of the part have a closing line, and every line is STANDS.

**Not contested.** These points name no undeclared change of claim and no moved verdict.
- **Point 2, R11 and R52:** "No verdict moves" (O48). Its "Dropping 'realizable' from the old list loses nothing" agrees with the R52 KEEP on Mimo B2.
- **Point 4, R22:** "R22 moves nothing". O52, O39, O20 and O45 divide as the verdicts require.
- **Point 6, R35, R36 and R37:** no symbol clashes, and O35 reads as before ("the theory agrees given the input the verdict states, and did before the change").
- **Point 7, R40:** the boundary fallback. The reply finds that O17, O51 and O49 "land right", and it names no move. W12.1 (R40) drafts the repair of the boundary hazard that 04 §7.10 recorded on O30 and O17. Neither reply to part B2 contests it. That bears on `determination/10`, and it is noted there.

### R42 (W17.2), point 1: KEEP

- **Why contested.** The reply's line is STANDS. Its point 1 names moved verdicts on O24 and N5, both toward the fixed verdicts, and it calls them declared.
- **The entry.** W17.2, "L473 s1: the population is of realizable transports". The heading predates check 1's fix: OLD "a population of realized transports", NEW "a population of candidate transports". Part XII, file-11 L473, revised L475. KIND CLAIM. REASON WORD clarification. CHECK: "check 1, FIX. …"
- **The checker.**
  - **O24.** The reply's quotation is wrong. The case says "reachable by hand" of the setting, not of the arrangement, and it never says whether the second arrangement was built. On the texts O24 stays AGREE, as the entry says. The change closes the "realized" reading that S81's step 4 (03) flagged as a possible harm to O24.
  - **N5** stays AGREE, or moves toward it, as the entry and conflict 1 already record. The quotations from N5 and from revised L475 and L195 check out.
  - **O48** stays AGREE, because L475's unchanged last sentence still excludes the wired arrangement. D3-T is unaffected, since both designs were built. O11 and N9 are not reached.
- **Text:** none changes. OLD, NEW, KIND (CLAIM) and DECLARATION stand as drafted. Mimo B2 gave STANDS and did not contest the change.
- **CHECK (append, exact):**

````text
After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS and named moves on O24 and N5, both toward and both declared; kept. The reply's O24 quotation "reachable by hand" is said of the setting, not the arrangement; on the texts O24 stays AGREE, and the change closes the "realized" reading that 03 watched for harm. Mimo's reply gave STANDS and did not contest it.
````

- **Housekeeping, not part of the ruling.** The entry's heading still says "the population is of realizable transports", the wording from before check 1's fix. It could be brought into line with NEW ("the population is of candidate transports") when the KEEP goes into CHECK. It appears in neither the note nor the record.
- **Earlier rulings:** none on R42 or W17.2.
- **Ruling file:** `ruling s90_xexam_atria_B2 item 1 R42.md` (md5 47000fd11f286be3a676298c90f566f3).

### R31 (W21.1), point 3: KEEP (one ruling with Mimo B2's)

- **Why contested.** The reply's line is STANDS. Its point 3 names moves "from unsettled to settled, all toward the fixed verdicts" on O11, O18, O31, N15 and N21. It also gives the typing that answers Mimo B2's FALLS: "a transport to a content is assessed on the content's contract, as in (R); a transport from a content is assessed on its domain's contract, as in Part V".
- **The checker.**
  - **The reply's typing is right.** It is the entry's own REASON. All its quotations are found.
  - **The claimed moves are not moves.**
    - File 11's ruled marks on O11, O18 and O31 are already AGREE (S81, determination 04), through Build and L401 s5. The definition only makes New checkable, which the entry records as "more securely".
    - O11's case says only that the key "looks like Tuesday's", which is similarity, and NEW excludes similarity as the criterion. "Wednesday is neither" rests on the absence of Build on Wednesday.
    - N15 and N21 have no file-11 mark yet. Any move toward that the test round finds traces to this declared definition (plan P2(b)).
  - **No verdict moves away**, and no undeclared change of claim is shown. D3-T and N4 are not named.
- **Text:** none changes. OLD, NEW, KIND CLAIM and DECLARATION stay byte for byte.
- **One reconciled append to CHECK (exact).** It replaces the separate appends of the two R31 rulings:

````text
After the cross-examination:
- s90_xexam_mimo_B2 (point 1, R31 FALLS: 'ill-typed and non-symmetric'): KEEP.
  - The transport from d to c is judged on c's contract as (R) judges a transport into c (L205–208, file-11 text unchanged, on which Deploy and so (N)'s repertoire rest). The transport from c to d is typed as in Part V. Both are checked on the changes c commits to.
  - The relation is taken on the contract of the content whose newness is in question. (N) is its only use, and nothing uses symmetry. 'Equivalence' is the file's two-direction sense (L357).
  - The declaration states the definition word for word.
  - The proposed 'each faithful on the contract of its source' would make c new whenever an earlier content commits beyond c. That is a change of claim, against plan row W21, and it could reopen N4.
- s90_xexam_atria_B2 (point 3, R31 STANDS; names moves 'from unsettled to settled, all toward the fixed verdicts' on O11, O18, O31, N15 and N21): KEEP.
  - It gives the same typing.
  - On O11, O18 and O31, file 11's ruled marks are already AGREE, through Build and L401 s5, so no mark moves. NEW makes New checkable, which is the 'more securely' recorded here.
  - O11's 'Wednesday is neither' rests on the absence of Build. The case says only that the key 'looks like' Tuesday's, which NEW excludes as a criterion.
  - N15 and N21 have no file-11 baseline yet. A move toward on either, if the test round finds one, traces to this declared definition.
````

- **Nothing else changes.** Nothing follows by program. W19.2's recheck of skeleton conflict 12 stands.
- **Earlier rulings:** batches 1 and 2 have none on R31.
- **Ruling file:** `ruling s90_xexam_atria_B2 item 2 R31.md` (md5 b1d84e98d086d354df938d76a7397be6).

### R32 (W13.1) and R33 (W13.2 + W12.2), point 5: KEEP both (found not contested)

- **Why listed.** Both lines are STANDS. Point 5 says the new wording "reproduces O30" and, with O21 and O50, "lets the theory accept the verdicts' weightings rather than contest them". It ends "No verdict moves away." It was sent to a checker to decide whether that names a moved verdict (Parts rule 2).
- **The entries.**
  - **R32 = W13.1**, "L419 s2: 'today' is dropped". CHECK: "check 1, SOUND".
  - **R33 = W13.2 + W12.2**, "L419: credit for content and ownership of a process are different attributions". CHECK: "check 1, SOUND, on the condition that W23.1 is corrected (it is)".
- **The checker: point 5 names no moved verdict.**
  - It is headed (a, c), not (d). All its quotations are found.
  - **The declared-input clause it cites is not from these changes.** "a weighting of credit among several contributions to one achievement" (L516) was added by R45 (W6.4 + W14.1, part B1). Neither R32 nor R33 adds any weighting.
  - **"Accept rather than contest" is true only as "does not contradict".**
    - O21, O27 and O50 stay SILENT on "mostly".
    - L516 bars treating a verdict's own "mostly" as the input ("rather than choosing the input from the verdict wanted").
    - What R33 closes is 1C B's contrary reading of O50's discovery point, which 04 and 07 had already ruled against ("complementary clauses of one rule").
  - **No ruled mark moves.** O30, O17, O40, O41, O51, N11 and N15 stay AGREE. O49, N13 and D3-T are not reached.
  - **One loose word.** O50's three achievements are not "exactly" the attributions of Parts X and XI. Nothing turns on it.
- **Text:** none changes in either entry. OLD, NEW, KIND (CLAIM) and DECLARATION stand as drafted.
- **CHECK, W13.1 (append, exact):**

````text
After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS and noted only that "today" is gone, matching Part XII; no move named; kept. Mimo's reply gave STANDS with no point.
````

- **CHECK, W13.2 + W12.2 (append, exact):**

````text
After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS; its "lets the theory accept the verdicts' weightings rather than contest them" (O21, O50) names no move. On the texts O21, O27 and O50 stay SILENT on "mostly", since the new sentence supplies no weighting and L516 bars taking it from the verdict. O50's discovery point is secured, as 07 ruled for file 11. O30 stays AGREE. Kept. The weighting clause the reply cites is W6.4 + W14.1's. Mimo's reply gave STANDS with no point.
````

- **Earlier rulings:** none. Mimo B2 gave STANDS on both, with no point.
- **Ruling file:** `ruling s90_xexam_atria_B2 item 3 R32-R33.md` (md5 d07e56b2b2bc048ad33a6b6f993fa6c6).

## Atria, part A1 (s90_xexam_atria_A1)

**The call is accepted.** It was accepted in pass 2, at attempt 5 of 5.
- Attempts 1 and 2 had status 0, after 739.3 and 1,802.4 s.
- Attempts 3 and 4 had status 200 and finish "length" with no content, after 1,240.0 and 1,190.7 s, and were rejected. Their files were not opened.
- Attempt 5 had status 200, finish "stop" and 0 bad chunks, after 1,017.4 s.
- The response's sha256, 3a6d3413…, matches the receipt. The last line is END OF REPORT. The reply is 1,103 words by `wc -w`.
- In pass 1, attempts 1–4 had ended with no reply, attempt 5 was in flight at the cut, and attempt 6 was refused.

**OVERALL:** `OVERALL: NEEDS REPAIR`

**Unexamined changes:** none. All 9 changes of the part (R01, R05, R08, R09, R15, R16, R17, R19, R20) have a closing line.

**Not contested, but bearing on batch 1.** None of these points names an undeclared change of claim or a moved verdict.
- **Point 4, R08 (W19.1).** Atria finds the declaration accurate and the forward use of \(E\), \(E'\), \(\tau\), \(\tau'\) and \(\lambda(k)\) in Part II a blemish, "Not incoherence". It read R08 as sent. Batch 1's FIX (Mimo A1, point 1) inserts the typing sentence that answers this blemish. Nothing needs reconciling.
- **Point 5, R15 and R20 (W20.1, W20.3).** "No verdict moves." Atria reads O45's second spring as a route "whether or not anyone described its work". That is the clause batch 1's R15 FIX adds to L231, so the two agree. Nothing needs reconciling.
- **Point 6, R09, R16, R19 and R05:** "checks that pass". Nothing here moves a verdict.
- **Point 3, R17 (task (c)).** Part VII's unchanged sentence at L339 names a pair but no block \(G\). The R17 ruling below passes this on as an optional notation point.

### R01 (W37.1), point 1: FIX (reconciled with batch 1; same text)

- **Why contested.** The reply says FALLS (task (b)).
- **The entry.** W37.1, "Restore 'blind' in Part 0's account of selection". File-11 L15, revised L13. KIND ORDER. REASON WORD erratum. DECLARATION none. CHECK: "check 1, FIX (kind only)".
- **Batch 1's ruling.** On Mimo A1's point 3, batch 1 ruled FIX: it deleted "blind", kept KIND ORDER and DECLARATION none, changed the fallback line and changed the REASON WORD from erratum to clarification. Batch 2 repeated it.
- **The reply.** The added clause "with no represented target in that history" is genuine ORDER. But "blind" is stated nowhere in the body: Part IV (L195) and Part XII (L475) impose no blindness on variation. So directed variation counts as selected under Part IV but not under the Part 0 gloss. That is a claim, and it breaks Part 0's rule that "the front matter states nothing the body does not state more exactly" (L35). The reply says no situation moves. Its repairs: delete "blind", or add blindness to Part IV's **Selected**.
- **The checker.**
  - **All quotations are verbatim** (L13, L35, L195, L405 and L475). "Blind" occurs only at revised L13 and never in file 11.
  - **The clause attaches to the history.** So it cannot fix the sense of the adjective, and on the strict sense L35's rule is broken.
  - **The same ruling as batch 1.** Deleting "blind" is safe under both readings of the word. The ruling now rests on two independent replies, one of which says FALLS outright, and on the further ground of L35.
  - **The second repair is refused.** Adding blindness to Part IV's Selected would be an undeclared CLAIM change to the body.
  - **Cases.** O11, N9, N11 and D3-T hold whether or not the word stays. No case turns on how the variation is produced.
- **OLD:** unchanged.
- **NEW (exact, identical to batch 1):**

````text
A correspondence can be *selected*, produced by variation and survival on a history of encountered changes, with no represented target in that history;
````

- **KIND:** ORDER, unchanged. **DECLARATION:** none, unchanged. The fallback line stays as batch 1 set it: "If a checker rules CLAIM: 'Part 0 now says that a selection history holds no represented target, as Part IV states.'"
- **REASON WORD:** erratum → clarification, as in batch 1.
- **REASON: the record sentence** replaces batch 1's so that it names both calls (exact, as the ruling sets it out):

````text
- After the cross-examination (Mimo, part A1, point 3; Atria, part A1, pass 2, point 1), "blind" is deleted.
- Its ordinary strict sense, variation not directed in any way (for example by a cue or a gradient that represents nothing), says more than Parts I–XVI state (S81 03 M2, R1's close call). That breaks Part 0's rule that "the front matter states nothing the body does not state more exactly".
- The clause alone states the body's sense.
- Atria's alternative, adding blindness to Part IV's Selected, is refused as an undeclared CLAIM change to the body.
````

- **CHECK (add, exact):**

````text
S90: FIX (Mimo A1 point 3, batch 1; Atria A1 point 1, reconciled, same text)
````

- **GAIN, LOSS and the title** follow batch 1. GAIN drops "in the same word as file 10". LOSS adds that Part 0 no longer uses file 10's word. The title change is optional.
- **By program:** the note's row R2-01 takes the reason "clarification", and the counts are unchanged. The "What the checks changed" row for W37.1 names both calls.
- **Ruling file:** `ruling s90_xexam_atria_A1 item 1 R01.md` (md5 350b00ba83df86898875ce993f691093).

### R17 (W20.2), point 2: KEEP

- **Why contested.** The reply's line is STANDS. Its point 2 names a move on O33, toward the fixed verdict, and calls it declared.
- **The entry.** W20.2, the non-circular dependence rider, drafted from the settled S88 positions (F3, block 1). File-11 L257, revised L255. KIND CLAIM. REASON WORD change of claim. CHECK: "Not put to check 1 or check 2. … Checked by its drafter as W19.1 was." The same field holds the settled fallback, which applies if X1 finds that the rider breaks a worked case.
- **The checker.**
  - **The move on O33 is toward the fixed verdict, and it is declared.** O33's ruled mark is AGREE on both file 11 and the draft. It rests on L151/L153 (the question's form) and L189 ("faithful"), and R17's S3 touches neither.
  - **The reply misreads O33.** It treats the table's rows as commitments that an edit could remove. In the case, the table is Lea's question rewritten, not a candidate. S88 already withdrew the O33 flip on this point.
  - **What the reply's "toward" does describe is already in the entry.** Accounts of the joint question with input-only contracts can now show dependence by deletion. The entry's GAIN records this, and the declaration's second sentence states it.
  - **The old defect is overstated.** The reply's "could not satisfy … at all" holds only on the mechanism-only reading, which is what the entry's REASON says.
  - **The reply's check that "\(p\) because \(p\)" still fails is right.** It fails through S2, as S88 found.
  - **Other cases.** D3-T, O5 and O7 are unaffected or move toward. No worked case breaks, so the fallback in W20.2's CHECK is not triggered.
- **Text:** none changes. OLD, NEW, KIND, REASON WORD and DECLARATION stand as drafted.
- **CHECK (append, exact):**

````text
After the cross-examination (S90, part A1): Atria's reply (pass 2, attempt 5) gave STANDS and named a move on O33, toward and declared; kept. O33's ruled mark rests on L151 and L189 ("faithful"), which S3 does not touch, and its table is the question's form, not a candidate (the O33 flip was withdrawn in S88). The move the reply names is the entry's GAIN, that accounts of input-only contracts can now witness. The reply's "'p because p' fails through S2" agrees with S88. Its point 3 (L339 names no block) is a notation point, passed on. Mimo's reply gave STANDS and did not contest the change.
````

- **Optional, for CASES AT RISK, O33.** Beside "holds AGREE", record the reply's "toward" reading: "toward for accounts of the joint question on the mechanism-only reading, which the case does not claim".
- **Point 3 is passed to the orchestrator**, as an optional notation point. L339 could name the deleted block, for example "with the skewness commitment as the deleted block". If it is adopted, it would be a new entry.
- **Mimo A1's letter \(G\)** (batch 1, passed on and not ruled). This ruling does not take it up. If the orchestrator adopts a new letter, the letter must also replace \(G\) in the fallback text in W20.2's CHECK.
- **Earlier rulings:** none on R17.
- **Ruling file:** `ruling s90_xexam_atria_A1 item 2 R17.md` (md5 1db4518b806bb9334ae654bd663b56dd).

## Atria, part C (s90_xexam_atria_C)

**The call is accepted.** It was accepted in pass 2, at attempt 6 of 6. Attempts 1–5 had status 0 and brought nothing back, after 1,802.4, 1,590.3, 497.8, 119.6 and 929.0 s. Attempt 6 had status 200, finish "stop" and 0 bad chunks, after 1,091.3 s. The response's sha256, bd51b785…, matches the receipt. The last line is END OF REPORT. The reply is 1,227 words by `wc -w`. In pass 1, attempt 1 was in flight at the cut, and attempts 2–6 were refused.

**OVERALL:** `OVERALL: NEEDS REPAIR`

**Unexamined changes:** none. All 11 changes of the part have a closing line.

**Not contested.** These points name no undeclared change of claim and no moved verdict.
- **Point 1, on R12.** The reply's R12 line is STANDS, but it adds "the same repair must touch it". R12's FIX (Mimo C) is exactly that repair.
- **Point 2, R12, R13 and R14 on N18:** "the declared distinction is exactly the fixed verdict". The point names no move, and it calls R14 "properly WORDING".
- **Point 4, R23 on N4 and N5:** "R23 therefore moves nothing by itself".
- **Point 5, R07:** "sound", and "it does not touch O14". Mimo C's FALLS on R07 was ruled KEEP. The checker read this point and did not count it.

### R13 (W35.2), point 1: FIX (reconciled with Mimo C's FIX, whose text is taken)

- **Why contested.** The reply says FALLS (task (c)): "'defined for every transport' contradicts the section's \(\operatorname{Ans}_S\) formula and Part IV's primitive-layer transports".
- **The reply.** \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is well typed only when \(t\)'s target is \(S\). Part IV holds selected transports at the primitive layer (L201), and (R)'s transports run from a carrier to a content, so "defined for every transport" is false as written. Its repairs: "for every transport into the simulation layer", or \(\operatorname{Ans}_E\). "R12 stands … but the same repair must touch it."
- **The checker.**
  - **The typing point holds.**
  - **\(\operatorname{Ans}_E\) is rejected.** It would edit R12's bullet, contradict L177 and W35.1's reason, and give an undeclared expectation to every Part V candidate and every carrier-to-content transport.
  - **Narrowing to the simulation layer is adopted.** The words "the simulation layer", not "\(S\)", cover Derivation 10's \(S_0\) and \(S_1\).
  - **Mimo's declaration point.** Once the clause carries a scope, R13's own declaration should state it, so the checker adds it.
  - **Cases.** N18 holds with no mark moving, and O23, O3, D3-T and Derivations 4 and 10 are not reached.
  - **Passed to R12's checker:** "R12's declaration … should read 'for every transport into the simulation layer'". R12's FIX does so, in the words "to the simulation layer".
- **Its NEW (exact):**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport into the simulation layer, surprise only for a selected one: a constructed transport that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

- **Its DECLARATION (exact):**

````text
Part IV now says that expectation and violation are defined for every transport into the simulation layer and surprise only for a selected one, that a constructed transport that fails at a pair of its contract is violated, that the failure is not surprise, and that a violation the system represents can be a recognized difficulty.
````

- **Its reason, to go in the entry marked "after the cross-examination" (exact):**

````text
The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is well typed only for a transport whose target is the simulation layer, as (A) at L250 shows. Part IV also has transports into the primitive layer (L201) and carrier-to-content transports under (R). So "every transport" said more than the formula defines. The sentence is narrowed to the scope that W35.1's REASON and L177 already give. No case moves: N18 holds as CHECK states it, and O23, O3 and D3-T are not reached.
````

- **Reconciled.** The pass takes Mimo C item 4's NEW and DECLARATION, and this ruling's reason paragraph for the REASON field (Reconciliation, item 3).
- **Ruling file:** `ruling s90_xexam_atria_C item 1 R13.md` (md5 5a35bb939c214d156be7ed9160645c0e).

### R06 (W36.1), point 3: KEEP

- **Why contested.** The reply's line is STANDS. Under (d), it names a move on N3 that R06 causes, toward the fixed verdict, and calls it declared.
- **The entry.** W36.1, "Part I: which sense of 'explanation' the fallibility commitment uses". File-11 L71, revised L69. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, FIX". CASES AT RISK already predicted "N3: toward on both questions".
- **The checker.**
  - **The move is toward the verdict, and it is declared.**
    - Read literally, the old sentence ("cannot count as explanation") denied N3's "Yes, an explanation … only in form". The new clause gives that yes: a false theory offered as an answer is "an explanatory candidate, which ordinary usage may still call an explanation".
    - The "No, it does not explain" answer stays, because the myth fails (F1) and non-circular dependence (revised L255, L273).
    - The move follows from the declaration's own two clauses.
  - **N1 holds**, carried by unchanged s1, L231 and R24 (L313), not by R06 alone. N2 holds or moves toward. O8, O15, N22 and D3-T hold.
  - **Every quotation checks.** The pointers to Part V and to Part VI at L313 ("a separate matter") are exact, and no coherence defect was found.
- **Text:** none changes.
- **CHECK (append, exact):**

````text
Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a move toward the fixed verdict on N3: the candidate/account distinction gives "No, it does not explain" with "Yes, an explanation … only in form", which the old s2 read literally denied. Mimo gave STANDS with no point. Ruled KEEP after the cross-examination: the move is toward, and it follows from the declaration's two clauses ("explanation" means an account; a false theory offered as an answer is a candidate that ordinary usage may call an explanation). The "No" rests on (F1) and non-circular dependence (L255, L273). N1 holds (s1, L231, R24), N2 holds or moves toward, and O8, O15 and N22 hold. The pointers to Part V and to Part VI (L313) are exact.
````

- **Earlier rulings:** none on R06, W36.1 or C06. Batch 1's R28 ruling found W22.1 consistent with L69, and this ruling agrees.
- **Ruling file:** `ruling s90_xexam_atria_C item 2 R06.md` (md5 6ca49961f50f78586c819d565ef221da).

### R21 (W58(i).1), point 3: KEEP

- **Why contested.** The reply's line is STANDS. Under (d), it names a declared move toward the fixed verdict on O45. It adds that the old "the ones actually written" contradicted (S) and the verdict.
- **The entry.** W58(i).1, "Part VI: the supports assessed are the subsets of the written Γ". File-11 L301, revised L299. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, SOUND. O36 is watched, not held on firmer text …"
- **The checker.**
  - **The move is real, and it is declared.** It comes from the declaration's own clause, "whether or not anyone has set them out", and the entry expected it ("holds, or moves toward").
    - On the S81 reading, file 11 was already AGREE on O45 through L309 s3, so the mark holds on firmer text.
    - For a reader of old L301's narrow reading, the case moves from split to agree.
  - **The reply's "contradicted (S) and the verdict" overstates the old ambiguity.** Only the narrow reading ("only the supports someone has set out") did. This does not bear on the entry.
  - **Other cases.** N1 holds. O36 holds AGREE on its natural reading, and stays watched as the CHECK says. O46, O47 and D3-T hold.
  - **Agreement with earlier rulings.** The ruling agrees with batch 1's R15 FIX (L231's "whether or not anyone has described their work") and with batch 2's R51 KEEP, which relied on "L299 as W58(i).1 words it (O36)".
- **Text:** none changes.
- **CHECK (append, exact):**

````text
Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on O45: 'whether or not anyone has set them out' has the second spring's support assessed from the start, in line with (S). Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move is toward and follows from the declaration's own clause. On the S81 reading file 11 was already AGREE on O45 through L309 s3, so the mark holds on firmer text; only old L301's narrow reading ('only the supports someone has set out') pulled against it, and the reply's 'contradicted (S) and the verdict' overstates that ambiguity. N1 holds. O36 holds AGREE on the case's natural reading (the replacement premise is outside Γ, which NEW's last clause excludes), and stays watched as check 2 says: on the other reading, (S) already assessed the rewritten route in file 11, and P stays critical in each route as written. O46 and O47 hold.
````

- **Earlier rulings:** none on R21. Mimo C gave STANDS with no point.
- **Ruling file:** `ruling s90_xexam_atria_C item 3 R21.md` (md5 e72966e1242786033e9cc68f04d905a2).

### R24 (W33.1), point 3: KEEP

- **Why contested.** The reply's line is STANDS. Under (d), it names a declared move toward the fixed verdict on N1: "Strike it out and the account works exactly as before" is read as the no-work test. It also claims an equivalence: closure of \(\mathsf S\) under adding and removing \(d\) "just is" the absence of a critical \(\{d\}\).
- **The entry.** W33.1, "Part VI: (E) tolerates a commitment that does no work; (B) marks it". File-11 L315, revised L313. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, FIX. Four defects: …"
- **The checker.**
  - **The N1 point is right.** It holds on the reading where the sun-god sentence constrains nothing. The declaration accounts for the move ("(E) has no condition that each commitment do work", "leaves the candidate's standing under (E) unchanged", "critical in no support"). No move away comes from R24.
  - **The reply's equivalence is false.** The Interference paragraph at revised L309 is a counterexample: there \(\Gamma=\{a,b\}\) and \(\mathsf S=\{\{a\}\}\), so \(\{b\}\) is critical in no support, yet adding \(b\) to the support \(\{a\}\) breaks it. The brute-force check over 256 families found 65 families where \(\{d\}\) is critical in no support and the test fails. NEW does not claim the equivalence. It only says the two-halved test implies its two consequences ("then"), and both hold.
  - **N1's watch stays as recorded.** Under the redundant-route and unfaithful-component readings, N1 is still at risk. Those risks come from (B), L307 and (F1), not from R24. O45, N2 and O8 hold.
- **Text:** none changes.
- **CHECK (append, exact):**

````text
Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N1 ("Strike it out and the account works exactly as before" read as the no-work test, with \(\{d\}\) critical in no support), and claimed that the test is equivalent to "\(\{d\}\) critical in no support". Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move on N1 is toward, on the reading where the sentence constrains nothing, and the declaration accounts for it. The claimed equivalence is false (Interference, L309: \(\{b\}\) is critical in no support but fails the addition half), and NEW does not assert it; NEW's "then" consequences follow from the two-halved test. N1's watch on the redundant-route and unfaithful readings stays as recorded. It comes from (B), L307 and (F1), not from this entry. O45, N2 and O8 hold.
````

- **A record point, outside the ruling.** W33.1's CHECK says that O2's "this derives L275 s2's rule" was struck and that O19 was added, watched. Its CASES AT RISK still ends the O2 item with that sentence and does not name O19. The two fields should be brought into line when the CHECK line is added. The theory text is unaffected.
- **Earlier rulings:** none on R24, W33.1 or C20.
- **Ruling file:** `ruling s90_xexam_atria_C item 4 R24.md` (md5 2474458947460c4d758775530d6a9b3a), with its check script (above).

### R25 (W40.1), point 3: FIX, declaration only (reconciled with Mimo C's KEEP: the pass takes this FIX)

- **Why contested.** The reply's line is STANDS. Under (d), it names a move on N22: Wren's bare denial "offers no component that responds to a change in what produces the appearance", so it is not an account of the appearance, and Yuri's memory machinery supplies one.
- **The checker** stated both replies' arguments (Parts rule 3). It did not open the Mimo C checker's ruling.
  - **"Bare" is defined only by the clause.** "Bare" occurs once in the revised text, at L335, and never in file 11. "Denial" occurs nowhere else in either text. So the clause is the theory's only statement of what puts a denial under the exclusion.
  - **The clause is a substantive condition** in the theory's own terms. Of (E)'s conjuncts the text says "None inspects a label" (L265), and "The word 'table' settles nothing" (L269). The declaration as drafted states the exclusion through the label alone.
  - **The clause is true.** It follows from Part V, through (F1) as at L269 and non-circular dependence as at L273.
  - **The batch-1 R51 test fails here.** Those rulings kept an entry because the omitted phrase "makes no claim of its own". This omitted clause is stated nowhere else, and it gives the declared claim its reach.
  - **N22.** The clause puts Wren under the exclusion and leaves Yuri outside it. The move is toward, and nothing moves away. Yuri's standing as a candidate comes from R06 (L69), not from R25. N8, N25 and O34 hold, and D3-T is not named.
  - **Mimo's repair is refused.** It makes the clause restrictive, paraphrases it and drops "bare". The fix instead inserts NEW's own clause word for word.
- **OLD, NEW, KIND (CLAIM) and REASON WORD (clarification):** unchanged.
- **DECLARATION (exact):**

````text
Part VII now says that where an absent structure appears to be present, why it appears is a separate question with its own target and contract, which an account of the absence neither answers nor needs to answer, and of which a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account.
````

- **CHECK (append, exact):**

````text
After the cross-examination (S90: Atria C point 3, R25 STANDS, naming a declared move toward N22; Mimo C point 5, R25 STANDS, saying the declaration leaves "bare denial" uncharacterised): FIX, declaration only. The clause "which offers no component that responds to a change in what produces the appearance" is the only place in file 11 or the draft that says what makes a denial bare, and it is what puts N22's Wren under the exclusion and Yuri outside it; the declaration now carries it in NEW's words. OLD, NEW and KIND unchanged.
````

- **CASES AT RISK (append to the N22 line, exact):** "Atria C (point 3) reads the same move toward; with the clause declared, both halves are accounted for."
- **By program:** the note's line for file-11 L337 takes the new declaration. The counts, N and M are unchanged. The list of what the checks changed gains a row for W40.1.
- **Conflicts:** none. The sources note's "Elimination" line stays true, and R06 agrees.
- **Earlier rulings:** none on R25.
- **Ruling file:** `ruling s90_xexam_atria_C item 5 R25.md` (md5 c2b72cbeefd03e5e7dd7cf0641b44720).

### R30 (W41.1), point 3: KEEP (one ruling with Mimo C's)

- **Why contested.** The reply's line is STANDS. Under (d), it names declared moves toward the fixed verdicts on N21 ("she knows it, tacitly"; "her grasp of it was not handed to her") and on O15.
- **The checker** read Mimo C's reply and the sibling ruling on it, and wrote one reconciled ruling.
  - **N21** moves toward on both questions, and the declaration covers both. "Knows it, tacitly" comes from the no-format clause at L401. "Formed it herself" comes from the witness-by-use clause at L403.
  - **O15 does not move.** File 11 already gives AGREE (S81 determination 01), so R30 only adds support. Where the entry's CHECK says "O15 toward", it should be read as support for the passage only.
  - **Mimo's FALLS fails**, for the sibling ruling's reasons: a marked parallel; the binding has to take the deliberative rule's place, or N21 is lost; L401 and L399 still guard the map; "lie on" and "lands on" set the same condition.
  - **No case moves away.** N13, O14, O18, O23 and O32 all hold, and D3-T is untouched.
- **Text:** none changes. OLD, NEW, KIND (CLAIM) and DECLARATION stay as drafted.
- **CHECK: the one reconciled append (exact).** It covers both replies and replaces the Mimo C checker's line:

````text
Cross-examination of revision 2 (S90 part C): Atria said STANDS (declared moves toward on N21, 'she knows it, tacitly' and 'her grasp of it was not handed to her'; O15 kept a hole in the diagrams, not in Sam's construction). Mimo said FALLS (the witness criteria differ from Part IX's reason use: the binding for 'the operative deliberative rule', no structural map, 'lie on' for 'lands on'). Ruled KEEP after the cross-examination. N21 moves toward on both questions, as declared (no format for Deploy; a witness by use for Build). O15 holds at AGREE, which is file 11's mark (S81 01): R30 only supports the passage, and 'toward' above means no more than that. 'As reason use asks of an objection' is a marked parallel. The binding must replace the deliberative rule as specifier, because a verbatim copy would fail N21. (R)'s fidelity and provenance (L401), Build (L399) and the active-route clause keep the map's guard. 'In the manner of' already means 'modelled on'. No case moves away.
````

- **Earlier rulings:** none on R30.
- **Ruling file:** `ruling s90_xexam_atria_C item 6 R30.md` (md5 4703e729928f2ac500bfea3b07db0d12).

### R34 (W35.3), point 3: KEEP

- **Why contested.** The reply's line is STANDS. Under (d), it names a declared move toward the fixed verdict on N19, and it says the change also fits N18 and O27.
- **The entry.** W35.3, "Part X: what a recognized difficulty is". File-11 L421, revised L423. KIND CLAIM. REASON WORD clarification. CHECK: "check 2, SOUND. N19 is watched, not simply toward …; N18 Q1 is watched …"
- **The checker.**
  - **N19.** The move is real and points toward the fixed verdict, and the declaration covers it.
    - Q1 goes from SILENT under file 11 to AGREE: Odile's foreseen clash fits the second limb, a conflict she represents, with no reader or observation needed.
    - The CHECK's watch point does not bite. The limb holds whichever demand is declared claimed and which protected, and also when both are in O and P, and the situation supplies that declaration.
    - Only one step is a reading rather than forced: taking the question's "problem" as the text's "recognized difficulty".
    - Q2 holds or moves toward. What it turns on through (P) belongs to (P) and W5.1, not to this entry.
  - **N18.** Q1 moves toward for both designers, by the declared first limb. L516's "of a repair" names the same O and P, so there is no clash.
  - **O27** stays SILENT on "mostly". The reply's gloss "the expert's claimed diagnoses" is loose, because the diagnoses are candidates, not claimed obligations. Read as a failure of the robot's own diagnostic obligation, the point still holds.
  - **O12** stays SILENT, and D3-T is untouched.
  - **Quotations and coherence.** Every quotation checks, "(Part XI)" points to the right place, and L223 agrees with L423.
- **Text:** none changes.
- **CHECK (append, exact):**

````text
Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N19 (the foreseen clash is a represented conflict, a recognized difficulty before any reader), and said the change also fits N18 and O27. Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. N19 Q1 moves toward (SILENT to AGREE) by the declaration's second clause, under every declaration that puts one demand in O and the other in P (O = P included), which the situation supplies. It is a reading only in taking the question's "problem" as the recognized difficulty. N19 Q2 holds or moves toward: what it turns on through (P) is (P)'s and W5.1's, not this entry's. N18 Q1 moves toward for both designers by the first clause. L516's "of a repair" names the same O and P. O27 holds SILENT on "mostly": the robot's "fits neither" is a represented failure of its diagnostic obligation, and the expert's diagnoses are candidates, not claimed obligations. O12 holds SILENT: the failure was represented, and the need met was stated afterwards. D3-T is untouched. "(Part XI)" is exact, and L223's "can be a recognized difficulty (Part X)" agrees.
````

- **Earlier rulings:** none on R34, W35.3 or C29. The R12 and R13 rulings find W35.3 unaffected.
- **Ruling file:** `ruling s90_xexam_atria_C item 7 R34.md` (md5 e797c134e2ea366d478a0ca042889041).

## Reconciliation

### Within this batch

1. **R31 (W21.1): KEEP and KEEP.** The Atria B2 checker read the Mimo B2 ruling and wrote one CHECK append that covers both replies (given under Atria B2, R31). Only that append goes in. The Mimo B2 ruling's own append is contained in it word for word.
2. **R30 (W41.1): KEEP and KEEP.** The Atria C checker read the Mimo C ruling and wrote one reconciled ruling. Only its CHECK line goes in (given under Atria C, R30). The Mimo C ruling's own line is not appended.
3. **R13 (W35.2): FIX and FIX. The pass takes Mimo C item 4's text.**
   - **What the two rulings share.**
     - Both rest on the same ground: the expectation is typed only for a transport whose target is the simulation layer.
     - Both refuse \(\operatorname{Ans}_E\).
     - Both put the opening clause into the declaration.
     - Neither moves a case.
   - **Where they differ, in three places:**
     - "to the simulation layer" (Mimo C item 4) or "into the simulation layer" (Atria C item 1);
     - "a constructed one that fails" (Mimo C item 4) or "a constructed transport that fails" (Atria C item 1);
     - the declaration's wording.
   - **Why Mimo C item 4's text:**
     1. R12's FIX (Mimo C item 1), the only ruling on R12, writes "a transport to the simulation layer \(S\)". Both R13 rulings say that R12 and R13 must carry one scope. Mimo C item 4 was written against R12's fix ("'to' is kept for one wording across R12 and R13"; "Atria's 'into' says the same"). Atria C item 1 asks R12's checker to scope R12 to match, and R12's ruling uses "to".
     2. "A constructed one" keeps "violated" inside the scope the clause has just named (Mimo C item 4, "The colon's second half"). Atria C item 1 gives no ground for "a constructed transport". Its own reason, that the sentence "is narrowed to the scope that W35.1's REASON and L177 already give", is better served by the narrower instance.
     3. Mimo C item 4's declaration states the scope for the instance too: "a constructed transport to the simulation layer".
   - **What is taken from Atria C item 1.** Its reason paragraph goes into the REASON field. It is scope-neutral and names both calls.
   - **What goes into CHECK.** Mimo C item 4's CHECK line already names both calls. The pass adds after it one sentence, which the recorder wrote and which is not a checker's: "Atria C (item 1) ruled FIX to the same effect with 'into the simulation layer' and 'a constructed transport'; the batch-3 reading takes this wording, which R12's fix shares."
4. **R25 (W40.1): KEEP (Mimo C item 5) and FIX (Atria C item 5). The pass takes the FIX.**
   - **What the two rulings share.**
     - The clause is non-restrictive.
     - "Bare denial" is a new phrase, found only at revised L335.
     - The clause is true, and its ground is Part V's (E).
     - N22 moves toward, and nothing moves away.
     - Mimo's proposed repair is refused, because it is restrictive, paraphrases the clause and drops "bare".
   - **Where they differ.** The rulings differ on one question: whether the clause is a claim of its own that the declaration must carry.
     - Mimo C item 5 says no. The clause gives the ground of the declared verdict, and on every kind of denial the declaration and NEW reach the same verdicts.
     - Atria C item 5 says yes. The clause is the theory's only statement of what puts a denial under the exclusion, no conjunct of (E) "inspects a label" (L265), and batch 1's R51 test ("makes no claim of its own") fails.
   - **Why the FIX.**
     - The FIX's declaration inserts NEW's own clause word for word, and keeps it non-restrictive. So it meets the only objection the KEEP ruling makes to changing the declaration (its point 3, against a restrictive paraphrase that drops "bare"), and it describes the sentence that is there.
     - On the KEEP ruling's own test, a declaration that reaches the same verdicts as NEW is exact. The fuller declaration reaches the same verdicts, because it quotes NEW.
     - So the fuller declaration is exact on both rulings' tests, and the drafted one is exact on only one of them.
     - The FIX changes no theory text, no KIND and no case.
   - **This is the recorder's reconciliation of two rulings, not a third ruling.** If the orchestrator prefers, it can give both rulings to a fresh checker before the pass. Until then, the pass uses the FIX.
   - **What goes into CHECK.** Atria C item 5's CHECK line, followed by one sentence the recorder wrote: "A second checker (Mimo C, item 5) ruled KEEP on the same replies, finding the drafted declaration exact; the batch-3 reading takes the FIX, whose declaration quotes NEW's clause word for word and so is exact on both rulings' tests."

### With batches 1 and 2

- **R01 (W37.1)** is the only entry of this batch that batch 1 or batch 2 had ruled.
  - Batch 1's FIX (Mimo A1, point 3) and this batch's FIX (Atria A1, point 1) have the same NEW, KIND, DECLARATION, fallback line and REASON WORD.
  - Only the REASON's record sentence and the CHECK change, so that they name both calls.
  - Batch 1's pending item 1 is amended accordingly.
- **Batch-3 rulings that checked their agreement with batches 1 and 2, and agree:**
  - R21 agrees with R15's FIX (batch 1) and with R51's KEEP (batch 2).
  - R06 agrees with R28's FIX (batch 1: L371's typing of the criticism's connection as a candidate).
  - R52 agrees with the batch-2 and R51 rulings, which cite Derivation 3 "(L566, W17.3)" as unchanged support for O24.
  - R17 leaves Mimo A1's letter-\(G\) point (batch 1) with the orchestrator.
- **Not contested here, and consistent with batch-1 FIXes:** Atria A1's points 4 (R08) and 5 (R15, R20).
- **No batch-3 ruling conflicts with a batch-1 or batch-2 ruling.**

## Pending edits to the change list, batches 1–3 (cumulative)

**None of these is made now.** They are to be applied in one pass to `tests/Revision 2 - change list, draft of 23 September.md`. One line per entry. The exact texts are in the batch that ruled it: b1 is batch 1's reading, b2 batch 2's, and b3 this file. Each edit is marked in its entry as made after the cross-examination, with the call and point that raised it. After the pass, the draft is rebuilt by program, and then the counts, the note's N and M, the revision note and the layer-1 record are checked.

1. **W37.1 (R01), FIX [b1 item 1; b3, reconciled].** NEW deletes "blind". REASON WORD erratum → clarification. Fallback line as in b1. GAIN and LOSS as in b1. The REASON record sentence and the CHECK line are the b3 texts, which name Mimo A1 point 3 and Atria A1 point 1. The title change is optional.
2. **W19.1 (R08), FIX [b1 item 2].** NEW inserts the typing sentence after sentence 2. WHERE, REASON, LOSS and CHECK change as b1 gives them. The carried-forward finding on Part II notation is closed.
3. **W20.1 (R15), FIX [b1 item 3].** NEW adds ", whether or not anyone has described their work". DECLARATION, CHECK and REASON change as b1 gives them. CASES AT RISK O45 becomes "holds AGREE, on firmer text", with the two follow-ons at list L168 and L190.
4. **W24.1 (R26), FIX [b1 item 4].** The condition reads "for every admitted generator \(a\)". REASON and CHECK change as b1 gives them.
5. **W22.1 (R28), FIX [b1 item 5].** NEW and DECLARATION as b1 gives them, and the CHECK line and the "What the checks changed" line are added.
6. **W6.3 (R39), FIX [b1 item 6, amended in b2].** KIND WORDING → CLAIM, with the DECLARATION added. REASON's last clause and CHECK are b2's, naming both calls. Counts are made once: CLAIM 48 → 49, WORDING 5 → 4, group B1 13 → 14 of 15.
7. **W19.2 (R51), KEEP three times [b1 item 7, amended in b2].** No text changes. CHECK takes the task (a) line (b1) and the task (d) line (b2). CASES AT RISK takes the O36 sentence (b2), and Mimo's N25 "toward" is recorded beside "watched". The "differ in nothing but" change is optional.
8. **W58(ii).1 (R04), KEEP [b2 item 9].** No text changes. CHECK takes b2's line.
9. **W7.5 (R48), FIX [b2 item 10].** NEW inserts "(EK) also on (P), ". DECLARATION, REASON (the paragraph and the "Not corrected" sentence), CHECK and GAIN change as b2 gives them.
10. **W35.1 (R12), FIX [b3].** NEW's preamble becomes "Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\)." The three bullets are unchanged. DECLARATION and CHECK are b3's.
11. **W35.2 (R13), FIX [b3, reconciled].** NEW, DECLARATION and CHECK are Mimo C item 4's, and the CHECK is followed by the recorder's reconciliation sentence. REASON adds Atria C item 1's reason paragraph. OLD, KIND and REASON WORD are unchanged. Apply together with item 10.
12. **W40.1 (R25), FIX, declaration only [b3, reconciled].** DECLARATION is Atria C item 5's. CHECK is Atria C item 5's line, followed by the recorder's reconciliation sentence. CASES AT RISK, N22, takes Atria C item 5's sentence. OLD, NEW and KIND are unchanged.
13. **W21.1 (R31), KEEP [b3].** No text changes. CHECK takes the one reconciled append (Atria B2 item 2), which covers both replies.
14. **W17.3 (R52), KEEP [b3].** No text changes. CHECK takes Mimo B2 item 2's note.
15. **W45.1 (R07), KEEP [b3].** No text changes. CHECK takes Mimo C item 2's line.
16. **W41.1 (R30), KEEP [b3].** No text changes. CHECK takes the one reconciled line (Atria C item 6). The entry's "O15 toward" is read as support for the passage only.
17. **W17.2 (R42), KEEP [b3].** No text changes. CHECK takes Atria B2 item 1's line. Optional: bring the heading into line with NEW ("candidate transports").
18. **W13.1 (R32), KEEP [b3].** No text changes. CHECK takes Atria B2 item 3's W13.1 line.
19. **W13.2 + W12.2 (R33), KEEP [b3].** No text changes. CHECK takes Atria B2 item 3's W13.2 + W12.2 line.
20. **W20.2 (R17), KEEP [b3].** No text changes. CHECK takes Atria A1 item 2's line. Optional: CASES AT RISK O33 takes the "toward" reading.
21. **W36.1 (R06), KEEP [b3].** No text changes. CHECK takes Atria C item 2's line.
22. **W58(i).1 (R21), KEEP [b3].** No text changes. CHECK takes Atria C item 3's line.
23. **W33.1 (R24), KEEP [b3].** No text changes. CHECK takes Atria C item 4's line. Housekeeping: reconcile CASES AT RISK (O2's struck sentence; O19) with CHECK.
24. **W35.3 (R34), KEEP [b3].** No text changes. CHECK takes Atria C item 7's line.
25. **"What the checks changed".** Add a part headed as after the cross-examination (S90), with one row for each of the 10 fixed entries: W37.1, W19.1, W20.1, W24.1, W22.1, W6.3, W7.5, W35.1, W35.2 and W40.1. Give each row its calls and points. The W37.1 row names Mimo A1 point 3 and Atria A1 point 1. The W6.3 row names Atria B1 point 1 and Mimo B1 point 2. The W35.2 row names Mimo C point 4 and Atria C point 1. The W40.1 row names Atria C point 3 and Mimo C point 5.
26. **"Counts", the bullet "The checks".** Every batch is now read, so it gains the S90 totals:
    - ten calls, all accepted (five of them in pass 2 after the restart);
    - 32 rulings on 24 entries: 10 entries fixed, 14 kept, none dropped;
    - 22 changes contested by at least one reply, 2 more (R32, R33) listed and ruled KEEP although found not contested, and 31 contested by neither reply.
27. **By program, after the pass.**
    - The counts become CLAIM 49, WORDING 4, ORDER 2, and the note reads N = 49 of M = 55 (from W6.3 alone).
    - The note's lines follow the new declarations of R2-12, R2-13, R2-15, R2-25, R2-28, R2-39 and R2-48, and W6.3 gains its second L447 line.
    - Row R2-01's reason column becomes "clarification".

**Passed to the orchestrator, not edits** (batches 1–3):
- R17's letter \(G\) (Mimo A1, point 4). If a new letter is adopted, it also replaces \(G\) in W20.2's CHECK fallback (b3).
- R17's L339 names no block (Atria A1, point 3). An optional notation point; if adopted, a new entry (b3).
- R55's bijection (Mimo A2, point 2; exhibited by Atria A2, point 1). Neither reply contests R55.
- Revised L51, "as a declared normative relation" (b1, from the R39 ruling).
- R10's "the ground of its restriction" at L159 (Mimo B1, point 4).
- R03's bolded "declared inputs" at L31, before any gloss (Mimo B1, point 5).
- What an active route depends on (b2, from the R48 ruling).
- A sentence at Part IV (L189) or (R) (L205–208) saying when a transport into c is faithful on c's contract (b3, from both R31 rulings). It concerns file-11 text outside the 55 changes.
- R13 and R25: the recorder's reconciliations (above), which the orchestrator may send to a fresh checker before the pass.

## Coverage: the 55 changes, the two replies to each, and the rulings

Each change is in one part, and each part went to both models. All ten calls were accepted, so no change is "not examined" by a model under Parts rule 5.
- **"No line"** means the reply gave the change no closing line: Mimo A1 on 5 changes, and Mimo B1 on 10. None of these 15 is the subject of a point. Three are mentioned in passing: Mimo A1 calls R20 "consistent with R15", and Mimo B1 cites R02 and R38 in its points on R03 and R39. Silence is not support (S90 rule 5), so these changes do not count as examined and upheld by that reply.
- **The ruling** is the one after reconciliation. b1, b2 and b3 name the batch.

| id | entry | part | Mimo | Atria | contested by | ruling |
|---|---|---|---|---|---|---|
| R01 | W37.1 | A1 | STANDS | FALLS | Mimo A1 pt 3 (undeclared, one reading); Atria A1 FALLS | FIX (b1; b3, same text) |
| R02 | W6.1 | B1 | no line | STANDS | — | none (not contested) |
| R03 | W7.1 | B1 | STANDS | STANDS | — | none (not contested) |
| R04 | W58(ii).1 | B1 | FALLS | STANDS | Mimo B1 FALLS | KEEP (b2) |
| R05 | W8.1 | A1 | no line | STANDS | — | none (not contested) |
| R06 | W36.1 | C | STANDS | STANDS | Atria C pt 3 (N3 toward) | KEEP (b3) |
| R07 | W45.1 | C | FALLS | STANDS | Mimo C FALLS | KEEP (b3) |
| R08 | W19.1 | A1 | FALLS | STANDS | Mimo A1 FALLS | FIX (b1) |
| R09 | W30.1 | A1 | no line | STANDS | — | none (not contested) |
| R10 | W57.1 + W32(b).1 | B1 | STANDS | STANDS | — | none (not contested) |
| R11 | W17.1 | B2 | STANDS | STANDS | — | none (not contested) |
| R12 | W35.1 | C | FALLS | STANDS | Mimo C FALLS | FIX (b3) |
| R13 | W35.2 | C | STANDS | FALLS | Mimo C pt 4 (undeclared clause); Atria C FALLS | FIX (b3, two rulings reconciled) |
| R14 | W35.4 | C | STANDS | STANDS | — | none (not contested) |
| R15 | W20.1 | A1 | STANDS | STANDS | Mimo A1 pt 2 (O45, one reading) | FIX (b1) |
| R16 | W39.1 | A1 | no line | STANDS | — | none (not contested) |
| R17 | W20.2 | A1 | STANDS | STANDS | Atria A1 pt 2 (O33 toward) | KEEP (b3) |
| R18 | W11.1 | B1 | no line | STANDS | — | none (not contested) |
| R19 | W9.1 | A1 | no line | STANDS | — | none (not contested) |
| R20 | W20.3 | A1 | no line | STANDS | — | none (not contested) |
| R21 | W58(i).1 | C | STANDS | STANDS | Atria C pt 3 (O45 toward) | KEEP (b3) |
| R22 | W28.1 | B2 | STANDS | STANDS | — | none (not contested) |
| R23 | W34.1 | C | STANDS | STANDS | — | none (not contested) |
| R24 | W33.1 | C | STANDS | STANDS | Atria C pt 3 (N1 toward) | KEEP (b3) |
| R25 | W40.1 | C | STANDS | STANDS | Mimo C pt 5 (undeclared description); Atria C pt 3 (N22 toward) | FIX, declaration only (b3; KEEP and FIX reconciled to FIX) |
| R26 | W24.1 | A2 | STANDS | STANDS | Mimo A2 pt 4 (undeclared, one reading) | FIX (b1) |
| R27 | W31.1 | A2 | STANDS | STANDS | — | none (not contested) |
| R28 | W22.1 | A2 | FALLS | STANDS | Mimo A2 FALLS | FIX (b1) |
| R29 | W22.2 | A2 | STANDS | STANDS | — | none (not contested) |
| R30 | W41.1 | C | FALLS | STANDS | Mimo C FALLS; Atria C pt 3 (N21, O15 toward) | KEEP (b3, one ruling) |
| R31 | W21.1 | B2 | FALLS and FALLS (two lines) | STANDS | Mimo B2 FALLS; Atria B2 pt 3 (O11, O18, O31, N15, N21 toward) | KEEP (b3, one ruling) |
| R32 | W13.1 | B2 | STANDS | STANDS | Atria B2 pt 5 (listed; found to name no move) | KEEP (b3) |
| R33 | W13.2 + W12.2 | B2 | STANDS | STANDS | Atria B2 pt 5 (listed; found to name no move) | KEEP (b3) |
| R34 | W35.3 | C | STANDS | STANDS | Atria C pt 3 (N19 toward) | KEEP (b3) |
| R35 | W23.1 | B2 | STANDS | STANDS | — | none (not contested) |
| R36 | W5.1 | B2 | STANDS | STANDS | — | none (not contested) |
| R37 | W23.2 | B2 | STANDS | STANDS | — | none (not contested) |
| R38 | W6.2 | B1 | no line | STANDS | — | none (not contested) |
| R39 | W6.3 | B1 | FALLS | FALLS | Atria B1 FALLS; Mimo B1 FALLS | FIX (b1, b2, one ruling) |
| R40 | W12.1 | B2 | STANDS | STANDS | — | none (not contested) |
| R41 | W25.1 | A2 | STANDS | STANDS | — | none (not contested) |
| R42 | W17.2 | B2 | STANDS | STANDS | Atria B2 pt 1 (O24, N5 toward) | KEEP (b3) |
| R43 | W25.2 | A2 | STANDS | STANDS | — | none (not contested) |
| R44 | W7.2 | B1 | no line | STANDS | — | none (not contested) |
| R45 | W6.4 + W14.1 | B1 | no line | STANDS | — | none (not contested) |
| R46 | W7.3 | B1 | no line | STANDS | — | none (not contested) |
| R47 | W7.4 | B1 | no line | STANDS | — | none (not contested) |
| R48 | W7.5 | B1 | STANDS | STANDS | Mimo B1 pt 3 (undeclared, one reading) | FIX (b2) |
| R49 | W15.1 | B1 | no line | STANDS | — | none (not contested) |
| R50 | W11.2 | B1 | no line | STANDS | — | none (not contested) |
| R51 | W19.2 | A2 | STANDS | STANDS | Mimo A2 pt 3 and task (d); Atria A2 pt 2 (O24, O36, O46 toward) | KEEP (b1 twice, b2) |
| R52 | W17.3 | B2 | STANDS | STANDS | Mimo B2 pt 2 (under-declared) | KEEP (b3) |
| R53 | W7.6 | B1 | no line | STANDS | — | none (not contested) |
| R54 | W10a.1 | A2 | STANDS | STANDS | — | none (not contested) |
| R55 | W19.3 + W10(b).1 | A2 | STANDS | STANDS | — | none (not contested) |

**In numbers.**
- **Lines.** Mimo gave 40 closing lines on the 55 changes: FALLS 8 (R04, R07, R08, R12, R28, R30, R31, R39), with R31 given two lines, and STANDS 32; 15 changes have no line. Atria gave 55 lines: FALLS 3 (R01, R13, R39) and STANDS 52.
- **FALLS lines upheld by a FIX:** R01, R08, R12, R13, R28 and R39 (both lines). **Answered by a KEEP:** R04, R07, R30 and R31.
- **Contested by at least one reply:** 22 changes. 2 more (R32, R33) were listed and ruled KEEP, found not contested. That makes 24 ruled. The other 31 were contested by neither reply.
- **OVERALL lines.** Mimo gave NEEDS REPAIR on all five parts. Atria gave SOUND on A2 and B2, and NEEDS REPAIR on A1, B1 and C.

## What is still to come

- **Every S90 part has now been read for both models:**
  - batch 1: Mimo A1, Mimo A2 and Atria B1;
  - batch 2: Atria A2 and Mimo B1;
  - batch 3 (this file): Mimo B2, Mimo C, Atria B2, Atria A1 and Atria C.
- **The pass on the change list** is made once, from the cumulative list above, and the draft is then rebuilt by program and checked.
- **The two S87 rows** in the same rerun, O5 and O30, are read in `results/S81 File 11 against every case - outputs/determination/10 Reading of Mimo's retry - O5 and O30.md`.

Dated 24 September 2026.
