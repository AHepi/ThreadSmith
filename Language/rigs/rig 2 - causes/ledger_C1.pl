% ledger_C1.pl - C1 she pushed the cart and it rolled away
line(1). line(2). line(3). line(4).
body(she, heavy_standing) :- line(1).
body(cart, light_loose) :- line(2).
did(e1, she, push, cart, away_from(she)) :- line(3).
said_moves(e1, cart, away_from(she)) :- line(4).
