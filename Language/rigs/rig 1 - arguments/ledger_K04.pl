% ledger_K04.pl - F04 flag SHOWS gate shut; BECAUSE claimed (the other model's audit case, run to see what the rig really does)
line(1). line(2). line(3). line(4).
holds(raised(flag)) :- line(1).
holds(shut(gate)) :- line(2).
holds(shut(gate)) :- line(3), holds(raised(flag)).
claim_because(4, shut(gate), raised(flag)) :- line(4).
