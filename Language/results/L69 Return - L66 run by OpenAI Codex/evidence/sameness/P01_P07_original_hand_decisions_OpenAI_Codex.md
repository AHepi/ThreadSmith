# P01 / P07 — original-ledger sameness hand decisions

Written by OpenAI Codex, under L66. This is a comparison of the completed original translations, made only after P18 was closed. It changes neither ledger. Evidence is read from `../../corpus/P01.txt`, `../../corpus/P07.txt`, `../../rigs/rig 1 - arguments/ledger_P01.json`, `../../rigs/rig 1 - arguments/ledger_P07.json`, and their `.pl` files. The exact program output is `P01_P07_original_OpenAI_Codex.stdout.txt`; its command, exit status and input hashes are in the adjacent `.run.json`. Corrections, if supplied, require another comparison and do not replace this evidence.

Seen: sentences 1–8 and 10 are identical. Sentence 9 changes from “a way of showing the outcome, not a cause that produced it” to “a cause that produced the outcome, not merely a way of showing it.” Worked out: this is the sole source-text difference. Read: `sameness.py` compares normalized wording, not meaning; it does not inspect Prolog, definitions, bins or the referents of line identifiers. Its “only” results are not by themselves new commitments, and its “both” results are not a proof of identical executable behavior.

## Every item in ONLY THE FIRST SAYS

| Original P01 line | Hand decision and counterpart | Source span and encoding evidence |
|---|---|---|
| a | Same intended criterion as P07 a, with different explanatory wording. Not an extra claim. | Both S1, “acts on whatever is copied faithfully across generations.” Both `.pl` files use `holds(selected(X)) :- line(a), holds(faithfully_copied(X))`. |
| g | Same filled-in SINCE link as P07 g. Wording about epistemic support versus redescription is a translator's explanation. | Both S5, “because groups of relatives are exactly where copies of the gene are clustered.” Both use `claim_since(g, same_process(group_selection,gene_helping), clustered_copies(kin_groups))`. |
| h | Same explicit denial as P07 h: “adds no cause” and “NOT [adds a cause]” are equivalent here. An executable asymmetry remains. | Both S6, “the group adds no cause of its own.” Both assert `denied(adds_own_cause(group))`; P07 additionally asserts `holds(neg(adds_own_cause(group)))`. |
| k | Same necessary alternatives as P07 k; “encoded for a generic system” versus “generic system reading” does not change them. | Both S8, “members were kin or the copies were bound together so that they could not defect.” Both use the same denied-cooperation rule with both alternatives denied. |
| n | Real contrast with P07 S9, but not a strict opposite. P01 asserts that the description shows the outcome. P07's “not merely” does not deny showing, and no positive showing line was extracted in its original translation. | P01 S9 “a way of showing the outcome”; P07 S9 “not merely a way of showing it.” P01 has `holds(shows_outcome(group_description))`; P07's handling of the qualified phrase is in bin entry 8. |
| o | Real production-polarity contrast with P07 p at the source level; the machine encodings are not a shared positive/negative predicate pair. | P01 S9 “not a cause that produced it” becomes `denied(produces(group_description,outcome))`; P07 S9 “a cause that produced the outcome” becomes `did(p,group_description,produced,outcome,none)`. No rig identity between `produces` and `did(...produced...)` is supplied. |
| s | Same intended S10 conclusion/support pointer as P07 s; different machine content. Do not count it as an independent source change. | Both S10 “Groups are therefore not selected”, read as relying on S6's denial. P01 uses unsigned `claim_since(s,selected(group),adds_own_cause(group))`; P07 uses `claim_since(s,neg(selected(group)),neg(adds_own_cause(group)))`. P01 bin entry 9 records the defect. |

## Every item in ONLY THE SECOND SAYS

