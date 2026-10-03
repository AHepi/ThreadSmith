# Summary for the owner

Suppose a population can perform NOT at one save, then EQU at the next, but has lost NOT. Its “ever performed” counter rises to two; its current repertoire remains one. That example is hypothetical. It shows why new appearances and retained capabilities need separate measurements.

This report supplies checked references, measurement procedures and a mapping to your six environments and four proposals. No Avida experiment was run here, and the supplied experimental results were not independently measured.

The immediate analysis can use saved instruction sequences and their abundance. Re-run them under one unchanged test environment, then record first appearances, losses, returns and the capabilities present together. **Checked:** stock Avida supports these operations, followed by external calculation, with qualifications below.

Two measurements need more information. Historical instruction use cannot be reconstructed by executing a saved program today. The published MODES ancestry filter needs records showing which sampled programs leave descendants; seeing the same sequence again is insufficient. **Checked:** these requirements come from the activity-statistics and MODES methods described below.

**Project inference:** the growing list can reveal acquisition within a prepared catalogue. Resource depletion can reveal interactions that maintain different capabilities. Neither observation alone answers whether the environment keeps generating opportunities for new learning. The report specifies observations that would count against those interpretations.

# The works

“Checked” means the reference or claim was checked against the linked source, not that its conclusions were independently reproduced. “Proposed” and “inference” identify this report’s procedures and deductions. No substantive claim below relies only on memory. Source-access limits appear in the final section.

## Shared procedures for these runs

**Proposed procedure P — fixed capability assay.** Preserve original saves and configurations. Index files by environment, seed, piece and absolute update; retain update 0 if available. Parse each save’s column declarations. Keep positive-abundance rows for population measurements and an unfiltered copy for ancestry. Identify a sequence by its complete instruction string plus instruction-set definition, checking equality rather than relying only on a hash. Keep numeric IDs separately for ancestry.

Create one reference environment containing exactly the supplied 77 tasks, each with `process:value=0:type=pow requisite:max_count=1`, no resource dependencies and no special input overrides. Preserve the name-to-task-index mapping. Fix instruction meanings, test-CPU limits and division conditions. For each snapshot, run stock analysis commands `PURGE_BATCH`, `LOAD <snapshot>`, `FILTER num_cpus > 0`, and `RECALCULATE 0 -1 0`. Export `id sequence num_cpus viable length` and every column from `task.0:binary` through `task.76:binary` using `DETAIL <output> <columns>`. Expand all 77 columns explicitly.

**Checked source:** [Avida commit 47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16), `cAnalyze.cc`, `cAnalyzeGenotype.cc/.h` and `cEnvironment.cc`. The loader aliases `num_units` to `num_cpus`; recalculation preserves abundance. Task marking precedes reward processing, so zero exponent does not suppress task detection. These are source checks, not runtime tests. P is a canonical-input assay, not performance on every possible input stream. Freeze a separate panel of legal input triples before testing generalisation.

**Proposed calculations from P.** Let n(g,k) be saved abundance, N(k) its sum, and b(g,j)=1 when the fixed assay detects task j. Calculate prevalence p(k,j)=Σg n(g,k)b(g,j)/N(k). Also report the matrix requiring viable replication; do not silently remove nonviable programs from its denominator. Define T(k) as tasks with positive prevalence. Report current coverage, first sampled tasks absent from every earlier T, losses since the previous sample, and returns previously seen but absent at the preceding sample. Repeat at prevalence 0.10, explicitly identifying that threshold convention.

Retention from sample a to k is |T(a)∩T(k)|/|T(a)|; an empty denominator is unavailable. This is endpoint population retention and includes reacquisition; continuous sampled retention instead intersects every T from a through k. Neither measures retention by one descendant. If initial history is missing, novelty means first recorded since the first available sample. Aggregate abundance by the entire 77-bit profile, including the all-zero profile. For profile frequencies q(v), calculate H=−Σv q(v)log₂q(v). Individual task prevalences overlap and cannot substitute for q(v).

