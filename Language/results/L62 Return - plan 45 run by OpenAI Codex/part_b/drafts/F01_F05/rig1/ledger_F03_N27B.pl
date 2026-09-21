% F03 N27-B: both movement facts are explicitly source-supplied.
line(1). line(2).
holds(moved(ada, red_box)) :- line(1).
holds(moved(bea, red_box)) :- line(2).
