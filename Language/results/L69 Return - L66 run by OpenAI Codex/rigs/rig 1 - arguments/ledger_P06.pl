% Written by OpenAI Codex, under L66. P06.

% a | GIVEN | filled in | sentence 1 | ALWAYS SHOWS: matter is alive; quick read as alive in the image
line(a).
holds(alive(X)) :- line(a), kind(X, matter).

% b | CLAIMED | filled in | sentence 4 | the order of beings began from God
line(b).
holds(began_from(order_of_beings,god)) :- line(b).

% c | CLAIMED | filled in | sentence 5 | ALWAYS MAKES: striking any link of Nature's chain breaks Nature's chain; causal reading of the image, with strike kept
line(c).
produced(broken(natures_chain)) :- line(c), holds(struck_link(natures_chain)).
