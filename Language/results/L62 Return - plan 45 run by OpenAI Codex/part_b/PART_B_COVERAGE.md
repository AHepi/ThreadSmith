# Part B exact-record coverage

Written by: OpenAI Codex

All 48 exact records prepared in the supplied manifest are accounted for below. Coverage is inventory, not evidence weight. A source-faithful no-run or no-adapter disposition is not converted into a failed run.

| Finding | Exact prepared IDs | Translation/adapters | Executed disposition |
| --- | --- | --- | --- |
| F01 | `N12-A` | `drafts/F01_F05/F01_TRANSLATION.md`; no legal complete adapter under original rule 12 | No run; documentary wording conflict |
| F02 | `N05-A`, `N06-A`, `N06-B` | `drafts/F01_F05/F02_TRANSLATIONS.md`; legal documentary pairs in its `rig1/` folder | No separate Part B run; N05-A also appears in Part A |
| F03 | `T39-B`, `T39-D`, `T39-I`, `C03`, `N27-A`, `N27-B` | `drafts/F01_F05/F03_TRANSLATIONS.md`; adapters only where no reading must be selected | No run; unresolved or documentary cases |
| F04 | `N14-A`, `N15-A`, `N15-B` | `drafts/F01_F05/F04_TRANSLATIONS.md` and matching `rig1/` pairs | Frozen and patched rig 1 for all three, plus labelled direct probes; evidence in `runs/F01_F05/` |
| F05 | `T21-B`, `T21-D`, `T21-I`, `N17-A`, `N17-B` | T21 in `drafts/F01_F05/F05_T21_TRANSLATIONS.md`; governing N17 translations/pairs under `selected/` | T21 no run; N17-A frozen/patched rig 2; N17-B frozen/patched rig 1; direct probes in `runs/F01_F05/` |
| F06 | `N16-A`, `N16-B` | `drafts/F06_F10/translations/F06.md`; N16-A rig-2 draft plus selected rig-1 projection; N16-B rig-1 draft | N16-A frozen/patched on both projections; N16-B frozen/patched rig 1; direct probes in `runs/F06_F10/` |
| F07 | `N19-A`, `N19-B`, `N20-A`, `N20-B` | `drafts/F06_F10/translations/F07.md` and matching `rig1/` pairs | Frozen/patched rig 1 for all four plus direct probes |
| F08 | `N23-A`, `N23-B` | `drafts/F06_F10/translations/F08.md` and matching `rig1/` pairs | Frozen/patched rig 1 for both; all-lines/remove-`s1` structural probes |
| F09 | `N25-A`, `N25-B` | `drafts/F06_F10/translations/F09.md` and matching `rig1/` pairs | Frozen/patched rig 1 for both; patched JSON what-if is adjudicative |
| F10 | `T26-B`, `T26-D`, `T26-I`, `T27-B`, `T27-D`, `T27-I` | `drafts/F06_F10/translations/F10.md` and matching `rig1/` pairs | T26 no run; T27-B/D/I frozen/patched rig 1 plus direct probes |
| F11 | `N29-A`, `N29-B` | Per-ID files and pairs under `drafts/F11_F15/` | Translation only; event identity is not a checker verdict |
| F12 | `N22-A`, `N22-B` | Per-ID files and pairs under `drafts/F11_F15/` | Frozen/patched rig 1 plus labelled dependency/relevance probes in `runs/F11_F15/` |
| F13 | `T61-B`, `T61-D`, `T61-I`, `T76-B`, `T76-D`, `T76-I` | Per-ID files and pairs under `drafts/F11_F15/` | No run; document-rule and question-fidelity cases |
| F14 | `N30-A`, `N30-B` | Per-ID files and pairs under `drafts/F11_F15/` | N30-A frozen/patched rig 1; N30-B frozen/patched rig 2; direct form/shape probes |
| F15 | `N18-A`, `N18-B` | Per-ID files and pairs under `drafts/F11_F15/` | Frozen/patched rig 1 plus exact relational co-reference and contradiction probes |

The prospective governing roles are in `PART_B_PREREGISTERED_RUN_MATRIX.md`. Some slice-level draft matrices are retained as preparation history even where a later pre-output review selected a different adapter. Exact run commands and hashes, rather than draft proposals, identify every executed input.
