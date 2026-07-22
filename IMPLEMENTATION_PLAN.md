# ThreadSmith Restoration Plan

Document status: reconstructed on 2026-07-22 for the Foundation/PC1 recovery only.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Inventory | Every supplied artifact is hashed, classified, and assigned an exact, inferred, or unresolved path. | 0 | Complete |
| Minimum reconstruction | Only the recovered two-crate Rust workspace, PC1 vectors, ADR, and durable recovery state exist. | 2 | Complete |
| Verification | Format, workspace check, Clippy with denied warnings, locked/offline checks, Foundation tests, PC1 tests, conformance vectors, and recovered-byte hashes pass. | 2 | Complete |
| Read-only acceptance | A separate reviewer finds no P0 or P1 restoration defect and confirms Foundation/PC1 boundaries. | 2 | Complete after repair cycle 1 |
| Provenance anchor | The commit containing this accepted tree and tag `threadsmith-foundation-pc1-reconstructed-0.1` form the new anchor; remote ref verification is recorded outside this self-referential tree. | 0 | Delivery gate |

The active scope excludes PC2 and every parser, YAML, compiler, runtime, builder, planner, provider, UI, CLI/MCP, and Android concern. The next bounded task after this baseline is `PC2 parser-dependency intake and semantic freeze`; it is not authorized within this restoration.

## PC2 parser intake tranche

This later tranche was authorized separately and completed as preparation only. It does not reopen or reinterpret the completed restoration gates above.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Dependency intake | Rust YAML 1.2 candidates, exact selection, provenance, licences, transitive risk, and offline rule recorded without workspace dependency mutation. | 2 | Complete |
| Semantic freeze | UTF-8 YAML to NFC JSON-shaped tree boundary, subset, scalars, collisions, ordering, root envelope, defaults, and diagnostics frozen. | 2 | Complete |
| Fixture design | Required valid and invalid parser-only cases carry exact expected trees or diagnostics. | 2 | Complete |
| Regression and evidence verification | Accepted Foundation/PC1 suites pass; provenance, licence, checksum, offline probe, and fixture integrity pass. | 2 | Complete |
| Read-only intake review | Separate read-only pass classifies P0–P3 findings and accepts only with no open P0/P1. | 2 | Complete; no open P0/P1 |

The active allowlist is `docs/pc2/**`, `conformance/pc2/parser/**`, and additive PC2 state entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. Production crates, root Cargo files, Foundation/PC1 conformance, identities, compilation, package resolution, runtime, builder, planner, providers, user surfaces, and delivery actions remain excluded.

If intake is accepted, the next bounded task is `PC2 parser implementation against the frozen intake and fixtures`. That statement records sequence only; it does not itself authorize implementation.

## PC2 parser implementation tranche

This tranche was authorized separately after the intake was accepted. It implements only the frozen source projection boundary.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Parser package | `threadsmith-compiler` projects one accepted UTF-8 YAML document into the frozen NFC JSON-shaped tree without compiling or creating authority. | 2 | Complete |
| Focused conformance | All frozen valid/invalid fixtures and deterministic edge cases pass through the public parser API. | 2 | Complete |
| Dependency qualification | Exact selected pin and resolved lock match intake; locked/offline graph, checksums, licences, and no-native boundary pass. | 2 | Complete |
| Regression qualification | Formatting, all-target workspace check, Clippy with warnings denied, Foundation, PC1, and PC2 suites pass offline and locked. | 2 | Complete |
| Read-only acceptance | Separate implementation and closure passes have no open P0/P1 finding. | 2 | Complete after repair cycles 1 and 2 |
| Publication | Accepted PC2 tree is committed to and fetched back from remote `main`; remote and local tree identities match. | 0 | Delivery gate |

The next bounded task is `PC3 scope intake and semantic freeze`; it is not authorized by this plan entry. PC2 acceptance does not authorize compiler semantics, resolution, identities, runtime, builder, providers, user surfaces, or release work.

## PC2 Standard reconciliation tranche

This bounded corrective tranche was authorized after the recovered Lattice Standard 0.3 exposed incompatibilities in the accepted PC2 parser boundary. The Standard supersedes the earlier reconstructed PC2 source assumptions where they conflict.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Normative reconciliation | Preserve the recovered Standard exactly and classify every accepted-PC2 deviation by lifecycle phase. | 2 | Complete |
| Parser correction | PC2 returns only an NFC JSON-shaped restricted-YAML tree, without source validation or defaults. | 2 | Complete |
| Focused conformance | Standard syntax, information preservation, signed scalars, forbidden YAML, duplicates, collisions, and deterministic output pass through the public API. | 2 | Complete |
| Regression qualification | Formatting, all-target checks, Clippy, Foundation, PC1, PC2, locked/offline, provenance, and documentation consistency pass. | 2 | Complete |
| Read-only acceptance | Separate implementation and closure passes have no open P0/P1 finding. | 2 | Complete after repair cycle 1 |
| Publication | Accepted reconciliation is committed and remote/local `main` tree identities match. | 0 | Delivery gate |

