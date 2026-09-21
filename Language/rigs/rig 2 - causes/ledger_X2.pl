% ledger_X2
line(1). line(2). line(3). line(4).
body(he, heavy_standing) :- line(1).
body(ball, light_loose) :- line(2).
did(e1, he, kick, ball, away_from(he)) :- line(3).
said_moves(e1, ball, away_from(he)) :- line(4).
