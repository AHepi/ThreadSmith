% ledger_E.pl - the letter paragraph. "When" and "who believes what" are not in the theory; see leftover.
line(1). line(2). line(3). line(4). line(u1). line(u2). line(u3).
holds(in_study(letter)) :- line(1).
denied(entered(jon, study)) :- line(2).
holds(quoted(jon, letter)) :- line(3).
claim_because(4, knows_words(jon), told(cleaner, jon)) :- line(4).
holds(knows_words(P)) :- line(u1), holds(quoted(P, letter)).
produced(knows_words(P)) :- line(u2), holds(read(P, letter)).
produced(knows_words(P)) :- line(u2), holds(told(Q, P)), holds(knows_words(Q)).
denied(read(P, letter)) :- line(u3), holds(in_study(letter)), denied(entered(P, study)).
