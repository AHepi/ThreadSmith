---
name: planning
description: Chooses what to do next in research on a claim, a skill or a workflow - which claim to put under test, which tests to run and in what order, how many times and when to stop, what to predict and freeze before a run, what counts as a result forcing a change, what is held out, how readers and markers are arranged and audited, and when to wait for the owner's word. Use it whenever the question is "what should we run next" or "is this result enough to act on". It never judges whether an explanation holds up; for that it calls the hard-to-vary skill by name.
---

# Planning

This skill chooses. It does not judge. Given a record (what has been claimed, tested, found and left untested) and an aim, it returns the next plan: what runs, in what order, what is predicted, what the result will and will not license, and where it stops to wait. Whether any explanation is hard to vary is the hard-to-vary skill's question, called by name and answered there.

Every rule below was used in one project's record before it was written here. None is new. Where a rule came from is in `references/`.

## The loop
1. **Read the record first.** The read-me, the status, the newest numbered file. Never plan from memory of a record.
2. **Freeze the question.** One claim, one aim, in a sentence. What would count as the claim failing.
3. **Write the plan before anything runs.** What is fixed (the thing under test, the readers, the settings, the sources, the framing), what runs and how many times, what counts as each outcome (decided before reading), the predictions, what follows either way, what the plan does not test, and its traps. Number it. It is not edited after the first run goes out. See `references/freezing.md`.
4. **Wait for the owner's word.** Each phase starts on it. A plan is shown; a run is not started. See `references/owner.md`.
5. **Run, and keep everything as it came.** Every return saved with its finish reason; an empty return kept and run once more, recorded; keys read from the environment and written to no file; the thing under test checked identical to its authority before every call; every reader's and marker's tool calls audited afterwards. See `references/readers-and-markers.md`.
6. **Read the result under the frozen criteria only.** Counts, never rates; no totals across arms; every claim checked against its source with every hit printed; predictions ticked one by one; what was not tested named.
7. **Decide what the result forces.** A change to the thing under test enters only when a test forces it, as one new numbered file, answering every open fault at once where the faults share a cause; then the same test again under the new file. A break seen once forces a repeat, not a change. See `references/changes.md`.
8. **Keep the sets apart.** What a change was written from is fitting; what no marker has read is held out and is spent once a version is judged on it; keyed corpora are the reserve. Freeze the split before the run that uses it. See `references/splits.md`.
9. **Freeze.** When the predictions of the hardening plan hold, the thing under test is frozen: no change until the next aim asks for one. Say so in its front door.

## What to watch for
- **A marker who wrote the thing under test.** Name it in every results file; add a blind second marker as soon as one is available; report agreement by field, and strike the fields that do not agree.
- **A result with n of one.** It is an observation. Three per box is a repeat; five is the least a judgment rests on.
- **A test that spends the held-out set.** Once read, it is fitting.
- **A reader that can see the answer.** A reader under test is never shown a key, a source's standing, the results of earlier tests, or the plan's predictions; a transport that gives it tools is audited for what it read.
- **A change made to tidy a result.** Only a forcing test makes a change.
- **A plan that cannot fail.** Every prediction names the count that would falsify it.

## The report
A results file: the short answer first; what was run; the table, by arm, never summed; the breaks and faults quoted; the predictions ticked; what follows; what this does not show; traps.

## References
| When | Open |
|---|---|
| writing a plan or its predictions | `references/freezing.md` |
| choosing sources, or deciding what a result may be tested on | `references/splits.md` |
| arranging a reader under test, a marker, or their audit | `references/readers-and-markers.md` |
| deciding whether a result forces a change, or when to freeze | `references/changes.md` |
| starting a phase, or asked to run something | `references/owner.md` |
| building a home-made test rig | `references/testing-against-cases.md` (on loan from the hard-to-vary skill) |
