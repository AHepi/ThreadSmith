# H64 Results - blind second marking by Sonnet 5, agreement with the first marker

Written 21 September 2026, after plan H63 ran: ninety-six Sonnet 5 marker agents, one per report, each given only the rules for its set, the source text, the report and (set 1) the skill to quote from; every agent's tool calls audited afterwards (`marking/second_marker_tool_audit.txt`): none read anything outside the hidden materials; twenty used the shell or a search on those same files. The second marker's marks and the alignment are in `marking/second_marker_comparison.json`; the program's summary in `marking/second_marker_compare.txt`. Nothing here is a score.

## The short answer
- **The claims that matter survive the second marker.** Both breaks of file 54 were flagged by the second marker on the same reports (004, F4-m1; 025, P3-m1). On the 48 repeat reports the two markers agree on break 1 and break 2 in every one (24 of 24 each): the second marker flagged break 2 in exactly one report, the DeepSeek file 30 F4 mode 1 repeat 1 run, quoting the same table row ("P7 | fixed | the owner set it"), and did not count the borderline P3 run as break 1. It found no CANNOT anywhere. All six control reports LEFT STANDING. RAN-versus-not agrees in 84 percent of the 528 test cells. Whether a report reached a finding by testing agrees in 46 of 48.
- **Three fields are unreliable as marked.** Shape at the boundaries: 34 of 48 agree, and every disagreement is the second marker saying PART where the first said NONE (seven bare-reader reports) or FULL (seven skill-mode reports); the order never inverted, and no bare-reader report was called FULL. "Turned one of the document's own tests back on it": 8 of 48, the first marker saying N in 47 and the second Y in 41; the criterion's words are read two ways and the field says nothing until they are fixed. The "same explanation at this level" verdict on the repeat set: 38 of 48, every disagreement the second marker reading "nothing tells them apart" as the verdict.
- **The second marker found breaks in twelve reports the first marker did not**, and they are of a kind the first marker had not looked for: faults in the skill's wording that make a reader drop a test or misapply a mark, rather than verdicts the wording forced wrongly. Plan 52 admits both. Four kinds recur across the twelve, and two of them are the two DeepSeek and Sonnet breaks seen from further off.
- **The first marker was wrong at least twice**, both caught on the repeat set: "diluted presentation" is the Time Traveller's phrase handed to the Psychologist ("'You think. You can explain that. It's presentation below the threshold, you know, diluted presentation.'"), which files H57 and H62 and several readers put in the Psychologist's mouth; and "no outside operator pressed the lever" (a Sonnet file 31 report) is false, since "it was the Psychologist himself who sent forth the model". The second marker also marked one first-marker claim MISREAD that the text bears out (the "one-fiftieth or one-hundredth" phrase is in Wells), and one sign question (a −0.3 point error in RR's figure; correcting it moves the figure +0.3) where the first marker's reading stands.

## Set 1: the 48 hidden reports of plan 49
| Field | Agreement | Reading |
|---|---|---|
| Shape | 34 of 48 | all fourteen: second says PART (first NONE ×7 on mode 0 reports, FULL ×7 on skill-mode reports) |
| By testing, Y/N | 46 of 48 | the two: first N, second Y |
| Turned own test, Y/N | 8 of 48 | first N ×47; second Y ×41. Unreliable field |
| Control mark | 48 of 48 | six LEFT STANDING (R1 ×3, D2 ×3), the rest empty |
| Tests, RAN versus not | 446 of 528 (84%) | per test: flip 46, pull 45, rival 44, remove 43, hunt 43, patches 41, reverse 40, inside 38, swap 36, poke 35, add a job 35 (of 48) |
| CANNOT | 0 from the second marker | as from the first |
| Breaks | both of the first marker's; twelve more from the second | listed below |

### The second marker's breaks, by kind
1. **Two vocabularies collide** (reports 002, 004, 009, 010): the eight part-marks (held, held if, ..., borrowed, fixed, unknown) and the provenance words (fitted, built, asserted) are two closed lists in the same style, and "nothing in the skill says the two vocabularies must not be mixed"; readers put *asserted* in the mark column and *borrowed* or *fixed* in the provenance column. The second marker quotes the skill's lines for both lists. This is the *fixed* stretch of H57 and the *Asserted*-as-a-mark fault of H62, seen from further off and under file 30: the collision is between the two lists, not in one word. File 31 patched one word of it.
2. **The report template drops tests** (023, 025, 030, 048): the seven-heading report in SKILL.md gives no heading for the jobs list Step 2 requires, and its whole-explanation-checks line ("flip, direction, answer hidden in the starting points, where the jobs came from, pairs that pull, catch-alls and their gauges, what the change list leaves out, rivals, and where the parts came from") names no slot for *look inside* or *add a job*; "a reader filling this template exactly, as this one did, has no slot" for them. Checked against SKILL.md line 144: true. This gives file 54's "look inside has almost no purchase" a wording cause the first marker did not see, and a fix that is not change 3 of file 54.
3. **"Held if" has no neighbour for a part-to-part dependency** (034, 047): the mark is defined only by a doubtful job, so a part that rests on another part, or two parts jointly necessary and neither sufficient, gets a hybrid mark the list does not contain ("Held — only as a pair with C").
4. **"Added" means two things** (004, 040): Step 2's provenance tag for a job the reader supplied, and Step 5's test "Add a job"; readers wrote the tag and never ran the test.
5. **Two marker errors**: report 036 is a bare-reader report (mode 0, which plan 52 says cannot be hidden) and the second marker charged the skill with a fault of a reader that never saw it; report 044's "break" is a document misread by the reader, and the second marker's own text says the document rules it out.
Kinds 1 to 4 are held as change candidates; none enters the skill under this entry.

