% F04 N15-B: source-supplied causal claim; no extra MAKE rule or direction is invented.
line(1). line(2). line(3).
holds(pushed(ada, box)) :- line(1).
holds(moved(box)) :- line(2).
claim_because(3, moved(box), pushed(ada, box)) :- line(3).
