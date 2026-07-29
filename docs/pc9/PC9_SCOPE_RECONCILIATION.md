# PC9 Expand Scope Reconciliation

Candidate date: 2026-07-29.

Acceptance date: 2026-07-29.

Status: accepted and frozen PC9 Expand scope reconciliation. The governing
independent re-review closed `PC9-SEM-001`, `PC9-CRI-001`, `PC9-CRI-002`, and
`PC9-CRI-003` with P0=P1=P2=P3=0, no refuted, underdetermined, or unverified
claim, and final disposition `PASS`. The substantive reconciliation region is
byte-identical to the reviewed candidate. PC9 implementation has not started
and overall PC9 product acceptance remains false.

## 1. Authenticated baseline and mutation boundary

The authoring gate authenticated:

```text
Repository=/workspace/ThreadSmith/repository
Remote_repository=AHepi/ThreadSmith
Branch=main
HEAD=630b664af272afaffb514b9dde8275cfc95357e9
Tree=f0d0303b3734da350f423f8ad146bcd4f32b5eee
Parent=eb6f1e35d314f3c436402f122f4752e4ecc34073
Subject=Implement and accept PC8 Lock
Local_main=630b664af272afaffb514b9dde8275cfc95357e9
Cached_origin_main=630b664af272afaffb514b9dde8275cfc95357e9
Fresh_remote_main=630b664af272afaffb514b9dde8275cfc95357e9
Ahead=0
Behind=0
Index=empty
Tracked_differences=absent
Untracked_paths=absent
Applicable_AGENTS.md=none
```

The authorized repository overlay is exactly:

```text
docs/standard/LATTICE_STANDARD_0.3_EXPAND_SEMANTICS_ERRATUM.md
docs/pc9/PC9_SCOPE_RECONCILIATION.md
docs/pc9/PC9_SEMANTIC_FREEZE.md
docs/pc9/PC9_EXPAND_SPECIFIED_CONFORMANCE_MANIFEST.json
```

No accepted file, durable state, implementation, test, generated plan,
conformance result, Cargo file, Git index entry, ref, or remote is mutable in
this gate.

## 2. Authority hierarchy and authenticated identities

The Standard is primary. Accepted semantic companions control only their
declared domains. Phase reconciliations and freezes preserve accepted phase
boundaries. Specified manifests are criteria rather than independent semantic
authority. Registries, acceptance records, and external reports are
procedural evidence and do not become dispatchable normative rules.

