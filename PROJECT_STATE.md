# ThreadSmith Project State

State record status: reconstructed. Updated 2026-07-23.

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
| Builder authorized | false |
| Runtime authorized | false |
| Next bounded task | PC6 Package-scan scope reconciliation and semantic freeze |

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
