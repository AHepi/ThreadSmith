# PC7 Resolve Scope Reconciliation and Semantic-Freeze Blocker Report

Reconciliation date: 2026-07-24.

Status: scope reconciled; semantic freeze blocked by unresolved normative
choices. No PC7 semantic-freeze candidate, conformance fixture manifest,
freeze-verification document, implementation, acceptance, or delivery action
is part of this report.

## Repository baseline

The mandatory baseline gate ran before any write.

| Field | Required and observed value |
|---|---|
| Repository | `AHepi/ThreadSmith` |
| Branch | `main` |
| `HEAD` | `75ea1adbf90aba4297d6238f2563029a1d436bd2` |
| `HEAD^{tree}` | `c7215691dc1f7fcb84bf5737e57539d255f7a28e` |
| Existing `origin/main` | `75ea1adbf90aba4297d6238f2563029a1d436bd2` |
| Existing `origin/main^{tree}` | `c7215691dc1f7fcb84bf5737e57539d255f7a28e` |
| Initial `git status --short` | Empty |
| Initial index | Clean; `git diff --cached --quiet` returned success |

No fetch or other remote operation was performed.

## Controlling material

The following material was read completely and reconciled in the accepted
authority order.

| Material | Relevance |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Primary authority for imports, requirements, deterministic resolution, Lockfiles, identities, compiler phase order, diagnostics, local-only behavior, and final determinism |
| `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` | Limits accepted PC4 default expansion to root source and does not traverse imported package content |
| `docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` | Controls byte encoding only after an owning phase has selected a complete canonical value |
| `docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md` | Controls exact PC6 candidates, arbitrary-size numeric package versions, retained verified bytes, source binding, profile vocabulary, and the explicit imported-module deferral |
| `docs/adr/0001-portable-core-language.md` | Requires one portable Rust semantic core after semantics are normatively closed and forbids authority inference from content processing |
| `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md` | Durable accepted phase state and PC6-to-PC7 boundary |
| Foundation and PC1 acceptance material | Artifact-role, native identity, non-authority, diagnostic, and compatibility evidence |
| All PC2 reconciliation, intake, freeze, review, verification, provenance, checksum, and parser fixture material | Exact restricted-YAML semantic operation and its root-source-only ownership |
| All PC3 reconciliation, intake, freeze, review, verification, provenance, checksum, and source-validation fixture material | Exact root Blueprint envelope validation and its deliberate non-validation of import elements |
| All PC4 reconciliation, freeze, review, verification, and default fixture material | Root-source default transformation and explicit exclusion of imported package traversal |
| All PC5 reconciliation, freeze, review, verification, and digest fixture material | Exact opaque `DigestedSource`, root Blueprint identity, and pre-import-expansion boundary |
| All PC6 reconciliation, freeze, erratum-acceptance, implementation review, implementation verification, and Package Scan fixture material | Exact opaque `ScannedSource`, candidate records, retained bytes, diagnostics, phase deferrals, and accepted implementation boundary |
| `crates/threadsmith-schema/src/lib.rs` | Recovered package, request, and Lockfile structures; compatibility evidence only |
| `crates/threadsmith-canonical/src/lib.rs` | Current canonical JSON, raw SHA-256, and generic resolved-preimage helpers |
| `crates/threadsmith-compiler/src/lib.rs` | Current accepted PC2 through PC6 public compiler boundary |
| `crates/threadsmith-compiler/src/package_scan.rs` | Current private construction and public read-only accessors for the exact PC6 output |
| `conformance/pc6/package_scan/fixture_manifest.json` | Accepted PC6 vectors, including numeric version order, retained-byte continuity, opaque module bytes, and later-phase deferrals |

The principal accepted authority hashes at the baseline are:

| Authority | SHA-256 |
|---|---|
| Lattice Standard 0.3 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| Default Semantics Erratum | `ed5d32095abe2f834f19cef20d27f20d60469ecf0ac1367ed75e4725e2527766` |
| Canonical JSON Erratum | `ac772adc17a98bb9ecd6f9916717d696a1614918e79fc996546742f0cd6015b7` |
| Package Scan Semantics Erratum | `235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25` |
| ADR 0001 | `6c7608a3efa9e3a6f7db93d8ba3cfee8837fbfb87b2f2344f1ad8cc121799b08` |
| PC6 semantic freeze | `4e444eaac263b453d5d80252f28a63db919fa36efb9fef0dc98319ca0e7e0204` |
| PC6 fixture manifest | `c339a3a726843380fc1f0f7fe2aeda29644009f729a4e275a474750000d27fbe` |

