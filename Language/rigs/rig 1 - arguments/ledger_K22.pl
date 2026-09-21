% ledger_K22.pl - F22 remove the push and ask about the movement
line(1). line(2). line(3). line(4).
holds(pushed(box)) :- line(1).
holds(moved(box)) :- line(2).
claim_because(3, moved(box), pushed(box)) :- line(3).
produced(moved(X)) :- line(4), holds(pushed(X)).
