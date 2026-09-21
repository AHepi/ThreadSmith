# Origin

**The goal**, from the project story: "Find or design a formal language that everyday reasoning prose can be turned into, that an external checker can read and find faults in (contradictions, jumps in reasoning, mismatches of category, property or type, and anything else that aids reasoning), and whose findings can be turned back into plain prose. The external checker is the one essential thing."

**In the owner's words** (Decisions 1, 5, 12): "It's purpose is to aid in reasoning. So it checks for logical inconsistencies, contradictions, jumps in reasoning, mismatches in category, properties or type. Basically anything that will aid in reasoning." "The one thing that is essential is an external checker." "The goal isn't exactness, but basic causal relations should be capturable, it must be combinatorial like human languages, but must be checker friendly."

**Authority document:** "Claude Fable Semantics - standalone theory" (file 10), frozen. Its definition of a kind, by the changes a thing responds to, is used as the whole semantics of the language (log 18).

## The first research state: twelve properties (log 01)
Worked out with the hard-to-vary skill before any research or building. Thirteen at first; one turned out to be inside two others.

A. What gets written down: 1 one name, one thing; 2 kinds; 3 strength marks; 4 separate parts with a direction; 5 the question, frozen.
B. What keeps the checker external: 6 fixed meaning, always an answer; 7 a sameness test; 8 evidence, not a score.
C. What keeps it tied to your words: 9 two-way anchor; 10 source marks; 11 leftover bin; 12 exact read-back.

Written up as `01 Theory - checked reasoning language - twelve properties.html` - **not in bundle**. Two unexpected results: the way back to prose should be exact and only the way in should guess; and source marks are the most firmly held property.

## How the pieces fit
You write four sentences about tomato plants. A translator turns them into twelve ledger lines. A checker finds a contradiction, a jump and a kind mistake. A read-back turns those findings into a plain report that points at your sentences.

| Part | What it does | What it hands on |
| --- | --- | --- |
| You | Write prose | Prose, to the translator |
| Translator (a language model) | Turns prose into ledger lines. The only step that guesses | Ledger to the checker; what does not fit to the leftover bin |
| Ledger | Holds your text as lines, each tied to your sentence and marked said / filled in / usual case | Lines, to the checker |
| Checker (fixed rules) | Finds faults. Never guesses | Findings, written in the ledger language |
| Read-back (fixed rules) | Turns lines into plain prose. Never guesses | The report, to you |
| Leftover bin | Holds prose that could not be written as lines | A "not checked" list, into the report |

As built, the checker has three layers: s(CASP) does the reasoning; the driver decides what to ask, takes lines out to see what changes, and writes the report from fixed wording; the checker rules are the fixed rules s(CASP) uses for every ledger. The translator, so far, is Claude working by hand.
