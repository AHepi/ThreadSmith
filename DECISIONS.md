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

## Lattice Standard 0.3 Canonical JSON Erratum decisions

These decisions close canonical byte encoding for Standard 0.3 without
implementing PC5 or selecting any additional artifact preimage.

| Decision | Resolution | Boundary |
|---|---|---|
| PC5-E-001 | Preserve the recovered Standard bytes and record a separate normative Canonical JSON Erratum. | Only byte encoding is clarified; every artifact-specific preimage and unaffected Standard rule remains controlling. |
| PC5-E-002 | Encode canonical JSON as one compact UTF-8 sequence with no BOM, insignificant whitespace, or trailing newline. | No wrapper, path, metadata, length prefix, NUL, or stage marker is added implicitly. |
| PC5-E-003 | Normalize object keys to NFC and order them by ascending unsigned UTF-8 bytes before escaping; preserve arrays unless an earlier semantic phase explicitly sorted them. | Canonical JSON never performs declaration or semantic collection sorting. |
| PC5-E-004 | Freeze quotation mark, reverse solidus, five short control escapes, lowercase `\u00xx` for every other C0 control, direct solidus, and direct UTF-8 for every other scalar. | Optional JSON escaping, non-ASCII `\uXXXX`, surrogate-pair escaping, and escaped solidus are non-conforming. |
| PC5-E-005 | Encode every integer already admitted by its owning schema in minimal ASCII base ten and encode booleans/null in lowercase. | PC5 remains signed-`i64` because PC2 established that input boundary; the erratum does not narrow the accepted Foundation generic arbitrary-integer preimage domain. |
| PC5-E-006 | Treat unpaired surrogates and NFC-colliding object keys as internal invariant violations with no canonical representation. | Accepted PC2-to-PC5 values make both states unreachable; no new PC5 source diagnostic is created. |

## PC5 Digest-phase scope-reconciliation decisions

These decisions freeze preparation only. They do not implement or accept PC5
product code.

| Decision | Resolution | Boundary |
|---|---|---|
| PC5-S-001 | Assign PC5 exactly the Standard `Digest` phase between PC4 Default and Package scan. | PC5 consumes only `DefaultedSource`; it does not repeat parsing, validation, or defaulting. |
| PC5-S-002 | Define the Blueprint preimage as exactly canonical JSON of the complete post-default root before import expansion. | Original YAML, wrappers, files, paths, diagnostics, provenance, compiler metadata, and expanded imports are excluded unless represented as source values. |
| PC5-S-003 | Create exactly one identity in PC5: `lattice:blueprint:sha256:<64 lowercase hex>`. | Package, declaration, Lockfile, Manifest, qualification, Binding, envelope, event, and every other identity remain deferred. |
| PC5-S-004 | Keep phase ownership and source binding in `threadsmith-compiler` while reusing `threadsmith-canonical` and the accepted PC1 native identity vocabulary. | A second canonical encoder, hash path, identity format, or authority meaning is forbidden. |
| PC5-S-005 | Freeze opaque `BlueprintDigest` and private-field `DigestedSource { defaulted_source, blueprint_digest }`, constructible only by consuming PC4 input through `digest_source`. | No public constructor, deserializer, or mutation may pair source A with source B's digest. A caller-created generic PC1 `NativeLatticeId` claim is not a PC5-produced `BlueprintDigest`. The wrapper and canonical bytes do not enter the preimage. |
| PC5-S-006 | Make PC5 semantically total and source-diagnostic-free over accepted `DefaultedSource`. | Internal encoding impossibility is a compiler defect; it is not a normal source result or partial success. |
| PC5-S-007 | Digest duplicate names, invalid kinds, malformed declarations, unknown references, wrong-type explicit values, and unresolved imports without validating them. | `SOURCE_DUPLICATE_NAME` and all later semantic failures remain for a later explicitly frozen owner. Digestibility is not acceptance. |
| PC5-S-008 | Preserve every array order and every value in the identity preimage; equate only sources that PC2-PC4 reduce to equal `DefaultedSource` values. | PC5 does not predict or impose later Manifest normalization or sorting. |
| PC5-S-009 | Prove root-profile participation at the canonical-preimage layer while requiring public PC5 tests to respect PC3's exact Core-profile gate. | An alternate profile cannot be forged into `DefaultedSource`; it is separately rejected by PC3. |
| PC5-S-010 | Keep canonical bytes out of the new PC5 output and initial PC5-specific public API while binding exact byte hex and hashes in conformance fixtures. | Existing generic canonical testability remains; no PC5 metadata or audit surface is invented. |
| PC5-S-011 | Freeze exact canonical, equivalence, distinction, later-invalid, binding, repeatability, and non-authority fixtures before implementation. | The fixture contract creates no Rust function, dependency, artifact, identity, or execution authority. |

