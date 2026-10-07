# 02 Models — does a rescue ratchet? Pres before and after a correction, computed

*Working file, 24 September 2026. Not frozen. Nothing in the repository was changed. Scripts: `ratchet/models/m1_gardener.py`, `m2_seasons.py`, `cx_counterexamples.py` (Python 3.11, standard library only, run in a few seconds). Their full outputs are inlined in the appendix, verbatim. Read for this: file 11 Parts II, III, V, VI (F11:L95–315); file 00 "Support families" to "Hard-to-vary and reach" (F00:L248–385) and L1300; draft 3 Part VI (D3:L295–313); the error-correction analysis of 24 September (sections 0–4, Appendix A10–A11, Part C); N1, N2 of the N-case book; D3-T; Deutsch ch. 1, pp.21–28, by page marker. The Pinker folder was not opened.*

**Tags.** [COMPUTED] = an exact output of the scripts on the stated finite model. [PROVED] = a short general argument, given in section 6. [INFERENCE] = a reading, which could be wrong.

---

## 0. The owner's position, checked

The position: a record of rescues is redundant, because a correction makes the mistake impossible to refit, and a bad rescue shows up as easier to vary by the measure that defines a good explanation.

1. **"A correction adds the failed case to the jobs, so any version that brings the mistake back fails."**
   - **True only at the failed pair itself.** [COMPUTED, PROVED] No version of any family that does the failed case repeats the old answer there. Once the old explanation is embedded, Pres also shrinks strictly: the old explanation is the witness. This holds in every family and model tried.
   - **False for the mistake as a whole.** [COMPUTED] E0's mistake covers four pairs (every sunny year with the early variety), not one. In a family rich enough to contain the "hybrid" version, Pres(J_after) holds versions that are right on every job and wrong exactly where E0 was wrong. Example: *sun = id, the early variety wins only in a wet windy spring*. Under a variety component that reads V, W and Wi, 56 of the 64 surviving versions do this. Adding the seed trial still leaves 24. Only when all four pairs are jobs does the count reach 0.
   - **The mistake is kept out only on the world's contract.** [COMPUTED] There it is kept out as a fact that nobody can see before a separating test. This is the analysis's "blocked as a fact, unmarked in the record", reached again.
2. **"A bad rescue registers as easier to vary."**
   - **False in general.** [COMPUTED, PROVED] On the recorded summers, wet, windy and early occur together. Swapping W and V maps the record onto itself, so any family that treats the two rescues alike gives the bad rescue exactly the Pres of the good one: 1:1, 4:4, 6:6, 64:64.
   - Under the port-swap family, "windy would fit as well" is true of the **good** rescue too: Pres = {wet, windy, early}.
   - The do-nothing patch has Pres = 1 in its natural single-exception family, the same as the good rescue.
   - The amended myth *shrinks* Pres, from 6 to 2. This is the same shape as the tilt's own honest correction (4 to 2), and after the amendment the myth is as small as the tilt (2 against 2).
   - The bad rescue registers as easier only when its part is given more ports than the good part. That is a choice of family, and the grid in CX3 flips both ways.
   - **The narrowing** registers only against the wider contract it left: 0 → 1. Its Pres equals the pre-failure Pres exactly, so without the recorded earlier index it looks like an honest narrow claim made from the start.
3. **The file-00 limit.** The embedding makes one comparison valid: the *later* explanation's family with more jobs, (H). There strictness is guaranteed. It does not yield the owner's comparisons:
   - Pres before and Pres after are **disjoint** in every rescue that added a part (all of M1's, and the myth's). They are never nested.
   - On fixed jobs, every added component makes Pres **weakly larger**, whether the rescue is good or bad.
   - It cannot separate a good from a bad rescue on the same record.
   - Nothing in it uses the fact that the correction is the author's *own*. It works for any extension. Organizations that are not extensions (tilt against myth) have no embedding unless an assembly rule is invented.

So, on these models, the Pres measure does not do the work that a record of rescues does. What separates the good rescue from the bad one is (A) on pairs that separate them: the world's contract, or a background job such as the seed trial that exercises the added part independently. That is a fact about answers, not a count of versions. [INFERENCE: whether this makes a record *necessary* is section 7.]

---

## 1. What was modelled

**The theory's terms, made finite.**

| Term | In the models |
|---|---|
| Target D | M1: a garden with 16 settings (edit–boundary pairs): W wet/dry, Wi windy/calm, V the neighbour's variety late/early, Sun: the south wall sunny or shaded (an admitted intervention). M2: 6 pairs, place N/E/S × half-year H1/H2. |
| Truth | M1: north first iff the variety is early; otherwise the sunnier bed first. M2: the season is sign(latitude) × sign(half); the equator has none. |
| Candidate (organization) | A list of components, each a function on stated ports. M1: `sun` (the sunnier bed ripens first) plus *override* parts (if any fires, north first). M2 tilt: tilt t, latitude factor g, heating law h. M2 myth: schedule, grief u, and in the amended myth a destination d for the banished warmth. |
| Contract C / jobs | A job is one pair. "Account(E_v, job)" is read as **(A) at that pair**. (F1) is not modelled. Non-circular dependence (draft-3 S3 reading) is checked in M1 (i). |
| Variation family | The product of the stated menus of the organization's components. Each menu is written out in the script, and each result names its family. |
| Pres(F) | The versions in the family that answer every job in F as the target does. |

**M1 jobs.** Five good summers (dry, calm, late variety, sunny wall; one pair) plus one shading test make J_before. The sixth summer f* (wet, windy, early variety) failed. J_after = J_before + f*. C_full = all 16 settings. BG_seed is a seed trial (early variety in a dry calm spring gives north first). BG_rain is another wet spring with the late variety (south first). The narrowing is read as "my explanation only covered the summers seen before the failure", so C_narrow = J_before. A bare variant drops the shading test.

**M1 candidates.**
- E0: the sunnier bed first.
- E_good: E0 + variety override "early → north".
- E_bad: E0 + rain override "wet → north".
- E_patch: E0 + an exception that fires at f* only.
- E_narrow: E0 on C_narrow.

