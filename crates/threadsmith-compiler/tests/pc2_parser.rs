use serde_json::{Value, json};
use std::fs;
use std::path::{Path, PathBuf};
use threadsmith_compiler::parse_blueprint_source;

fn repository_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("../..")
}

fn read(relative: &str) -> Vec<u8> {
    fs::read(repository_root().join(relative)).unwrap()
}

fn expected_json(relative: &str) -> Value {
    serde_json::from_slice(&read(relative)).unwrap()
}

fn assert_valid(name: &str) {
    let base = format!("conformance/pc2/parser/valid/{name}");
    let actual = parse_blueprint_source(&read(&format!("{base}.yaml"))).unwrap();
    assert_eq!(actual, expected_json(&format!("{base}.expected.json")));
}

fn assert_invalid(name: &str) {
    let base = format!("conformance/pc2/parser/invalid/{name}");
    let actual = parse_blueprint_source(&read(&format!("{base}.yaml"))).unwrap_err();
    let expected = expected_json(&format!("{base}.expected.json"));
    assert_eq!(serde_json::to_value(actual).unwrap(), expected);
}

#[test]
fn valid_conformance_fixtures() {
    for name in [
        "minimal_blueprint",
        "complete_root_keys",
        "empty_optional_lists",
        "unicode_nfc",
    ] {
        assert_valid(name);
    }
}

#[test]
fn invalid_conformance_fixtures() {
    for name in [
        "unknown_root_key",
        "missing_required_key",
        "duplicate_key",
        "nfc_collision",
        "forbidden_anchor",
        "forbidden_tag",
        "invalid_float_scalar",
        "extended_unit_kind",
        "illegal_defaults",
    ] {
        assert_invalid(name);
    }
}

#[test]
fn supported_scalars_and_array_order_are_deterministic() {
    let source = br#"
profile: lattice-core-0.1
module: scalar_fixture
version: "1.0.0"
purpose: scalar projection
imports: [yes, true, false, null, 0, -7, 18446744073709551615, "1.0"]
resources: [{z: last, a: first}]
"#;
    let expected = json!({
        "profile": "lattice-core-0.1",
        "module": "scalar_fixture",
        "version": "1.0.0",
        "purpose": "scalar projection",
        "imports": ["yes", true, false, null, 0, -7, 18446744073709551615_u64, "1.0"],
        "resources": [{"a": "first", "z": "last"}],
        "contracts": [],
        "units": [],
        "links": [],
        "policies": [],
        "scenarios": []
    });
    for _ in 0..3 {
        assert_eq!(parse_blueprint_source(source).unwrap(), expected);
    }
}

#[test]
fn accepted_yaml_forms_project_identically() {
    let lf = b"profile: lattice-core-0.1\nmodule: forms\nversion: '1.0.0'\npurpose: comments are discarded # comment\nunits: []\n";
    let crlf = b"profile: lattice-core-0.1\r\nmodule: forms\r\nversion: '1.0.0'\r\npurpose: comments are discarded # comment\r\nunits: []\r\n";
    assert_eq!(parse_blueprint_source(lf), parse_blueprint_source(crlf));
}

#[test]
fn nested_duplicate_and_collision_checks_fail_closed() {
    let duplicate = b"profile: lattice-core-0.1\nmodule: nested\nversion: x\npurpose: x\nresources: [{name: one, name: two}]\n";
    let collision = "profile: lattice-core-0.1\nmodule: nested\nversion: x\npurpose: x\nresources: [{Café: one, Cafe\u{301}: two}]\n";
    assert_eq!(
        parse_blueprint_source(duplicate).unwrap_err().code,
        "SOURCE_DUPLICATE_KEY"
    );
    assert_eq!(
        parse_blueprint_source(collision.as_bytes())
            .unwrap_err()
            .code,
        "SOURCE_NFC_COLLISION"
    );
}

