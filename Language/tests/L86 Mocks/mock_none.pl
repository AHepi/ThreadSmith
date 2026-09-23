% mock_none.pl - mock for plan L86
line(a). line(b). line(c). line(d). line(e).
holds(out(lamp)) :- line(a).
holds(burned_down(wick)) :- line(b).
claim_because(c, out(lamp), burned_down(wick)) :- line(c).
holds(dark(room)) :- line(d).
claim_since(e, dark(room), out(lamp)) :- line(e).
