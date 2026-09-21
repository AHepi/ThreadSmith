# H63 Plan - blind second marking by Sonnet 5 of the 96 marked reports

Written 21 September 2026, on the owner's word ("Go"), before any second-marker run. Once the first marker agent starts, this file stays as it is. It is item 1 of the testing method proposed after H62: the one marker who wrote the skill, chose the corpus, marked every report, changed the skill and marked the change is checked against a second marker that has seen none of that.

## The question
How far do the marks that carry claims 1 to 5 of the audit brief (file H60) survive a second marker? Where the two markers disagree, which fields and which reports, and does the disagreement touch a claim?

## What is marked
1. **The 48 hidden reports of plan 49** (`marking/to_mark.md`: the close-marking sample, mode labels stripped, numbered), under **plan 52's "Close marking, per report"** rules exactly: shape; each of the eleven tests RAN, NAME ONLY, ABSENT or CANNOT; up to five claims about the document, SUPPORTED, MISREAD or OUTSIDE, each with the quote; the verdict as given; breaks, each with the skill's line quoted; the two yes-or-no marks; the control mark for a control's report (D2 and R1 are the controls in the sample); the layer at fault, named. The first marker's marks are in `marking/close_marks_restored.json`.
2. **The 48 repeat reports** of plans H56 and H58 (DeepSeek and Sonnet 5, file 30 and file 31, twelve each), reader, version, mode and repeat stripped, shuffled and numbered, under **plan H56's recurrence criteria** word for word: does break 1 recur (P3), does break 2 recur (F4), plus shape, whether the flip was run, redirected or absent, every use of *fixed* and whether it is the mark's proper use under the criteria, the "same explanation at this level" verdict, and up to three claims checked. The first marker's marks are in `marking/first_marker_repeat_marks.json`, written from files H57, H59 and H62 before this plan was run.

## The second marker
Claude Sonnet 5 through the session's Workflow tool (model pinned to Sonnet, effort high; never Fable 5.1 or Opus 5, decision H4), one agent per report, ninety-six agents, each given only: the rules file for its set, the source text (rebuilt by `fetch.py`, provenance header stripped, paragraph breaks kept), the report, and for set 1 the skill (file 30) to quote a break's line from. It is told the source id (as `to_mark.md` shows it) and nothing else about the run. It returns its marks as validated structured output; nothing is written by the agent. It is told to read nothing outside the files named; every agent's tool calls are audited afterwards as in H61, and any agent that read outside is reported and its marks set aside in a second count.

## How agreement is read
By program (`second_marker.py compare`), then by eye where the program cannot align:
- **Shape, the two yes-or-no marks, the control mark**: exact agreement, counted over 48.
- **Tests**: agreement per cell over 48 × 11, and separately RAN-versus-not; the second marker's CANNOT cells listed in full.
- **Breaks**: the reports each marker flags, side by side; a break is "shared" when both flag the same report and the second marker's quoted skill line is the same passage.
- **Claims**: cannot be aligned one to one (each marker chooses its claims); the two distributions are reported, and where both chose the same claim (by the marker's own wording matched by eye), the marks are compared.
- **Repeat set**: break 1 and break 2 recurrence per report, both markers, side by side; flip status; the *fixed* uses.
No totals across sets; nothing is scored. Disagreements are listed report by report with both markers' words.

## Predictions, frozen
1. Shape agrees in at least 44 of 48 in each set.
2. Tests: RAN-versus-not agrees in at least 80 percent of the 528 cells. The second marker records no CANNOT; if it records any, each is quoted and is a finding in itself.
3. Breaks, set 1: the second marker flags at least one of the two reports where the first marker found a break (report 004, F4-m1, the *fixed* on the levers; and the P3-m1 report, the flip on the disjunction), and flags breaks in no more than five reports the first marker did not.
4. Repeat set: the second marker flags break 2 in the DeepSeek file 30 F4 mode 1 repeat 1 report; it does not count the borderline P3 report (H57, m1-r2) as break 1; it flags no break in any file 31 report.
5. Controls: the six D2 and R1 reports get LEFT STANDING from the second marker in at least four.
6. The two yes-or-no marks agree in at least 40 of 48 each.
7. The second marker's misreads-of-the-document (claims it marks MISREAD) include at least one claim the first marker marked SUPPORTED with a quote, on rereading of which the first marker was wrong. (A prediction that the first marker erred somewhere; Lesson 46 says it did once before.)

## What follows
- Agreement at or above the predictions: the marks stand as evidence with a stated inter-marker agreement; the audit brief's first attack is answered with a number.
- Below: the fields that disagree are named as unreliable, the claims that rest on them are re-stated with that caveat in a new results file, and the marking plan for any further test is revised to whichever marker's reading the disagreements favour after a third reading.

## What this does not test
- Whether the second marker is right where the two disagree; that needs a third reading, which this plan does not run.
- Modes 0's reports, which cannot be hidden (plan 52), from a marker that can see the report has no marks.
- Anything the reports themselves cannot show (a contaminated reader).

## Traps
- Treating the second marker as ground truth. It is a second reading.
- Counting agreement on claims when the two markers checked different claims.
- Reading a CANNOT from the second marker as the skill's edge before quoting it.
