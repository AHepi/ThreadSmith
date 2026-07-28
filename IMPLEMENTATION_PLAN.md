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

## Lattice Standard 0.3 Canonical JSON Erratum and PC5 semantic-freeze tranche

This documentation-only tranche was authorized after PC4 acceptance. It closes
the Standard's identity-affecting JSON string-escape ambiguity and freezes only
the immediately following `DefaultedSource -> DigestedSource` phase. It does
not implement product code.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Canonical byte closure | One narrow normative erratum selects exact UTF-8, punctuation, NFC, object-key, array, integer, string-escape, Unicode, BOM, whitespace, and newline bytes without changing an artifact preimage. | 2 | Complete |
| Lifecycle and identity ownership | PC5 owns only Standard `Digest`, consumes PC4 `DefaultedSource`, and creates exactly one Blueprint content identity before Package scan. | 2 | Complete |
| Preimage and output binding | The complete post-default root is canonicalized and hashed; opaque `DigestedSource` binds the resulting `BlueprintDigest` to the exact input without exposing a mismatch constructor. | 2 | Complete |
| Diagnostic and deferral boundary | PC5 is total over its accepted input, emits no source diagnostic, and digests duplicate names and every other later-invalid declaration form without semantic endorsement. | 2 | Complete |
| Fixture design | Exact byte-hex/SHA-256, source-equivalence, distinction, profile-boundary, invalid-but-digestible, and output-binding cases are frozen. | 2 | Complete |
| Regression and consistency verification | Foundation through PC4, both earlier authorities, the new erratum, fixture integrity, independently recalculated hashes, and repository-boundary checks pass. | 2 | Complete: 43 existing tests; all semantic fixture checks pass |
| Read-only acceptance | A visibly separate adversarial semantic pass classifies P0-P3 and accepts only with no open P0/P1. | 2 | Complete after repair cycle 1; no open findings |

