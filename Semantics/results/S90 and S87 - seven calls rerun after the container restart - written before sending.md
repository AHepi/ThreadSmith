# S90 and S87: seven calls rerun after the container restart

*Written by a Claude subagent for the orchestrator on 23 September 2026, from about 23:40 UTC, before any of the seven calls was sent again. It is committed with the job list `tools/s90 and s87 jobs - rerun after restart.json`, before the runner is started. When it was written, no pass-2 file of any of the seven tags existed.*

*What the writer opened and did not open.*
- **Opened:**
  - the receipt and the error file of each of the seven calls;
  - the two runner logs of 23 September (the S90 parts run and the S87 retry run);
  - the two original job lists, `tools/s87_run.py` and `tools/s80_call.py`;
  - `results/S90 Parts - how they will be read, written before sending.md`, rule 4 of the S90 rule, and rule 5 of 05, and 05c in full;
  - the 60-character content of Mimo B2's pass-1 attempt 2 (the provider's refusal notice, seen while listing the files; attempt 3's content is empty).
- **Not opened:** any reasoning file; any reply or reading of any part or row; any other attempt file.

## 1. What happened

**The container restarted at about 23:30 UTC on 23 September 2026.** Two runners were then going, and both had been started before the restart:
- the S90 parts run (`tools/s90_jobs - revision 2 draft in five parts.json`, started 21:33:45);
- the S87 Mimo retry run (`tools/s87_jobs - Mimo retry, one row per call.json`, started 22:33:06).

Both kept the proxy settings they were started with. Those named the agent proxy at `127.0.0.1:34733`. After the restart the proxy is at another port, so from then on every attempt of both runners was refused.

**The cut, reconstructed from the receipts.** The times below come from each receipt's attempt history, the runner's back-off between failed attempts (20, 40, 80, 120 and 120 s) and the time each call ended in its runner's log. They are good to about a second.
- At about **23:31:13**, the attempt in flight of six calls lost its connection with no reply: Atria A1 (attempt 5), Atria B2 (2), Atria C (1), Mimo B2 (4), O5 (1) and O30 (1).
- Mimo C's attempt 2 had waited 2,765 s for a Mimo slot. It got one at about 23:31:18 and was refused at once.
- **Every attempt after that was refused at once** (0.0 s). The back-off used up each call's remaining attempts, and the seven calls ended as failed **between 23:33 and 23:37**.

