#### Agreement per field, per set of 48 and pooled (agree / disagree / unreadable)

| field | set | harness (stage_b.py) | independent (recompute.py) | threshold: harness / independent | disagreeing and unreadable reports named alike | match |
|---|---|---|---|---|---|---|
| test_remove | p52 | 46 / 2 / 0 | 46 / 2 / 0 | 39 / 39 | yes | yes |
| test_remove | repeat | 48 / 0 / 0 | 48 / 0 / 0 | 39 / 39 | yes | yes |
| test_remove | pooled 96 | 94 / 2 / 0 | 94 / 2 / 0 | (never the gate) | | yes |
| test_remove | **certified** | True | True | | | yes |
| test_swap | p52 | 40 / 8 / 0 | 40 / 8 / 0 | 42 / 42 | yes | yes |
| test_swap | repeat | 48 / 0 / 0 | 48 / 0 / 0 | 42 / 42 | yes | yes |
| test_swap | pooled 96 | 88 / 8 / 0 | 88 / 8 / 0 | (never the gate) | | yes |
| test_swap | **certified** | False | False | | | yes |
| test_poke | p52 | 39 / 9 / 0 | 39 / 9 / 0 | 42 / 42 | yes | yes |
| test_poke | repeat | 38 / 10 / 0 | 38 / 10 / 0 | 42 / 42 | yes | yes |
| test_poke | pooled 96 | 77 / 19 / 0 | 77 / 19 / 0 | (never the gate) | | yes |
| test_poke | **certified** | False | False | | | yes |
| test_flip | p52 | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| test_flip | repeat | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| test_flip | pooled 96 | 94 / 2 / 0 | 94 / 2 / 0 | (never the gate) | | yes |
| test_flip | **certified** | True | True | | | yes |
| test_reverse | p52 | 41 / 7 / 0 | 41 / 7 / 0 | 39 / 39 | yes | yes |
| test_reverse | repeat | 42 / 6 / 0 | 42 / 6 / 0 | 39 / 39 | yes | yes |
| test_reverse | pooled 96 | 83 / 13 / 0 | 83 / 13 / 0 | (never the gate) | | yes |
| test_reverse | **certified** | True | True | | | yes |
| test_hunt | p52 | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| test_hunt | repeat | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| test_hunt | pooled 96 | 94 / 2 / 0 | 94 / 2 / 0 | (never the gate) | | yes |
| test_hunt | **certified** | True | True | | | yes |
| test_addjob | p52 | 39 / 9 / 0 | 39 / 9 / 0 | 39 / 39 | yes | yes |
| test_addjob | repeat | 43 / 5 / 0 | 43 / 5 / 0 | 39 / 39 | yes | yes |
| test_addjob | pooled 96 | 82 / 14 / 0 | 82 / 14 / 0 | (never the gate) | | yes |
| test_addjob | **certified** | True | True | | | yes |
| test_rival | p52 | 41 / 7 / 0 | 41 / 7 / 0 | 39 / 39 | yes | yes |
| test_rival | repeat | 48 / 0 / 0 | 48 / 0 / 0 | 39 / 39 | yes | yes |
| test_rival | pooled 96 | 89 / 7 / 0 | 89 / 7 / 0 | (never the gate) | | yes |
| test_rival | **certified** | True | True | | | yes |
| test_pull | p52 | 44 / 4 / 0 | 44 / 4 / 0 | 39 / 39 | yes | yes |
| test_pull | repeat | 46 / 2 / 0 | 46 / 2 / 0 | 39 / 39 | yes | yes |
| test_pull | pooled 96 | 90 / 6 / 0 | 90 / 6 / 0 | (never the gate) | | yes |
| test_pull | **certified** | True | True | | | yes |
| test_patches | p52 | 41 / 7 / 0 | 41 / 7 / 0 | 39 / 39 | yes | yes |
| test_patches | repeat | 48 / 0 / 0 | 48 / 0 / 0 | 39 / 39 | yes | yes |
| test_patches | pooled 96 | 89 / 7 / 0 | 89 / 7 / 0 | (never the gate) | | yes |
| test_patches | **certified** | True | True | | | yes |
| test_inside | p52 | 40 / 8 / 0 | 40 / 8 / 0 | 39 / 39 | yes | yes |
| test_inside | repeat | 40 / 8 / 0 | 40 / 8 / 0 | 39 / 39 | yes | yes |
| test_inside | pooled 96 | 80 / 16 / 0 | 80 / 16 / 0 | (never the gate) | | yes |
| test_inside | **certified** | True | True | | | yes |
| shape_elements | p52 | 35 / 13 / 0 | 35 / 13 / 0 | 39 / 39 | yes | yes |
| shape_elements | repeat | 41 / 7 / 0 | 41 / 7 / 0 | 39 / 39 | yes | yes |
| shape_elements | pooled 96 | 76 / 20 / 0 | 76 / 20 / 0 | (never the gate) | | yes |
| shape_elements | **certified** | False | False | | | yes |
| shape | p52 | 48 / 0 / 0 | 48 / 0 / 0 | 44 / 44 | yes | yes |
| shape | repeat | 46 / 2 / 0 | 46 / 2 / 0 | 44 / 44 | yes | yes |
| shape | pooled 96 | 94 / 2 / 0 | 94 / 2 / 0 | (never the gate) | | yes |
| shape | **certified** | True | True | | | yes |
| turned_own_test | p52 | 45 / 3 / 0 | 45 / 3 / 0 | 44 / 44 | yes | yes |
| turned_own_test | repeat | 47 / 1 / 0 | 47 / 1 / 0 | 44 / 44 | yes | yes |
| turned_own_test | pooled 96 | 92 / 4 / 0 | 92 / 4 / 0 | (never the gate) | | yes |
| turned_own_test | **certified** | True | True | | | yes |
| same_explanation | p52 | 48 / 0 / 0 | 48 / 0 / 0 | 44 / 44 | yes | yes |
| same_explanation | repeat | 47 / 1 / 0 | 47 / 1 / 0 | 44 / 44 | yes | yes |
| same_explanation | pooled 96 | 95 / 1 / 0 | 95 / 1 / 0 | (never the gate) | | yes |
| same_explanation | **certified** | True | True | | | yes |
| marks_per_part | p52 | reports agreeing 37; gate: 6 of 16 documents | reports agreeing 37; gate: 37 of 48 reports | 14 of 16 documents / 40 of 48 reports | yes | **no** |
| marks_per_part | repeat | reports agreeing 44; gate: 0 of 2 documents | reports agreeing 44; gate: 44 of 48 reports | 2 of 2 documents / 40 of 48 reports | yes | **no** |
| marks_per_part | pooled 96 | 81 / 14 / 1 | 81 / 14 / 1 | (never the gate) | | yes |
| marks_per_part | **certified** | False | False | | | yes |
| pairs_that_pull | p52 | 47 / 1 / 0 | 47 / 1 / 0 | 40 / 40 | yes | yes |
| pairs_that_pull | repeat | 46 / 2 / 0 | 46 / 2 / 0 | 40 / 40 | yes | yes |
| pairs_that_pull | pooled 96 | 93 / 3 / 0 | 93 / 3 / 0 | (never the gate) | | yes |
| pairs_that_pull | **certified** | True | True | | | yes |
| rivals_built | p52 | 36 / 9 / 3 | 36 / 9 / 3 | 40 / 40 | yes | yes |
| rivals_built | repeat | 41 / 3 / 4 | 41 / 3 / 4 | 40 / 40 | yes | yes |
| rivals_built | pooled 96 | 77 / 12 / 7 | 77 / 12 / 7 | (never the gate) | | yes |
| rivals_built | **certified** | False | False | | | yes |
| remove_in_groups | p52 | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| remove_in_groups | repeat | 45 / 3 / 0 | 45 / 3 / 0 | 39 / 39 | yes | yes |
| remove_in_groups | pooled 96 | 92 / 4 / 0 | 92 / 4 / 0 | (never the gate) | | yes |
| remove_in_groups | **certified** | True | True | | | yes |
| question_identity | p52 | 1 / 0 / 47 | 1 / 0 / 47 | 46 / 46 | yes | yes |
| question_identity | repeat | 3 / 1 / 44 | 3 / 1 / 44 | 46 / 46 | yes | yes |
| question_identity | pooled 96 | 4 / 1 / 91 | 4 / 1 / 91 | (never the gate) | | yes |
| question_identity | **certified** | False | False | | | yes |
| modules_self_reported | p52 | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| modules_self_reported | repeat | 47 / 1 / 0 | 47 / 1 / 0 | 39 / 39 | yes | yes |
| modules_self_reported | pooled 96 | 94 / 2 / 0 | 94 / 2 / 0 | (never the gate) | | yes |
| modules_self_reported | **certified** | True | True | | | yes |
| marks_outside_closed_list | p52 | 40 / 5 / 3 | 40 / 5 / 3 | 39 (printed; not a candidate) / none | yes | **no** |
| marks_outside_closed_list | repeat | 46 / 2 / 0 | 46 / 2 / 0 | 39 (printed; not a candidate) / none | yes | **no** |
| marks_outside_closed_list | pooled 96 | 86 / 7 / 3 | 86 / 7 / 3 | (never the gate) | | yes |
| marks_outside_closed_list | **certified** | False (not a candidate) | none (not a candidate) | | | **no** |
| attributions | p52 | 39 / 9 / 0 | 39 / 9 / 0 | 39 / 39 | yes | yes |
| attributions | repeat | 41 / 7 / 0 | 41 / 7 / 0 | 39 / 39 | yes | yes |
| attributions | pooled 96 | 80 / 16 / 0 | 80 / 16 / 0 | (never the gate) | | yes |
| attributions | **certified** | True | True | | | yes |
| layer_at_fault | p52 | 35 / 11 / 2 | 35 / 11 / 2 | 39 (printed; not a candidate) / none | yes | **no** |
| layer_at_fault | repeat | 31 / 17 / 0 | 31 / 17 / 0 | 39 (printed; not a candidate) / none | yes | **no** |
| layer_at_fault | pooled 96 | 66 / 28 / 2 | 66 / 28 / 2 | (never the gate) | | yes |
| layer_at_fault | **certified** | False (not a candidate) | none (not a candidate) | | | **no** |
| modules_served | p52 / repeat / pooled | 0/0/48, 0/0/48, 0/0/96 | not counted | 39 printed / none | | not compared |

