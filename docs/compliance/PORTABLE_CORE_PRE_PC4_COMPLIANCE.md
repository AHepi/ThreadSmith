# Portable Core Pre-PC4 Compliance Check

Review date: 2026-07-22.

Status: compliance review complete; no PC4 scope or implementation work is included.

## Baseline and controlling evidence

The review began from clean local and remote `main` at commit
`394a3cf4f0c60b650d6c32dc5544b59aff54109a`, tree
`ebf871ceb2667c0bd796a8eba17e8ec8a98a275a`.

| Evidence | Role |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Controlling Lattice semantics; SHA-256 `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| YAML 1.2.2 sections 5.1 and 5.7 | Referenced syntax definition for printable/quoted characters and escape decoding |
| `docs/pc2/PC2_STANDARD_RECONCILIATION.md` and `docs/pc2/PARSER_SEMANTIC_FREEZE.md` | Accepted PC2 ownership and parser contract |
| `docs/pc3/PC3_SCOPE_RECONCILIATION.md` and `docs/pc3/PC3_SEMANTIC_FREEZE.md` | Accepted PC3 ownership and preservation contract |
| `crates/threadsmith-compiler/src/lib.rs` and focused tests | Current public PC2/PC3 execution paths |
| `docs/adr/0001-portable-core-language.md`, `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md` | Rust ownership, state, tranche, and durable-decision boundaries |

## Phase compliance

| Concern | Finding |
|---|---|
| PC2 ownership | `parse_blueprint_source` performs UTF-8/restricted-YAML parsing, JSON projection, NFC normalization, key-collision checks, and deterministic source diagnostics only. |
| PC3 ownership | `validate_blueprint_source` checks only the Core root envelope and returns `ValidatedSource` over the unchanged PC2 value. |
| Default leakage | None. Absent members remain absent; explicit empty and explicit values remain present; no root, port, unit, link, predicate, fallback, or scenario default is inserted. |
| Later phases | No package scan, resolution, Lockfile generation, digest, identity, import expansion, declaration normalization, insertion, static checking, Manifest, persistence, qualification, Binding, or runtime behavior exists in `threadsmith-compiler`. |
| Data preservation | PC2 preserves member presence, explicit values, JSON categories, and array order. PC3 returns value equality and does not mutate or discard that information. Source positions are not retained, but the Standard does not require them at this boundary. |
| Authority | Compiler APIs create neither identity nor authority. `ValidatedSource` explicitly carries only a non-authoritative root-shape guarantee. Existing Foundation schema representations do not constitute compiler-produced Lockfiles or Manifests. |
| Errors | PC2 owns parser errors; PC3 owns root-envelope errors. PC3 does not emit later Standard errors. Additional ThreadSmith codes remain permitted by Standard section 36 and do not change a Standard code's meaning. |
| Determinism | Parser diagnostic precedence, root-validation precedence, object projection, array preservation, duplicate/NFC rejection, and repeated results are covered by focused tests. |

## Standard deviation and repair

| Severity | Classification | Finding | Resolution |
|---|---|---|---|
| P1 | Bug | PC2 rejected YAML 1.2 escape-decoded C0/DEL/C1 string content and raw non-C0 characters even inside quoted scalars. The Lattice forbidden-feature list adds no such decoded-value restriction, and this rejection created a narrower ThreadSmith-only string language. | Repaired by separating raw YAML presentation validity from decoded JSON string content. Valid double-quoted escapes and JSON-compatible quoted characters are preserved; invalid raw non-printable characters outside quoted scalars still produce `SOURCE_FORBIDDEN_YAML`. A conformance fixture and focused regression cover the boundary. |
| P0 | — | None. | — |
| P2 | — | None. | — |
| P3 | — | None. | — |

Compatibility impact: previously rejected Standard-valid strings now parse successfully. Invalid raw non-C0 characters outside quoted scalars remain rejected, with the corrected parser-owned `SOURCE_FORBIDDEN_YAML` code instead of the former `SOURCE_INVALID_UTF8` classification. The repair does not change the value produced for previously accepted source, relax anchors/tags/aliases/floats/non-string keys/duplicates/collisions, add a dependency, or alter PC3 behavior.

## Verification

All commands used Rust 1.97.1 with `--locked --offline` where applicable.

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | pass |
| `cargo check --workspace --all-targets --locked --offline` | pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | pass |
| `cargo test --workspace --all-targets --locked --offline` | pass: 40 tests, 0 failed |
| Foundation canonical tests | pass: 7 |
| PC1 conformance tests | pass: 5 |
| Foundation schema/authority tests | pass: 5 |
| PC2 parser tests | pass: 16 |
| PC3 source-validation tests | pass: 7 |
| Fixture JSON, unique IDs, and referenced paths | pass: 16 cases |
| Cargo dependency tree and metadata resolution | pass; compiler graph unchanged |
| Standard, root Cargo, lockfile, and ADR hashes | unchanged |
| `git diff --check` | pass |

## Review conclusion

The corrected worktree is semantically ready for a separately authorized PC4 scope reconciliation. The repair is not committed or pushed by this review because no delivery action was authorized. If remote `main` remains the required provenance source, this repair must be accepted and published before PC4 work begins from that remote baseline.
