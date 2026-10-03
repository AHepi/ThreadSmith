# S105 Round 3 — moves after round 3 (rule 16, counted strictly)

*Integration, 28 September 2026. Rule 16: the formal changes that answer a finding that holds (M, W or I: a changed or new definition, a changed claim or encoding, a change to the program's reading of a definition), plus the text changes applied. Counted as round 2's second checker counted (lesson S41). Findings that hold: area 1 28 (M 14, W 14), area 2 1 (I: W3, no change adopted), area 3 21 (M 9, W 12).*

## Counted

| # | area | finding(s) | move | kind |
|---|---|---|---|---|
| 1 | A1 (= A3 F1) | B3, S-fQ2; S1 | D11.3: ≺_h well founded (F1); D18.1's uniqueness proviso dropped with it | changed definition |
| 2 | A1 | B1 | D12.1: provenance of a holding (t, o_t), h(t) := h(t, o_t) (F2) | changed definition |
| 3 | A1 | B-e6, B1 | D12.3: a relay or record carries its source's provenance (F3) | changed definition |
| 4 | A1 | B2 | D12.2: CT exact, t held at an output of the trace (F4) | changed definition |
| 5 | A1 | B8 | D12.1: H ≠ ∅ (F5) | changed definition |
| 6 | A1 | B5, S-D2 | D11.2: H and surv typed as contents (F6) | changed definition |
| 7 | A1 | S-D2 | D18.1: Held with D12.5's extent (F7) | changed definition |
| 8 | A1 | B6 | D3.3: obs the one value or ⊥ (F8) | changed definition |
| 9 | A1 | B9, S-fQ6 | D13.8: "immediately after" defined (F9) | changed definition |
| 10 | A1 | S-D1 | D4.6: O_j, the ports j assigns (F10) | changed definition |
| 11 | A1 | W1/W2 | D5.7: Fid⁺ only for L630; L220 narrow (F11) | changed definition |
| 12 | A1 | K1 | CT8 (s104_creative_transport.py): Con read under T′ with Held computed (F12) | the program's reading of a definition |
| 13 | A3 | W6 | D12.1: surv := Faithful_H ∧ Env (F2) | changed definition |
| 14 | A3 | S2(iii) | D13.3: ExplUse defined through UsesClaim (F3) | changed definition |
| 15 | A3 | S-e-Acc | D14.7: δ_c quantified (F4) | changed definition |
| 16 | A3 | W8 | FC18: D4.4's reading, I94 a look; CEX → H (F5) | changed claim |
| 17 | A3 | S2(i), S2(ii), S3 | the program's D18.1 graph: 82 nodes, the missing edges (F6) | the program's reading of a definition |
| 18 | A3 | S-b | D0.2: the symbols used and not listed, classed (F7) | changed definition (area 3 left it uncounted, calling it a register; it is the numbered paragraph D0.2 answering a finding that holds, and round 2's second checker counted D0.2's classing: counted here) |
| 19–24 | A1 | O1–O3 (×4), W1/W2, K2 | R3A1-T1 (L61), T2 (L49), T3, T4 (L69), T5 (L220), T6 (L201) | text changes applied |
| 25–29 | A3 | B-Q23n; O4 (×4); O5 (×4); W7, S-e-represented; S1 | R3A3-T1, T2, T3 (L397), T4 (L405), T5 (L375) | text changes applied |

| | formal | text applied | moves |
|---|---|---|---|
| area 1 | 12 | 6 | 18 |
| area 2 | 0 | 0 | 0 |
| area 3 | 6 | 5 | 11 |
| **total** | **18** | **11** | **29** |

The areas' own counts: 18, 0, 10 (28). The difference is row 18. **Moves: 29, not 0: the series continues (rule 17).**

## Not counted

| item | why |
|---|---|
| A3 F1 (D11.3) | the same fix as A1 F1, counted once |
| FC77 restated (A1) | re-based on D12.1's H ≠ ∅ (counted, row 5); status H unchanged |
| the primed ids of FC02, FC07, FC28, FC32, FC36, FC78, FC81–FC83 | re-based (editorial), results unchanged |
| D12.7, D12.8 on h(t, o_t); D12.9, D15.8 on surv | re-based on rows 2, 13 |
| FC98's printed cycle and sink list (A3) | a test part's print, following row 17 |
| FC14, FC32.new1 reading the formal core after round 3 (integration) | a path, not a reading of a definition |
| sel(h_nonempty=, env=) combined (integration) | the code of rows 5 and 13 |
| A2: core.SLOT_QUANTIFIER (default every, D6.3 as it stands) | no formal change adopted (W3 holds against an invention only; owner question R3-Q1) |
| inventions I167–I182 (I166, I162 for Build, I169, I50 at L220 settled in the text) | register entries |
| new test claims: FC12.new2, FC12.new3, FC13.new1, FC28.new1, FC28.new2, FC84.new2, FC97.new1, FC98.new1, FC104.new1 (A1); FC23.new1, FC25.new1, FC47.new1 (A2); FC98.new2, FC72.new1, FC80.new1, FC32.new1, FC90.new1, FC102.new1, FC103.new1 (A3); test parts FC30.new1 (d)–(f); model/e9.py (E9's instance, I182) | new test claims and test parts |
| owner question R3-Q1; parked P1–P7 (none new) | records |

## After the second checker on the critical review (28 September 2026)

*`results/S105 Round 3 - the second checker on the critical review.md`; the four objections of `results/S105 Round 3 - critical review of the round.md` §3. Counted as above (rule 16, strictly).*

| # | objection | move | kind |
|---|---|---|---|
| 30 | 2 | R3SC-L13: L13, " and criticism" deleted (D12.2 asks no criticism; FC32.new1 (f), FC84.new1 (a)) | text change applied |
| 31 | 3 | R3SC-L61: L61, "their necessity" → "necessity (D16.XV)" (FC30.new1 (g)) | text change applied |

| | formal | text applied | moves |
|---|---|---|---|
| integration | 18 | 11 | 29 |
| second check | 0 | 2 | 2 |
| **total** | **18** | **13** | **31** |

Not counted: D16.4's δ (objection 1), the change of row 15 (F4, I180) in its second place, one fix counted once (as X1, X8); I183, a register entry; CT8's constant `held_trees` removed (objection 4), the code of row 12 (F12), output unchanged but CT8's header label; test parts FC30.new1 (g), FC32.new1 (f). If D16.4 were counted apart: 32. **Moves: 31, not 0: the series continues (rule 17).**
