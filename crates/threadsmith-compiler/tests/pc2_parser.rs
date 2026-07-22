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
        "deferred_source_validation",
        "literal_block_string",
        "scalar_resolution",
    ] {
        assert_valid(name);
    }
}

#[test]
fn invalid_conformance_fixtures() {
    for name in [
        "duplicate_key",
        "nfc_collision",
        "forbidden_anchor",
        "forbidden_tag",
        "invalid_float_scalar",
        "folded_block_string",
        "integer_out_of_range",
        "non_string_key",
    ] {
        assert_invalid(name);
    }
}

#[test]
fn absent_and_explicit_empty_fields_remain_distinguishable() {
    assert_eq!(parse_blueprint_source(b"{}\n").unwrap(), json!({}));
    assert_eq!(
        parse_blueprint_source(b"imports: []\nunits: []\n").unwrap(),
        json!({"imports": [], "units": []})
    );
}

#[test]
fn source_validation_is_deferred_to_pc3() {
    let source =
        b"module: x\nunknown: retained\ndefaults: {policy: allow}\nunits: [{kind: store}]\n";
    assert_eq!(
        parse_blueprint_source(source).unwrap(),
        json!({
            "module": "x",
            "unknown": "retained",
            "defaults": {"policy": "allow"},
            "units": [{"kind": "store"}]
        })
    );
    assert_eq!(
        parse_blueprint_source(b"[not, a, root, mapping]\n").unwrap(),
        json!(["not", "a", "root", "mapping"])
    );
}

#[test]
fn yaml_core_scalars_are_json_shaped_and_i64_bounded() {
    let source = b"values: [null, Null, NULL, ~, true, True, FALSE, 00, -0, +17, 0o17, 0x1f, yes, 1_000, '1.0']\nempty:\n";
    assert_eq!(
        parse_blueprint_source(source).unwrap(),
        json!({
            "values": [null, null, null, null, true, true, false, 0, 0, 17, 15, 31, "yes", "1_000", "1.0"],
            "empty": null
        })
    );

    for value in [
        "9223372036854775808",
        "-9223372036854775809",
        "0x8000000000000000",
    ] {
        let source = format!("value: {value}\n");
        assert_eq!(
            parse_blueprint_source(source.as_bytes()).unwrap_err().code,
            "SOURCE_INVALID_SCALAR",
            "{value}"
        );
    }
}

#[test]
fn literal_strings_markers_and_yaml_12_directive_are_accepted() {
    let bare = b"purpose: |\n  first\n  second\n";
    let marked = b"---\npurpose: |\n  first\n  second\n...\n";
    let directed = b"%YAML 1.2 # standard version\n---\npurpose: |\n  first\n  second\n...\n";
    assert_eq!(parse_blueprint_source(bare), parse_blueprint_source(marked));
    assert_eq!(
        parse_blueprint_source(bare),
        parse_blueprint_source(directed)
    );
}

#[test]
fn explicit_string_keys_are_accepted_but_collection_keys_are_not() {
    assert_eq!(
        parse_blueprint_source(b"? explicit\n: value\n").unwrap(),
        json!({"explicit": "value"})
    );
    assert_eq!(
        parse_blueprint_source(b"? [collection]\n: value\n")
            .unwrap_err()
            .code,
        "SOURCE_NON_STRING_KEY"
    );
}

#[test]
fn yaml_core_tags_are_honored_and_custom_or_wrong_kind_tags_are_rejected() {
    assert_eq!(
        parse_blueprint_source(
            b"string: !!str 123\ninteger: !!int '0x10'\nboolean: !!bool 'TRUE'\nnothing: !!null ''\nsequence: !!seq [one]\nmapping: !!map {key: value}\n? !!str true\n: string key\n"
        )
        .unwrap(),
        json!({
            "string": "123",
            "integer": 16,
            "boolean": true,
            "nothing": null,
            "sequence": ["one"],
            "mapping": {"key": "value"},
            "true": "string key"
        })
    );

    for source in [
        b"value: !custom text\n".as_slice(),
        b"value: !!float 1.0\n".as_slice(),
        b"value: !!binary bytes\n".as_slice(),
        b"value: !!map scalar\n".as_slice(),
        b"value: !!seq {}\n".as_slice(),
    ] {
        assert!(parse_blueprint_source(source).is_err());
    }
}

