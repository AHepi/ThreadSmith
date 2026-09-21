% ledger_B.pl - B rope and cart
line(1). line(2). line(3). line(4).
body(he, heavy_standing) :- line(1).  doer(he) :- line(1).
body(cart, light_loose) :- line(2).
did(r1, he, pull, cart, toward(he)) :- line(3).
said_moves(r1, cart, away_from(he)) :- line(4).
