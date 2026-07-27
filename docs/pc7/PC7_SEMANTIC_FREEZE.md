# PC7 Resolve Semantic Freeze — Accepted Fifth Repair

Repair-acceptance date: 2026-07-27.

Status: the fifth repair is independently reviewed, accepted, published, and
refrozen at fixture maturity `specified`. This semantic acceptance does not
qualify the repaired criteria, accept PC7 implementation, accept PC7 overall,
or authorize later product work.

## Normative authority

Lattice Standard 0.3 and every published accepted erratum remain normative
authority. The accepted fifth-repair Resolve Semantics Erratum, exact
standalone conformance manifest, this semantic freeze, and the V1 authority
registry are the published Resolve authority set within their stated scopes.

Independent adjudication at SHA-256
`4d22f38aff643fa8ad1469935f1e1372c22e51a4009e6bf24aeb629662193060`
controls this repair's five P1, three P2, and one P3 findings and their
severity boundaries. The authenticated external blind derivation at SHA-256
`c0ae858d70b6e947d184d4eb7dd9f1ba56056ce595462121ace73d2bfd1a41f0`
and consultation report at SHA-256
`2005bfeee4a15f2285a84c0717e6647f2778bb877e1cadf8ed9161822a8e295a`
are advisory evidence only. No advisory recommendation is silently promoted
to a normative rule.

The governing independent fourth-repair review at SHA-256
`96c501942269b9b694ec1df01a9330c547bd24ce355810c6bfa9a1daca78a65a`
derived the fourth candidate's repaired Unicode-scalar strict-parse semantics,
retained PC7-AJ-P3-01 as dormant and open, and found only
PC7-SR4-IR-P1-01 acceptance-blocking. The fifth repair is bounded to one
durable raw-registry unpaired-surrogate discriminator and its exact closed
schema, population, and NC-46 bindings.

The governing fifth-repair independent review at SHA-256
`6f664ac7218c45be2244bfa029f5ae915a9a53739d5355ef286f1dedeea0aef9`
recomputed PC7-SR4-IR-P1-01 closed with P0=0, P1=0, P2=0, and P3=1.
PC7-AJ-P3-01 remains dormant, open, future-only, non-dispatchable, excluded
from current populations, and non-blocking.

## Bound artifact identities

The accepted baseline is repository commit
`ded743ea3577ffc2b955565dee9159287ec98e05`, tree
`e26180101c53c5cf44e4f270a9e868a4582be392`, parent
`75ea1adbf90aba4297d6238f2563029a1d436bd2`.

| Controlling document | Accepted baseline SHA-256 |
|---|---|
| Lattice Standard 0.3 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| Default Semantics Erratum | `ed5d32095abe2f834f19cef20d27f20d60469ecf0ac1367ed75e4725e2527766` |
| Canonical JSON Erratum | `ac772adc17a98bb9ecd6f9916717d696a1614918e79fc996546742f0cd6015b7` |
| Package Scan Semantics Erratum | `235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25` |
| Resolve Semantics Erratum | `4507fdfe2147f460c2f791b494517878c0d04620d020a6b8c512294aab868b24` |
| PC7 Scope Reconciliation | `4cee5f0beacd663ee9ab3bb9c05060342de18c1d6d7b56d3a477c46c15d80243` |
| PC7 Semantic Freeze | `48ac10106028f8e6ace85ee9f633bd1e0319e3b5575b9b33a0ca5f0fc99b0672` |
| PC7 Specified Conformance Manifest | `1fb0c0588310a32c4a5c4fa7ff9d9a268ab940a61ae913d00bb465eb2a83ef10` |

| Accepted document | Final identity carrier |
|---|---|
| Resolve Semantics Erratum | final byte count and SHA-256 in the V1 registry |
| PC7 Specified Conformance Manifest | final byte count and SHA-256 in the V1 registry |
| PC7 Semantic Freeze | final byte count and SHA-256 in the V1 registry |

The durable manifest path is
`docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json`. Its maturity is
exactly `specified`. It is not dispatchable, executable, qualified,
implementation-verified, or implementation-reviewed.