| Original P07 line | Hand decision and counterpart | Source span and encoding evidence |
|---|---|---|
| a | Same criterion as P01 a; only explanatory wording differs. | Both S1, faithful copying; identical selected-from-copied rule. |
| g | Same filled-in support claim as P01 g. | Both S5, the “because” clause; identical `claim_since(g,...)`. |
| h | Same explicit denial as P01 h; extra signed wrapper changes implementation. | Both S6, “adds no cause”; `holds(neg(...))` occurs additionally in P07. |
| k | Same necessary alternatives as P01 k. | Both S8, kin or bound copies; identical rule. |
| n | Actor/classification setup for P07's production event, with no matching P01 row. This is a translation-form asymmetry, not a new source sentence about a description's physical behavior. | P07 S9 names “The group description”; line n adds `kind(group_description,description)` and `body(group_description,not_stated)`. “Response to a press not stated” is an encoding annotation, not words asserted by the passage. |
| o | Target/classification setup for P07 p, with no matching P01 setup row. Its label o must not be aligned to P01 o by identifier alone: P01 o denies production. | P07 S9 names “the outcome”; line o adds `kind(outcome,outcome)` and `body(outcome,not_stated)`. |
| p | Genuine positive production claim opposed to P01 S9's negative production claim. The different predicate forms prevent treating their executable representations as direct logical opposites without a bridge. | P07 S9 “a cause that produced the outcome”; counterpart P01 o, “not a cause that produced it.” Verb `produced` is retained; no shape is supplied. |
| s | Same intended inference as P01 s, with a different signed encoding. | Both S10 “therefore”; P07's wrapper terms preserve the chosen polarity whereas P01's original argument slots do not. |

## Every item in NEAR, JUDGE BY HAND

| Printed near pair | Hand decision |
|---|---|
| P01 h / P07 h, overlap 0.67 | Semantically the same denial, from identical S6. Surface negation placement explains the near match; P07's extra `holds(neg(...))` is an implementation asymmetry. |
| P01 k / P07 k, overlap 0.80 | Same necessary-alternatives reading of identical S8. Only the translator's generic-reading annotation changes. |

## Matches that need more than wording

The eleven “both” matches have matching standing. Nevertheless q has different implementation: P01 asserts only `denied(selected(group))`, while P07 also asserts `holds(neg(selected(group)))`. That difference supports the signed-claim asymmetry at s. It is not a difference in S10. The program does not compare machine clauses and therefore cannot reveal it.

The original P01 o and P07 p were not offered as a near pair, yet their S9 source spans carry the main contrast. Conversely n/o in P07 are event scaffolding, not a replacement for P01 n/o based on letter identity. Equal row names or unequal row counts do not settle meaning.

## Bin comparison, entry by entry

Entry numbers below are one-based positions in each JSON `bin_entries` / `leftover` list. Counts are inventory only.

| P01 entry | P07 entry | Source and hand decision |
|---|---|---|
| 1 | 1 | Identical S2 span, “with every generation, so it cannot be the thing that selection preserves.” Both exclude timing/frequency and modal inability; reason wording differs without a substantive retention difference. |
| 2 | 2 | Identical whole S3. Both retain the probability-conditioned spread/explanation in the bin; neither asserts spread unconditionally. |
| 3 | 3 | Identical whole S4. Both exclude weighted probability/cost comparisons; P07 additionally spells out why “usual case” does not become an ordinary USUALLY rule. |
| 4 | 4 | Identical S5. P01's selected span starts “What looks like”; P07 starts “looks like.” Both exclude appearance, distance/viewpoint and location. Neither executes a mathematical identity proof. |
| 5 | 5 | Identical S6 modal rewriteability and same-answer clause. Both leave the supporting bridge to h unexecuted. |
| 6 | 6 | Identical S7 modal antecedent and relative-speed qualification. Both keep i/j as independently asserted generic reasons under their recorded reading while binning the quantitative conditional explanation. |
| 7 | 7 | Identical S8. P01 cites “could not defect; so that”; P07 cites “so that they could not defect.” Both record excluded purpose/impossibility and keep an opaque bound-without-defection alternative. This is span/wording variation. |
| 8 | 9 | Identical S10 location clause. Both exclude location and refrain from inventing a meeting event. |
| 9 | none | Identical S10 “therefore,” but P01 bins the original unsigned-inference limitation. P07's different signed-wrapper implementation avoids that particular bin entry. This is a translator/encoding asymmetry, not a source difference. |
| none | 8 | Changed S9 “is a cause; not merely a way of showing it.” P07 retains production as event p and bins the metalinguistic exclusive-status qualification. P01 has no matching bin entry and directly denies production in o. “Not merely showing” does not mean “not showing.” |

Seen: both original bins have nine entries but they do not contain the same nine items. Worked out: the source-level change is the S9 contrast; the extra S10 bin difference and signed predicate wrappers arise from independent translation. The n/o event scaffolding is another independent representational choice. No harmonization or hidden repair has been made in this comparison.
