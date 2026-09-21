% ledger_K22b.pl - hostile case, added after the clean sweep: a result with TWO stated causes, only one of them changed
line(1). line(2). line(3). line(4). line(5).
holds(pushed(box)) :- line(1).
holds(tilted(floor)) :- line(2).
holds(moved(box)) :- line(3).
claim_because(4, moved(box), pushed(box)) :- line(4).
claim_because(5, moved(box), tilted(floor)) :- line(5).
