# 52 Marking plan - frozen before the corpus is read

Written 20 September 2026, after the pilot (file 51) and before any phase 2 run is read. Once phase 2 starts, this file stays as it is.
It answers the question plan 49 left open: how the reader's reports are marked.

## What is being measured, and what is not
The corpus is forty-nine outside documents. Nobody here knows which of their explanations are true, and several are live disputes. So **truth is not marked.** What is marked is the skill: where its words did work in a reader that had never seen them, and where they broke.

"Broke" is given four concrete meanings, and each has its own mark below: a test that **cannot be run** on a document of that kind; a test **run in name only**; a verdict the skill's wording **forced wrongly**; and a module the router **failed to open** when the case needed it.

## The layers, kept apart
A report can be wrong in three places, and the marks must say which.
1. **The document.** What it actually says. Checked against the text.
2. **The skill.** What its words told the reader to do.
3. **The reader.** DeepSeek V4.1 Flash, which may simply be careless.
A finding contradicted by the document is the reader's fault unless the skill's wording pushed it there; only then is it the skill's. The marker must name which, in one line, every time.

## How the replies reach the marker
A program strips the mode label, the module list and the timings, shuffles with an unrecorded seed, and numbers the reports. Modes 1 and 2 are then indistinguishable on the page. **Mode 0 is not hidden:** its reports carry no marks and no frozen question, so the marker can always tell them. This is recorded as a limit, not worked around. The marker never opens the mapping file until every mark is saved.

## What gets marked, and how much
147 reports is too many to mark closely. So:

**Close marking: a stratified sample of sixteen sources, two from each of the eight domains, drawn by program with a recorded seed, times three modes = 48 reports.** The draw happens before any report is read.

**Light marking: the remaining thirty-three sources, three modes each = 99 reports.** Shape and breaks only, most of it by program.

### Close marking, per report
1. **Shape.** FULL (the question frozen, parts and jobs listed, a change list, tests run, a mark on every part, and the report's seven headings), PART, or NONE.
2. **Each of the eleven tests**, one mark: **RAN** (applied with a concrete change or a named neighbour), **NAME ONLY** (mentioned with no content behind it), **ABSENT**, or **CANNOT** (the reader says, or the document shows, that the test has no purchase on a document of this kind). CANNOT is the mark that finds the skill's edges.
3. **Up to five claims about the document**, chosen as: the weakest-part claim, the verdict, and the first three part-marks. Each gets **SUPPORTED** (the document's own words bear it out; the marker quotes them), **MISREAD** (the document says otherwise; quote), or **OUTSIDE** (about matters the document does not contain, so the text cannot settle it).
4. **The verdict**, recorded as given.
5. **Breaks.** Zero or more, each as: the quoted line of the skill, what the reader did with it, and why that is the skill's doing rather than the reader's.
6. **Two yes-or-no marks.** Did the report reach any finding **by testing the document** rather than by recalling what is said about it in the world? Did it take one of the document's **own tests and turn it back on the document**?

### Light marking, per report
Shape (by program: the seven headings, the eight marks, "the question, frozen"), length, modules opened, and any break the marker notices while skimming. No claim-checking.

### Controls
Eight sources are controls: S5, S11, S16, S12, C6, C7, D2, R1. A control's report is marked **LEFT STANDING** when the verdict is to rely on it, or to rely on it for a narrower question the document itself states; **FALSE ALARM** when the report faults it for being coarse, for lacking detail it never claimed, or for resting on a convention that is free.

## How the table is read
Case by mode, marks side by side. No totals, no score, no ranking of modes by counting RANs. The three readings that matter:
- **Mode 1 against mode 2, box by box.** Where they differ, the difference is the router's doing or noise; one run per box cannot tell them apart, so any difference is reported as a single observation, not a result.
- **Mode 0 against modes 1 and 2.** What did the bare reader find that the skill's structure crowded out? A finding present in mode 0 and absent in both others is a cost of the skill, and is reported as one.
- **The CANNOT and BREAK columns.** These are the answer to the owner's question. They are reported in full, quoted, one line each, and they are not counted.

## What would count as failure of this test
- **The skill is idle.** Modes 1 and 2 find nothing mode 0 did not, on any source.
- **The skill is ritual.** NAME ONLY outnumbers RAN across the sample. Then the skill produces the form of the method without the method.
- **The skill makes a prosecutor.** Three or more of the eight controls draw a FALSE ALARM under modes 1 or 2.
- **The marking is noise.** The marker cannot decide SUPPORTED against MISREAD without rereading the whole document on more than a quarter of the claims. Then claim-checking is dropped and the test reports shape and breaks only.
- **The corpus is the wrong shape.** CANNOT clusters on one domain, which would say the documents, not the skill, were wrong for that row.

## Known weaknesses of this marking plan, stated before use
- The marker wrote the skill and chose the corpus. This is the same flaw plan 42 named and no blinding here repairs it. A second marker, human or another model, is the only real fix and is not available today.
- Mode 0 cannot be hidden.
- One run per box. No box's mark can be told from noise.
- Nine sources are truncated, so a report faulted for missing something answered in a later page would be wrongly marked. The truncated nine are listed in file 50 and the marker checks that list before recording a MISREAD.
- Claim-checking reads the document with the report in hand, which is the order most likely to make the marker agree with the report. Against it: every SUPPORTED must carry a quote.

## Traps
- Marking a report as wrong because its verdict is unwelcome. The mark is about the document's words, not about who is right in the dispute.
- Letting a full report pass because it is well written.
- Recording a break without quoting the line of the skill that caused it.
- Opening the mapping file before the marks are saved.