#[test]
fn arrays_preserve_order_and_objects_emit_deterministically() {
    let source = b"z: last\na: first\nvalues: [third, first, second]\n";
    let value = parse_blueprint_source(source).unwrap();
    assert_eq!(value["values"], json!(["third", "first", "second"]));
    for _ in 0..3 {
        assert_eq!(parse_blueprint_source(source).unwrap(), value);
    }
    assert_eq!(
        serde_json::to_string(&value).unwrap(),
        r#"{"a":"first","values":["third","first","second"],"z":"last"}"#
    );
}

#[test]
fn accepted_line_endings_project_identically() {
    let lf = b"purpose: |\n  line one\n  line two\n";
    let crlf = b"purpose: |\r\n  line one\r\n  line two\r\n";
    let cr = b"purpose: |\r  line one\r  line two\r";
    assert_eq!(parse_blueprint_source(lf), parse_blueprint_source(crlf));
    assert_eq!(parse_blueprint_source(lf), parse_blueprint_source(cr));
}

#[test]
fn nested_duplicate_and_collision_checks_fail_closed() {
    let duplicate = b"resources: [{name: one, name: two}]\n";
    let collision = "resources: [{Café: one, Cafe\u{301}: two}]\n";
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
        b"purpose: >\n  folded\n",
        b"resources: [*missing]\n",
        b"<<: {}\n",
        b"purpose: !text tagged\n",
        b"purpose: &anchor anchored\n",
    ];
    for source in cases {
        assert_eq!(
            parse_blueprint_source(source).unwrap_err().code,
            "SOURCE_FORBIDDEN_YAML"
        );
    }
}

#[test]
fn invalid_source_and_float_categories_are_rejected() {
    assert_eq!(
        parse_blueprint_source(b"value: \xff").unwrap_err().code,
        "SOURCE_INVALID_UTF8"
    );

    for value in ["1.0", "1e3", ".inf", "-.Inf", ".NAN"] {
        let source = format!("value: {value}\n");
        assert_eq!(
            parse_blueprint_source(source.as_bytes()).unwrap_err().code,
            "SOURCE_INVALID_SCALAR",
            "{value}"
        );
    }
}

#[test]
fn forbidden_yaml_has_global_precedence_over_scalar_validation() {
    let source = b"version: 1.0\npurpose: &forbidden later\n";
    let diagnostic = parse_blueprint_source(source).unwrap_err();
    assert_eq!(diagnostic.code, "SOURCE_FORBIDDEN_YAML");
    assert_eq!(diagnostic.path, "/purpose");
    assert_eq!((diagnostic.line, diagnostic.column), (Some(2), Some(10)));
}

#[test]
fn multiple_documents_wrong_directives_and_forbidden_characters_fail_closed() {
    let forbidden_yaml: &[&[u8]] = &[
        b"value: one\n---\nvalue: two\n",
        b"%YAML 1.1\n---\nvalue: one\n",
        b"%TAG !e! tag:example.com,2026:\n---\nvalue: one\n",
        b"%YAML 1.2\n%YAML 1.2\n---\nvalue: one\n",
    ];
    for source in forbidden_yaml {
        assert_eq!(
            parse_blueprint_source(source).unwrap_err().code,
            "SOURCE_FORBIDDEN_YAML"
        );
    }

    for source in [
        b"\xef\xbb\xbfvalue: one\n".as_slice(),
        b"value: one\0\n".as_slice(),
    ] {
        assert_eq!(
            parse_blueprint_source(source).unwrap_err().code,
            "SOURCE_INVALID_UTF8"
        );
    }
}
