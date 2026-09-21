% ledger_E.pl - E the ball bounced back faster than she threw it
line(1). line(2). line(3). line(4). line(5). line(6).
body(she, heavy_standing) :- line(1).
body(ball, light_loose) :- line(2).
body(wall, fixed) :- line(3).
did(e1, she, throw, ball, toward(wall)) :- line(4).
did(e2, ball, hit, wall, toward(wall)) :- line(5), result_possible(e1, ball, toward(wall)).
said_moves(e2, ball, away_from(wall)) :- line(6).
