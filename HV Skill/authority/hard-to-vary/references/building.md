# Building with the tests

Open this when the explanation, theory or design does not exist yet. The tests in the main file still do all the work. What changes is that you are now the owner as well as the critic, so the fit between your jobs and your parts proves little unless you arrange for it to be able to fail.

Contents: 1 The order. 2 What to watch. 3 Traps.

## 1. The order

**Case.** Asked what a bridge design must have, an engineer who starts from a favourite truss will write requirements the truss happens to meet. One who starts from the river, the loads and the soil will find out whether the truss belongs.

**Point.** Question, then jobs, then parts, then tests.

- **If you are improving something that has already run, start from the record:** what worked and what failed, each tagged by how you know. Every change you propose should be held in place by something on that list.
- **Get a real case from the owner before writing the jobs,** if you can. Jobs written without one are your guess at what the owner will bring.
- **List the jobs first, each as a contrast,** and mark each **given** (the owner named it), **fixed** (the owner made it a requirement and it is not up for test) or **added** (yours). A part held only by an added job is *held if* that job is real.
- **Propose parts freely.** A guess needs no justification to be proposed.
- **Run remove and swap on every part.** Keep a note of what was cut, merged or renamed. A build in which nothing was cut was probably tested softly.
- **Walk the parts by hand through every earlier case** before building anything. It costs minutes.

## 2. What to watch

- **Pairs that pull.** Does making one part stronger make another weaker? Name the pair, where the line is drawn, and what would show the line is in the wrong place. Designs fail at the joints more often than inside a part.
- **Catch-alls.** A bin, a fallback, an "anything else" clause can absorb any failure, so it holds nothing in place. Allow one only with a gauge: something you can look at that would show it is swallowing a job.
- **The answer hidden in your own job list.** "Does the job" means your jobs. If the list is wrong, the parts can be tidy and useless. Say so in the report.
- **Where each part came from.** Built (a test here forced it), borrowed (rests on another explanation; name it, and name its best rival), or fitted. For a builder, *fitted* includes "this is how such things are usually made, as far as I recall". Those are the first parts to check.
- **One version.** If the thing now lives in several documents, merge it into one before testing. Otherwise nobody can say which version a result tested. When a second theory follows the first, say whether it replaces parts, fills them in, or sits beside them.
- **Pokes that could catch the whole thing out.** At least one must be something a person could actually try.

## 3. Traps

- Writing the jobs after the parts. The jobs then describe the parts.
- Marking your own jobs as the owner's.
- A build where nothing was cut.
- A catch-all with no gauge.
- Borrowing an idea without naming its rival.
