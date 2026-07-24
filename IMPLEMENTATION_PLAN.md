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

The next bounded task is `PC7 Resolve implementation only`. This sequence
statement authorizes no Lock implementation, product layer, Builder, runtime,
provider, installation, CLI, MCP, UI, Android, or execution work.
