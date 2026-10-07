# Case 04: the cache causes the crash

From a bug post-mortem:

"Symptom: the export service crashes about once an hour under load. Hypothesis: a race in the new response cache. Test: we turned the cache off with the feature flag and ran the load test 20 times for an hour each. Zero crashes in 20 runs. With the cache on, the original incident report shows crashes. Root cause: the response cache. Fix: we will remove the cache."

Task: before this root cause is accepted, what must be questioned or tested?
