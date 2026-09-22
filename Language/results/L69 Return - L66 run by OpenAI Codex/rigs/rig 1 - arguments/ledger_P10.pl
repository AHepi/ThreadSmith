% Written by OpenAI Codex, under L66. P10.

% a | CLAIMED | said | sentence 3 | a part claiming to be another is absurd
line(a).
holds(absurd(part_claiming_another_role)) :- line(a).

% b | CLAIMED | said | sentence 3 | mourning ordained tasks or pains is absurd
line(b).
holds(absurd(mourning_ordained_tasks)) :- line(b).

% c | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: a thing is part of the whole; reading all as the things described in this cosmic account
line(c).
holds(part_of(X,whole)) :- line(c), kind(X, thing).

% d | GIVEN | filled in | sentence 4 | Nature is the body of the whole
line(d).
holds(body_of(nature,whole)) :- line(d).

% e | GIVEN | filled in | sentence 4 | God is the soul of the whole
line(e).
holds(soul_of(god,whole)) :- line(e).

% f | CLAIMED | filled in | sentence 4 | the divine whole changes in manifestation while remaining the same whole
line(f).
holds(same_whole_changed_manifestation(divine_whole)) :- line(f).

% g | CLAIMED | filled in | sentence 5 | our bliss DEPENDS ON the conditions we blame; what we blame read as conditions
line(g).
depends(our_bliss, blamed_conditions) :- line(g).

% h | GIVEN | said | sentence 6 | heaven is a heaven; response to a press not stated
line(h).
kind(heaven, heaven) :- line(h).
body(heaven, not_stated) :- line(h).

% i | GIVEN | said | sentence 6 | blindness is a blindness; response to a press not stated
line(i).
kind(blindness, blindness) :- line(i).
body(blindness, not_stated) :- line(i).

% j | GIVEN | said | sentence 6 | weakness is a weakness; response to a press not stated
line(j).
kind(weakness, weakness) :- line(j).
body(weakness, not_stated) :- line(j).

% k | CLAIMED | filled in | sentence 6 | k: heaven BESTOWS blindness
line(k).
did(k, heaven, bestows, blindness, none) :- line(k).

% l | CLAIMED | filled in | sentence 6 | l: heaven BESTOWS weakness
line(l).
did(l, heaven, bestows, weakness, none) :- line(l).

% m | CLAIMED | filled in | sentence 9 | nature is art
line(m).
holds(is_art(nature)) :- line(m).

% n | CLAIMED | filled in | sentence 9 | chance is direction
line(n).
holds(is_direction(chance)) :- line(n).

% o | CLAIMED | filled in | sentence 9 | discord is harmony
line(o).
holds(is_harmony(discord)) :- line(o).

% p | CLAIMED | filled in | sentence 9 | partial evil is universal good
line(p).
holds(is_universal_good(partial_evil)) :- line(p).

% q | CLAIMED | filled in | sentence 9 | ALWAYS SHOWS: whatever exists is right; SHOWS chosen for the evaluative universal
line(q).
holds(right(X)) :- line(q), holds(exists(X)).