| Order | Classification | Path | Bytes | Lines | SHA-256 | PC9 role |
|---:|---|---|---:|---:|---|---|
| 1 | normative | `docs/standard/LATTICE_STANDARD_0.3.md` | 66,657 | 2,492 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` | Primary phase, import, namespace, collision, identity, and diagnostic allocation |
| 2 | normative | `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` | 10,019 | 238 | `ed5d32095abe2f834f19cef20d27f20d60469ecf0ac1367ed75e4725e2527766` | Exact default targets, values, traversal, preservation, and identity participation |
| 3 | normative | `docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` | 6,173 | 154 | `ac772adc17a98bb9ecd6f9916717d696a1614918e79fc996546742f0cd6015b7` | Existing identity and artifact byte preservation |
| 4 | normative | `docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md` | 152,906 | 2,621 | `235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25` | Exact retained selected-module bytes and PC6 identities |
| 5 | normative | `docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md` | 1,413,209 | 36,748 | `a0ab4b4eaa0e06d0105fd43b06e684c7581e7b359d6a89cc76eb44b9057fc72e` | Exact ResolvedSource, admitted imports, graph, provenance, parses, and cycle exclusion |
| 6 | normative | `docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md` | 25,595 | 442 | `bd44aa9d43c6b6abf354f0ca556a66fbab97a06b3c24f21394ffe7769e3875bc` | Exact LockedSource, Lockfile, bytes, identity, and Expand handoff |
| 7 | normative | `docs/pc4/PC4_SCOPE_RECONCILIATION.md` | 7,305 | 147 | `53030b8579035a5868fae896729c79700026d7a77c86ff4964a92d72cae16e75` | Root Default boundary and imported-content exclusion |
| 8 | normative | `docs/pc4/PC4_SEMANTIC_FREEZE.md` | 7,753 | 223 | `1b245fecd519f8c9f61f15533421a501af00d2b96894ab3267e84b2352b39119` | Frozen exact insertion algorithm and no-provenance representation |
| 9 | normative | `docs/pc5/PC5_SCOPE_RECONCILIATION.md` | 11,875 | 231 | `63a789ac00c66f09f32b9260beb82897a9f5eff40dfc50d9dff06058b4f0d325` | Post-default pre-import Blueprint digest boundary |
| 10 | normative | `docs/pc5/PC5_SEMANTIC_FREEZE.md` | 9,731 | 279 | `79cd2d924f0e64278c9fe81947d6d25aa6812fbc333f9d2654f7607f888be85b` | Exact root preimage and later-invalid preservation |
| 11 | normative | `docs/pc6/PC6_SCOPE_RECONCILIATION.md` | 26,150 | 589 | `5f8594cc52446755907f4f18b754e0d95a8433b92345f77d92ea91c4c42f51f7` | Selected package and immutable snapshot boundary |
| 12 | normative | `docs/pc6/PC6_SEMANTIC_FREEZE.md` | 8,012 | 214 | `4e444eaac263b453d5d80252f28a63db919fa36efb9fef0dc98319ca0e7e0204` | Exact ScannedSource and retained bytes |
| 13 | normative | `docs/pc7/PC7_SCOPE_RECONCILIATION.md` | 38,667 | 582 | `4cee5f0beacd663ee9ab3bb9c05060342de18c1d6d7b56d3a477c46c15d80243` | Resolve phase allocation and later Expand ownership |
| 14 | normative | `docs/pc7/PC7_SEMANTIC_FREEZE.md` | 30,129 | 589 | `47f2b65f3807e0fe4940c7c6c15475fa472f0a578dba2bccaaba670e43654169` | Frozen successful source, graph, selected-module, and diagnostic boundary |
| 15 | normative | `docs/pc8/PC8_SCOPE_RECONCILIATION.md` | 34,394 | 473 | `a41990db0e2263a94356b2d87783e8f484d464e3f503200255aa0e81a3072c73` | Resolve-to-Lock-to-Expand source-bound allocation |
| 16 | normative | `docs/pc8/PC8_SEMANTIC_FREEZE.md` | 15,024 | 267 | `c23f846c3dc7e795551f9fc2fbd0e65b2ba5bbc91eec269a5dda8490e231a0b1` | Frozen exact LockedSource and non-authority handoff |
| 17 | specified criteria | `docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json` | 1,306,575 | 35,116 | `da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c` | Accepted public PC7 construction and semantic-projection shapes |
| 18 | specified criteria | `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V2.json` | 1,053,112 | 25,732 | `314e1cd73f23c07067e167d37e84782c7a301b13b4c6458d62a37d0423c4482a` | Current accepted PC8 construction and LockedSource criteria |
| 19 | procedural | `docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json` | 2,041 | 55 | `7f39265be8bfd6db9fc93cedf357572eb5fab960000b9d6897ef983021112161` | PC7 accepted authority closure; non-normative |
| 20 | procedural | `docs/pc8/PC8_AUTHORITY_REGISTRY_V2.json` | 21,344 | 525 | `b442f1acb4a7eb316ed9d61da02af3c1e5c60c34f55cf6eefefa751339d0a2c6` | Current PC8 criteria routing; non-normative |
| 21 | procedural | `docs/pc8/PC8_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md` | 13,175 | 299 | `ab9da161e5011f51d6689bb53224cde6b5d5c235dc621d3a062581243702740b` | Published PC8 product boundary and PC9 authorization; non-normative |

Production code and tests were not consulted to select semantics.

## 3. Lifecycle reconciliation

```text
accepted source-bound PC8 LockedSource
                    |
                    v
                  Expand
  rooted import-path instantiation
  alias namespace construction
  imported default materialization
  declaration flattening and provenance
  NAMESPACE_COLLISION
                    |
                    v
 non-authoritative ExpandedSource
                    |
                    v
                 Normalize
