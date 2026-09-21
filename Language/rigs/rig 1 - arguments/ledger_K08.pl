% ledger_K08.pl - F08 the jar broke, NOT because it was dropped
line(1). line(2). line(3).
holds(dropped(jar)) :- line(1).
holds(broke(jar)) :- line(2).
denied_because(3, broke(jar), dropped(jar)) :- line(3).
