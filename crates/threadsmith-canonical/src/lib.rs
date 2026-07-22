#![forbid(unsafe_code)]

use serde_json::{Number, Value};
use sha2::{Digest, Sha256};
use threadsmith_schema::{ArtifactKind, NativeLatticeId, SchemaError, Sha256Digest, error_code};
use unicode_normalization::UnicodeNormalization;

/// Produces the reconstructed Foundation canonical JSON byte form.
///
/// Strings and object keys are normalized to NFC, object keys are sorted,
/// whitespace is omitted, and floating-point numbers are rejected.
pub fn canonical_bytes(value: &Value) -> Result<Vec<u8>, SchemaError> {
    let mut output = Vec::new();
    write_canonical_value(value, &mut output)?;
    Ok(output)
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

fn write_canonical_value(value: &Value, output: &mut Vec<u8>) -> Result<(), SchemaError> {
    match value {
        Value::Null => output.extend_from_slice(b"null"),
        Value::Bool(true) => output.extend_from_slice(b"true"),
        Value::Bool(false) => output.extend_from_slice(b"false"),
        Value::Number(number) => write_canonical_number(number, output)?,
        Value::String(text) => write_canonical_string(text, output),
        Value::Array(values) => {
            output.push(b'[');
            for (index, value) in values.iter().enumerate() {
                if index != 0 {
                    output.push(b',');
                }
                write_canonical_value(value, output)?;
            }
            output.push(b']');
        }
        Value::Object(values) => {
            let mut normalized = Vec::with_capacity(values.len());
            for (raw_key, raw_value) in values {
                let key: String = raw_key.nfc().collect();
                normalized.push((key, raw_value));
            }
            normalized.sort_by(|left, right| left.0.as_bytes().cmp(right.0.as_bytes()));
            for pair in normalized.windows(2) {
                if pair[0].0 == pair[1].0 {
                    return Err(SchemaError::new(
                        error_code::SCHEMA_INVALID,
                        format!(
                            "duplicate canonical object key after NFC normalization: {:?}",
                            pair[0].0
                        ),
                    ));
                }
            }

            output.push(b'{');
            for (index, (key, value)) in normalized.into_iter().enumerate() {
                if index != 0 {
                    output.push(b',');
                }
                write_canonical_string(&key, output);
                output.push(b':');
                write_canonical_value(value, output)?;
            }
            output.push(b'}');
        }
    }
    Ok(())
}

fn write_canonical_number(number: &Number, output: &mut Vec<u8>) -> Result<(), SchemaError> {
    let text = number.as_str();
    if text.bytes().any(|byte| matches!(byte, b'.' | b'e' | b'E')) {
        return Err(SchemaError::new(
            error_code::SCHEMA_INVALID,
            "floating-point numbers are not supported in canonical values",
        ));
    }
    if text == "-0" {
        output.push(b'0');
    } else {
        output.extend_from_slice(text.as_bytes());
    }
    Ok(())
}

fn write_canonical_string(text: &str, output: &mut Vec<u8>) {
    const HEX: &[u8; 16] = b"0123456789abcdef";

    output.push(b'"');
    for character in text.nfc() {
        match character {
            '"' => output.extend_from_slice(br#"\""#),
            '\\' => output.extend_from_slice(br#"\\"#),
            '\u{0008}' => output.extend_from_slice(br"\b"),
            '\t' => output.extend_from_slice(br"\t"),
            '\n' => output.extend_from_slice(br"\n"),
            '\u{000c}' => output.extend_from_slice(br"\f"),
            '\r' => output.extend_from_slice(br"\r"),
            character if character <= '\u{001f}' => {
                let byte = character as u8;
                output.extend_from_slice(br"\u00");
                output.push(HEX[usize::from(byte >> 4)]);
                output.push(HEX[usize::from(byte & 0x0f)]);
            }
            character => {
                let mut encoded = [0_u8; 4];
                output.extend_from_slice(character.encode_utf8(&mut encoded).as_bytes());
            }
        }
    }
    output.push(b'"');
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