The implementation allowlist is `crates/threadsmith-compiler/src/lib.rs`, its PC2 focused test, `conformance/pc2/parser/**`, `docs/standard/LATTICE_STANDARD_0.3.md`, `docs/pc2/**`, and additive state entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. Cargo manifests, the lockfile, schema/canonical crates, Foundation/PC1 conformance, identities, package resolution, Lockfiles, Manifests, qualification, Binding, runtime, builder, providers, and user surfaces remain excluded.

Only after this tranche is accepted and published may the next bounded task return to `PC3 scope reconciliation and semantic freeze`. This plan entry does not authorize PC3 implementation.

## PC3 scope reconciliation and semantic-freeze tranche

This documentation-only tranche was authorized after PC2 became Standard-aligned. It maps PC3 to the immediately following lifecycle stage without implementing product code.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Lifecycle reconciliation | PC3 is derived from the Standard pipeline rather than convenience or future architecture. | 2 | Complete |
| Responsibility freeze | `Source validate` owns exact Core root-envelope checks and produces only `Valid root shape`. | 2 | Complete |
| Authority and deferral boundary | Defaults, identities, resolution, declaration normalization, static checking, Manifests, qualification, Binding, and runtime remain later. | 2 | Complete |
| Fixture design | Root-valid, root-invalid, precedence, preservation, and deferred-semantics cases have exact expected outcomes. | 2 | Complete |
| Regression and consistency verification | Foundation, PC1, PC2, Standard, fixture, documentation, and provenance checks pass. | 2 | Complete |
| Read-only acceptance | A separate adversarial pass classifies P0-P3 and accepts only with no open P0/P1. | 2 | Complete after repair cycle 1 |

The documentation allowlist is `docs/pc3/**`, `conformance/pc3/source_validate/**`, and additive PC3 state entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. Rust source, Cargo files, accepted conformance artifacts, PC2 semantics, defaults, identities, packages, resolution, Lockfiles, Manifests, qualification, Binding, runtime, builder, providers, user surfaces, and delivery actions remain excluded.

If this freeze passes verification and review, the next bounded task is `PC3 Source validate implementation against the frozen root-envelope fixtures`. That sequence statement does not authorize implementation.

## PC3 Source validate implementation tranche

This tranche was authorized after the PC3 scope and semantics were accepted. It implements only the frozen `Source validate -> Valid root shape` boundary.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Public boundary | `threadsmith-compiler` validates one PC2 value and returns a non-authoritative wrapper over the unchanged tree. | 2 | Complete |
| Frozen behavior | Root type, key allowlist, required keys, selectors, metadata syntax, collection categories, and deterministic precedence match the freeze. | 2 | Complete |
| Focused conformance | All 19 frozen fixtures and focused grammar, exhaustive categories, precedence, preservation, and non-ownership tests pass. | 2 | Complete: 7 tests |
| Regression qualification | Formatting, all-target checks, Clippy, Foundation, PC1, and PC2 pass locked and offline. | 2 | Complete: 39 tests total |
| Read-only acceptance | Separate implementation and closure reviews have no open P0/P1 finding. | 2 | Complete after repair cycle 1 |
| Publication | Accepted PC3 tree is committed to and fetched back from remote `main`; local and remote tree identities match. | 0 | Delivery gate; record externally |

The production allowlist is `crates/threadsmith-compiler/src/lib.rs`; focused tests are limited to `crates/threadsmith-compiler/tests/pc3_source_validate.rs`. Evidence may change under `docs/pc3/**`, `conformance/pc3/source_validate/**`, and additive PC3 entries in the three durable state files. Cargo files, accepted Foundation/PC1/PC2 semantics, defaults, declarations, resolution, identities, Lockfiles, Manifests, qualification, Binding, runtime, builder, providers, user surfaces, and PC4 remain excluded.

## Lattice Standard 0.3 Default Semantics Erratum tranche

This documentation-only tranche was authorized after the initial PC4 inquiry found that Standard 0.3 did not uniquely identify several identity-affecting default targets and encodings. The recovered Standard remains byte-exact; the erratum is a narrow normative companion.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Predicate resolution | Exact source targets and the canonical constant-true JSON expression are defined without adding a predicate operator. | 2 | Complete |
| Model fallback resolution | Source ownership and JSON encoding are exact while Run Binding authority remains unchanged. | 2 | Complete |
| Port target resolution | Module and unit input/output target scopes are exhaustive and no similarly named fields are captured. | 2 | Complete |
| Invalid-data behavior | Present, malformed, and ambiguous data has deterministic preservation and deferral behavior without declaration validation. | 2 | Complete |
| Identity and determinism | Post-default representation, idempotence, ordering, provenance absence, and identity-preimage participation are explicit. | 2 | Complete |
| Fixture obligations | Exact valid, invalid/deferred, idempotence, no-convenience-default, and identity-equivalence cases are required for the later PC4 freeze. | 2 | Complete |
| Regression and read-only review | Foundation through PC3 regressions and a separate adversarial semantic review find no open P0/P1. | 2 | Complete: 40 tests; no open P0/P1 |

