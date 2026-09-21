% ledger_K14.pl - F14 the brass latch is exempt; what it did is not stated
line(1). line(2). line(3). line(4).
produced(opens(L)) :- line(1), holds(pressed(L)), not exception(1, L).
exception(1, L) :- denied(opens(L)).
holds(pressed(brass_latch)) :- line(2).
exempt(1, brass_latch) :- line(3).
claim_because(4, opens(brass_latch), pressed(brass_latch)) :- line(4).