The exact durable trust-root carrier is
`docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json` with format
`threadsmith-pc7-authority-registry-1`. It has exactly `format`,
`baseline_commit`, `baseline_tree`, and `documents` in that order.
`documents` has eight rows in the manifest's exact preflight order; every row
has exactly `key`, `path`, `bytes`, and `sha256` and binds one final authority
file. Its UTF-8, no-BOM, LF-only, two-space JSON serialization, member order,
row order, canonical decimal byte counts, lowercase SHA-256 values, and
exactly one final LF are normative. Its standalone bytes are the only
admitted V1 serialization.

`registry_strict_json_parse` applies recursively to every string value and
object-member name and admits only Unicode scalar-value sequences. A
non-surrogate `\uXXXX` escape denotes its scalar. A high-surrogate escape
`\uD800` through `\uDBFF` is admitted only when immediately followed in the
same string by a low-surrogate escape `\uDC00` through `\uDFFF`; `H,L` denote
`0x10000 + ((H - 0xD800) << 10) + (L - 0xDC00)`. Every lone, reversed,
separated, repeated, mismatched, or truncated surrogate construction rejects
at strict parse. It is never replaced, preserved as a code unit, deleted,
normalized, deferred, or passed to canonical-byte comparison. Literal UTF-8
supplementary scalars and valid escaped pairs denote the same parsed scalar;
invalid raw UTF-8 scalar encodings reject. No NFC occurs at strict parse, and
duplicate member names are compared after valid scalar decoding.

The V1 pre-schema serializer consumes the one parsed value produced from the
actual immutable registry bytes and is total for every strictly parsed value
after unknown-member inspection completes. It does not consume a projected,
member-dropped, defaulted, reordered, or separately constructed object. It
uses the exact two-space layout, schema-position member orders, unsigned
UTF-8 order for other object positions, accepted canonical JSON string
escaping, exact finite-decimal normalization, and one final LF defined by the
Resolve erratum. This boundary lets canonical-byte comparison reject every
alternate spelling without masking a later missing-member, type, format,
baseline, document-order, or path-binding discriminator.

The baseline fields identify commit
`ded743ea3577ffc2b955565dee9159287ec98e05` and its root tree
`e26180101c53c5cf44e4f270a9e868a4582be392`; acceptance verifies that
relation against the complete bundle. They do not require the final
acceptance commit or tree to reuse either identity, and ordinary preflight
does not require Git.

Generator and interpreter receive one explicit `PC7AuthorityInputsV1`
containing a read-only authority-root capability and the immutable registry
bytes. Their CLI adapters require exactly one `--pc7-authority-root` and one
`--pc7-authority-registry`; neither has a default, repeat form, environment,
search-path, network, current-directory, report, or compiled-constant
fallback. The registry argument designates the fixed path beneath the root.
The generated plan binds registry byte count and SHA-256, and the interpreter
independently repeats preflight before interpreting that plan.

Every intake or document failure rejects as
`PC7_AUTHORITY_PREFLIGHT_REJECTED`. Root binding failures use
`authority#/root`. Missing or unreadable registry bytes, wrong registry path,
invalid UTF-8, BOM, malformed JSON, any unpaired-surrogate string, duplicate
decoded keys, or noncanonical bytes use `authority#/registry`. Every strict
parse failure has reason `UTF-8/BOM/JSON/duplicate failure`.

The exact stage order is `invocation_authority_root`,
`invocation_registry_binding`, `registry_read`,
`registry_strict_json_parse`, `registry_unknown_members`,
`registry_canonical_bytes`, `registry_missing_members`,
`registry_member_types`, `registry_format`, `registry_baseline_commit`,
`registry_baseline_tree`, `registry_document_key_order`,
`registry_document_path_bindings`, and `authority_document_bytes`. Each
completes before the next begins. Strict parsing receives the actual supplied
bytes; unknown-member inspection and canonical serialization receive only its
one parsed result.

