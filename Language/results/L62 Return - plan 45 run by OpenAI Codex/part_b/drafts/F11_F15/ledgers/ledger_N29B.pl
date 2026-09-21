% Written by OpenAI Codex, under plan 45, from the other model's corpus.
% N29-B: the source expressly distinguishes p1 from p2.
line(1). line(2). line(p1). line(p2). line(5).
kind(ada, person) :- line(1).
doer(ada) :- line(1).
kind(box, box) :- line(2).
did(p1, ada, push, box, none) :- line(p1).
did(p2, ada, push, box, none) :- line(p2).
holds(distinct(p1, p2)) :- line(5).

