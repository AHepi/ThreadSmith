# PC5 Digest-Phase Implementation Read-Only Review

Review date: 2026-07-23.

Status: the repaired PC5 implementation passed its final independent,
compliance-bearing read-only review. The review found no P0 or P1 issue and
recommended PC5 acceptance and publication. The P2 and P3 findings below are
retained as non-blocking debt.

## Baseline and reviewed worktree

| Field | Reviewed value |
|---|---|
| Branch | `main` |
| Baseline commit | `1f6ac46647e49519add2f732fc0148dad05fe6d6` |
| Baseline tree | `1ac37136547c1247854558987a441fc3e4ddab96` |
| Baseline `origin/main` | `1f6ac46647e49519add2f732fc0148dad05fe6d6` |

The exact reviewed worktree was intentionally uncommitted.

Modified:

- `Cargo.lock`
- `DECISIONS.md`
- `IMPLEMENTATION_PLAN.md`
- `PROJECT_STATE.md`
- `crates/threadsmith-canonical/src/lib.rs`
- `crates/threadsmith-compiler/Cargo.toml`
- `crates/threadsmith-compiler/src/lib.rs`

Untracked:

- `crates/threadsmith-canonical/tests/pc5_canonical_json.rs`
- `crates/threadsmith-compiler/tests/pc5_digest.rs`
- `docs/pc5/PC5_IMPLEMENTATION_VERIFICATION.md`

The reviewer read the Standard, both accepted errata, PC2-PC5 reconciliation,
freeze, implementation-verification, and review evidence, the PC5 fixture
manifest, durable state, the complete baseline-to-worktree diff, production
code, and Foundation-through-PC5 tests. The implementation was traced as code
rather than accepted from its tests or verification report alone.

## Reproduced qualification

The reviewer used the existing isolated Rust 1.97.1 toolchain and Cargo cache
with frozen, offline dependency resolution. No download, synchronization, or
installation occurred.

| Command or check | Result |
|---|---|
| `cargo +1.97.1 fmt --all -- --check` | Pass |
| `cargo +1.97.1 check --workspace --all-targets --frozen` | Pass |
| `cargo +1.97.1 test --workspace --all-targets --frozen` | Pass: 52 passed, 0 failed, 0 ignored |
| `cargo +1.97.1 clippy --workspace --all-targets --all-features --frozen -- -D warnings` | Pass: no warnings |
| `cargo +1.97.1 tree --workspace --frozen` | Pass: 31 packages |
| Fixture JSON and category counts | Pass: 8 canonical, 5 equivalent presentations, 8 distinctions, 6 later-invalid cases |
| Canonical byte and SHA-256 vectors | Pass: all 8 |
| Standard, errata, frozen-document, fixture, and prior-conformance integrity | Pass |
| Dependency and edit-boundary checks | Pass; no external dependency added |
| `git diff --check` | Pass |

The 52 tests comprised:

| Suite | Passed |
|---|---:|
| Foundation canonical | 7 |
| Foundation schema | 5 |
| PC1 conformance | 5 |
| PC2 parser | 16 |
| PC3 source validation | 7 |
| PC4 defaults | 3 |
| PC5 canonical JSON | 3 |
| PC5 Digest | 6 |
| **Total** | **52** |

Foundation through PC4 supplied 43 regressions; PC5 supplied 9 focused tests.

## Findings

| Severity | Exact location | Finding and governing concern | Disposition |
|---|---|---|---|
| P0 | None | No catastrophic identity, authority, security, data-loss, or repository-integrity failure was found. | No action. |
| P1 | None | No acceptance-blocking semantic, totality, canonicalization, preimage, source-binding, diagnostic, or phase-ownership defect remained after repair. | No action. |
| P2 | `crates/threadsmith-canonical/src/lib.rs:134-147`; evidence wording at `docs/pc5/PC5_IMPLEMENTATION_VERIFICATION.md:23-28` | The generic canonical API can accept hidden unchecked `serde_json::Number` spellings such as `+1` and `01` and emit non-minimal bytes. These representations are outside the admitted PC5 domain and PC5 rejects both, so no reviewed PC5 digest is affected. | Non-blocking generic canonical hardening debt. A later bounded repair may validate arbitrary-precision integer grammar while preserving arbitrary minimal integers and the accepted `-0` to `0` behavior. |
| P2 | `crates/threadsmith-compiler/tests/pc5_digest.rs:215-243` | Repository tests cover the required rejection categories but do not permanently lock all externally reproduced multi-error ordering, signed-boundary acceptance, non-minimal number spelling, and RFC 6901 escaping cases. External read-only probes confirmed the current implementation. | Non-blocking regression-coverage debt. A later bounded test-only tranche may add table-driven cases. |
| P3 | `crates/threadsmith-compiler/src/lib.rs:23-27` | `SourceDiagnostic` rustdoc names PC2 and PC3 but does not mention the new pre-PC3 value-domain admission boundary. | Non-functional documentation debt. |

