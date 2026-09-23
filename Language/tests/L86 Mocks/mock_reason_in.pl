% mock_reason_in.pl - mock for plan L86
line(a). line(d). line(e). line(g).
holds(out(lamp)) :- line(a).
holds(dark(room)) :- line(d).
claim_since(e, dark(room), out(lamp)) :- line(e).
holds(dark(room)) :- line(g), holds(out(lamp)), holds(closed(shutters)).
