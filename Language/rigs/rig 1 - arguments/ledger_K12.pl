% ledger_K12.pl - F12 two habits pull opposite ways about the latch
line(1). line(2). line(3).
kind(tonight, evening) :- line(1).
holds(open(latch, O)) :- line(2), kind(O, evening), not exception(2, O).
exception(2, O) :- denied(open(latch, O)).
denied(open(latch, O)) :- line(3), kind(O, evening), not exception(3, O).
exception(3, O) :- holds(open(latch, O)).
