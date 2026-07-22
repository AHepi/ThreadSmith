use serde_json::Value;
use std::collections::BTreeMap;
use threadsmith_canonical::{canonical_bytes, canonical_sha256};

const FIXTURES: &str = include_str!("../../../conformance/pc5/digest/fixture_manifest.json");

fn fixture_manifest() -> Value {
    serde_json::from_str(FIXTURES).unwrap()
}

fn decode_hex(text: &str) -> Vec<u8> {
    assert_eq!(text.len() % 2, 0, "hex value must contain whole bytes");
    (0..text.len())
        .step_by(2)
        .map(|index| u8::from_str_radix(&text[index..index + 2], 16).unwrap())
        .collect()
}

#[test]
fn canonical_json_erratum_vectors_match_exact_bytes_and_hashes() {
    let manifest = fixture_manifest();
    let vectors = manifest["canonical_json_vectors"].as_array().unwrap();
    assert_eq!(vectors.len(), 8);

    for vector in vectors {
        let id = vector["id"].as_str().unwrap();
        let expected = decode_hex(vector["canonical_utf8_hex"].as_str().unwrap());
        let actual =
            canonical_bytes(&vector["input"]).unwrap_or_else(|error| panic!("{id}: {error}"));
        assert_eq!(actual, expected, "canonical bytes for {id}");
        assert_eq!(
            canonical_sha256(&vector["input"]).unwrap().to_string(),
            vector["sha256"].as_str().unwrap(),
            "SHA-256 for {id}"
        );
        assert!(!actual.starts_with(&[0xef, 0xbb, 0xbf]), "BOM for {id}");
        assert!(!actual.ends_with(b"\n"), "trailing newline for {id}");
    }
}

#[test]
fn canonical_profile_participation_matches_the_frozen_unreachable_vector() {
    let manifest = fixture_manifest();
    let group = &manifest["source_equivalence_groups"][0];
    let profile = &manifest["profile_boundary"];
    let mut value = group["expected_defaulted_value"].clone();

    assert_eq!(
        canonical_bytes(&value).unwrap(),
        decode_hex(group["canonical_utf8_hex"].as_str().unwrap())
    );
    assert_eq!(
        canonical_sha256(&value).unwrap().to_string(),
        group["sha256"].as_str().unwrap()
    );
    assert_eq!(
        canonical_sha256(&value).unwrap().to_string(),
        profile["base_profile"]["sha256"].as_str().unwrap()
    );
    value["profile"] = profile["alternate_profile_canonical_preimage"]["value"].clone();
    assert_eq!(
        canonical_sha256(&value).unwrap().to_string(),
        profile["alternate_profile_canonical_preimage"]["sha256"]
            .as_str()
            .unwrap()
    );
}

#[test]
fn canonical_core_preserves_array_order_and_foundation_integer_domain() {
    let first = serde_json::json!([{"unit": "alpha"}, {"unit": "beta"}]);
    let second = serde_json::json!([{"unit": "beta"}, {"unit": "alpha"}]);
    assert_ne!(
        canonical_bytes(&first).unwrap(),
        canonical_bytes(&second).unwrap()
    );

    let arbitrary: Value = serde_json::from_str(
        "{\"big\":123456789012345678901234567890123456789012345678901234567890}",
    )
    .unwrap();
    assert_eq!(
        canonical_bytes(&arbitrary).unwrap(),
        b"{\"big\":123456789012345678901234567890123456789012345678901234567890}"
    );

    let ordered: BTreeMap<_, _> = [
        ("empty", serde_json::json!({})),
        ("values", serde_json::json!([true, false, null])),
    ]
    .into_iter()
    .collect();
    assert_eq!(
        canonical_bytes(&serde_json::to_value(ordered).unwrap()).unwrap(),
        br#"{"empty":{},"values":[true,false,null]}"#
    );
}
