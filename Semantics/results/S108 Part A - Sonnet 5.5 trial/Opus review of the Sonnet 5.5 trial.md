# Opus review of the Sonnet 5.5 trial (S53): Part A, section 2, computed twice

*A fresh Opus 5.5 agent, 28 September 2026. Compared: Opus 5.5's `results/S108 Part A - section 2 - variants computed.md` / `.json` and its program copy `S108 Part A - computation/section 2 model/`, with Sonnet 5.5's `section 2 - variants computed (Sonnet 5.5).md` / `.json` and its copy `section 2 model/` (this folder). Both worked from the same reply and rule 5. Reruns were made on scratch copies of both programs, every run under `timeout`, PYTHONHASHSEED=0. Nothing here changes the theory. "Model" is used only for the program's folder.*

## 1. Comparison

**Variants and how they were implemented**

| variant | Opus 5.5 | Sonnet 5.5 | same? |
|---|---|---|---|
| V2.1, V2.2, V2.3, V2.6, V2.7 | as written | as written; the code is the same as Opus's line for line | yes |
| V2.3b (τ(a) ≠ 1) | not done | added as its own reading: 6 accounts on τ[C] ⊆ {1}×B survive V2.3, 0 survive V2.3b | Sonnet did more |
| V2.4 (NC1 back in (E)) | replaces (E) wherever the program computes the current (E), including the explicit `account(reading="S106")` calls | changes only the default; `claims_s106.py` and `claims_r3a2.py` still compute the old (E) by name | **no**: Sonnet's reach is partial |
| V2.5 (Sel with H = ∅) | `sel()` whatever the caller asks, plus the two hand-written "H nonempty" tests (`claims_s41.py` FC30.new1 (d), CT8) | flips the global `SEL_H_NONEMPTY` only; explicit `h_nonempty=True` calls and the hand-written tests are unchanged | **no**: Sonnet's reach is partial |
| V2.8 | not implemented (out of scope) | not implemented (out of scope) | yes |
| off = round 4 | suite identical to the printout (133 / 2 / 7) | the same | yes |

**Computed effects**

| place | Opus 5.5 | Sonnet 5.5 | verdict |
|---|---|---|---|
| worked cases | V2.3: E_rev, E_fwd on C_id T→F. V2.4: 11 T→F. V2.5: every account F→T on a history with nothing tried | V2.3: E_rev on C_id (E_fwd as small case H2). V2.4: the same 10 (ℰ_myth1 as small case F). V2.5: the same, as its "scenario (ii)" | agree |
| FC-E1–E5, CT1–CT8 | no (E) moves; V2.5 does not reach CT8 (its H is nonempty) | no (E) moves; V2.5 "reaches" CT8, but only through a history set by hand in place of CT8's own | agree on (E); Sonnet's CT8 claim rests on a hand-set input |
| generated worlds, scale 4 (17,280 each; same design, different seeds) | F→T / T→F: V2.1 57, V2.2 23, V2.3 253, V2.4 972, V2.5 1,027 of 1,027; V2.6 310/310 kind ii lost; V2.7 410/1,822 ConfCl lost | V2.1 59, V2.2 16, V2.3 264, V2.4 952, V2.5 1,022 of 1,022; V2.6 142/142; V2.7 393/1,873 | agree in direction and size; both reproduce exactly on rerun (Opus's routes script, Sonnet's V2.2 and V2.4 worlds) |
| suite V2.1, V2.2, V2.3, V2.6, V2.7 | 133/2/7, 133/2/7, 132/3/7, 132/3/7, 132/3/7 | the same, the same claims | agree |
| suite V2.4 | **127/8/7**: + FC23.new1 (h) | **128/7/7** | **Opus right**. Rerun: FC23.new1 is a counterexample in Opus's copy ((E) under the four quantifiers F,F,T,T) and holds in Sonnet's only because Sonnet's V2.4 leaves the "S106" calls alone. In the same rerun, Sonnet's copy prints the lookups M1–M3 as meeting (E) under V2.4, against its own default calls |
| suite V2.5 | **131/4/7**: + FC30.new1 (e) | **132/3/7** | **Opus right**. Rerun: FC30.new1 (e), the reply's own case, moves in Opus's copy and stays "Dec True" in Sonnet's |
| count moves in the suite | left out as "timed" | reported: FC29, FC37, FC46, FC51 (V2.1, V2.2); FC47, FC49, **FC50 (a) 572 → 0** (V2.6) | **Sonnet right**. These searches are seeded and run to the end, so the counts depend on the seed, not on time. Under V2.6, FC50 (a) holds only because nothing meets its hypothesis |

**Edges: the 20 in-scope rows the reply named**