The erratum allowlist is `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` plus additive state entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. The recovered Standard, conformance fixtures, Rust source, Cargo files, dependencies, PC2, PC3, declaration validation, resolution, Lockfiles, identities, Manifests, qualification, Binding, runtime, builder, providers, and user surfaces remain unchanged.

After verification and review, the next bounded task is `PC4 Default-phase scope reconciliation and semantic freeze against Standard 0.3 plus its Default Semantics Erratum`. This sequence statement does not authorize PC4 implementation.

## PC4 Default-phase scope reconciliation and semantic-freeze tranche

This documentation-only tranche was authorized after the Default Semantics Erratum removed the identity-affecting ambiguity. It freezes the exact `ValidatedSource -> DefaultedSource` boundary without implementing product code.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Lifecycle and ownership | PC4 owns only Standard `Default` in `threadsmith-compiler`, consumes PC3 output, and feeds PC5 Digest. | 2 | Complete |
| Output boundary | `DefaultedSource` contains only the expanded JSON-shaped value and remains non-authoritative. | 2 | Complete |
| Exact semantics | Every erratum target, value, traversal rule, explicit-value rule, malformed-data rule, and idempotence rule is frozen. | 2 | Complete |
| Diagnostics and deferral | PC4 owns no semantic diagnostic and cannot absorb PC3 or later validation errors. | 2 | Complete |
| Fixture design | Nine exact cases cover all targets, overrides, empty values, malformed preservation, ambiguity, non-recursion, repetition, and identity-preimage comparisons. | 2 | Complete |
| Regression and consistency verification | Foundation through PC3, Standard, erratum, fixture, documentation, and repository-boundary checks pass. | 2 | Complete: 40 tests; all consistency checks pass |
| Read-only acceptance | A separate adversarial semantic pass classifies P0–P3 and accepts only with no open P0/P1. | 2 | Complete: no findings |

The documentation allowlist is `docs/pc4/**`, `conformance/pc4/default/**`, and additive PC4 entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. The accepted Standard and erratum, Rust source, Cargo files, dependencies, Foundation, PC1, PC2, PC3, identity, resolution, Lockfiles, Manifests, qualification, Binding, runtime, builder, providers, and user surfaces remain unchanged.

If verification and review accept this freeze, the next bounded task is `PC4 Default-phase implementation against the frozen semantics and fixtures`. That sequence statement does not authorize implementation, commit, push, or release work.

## PC4 Default-phase implementation tranche

This tranche was authorized after the PC4 scope and semantics were accepted. It implements only the frozen `ValidatedSource -> DefaultedSource` transformation.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Public boundary | `threadsmith-compiler` consumes PC3 `ValidatedSource` and returns an opaque, non-authoritative `DefaultedSource`. | 2 | Complete |
| Frozen behavior | Exact absent-member insertion, explicit-value precedence, malformed-data preservation, bounded traversal, and idempotence match the freeze. | 2 | Complete |
| Focused conformance | Every frozen target and preservation case passes through the public boundary, including deterministic replay and identity-preimage comparisons. | 2 | Complete: 3 tests; all 9 fixtures |
| Regression qualification | Formatting, all-target checks, Clippy, Foundation, PC1, PC2, and PC3 pass locked and offline. | 2 | Complete: 43 tests total |
| Read-only acceptance | A separate implementation review classifies P0–P3 and accepts only with no open finding. | 2 | Complete: no findings; no repair cycle |
| Publication | Accepted PC4 tree is committed to and fetched back from remote `main`; local and remote identities are recorded externally. | 0 | Delivery gate |

The production allowlist is `crates/threadsmith-compiler/src/lib.rs`; focused tests are limited to `crates/threadsmith-compiler/tests/pc4_default.rs`. Evidence may change under `docs/pc4/**`, `conformance/pc4/default/**`, and additive PC4 entries in the three durable state files. The accepted Standard and erratum, Cargo files, dependencies, Foundation through PC3 semantics, canonicalization, digests, identities, packages, resolution, Lockfiles, Manifests, qualification, Binding, runtime, builder, providers, and user surfaces remain unchanged.

The next bounded task is `PC5 Digest-phase scope reconciliation and semantic freeze`. PC4 acceptance does not authorize it, and no PC5 work begins in this tranche.
