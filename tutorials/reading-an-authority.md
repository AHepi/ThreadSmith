# Reading an authority

**TERM: Authority.** The thing actually under test at a research state. Preserved once used; superseded by a new file, never edited in place.

## Plain-language meaning
When a test plan says "Authority document: 'Claude Fable Semantics - standalone theory' (file 10). Frozen.", it is naming the fixed point the whole test leans on. If the authority moved during the test, the result would mean nothing.

## Tiny demonstration
Open [38 The ledger language - complete definition.md](<../Language/authority/38 The ledger language - complete definition.md>). The first lines say what it is for and name the three roles that stay apart: translator, checker, read-back. There is no history in it; log 36 records that it was "checked by program for leftover history: none". That is what a clean authority looks like: one file, one version, nothing to reconcile.

Now open the log in the [project story](<../records/Checked reasoning language - project story.md>) at entry 38: "The clean language file updated for the two changes: a fourth standing, TOLD in a named world; 'cannot tell' under SO THAT; two new traps. Output: '38 The ledger language - complete definition.md', which supersedes file 36." So 38 replaced 36, which (log 36) replaced rulebook 34, which replaced 33, 23 and 20. None of the older ones are in this repository; the log describes each.

## Contrast
- **Authority is not a test.** File 38 defines the language. It gives no task. File 39, the translator prompt, is what you hand over with it, and a plan such as 37 says what was expected of a run.
- **Authority is not the record.** The project story tells you how 38 came to be; 38 itself says only what the language is.
- **An authority can be missing.** The semantics' authority document (file 10, and the revised 20) is not in either bundle. [Semantics/authority/](<../Semantics/authority/>) says so rather than pretending.

## Where to find it
`<project>/authority/`. The project's `INDEX.md` says which one is current and what it superseded.

## Follow the chain
Authority (38) -> Test ([37 Test plan](<../Language/tests/37 Test plan - blind sample from the literary stress test.md>)) -> Raw result (`Language/rigs/rig 1 - arguments/raw_log.txt`, ledgers `T..`) -> Interpretation ([37 Test results](<../Language/results/37 Test results - blind sample from the literary stress test.md>)) -> Lesson (log 37: the miss on a told story, fixed by patch 15 and written into 38).
