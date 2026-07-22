#![forbid(unsafe_code)]

use serde_json::{Number, Value};
use sha2::{Digest, Sha256};
use std::collections::BTreeMap;
use threadsmith_schema::{ArtifactKind, NativeLatticeId, SchemaError, Sha256Digest, error_code};
use unicode_normalization::UnicodeNormalization;

/// Produces the reconstructed Foundation canonical JSON byte form.
///
/// Strings and object keys are normalized to NFC, object keys are sorted,
/// whitespace is omitted, and floating-point numbers are rejected.
pub fn canonical_bytes(value: &Value) -> Result<Vec<u8>, SchemaError> {
    let normalized = normalize_value(value)?;
    serde_json::to_vec(&normalized).map_err(|error| {
        SchemaError::new(
            error_code::SCHEMA_INVALID,
            format!("canonical JSON serialization failed: {error}"),
        )
    })
}

/// Calculates SHA-256 over the canonical byte form.
pub fn canonical_sha256(value: &Value) -> Result<Sha256Digest, SchemaError> {
    let bytes = canonical_bytes(value)?;
    Ok(sha256_digest(&bytes))
}

/// Creates a typed native identity claim from an explicitly resolved preimage.
///
/// This API does not select an artifact-specific preimage, remove self-identity
/// or compiler metadata, validate an artifact, or grant authority. Those rules
/// require the missing Standard and artifact-specific APIs. An absent preimage
/// is rejected before any identity claim is created.
pub fn identity_claim_from_resolved_preimage(
    kind: ArtifactKind,
    preimage: Option<&Value>,
) -> Result<NativeLatticeId, SchemaError> {
    let preimage = preimage.ok_or_else(|| {
        SchemaError::new(
            error_code::IDENTITY_PREIMAGE_UNRESOLVED,
            format!("canonical preimage for {kind} identity is unresolved"),
        )
    })?;
    Ok(NativeLatticeId::from_canonical_digest(
        kind,
        canonical_sha256(preimage)?,
    ))
}

/// Verifies a non-authoritative native claim against a resolved preimage.
///
/// This verifies canonical bytes, digest, and kind only. It does not establish
/// that the caller selected the Standard-defined artifact preimage.
pub fn verify_preimage_claim(
    kind: ArtifactKind,
    preimage: Option<&Value>,
    claimed: &NativeLatticeId,
) -> Result<(), SchemaError> {
    let expected = identity_claim_from_resolved_preimage(kind, preimage)?;
    if claimed.kind() != kind {
        return Err(SchemaError::new(
            error_code::IDENTITY_KIND_UNSUPPORTED,
            format!(
                "claimed identity kind {} does not match expected kind {kind}",
                claimed.kind()
            ),
        ));
    }
    if &expected != claimed {
        return Err(SchemaError::new(
            error_code::IDENTITY_FORMAT_INVALID,
            format!("identity mismatch: expected {expected}, got {claimed}"),
        ));
    }
    Ok(())
}

/// Calculates SHA-256 over an exact byte sequence.
#[must_use]
pub fn sha256_digest(bytes: &[u8]) -> Sha256Digest {
    let digest = Sha256::digest(bytes);
    let mut output = [0_u8; 32];
    output.copy_from_slice(&digest);
    Sha256Digest::from_bytes(output)
}

fn normalize_value(value: &Value) -> Result<Value, SchemaError> {
    match value {
        Value::Null | Value::Bool(_) => Ok(value.clone()),
        Value::Number(number) => normalize_number(number),
        Value::String(text) => Ok(Value::String(text.nfc().collect())),
        Value::Array(values) => values
            .iter()
            .map(normalize_value)
            .collect::<Result<Vec<_>, _>>()
            .map(Value::Array),
        Value::Object(values) => {
            let mut normalized = BTreeMap::new();
            for (raw_key, raw_value) in values {
                let key: String = raw_key.nfc().collect();
                match normalized.entry(key) {
                    std::collections::btree_map::Entry::Vacant(entry) => {
                        entry.insert(normalize_value(raw_value)?);
                    }
                    std::collections::btree_map::Entry::Occupied(entry) => {
                        return Err(SchemaError::new(
                            error_code::SCHEMA_INVALID,
                            format!(
                                "duplicate canonical object key after NFC normalization: {:?}",
                                entry.key()
                            ),
                        ));
                    }
                }
            }
            Ok(Value::Object(normalized.into_iter().collect()))
        }
    }
}

