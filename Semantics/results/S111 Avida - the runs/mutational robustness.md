# S111 mutational robustness (written by tools/s111_measure_mutational_robustness.py)

Every one-instruction change of each genotype, run alone in the test processor. "viable": still makes an exact copy of itself; "neutral": viable and fitness unchanged (within one part in a million).

Ancestor: 100 instructions, 2500 one-change programs; viable 0.812, neutral 0.176, lethal 0.188, higher fitness 0.573.

| run | update | length | tasks | viable | neutral | within 1% | lethal | higher fitness |
|---|---|---|---|---|---|---|---|---|
| main_low_seed1 | 10000 | 95 | not nand orn or nor | 0.755 | 0.225 | 0.308 | 0.245 | 0.029 |
| main_low_seed1 | 30000 | 98 | not nand and orn or andn nor | 0.721 | 0.211 | 0.262 | 0.279 | 0.028 |
| main_low_seed1 | 50000 | 100 | not nand and orn or andn nor | 0.688 | 0.188 | 0.272 | 0.312 | 0.031 |
| main_low_seed2 | 10000 | 105 | not nand orn or andn nor | 0.796 | 0.157 | 0.205 | 0.204 | 0.027 |
| main_low_seed2 | 30000 | 106 | not nand orn or nor xor equ | 0.736 | 0.153 | 0.221 | 0.264 | 0.017 |
| main_low_seed2 | 50000 | 110 | not nand orn or andn nor xor equ | 0.714 | 0.139 | 0.198 | 0.286 | 0.021 |
| main_low_seed3 | 10000 | 106 | not orn or andn nor | 0.733 | 0.247 | 0.344 | 0.267 | 0.072 |
| main_low_seed3 | 30000 | 107 | not nand orn or andn nor equ | 0.727 | 0.173 | 0.221 | 0.273 | 0.016 |
| main_low_seed3 | 50000 | 108 | not nand orn or andn nor equ | 0.694 | 0.181 | 0.234 | 0.306 | 0.023 |
| main_default_seed1 | 10000 | 103 | not orn or andn nor | 0.807 | 0.251 | 0.328 | 0.193 | 0.034 |
| main_default_seed1 | 30000 | 104 | not nand orn or andn nor xor equ | 0.765 | 0.212 | 0.269 | 0.235 | 0.016 |
| main_default_seed1 | 50000 | 105 | not nand and orn or andn nor xor equ | 0.758 | 0.173 | 0.246 | 0.242 | 0.053 |
| main_default_seed2 | 10000 | 107 | not nand and orn or andn nor | 0.734 | 0.186 | 0.295 | 0.267 | 0.063 |
| main_default_seed2 | 30000 | 147 | not nand and orn or andn nor xor equ | 0.769 | 0.292 | 0.408 | 0.231 | 0.053 |
| main_default_seed2 | 50000 | 128 | not nand and orn or andn nor xor equ | 0.719 | 0.257 | 0.336 | 0.281 | 0.062 |
| main_default_seed3 | 10000 | 95 | not and orn or andn nor | 0.711 | 0.194 | 0.251 | 0.289 | 0.040 |
| main_default_seed3 | 30000 | 90 | not nand and orn or andn nor | 0.694 | 0.172 | 0.234 | 0.306 | 0.035 |
| main_default_seed3 | 50000 | 89 | not nand and orn or andn nor | 0.786 | 0.212 | 0.273 | 0.214 | 0.027 |
| main_high_seed1 | 10000 | 95 | nand orn or andn nor | 0.794 | 0.345 | 0.488 | 0.206 | 0.062 |
| main_high_seed1 | 30000 | 87 | not nand and orn or andn nor | 0.765 | 0.243 | 0.377 | 0.235 | 0.084 |
| main_high_seed1 | 50000 | 93 | not nand and orn or andn nor equ | 0.779 | 0.272 | 0.429 | 0.221 | 0.114 |
| main_high_seed2 | 10000 | 99 | not nand or andn nor | 0.799 | 0.316 | 0.481 | 0.201 | 0.103 |
| main_high_seed2 | 30000 | 77 | not orn or andn nor | 0.762 | 0.333 | 0.393 | 0.238 | 0.045 |
| main_high_seed2 | 50000 | 75 | not nand orn or andn nor equ | 0.754 | 0.301 | 0.311 | 0.246 | 0.032 |
| main_high_seed3 | 10000 | 108 | nand and or andn nor | 0.779 | 0.382 | 0.532 | 0.221 | 0.095 |
| main_high_seed3 | 30000 | 97 | not nand and orn or andn nor | 0.695 | 0.287 | 0.391 | 0.305 | 0.046 |
| main_high_seed3 | 50000 | 99 | not nand and orn or andn nor | 0.740 | 0.361 | 0.490 | 0.260 | 0.080 |

## By condition (mean, smallest to largest over the three seeds)

| condition | update | viable | neutral | within 1% | lethal | length |
|---|---|---|---|---|---|---|
| low | 10000 | 0.761 (0.733 to 0.796) | 0.210 (0.157 to 0.247) | 0.286 (0.205 to 0.344) | 0.239 (0.204 to 0.267) | 102 (95 to 106) |
| low | 30000 | 0.728 (0.721 to 0.736) | 0.179 (0.153 to 0.211) | 0.235 (0.221 to 0.262) | 0.272 (0.264 to 0.279) | 104 (98 to 107) |
| low | 50000 | 0.698 (0.688 to 0.714) | 0.169 (0.139 to 0.188) | 0.235 (0.198 to 0.272) | 0.302 (0.286 to 0.312) | 106 (100 to 110) |
| default | 10000 | 0.750 (0.711 to 0.807) | 0.210 (0.186 to 0.251) | 0.291 (0.251 to 0.328) | 0.249 (0.193 to 0.289) | 102 (95 to 107) |
| default | 30000 | 0.743 (0.694 to 0.769) | 0.226 (0.172 to 0.292) | 0.304 (0.234 to 0.408) | 0.257 (0.231 to 0.306) | 114 (90 to 147) |
| default | 50000 | 0.754 (0.719 to 0.786) | 0.214 (0.173 to 0.257) | 0.285 (0.246 to 0.336) | 0.246 (0.214 to 0.281) | 107 (89 to 128) |
| high | 10000 | 0.790 (0.779 to 0.799) | 0.348 (0.316 to 0.382) | 0.500 (0.481 to 0.532) | 0.209 (0.201 to 0.221) | 101 (95 to 108) |
| high | 30000 | 0.741 (0.695 to 0.765) | 0.288 (0.243 to 0.333) | 0.387 (0.377 to 0.393) | 0.260 (0.235 to 0.305) | 87 (77 to 97) |
| high | 50000 | 0.758 (0.740 to 0.779) | 0.312 (0.272 to 0.361) | 0.410 (0.311 to 0.490) | 0.242 (0.221 to 0.260) | 89 (75 to 99) |

## Low beside high (R2; the plan's rule: a difference only if every seed of one lies beyond every seed of the other)

- share_viable at 10000: no clear difference
- share_neutral at 10000: high above low
- share_viable_fitness_within_1_percent at 10000: high above low
- share_viable at 30000: no clear difference
- share_neutral at 30000: high above low
- share_viable_fitness_within_1_percent at 30000: high above low
- share_viable at 50000: high above low
- share_neutral at 50000: high above low
- share_viable_fitness_within_1_percent at 50000: high above low
