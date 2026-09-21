% ledger_C4.pl - C4 he leaned on the wall and the wall stayed
line(1). line(2). line(3). line(4).
body(he, heavy_standing) :- line(1).
body(wall, fixed) :- line(2).
did(e1, he, lean_on, wall, toward(wall)) :- line(3).
said_stays(e1, wall) :- line(4).
