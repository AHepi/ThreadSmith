# Foundation/PC1 Read-Only Acceptance Review

Review status: accepted on 2026-07-22 after one bounded repair cycle. The review was performed in fresh read-only contexts separate from implementation. Reviewers did not edit, format, stage, commit, push, install, or run the full suite.

## Initial review

| Severity | Finding | Disposition |
|---|---|---|
| P1 | The first reconstructed identity API could hash any supplied value while its names and successful manifest fixture implied artifact-specific preimage validation. | Repaired by narrowing names, documentation, vectors, and reports to non-authoritative already-resolved preimage claims. Successful manifest and blueprint artifact fixtures were removed; their PC1 preimages remain unresolved. |
| P1 | The first PC1 integration test checked only profiles and unresolved statuses rather than the complete recovered model. | Repaired with a strict typed representation of every recovered field, denied unknown fields, exact value assertions, and negative unknown, missing, mistyped, and unsupported categorical cases. |
| P2 | Arbitrary-size integer parity with the supplied oracle was unresolved. | Repaired by enabling arbitrary-precision JSON numbers, rejecting floating forms, normalizing negative zero, and adding differential vectors. |
| P2 | Digest mismatch and unresolved-preimage verifier branches lacked coverage. | Repaired with direct public-path tests. |
| P3 | The verification report overstated the surviving migration-receipt test breadth. | Repaired by distinguishing the directly tested Equivalent path from static inspection of all successful constructor paths. |

The provenance reviewer also required this review record, durable-state transition, and `SHA256SUMS` before delivery. Those closeout items are part of the final tree.

## Repair verification

The repaired workspace passed formatting, all-target locked/offline check, denied-warning Clippy, 17 all-target tests, targeted Foundation and PC1 selections, doctests, metadata resolution, dependency-tree resolution, recovered-byte hashes, wheel and RECORD integrity, and six valid plus two invalid legacy-oracle differential vectors.

## Fresh repair review

| Classification | Result |
|---|---|
| P0 | None |
| P1 | None |
| P2 | None |
| P3 | None |
| Foundation/PC1 reconstructed baseline | Accepted |
| Byte-exact restoration | Not claimed |
| PC2 | Not started |

The fresh reviewer confirmed that the public canonical API is limited to non-authoritative mathematics over caller-supplied resolved preimages; the complete recovered PC1 object and its negative schema cases are exercised; arbitrary integers, negative zero, digest mismatch, and absent-preimage paths are covered; recovered artifacts remain byte-identical; the missing Standard and artifact-specific blueprint/manifest preimage rules remain explicit; and no PC2 or unrelated product surface entered the tree.

## Accepted unresolved gaps

Artifact-specific blueprint and manifest preimage extraction remains unresolved because the Lattice Standard 0.3 document and original native implementation were not recovered. The recovered migration receipt source does not constrain `RequiredNextAction` by outcome, although every receipt remains non-authoritative. The original external suites, dependency lock, directive content, licence, paths, Git history, and baseline commit remain missing. These gaps prevent any byte-exact or original-history claim but do not invalidate the bounded reconstructed Foundation/PC1 provenance anchor.

READ_ONLY_REVIEW_COMPLETE=true
