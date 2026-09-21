% ledger_K08b.pl - F08 the same, with a line that makes dropping produce breaking
line(1). line(2). line(3). line(4).
holds(dropped(jar)) :- line(1).
holds(broke(jar)) :- line(2).
denied_because(3, broke(jar), dropped(jar)) :- line(3).
produced(broke(X)) :- line(4), holds(dropped(X)).