The documentation allowlist is
`docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md`, `docs/pc5/**`,
`conformance/pc5/digest/**`, and additive PC5 entries in `PROJECT_STATE.md`,
`IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. The recovered Standard, accepted
Default Semantics Erratum, Rust source, Cargo files, dependencies, Foundation
through PC4 conformance artifacts, package resolution, Lockfiles, import
expansion, declaration validation, later identities, Manifests, qualification,
Binding, runtime, Builder, providers, and user surfaces remain unchanged.

The next bounded task is `PC5 Digest-phase implementation against the frozen
semantics and fixtures`. That sequence statement does not authorize
implementation, dependency mutation, commit, push, package work, or any later
compiler or runtime phase.

## PC5 Digest-phase implementation tranche

This tranche implemented and focused-tested only the frozen
`DefaultedSource -> DigestedSource` boundary. Independent review and acceptance
completed as separate gates; every later phase remains separate and
unauthorized.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Canonical core closure | The single accepted Rust encoder emits every Canonical JSON Erratum byte while retaining the Foundation arbitrary-integer domain. | 2 | Complete: all 8 golden byte/hash vectors and the arbitrary-integer regression pass |
| Public PC5 boundary | Opaque `BlueprintDigest` and `DigestedSource` bind one exact post-default source through `digest_source`. | 2 | Complete: public-path tests pass |
| Focused conformance | Every canonical, equivalence, distinction, profile, later-invalid, binding, repeatability, non-authority, and public-input-domain requirement uses the public path where reachable. | 2 | Complete: 9 focused PC5 tests |
| Totality repair | Caller-created values outside the frozen PC2 domain fail closed before `ValidatedSource`; genuine PC2 values and later-invalid domain-valid declarations retain their accepted paths. | 1 | Complete, verified, and independently reviewed |
| Regression qualification | Formatting, all-target check/test, all-feature Clippy, dependency tree, Foundation, and PC1-PC4 pass locked and offline. | 2 | Complete post-repair: Rust 1.97.1, 52 tests total; 43 prior-phase regressions |
| Independent implementation review | A separate read-only reviewer examines the repaired verified implementation and classifies actionable findings. | 2 | Complete: no open P0/P1; P0=0, P1=0, P2=2, P3=1 |
| Acceptance | Accept only after complete verification and repaired independent review. | 0 | Complete within the frozen PC5 Digest boundary |
| Publication | Publish the complete accepted tree only through the separately authorized, single-commit, non-force Git Data procedure; record commit identity externally. | 0 | Complete only through that publication procedure; identity remains external |

The implementation allowlist is the two canonical/compiler source files, two
focused test files, compiler manifest, mechanically updated lockfile, one
verification report, and additive PC5 implementation state entries. No external
dependency or later compiler/runtime behavior is permitted.

The accepted review retains three non-blocking debt items: the generic
canonical API can accept hidden unchecked `+1` and `01` number spellings outside
the PC5-admitted domain; permanent tests do not cover every externally probed
ordering, signed-boundary, non-minimal-number, and RFC 6901 case; and
`SourceDiagnostic` rustdoc omits pre-PC3 domain admission. These P2/P2/P3 items
do not alter the accepted PC5 bytes, preimage, totality, opacity, binding, or
phase ownership and are not repaired by this gate.

The next bounded task is `PC6 Package-scan scope reconciliation and semantic freeze`.
This does not authorize PC6 implementation, Builder, runtime, provider, or any
execution behavior.

## PC6 Package Scan erratum-acceptance and semantic-freeze tranche

This documentation-only tranche accepts the independently reviewed Package Scan
Semantics Erratum and freezes PC6 without implementing it.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Scope reconciliation | Preserve the completed ambiguity analysis and close its identified gaps only through the accepted normative companion. | 0 | Complete |
| Erratum acceptance | Derive the accepted companion from the exact fourth repaired candidate without changing its normative algorithm, fixtures, vectors, diagnostics, or identities. | 0 | Complete |
| Independent review evidence | Record the supplied complete fourth-repair review accurately without presenting this acceptance task as another independent review. | 0 | Complete: P0=0, P1=0, P2=0, P3=0 |
| Semantic freeze | Freeze exact input, output, ownership, immutable-byte continuity, package identity, diagnostics, non-authority, and deferred behavior. | 0 | Complete |
| Golden verification | Recompute authoritative constants, package vectors and identities, fixture populations, diagnostic expectations and vocabulary, normative-region equality, and DATA_CHANGED identity. | 0 | Complete |
| Tree-boundary qualification | Prove every Rust, Cargo, PC1-PC5 implementation, conformance, and authority path byte-identical to baseline. | 0 | Complete; Rust toolchain unavailable and non-blocking because no compilable or dependency input changed |
| Publication | Commit the exact seven-path documentation/state inventory once and publish one non-force child of the required baseline. | 0 | Delivery gate |

The only permitted paths are the accepted Package Scan Erratum,
`docs/pc6/PC6_SCOPE_RECONCILIATION.md`,
`docs/pc6/PC6_SEMANTIC_FREEZE.md`,
`docs/pc6/PC6_ERRATUM_ACCEPTANCE_AND_FREEZE_VERIFICATION.md`, and additive
updates to `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`.
Rust source, tests, Cargo files, dependencies, existing conformance fixtures,
Foundation and PC1-PC5 semantics, Resolve, Lock, Expand, Normalize, Static
check, Manifest, Builder, runtime, providers, and product surfaces remain
unchanged.

The next bounded task is `PC6 Package Scan implementation only`. This records
sequence; it does not begin implementation or authorize Builder, runtime,
provider, package-product, CLI, MCP, UI, Android, or execution work.

## PC6 Package Scan implementation tranche

This separately authorized tranche implements only the frozen
`DigestedSource + PortableProjectSnapshot -> ScannedSource` boundary.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Snapshot boundary | Exact optional `packages` lookup result is acquired into one immutable portable subtree with a non-semantic acquisition error surface. | 2 | Implemented; focused public-path qualification passes |
| Public PC6 boundary | Private-field wrappers bind the exact source, admitted descriptor, phase-produced package identity, and retained verified bytes without mismatch constructors. | 2 | Implemented; focused public-path and opacity checks pass |
| Frozen semantics | Structural discovery, numeric candidate order, accepted-PC2 parser mapping, closed schema, paths, metadata audit, raw-byte verification, canonical package construction, and all 31 diagnostics match the accepted erratum. | 2 | Complete; all focused frozen cases and the independent review pass |
| Durable conformance | Machine-readable material preserves 34 byte constants, six canonical vectors, 19 identities, 18 presentations, 18 path scalars, six pointers, 184 fixture IDs, 124 expectations, and 31 codes. | 2 | Complete; exact-byte plan materialization, closed vocabularies, all population/golden arithmetic, and all 184 executed rows pass |
| Focused qualification | The public PC6 path executes the complete fixture set, exact package results, exact diagnostics, identity vectors, ordering, source binding, retained bytes, and opacity checks. | 2 | Complete: 13 tests, 184 unique fixtures, 180 scan runs, 123 diagnostics, 53 successes, eight acquisition cases, 124 expectations, and 31 codes |
| Regression qualification | Formatting, all-target checks/tests, all-feature Clippy, Foundation, and PC1-PC5 pass locked and offline. | 2 | Complete: Rust 1.97.1 frozen/offline formatting, workspace all-target check, all 67 workspace tests, all-workspace/all-feature Clippy with warnings denied, frozen dependency tree, executable-plan closure, golden/authority checks, and repository immutability pass |
| Read-only acceptance | A separate adversarial review accepts only with no open P0/P1 and no false-positive fixture path. | 2 | Complete: P0=0, P1=0, P2=0, P3=0 |
| Acceptance | Accept PC6 only after implementation verification and the separate read-only review complete successfully. | 0 | Complete within the frozen Package Scan boundary |
| Delivery | Publish the exact accepted thirteen-path tree only through the separately authorized single-commit, non-force Git Data procedure. | 0 | Complete; accepted PC6 publication baseline |

The implementation allowlist is compiler source, compiler PC6 tests,
`conformance/pc6/package_scan/**`, one PC6 implementation-verification
document, and additive PC6 implementation entries in the three durable state
files. Cargo manifests, `Cargo.lock`, the canonical and schema crates, accepted
Standard and errata, PC1-PC5 fixtures and evidence, Resolve and every later
phase, Builder, runtime, providers, and product surfaces remain unchanged.

The isolated Rust 1.97.1 toolchain is available under
`/tmp/threadsmith-rustup/toolchains/1.97.1-x86_64-unknown-linux-gnu/bin/`.
Rust commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452`, Cargo commit
`c980f4866141969fab6254a680546a277789d6f0`, rustfmt 1.9.0-stable, and
Clippy 0.1.97 are verified. Dependencies were already cached. Every Cargo
qualification command ran frozen and offline, and no network operation
occurred.

The fixture-infrastructure repair closes the notation-only gap with a
deterministic generated plan and an unknown-field-rejecting Rust interpreter.
The generator proves all 184 rows are uniquely dispatched, every
source/base/node/operation is constructible without implicit filesystem state,
all fixed results are complete, and all authoritative data is reachable. The
plan repair materializes every `REPLACE_HEX` operand as direct exact lowercase
hex. The accepted-PC2 precedence repair passes 18 focused tests. A final
two-file test-harness repair replaces manual parity checks with
`is_multiple_of` and groups stable comparison inputs without changing any
assertion or expected result. The complete focused matrix now passes:
formatting, frozen all-target compilation, 13 focused PC6 tests, all 184
fixtures and 180 public scan runs, all-feature Clippy with warnings denied, the
deterministic plan checker, and textual-diff checks. Full frozen workspace
qualification also passes with exactly 67 tests, workspace all-target checking,
all-workspace/all-feature Clippy with warnings denied, frozen dependency-tree
resolution, the executable-plan and golden checks, accepted-authority hashes,
and byte-identical non-status repository inputs. Implementation verification is
complete. The separate independent read-only review reproduced the frozen
qualification and complete fixture evidence, reported P0=0, P1=0, P2=0, and
P3=0, and recommended acceptance. The bounded PC2 explicit-tag
diagnostic-precedence repair is accepted as part of the PC6 publication
candidate. PC6 is accepted within the frozen Package Scan boundary. The next
bounded task after its completed publication was the separately authorized PC7
Resolve semantic gate. Builder, runtime, providers, and every later product
phase remain unauthorized.

## PC7 Resolve erratum-acceptance and semantic-freeze tranche

This documentation-only tranche accepts the independently reviewed second
repaired Resolve Semantics Erratum and freezes PC7 without implementing
Resolve.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Baseline and scope intake | Verify the accepted PC6 bundle, required commit/tree/parent/subject, local and remote `main`, and exact preserved PC7 scope report. | 0 | Complete |
| Reviewed-artifact intake | Verify exact candidate, final review, and preregistration identities, complete byte properties, and review disposition. | 0 | Complete |
| Erratum acceptance | Add only procedural acceptance metadata while preserving every reviewed normative and fixture-criteria byte. | 0 | Complete |
| Durable specified criteria | Retain the complete strict JSON manifest containing exact schemas, constructors, references, inputs, expected results, bytes, hashes, selectors, relations, coverage, and future vectors. | 0 | Complete; 96 current fixtures and three non-dispatchable future vectors at maturity `specified` |
| Independent review evidence | Record the supplied final review without conducting another semantic review. | 0 | Complete: all five prior P1 findings closed; P0=0, P1=0, P2=0, P3=1; independence uncompromised |
| Semantic freeze | Bind exact ScannedSource and optional immutable Lockfile input, source/byte/output continuity, lock reuse, numeric selection, fixed-point behavior, selected-module intake, cycles, diagnostics, paths, non-authority, and deferrals. | 0 | Complete |
| Criteria verification | Strict-parse and schema-check the manifest; recompute populations, references, identities, constructibility, relations, pass boundaries, and two independent canonical preimages. | 0 | Complete |
| Tree-boundary qualification | Prove every Rust, Cargo, earlier implementation, existing conformance, and path outside the eight-path allowlist byte-identical to baseline. | 0 | Complete; no Rust or dependency command required or run |
| Publication | Create one documentation-only child commit and publish one non-force fast-forward update of `main`. | 0 | Complete |

The exact allowlist is
`docs/pc7/PC7_SCOPE_RECONCILIATION.md`,
`docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md`,
`docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json`,
`docs/pc7/PC7_SEMANTIC_FREEZE.md`,
`docs/pc7/PC7_ERRATUM_ACCEPTANCE_AND_FREEZE_VERIFICATION.md`,
`PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`.

Rust source, tests, Cargo files, dependencies, existing conformance fixtures,
earlier accepted errata and phase documents, Lock, Expand, declaration
processing, Manifest, qualification, Binding, Builder, runtime, providers,
installation, CLI, MCP, UI, Android, and every product surface remain
unchanged.

The retained criteria contain 43 registered new choices, 21 unique Resolve
diagnostic codes, 62 diagnostic fixtures, 29 ordinary success fixtures, five
relation fixtures, 118 schema categories, 11 rank comparisons, eight mandatory
gate-order criteria, and exact chain-255 preimages. The sole P3 remains
nonnormative provenance debt and does not authorize a repair.

At the 2026-07-25 publication, the then-recorded next task was `PC7 Resolve
implementation only`. That historical sequence was superseded when subsequent
implementation review exposed semantic and executable-criteria defects.

## PC7 five-repair acceptance, refreeze, and publication tranche

This documentation-only tranche accepts the exact independently reviewed
fifth repair and refreezes PC7 without executing implementation qualification.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Authenticated intake | Verify the consult package, fifth candidate, author report, candidate manifest, checksum closure, governing fifth review, bundle, checkout, and fresh remote baseline. | 0 | Complete |
| Fifth review disposition | Record PC7-SR4-IR-P1-01 recomputed closed and retain PC7-AJ-P3-01 dormant, open, future-only, non-dispatchable, outside current populations, and non-blocking. | 0 | Complete; P0=0, P1=0, P2=0, P3=1 |
| Exact semantic acceptance | Preserve every byte from `NORMATIVE SECTION 1 — Authority, amendment, and precedence` through the reviewed fifth candidate's final byte. | 0 | Complete |
| Durable criteria | Copy the complete standalone manifest byte-for-byte and prove equality with the embedded copy. | 0 | Complete; 118 current fixtures, 45 choices, 15 schema discriminators, maturity `specified` |
| Authority registry | Rebind only the accepted erratum and semantic-freeze procedural byte counts and SHA-256 values; keep all other V1 bytes and overlay-baseline provenance unchanged. | 0 | Complete |
| Acceptance evidence | Amend the historical PC7 acceptance record with the five-repair chain, exact identities, recomputations, dormant P3, tree boundary, and publication procedure. | 0 | Complete |
| Evidence reset | Keep implementation started while resetting focused qualification, implementation verification, implementation review, and overall PC7 acceptance to false against the refrozen authority. | 0 | Complete |
| Tree boundary | Prove every Rust, Cargo, executable-plan, implementation, test, prior-conformance, prior-erratum, and non-allowlisted path byte-identical to baseline. | 0 | Complete; no product or toolchain execution |
| Publication | Create exactly one documentation-only child commit and publish one non-force fast-forward update of `main`; record the self-excluded commit and tree identities externally. | 0 | Complete through the separately authorized publication procedure |

The accepted criteria remain specified rather than dispatchable, executable,
qualified, implementation-verified, or implementation-reviewed. PC7 remains
unaccepted; Builder, runtime, and every later product phase remain
unauthorized. Exactly one bounded task is active:

```text
NEXT_BOUNDED_TASK=separate read-only PC7 implementation and executable-conformance impact assessment against the refrozen semantic authority; identify the exact bounded implementation, generator, interpreter, plan, and qualification deltas without modifying repository content
```

## PC7 Resolve implementation-acceptance and publication tranche

This 2026-07-28 tranche accepts and publishes only the exact independently
qualified PC7 Resolve implementation and executable-conformance candidate. It
does not repair, refactor, regenerate substantively, reinterpret semantics,
modify accepted authority, reopen findings, or begin PC8.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Baseline authentication | Required branch, HEAD, tree, local `main`, cached `origin/main`, fresh remote `main`, empty index, and exact six-path unstaged candidate match. | 0 | Complete |
| Candidate identity | All six reviewed path hashes equal the qualified identities and remain unchanged through durable-state authoring. | 0 | Complete |
| Governing evidence | Semantic publication, final repair, implementation re-review, focused qualification, and qualification-review hashes and byte formats match. | 0 | Complete |
| Acceptance eligibility | The qualification review records 168 recomputed claims, no unresolved claim class, P0=0, P1=0, P2=0, P3=0, and `PASS`. | 0 | Complete |
| Regression spine | Rust 1.97.1 formatting, workspace all-target checking, full tests, warning-denied Clippy, frozen dependency tree, and textual-diff checks pass offline with external targets. | 0 | Complete; 78 of 78 workspace tests pass |
| Executable conformance | The unfiltered public-boundary PC7 binary, generator admission and rejection self-tests, checked plan, Python syntax, and fixture-set equality pass. | 0 | Complete; 11 of 11 PC7 tests and 118 of 118 current fixtures pass |
| Determinism | Two authenticated disposable regenerations equal one another and the checked plan byte-for-byte. | 0 | Complete; 34,460,681 bytes at SHA-256 `4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d` |
| Durable acceptance | Amend only `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`; create only the PC7 acceptance record. | 0 | Complete |
| Staged boundary | Reauthenticate all inputs, then stage exactly the ten authorized paths with no unstaged difference. | 0 | Complete through the separately authorized delivery procedure |
| Publication | Create one child commit with the required subject and publish only `refs/heads/main` by normal non-force fast-forward after a fresh remote check. | 0 | Complete through the separately authorized delivery procedure |

The six accepted implementation and executable-criteria paths are
`conformance/pc7/resolve/build_executable_fixture_plan.py`,
`conformance/pc7/resolve/executable_fixture_plan.json`,
`crates/threadsmith-compiler/src/lib.rs`,
`crates/threadsmith-compiler/src/resolve.rs`,
`crates/threadsmith-compiler/tests/pc7_resolve.rs`, and
`crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs`. The
four durable paths are `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`,
`DECISIONS.md`, and
`docs/pc7/PC7_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md`. No other path may
enter the commit.

The complete workspace suite passes exactly 78 tests: 67 retained
Foundation-through-PC6 tests and 11 PC7 tests, with zero failure, ignore,
measured, or filter. The PC7 binary separately passes all 11 unfiltered tests.
Its strict interpreter proves exact set equality across 118 defined, 118
generated, and 118 executed current fixture IDs. Four future vectors remain
non-dispatchable and excluded. The sorted fixture-ID preimage is 2,576 bytes
at SHA-256
`ab7b72bdb33a255d2539a204cd880fa7aedab61b8672cfa3f02d8342d510f221`.
Fixture maturity advances from `specified` to `qualified` only for the frozen
PC7 Resolve boundary.

The historical semantic review state
`RESOLVE_ERRATUM_REVIEW_P3=1` remains intact and distinct. Current PC7
implementation and qualification-review findings are P0=0, P1=0, P2=0, and
P3=0. Acceptance creates no new Lockfile, `lock_id`, Manifest, Binding,
identity, authority, persistence, installation, provider, model, network,
Builder, runtime, CLI, MCP, UI, Android, or other product behavior.

The final commit, tree, remote, and push identities are deliberately excluded
from this self-referential tranche and are recorded only by the external
operator report. Publication makes the prospective durable state
authoritative; PC8 remains unstarted, Builder and runtime remain unauthorized,
and exactly one bounded task follows:

```text
NEXT_BOUNDED_TASK=PC8 Lock scope reconciliation and semantic freeze only
```

## PC8 Lock semantic-acceptance, freeze, and documentation-publication tranche

This 2026-07-28 tranche accepts and freezes only the exact independently
reviewed PC8 Lock semantic and specified-conformance candidate. It does not
repair or reinterpret semantics, implement Lock, construct executable
conformance, perform physical Lockfile persistence, qualify product code,
accept PC8 overall, or begin Expand or any later phase.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Baseline authentication | Required branch, HEAD, tree, local `main`, cached `origin/main`, fresh remote `main`, empty index, absent tracked differences, and exact four-path overlay match. | 0 | Complete |
| Governing evidence | Superseding review, unchanged historical source, author repair report, and exact four-line procedural serialization correction authenticate. | 0 | Complete; governing P0=0, P1=0, P2=0, P3=0 and `PASS` |
| Exact semantic acceptance | Preserve the substantive regions of the scope reconciliation, semantic freeze, and Lock Erratum byte-for-byte while changing only procedural metadata and status envelopes. | 0 | Complete; all three region hashes and byte counts equal |
| Durable specified criteria | Preserve the complete standalone manifest byte-for-byte and advance only procedural maturity to `specified`. | 0 | Complete; 20 fixtures, 19 relations, 41 discriminators, four registries, 235 spans, four future-only rows |
| Authority registry | Bind accepted PC1-PC7 authority, reviewed and accepted PC8 identities, governing review, acceptance path, required commit parent and subject, publication mode, and external evidence boundary. | 0 | Complete |
| Acceptance verification | Record authentication, review closure, immutable-region equality, populations, accepted identities, durable status, exact publication boundary, and self-excluded final evidence. | 0 | Complete |
| Durable state | Amend only `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`; keep implementation unstarted and overall PC8 acceptance false. | 0 | Complete |
| Tree boundary | Prove the complete repository delta is exactly the declared nine-path acceptance envelope and every other baseline path is byte-identical. | 0 | Complete through the separately authorized publication procedure |
| Publication | Create exactly one documentation-only child of `54b8b2b380606428f0d41f33d5d32c985c18c7ea` and publish one normal non-force fast-forward update of `refs/heads/main`; record self-excluded identities externally. | 0 | Complete through the separately authorized publication procedure |

The standalone manifest remains the exact reviewed 1,040,963-byte file at
SHA-256
`72a680a44a6d49388f1e26bac46e7e59862a1e502a74a72c239a8c908bf03399`.
Its reviewed candidate-status members are intentionally unchanged. The
accepted procedural state is recorded by the V1 authority registry,
acceptance verification, durable state, commit, and publication evidence.

The accepted criteria remain specified rather than dispatchable, executable,
qualified, implementation-verified, or implementation-reviewed. The
non-ASCII package-name case, proper-prefix package-name case, non-Core
profile case, and physical persistence adapter remain future-only and
non-dispatchable.

Exactly one bounded task follows:

```text
NEXT_BOUNDED_TASK=separate read-only PC8 implementation and executable-conformance impact assessment against the newly frozen authority
```

## PC8 Lock specified-conformance criteria V2 acceptance and supersession tranche

This 2026-07-29 tranche is procedural acceptance preparation for the exact
reviewed V2 manifest. It becomes operative only with the exact publication
contract below. It does not alter frozen semantics, repair Task 2, authorize
Task 3, accept PC8 overall, perform persistence, or begin Builder, runtime,
product, Expand, PC9, or later work.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Baseline authentication | Required `main`, HEAD `89fe4493a7642cffa76e731911bcabf225dacc7a`, tree `c7e2d30b718bc162c09b2b30387329dac8b38e9e`, matching cached remote, empty real index, exact V2 candidate, and exact five-path implementation overlay authenticate. | 0 | Complete for acceptance preparation |
| Review closure | Impact assessment, V2 author report, unchanged historical review, and governing superseding review authenticate; the superseding report adds exactly four alias lines and changes no evidence or semantic result. | 0 | Complete; governing disposition `PASS`, zero findings and unverified claims |
| Authority routing | Preserve V1 registry/manifest as immutable superseded history, preserve all normative authority, and route only the exact V2 manifest after operative publication. | 0 | Complete in registry V2; no semantic change |
| Durable acceptance | Add only registry V2, the acceptance/supersession record, and durable V2 entries in `DECISIONS.md`, `IMPLEMENTATION_PLAN.md`, and `PROJECT_STATE.md`; include the reviewed V2 manifest unchanged. | 0 | Complete in the prospective six-path envelope |
| Tree boundary | Independently reproduce one six-path prospective tree from two temporary indexes initialized from the required parent; exclude and reauthenticate all five implementation paths. | 0 | Required before publication; resulting tree identity is self-excluded |
| Publication | Create one documentation-only commit with subject `Accept PC8 Lock specified-conformance criteria V2` and normally fast-forward `refs/heads/main` from the exact parent. | 0 | Operative only when the external operator report records successful publication and converged refs |

The operative status transition is:

```text
PC8_SEMANTICS_ACCEPTED=true
PC8_SEMANTICS_FROZEN=true
PC8_SPECIFIED_CONFORMANCE_V1_CURRENT=false
PC8_SPECIFIED_CONFORMANCE_V2_REVIEWED=true
PC8_SPECIFIED_CONFORMANCE_V2_ACCEPTED=true
PC8_SPECIFIED_CONFORMANCE_V2_PUBLISHED=true
POST_FREEZE_PC8_SPECIFIED_CRITERIA_SUPERSESSIONS=1
POST_FREEZE_PC8_LOCK_NORMATIVE_SUPERSESSIONS=0
PC8_IMPLEMENTATION_STARTED=true
PC8_TASK_1_ACCEPTED=true
PC8_TASK_2_ACCEPTED=false
PC8_TASK_3_AUTHORIZED=false
PC8_ACCEPTED=false
OPEN_CONFORMANCE_CRITERIA_DEFECTS=0
OPEN_IMPLEMENTATION_DEFECTS=2
OPEN_IMPLEMENTATION_DEFECT_IDS=PC8-T2-SM-02,PC8-T2-SC-03
```

The failed V1-bound Task 2 generator and checked plan remain invalid and are
preserved only as evidence. Exactly one bounded task follows operative
publication:

```text
NEXT_BOUNDED_TASK=repair Task 2 generator against registry/manifest V2 for PC8-T2-SM-02 exact inner-constant isolation and dual-defect control, and PC8-T2-SC-03 declaration-resolved consumer traversal plus full-branch dormant-cycle rejection; regenerate the checked plan and submit it to a fresh independent Task 2 review; Task 3 remains closed
```