Finding totals are P0=0, P1=0, P2=2, and P3=1. The review does not conceal or
repair the retained debt.

## Compliance verdicts

### Public construction and totality

Pass. `ValidatedSource`, `DefaultedSource`, `BlueprintDigest`, and
`DigestedSource` keep private fields. No public constructor, conversion,
deserializer, mutation, or replacement path bypasses admission or breaks the
source/digest binding. Every publicly constructible `DefaultedSource` is in the
canonical PC5 domain, making `digest_source(DefaultedSource) -> DigestedSource`
genuinely total and source-error-free. The canonical invariant failure is not
publicly reachable through the accepted PC2-to-PC5 path.

### Domain admission and deterministic diagnostics

Pass. Pre-PC3 admission accepts exactly null, booleans, minimal signed `i64`
integers, NFC strings, arrays, and objects with NFC keys and no post-NFC key
collision. Invalid caller-created values fail unchanged with
`SOURCE_VALUE_DOMAIN_INVALID`. Arrays use increasing indices; objects use
ascending raw UTF-8 key bytes; object key sets are checked before depth-first
child traversal; paths use RFC 6901; raw-value failures have no source line or
column. Genuine PC2 output retains the frozen PC3 diagnostic precedence.

### Canonical bytes and Blueprint preimage

Pass. The complete exact `DefaultedSource` root is canonically encoded by the
single `threadsmith-canonical` writer and hashed there with SHA-256. Array order
is preserved. All eight golden byte and digest vectors are unchanged. The only
created identity text is
`lattice:blueprint:sha256:<64 lowercase hexadecimal characters>`.

### API opacity and source binding

Pass. `BlueprintDigest` cannot be promoted from an arbitrary generic caller
claim, and `DigestedSource` can be constructed only by consuming one exact
`DefaultedSource` through `digest_source`. The retained source is unchanged.
Canonical bytes are transient and the output contains no provenance,
diagnostic, artifact, permission, Binding, or authority metadata.

### Diagnostics and phase ownership

Pass. `SOURCE_VALUE_DOMAIN_INVALID` is boundary-domain admission before PC3,
not a PC5 diagnostic or declaration validator. Duplicate declaration names,
invalid unit kinds, malformed bodies, unknown references, wrong-type values
inside the PC2 domain, and unresolved imports remain digestible and deferred.
PC5 does not reinterpret digestibility as semantic acceptance.

### Fixtures and test quality

Pass with the retained P2 coverage debt. Tests compare all eight canonical
vectors and independently check their SHA-256 values; exercise all five
equivalent presentations, all eight distinctions, and all six later-invalid
cases; use public phase paths wherever reachable; repeat reachable digests at
least three times; preserve both array orders; verify exact digest text, kind,
source preservation, repeatability, alternate-profile participation, normal
PC3 rejection, and the Foundation arbitrary-integer vector. No malformed
fixture entry is silently skipped.

### Evidence accuracy

Pass with the retained P2 wording caveat about the generic unchecked-number
edge. The implementation verification accurately records Rust 1.97.1,
formatting, frozen all-target checks, 52 passing tests, warning-denied Clippy,
the 31-package frozen tree, fixture and hash results, unchanged controlling
documents, approved local path edges, and no external dependency or network
use.

## Residual risks and recommendation

The review retains the two P2 findings and one P3 finding above. It also notes
inherited unbounded input size/depth resource-exhaustion risk, the absence of a
cross-platform binary-reproducibility proof, and the ordinary cryptographic
assumption that SHA-256 collisions are infeasible. None is an open P0 or P1
within the frozen PC5 boundary.

The independent reviewer recommended PC5 acceptance and publication. The
reviewer edited no file and performed no acceptance, commit, push, network, or
later-phase work.