Existing code and recovered schema types were treated as compatibility
evidence, never as authority for a missing semantic choice.

## Reconciliation verdict

The broad phase boundary is determined:

```text
accepted opaque ScannedSource
        |
        v
PC7 Resolve
        |
        v
source-bound exact selected versions
        |
        v
Lock
```

The accepted material does not completely determine the semantic operation
inside that boundary. In particular, it does not define an exhaustive import
requirement envelope, selected-module admission, profile filtering, existing
Lockfile intake, constraint-provenance fixed point, or deterministic diagnostic
surface. Each omission can change a selected version, successful output,
primary diagnostic, or later `lock_id`.

Consequently two independent implementations cannot yet be required to accept
the same complete input and produce the same selection, retained parsed module
state, primary diagnostic, or successful output. Authoring a freeze or exact
semantic fixtures would invent local ThreadSmith semantics.

## Exact phase ownership

The following ownership boundary is fixed even though the internal operation
is not freezeable.

| PC7 owns | PC7 does not own |
|---|---|
| Consumption of the exact opaque PC6 `ScannedSource` | Repeating Package Scan, descriptor admission, file verification, package identity creation, or package ordering |
| Root and reachable transitive package-requirement collection | Reading a live package path, taking a filesystem capability, fetching, installing, or accepting registry candidates |
| Resolve's same-name/version deduplication rule and its named diagnostic | Changing the PC6 candidate universe or manufacturing duplicate candidates |
| Existing-lock preference to the extent required by Standard section 13 | Canonical Lockfile creation, `lock_id`, atomic persistence, or later Lock-phase output |
| Selection of one exact version for each reachable package name after candidate eligibility is normatively closed | Import expansion, namespacing, declaration merging, or flattening |
| The resolution fixed point and no-common-version failure | Imported declaration defaults, declaration-body validation, normalization, generated gates, or static checking |
| Parsing only the selected retained module bytes needed to discover transitive imports | Parsing a different byte stream, rereading mutable paths, or creating a competing imported-source pipeline |
| Import-cycle rejection, because the Standard assigns `RESOLVE_IMPORT_CYCLE` | Namespace-collision diagnostics owned by Expand or later declaration diagnostics |
| A source/package/byte-bound successful Resolve result | Lockfile, Manifest, qualification, Binding, Builder, runtime, provider, secret, model, filesystem, network, or execution authority |

This is phase allocation, not a completed semantic contract. The exact rules
for several owned operations remain unresolved below.

## Complete conceptual input

| Input element | Reconciled rule | Remaining gap |
|---|---|---|
| `ScannedSource` | Mandatory first and controlling input; it contains the exact `DigestedSource`, ordered admitted package records, package identities, descriptors, and all verified declared bytes | None at the PC6 boundary |
| Root requirements | Must come from the root Blueprint already bound inside `ScannedSource`; Resolve must not accept an independently paired root value | Import-element grammar and diagnostics are not frozen |
| Package candidates | Must be exactly the package records already in `ScannedSource` | Profile filtering and future duplicate composition are not frozen |
| Selected module bytes | Must be the retained verified bytes at each selected descriptor's exact `module_file` logical path | Parser operation, envelope admission, and error mapping are not frozen |
| Active compiler profile | The accepted root is `lattice-core-0.1`; compatibility must be decided against each candidate's admitted profile set | Whether incompatible candidates are filtered, immediately rejected, or considered only after version selection is not stated |
| Existing Lockfile state | Standard section 13 requires an optional existing locked version to be considered before greatest-version selection | No accepted Resolve input type, parser, validation state, absence representation, or stale/invalid handling is defined |
| Host capability | None; PC6 consumed the only snapshot capability and retained exact bytes | None |

