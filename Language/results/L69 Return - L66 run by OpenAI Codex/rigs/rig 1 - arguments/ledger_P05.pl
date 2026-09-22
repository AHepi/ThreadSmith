% Written by OpenAI Codex, under L66. P05.

% a | CLAIMED | said | sentence 3 | integrity of your own mind is sacred
line(a).
holds(sacred(own_mental_integrity)) :- line(a).

% b | CLAIMED | filled in | sentence 3 | being sacred NEEDS own mental integrity; restriction read as an only-ways line
line(b).
denied(sacred(X)) :- line(b), denied(own_mental_integrity(X)).

% c | CLAIMED | said | sentence 6 | good is a name
line(c).
holds(name(good)) :- line(c).

% d | CLAIMED | said | sentence 6 | bad is a name
line(d).
holds(name(bad)) :- line(d).

% e | CLAIMED | filled in | sentence 6 | ALWAYS SHOWS: what follows my constitution is right; definitional reading
line(e).
holds(right(X)) :- line(e), holds(follows_my_constitution(X)).

% f | CLAIMED | said | sentence 6 | right NEEDS follows my constitution
line(f).
denied(right(X)) :- line(f), denied(follows_my_constitution(X)).

% g | CLAIMED | filled in | sentence 6 | ALWAYS SHOWS: what goes against my constitution is wrong; definitional reading
line(g).
holds(wrong(X)) :- line(g), holds(against_my_constitution(X)).

% h | CLAIMED | said | sentence 6 | wrong NEEDS against my constitution
line(h).
denied(wrong(X)) :- line(h), denied(against_my_constitution(X)).

% i | GIVEN | filled in | sentence 8 | we yield to badges, names, societies and institutions
line(i).
holds(yield_to(we,social_labels_and_institutions)) :- line(i).

% j | CLAIMED | filled in | sentence 9 | ALWAYS SHOWS: a decent and well-spoken individual affects me
line(j).
holds(affects(X,speaker)) :- line(j), kind(X, decent_well_spoken_individual).

% k | CLAIMED | filled in | sentence 9 | ALWAYS SHOWS: a decent and well-spoken individual sways me
line(k).
holds(sways(X,speaker)) :- line(k), kind(X, decent_well_spoken_individual).
