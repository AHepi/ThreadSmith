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

## PC3 scope-reconciliation decisions

These decisions freeze preparation only. They do not implement or accept PC3 product code.

| Decision | Resolution | Boundary |
|---|---|---|
| PC3-S-001 | Assign PC3 exactly the Standard `Source validate` phase, whose output is `Valid root shape`. | The explicit output prevents declaration normalization or cross-declaration static checking from being pulled forward. |
| PC3-S-002 | Keep ownership in `threadsmith-compiler` and represent success conceptually as a non-authoritative wrapper over the unchanged PC2 value. | `threadsmith-schema` remains data structures; PC3 creates no identity, artifact, Manifest, Binding, or authority. |
| PC3-S-003 | Validate the exact root allowlist, six required keys, metadata scalar categories, Core lattice/profile selectors, module-name grammar, Core version form, and declaration-list container categories. | PC3 applies no declaration-element validation and no defaults. |
| PC3-S-004 | Preserve absent versus explicit members and every array order without mutation. | Standard section 16 insertion belongs to `Default`; canonical collection ordering belongs to `Sort`. |
| PC3-S-005 | Freeze first error as root type, UTF-8-sorted unknown key, Standard-ordered missing key, then Standard-ordered invalid root value. | Diagnostics use stable code and RFC 6901 path; source positions are unavailable at the accepted PC2 value boundary. |
| PC3-S-006 | Defer declaration forms, name uniqueness, unit-profile checks, references, contracts, ports, links, policies, routes, controls, budgets, secrets, and completeness. | Deferral is not semantic acceptance; later lifecycle intakes must allocate and freeze these rules. |
| PC3-S-007 | Add no dependency during scope freeze. | Existing JSON data and standard Rust operations suffice; any dependency reopens licence and provenance intake. |

## PC3 implementation decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC3-P-001 | Expose `validate_blueprint_source(Value) -> Result<ValidatedSource, SourceDiagnostic>` in `threadsmith-compiler`. | The caller supplies accepted PC2 data; PC3 neither reparses YAML nor revalidates PC2 syntax. |
| PC3-P-002 | Keep `ValidatedSource.value` private and expose only immutable borrowing and consuming extraction. | The wrapper proves only frozen root shape and carries no identity, canonical-byte, Manifest, Binding, or authority meaning. |
| PC3-P-003 | Reuse `SourceDiagnostic` with PC3 positions always absent. | PC3 owns only its four frozen codes and RFC 6901 path; it does not reuse later compiler errors. |
| PC3-P-004 | Implement name and version recognition with standard Rust operations. | No regex/parser dependency or Cargo graph mutation is required. |
| PC3-P-005 | Treat declaration array elements as opaque and return the input value unchanged. | No defaults, declaration validation, profile unit-kind gate, resolution, or static checking enters PC3. |

## Lattice Standard 0.3 Default Semantics Erratum decisions

These decisions resolve only ambiguities already present in Standard section 16. They do not implement PC4 or authorize any later phase.

| Decision | Resolution | Boundary |
|---|---|---|
| PC4-E-001 | Preserve the recovered Standard bytes and record a separate normative Default Semantics Erratum. | Only the four authorized ambiguity classes are clarified; every unaffected Standard rule remains controlling. |
| PC4-E-002 | Expand a missing link or policy `when` to `{"all":[]}`. | The existing empty-`all` rule supplies constant true; controller transition triggers and other fields are not default targets. |
| PC4-E-003 | Own model fallback at `units[*].fallback` for exact `kind: model` and encode the default as JSON `false`. | Source fallback grants no authority and does not replace Run Binding reconciliation. |
| PC4-E-004 | Apply input defaults to root inputs and unit input ports; apply output cardinality to root exports and unit output ports. | Expansion occurs before imports and does not search arbitrary nested data. |
| PC4-E-005 | Treat object-member presence as absolute explicit-value precedence, even for empty, null, contradictory, wrong-type, or later-invalid values. | PC4 neither repairs nor validates present data; later phases retain responsibility. |
| PC4-E-006 | Leave non-object elements and invalid nested containers unchanged; omit kind-dependent defaults when unit kind is missing, non-string, or unknown. | PC4 remains deterministic and non-validating while unambiguous defaults at other exact targets still apply. |
| PC4-E-007 | Insert no provenance or convenience metadata and require idempotent expansion. | Omitted and explicit default values converge to one post-default identity preimage; explicit non-default values remain distinct. |
| PC4-E-008 | Require exhaustive exact-value, preservation, invalid/deferred, idempotence, and identity-preimage fixtures in the later PC4 freeze. | The erratum defines fixture obligations but creates no PC4 fixture or product implementation. |

