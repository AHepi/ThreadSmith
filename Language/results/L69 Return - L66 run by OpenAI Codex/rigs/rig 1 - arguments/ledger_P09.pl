% Written by OpenAI Codex, under L66. P09.

% a | CLAIMED | said | sentence 1 | NOT [creation is crammed with body]
line(a).
denied(crammed_with_body(creation)) :- line(a).

% b | CLAIMED | said | sentence 1 | NOT [creation is blocked about by body]
line(b).
denied(blocked_by_body(creation)) :- line(b).

% c | CLAIMED | said | sentence 1 | void exists
line(c).
holds(exists(void)) :- line(c).

% d | CLAIMED | said | sentence 2 | void is intangible
line(d).
holds(intangible(void)) :- line(d).

% e | GIVEN | said | sentence 3 | body has the property of blocking and checking
line(e).
holds(blocking_and_checking_property(body)) :- line(e).

% f | CLAIMED | said | sentence 6 | solid objects are formed of matter mixed with void
line(f).
holds(matter_mixed_with_void(solid_objects)) :- line(f).

% g | GIVEN | said | sentence 6 | moisture is a moisture; response to a press not stated
line(g).
kind(moisture, moisture) :- line(g).
body(moisture, not_stated) :- line(g).

% h | CLAIMED | said | sentence 6 | moisture seeps
line(h).
holds(seeps(moisture)) :- line(h).

% i | CLAIMED | said | sentence 6 | drops stand out
line(i).
holds(stand_out(drops)) :- line(i).

% j | CLAIMED | said | sentence 6 | food finds a way through living frames
line(j).
holds(finds_way(food,living_frames)) :- line(j).

% k | GIVEN | said | sentence 6 | trees is a trees; response to a press not stated
line(k).
kind(trees, trees) :- line(k).
body(trees, not_stated) :- line(k).

% l | GIVEN | said | sentence 6 | fruit is a fruit; response to a press not stated
line(l).
kind(fruit, fruit) :- line(l).
body(fruit, not_stated) :- line(l).

% m | CLAIMED | said | sentence 6 | trees increase
line(m).
holds(increase(trees)) :- line(m).

% n | CLAIMED | said | sentence 6 | n: trees YIELD fruit
line(n).
did(n, trees, yield, fruit, none) :- line(n).
holds(yield(trees,fruit)) :- line(n).

% o | CLAIMED | said | sentence 6 | the trees' food is poured
line(o).
holds(poured(trees_food)) :- line(o).

% p | CLAIMED | said | sentence 6 | line m BECAUSE line o
line(p).
claim_because(p, increase(trees), poured(trees_food)) :- line(p).

% q | CLAIMED | said | sentence 6 | line n BECAUSE line o
line(q).
claim_because(q, yield(trees,fruit), poured(trees_food)) :- line(q).

% r | GIVEN | said | sentence 6 | voices is a voices; response to a press not stated
line(r).
kind(voices, voices) :- line(r).
body(voices, not_stated) :- line(r).

% s | GIVEN | said | sentence 6 | walls is a walls; response to a press not stated
line(s).
kind(walls, walls) :- line(s).
body(walls, not_stated) :- line(s).

% t | CLAIMED | said | sentence 6 | t: voices PASS walls
line(t).
did(t, voices, pass, walls, none) :- line(t).

% u | CLAIMED | said | sentence 6 | voices fly reverberant
line(u).
holds(fly_reverberant(voices)) :- line(u).

% v | CLAIMED | said | sentence 6 | frost seeps
line(v).
holds(seeps(frost)) :- line(v).

% w | CLAIMED | said | sentence 9 | body tends to load things downward; propensity to load, not motion of body itself
line(w).
tends(body, load_down(things)) :- line(w).

% x | GIVEN | said | sentence 9 | void is imponderable
line(x).
holds(imponderable(void)) :- line(x).

% y | CLAIMED | said | sentence 11 | void exists
line(y).
holds(exists(void)) :- line(y).

% z | CLAIMED | said | sentence 11 | void is invisible
line(z).
holds(invisible(void)) :- line(z).
