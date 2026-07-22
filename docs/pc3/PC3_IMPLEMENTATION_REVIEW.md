# PC3 Source-Validation Implementation Read-Only Review

Review date: 2026-07-22.

Review boundary: the public PC3 API in `threadsmith-compiler`, its focused integration test, all 19 frozen fixtures, implementation evidence, and additive durable-state entries. The review was performed as a separate read-only adversarial pass in the primary workspace; no independent agent context was available.

## Review criteria

- the public result cannot be constructed without the frozen root checks;
- validation preserves the complete PC2 value and inserts no defaults;
- declaration elements remain opaque;
- diagnostic codes, paths, and precedence match the freeze;
- no later-phase code, error, identity, artifact, or authority enters PC3;
- tests use the public PC2-to-PC3 path and cannot pass by bypassing production code; and
- accepted Foundation, PC1, PC2, Standard, dependency, and authority boundaries remain unchanged.

## Findings

| Severity | Finding | Resolution |
|---|---|---|
| P0 | None. | — |
| P1 | The initial focused suite exercised representative missing/type failures but did not independently remove every required key or mistype every root collection. A future omission from the required-key constant or collection match could therefore evade focused detection. | Repaired in cycle 1 with a table-driven public-API test covering all six required fields, all five scalar root fields, and all nine collection fields. Focused and full qualification pass after repair. |
| P2 | No new implementation finding. The semantic freeze already records that exact later-phase ownership of declaration-name uniqueness and Core unit-kind rejection remains unresolved. | Remains outside PC3; no corresponding code or diagnostic appears in the implementation. |
| P3 | None. | — |

## Closure review

The fresh post-repair read-only pass confirmed:

- `ValidatedSource.value` is private and the only constructor path is `validate_blueprint_source`;
- the implementation owns exactly `SOURCE_ROOT_TYPE`, `SOURCE_UNKNOWN_KEY`, `SOURCE_REQUIRED_KEY_MISSING`, and `SOURCE_INVALID_ROOT_VALUE` for PC3;
- every frozen allowed/required key and value category is exercised through the public API;
- all 19 fixture cases use the production validator, with deterministic replay and exact unchanged-value checks;
- later-invalid declaration content succeeds only as explicitly deferred, non-authoritative data;
- no dependency, Cargo, Foundation, PC1, PC2, Standard, ADR, identity, Manifest, Binding, or runtime change exists; and
- formatting, static checks, Clippy, 39 tests, metadata, JSON integrity, and diff checks pass locked and offline.

There are no open P0 or P1 findings. PC3 implementation is accepted within the frozen `Source validate -> Valid root shape` boundary. This acceptance does not authorize PC4 or any later compiler/runtime phase.
