# Probe fail 15 (brittleness): the falsifier table's first column is headed ID instead of F. Expected: a clear message about the column name.
C1. "The new price cache makes checkout pages load faster: median 310 ms against 420 ms over one week."
C2. "The cache never serves a stale price."
Source: the team's release note, "Results" paragraph.

| ID | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | Rerun of the same week's traffic replay shows a median gap of less than 50 ms between cache on and cache off | survived | ran replay_compare.py on the saved week; printed "median 312 ms on, 418 ms off" | none |
| F2 | C1 | With the cache on for half the servers and off for the other half in the same week, the median gap is under 50 ms | missing | none | C1 held if no other change in that week sped pages up |
| F3 | C2 | At least one stale price is found in the 9-day log of price reads checked against the price table | reported | release note: "no stale price was seen in 9 days of logs" | none, as reported |
| F4 | C2 | A price changed on purpose during a load test is served stale at least once in 1,000 reads | missing | none | C2 held only for the price changes that happened to occur |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | missing | F2: one week only, no peak season |
| Q1 | C2 | missing | F4: only the price changes that happened |
| Q2 | all | does not apply | considered a supplied answer in the replay; the replay holds raw traffic only, nothing handed in |
| Q3 | C1 | missing | F2: a release in the same week could explain the gain |
| Q3 | C2 | missing | F4: no planted change, so absence of stale reads may be luck |
| Q4 | C1 | covered | F1: worked out, the two arms differ in the cache switch only |
| Q4 | C2 | does not apply | considered two measures agreeing by construction; there is one measure and no arms |
| Q5 | C1 | covered | F1: counted per page type from replay output |
| Q5 | C2 | missing | F4 |
| Q6 | C1 | missing | F2 |
| Q6 | C2 | covered | F3: "9 days of logs" of the same build, as reported |
| Q7 | all | covered | worked out: both claims are about outputs, load time and served price |
| Q8 | all | does not apply | considered a fitted part meeting new traffic; nothing in the cache was fitted or learned |
| Q9 | C1 | covered | F1: replay of a full week, about 2 million page loads, counted |
| Q9 | C2 | missing | F4: 9 days may hold too few price changes to expect a stale read |
| Q10 | all | missing | F2, F4: the release note does not say whether the pass mark was fixed before the week |
| Q11 | C1 | covered | F1: we ran the replay ourselves |
| Q11 | C2 | covered | F3: reported, not rerun by us |
| Q12 | all | missing | F4: a stale price would be charged to customers |
| Q13 | all | covered | F1: every page load in the week counted, none excluded |

Claim as it stands: on one week of replayed traffic, the cache cut the median checkout load from 418 ms to 312 ms. No stale price was reported in 9 days; held if a planted price change is also served fresh.

Next test: change 20 prices on purpose during a load test and count stale reads (F4).