An existing Lockfile cannot be supplied as an unvalidated path or arbitrary
recovered `LockfileBody`. If lock reuse is supported, Resolve must receive
either an already validated immutable compiler input or a precisely specified
value whose validation is assigned to Resolve. The authority does not select
between those alternatives.

Active-profile compatibility is not yet safely allocated. If profile
membership determines candidate eligibility, it is necessarily
selection-affecting Resolve input. If it instead validates an imported module
after version selection, it could belong to selected-module admission or a
later compatibility check. The Standard and accepted errata do not choose
among these meanings, so this report does not assign one locally.

## Current public API evidence

The accepted public chain currently ends at:

```text
scan_packages(
    DigestedSource,
    PortableProjectSnapshot
) -> Result<ScannedSource, PackageScanDiagnostic>
```

`ScannedSource` exposes read-only access to its exact `DigestedSource` and
ordered `ScannedPackage` sequence. Each package exposes its admitted
descriptor, PC6-created package identity, and sorted `VerifiedPackageFile`
records; each verified record exposes one logical path and the exact retained
bytes. All semantic fields have private construction.

No current compiler API accepts an existing Lockfile, validates Lockfile
compatibility, parses a selected package module, represents a transitive
requirement, performs Resolve, returns a resolved-source wrapper, or emits a
Resolve diagnostic. The recovered schema `RequestedBy`, `LockedPackage`, and
`LockfileBody` constructors are not compiler phase evidence and cannot fill
those gaps.

## Candidate universe and deduplication

The current candidate universe is closed to:

```text
ScannedSource.packages()
```

No project path, descriptor, module file, package store, registry, network
source, installation result, or caller-supplied package record may augment or
replace it.

PC6 orders successful candidates by package-name ASCII bytes and then by
numeric canonical version. Its accepted layout admits at most one physical
candidate for one exact package name and version. Snapshot aliases fail before
PC6 rather than producing duplicates.

The Standard nevertheless assigns this rule to Resolve:

```text
same package name + same version + different package identities
    -> RESOLVE_DUPLICATE_VERSION
```

That diagnostic is unreachable from the sole accepted `ScannedSource` input.
The Package Scan Erratum reserves reachability for a future accepted
composition mechanism, but no such mechanism currently exists. PC7 must not
invent one merely to make the diagnostic reachable.

For that hypothetical future input, authority does not state whether repeated
records with the same name, version, and identity collapse, which occurrence
or provenance survives, or how duplicate checking precedes profile and
Lockfile checks. Those choices are not needed for the present PC6 universe but
prevent a claimed complete future-proof deduplication contract.

## Import requirement grammar

The accepted material determines some but not all of the grammar.

| Property | Determined rule | Unresolved rule |
|---|---|---|
| Package name | `^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$` | Exact import-member type and diagnostic target |
| Alias name | The shown `as` value is used as a source-level namespace and local names match `^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$` | Whether `as` is required, its exact admitted grammar, duplicate-alias behavior, and whether alias defects belong to Resolve or Expand |
| Import object | Standard section 11 shows `use`, `version`, and `as` | The example is not declared an exhaustive required-key schema; unknown, missing, non-string, duplicate, and malformed members have no assigned behavior |
| Requirement forms | Exact version or one caret range | Exact lexical grammar, leading-zero policy, whitespace policy, and unsupported syntax behavior are not stated |
| Caret lower bound | Inclusive | None |
| Caret upper bound | Exclusive | None |
| `^M.m.p`, `M > 0` | `>= M.m.p` and `< (M+1).0.0` | Component spelling and arbitrary-size increment mechanics are not explicitly assigned to requirements |
| `^0.m.p`, `m > 0` | `>= 0.m.p` and `< 0.(m+1).0` | Component spelling and arbitrary-size increment mechanics are not explicitly assigned to requirements |
| `^0.0.p` | Exactly `0.0.p` | Component spelling is not explicitly assigned to requirements |
| Exact version | Equality with one candidate version | Exact token admission is not frozen |
| Multiple requirements | A version must satisfy every requirement; requirements therefore form a conjunction/intersection | Duplicate requirement retention, normalization, provenance, and later `requested_by` representation are not frozen |
| Empty intersection | Resolution fails with `RESOLVE_NO_COMMON_VERSION` | Canonical package target, requirement target, and first-failure ordering are not frozen |
| Missing package | Candidate set for the required name is empty | Whether this is `RESOLVE_NO_COMMON_VERSION` or a permitted additional missing-package diagnostic is not stated |
| Requirement order | Must not change the mathematical satisfying set | Canonical traversal, primary failure, duplicate treatment, and Lockfile provenance order before Lock are not stated |
| Profile | Candidate descriptors carry a nonempty set containing Core and/or Builder | Exact compatibility test and diagnostic behavior are not stated |

