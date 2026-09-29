# S111 Marletto's test on the logic tasks (written by tools/s111_marletto_test_on_the_logic_tasks.py)

Update 50,000. Tasks performed by at least 10% of the organisms. Shares are of the organisms covered (the most common genotypes, together at least 90% of the organisms, at most 300 genotypes), each genotype run alone in the test processor.

Columns: the sites of the most common genotype whose single knockout stops the task; of them, the "task-only" sites (copying survives their knockout), with their instructions; then the share of covered organisms whose genotype performs the task: as found; after the dominant's task sites are knocked out in the dominant only; after every genotype's own task sites are knocked out (all of them, as planned; this also stops copying); after every genotype's own task-only sites are knocked out (added), with the share of the former performers that still copy themselves. Last column: organisms covered / organisms (with the plan's cap of 300 genotypes; then without it).

| run | task | dominant: stopping sites | task-only sites (instructions) | as found | dominant only | every genotype, all sites | every genotype, task-only sites | still copying | covered |
|---|---|---|---|---|---|---|---|---|---|
| main_low_seed1 | NOT | 21 | 2 (nand IO) | 0.998 | 0.984 | 0.000 | 0.428 | 1.000 | 2036 / 3600 |
| main_low_seed1 | NAND | 26 | 7 (IO sub nop-C IO nop-C IO nop-C) | 0.998 | 0.984 | 0.000 | 0.016 | 0.993 | 2036 / 3600 |
| main_low_seed1 | AND | 26 | 7 (IO IO nop-C add inc nop-C IO) | 1.000 | 0.987 | 0.000 | 0.000 | 0.996 | 2036 / 3600 |
| main_low_seed1 | ORN | 26 | 7 (IO sub nop-C IO nand nand IO) | 0.998 | 0.984 | 0.000 | 0.149 | 1.000 | 2036 / 3600 |
| main_low_seed1 | OR | 40 | 21 (IO IO nop-C nand nand add sub nop-C IO dec nop-C IO nand add nop-C nand nand inc nop-C nand IO) | 1.000 | 0.987 | 0.000 | 0.000 | 0.981 | 2036 / 3600 |
| main_low_seed1 | ANDN | 27 | 8 (IO add inc dec nop-C pop nand nand) | 1.000 | 0.987 | 0.000 | 0.057 | 0.980 | 2036 / 3600 |
| main_low_seed1 | NOR | 38 | 19 (IO IO nop-C nand nand add sub nop-C IO dec nop-C IO nand add nop-C inc nop-C IO nop-C) | 1.000 | 0.987 | 0.000 | 0.000 | 0.981 | 2036 / 3600 |
| main_low_seed1 (no cap) | NOT | 21 | 2 (nand IO) | 0.896 | 0.887 | 0.000 | 0.390 | 1.000 | 3240 / 3600 |
| main_low_seed1 (no cap) | NAND | 26 | 7 (IO sub nop-C IO nop-C IO nop-C) | 0.884 | 0.876 | 0.000 | 0.022 | 0.991 | 3240 / 3600 |
| main_low_seed1 (no cap) | AND | 26 | 7 (IO IO nop-C add inc nop-C IO) | 0.882 | 0.874 | 0.000 | 0.009 | 0.996 | 3240 / 3600 |
| main_low_seed1 (no cap) | ORN | 26 | 7 (IO sub nop-C IO nand nand IO) | 0.881 | 0.872 | 0.000 | 0.122 | 1.000 | 3240 / 3600 |
| main_low_seed1 (no cap) | OR | 40 | 21 (IO IO nop-C nand nand add sub nop-C IO dec nop-C IO nand add nop-C nand nand inc nop-C nand IO) | 0.830 | 0.821 | 0.000 | 0.006 | 0.981 | 3240 / 3600 |
| main_low_seed1 (no cap) | ANDN | 27 | 8 (IO add inc dec nop-C pop nand nand) | 0.869 | 0.861 | 0.000 | 0.056 | 0.981 | 3240 / 3600 |
| main_low_seed1 (no cap) | NOR | 38 | 19 (IO IO nop-C nand nand add sub nop-C IO dec nop-C IO nand add nop-C inc nop-C IO nop-C) | 0.834 | 0.826 | 0.000 | 0.006 | 0.982 | 3240 / 3600 |
| main_low_seed2 | NOT | 18 | 5 (push nop-C nand swap nop-C) | 0.989 | 0.967 | 0.000 | 0.402 | 1.000 | 1997 / 3600 |
| main_low_seed2 | NAND | 25 | 12 (push pop nop-C swap nop-A nop-C nop-C nop-A nand swap IO nop-C) | 0.997 | 0.975 | 0.000 | 0.128 | 0.973 | 1997 / 3600 |
| main_low_seed2 | ORN | 21 | 8 (push IO nop-C nand nand nop-C IO nop-C) | 0.996 | 0.974 | 0.000 | 0.145 | 0.998 | 1997 / 3600 |
| main_low_seed2 | OR | 34 | 21 (push pop nop-C nop-A IO nop-C nop-C nop-C IO nop-C nop-A nand nand IO nop-C sub nop-C nand nop-C nop-C IO) | 0.995 | 0.973 | 0.000 | 0.000 | 0.957 | 1997 / 3600 |
| main_low_seed2 | ANDN | 42 | 29 (push swap nop-A IO nop-C nop-C nop-C IO nop-C nand nop-A nand nand IO nop-C push sub nop-C nand nop-C swap nop-C nand nop-C push pop pop sub IO) | 0.994 | 0.972 | 0.000 | 0.000 | 0.963 | 1997 / 3600 |
| main_low_seed2 | NOR | 32 | 19 (push pop nop-C swap nop-A IO nop-C nop-C nop-C IO nop-C nop-A nand nand IO nop-C nop-C IO nop-C) | 0.995 | 0.973 | 0.000 | 0.004 | 0.943 | 1997 / 3600 |
| main_low_seed2 | XOR | 45 | 32 (push pop nop-C swap nop-A IO nop-C nop-C nop-C IO nop-C nand nop-A nand nand IO nop-C sub nop-C nand nop-C swap nop-C nand nop-C push nop-C pop dec sub sub IO) | 0.994 | 0.972 | 0.000 | 0.000 | 0.931 | 1997 / 3600 |
| main_low_seed2 | EQU | 39 | 26 (push pop nop-C swap nop-A IO nop-C nop-C nop-C IO nop-C nand nop-A nand nand IO nop-C sub nop-C nand nop-C swap nop-C nand swap IO) | 0.994 | 0.972 | 0.000 | 0.000 | 0.931 | 1997 / 3600 |
| main_low_seed2 (no cap) | NOT | 18 | 5 (push nop-C nand swap nop-C) | 0.844 | 0.830 | 0.000 | 0.363 | 0.999 | 3240 / 3600 |
| main_low_seed2 (no cap) | NAND | 25 | 12 (push pop nop-C swap nop-A nop-C nop-C nop-A nand swap IO nop-C) | 0.831 | 0.817 | 0.000 | 0.125 | 0.975 | 3240 / 3600 |
| main_low_seed2 (no cap) | ORN | 21 | 8 (push IO nop-C nand nand nop-C IO nop-C) | 0.846 | 0.832 | 0.000 | 0.134 | 0.995 | 3240 / 3600 |
| main_low_seed2 (no cap) | OR | 34 | 21 (push pop nop-C nop-A IO nop-C nop-C nop-C IO nop-C nop-A nand nand IO nop-C sub nop-C nand nop-C nop-C IO) | 0.786 | 0.773 | 0.000 | 0.012 | 0.958 | 3240 / 3600 |
| main_low_seed2 (no cap) | ANDN | 42 | 29 (push swap nop-A IO nop-C nop-C nop-C IO nop-C nand nop-A nand nand IO nop-C push sub nop-C nand nop-C swap nop-C nand nop-C push pop pop sub IO) | 0.760 | 0.747 | 0.000 | 0.010 | 0.963 | 3240 / 3600 |
| main_low_seed2 (no cap) | NOR | 32 | 19 (push pop nop-C swap nop-A IO nop-C nop-C nop-C IO nop-C nop-A nand nand IO nop-C nop-C IO nop-C) | 0.793 | 0.780 | 0.000 | 0.014 | 0.946 | 3240 / 3600 |
| main_low_seed2 (no cap) | XOR | 45 | 32 (push pop nop-C swap nop-A IO nop-C nop-C nop-C IO nop-C nand nop-A nand nand IO nop-C sub nop-C nand nop-C swap nop-C nand nop-C push nop-C pop dec sub sub IO) | 0.750 | 0.736 | 0.000 | 0.011 | 0.932 | 3240 / 3600 |
| main_low_seed2 (no cap) | EQU | 39 | 26 (push pop nop-C swap nop-A IO nop-C nop-C nop-C IO nop-C nand nop-A nand nand IO nop-C sub nop-C nand nop-C swap nop-C nand swap IO) | 0.764 | 0.750 | 0.000 | 0.011 | 0.932 | 3240 / 3600 |
| main_low_seed3 | NOT | 21 | 9 (pop dec swap swap nop-C dec sub inc IO) | 0.995 | 0.981 | 0.000 | 0.526 | 0.999 | 1947 / 3599 |
| main_low_seed3 | NAND | 12 | 0 () | 1.000 | 0.986 | 0.000 | 0.031 | 0.997 | 1947 / 3599 |
| main_low_seed3 | ORN | 19 | 7 (IO nop-C IO IO nand nop-C nand) | 1.000 | 0.986 | 0.000 | 0.000 | 0.997 | 1947 / 3599 |
| main_low_seed3 | OR | 28 | 16 (IO IO IO IO add nop-C inc sub IO nop-C nand nop-C nand nop-C IO nop-C) | 1.000 | 0.986 | 0.000 | 0.000 | 0.999 | 1947 / 3599 |
| main_low_seed3 | ANDN | 21 | 9 (IO nop-A nand add nop-C inc nop-C IO nop-C) | 0.998 | 0.984 | 0.000 | 0.000 | 1.000 | 1947 / 3599 |
| main_low_seed3 | NOR | 31 | 19 (IO IO IO IO add nop-C inc sub IO nop-C nand nop-C nand nop-C push nop-C pop nand IO) | 1.000 | 0.986 | 0.000 | 0.000 | 0.999 | 1947 / 3599 |
| main_low_seed3 | EQU | 37 | 25 (IO nop-C IO nand push IO IO IO IO swap-stk IO add nop-C inc sub IO nop-C nand nop-C nand nop-C swap-stk pop nand IO) | 1.000 | 0.986 | 0.000 | 0.000 | 0.996 | 1947 / 3599 |
| main_low_seed3 (no cap) | NOT | 21 | 9 (pop dec swap swap nop-C dec sub inc IO) | 0.870 | 0.861 | 0.000 | 0.459 | 0.999 | 3240 / 3599 |
| main_low_seed3 (no cap) | NAND | 12 | 0 () | 0.898 | 0.890 | 0.000 | 0.051 | 0.997 | 3240 / 3599 |
| main_low_seed3 (no cap) | ORN | 19 | 7 (IO nop-C IO IO nand nop-C nand) | 0.888 | 0.880 | 0.000 | 0.030 | 0.997 | 3240 / 3599 |
| main_low_seed3 (no cap) | OR | 28 | 16 (IO IO IO IO add nop-C inc sub IO nop-C nand nop-C nand nop-C IO nop-C) | 0.857 | 0.849 | 0.000 | 0.012 | 0.999 | 3240 / 3599 |
| main_low_seed3 (no cap) | ANDN | 21 | 9 (IO nop-A nand add nop-C inc nop-C IO nop-C) | 0.885 | 0.876 | 0.000 | 0.016 | 0.999 | 3240 / 3599 |
| main_low_seed3 (no cap) | NOR | 31 | 19 (IO IO IO IO add nop-C inc sub IO nop-C nand nop-C nand nop-C push nop-C pop nand IO) | 0.845 | 0.836 | 0.000 | 0.012 | 0.998 | 3240 / 3599 |
| main_low_seed3 (no cap) | EQU | 37 | 25 (IO nop-C IO nand push IO IO IO IO swap-stk IO add nop-C inc sub IO nop-C nand nop-C nand nop-C swap-stk pop nand IO) | 0.819 | 0.810 | 0.000 | 0.011 | 0.996 | 3240 / 3599 |
| main_default_seed1 | NOT | 12 | 1 (IO) | 0.994 | 0.982 | 0.000 | 0.158 | 1.000 | 1002 / 3591 |
| main_default_seed1 | NAND | 13 | 2 (nand IO) | 0.984 | 0.972 | 0.000 | 0.069 | 1.000 | 1002 / 3591 |
| main_default_seed1 | AND | 38 | 27 (IO IO IO IO IO IO IO IO swap nop-C nand IO swap nop-C pop nand swap nop-C nand IO nop-A swap-stk IO IO nop-C swap if-less) | 0.924 | 0.912 | 0.000 | 0.000 | 0.955 | 1002 / 3591 |
| main_default_seed1 | ORN | 28 | 17 (IO IO IO IO IO swap nop-C nand IO nop-C IO nop-A IO IO nop-C swap if-less) | 0.956 | 0.944 | 0.000 | 0.078 | 0.954 | 1002 / 3591 |
| main_default_seed1 | OR | 30 | 19 (nop-C IO IO IO nop-A nand if-label nop-A nop-A swap nop-C nand nop-C nand swap nop-C swap IO nop-A) | 0.942 | 0.930 | 0.000 | 0.000 | 0.964 | 1002 / 3591 |
| main_default_seed1 | ANDN | 17 | 6 (IO nop-C nand add inc IO) | 0.969 | 0.957 | 0.000 | 0.084 | 1.000 | 1002 / 3591 |
| main_default_seed1 | NOR | 38 | 27 (nop-C IO nand push IO IO nand if-label nop-A nop-A nop-C nand nop-C nand nop-A swap nop-C pop nand nop-C nop-A swap IO nand add inc IO) | 0.910 | 0.898 | 0.000 | 0.000 | 0.970 | 1002 / 3591 |
| main_default_seed1 | XOR | 37 | 26 (nop-C IO nand push IO IO IO nop-A nand if-label nop-A nop-A swap nop-C nand nop-C nand nop-A swap nop-C pop nand swap nop-C nand IO) | 0.914 | 0.902 | 0.000 | 0.000 | 0.973 | 1002 / 3591 |
| main_default_seed1 | EQU | 37 | 26 (nop-C IO nand push IO IO IO nop-A nand if-label nop-A nop-A swap nop-C nand nop-C nand nop-A swap nop-C pop nand nop-C nop-C IO nop-C) | 0.908 | 0.896 | 0.000 | 0.000 | 0.975 | 1002 / 3591 |
| main_default_seed1 (no cap) | NOT | 12 | 1 (IO) | 0.728 | 0.724 | 0.000 | 0.187 | 0.992 | 3232 / 3591 |
| main_default_seed1 (no cap) | NAND | 13 | 2 (nand IO) | 0.729 | 0.726 | 0.000 | 0.095 | 0.996 | 3232 / 3591 |
| main_default_seed1 (no cap) | AND | 38 | 27 (IO IO IO IO IO IO IO IO swap nop-C nand IO swap nop-C pop nand swap nop-C nand IO nop-A swap-stk IO IO nop-C swap if-less) | 0.516 | 0.513 | 0.000 | 0.017 | 0.960 | 3232 / 3591 |
| main_default_seed1 (no cap) | ORN | 28 | 17 (IO IO IO IO IO swap nop-C nand IO nop-C IO nop-A IO IO nop-C swap if-less) | 0.601 | 0.598 | 0.000 | 0.073 | 0.964 | 3232 / 3591 |
| main_default_seed1 (no cap) | OR | 30 | 19 (nop-C IO IO IO nop-A nand if-label nop-A nop-A swap nop-C nand nop-C nand swap nop-C swap IO nop-A) | 0.578 | 0.574 | 0.000 | 0.024 | 0.970 | 3232 / 3591 |
| main_default_seed1 (no cap) | ANDN | 17 | 6 (IO nop-C nand add inc IO) | 0.680 | 0.677 | 0.000 | 0.104 | 0.996 | 3232 / 3591 |
| main_default_seed1 (no cap) | NOR | 38 | 27 (nop-C IO nand push IO IO nand if-label nop-A nop-A nop-C nand nop-C nand nop-A swap nop-C pop nand nop-C nop-A swap IO nand add inc IO) | 0.520 | 0.516 | 0.000 | 0.018 | 0.964 | 3232 / 3591 |
| main_default_seed1 (no cap) | XOR | 37 | 26 (nop-C IO nand push IO IO IO nop-A nand if-label nop-A nop-A swap nop-C nand nop-C nand nop-A swap nop-C pop nand swap nop-C nand IO) | 0.524 | 0.521 | 0.000 | 0.020 | 0.968 | 3232 / 3591 |
| main_default_seed1 (no cap) | EQU | 37 | 26 (nop-C IO nand push IO IO IO nop-A nand if-label nop-A nop-A swap nop-C nand nop-C nand nop-A swap nop-C pop nand nop-C nop-C IO nop-C) | 0.528 | 0.524 | 0.000 | 0.021 | 0.974 | 3232 / 3591 |
| main_default_seed2 | NOT | 19 | 4 (dec nop-C IO nand) | 0.986 | 0.975 | 0.000 | 0.026 | 1.000 | 835 / 3592 |
| main_default_seed2 | NAND | 23 | 7 (IO pop IO nop-C nand IO nop-C) | 0.943 | 0.932 | 0.000 | 0.038 | 1.000 | 835 / 3592 |
| main_default_seed2 | AND | 30 | 12 (dec nop-C IO nand if-label swap IO pop dec sub IO pop) | 0.945 | 0.934 | 0.000 | 0.613 | 0.977 | 835 / 3592 |
| main_default_seed2 | ORN | 21 | 6 (nand nop-C IO IO nand IO) | 0.969 | 0.958 | 0.000 | 0.045 | 1.000 | 835 / 3592 |
| main_default_seed2 | OR | 29 | 10 (IO nand pop IO IO nand pop nop-C IO nop-C) | 0.962 | 0.951 | 0.000 | 0.000 | 0.955 | 835 / 3592 |
| main_default_seed2 | ANDN | 21 | 6 (dec nop-C swap dec sub IO) | 0.964 | 0.953 | 0.000 | 0.775 | 0.984 | 835 / 3592 |
| main_default_seed2 | NOR | 26 | 8 (IO nand IO IO nand pop nop-C nand) | 0.959 | 0.949 | 0.000 | 0.000 | 0.971 | 835 / 3592 |
| main_default_seed2 | XOR | 45 | 25 (IO nand IO pop IO IO nand push push IO IO IO nop-C IO nand nop-C pop nand push swap-stk dec nop-C pop nand IO) | 0.909 | 0.898 | 0.000 | 0.000 | 0.958 | 835 / 3592 |
| main_default_seed2 | EQU | 38 | 19 (IO nand IO pop IO IO nand push push IO IO IO nop-C IO nand nop-C pop nand IO) | 0.933 | 0.922 | 0.000 | 0.000 | 0.959 | 835 / 3592 |
| main_default_seed2 (no cap) | NOT | 19 | 4 (dec nop-C IO nand) | 0.705 | 0.702 | 0.000 | 0.117 | 0.998 | 3233 / 3592 |
| main_default_seed2 (no cap) | NAND | 23 | 7 (IO pop IO nop-C nand IO nop-C) | 0.684 | 0.682 | 0.000 | 0.101 | 1.000 | 3233 / 3592 |
| main_default_seed2 (no cap) | AND | 30 | 12 (dec nop-C IO nand if-label swap IO pop dec sub IO pop) | 0.607 | 0.604 | 0.000 | 0.366 | 0.979 | 3233 / 3592 |
| main_default_seed2 (no cap) | ORN | 21 | 6 (nand nop-C IO IO nand IO) | 0.681 | 0.679 | 0.000 | 0.100 | 0.997 | 3233 / 3592 |
| main_default_seed2 (no cap) | OR | 29 | 10 (IO nand pop IO IO nand pop nop-C IO nop-C) | 0.624 | 0.621 | 0.000 | 0.050 | 0.972 | 3233 / 3592 |
| main_default_seed2 (no cap) | ANDN | 21 | 6 (dec nop-C swap dec sub IO) | 0.662 | 0.659 | 0.000 | 0.433 | 0.985 | 3233 / 3592 |
| main_default_seed2 (no cap) | NOR | 26 | 8 (IO nand IO IO nand pop nop-C nand) | 0.621 | 0.618 | 0.000 | 0.047 | 0.978 | 3233 / 3592 |
| main_default_seed2 (no cap) | XOR | 45 | 25 (IO nand IO pop IO IO nand push push IO IO IO nop-C IO nand nop-C pop nand push swap-stk dec nop-C pop nand IO) | 0.499 | 0.497 | 0.000 | 0.033 | 0.970 | 3233 / 3592 |
| main_default_seed2 (no cap) | EQU | 38 | 19 (IO nand IO pop IO IO nand push push IO IO IO nop-C IO nand nop-C pop nand IO) | 0.572 | 0.569 | 0.000 | 0.044 | 0.970 | 3233 / 3592 |
| main_default_seed3 | NOT | 13 | 4 (IO IO nand IO) | 0.975 | 0.964 | 0.000 | 0.016 | 0.998 | 1079 / 3598 |
| main_default_seed3 | NAND | 13 | 4 (IO nop-C nand IO) | 0.967 | 0.956 | 0.000 | 0.011 | 1.000 | 1079 / 3598 |
| main_default_seed3 | AND | 17 | 8 (IO nop-C IO nand nand inc add IO) | 0.970 | 0.959 | 0.000 | 0.000 | 1.000 | 1079 / 3598 |
| main_default_seed3 | ORN | 16 | 7 (IO nop-C dec nand IO swap IO) | 0.969 | 0.957 | 0.000 | 0.004 | 0.997 | 1079 / 3598 |
| main_default_seed3 | OR | 19 | 10 (IO nop-C dec nand swap IO nand nand IO nop-C) | 0.963 | 0.952 | 0.000 | 0.000 | 0.998 | 1079 / 3598 |
| main_default_seed3 | ANDN | 22 | 13 (IO nop-C dec nand IO nand swap IO nand add nop-C inc IO) | 0.957 | 0.946 | 0.000 | 0.000 | 0.998 | 1079 / 3598 |
| main_default_seed3 | NOR | 20 | 11 (IO nop-C dec nand IO nand push swap pop nand IO) | 0.957 | 0.946 | 0.000 | 0.000 | 1.000 | 1079 / 3598 |
| main_default_seed3 (no cap) | NOT | 13 | 4 (IO IO nand IO) | 0.706 | 0.703 | 0.000 | 0.066 | 0.999 | 3239 / 3598 |
| main_default_seed3 (no cap) | NAND | 13 | 4 (IO nop-C nand IO) | 0.746 | 0.742 | 0.000 | 0.067 | 1.000 | 3239 / 3598 |
| main_default_seed3 (no cap) | AND | 17 | 8 (IO nop-C IO nand nand inc add IO) | 0.718 | 0.715 | 0.000 | 0.028 | 1.000 | 3239 / 3598 |
| main_default_seed3 (no cap) | ORN | 16 | 7 (IO nop-C dec nand IO swap IO) | 0.702 | 0.698 | 0.000 | 0.039 | 0.993 | 3239 / 3598 |
| main_default_seed3 (no cap) | OR | 19 | 10 (IO nop-C dec nand swap IO nand nand IO nop-C) | 0.642 | 0.639 | 0.000 | 0.028 | 0.998 | 3239 / 3598 |
| main_default_seed3 (no cap) | ANDN | 22 | 13 (IO nop-C dec nand IO nand swap IO nand add nop-C inc IO) | 0.618 | 0.614 | 0.000 | 0.027 | 0.998 | 3239 / 3598 |
| main_default_seed3 (no cap) | NOR | 20 | 11 (IO nop-C dec nand IO nand push swap pop nand IO) | 0.642 | 0.638 | 0.000 | 0.028 | 0.999 | 3239 / 3598 |
| main_high_seed1 | NOT | 20 | 7 (h-search nop-C swap nop-C nand IO if-less) | 0.802 | 0.793 | 0.000 | 0.043 | 0.980 | 560 / 3532 |
| main_high_seed1 | NAND | 23 | 10 (IO nop-C IO nand nand nop-A IO nop-C IO nand) | 0.821 | 0.812 | 0.000 | 0.016 | 0.326 | 560 / 3532 |
| main_high_seed1 | AND | 30 | 17 (IO nop-C IO nand nand nop-A swap IO nop-C nop-C IO IO IO inc if-less add if-less) | 0.723 | 0.714 | 0.000 | 0.009 | 1.000 | 560 / 3532 |
| main_high_seed1 | ORN | 22 | 9 (h-search nop-C IO nand nand IO IO if-less if-less) | 0.843 | 0.834 | 0.000 | 0.025 | 0.996 | 560 / 3532 |
| main_high_seed1 | OR | 27 | 14 (IO nop-C IO nand nand nop-A IO swap nop-C IO IO nand nand IO) | 0.802 | 0.793 | 0.000 | 0.016 | 0.991 | 560 / 3532 |
| main_high_seed1 | ANDN | 25 | 12 (h-search IO nop-C IO nand push pop inc add IO if-less if-less) | 0.814 | 0.805 | 0.000 | 0.018 | 0.987 | 560 / 3532 |
| main_high_seed1 | NOR | 30 | 17 (IO nop-C IO nand nand nop-A IO swap nop-C IO IO nand push pop inc add IO) | 0.784 | 0.775 | 0.000 | 0.018 | 0.964 | 560 / 3532 |
| main_high_seed1 | EQU | 33 | 20 (IO nop-C IO nand nand nop-A h-search add IO nop-C sub nop-C IO IO IO IO inc if-less add if-less) | 0.702 | 0.693 | 0.000 | 0.007 | 1.000 | 560 / 3532 |
| main_high_seed1 (no cap) | NOT | 20 | 7 (h-search nop-C swap nop-C nand IO if-less) | 0.521 | 0.520 | 0.000 | 0.059 | 0.950 | 3179 / 3532 |
| main_high_seed1 (no cap) | NAND | 23 | 10 (IO nop-C IO nand nand nop-A IO nop-C IO nand) | 0.504 | 0.502 | 0.000 | 0.048 | 0.487 | 3179 / 3532 |
| main_high_seed1 (no cap) | AND | 30 | 17 (IO nop-C IO nand nand nop-A swap IO nop-C nop-C IO IO IO inc if-less add if-less) | 0.346 | 0.344 | 0.000 | 0.027 | 0.992 | 3179 / 3532 |
| main_high_seed1 (no cap) | ORN | 22 | 9 (h-search nop-C IO nand nand IO IO if-less if-less) | 0.519 | 0.517 | 0.000 | 0.048 | 0.988 | 3179 / 3532 |
| main_high_seed1 (no cap) | OR | 27 | 14 (IO nop-C IO nand nand nop-A IO swap nop-C IO IO nand nand IO) | 0.443 | 0.441 | 0.000 | 0.038 | 0.972 | 3179 / 3532 |
| main_high_seed1 (no cap) | ANDN | 25 | 12 (h-search IO nop-C IO nand push pop inc add IO if-less if-less) | 0.467 | 0.465 | 0.000 | 0.039 | 0.991 | 3179 / 3532 |
| main_high_seed1 (no cap) | NOR | 30 | 17 (IO nop-C IO nand nand nop-A IO swap nop-C IO IO nand push pop inc add IO) | 0.394 | 0.392 | 0.000 | 0.035 | 0.956 | 3179 / 3532 |
| main_high_seed1 (no cap) | EQU | 33 | 20 (IO nop-C IO nand nand nop-A h-search add IO nop-C sub nop-C IO IO IO IO inc if-less add if-less) | 0.324 | 0.322 | 0.000 | 0.025 | 0.999 | 3179 / 3532 |
| main_high_seed2 | NOT | 13 | 3 (nop-C dec IO) | 0.808 | 0.800 | 0.000 | 0.141 | 1.000 | 589 / 3542 |
| main_high_seed2 | NAND | 17 | 7 (IO swap IO nand swap swap IO) | 0.491 | 0.482 | 0.000 | 0.019 | 1.000 | 589 / 3542 |
| main_high_seed2 | ORN | 13 | 3 (dec IO nand) | 0.818 | 0.810 | 0.000 | 0.088 | 1.000 | 589 / 3542 |
| main_high_seed2 | OR | 21 | 11 (IO nop-C dec sub swap IO nand nand nop-A IO nop-A) | 0.747 | 0.739 | 0.000 | 0.007 | 1.000 | 589 / 3542 |
| main_high_seed2 | ANDN | 17 | 7 (IO swap IO nand add inc IO) | 0.857 | 0.849 | 0.000 | 0.031 | 1.000 | 589 / 3542 |
| main_high_seed2 | NOR | 21 | 11 (IO nop-C dec sub swap IO nand nop-A add inc IO) | 0.779 | 0.771 | 0.000 | 0.007 | 1.000 | 589 / 3542 |
| main_high_seed2 | EQU | 30 | 20 (IO nop-C dec sub swap IO nand nand nop-A IO push nop-A IO swap IO nand swap pop nand IO) | 0.645 | 0.637 | 0.000 | 0.003 | 1.000 | 589 / 3542 |
| main_high_seed2 (no cap) | NOT | 13 | 3 (nop-C dec IO) | 0.583 | 0.581 | 0.000 | 0.158 | 1.000 | 3188 / 3542 |
| main_high_seed2 (no cap) | NAND | 17 | 7 (IO swap IO nand swap swap IO) | 0.365 | 0.363 | 0.000 | 0.037 | 0.998 | 3188 / 3542 |
| main_high_seed2 (no cap) | ORN | 13 | 3 (dec IO nand) | 0.557 | 0.555 | 0.000 | 0.103 | 0.999 | 3188 / 3542 |
| main_high_seed2 (no cap) | OR | 21 | 11 (IO nop-C dec sub swap IO nand nand nop-A IO nop-A) | 0.461 | 0.460 | 0.000 | 0.047 | 0.999 | 3188 / 3542 |
| main_high_seed2 (no cap) | ANDN | 17 | 7 (IO swap IO nand add inc IO) | 0.598 | 0.596 | 0.000 | 0.086 | 0.998 | 3188 / 3542 |
| main_high_seed2 (no cap) | NOR | 21 | 11 (IO nop-C dec sub swap IO nand nop-A add inc IO) | 0.473 | 0.471 | 0.000 | 0.051 | 0.999 | 3188 / 3542 |
| main_high_seed2 (no cap) | EQU | 30 | 20 (IO nop-C dec sub swap IO nand nand nop-A IO push nop-A IO swap IO nand swap pop nand IO) | 0.299 | 0.298 | 0.000 | 0.030 | 1.000 | 3188 / 3542 |
| main_high_seed3 | NOT | 16 | 3 (IO nand swap) | 0.843 | 0.835 | 0.000 | 0.044 | 0.913 | 521 / 3539 |
| main_high_seed3 | NAND | 13 | 0 () | 0.871 | 0.864 | 0.000 | 0.117 | 0.985 | 521 / 3539 |
| main_high_seed3 | AND | 25 | 12 (IO nop-A h-search add inc swap nop-C nand nop-A nand nop-C mov-head) | 0.766 | 0.758 | 0.000 | 0.023 | 0.977 | 521 / 3539 |
| main_high_seed3 | ORN | 16 | 3 (IO nand swap) | 0.873 | 0.866 | 0.000 | 0.081 | 0.989 | 521 / 3539 |
| main_high_seed3 | OR | 19 | 6 (nop-C nop-A if-label IO nand swap) | 0.852 | 0.845 | 0.000 | 0.017 | 0.908 | 521 / 3539 |
| main_high_seed3 | ANDN | 22 | 9 (IO nop-A add inc swap nop-C nop-A nand mov-head) | 0.773 | 0.766 | 0.000 | 0.019 | 0.978 | 521 / 3539 |
| main_high_seed3 | NOR | 28 | 15 (IO nop-A h-search swap nop-C IO IO nand nop-A nand mov-head IO swap sub IO) | 0.656 | 0.649 | 0.000 | 0.013 | 0.915 | 521 / 3539 |
| main_high_seed3 (no cap) | NOT | 16 | 3 (IO nand swap) | 0.612 | 0.611 | 0.000 | 0.083 | 0.932 | 3186 / 3539 |
| main_high_seed3 (no cap) | NAND | 13 | 0 () | 0.631 | 0.629 | 0.000 | 0.102 | 0.983 | 3186 / 3539 |
| main_high_seed3 (no cap) | AND | 25 | 12 (IO nop-A h-search add inc swap nop-C nand nop-A nand nop-C mov-head) | 0.485 | 0.484 | 0.000 | 0.054 | 0.978 | 3186 / 3539 |
| main_high_seed3 (no cap) | ORN | 16 | 3 (IO nand swap) | 0.638 | 0.637 | 0.000 | 0.103 | 0.988 | 3186 / 3539 |
| main_high_seed3 (no cap) | OR | 19 | 6 (nop-C nop-A if-label IO nand swap) | 0.581 | 0.580 | 0.000 | 0.032 | 0.920 | 3186 / 3539 |
| main_high_seed3 (no cap) | ANDN | 22 | 9 (IO nop-A add inc swap nop-C nop-A nand mov-head) | 0.491 | 0.490 | 0.000 | 0.052 | 0.978 | 3186 / 3539 |
| main_high_seed3 (no cap) | NOR | 28 | 15 (IO nop-A h-search swap nop-C IO IO nand nop-A nand mov-head IO swap sub IO) | 0.391 | 0.390 | 0.000 | 0.040 | 0.921 | 3186 / 3539 |
