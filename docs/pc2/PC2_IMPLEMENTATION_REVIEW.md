# PC2 Parser Implementation Read-Only Review

Review date: 2026-07-22.

Result: accepted for the bounded PC2 source-parser implementation gate with no open P0 or P1 finding.

The review was performed as visibly separate read-only passes after focused implementation stopped. No independent reviewer context was available, and no file was edited during either acceptance pass.

## Scope reviewed

The review covered the public `parse_blueprint_source` path, all implementation and focused-test code, the frozen fixture boundary, exact dependency graph and features, root workspace mutation, deterministic diagnostic order, fail-closed forbidden-feature behavior, and preservation of accepted Foundation/PC1 files and hashes.

## Findings and repairs

| Severity | Finding | Disposition |
|---|---|---|
| P1 | Out-of-range decimal mapping keys initially reached key-category rejection instead of the earlier frozen invalid-scalar diagnostic. | Repair cycle 1: range-check before key category; focused regression added and passed. |
| P1 | Initial projection interleaved scalar checks with event scanning, allowing an early scalar error to outrank a later forbidden YAML feature contrary to the frozen validation phases. | Repair cycle 2: complete read-only event audit now precedes projection; precedence regression added and passed. |
| P0 | None. | No action. |
| P1 | None open after repair cycle 2. | Accepted. |
| P2 | No maximum source size or nesting depth was frozen. Deeply nested adversarial input can consume substantial memory or stack before a diagnostic. | Recorded, not repaired: introducing a rejection limit would alter accepted source semantics and requires a future semantic-policy decision. |
| P2 | The ThreadSmith project licence remains unresolved. | Dependency graph is permissively licensed and fully recorded; compatibility must be rechecked when the project licence is selected. |
| P3 | The parser performs two event traversals to preserve global diagnostic precedence. | Accepted deterministic cost for PC2; performance optimization is outside the bounded acceptance gate. |

## Boundary judgment

`threadsmith-schema` remains unchanged and owns schemas/data structures. `threadsmith-compiler` owns source parsing but contains no compiler resolution or execution path. No API creates identities, digests, Manifests, packages, qualification, Binding, executable artifacts, runtime state, builder state, provider access, or user surface.

Foundation and PC1 source and conformance hashes match the accepted baseline. The exact selected parser pin, default-feature state, and lock graph match the accepted intake. The closure pass found no false-positive fixture path and no open acceptance-level defect.
