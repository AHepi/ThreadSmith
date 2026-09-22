% Written by Astra Ultra under L72. T07-B independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(nora).
kind(nora, thing) :- line(nora).
body(nora, not_stated) :- line(nora).
doer(nora) :- line(nora).
line(story).
kind(story, story) :- line(story).
body(story, not_stated) :- line(story).
line(telling).
did(telling, nora, tell, story, not_stated) :- line(telling).
holds(told(nora, story)) :- line(telling).
line(storydoor).
kind(door, door) :- line(storydoor).
body(door, not_stated) :- line(storydoor).
line(storyopen).
holds(open(door)) :- line(storyopen).
line(room).
kind(room, room) :- line(room).
body(room, not_stated) :- line(room).
line(actualdoor).
kind(door, door) :- line(actualdoor).
body(door, not_stated) :- line(actualdoor).
line(actualshut).
holds(stayed_shut(door)) :- line(actualshut).
denied(open(door)) :- line(actualshut).