#### W10.17: closed-list values per enum field, per marker (of 96)

| field | first marker: harness / independent | second marker: harness / independent | match |
|---|---|---|---|
| test_remove | 96 / 96 | 96 / 96 | yes |
| test_swap | 96 / 96 | 96 / 96 | yes |
| test_poke | 96 / 96 | 96 / 96 | yes |
| test_flip | 96 / 96 | 96 / 96 | yes |
| test_reverse | 96 / 96 | 96 / 96 | yes |
| test_hunt | 96 / 96 | 96 / 96 | yes |
| test_addjob | 96 / 96 | 96 / 96 | yes |
| test_rival | 96 / 96 | 96 / 96 | yes |
| test_pull | 96 / 96 | 96 / 96 | yes |
| test_patches | 96 / 96 | 96 / 96 | yes |
| test_inside | 96 / 96 | 96 / 96 | yes |
| shape | 96 / 96 | 96 / 96 | yes |
| turned_own_test | 96 / 96 | 96 / 96 | yes |
| same_explanation | 96 / 96 | 96 / 96 | yes |
| remove_in_groups | 96 / 96 | 96 / 96 | yes |
| question_identity | 10 / 10 | 14 / 14 | yes |
| layer_at_fault | 95 / 95 | 95 / 95 | yes |
| fields named unreadable | ['question_identity'] | ['question_identity'] | yes |