The current recovered `RequestedBy` and `LockfileBody` types accept canonical
exact/caret strings and sort later records. They do not establish the missing
source grammar, Resolve diagnostics, duplicate semantics, or phase ownership.

## Version comparison and selection

Candidate version comparison is sufficiently determined. Every PC6 candidate
has three canonical decimal components. Each component is an arbitrary-size
non-negative integer. Comparison is by the `(major, minor, patch)` tuple; for
one component, fewer decimal digits means smaller and equal-length components
compare by ASCII bytes. Machine-integer conversion and lexical whole-string
ordering are forbidden. Thus `10.0.0` is greater than `2.0.0`.

The high-level selection preference is also determined:

| Priority | Rule |
|---:|---|
| 1 | Reuse the existing locked version when it satisfies every applicable requirement and still exists |
| 2 | Otherwise select the numerically greatest available satisfying version |
| 3 | If none exists, fail with `RESOLVE_NO_COMMON_VERSION` |

The policy is therefore neither lowest-compatible nor unconditionally
highest-compatible. A compatible existing lock takes precedence over the
greatest candidate.

The following selection-affecting meanings remain unresolved:

| Question | Why it changes conformance |
|---|---|
| What does locked version “still exists” mean? | Name/version presence, exact package-identity equality, or some other Lockfile consistency test can select different content |
| When is profile compatibility applied? | Filtering before selection, rejecting the greatest incompatible version, or failing a package can choose different versions or diagnostics |
| What makes an existing Lockfile compatible? | Root digest, lattice, profile, package identity, requested-by data, and partial staleness have no complete validation rule |
| What happens to a stale lock entry? | Ignoring it and selecting greatest differs from rejecting the Lockfile |
| How are malformed requirements treated? | Rejection, later validation, or exclusion changes success and primary diagnostics |

These gaps prevent an exact selection fixture even though the preference rule
itself is clear.

## Fixed-point behavior

Standard section 13 fixes this outline:

| Stage | Fixed rule |
|---|---|
| Scan | Already completed by PC6; PC7 must not repeat it |
| Deduplicate | Different identities for one name/version are a Resolve error |
| Collect | Gather root and reachable transitive requirements |
| Reuse | Prefer a compatible existing locked version that still exists |
| Select | Otherwise choose the numerically greatest satisfying candidate |
| Restart | Restart when a selected package introduces a new requirement |
| Finish | Stop after a complete pass changes nothing |
| Bound | More than 256 passes is an error |

A previously selected version may and, when it no longer satisfies all
discovered requirements, must be replaced by the applicable reuse-or-greatest
selection. Otherwise the stated “satisfies every requirement” rule cannot
hold.

The outline is not an executable deterministic algorithm. It omits:

| Missing rule | Observable consequence |
|---|---|
| Initial package and requirement traversal order | Different selected modules may be parsed first and yield different primary failures |
| Whether a pass collects all newly visible requirements or restarts after the first | Pass counts, the 256 bound, parse order, and diagnostics can differ |
| Exact meaning of “changes” | A new requirement, changed selected version, changed reachable module, changed lock-reuse decision, or changed cycle graph may trigger different restarts |
| Requirement provenance and retraction | Requirements contributed by a version that is later deselected may incorrectly persist and cause a false conflict |
| Replacement timing | Parsing old and new selected modules in one pass can expose different requirements and failures |
| Stable iteration order | Package name, version, root import index, transitive import index, module name, and graph order are not composed into one normative order |
| Cycle-check timing | Early cycle rejection and post-fixed-point cycle rejection can select different primary diagnostics |
| Bound counting | Initial pass, restarted partial pass, and final unchanged pass are not classified |
| Bound diagnostic | The Standard states “an error” but assigns no stable code or path |
| Oscillation behavior | No canonical state comparison or selected diagnostic is defined if selection and reachable constraints do not converge monotonically |

