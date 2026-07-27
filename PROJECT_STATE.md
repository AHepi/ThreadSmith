# ThreadSmith Project State

State record status: reconstructed. Updated 2026-07-28.

| Field | Value |
|---|---|
| Repository | `AHepi/ThreadSmith` |
| Branch | `main` |
| Historical state supplied by operator | `FOUNDATION_ACCEPTED=true`, `PC1_ACCEPTED=true`, `PC2_STARTED=false` |
| Restoration phase | Accepted Foundation/PC1 provenance tree; Git commit and tag identities are external to this self-referential state file |
| Exact original Git history available | false |
| Byte-exact repository restoration possible | false |
| Recovered workspace shape | Rust virtual workspace with `threadsmith-schema` and `threadsmith-canonical` |
| PC2 started | false |
| Foundation reconstructed baseline accepted | true |
| PC1 reconstructed baseline accepted | true |
| Verification complete | true |
| Separate read-only review complete | true |
| Reconstructed files | 15 |
| Missing or unresolved evidence categories | 9 |
| Current provenance name | `threadsmith-foundation-pc1-reconstructed-0.1` |
| PC2 parser intake started | true |
| PC2 parser semantics frozen | true |
| PC2 implementation started | true |
| PC2 accepted | true |
| Selected parser path | `saphyr-parser =0.0.11`, event API, exact pin committed in the workspace lock |
| PC2 Standard reconciliation started | true |
| Controlling source specification | `docs/standard/LATTICE_STANDARD_0.3.md`, recovered SHA-256 `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| PC2 Standard aligned | true |
| PC2 reconciliation verification complete | true |
| PC2 reconciliation read-only review complete | true |
| PC2 diagnostic-precedence repair complete | true; accepted as part of the published PC6 candidate after the shared explicit-tag classifier and 18 focused parser tests passed verification and independent review |
| PC3 scope reconciled | true |
| PC3 semantics frozen | true |
| PC3 freeze verification complete | true |
| PC3 freeze read-only review complete | true |
| PC3 implementation started | true |
| PC3 accepted | true |
| PC3 implementation verification complete | true |
| PC3 implementation read-only review complete | true |
| Default Semantics Erratum complete | true |
| Default Semantics Erratum controlling companion | `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` |
| Default Semantics Erratum verification complete | true |
| Default Semantics Erratum read-only review complete | true; no open P0 or P1 |
| Original Lattice Standard 0.3 bytes changed | false |
| PC4 ready | true |
| PC4 scope reconciled | true |
| PC4 semantics frozen | true |
| PC4 freeze verification complete | true |
| PC4 freeze read-only review complete | true; no open P0 or P1 |
| PC4 implementation started | true |
| PC4 implementation verification complete | true |
| PC4 implementation read-only review complete | true; no P0, P1, P2, or P3 findings |
| PC4 accepted | true |
| Canonical JSON Erratum complete | true |
| Canonical JSON Erratum controlling companion | `docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` |
| Canonical JSON Erratum verification complete | true |
| Canonical JSON Erratum read-only review complete | true; no open P0 or P1 |
| PC5 scope reconciled | true |
| PC5 semantics frozen | true |
| PC5 freeze verification complete | true |
| PC5 freeze read-only review complete | true; no open P0 or P1 |
| PC5 implementation started | true |
| PC5 implementation verification complete | true; post-repair Rust 1.97.1 frozen, network-silent qualification passes 52 tests |
| PC5 totality repair complete | true |
| PC5 repair read-only review complete | true |
| PC5 implementation read-only review complete | true; final repaired review found P0=0, P1=0, P2=2, P3=1 |
| PC5 review findings | P0=0, P1=0, P2=2, P3=1; P2/P3 retained as non-blocking debt |
| PC5 accepted | true |
| PC6 scope reconciled | true |
| Package Scan Semantics Erratum accepted | true |
| Package Scan Semantics Erratum controlling companion | `docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md` |
| Package Scan fourth-repair independent review | complete; P0=0, P1=0, P2=0, P3=0 |
| PC6 semantics frozen | true |
| PC6 freeze verification complete | true; documentation, golden arithmetic, and exact baseline-tree boundaries pass |
| PC6 implementation started | true |
| PC6 focused qualification | complete; isolated Rust 1.97.1, 18 PC2 tests, all-target compiler check, 13 PC6 tests, all-feature Clippy with warnings denied, executable-plan check, and `git diff --check` pass frozen and offline |
| PC6 fixture interpreter | complete; all 184 unique fixtures and 180 public scan runs execute with 123 diagnostic cases, 53 successful cases, eight acquisition cases, 124 diagnostic expectations, and all 31 codes |
| PC6 mechanical verification | complete for exact `REPLACE_HEX` materialization, 184-case dispatch, all frozen populations, golden byte/hash/identity arithmetic, DATA_CHANGED, allowed repair boundaries, and `git diff --check` |
| PC6 implementation verification complete | true; full frozen/offline Rust 1.97.1 workspace qualification passes 67 tests, workspace all-target checking, all-feature Clippy with warnings denied, frozen dependency-tree resolution, executable-plan closure, golden population checks, authority hashes, and repository immutability |
| PC6 implementation review complete | true; separate read-only review found P0=0, P1=0, P2=0, P3=0 and recommended acceptance |
| PC6 review findings | P0=0, P1=0, P2=0, P3=0 |
| PC6 accepted | true |
| PC7 scope reconciled | true |
| Resolve Erratum candidate complete | true |
| Resolve Erratum candidate review complete | true |
| Resolve Erratum repair complete | true |
| Resolve Erratum repair review complete | true |
| Resolve Erratum second repair complete | true |
| Resolve Erratum second-repair review complete | true; P0=0, P1=0, P2=0, P3=1, independence uncompromised |
| Resolve Semantics Erratum accepted | true |
| Resolve Semantics Erratum controlling companion | `docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md` |
| PC7 semantics frozen | true |
| PC7 fixture maturity | qualified; 118 current fixtures are dispatchable and execute through the public Resolve boundary; four future vectors remain non-dispatchable and excluded |
| PC7 retained review debt | `RESOLVE_ERRATUM_REVIEW_P3=1`; the dormant future-only semantic P3 remains distinct from the zero-finding implementation and qualification reviews |
| PC7 implementation started | true |
| PC7 fixture interpreter complete | true |
| PC7 focused qualification complete | true |
| PC7 implementation verification complete | true |
| PC7 implementation review complete | true |
| PC7 qualification review complete | true |
| PC7 implementation and qualification review findings | P0=0, P1=0, P2=0, P3=0 |
| PC7 accepted | true; limited to the frozen Resolve boundary |
| Push complete | true |
| Builder authorized | false |
| Runtime authorized | false |
| PC8 started | false |
| Next bounded task | PC8 Lock scope reconciliation and semantic freeze only |

The recovered files are evidence, not a complete repository snapshot. No entry in this record claims that reconstructed files match the lost workspace byte for byte.

The accepted PC2 implementation adds `threadsmith-compiler` solely as the owner of UTF-8 restricted-YAML source projection into an NFC-normalized JSON-shaped tree. It adds no compilation, resolution, identity, digest, Manifest, execution, runtime, or builder behavior. Foundation/PC1 code, semantics, identities, canonical-byte rules, authority boundaries, and conformance evidence remain unchanged; `threadsmith-schema` remains limited to schemas and data structures.

The recovered Lattice Standard 0.3 subsequently proved that accepted PC2 had absorbed root validation, default insertion, and profile checks belonging to later compiler phases and had rejected Standard-permitted syntax. The accepted reconciliation corrects PC2 to the Standard's `Parse` phase only. It preserves absent fields for `Source validate`, adds no later compiler behavior, and leaves PC3 unstarted. Commit and remote-tree identities are external delivery evidence because they cannot be embedded self-referentially in this file.

The PC3 scope reconciliation assigns PC3 exactly the Standard `Source validate` phase and its `Valid root shape` output. The freeze validates only the Core root envelope and compatibility selectors, preserves the PC2 value unchanged, and leaves defaults, declaration semantics, resolution, identities, static checking, Manifests, and authority to later named phases. At freeze acceptance, PC3 implementation remained unstarted.

PC3 implementation adds the public `validate_blueprint_source` boundary and non-authoritative `ValidatedSource` wrapper in `threadsmith-compiler`. It performs only the frozen root checks, returns the unchanged PC2 value, adds no dependency, and is accepted after focused verification, full regression qualification, one bounded test-coverage repair, and a fresh read-only closure review. Publication identities remain external because they cannot be embedded self-referentially in this state file.

The Default Semantics Erratum is a separate normative companion to the recovered Standard and leaves the recovered Standard bytes unchanged. It resolves only exact default targets, values, expanded JSON representations, deterministic traversal, identity-preimage participation, invalid-data deferral, and fixture obligations. It adds no product code, declaration, feature, phase, authority, or runtime behavior. PC4 is ready for a separately authorized scope reconciliation and semantic freeze; PC4 implementation has not started.

The PC4 scope reconciliation and semantic freeze assign PC4 exactly the Standard `Default` phase. The future `threadsmith-compiler` boundary consumes PC3 `ValidatedSource` and produces non-authoritative `DefaultedSource` containing only the expanded JSON-shaped value for PC5. Exact fixtures bind every default target, explicit-value precedence, malformed-data preservation, non-recursive traversal, idempotence, and identity-preimage equality or distinction. No PC4 product code, diagnostic, dependency, identity, artifact, or authority behavior is introduced by the freeze.

PC4 implementation adds the public `apply_blueprint_defaults` boundary and opaque `DefaultedSource` wrapper in `threadsmith-compiler`. It applies only the accepted erratum and frozen defaults, preserves every present or malformed value required by later phases, and emits no diagnostic or provenance metadata. Focused fixtures prove deterministic and idempotent expansion plus post-default equality and distinction; full locked/offline qualification passes with 43 tests. No canonical bytes, digest, identity, artifact, authority, or later compiler/runtime behavior is created. At PC4 acceptance, PC5 remained unstarted and unauthorized.

The Canonical JSON Erratum is a narrow normative companion to the recovered Standard and leaves the recovered Standard bytes unchanged. It closes exact UTF-8, punctuation, object-key ordering, array preservation, signed-integer, string-escape, direct-Unicode, BOM, whitespace, and trailing-newline rules for every Standard canonical JSON use. It adds no preimage, identity, phase, validation, artifact, or authority rule. Exact byte-hex and SHA-256 vectors bind the closed encoding, including PC2-preserved decoded control characters.

The PC5 scope reconciliation and semantic freeze assign PC5 exactly the Standard `Digest` phase. The future `threadsmith-compiler` boundary consumes opaque PC4 `DefaultedSource`, reuses the single canonical Rust core, creates exactly one opaque `BlueprintDigest`, and returns non-authoritative `DigestedSource` binding that digest to the exact source. The preimage is the complete canonical JSON of the post-default root before import expansion. PC5 owns no source diagnostic and deliberately digests duplicate names and other later-invalid content. Exact fixtures bind canonical bytes, presentation/default equivalence, source distinctions, array order, the accepted PC3 profile boundary, later-invalid digestibility, output pairing, and authority absence. At semantic-freeze acceptance, no PC5 Rust implementation, dependency change, commit, push, later identity, package phase, Lockfile, Manifest, Builder, runtime, provider, or user surface had started.

The authorized PC5 implementation tranche has written the exact canonical JSON encoder closure, opaque Blueprint digest binding, existing workspace path edges, and focused fixture tests. A bounded totality repair now admits caller-created values to the frozen PC2 value domain before PC3 construction, so every publicly reachable `DefaultedSource` remains canonically encodable without moving declaration validation into PC3 or PC5. Post-repair qualification with the pinned Rust 1.97.1 toolchain passes formatting, frozen all-target compilation, all-feature Clippy with warnings denied, the frozen dependency tree, and all 52 workspace tests: 43 Foundation-through-PC4 regressions and 9 focused PC5 tests. Fixture, golden-hash, controlling-document, prior-conformance, dependency-inventory, and edit-boundary checks also pass without an external package or connection. The final repaired read-only review found P0=0, P1=0, P2=2, and P3=1 and recommended acceptance. PC5 is accepted within the frozen Digest boundary; the P2/P3 findings remain explicit non-blocking debt. Builder, runtime, and PC6 implementation remain unauthorized. The next bounded task is PC6 Package-scan scope reconciliation and semantic freeze.

The accepted Package Scan Semantics Erratum closes the identity-affecting PC6
ambiguities recorded by the preserved scope reconciliation. Its exact reviewed
fourth repaired candidate passed independent read-only review with P0=0, P1=0,
P2=0, and P3=0. PC6 is now semantically frozen around explicit immutable
project-snapshot intake, exhaustive local package discovery and descriptor
admission, declared-file verification, retained-byte continuity, exact
canonical package construction, package content identity, deterministic
diagnostics, and a source-bound non-authoritative scanned result. Rust
qualification was not run for this documentation-only acceptance because the
toolchain was unavailable; exact baseline comparison proves every Rust, Cargo,
PC1-PC5 implementation, and conformance path unchanged. At that
documentation-only gate, PC6 implementation had not started; PC6 was not
accepted, and Builder and runtime remained unauthorized.
The authorized PC6 production implementation now adds the compiler-owned
immutable snapshot boundary, exact global staged Package Scan, opaque
package/source bindings, all 31 diagnostics, retained verified bytes, canonical
package identity construction, focused external tests, and a durable
machine-readable fixture manifest carrying all frozen populations. The
fixture-infrastructure repair adds a closed deterministic plan and Rust
interpreter for all 184 authoritative rows. The accepted-PC2 precedence repair,
exact `REPLACE_HEX` materialization, and final two-file Clippy repair now pass
the complete focused matrix with the isolated Rust 1.97.1 toolchain and cached
dependencies: formatting, 18 PC2 tests, frozen all-target compilation, 13 PC6
tests, all 184 fixtures and 180 public scan runs, all-feature Clippy with
warnings denied, the deterministic plan checker, and textual-diff checks. No
network operation, Cargo/dependency change, production-semantic change,
fixture-authority change, review, acceptance, commit, or push occurred. Full
frozen workspace qualification then passed formatting, workspace all-target
checking, all 67 workspace tests, all-workspace/all-feature Clippy with
warnings denied, frozen dependency-tree resolution, executable-plan closure,
golden population and authority-hash checks, and textual-diff checks. The
workspace tests comprise 54 Foundation-through-PC5 tests and 13 PC6 tests.
All Cargo and lockfile bytes, accepted authorities, source, tests, fixtures,
generator, and executable plan remained unchanged during qualification.
Implementation verification is complete. A separate independent read-only
review reproduced the complete frozen/offline qualification and fixture,
diagnostic, vector, identity, opacity, phase, authority, regression, and
evidence checks. It found P0=0, P1=0, P2=0, and P3=0 and recommended
acceptance. The bounded PC2 explicit-tag diagnostic-precedence repair is
accepted as part of this PC6 candidate. PC6 is accepted within the frozen
Package Scan boundary. Its publication is the accepted baseline for the PC7
gate below. Builder and runtime remain unauthorized.

The earlier second-repair acceptance is retained as history and is superseded
by the completed five-repair semantic and conformance-criteria chain. The
governing fifth-repair review at SHA-256
`6f664ac7218c45be2244bfa029f5ae915a9a53739d5355ef286f1dedeea0aef9`
recomputed PC7-SR4-IR-P1-01 closed and reported P0=0, P1=0, P2=0, and P3=1.
PC7-AJ-P3-01 remains open, dormant, future-only, non-dispatchable, excluded
from current populations, and non-blocking.

The fifth repair is accepted and published as the controlling Standard 0.3
companion only for Resolve and the validation of optionally supplied existing
Lockfile bytes needed by Resolve. Its complete normative region and embedded
manifest remain byte-identical to the reviewed fifth candidate. The exact
standalone manifest remains at maturity `specified`: 118 current fixtures, 45
registered new choices, 15 schema discriminators, and four non-dispatchable
future vectors. The increase from 14 to 15 schema discriminators is the fifth
repair's sole substantive population change.

PC7 semantics are refrozen around the exact opaque ScannedSource plus optional
immutable ExistingLockfileInput, source-bound successful ResolvedSource,
retained PC6 bytes and parsed-module continuity, active-profile eligibility,
per-package lock reuse, arbitrary-size numeric selection, simultaneous
fixed-point passes, contribution retraction, unchanged-pass success, the
256-pass boundary, canonical cycle selection, total diagnostic precedence,
exact logical paths, and non-authority. Resolve creates no identity and does
not generate or persist a Lockfile. No Rust implementation, fixture
interpreter, deterministic plan generator, Cargo change, dependency, Builder,
runtime, provider, installation, CLI, MCP, UI, Android, or product byte changed
in this documentation-only publication. PC7 implementation had already
started before the repair chain, but all earlier focused qualification,
implementation verification, and implementation-review claims are invalidated
against the refrozen authority. The sole active next task is a separate
read-only impact assessment; it authorizes no repository modification.

```text
FOUNDATION_ACCEPTED=true
PC1_ACCEPTED=true
PC2_ACCEPTED=true
PC2_DIAGNOSTIC_PRECEDENCE_REPAIR_COMPLETE=true
PC3_ACCEPTED=true
DEFAULT_ERRATUM_COMPLETE=true
CANONICAL_JSON_ERRATUM_COMPLETE=true
PC4_ACCEPTED=true
PC5_ACCEPTED=true
PACKAGE_SCAN_ERRATUM_ACCEPTED=true
PC6_SCOPE_RECONCILED=true
PC6_SEMANTICS_FROZEN=true
PC6_IMPLEMENTATION_STARTED=true
PC6_FIXTURE_INTERPRETER_COMPLETE=true
PC6_FOCUSED_QUALIFICATION_COMPLETE=true
PC6_IMPLEMENTATION_VERIFICATION_COMPLETE=true
PC6_IMPLEMENTATION_REVIEW_COMPLETE=true
PC6_REVIEW_P0=0
PC6_REVIEW_P1=0
PC6_REVIEW_P2=0
PC6_REVIEW_P3=0
PC6_ACCEPTED=true
PC7_SCOPE_RECONCILED=true
RESOLVE_ERRATUM_CANDIDATE_COMPLETE=true
RESOLVE_ERRATUM_CANDIDATE_REVIEW_COMPLETE=true
RESOLVE_ERRATUM_REPAIR_COMPLETE=true
RESOLVE_ERRATUM_REPAIR_REVIEW_COMPLETE=true
RESOLVE_ERRATUM_SECOND_REPAIR_COMPLETE=true
RESOLVE_ERRATUM_SECOND_REPAIR_REVIEW_COMPLETE=true
RESOLVE_ERRATUM_REVIEW_P0=0
RESOLVE_ERRATUM_REVIEW_P1=0
RESOLVE_ERRATUM_REVIEW_P2=0
RESOLVE_ERRATUM_REVIEW_P3=1
RESOLVE_ERRATUM_ACCEPTED=true
PC7_SEMANTIC_FREEZE_REOPENED=false
PC7_SEMANTIC_AND_CRITERIA_FOURTH_REPAIR_CANDIDATE_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FOURTH_REPAIR_REVIEW_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FIFTH_REPAIR_CANDIDATE_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FIFTH_REPAIR_REVIEW_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_REPAIR_ACCEPTED=true
PC7_SEMANTIC_AND_CRITERIA_REPAIR_PUBLISHED=true
PC7_SEMANTICS_FROZEN=true
PC7_IMPLEMENTATION_STARTED=true
PC7_FIXTURE_INTERPRETER_COMPLETE=true
PC7_FOCUSED_QUALIFICATION_COMPLETE=true
PC7_IMPLEMENTATION_VERIFICATION_COMPLETE=true
PC7_IMPLEMENTATION_REVIEW_COMPLETE=true
PC7_QUALIFICATION_REVIEW_COMPLETE=true
PC7_REVIEW_P0=0
PC7_REVIEW_P1=0
PC7_REVIEW_P2=0
PC7_REVIEW_P3=0
PC7_ACCEPTED=true
PUSH_COMPLETE=true
PC8_STARTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
FIXTURE_MATURITY=qualified
REVIEW_P0=0
REVIEW_P1=0
REVIEW_P2=0
REVIEW_P3=1
NEXT_BOUNDED_TASK=PC8 Lock scope reconciliation and semantic freeze only
```

## 2026-07-28 PC7 implementation-acceptance amendment

This amendment accepts the exact independently qualified six-path PC7 Resolve
implementation and executable-conformance candidate. The accepted candidate
identities are:

| Path | SHA-256 |
|---|---|
| `conformance/pc7/resolve/build_executable_fixture_plan.py` | `02968be53c6403953fe3e7c691a3acd36eba0dc5c6c5ec6462a75e5c2201764b` |
| `conformance/pc7/resolve/executable_fixture_plan.json` | `4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d` |
| `crates/threadsmith-compiler/src/lib.rs` | `00e726435f9b8442da89992971ce18b382c881849401b57693c4c6554a6d9a87` |
| `crates/threadsmith-compiler/src/resolve.rs` | `bc9a8e8718702ffd9ef1077cf9c4da3c731f0faee27865bdb80405a535f9c2ca` |
| `crates/threadsmith-compiler/tests/pc7_resolve.rs` | `df7d77543102979f8fd02e991a547d9cd2e1ff339a4f753b7d475110d5e533f1` |
| `crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs` | `3efdbfe63ec403b737e05a0444956efe09e3d059d2a4b064a9622f65976fe326` |

Acceptance is controlled by the semantic-publication report at SHA-256
`48a9cb9b90e83397ede415515574ece94a64d78f05585d48aaf074f5ae2710e8`,
the final implementation repair at
`c4e26cd22737a2e807a5d23b2ca8323e5fcc7460d0a494439c47d70bb2c12600`,
the implementation re-review at
`710fec8d3b48aeeee57da272bf2d5f0062840fb809b01aa2e34f0e150517668e`,
the refreshed focused qualification at
`1c4ecf8ec5ea238ca4b833d28b3f575592c547decd511434fc7253c26768be27`,
and its independent review at
`8bc60be961f2a81fdf7ac82ae1ecaf2d7dd2bb05e7c39d555f23e1e73b69605d`.
The last review records `RECOMPUTED=168`, no derived, refuted,
underdetermined, or unverified claim, P0=0, P1=0, P2=0, P3=0, and disposition
`PASS`.

The final acceptance regression used the already available Rust 1.97.1
toolchain, cached dependencies, offline Cargo operation, repository-external
targets, and repository-external Python caches. Formatting, workspace
all-target checking, 78 of 78 complete workspace tests, all-target/all-feature
Clippy with warnings denied, frozen dependency-tree resolution, 11 of 11
unfiltered PC7 tests, generator rejection self-tests, checked-plan
verification, Python syntax checking, two authenticated disposable
regenerations, and Git textual-diff checks all passed with zero failures,
ignores, or filters.

All 118 defined current fixture IDs equal the 118 generated plan IDs and the
118 public-boundary executed IDs. Exactly four future vectors remain excluded
and non-dispatchable. The fixture-ID preimage is 2,576 bytes with SHA-256
`ab7b72bdb33a255d2539a204cd880fa7aedab61b8672cfa3f02d8342d510f221`.
Both regenerated plans equal each other and the checked 34,460,681-byte plan
at SHA-256
`4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d`.
Fixture maturity is therefore `qualified` for the frozen PC7 Resolve scope.

Acceptance remains limited to opaque PC6 `ScannedSource` plus optional
immutable existing-Lockfile input through the frozen Resolve outcome. It
creates no Lockfile, `lock_id`, Manifest, Binding, authority, persistence,
installation, provider, model, network, Builder, runtime, CLI, MCP, UI,
Android, or other product behavior. The historical dormant future-only
semantic finding remains `RESOLVE_ERRATUM_REVIEW_P3=1`; it is not a PC7
implementation or qualification-review finding and is neither closed nor
reclassified here.

Publication is limited to one normal non-force fast-forward update of
`refs/heads/main` containing the six reviewed candidate paths and the four
durable acceptance paths. The commit, tree, remote, and push identities are
self-excluded from repository state and belong only in the external operator
report. This durable record becomes accepted publication authority only when
that exact commit is published. PC8 remains unstarted, Builder and runtime
remain unauthorized, and the sole next bounded task is PC8 Lock scope
reconciliation and semantic freeze only.
