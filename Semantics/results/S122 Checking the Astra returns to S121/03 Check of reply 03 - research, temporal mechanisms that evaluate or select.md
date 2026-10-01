# Check of GPT 6 Astra's reply 03: research, temporal mechanisms that evaluate or select (log S122)

*Written by Claude (Opus 5.5) on 1 October 2026, decision S75, by the one agent doing the whole S122 job (S56, S68). Reply checked: `tests/S121 Returns from GPT 6 Astra/03 Return - research, temporal mechanisms that evaluate or select.docx` (kept unchanged; read through its extracted text beside it and, for its links, the Word file itself), answering `tests/S121 Briefs for GPT 6 Astra/03 Research, checked - temporal mechanisms that evaluate or select.md`. The owner's report: `tests/S121 Material - the owner's report on temporal computation in neurons/`. Avida source: 2.14.0 at commit 47f13dad, the clone in the scratch space, read only. Outside sources were opened on the web on 1 October 2026 (PubMed records through the PubMed connector; papers and pages through a web fetch; one through a web search where the publisher refused the fetch); what could not be read is said. In the owner's Avida terms (S61): the **execution environment** is the whole simulated world, and it is the selector under test (S72). No Avida process was run for this check. No GLM check (S70's latest word on GLM). The reply holds no code (`tools/s122/03/00 Where each file came from.md`).*

## 1. What the reply offers

1. **Nine mechanisms mapped to Avida selectors**, in a table and one section each: habituation and stimulus-specific adaptation; reward prediction error and temporal-difference learning; eligibility traces; neuromodulated plasticity; homeostatic plasticity; neuromodulation in evolutionary robotics; a reservoir read out as a critic; learning progress; resource depletion and renewal. For each: what the opened source reports, how it would act as an Avida selector, its grade ("2 / 1": a grade 2 rule acting on grade 1 named task checks, every time), a cost in lines of driver code (no C++), and what would count against it.
2. **A check of the owner's report's 22 sources**, one line each: 18 hold, 2 hold in part (3, 11), 1 does not hold (6); source 6's number points at the wrong article.
3. **Where nothing is known**: no grade 3 mechanism was found; one Avida precedent of temporal feedback exists already (resources that run down and refill, Chow et al. 2004); no blockwise learned selector of the kind proposed was found (a bounded search, not a census).
4. **A hard-to-vary note**: history matters only if two histories with the same present give different responses; a timer does the same job as the report's resetting trace with one threshold.
5. **Five options with costs** (none chosen), from a 0-CPU-hour replay check of the driver to an outer search over controllers.
6. **32 references**, every one marked "checked", with the access route stated (abstract only, alternate copy, cookie redirect).

It ran no Avida process and says so; it ran only a check of its own document ("AUDIT_ROWS=22 MECHANISM_SECTIONS=9 REFERENCES=32 FINAL_LINE=END OF REPORT", pasted as one line). The counts in that line match the document: 22 audit rows, 9 mechanism sections, 32 references, last line `END OF REPORT`.

## 2. Its Avida claims, checked against 47f13dad and the record

The reply did not open Avida (it says so) and makes few Avida claims.

| # | Claim | Holds? | Where |
|---|---|---|---|
| 1 | Avida already has temporal feedback: resources that run down with use and are renewed by inflow, so pay depends on past consumption. | holds | `main/cEnvironment.cc` resource processing (S113's plan, section 2, cites `DoProcesses` from line 1610); stock example `support/config/misc/environment-9resource.cfg` exists; S113's COMMON TASKS PAY LESS and S118's P1 used it |
| 2 | "Reload resets resource stocks", so a blockwise driver must keep an external pool. | in part | Stock `SavePopulation` writes programs, not resource levels, so a plain reload starts each resource afresh. But S113's runner already carried the levels across reloads by writing them as the next piece's starting amounts, and S114 found **no reset** that way (largest difference 0), only a disturbance for some updates after each reload (median 13% per update against 3.6% unbroken). The reply's remedy is already in use. |
| 3 | The blockwise versions need no C++ if the existing driver is reused. | holds | Reply 01's runner does exactly this with stock Avida (its C++ diff is empty; checked in `01 Check ...`, section 2) |
| 4 | An in-process hook to avoid restarts might take 200 to 500 C++ lines (unchecked, it says). | not checked as a number; one correction | Stock Avida can already change a task's pay during a run without restarting (`SetReactionValue`, `SetReactionValueMult`, registered in `actions/EnvironmentActions.cc` lines 1731-1732), but only from the events file, which cannot read the program population; so a selector that reads and pays in one process does need new code. The line count is an estimate. |
| 5 | A 50,000-update run in 1,000-update pieces gives the selector only 50 decisions. | holds | arithmetic; reply 01's runner steps once per piece |
| 6 | Costs from one CPU-hour per 50,000 updates (e.g. 12 runs of 10,000 updates = 2.4 CPU-hours). | holds, as arithmetic and, roughly, as a rate | measured in the whole S122 pilot from the ancestor in a 60 x 60 world: about 61 CPU-seconds per 1,000-update piece on average (about 40 in the first piece, about 60 later), plus about 2 CPU-seconds per six-order assay: about 0.35 CPU-hours per 20,000 updates and about 0.9 per 50,000 (`01 Check ...`, section 6). *Corrected after the pilot finished: when first committed this row said "the rate is generous from the ancestor" and gave about 40 CPU-seconds per piece and 0.55 CPU-hours per 50,000, read from the first piece alone.* |

## 3. Its outside sources, spot-checked

Thirteen of its 32 sources were opened here: eight of the owner's report's (the three it flags and five it says hold) and five of the mechanism sources.

**The owner's report's sources.**

| Report source | Reply's verdict | What was found | Agrees? |
|---|---|---|---|
| 6, cited for "experiments on cortical pyramidal neurons ... sensitivity to the order and speed of synaptic activation" | does not hold: the number points at Brette and Gerstner's 2005 AdEx model | PubMed 16014787 is "Adaptive exponential integrate-and-fire model as an effective description of neuronal activity" (Brette and Gerstner, J Neurophysiol 94:3637-42, 2005; doi:10.1152/jn.00686.2005): a model paper, no dendritic sequence experiment. The report's title for it ("Dendritic sensitivity to temporal input sequences") belongs to its source 7. | **yes** |
| 3, labelled "Dendritic computation review" | holds in part: a primary experimental article, not a review | PubMed 15156147 is Polsky, Mel and Schiller 2004, "Computational subunits in thin dendrites of pyramidal cells" (Nat Neurosci 7:621-7; doi:10.1038/nn1253), type "Journal Article": confocal imaging and focal stimulation in rat neocortex; nearby inputs on one branch summed sigmoidally. It supports the report's nonlinear-subunit claim; the label is wrong. | **yes** |
| 11, cited (with 12) for "event driven simulation can save work when activity is sparse" | holds in part: supports the clock/event distinction and its limits, not the sparse-activity saving | The Brian page ("How Brian works", stable) says an event-driven method "can be more accurate than a clock-driven simulation, but it is usually substantially more computationally expensive (especially for larger networks)". It does not support the saving; it says the opposite as a general rule. | **yes**; if anything the reply is generous ("in part" could be "does not support the saving") |
| 1, "20 response behaviours using a compact model with different parameter settings" | holds | Izhikevich 2004 (IEEE Trans Neural Networks 15(5), opened as PDF): "In Fig. 1, we review 20 of the most prominent features"; the caption: "simulations of the same model (1) and (2), with different choices" of parameters. | **yes** |
| 2, a two-layer network for a pyramidal neuron | holds | PubMed 12670427, Poirazi, Brannon and Mel 2003 (Neuron 37:989-99; doi:10.1016/s0896-6273(03)00149-1): a CA1 compartmental model whose firing rate is predicted by a two-layer "neural network"; the abstract supports the report's sentence. | **yes** |
| 4, "five to eight layers" for a simulated cortical neuron | holds | PubMed 34380016, Beniaguev, Segev and London 2021 (Neuron 109:2727-2739.e3; doi:10.1016/j.neuron.2021.07.002): "A temporally convolutional DNN with five to eight layers was required" for a layer-5 pyramidal cell model. | **yes** |
| 13, SpiNNaker, -30, 0 and +30 microseconds | holds | Lagorce et al. 2015 (Front Neurosci 9:206), section 4.3: ITDs "-30 [phase (1)], 0 [phase (2)] and 30 µs [phase (3)]", spikes jittered "between -5 and 5 µs". | **yes** |
| 18, a 2024 PRL spiking flip-flop in a resonant tunnelling diode neuron | holds | The publisher refused the fetch (HTTP 403); a web search gave the abstract and record: Donati et al., Phys Rev Lett 133, 267301, published 24 December 2024, "a spiking flip-flop memory mechanism that allows controllably switching between neural-like excitable spike-firing and quiescent dynamics". That pulse **timing** decides the switching (the reply's "switching depends on pulse timing") was not seen in the abstract: unverified here. | **yes**, the timing detail unverified |

**The mechanism sources.**

| Source | Reply's use | What was found | Agrees? |
|---|---|---|---|
| 31, Chow, Wilke, Ofria, Lenski and Adami 2004 (Science 305:84-86) | Avida pay for logic functions depends on resources consumed; inflow, outflow, consumption | Opened (author copy, p. 84): reward for a logic function "declines with consumption of the reward by other organisms"; "Resources flow into the reactor at a constant rate, and they flow out in proportion to their abundance." | **yes** |
| 25, Schultz, Dayan and Montague 1997 (Science 275:1593-1599) | TD error, p. 1595, Eq. 3: reward plus discounted next value minus present value | Opened (author copy): equation (3) is δ(t) = r(t) + γV̂(t+1) − V̂(t). | **yes** |
| 27, Turrigiano et al. 1998 (Nature 391:892-896) | compensation for sustained activity changes, roughly multiplicative scaling, Figs. 1-4 | Opened: TTX and bicuculline experiments; Figure 4 caption, "Activity scales mEPSC amplitudes multiplicatively". | **yes** |
| 30, Oudeyer, Kaplan and Hafner 2007 (IEEE Trans Evol Comput 11:265-286) | Intelligent Adaptive Curiosity allocates by learning progress, not raw error | Opened (author PDF): the robot "maximizes its learning progress"; learning progress evaluated "by measuring the decrease of the error". | **yes** |
| 32, Thompson and Spencer 1966 (Psychol Rev 73:16-43) | habituation: decrement with repetition, recovery after a pause; excludes receptor adaptation and fatigue | Opened: habituation as "response decrement as a result of repeated stimulation"; spontaneous recovery used as the criterion; decrements from very rapid stimulation, trauma and the like "best excluded". | **yes** |

**So**: of 13 sources opened, the reply's account holds for all 13, its three flags on the owner's report included; one detail (timing in source 18) could not be seen.

**For the owner's report, in sum**: of the eight report sources opened here, five hold as cited (1, 2, 4, 13, 18), one holds with a wrong label (3, an experiment, not a review), one is the wrong article (6; the report's claim rests on source 7 alone, which the reply opened and says holds), and one does not support the sentence it is cited for (11, the sparse-activity saving; source 12 is cited with it and was not opened here). None of these changes the report's main line (timing adds no class of computation that logic with memory lacks; the gain, if any, is in cost and representation), which rests on source 5 (sequential logic), checked by replies 01, 03 and 04 alike.

## 4. The grades against the brief's definitions

Every mechanism is graded "2 / 1": a rule written down (grade 2) acting on named task checks (grade 1). That is the brief's own scale used strictly: a trace's decay, a gate's threshold, a critic's declared return, a homeostatic set point and a learning-progress window are all written in advance. The reply also says, correctly, that moving the target into an outer search (evolutionary robotics) does not make it unnamed. No grade 3 claim is made. Agrees with S120's reading of the earlier research reply (03 to S119) and with replies 01 and 04 here.

## 5. What it adds to the owner's question

- **The precedent that matters most is already in Avida**: resources that run down and refill are a decaying trace with adaptation built into the world, pay falling as a capability becomes common and recovering when it fades. S113's COMMON TASKS PAY LESS and S118's P1 already ran it (8 to 17 common tasks at 50,000; 12 to 21 at 20,000). A temporal selector of reply 01's kind is, in its adaptation unit, a slower, between-pieces version of this.
- **Reward prediction error is signed, not "unusualness"**: a selector paying large absolute surprise implements surprise-seeking, not TD learning. This bears directly on reply 01's expectation unit, which pays the absolute forecast error (see `01 Check ...`, section 4).
- **The distinction a temporal selector must pass**: identical present, different histories, different responses; and a timer or a stored count may do the same job. Reply 04 turns this into its experiment.
- **Learning progress can be manufactured** by reload undercounts, forgetting and relearning, or moving probes. Reply 01's runner avoids the first (it reads an assay, not the live count).

## 6. Strengths and weaknesses

- **Strengths**: every source marked checked with its access route; the three flags on the owner's report are right; grades used strictly; costs stated as estimates; the restart problem carried into every design.
- **Weaknesses**: no Avida code was read, so its one Avida-specific claim about restarts (claim 2) misses that the record's own runner already carries resource levels; costs are in lines of code and an unmeasured CPU rate; the mechanisms are listed side by side rather than tied to the gaps S117 found (reply 04 does that).

## 7. Runs it proposes, with costs

All "options for Claude", none chosen: a replay check of a frozen selector on saved summaries (0 Avida CPU-hours); a short causal pilot (one mechanism, four arms, three seeds, 10,000 updates: 2.4 CPU-hours); a longer comparison (12 runs of 50,000: 12 CPU-hours); a restart-contribution comparison (6 CPU-hours); an outer search over controllers (for example 12 CPU-hours before held-out tests). At the rate measured in the whole S122 pilot (about 0.9 CPU-hours per 50,000 updates from the ancestor, more once programs are longer), these estimates are about right (corrected after the pilot finished; first committed as "about 0.55 ... upper estimates", from the first piece alone). They are carried into the plan (`00 What the three replies offer, and a plan of runs.md`) where they serve the owner's question; anything over about 3 CPU-hours needs the owner's word.
