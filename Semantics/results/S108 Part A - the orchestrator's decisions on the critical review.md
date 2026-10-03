# S108: Part A, round 1, the orchestrator's decisions on the critical review

*Claude (the orchestrator), 28 September 2026, after `results/S108 Part A - critical review.md` (a fresh Opus 5.5 agent, commit 551007c). Rule 9 of Part A's rule; decision S13. These are Claude's decisions, not the owner's.*

## What the review found

Four objections matter:
- **O1.** C5 (V2.3) drops the owner's weathervane and two-part sign when the change is read as a boundary. It should be flagged against S41 Q15 and S44.
- **O2.** C6 and C11 name the one-part sign as the owner's S44 case, but the owner's case is the two-part sign. The decision these two go against is S45.
- **O3.** V3.5's "contradicted" mark rests on how the program encodes a construction trace.
- **O4.** e4.29 shows no move. The review also noted that L538.s2 ("Eliminative explanation … is the exposed case") is not met by E5 even with no variant on, which is a finding about the state after round 4.

There are nine minor objections, O5 to O13. The review holds that a second round of Part A is needed.

## Decisions

1. **One second checker.** All thirteen objections go together to one fresh Opus 5.5 second checker. It corrects the dependency map, the edge standings and the candidate list, in maths and code where a run settles a point. It changes nothing in the theory (rule 11).
2. **O4's L538.s2 finding.** It is recorded for the owner and for later, as a point about the theory after round 4. It is not fixed in Part A, which changes nothing, and the review series is on hold (S52).
3. **The tabulation's three out-of-scope flags** (the review asks for a ruling before round 2):
   - **V1.6** adds a condition on Acc. Its formula, without its added sentence (S40), goes into round 2 as a variant for section 2, the section that holds Acc.
   - **V1.7** defines Excl(Σ), which the frozen D3.5 makes a declared input. Varying a frozen item is Part B's work, so V1.7 goes to Part B.
   - **V2.8.** Its D16.XV change is the same change as V4.4, which was computed, so it is not implemented again. Its part on the frozen L315.s7 goes to Part B.
4. **A second round of Part A** follows (rule 10), under its own rule, written and committed before sending. It uses four GLM agents again, one per section, with the same frozen template. It aims at the gaps, in the review's order:
   1. the readings each candidate rests on, under their other choices;
   2. the untouched middle definitions, first those the map places upstream of (E), Dec, Expl, (Suff) and (Nec): D6.9, D11.2, D11.3, D6.8, D9.1, D9.2 and D5.7;
   3. the edges claimed only.
5. **The mechanical whole-suite runs** go to the Sonnet harness in round 2, as the rule assigns (O12 (c)). The Sonnet 5.5 trial (decision S53), now running on section 2, may change who computes in round 2. That is decided when its review is in.
6. **A plain-words file for Part A round 1** is written after the second checker (decision S48).
