# P11 / P14 correction1 — primary sameness hand decisions

Written by OpenAI Codex, under L66. Inputs are `../../rigs/rig 1 - arguments/ledger_P11.json` and `ledger_P14_correction1.json`, their `.pl` files and unchanged `../../corpus/P11.txt` / `P14.txt`. Exact output and command/input hashes are in adjacent `P11_P14_correction1_primary_OpenAI_Codex.*` files. Original evidence is retained. The separate `P11_P14_original_hand_decisions_correction1_OpenAI_Codex.md` withdraws an erroneous characterization of original P14 g's behavior under MAKE NOT SO; the account here uses the actual rig reports and raw logs.

Seen: S1–7 and S9–10 are shared verbatim. S8 changes “a way of speaking, not a cause” / “shows” / “goes on as before” into “not a way of speaking; it is a cause” / “produces” / “stops.” Read: the tool compares normalized wording, not meaning, so near matches may express opposite commitments. Worked out: the correction removes an inserted “merely” from P14 i; it changes no source or what-if expectation.

## Every item in ONLY THE FIRST SAYS

| P11 line | Hand decision and source reference |
|---|---|
| a | Same rule as corrected P14 a, from identical S4 “helper pays the cost.” Identical Prolog; translator annotations differ. |
| b | Same rule as corrected P14 b, from identical S4 “every member shares the benefit.” Same explicit group restriction and Prolog. |
| c | Same qualitative comparison as corrected P14 c, from identical S4 “does worse.” Different annotation length introduces no quantitative claim. |
| h | Genuine showing claim from P11 S8 “group structure shows the spread of helping.” It is not corrected P14 h's positive causal dependence claim. |
| i | Opposite of corrected P14 h: P11 S8 denies being a cause and records `denied_because(i,spreads(helping),exists(group_structure))`. Its near wording does not erase the NOT. |
| j | Opposite removal expectation to corrected P14 j: P11 S8 spread “goes on as before.” The common positive spread query has `claims: true`; magnitude/trajectory sameness is binned. |
| m | Same retrospective rule as corrected P14 m, from identical S10. “Things” versus “what” and differing annotations are not substantive. |

## Every item in ONLY THE SECOND SAYS

| P14 correction1 line | Hand decision and source reference |
|---|---|
| a | Same rule as P11 a, identical S4 cost clause. |
| b | Same rule as P11 b, identical S4 benefit clause. |
| c | Same rule as P11 c, identical S4 qualitative comparison. |
| h | Positive BECAUSE claim from P14 S8 “it is a cause” / “produces,” opposed to P11 i's denied BECAUSE. “Structure” is read as its presence, marked filled in. This does not add an executable production law. |
| i | Exact negative metalinguistic content, “not a way of speaking,” from P14 S8. P11 S8's positive counterpart remains in its bin, so retaining this as a line is a translation asymmetry as well as a genuine source contrast. Correction1 removes the original inserted “merely.” |
| j | Negative expectation under removal, from P14 S8 “the spread stops,” opposed to P11 j. The common positive spread query has `claims: false`; success of that expectation does not by itself derive an explicit negative spread fact. |
| m | Same rule as P11 m from identical S10, with explanatory wording variation. |

## Every item in NEAR, JUDGE BY HAND

| Printed near pair | Hand decision |
|---|---|
| P11 a / P14 a, overlap 0.55 | Same S4 cost rule; only translator annotation differs. |
| P11 b / P14 b, overlap 0.91 | Same S4 benefit rule with same group restriction. |
| P11 c / P14 c, overlap 0.75 | Same S4 qualitative comparison; no magnitude is computed in either. |
| P11 i / P14 h, overlap 0.64 | Opposite causal commitments from changed S8: denied BECAUSE versus asserted BECAUSE. |
| P11 j / P14 j, overlap 0.84 | Opposite expectations under the same specified removal, from changed S8: positive query expected true versus false. |
| P11 m / P14 m, overlap 0.69 | Same retrospective rule from identical S10; annotations differ. |

## Shared wording, standing and the actual counterfactual operation

Seen: sameness flags g as `[GIVEN]` in P11 and `[CLAIMED]` in corrected P14 while wording remains “helping spreads.” Both encode the actual-world source outcome as a fact gated by g. The surrounding relation determines what the driver removes, so inspecting that fact clause alone is insufficient.

Seen in `../rig1/P11_OpenAI_Codex.report.txt` and `.raw.txt`: MAKE NOT SO f removes f, keeps g, and proves spread with g as justification. P11's positive expectation therefore prints HOLDS. Its denied BECAUSE i is reported Fine because the ledger supplies no production route.

Seen in `../rig1/P14_correction1_OpenAI_Codex.report.txt` and `.raw.txt`: the driver sets aside g because h declares it came from f. The relevant raw query is `holds(spreads(helping))` with `removed: ['f', 'g']`, yielding “No models.” P14's negative expectation therefore prints HOLDS. The independent causal check still reports JUMP at h: even granting the proposed cause, the ledger supplies no executable production route. This is neither proof of an explicit negative spread fact nor confirmation of a production mechanism.

Seen in `../consequences/P14_correction1_OpenAI_Codex.report.txt`: simply taking out line f removes only the structure-existence fact. That tool does not apply the counterfactual driver's dependency removal. Worked out: the two operations ask different questions; treating them as interchangeable would wrongly label g an independent counterfactual premise. g is source-said actual outcome, not an added production premise. No retranslation to erase this distinction is made.

## Every bin entry compared

| P11 entry | P14 correction1 entry | Hand decision and source reference |
|---|---|---|
| 1 | 1 | Identical whole S1; both bin descendant counts and combined causal criterion without weakening its conditions. |
| 2 | 2 | Identical whole S2; both bin modal possibility, not assert a realized qualifying group. |
| 3 | 3 | Identical whole S3; both bin reproduction quantities and alternative outlasts/outgrows/outfights causes. |
| 4 | 4 | Identical S4 joint “because” clause; both bin the compound explanation/magnitudes while retaining qualitative a/b/c. |
| 5 | 5 | Identical S5 “So”; both lack an executable bridge from the binned quantified comparisons. |
| 6 | 6 | Identical whole S6; both bin “how much” dependence rather than reduce it to presence/absence. |
| 7 | 7 | Identical whole S7; both retain the greatly/stronger condition and nested clustering explanation in the bin. |
| 8 | 8 | Changed S8. P11 bins “a way of speaking; as before”; corrected P14 cites “not a way of speaking; stops,” explaining that i retains the exact denial while stopping transition/time is not modeled. The positive metalinguistic phrase is binned only in P11; the negative is represented in P14. Persistence versus nonpersistence expectations remain opposite in j. |
| 9 | 9 | Identical S9 attribution and “afterwards”; both leave attribution and exact time uncomputed while retaining k/l. |

All nine entries on each side have been compared. Equal counts are inventory, not semantic evidence. Worked out: S8 carries the real causal/redescription and counterfactual contrast; S4/S10 near rows are paraphrase differences. The g standing choice and asymmetric metalinguistic retention stay visible. Correction1 repairs only the explicit qualification error, with all original files preserved.
