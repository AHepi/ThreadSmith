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

The later `PC2-R-*` reconciliation decisions supersede entries in this section and the implementation section wherever the recovered Standard proves a conflict. The original entries remain visible as historical provenance rather than active semantics.

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

## PC2 parser implementation decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC2-P-001 | Add `threadsmith-compiler` and expose `parse_blueprint_source(&[u8]) -> Result<serde_json::Value, SourceDiagnostic>`. | The result is a non-authoritative source projection; no compiler output or identity API exists. |
| PC2-P-002 | Run a complete event audit before scalar projection. | This preserves the frozen global precedence of YAML syntax and forbidden-feature diagnostics over scalar and tree validation. |
| PC2-P-003 | Retain decoded pre-NFC mapping keys until duplicate and collision checks finish. | Equal decoded keys produce `SOURCE_DUPLICATE_KEY`; distinct decoded keys with one NFC form produce `SOURCE_NFC_COLLISION` at every depth. |
| PC2-P-004 | Keep diagnostics to code, RFC 6901 path, and optional one-based source position. | Upstream parser prose is not exposed as a stable field. |
| PC2-P-005 | Inject only the seven absent optional root lists and perform only the frozen root-envelope and portable unit-kind gates. | Scenario sufficiency, wiring, packages, contracts, policies, routes, and other compiler semantics remain out of scope. |
| PC2-P-006 | Commit the exact `saphyr-parser =0.0.11` pin with default features disabled and the resolved Cargo lock. | The resolved graph matches intake; any version, feature, source, script, or licence change reopens dependency review. |
| PC2-P-007 | Do not create a PC2 tag. | The existing tag names the reconstructed Foundation/PC1 provenance anchor; PC2 is a bounded capability acceptance, not a release or replacement baseline policy. |

## PC2 Standard reconciliation decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC2-R-001 | Treat the recovered Lattice Standard 0.3 as controlling and preserve its supplied bytes under `docs/standard/`. | Earlier PC2 source decisions are superseded only where the Standard proves a conflict; Foundation/PC1 evidence remains historical and unchanged. |
| PC2-R-002 | Restrict PC2 ownership to `Read`/`Parse` projection and remove root, declaration, profile, and default behavior. | PC3 owns `Source validate`; the later `Default` phase owns insertion. PC2 success is not Blueprint acceptance. |
| PC2-R-003 | Preserve absent object members exactly and retain explicitly supplied empty lists. | The `serde_json::Value` boundary remains sufficient once default injection is removed; no enriched source representation is needed for the frozen PC3 input. |
| PC2-R-004 | Use YAML 1.2 Core plain-scalar resolution, reject floats, and require resolved integers to fit signed `i64`. | This implements the Standard's JSON-shaped scalar categories without retaining the former decimal-only/positive-`u64` dialect. |
| PC2-R-005 | Accept literal block strings, explicit string keys, matching YAML core JSON-category tags, one marked document, and an optional YAML 1.2 directive. | Folded strings, multiple documents, custom/tag directives, custom or mismatched tags, anchors, aliases, merge keys, and non-string keys remain parser-level errors. |
| PC2-R-006 | Keep deterministic parser diagnostics but retire root/profile/default codes from PC2. | Later phases may use the Standard's stable compiler codes; PC2 exposes only parser-boundary codes. |
| PC2-R-007 | Keep `saphyr-parser =0.0.11` and the accepted lock graph unchanged. | No dependency, licence, native, FFI, offline, or reproducibility policy is reopened. |
| PC2-R-008 | Supersede incompatible fixtures instead of preserving false acceptance evidence as active conformance. | Historical PC2 ledgers and reports remain unchanged and continue to describe their original accepted trees. |
