use serde_json::{Value, json};
use std::fs;
use std::path::{Path, PathBuf};
use threadsmith_compiler::{parse_blueprint_source, validate_blueprint_source};

fn repository_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("../..")
}

fn fixture_manifest() -> Value {
    serde_json::from_slice(
        &fs::read(repository_root().join("conformance/pc3/source_validate/fixture_manifest.json"))
            .unwrap(),
    )
    .unwrap()
}

fn minimal_root() -> Value {
    json!({
        "lattice": "0.3",
        "profile": "lattice-core-0.1",
        "module": "tiny_writer",
        "version": "1.0.0",
        "purpose": "Minimal",
        "units": []
    })
}

#[test]
fn frozen_conformance_fixtures_match_public_pc3_api() {
    let manifest = fixture_manifest();
    let cases = manifest["cases"].as_array().unwrap();
    assert_eq!(cases.len(), 19);

    for case in cases {
        let id = case["id"].as_str().unwrap();
        let input = case["input"].clone();
        let expected = &case["expected"];
        for _ in 0..3 {
            let result = validate_blueprint_source(input.clone());
            if expected["result"] == "valid_unchanged" {
                let validated = result.unwrap_or_else(|error| panic!("{id}: {error:?}"));
                assert_eq!(validated.as_value(), &input, "{id}");
                assert_eq!(validated.into_value(), input, "{id}");
            } else {
                let error = result.expect_err(id);
                assert_eq!(error.code, expected["code"].as_str().unwrap(), "{id}");
                assert_eq!(error.path, expected["path"].as_str().unwrap(), "{id}");
                assert_eq!((error.line, error.column), (None, None), "{id}");
            }
        }
    }
}

#[test]
fn module_names_follow_only_the_frozen_local_name_grammar() {
    for module in ["a", "a0", "alpha_beta", "a0_b1_c2"] {
        let mut value = minimal_root();
        value["module"] = json!(module);
        assert!(validate_blueprint_source(value).is_ok(), "{module}");
    }

    for module in ["", "A", "a-b", "a__b", "_a", "a_", "éclair"] {
        let mut value = minimal_root();
        value["module"] = json!(module);
        let error = validate_blueprint_source(value).unwrap_err();
        assert_eq!(error.code, "SOURCE_INVALID_ROOT_VALUE", "{module}");
        assert_eq!(error.path, "/module", "{module}");
    }
}

#[test]
fn versions_follow_only_the_frozen_three_component_form() {
    for version in ["0.0.0", "1.0.0", "01.002.0003", "999.999.999"] {
        let mut value = minimal_root();
        value["version"] = json!(version);
        assert!(validate_blueprint_source(value).is_ok(), "{version}");
    }

    for version in ["", "1", "1.0", "1.0.0.0", "1.0.0-beta", "+1.0.0", "١.٠.٠"] {
        let mut value = minimal_root();
        value["version"] = json!(version);
        let error = validate_blueprint_source(value).unwrap_err();
        assert_eq!(error.code, "SOURCE_INVALID_ROOT_VALUE", "{version}");
        assert_eq!(error.path, "/version", "{version}");
    }
}

#[test]
fn diagnostic_precedence_is_independent_of_object_insertion_order() {
    let cases = [
        (
            json!({"zeta": 1, "alpha": 2}),
            ("SOURCE_UNKNOWN_KEY", "/alpha"),
        ),
        (
            json!({"lattice": 3, "profile": 4, "units": {}}),
            ("SOURCE_REQUIRED_KEY_MISSING", "/module"),
        ),
        (
            json!({
                "lattice": 3,
                "profile": 4,
                "module": "Bad",
                "version": "bad",
                "purpose": null,
                "units": {}
            }),
            ("SOURCE_INVALID_ROOT_VALUE", "/lattice"),
        ),
    ];

    for (value, (code, path)) in cases {
        let first = validate_blueprint_source(value.clone()).unwrap_err();
        assert_eq!((first.code, first.path.as_str()), (code, path));
        for _ in 0..3 {
            assert_eq!(validate_blueprint_source(value.clone()).unwrap_err(), first);
        }
    }
}

#[test]
fn every_required_and_categorized_root_field_is_enforced() {
    for key in [
        "lattice", "profile", "module", "version", "purpose", "units",
    ] {
        let mut value = minimal_root();
        value.as_object_mut().unwrap().remove(key);
        let error = validate_blueprint_source(value).unwrap_err();
        assert_eq!(error.code, "SOURCE_REQUIRED_KEY_MISSING", "{key}");
        assert_eq!(error.path, format!("/{key}"), "{key}");
    }

    for key in ["lattice", "profile", "module", "version", "purpose"] {
        let mut value = minimal_root();
        value[key] = Value::Null;
        let error = validate_blueprint_source(value).unwrap_err();
        assert_eq!(error.code, "SOURCE_INVALID_ROOT_VALUE", "{key}");
        assert_eq!(error.path, format!("/{key}"), "{key}");
    }

    for key in [
        "imports",
        "inputs",
        "contracts",
        "resources",
        "units",
        "links",
        "policies",
        "exports",
        "scenarios",
    ] {
        let mut value = minimal_root();
        value[key] = json!({});
        let error = validate_blueprint_source(value).unwrap_err();
        assert_eq!(error.code, "SOURCE_INVALID_ROOT_VALUE", "{key}");
        assert_eq!(error.path, format!("/{key}"), "{key}");
    }
}

#[test]
fn pc2_to_pc3_preserves_absence_explicit_empty_values_and_array_order() {
    let source = b"lattice: '0.3'\nprofile: lattice-core-0.1\nmodule: preserved\nversion: '1.0.0'\npurpose: ''\nunits: [third, first, second]\nlinks: []\n";
    let parsed = parse_blueprint_source(source).unwrap();
    assert!(!parsed.as_object().unwrap().contains_key("imports"));
    assert_eq!(parsed["links"], json!([]));
    assert_eq!(parsed["units"], json!(["third", "first", "second"]));

    let validated = validate_blueprint_source(parsed.clone()).unwrap();
    assert_eq!(validated.as_value(), &parsed);
    assert!(
        !validated
            .as_value()
            .as_object()
            .unwrap()
            .contains_key("imports")
    );
    assert_eq!(validated.as_value()["links"], json!([]));
    assert_eq!(
        validated.as_value()["units"],
        json!(["third", "first", "second"])
    );
}

#[test]
fn declaration_elements_are_opaque_and_receive_no_defaults() {
    let mut value = minimal_root();
    value["units"] = json!([
        7,
        {"unit": "Bad-Name", "kind": "store", "missing_semantics": true}
    ]);
    value["contracts"] = json!([null]);

    let validated = validate_blueprint_source(value.clone()).unwrap();
    assert_eq!(validated.into_value(), value);
}
