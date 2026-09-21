% ledger_K10.pl - F10 push SO THAT the box moves; text never says it moved (the other model's audit case, run to see what the rig really does)
line(1). line(2). line(3).
claim_plan(1, push(box), stays(box)) :- line(1).
changes(push(X), place(X)) :- line(2).
depends(stays(X), place(X)) :- line(3).
