use std::path::PathBuf;
use threadsmith_compiler::{ExistingLockfileInput, resolve_diagnostic_codes, resolve_source};

#[path = "support/pc7_fixture_interpreter.rs"]
mod pc7_fixture_interpreter;

fn authority_inputs() -> pc7_fixture_interpreter::PC7AuthorityInputsV1 {
    let authority_root = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("../..")
        .canonicalize()
        .expect("repository authority root");
    let registry_path = authority_root.join("docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json");
    let registry_bytes = std::fs::read(&registry_path).expect("actual immutable registry bytes");
    pc7_fixture_interpreter::PC7AuthorityInputsV1 {
        authority_root,
        registry_path,
        registry_bytes,
    }
}

#[test]
fn diagnostic_vocabulary_is_exact_and_unique() {
    let codes = resolve_diagnostic_codes();
    assert_eq!(codes.len(), 21);
    let unique = codes
        .iter()
        .copied()
        .collect::<std::collections::BTreeSet<_>>();
    assert_eq!(unique.len(), codes.len());
    assert_eq!(codes[0], "RESOLVE_DUPLICATE_VERSION");
    assert_eq!(codes[20], "RESOLVE_IMPORT_CYCLE");
}

#[test]
fn public_boundary_requires_opaque_pc6_source_and_explicit_lock_input() {
    let boundary: fn(
        threadsmith_compiler::ScannedSource,
        ExistingLockfileInput,
    ) -> Result<
        threadsmith_compiler::ResolvedSource,
        threadsmith_compiler::ResolveDiagnostic,
    > = resolve_source;
    let absent = ExistingLockfileInput::absent();
    assert!(absent.bytes().is_none());
    let zero = ExistingLockfileInput::from_bytes(Vec::<u8>::new());
    assert_eq!(zero.bytes(), Some([].as_slice()));
    let _ = boundary;
}

#[test]
fn lock_package_scalar_grammar_uses_field_then_index_order() {
    pc7_fixture_interpreter::assert_lock_package_scalar_grammar_order();
}

#[test]
fn lock_top_level_type_stage_precedes_scalar_stage() {
    pc7_fixture_interpreter::assert_lock_top_level_type_stage_precedes_scalar_stage();
}

#[test]
fn lock_diagnostic_paths_encode_pointer_tokens() {
    pc7_fixture_interpreter::assert_lock_paths_encode_pointer_tokens();
}

#[test]
fn lock_negative_zero_rejects_at_public_source_boundary() {
    pc7_fixture_interpreter::assert_lock_negative_zero_rejected_at_source_intake();
}

#[test]
fn all_current_fixtures_execute_through_the_public_pc7_boundary() {
    let summary = pc7_fixture_interpreter::execute_all(&authority_inputs())
        .expect("authority preflight and all current fixture dispatch");
    assert_eq!(summary.defined, 118);
    assert_eq!(summary.generated, 118);
    assert_eq!(summary.executed, 118);
    assert_eq!(summary.future_vectors, 4);
}

#[test]
fn raw_unpaired_surrogate_registry_rejects_before_dispatch() {
    let mut inputs = authority_inputs();
    let source = br#"  "format": "threadsmith-pc7-authority-registry-1",
"#;
    let replacement = br#"  "format": "\ud800",
"#;
    assert_eq!(
        inputs
            .registry_bytes
            .windows(source.len())
            .filter(|window| *window == source)
            .count(),
        1
    );
    let offset = inputs
        .registry_bytes
        .windows(source.len())
        .position(|window| window == source)
        .unwrap();
    inputs
        .registry_bytes
        .splice(offset..offset + source.len(), replacement.iter().copied());
    assert_eq!(inputs.registry_bytes.len(), 2011);
    let rejection = pc7_fixture_interpreter::execute_all(&inputs)
        .expect_err("unpaired surrogate must fail raw-byte preflight");
    assert_eq!(
        rejection,
        pc7_fixture_interpreter::AuthorityPreflightRejection {
            code: "PC7_AUTHORITY_PREFLIGHT_REJECTED",
            gate: "registry_strict_json_parse",
            path: "authority#/registry".to_owned(),
            reason: "UTF-8/BOM/JSON/duplicate failure",
            fixture_dispatch_started: false,
        }
    );
}

