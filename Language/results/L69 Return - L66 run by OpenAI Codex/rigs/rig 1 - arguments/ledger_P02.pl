% Written by OpenAI Codex, under L66. P02.

% a | CLAIMED | filled in | sentence 2 | ALWAYS SHOWS: when men are prepared for nongoverning government, they will have nongoverning government; categorical forecast read as SHOWS
line(a).
holds(have_nongoverning_government(men)) :- line(a), holds(prepared_for_nongoverning_government(men)).

% b | CLAIMED | said | sentence 3 | government is an expedient
line(b).
holds(expedient(government)) :- line(b).

% c | GIVEN | said | sentence 4 | objections have been brought against a standing army
line(c).
holds(objections_brought(standing_army)) :- line(c).

% d | CLAIMED | filled in | sentence 5 | standing army is an instrument of standing government
line(d).
holds(instrument_of(standing_army,standing_government)) :- line(d).

% e | GIVEN | said | sentence 6 | people have chosen government as their mode
line(e).
holds(chosen_mode(people,government)) :- line(e).

% f | GIVEN | said | sentence 7 | the present Mexican war occurred
line(f).
holds(occurred(mexican_war)) :- line(f).

% g | GIVEN | filled in | sentence 7 | individuals use standing government
line(g).
holds(use(individuals,standing_government)) :- line(g).
