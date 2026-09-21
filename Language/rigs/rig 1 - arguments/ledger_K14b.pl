% ledger_K14b.pl - F14 control: an exemption aimed at an ALWAYS line
line(1). line(2). line(3).
produced(opens(L)) :- line(1), holds(pressed(L)).
holds(pressed(brass_latch)) :- line(2).
exempt(1, brass_latch) :- line(3).
