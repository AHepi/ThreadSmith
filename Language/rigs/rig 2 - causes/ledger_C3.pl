% ledger_C3.pl - C3 he threw the ball at the wall and it bounced back
line(1). line(2). line(3). line(4). line(5). line(6).
body(he, heavy_standing) :- line(1).
body(ball, light_loose) :- line(2).
body(wall, fixed) :- line(3).
did(e1, he, throw, ball, toward(wall)) :- line(4).
did(e2, ball, hit, wall, toward(wall)) :- line(5), result_possible(e1, ball, toward(wall)).
said_moves(e2, ball, away_from(wall)) :- line(6).
