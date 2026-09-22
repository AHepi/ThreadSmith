% Written by OpenAI Codex, under L66. P01.

% a | CLAIMED | filled in | sentence 1 | ALWAYS SHOWS: when a thing is faithfully copied across generations, selection acts on it; SHOWS is my reading of the criterion
line(a).
holds(selected(X)) :- line(a), holds(faithfully_copied(X)).

% b | CLAIMED | said | sentence 1 | gene is faithfully copied across generations
line(b).
holds(faithfully_copied(gene)) :- line(b).

% c | CLAIMED | said | sentence 2 | NOT [group is copied]
line(c).
denied(faithfully_copied(group)) :- line(c).

% d | CLAIMED | said | sentence 2 | group dissolves and reforms
line(d).
holds(dissolves_and_reforms(group)) :- line(d).

% e | CLAIMED | said | sentence 5 | selection between groups is the same process as gene-level helping spread
line(e).
holds(same_process(group_selection,gene_helping)) :- line(e).

% f | CLAIMED | said | sentence 5 | groups of relatives have clustered copies of the gene
line(f).
holds(clustered_copies(kin_groups)) :- line(f).

% g | CLAIMED | filled in | sentence 5 | line e SINCE line f; epistemic justification of a redescription, not production of sameness
line(g).
claim_since(g, same_process(group_selection,gene_helping), clustered_copies(kin_groups)) :- line(g).

% h | CLAIMED | said | sentence 6 | group adds no cause of its own
line(h).
denied(adds_own_cause(group)) :- line(h).

% i | CLAIMED | said | sentence 7 | within each group the non-helper outbreeds the helper
line(i).
holds(outbreeds(nonhelper,helper)) :- line(i).

% j | CLAIMED | said | sentence 7 | migration mixes the groups
line(j).
holds(mixes(migration,groups)) :- line(j).

% k | CLAIMED | filled in | sentence 8 | cooperation spreading NEEDS ONE OF: kin members, copies bound without defection; encoded for a generic system
line(k).
denied(cooperation_spread(X)) :- line(k), denied(kin_members(X)), denied(bound_without_defection(X)).

% l | GIVEN | said | sentence 8 | cooperation has spread in social insects
line(l).
holds(cooperation_spread(social_insects)) :- line(l).

% m | GIVEN | said | sentence 8 | cooperation has spread in the cell
line(m).
holds(cooperation_spread(cell)) :- line(m).

% n | CLAIMED | said | sentence 9 | group description shows the outcome
line(n).
holds(shows_outcome(group_description)) :- line(n).

% o | CLAIMED | said | sentence 9 | NOT [group description produced the outcome]
line(o).
denied(produces(group_description,outcome)) :- line(o).

% q | CLAIMED | said | sentence 10 | NOT [groups are selected]
line(q).
denied(selected(group)) :- line(q).

% r | CLAIMED | said | sentence 10 | genes are selected
line(r).
holds(selected(gene)) :- line(r).

% s | CLAIMED | filled in | sentence 10 | line q SINCE line h; chosen referent of therefore
line(s).
claim_since(s, selected(group), adds_own_cause(group)) :- line(s).