**M2 jobs.**
- J_greek: N in both halves.
- J_sailor: J_greek + the sailor's two southern pairs.
- J_world: all six pairs.
- The tilt also takes two component jobs outside the seasons question: BG_heat (a plate facing a lamp warms) and BG_elev (the Greek noon sun is high in H1). The myth takes none, since nothing but the seasons bears on Demeter.
- A hypothetical "in-phase" report tests Deutsch's "nowhere to go".

**M2 candidates.**
- T*: tilt, sphere, direct heating.
- The escape-clause tilt ("elsewhere the same", Deutsch pp.27–28), which is flat geometry on these places.
- M0: the original myth.
- M1: the amended myth, "she sends the warmth south and calls it home".
- The myth narrowed to Greece.

---

## 2. M1, the gardener: results per rescue

Base stated family: `sun` = all 4 maps; the added part = all predicates on its own ports (variety reads V; rain reads W, the owner's "wet"; a second run lets rain read W and Wi); the exception = fires at one setting, or off. Embedding U = sun × var[V] × rain[W] × exc[single], |U| = 1088. Vers(E) = the points of U whose parts absent from E are off. [COMPUTED]

| Rescue | (i) (A) on its contract; (A) on C_full | (ii) \|Pres\| before (E0, J_before) → after (own family, J_after) | E0 in Pres after? | Surviving versions repeating E0's error elsewhere | (iii) (H) in U: Pres_E1(J_after) vs Pres_E1(J_before) | Pres_E0(J_before) vs Pres_E1(J_before) | Pres_E1(J_after) vs Pres_E0(J_before) | (iv) enlarges? |
|---|---|---|---|---|---|---|---|---|
| E_good (early → N), stated on C_full | yes; yes | 1 of 4 → 1 of 16 | no | 0 (but 56 of 64 when var reads V,W,Wi: CX1) | 2 → 1, strict | strictly inside (1 ⊊ 2) | disjoint | no (1 = 1) |
| E_bad (wet → N), rain reads W | yes on J_after; **no** on C_full (4 pairs) | 1 → 1 of 16 | no | 1 (itself) | 2 → 1, strict | strictly inside | disjoint | **no** (equal to E_good) |
| E_bad, rain reads W and Wi | yes on J_after; no | 1 → 4 of 64 | no | 4 | 8 → 4, strict | strictly inside | disjoint | yes (+3), only by the wider menu |
| E_patch, single-exception family | yes on J_after; no (3 pairs) | 1 → 1 of 68 | no | 1 (itself) | 17 → 1, strict | strictly inside | disjoint | **no** |
| E_patch, any-predicate family (4 ports) | yes on J_after; no | 1 → 24576 of 262144 | — | — | — | — | — | yes, only by the menu |
| E_narrow = E0 on C_narrow | yes, and non-circular (the shading test is the witness); **bare** records only: (A) yes, non-circular **no** | Pres(C_narrow) = Pres(J_before) = 1; Pres_E0(J_after) = 0 | is E0 | all 4 of E0's errors lie outside C_narrow | — | — | — | vs the failed contract yes (0 → 1); vs the pre-failure claim **equal** |

In the fully common family (every part of U free), Pres depends on the jobs alone:
- |Pres(J_before)| = 68, |Pres(J_after)| = 52, |Pres(J_after + BG_seed)| = 35, |Pres(C_full)| = 13.
- E_good, E_bad and E_patch are all members of Pres(J_after).
- Only E_good survives BG_seed or C_full.
- The 13 on C_full have one answer profile, inflated by idle exceptions (CX4).

For comparison, option (b) of the 24 September analysis. [COMPUTED]
- **Marked** (no consequence beyond the failed pair): E_patch (on any contract), E_narrow, and E_good and E_bad when their contract is confined to the record J_after.
- **Not marked:** E_good and E_bad on C_full (3 consequences each).

## 3. M2, the seasons: results per rescue

| Candidate / rescue | (i) (A): J_greek / J_sailor / J_world | (ii) \|Pres\| before → after | Old version in Pres after? | Surviving versions keeping the old error | (iii) (H) | (iv) enlarges? |
|---|---|---|---|---|---|---|
| Myth amended, law family (d ∈ {none, S, E}) | yes / yes / **no** (equator) | own family 2 of 36 → 2 of 108. Embedded: Pres_M1(J_greek) = 6 → Pres_M1(J_sailor) = 2 | no (d = none excluded) | 2 of 2 keep M0's error at the equator | 6 → 2, strict. Pres_M1(J_sailor) vs Pres_M0(J_greek): disjoint | **no**: after = before (2 = 2), and it shrinks by 4 inside its family, as a correction does |
| Myth amended, table family (grief reads state and place) | same | 2 → 18 of 2916 | — | — | — | yes (+16), only by the menu |
| Myth narrowed to Greece (after the report) | yes on J_greek | Pres = 2, **equal** to before the report; vs J_sailor 0 → 2 | — | — | — | only against the wider contract |
| Tilt's own correction, escape → sphere (same organization: file 00 met), law menus | T*: yes / yes / yes; escape version fails the S pairs | 4 → 2 (T1); 2 → 1 (with BG) | no | 0 (law menus); 2 of 6 (table menus) | strict | no |

What Pres(J_greek) leaves open at the unseen southern pair S,H1, *before* the report. [COMPUTED]

| Family | Answers at S,H1 across Pres | In-phase report: \|Pres\| |
|---|---|---|
| Tilt, law menus (sphere or flat/escape) | summer, winter | 2 |
| Tilt, law menus + BG_heat, BG_elev | summer, winter | 1 |
| Tilt, one law everywhere (sphere only) + BG | winter only (right) | **0: nowhere to go** |
| Tilt, table menus + BG | all three | 6 |
| Myth, own organization (d = none) | summer only (wrong) | 2 |
| Myth, embedded (d free) | summer, winter | 4 |

On the sailor's jobs, the amended myth and the tilt are the same size (2 and 2 under law menus). Each Pres is one relabelling pair: myth (Persephone away in H1, her absence brings summer); tilt (t−1, inverse heating). BG_heat removes the tilt's relabelling. Nothing removes the myth's.

---

## 4. The embedding (file 00's limit)

**What goes wrong naively.** [COMPUTED] The families before and after have different organizations:
- **Subset tests are ill-typed.** A version before is (sun); after it is (sun, override). As sets, Pres after ∩ Pres before is empty for every rescue, so a naive program says "not inside" for the good rescue too.
- **Answer profiles** are the only common currency. Every rescue changes the answer at f*, so "profiles after ⊆ profiles before" is False for all of them. On the old jobs, every surviving profile is the truth, so the sets are trivially equal.
- **Counts** say good = bad = patch = narrow = before (all 1).
- **Fractions** make the do-nothing patch the hardest to vary (1/68 against 1/16). They also make the amended myth *harder* to vary than the original (2/108 against 2/36).

**The embedding.** Take the later organization and put "off" (or a constant) in the added part's menu. The old explanation is then the new one with the part switched off. Redoing (ii)–(iv) inside it gives the following. [COMPUTED; PROVED in section 6]

- **Valid and useful.** (H) compares the later family on J_before and on J_after. The shrink is always **strict**: the embedded old explanation did J_before and fails f*. It is the witness file 00 said might be missing. This is the owner's point (1), exactly at the failed pair.
- **Not the owner's (iii).** On fixed jobs, Pres_E0(F) ⊆ Pres_E1(F) for every F, because Vers(E0) ⊆ Vers(E1). Adding a part never makes the explanation harder to vary on the old jobs. It was strictly easier in every rescue here (1 → 2 for good and bad alike; 1 → 17 for the patch; 2 → 6 for the myth).
- **Not a before/after order.** Pres_E1(J_after) and Pres_E0(J_before) were **disjoint** in every rescue that added a part (all of M1's, and the myth's). The only comparison left is counts, and counts depend on menus (CX3).
- **Not good against bad.** In the fully common family, Pres depends on the jobs alone. Good, bad and patch rescues are all members of Pres(J_after). The only thing that tells them apart is membership of Pres on a job set that separates them, and that is (A).
- **Not specific to one's own correction.** The construction needs only that the later organization *extends* the earlier one. E_good and E_bad are handled identically, and so would be a rival's extension. Relaxing the limit "for one's own correction" therefore does no formal work. What makes a correction one's own is its history. [INFERENCE] For organizations that are not extensions (tilt against myth), there is no embedding unless an assembly rule is invented, which would be the cross-theory ranking file 00 refused.
- **The added part's menu is a free choice**, and it decides (ii)–(iv): see CX1 and CX3.

**Verdict.** The embedding makes (H) meaningful between an explanation and its extension, with guaranteed strictness. That delivers the owner's point (1) at the failed pair and nothing more. It does not turn hard-to-vary into a ranking of people. It also does not rank the correction above the original, or the good rescue above the bad one.

---

## 5. Counterexamples found

**CX1: a good correction that leaves the old mistake refittable.** [COMPUTED]
- E_good passes (A) on J_after (which holds f*) and on C_full.
- Let the variety part read V, W and Wi. That is natural: "does the early variety win in every spring?" is exactly what is unknown.
- Pres(J_after) then has 64 versions, and **56** of them give E0's wrong answer at some other early-variety sunny pair. Example: (sun=id, var = early∧wet∧windy) is wrong as E0 at 3 pairs.
- With the seed trial it is still 24. With every pair of M(E0) as a job it is 0, and on C_full it is 0.
- With V+W it is 2 of 4, e.g. "the early variety wins only in a wet spring".
- The owner's claim holds only under the poorest menu (var reads V: 0). There the family itself does the work.
- Two more instances:
  - M2: both surviving amended myths keep the original myth's error at the equator.
  - The tilt under table menus: 2 of 6 survivors repeat the escape version's error.

**CX2: bad rescues that do not enlarge Pres.** [COMPUTED, PROVED]
- (a) **The symmetry of the record.** Swapping W and V maps J_after onto itself and keeps its answers. For every family pair built alike, Pres_bad is the swap of Pres_good:
  - var[V] vs rain[W]: 1:1;
  - V+Wi vs W+Wi: 4:4;
  - V+Sun vs W+Sun: 6:6;
  - V+W+Wi vs W+V+Wi: 64:64.
  - The port-swap family gives Pres(J_after) = {wet, windy, early}: "windy would fit as well" is equally true of the good rescue.
  - The world breaks the symmetry (on C_full, Pres_bad = 0), and so does BG_seed (only "early" survives). Both do it through (A).
- (b) **The do-nothing patch**, single-exception family: |Pres| = 1, equal to the good rescue and to E0 before.
- (c) **The amended myth**, law family: Pres 6 → 2 in its family. After the amendment it equals the original's pre-report 2 and the tilt's 2. By the measure, the bad rescue looks like a correction.
- (d) **The narrowing**: Pres(C_narrow) = Pres(J_before). There is no enlargement relative to the claim before the failure.

**CX3: results that flip with the family.** [COMPUTED]
- **Grid of |Pres(J_after)|, good : bad.** The three swap-symmetric pairs are equal (1:1, 4:4, 6:6). Otherwise either direction appears: "bad easier" (e.g. 1:96) and "good easier" (e.g. 64:1).
- **Patch:** 1 (single exception) against 24576 (any predicate).
- **Amended myth:** 2 (law) against 18 (table).
- **Original myth before the report:** unanimous at the south in its own family ("hard to vary", and wrong), spread in the embedded family.
  - Deutsch's "slight variants … it has to go elsewhere – into the southern hemisphere" (D p.21) is a verdict in the *embedded* family.
- **Tilt:** unanimous at the south, with "nowhere to go" (D p.25), **only** in the family that admits one law everywhere.
  - With the escape clause admitted, the tilt with every background job still fits an in-phase report.
  - Deutsch excludes that variant because it is "no longer an explanation of seasons, just a (purported) rule of thumb" (D p.28). That is a restriction of the family, not a Pres count.
- **Leave-the-report-out:** it flags the tilt exactly as it flags the myth, unless the family is sphere-only.
- This matches Derivation 3: "what H leaves open about t is what T leaves open" (F11:L197). The family plays the part of the population.

**CX4: (H) non-strict, and idle parts in the count.** [COMPUTED]
- Adding a genuinely new job (BG_rain) to E_good's jobs excludes nothing (1 = 1).
- In the fully common family, Pres(C_full) has 13 members and one answer profile. Twelve of them carry an idle exception that fires where the answer is north anyway.

**CX5: history-free detection fails.** [COMPUTED]
- A leave-one-out test ("is the answer at x fixed by the other jobs?") does **not** flag the amended myth: each southern pair pins d for the other.
- Leaving out the sailor's report as a block does flag it, but that needs to know which jobs arrived together, which is history.
- In the gardener, leave-one-out flags good and bad alike on J_after (both open at f*). With BG_seed it separates them only because E_bad already fails (A).

---

## 6. Four small facts behind the numbers [PROVED]

1. **Failed pair.** If f* ∈ F and E0 answered f* wrongly, no v ∈ Pres(F) repeats E0's answer at f*. If E0 ∈ V and E0 does F_old, then Pres(F_old ∪ {f*}) ⊊ Pres(F_old). *Proof:* Pres requires the right answer at f*, and E0 is in the second set but not the first. ∎
2. **Extension.** If Vers(E0) ⊆ Vers(E1) inside a common U, then Pres_E0(F) = Pres_U(F) ∩ Vers(E0) ⊆ Pres_U(F) ∩ Vers(E1) = Pres_E1(F) for every F. ∎ So on fixed jobs, adding a part can only enlarge Pres.
3. **Hybrid.** Suppose V contains h, which answers as E1 on F and as E0 on M(E0) \ F. Then h ∈ Pres(F), and h repeats E0's mistake on M(E0) \ F. Hence "the mistake cannot come back" holds for every family rich enough to hold hybrids iff M(E0) ⊆ F. ∎
4. **Symmetry.** Let σ be a permutation of the settings that maps F onto F and keeps the truth on F. Let σ map the good family onto the bad family, part by part. Then Pres_bad(F) = σ(Pres_good(F)), so every quantity computed from (V, F, Pres) is the same for both. ∎ On the gardener's record, σ is the W↔V swap.

## 7. Bearing on the record of rescues [INFERENCE]

**What the models support.**
- (E) with (A) blocks the general bad rescue on an open question, as a fact. Neither Pres nor option (b) catches it before a separating test. Pres cannot catch it, by fact 4.
- What Pres can register depends on a remembered earlier job set:
  - the narrowing registers as an enlargement only against the recorded wider index;
  - the fitted myth registers only when the report is left out as a block.
- Both need the history of which jobs a change was fitted to. That is the content of a record of rescues. The theory already keeps part of it in the historical index.

**Where option (b) marks what Pres misses, and the reverse.**
- (b) marks the single-exception patch and the law-family myth; Pres does not.
- Pres "registers" the W+Wi bad rescue only through its wider menu; (b) does not mark it on C_full.
- So on these models the two are not redundant with each other, and the owner's ground for calling the record redundant ("by definition") does not hold.

**The owner's intuition holds under two conditions,** and then as (A) rather than as looseness:
- the family is law-like (one law everywhere), and
- background jobs exercise the added part independently (the seed trial; the lamp and the card).

Under those conditions a bad rescue is not "easier to vary": it fails outright (BG_seed; the in-phase report under the sphere-only family). That is Deutsch's "the best explanations are the ones that are most constrained by existing knowledge" (D p.26), read as more jobs.

## 8. What I am unsure of

1. **Jobs are single pairs** and Account is read as (A) only. (F1) might exclude some versions counted here (for example rain anchored to rain). If so, it would shrink the bad rescue's Pres, not enlarge it. The direction of CX2 would stand.
2. **The menus are my statements.** The results are exact given them, and CX3 shows that they are what decides. A reader may hold that one menu is *the* right one. The theory supplies no rule that picks it, and the analysis's option (c) cost already says V becomes an assessor's input (D3:L516).
3. **The narrowing is read as "the summers seen before the failure".** If "the five recorded summers" includes the failure, E0 fails (A) on it. The analysis's Situation 3 (the bad rescue on the confined record) is covered as E_bad on J_after.
4. **The embedding uses a product family with "off" in the menu.** An embedding by a constant other than "off" gives the same containment facts (facts 1 and 2 need only Vers(E0) ⊆ Vers(E1)). Neighbourhood families (single edits of the candidate) were not run.
5. **Toy models.** A property shown in a finite model is a counterexample to a general claim. It is not evidence about how often real rescues behave so.

---

## Appendix — script outputs, verbatim

### `m1_gardener.py`

```text
==============================================================================
M1  THE GARDENER
==============================================================================
Settings: 16 = W{dry,wet} x Wi{calm,windy} x V{late,early} x Sun{sunS,shadeS}
Truth: N first iff V=early; otherwise the sunnier bed first.
E0 = (sun=id): the sunnier bed ripens first.
M(E0) = pairs where E0 is wrong = {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS, wet/windy/early/sunS}
J_before (records + shading test) = {dry/calm/late/sunS, dry/calm/late/shadeS}
f* (the failed sixth summer)      = wet/windy/early/sunS
J_after = J_before + f*
C_full = all 16 settings (every admitted change of the named variables)
BG_seed = {dry/calm/early/sunS}  BG_rain = {wet/calm/late/sunS}

------------------------------------------------------------------------------
(i) THE (A) TEST AND NON-CIRCULAR DEPENDENCE, each candidate on its stated contract
------------------------------------------------------------------------------
E0 (before)                 on J_before                           (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E0 (after the failure)      on J_after                            (A)=False NonCirc=True   fails at {wet/windy/early/sunS}
E_good                      on C_full                             (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_good                      on J_after                            (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_bad (wet->N)              on C_full                             (A)=False NonCirc=True   fails at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/late/sunS, wet/windy/late/sunS}
E_bad (wet->N)              on J_after (analysis Sit.3)           (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_patch (exception at f*)   on C_full                             (A)=False NonCirc=True   fails at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
E_patch (exception at f*)   on J_after                            (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_narrow = E0               on C_narrow (summers seen + shading)  (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_narrow_bare = E0          on C_narrow_bare (summers seen only)  (A)=True  NonCirc=False  no pair of C changes the answer

------------------------------------------------------------------------------
(ii)-(iv) NAIVE: each candidate in its OWN family (different organizations)
------------------------------------------------------------------------------
Stated menus: sun = all 4 maps {S,N}->{S,N}; an override reading ports P = all
predicates on P (off included); the exception = fires at exactly one setting (or off).
E0 before                    |V|=     4  |Pres|=    1  fraction=0.2500
E0 after the failure         |V|=     4  |Pres|=    0  fraction=0.0000
E_good  [var reads V]        |V|=    16  |Pres|=    1  fraction=0.0625
E_bad   [rain reads W]       |V|=    16  |Pres|=    1  fraction=0.0625
E_bad   [rain reads W,Wi]    |V|=    64  |Pres|=    4  fraction=0.0625
E_patch [single exception]   |V|=    68  |Pres|=    1  fraction=0.0147
E_narrow (E0 on C_narrow)    |V|=     4  |Pres|=    1  fraction=0.2500
E_patch [any predicate, 4 ports] |V|=262144  |Pres|=24576  fraction=0.0938

Naive subset test Pres_after <= Pres_before: the elements are tuples of different
length (sun) vs (sun, override); as Python sets they are always disjoint:
   E_good  [var reads V]        Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
   E_bad   [rain reads W]       Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
   E_bad   [rain reads W,Wi]    Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
   E_patch [single exception]   Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
Answer profiles as the only common currency (profile on C_full):
   E_good  [var reads V]        profiles(after) inside profiles(before)? False
   E_bad   [rain reads W]       profiles(after) inside profiles(before)? False
   E_bad   [rain reads W,Wi]    profiles(after) inside profiles(before)? False
   E_patch [single exception]   profiles(after) inside profiles(before)? False
   (any rescue changes the answer at f*, so this is False for every rescue; restricted
    to J_before every surviving profile equals the truth, so it is trivially "equal".)

------------------------------------------------------------------------------
(v) EMBEDDING  U = sun x var[V] x rain[W] x exc[single]   |U| = 1088
    Vers(E) = points of U whose components absent from E are off.
------------------------------------------------------------------------------
E0: |Vers|=4  |Pres(J_before)|=1  |Pres(J_after)|=0  |Pres(C_narrow)|=1  |Pres(C_full)|=0

E_good = (sun=id, var=early, rain=off, exc=off)   |Vers|=16
  (ii)  |Pres(J_before)|=2  |Pres(J_after)|=1  |Pres(C_full)|=1
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 0
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_good(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_good(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_good(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? True

E_bad = (sun=id, var=off, rain=wet, exc=off)   |Vers|=16
  (ii)  |Pres(J_before)|=2  |Pres(J_after)|=1  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 1
           e.g. (sun=id, var=off, rain=wet, exc=off)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_bad(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_bad(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_bad(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? False

E_patch = (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)   |Vers|=68
  (ii)  |Pres(J_before)|=17  |Pres(J_after)|=1  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 1
           e.g. (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_patch(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_patch(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_patch(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? False

Narrowing in U: E_narrow = E0 on C_narrow.  Pres_E0(C_narrow) vs Pres_E0(J_before): equal;
   vs Pres_E0(J_after): first STRICTLY CONTAINS second (1 vs 0)

------------------------------------------------------------------------------
(v) EMBEDDING  U = sun x var[V] x rain[W,Wi] x exc[single]   |U| = 4352
    Vers(E) = points of U whose components absent from E are off.
------------------------------------------------------------------------------
E0: |Vers|=4  |Pres(J_before)|=1  |Pres(J_after)|=0  |Pres(C_narrow)|=1  |Pres(C_full)|=0

E_good = (sun=id, var=early, rain=off, exc=off)   |Vers|=16
  (ii)  |Pres(J_before)|=2  |Pres(J_after)|=1  |Pres(C_full)|=1
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 0
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_good(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_good(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_good(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? True

E_bad = (sun=id, var=off, rain=wet&calm|wet&windy, exc=off)   |Vers|=64
  (ii)  |Pres(J_before)|=8  |Pres(J_after)|=4  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 4
           e.g. (sun=id, var=off, rain=wet&windy, exc=off)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
           e.g. (sun=id, var=off, rain=wet&calm|wet&windy, exc=off)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS}
           e.g. (sun=id, var=off, rain=dry&windy|wet&windy, exc=off)  wrong as E0 at {dry/calm/early/sunS, wet/calm/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_bad(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_bad(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_bad(J_after)| - |Pres_E0(J_before)| = +3 ;  vs E_good on J_after: +3
        does the candidate itself pass (A) on C_full? False

E_patch = (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)   |Vers|=68
  (ii)  |Pres(J_before)|=17  |Pres(J_after)|=1  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 1
           e.g. (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_patch(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_patch(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_patch(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? False

Narrowing in U: E_narrow = E0 on C_narrow.  Pres_E0(C_narrow) vs Pres_E0(J_before): equal;
   vs Pres_E0(J_after): first STRICTLY CONTAINS second (1 vs 0)

------------------------------------------------------------------------------
FULLY COMMON FAMILY: all of U free (Pres depends on the jobs only)
------------------------------------------------------------------------------
  |Pres(J_before (= C_narrow) )| =   68   members among named: E0, E_good, E_bad, E_patch
  |Pres(J_after               )| =   52   members among named: E_good, E_bad, E_patch
  |Pres(J_after + BG_seed     )| =   35   members among named: E_good
  |Pres(J_after + BG_rain     )| =   17   members among named: E_good, E_patch
  |Pres(C_full                )| =   13   members among named: E_good
  Pres(J_after) vs Pres(J_before): first STRICTLY INSIDE second  (the narrowing moves back from the first to the second)

------------------------------------------------------------------------------
COMPARISON: what the record of option (b) marks (no consequence beyond the failed pair)
------------------------------------------------------------------------------
  E_good   on C_full   consequences: 3   -> not marked
  E_good   on J_after  consequences: 0   -> MARKED (absorbed)
  E_bad    on C_full   consequences: 3   -> not marked
  E_bad    on J_after  consequences: 0   -> MARKED (absorbed)
  E_patch  on C_full   consequences: 0   -> MARKED (absorbed)
  E_patch  on J_after  consequences: 0   -> MARKED (absorbed)
  E_narrow: the limit follows from no component -> MARKED (absorbed)
```

### `m2_seasons.py`

```text
==============================================================================
M2  THE SEASONS
==============================================================================
Truth: N,H1=summer, N,H2=winter, E,H1=none, E,H2=none, S,H1=winter, S,H2=summer
J_greek = {N,H1, N,H2}   J_sailor = J_greek + {S,H1, S,H2}   J_world = all 6 pairs

------------------------------------------------------------------------------
(i) THE (A) TEST
------------------------------------------------------------------------------
  Tilt T* (t+1, sphere, direct)    on J_greek  (A)=True  
  Tilt T* (t+1, sphere, direct)    on J_sailor (A)=True  
  Tilt T* (t+1, sphere, direct)    on J_world  (A)=True  
  Tilt with escape clause (flat)   on J_greek  (A)=True  
  Tilt with escape clause (flat)   on J_sailor (A)=False fails at {S,H1, S,H2}
  Tilt with escape clause (flat)   on J_world  (A)=False fails at {E,H1, E,H2, S,H1, S,H2}
  Myth M0 (original)               on J_greek  (A)=True  
  Myth M0 (original)               on J_sailor (A)=False fails at {S,H1, S,H2}
  Myth M0 (original)               on J_world  (A)=False fails at {E,H1, E,H2, S,H1, S,H2}
  Myth M1 (amended, d=S)           on J_greek  (A)=True  
  Myth M1 (amended, d=S)           on J_sailor (A)=True  
  Myth M1 (amended, d=S)           on J_world  (A)=False fails at {E,H1, E,H2}

------------------------------------------------------------------------------
(ii) Pres AND WHAT IT LEAVES OPEN AT UNSEEN PAIRS (spread = answers across Pres)
------------------------------------------------------------------------------
  tilt, law menus, no background jobs            |V|=   12  |Pres(J_greek )|=   4  spread {'S,H1': ['summer', 'winter'], 'E,H1': ['none', 'summer']}
  tilt, law menus, no background jobs            |V|=   12  |Pres(J_sailor)|=   2  spread {'E,H1': ['none']}
  tilt, law menus, no background jobs            |V|=   12  |Pres(J_world )|=   2  spread 
  tilt, law menus + BG_heat, BG_elev             |V|=   12  |Pres(J_greek )|=   2  spread {'S,H1': ['summer', 'winter'], 'E,H1': ['none', 'summer']}
  tilt, law menus + BG_heat, BG_elev             |V|=   12  |Pres(J_sailor)|=   1  spread {'E,H1': ['none']}
  tilt, law menus + BG_heat, BG_elev             |V|=   12  |Pres(J_world )|=   1  spread 
  tilt, sphere only (one law everywhere) + BG    |V|=    6  |Pres(J_greek )|=   1  spread {'S,H1': ['winter'], 'E,H1': ['none']}
  tilt, sphere only (one law everywhere) + BG    |V|=    6  |Pres(J_sailor)|=   1  spread {'E,H1': ['none']}
  tilt, sphere only (one law everywhere) + BG    |V|=    6  |Pres(J_world )|=   1  spread 
  tilt, TABLE menus (all g, all h) + BG          |V|= 2187  |Pres(J_greek )|=  18  spread {'S,H1': ['none', 'summer', 'winter'], 'E,H1': ['none', 'summer', 'winter']}
  tilt, TABLE menus (all g, all h) + BG          |V|= 2187  |Pres(J_sailor)|=   6  spread {'E,H1': ['none', 'summer', 'winter']}
  tilt, TABLE menus (all g, all h) + BG          |V|= 2187  |Pres(J_world )|=   2  spread 
  myth, original organization (d fixed none)     |V|=   36  |Pres(J_greek )|=   2  spread {'S,H1': ['summer'], 'E,H1': ['summer']}
  myth, original organization (d fixed none)     |V|=   36  |Pres(J_sailor)|=   0  spread {'E,H1': []}
  myth, original organization (d fixed none)     |V|=   36  |Pres(J_world )|=   0  spread 
  myth, amended organization (d in none,S,E)     |V|=  108  |Pres(J_greek )|=   6  spread {'S,H1': ['summer', 'winter'], 'E,H1': ['summer', 'winter']}
  myth, amended organization (d in none,S,E)     |V|=  108  |Pres(J_sailor)|=   2  spread {'E,H1': ['summer']}
  myth, amended organization (d in none,S,E)     |V|=  108  |Pres(J_world )|=   0  spread 
  myth amended, TABLE menu (grief reads state and place) |V|= 2916  |Pres(J_sailor)|=  18  spread {'E,H1': ['none', 'summer', 'winter']}

------------------------------------------------------------------------------
(ii)-(iv) THE MYTH'S RESCUE: naive (own families) and embedded (d switched to none)
------------------------------------------------------------------------------
  NAIVE own families: original on J_greek |Pres|=2 of 36 (0.0556); amended on J_sailor |Pres|=2 of 108 (0.0185)
  NAIVE, table menu for the amended grief: amended on J_sailor |Pres|=18 of 2916  (original: 2)
  EMBEDDED in the amended organization; Vers(M0) = d=none (36), Vers(M1) = all d (108):
    |Pres_M0(J_greek)|=2  |Pres_M0(J_sailor)|=0  |Pres_M1(J_greek)|=6  |Pres_M1(J_sailor)|=2
    M0 (d switched off) in Pres_M1(J_sailor)? False
    (iii) Pres_M1(J_sailor) vs Pres_M1(J_greek) [(H)]: first STRICTLY INSIDE second
          Pres_M0(J_greek) vs Pres_M1(J_greek) [old jobs]: first STRICTLY INSIDE second
          Pres_M1(J_sailor) vs Pres_M0(J_greek): disjoint
    (iv) |Pres_M1(J_sailor)| - |Pres_M0(J_greek)| = +0  -> the amendment does NOT enlarge Pres
         |Pres_M1(J_sailor)| - |Pres_M1(J_greek)| = -4  (the same shrink a correction shows)
    M(M0) = {E,H1, E,H2, S,H1, S,H2}
    versions in Pres_M1(J_sailor) that keep M0's wrong answer somewhere in M(M0): 2 of 2 (at E)
    spread of Pres_M1(J_greek) at the sailor's pairs: {'S,H1': ['summer', 'winter'], 'S,H2': ['summer', 'winter']}

------------------------------------------------------------------------------
THE TILT'S OWN CORRECTION (escape clause -> sphere): same organization, file 00 condition met
------------------------------------------------------------------------------
  tilt, law menus, no background jobs      |Pres(J_greek)|=4  |Pres(J_sailor)|=2  (H): first STRICTLY INSIDE second;  escape version in Pres(J_sailor)? False
  tilt, law menus + BG_heat, BG_elev       |Pres(J_greek)|=2  |Pres(J_sailor)|=1  (H): first STRICTLY INSIDE second;  escape version in Pres(J_sailor)? False
  M(escape version) = {E,H1, E,H2, S,H1, S,H2}
  tilt, law menus, no background jobs      versions in Pres(J_sailor) giving the escape version's wrong answer somewhere: 0 of 2
  tilt, law menus + BG_heat, BG_elev       versions in Pres(J_sailor) giving the escape version's wrong answer somewhere: 0 of 1
  tilt, TABLE menus (all g, all h) + BG    versions in Pres(J_sailor) giving the escape version's wrong answer somewhere: 2 of 6

------------------------------------------------------------------------------
"NOWHERE TO GO" (Deutsch p.25): a hypothetical report that the south is IN phase with Greece
------------------------------------------------------------------------------
  tilt, law menus, no background jobs            |Pres(in-phase report)| =   2  e.g. (t+1, flat/escape, direct)
  tilt, law menus + BG_heat, BG_elev             |Pres(in-phase report)| =   1  e.g. (t+1, flat/escape, direct)
  tilt, sphere only (one law everywhere) + BG    |Pres(in-phase report)| =   0  -> nowhere to go
  tilt, TABLE menus (all g, all h) + BG          |Pres(in-phase report)| =   6  e.g. (t+1, g+1+1+1, hs/w/n)
  myth, original organization (d fixed none)     |Pres(in-phase report)| =   2  e.g. (sched:ha, u:home->summer,away->winter, d=none)
  myth, amended organization (d in none,S,E)     |Pres(in-phase report)| =   4  e.g. (sched:ha, u:home->summer,away->winter, d=none)

------------------------------------------------------------------------------
TILT vs AMENDED MYTH on the jobs each now does
------------------------------------------------------------------------------
  tilt, law menus, no background jobs            |Pres(J_sailor)| = 2
  tilt, law menus + BG_heat, BG_elev             |Pres(J_sailor)| = 1
  tilt, sphere only (one law everywhere) + BG    |Pres(J_sailor)| = 1
  myth, amended organization (d in none,S,E)     |Pres(J_sailor)| = 2
      myth version in Pres: (sched:ha, u:home->summer,away->winter, d=S)
      myth version in Pres: (sched:ah, u:home->winter,away->summer, d=S)
      tilt version in Pres (T1): (t+1, sphere, direct)
      tilt version in Pres (T1): (t-1, sphere, inverse)

------------------------------------------------------------------------------
HISTORY-FREE vs HISTORY-USING detection of a fitted part
  LOO(x): is the answer at x fixed by Pres(F - {x})?  BLOCK: is it fixed by Pres(F - block)?
------------------------------------------------------------------------------
  amended myth (embedded family)   LOO at S,H1: answers ['winter']
  amended myth (embedded family)   LOO at S,H2: answers ['summer']
  amended myth (embedded family)   BLOCK (sailor's report left out): answers at S,H1 ['summer', 'winter'], at S,H2 ['summer', 'winter']
  tilt T1 (no background)          LOO at S,H1: answers ['winter']
  tilt T1 (no background)          LOO at S,H2: answers ['summer']
  tilt T1 (no background)          BLOCK (sailor's report left out): answers at S,H1 ['summer', 'winter'], at S,H2 ['summer', 'winter']
  tilt T2 (+BG)                    LOO at S,H1: answers ['winter']
  tilt T2 (+BG)                    LOO at S,H2: answers ['summer']
  tilt T2 (+BG)                    BLOCK (sailor's report left out): answers at S,H1 ['summer', 'winter'], at S,H2 ['summer', 'winter']
  tilt T3 (sphere only, +BG)       LOO at S,H1: answers ['winter']
  tilt T3 (sphere only, +BG)       LOO at S,H2: answers ['summer']
  tilt T3 (sphere only, +BG)       BLOCK (sailor's report left out): answers at S,H1 ['winter'], at S,H2 ['summer']

------------------------------------------------------------------------------
NARROWING: "the myth only covers Greece" (after the report)
------------------------------------------------------------------------------
  Pres_M0(J_greek) after narrowing vs before the report: equal (|2| vs |2|);  vs Pres_M0(J_sailor): first STRICTLY CONTAINS second (0)

------------------------------------------------------------------------------
OPTION (b) consequences (pairs of J_world other than the sailor's where the change matters)
------------------------------------------------------------------------------
  myth amendment d: none -> S        consequences {} -> MARKED (absorbed)
  tilt correction flat -> sphere     consequences {E,H1, E,H2} -> not marked
```

### `cx_counterexamples.py`

```text
==============================================================================
CX1  A GOOD CORRECTION THAT LEAVES THE OLD MISTAKE REFITTABLE
==============================================================================

Family: sun x var[V]  |V|=16   E_good = (sun=id, var=early)
  E_good passes (A) on J_after (holds f*)? True   on C_full? True
  jobs = J_after + {}                                                         |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS}                                      |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS}                                     |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {wet/calm/early/sunS}                                      |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS}                |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, wet/calm/early/sunS}                 |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS, wet/calm/early/sunS}                |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS} |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + BG_seed (the seed trial)                                   |Pres|=  1  mistake-reinstating=  0
  jobs = C_full (the world's contract)                                        |Pres|=  1  mistake-reinstating=  0

Family: sun x var[V+W]  |V|=64   E_good = (sun=id, var=early&dry|early&wet)
  E_good passes (A) on J_after (holds f*)? True   on C_full? True
  jobs = J_after + {}                                                         |Pres|=  4  mistake-reinstating=  2
      e.g. (sun=id, var=early&wet)  gives E0's wrong S at {dry/calm/early/sunS, dry/windy/early/sunS}
  jobs = J_after + {dry/calm/early/sunS}                                      |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS}                                     |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {wet/calm/early/sunS}                                      |Pres|=  4  mistake-reinstating=  2
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS}                |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, wet/calm/early/sunS}                 |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS, wet/calm/early/sunS}                |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS} |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + BG_seed (the seed trial)                                   |Pres|=  2  mistake-reinstating=  0
  jobs = C_full (the world's contract)                                        |Pres|=  1  mistake-reinstating=  0

Family: sun x var[V+W+Wi]  |V|=1024   E_good = (sun=id, var=early&dry&calm|early&dry&windy|early&wet&calm|early&wet&windy)
  E_good passes (A) on J_after (holds f*)? True   on C_full? True
  jobs = J_after + {}                                                         |Pres|= 64  mistake-reinstating= 56
      e.g. (sun=id, var=early&wet&windy)  gives E0's wrong S at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
  jobs = J_after + {dry/calm/early/sunS}                                      |Pres|= 32  mistake-reinstating= 24
  jobs = J_after + {dry/windy/early/sunS}                                     |Pres|= 32  mistake-reinstating= 24
  jobs = J_after + {wet/calm/early/sunS}                                      |Pres|= 32  mistake-reinstating= 24
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS}                |Pres|= 16  mistake-reinstating=  8
  jobs = J_after + {dry/calm/early/sunS, wet/calm/early/sunS}                 |Pres|= 16  mistake-reinstating=  8
  jobs = J_after + {dry/windy/early/sunS, wet/calm/early/sunS}                |Pres|= 16  mistake-reinstating=  8
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS} |Pres|=  8  mistake-reinstating=  0
  jobs = J_after + BG_seed (the seed trial)                                   |Pres|= 32  mistake-reinstating= 24
  jobs = C_full (the world's contract)                                        |Pres|=  1  mistake-reinstating=  0

  (check: in every family above no version in Pres(J_after) repeats E0's answer at f* itself)

==============================================================================
CX2  A BAD RESCUE THAT DOES NOT ENLARGE Pres: the record cannot tell wet from early
==============================================================================
swap(J_after) == J_after as a set? True ; truth kept on J_after under the swap? True
swap(C_full truth) == truth? False  (the world is not symmetric)
good reads     bad reads        |Pres_g|   |Pres_b| swap bijection |Pres_g|full |Pres_b|full
V              W                       1          1           True            1            0
V+Wi           W+Wi                    4          4           True            1            0
V+Sun          W+Sun                   6          6           True            5            0
V+W            W+V                     4          4           True            1            1
V+W+Wi         W+V+Wi                 64         64           True            1            1

Port-swap family (override fires on one literal): Pres(J_after) = ['(sun=id, cond=wet)', '(sun=id, cond=windy)', '(sun=id, cond=early)']
  -> "windy would fit as well" and "wet would fit as well" hold of the GOOD rescue too.
  with the seed trial BG_seed added: ['(sun=id, cond=early)']
  with another wet spring BG_rain added: ['(sun=id, cond=windy)', '(sun=id, cond=early)']

Do-nothing patch, single-exception family: |Pres(J_after)| = 1 (E_good with var[V]: 1; E0 before: 1)

==============================================================================
CX3  VERDICTS THAT FLIP WITH THE VARIATION FAMILY
==============================================================================
|Pres(J_after)| for E_good (rows: ports its variety component reads) vs E_bad (columns)
            bad:W           bad:W+Wi        bad:W+Sun       bad:W+Wi+Sun    
good:V      1:1 equal       1:4 bad easier  1:6 bad easier  1:96 bad easier 
good:V+Wi   4:1 good easier 4:4 equal       4:6 bad easier  4:96 bad easier 
good:V+Sun  6:1 good easier 6:4 good easier 6:6 equal       6:96 bad easier 
good:V+W+Wi 64:1 good easier64:4 good easier64:6 good easier64:96 bad easier

Do-nothing patch: single-exception family |Pres(J_after)|=1 ; any-predicate family |Pres(J_after)|=24576

==============================================================================
CX4  (H) NON-STRICT, AND IDLE PARTS IN THE COUNT
==============================================================================
E_good family sun x var[V]: Pres(J_after + BG_rain) vs Pres(J_after): equal (1 vs 1)
  -> a genuinely new job (another wet spring) is added and nothing is excluded.
Fully common family U: |Pres(C_full)| = 13, although only one answer profile survives:
    (sun=id, var=early, rain=off, exc=off)
    (sun=id, var=early, rain=off, exc=only@dry/calm/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@dry/calm/early/sunS)
    (sun=id, var=early, rain=off, exc=only@dry/calm/early/shadeS)
    (sun=id, var=early, rain=off, exc=only@dry/windy/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@dry/windy/early/sunS)
    (sun=id, var=early, rain=off, exc=only@dry/windy/early/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/calm/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/calm/early/sunS)
    (sun=id, var=early, rain=off, exc=only@wet/calm/early/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/windy/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/windy/early/sunS)
    (sun=id, var=early, rain=off, exc=only@wet/windy/early/shadeS)
  -> every surviving version gives the true answers; the count is inflated by idle
     exceptions that fire where the answer is N anyway (counting versions is no warrant).

==============================================================================
CX5  LEAVE-ONE-OUT (history-free) vs LEAVE-THE-FAILURE-OUT, gardener
==============================================================================
  jobs J_after            E_good var[V]  passes (A) on the jobs? True   answers at f* fixed by the other jobs: ['N', 'S']
  jobs J_after            E_bad rain[W]  passes (A) on the jobs? True   answers at f* fixed by the other jobs: ['N', 'S']
  jobs J_after + BG_seed  E_good var[V]  passes (A) on the jobs? True   answers at f* fixed by the other jobs: ['N']
  jobs J_after + BG_seed  E_bad rain[W]  passes (A) on the jobs? False  answers at f* fixed by the other jobs: []
```

