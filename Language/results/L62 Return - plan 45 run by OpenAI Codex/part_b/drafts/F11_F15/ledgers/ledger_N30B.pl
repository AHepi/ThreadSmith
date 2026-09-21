% Written by OpenAI Codex, under plan 45, from the other model's corpus.
% Keep the source verb ring. It is not replaced with a shape-book verb.
line(1). line(2). line(p1).
kind(ada, person) :- line(1).
doer(ada) :- line(1).
kind(bell, bell) :- line(2).
did(p1, ada, ring, bell, none) :- line(p1).