#[test]
fn forbidden_yaml_surface_is_rejected() {
    let cases: &[&[u8]] = &[
        b"---\nprofile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n...\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: |\n  block\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\nresources: [*missing]\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n? resources\n: []\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n? [resources]\n: []\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n<<: {}\n",
    ];
    for source in cases {
        assert_eq!(
            parse_blueprint_source(source).unwrap_err().code,
            "SOURCE_FORBIDDEN_YAML"
        );
    }
}

#[test]
fn invalid_source_and_scalar_categories_are_rejected() {
    let invalid_utf8 = b"profile: \xff";
    assert_eq!(
        parse_blueprint_source(invalid_utf8).unwrap_err().code,
        "SOURCE_INVALID_UTF8"
    );

    for version in ["01", "+1", "0x10", "0o10", "1_000", "1e3", ".inf", "-0"] {
        let source =
            format!("profile: lattice-core-0.1\nmodule: x\nversion: {version}\npurpose: x\n");
        assert_eq!(
            parse_blueprint_source(source.as_bytes()).unwrap_err().code,
            "SOURCE_INVALID_SCALAR",
            "{version}"
        );
    }

    let out_of_range_key = b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\nresources: [{18446744073709551616: value}]\n";
    assert_eq!(
        parse_blueprint_source(out_of_range_key).unwrap_err().code,
        "SOURCE_INVALID_SCALAR"
    );
}

#[test]
fn parser_performs_no_deeper_compiler_validation() {
    let source = b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\nunits: [{kind: program, unresolved: anything}]\nscenarios: []\n";
    assert!(parse_blueprint_source(source).is_ok());
}

#[test]
fn forbidden_yaml_has_global_precedence_over_scalar_validation() {
    let source = b"profile: lattice-core-0.1\nmodule: x\nversion: 1.0\npurpose: &forbidden later\n";
    let diagnostic = parse_blueprint_source(source).unwrap_err();
    assert_eq!(diagnostic.code, "SOURCE_FORBIDDEN_YAML");
    assert_eq!(diagnostic.path, "/purpose");
    assert_eq!((diagnostic.line, diagnostic.column), (Some(4), Some(10)));
}

#[test]
fn root_envelope_validation_is_shallow_and_deterministic() {
    let cases: &[(&[u8], &str, &str)] = &[
        (b"[]\n", "SOURCE_ROOT_TYPE", ""),
        (
            b"profile: wrong\nmodule: x\nversion: x\npurpose: x\n",
            "SOURCE_INVALID_ROOT_VALUE",
            "/profile",
        ),
        (
            b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\nimports: null\n",
            "SOURCE_INVALID_ROOT_VALUE",
            "/imports",
        ),
    ];
    for (source, code, path) in cases {
        let diagnostic = parse_blueprint_source(source).unwrap_err();
        assert_eq!(diagnostic.code, *code);
        assert_eq!(diagnostic.path, *path);
    }
}

#[test]
fn directives_multiple_documents_and_forbidden_characters_fail_closed() {
    let forbidden_yaml: &[&[u8]] = &[
        b"%YAML 1.2\n---\nprofile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n",
        b"profile: lattice-core-0.1\nmodule: x\nversion: x\npurpose: x\n---\nprofile: lattice-core-0.1\nmodule: y\nversion: y\npurpose: y\n",
    ];
    for source in forbidden_yaml {
        assert_eq!(
            parse_blueprint_source(source).unwrap_err().code,
            "SOURCE_FORBIDDEN_YAML"
        );
    }

    for source in [
        b"\xef\xbb\xbfprofile: lattice-core-0.1\n".as_slice(),
        b"profile: lattice-core-0.1\rmodule: x\n".as_slice(),
        b"profile: lattice-core-0.1\0\n".as_slice(),
    ] {
        assert_eq!(
            parse_blueprint_source(source).unwrap_err().code,
            "SOURCE_INVALID_UTF8"
        );
    }
}