## PC5 Digest-phase implementation decisions

These decisions record implementation choices only. Their later verification,
independent review, and acceptance are recorded by separate gates below.

| Decision | Resolution | Boundary |
|---|---|---|
| PC5-P-001 | Replace delegation to generic JSON serialization with one exact writer inside `threadsmith-canonical`. | The existing public canonical API and SHA-256 owner remain unchanged; the writer closes only erratum bytes. |
| PC5-P-002 | Encode integers from `serde_json::Number::as_str`, rejecting floating syntax and normalizing only negative zero. | The existing `arbitrary_precision` Foundation domain remains intact while PC5 inputs remain signed `i64`. |
| PC5-P-003 | Normalize keys, sort their UTF-8 bytes before escaping, reject normalized collisions, and preserve arrays recursively. | Canonical encoding performs no semantic collection sort or declaration validation. |
| PC5-P-004 | Add only existing `threadsmith-canonical` and `threadsmith-schema` workspace path edges to `threadsmith-compiler`. | Cargo.lock records only those local dependency edges; the external graph is unchanged. |
| PC5-P-005 | Wrap the canonical Blueprint-kind `NativeLatticeId` in private-field `BlueprintDigest`. | Generic caller-created native claims retain their PC1 meaning but cannot become PC5-produced digests through the public API. |
| PC5-P-006 | Construct private-field `DigestedSource` only through `digest_source(DefaultedSource)`. | No constructor, deserializer, mutation, or replacement can publicly pair an independent source and digest. |
| PC5-P-007 | Treat canonical encoding failure for public PC5 input as an internal invariant failure. | PC5 returns no `SourceDiagnostic` and does not validate duplicate names or any later-invalid declaration content. |
| PC5-P-008 | Keep canonical bytes transient and expose only immutable digest/source borrows plus consuming source recovery. | No canonical-byte metadata, provenance, authority, artifact, or later identity is stored. |
| PC5-P-009 | At the earlier unavailable-toolchain checkpoint, stop rather than installing software or using non-Rust substitutes as acceptance evidence. | Fixture/hash/static checks were recorded separately at that checkpoint; verification later completed after the pinned toolchain was restored. Review and acceptance remain separate gates. |

## PC5 Digest-phase totality repair decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC5-R-001 | Admit caller-created `serde_json::Value` input to the frozen PC2 value domain before PC3 root validation can construct `ValidatedSource`. Reject failure with `SOURCE_VALUE_DOMAIN_INVALID`. | This is phase-input domain admission, not declaration validation or a PC5 diagnostic. Genuine PC2 output and frozen PC3 diagnostic precedence are unchanged. |
| PC5-R-002 | Walk arrays by increasing index and objects by ascending raw UTF-8 key bytes, depth first. Check each object's key set before its child values; report the later raw-sorted key for a post-NFC collision and otherwise the first raw-sorted non-NFC key. | Diagnostic paths use the existing RFC 6901 pointer representation and have no source line or column because raw values carry no source coordinates. |
| PC5-R-003 | Reject non-NFC strings or keys, non-minimal/non-`i64` numbers, and post-NFC key collisions without normalizing or mutating caller input. | `digest_source(DefaultedSource) -> DigestedSource`, the canonical writer, digest preimage, declaration-validation ownership, and later-phase semantics are unchanged. |

