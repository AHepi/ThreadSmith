# ThreadSmith Foundation/PC1 Restoration Decisions

Document status: reconstructed on 2026-07-22 from the supplied recovery evidence.

| Decision | Resolution | Evidence and boundary |
|---|---|---|
| R-001 | Restore a two-crate Rust workspace only. | The recovered root manifest names `threadsmith-schema` and `threadsmith-canonical`; it does not name a migration crate. |
| R-002 | Place the recovered schema source at `crates/threadsmith-schema/src/lib.rs`. | This is a high-confidence reconstructed placement based on its schema API and its explicit reference to `threadsmith-canonical`. The source bytes remain exact. |
| R-003 | Place the recovered PC1 model at `conformance/pc1/core_model.json` and ADR 0001 at `docs/adr/0001-portable-core-language.md`. | These are reconstructed placements; neither original directory survived. The file bytes remain exact. |
| R-004 | Reconstruct the minimum canonical preimage machinery from converging supplied evidence. | The root dependency set, recovered schema API contract, recovered ADR, PC1 model, and observable legacy-oracle behavior support NFC-normalized, sorted, compact UTF-8 JSON and SHA-256 typed claims. The API does not select artifact-specific preimages, validate artifacts, or grant authority. This is not claimed to be the lost source. |
| R-005 | Reject absent identity preimages. | The PC1 model explicitly marks blueprint and manifest preimages unresolved, and the recovered schema defines `IDENTITY_PREIMAGE_UNRESOLVED`. |
| R-006 | Keep native and legacy authority distinct. | The recovered schema source is controlling evidence. Legacy claims remain representable for comparison but cannot grant authority; migration receipts always have `AuthorityEffect::None`. |
| R-007 | Do not place the legacy wheel in the public repository. | Its bytes and RECORD verify, but its original ThreadSmith path, licence, and redistribution provenance are unresolved. Its SHA-256 remains recorded and checked externally. |
| R-008 | Preserve the zero-byte directive exactly without interpreting it. | The supplied object contains no substantive directive content. Its absence remains an unresolved gap. |
| R-009 | Do not recreate Lattice Standard 0.3 from the legacy wheel. | The Standard was not supplied, and the wheel is an oracle rather than native semantic authority. |
| R-010 | Stop at PC1. | YAML, parser selection, compiler, runtime, builder, provider, UI, CLI/MCP, Android, and all PC2 work remain excluded. |
| R-011 | Keep artifact-specific blueprint and manifest identity calculation unresolved. | The recovered PC1 model says both preimages are unresolved, the Standard is missing, and the manifest compiler-exclusion rule alone is insufficient to reconstruct every artifact preimage safely. |
| R-012 | Preserve recovered migration-receipt behavior without widening it. | Receipts always remain non-authoritative. The recovered source does not constrain `RequiredNextAction` by outcome; this is recorded as an unresolved nonblocking gap rather than silently changed. |

## PC2 parser intake decisions

These decisions are new PC2 preparation, not reconstructed Foundation/PC1 history.

| Decision | Resolution | Boundary |
|---|---|---|
| PC2-I-001 | Select `saphyr-parser =0.0.11` with default features disabled and consume only its low-level event API. | The future `threadsmith-compiler` owns projection and validation. No dependency is added during intake. |
| PC2-I-002 | Freeze a strict YAML 1.2 subset to one UTF-8 document and a JSON-shaped NFC-normalized tree. | Anchors, aliases, tags, directives, document markers, merge keys, complex keys, and block scalars are forbidden. |
| PC2-I-003 | Keep scalar interpretation narrower than the dependency. | Only null, booleans, bounded decimal integers, and strings exist; floats and alternate numeric forms are rejected unless quoted as strings. |
| PC2-I-004 | Reject duplicate decoded keys and distinct keys that collide after NFC at every mapping depth. | Validation occurs before unknown-root checks or default injection; arrays retain source order. |
| PC2-I-005 | Freeze the Blueprint root envelope. | `profile`, `module`, `version`, and `purpose` are required. `imports`, `resources`, `contracts`, `units`, `links`, `policies`, and `scenarios` default to empty lists. No other root key is accepted. |
| PC2-I-006 | Keep PC1 defaults profile-owned. | A source `defaults` root is rejected; the parser injects only absent optional empty lists. |
| PC2-I-007 | Preserve the portable-core unit-kind gate. | `program`, `model`, `gate`, `controller`, and `broker` are accepted; Extended-only and unknown kinds are rejected without compiling. |
| PC2-I-008 | Freeze first-error diagnostic behavior independently of upstream wording. | Stable output is code, JSON Pointer path, and one-based source position, using a fixed validation order. |
| PC2-I-009 | Preserve authority boundaries. | Parsing creates no identity, hash, Manifest, resolution, qualification, Binding, executable artifact, or authority. |
| PC2-I-010 | Record third-party execution surfaces explicitly. | `arraydeque` contains internal Rust `unsafe`; `thiserror`, `proc-macro2`, and `quote` have pinned build scripts that probe the selected `rustc`. The graph has no native FFI, system libyaml, C/C++ compiler, or system-library probe. Any version, feature, source, script, or graph change reopens intake. |