### Claims marked MISREAD by the second marker, set 1
Six. Two aligned with a first-marker claim: 029 (the "one-fiftieth or one-hundredth" gauge; the phrase is in the text, the first marker's SUPPORTED stands) and 044 (the sign of the 0.3-point correction; the first marker's reading stands). Three concerned claims the first marker had not chosen (032 the "inherited from 2009" section structure; 035 a verdict-level claim; 004 a part the Medical Man is said to supply). One is open (037, S14b, whether the report's "infers failed manipulation" reading is the document's): a third reading, which this plan does not run.

## Set 2: the 48 repeat reports
| Field | Agreement | Reading |
|---|---|---|
| Break 1 recurs (P3, 24) | 24 of 24 | none, both markers; the borderline run quoted and not counted by the second marker either |
| Break 2 recurs (F4, 24) | 24 of 24 | one, both markers: DeepSeek file 30 F4-m1-r1, the levers |
| Flip status, P3 under file 31 | | DeepSeek: 5 redirected, 1 run; Sonnet: 5 redirected, 1 run (the first marker read the Sonnet m2-r1 flip on Section VI as redirected; the second as run) |
| *fixed* judged improper | 2 | the levers (F4-m1-r1) and "Fixed / derived" (Sonnet file 31 P3-m2-r1): the same two the first marker named. The Sonnet file 30 *fixed* on the threshold patch the second marker judged proper; the first marker called it the H57 stretch. Disagreement recorded |
| Shape FULL | 45 of 48 | PART: Sonnet 30 P3-m1-r3; DeepSeek 30 F4-m2-r2; Sonnet 31 F4-m1-r1 |
| Same-explanation verdict | 38 of 48 | all ten: second Y, first N |
| MISREAD claims from the second marker | 9 | the three Filby attributions and "he concedes" the first marker had caught; four attributions of "diluted presentation" to the Psychologist and one "no outside operator", which the first marker had not; "bloodied bare feet" for blood-stained socks |

## Predictions from plan H63, marked
1. Shape agrees in at least 44 of 48 in each set: **not borne out** (34; 45 on the repeat set by the second marker's FULL count).
2. RAN-versus-not at least 80 percent; no CANNOT: **borne out** (84%; none).
3. The second marker flags at least one of the first marker's two breaks: **borne out** (both); in no more than five other reports: **not borne out** (twelve, of a kind the prediction did not foresee).
4. Repeat set, break 2 in F4-m1-r1, the borderline not counted, none under file 31: **borne out** in every part.
5. Controls LEFT STANDING in at least four of six: **borne out** (six).
6. The two yes-or-no marks agree in at least 40 of 48 each: **half borne out** (46; 8).
7. At least one first-marker claim wrong on rereading: **borne out** (the "diluted presentation" attribution let pass in H57 and H62; "no outside operator" let pass in H62).

## What follows
- Claims 1, 2 and 5 of the audit brief stand with an inter-marker number beside each: both breaks shared; recurrence 48 of 48; RAN-versus-not 84%; controls 6 of 6; no CANNOT from either marker.
- Three fields are struck from further use as marked: shape's PART boundary (a written rule is needed), "turned own test" (the criterion is reworded or dropped), the same-explanation verdict as a count (kept as quotes only).
- Four change candidates for the skill, held: the two-list collision (broader than file 31's clause); the report template's missing slots for jobs, *look inside* and *add a job*; a mark for part-to-part dependency; the double meaning of "added". None enters the skill until a plan tests it, and the owner's call on file 31 comes first.
- The first marker's two attribution errors are corrected in this file and not in H57 or H62, which stay as written.

## What this does not show
- Which marker is right where they disagree; that is a third reading.
- Anything about the 99 light-marked reports.
- The second marker's own consistency (one agent per report, never two on the same report).

## Traps
- Reading 84 percent as a pass mark. The disagreements sit on four tests (poke, add a job, swap, inside), and those are where the skill's wording is loosest by the second marker's own breaks.
- Reading the twelve extra breaks as twelve faults. They are four kinds, each quoted from the skill.
