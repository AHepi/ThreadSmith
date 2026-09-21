% ledger_C.pl - the henhouse paragraph
line(1). line(2). line(3). line(4). line(5). line(6). line(u1). line(u2). line(u3).
holds(gone(hens)) :- line(1).
denied(has_gap(fence)) :- line(2).
denied(can_climb(fox, fence)) :- line(3).
denied(opened(gate)) :- line(4).
holds(took(fox, hens)) :- line(5).
claim_because(6, gone(hens), took(fox, hens)) :- line(6).
holds(got_inside(fox)) :- line(u1), holds(took(fox, hens)).
denied(got_inside(fox)) :- line(u2), denied(has_gap(fence)), denied(can_climb(fox, fence)), denied(opened(gate)).
produced(gone(hens)) :- line(u3), holds(took(fox, hens)).