The required fixed point must be defined over requirements contributed by the
root plus the modules of the currently selected reachable versions. A future
normative rule must say exactly when contributions from deselected versions
are removed. Retaining all ever-seen requirements is not equivalent and cannot
be chosen locally.

## Imported-module intake and retained-byte continuity

The retained-byte boundary is exact:

```text
selected ScannedPackage
    -> descriptor.module_file()
    -> matching VerifiedPackageFile
    -> VerifiedPackageFile.bytes()
```

Resolve must consume those exact bytes. It must not reopen a project path,
compare a mutable file, ask PC6 to rescan, or accept an independently supplied
module value.

PC2 provides one accepted restricted-YAML operation, but it is accepted for
root source and is reused by PC6 only because the Package Scan Erratum says so
explicitly for `package.yaml`. The same erratum expressly says that it does
not normatively assign partial PC2 or PC3 behavior to Resolve.

The following imported-module rules remain open:

| Question | Missing normative decision |
|---|---|
| Parser | Whether selected `module_file` bytes invoke accepted PC2 exactly, another restricted operation, or a distinct envelope parser |
| Root shape | Whether an imported module reuses the complete PC3 root Blueprint allowlist and required keys, uses the shorter section 11 module envelope, or has another exhaustive schema |
| Defaults | Whether absence of `imports` is interpreted as empty solely for collection, whether all PC4 root defaults apply to imported values, and which later phase owns imported declaration defaults |
| Metadata agreement | Whether module `lattice`, `profile`, `module`, and `version` must agree with the active compiler, package name, descriptor version, or alias |
| Body opacity | Which root members must be admitted now while declaration elements and their defaults remain deferred |
| Failure mapping | Stable codes and paths for UTF-8, restricted-YAML, root-shape, requirement-member, metadata, and profile failures |
| Parsing order | Which selected module is parsed first and when a replacement invalidates prior parsed state |
| Retained representation | Whether the successful output retains the full accepted parsed value, an imports-only projection plus the full value, or another immutable byte-bound form for Expand |

Resolve must parse enough of each currently selected module to collect its
transitive package requirements. It must not validate declaration bodies,
expand namespaces, insert defaults into imported declarations, normalize, or
statically check merely because the parser exposes those values.

A later accepted implementation should use one private opaque result that
binds the exact `ScannedSource`, selected PC6 records, selected retained module
bytes, and their accepted parsed representations. Expand and later phases must
consume that retained representation rather than parse different bytes.
Neither the wrapper name `ResolvedSource` nor its exact fields can be frozen
until the imported-module contract is closed.

## Import-cycle ownership

The Standard's stable code `RESOLVE_IMPORT_CYCLE` assigns import-cycle
rejection to Resolve, not Expand. PC7 therefore owns cycle absence for the
reachable selected module graph.

The exact cycle operation is still unresolved. Authority does not define the
graph node identity, treatment of root-to-package and package-to-package
edges, self-imports, duplicate edges, aliases, selection replacements,
unreachable package cycles, canonical cycle representative, diagnostic path,
or precedence against module parse, profile, missing-package, and
no-common-version failures.

PC7 must not move namespace-collision detection into Resolve. Conversely,
Expand must not silently become the owner of the already named Resolve cycle
diagnostic.

## Lockfile ownership

The phase order is explicit:

```text
Resolve -> Lock -> Expand
```

The ownership split that follows from the Standard is:

| Concern | Owner |
|---|---|
| Consult an existing compatible locked version as a selection preference | Resolve |
| Select exact package versions | Resolve |
| Preserve complete requirement provenance needed for `requested_by` | Resolve output handed to Lock |
| Generate canonical Lockfile content after successful resolution | Lock |
| Sort packages and `requested_by` in canonical Lockfile form | Lock |
| Calculate `lock_id` with the identity field omitted | Lock |
| Write or replace the Lockfile atomically | Lock or its compiler persistence boundary |

PC7 must not create a Lockfile or `lock_id`.