## PC5 Digest-phase acceptance decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC5-A-001 | Accept the verified, totality-repaired PC5 implementation after its final independent read-only review reported P0=0, P1=0, P2=2, and P3=1. | Qualification passed 52 tests with the pinned Rust 1.97.1 toolchain; no acceptance-blocking finding remains. |
| PC5-A-002 | Retain the two generic/test-hardening P2 findings and the rustdoc P3 finding as explicit non-blocking debt. | Acceptance neither conceals nor repairs that debt and does not change canonical bytes, the Blueprint preimage, source binding, or phase ownership. |
| PC5-A-003 | Accept PC5 only within the frozen `DefaultedSource -> digest_source -> DigestedSource` boundary. | Acceptance creates no package, Lockfile, Manifest, qualification, Binding, Builder, runtime, provider, or execution authority. |
| PC5-A-004 | Require PC6 Package scan to undergo its own scope reconciliation and semantic freeze before any implementation. | PC5 acceptance does not authorize PC6 implementation or any later compiler or product layer. |

## PC6 Package Scan erratum-acceptance decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC6-E-001 | Accept the exact fourth repaired Package Scan candidate as the normative Standard 0.3 companion after its independent review reported P0=0, P1=0, P2=0, and P3=0. | Acceptance records supplied review evidence and is not another independent review. |
| PC6-E-002 | Preserve the candidate's complete normative algorithm, diagnostic vocabulary and precedence, fixture model, authoritative bytes, golden vectors, package identities, and expected outcomes. | Only procedural header, review-history, acceptance-disposition, and final-state wording may change. |
| PC6-E-003 | Record both the reviewed-candidate SHA-256 and the final accepted-companion SHA-256 in the acceptance verification evidence. | The accepted file does not contain its own self-referential hash. |
| PC6-E-004 | Preserve the original Standard, Default Semantics Erratum, Canonical JSON Erratum, ADR, and PC1-PC5 authority unchanged. | The companion closes Package Scan omissions only. |

## PC6 Package Scan semantic-freeze decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC6-S-001 | Assign PC6 exactly the Standard `Package scan` phase between PC5 Digest and Resolve. | PC6 consumes `DigestedSource`; Resolve is the only immediate downstream phase. |
| PC6-S-002 | Require an explicit complete immutable portable snapshot bounded to exact lookup of the optional `packages` subtree. | Ambient directories, environment variables, source content, live rereads, and runtime authority cannot supply the snapshot. |
| PC6-S-003 | Own exact local discovery, descriptor parsing and schema admission, directory agreement, declared-path admission, metadata no-link audit, and declared-file verification. | PC6 neither selects a version nor parses imported module meaning. |
| PC6-S-004 | Bind every admitted package descriptor and identity to the exact immutable bytes verified for every declared logical path. | Later phases consume retained content only; source, identity, and bytes have no mismatch constructor. |
| PC6-S-005 | Construct the exact six-member canonical package descriptor and create the sole phase-produced `lattice:package:sha256:...` identity. | Package identity proves content identity only and grants no authority. |
| PC6-S-006 | Return one deterministic primary diagnostic from the accepted 31-code vocabulary and no partial scanned result. | Snapshot-acquisition and operational exhaustion failures remain non-semantic failures outside `PackageScanOutcome`. |
| PC6-S-007 | Bind the ordered scanned packages to the exact consumed `DigestedSource` in a non-authoritative `ScannedSource`. | No public construction, deserialization, replacement, mutation, live path, or capability may break the binding. |
| PC6-S-008 | Defer Resolve, version selection, Lockfile behavior, import expansion, declaration validation, normalization, static checking, declaration identities, Manifest, qualification, Binding, runtime, providers, installation, networking, and authority. | Deferral is not acceptance and does not allocate incomplete later-phase semantics to PC6. |
| PC6-S-009 | Treat Rust unavailability as non-blocking for this documentation-only gate after exact baseline-tree comparison proves all compilable, Cargo, implementation, and PC1-PC5 conformance inputs unchanged. | No Rust command, installation, dependency resolution, or implementation qualification is claimed. |
| PC6-S-010 | Set the next bounded task to PC6 Package Scan implementation only. | PC6 implementation remains unstarted and PC6, Builder, and runtime remain unaccepted or unauthorized. |