```

Physical Lockfile persistence is not on this dependency path. Expand consumes
the accepted in-memory `LockedSource`.

## 4. Gap classification

| Gap | Class | Competing readings | Candidate closure |
|---|---|---|---|
| `EXPAND-GAP-01` | absence | Consume ResolvedSource, Lockfile, or independently paired fields | Exactly one accepted `LockedSource` |
| `EXPAND-GAP-02` | ambiguity | One namespace instance per selected package or per import path | One per root-to-node edge path |
| `EXPAND-GAP-03` | ambiguity | Alias, package, or module name forms namespace segments | Exact admitted alias segments |
| `EXPAND-GAP-04` | absence | Breadth-first, selected-package order, graph-edge order, or source-order DFS | Source-index depth-first pre-order |
| `EXPAND-GAP-05` | contradiction risk | PC4 excludes package traversal while later declaration identities require defaults | Exact PC4 algorithm applied to copied imported parsed modules inside Expand, without changing PC4 output or Blueprint digest |
| `EXPAND-GAP-06` | absence | Which root collections flatten and which field names them | Exact eight-collection registry |
| `EXPAND-GAP-07` | ambiguity | Rewrite bodies now or carry namespace context to Normalize | Preserve bodies and carry exact context |
| `EXPAND-GAP-08` | absence | Imported invalid declarations fail Expand or remain later | Preserve with null effective name; Normalize owns validity |
| `EXPAND-GAP-09` | ambiguity | Collision across all names, per class, or only source duplicates | Per collection/effective-name key with imported participation |
| `EXPAND-GAP-10` | absence | Collision group and path selection | Closed collection/name/numeric-ordinal order |
| `EXPAND-GAP-11` | absence | Flattened membership, order, and provenance representation | Closed record and output structures |
| `EXPAND-GAP-12` | ambiguity | Expand creates identities or artifacts | Both created populations empty |
| `EXPAND-GAP-13` | absence | Exact Normalize intake | Consume exact ExpandedSource and contexts; no re-expansion |
| `EXPAND-GAP-14` | absence | Closed specified criteria and maturity | Standalone closed manifest at specified-only maturity |

There is no accepted-authority contradiction after applying amendment
precedence. `EXPAND-GAP-05` is resolved by allocating the first possible
package-content default materialization point without reopening the already
completed root Default phase.

## 5. Exact input and preserved state

The input is exactly one immutable accepted `LockedSource`. The following are
preserved transitively and may only be read through it:

```text
exact ResolvedSource
exact ScannedSource and DigestedSource
exact root DefaultedSource
exact blueprint_digest
exact selected PC6 package records and package identities
exact retained selected-module bytes and declared digests
exact retained parsed selected-module representations
exact admitted import projections and source indexes
exact converged requirements, graph, and edge provenance
exact canonical Lockfile, lock_id, and emitted bytes
```

Expand has no host capability. It does not require a current directory,
package snapshot, Lockfile path, network, clock, randomness, provider,
environment variable, cache, compiler metadata, or persistence result.

## 6. Namespace-instance model

Resolve selects one package version per package name. Expand does not duplicate
that selection. It instantiates the selected module once for each rooted
import-edge path because aliases describe composition occurrences rather than
package selection records.

For:

```text
root --alias a--> alpha --alias g--> gamma
root --alias b--> beta  --alias z--> gamma
```

the instance namespaces are exactly:

```text
a
a::g
b
b::z
```

under depth-first pre-order. The one selected `gamma` record is reused as
immutable input for two distinct namespace instances. No instance is
deduplicated by package identity.

## 7. Imported defaults without reopening PC4

PC4 remains exactly the pre-Digest root operation. The root value and its
Blueprint digest remain byte-for-byte and identity-for-identity unchanged.

Resolve necessarily parsed selected module bytes to admit transitive imports
but explicitly deferred imported declaration defaults. Expand is the first
phase whose declared purpose activates imported declarations. The candidate
therefore applies the already accepted PC4 algorithm to a copy of each retained
parsed module representation before flattening that instance.

This allocation:

- introduces no new default value or target;
- adds no provenance marker to the copied value;
- does not call the public PC4 phase or create `DefaultedSource`;
- does not replace the retained parsed representation;
- does not change `blueprint_digest`, package identity, Lockfile, or `lock_id`;
- does not validate declaration forms or references; and
- gives later declaration identities the applicable expanded default values
  required by accepted authority.

## 8. Declaration movement

The eight flattened collections are:

```text
inputs contracts resources units links policies exports scenarios
```

Root records remain first in source order. Imported records follow by
module-instance order and then selected module source-array order. Each record
contains the original collection, namespace sequence and rendering, nullable
effective name, exact source value, and complete source-bound provenance.

`imports` is consumed as composition control and is not emitted as a
declaration. Imported module metadata remains in the module-instance copied
value. No declaration is filtered by an invented visibility rule.

## 9. Names, references, and Normalize

Expand needs only the collection discriminator to construct an
`effective_name` candidate. Valid local names receive the current namespace;
malformed headers remain present with `effective_name=null`.

Declaration bodies are not rewritten. Each module context records direct alias
to child-namespace bindings. Normalize receives those bindings and the exact
source body, so it can later validate and interpret local and direct-import
references without reparsing or reconstructing import state.

This boundary intentionally prevents Expand from silently taking Normalize's
declaration-form, reference, endpoint, compatibility, or resolved-form work.

## 10. Collision and diagnostic ownership

Expand owns only `NAMESPACE_COLLISION`. A collision requires equal
`(collection, effective_name)` and at least one imported participant. Root-only
duplicates remain available for later `SOURCE_DUPLICATE_NAME` allocation.
Malformed names do not become collision keys.

Collision discovery completes before selection. Primary selection is by
collection rank, effective-name bytes, numeric second ordinal, then numeric
first ordinal, where each ordinal is the zero-based position in the complete
frozen collection order. The path names the second occurrence. A failure
returns no partial `ExpandedSource`.

`RESOLVE_IMPORT_CYCLE` cannot enter this gate. Other declaration and static
diagnostics remain later.

## 11. Successful output and authority boundary

The exact successful conceptual members are:

```text
locked_source
root_reference_context
module_instances
declarations
created_identities=[]
created_artifacts=[]
authority=none
phase_status=non_authoritative_expanded_source
```

The wrapper, namespaces, copied module values, declaration records, reference
contexts, and provenance receive no Lattice identity. Expand does not alter
existing identities and does not create an artifact or permission.

## 12. Determinacy inventory

| Observable | Complete determining rule |
|---|---|
| Accepted input | One exact accepted LockedSource |
| Success/failure branch | Complete collision population after expansion |
| Instance membership | Every finite root-to-node import-edge path |
| Instance order | Source-index DFS pre-order |
| Namespace | Exact alias segment sequence and `::` join |
| Imported value | Exact retained parse plus exact PC4 insertions |
| Flattened membership | All elements of eight root/imported collections |
| Flattened order | Root first; then instance order; then source index |
| Effective name | Valid discriminator plus namespace, otherwise null |
| Provenance | Root or selected package/module plus complete edge chain |
| Reference context | Direct alias to child namespace in source order |
| Diagnostic | Exact code, path, four-member detail, and group precedence |
| Created state | Empty identity and artifact sequences; authority none |
| Next consumer | Exact ExpandedSource to Normalize |

Expand creates no canonical bytes, digest, signature, or identity. An Expand
identity-preimage registry would therefore invent an observable and is
intentionally absent.

## 13. Specified-conformance coverage

The standalone manifest declares exact populations:

| Population | Cardinality |
|---|---:|
| accepted authority records | 21 |
| classified rule bundles | 49 |
| normative choices | 19 |
| declaration collections | 8 |
| recursively closed schemas | 23 |
| current public constructions | 20 |
| current fixtures | 20 |
| success/failure relations | 15 |
| collision-selector probes | 7 |
| input/ambient boundary probes | 2 |
| declared post-schema validators | 1 |
| discriminators | 32 |
| isolated schema mutations | 10 |
| future-only rows | 5 |

Current constructions begin with exact root source bytes and exact portable
snapshot content and proceed through public PC2, PC3, PC4, PC5, PC6, PC7, and
PC8 boundaries. They do not forge phase state. Expected outcomes are retained
as complete canonical JSON semantic projections and independently declared
hashes. Failure rows admit only their exact diagnostic.

The fixture set distinguishes alias versus package naming, direct versus
chained namespaces, per-path versus per-package instantiation, DFS versus
breadth-first order, root source order, source indexes 2 and 10, imported
omitted versus explicit defaults, exact parsed-value preservation, eight
collection membership, imports exclusion, root-first ordering,
malformed-name deferral, cross-collection equality, root-only duplicates,
zero-based ordinal origin, collection-rank precedence, effective-name byte
precedence, numeric first and second ordinal behavior, rendered-decimal
rejection, first-two selection from a three-member collision group,
reference-context creation, absence of body rewrite, Lock preservation, a
controlled ambient pair, a public PC7-intermediate negative invocation, and
empty created state.

The five future-only rows name their activation conditions and are excluded
from current dispatch. The manifest has maturity `specified`; no generator,
plan, interpreter, public dispatch, execution, qualification, or independent
review result exists.

## 14. Rule-provenance summary

The focused erratum contains the complete 49-row ledger:

```text
[S]=12
[C]=10
[N]=19
[D]=8
TOTAL=49
```

Every `[N]` rule has exactly one `EXPAND-NC-*` identifier and at least one
named discriminator. The manifest's `rule_provenance` and
`normative_choices` populations must equal those exact sets, not only those
counts.

## 15. Explicit exclusions

This candidate does not:

```text
change PC1-PC8 authority
change root defaults or Blueprint identity
scan, select, parse, converge, or reject cycles
change Lockfile content, bytes, lock_id, or persistence
normalize declaration forms or resolve references
insert generated gates
statically check declarations
identify or canonically sort declarations
create or persist a Manifest
qualify, bind, execute, record, or replay
authorize Builder, runtime, providers, installation, CLI, MCP, UI, or Android
implement code, tests, generators, interpreters, or plans
accept, freeze, stage, commit, push, or publish PC9
```

## 16. Accepted reconciliation disposition

```text
PC8_ACCEPTED=true
PC9_SCOPE_RECONCILIATION_CANDIDATE_COMPLETE=true
PC9_SEMANTIC_FREEZE_CANDIDATE_COMPLETE=true
PC9_SPECIFIED_CONFORMANCE_CANDIDATE_COMPLETE=true
PC9_SCOPE_RECONCILIATION_REPAIR_COMPLETE=true
PC9_SEMANTIC_REPAIR_COMPLETE=true
PC9_CRITERIA_REPAIR_COMPLETE=true
PC9_GOVERNING_FINDINGS_CLOSED=4
PC9_REVIEW_P0=0
PC9_REVIEW_P1=0
PC9_REVIEW_P2=0
PC9_REVIEW_P3=0
PC9_SEMANTICS_ACCEPTED=true
PC9_SPECIFIED_CONFORMANCE_ACCEPTED=true
PC9_SEMANTIC_FREEZE_COMPLETE=true
PC9_SEMANTICS_FROZEN=true
PC9_DOCUMENTATION_PUBLISHED=true
PC9_IMPLEMENTATION_STARTED=false
PC9_QUALIFIED=false
PC9_ACCEPTED=false
OPEN_PC9_NORMATIVE_DEFECTS=0
OPEN_PC9_CONFORMANCE_CRITERIA_DEFECTS=0
OPEN_PC9_IMPLEMENTATION_DEFECTS=0
OPEN_PC9_PROCEDURAL_DEFECTS=0
OPEN_NORMATIVE_DEFECTS=0
OPEN_CONFORMANCE_CRITERIA_DEFECTS=0
OPEN_IMPLEMENTATION_DEFECTS=0
OPEN_PROCEDURAL_DEFECTS=0
FIXTURE_MATURITY=specified
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
PUSH_COMPLETE=true
FINAL_DISPOSITION=PASS
NEXT_BOUNDED_TASK=separate read-only PC9 implementation and executable-conformance impact assessment against the newly frozen authority
```
