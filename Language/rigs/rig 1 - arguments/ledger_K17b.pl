% ledger_K17b.pl - F17 the door at two stages, with the stage in the fact
line(1). line(2).
holds(open(door, morning)) :- line(1).
denied(open(door, evening)) :- line(2).