fn normalize_number(number: &Number) -> Result<Value, SchemaError> {
    let text = number.as_str();
    if text.bytes().any(|byte| matches!(byte, b'.' | b'e' | b'E')) {
        return Err(SchemaError::new(
            error_code::SCHEMA_INVALID,
            "floating-point numbers are not supported in canonical values",
        ));
    }
    if text == "-0" {
        return Ok(Value::Number(Number::from(0)));
    }
    Ok(Value::Number(number.clone()))
}

#[cfg(test)]
mod tests {
    use super::*;
    use serde_json::json;

    #[test]
    fn canonical_form_normalizes_and_sorts() {
        let value = json!({"z": 1, "purpose": "Cafe\u{301} response", "a": true});
        assert_eq!(
            canonical_bytes(&value).unwrap(),
            "{\"a\":true,\"purpose\":\"Café response\",\"z\":1}".as_bytes()
        );
    }

    #[test]
    fn duplicate_keys_after_normalization_are_rejected() {
        let value: Value = serde_json::from_str("{\"Café\":1,\"Cafe\\u0301\":2}").unwrap();
        assert_eq!(
            canonical_bytes(&value).unwrap_err().code(),
            error_code::SCHEMA_INVALID
        );
    }

    #[test]
    fn floating_point_values_are_rejected() {
        assert_eq!(
            canonical_bytes(&json!(1.5)).unwrap_err().code(),
            error_code::SCHEMA_INVALID
        );
    }

    #[test]
    fn unresolved_preimages_are_rejected() {
        assert_eq!(
            identity_claim_from_resolved_preimage(ArtifactKind::Blueprint, None)
                .unwrap_err()
                .code(),
            error_code::IDENTITY_PREIMAGE_UNRESOLVED
        );
    }

    #[test]
    fn native_identity_is_derived_from_canonical_bytes() {
        let identity = identity_claim_from_resolved_preimage(
            ArtifactKind::Package,
            Some(&json!({"z": 1, "a": 2})),
        )
        .unwrap();
        assert_eq!(
            identity.to_string(),
            "lattice:package:sha256:c2985c5ba6f7d2a55e768f92490ca09388e95bc4cccb9fdf11b15f4d42f93e73"
        );
    }

    #[test]
    fn preimage_claim_verification_checks_all_failure_paths() {
        let value = json!({"a": 2, "z": 1});
        let identity =
            identity_claim_from_resolved_preimage(ArtifactKind::Package, Some(&value)).unwrap();
        verify_preimage_claim(ArtifactKind::Package, Some(&value), &identity).unwrap();
        assert_eq!(
            verify_preimage_claim(ArtifactKind::Manifest, Some(&value), &identity)
                .unwrap_err()
                .code(),
            error_code::IDENTITY_KIND_UNSUPPORTED
        );
        let wrong_digest = NativeLatticeId::from_canonical_digest(
            ArtifactKind::Package,
            Sha256Digest::from_bytes([1_u8; 32]),
        );
        assert_eq!(
            verify_preimage_claim(ArtifactKind::Package, Some(&value), &wrong_digest)
                .unwrap_err()
                .code(),
            error_code::IDENTITY_FORMAT_INVALID
        );
        assert_eq!(
            verify_preimage_claim(ArtifactKind::Package, None, &identity)
                .unwrap_err()
                .code(),
            error_code::IDENTITY_PREIMAGE_UNRESOLVED
        );
    }

    #[test]
    fn arbitrary_size_integers_match_the_recovered_oracle_domain() {
        let value: Value = serde_json::from_str(
            "{\"big\":123456789012345678901234567890123456789012345678901234567890}",
        )
        .unwrap();
        assert_eq!(
            canonical_bytes(&value).unwrap(),
            "{\"big\":123456789012345678901234567890123456789012345678901234567890}".as_bytes()
        );
        let negative_zero: Value = serde_json::from_str("-0").unwrap();
        assert_eq!(canonical_bytes(&negative_zero).unwrap(), b"0");
    }
}
