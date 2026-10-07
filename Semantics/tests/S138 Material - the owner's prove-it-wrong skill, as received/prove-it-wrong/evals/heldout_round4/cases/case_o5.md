# case_o5

Project SIGNAL — Version 4 report (adaptive traffic-signal control)

**Claim C4.1:** The v4 learned controller reduces mean vehicle delay by 11.8% (95% CI 9.9–13.6%) versus the tuned actuated-control baseline on the held-out evaluation set, within the simulation scope stated in the evaluation contract.

Setup. v4 replaces the v3 hand-built queue features with a learned state encoder trained jointly with the policy. All results come from microsimulation.

Evaluation contract (frozen 2026-05-02, before v4 training began): primary metric mean delay per vehicle; 20 held-out road networks generated from city templates not used in training; demand at 60%, 80%, 100% and 120% of design capacity; 10 independent simulator seeds per network × demand cell; baseline actuated control re-tuned by a separate team member for each network. No metric was changed after results were seen.

Results. The reduction holds at every demand level (smallest: 7.1% at 120%). It holds on 19 of 20 networks; the exception (a grid with very long blocks) shows −1.4%, within noise. Delay on unsignalised side streets and at the boundary intersections controlled by the baseline was tracked to check for queues pushed elsewhere: it changed by +0.6% (CI −0.8 to +2.0%). Stop counts and 95th-percentile pedestrian wait were also tracked; pedestrian wait rose 3% (within the contract's 5% tolerance). Ablation: v4 with the v3 features recovers only 3.2% of the gain, so the encoder accounts for most of the improvement. The evaluation harness was run by a team member who did not train v4.

Register of claims we cannot make: real-world deployment benefit; behaviour under sensor failure or detector noise beyond the simulated model; emergency-vehicle priority; demand above 120%.

Task: before this claim is accepted, what must be questioned or tested?
