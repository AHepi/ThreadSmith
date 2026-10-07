Post-mortem: On September 18, our checkout service experienced a cascading failure caused by an unbounded retry loop in the payment-gateway client, which amplified a brief upstream latency spike into a 40-minute full outage affecting all regions.

The fix introduces a token-bucket rate limiter and exponential backoff with jitter on the payment-gateway client, capped at 3 retries, plus a circuit breaker that opens after 5 consecutive failures within a 10-second window. Before rollout, we reproduced the original incident in a staging environment by injecting the same upstream latency profile (p99 4.2s) via our fault-injection harness, and confirmed the old code reproduced the cascading failure while the new code degraded gracefully, shedding load and returning cached responses instead of retrying indefinitely.

We load-tested the new client at 3x peak historical traffic (that day's traffic plus the retry storm pattern) on a staging cluster matching production topology, and verified CPU, memory, and connection-pool metrics stayed within normal bounds. The change was rolled out via canary to 5% of traffic in each of our three regions for 48 hours, with automated rollback tied to error-rate and latency SLO alerts; no rollback triggered. We also ran the existing full payment integration test suite (212 tests) against the new client with no regressions, and verified the circuit breaker's half-open recovery behavior against a scripted upstream recovery scenario.

Full rollout completed October 2 with no recurrence.

Task: before this claim is accepted, what must be questioned or tested?
