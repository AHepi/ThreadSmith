% ledger_C2.pl - C2 she dropped the cup and it fell
line(1). line(2). line(3). line(4).
body(she, heavy_standing) :- line(1).
body(cup, light_loose) :- line(2).
did(e1, she, drop, cup, none) :- line(3).
said_moves(e1, cup, down) :- line(4).