Unknown-member inspection covers root members and object-valued document rows.
It orders complete RFC-6901-escaped `authority#/registry/...` paths by unsigned
UTF-8 bytes, so names containing `/` and `~` are escaped and selected
deterministically. The raw-byte root-`zzz` criterion requires exactly
`PC7_AUTHORITY_PREFLIGHT_REJECTED`, `registry_unknown_members`,
`authority#/registry/zzz`, and `unknown registry member`; parsed-object-only
mutation is forbidden. Only after no unknown member exists may
`registry_canonical_bytes` compare the supplied bytes with the pre-schema
serialization.

The durable
`AUTHORITY-D-REGISTRY-UNPAIRED-SURROGATE` criterion takes the complete final
supplied V1 registry bytes at `PC7AuthorityInputsV1.registry_bytes`. It
requires the unique root-format line bytes
`202022666f726d6174223a2022746872656164736d6974682d7063372d617574686f726974792d72656769737472792d31222c0a`
and replaces only the 36-byte content
`746872656164736d6974682d7063372d617574686f726974792d72656769737472792d31`
with the six ASCII bytes `5c7564383030`, retaining both quotes and every
other raw byte. The resulting line is exactly
`202022666f726d6174223a20225c7564383030222c0a`.

Those complete mutated bytes are supplied unchanged through the same raw
boundary and require exactly `PC7_AUTHORITY_PREFLIGHT_REJECTED`,
`registry_strict_json_parse`, `authority#/registry`, and
`UTF-8/BOM/JSON/duplicate failure`. Parsed-object substitution, projection,
host-parser preprocessing, replacement characters, reserialization, and
direct internal-validator invocation are forbidden. The governing fourth
construction is retained as provenance at 2,011 bytes with SHA-256
`f3ba4869cdb8097f7143d98d22f56e8e5eff5509db1a9d132d5498db8dbd9a92`;
the final fifth construction is derived afresh from the final registry.

Missing members follow top-level member, document index, and row-member order.
Wrong format or baseline identity uses the corresponding `format`,
`baseline_commit`, or `baseline_tree` path. Registry path substitutions are
rejected before any authority file is read.

After registry intake completes, each authority file is completed in the
manifest's eight-key order. Missing, unreadable, byte-count-mismatched, or
digest-mismatched files use `authority#/<authority-document-key>`; byte count
precedes SHA-256, and multiple mismatches select the first document key. All
rejection occurs before manifest or plan interpretation, construction,
dispatch, or Resolve execution and creates no `ResolveOutcome`. Changing the
erratum's outcome-bearing first-gate sentence while leaving registry and
manifest bytes unchanged MUST reject at
`authority#/resolve_semantics_erratum`.

At acceptance, the three repaired hashed documents are finalized without the
registry's final hash, their byte counts and hashes are computed, and the
registry is constructed once with those values and the five unchanged
documents. An independent reproducer verifies all four prospective byte
sequences and the exact four-path baseline overlay before the four are
reviewed and published together. No final commit/tree identity or fifth
normative artifact is required, so the construction has no hash cycle.

## Lifecycle boundary

```text
exact opaque ScannedSource
        +
optional ExistingLockfileInput
        |
        v
PC7 Resolve
        |
        v
opaque non-authoritative ResolvedSource
        |
        v
Lock (deferred)
```

Resolve begins only after successful PC6 Package Scan and ends before Lock.

## Exact conceptual input

PC7 consumes exactly:

```text
one exact opaque ScannedSource
+
ExistingLockfileInput = Absent or one immutable supplied byte sequence
```

No other member or capability exists. Absent Lockfile input and a supplied
zero-byte sequence are distinct. Resolve derives the root source, active
profile, Blueprint digest, package candidates, descriptors, package
identities, declared module paths, and verified immutable bytes only through
the exact ScannedSource. It does not repeat PC6, read a live path, inspect a
package directory, use a network, fetch or install a package, invoke a
provider, consult a clock, use randomness, or receive a host capability.

The current candidate universe is exactly `ScannedSource.packages()`. The
four duplicate-composition vectors remain future criteria and are
non-dispatchable through the current accepted ScannedSource boundary. This
accepted repair creates no composition seam. The fourth records dormant textual
version-path ordering as future composition-seam debt only.

## Exact Resolve ownership

