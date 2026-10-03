# S109 Part B round 1 - the whole suite per variant

Each run: `tools/sonnet_harness/run_claims.py` on the section's copy with `S109B_VARIANT` (and its reading) set, scale 4, time cap 45 s, compared with `formal claims, after round 4.json` (key after_round4). Moved = claims whose status or a part's status differs from the record.

| section | variant | exit | time | counts (of 142) | claims that move | note |
|---|---|---|---|---|---|---|
| B1 | PB1.1 | 0 | 490 s | H 133, CEX 2, NT 7 | none |  |
| B1 | PB1.2-strict | 0 | 576 s | H 118, CEX 17, NT 7 | FC101 H→CEX; FC22 H→CEX; FC23 parts: (c) area 2: restating lookups / (d) area 2: the slot quantifier (A2-02; R3-Q1, a; FC23.new1 H→CEX; FC23.new2 H→CEX; FC23.new3 H→CEX; FC23.new5 H→CEX; FC25.new2 H→CEX; FC26 H→CEX; FC27.new1 H→CEX; FC30.new1 H→CEX; FC34 parts: wide reading: a candidate meeting (E) on both; FC42.new1 H→CEX; FC62 H→CEX; FC63 parts: (c-ii) the Leibniz candidate, sum restricted to ; FC72.new2 H→CEX; FC90.new1 H→CEX; FC99 H→CEX |  |
| B1 | PB1.3 | 0 | 483 s | H 133, CEX 2, NT 7 | none |  |
| B1 | PB1.4 | 0 | 482 s | H 132, CEX 3, NT 7 | FC05 parts: (ii) reading (ii), no longer a reading of L119; FC103.new1 H→CEX |  |
| B1 | PB1.6 | 0 | 482 s | H 132, CEX 3, NT 7 | FC01 H→CEX |  |
| B1 | PB1.7 | 0 | 504 s | H 132, CEX 3, NT 7 | FC25.new2 H→CEX |  |
| B1 | PB1.8 | 0 | 505 s | H 132, CEX 3, NT 7 | FC05 H→CEX |  |
| B1 | PB1.9 | 0 | 510 s | H 131, CEX 4, NT 7 | FC04 parts: (b) a finer contract can separate; FC05 H→CEX; FC16 H→CEX |  |
| B2 | PB2.1 | 0 | 496 s | H 131, CEX 4, NT 7 | FC104.new1 H→CEX; FC67 H→CEX |  |
| B2 | PB2.2 | 0 | 498 s | H 131, CEX 4, NT 7 | FC27.new1 H→CEX; FC77 H→CEX |  |
| B2 | PB2.3 | 0 | 501 s | H 133, CEX 2, NT 7 | FC42.new1 parts: (d) the other choice: δ_v quantified; FC80.new1 parts: (a) W6: fidelity on H is required, not all the e |  |
| B2 | PB2.4 | 0 | 488 s | H 130, CEX 5, NT 7 | FC109 H→CEX; FC21 H→CEX; FC96 H→CEX |  |
| B2 | PB2.5-bg-input | 0 | 702 s | H 133, CEX 2, NT 7 | none |  |
| B2 | PB2.5-bg | 0 | 495 s | H 131, CEX 4, NT 7 | FC23.new1 H→CEX; FC62 H→CEX |  |
| B2 | PB2.6 | 0 | 502 s | H 133, CEX 2, NT 7 | none |  |
| B2 | PB2.7 | 0 | 512 s | H 127, CEX 8, NT 7 | FC23 parts: (c) area 2: restating lookups / (e) S106: a lookup E_lk meets (E); FC23.new1 H→CEX; FC23.new2 H→CEX; FC23.new5 H→CEX; FC25.new2 H→CEX; FC27.new1 H→CEX; FC72.new2 H→CEX |  |
| B3 | PB3.1 | 0 | 489 s | H 132, CEX 3, NT 7 | FC30.new1 H→CEX |  |
| B3 | PB3.2 | 0 | 484 s | H 132, CEX 3, NT 7 | FC98 H→CEX |  |
| B3 | PB3.3 | 0 | 485 s | H 130, CEX 5, NT 7 | FC102.new1 H→CEX; FC12.new1 parts: round 2's D12.1 (no cod t exclusion), tags; FC12.new2 H→CEX; FC30.new1 H→CEX; FC83 parts: U and K with Build read as Held (D13.3 as it now / without I161 (the review's R1) |  |
| B3 | PB3.4 | 0 | 477 s | H 126, CEX 8, NT 8 | FC12.new1 H→CEX; FC12.new2 H→CEX; FC30.new1 H→CEX; FC83 H→CEX; FC84.new1 H→NT; FC98 H→CEX; FC98.new1 H→CEX | error: ['FC84.new1'] |
| B3 | PB3.5 | 0 | 499 s | H 133, CEX 2, NT 7 | none |  |
| B3 | PB3.6 | 0 | 497 s | H 132, CEX 3, NT 7 | FC30.new1 H→CEX |  |
| B3 | PB3.7 | 0 | 492 s | H 133, CEX 2, NT 7 | none |  |
| B3 | none | 0 | 491 s | H 133, CEX 2, NT 7 | none |  |
| B4 | PB4.1 | 0 | 494 s | H 130, CEX 5, NT 7 | FC56 H→CEX; FC72 H→CEX; FC72.new1 H→CEX |  |
| B4 | PB4.2 | 0 | 496 s | H 132, CEX 3, NT 7 | FC56 H→CEX |  |
| B4 | PB4.4p-all | 0 | 503 s | H 126, CEX 9, NT 7 | FC23.new2 H→CEX; FC30.new1 H→CEX; FC47.new1 H→CEX; FC56 H→CEX; FC72 H→CEX; FC72.new1 H→CEX; FC72.new2 H→CEX |  |
| B4 | PB4.4p-no-records | 0 | 505 s | H 126, CEX 9, NT 7 | FC23.new2 H→CEX; FC30.new1 H→CEX; FC47.new1 H→CEX; FC56 H→CEX; FC72 H→CEX; FC72.new1 H→CEX; FC72.new2 H→CEX |  |
| B4 | PB4.5 | 0 | 521 s | H 132, CEX 3, NT 7 | FC74 parts: a criticism without bearing; FC76 H→CEX |  |
| B4 | PB4.6 | 0 | 512 s | H 133, CEX 2, NT 7 | none |  |
| B4 | PB4.7 | 0 | 510 s | H 133, CEX 2, NT 7 | none |  |
| B4 | PB4.8 | 0 | 509 s | H 131, CEX 4, NT 7 | FC47.new1 H→CEX; FC72.new2 H→CEX |  |
