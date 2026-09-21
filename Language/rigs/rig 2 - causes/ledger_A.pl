% ledger_A.pl - the owner's ball and coin paragraph, second form. NO usual-case lines.
line(1). line(2). line(3). line(4). line(5). line(6). line(7). line(8). line(9). line(10). line(11). line(12). line(13).
body(sally, heavy_standing) :- line(1).
doer(sally) :- line(1).
body(ball, light_loose) :- line(2).
body(wall, fixed) :- line(3).
body(coin, light_loose) :- line(4).
did(p1, sally, throw, ball, toward(wall)) :- line(5).
said_moves(p1, sally, away_from(wall)) :- line(6).
did(p3, ball, hit, wall, toward(wall)) :- line(7), result_possible(p1, ball, toward(wall)).
said_moves(p3, ball, away_from(wall)) :- line(8).
touches(p4, ball, sallys_face) :- line(9), result_possible(p3, ball, away_from(wall)).
did(c1, sally, close_fist_on, coin, none) :- line(10).
did(c2, sally, open_fist_on, coin, none) :- line(11).
said_moves(c2, coin, across) :- line(12).
said_moves(c3, coin, down) :- line(13).
