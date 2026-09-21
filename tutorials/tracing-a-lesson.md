# Tracing a lesson

**TERM: Lesson.** Something that failed while being made or tested, and how it was fixed. Only failures; each points at evidence.

## Plain-language meaning
A lesson is worth little on its own. Its value is that you can walk from it back to the test that exposed the failure and forward to the file that fixed it.

## What to open
Open the project's Lessons file in `records/` at any entry. It names the thing that failed, how the failure showed, and the fix. Then walk it:

Back:
1. **The thing that failed:** the file (an instruction, a plan, a rule) named in the lesson, in `tests/` or `authority/`.
2. **The evidence:** the run or return that showed it, in `results/` or `rigs/`, or the log entry that counts it where the evidence is not in the repository.
3. **Why it counts as a failure:** the earlier entry or result the failure contradicts.

Forward:
4. **The fix:** the later numbered file the lesson names.
5. **What the fix gives up:** the "gives up" line for it, in the log or in the project's list of patches.
6. **Where it went next:** the log entry that first used the fix.

## Contrast
- **A lesson is not a decision.** Decisions are the owner's instructions in the owner's words. A lesson is what broke.
- **A lesson is not a synthesis.** It is tied to one authority, one test, one run. If the same pattern shows up across several states, that is for a later synthesis, which is a separate file when it exists.

## Follow the chain
Authority (as it stood) -> Test (the file that failed) -> Raw result (the evidence) -> Interpretation (the log entry that read it) -> Lesson -> Next authority (the fix).
