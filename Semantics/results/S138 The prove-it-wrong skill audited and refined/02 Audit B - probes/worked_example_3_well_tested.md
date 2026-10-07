C1. "The new date parser reads every timestamp in our 2023 to 2025 log archive identically to the reference library."
Source: release notes, "Parser" section, written by us.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | At least one timestamp in the archive is read differently by the new parser and the reference library | survived | ran compare_all.py over all 41,207,113 timestamps; printed "0 differences"; output in runs/compare_2025-09-30.txt | none |
| F2 | C1 | At least one of 2,000,000 generated strings in the archive's formats, including leap days and offsets, is read differently | survived | ran fuzz_dates.py with the saved seed list; printed "0 differences" | none |
| F3 | C1 | A colleague who did not write the parser reruns the full comparison on another machine and finds at least one difference | survived | rerun by a second engineer; their output runs/compare_rerun.txt shows 0 differences | none |
| F4 | C1 | Timestamps from sources other than the archive, such as new log formats, are read differently | outside the claim | none | the claim covers the archive only; other sources are a new claim |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | covered | F4: scoped to the archive; other sources are outside the claim |
| Q2 | C1 | does not apply | the reference library is an independent implementation, not a supplied answer |
| Q3 | C1 | covered | F1: the reference library is the rival, run on every item |
| Q4 | C1 | does not apply | one comparison, with no arms that could agree by construction |
| Q5 | C1 | covered | F1: every single timestamp compared, not a sample or an average |
| Q6 | C1 | covered | F1: the same inputs, same build, go to both parsers |
| Q7 | C1 | covered | worked out: the claim, "identically to the reference library", is about outputs only |
| Q8 | C1 | does not apply | nothing in the parser was fitted, learned or tuned |
| Q9 | C1 | covered | F1, F3: the full population, plus an independent rerun |
| Q10 | C1 | covered | design note dated before the run: "compare every archive timestamp against the reference" |
| Q11 | C1 | covered | F3: outputs saved and rerun by someone else |
| Q12 | C1 | covered | release benchmark: "speed within 2%, memory within 1%" |
| Q13 | C1 | covered | every timestamp counted, including malformed lines, which both parsers must reject alike |

Well-tested: C1. Its main falsifiers were sought and survived.

**Claim as it stands:** unchanged. The parser reads every timestamp in the archive as the reference library does. Formats outside the archive are not claimed.

**Next test:** none needed for this claim. If the parser is to be used on other sources, a sample from each new source comes first.
