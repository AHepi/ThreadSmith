# Reading an authority

**TERM: Authority.** The thing actually under test at a research state. Preserved once used; superseded by a new file, never edited in place.

## Plain-language meaning
When a test plan opens with "Authority: <file NN>. Frozen.", it is naming the fixed point the whole test leans on. If the authority moved during the test, the result would mean nothing.

## What to open
1. The project's `authority/`. The INDEX says which file is current and what it superseded. A clean authority is one file, one version, with no history in it; the history is in the log.
2. The log entry with the authority's number, in the project's `records/`. It says what changed from the version before, and what forced the change.
3. A test plan in `tests/` that names it. The plan's first lines name the authority and say that they were written before the run.

## Contrast
- **Authority is not a test.** The authority defines the thing; a plan says what was expected of a run against it.
- **Authority is not the record.** The log tells you how the authority came to be; the authority itself says only what the thing is.
- **An authority can be missing.** A project's `authority/` says so, with a note naming what is absent and the log entry that describes it, rather than pretending.

## Follow the chain
Authority (file NN) -> Test (a later plan naming NN) -> Raw result (the run, kept as it came) -> Interpretation (the results file, and the log entry of the same number) -> Lesson (what failed and what fixed it; often the next authority).
