# PC3 Scope Reconciliation

Reconciliation date: 2026-07-22.

## Controlling evidence

| Evidence | Role |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Controlling specification; recovered SHA-256 `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| `docs/pc2/PC2_STANDARD_RECONCILIATION.md` | Accepted allocation of parsing to PC2 and source validation to PC3 |
| `docs/pc2/PARSER_SEMANTIC_FREEZE.md` | Accepted PC2 input/output and information-preservation boundary |
| `crates/threadsmith-compiler/src/lib.rs` and `tests/pc2_parser.rs` | Accepted PC2 implementation and regression route |
| `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, `DECISIONS.md` | Repository state, tranche sequence, and durable decisions |
| `docs/adr/0001-portable-core-language.md` | Accepted Rust ownership boundary |
| Git history through `94c3978` | Published PC2 Standard-aligned provenance baseline |

Foundation and PC1 artifacts constrain identity, canonical-byte, native/legacy, migration, and authority behavior. PC3 does not reopen them.

## Lifecycle reconciliation

The Standard fixes this order:

```text
Read -> Parse -> Source validate -> Default -> Digest -> Package scan ->
Resolve -> Lock -> Expand -> Normalize -> Insert -> Static check ->
Identify -> Sort -> Manifest -> Persist
```

PC2 owns `Parse`. The immediately following responsibility is therefore:

```text
PC3 = Source validate
PC3 output = Valid root shape
```

The output phrase is controlling. PC3 is not a general semantic checker. The later `Default`, `Normalize`, and `Static check` phases remain distinct even when an implementation could technically perform one of their checks earlier.

## Ownership

| Item | Frozen allocation |
|---|---|
| Owning crate | `threadsmith-compiler` |
| Input owner | PC2 parser in `threadsmith-compiler` |
| PC3 responsibility | Validate the Core Blueprint root envelope and compatibility selectors without changing the parsed tree |
| PC3 output | A non-authoritative validated-source wrapper over the unchanged PC2 value tree |
| Immediate consumer | The later Standard `Default` phase |
| Schema crate | `threadsmith-schema` remains schemas and data structures; it does not own source parsing or phase control |

No new crate or dependency is selected.

## Exact PC3 responsibility

PC3 validates only these facts:

1. the PC2 value is an object;
2. its root keys are drawn exactly from the Standard section 10 allowlist;
3. all six required root keys are present;
4. `lattice`, `profile`, `module`, `version`, and `purpose` are strings;
5. `lattice` is exactly `0.3` and `profile` is exactly `lattice-core-0.1`;
6. `module` matches the Standard local-name grammar;
7. `version` has the Core `MAJOR.MINOR.PATCH` form: three non-empty ASCII-decimal components and no prerelease or build suffix;
8. `imports`, `inputs`, `contracts`, `resources`, `units`, `links`, `policies`, `exports`, and `scenarios`, when present, are arrays.

The validation order is:

```text
lattice, profile, module, version, purpose, imports, inputs, contracts,
resources, units, links, policies, exports, scenarios
```

PC3 does not require `purpose` to be non-empty or prohibit leading zeroes in version components because the Standard states neither rule.

## Responsibilities deliberately left later

| Concern considered | PC3 allocation | Reason |
|---|---|---|
| Declaration element schemas and required fields | Deferred | `Source validate` promises only a valid root shape; resolved declaration forms are the later `Normalize` output |
| Declaration-name grammar and uniqueness | Deferred | The Standard requires them but does not assign them to `Source validate`; `SOURCE_DUPLICATE_NAME` remains later |
| Imports, aliases, packages, requirements, and cycles | Deferred | Package scan, Resolve, Lock, and Expand are explicit later stages |
| Contract shape, codecs, limits, and compatibility | Deferred | Declaration normalization and static cross-declaration checks are later |
| Ports, links, producer counts, labels, and references | Deferred | These are cross-declaration validity owned by `Static check` |
| Policy expressions and operators | Deferred | Policy validity is not root shape; `POLICY_UNKNOWN_OPERATOR` remains later |
| Route predicates and ambiguity | Deferred | Routing depends on resolved declarations and belongs to `Static check` |
| Unit kind/mode pairs and Extended-only kinds | Deferred | Profile checking is required but is not the `Valid root shape` output |
| Controller bounds and cycles | Deferred | `CONTROL_UNBOUNDED_CYCLE` is static validity |
| Budgets and limits | Deferred | `BUDGET_INVALID` requires semantic and parent-bound context |
| Secrets and ambient model authority | Deferred | `SECRET_IN_SOURCE` and `MODEL_DIRECT_EFFECT` are static authority checks |
| Portable-Core completeness | Deferred | Completeness requires normalized and expanded declarations |

Deferral does not make these forms valid. It means PC3 neither accepts nor rejects their meaning. A later scope freeze must allocate each check before implementation.

## Authority boundary

PC3 may reject an invalid root envelope and wrap a successfully checked tree with a non-authoritative phase marker. It may not mutate or canonicalize the tree.

PC3 must not apply defaults, compute canonical bytes or hashes, issue identities, scan or resolve packages, create a Lockfile, expand imports, normalize declarations, insert gates, perform cross-declaration static checking, create or persist a Manifest, qualify scenarios, create a Run Binding, or grant execution authority.

## Downstream dependency

The next lifecycle consumer may rely only on the root guarantees listed above. It may not treat PC3 success as proof that declarations, references, contracts, policies, routes, controls, resources, packages, or authority are valid.

## Acceptance criteria

The freeze is acceptable when:

- ownership remains in `threadsmith-compiler`;
- every permitted, required, and typed root rule has an exact fixture;
- omitted optional fields remain absent and explicit empty arrays remain explicit;
- success preserves the PC2 value exactly;
- diagnostics follow `PC3_SEMANTIC_FREEZE.md`;
- boundary fixtures prove later semantic failures are deferred, not compiler-valid;
- Foundation, PC1, and PC2 regressions remain green; and
- no product implementation or dependency mutation occurs.