## PC6 Package Scan implementation decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC6-P-001 | Add `package_scan` as a private compiler module and re-export only the frozen public boundary. | PC2-PC5 functions and behavior remain unchanged; Resolve and later phases are not introduced. |
| PC6-P-002 | Model snapshot acquisition input as owned immutable object-class nodes and names, then consume it into a private portable tree sorted by NFC UTF-8 bytes. | The API represents only the exact optional `packages` child; unrelated project-root entries and ambient filesystem access are absent. |
| PC6-P-003 | Keep `SnapshotAcquisitionError` separate from `PackageScanDiagnostic`. | Unrepresentable names, malformed UTF-16, namespace aliasing, incomplete views, concurrent mutation, exhaustion, and inconsistent host state create no semantic PC6 outcome. |
| PC6-P-004 | Execute structural discovery, parser, shallow schema, collections, metadata audit, declared-file verification, and canonical derivation as global passes. | Every pass completes across candidates before the next begins; structural UTF-8 order and successful numeric version order remain distinct. |
| PC6-P-005 | Reuse `parse_blueprint_source` for descriptor parsing and map only its six stable outcomes. | No second YAML dialect, Blueprint root validation, or finer parser reclassification is introduced. |
| PC6-P-006 | Define the admitted six-member descriptor and verified-file records inside `threadsmith-compiler`, with private fields and read-only accessors. | Recovered `threadsmith-schema::PackageDescriptor` remains compatibility evidence and is not used to override the accepted PC6 grammar. |
| PC6-P-007 | Reuse `threadsmith-canonical` for exact raw SHA-256, canonical JSON, and package-descriptor hashing, then privately wrap the resulting Package-kind identity. | No serializer, hash implementation, arbitrary package-identity constructor, or unchecked generic-ID promotion is added. |
| PC6-P-008 | Retain declared bytes as immutable shared byte slices keyed by sorted logical paths inside each inseparable package record. | Hard-linked entries may share storage but remain distinct logical paths; later consumers receive retained bytes only. |
| PC6-P-009 | Preserve the complete frozen fixture populations in one JSON manifest and add public-path integration tests plus external compile-fail opacity examples. | The current loader closes population counts and golden arithmetic only; an adversarial pass found that notation-string inputs do not yet satisfy the required independently executable fixture model. |
| PC6-P-010 | Make no Cargo or dependency change. | Existing compiler, canonical, schema, parser, JSON, Unicode, and SHA-256 dependencies are sufficient. |
| PC6-P-011 | Leave the implementation uncommitted and unaccepted because the pinned toolchain is unavailable. | Mechanical verification is recorded, but compilation, formatting, tests, Clippy, and PC1-PC5 regression qualification are not claimed or substituted. |
| PC6-P-012 | Classify the missing closed 184-row fixture interpreter as acceptance-blocking rather than treating population validation as execution. | Repair must preserve every frozen fixture and exact operation, construct its exact source/snapshot or acquisition failure, and compare its exact public PC6 outcome before qualification or acceptance. |

