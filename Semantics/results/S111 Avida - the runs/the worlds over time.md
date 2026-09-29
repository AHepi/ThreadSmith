# S111 the worlds over time (written by tools/s111_measure_the_worlds_over_time.py)

Each cell: the mean over the seeds, with the smallest and largest in brackets. "At the last save": update 50,000.

| measure | low |
|---|---|
| copy error rate | 0.0025 |
| runs | 3 |
| births with offspring identical to parent (C3) | 0.671 (0.644 to 0.692) |
| births per organism per update (C4) | 0.0586 (0.0521 to 0.0637) |
| average generation at the end (C4) | 1132 (813 to 1348) |
| fewest organisms from update 1,000 on (M1) | 3597 (3597 to 3598) |
| essential sites still the ancestor's (R3), at the last save | 0.962 (0.957 to 0.971) |
| non-essential sites still the ancestor's (R3), at the last save | 0.889 (0.884 to 0.896) |
| organisms with the ancestor's copy loop exactly (M2), at the last save | 0.933 (0.906 to 0.950) |
| organisms with the ancestor's head exactly (M2), at the last save | 0.892 (0.887 to 0.900) |
| organisms identical to the ancestor (M2), at the last save | 0.000 (0.000 to 0.000) |
| mean genome length, at the last save | 106.7 (104.3 to 110.5) |
| living genotypes, at the last save | 2095.0 (2043.0 to 2157.0) |
| runs performing each task at the end (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU) | 3 3 3 3 3 3 3 0 0 |

## Over time, per run: essential / non-essential sites still the ancestor's, and share with the copy loop exactly

| run | 1000 | 10000 | 20000 | 30000 | 40000 | 50000 |
|---|---|---|---|---|---|---|
| main_low_seed1 | 0.96 / 0.88 / 0.94 | - | - | - | - | - |
| main_low_seed2 | 0.96 / 0.89 / 0.91 | - | - | - | - | - |
| main_low_seed3 | 0.97 / 0.90 / 0.95 | - | - | - | - | - |

## Tasks at the end, organisms performing each (of about 3,600)

| run | NOT | NAND | AND | ORN | OR | ANDN | NOR | XOR | EQU |
|---|---|---|---|---|---|---|---|---|---|
| main_low_seed1 | 3493 | 2883 | 2 | 3513 | 3390 | 6 | 3399 | 0 | 0 |
| main_low_seed2 | 3446 | 3345 | 2775 | 3438 | 3290 | 424 | 3279 | 0 | 0 |
| main_low_seed3 | 2012 | 14 | 4 | 3311 | 3344 | 26 | 1466 | 0 | 0 |

## Controls

- control_K1_random_programs: {"last_update_with_organisms": 66, "organisms_at_last_line": 8, "births_after_update_0": 0}
- control_K2_copy_loop_knocked_out: {"last_update_with_organisms": 65, "organisms_at_last_line": 1, "births_after_update_0": 0}
- control_K3_knocked_out_nothing_dies_of_age: {"last_update_with_organisms": 2000, "organisms_at_last_line": 1, "births_after_update_0": 0}
- control_K4_knocked_out_beside_ancestor_nothing_dies_of_age: {"last_update_with_organisms": 2000, "organisms_at_last_line": 3600, "births_after_update_0": 266353, "knocked_out_alive_at_500": 1108, "organisms_at_500": 3137, "knocked_out_alive_at_1000": 1918, "organisms_at_1000": 3600, "knocked_out_alive_at_1500": 2297, "organisms_at_1500": 3600, "knocked_out_alive_at_2000": 2873, "organisms_at_2000": 3600}
- control_K5_no_mutation: {"last_update_with_organisms": 5000, "organisms_at_last_line": 3600, "births_after_update_0": 1027, "at_5000": {"organisms": 3600, "genotypes": 1, "copy_loop_exact": 1.0, "head_exact": 1.0, "whole_ancestor": 1.0, "mean_length": 100.0, "conserved_essential": 1.0, "conserved_non_essential": 1.0}, "share_births_identical_to_parent": 1.0}
