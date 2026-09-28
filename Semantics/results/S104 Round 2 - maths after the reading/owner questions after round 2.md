# S104 Round 2 — owner questions after round 2

*Integration, 28 September 2026. From `area N - verdicts and formal fixes.md` (A1 §5, A2 §4, A3 "Owner questions"). 26 questions asked; 25 after one merge (A1 OQ-1 = A3 OQ11). None applied. "Blocks": a change waits whichever side is taken. "Standing": one of the owner's standing questions — where values are placed (S31); the reading of "argument" (S23); what hard to vary covers (S34, parked).*

## A. Block a change (8)

| # | question | side 1 | side 2 | from | standing |
|---|---|---|---|---|---|
| Q1 | The loop Rep → Con → Build → Rep ("represented", L197, L405; "no cycle", L526): where to cut it | K: Sel, Con, Build read (R) only at earlier occurrences; no cycle; a first construction of c gives no representation of c (FC98 (d)) | T: Con's "represented target" read as held through Θ; no cycle; a first construction represents (L405 "A first representation may be constructed") | A3 OQ1; E03, D18.1, D13.3; I146 | — |
| Q2 | (Suff) at L536: keep "with a transport whose provenance is not declared" | keep: (Suff) claimed only of non-declared transports; Def(L536) ⊊ Def(L17) | drop: (Suff) as L17 states it; (E) takes no provenance (L277) | A3 OQ3; E06 | — |
| Q3 | "prediction" at L151 | L151 stops borrowing it: writes Ans_E(τa,σb) | L219 widens "prediction" to every transport (I51 written in) | A1 OQ-6; FC35, I51, matter 6 | — |
| Q4 | The formal core's primitives (δ, Offered, restriction, Integrated, Nontrivial, Prepares, BindingConstruction, TransferComposite, ExplUse, MadeFrom, Applies, Aims*, O_ex, K, Rec, Chg, Rule, Occurs, Attempt, Qf, AtRest) | list them at L522 as stated, not defined (GLM) | define some, so L596 holds without new inputs | A3 OQ2; FC98 (b), L522, L596 | — |
| Q5 | Tolerance in (CT1) (ϑ of RetReal^{q,r}_ϑ) | over each execution's output and return | over the family of executions (fallible performance kept as capability) | A3 OQ12; E17, D15.2; I153 | — |
| Q6 | "episode" (L55 vs L197, L405, L429) | a delimited subhistory (the body's uses; D13.8) | L55's: a history in which contracts change, each change recorded (then Con and (EX) need contract changes) | A1 OQ-5; H06, C07, C02, D12.2; I131 | — |
| Q7 | "event" (L53, L55, L161, L397, L604, L612; defined nowhere) | a nonempty set of occurrences of one history (I45) | events have identities of their own (L612 "lost event identities") | A1 OQ-4; D11.1, I45, FC105, matter 2 | — |
| Q8 | 𝔓^adv_Θ in (U2) | defined | (U2), (U3) stated as conditional on it | A3 OQ7; D16.4, NF12 | — |

## B. Open readings (17)

| # | question | side 1 | side 2 | from | standing |
|---|---|---|---|---|---|
| Q9 | May a footprint bijection recode port values (D4.2's equal-domain clause, I10) | Mimo: that is "where values are placed", the owner's; not written in | GLM: nothing in the owner's words points either way; write equal domains in | A1 OQ-1 (D4.2, I10) = A3 OQ11 (FC18, I10 (a)) | where values are placed — per Mimo; A2 (D5.1) reads port values as not that question |
| Q10 | Must value maps κ be injective (FC20, I14) | yes (GLM): a merging κ hides a difference (F1) should catch (L245) | no: L189 lets π merge values; κ stays open | A1 OQ-2 | — |
| Q11 | Does a failed prediction ((A) at a pair) count as violation (L220) | yes (Mimo): then the words must say so | no: L220 names fidelity, which L189 defines by (F1), (F2) only | A1 OQ-3; I50, D12.7 | — |
| Q12 | May a population hold variants discovered new (FC83) | yes (GLM): S20 "a variation is a competitor … two discovered variations" | no: L225, L47 keep origin with construction; FC83' formalizes the sentence as it stands | A1 OQ-7 | touches what hard to vary covers (parked; cf. P2) |
| Q13 | Can a question or a defect be a target organization for p_δ (FC107) | the owner's (GLM) | L161 says only "another question with its own contract" | A1 OQ-8 | — |
| Q14 | T9 (L195) in (R)'s sense for a coding search | a search whose code represents H, the survival condition or cod t is not selected | a coded-fitness search is ordinarily selection; its class turns on the provenance of the code's writing | A1 OQ-9; C03, C02 | — |
| Q15 | NC2's contrast when the baseline answer is ⊥ (D6.4, I22) | asymmetric (the maths): a contrast needs a determined baseline | symmetric: a value against ⊥ at either point counts (else M13 admits no NC2) | A2 OQ-1 | — |
| Q16 | May the deleted block G be the whole of Γ (D6.4) | G ≠ Γ: with G = Γ NC2 asks little | G ⊆ Γ (the text; L293): G ≠ Γ fails every one-commitment candidate | A2 OQ-2 | — |
| Q17 | Where boundary values sit for NC1 (I79) | boundary coordinates of their own, checked apart (L255 names two routes) | carried by components (the program) | A2 OQ-3 | — |
| Q18 | Is a problem posed again once the ruling-out argument stops being usable (D10.6) | yes: L317 "while the argument stays usable" | S20 "the mistake shouldn't be able to creep back in" points the other way | A2 OQ-4 | touches S20 (cf. P3, parked) |
| Q19 | What "work" is (L231, (B), L305, L313; E02) | work for (E) as a whole, (F2) included (FC-E1) | work for the answer to 𝒬 only: a relevance condition, a new definition | A2 OQ-5 | — |
| Q20 | "requires" at L443 (I59) | a necessary condition on explanatory aims | their characterization | A3 OQ4 | — |
| Q21 | (CT3) (I62, L479) | a consequence of "achievable" (T14) | an assumption on Admit | A3 OQ5 | — |
| Q22 | "can affect its operative use" (L487; H16) | read through active routes (I159) | left modal | A3 OQ6 | — |
| Q23 | Is a bare premise an argument (I88; L397) | no: "argument steps whose leaves are premises" | yes: an argument may have no step | A3 OQ8 | the reading of "argument" (S23) |
| Q24 | Value sets of the contract's membership and query ports (I67) | fixed | left open | A3 OQ9 | — |
| Q25 | The rule at the ends of the line of cells (I100) | stated (reflect, stop) | left open | A3 OQ10 | — |

Not owner questions (the areas' own rulings): A2 — D5.1 (value maps: port values), I65, FC62, FC63/I99; A3 — the window bound at L626 (computed: a fix, not a choice).