## PC6 Package Scan acceptance decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC6-A-001 | Accept the bounded PC2 explicit-tag diagnostic-precedence repair as part of the PC6 publication candidate. | The shared three-outcome classifier and 18 focused parser tests preserve accepted PC2 behavior; no declaration validation or independent PC6 semantics move into PC2. |
| PC6-A-002 | Record PC6 implementation verification as complete after the isolated Rust 1.97.1 frozen/offline workspace sequence passed exactly 67 tests. | The result comprises 54 Foundation-through-PC5 tests and 13 PC6 tests with zero failure, ignore, measured, or filter; no Cargo or lockfile change is accepted. |
| PC6-A-003 | Accept the separate independent read-only implementation review with P0=0, P1=0, P2=0, and P3=0. | The review changed no repository file, granted no acceptance itself, reproduced qualification, and found no acceptance-blocking or non-blocking implementation finding. |
| PC6-A-004 | Accept PC6 only within the frozen `DigestedSource + PortableProjectSnapshot -> ScannedSource` Package Scan boundary. | Acceptance covers snapshot intake, discovery, descriptor admission, declared-file verification, immutable retained bytes, package content identities, deterministic diagnostics, and source binding only. |
| PC6-A-005 | Retain the two reviewed operational residual risks as non-conformance, non-blocking risks. | The accepted freeze defines no semantic resource maxima, and a future real host adapter must establish an alias-free point-in-time snapshot and translate host failures into `SnapshotAcquisitionError`. |
| PC6-A-006 | Keep Builder and runtime unauthorized and leave PC7 unstarted. | PC6 acceptance creates no Resolve, Lockfile, imported-module, declaration, Manifest, Binding, installation, provider, product, filesystem, network, secret, model, runtime, or execution authority. |
| PC6-A-007 | Make PC6 publication the next bounded task after acceptance. | The committed acceptance records may describe publication as pending; the GitHub ref update and resulting commit identity remain external delivery evidence. |

## PC7 Resolve erratum-acceptance decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC7-E-001 | Accept the exact independently reviewed second repaired Resolve candidate as the normative Standard 0.3 companion for Resolve and optional existing-Lockfile intake needed by Resolve. | Acceptance records the completed review and is not another semantic review. |
| PC7-E-002 | Preserve the candidate region beginning at Normative Section 1 through its final byte and extract the embedded strict JSON value exactly from opening `{` through closing `}`. | Only procedural acceptance metadata outside the reviewed normative and fixture regions differs. |
| PC7-E-003 | Retain the complete machine-readable manifest as durable specified criteria. | Criteria include schemas, constructors, references, exact inputs and outcomes, canonical bytes and hashes, diagnostics and paths, precedence, selectors, relations, coverage, and future vectors rather than count-only claims. |
| PC7-E-004 | Keep fixture maturity exactly `specified`. | No strict deterministic plan generator, public-boundary interpreter, production Resolve implementation, complete execution, or qualification evidence exists. |
| PC7-E-005 | Record the final independent disposition as P0=0, P1=0, P2=0, P3=1 with independence uncompromised and all five prior P1 findings closed. | The sole P3 is non-blocking nonnormative provenance debt and does not authorize candidate modification. |
| PC7-E-006 | Interpret the reported diagnostic populations by label: 21 unique phase diagnostic codes and 62 current diagnostic fixture rows. | Fixture rows intentionally reuse codes across distinct paths, failure forms, precedence pairs, and boundary discriminators. |
| PC7-E-007 | Preserve Lattice Standard 0.3 as primary and each earlier erratum only within its stated scope. | Existing Rust types, current behavior, and implementation convenience remain nonnormative evidence. |

