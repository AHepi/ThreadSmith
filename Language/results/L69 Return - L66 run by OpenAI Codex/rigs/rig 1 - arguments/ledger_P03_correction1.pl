% Correction 1 written by OpenAI Codex under L66. Originals retained.
% Written by OpenAI Codex, under L66. P03.

% a | CLAIMED | said | sentence 1 | unjust laws exist
line(a).
holds(exist(unjust_laws)) :- line(a).

% g | GIVEN | said | sentence 4 | government is a government; response to a press not stated
line(g).
kind(government, government) :- line(g).
body(government, not_stated) :- line(g).

% r | GIVEN | said | sentence 4 | remedy is a remedy; response to a press not stated
line(r).
kind(remedy, remedy) :- line(r).
body(remedy, not_stated) :- line(r).

% w | CLAIMED | said | sentence 4 | remedy is worse than evil; qualitative comparison without a measured degree
line(w).
holds(worse_than(remedy,evil)) :- line(w).

% m | CLAIMED | filled in | sentence 5 | government MAKES remedy [worse than evil]; pronouns resolved as government/remedy
line(m).
social(m, makes, government, remedy, worse_than_evil) :- line(m).
