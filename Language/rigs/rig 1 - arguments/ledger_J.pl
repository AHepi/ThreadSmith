% ledger_J.pl - the owner's ball sentences, as ONE ledger holding pressing patterns and BECAUSE claims together
line(1). line(2). line(3). line(5). line(6). line(7). line(8). line(9).
body(sally, heavy_standing) :- line(1).
body(ball, light_loose) :- line(2).
body(wall, fixed) :- line(3).
did(p1, sally, throw, ball, toward(wall)) :- line(5).
said_moves(p1, sally, away_from(wall)) :- line(6).
said_moves(p1, ball, toward(wall)) :- line(7).
claim_because(8, moves(sally, away_from(wall)), happened(p1)) :- line(8).
claim_because(9, moves(ball, toward(wall)), happened(p1)) :- line(9).
