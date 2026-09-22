% Written by OpenAI Codex, under L66. P15.

% a | CLAIMED | filled in | sentence 1 | little minds are preoccupied with foolish consistency
line(a).
holds(preoccupied(little_minds,foolish_consistency)) :- line(a).

% b | CLAIMED | filled in | sentence 2 | ALWAYS SHOWS: a great soul has nothing to do with consistency
line(b).
denied(concerned_with(X,consistency)) :- line(b), kind(X, great_soul).

% c | CLAIMED | said | sentence 7 | pythagoras was misunderstood
line(c).
holds(misunderstood(pythagoras)) :- line(c).

% d | CLAIMED | said | sentence 7 | socrates was misunderstood
line(d).
holds(misunderstood(socrates)) :- line(d).

% e | CLAIMED | said | sentence 7 | jesus was misunderstood
line(e).
holds(misunderstood(jesus)) :- line(e).

% f | CLAIMED | said | sentence 7 | luther was misunderstood
line(f).
holds(misunderstood(luther)) :- line(f).

% g | CLAIMED | said | sentence 7 | copernicus was misunderstood
line(g).
holds(misunderstood(copernicus)) :- line(g).

% h | CLAIMED | said | sentence 7 | galileo was misunderstood
line(h).
holds(misunderstood(galileo)) :- line(h).

% i | CLAIMED | said | sentence 7 | newton was misunderstood
line(i).
holds(misunderstood(newton)) :- line(i).

% j | CLAIMED | filled in | sentence 7 | ALWAYS SHOWS: every pure and wise spirit that took flesh was misunderstood; embodied-spirit condition retained
line(j).
holds(misunderstood(X)) :- line(j), kind(X, pure_wise_embodied_spirit).

% k | CLAIMED | filled in | sentence 8 | ALWAYS SHOWS: a great person is NOT misunderstood; categorical implication chosen from the printed is not
line(k).
denied(misunderstood(X)) :- line(k), kind(X, great_person).

% l | CLAIMED | filled in | sentence 10 | his volition is constrained by the law of his being
line(l).
holds(constrained_by(volition,law_of_his_being)) :- line(l).
