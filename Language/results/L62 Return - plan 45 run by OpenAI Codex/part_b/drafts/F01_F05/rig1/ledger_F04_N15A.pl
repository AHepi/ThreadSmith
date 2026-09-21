% F04 N15-A: occurrence and denial of this proposed producer coexist.
line(1). line(2). line(3).
holds(pushed(ada, box)) :- line(1).
holds(moved(box)) :- line(2).
denied_because(3, moved(box), pushed(ada, box)) :- line(3).
