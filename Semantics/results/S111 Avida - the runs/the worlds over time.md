# S111 the worlds over time (written by tools/s111_measure_the_worlds_over_time.py)

Each cell: the mean over the seeds, with the smallest and largest in brackets. "At the last save": update 50,000.

| measure | low | default | high |
|---|---|---|---|
| copy error rate | 0.0025 | 0.0075 | 0.02 |
| runs | 3 | 3 | 3 |
| births with offspring identical to parent (C3) | 0.693 (0.684 to 0.704) | 0.400 (0.356 to 0.445) | 0.131 (0.090 to 0.154) |
| births per organism per update (C4) | 0.0751 (0.0707 to 0.0815) | 0.0603 (0.0438 to 0.0749) | 0.0363 (0.0234 to 0.0429) |
| average generation at the end (C4) | 7474 (7220 to 7859) | 9208 (7735 to 10201) | 11521 (6310 to 15940) |
| fewest organisms from update 1,000 on (M1) | 3597 (3597 to 3598) | 3577 (3558 to 3588) | 3497 (3481 to 3518) |
| essential sites still the ancestor's (R3), at the last save | 0.836 (0.682 to 0.930) | 0.682 (0.567 to 0.788) | 0.582 (0.495 to 0.724) |
| non-essential sites still the ancestor's (R3), at the last save | 0.178 (0.150 to 0.205) | 0.094 (0.056 to 0.123) | 0.051 (0.034 to 0.059) |
| organisms with the ancestor's copy loop exactly (M2), at the last save | 0.000 (0.000 to 0.000) | 0.000 (0.000 to 0.000) | 0.163 (0.000 to 0.487) |
| organisms with the ancestor's head exactly (M2), at the last save | 0.373 (0.000 to 0.743) | 0.000 (0.000 to 0.000) | 0.000 (0.000 to 0.000) |
| organisms whose genotype still copies itself exactly (added), at the last save | 0.857 (0.829 to 0.872) | 0.710 (0.659 to 0.768) | 0.650 (0.623 to 0.686) |
| organisms identical to the ancestor (M2), at the last save | 0.000 (0.000 to 0.000) | 0.000 (0.000 to 0.000) | 0.000 (0.000 to 0.000) |
| mean genome length, at the last save | 105.3 (99.2 to 108.4) | 109.4 (90.3 to 131.5) | 87.8 (75.5 to 100.5) |
| living genotypes, at the last save | 1695.3 (1634.0 to 1728.0) | 2801.0 (2660.0 to 2966.0) | 3281.0 (3253.0 to 3318.0) |
| runs performing each task at the end (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU) | 3 3 3 3 3 3 3 1 2 | 3 3 3 3 3 3 3 2 2 | 3 3 3 3 3 3 3 0 2 |

## Over time, per run: essential / non-essential sites still the ancestor's, and share with the copy loop exactly

Each cell: essential sites / non-essential sites still the ancestor's / share with the copy loop exactly / share whose genotype still copies itself exactly (added).

