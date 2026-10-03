"""Writes 'S108 Part A round 2 - the dependency map, after the cross-examination.md' from the map after round 2 (.md, read,
never written): each amendment a marked replacement ([X..] = the objection id in the settled file). Asserts every anchor is found.
  python3 -B s108r2x_map_md.py
"""
import hashlib

RES = "/home/user/ThreadSmith/Semantics/results/"
IN = RES + "S108 Part A round 2 - the dependency map, after round 2.md"
OUT = RES + "S108 Part A round 2 - the dependency map, after the cross-examination.md"
src = open(IN, encoding="utf-8").read()
md5 = hashlib.md5(src.encode("utf-8")).hexdigest()
t = src


def rep(old, new):
    global t
    assert t.count(old) == 1, ("anchor not unique or absent", old[:80])
    t = t.replace(old, new)


rep("# S108 Part A round 2 - the dependency map, after round 2\n",
    "# S108 Part A round 2 - the dependency map, after the cross-examination\n\n"
    "*A corrected copy of `S108 Part A round 2 - the dependency map, after round 2.md` (md5 %s, kept as it was sent to the GLM "
    "cross-examination), amended under rule 4 of `S108 Part A round 2 - how the GLM cross-examination will be read, written before "
    "sending.md` for every objection that stands, each amendment marked with its objection id ([Xa1] … [Xd2], settled in "
    "`S108 Part A round 2 - the GLM cross-examination, settled.md`). The `.json` is `…, after the cross-examination.json`, built by "
    "`computation/cross-examination runs/s108r2x_map_amend.py`; this file by `s108r2x_map_md.py`. 29 September 2026, one Opus 5.5 "
    "agent (S56).*\n\n## Original header (after round 2)\n" % md5)
rep("Status: complete, 29 September 2026, before the GLM cross-examination (S56), which is read under its own rule. The candidate list (rule 7) is `S108 Part A round 2 - candidate definitions of explanation, after round 2.md`.",
    "Status: complete, 29 September 2026, before the GLM cross-examination (S56), which is read under its own rule. The candidate list (rule 7) is `S108 Part A round 2 - candidate definitions of explanation, after round 2.md`. "
    "**After the cross-examination** (this copy): 16 objections, 7 stand, 7 stand in part, 2 do not; the amendments are listed in §9; the candidate list after it is `S108 Part A round 2 - candidate definitions of explanation, after the cross-examination.md`.")
rep("| round-2 edges | – | 110: computed 70, claimed only 32 (19 of them of the 10 variants flagged out of scope and not implemented), contradicted 8 |",
    "| round-2 edges | – | 110: computed 70, claimed only 32 (19 of them of the 10 variants flagged out of scope and not implemented), contradicted 8 |\n"
    "| **after the cross-examination** [Xc1, Xb1] | – | **edges 351: computed 268, claimed only 51, contradicted 32** (14 parts split off: 12 from 11 rows [Xc1], 2 [Xb1]); round-2 edges 123: computed 72, claimed only 38, contradicted 13; template items touched: computed 187, claimed only 37, untouched 591; middle items untouched 426 |")
rep("| R2V4.3 | C13 read at the content (e) | 0 | out on 25 held relays of 3,208 chains (the reply's \"0 moves\" contradicted) | – |",
    "| R2V4.3 | C13 read at the content (e) | 0 | out on 25 held relays of 3,208 chains under S108r2-4-I3 (the reply's \"0 moves\" contradicted on that reading); **[Xb1]** with Sel at a holding of t read as the fixed point's (inherited) value: 4; at any holding: 0 (the lemma holds) | – |")
rep("| e1.46 | claimed only | computed | section 2, round 2 |",
    "| e1.46 [Xc1: split; its X:(Nec) part is e1.46b, contradicted] | claimed only | computed | section 2, round 2 |")
rep("<!-- /changes -->",
    "| e2.38 [Xc3] | computed | computed | section 2, R2V2.11 (FC21.v1, FC21.v2) | the suite's blind spot is closed: FC21.v2 holds off, counterexample under V2.2 (the builder had skipped this row: a trailing comma in section 2's .json) |\n"
    "| e2.39 [Xc3] | computed | computed | section 2, R2V2.11 (FC21.v1, FC21.v2) | the suite's blind spot is closed: FC21.v1 holds off, counterexample under V2.1 |\n"
    "| e1.46b [Xc1] | claimed only (in e1.46) | contradicted | section 2, round 2 | (Nec) as L538 states it is independent of V1.6's formula (R2V2.8) |\n"
    "| e2.14b [rule 5] | claimed only (after O2) | computed | the settlement of the cross-examination | (Suff)'s defeat set (L536; L17 (S41)) on the 51 worked accounts, history 'nothing tried': 0 off, 51 under V2.5 (`cross-examination runs/e2_14b_suff_under_v25.py`) |\n"
    "<!-- /changes -->")