Resolve owns the accepted erratum's exhaustive import admission, canonical
constraint grammar, arbitrary-size numeric comparison, requirement
conjunction, candidate grouping, identical-record collapse, active-profile
eligibility, existing-Lockfile intake and validation, per-package reuse,
greatest-compatible fallback, requirement provenance, retraction,
reachability, deterministic fixed-point passes, selected-module intake,
import-graph construction, cycle rejection, and total primary diagnostic
order.

Root and selected-module imports use the same closed three-field schema.
Applicable requirements retain exact constraint text, interval, alias,
logical source path, and contributor. Text ordering uses unsigned NFC UTF-8
bytes except where the erratum assigns arbitrary-size numeric version order.

## Existing Lockfile intake and reuse

Optional Lockfile input is immutable bytes, never a path. Supplied bytes pass
the exact source, six-member closed-schema, existing `lock_id`, and context
gates in that order. Resolve verifies an existing `lock_id` but never creates
one.

As genuinely new choice NC-45, a direct Lockfile JSON integer is any
mathematical integer with no minimum or maximum. Negative integers are
admitted at source intake. Its canonical source grammar is `0` or
`-?[1-9][0-9]*`; leading zeros, plus signs, fractions, exponents, negative
zero, and nonfinite spellings are forbidden independently of magnitude. No
canonical integer lies outside the admitted domain, so magnitude never
produces a source-range diagnostic. A forbidden spelling in `lock_version`
is `RESOLVE_LOCK_SOURCE_INVALID` at `lock#/lock_version`; an admitted integer
other than `1` is `RESOLVE_LOCK_SCHEMA_INVALID` at
`lock#/lock_version` in closed-schema stage 4.

Closed-schema stages are global gates completed in order. The stage-3 type
scan completes before stage-4 fixed values, and the complete stage-14 package
name scan completes before any stage-15 `requested_by` order failure becomes
eligible. Durable dual-defect criteria bind, respectively,
`lock#/lattice` and `lock#/packages/1/name`; stage-only controls bind each
component failure independently.

Context binds lattice `0.3`, the exact active profile, and the root Blueprint
digest inside ScannedSource. Reuse is decided independently for each required
package. Stale version, stale identity, missing entry, profile ineligibility,
and constraint incompatibility are nonfatal per-package misses followed by
the ordinary greatest eligible satisfying selection. Valid extra entries are
retained as sorted unreferenced entries and create no selection.

## Candidate grouping and numeric selection

Candidate groups are keyed by package name and arbitrary-size numeric
`major.minor.patch` version. Byte-identical semantic records collapse.
Different package identities for one name and version fail under the accepted
duplicate rule, although that condition is not constructible through the
current public ScannedSource boundary.

For every required package, Resolve distinguishes no package group, no
active-profile-eligible candidate, and no candidate satisfying all applicable
constraints. A compatible reusable Lockfile entry is preferred; otherwise
the numerically greatest eligible satisfying candidate is selected.

The specified criteria retain complete adjacent values at `u128::MAX` and
`u128::MAX + 1`, plus adjacent 80- and 81-digit components whose lexical and
numeric orders differ. Root and transitive public-boundary fixtures require
the complete selection
`1.0.100000000000000000000000000000000000000000000000000000000000000000000000000000000`.
These distinctions refute signed-i64, unsigned-u64, u128, fixed-30-digit,
lexical, saturating, and truncating implementations without relying on source
inspection.

## Replacement, contribution retraction, and passes

Every pass computes its complete next selection simultaneously from the
pass-start contribution state. Root contributions always apply. Selected
package contributions apply only when reachable from root through pass-start
selections.

Reachability and contributions are recomputed from root on every pass.
Contributions from replaced or unreachable selections retract before the next
pass. Names not required in the current pass are absent from the next
selection.

Passes are numbered 1 through 256. Success requires one complete unchanged
pass under the exact selection-state equality rule. An unchanged pass 256 may
succeed. If pass 256 changes, pass 257 is not started and
`RESOLVE_PASS_LIMIT` is returned at `resolve#/passes/257`. A repeated
non-adjacent historical state is not success.

