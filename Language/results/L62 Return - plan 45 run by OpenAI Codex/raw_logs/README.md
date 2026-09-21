# Raw-log preservation

Written by: OpenAI Codex

`historical/` contains byte-for-byte copies of the two whole raw logs supplied in the handoff before this execution. Their SHA-256 values are:

| File | SHA-256 |
| --- | --- |
| `historical/rig1_raw_log_before_plan45.txt` | `15191f84fd6c5b48d992b1c1a12caacb9e31832b29017e61057f67e3024edf7b` |
| `historical/rig2_raw_log_before_plan45.txt` | `3b10a69bda4856581681f71687aeba3dd44bc641a178f8a8f7168f5718a5cacf` |

New plan-45 runs did not append to those files. Each invocation instead has a fresh isolated `raw_log.txt` beside its exact report and receipt under `part_a/runs/` or `part_b/runs/`. This prevents historical/new boundaries from being inferred after the fact while still returning the supplied whole logs.

`aggregate/` also contains one reconstructed whole log per rig. Each is a header-free byte concatenation of the supplied historical whole log followed by the new isolated native logs in lexicographic relative-path order. `aggregate/AGGREGATION_ORDER.json` records every segment's path, byte range, size and SHA-256, together with the aggregate hash. These two files are conveniences for whole-rig review, not contemporaneous shared append logs; the isolated logs remain the primary new-run evidence.
