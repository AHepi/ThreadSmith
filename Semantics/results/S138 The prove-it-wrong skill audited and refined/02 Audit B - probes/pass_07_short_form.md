# Probe pass 07: the short form, correctly written. Expected: passes.
C1. "The new price cache makes checkout pages load faster: median 310 ms against 420 ms over one week."
C2. "The cache never serves a stale price."
Source: the team's release note, "Results" paragraph.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | Rerun of the same week's traffic replay shows a median gap of less than 50 ms between cache on and cache off | survived | ran replay_compare.py on the saved week; printed "median 312 ms on, 418 ms off" | none |
| F2 | C1 | With the cache on for half the servers and off for the other half in the same week, the median gap is under 50 ms | missing | none | C1 held if no other change in that week sped pages up |
| F3 | C2 | At least one stale price is found in the 9-day log of price reads checked against the price table | reported | release note: "no stale price was seen in 9 days of logs" | none, as reported |
| F4 | C2 | A price changed on purpose during a load test is served stale at least once in 1,000 reads | missing | none | C2 held only for the price changes that happened to occur |

Short form: all 13 questions asked; missing: Q3 (F2), Q5 (F4)

Claim as it stands: on one replayed week, a median of 312 ms against 418 ms.

Next test: change 20 prices on purpose and count stale reads (F4).
