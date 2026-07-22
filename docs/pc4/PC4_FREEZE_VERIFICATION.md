# PC4 Default-Phase Freeze Verification

Verification date: 2026-07-22.

## Baseline and scope

| Field | Value |
|---|---|
| Repository branch | `main` |
| Remote-main and local HEAD | `7cf2b504c28398b6e2446d7cc9d61a27f8b81683` |
| Baseline tree | `3183d3162c2201084ff7ee09ad8fc6223800698d` |
| Initial task worktree | The four accepted, uncommitted Default Erratum paths were present; no unrelated change was present |
| PC4 product implementation | Not started |
| Original Standard SHA-256 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379`, unchanged |
| Default Erratum SHA-256 | `ed5d32095abe2f834f19cef20d27f20d60469ecf0ac1367ed75e4725e2527766`, unchanged |

The PC4 task changed only `docs/pc4/**`,
`conformance/pc4/default/**`, and additive PC4 entries in the three durable
state files. It did not modify the accepted erratum, Standard, Rust source,
Cargo files, dependencies, or Foundation-through-PC3 conformance artifacts.

## Results

All Cargo commands used Rust 1.97.1 with the accepted lock and offline cache.

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | Pass |
| `cargo check --workspace --all-targets --locked --offline` | Pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | Pass |
| `cargo test --workspace --all-targets --locked --offline` | Pass: 40 passed, 0 failed |
| Foundation canonical regressions | Pass: 7 |
| Foundation schema/authority regressions | Pass: 5 |
| PC1 conformance regressions | Pass: 5 |
| PC2 parser regressions | Pass: 16 |
| PC3 source-validation regressions | Pass: 7 |
| Standard original-byte hash | Pass: unchanged |
| Default Erratum hash | Pass: unchanged |
| All tracked JSON integrity | Pass |
| PC4 fixture cases and unique IDs | Pass: 9 cases, 9 unique IDs |
| PC4 fixture referenced paths | Pass |
| Expected-output root collections | Pass: every output has all nine arrays |
| Identity-preimage equivalence group | Pass: expected values equal |
| Explicit-nondefault distinction group | Pass: expected values differ |
| Exact target spot checks | Pass: unit, predicate, link, scenario, malformed, and ambiguity expectations |
| Product, Cargo, prior-conformance diff | Pass: no change |
| `git diff --check` | Pass |

One initial documentation assertion matched wording more narrowly than the
document used. The assertion was corrected and passed; no repository or
semantic change was required.

## Proven

The freeze has an exact PC3 input and PC5 consumer, assigns ownership to
`threadsmith-compiler`, defines a non-authoritative expanded-value-only output,
binds every erratum default and preservation rule to exact fixture values, and
defines a no-diagnostic deterministic phase. The fixture manifest proves its
own JSON integrity, unique case identities, output shape, equivalence group,
and distinction group.

## Not proven or implemented

No PC4 public function, `DefaultedSource` Rust type, transformation code,
implementation test, canonical byte stream, digest, identity, package
resolution, Lockfile, import expansion, declaration validation, static check,
Manifest, qualification, Binding, runtime, replay, builder, provider, or user
surface is implemented or proven by this documentation-only gate.
