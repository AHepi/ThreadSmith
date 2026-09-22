# P11 / P14 — original-ledger sameness hand decisions

Written by OpenAI Codex, under L66. Compared after all eighteen independent translations were closed. Original evidence is read from `../../corpus/P11.txt`, `../../corpus/P14.txt`, `../../rigs/rig 1 - arguments/ledger_P11.json`, `../../rigs/rig 1 - arguments/ledger_P14.json`, and their `.pl` files. Exact stdout, stderr and hashed run metadata are adjacent under `P11_P14_original_OpenAI_Codex`. These decisions do not modify either ledger.

Seen: sentences 1–7 and 9–10 are identical. S8 alone changes from “a way of speaking, not a cause” / “shows” / spread “goes on as before” to “not a way of speaking; it is a cause” / “produces” / spread “stops.” Read: `sameness.py` compares normalized wording, not meaning. Worked out: high word overlap can conceal an explicit reversal of causal or counterfactual commitment.

## Every item in ONLY THE FIRST SAYS

| Original P11 line | Hand decision and counterpart | Source span and encoding evidence |
|---|---|---|
| a | Same general rule as P14 a. “Descriptive general reading” and “generic description” are explanatory annotations. | Both S4, “the helper pays the cost”; identical `holds(pays_cost(X))` rule for helping members. |
| b | Same restricted benefit rule as P14 b. | Both S4, “every member shares the benefit”; identical rule over `member_of(G)` with `helping_in(G)`. |
| c | Same qualitative comparison as P14 c. The longer P11 disclaimer does not add a magnitude. | Both S4, “a member who helps does worse than a member who does not”; identical `does_worse(X,Y)` rule within a common group. |
| h | Genuine redescription claim with no identical P14 assertion: P11 says structure shows the spread. P14 h says BECAUSE, and cannot be identified with this “shows” claim. | P11 S8 “group structure shows the spread of helping”; `holds(shows_spread(group_structure,helping))`. |
| i | Opposite causal commitment to P14 h; not a paraphrase, despite the near match. | P11 S8 “not a cause”; `denied_because(i,spreads(helping),exists(group_structure))`. P14 h uses positive `claim_because(h,...)`. |
| j | Opposite counterfactual expectation to P14 j. | P11 S8 “remove the structure and the spread goes on as before”; JSON what-if asks `holds(spreads(helping))` after making `exists(group_structure)` false, with `claims: true`. |
| m | Same retrospective rule as P14 m; “things” versus “what” and annotation wording do not change content. | Both S10, “groups were the things selection was acting on”; identical groups-selected-from-cooperation-spread rule. |

## Every item in ONLY THE SECOND SAYS

| Original P14 line | Hand decision and counterpart | Source span and encoding evidence |
|---|---|---|
| a | Same rule as P11 a. | Identical S4 “helper pays the cost”; identical Prolog rule. |
| b | Same rule as P11 b. | Identical S4 “every member shares the benefit”; identical Prolog rule. |
| c | Same qualitative comparison as P11 c. | Identical S4 “does worse”; identical Prolog rule. |
| h | Positive causal/dependence claim, opposite P11 i; not equivalent to P11 h's showing. The transformation of “produces” into BECAUSE is the original translator's recorded filled-in choice. | P14 S8 “it is a cause: the group structure produces the spread of helping”; `claim_because(h,spreads(helping),exists(group_structure))`. No PRODUCES law is added. |
| i | A separate metalinguistic denial. P11's positive “way of speaking” phrase is in its bin, so this is both a source contrast and an asymmetric decision about retaining the metalinguistic clause. | P14 S8 “This is not a way of speaking”; `denied(merely_way_of_speaking(group_selection_account))`. P11 bin entry 8 contains “a way of speaking.” P14's insertion of “merely” and its referent choice are visible translation choices, not exact source words. |
| j | Opposite counterfactual expectation to P11 j. | P14 S8 “remove the structure and the spread stops”; same make-not-so target and positive query as P11, but `claims: false`. False expected success of the positive query is not by itself explicit derivation of a negative spread fact. |
| m | Same rule as P11 m. | Identical S10 retrospective generalization and identical Prolog rule. |

