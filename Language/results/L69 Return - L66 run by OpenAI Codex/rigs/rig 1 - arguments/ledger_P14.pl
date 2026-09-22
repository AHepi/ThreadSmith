% Written by OpenAI Codex, under L66. P14.

% a | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: a helping member pays the cost; generic description
line(a).
holds(pays_cost(X)) :- line(a), kind(X, helping_member).

% b | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: a member of a group with helping shares the benefit; explicit group restriction
line(b).
holds(shares_benefit(X)) :- line(b), kind(X, member_of(G)), holds(helping_in(G)).

% c | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: within a group a helping member does worse than a nonhelping member; qualitative comparison only
line(c).
holds(does_worse(X,Y)) :- line(c), kind(X, helping_member_of(G)), kind(Y, nonhelping_member_of(G)).

% d | CLAIMED | said | sentence 5 | selection within groups works against helping
line(d).
holds(works_against(selection_within_groups,helping)) :- line(d).

% e | CLAIMED | said | sentence 5 | selection between groups works for helping
line(e).
holds(works_for(selection_between_groups,helping)) :- line(e).

% f | GIVEN | said | sentence 8 | group structure exists
line(f).
holds(exists(group_structure)) :- line(f).

% g | CLAIMED | said | sentence 8 | helping spreads
line(g).
holds(spreads(helping)) :- line(g).

% h | CLAIMED | filled in | sentence 8 | line g BECAUSE line f; structure names its presence as the cause
line(h).
claim_because(h, spreads(helping), exists(group_structure)) :- line(h).

% i | CLAIMED | said | sentence 8 | NOT [this group-selection account is merely a way of speaking]
line(i).
denied(merely_way_of_speaking(group_selection_account)) :- line(i).

% j | CLAIMED | filled in | sentence 8 | WHAT IF MAKE line f NOT SO: THEN line g would NOT be so; remove read as actual absence
line(j).


% k | CLAIMED | said | sentence 9 | kin accounting is arithmetic done afterwards
line(k).
holds(afterwards_arithmetic(kin_accounting)) :- line(k).

% l | CLAIMED | said | sentence 9 | NOT [kin accounting changes what produced the outcome]
line(l).
denied(changes_producer(kin_accounting,outcome)) :- line(l).

% m | CLAIMED | filled in | sentence 10 | ALWAYS SHOWS: where cooperation has spread, groups were what selection acted on; retrospective generalisation
line(m).
holds(groups_selected(X)) :- line(m), holds(cooperation_spread(X)).

% n | GIVEN | said | sentence 10 | cooperation has spread in social_insects
line(n).
holds(cooperation_spread(social_insects)) :- line(n).

% o | GIVEN | said | sentence 10 | cooperation has spread in cell
line(o).
holds(cooperation_spread(cell)) :- line(o).

% p | GIVEN | said | sentence 10 | cooperation has spread in human_tribe
line(p).
holds(cooperation_spread(human_tribe)) :- line(p).
