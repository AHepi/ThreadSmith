# 05 How the cross-examination will be read, written before sending

*Written by Claude on 23 September 2026, before the cross-examination brief was sent to Atria or Mimo, and committed with the brief and its job list before either call is sent. No reply existed when it was written.*

## What is sent

- **The brief:** `Semantics/tests/S87 Cross-examination - the S81 determination, file 11 against file 10.md` (md5 6acd78f5217acf2ce4e95acdbc1454f3, sha256 8e70216af88f…; 25,477 words by `wc -w`, 25,536 by the runner's count). It is sent whole, as the one user message, once to Atria and once to Mimo, and neither sees the other's reply.
- **The job list:** `Semantics/tools/s87_jobs - S81 determination cross-examination.json`, run by `tools/s87_run.py`:
  - `s87_xexam_atria`: Atria, effort medium, max_tokens ladder [65536, 65536], max_pass 1, max_rejects 3;
  - `s87_xexam_mimo`: Mimo, effort medium, max_tokens ladder [131072, 131072], max_pass 1, max_rejects 3.
- **Where the replies land:** `Semantics/results/S87 Cross-examination - the S81 determination - returns/`.
- **What the brief holds:** file 11 in full (md5 5e494c1095d920d128b9a79de378f923, checked on the embedded block); file 10, excerpted, with line numbers; all 52 cases from the case book; the plan's rules word for word (the words Claude rules with, P1 to P4, tests (a) to (d), the standing clauses) and the Stage 1 mark rules; seven pressed rows (O5, O30, O17, O35, O40, O48, O45), each with its case, the determination's ruling and reasons, the verifiers' contrary readings and the marks; the determination's summary; the tasks.
- **Names in the brief.** The brief names no model, because it is sent whole to the two auditors whose own Stage 2 marks it reports. In it, the determiner is "the determiner", Atria is "auditor 1" and Mimo is "auditor 2". Quotations from the plan and the determination carry those substitutions in square brackets.

## The rule

1. **The replies are evidence, not results.** No reply changes a ruling by itself.
2. **Every row where either reply says RULING FALLS, and every new away-row either reply names, is re-read from the texts by a fresh Claude determiner.** The determiner reads file 10, file 11, the case book, the determination (04 and its raw readings) and the reply. It first states the determination's ruling, then the reply's argument, and then rules.
3. **A change of ruling is recorded** with its reason, and with the fact that it came after the cross-examination.
4. **If a changed row is a theory change away** from the thoughtful person, test (b) fails, and the standing verdict is re-applied under the plan's three clauses.
5. **A failed call supports nothing.** A call not accepted within its one pass (finish "stop" and `END OF REPORT` on the last line, as `tools/s80_call.py` accepts) counts neither for nor against the determination, and no ruling cites it.
6. **The two replies are read independently.**

The brief's header notes carry this rule for the record, in words that name no model.

## Beside the rule

- A reply's points under tasks 3 and 4 (the standing clause, the P2 scoring choice, anything else) are evidence of the same kind. S81 Results answers each point that would change a test, a prediction's score or the clause applied, with its reason.
- Rows named in 04 section 7.11 but not pressed in the brief: O21 and O27. Both are SILENT in both files, so a change on either could only be toward the thoughtful person. Either reply may still raise them under task 2 or 4.
- The supplementary audit of Mimo on tester A is read under its own reading rule and is not part of this cross-examination.
