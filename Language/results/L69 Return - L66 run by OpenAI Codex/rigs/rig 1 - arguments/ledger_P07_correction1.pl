% Correction 1 written by OpenAI Codex under L66. Originals retained.
% Written by OpenAI Codex, under L66. P07.

% a | CLAIMED | filled in | sentence 1 | ALWAYS SHOWS: what is copied faithfully across generations is acted on by selection; SHOWS chosen as a criterion
line(a).
holds(selected(X)) :- line(a), holds(faithfully_copied(X)).

% b | CLAIMED | said | sentence 1 | gene is faithfully copied across generations
line(b).
holds(faithfully_copied(gene)) :- line(b).

% c | CLAIMED | said | sentence 2 | NOT [group is copied]
line(c).
denied(copied(group)) :- line(c).

% d | CLAIMED | said | sentence 2 | group dissolves and reforms
line(d).
holds(dissolves_and_reforms(group)) :- line(d).

% e | CLAIMED | said | sentence 5 | selection between groups is the same process as gene-level helping spread
line(e).
holds(same_process(group_selection,gene_helping)) :- line(e).

% f | CLAIMED | said | sentence 5 | groups of relatives have clustered copies of the gene
line(f).
holds(clustered_copies(kin_groups)) :- line(f).

% g | CLAIMED | filled in | sentence 5 | line e SINCE line f; because read as support for a redescription
line(g).
claim_since(g, same_process(group_selection,gene_helping), clustered_copies(kin_groups)) :- line(g).

% h | CLAIMED | said | sentence 6 | NOT [group adds a cause of its own]
line(h).
denied(adds_own_cause(group)) :- line(h).
holds(neg(adds_own_cause(group))) :- line(h).

% i | CLAIMED | said | sentence 7 | within each group the non-helper outbreeds the helper
line(i).
holds(outbreeds(nonhelper,helper)) :- line(i).

% j | CLAIMED | said | sentence 7 | migration mixes the groups
line(j).
holds(mixes(migration,groups)) :- line(j).

% k | CLAIMED | filled in | sentence 8 | cooperation spreading NEEDS ONE OF: kin members, copies bound without defection; generic system reading
line(k).
denied(cooperation_spread(X)) :- line(k), denied(kin_members(X)), denied(bound_without_defection(X)).

% l | GIVEN | said | sentence 8 | cooperation has spread in social insects
line(l).
holds(cooperation_spread(social_insects)) :- line(l).

% m | GIVEN | said | sentence 8 | cooperation has spread in the cell
line(m).
holds(cooperation_spread(cell)) :- line(m).

% n | GIVEN | said | sentence 9 | group_description is a description; response to a press not stated
line(n).
kind(group_description, description) :- line(n).
body(group_description, not_stated) :- line(n).

% o | GIVEN | said | sentence 9 | outcome is a outcome; response to a press not stated
line(o).
kind(outcome, outcome) :- line(o).
body(outcome, not_stated) :- line(o).

% p | CLAIMED | said | sentence 9 | p: group_description PRODUCED outcome; verb kept exactly as produced
line(p).
did(p, group_description, produced, outcome, none) :- line(p).

% q | CLAIMED | said | sentence 10 | NOT [groups are selected]
line(q).
denied(selected(group)) :- line(q).
holds(neg(selected(group))) :- line(q).

% r | CLAIMED | said | sentence 10 | genes are selected
line(r).
holds(selected(gene)) :- line(r).

% s | CLAIMED | filled in | sentence 10 | line q SINCE line h; chosen reason for therefore, with explicit negative content
line(s).
claim_since(s, neg(selected(group)), neg(adds_own_cause(group))) :- line(s).
