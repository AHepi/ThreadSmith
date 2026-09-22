% Written by OpenAI Codex, under L66. P18.

% a | CLAIMED | filled in | sentence 1 | ALWAYS SHOWS: a thing was NOT born from nothing before now; past stage retains ever yet
line(a).
denied(born_from_nothing_before_now(X)) :- line(a), kind(X, thing).

% b | CLAIMED | filled in | sentence 2 | fear holds dominion over mortality
line(b).
holds(holds_dominion(fear,mortality)) :- line(b).

% c | SUPPOSED in case all_from_all | filled in | sentence 4 | ALWAYS SHOWS: any kind sprang from any thing; supposed universal reading of all from all
line(c).
holds(sprang_from(K,T)) :- line(c), kind(K, thing_kind), kind(T, thing).

% d | GIVEN | filled in | sentence 7 | ALWAYS SHOWS: a created thing is produced from fixed seeds; descriptive universal
line(d).
holds(produced_from_fixed_seeds(X)) :- line(d), kind(X, created_thing).

% e | CLAIMED | filled in | sentence 7 | ALWAYS SHOWS: each birth comes from its own stuff and primal bodies; one material-origin description
line(e).
holds(originates_in_own_primal_stuff(X)) :- line(e), kind(X, birth).

% f | CLAIMED | filled in | sentence 8 | ALWAYS SHOWS: each thing has a power of its own; secret resides read as possession of an intrinsic power
line(f).
holds(has_own_power(X)) :- line(f), kind(X, thing).
