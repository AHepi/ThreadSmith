% Written by Astra Ultra under L72. T05-D independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(note).
kind(note, note) :- line(note).
body(note, not_stated) :- line(note).
line(ada).
kind(ada, thing) :- line(ada).
body(ada, not_stated) :- line(ada).
doer(ada) :- line(ada).
line(gate).
kind(gate, gate) :- line(gate).
body(gate, not_stated) :- line(gate).
line(opening).
did(opening, ada, open, gate, not_stated) :- line(opening).
holds(opened(ada, gate)) :- line(opening).