| | Opus 5.5 | Sonnet 5.5 |
|---|---|---|
| tally | computed 13, contradicted 3, not settled 4 | computed 11, contradicted 1, not settled 2, mixed 6 |
| same headline status | 12 rows: r1, r3, r6, r8, r9, r10, r11, r13, r14, r16, r18, r19 | |
| differ in substance | r5 (V2.2, L299.s1): **contradicted**. Rerun reproduces the witness: S = {{k0,k1},{k0,k2},Γ}, Γ meets (E) under V2.2, and block {k1,k2} is critical with no singleton of it critical | r5: computed, from cases B and C only (no singleton critical anywhere). The reply's "such a candidate now fails (E)" is not general. **Opus right** |
| | r7 (V2.3, L329.s3): **contradicted as to L329.s3**. Identification (Z_y ≠ ∅ ∧ \|f[Z_y]\| = 1) reads no (E); FC57, FC58 and Ident do not move | r7: computed. It checks only the reply's "why" clause and not the item it names. **Opus right** |
| differ in labelling | r2, r4, r12, r15, r17, r20: Opus says computed or not settled | Sonnet says "mixed" | Sonnet's labels are more careful on r12, r15 and r17. Opus's own text for these rows says a part is not computed |
| r6 (V2.2, fewer problems) | contradicted: Riv does not move (0 of 3,835), and D10.1 reads NotOut_j, not Acc | contradicted, but "on the proxy": problems = both meet Acc ∧ rivals | same status. Sonnet's proxy misreads D10.1 |
| L309 (the reply's unsettled edge) | computed: S = {{a}}, unchanged | computed (case D): the same | agree |
| edges added | 17 | 12 (JSON; 16 bullets in the md) | Opus's are structural (critical blocks, L307 blocked, quantifier, the copy stays Dec); many of Sonnet's are claim moves or null results |

**Errors found**

| # | whose | what |
|---|---|---|
| S1 | Sonnet | V2.4 is implemented only partly (see above). It misses the edge "V2.4 makes (E) depend on D6.3's quantifier again", which contradicts the reply's I136/I184 note ("quantifier-independent"). Its V2.4 suite total is wrong |
| S2 | Sonnet | V2.5 is implemented only partly. It never reaches the program's own encodings of the declared link (FC30.new1 (d), (e)). So r14's "the student's declared copy becomes an explanation" rests on a history set by hand. On the program's computed history (FC30.new1 (d)) the copy of a worked-out formula stays Dec under U, T and T′ (rerun) |
| S3 | Sonnet | "FC107 under V2.4 differs only in a printed generated label". Its own printout shows Acc True → False for the identity candidate on p_δ, which is the r11 (Bearing) edge |
| S4 | Sonnet | "(Suff)'s defeat set and Out_j are not program functions". In fact `suff_defeats` (claims_s41.py), `usable` and `rules_out` (args.py) and `expl_ruled_out` are, and FC23.new2 (f), a defeat-set computation, moved in its own V2.4 run. Parts of r12 and r15 were left unsettled when they could have been computed |
| S5 | Sonnet | Its problem proxy puts Acc in place of NotOut_j (D10.1). The added edge "V2.1 adds kind-ii problems (47 → 57)" and the V2.3 and V2.4 problem counts rest on that proxy, not on D10.1 |
| S6 | Sonnet | r5 and r7 are marked computed (see the edge table) |
| S7 | Sonnet | Unbacked generalisations. First: "the candidate with no commitments meets (E) whenever the answer varies over C" rests on one case, and 0 of the 355 generated worlds with no commitments moved. Second: it marks the reply's "newly meeting (E): the written-in candidate" as contradicted by reading it as L273, but the reply names a class of candidates |
| O1 | Opus | It left out the hypothesis counts as "timed", so it missed that FC50 (a) becomes vacuous under V2.6, and the count moves |
| O2 | Opus | It marks R12, R15 and R17 computed although a part of each is unsettled, which its own row text says. Its "14 computed" overstates |
| O3 | Opus | N16 says "no claim builds a candidate whose Dependence needs a block of two or more (FC37–FC40 test set systems)". But under V2.2, FC46's accounts drop from 962 to 927, and the FC29, FC37 and FC51 counts move. The gap it names (no claim's *result* separates V2.2) still holds |
| O4 | Opus | It did not examine the reading of V2.3 through τ, which Sonnet's V2.3b shows matters (6 accounts) |

**Time.** Sonnet 5.5 took 76 min 25 s (timing.txt: 21:32:25–22:48:50; commit a374058 at 22:48:58). Opus 5.5 took about 61 min, from its copy (18:37) to its commit 6e17160 (19:38:23), while three other section agents ran (load 5–8 on 4 cores).

## 2. Verdict

On what can be counted, Sonnet 5.5 matched Opus 5.5:
- the same variants and the same code for five of them;
- the same moves on the worked cases;
- generated-world counts of the same size, reproducible on rerun;
- the same suite results for five of seven variants;
- 12 of 20 edge statuses the same.

It did three things better:
- it reported the count moves (FC50 (a) vacuous under V2.6);
- it built a finite analogue of L311;
- it tested V2.3's reading through τ.

Its "mixed" labels are more careful than Opus's "computed".

It fell short where the job is analysis rather than bookkeeping:
- two variants reached only part of the program, so their suite results and one edge the reply got wrong (V2.4's quantifier) were missed;
- the reply's V2.5 claim was accepted on a history set by hand, where the program's own history for the copy says otherwise;
- it misread one line of its own output (FC107);
- it said functions were missing that exist;
- a proxy misread a definition (D10.1);
- two edges were marked computed where a closer reading, or a search for a counterexample, contradicts them.

Every one of these needed an Opus check to find. It also took longer than Opus did under heavier load.

It genuinely helps as an **independent second computation**: agreement on the numbers is worth having, and it found one thing Opus missed. It does not genuinely help as **the agent of record** for this kind of analysis. Its errors are the quiet kind, a variant that reaches part of the program or a claim read too loosely, and they pass without a reviewer. On this trial the answer to S46 ("maybe analysis isn't something it should be used for. Unless it's something that genuinely helps") is:
- yes for a replication that Opus reviews;
- no as a replacement for the Opus computation or its review.

Sonnet's mechanical jobs stay as S46 has them.

Reviewed by one Opus 5.5 agent, 28 September 2026. Reruns: FC23.new1 and FC107 under V2.4, FC30.new1 under V2.5, in both copies; Opus's `s108_s2_routes.py` (identical to its printout); Sonnet's `s108_section2_worlds.py` V2.2 and V2.4 (identical to its printouts).
