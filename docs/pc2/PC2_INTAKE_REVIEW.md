# PC2 Parser Intake Read-Only Review

Review date: 2026-07-22.

Result: accepted for the bounded parser-dependency intake and semantic-freeze gate.

The review was performed as a separate read-only pass after the freeze and verification work stopped. It used the same execution context; no independent reviewer context was available. No file was edited during the review pass.

## Scope reviewed

The review covered the complete changed-file set, the dependency selection and machine provenance record, the semantic freeze, all valid and invalid fixtures, durable state changes, accepted Foundation/PC1 hashes and tests, public crate APIs, root Cargo files, and the forbidden-scope boundary.

The reviewed change set contained only additive PC2 intake material under `docs/pc2` and `conformance/pc2/parser`, plus additive state entries in `DECISIONS.md`, `IMPLEMENTATION_PLAN.md`, and `PROJECT_STATE.md`. `Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`, production crates, Foundation conformance, PC1 conformance, and ADR 0001 had zero diff. No `.rs` file, compiler crate, parser dependency, identity code, runtime code, builder code, or product surface was added.

## Findings

| Severity | Finding | Disposition |
|---|---|---|
| P0 | None. | No action. |
| P1 | None. | No action. |
| P2 | The ThreadSmith project licence remains unresolved, so compatibility must be rechecked before dependency addition or distribution even though the selected graph offers permissive licence paths. | Accepted intake risk; does not choose a project licence. Reopen intake if the future project licence conflicts. |
| P2 | `arraydeque 0.5.1` contains internal Rust `unsafe`; `thiserror`, `proc-macro2`, and `quote` run pinned build scripts that probe `rustc`. | Fully recorded with exact versions and checksums. Any graph, source, feature, or script change reopens intake. |
| P3 | `saphyr-parser` remains a pre-1.0 API and may change upstream. | Exact `=0.0.11` pin, event qualification, frozen fixtures, and lockfile requirement contain the risk. |
| P3 | The selected dependency is intentionally absent from the accepted workspace lock during preparation. | The implementation tranche must add the exact pin, commit the resolved lock, and repeat locked/offline and licence verification. |

Before the read-only pass, verification corrected an inaccurate draft statement that the graph had no build scripts. The final record now identifies all three scripts and their `rustc` probes. No review repair cycle was required.

## Boundary judgment

Foundation identities and canonical-byte rules are unchanged. Blueprint and Manifest remain non-authoritative at the parser boundary, and their identity preimages remain unresolved. Native/legacy separation and migration-receipt non-authority are unchanged. The parser creates no identity, digest, Manifest, package resolution, compilation result, qualification, Binding, execution authority, or runtime state.

Ownership remains correct: `threadsmith-schema` owns schemas and data structures; the future `threadsmith-compiler` owns source parsing. The fixtures test only parser projection and shallow source-profile validation. In particular, parser-valid empty scenarios do not override the PC1 compiler requirement that a scenario is required.

With no open P0 or P1 finding, `PC2_PARSER_SEMANTICS_FROZEN=true` is supportable. This review does not make `PC2_IMPLEMENTATION_STARTED` or `PC2_ACCEPTED` true.