## PC7 Resolve semantic-freeze decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC7-S-001 | Assign PC7 exactly the Standard Resolve phase between accepted PC6 Package Scan and the later Lock phase. | Resolve consumes the opaque PC6 ScannedSource and creates no Lockfile or later artifact. |
| PC7-S-002 | Freeze the complete input as one exact ScannedSource plus optional ExistingLockfileInput represented only as Absent or one immutable supplied byte sequence. | Absent and zero bytes differ; no live path, filesystem, network, fetch, install, provider, clock, randomness, or host capability enters. |
| PC7-S-003 | Close the current candidate universe to `ScannedSource.packages()` and preserve the three duplicate-composition cases only as non-dispatchable future vectors. | PC7 creates no composition seam and no current fixture fabricates an invalid ScannedSource. |
| PC7-S-004 | Apply exact profile eligibility, arbitrary-size numeric version ordering, compatible per-package lock reuse, and greatest eligible satisfying fallback after identical-record collapse. | Missing group, profile incompatibility, and no common version remain distinct diagnostics; Resolve verifies but never creates `lock_id`. |
| PC7-S-005 | Recompute root reachability and contribution provenance from the pass-start state, calculate the next selection simultaneously, and retract deselected or unreachable contributions before the next pass. | Ever-seen requirement accumulation, within-pass contribution, and stale selection retention are non-conforming. |
| PC7-S-006 | Permit passes 1 through 256 and require one unchanged pass for success; a changed pass 256 returns the pass-limit diagnostic at forbidden pass 257. | A repeated non-adjacent historical state is not success, and operational exhaustion is not a semantic diagnostic. |
| PC7-S-007 | Parse selected modules only from exact immutable PC6-retained bytes using the accepted PC2 operation and frozen Resolve crosswalk, envelope, metadata, and import rules. | No reread, competing parser source, imported declaration defaulting, expansion, normalization, generated insertion, or static checking occurs. |
| PC7-S-008 | Construct the converged import graph and select cycles by the exact directed-edge token, rotation, and bytewise-minimum rules only after an unchanged pass. | Traversal implementation form, call-stack use, caching, and scheduling are nonnormative when observations are identical. |
| PC7-S-009 | Return either one total-order primary diagnostic or one opaque twelve-member ResolvedSource binding exact source, selections, retained modules, requirements, pass trace, reuse decisions, and graph. | Failure returns no partial output; success contains empty created identities and artifacts, literal no authority, and no PC7 identity. |
| PC7-S-010 | Freeze exact logical paths, within-gate rank comparison, mandatory gate order, and complete-path tie breaking for all 21 Resolve codes. | A later-gate diagnostic does not exist early merely because its numeric rank is lower. |
| PC7-S-011 | Retain 96 current fixtures, three future vectors, 43 registered choices, 118 schema categories, 11 rank comparisons, eight gate-order criteria, and the exact chain-255 fixture and plan preimages. | A later PC7 implementation gate must add strict dispatch, public-boundary execution, complete result comparison, and qualification before maturity advances. |
| PC7-S-012 | Authorize only the later PC7 Resolve implementation gate. | Lock, Expand, declaration processing, Manifest, qualification, Binding, Builder, runtime, providers, installation, CLI, MCP, UI, Android, and every product surface remain unauthorized. |

## PC7 fifth-repair acceptance and refreeze decisions

The decisions below supersede only the procedural acceptance, maturity, and
next-task state recorded by the earlier PC7 acceptance tranche. They do not
alter any reviewed normative or conformance-criteria byte.