#### W10.16: the split on the twice-reworded fields

Harness: stage_b.py (read set = folder-qualified record file names; percentages over readable reports). Independent, primary: reading B (those plus the run ids named in section 14.1; percentages over all reports in the subset). Independent, reading A over readable: the harness's reading, as the independent also computed it.

| field | quantity | harness | independent, primary (B, of n) | match | independent, reading A over readable | match |
|---|---|---|---|---|---|---|
| marks_per_part | read n | 20 | 26 | **no** | 20 | yes |
| marks_per_part | read agree | 20 | 23 | **no** | 20 | yes |
| marks_per_part | unread n | 76 | 70 | **no** | 76 | yes |
| marks_per_part | unread agree | 61 | 58 | **no** | 61 | yes |
| marks_per_part | read % | 100.0 | 88.5 | **no** | 100.0 | yes |
| marks_per_part | unread % | 81.3 | 82.9 | **no** | 81.3 | yes |
| marks_per_part | gap, points | 18.7 | 5.6 | **no** | 18.7 | yes |
| pairs_that_pull | read n | 20 | 26 | **no** | 20 | yes |
| pairs_that_pull | read agree | 19 | 24 | **no** | 19 | yes |
| pairs_that_pull | unread n | 76 | 70 | **no** | 76 | yes |
| pairs_that_pull | unread agree | 74 | 69 | **no** | 74 | yes |
| pairs_that_pull | read % | 95.0 | 92.3 | **no** | 95.0 | yes |
| pairs_that_pull | unread % | 97.4 | 98.6 | **no** | 97.4 | yes |
| pairs_that_pull | gap, points | -2.4 | -6.3 | **no** | -2.4 | yes |
| rivals_built | read n | 20 | 26 | **no** | 20 | yes |
| rivals_built | read agree | 17 | 23 | **no** | 17 | yes |
| rivals_built | unread n | 76 | 70 | **no** | 76 | yes |
| rivals_built | unread agree | 60 | 54 | **no** | 60 | yes |
| rivals_built | read % | 94.4 | 88.5 | **no** | 94.4 | yes |
| rivals_built | unread % | 84.5 | 77.1 | **no** | 84.5 | yes |
| rivals_built | gap, points | 9.9 | 11.3 | **no** | 9.9 | yes |
| all three | the read reports (the set) | 20 reports | 26 reports | **no** | 20 reports (A) | yes |
| all three | falsified on | ['marks_per_part'] | ['rivals_built'] | **no** | ['marks_per_part'] | yes |
| pairs_that_pull | falsified under any of the independent's 5 readings x 2 bases | harness: False (its one reading) | False | yes | | |

#### The certified list and the predictions

| item | harness | independent | match |
|---|---|---|---|
| certified list | 16 fields | 16 fields (the same names) | yes |
| P3.1 holds | True | True | yes |
| P3.1 fields reaching 44 in both sets | ['same_explanation', 'shape', 'turned_own_test'] | ['same_explanation', 'shape', 'turned_own_test'] | yes |
| P3.2 holds | False | False | yes |
| P3.3 holds | False | False | yes |
| P3.4 holds | False | False | yes |
| P3.5 holds | False | False | yes |
| other fields at 39: the fields failing (harness: implied by its certified list) | ['shape_elements'] | ['shape_elements'] | yes |
| W10.16 holds | False | False | yes |
| W10.17 holds | False | False | yes |

Totals (never a score, only the size of the comparison): 450 items, 417 matching; numbers 317 compared, 288 matching; verdicts 31 compared, 29 matching; lists 102 compared, 100 matching. Cause checks 26, matching 26.
