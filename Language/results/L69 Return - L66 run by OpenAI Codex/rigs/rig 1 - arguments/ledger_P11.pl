% Written by OpenAI Codex, under L66. P11.

% a | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: a helping member pays the cost; descriptive general reading
line(a).
holds(pays_cost(X)) :- line(a), kind(X, helping_member).

% b | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: a member of a group with helping shares the benefit; group restriction made explicit
line(b).
holds(shares_benefit(X)) :- line(b), kind(X, member_of(G)), holds(helping_in(G)).

% c | CLAIMED | filled in | sentence 4 | ALWAYS SHOWS: within a group, a helping member does worse than a nonhelping member; worse retained as an opaque qualitative comparison
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

% g | GIVEN | said | sentence 8 | helping spreads
line(g).
holds(spreads(helping)) :- line(g).

% h | CLAIMED | said | sentence 8 | group structure shows the spread of helping
line(h).
holds(shows_spread(group_structure,helping)) :- line(h).

% i | CLAIMED | filled in | sentence 8 | NOT [line g BECAUSE line f]; structure read as the presence of that structure
line(i).
denied_because(i, spreads(helping), exists(group_structure)) :- line(i).

% j | CLAIMED | filled in | sentence 8 | WHAT IF MAKE line f NOT SO: THEN line g would still be so; remove read as actual absence, not merely unsaid
line(j).


% k | CLAIMED | said | sentence 9 | kin accounting is arithmetic done afterwards
line(k).
holds(afterwards_arithmetic(kin_accounting)) :- line(k).

% l | CLAIMED | said | sentence 9 | NOT [kin accounting changes what produced the outcome]
line(l).
denied(changes_producer(kin_accounting,outcome)) :- line(l).

% m | CLAIMED | filled in | sentence 10 | ALWAYS SHOWS: where cooperation has spread, groups were the things selection acted on; retrospective descriptive reading
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
