% ledger_T11B.pl - T11-B (the other model's text; translated by Claude under file 36)
line(1). line(2). line(3). line(4).
holds(burning(lamp)) :- line(1).
holds(returned(visitor)) :- line(2).
claim_since(3, returned(visitor), burning(lamp)) :- line(3).
denied_because(4, returned(visitor), burning(lamp)) :- line(4).
