% ledger_K13.pl - F13 ALWAYS latch opens gate; pressed; did not open (the other model's audit case, run to see what the rig really does)
line(1). line(2). line(3).
produced(opens(gate)) :- line(1), holds(pressed(latch)).
holds(pressed(latch)) :- line(2).
denied(opens(gate)) :- line(3).