rep("42 runs in; 0 not yet run when this table was generated. No run timed out; no run changed its program folder.\n<!-- /suite -->",
    "42 runs in; 0 not yet run when this table was generated. No run timed out; no run changed its program folder.\n<!-- /suite -->\n\n"
    "**[Xb3, Xc4] No round-2 suite run of R2V4.8 or R2V4.2.** Section 4's R4E18 (r2e4.17) and R4E05 (r2e4.04) pointed to \"§8\", which has neither. "
    "R2V4.8 (cut U) is a function parameter (`rd=\"U\"`), not a switch of the copy: FC98 (c) and FC32.new1 (b) compute U beside K, T and T′ in every off run "
    "(U: two fixed points for a first construction and none for a selection; the cycle Live → (K2) → Live), and section 4 §2 and its worlds give U's effect on every "
    "account (2 or 0 fixed points), which N41 records. A suite run with U in place of T′ throughout was not made; recorded as a departure. R2V4.2's claims rest on round 1's "
    "suite run under V4.2 and section 4 §2. **[Xa3]** Section 1's seven runs above were made by the continuing agent's script, as section 2's and 3's; section 1's own file "
    "still says \"not run here\" (kept as sent; the settled file records it).")
rep("| S3 | 12 / 1 / 36 | 21 / 0 / 116 |\n| S4 | 9 / 0 / 28 | 27 / 12 / 94 |",
    "| S3 | 12 / 1 / 36 | 21 / 0 / 116 |\n| S4 | 9 / 0 / 28 | 27 / 12 / 94 |\n\n"
    "**[Xc1] After the cross-examination's splits**: S1 12 / 4 / 41, 22 / 9 / 123; S2 32 / 3 / 60, **55 / 5** / 93 (L231.s3); S3 **11 / 2** / 36 (D13.2), 21 / 0 / 116; "
    "S4 **8 / 1** / 28 (D16.1), **26 / 13** / 94 (L630.s5). L55.n3, L397.s16, D10.1, D12.1 and X:(Nec) stay computed through other edges.")
rep("Of these, upstream of (E) or Dec by D18.1's graph or statement: D5.7, D6.5 (Dependence), D12.3 (Dec itself; R2V2.4 flagged, in effect D12.4 [FROZEN]), D18.1 (the order; R2V4.8 reached it through L526.s18).",
    "Of these, upstream of (E) or Dec by D18.1's graph or statement: D5.7, D6.5 (Dependence), D12.3 (Dec itself; R2V2.4 flagged, in effect D12.4 [FROZEN]), D18.1 (the order; R2V4.8 reached it through L526.s18). "
    "**[Xc2]** What each of D6.5, D12.3, D18.1 leaves to vary, and why none is a gap a third round could reach that the computation has not given: §7.")
rep("### 6.2 Edges still claimed only (46)", "### 6.2 Edges still claimed only (46; after the cross-examination 51)")
rep("e2.14b (O2); e4.40c", "e2.14b (O2; **computed after the cross-examination**: V2.5 takes (Suff)'s defeat set from 0 to 51 of the worked accounts on the 'nothing tried' history, rule 5's check); e4.40c")
rep("- **Round 2's (32)**:", "- **[Xc1] Parts split off by the cross-examination (6)**: r2e3.18c (D10.1 under R2V3.8), r2e3.22b (D13.2, D16.1 under R2V3.10), r2e3.17b (L397.s16), r2e3.03b (L55.n3), r2e2.18b (L231.s3), r2e4.09b (L630.s5): each a part its row's own text said was not computed (a sentence the program does not read, or a FROZEN definition not run). R2V3.8's (Nec) part, also uncomputed in round 2, was computed in the settlement (r2e3.18b: contradicted as to L538's (Nec); under L61's reading it moves on the premise-alone case, the mirror of (Suff)).\n- **Round 2's (32)**:")
rep("| the bridge (FC84.new1) | builds no candidate: no variant's effect on it as an explanation is computed (as after round 1); only its provenance and CreateEx |",
    "| the bridge (FC84.new1) | builds no candidate: no variant's effect on it as an explanation is computed (as after round 1); only its provenance and CreateEx; **[Xd1]** CreateEx moves only on its history (a2) (a first design criticized), with 'created' read as CreateEx and p_c the brief; on (a1) nothing moves |\n"
    "| **[Xb1]** R2V4.3 (e): 'Sel at o' read at the holding's staged conditions (S108r2-4-I3), at a holding of t's fixed-point value, or at any holding | 25 / 4 / 0 held outputs of 3,208 chains drop: C13's fifth reading turns on it |\n"
    "| **[Xc5]** S108-4-I7: round 1's V4.7 (D16.3, Enable) computed on a toy only; D16.3 not varied again in round 2 | round 1's own reach: none; Enable is reached by UU, UC, UECS and Classes only; (E), Dec and the defeat conditions do not reach it (e4.35): it does not bear on the explanation definition |")
