% Written by Astra Ultra under L72. T05-B independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(note).
kind(note, note) :- line(note).
body(note, not_stated) :- line(note).
line(ada).
kind(ada, thing) :- line(ada).
body(ada, not_stated) :- line(ada).
doer(ada) :- line(ada).
line(folding).
did(folding, ada, fold, note, not_stated) :- line(folding).
holds(folded(ada, note)) :- line(folding).
line(gate).
kind(gate, gate) :- line(gate).
body(gate, not_stated) :- line(gate).
line(shut).
holds(remained_shut(gate)) :- line(shut).