## Every item in NEAR, JUDGE BY HAND

| Printed near pair | Hand decision |
|---|---|
| P11 a / P14 a, overlap 0.55 | Same rule, identical S4; translator annotation accounts for wording variation. |
| P11 b / P14 b, overlap 0.91 | Same rule with the same explicit group restriction, identical S4. |
| P11 c / P14 c, overlap 0.75 | Same qualitative comparison, identical S4; the language does not compute the degree of disadvantage. |
| P11 i / P14 h, overlap 0.64 | Opposite causal standing at changed S8: NOT BECAUSE versus BECAUSE. Shared words do not establish sameness; the negation is decisive. |
| P11 j / P14 j, overlap 0.84 | Opposite expected outcome under the same specified removal at changed S8: spread persists versus does not. The word “NOT” and the different `claims` booleans are decisive. |
| P11 m / P14 m, overlap 0.69 | Same retrospective rule from identical S10. Only “things”/“what” and annotation wording differ. |

## Same wording, different standing and implementation

The program correctly flags g: P11 `[GIVEN] helping spreads` and P14 `[CLAIMED] helping spreads`. Seen: both original `.pl` files encode it as unconditional `holds(spreads(helping)) :- line(g)`. The standing difference is therefore visible in the prose but not operative in the executable fact clause. In P14 the claimed effect is simultaneously available as a premise; that can keep spread true after removing the proposed cause without demonstrating independence in the source. This original translation defect is not evidence against the passage. Any correction must be separately filed and rerun.

P11 f/g treat structure and current spread as scenario givens; P14 f treats structure as given while g marks spread claimed. These independently chosen standings belong to different S8 causal presentations and must not be silently aligned. The other eight wording matches have the same recorded standing. The program's wording matcher also does not inspect the what-if payload, whose opposite `claims` expectations provide the exact behavioral contrast for j.

## Bin comparison, entry by entry

Entry numbers are one-based positions in the original JSON bin lists. Counts are inventory only.

| P11 entry | P14 entry | Source and hand decision |
|---|---|---|
| 1 | 1 | Identical whole S1. Both bin the selection criterion because it contains varying descendant counts and combined causal contributors; neither weakens it to variation alone. |
| 2 | 2 | Identical whole S2, “Groups can be such things.” Both retain possibility in the bin rather than assert a satisfying actual group. |
| 3 | 3 | Identical whole S3. Both bin quantified descendant comparison and the alternatives outlasts/outgrows/outfights, selecting no disjunct. |
| 4 | 4 | Identical S4 “because the helper pays the cost and every member shares the benefit.” Both bin the joint explanation and magnitude while retaining the qualitative descriptive rules a/b/c. |
| 5 | 5 | Identical S5 “So.” Both leave the support bridge unexecuted because its quantified premises are binned. |
| 6 | 6 | Identical whole S6, “how much” variation. Both bin degree-dependent rather than merely presence-dependent influence. |
| 7 | 7 | Identical whole S7. Both bin the greatly/stronger condition and its nested cluster/stay explanation instead of asserting unconditional helping spread from this sentence. |
| 8 | 8 | Changed S8: P11 bins “a way of speaking; as before,” P14 bins “not a way of speaking; stops.” Both exclude the full time/rate/manner detail. P11 leaves its positive metalinguistic phrase entirely in the bin; P14 retains an explicit negative metalinguistic line i while also mentioning the phrase in the bin reason. That is an independent translation asymmetry. P11 retains positive persistence expectation; P14 retains negative expectation, so the change is not merely bin wording. |
| 9 | 9 | Identical S9 attribution and “afterwards.” Both leave attribution/exact time uncomputed while retaining the same opaque arithmetic description k and denial l. |

Worked out from the cited spans: the meaningful source contrast is causal production versus redescription, coupled to opposed removal expectations in S8. Generic-rule near matches in S4 and S10 are false differences caused by prose annotations. The standing of g, retained metalinguistic line i, and unconditional implementation of P14's claimed effect are translation/execution choices that must remain visible. Equal bin counts do not establish equality of their content. No original file was harmonized or repaired here.
