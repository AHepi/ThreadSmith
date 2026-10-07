# S111 copying and knockouts (written by tools/s111_measure_copying_and_knockouts.py)

Ancestor: 100 instructions, makes an exact copy of itself: yes; 389 instructions executed per copy.

## Knockout test (C2): sites whose knockout stops exact self-copying

15 of 100 sites: 1 h-alloc, 2 h-search, 3 nop-C, 4 nop-A, 5 mov-head, 6 nop-C, 92 h-search, 93 h-copy, 94 if-label, 95 nop-C, 96 nop-A, 97 h-divide, 98 mov-head, 99 nop-A, 100 nop-B

The other 85 sites: knockout leaves self-copying and fitness as they were (fitness ratios: [1.0]).

## Copy fidelity (C3)

| condition | error rate per copied instruction | expected identical | identical of 1,000 sampled | offspring that copy themselves |
|---|---|---|---|---|
| low | 0.0025 | 0.703 to 0.710 | 723 | 950 |
| default | 0.0075 | 0.425 to 0.438 | 436 | 876 |
| high | 0.02 | 0.120 to 0.130 | 124 | 664 |

## Controls

K1: 0 of 10000 random programs of length 100 make an exact copy of themselves.
K2: the ancestor with its copy loop knocked out makes an exact copy of itself: no.
