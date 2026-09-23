# S80 Plan - third version, cut to a quick verdict

Written 23 September 2026 by Claude, on the owner's word (decision S13): "HV isn't the central job. Working on the semantics is. Just a quick verdict is enough. And you are the authority, not Mimo or Atria. You make the big decisions." Frozen at commit; not edited after the first reader call. The second version (hash f5243244f7554ea2) stays beside it, unrun; its second cross-examination was stopped unreturned when the round was cut.

## What is run
- Readers: Atria, Mimo, DeepSeek, by API, thinking on (`reasoning_effort` high), temperature 0.7, the second version's request shape and acceptance test (finish "stop" and END OF REPORT).
- Conditions: ST, the skill (13,648 words as sent); PT, the placebo "Careful review" (length-matched, same framing sentence); NT, a one-line system prompt. The reader task is the second version's neutral one.
- Document: the seeded one only (eight planted errors, four of the skill's kind and four ordinary; D3 the natural error). False alarms are read from the seeded reports' other items ("under load").
- Three repetitions: 27 reports. No Opus arm, no clean document, no thinking-off cells.
- Marking: one marker per report, never the reader's own model (Atria's reports by Mimo, Mimo's by Atria, DeepSeek's by Atria, Mimo, Atria for r1 to r3), with the second version's marker task, fenced report, and key with the kind labels removed. Claude then reads every mark against its report and the key, overrules where the mark is wrong (each overrule listed with the report's words), and gives the verdict.
- Tool: `tools/s80_quick.py` (readers, mark, table), reusing the second version's caller, texts, key slicer and validator.

## The verdict, and how it is read
The question is skill against placebo on HV errors found, with thinking on. **Keep** the skill as an audit aid if it beats the placebo on HV by at least one error per report on average on at least two of the three readers, without more MISTAKEN items. **Abandon** it as an audit aid if it does not beat the placebo on HV on any reader (nothing is lost by using the placebo or nothing in its place). Otherwise **no verdict at this size**, said as such, and the skill stays as it is, unused in audits until a case calls for it. With three repetitions a difference of one error is at the edge of noise; the results say so. Scope: these planted kinds, on this document, for auditing; the plants and rules are the skill author's own.

## Predictions
The sealed list (Q1 to Q5) and the sealed addendum (Q6 to Q9) stand as written; they are read against the cells that were run and marked "not run" where their cells were cut.

## Not tested
Thinking off; the clean document; Opus; everything in the second version's "Not tested".