**Proposed procedure K — fitness-sensitive instructions.** Use a separate fixed reference assay: the nine supplied graded rewards, the other 68 tasks at zero reward, no limiting resources, and unchanged inputs/restrictions. Load and filter current rows as in P, run `RECALCULATE 0 -1 0`, then `FILTER viable == 1` and `ANALYZE_KNOCKOUTS <unique-output> 1`. Sum the lethal and detrimental single-ablation columns per sequence; report the maximum, abundance-weighted mean and distribution at each snapshot. Cache identical sequences under the identical configuration. **Checked source:** `cAnalyze.cc`, `AnalyzeKnockouts`, replaces each instruction with the internal null and restores it before the next test. A deletion or ordinary modifier `nop` is not this operation. K measures dependence under one reference reward rule, not resource-dependent success in the live population. Keep task-loss ablations separate. Single-site tests miss redundancy and interactions; fragile implementations can have many sensitive sites without additional capabilities.

## Bedau and Packard — inherited use

**Checked reference:** Mark A. Bedau and Norman H. Packard (1991), “Measurement of Evolutionary Activity, Teleology, and Life.” In C. G. Langton, C. Taylor, J. D. Farmer and S. Rasmussen, eds., *Artificial Life II*, SFI Studies in the Sciences of Complexity X, Addison-Wesley, 431–461. [Author bibliography](https://people.reed.edu/~mab/papers/alife2.ab.htm); [manuscript, §§3–4](https://people.reed.edu/~mab/publications/papers/alife2.pdf). The bibliography says 1991; this manuscript’s header says 1992.

**Checked:** Their example increments a rule’s use counter when executed, carries its history through replication, and resets the changed rule’s counter following modification. Its activity distribution concerns inherited use, not merely different programs.

**Proposed mapping and stock sufficiency:** Increment a counter attached to each inherited instruction when executed; transfer identity and count during copying, resetting changed or inserted instructions; archive the distribution at every save. Normalize the counter histogram H(u) across current instruction copies; form tail R(u)=Σv≥u H(v). At a declared integer usage threshold u₀, report R(u₀)−R(u₀+1), the discrete tail-slope reading, alongside sensitivity to u₀. This needs execution and instruction-inheritance instrumentation absent from the stated saves. Stock re-execution supplies present traces, not historical counters. Replication code or idle loops could accumulate use without additional task capability; pair this measure with P.

## Bedau, Snyder and Packard — classes of dynamics

**Checked reference:** Mark A. Bedau, Emile Snyder and Norman H. Packard (1998), “A Classification of Long-Term Evolutionary Dynamics.” In C. Adami, R. K. Belew, H. Kitano and C. E. Taylor, eds., *Artificial Life VI*, MIT Press, 228–237. [Author manuscript, equations 1–8 and classification](https://people.reed.edu/~mab/publications/papers/alife6.pdf).

**Checked:** Diversity, mean cumulative activity and new activity describe distinct long-run patterns. A random-selection shadow supplies a comparison for interpreting adaptive activity. Original Class 1 has no adaptive activity; Class 2 has positive new activity with bounded diversity/mean activity; Class 3 has positive new activity with unbounded diversity. Later work extends Class 3.

**Proposed sampled adaptation:** For sequence presence I(g,k), retain s(g,k)=Σh≤k I(g,h), then report a(g,k)=I(g,k)s(g,k), diversity D(k)=Σg I(g,k), total activity, and mean/median among present sequences. In snapshot units, raw new activity is the sum of a(g,k) within a chosen window [a₀,a₁], divided by D(k). For the paper’s calibration, collapse real/shadow activity distributions over time: center the window on their lowest crossing a*, with half-width 0.05(a_max−a*); a_max is the largest observed activity. If no crossing exists, report calibration unavailable. Empty populations have unavailable averages.

Sequences and abundances suffice for raw sampled statistics, but not the shadow or continuous lifetimes. Multiplying by 1,000 does not recover missed appearances. No-task-reward runs still select for replication and are not random-selection shadows. A finite trace cannot determine an asymptotic class.

## Channon — Geb and component-normalised activity

**Checked reference:** Alastair Channon (2006), “Unbounded Evolutionary Dynamics in a System of Agents that Actively Process and Transform Their Environment.” *Genetic Programming and Evolvable Machines* 7, 253–281. [DOI 10.1007/s10710-006-9009-3](https://doi.org/10.1007/s10710-006-9009-3). Earlier application: Channon (2001), “Passing the ALife Test: Activity Statistics Classify Evolution in Geb as Unbounded,” *Advances in Artificial Life*, LNCS 2159, 417–426, [DOI 10.1007/3-540-44811-X_45](https://doi.org/10.1007/3-540-44811-X_45).

**Checked:** The later Geb work addresses divergence between the studied population and its shadow through component normalization. Median activity guards against a few persistent components dominating the mean. Components are developmental-rule parts, not Avida instruction sequences.

**Checked methodological precursor:** Alastair Channon (2003), “Improving and Still Passing the ALife Test: Component-Normalised Activity Statistics Classify Evolution in Geb as Unbounded,” in R. K. Standish, M. A. Bedau and H. A. Abbass, eds., *Artificial Life VIII*, MIT Press, 173–181. [Author-uploaded text, equations 9–15](https://www.researchgate.net/publication/228871296_Improving_and_still_passing_the_ALife_test_Component-normalised_activity_statistics_classify_evolution_in_Geb_as_unbounded).

**Proposed mapping:** Start a matched shadow from each real sample; randomize selection choices while preserving specified replication, change and deletion event rules. At the next sample, accumulate real-minus-shadow presence per component, then reset the shadow to the real state. Keep cumulative differences through absence, but absent components contribute zero to current totals. Following the paper’s symmetry assumption, set the threshold to the magnitude of the most negative normalized activity observed over the run. Count each component once at its first crossing; normalized new activity is their summed normalized activity divided by current real diversity. The threshold cannot be calculated from these saves alone.

Calculate the median over components present in the real sample. Stock saves lack this counterfactual history. A shadow needs an explicit additional simulator or instrumentation; switching off task rewards does not implement it. Sequence normalization also does not imply new behavior: use P alongside it.

## Taylor and colleagues — York perspectives

**Checked reference:** Tim Taylor, Mark Bedau, Alastair Channon, David Ackley, Wolfgang Banzhaf, Guillaume Beslon, Emily Dolson, Tom Froese, Simon Hickinbotham, Takashi Ikegami, Barry McMullin, Norman Packard, Steen Rasmussen, Nathaniel Virgo, Eran Agmon, Edward Clark, Simon McGregor, Charles Ofria, Glen Ropella, Lee Spector, Kenneth O. Stanley, Adam Stanton, Christopher Timperley, Anya Vostinar and Michael Wiser (2016). “Open-Ended Evolution: Perspectives from the OEE Workshop in York.” *Artificial Life* 22(3), 408–423. [DOI 10.1162/ARTL_a_00210](https://doi.org/10.1162/ARTL_a_00210); [text, §3](https://www.tim-taylor.com/papers/taylor2016openended.pdf).

**Checked:** This synthesis separates observable hallmarks from proposed mechanisms and discusses several forms of open-endedness. It supplies no single new snapshot statistic.

**Proposed mapping:** Apply P and K as separate trajectories for acquisition, retention and instruction dependence; add actual interaction records where available. Stock re-evaluation supports the first three, not unrecorded interactions. Increasing “ever seen” coverage with declining retained coverage counts against accumulation as defined here. A rising curve over 50 pieces does not settle unlimited continuation.

## Packard and colleagues — overview

**Checked reference:** Norman Packard, Mark A. Bedau, Alastair Channon, Takashi Ikegami, Steen Rasmussen, Kenneth O. Stanley and Tim Taylor (2019). “An Overview of Open-Ended Evolution: Editorial Introduction to the Open-Ended Evolution II Special Issue.” *Artificial Life* 25(2), 93–103. [DOI 10.1162/artl_a_00291](https://doi.org/10.1162/artl_a_00291); [text, §§2–3](https://arxiv.org/pdf/1909.04430).

**Checked:** Its provisional categories concern new entities/interactions, evolvability, major transitions and semantic evolution. These organize questions rather than supply four numerical measurements.

**Proposed mapping:** Use P for capability change. For each claimed new interaction, retain participating sequences, the environment and an intervention removing that interaction. For evolvability, compare descendants’ capability production under one frozen variation-and-test protocol. These need additional assays; P alone cannot answer them. Assigned groups in B2/B3/C are not automatically evolved units of replication; an experimenter’s `nand`→`nor` substitution is not itself evolving semantics.

## Dolson and colleagues — MODES

**Checked reference:** Emily L. Dolson, Anya E. Vostinar, Michael J. Wiser and Charles Ofria (2019). “The MODES Toolbox: Measurements of Open-Ended Dynamics in Evolving Systems.” *Artificial Life* 25(1), 50–73. [DOI 10.1162/artl_a_00280](https://doi.org/10.1162/artl_a_00280); [text, §§3–5](https://cse.msu.edu/~dolsonem/pdfs/modes_paper.pdf).

**Checked:** Their persistence filter retains sampled programs having descendants a chosen number of generations later. For retained component set F(k), change is |F(k)∖F(k−1)|, novelty is |F(k)∖∪h<k F(h)|, complexity is maximum informative-site count, and ecology is component-frequency Shannon entropy. Their Avida experiments used modified instrumentation; null-site ablations approximate informative sites. Persistence leaves some neutral change.

**Proposed mapping:** Declare full sequences as components and K as reference-fitness complexity. If individual ancestry exists, filter sampled copies and aggregate their frequencies at sampling time k, not descendant abundance. Timestamp results at k despite the reporting delay. Take the complexity maximum only over retained components. Freeze the generation lag before comparisons; retain generation coordinates across reloads, since generations are not updates or pieces. Samples lacking the required future record are censored, not zero. Without ancestry, report P’s unfiltered analogues. Full-sequence components can retain neutral differences; K with nine rewarded tasks is not a measure of all 77 capabilities. K needs new stock assays. Earlier endpoint task-loss ablations cannot substitute for fitness-loss ablations. Additional source and ancestry cautions appear below.

## Soros and Stanley — minimal conditions

**Checked reference:** L. B. Soros and Kenneth O. Stanley (2014). “Identifying Necessary Conditions for Open-Ended Evolution through the Artificial Life World of Chromaria.” *Artificial Life 14: Proceedings of the Fourteenth International Conference on the Synthesis and Simulation of Living Systems*, MIT Press, 793–800. [Institutional record](https://stars.library.ucf.edu/scopus2010/9117/). This corrects the brief’s shorthand title.

**Checked:** The proposed conditions concern a nontrivial replication criterion, newly created opportunities, program-directed interaction, and in-principle unbounded possible phenotype size and complexity. The 2014 experiment removes opportunity creation by preventing agents from sensing each other; it does not independently test all four conditions.

**Proposed mapping:** For growing list, join P to each reward activation and its triggering prevalence. Count tasks first detected before versus after activation. For depletion, join consumption/resource levels to task prevalence and test frequency dependence below. Snapshots supply capability timing only; controller/resource logs or additional runs supply causal tests. B2/B3 need serialized generated problems. Unlocking a listed task activates a prepared opportunity; it does not create a task definition.

## Stanley, Lehman and Soros — the 2017 essay

**Checked reference:** Kenneth O. Stanley, Joel Lehman and Lisa Soros (19 December 2017). “Open-endedness: The last grand challenge you’ve never heard of.” *O’Reilly Radar*. [Publisher text](https://www.oreilly.com/radar/open-endedness-the-last-grand-challenge-youve-never-heard-of/). This is a web essay; no DOI is displayed.

**Checked:** It discusses creating challenges as well as solving them and presents proposed conditions as revisable. It supplies no independent numerical measure.

**Proposed mapping:** Keep distinct columns for new sequences, new task profiles, changed rewards, changed problem definitions and changed evaluator rules. Populate the first two from P, the others from configuration/controller archives. Stock snapshots alone cannot populate all columns. B1 can keep moving while one skill suffices; B2/B3 may generate easy variants; C may change preferences without adding capability. No “essay score” is warranted.

## Banzhaf and colleagues — variation, innovation and emergence

**Checked reference:** Wolfgang Banzhaf, Bert Baumgaertner, Guillaume Beslon, René Doursat, James A. Foster, Barry McMullin, Vinicius Veloso de Melo, Thomas Miconi, Lee Spector, Susan Stepney and Roger White (2016). “Defining and simulating open-ended novelty: requirements, guidelines, and challenges.” *Theory in Biosciences* 135, 131–161. [DOI 10.1007/s12064-016-0229-7](https://doi.org/10.1007/s12064-016-0229-7); [text, pp.141–143, 152](https://www.cs.mun.ca/~banzhaf/papers/OEE_2016.pdf).

**Checked:** Variation changes a model’s values; innovation changes its types or relationships; emergence changes its descriptive framework. Classification is model-relative. The discussion permits innovation in Avida-like executing-program systems.

**Proposed mapping:** Freeze the descriptive model, then annotate candidate events with the variable, type, relationship or framework change needed to describe them. Within a model of 77 capability flags, acquiring a listed task changes a value. P detects that; broader classifications need traces and interaction evidence. Label reward additions as controller events. The 77-bit projection cannot diagnose everything the machine can do. An observer’s changed vocabulary alone does not identify new organization in the population.

## Lenski and colleagues — complex capabilities in Avida

**Checked reference:** Richard E. Lenski, Charles Ofria, Robert T. Pennock and Christoph Adami (2003). “The evolutionary origin of complex features.” *Nature* 423, 139–144. [DOI 10.1038/nature01568](https://doi.org/10.1038/nature01568).

**Checked, authors’ report:** Rewarded simpler functions supplied routes to complex functions, without any one intermediate being indispensable. Historical changes and functional assays connect earlier sequences to the first complex-capability performer.

**Proposed mapping:** Use P to locate the first saved EQU-performing sequence. Follow its recorded ancestry, re-assay available ancestors, and tabulate task gains/losses. Ablate or revert candidate instructions under unchanged conditions. Stock analysis can test supplied ancestral sequences; missing ancestors cannot be reconstructed from endpoints. First sampled detection need not bracket the original acquisition: an earlier appearance could have been lost between saves. Event logs or complete ancestry are needed to locate that origin. Reuse requires an inherited functional contribution, not merely similar code. This bears on graded, EQU-only, growing-list and large-list runs, and B2/B3 transfer claims.

## Chow and colleagues — depletable resources

**Checked reference:** Stephanie S. Chow, Claus O. Wilke, Charles Ofria, Richard E. Lenski and Christoph Adami (2004). “Adaptive Radiation from Resource Competition in Digital Organisms.” *Science* 305(5680), 84–86. [DOI 10.1126/science.1096307](https://doi.org/10.1126/science.1096307); [author text](https://cse.msu.edu/~ofria/pubs/2004ChowEtAl.pdf).

**Checked, authors’ report:** Nine separately depleted/replenished task resources supported persistent groups and invasion when rare under some supply regimes. Ancestry-defined group richness approached a plateau. Its clustering statistic is not a sequence count.

**Proposed mapping:** P supplies a separately labelled profile-diversity adaptation. For frequency dependence, choose two archived profiles and representative sequences, set `COPY_MUT_PROB`, `DIVIDE_INS_PROB` and `DIVIDE_DEL_PROB` to zero, keep every other change rate zero, and compete them starting one group at 1%, 10%, 50%, 90% and 99%. Fix resource initialization, inflow/outflow and sampling times; repeat placements. Record frequency change. Growth when rare and decline when common would support that pairwise restoring mechanism. A negative result does not exclude community-dependent feedback; that test must preserve surrounding groups and control resource transients. These are new stock-configured runs. Reproducing the original clustering additionally needs ancestry and the supplementary algorithm, not inspected here.

## Walker and Ofria — diversity and capability acquisition

**Checked reference:** Bess L. Walker and Charles Ofria (2012). “Evolutionary Potential is Maximized at Intermediate Diversity Levels.” *Artificial Life 13: Proceedings of the Thirteenth International Conference on the Synthesis and Simulation of Living Systems*, MIT Press, 116–120. [DOI 10.7551/978-0-262-31050-5-ch017](https://doi.org/10.7551/978-0-262-31050-5-ch017); [author text, methods and Table 3](https://cse.msu.edu/~ofria/pubs/2012WalkerOfria.pdf).

**Checked, authors’ report:** They measure task-profile Shannon diversity and endpoint EQU occurrence. Among tested supplies, diversity peaked at inflow 10, whereas EQU occurrence peaked at 100 resource units per resource per update.

**Proposed mapping:** Compute P’s profile entropy for nine tasks and separately for 77. For an analogue of its viable-program diversity, filter viable programs and renormalize abundances. Retain all-program entropy separately. Use base 2 here and report bits; the paper’s logarithm base was not located. Report endpoint capability presence per seed beside diversity, first appearance and losses. Sequences, abundance and stock re-evaluation suffice for this standardized adaptation. Marginal task totals do not. The assay need not reproduce performances during the live run, and profile diversity need not mean increasingly complex capabilities.

## Stout and Spector — an activity-statistics countercase

**Checked reference:** Andrew Stout and Lee Spector (2005). “Validation of Evolutionary Activity Metrics for Long-Term Evolutionary Dynamics.” *GECCO ’05*, ACM, 137–142. [Author text, §3.2](https://faculty.hampshire.edu/lspector/pubs/Evolutionary_Activity.pdf).

**Checked, authors’ report:** Positive normalized new activity arose largely from neutral sequence changes in a static-fitness example. Changing the target produced alternating novelty and persistence without ongoing accumulation in that example.

**Proposed mapping:** Place sequence activity beside P’s task/profile novelty and retention. Changing sequences with unchanged profiles count as sequence turnover. Profiles alternating after their first appearances count as recurrence. Stock re-evaluation plus external aggregation supports this comparison; normalized activity still needs a shadow. This bears on B1 and interpretations of growing/depleting environments. These countercases do not predict that every changing environment must cycle.

## Wang and colleagues — POET

**Checked reference:** Rui Wang, Joel Lehman, Jeff Clune and Kenneth O. Stanley (2019). “POET: Open-Ended Coevolution of Environments and their Optimized Solutions.” *GECCO ’19*, ACM, 142–151. [DOI 10.1145/3321707.3321799](https://doi.org/10.1145/3321707.3321799); [conference text, §§4–5](https://www.cmap.polytechnique.fr/~nikolaus.hansen/proceedings/2019/GECCO/proceedings/proceedings_files/pap355s3-file1.pdf).

**Checked, authors’ report:** POET generates obstacle courses alongside controllers and transfers solutions between courses. Some generated-and-solved targets were not reached by direct-path curriculum controls within tested budgets. Coverage uses distances from sampled courses to generated-and-solved courses.

**Proposed mapping:** Terrain distance has no supplied Boolean-task equivalent; use P’s explicitly different catalogue coverage. For B2/B3, archive each generated function/graph and evaluate every saved solver population against the same archived problems, recording first solutions and later retention. Those measures require the proposed evaluators and archive; existing stock saves cannot supply them. Problem size can rise while one strategy suffices. The paper does not test an evolving chooser population like C.

## Wang and colleagues — Enhanced POET and ANNECS

**Checked reference:** Rui Wang, Joel Lehman, Aditya Rawal, Jiale Zhi, Yulun Li, Jeffrey Clune and Kenneth Stanley (2020). “Enhanced POET: Open-ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions.” *ICML*, PMLR 119, 9940–9951. [Publisher record and text](https://proceedings.mlr.press/v119/wang20l.html).

**Checked:** ANNECS accumulates environments that, when created, satisfy a neither-too-easy-nor-too-hard criterion against all agents generated so far, active and archived, and are eventually solved. It separates admitting a challenge from solving it.

**Proposed mapping:** For B2/B3, freeze scoring, admission and solution thresholds; archive generated problems and every agent needed for the historical test. Mark eligibility at creation and increment once upon eventual solution. Record later loss separately. Additional evaluators/logging are required. Ordinary 77-task presence is not literal ANNECS: it lacks the specified graded challenge test. Repeated easy instances and a narrow generator can inflate an adapted count; canonicalize equivalent instances and retain fixed external probes.

# Which measure bears on which environment or proposal

**Project mapping, not additional source claims.** F = fixed graded; E = EQU only; N = no task rewards; G = growing list; D = common tasks pay less; L = fixed large list. Results remain per-seed trajectories.

| Measure or framework | Six environments | Earlier proposals | Contrast examined |
|---|---|---|---|
| Inherited use; sampled and shadow-normalized activity | F, E, N, G, D, L | B1, B2, B3, C with required history | Use/persistence versus turnover, not necessarily new capability |
| P: acquisition, loss, return, retention | F, E, N, G, D, L | B1 archived targets; B2 functions; B3 graphs; C external assessment | Accumulation versus forgetting or moving evaluation |
| MODES change and novelty | F, E, N, G, D, L after ancestry audit | B1–B3 and C, separately by role | New retained components versus recurrence |
| K and MODES complexity | F, E, N, G, D, L | B1–B3; distinguish C’s choosers and candidates | Fitness-sensitive instructions versus task count or sequence length |
| Profile entropy; MODES ecology | F, E, N, G, D, L; D adds resource feedback | B2/B3 roles; C chooser/candidate distributions | Coexisting capabilities versus sequence diversity |
| Resource-frequency intervention | D; other environments as specified controls | Proposals claiming frequency feedback | Restoring effect versus transient mixture |
| Ancestry and reuse assays | F, E, N, G, D, L | B2/B3 transfer; B1 retained methods | Inherited contribution versus rediscovery |
| Soros conditions; POET coverage; ANNECS | G prepared curriculum; D opportunities; F/E/N/L contrasts | B2/B3 generated challenges; B1 target novelty; C independent criteria | Created and solved challenges versus schedule changes |
| Taylor/Packard/Banzhaf frameworks | All six, with declared models | All four proposals | Hallmarks versus mechanism, model change or evaluator drift |

**Proposed additions to earlier measures:** preserve the retention matrix; distinguish probes never rewarded anywhere from tasks merely unrewarded so far; require ancestral functional tests for reuse. For C, archive chooser versions and decisions, then assess chosen candidates against fixed problems independently of chooser preference. Chooser persistence is not chooser accuracy.

# What the literature already reports about growing and depleting environments

**Checked:** Lenski and colleagues report routes to complex logic functions through rewarded intermediates. POET reports generated curricula and transfers. Neither tests this exact 77-task, 10%-threshold growing list. The former uses supplied functions; the latter generates courses within an encoded domain.

**Project inference:** G measures progression through prepared reward levels. Log level and actual capability separately. A level increase without subsequent retained capability gain counts against interpreting level count as learning. Replay a recorded schedule on another run to remove dependence on that run’s population while retaining changing rewards. This control is proposed, not run here.

**Checked:** Chow reports coexistence and richness approaching a plateau. Walker and Ofria report different supplies for peak diversity and peak EQU occurrence after 100,000 updates. Their depletion setting adds difficulty-scaled rewards absent from Chow’s setting; neither result is a parameter-free prediction for D. In MODES’s NK fitness-sharing treatment, change and ecological diversity rose without increased final novelty; the authors suggest recurrence. That treatment is not Avida resource depletion.

**Project inference:** D can maintain or cycle among capabilities without expanding its repertoire. Plot first appearances and retention beside entropy, consumption and resources. Restoring resources at every reload could interrupt this feedback; use the separate restart investigation before attributing patterns solely to depletion.

# Works searched for and not found

All nine requested topics were located. The Soros–Stanley item has the corrected title above; the 2017 item is an essay. **Checked bibliographic gap:** no DOI was located for the cited Bedau chapters or O’Reilly essay; stable source links are supplied.

No published experiment matching the exact growing-list rule was located in searches combining Avida with “77 tasks,” “growing tasks,” “curriculum,” “progressive tasks,” and NAND complexity. No source was located reporting B2, B3 or C implemented in this project’s specified commit. These are search outcomes, not claims of nonexistence. This is a targeted survey, not an exhaustive census through September 2026.

# Assumptions and what you are unsure of

The frozen question is which observations distinguish capability acquisition and retention from churn in these runs. Reference checking, exact procedures and the environment mapping are **given** jobs. The supplied run design is **fixed**. Neutral churn, reward-only changes and restart artifacts are **added** discrimination cases. The owner’s constructor-theory interpretation is outside this test; these operational measurements do not automatically settle that interpretation of knowledge.

| Part tested with the hard-to-vary method | Mark and consequence |
|---|---|
| Sequence identity as capability novelty | **Loose:** neutral instruction changes alter sequence novelty without changing the target capability |
| Stable identity and fixed assay | **Held for this comparison:** renumbering reload IDs or changing rewards must not manufacture a capability |
| Particular inputs and prevalence threshold | **Fixed:** measurement choices; alternate frozen panels/thresholds test sensitivity |
| Descendant persistence | **Unknown for these archives:** recurrence and descent can give identical snapshots; inspect genealogy and reload mappings |
| Environmental feedback causing accumulation | **Unknown:** positive or absent accumulation both fit “environment matters”; schedule replay and resource interventions separate narrower claims |
| Activity as adaptation | **Borrowed:** depends on component choice/filtering; Stout–Spector prevents treating new activity alone as new capability |

**Proposed reasoning checks:** profiles A→B→A accumulate change but stop adding first-seen profiles after B. An unchanged program can gain Avida fitness through a reward increase without gaining a task. A longer persistence filter can exclude short-lived useful branches while reducing transient churn. Keep both effects visible; do not choose its lag for the desired outcome. These are logical countercases or proposed tests, not measured results.

**Checked source correction:** `SavePopulation` at this commit defaults to including retained ancestral sequence groups. The old `SaveHistoricPopulation` name is not a registered action. Group ancestry is not individual genealogy. Reloads assign new group IDs; inspect headers, parents and cross-piece mappings before joining ancestry. Historical zero-abundance rows must not inflate current diversity. Cumulative `total_units` also restarts on reload. Relevant source: `SaveLoadActions.cc`, `cPopulation.cc`, `systematics/GenotypeArbiter.cc` and `Genotype.cc` in the linked commit.

**Checked source caution:** MODES-related commands are registered, but `COUNT_NEW_SIG_LINEAGES` hard-codes 4,200 updates and `GET_SKELETONS` has suspicious boundary handling during null removal. These are static findings, not reproduced failures. Registration does not supply a tested MODES pipeline. P/K avoid these wrappers; no source was changed.

Actual saves, controller/resource logs and input configuration were unavailable. The 18 running experiments’ results remain unknown here. Three seeds are three replicates; 50 snapshots are repeated observations within each. The catalogue caps named-task coverage at 77 and occupied-cell profile entropy at log₂(3,600) bits. These limits concern the measurements, not every possible virtual-machine behavior.

**Checked access limits:** source checks used the pinned checkout. Most methodological papers were read in relevant full-text sections; Lenski’s claim uses the publisher abstract, Soros 2014 uses its institutional record and indexed manuscript passages, and Channon uses publisher material plus accessible author text. Chow’s supplementary clustering algorithm was not inspected. DOI strings were checked where available; not every resolver opened. No population analysis, runtime test or continuation was performed here.

**Next action:** inventory one run’s actual saves and configurations, then execute P unchanged across its snapshots. Return the capability/retention matrix with the ancestry audit. This resolves which literature measurements the archives can carry before adding instrumentation.

END OF REPORT
