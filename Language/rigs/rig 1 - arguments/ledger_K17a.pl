% ledger_K17a.pl - F17 the door at two stages, with the stage left out
line(1). line(2).
holds(open(door)) :- line(1).
denied(open(door)) :- line(2).