| Decision | Resolution | Boundary |
|---|---|---|
| PC7-R5-A-001 | Accept the exact fifth semantic and conformance-criteria repair after the governing independent review recomputed PC7-SR4-IR-P1-01 closed with P0=0, P1=0, P2=0, and P3=1. | Acceptance records the supplied review; it is not another semantic review. |
| PC7-R5-A-002 | Preserve the complete reviewed region beginning at `NORMATIVE SECTION 1 — Authority, amendment, and precedence` and the standalone-to-embedded manifest equality byte-for-byte. | Only pre-normative procedural status, semantic-freeze procedure, mechanically dependent registry bindings, durable state, acceptance evidence, and publication bookkeeping may differ. |
| PC7-R5-A-003 | Keep fixture maturity exactly `specified`. | The repaired criteria are non-dispatchable, non-executable, non-qualified, implementation-unverified, and implementation-unreviewed. |
| PC7-R5-A-004 | Retain PC7-AJ-P3-01 as open, dormant, future-only, non-dispatchable, excluded from every current population, and non-blocking. | Acceptance does not repair, delete, reclassify, dispatch, or close the future vector. |
| PC7-R5-A-005 | Reconstruct the V1 authority registry from final accepted bytes while retaining the repair-overlay baseline commit and tree. | Relative to the fifth candidate registry, only the erratum and semantic-freeze `bytes` and `sha256` fields may change; the unchanged manifest row and every unaffected byte remain exact. |
| PC7-R5-A-006 | Treat the increase from 14 to 15 schema discriminators as the fifth repair's sole substantive population change. | All 118 fixtures, 45 choices, 127 schema categories, existing discriminator rows, identifiers, references, outcomes, and future dispositions remain unchanged. |
| PC7-R5-A-007 | Invalidate earlier focused qualification, implementation verification, and implementation review against the refrozen authority while retaining `PC7_IMPLEMENTATION_STARTED=true` and `PC7_ACCEPTED=false`. | Semantic acceptance does not qualify existing implementation or authorize Builder, runtime, or a later phase. |
| PC7-R5-A-008 | Publish the exact eight-path documentation/state inventory as one non-force child of the required baseline. | The resulting commit and tree are self-excluded publication evidence and are recorded only in the external operator report. |
| PC7-R5-A-009 | Make a separate read-only PC7 implementation and executable-conformance impact assessment the sole active next task. | The assessment may identify exact bounded implementation, generator, interpreter, plan, and qualification deltas but must not modify repository content. |

## PC7 Resolve implementation-acceptance decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC7-A-001 | Accept only the exact six-path candidate bound by the recorded SHA-256 identities after the final repair, implementation re-review, refreshed focused qualification, and qualification review all authenticate. | Acceptance does not authorize any repair, refactor, semantic reinterpretation, or candidate-byte change. |
| PC7-A-002 | Record PC7 focused qualification and implementation verification complete after the Rust 1.97.1 frozen/offline regression spine passes exactly 78 workspace tests and 11 unfiltered PC7 tests. | All Cargo targets and Python caches remain outside the repository; Cargo manifests, `Cargo.lock`, dependencies, and PC1-PC6 behavior remain unchanged. |
| PC7-A-003 | Advance fixture maturity to `qualified` only after the strict public-boundary interpreter proves `defined_fixture_ids == generated_fixture_ids == executed_fixture_ids` for all 118 current fixtures. | Four future vectors remain non-dispatchable, excluded, and unexecuted. |
| PC7-A-004 | Accept the checked 34,460,681-byte executable plan at SHA-256 `4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d`. | Two authenticated disposable regenerations must equal one another and the checked plan; generator rejection self-tests remain part of admission. |
| PC7-A-005 | Record both implementation review and qualification review complete with P0=0, P1=0, P2=0, and P3=0. | The distinct historical dormant semantic state `RESOLVE_ERRATUM_REVIEW_P3=1` remains open, future-only, non-dispatchable, and neither closed nor reclassified. |
| PC7-A-006 | Accept PC7 only within the frozen Resolve boundary from opaque PC6 `ScannedSource` plus optional immutable existing-Lockfile bytes to one total diagnostic or source-bound `ResolvedSource`. | Resolve creates no Lockfile, `lock_id`, Manifest, Binding, identity, authority, persistence, installation, provider, model, network, Builder, runtime, CLI, MCP, UI, Android, or other product behavior. |
| PC7-A-007 | Bind durable acceptance to exactly the six reviewed candidate paths and four acceptance-record paths. | No accepted authority, other implementation, earlier conformance material, Cargo path, or unrelated repository path may change. |
| PC7-A-008 | Publish one normal non-force fast-forward child of the required baseline to `refs/heads/main` only after a fresh remote identity check. | No tag, branch, pull request, merge, rebase, amend, squash, force option, alternate ref, or second commit is authorized. |
| PC7-A-009 | Treat the durable acceptance record as publication authority only after the exact commit is successfully pushed and local, cached-remote, and fresh-remote identities converge on it with a clean index and worktree. | Final commit, tree, remote, and push identities are self-excluded and belong only in the external operator report. |
| PC7-A-010 | Keep PC8 unstarted and make PC8 Lock scope reconciliation and semantic freeze the only next bounded task. | Naming the task authorizes no Lock implementation, Lockfile creation, Builder, runtime, or later product work. |

