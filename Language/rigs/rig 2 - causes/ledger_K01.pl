% ledger_K01.pl - F01: Mara pushes a box; nothing says how the box answers a press
line(1). line(2). line(3).
body(mara, heavy_standing) :- line(1).
did(e1, mara, push, box, away_from(mara)) :- line(2).
said_moves(e1, box, away_from(mara)) :- line(3).
