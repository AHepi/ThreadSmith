# Probe pass 03: a well-tested claim, no missing rows, with a Well-tested line. Expected: passes.
C1. "The new date parser reads every timestamp in our 2023 to 2025 archive as the reference library does."
Source: release notes, "Parser" section, written by us.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | At least one timestamp in the archive is read differently by the new parser and the reference library | survived | ran compare_all.py over all 41,207,113 timestamps; printed "0 differences" | none |
| F2 | C1 | A colleague who did not write the parser reruns the comparison on another machine and finds at least one difference | survived | watched the rerun; output runs/compare_rerun.txt shows "0 differences" | none |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | covered | F1: the claim is scoped to the archive by its own words |
| Q2, Q4, Q8 | C1 | does not apply | considered a supplied or fitted answer; the reference library is independent, there is one comparison, nothing was fitted |
| Q3 | C1 | covered | F1: the reference library is the rival, run on every item |
| Q5 | C1 | covered | F1: every timestamp compared one by one |
| Q6 | C1 | covered | F1: same inputs and same build for both parsers |
| Q7 | C1 | covered | worked out: "as the reference library does" is a claim about outputs only |
| Q9 | C1 | covered | F1, F2: the whole population, and a second run by someone else |
| Q10 | C1 | covered | design note dated before the run: "compare every archive timestamp" |
| Q11 | C1 | covered | F2: rerun by someone else and watched |
| Q12 | C1 | covered | release benchmark: "speed within 2%" |
| Q13 | C1 | covered | F1: every timestamp counted, malformed lines included |

Well-tested: C1. Its main falsifiers were sought and survived.

Claim as it stands: unchanged; the parser reads every archive timestamp as the reference library does.

Next test: a sample from each new log source before the parser is used on it.
