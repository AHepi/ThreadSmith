% Written by OpenAI Codex, under L66. P16.

% a | CLAIMED | filled in | sentence 1 | ALWAYS SHOWS: if injustice is NOT part of necessary governmental friction, government will wear out; figurative forecast with the supplied negative condition
line(a).
holds(wears_out(government)) :- line(a), denied(part_of(injustice,necessary_governmental_friction)).

% b | CLAIMED | filled in | sentence 3 | Do [make life counter-friction] SO THAT [government stops]; a proposed plan, not an achieved goal
line(b).
claim_plan(b, make_life_counterfriction, stops(government)) :- line(b).

% c | GIVEN | said | sentence 5 | State has provided ways for remedying the evil
line(c).
holds(provided(state,remedial_ways)) :- line(c).
