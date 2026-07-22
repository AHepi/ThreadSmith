# PC5 Digest-Phase Freeze Verification

Verification date: 2026-07-22.

## Baseline and scope

| Field | Value |
|---|---|
| Repository branch | `main` |
| Initial local and remote commit | `4aff4c567c241a1b29ab0681c8e0a83826f3c83f` |
| Initial local and remote tree | `e196d28d5a4b93199fc8e20d9134ba80677b8f33` |
| Initial worktree | Clean |
| PC5 product implementation | Not started |
| Original Standard SHA-256 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379`, unchanged |
| Default Semantics Erratum SHA-256 | `ed5d32095abe2f834f19cef20d27f20d60469ecf0ac1367ed75e4725e2527766`, unchanged |
| Canonical JSON Erratum SHA-256 | `ac772adc17a98bb9ecd6f9916717d696a1614918e79fc996546742f0cd6015b7` |

The task changed only the new Canonical JSON Erratum, `docs/pc5/**`,
`conformance/pc5/digest/**`, and additive PC5 entries in the three durable
state files. It did not modify Rust source, Cargo files, dependencies, the
recovered Standard, the accepted Default Semantics Erratum, or any
Foundation-through-PC4 conformance artifact.

## Verification results

| Check | Result |
|---|---|
| `git fetch origin main` and branch comparison | Pass at intake; local `main` and `origin/main` had the same commit and tree |
| Fixture JSON parsing | Pass |
| Fixture identity uniqueness | Pass: 33 unique case/group/requirement IDs |
| Referenced document paths | Pass |
| Canonical byte vectors | Pass: 8 exact byte-hex values and 8 SHA-256 values |
| Source-equivalence group | Pass: 5 YAML presentations independently project/default to one expected value, byte stream, and digest |
| Digest distinctions | Pass: 8 exact expected digests and every named inequality |
| Profile boundary | Pass: alternate profile changes the canonical preimage and is separately rejected with `SOURCE_INVALID_ROOT_VALUE` at `/profile` |
| Later-invalid digestibility | Pass: 6 independently projected/defaulted cases have the frozen hashes |
| Independent encoder cross-check | Pass: separate Python and JavaScript implementations agree on the escape, Unicode, key-order, signed-`i64`, and complete Blueprint vectors |
| Accepted Foundation/PC1/PC2/PC3/PC4 test binaries | Pass: 43 passed, 0 failed |
| Original Standard and Default Erratum hashes | Pass: unchanged |
| Product, Cargo, dependency, and prior-conformance diff | Pass: no change |
| `git diff --check` | Pass |

The 43 accepted test binaries comprise 5 schema/authority, 7 canonical, 5 PC1,
16 PC2, 7 PC3, and 3 PC4 tests. They were rerun directly from the accepted
baseline build artifacts in this checkout.

## Toolchain limitation

This fresh shell did not contain `rustc` or `cargo`, and the previously recorded
external Rust toolchain path no longer existed. No toolchain or package was
installed because the documentation-only scope did not authorize installation.
Consequently `cargo fmt`, workspace check, Clippy, and a fresh locked/offline
rebuild were not rerun.

This does not mask a product-code result: no Rust source, manifest, lockfile, or
dependency changed, the accepted 43 test binaries reran successfully, and the
published PC4 verification already records the full static and locked/offline
qualification for the unchanged product tree. A later PC5 implementation may
not rely on this substitute; it must run the real pinned Rust formatting,
all-target, Clippy, test, locked/offline, and dependency checks before
acceptance.

## Proven

The freeze uniquely selects canonical JSON bytes for every value reachable in
`DefaultedSource`; the complete post-default root is the Blueprint preimage;
only one Blueprint identity is created; `DigestedSource` binds that identity to
the exact input; duplicate names and all other later-invalid content remain
digestible; canonical bytes are not PC5 output metadata; and no later identity,
artifact, or authority enters the phase.

The fixture manifest is internally coherent and its critical golden bytes and
hashes agree across two independent calculations. Its source cases use only
the accepted restricted-YAML surface and independently reproduce the frozen
PC3 and PC4 transformations.

## Not implemented or proven

No `BlueprintDigest`, `DigestedSource`, `digest_source`, PC5 canonical encoder
change, path dependency, implementation test, package scan, package identity,
Lockfile, import expansion, declaration validation, static check, later
identity, Manifest, persistence, qualification, Binding, runtime, replay,
Builder, provider, or user surface is implemented.

The documentation gate does not prove that the future Rust PC5 implementation
passes the new vectors, cross-platform behavior, binary reproducibility, or
release readiness. Those claims require the separately authorized
implementation and qualification gate.