## PC8 Lock semantic-acceptance and freeze decisions

| Decision | Resolution | Boundary |
|---|---|---|
| PC8-E-001 | Accept the exact repaired PC8 Lock semantic and specified-conformance candidate after the governing superseding independent review closed `PC8-RR-P2-01` and returned P0=0, P1=0, P2=0, P3=0, no refuted, underdetermined, or unverified claim, and final disposition `PASS`. | Acceptance records completed independent evidence; it is not another semantic review or repair. |
| PC8-E-002 | Preserve the reviewed substantive regions of `PC8_SCOPE_RECONCILIATION.md`, `PC8_SEMANTIC_FREEZE.md`, and Lock Erratum Normative Sections 1 through 17 byte-for-byte. | Only pre-region procedural metadata and post-region acceptance/status envelopes may differ. |
| PC8-E-003 | Preserve `PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST.json` as one exact whole-file byte sequence at its reviewed identity. | Its candidate-status members remain historical reviewed-candidate data; procedural acceptance is external to the immutable criteria. |
| PC8-E-004 | Advance fixture maturity only to `specified`. | No deterministic generator, strict interpreter, public-boundary dispatch, complete execution, qualification, implementation verification, or implementation review exists. |
| PC8-E-005 | Retain all frozen populations and boundaries exactly: 20 current sources and fixtures, 19 relations, 41 discriminators, 12 isolated schema mutations, four preimage registries covering 235 spans, and four future-only non-dispatchable rows. | Acceptance cannot add, remove, dispatch, reclassify, or reinterpret a criterion. |
| PC8-E-006 | Use `PC8_AUTHORITY_REGISTRY_V1.json` to bind accepted PC1-PC7 authority, reviewed and accepted PC8 identities, governing evidence, the acceptance-verification path, and the self-excluded commit/publication evidence boundary. | External reports and procedural records remain evidence rather than dispatchable normative authority. |
| PC8-E-007 | Accept and freeze only portable pure Lock construction from one exact authenticated PC7 `ResolvedSource` to one exact source-bound `LockedSource`. | Physical atomic replacement remains allocated to the future PC8 Lockfile Persistence Adapter and is not performed by semantic acceptance. |
| PC8-E-008 | Keep `PC8_IMPLEMENTATION_STARTED=false` and `PC8_ACCEPTED=false`. | Semantic and specified-conformance acceptance does not implement, qualify, independently review, or accept overall PC8 product behavior. |
| PC8-E-009 | Publish exactly the nine-path documentation/state envelope as one normal non-force fast-forward child of `54b8b2b380606428f0d41f33d5d32c985c18c7ea`. | No implementation, test, Cargo, dependency, earlier authority, earlier conformance, generated-plan, or unrelated path may enter. |
| PC8-E-010 | Record final commit, tree, push, local, cached-remote, and fresh-remote identities only in the external operator report. | Same-commit self-reference is excluded; publication is valid only when the external report proves the published tree equals the independently verified staged tree. |
| PC8-E-011 | Keep Builder, runtime, providers, installation, product surfaces, Expand, PC9, and later phases unauthorized. | PC8 semantic publication creates no adjacent-phase or product authority. |
| PC8-E-012 | Make a separate read-only PC8 implementation and executable-conformance impact assessment the sole next bounded task. | The assessment may identify exact production, generator, interpreter, fixture, test, plan, qualification, and durable-state surfaces but may not modify repository content. |
