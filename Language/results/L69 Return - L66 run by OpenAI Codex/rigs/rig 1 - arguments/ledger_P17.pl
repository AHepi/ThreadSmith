% Written by OpenAI Codex, under L66. P17.

% a | GIVEN | said | sentence 3 | tribes is a tribes; response to a press not stated
line(a).
kind(tribes, tribes) :- line(a).
body(tribes, not_stated) :- line(a).

% b | GIVEN | said | sentence 3 | other_tribes is a tribes; response to a press not stated
line(b).
kind(other_tribes, tribes) :- line(b).
body(other_tribes, not_stated) :- line(b).

% c | CLAIMED | said | sentence 3 | c: tribes SUPPLANTED other_tribes
line(c).
did(c, tribes, supplanted, other_tribes, none) :- line(c).
holds(supplanted(tribes,other_tribes)) :- line(c).

% d | GIVEN | said | sentence 3 | morality is an element in tribal success
line(d).
holds(element_of(morality,tribal_success)) :- line(d).