## Selected-module continuity

Resolve locates each selected descriptor's `module_file` only in that
candidate's immutable verified-file mapping. It applies the accepted PC2
restricted-YAML parser to those exact retained bytes and uses the accepted
six-code Resolve crosswalk.

The selected module uses the exact full Core root envelope and metadata
binding frozen by the erratum. A missing `imports` member contributes no
requirement but is not inserted into the retained parsed value. Declaration
elements remain opaque. Resolve performs no imported declaration defaulting,
namespace expansion, normalization, generated-structure insertion, or static
checking.

Every successful selected-module record binds the selected PC6 package
record, `module_file`, exact retained bytes, declared byte digest, one PC2
parsed value, and admitted imports projection. Later phases must consume that
retained representation and must not parse another byte source.

## Envelope admission, graph, and cycles

The selected-module envelope, independently reachable import defects, and
metadata binding follow the erratum's gathering and total-order rules.
Multiple selected-module intake failures reachable in one pass are compared
under the accepted diagnostic order; no partial output exists.

After an unchanged pass, Resolve constructs the exact root and selected
package graph. Every applicable requirement creates one labeled directed
edge. Parallel edges remain distinct. Cycle selection enumerates simple
directed edge cycles, rotates but never reverses each sequence, and selects
the bytewise least normalized token sequence. Cycle detection occurs only
after convergence and therefore follows module-intake failures and the pass
limit.

Traversal implementation form is nonnormative. Iteration, recursion,
call-stack use, caching, and internal scheduling have no conformance
significance when all required observations are identical.

## Diagnostics and paths

The accepted erratum binds 21 Resolve diagnostic codes: three existing
Standard codes plus 18 newly specified Resolve codes. The durable manifest
contains 81 diagnostic fixture rows. These are different populations:
`21` counts unique phase diagnostic codes, while `81` counts current
diagnostic fixtures, including multiple paths, precedence comparisons, and
boundary discriminators that reuse codes.

Diagnostics use exactly the `root#`, `packages/`, `lock#`, and
`resolve#/passes/` logical anchors with the accepted pointer and
percent-encoding rules. Lower numeric rank controls only among candidates
simultaneously reachable inside one gate; mandatory earlier gates prevent
later diagnostics from existing. Complete canonical path breaks same-rank
ties.

For equal-rank root-import defects at indexes 2 and 10, complete rendered
UTF-8 path bytes select `root#/imports/10/as`. An index-2-only control selects
`root#/imports/2/as`, proving increasing array traversal and final
rank-then-path-byte order are separate rules. The filler imports are complete,
valid, and introduce no earlier diagnostic.

Failure returns one primary object containing code and path, plus canonical
cycle detail only for `RESOLVE_IMPORT_CYCLE`. It returns no ResolvedSource and
no partial selection.

## Exact successful output

Successful `ResolvedSource` binds exactly the accepted twelve conceptual
members:

```text
scanned_source
active_profile
existing_lock
resolution_passes
selected_packages
selected_modules
applicable_requirements
import_graph
created_identities
created_artifacts
authority
phase_status
```

The first member is the exact consumed ScannedSource. The output retains every
semantically relevant pass, reuse, selected-record, selected-module,
requirement, provenance, and graph observation required by the erratum.
`created_identities` and `created_artifacts` are empty, `authority` is
`none`, and `phase_status` is
`non_authoritative_resolved_source`.

PC7 creates no identity. ResolvedSource, its trace, selected set, and graph
remain non-authoritative phase state. Existing package identities remain PC6
identities; an existing `lock_id` is verified input only.

Expected `scanned_source` is built before Resolve solely through the accepted
PC2-through-PC6 fixture construction. Its complete projection contains exact
`active_profile`, `blueprint_digest`, `defaulted_root`, and the complete
ordered PC6 packages with full descriptors, package identities, paths,
declared digests, and retained bytes. The expected member MUST NOT be read,
copied, substituted, erased, or normalized from actual ResolvedSource output.
The complete twelve-member actual and expected outputs are compared. A
relation also replaces only expected `scanned_source` with a deliberately
wrong value; the correct comparison MUST be equal and that comparison MUST be
unequal.