## PC4 Default-phase scope-reconciliation decisions

These decisions freeze preparation only. They do not implement or accept PC4 product code.

| Decision | Resolution | Boundary |
|---|---|---|
| PC4-S-001 | Assign PC4 exactly the Standard `Default` phase between PC3 and PC5. | PC4 consumes `ValidatedSource`; PC5 Digest is the only immediate downstream phase. |
| PC4-S-002 | Keep ownership in `threadsmith-compiler` and freeze the conceptual output type as `DefaultedSource`. | The wrapper contains only the expanded JSON-shaped value and is non-authoritative. |
| PC4-S-003 | Apply every target, exact value, traversal rule, and malformed-data rule from the accepted Default Semantics Erratum without reinterpretation. | Resolved erratum decisions are not reopened or extended. |
| PC4-S-004 | Retain no serialized provenance, source-presence ledger, default marker, source span, diagnostic, compiler metadata, or sidecar. | Only expanded values reach the PC5 identity preimage; wrapper type state is non-serialized. |
| PC4-S-005 | Own no PC4 semantic diagnostic. | PC3-invalid roots cannot enter through `ValidatedSource`; later-invalid declaration data is preserved for later owners. |
| PC4-S-006 | Preserve explicit members absolutely and preserve malformed or ambiguous elements while still applying independent unambiguous defaults. | PC4 expansion is total, deterministic, non-validating, and idempotent. |
| PC4-S-007 | Freeze nine exact input/output fixtures plus equality and distinction groups. | The future public implementation must replay every case, reapply defaults, preserve array order, and insert no unlisted field. |
| PC4-S-008 | Defer canonical bytes, hashing, identities, packages, resolution, Lockfiles, expansion, normalization, static checks, Manifests, qualification, Binding, and runtime. | PC4 prepares identity-bearing data but creates neither identity nor authority. |

## PC4 Default-phase implementation decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC4-P-001 | Expose `apply_blueprint_defaults(ValidatedSource) -> DefaultedSource` in `threadsmith-compiler`. | PC4 consumes only PC3-validated root data and cannot parse or repeat root validation. |
| PC4-P-002 | Keep `DefaultedSource.value` private and expose only immutable borrowing and consuming extraction. | The wrapper proves only that frozen expansion ran; it carries no serialized metadata, identity, artifact, or authority meaning. |
| PC4-P-003 | Use exact object-member presence to decide insertion and preserve all present values unchanged. | Empty, null, wrong-type, contradictory, and later-invalid values retain explicit precedence and remain for later owners. |
| PC4-P-004 | Traverse only the frozen root arrays and unit port arrays, preserving array order and ignoring non-object elements or invalid containers. | PC4 performs no recursive convenience defaulting and emits no later-phase validation diagnostic. |
| PC4-P-005 | Dispatch kind-dependent defaults only for exact recognized string kinds while applying independent port defaults separately. | Missing, non-string, or unknown kinds receive no mode, repair, or fallback inference. |
| PC4-P-006 | Represent constant true by constructing the accepted JSON value `{"all":[]}` at each absent link or policy predicate target. | PC4 adds no predicate operator, evaluation behavior, route, permission, or runtime meaning. |
| PC4-P-007 | Test equality of post-default JSON values without implementing identity machinery. | Omitted and explicit defaults converge; explicit non-defaults differ, while PC5 canonicalization and digest remain unstarted. |
| PC4-P-008 | Add no dependency, diagnostic, canonical serializer, digest, identity API, or authority mechanism. | PC4 remains deterministic identity preparation only; PC5 and every later phase require separate authorization. |
