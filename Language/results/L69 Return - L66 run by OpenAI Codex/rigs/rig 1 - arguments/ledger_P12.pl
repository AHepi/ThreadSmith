% Written by OpenAI Codex, under L66. P12.

% a | CLAIMED | filled in | sentence 1 | ALWAYS SHOWS: under any circumstance sociability is the greatest advantage in the struggle for life; ranking retained as an opaque description
line(a).
holds(greatest_advantage(sociability,C)) :- line(a), kind(C, circumstance).

% b | CLAIMED | said | sentence 5 | language is an element of growing intelligence
line(b).
holds(element_of(language,growing_intelligence)) :- line(b).

% c | CLAIMED | said | sentence 5 | imitation is an element of growing intelligence
line(c).
holds(element_of(imitation,growing_intelligence)) :- line(c).

% d | CLAIMED | said | sentence 5 | accumulated experience is an element of growing intelligence
line(d).
holds(element_of(accumulated_experience,growing_intelligence)) :- line(d).

% e | CLAIMED | filled in | sentence 5 | ALWAYS SHOWS: an unsociable animal is deprived of language
line(e).
denied(has(X,language)) :- line(e), kind(X, unsociable_animal).

% f | CLAIMED | filled in | sentence 5 | ALWAYS SHOWS: an unsociable animal is deprived of imitation
line(f).
denied(has(X,imitation)) :- line(f), kind(X, unsociable_animal).

% g | CLAIMED | filled in | sentence 5 | ALWAYS SHOWS: an unsociable animal is deprived of accumulated experience
line(g).
denied(has(X,accumulated_experience)) :- line(g), kind(X, unsociable_animal).

% h | CLAIMED | said | sentence 6 | ants combine sociability with developed intelligence
line(h).
holds(combine_traits(ants,sociability,developed_intelligence)) :- line(h).

% i | CLAIMED | said | sentence 6 | parrots combine sociability with developed intelligence
line(i).
holds(combine_traits(parrots,sociability,developed_intelligence)) :- line(i).

% j | CLAIMED | said | sentence 6 | monkeys combine sociability with developed intelligence
line(j).
holds(combine_traits(monkeys,sociability,developed_intelligence)) :- line(j).

% k | CLAIMED | filled in | sentence 7 | ALWAYS SHOWS: the fittest are the most sociable animals; descriptive classification using the supplied ranking words
line(k).
holds(most_sociable(X)) :- line(k), kind(X, fittest_animal).

% l | CLAIMED | said | sentence 7 | sociability appears as the chief factor of evolution
line(l).
holds(appears_chief_factor(sociability,evolution)) :- line(l).

% m | CLAIMED | said | sentence 7 | sociability secures the well-being of the species
line(m).
holds(secures(sociability,species_wellbeing)) :- line(m).

% n | CLAIMED | said | sentence 7 | sociability favours the growth of intelligence
line(n).
holds(favours(sociability,intelligence_growth)) :- line(n).