| run | 1000 | 10000 | 20000 | 30000 | 40000 | 50000 |
|---|---|---|---|---|---|---|
| main_low_seed1 | 0.96 / 0.88 / 0.94 / 0.87 | 0.91 / 0.23 / 0.00 / 0.85 | 0.92 / 0.13 / 0.00 / 0.83 | 0.91 / 0.14 / 0.00 / 0.83 | 0.88 / 0.14 / 0.00 / 0.86 | 0.90 / 0.15 / 0.00 / 0.87 |
| main_low_seed2 | 0.96 / 0.89 / 0.91 / 0.86 | 0.99 / 0.35 / 0.01 / 0.86 | 0.99 / 0.27 / 0.00 / 0.82 | 0.99 / 0.26 / 0.00 / 0.83 | 0.95 / 0.22 / 0.00 / 0.83 | 0.93 / 0.20 / 0.00 / 0.83 |
| main_low_seed3 | 0.97 / 0.90 / 0.95 / 0.80 | 0.92 / 0.33 / 0.00 / 0.89 | 0.83 / 0.23 / 0.00 / 0.81 | 0.76 / 0.21 / 0.00 / 0.82 | 0.71 / 0.18 / 0.00 / 0.83 | 0.68 / 0.18 / 0.00 / 0.87 |
| main_default_seed1 | 0.95 / 0.73 / 0.89 / 0.70 | 0.72 / 0.17 / 0.01 / 0.75 | 0.79 / 0.12 / 0.00 / 0.78 | 0.80 / 0.11 / 0.00 / 0.71 | 0.75 / 0.11 / 0.00 / 0.73 | 0.79 / 0.12 / 0.00 / 0.70 |
| main_default_seed2 | 0.94 / 0.70 / 0.89 / 0.74 | 0.78 / 0.16 / 0.09 / 0.76 | 0.59 / 0.13 / 0.00 / 0.74 | 0.60 / 0.13 / 0.00 / 0.67 | 0.60 / 0.11 / 0.00 / 0.64 | 0.57 / 0.10 / 0.00 / 0.66 |
| main_default_seed3 | 0.95 / 0.73 / 0.88 / 0.72 | 0.87 / 0.09 / 0.01 / 0.79 | 0.84 / 0.07 / 0.00 / 0.72 | 0.73 / 0.06 / 0.00 / 0.74 | 0.71 / 0.06 / 0.00 / 0.75 | 0.69 / 0.06 / 0.00 / 0.77 |
| main_high_seed1 | 0.91 / 0.49 / 0.78 / 0.49 | 0.79 / 0.06 / 0.18 / 0.62 | 0.66 / 0.06 / 0.00 / 0.66 | 0.72 / 0.06 / 0.00 / 0.59 | 0.71 / 0.06 / 0.20 / 0.58 | 0.72 / 0.06 / 0.49 / 0.62 |
| main_high_seed2 | 0.88 / 0.39 / 0.76 / 0.54 | 0.74 / 0.07 / 0.29 / 0.61 | 0.71 / 0.05 / 0.10 / 0.67 | 0.68 / 0.05 / 0.48 / 0.67 | 0.38 / 0.05 / 0.00 / 0.66 | 0.49 / 0.03 / 0.00 / 0.69 |
| main_high_seed3 | 0.90 / 0.51 / 0.79 / 0.50 | 0.75 / 0.07 / 0.17 / 0.62 | 0.72 / 0.08 / 0.06 / 0.61 | 0.60 / 0.07 / 0.00 / 0.65 | 0.59 / 0.06 / 0.00 / 0.65 | 0.53 / 0.06 / 0.00 / 0.64 |

## Tasks at the end, organisms performing each (of about 3,600)

| run | NOT | NAND | AND | ORN | OR | ANDN | NOR | XOR | EQU |
|---|---|---|---|---|---|---|---|---|---|
| main_low_seed1 | 3557 | 3523 | 3524 | 3510 | 3351 | 3475 | 3372 | 0 | 0 |
| main_low_seed2 | 3464 | 3442 | 25 | 3494 | 3309 | 3216 | 3323 | 3179 | 3222 |
| main_low_seed3 | 3479 | 3553 | 17 | 3523 | 3435 | 3512 | 3407 | 0 | 3316 |
| main_default_seed1 | 3491 | 3494 | 2738 | 3054 | 2983 | 3316 | 2750 | 2785 | 2799 |
| main_default_seed2 | 3460 | 3344 | 3088 | 3351 | 3161 | 3315 | 3158 | 2688 | 2975 |
| main_default_seed3 | 3255 | 3353 | 3289 | 3272 | 3069 | 2975 | 3072 | 0 | 0 |
| main_high_seed1 | 2829 | 2755 | 2131 | 2862 | 2556 | 2680 | 2372 | 0 | 2079 |
| main_high_seed2 | 2850 | 1814 | 136 | 2805 | 2393 | 2900 | 2437 | 0 | 1740 |
| main_high_seed3 | 3055 | 3135 | 2666 | 3172 | 2907 | 2651 | 2229 | 0 | 0 |

## Controls

- control_K1_random_programs: {"last_update_with_organisms": 66, "organisms_at_last_line": 8, "births_after_update_0": 0}
- control_K2_copy_loop_knocked_out: {"last_update_with_organisms": 65, "organisms_at_last_line": 1, "births_after_update_0": 0}
- control_K3_knocked_out_nothing_dies_of_age: {"last_update_with_organisms": 2000, "organisms_at_last_line": 1, "births_after_update_0": 0}
- control_K4_knocked_out_beside_ancestor_nothing_dies_of_age: {"last_update_with_organisms": 2000, "organisms_at_last_line": 3600, "births_after_update_0": 266353, "knocked_out_alive_at_500": 0, "organisms_at_500": 3137, "knocked_out_alive_at_1000": 0, "organisms_at_1000": 3600, "knocked_out_alive_at_1500": 0, "organisms_at_1500": 3600, "knocked_out_alive_at_2000": 0, "organisms_at_2000": 3600}
- control_K5_no_mutation: {"last_update_with_organisms": 5000, "organisms_at_last_line": 3600, "births_after_update_0": 1027, "at_5000": {"organisms": 3600, "genotypes": 1, "copy_loop_exact": 1.0, "head_exact": 1.0, "whole_ancestor": 1.0, "mean_length": 100.0, "conserved_essential": 1.0, "conserved_non_essential": 1.0}, "share_births_identical_to_parent": 1.0}
