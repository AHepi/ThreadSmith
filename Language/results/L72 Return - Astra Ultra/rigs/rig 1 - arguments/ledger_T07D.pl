% Written by Astra Ultra under L72. T07-D independent translation.
% Standing and source marks are in the paired JSON; no rules added to the checker.
line(door).
kind(door, door) :- line(door).
body(door, not_stated) :- line(door).
line(open).
holds(open(door, described_moment)) :- line(open).
line(notopen).
denied(open(door, described_moment)) :- line(notopen).
