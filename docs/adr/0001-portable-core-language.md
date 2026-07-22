# ADR 0001: Portable canonical-core language

Date: 2026-07-22

Status: Accepted

Decision owner: Foundation F1

## Context

ThreadSmith requires one portable canonical core for desktop, CLI, local services, MCP, SDK bindings, and Android. The beginner installation path cannot require Python, pip, a virtual environment, a shell, or a separately installed language runtime. Lattice Standard 0.3 permits independent implementation languages but requires fixed normative inputs to produce the same canonical artifacts and identities.

The supplied Python wheel is an isolated legacy oracle. It is not the production dependency or the semantic authority. The F1 baseline had no Rust compiler or Cargo installation. A separately authorized F2 environment prerequisite has since installed and verified the exact toolchain without creating product code.

## Decision

ThreadSmith's portable canonical core will be implemented in stable Rust. Rust owns the native schema, canonical serialization, identity calculation, compilation semantics, deterministic policy, package verification, Run Binding validation, runtime record, and replay semantics as those packages enter their authorized tranches.

Non-Rust surfaces use narrow, versioned bindings over the Rust core. No surface may independently implement canonicalization, identity, Binding, policy, event-fold, package-activation, or replay meaning. Rust is an implementation choice and cannot add, remove, or reinterpret Lattice semantics.

The F2 environment prerequisite selects Rust 1.97.1 through rustup 1.29.0. The repository pin uses the minimal profile plus `clippy` and `rustfmt`. Its numeric channel is host-neutral; the current installation and host standard library were verified for `x86_64-unknown-linux-gnu`. The exact source edition, supported target policy, Cargo workspace, and dependency lockfile remain for the actual F2 implementation scope freeze because this environment-only task forbids product scaffolding.

## Decision factors

| Requirement | Consequence of the decision |
|---|---|
| Desktop, CLI, and services | The same core can build as native libraries and standalone executables without an end-user language runtime. |
| Android | The core can target Android through its native toolchain and a thin platform adapter. Target availability is feasibility evidence only; Android support still requires a real APK and tranche acceptance. |
| One canonical implementation | Canonical bytes, identities, authorization, event state, and replay remain in one implementation rather than being rewritten for each surface. |
| Deterministic semantics | Rust's byte and integer types support the restricted canonical model, but determinism is established only by explicit algorithms and conformance vectors. Rust itself is not evidence of determinism. |
| Beginner distribution | Compiled artifacts avoid exposing Python, package managers, shells, or virtual environments to ordinary users. |
| Boundary safety | Ownership and typed interfaces suit identity and authority code. Any later `unsafe` code must be confined to a separately reviewed FFI or platform module. |
| Legacy compatibility | Python remains available only in the isolated reference area and future differential-test environment. It never becomes a runtime dependency. |

## Binding rule

The binding mechanism is not selected in F1. The owning surface tranche must choose it without changing this boundary.

Bindings exchange versioned canonical UTF-8 bytes or owned byte buffers and stable status/error codes. Stateful interfaces use opaque handles only when unavoidable. Allocation and release ownership are explicit. Rust structs, enums, collections, panics, compiler-dependent layouts, and internal ABI details do not cross the boundary. A platform adapter may translate transport types, but it cannot reinterpret semantic objects or errors.

Android will use a thin managed-to-native adapter over the canonical library. UI and asynchronous lifecycle control remain on the platform side; canonical semantics remain in Rust. The exact JNI or binding generator choice is deferred to the Android paired-client tranche.

## Reproducibility rule

Semantic reproducibility and binary reproducibility are separate claims.

Canonical identities depend only on the Standard-defined preimages. Rust version, host, linker, SDK, build path, compiler metadata, and build timestamp cannot enter a semantic preimage. Manifest identity excludes compiler implementation metadata as required by Lattice Standard 0.3.

