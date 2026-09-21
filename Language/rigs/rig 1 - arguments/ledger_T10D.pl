% ledger_T10D.pl - T10-D (the other model's text; translated by Claude under file 36)
line(1). line(2). line(3).
holds(opened(i, window)) :- line(1).
holds(stayed_dry(letter)) :- line(2).
claim_because(3, stayed_dry(letter), opened(i, window)) :- line(3).