The Standard says only the compiler creates or validates a Lockfile, but it
does not assign validation of an existing file to a point before Resolve,
Resolve itself, or Lock. Reuse cannot be deterministic until validation and
compatibility are settled. Unresolved cases include wrong `lock_version`,
wrong lattice/profile/root digest, duplicate packages, noncanonical versions,
wrong package identity, missing selected content, stale `requested_by`,
unknown members, invalid `lock_id`, and a valid lock whose pinned package no
longer exists.

The recovered schema `LockfileBody` is not a normative answer. It has no
accepted parser or validation outcome, omits the outer `lock_id`, and cannot
define the missing phase and diagnostic ownership by precedent.

## Successful output and identities

The Standard names Resolve's output only as “Exact versions.” A successful
phase result must at least preserve:

| Required semantic content | Reason |
|---|---|
| Exact consumed `ScannedSource` | Prevent source/package substitution |
| One exact selected PC6 record per reachable package name | Preserve descriptor, package identity, and byte binding |
| Exact selected module bytes and accepted parsed representation | Prevent mutable-path rereads or a competing intake pipeline |
| Complete active requirement set with deterministic provenance | Permit Lock to construct canonical `requested_by` content |
| Reachability and import edges needed by Expand and cycle proof | Preserve the fixed-point result without rediscovery from different bytes |

Diagnostics, mutable paths, snapshot or provider capabilities, runtime
permissions, execution authority, unrelated provenance, and non-semantic trace
data must not be embedded as identity-bearing content. A lock-reuse trace is
not required by the Standard when it does not change the selected result.

PC7 creates no identity. The accepted identity table contains package and lock
identities but no resolution, selected-package-set, or `ResolvedSource`
identity. Package identities already belong to PC6. `lock_id` belongs to the
later Lock phase. The durable “Package Set” artifact also has no specified
identity preimage. No new identity kind or guessed preimage may be introduced.

## Resolve diagnostics and precedence

Only three stable Resolve codes and broad meanings are accepted:

| Code | Accepted owner and meaning | Reachability or unresolved detail |
|---|---|---|
| `RESOLVE_DUPLICATE_VERSION` | Resolve; same package name and version with different identities | Unreachable through the sole current PC6 input; future composition and exact primary target are undefined |
| `RESOLVE_NO_COMMON_VERSION` | Resolve; no version satisfies all requirements | Reachable in principle; package selection, requirement provenance, path, and precedence are undefined |
| `RESOLVE_IMPORT_CYCLE` | Resolve; import cycle | Reachable in principle; graph, canonical cycle, path, and precedence are undefined |

No accepted Resolve diagnostic code or canonical target exists for:

| Condition | Ambiguity |
|---|---|
| Missing package | Could be the empty-set case of `RESOLVE_NO_COMMON_VERSION` or a permitted additional code |
| Invalid or unsupported requirement | No code, path, or precedence |
| Malformed import object | No code, path, or owner split with source validation |
| Incompatible package or module profile | No Resolve mapping; later `ABI_INCOMPATIBLE` cannot be repurposed without authority |
| Selected module invalid UTF-8 or restricted YAML | PC2 codes cannot be exposed as PC7 diagnostics without an explicit crosswalk |
| Invalid selected module envelope or metadata mismatch | PC3 codes cannot be exposed as PC7 diagnostics without an explicit crosswalk |
| More than 256 passes | Required error has no code or target |
| Invalid, stale, or mismatching existing Lockfile | Neither Resolve-versus-Lock owner nor code/path is fixed |
| Internal non-convergence distinct from the pass bound | No classification |

The accepted material also supplies no global primary-diagnostic precedence
across deduplication, root import admission, existing-lock validation, profile
compatibility, selected-module parsing, module-envelope admission, missing
packages, fixed-point replacements, no-common-version conflicts, cycles, and
the pass bound. It supplies no canonical Resolve path syntax combining root
JSON pointers, package names, versions, retained logical module paths, and
transitive import indices.

PC7 must not reuse PC2, PC3, PC6, Lock, Expand, or Static Check diagnostics
outside their accepted owner merely because existing code provides a
convenient error type.

## Explicit phase deferrals