The environment gate records the compiler and Cargo versions below. Actual F2 implementation must select its source edition, create and preserve `Cargo.lock`, and use locked dependency resolution as soon as a Cargo workspace exists. Release hardening must additionally control dependency sources, build scripts, native compilers, linkers, SDKs, paths, timestamps, archive ordering, and signing inputs. No byte-reproducible binary claim is permitted until isolated duplicate builds prove it on each supported target.

## Verified toolchain record

| Field | Verified value |
|---|---|
| Rust release | `rustc 1.97.1 (8bab26f4f 2026-07-14)`; full commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452`; LLVM 22.1.6 |
| Cargo | `cargo 1.97.1 (c980f4866 2026-06-30)`; full commit `c980f4866141969fab6254a680546a277789d6f0` |
| rustup | `rustup 1.29.0 (28d1352db 2026-03-05)` |
| Additional components | `rustfmt 1.9.0-stable`; `clippy 0.1.97` |
| Installed component set | cargo, clippy, rust-std, rustc, and rustfmt |
| Verified host and installed target | `x86_64-unknown-linux-gnu` |
| Repository pin | `rust-toolchain.toml`: channel `1.97.1`, profile `minimal`, components `clippy` and `rustfmt` |
| Installer integrity | Official rustup 1.29.0 archive; SHA-256 `4acc9acc76d5079515b46346a485974457b5a79893cfb01112423c89aeb5aa10` |
| `CARGO_HOME` | `/workspace/scratch/15c5bb854ce4/toolchains/threadsmith/cargo` |
| `RUSTUP_HOME` | `/workspace/scratch/15c5bb854ce4/toolchains/threadsmith/rustup` |
| Sysroot | `/workspace/scratch/15c5bb854ce4/toolchains/threadsmith/rustup/toolchains/1.97.1-x86_64-unknown-linux-gnu` |

The installation is outside the repository and used `--no-modify-path`. Commands must run with the recorded homes and `CARGO_HOME/bin` prepended to `PATH`. Because this workspace rewrites persistent symlinks, the rustup proxies are regular hard links to the same verified rustup executable and were retested in fresh command contexts. This is an environment fact, not a product distribution choice.

## Licensing consequences

This decision does not resolve the missing ThreadSmith licence, the legacy wheel's missing licence/provenance, or licences for future crates, SDKs, runtimes, models, and installers. Every dependency must later record its source, version, digest, licence, required notices, and distribution status. The legacy wheel remains non-redistributable as a product dependency until its status is established.

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Python | Rejected for production core; retained only as the isolated legacy oracle. Its interpreter and packaging path conflict with the ordinary-application and Android goals. |
| Kotlin/JVM or Kotlin Multiplatform | Rejected as the universal core. It is a strong Android surface option but would introduce a managed-runtime or native split for desktop, CLI, and services. |
| TypeScript/Node.js | Rejected as canonical core. It may suit a UI surface but weakens native Android, on-device, and standalone-library deployment. |
| C++ | Rejected. Portability is strong, but memory and ABI variability add avoidable risk to identity, authority, and replay code. |
| Go | Rejected. Standalone CLI/server deployment is strong, but shared-library and mobile embedding boundaries are less suitable for the required common core. |
| WebAssembly | Rejected as the sole core target. It may become an additional binding target, but it does not remove native filesystem, secure-storage, installer, or Android integration needs. |

## Acceptance consequences

| Field | Value |
|---|---|
| Decision | `D-009=ACCEPTED` |
| Portable core language | Rust |
| Exact Rust version | `1.97.1` |
| Rust toolchain currently available | `true` |
| F1 language decision blocked | `false` |
| F2 environment gate accepted | `true` |
| F2 implementation environment ready | `true` |
| F2 implementation started | `false` |
| F2 accepted | `false` |
| Source edition and `Cargo.lock` | Deferred to actual F2 implementation scope freeze |
| Product code created by this decision | `false` |

This decision may be reconsidered only if a documented platform constraint makes one canonical Rust core infeasible. Tool availability, developer preference, or convenience is not sufficient. Any replacement must preserve the same canonical artifacts, identities, authority boundaries, and cross-surface single-core rule.