## Operational resource treatment

Resolve semantics are finite and deterministic over finite accepted input.
The 256-pass rule is the sole semantic convergence bound. Memory, stack,
cache, scheduling, platform, locale, clock, randomness, filesystem, and
network state cannot select a semantic result.

Operational resource failure is a non-result outside `ResolveOutcome`. It
cannot substitute for a success or Resolve diagnostic and produces no partial
ResolvedSource.

## Strict deferral

PC7 does not generate, canonicalize for generation, identify, write, or
persist a Lockfile. Lock exclusively owns new canonical Lockfile content, new
`lock_id`, and atomic persistence.

PC7 does not own namespace expansion, import flattening, imported declaration
defaults, declaration validation, normalization, generated intake gates,
static checking, declaration identities, later collection sorting, Manifest,
qualification, Binding, Builder, runtime, providers, installation, CLI, MCP,
UI, Android, filesystem effects, network effects, secrets, models, events,
replay, or any product surface.

## Durable conformance criteria

The exact machine-readable manifest retains every authoritative schema,
construction rule, generator vocabulary, input, expected output, canonical
byte and hash, diagnostic code and path, precedence criterion, relation
selector, projection rule, chain-255 constructor, reference-expansion rule,
pass-boundary case, coverage ledger, and reference-closure datum reviewed for
PC7.

It contains 118 current fixtures: 81 diagnostic, 31 ordinary success, and 6
success-relation rows. It separately retains 4 non-dispatchable future
vectors. The current manifest closes exactly 21 diagnostic codes, 127 schema
categories, 15 schema discriminators, 45 registered new choices, 11 reachable
rank comparisons, 10 mandatory gate-order criteria, 1 path-order criterion,
1 scanned-source discriminator, and 255 generated chain records. NC-01
through NC-39 and NC-41 through NC-46 are registered; NC-40 remains
intentionally absent.

The authoritative-data populations are exactly 105 byte constants, 38 Lock
inputs, 57 module oracles, 67 package records, 112 Resolve inputs, and 31
successful outputs. The 118 fixture IDs, sorted by unsigned UTF-8 bytes and
joined with LF including a final LF, form 2,576 bytes with SHA-256
`ab7b72bdb33a255d2539a204cd880fa7aedab61b8672cfa3f02d8342d510f221`.
All fixture-ID arrays use that same strict UTF-8 comparator; no accepted-byte
grandfathering exists. A valid adjacent inversion rejects at the first later
element's exact JSON Pointer.

The 57 module-oracle keys are exactly the 67 package-record keys minus the six
named current records that are never selected in the extreme-version
fixtures and the four named records used only by the non-dispatchable numeric
duplicate-conflict vector. `path_order_boundary` is optional and no longer
falls outside the fixture-diagnostic member partition. Authority preflight
paths and manifest-root JSON Pointers are disjoint terminal types, so every
schema-discriminator expected path matches exactly one union variant.
`authority_preflight_discriminator` is the closed fifth new-choice coverage
classification. The two older diagnostic future vectors require
`packages/duplicate_pkg/1.0.0`; the numeric-order vector requires
`packages/duplicate_pkg/2.0.0`; the collapse vector has no diagnostic path.
The vector remains non-dispatchable and no composition seam is created.

The third repair adds no fixture, package, discriminator, or registered
normative choice. It adds one closed schema category solely to type the
raw-byte unknown-member discriminator. The populations are 118 current
fixtures, 4 future vectors, 127 schema categories, 14 schema discriminators,
and 45 registered choices. The durable registry construction remains the one
`[N]` NC-46 authority-preflight choice. Correcting unknown-member precedence
and binding it to actual supplied bytes are `[C]`; the total pre-schema
serializer is `[N, NC-46]` completion of that already registered invalid-input
choice, not a separately observable NC-47. The five second-repair schema
repairs remain `[C]`, except that the future-only vector binding remains
`[D]`.