old7 = t[t.index("## 7. Is a third round of Part A needed? (rule 10)"):t.index("## 8. Unsure")]
rep(old7, old7 + """### 7 after the cross-examination [Xc2]

The cross-examination (job c) found that the paragraph above names D5.7 alone, and that its sentence "every middle definition upstream … has been varied and computed" holds only under the convention that a definition named by a computed edge counts as touched. Three upstream middle definitions have never been varied themselves: **D6.5, D12.3, D18.1**. What each leaves to vary:

- **D6.5** (Dependence) is NC0 ∧ NC2, and NC0 holds of every candidate (D6.2): D6.5 is NC2, which is D6.4. D6.4 was varied four ways (V2.1, V2.2, V2.3, V2.3b), and V2.4 restores the conjunct S106 took out of D6.5 (C6). A further variant of D6.5 adds or drops a conjunct of (E), which is D6.7 [FROZEN]'s.
- **D12.3** (Dec) is D12.4's inheritance [FROZEN] and the complement of Sel ∨ Con. Sel and Con were varied by fourteen variants over two rounds. The complement's own form, varied, gives only limits the list already carries, each an exact count on a history kind already computed: every constructed link declared (C8's and C20's direction at its widest), every selected link declared (C16's), the rule gone (C12).
- **D18.1** is the order, not a definition a candidate reads; round 2 varied it where it binds the explanation definition (L526.s18, R2V4.8: Dec without a value), and FC32.new1 and FC98 compute the graph under every cut.

The other findings that stand change standings (§9) but open no new gap on (E), Dec, Expl, (Suff) or (Nec) that a variant inside Part A's rule could reach: the parts split off (§6.2) are sentences the program does not read or FROZEN definitions (D10.1, D13.2, D16.1), and the one on (Nec) (R2V3.8) was computed in the settlement; R2V4.3 (e) now has all three of its readings computed; e2.38 and e2.39 were closed already. **So: no third round of Part A. Part A ends; Part B follows (S52).**

""")
rep("## 8. Unsure\n", "## 8. Unsure\n\n- **[Xa1] Section 2's worked-case run** was cut twice by a timeout before round 2 was written; every number section 2 and this map take from it was reproduced by the rerun after the cross-examination (`computation/cross-examination runs/Xa1 section 2 worked cases, rerun/`).\n")
t = t.rstrip("\n") + """

## 9. Amendments after the GLM cross-examination

| objection | amendment | where |
|---|---|---|
| Xa1 | the section-2 worked-case numbers now rest on a kept run (all reproduced); edges r2e2.02, r2e2.05, r2e2.06, e2.06c, e2.07 noted | `.json`; §8 |
| Xa3 | section 1's seven suite runs recorded as made by script (its file kept as sent) | §5 |
| Xb1 | R2V4.3 (e) under three readings: 25 / 4 / 0; r2e4.06 qualified and split (r2e4.06b computed: 0 moves), r2e4.05 qualified and split (r2e4.05b contradicted) | §2, §6.3, `.json` |
| Xb3, Xc4 | r2e4.17's and r2e4.04's evidence re-pointed; no R2V4.8 or R2V4.2 suite run, recorded as a departure | §5, `.json` |
| Xc1 | eleven rows split into twelve parts: six claimed only, five contradicted (R2V3.8's (Nec) part computed for the settlement: `xc1_nec_under_r2v38.py`), one computed; counts and stretches recomputed | §0, §3, §6.1, §6.2, `.json` |
| Xc2 | D6.5, D12.3, D18.1 named and argued; the verdict: no third round | §6.1, §7, `.json` (`gaps`, `third_round_needed`) |
| Xc3 | e2.38, e2.39 carry R2V2.11's closure; two rows in the changes | §3, `.json` |
| Xc5 | S108-4-I7 back in §6.3, with its reach (none on the explanation definition) | §6.3, `.json` |
| Xd1 | the bridge's CreateEx conditions | §6.3 |
| rule 5 (no objection) | e2.14b computed: claimed only → computed | §3, §6.2, `.json` |

Not amended here (settled as not standing, or as errata of the section files, which are kept as sent): Xa2, Xa4, Xb2, Xb4, Xb5; Xd2 concerns the candidate list only.
"""
open(OUT, "w", encoding="utf-8").write(t)
assert hashlib.md5(open(IN, encoding="utf-8").read().encode("utf-8")).hexdigest() == md5
print("written", OUT, len(t))
