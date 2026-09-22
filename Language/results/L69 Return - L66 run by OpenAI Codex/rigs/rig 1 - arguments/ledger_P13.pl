% Written by OpenAI Codex, under L66. P13.

% a | GIVEN | said | sentence 1 | atoms is a atoms; response to a press not stated
line(a).
kind(atoms, atoms) :- line(a).
body(atoms, not_stated) :- line(a).

% b | GIVEN | said | sentence 1 | weight is a own_weight; response to a press not stated
line(b).
kind(weight, own_weight) :- line(b).
body(weight, not_stated) :- line(b).

% c | GIVEN | said | sentence 1 | c: weight BEARS atoms down
line(c).
did(c, weight, bears, atoms, down) :- line(c).

% d | GIVEN | said | sentence 1 | atoms MOVES down as a result of happening c
line(d).
said_moves(c, atoms, down) :- line(d).
holds(moves(atoms,down)) :- line(d).

% e | CLAIMED | said | sentence 1 | atoms decline from their course
line(e).
holds(decline_from_course(atoms)) :- line(e).

% f | CLAIMED | filled in | sentence 2 | WHAT IF MAKE line e NOT SO: THEN line d would NOT be so; wont to swerve mapped to declining course
line(f).


% g | CLAIMED | filled in | sentence 5 | ALWAYS SHOWS: void yields; categorical ever-yielding description
line(g).
holds(yields(X)) :- line(g), kind(X, void).

% h | GIVEN | said | sentence 5 | void is a void; response to a press not stated
line(h).
kind(void, void) :- line(h).
body(void, not_stated) :- line(h).
