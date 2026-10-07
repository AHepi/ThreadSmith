# case_g2

Research note: momentum in liquid futures, 2013–2023

We backtested a 120-day breakout momentum system on a universe of 56 futures contracts (equity index, rates, energy, metals, ags), rebalanced weekly, 2013 through 2023. The system returned 11.4% annualised with a Sharpe ratio of 1.7 and a maximum drawdown of 9.2%. Trades were simulated at the settlement price, with commission of USD 1.20 per side per contract included. Among the lookbacks tested (60, 90, 120, 180 days), 120 days performed best across the full sample, and we adopt it for the live launch. After inspecting the 2020 drawdown we added a volatility filter that cuts exposure when 20-day realised volatility exceeds its 90th percentile; with the filter the Sharpe rises to 1.9. The universe was constructed from the 56 most liquid contracts currently listed. We believe the strategy is robust: it was profitable in 10 of 11 calendar years, and the equity curve shows no dependence on any single sector. Initial live capital of USD 250 million is proposed, which implies average positions of roughly 45 contracts per signal. Backtest code and data are available on request.

Task: before this claim is accepted, what must be questioned or tested?
