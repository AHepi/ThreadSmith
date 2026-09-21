% Written by OpenAI Codex, under plan 45, from the other model's corpus.
% N29-A: one physical happening p1; sentence 2 is a second mention, not p2.
line(1). line(2). line(p1). line(4).
kind(ada, person) :- line(1).
doer(ada) :- line(1).
kind(box, box) :- line(2).
did(p1, ada, push, box, none) :- line(p1).
denied(second_push(ada, box)) :- line(4).