#[test]
fn registry_unbounded_nonnegative_byte_count_reaches_document_gate() {
    let mut inputs = authority_inputs();
    let source = br#""bytes": 66657"#;
    let replacement =
        br#""bytes": 100000000000000000000000000000000000000000000000000000000000000000000000000000000"#;
    assert_eq!(
        inputs
            .registry_bytes
            .windows(source.len())
            .filter(|window| *window == source)
            .count(),
        1
    );
    let offset = inputs
        .registry_bytes
        .windows(source.len())
        .position(|window| window == source)
        .unwrap();
    inputs
        .registry_bytes
        .splice(offset..offset + source.len(), replacement.iter().copied());
    let rejection = pc7_fixture_interpreter::execute_all(&inputs)
        .expect_err("wrong admitted byte count must reject at document bytes");
    assert_eq!(
        rejection,
        pc7_fixture_interpreter::AuthorityPreflightRejection {
            code: "PC7_AUTHORITY_PREFLIGHT_REJECTED",
            gate: "authority_document_bytes",
            path: "authority#/lattice_standard".to_owned(),
            reason: "authority document byte count mismatch",
            fixture_dispatch_started: false,
        }
    );
}

#[test]
fn plan_registry_binding_mismatch_rejects_before_dispatch() {
    let inputs = authority_inputs();
    let mut plan = std::fs::read(
        inputs
            .authority_root
            .join("conformance/pc7/resolve/executable_fixture_plan.json"),
    )
    .expect("checked-in plan bytes");
    let source = br#""registry_bytes":2041"#;
    let replacement = br#""registry_bytes":2042"#;
    assert_eq!(
        plan.windows(source.len())
            .filter(|window| *window == source)
            .count(),
        1
    );
    let offset = plan
        .windows(source.len())
        .position(|window| window == source)
        .unwrap();
    plan.splice(offset..offset + source.len(), replacement.iter().copied());
    let rejection = pc7_fixture_interpreter::execute_plan_bytes(&inputs, &plan)
        .expect_err("plan registry binding mismatch must fail before dispatch");
    assert_eq!(rejection.code, "PC7_AUTHORITY_PREFLIGHT_REJECTED");
    assert_eq!(rejection.gate, "plan_registry_binding");
    assert_eq!(rejection.path, "authority#/registry");
    assert_eq!(rejection.reason, "plan registry binding mismatch");
    assert!(!rejection.fixture_dispatch_started);
}

#[test]
fn changed_resolve_authority_rejects_before_dispatch() {
    let source = authority_inputs();
    let disposable = std::env::temp_dir().join(format!(
        "threadsmith-pc7-authority-mutation-{}",
        std::process::id()
    ));
    if disposable.exists() {
        std::fs::remove_dir_all(&disposable).expect("remove stale exact disposable path");
    }
    for relative in [
        "docs/standard/LATTICE_STANDARD_0.3.md",
        "docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md",
        "docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md",
        "docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md",
        "docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md",
        "docs/pc7/PC7_SCOPE_RECONCILIATION.md",
        "docs/pc7/PC7_SEMANTIC_FREEZE.md",
        "docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json",
        "docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json",
    ] {
        let target = disposable.join(relative);
        std::fs::create_dir_all(target.parent().unwrap()).expect("disposable parent");
        std::fs::copy(source.authority_root.join(relative), target).expect("copy authority input");
    }
    let resolve_path =
        disposable.join("docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md");
    let text = std::fs::read_to_string(&resolve_path).expect("Resolve authority UTF-8");
    let from = "The first failing gate returns its primary diagnostic";
    let to = "The last failing gate returns its primary diagnostic";
    assert!(text.matches(from).count() >= 1);
    std::fs::write(&resolve_path, text.replacen(from, to, 1)).expect("disposable mutation");
    let inputs = pc7_fixture_interpreter::PC7AuthorityInputsV1 {
        authority_root: disposable.clone(),
        registry_path: disposable.join("docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json"),
        registry_bytes: source.registry_bytes,
    };
    let rejection = pc7_fixture_interpreter::execute_all(&inputs)
        .expect_err("changed authority bytes must fail before dispatch");
    assert_eq!(rejection.code, "PC7_AUTHORITY_PREFLIGHT_REJECTED");
    assert_eq!(rejection.gate, "authority_document_bytes");
    assert_eq!(rejection.path, "authority#/resolve_semantics_erratum");
    assert!(!rejection.fixture_dispatch_started);
    std::fs::remove_dir_all(&disposable).expect("remove exact disposable path");
}
