% ledger_F.pl - the owner's ball and coin paragraph
line(1). line(2). line(3). line(4). line(5). line(6). line(7). line(8). line(9). line(10). line(11). line(12). line(13). line(14). line(15).
line(k1). line(u1). line(u2). line(u3).
holds(threw(sally, ball, wall)) :- line(1).
holds(moved(sally, backwards)) :- line(2).
claim_because(3, moved(sally, backwards), threw(sally, ball, wall)) :- line(3).
produced(moved(P, backwards)) :- line(4), holds(threw(P, ball, wall)).
holds(bounced(ball, wall)) :- line(5).
holds(hit(ball, sallys_face)) :- line(6).
claim_because(7, hit(ball, sallys_face), threw(sally, ball, wall)) :- line(7).
produced(hit(ball, sallys_face)) :- line(8), holds(threw(sally, ball, wall)), holds(bounced(ball, wall)).
holds(held(sally, coin)) :- line(9).
holds(closed_fist(sally)) :- line(10).
holds(turned_hand_down(sally)) :- line(11).
holds(opened_fist(sally)) :- line(12).
holds(moved(coin, sideways)) :- line(13).
holds(landed(coin, ground_below)) :- line(14).
claim_like(15, ball_event, coin_event) :- line(15).
kind(ball, light_thing) :- line(k1).
% usual case: throwing a light thing does not move the thrower
denied(moved(P, backwards)) :- line(u1), holds(threw(P, T, wall)), kind(T, light_thing), not exception(u1, P).
exception(u1, P) :- holds(moved(P, backwards)).
% usual case: opening a fist that faces down lets go of what is in it
holds(let_go(sally, coin)) :- line(u3), holds(held(sally, coin)), holds(turned_hand_down(sally)), holds(opened_fist(sally)).
% usual case: a thing let go of falls straight down and does not move sideways
denied(moved(T, sideways)) :- line(u2), holds(let_go(sally, T)), not exception(u2, T).
exception(u2, T) :- holds(moved(T, sideways)).
