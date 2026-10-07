# case_n3

Deployment review: Sentinel-4 fraud model, Meridian Card Services, card-not-present acquiring

Sentinel-4, a gradient-boosted sequence model, ran against the incumbent rules engine on randomized production traffic from 14 August to 9 October. Card-not-present transactions were split 45% to Sentinel-4, 45% to the incumbent, and 10% shadow-scored, with assignment by hashed customer ID so every customer's transactions stayed in one arm. Primary endpoints, fixed before unblinding, were fraud losses per $1,000 of processed volume and the false-decline rate on confirmed-legitimate transactions. Because chargebacks lag transactions, the analysis window was frozen only after every transaction in the period had 60 days of label maturation and pending disputes had been adjudicated. Sentinel-4 reduced fraud losses 23% (p < 0.01) while false declines rose 0.04 percentage points, inside the pre-registered non-inferiority margin of 0.10. False-decline rates were also checked per issuing region and for first-time customers; no subgroup breached the margin. Median scoring latency was 38 ms against a 50 ms budget. Fraud analysts blind to arm reviewed 400 randomly sampled alerts and judged 92% of Sentinel-4's review-worthy. Rollout began 20 October under a pre-agreed rollback trigger tied to either endpoint.

Task: before this claim is accepted, what must be questioned or tested?