| Deferred work | Later owner or status |
|---|---|
| Canonical Lockfile body, `lock_id`, and atomic persistence | Lock |
| Namespace assignment, chained namespaces, imported declaration expansion, and flattening | Expand |
| Imported declaration default expansion not needed solely to collect requirements | Requires later normative allocation; not PC7 by convenience |
| Declaration normalization | Normalize |
| Generated external intake gates | Insert |
| Cross-declaration and reference validity | Static check |
| Declaration identities | Identify |
| Canonical collection sorting outside Resolve's own deterministic state | Sort |
| Manifest content, `manifest_id`, and persistence | Manifest and Persist |
| Qualification and Qualification Record | Qualifier |
| Run Binding and execution authority | Binding owner |
| Builder, runtime, providers, events, replay, secrets, models, filesystem effects, and network effects | Outside PC7 |
| Package installation, registry access, and fetching | Deferred product scope; forbidden in Core Resolve |
| CLI, MCP, UI, and Android work | Later product work |

Resolve remains local-only, compile-time, non-executable, and
non-authoritative.

## Fixture coverage ledger

No PC7 fixture manifest is authorized while the semantic result is
underdetermined. The following ledger records the required future coverage
without assigning guessed bytes, diagnostics, paths, identities, or outputs.

| Required coverage | Constructible accepted basis | Why an exact PC7 fixture is or is not closed |
|---|---|---|
| Empty universe, no imports | Existing PC6 `DS-A` with absent or empty package snapshot produces exact empty `ScannedSource` | Successful empty selection and absence of later artifacts are conceptually closed; final output representation is not |
| One exact compatible package | Existing minimal PC6 package record can supply the candidate | Exhaustive root import grammar, profile check, and output representation are missing |
| Multiple compatible versions | Existing PC6 multiple-version records supply exact candidates | Lock absence/intake and exact requirement admission are not frozen |
| Numeric `2.0.0` versus `10.0.0` | Existing PC6 numeric-order records prove candidate comparison | Resolve selection fixture still needs a frozen import requirement and output |
| Multiple intersecting root constraints | Candidate versions can be supplied by PC6 | Duplicate/import schema, provenance, and deterministic order are missing |
| No common version | Candidate set and mathematical conflict can be constructed | Primary package/requirement target and precedence are missing |
| Transitive constraint after initial selection | Selected package modules can carry import-shaped bytes | Imported module parser/envelope and restart semantics are missing |
| Restart changes a selection | A high version can introduce a constraint that invalidates an earlier choice | Contribution retraction, replacement timing, and pass rules are missing |
| Multiple fixed-point iterations | A chain of selected modules can introduce requirements | Pass definition, traversal, parsing order, and bound accounting are missing |
| Presentation-order-independent convergence | Equivalent source and candidate orders can be varied | Canonical requirement and iteration order are missing |
| Missing package | Root or selected module can name an absent package | Missing-versus-no-common diagnostic classification is missing |
| Duplicate version | Not constructible through accepted PC6 `ScannedSource` | Must remain unreachable unless a later accepted composition mechanism is added |
| Compatible and incompatible profiles | PC6 records can contain Core and/or Builder profile sets | Compatibility and failure policy are missing |
| Valid lock reuse | Recovered logical lock values exist as compatibility evidence | Accepted Lockfile input and validation are missing |
| Stale or incompatible lock | Staleness dimensions can be described | Owner, fallback-versus-error behavior, code, and path are missing |
| Selected-module parser failure | PC6 already retains malformed and opaque module bytes successfully | PC7 parser operation and crosswalk are missing |
| Invalid module envelope | PC6 can retain any digest-valid bytes | Imported module root grammar and diagnostic mapping are missing |
| Import cycles | Requirement-shaped module bytes can form cycles | Graph, detection timing, representative, code path, and precedence are missing |
| Source/package/byte/output binding | Existing private PC6 wrappers provide the lower boundary | Exact PC7 wrapper and retained parsed representation are missing |
| Repeated resolution equality | Identical `ScannedSource` can be supplied repeatedly | Equality-bearing successful output is not frozen |
| No filesystem reread | PC7 can be designed with no host capability and PC6 retained bytes | Must be asserted after the PC7 API is frozen |
| No network access | Candidate universe is already closed | Must be asserted after the PC7 operation is frozen |
| No Lockfile, Manifest, Binding, or later identity | Phase boundary and identity table close the negative rule | Must be asserted against the future output API |
| No authority creation | Accepted non-authority boundary is closed | Must be asserted against the future output API |