The fourth repair also adds no fixture, package, discriminator, schema
category, or registered normative choice. Its required
`registry_string_domain` string is contained by the existing
`authority_preflight` schema. The Unicode-scalar admission and exact
surrogate-pair rule are a substantive `[N, NC-46]` completion of NC-46's
already registered strict authority-intake decision, not a separately
dispatchable NC-47. All declared populations therefore remain unchanged.

The fifth repair adds no fixture, package, schema category, or registered
normative choice. It adds only
`AUTHORITY-D-REGISTRY-UNPAIRED-SURROGATE`, increasing the exact discriminator
population from 14 to 15, and binds it directly to NC-46 without replacing
`AUTHORITY-D-RESOLVE-SENTENCE-MUTATION`. Its closed optional fields are
admitted only on that exact discriminator ID. This is durable specified
criteria for the already selected `[N, NC-46]` scalar-intake semantics, not a
new NC-47 or other semantic choice.

The manifest requires set equality, not equal counts alone, for defined,
generated, and—only after later execution—executed current fixture IDs. It
also closes every forward and reverse reference, coverage reference, array
order, population, expected structure, canonical byte count, and SHA-256.
Unknown fields, duplicate IDs or JSON keys, dangling or ambiguous references,
unused authoritative data, invalid ranks or stages, invalid array order, and
undispatched current rows are strict conformance-tool rejections.

These repaired criteria are not yet implemented by the existing generator or
interpreter. They are therefore only specified and do not yet sustain an
implementation-completeness claim. A later implementation gate must prove:

```text
defined_fixture_ids == generated_plan_ids == executed_fixture_ids
```

and compare complete results through the public PC7 boundary before maturity
can advance.

## Implementation boundary

This accepted repair creates no Rust type, function, diagnostic
implementation, fixture interpreter, deterministic plan generator,
production test, Cargo change, dependency, artifact, or product behavior.
Existing implementation and earlier implementation evidence are invalidated
against the refrozen authority. Fresh qualification remains false.

The next bounded task is a separate read-only implementation and
executable-conformance impact assessment. It may identify exact bounded
implementation, generator, interpreter, plan, and qualification deltas but
must not modify repository content.

The governing fourth review derived the repaired PC7-SR3-IR-P1-01 semantics
and identified the distinct durable-criteria defect PC7-SR4-IR-P1-01.
The governing fifth review independently recomputed PC7-SR4-IR-P1-01 closed.
PC7-IR-P1-02 through PC7-IR-P1-06 remain independently recomputed.
PC7-AJ-P3-01 remains dormant, open, future-only, non-dispatchable, excluded
from current populations, and non-blocking.

```text
PC7_SEMANTIC_FREEZE_REOPENED=false
PC7_SEMANTIC_AND_CRITERIA_THIRD_REPAIR_CANDIDATE_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_THIRD_REPAIR_REVIEW_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FOURTH_REPAIR_CANDIDATE_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FOURTH_REPAIR_REVIEW_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FIFTH_REPAIR_CANDIDATE_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_FIFTH_REPAIR_REVIEW_COMPLETE=true
PC7_SEMANTIC_AND_CRITERIA_REPAIR_ACCEPTED=true
PC7_SEMANTIC_AND_CRITERIA_REPAIR_PUBLISHED=true
PC7_SEMANTICS_FROZEN=true
PC7_IMPLEMENTATION_STARTED=true
PC7_FOCUSED_QUALIFICATION_COMPLETE=false
PC7_IMPLEMENTATION_VERIFICATION_COMPLETE=false
PC7_IMPLEMENTATION_REVIEW_COMPLETE=false
PC7_ACCEPTED=false
PUSH_COMPLETE=true
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
FIXTURE_MATURITY=specified
REPAIR_ATTEMPTED=true
REVIEW_STATUS=fifth_repair_independently_reviewed_and_accepted
REVIEW_P0=0
REVIEW_P1=0
REVIEW_P2=0
REVIEW_P3=1
NEXT_BOUNDED_TASK=separate read-only PC7 implementation and executable-conformance impact assessment against the refrozen semantic authority; identify the exact bounded implementation, generator, interpreter, plan, and qualification deltas without modifying repository content
```
