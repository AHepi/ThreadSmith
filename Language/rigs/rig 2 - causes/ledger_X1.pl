% ledger_X1
line(1). line(2). line(3).
body(door, light_loose) :- line(1).
did(e1, wind, push, door, toward(frame)) :- line(2).
said_moves(e1, door, toward(frame)) :- line(3).