No golden PC7 identity is appropriate because PC7 creates no identity.

## Unresolved ambiguity ledger

| ID | Normative ambiguity | Affected property |
|---|---|---|
| `R-01` | Exhaustive `imports[]` object schema, member types, alias rules, duplicates, and canonical traversal | Selection and diagnostics |
| `R-02` | Exact requirement lexical grammar, canonical component spelling, normalization, and unsupported syntax | Selection and diagnostics |
| `R-03` | Active-profile compatibility, exact phase owner, filtering stage, and failure behavior | Candidate universe, selection, phase ownership, and diagnostics |
| `R-04` | Existing Lockfile representation, validation owner, compatibility, identity matching, and stale fallback | Selection, diagnostics, and Lock ownership |
| `R-05` | Exact fixed-point state, requirement provenance/retraction, restart triggers, pass counting, and stable traversal | Selection, termination, and diagnostics |
| `R-06` | Accepted parser for selected retained module bytes | Selection and diagnostics |
| `R-07` | Imported module envelope, metadata agreement, root defaults needed for imports, and declaration-body opacity | Selection, phase ownership, and diagnostics |
| `R-08` | Retained parsed module representation and exact successful output contract | Output and byte continuity |
| `R-09` | Import-cycle graph, detection timing, representative, and path | Diagnostics and phase behavior |
| `R-10` | Missing-package classification | Diagnostics |
| `R-11` | Stable codes and canonical paths for module, requirement, profile, lock, and pass-bound failures | Diagnostics |
| `R-12` | Global primary-diagnostic precedence across all Resolve stages and iterations | Diagnostics |
| `R-13` | Same-identity duplicate collapse for any future composition mechanism | Candidate universe and output |

Any one of `R-01` through `R-12` is sufficient to block a complete PC7
semantic freeze. Several affect which version is selected, not merely message
prose.

## Smallest necessary normative action

The smallest coherent next action is one focused Lattice Standard 0.3 Resolve
Semantics Erratum or one equivalently authoritative focused decision. Splitting
the issues into unrelated local choices would leave circular dependencies
between selected-module parsing, transitive constraints, lock reuse, the fixed
point, and primary diagnostics.

The focused action must close exactly:

| Required closure | Boundary |
|---|---|
| Exhaustive root and imported import-requirement grammar | No declaration-body validation |
| Exact requirement version grammar and arbitrary-size interval arithmetic | No prerelease, build metadata, or new range forms |
| Candidate profile compatibility and duplicate behavior | No new candidate source or package composition mechanism |
| Existing Lockfile input, validation state, reuse, staleness, and identity matching | No Lockfile generation or `lock_id` in Resolve |
| Executable fixed-point algorithm with contribution retraction, deterministic order, restart triggers, pass counting, and termination | No package fetch |
| Selected-module parser, imported envelope, metadata agreement, and retained representation | No import expansion, declaration defaulting, normalization, or static checking |
| Resolve-owned cycle operation | No namespace-collision reassignment |
| Complete Resolve diagnostic vocabulary, canonical paths, and global primary precedence | No reuse of another phase's codes without an explicit crosswalk |
| Exact successful source/package/byte-bound output and explicit creation of no identity | Lock remains the next phase |

The action may name a private conceptual output, but it must not prescribe a
Rust layout, add a product surface, create authority, or begin implementation.

## Reconciliation result

PC7's phase position, mandatory PC6 input, closed candidate source, retained
byte continuity, local-only boundary, broad lock-selection role, high-level
version preference, candidate numeric comparison, cycle ownership, absence of
a PC7 identity, Lock-phase separation, and later deferrals are reconciled.

PC7's complete selection, module intake, fixed point, Lockfile input,
diagnostics, and successful output are not normatively closed. The authorized
stop condition therefore applies.

```text
PC7_SCOPE_RECONCILED=true
PC7_SEMANTICS_FROZEN=false
PC7_FREEZE_CANDIDATE_COMPLETE=false
PC7_IMPLEMENTATION_STARTED=false
PC7_ACCEPTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=focused Resolve erratum or ambiguity decision
```
