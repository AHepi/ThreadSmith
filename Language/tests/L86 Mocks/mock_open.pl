% mock_open.pl - mock for plan L86
line(a). line(b). line(c). line(k). line(g).
holds(out(lamp)) :- line(a).
holds(burned_down(wick)) :- line(b).
claim_because(c, out(lamp), burned_down(wick)) :- line(c).
kind(lamp, lamp) :- line(k).
produced(out(L)) :- line(g), kind(L, lamp), holds(wick_of(W, L)), holds(burned_down(W)).