**Each error file ends with the same failure** (the host is the provider's: Atria's or Mimo's):

```
ProxyError(MaxRetryError('HTTPSConnectionPool(host=…, port=443): Max retries exceeded with url: /v1/chat/completions (Caused by ProxyError('Unable to connect to proxy', NewConnectionError("HTTPSConnection(host='127.0.0.1', port=34733): Failed to establish a new connection: [Errno 111] Connection refused")))'))
```

| tag | provider | pass 1 asked (UTC) | ended (UTC) | error file's first line | attempts refused at once by the proxy |
|---|---|---|---|---|---|
| `s90_xexam_atria_A1` | Atria | 21:33:45 | 23:33:13 | status 0 after 6 attempts (0 came back but were not accepted) | 6 |
| `s90_xexam_mimo_B2` | Mimo | 22:15:45 | 23:35:13 | status 0 after 6 attempts (2 came back but were not accepted) | 5, 6 |
| `s90_xexam_atria_B2` | Atria | 22:37:38 | 23:37:13 | status 0 after 6 attempts (0 came back but were not accepted) | 3 to 6 |
| `s90_xexam_mimo_C` | Mimo | 22:22:08 | 23:37:18 | status 0 after 6 attempts (0 came back but were not accepted) | 2 to 6 |
| `s90_xexam_atria_C` | Atria | 23:19:21 | 23:37:33 | status 0 after 6 attempts (0 came back but were not accepted) | 2 to 6 |
| `s87_xexam_mimo_O5` | Mimo | 22:33:06 | 23:37:33 | status 0 after 6 attempts (0 came back but were not accepted) | 2 to 6 |
| `s87_xexam_mimo_O30` | Mimo | 22:33:06 | 23:37:33 | status 0 after 6 attempts (0 came back but were not accepted) | 2 to 6 |

**Attempts before the cut.**
- **Mimo B2 had two replies that came back and were rejected:**
  - attempt 2: status 200, finish `content_filter`, 60 characters, after 1,111.2 s (about 22:41);
  - attempt 3: status 200, finish `length`, no content, after 2,291.9 s (about 23:19).

  Their attempt files are `s90_xexam_mimo_B2.pass1.a2.*` and `.pass1.a3.*`.
- **Some attempts ended before the cut with no reply** (status 0, nothing came back):
  - Atria A1, attempts 1 to 4 (1,802.6, 1,802.3, 1,802.3 and 1,297.2 s);
  - Atria B2, attempt 1 (1,802.5 s);
  - Mimo B2, attempt 1 (395.7 s);
  - Mimo C, attempt 1 (1,364.6 s).

  Atria A2 and B1 had attempts like these in the same run before their accepted replies came back (A2: three of about 1,802 s; B1: one of 1,802 s and one of 1,094 s).
- **No other attempt of the seven brought anything back.**

**What was committed.** The seven calls' error files, receipts, attempt files and any request not yet committed went in at **1feb425**. The requests of Atria A1, O5 and O30 were already committed (d8ee479 and 2155d0f), and the runner rewrote them unchanged.

**The providers answer now.** At 23:42 UTC, from a shell started after the restart, a request with no key to each provider's `/v1/chat/completions` returned 401 from both.

## 2. The ruling

Claude decides this under decision S18.

1. **A failure caused by the session's own network being cut is not a reply from the model, and it does not use up the call.**
   - The seven calls did not fail on anything a model did. Each pass 1 was ended by the cut: the attempt in flight lost its connection, and every attempt left was refused by a proxy address that no longer existed.
   - The rules each part carries say a failed call supports nothing (S90 rule 4; S90 Parts rule 5; 05 rule 5 and 05c item 2). Those rules are about calls the models did not answer acceptably. They do not reach a pass cut short by the session itself.
2. **Each of the seven is sent once more, as pass 2.**
   - It goes with the same brief bytes and the same settings: the same provider, effort, ladder, attempts, `max_rejects`, note and out folder. Only `max_pass` goes from 1 to 2, so that the runner allows the pass.
   - This note is the new note, written before sending, that S90 rule 4 and S90 Parts rule 5 ask for before a part is rerun. For O5 and O30 it is the note that allows a pass the S87 retry job list did not.
   - There is no pass 3.
3. **Mimo B2's two rejected attempts are recorded as model failures within pass 1.**
   - They came back from the model and failed the runner's acceptance: `content_filter`, and `length` with no content.
   - They stay on the record with pass 1, are reported with the result of B2 for Mimo, and are not read for arguments (S90 Parts rule 5).
   - Pass 2 gets the runner's usual allowance of 6 attempts and at most 3 rejected replies. So Mimo B2 may have up to five rejected replies across the two passes. That is stated here, not hidden (section 4).
4. **Each reply is read by the rule its part already had.**
   - S90 parts (Atria A1, B2 and C; Mimo B2 and C): the S90 rule (`results/S90 How the cross-examination of the revision 2 draft will be read - written before sending.md`) and `results/S90 Parts - how they will be read, written before sending.md`, each reply independently of every other.
   - S87 rows (O5 and O30): rules 05, 05b and 05c in `results/S81 File 11 against every case - outputs/determination/`, with 05c item 7's independence rules.
   - The pass-2 reply stands where the pass-1 reply would have stood. Nothing else in those rules changes.
5. **A pass-2 failure supports nothing.**
   - A pass-2 call the runner does not accept counts neither for nor against any change or ruling.
   - Its attempt files are kept and not read for arguments.
   - Its part's changes are reported as not examined by that model (S90), or its row as not examined by Mimo (S87).
   - This holds whatever the cause, a second cut of the network included. Any further send would need its own note, written before sending.

## 3. What is sent

**The job list.** `tools/s90 and s87 jobs - rerun after restart.json` (sha256 dfd30a792ca1c426799b2e7d1ec15880d4c836cd4352f1205c4f4bea2aae8e60). It has purpose "audit" and seven jobs. Each job was copied field for field from its original job list, and a program checked that `max_pass` (now 2) is the only field that differs:
- Atria A1, B2 and C and Mimo B2 and C come from `tools/s90_jobs - revision 2 draft in five parts.json` (sha256 43d62bcf49bc…);
- O5 and O30 come from `tools/s87_jobs - Mimo retry, one row per call.json` (sha256 2e2e61c841f8…).

| tag | brief, in `tests/` | brief sha256 (first 12) = pass 1's `user_sha256` | effort | ladder | out folder |
|---|---|---|---|---|---|
| `s90_xexam_atria_A1` | `S90 Cross-examination - part A1, errata and pointers, Parts 0 to VI.md` | 8e7b98f33710 | medium | 65,536, 65,536 | `results/S90 … - returns/parts/` |
| `s90_xexam_atria_B2` | `S90 Cross-examination - part B2, ownership, repair, selection, newness.md` | 55d498b3fcee | medium | 65,536, 65,536 | the same |
| `s90_xexam_atria_C` | `S90 Cross-examination - part C, source-derived clarifications.md` | a94c8ef9ead3 | medium | 65,536, 65,536 | the same |
| `s90_xexam_mimo_B2` | part B2, as above | 55d498b3fcee | medium | 131,072, 131,072 | the same |
| `s90_xexam_mimo_C` | part C, as above | a94c8ef9ead3 | medium | 131,072, 131,072 | the same |
| `s87_xexam_mimo_O5` | `S87 Cross-examination - retry, O5 alone.md` | 97297d856d51 | medium | 131,072, 131,072 | `results/S87 … - returns/Mimo retry one row per call/` |
| `s87_xexam_mimo_O30` | `S87 Cross-examination - retry, O30 alone.md` | a6db38cc09e2 | medium | 131,072, 131,072 | the same |

**The job settings.**
- Every job has 6 attempts, `max_rejects` 3 and `max_pass` 2.
- Thinking is on. The temperature is 0.7, and there is no system text.
- Every brief is unchanged since its commit (4901a65 for the S90 parts, ff36cd4 for the S87 rows), and its sha256 equals the `user_sha256` of its pass-1 receipt.

**The dry run.** It was run with no keys set, sent nothing and left `git status` unchanged. It showed all seven as **pass 2 of at most 2**, with nothing already in the way of any file pass 2 may write: 7 calls, Atria 3 and Mimo 4.

**Pass 1's files are kept.** Before sending, the runner renames each call's pass-1 receipt, error file and request to its pass-1 name, for example `s90_xexam_atria_A1.receipt.json` → `s90_xexam_atria_A1.pass1.receipt.json`. That is 21 renames in all, none of them over an existing file. The files as first written stay in history at 1feb425 (and at d8ee479 and 2155d0f for three of the requests). Mimo B2's `pass1.a2` and `pass1.a3` files are not touched. Pass 2's rejected replies, if any, go to `<tag>.pass2.a<n>.*`.

**Slots.** No other runner is alive. At most three calls are in flight to each provider across every process. The three Atria calls start at once. Mimo B2, Mimo C and O5 take the three Mimo slots, and O30 waits in the runner's queue until one of them ends.

**The requests.** The pass-2 request of each call is expected to be byte-identical to its pass-1 request, since the body is built from the same brief and settings. That is checked against each pass-1 receipt's `request_sha256` when the pass-2 requests are committed.

## 4. Confounds, stated before the data

- **More chances.** These seven calls get a second pass, and the other S90 parts and S87 rows had one. An accepted reply is still one that happened to finish "stop" with END OF REPORT within the ceiling. Mimo B2 has already shown two failures (`content_filter`, then a reply that ran into the 131,072-token limit), and pass 2 may add up to three more before one is accepted.
- **Timing.** Pass 2 goes out after other replies came back and after some were read (S90 batch 1 at fbcef8c; Atria A2 and Mimo B1, and O17, returned at c137e86). The models see none of them. The readers follow the independence rules of their parts: S90 Parts rule 1, and 05c item 7.
- **The same model has seen the same text before.** Each pass-2 call is new and carries no earlier attempt, as in 05c section 7.
- **Atria's long silences.** Atria's pass-1 attempts of about 1,802 s may recur in pass 2, and six attempts may not be enough.

## 5. Lesson candidate

**A restart cuts the network for runs already going; runs must be relaunched after a restart.**
- A process started before the restart keeps the old proxy address, and every connection it opens afterwards is refused.
- The runner counts each refusal as a failed attempt. Its back-off used up the six attempts of each of the seven calls within about six minutes of the cut.
- The candidate rule: after a container restart, check every runner that was going, and relaunch from a shell started after the restart any call it had not finished. A call that failed on the dead proxy is sent again under a note written before sending, like this one.

## Decided

Decided by Claude under decision S18, 23–24 September 2026.
