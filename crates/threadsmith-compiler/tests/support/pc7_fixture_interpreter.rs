use serde::Deserialize;
use serde_json::{Map, Value};
use std::cmp::Ordering;
use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::path::PathBuf;
use threadsmith_canonical::{canonical_bytes, sha256_digest};
use threadsmith_compiler::{
    ExistingLockfileInput, ResolvedSource, ScannedPackage, ScannedSource, SnapshotEntry,
    SnapshotName, SnapshotNode, acquire_project_snapshot, apply_blueprint_defaults, digest_source,
    parse_blueprint_source, resolve_source, scan_packages, validate_blueprint_source,
};
use unicode_normalization::UnicodeNormalization;

const PLAN_BYTES: &[u8] =
    include_bytes!("../../../../conformance/pc7/resolve/executable_fixture_plan.json");
const MANIFEST_BYTES: &[u8] =
    include_bytes!("../../../../docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json");
const MANIFEST_SHA256: &str = "da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c";
const REGISTRY_RELATIVE_PATH: &str = "docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json";
const REGISTRY_FORMAT: &str = "threadsmith-pc7-authority-registry-1";
const BASELINE_COMMIT: &str = "ded743ea3577ffc2b955565dee9159287ec98e05";
const BASELINE_TREE: &str = "e26180101c53c5cf44e4f270a9e868a4582be392";
const AUTHORITY_DOCUMENTS: [(&str, &str); 8] = [
    ("lattice_standard", "docs/standard/LATTICE_STANDARD_0.3.md"),
    (
        "default_semantics_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md",
    ),
    (
        "canonical_json_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md",
    ),
    (
        "package_scan_semantics_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md",
    ),
    (
        "resolve_semantics_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md",
    ),
    (
        "pc7_scope_reconciliation",
        "docs/pc7/PC7_SCOPE_RECONCILIATION.md",
    ),
    ("pc7_semantic_freeze", "docs/pc7/PC7_SEMANTIC_FREEZE.md"),
    (
        "pc7_specified_conformance_manifest",
        "docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json",
    ),
];

#[derive(Clone, Debug)]
pub struct PC7AuthorityInputsV1 {
    pub authority_root: PathBuf,
    pub registry_path: PathBuf,
    pub registry_bytes: Vec<u8>,
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct AuthorityPreflightRejection {
    pub code: &'static str,
    pub gate: &'static str,
    pub path: String,
    pub reason: &'static str,
    pub fixture_dispatch_started: bool,
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ExecutionSummary {
    pub defined: usize,
    pub generated: usize,
    pub executed: usize,
    pub future_vectors: usize,
}

fn reject(
    gate: &'static str,
    path: impl Into<String>,
    reason: &'static str,
) -> AuthorityPreflightRejection {
    AuthorityPreflightRejection {
        code: "PC7_AUTHORITY_PREFLIGHT_REJECTED",
        gate,
        path: path.into(),
        reason,
        fixture_dispatch_started: false,
    }
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct Plan {
    authority: PlanAuthority,
    cases: Vec<Case>,
    fixture_plan_version: String,
    future_vector_ids: Vec<String>,
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct PlanAuthority {
    manifest_path: String,
    manifest_sha256: String,
    registry_bytes: usize,
    registry_sha256: String,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "class", rename_all = "snake_case", deny_unknown_fields)]
enum Case {
    Diagnostic {
        expected: Value,
        fixture_id: String,
        input_ref: String,
    },
    Success {
        expected: Value,
        fixture_id: String,
        input_ref: String,
    },
    SuccessRelation {
        expected: RelationExpectation,
        fixture_id: String,
        input_refs: Vec<String>,
    },
}

impl Case {
    fn id(&self) -> &str {
        match self {
            Self::Diagnostic { fixture_id, .. }
            | Self::Success { fixture_id, .. }
            | Self::SuccessRelation { fixture_id, .. } => fixture_id,
        }
    }
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct RelationExpectation {
    operation: Value,
    outputs: Vec<Value>,
}

struct ParsedRegistry {
    value: Value,
    number_lexemes: BTreeMap<String, String>,
}

struct RegistryJsonParser<'a> {
    bytes: &'a [u8],
    position: usize,
    number_lexemes: BTreeMap<String, String>,
}

impl<'a> RegistryJsonParser<'a> {
    fn new(text: &'a str) -> Self {
        Self {
            bytes: text.as_bytes(),
            position: 0,
            number_lexemes: BTreeMap::new(),
        }
    }

    fn parse(mut self) -> Result<ParsedRegistry, ()> {
        self.whitespace();
        let value = self.value("")?;
        self.whitespace();
        if self.position != self.bytes.len() {
            return Err(());
        }
        Ok(ParsedRegistry {
            value,
            number_lexemes: self.number_lexemes,
        })
    }

    fn value(&mut self, pointer: &str) -> Result<Value, ()> {
        match self.bytes.get(self.position).copied() {
            Some(b'{') => self.object(pointer),
            Some(b'[') => self.array(pointer),
            Some(b'"') => self.string().map(Value::String),
            Some(b't') if self.literal(b"true") => Ok(Value::Bool(true)),
            Some(b'f') if self.literal(b"false") => Ok(Value::Bool(false)),
            Some(b'n') if self.literal(b"null") => Ok(Value::Null),
            Some(b'-' | b'0'..=b'9') => self.number(pointer),
            _ => Err(()),
        }
    }

    fn object(&mut self, pointer: &str) -> Result<Value, ()> {
        self.position += 1;
        self.whitespace();
        let mut output = Map::new();
        if self.take(b'}') {
            return Ok(Value::Object(output));
        }
        loop {
            let key = self.string()?;
            if output.contains_key(&key) {
                return Err(());
            }
            self.whitespace();
            if !self.take(b':') {
                return Err(());
            }
            self.whitespace();
            let child_pointer = format!("{pointer}/{}", pointer_token(&key));
            let value = self.value(&child_pointer)?;
            output.insert(key, value);
            self.whitespace();
            if self.take(b'}') {
                break;
            }
            if !self.take(b',') {
                return Err(());
            }
            self.whitespace();
        }
        Ok(Value::Object(output))
    }

    fn array(&mut self, pointer: &str) -> Result<Value, ()> {
        self.position += 1;
        self.whitespace();
        let mut output = Vec::new();
        if self.take(b']') {
            return Ok(Value::Array(output));
        }
        loop {
            let child_pointer = format!("{pointer}/{}", output.len());
            output.push(self.value(&child_pointer)?);
            self.whitespace();
            if self.take(b']') {
                break;
            }
            if !self.take(b',') {
                return Err(());
            }
            self.whitespace();
        }
        Ok(Value::Array(output))
    }

    fn string(&mut self) -> Result<String, ()> {
        if !self.take(b'"') {
            return Err(());
        }
        let mut output = String::new();
        let mut segment_start = self.position;
        loop {
            let byte = self.bytes.get(self.position).copied().ok_or(())?;
            match byte {
                b'"' => {
                    output.push_str(
                        std::str::from_utf8(&self.bytes[segment_start..self.position])
                            .map_err(|_| ())?,
                    );
                    self.position += 1;
                    return Ok(output);
                }
                b'\\' => {
                    output.push_str(
                        std::str::from_utf8(&self.bytes[segment_start..self.position])
                            .map_err(|_| ())?,
                    );
                    self.position += 1;
                    let escape = *self.bytes.get(self.position).ok_or(())?;
                    self.position += 1;
                    match escape {
                        b'"' => output.push('"'),
                        b'\\' => output.push('\\'),
                        b'/' => output.push('/'),
                        b'b' => output.push('\u{0008}'),
                        b'f' => output.push('\u{000c}'),
                        b'n' => output.push('\n'),
                        b'r' => output.push('\r'),
                        b't' => output.push('\t'),
                        b'u' => {
                            let first = self.hex_quad()?;
                            let scalar = if (0xd800..=0xdbff).contains(&first) {
                                if !self.take(b'\\') || !self.take(b'u') {
                                    return Err(());
                                }
                                let second = self.hex_quad()?;
                                if !(0xdc00..=0xdfff).contains(&second) {
                                    return Err(());
                                }
                                0x10000
                                    + ((u32::from(first) - 0xd800) << 10)
                                    + (u32::from(second) - 0xdc00)
                            } else if (0xdc00..=0xdfff).contains(&first) {
                                return Err(());
                            } else {
                                u32::from(first)
                            };
                            output.push(char::from_u32(scalar).ok_or(())?);
                        }
                        _ => return Err(()),
                    }
                    segment_start = self.position;
                }
                0x00..=0x1f => return Err(()),
                _ => self.position += 1,
            }
        }
    }

    fn hex_quad(&mut self) -> Result<u16, ()> {
        let end = self.position.checked_add(4).ok_or(())?;
        let bytes = self.bytes.get(self.position..end).ok_or(())?;
        let mut value = 0_u16;
        for byte in bytes {
            let digit = u16::from(json_hex_digit(*byte)?);
            value = value
                .checked_mul(16)
                .and_then(|value| value.checked_add(digit))
                .ok_or(())?;
        }
        self.position = end;
        Ok(value)
    }

    fn number(&mut self, pointer: &str) -> Result<Value, ()> {
        let start = self.position;
        self.take(b'-');
        if self.take(b'0') {
            if self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                return Err(());
            }
        } else {
            if !self
                .bytes
                .get(self.position)
                .is_some_and(|byte| matches!(byte, b'1'..=b'9'))
            {
                return Err(());
            }
            self.position += 1;
            while self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                self.position += 1;
            }
        }
        if self.take(b'.') {
            if !self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                return Err(());
            }
            while self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                self.position += 1;
            }
        }
        if self
            .bytes
            .get(self.position)
            .is_some_and(|byte| matches!(byte, b'e' | b'E'))
        {
            self.position += 1;
            if self
                .bytes
                .get(self.position)
                .is_some_and(|byte| matches!(byte, b'+' | b'-'))
            {
                self.position += 1;
            }
            if !self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                return Err(());
            }
            while self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                self.position += 1;
            }
        }
        let text = std::str::from_utf8(&self.bytes[start..self.position]).map_err(|_| ())?;
        self.number_lexemes
            .insert(pointer.to_owned(), text.to_owned());
        Ok(Value::Number(0.into()))
    }

    fn literal(&mut self, literal: &[u8]) -> bool {
        if self.bytes.get(self.position..self.position + literal.len()) == Some(literal) {
            self.position += literal.len();
            true
        } else {
            false
        }
    }

    fn whitespace(&mut self) {
        while self
            .bytes
            .get(self.position)
            .is_some_and(|byte| matches!(byte, b' ' | b'\n' | b'\r' | b'\t'))
        {
            self.position += 1;
        }
    }

    fn take(&mut self, expected: u8) -> bool {
        if self.bytes.get(self.position) == Some(&expected) {
            self.position += 1;
            true
        } else {
            false
        }
    }
}

fn json_hex_digit(value: u8) -> Result<u8, ()> {
    match value {
        b'0'..=b'9' => Ok(value - b'0'),
        b'a'..=b'f' => Ok(value - b'a' + 10),
        b'A'..=b'F' => Ok(value - b'A' + 10),
        _ => Err(()),
    }
}

fn strict_registry_parse(raw: &[u8]) -> Result<ParsedRegistry, AuthorityPreflightRejection> {
    if raw.starts_with(&[0xef, 0xbb, 0xbf]) {
        return Err(reject(
            "registry_strict_json_parse",
            "authority#/registry",
            "UTF-8/BOM/JSON/duplicate failure",
        ));
    }
    let text = std::str::from_utf8(raw).map_err(|_| {
        reject(
            "registry_strict_json_parse",
            "authority#/registry",
            "UTF-8/BOM/JSON/duplicate failure",
        )
    })?;
    RegistryJsonParser::new(text).parse().map_err(|()| {
        reject(
            "registry_strict_json_parse",
            "authority#/registry",
            "UTF-8/BOM/JSON/duplicate failure",
        )
    })
}

fn pointer_token(value: &str) -> String {
    value.replace('~', "~0").replace('/', "~1")
}

fn canonical_nonnegative_integer(value: &str) -> bool {
    value == "0"
        || value
            .as_bytes()
            .first()
            .is_some_and(|first| matches!(first, b'1'..=b'9'))
            && value.as_bytes()[1..].iter().all(u8::is_ascii_digit)
}

fn decrement_decimal_magnitude(value: &mut Vec<u8>) {
    let mut index = value.len();
    while index != 0 {
        index -= 1;
        if value[index] == 0 {
            value[index] = 9;
        } else {
            value[index] -= 1;
            break;
        }
    }
    if value.first() == Some(&0) {
        value.remove(0);
    }
}

fn canonical_registry_number(value: &str, render_budget: usize) -> Result<String, ()> {
    let (negative, unsigned) = value
        .strip_prefix('-')
        .map_or((false, value), |value| (true, value));
    let (coefficient, exponent) = unsigned.find(['e', 'E']).map_or((unsigned, None), |index| {
        (&unsigned[..index], Some(&unsigned[index + 1..]))
    });
    let (integer, fraction) = coefficient
        .split_once('.')
        .map_or((coefficient, ""), |parts| parts);
    let mut digits = integer.as_bytes().to_vec();
    digits.extend_from_slice(fraction.as_bytes());
    if digits.iter().all(|digit| *digit == b'0') {
        return Ok("0".to_owned());
    }

    let (exponent_negative, exponent_digits) = exponent.map_or((false, ""), |exponent| {
        exponent.strip_prefix('-').map_or_else(
            || (false, exponent.strip_prefix('+').unwrap_or(exponent)),
            |digits| (true, digits),
        )
    });
    let mut exponent_magnitude = exponent_digits
        .bytes()
        .skip_while(|digit| *digit == b'0')
        .map(|digit| digit - b'0')
        .collect::<Vec<_>>();
    let mut point = integer.len();
    let mut before_point = 0_usize;
    let shift_budget = render_budget.saturating_add(digits.len()).saturating_add(1);
    let mut shifts = 0_usize;
    while !exponent_magnitude.is_empty() {
        if shifts == shift_budget {
            return Err(());
        }
        decrement_decimal_magnitude(&mut exponent_magnitude);
        if exponent_negative {
            if point == 0 {
                before_point = before_point.checked_add(1).ok_or(())?;
            } else {
                point -= 1;
            }
        } else {
            point = point.checked_add(1).ok_or(())?;
        }
        shifts += 1;
    }

    let leading = digits.iter().position(|digit| *digit != b'0').ok_or(())?;
    let trailing = digits.iter().rposition(|digit| *digit != b'0').ok_or(())? + 1;
    let significant = &digits[leading..trailing];
    let mut rendered = String::new();
    if before_point != 0 {
        let zero_count = before_point.checked_add(leading).ok_or(())?;
        rendered.push_str("0.");
        rendered.extend(std::iter::repeat_n('0', zero_count));
        rendered.extend(significant.iter().map(|digit| char::from(*digit)));
    } else if point <= leading {
        rendered.push_str("0.");
        rendered.extend(std::iter::repeat_n('0', leading - point));
        rendered.extend(significant.iter().map(|digit| char::from(*digit)));
    } else {
        let decimal_position = point - leading;
        if decimal_position < significant.len() {
            rendered.extend(
                significant[..decimal_position]
                    .iter()
                    .map(|digit| char::from(*digit)),
            );
            rendered.push('.');
            rendered.extend(
                significant[decimal_position..]
                    .iter()
                    .map(|digit| char::from(*digit)),
            );
        } else {
            rendered.extend(significant.iter().map(|digit| char::from(*digit)));
            rendered.extend(std::iter::repeat_n(
                '0',
                decimal_position - significant.len(),
            ));
        }
    }
    if negative {
        rendered.insert(0, '-');
    }
    if rendered.len() > render_budget {
        return Err(());
    }
    Ok(rendered)
}

fn registry_pretty_bytes(registry: &ParsedRegistry, render_budget: usize) -> Result<Vec<u8>, ()> {
    fn scalar(
        value: &Value,
        pointer: &str,
        number_lexemes: &BTreeMap<String, String>,
        render_budget: usize,
    ) -> Result<String, ()> {
        match value {
            Value::Number(_) => {
                canonical_registry_number(number_lexemes.get(pointer).ok_or(())?, render_budget)
            }
            Value::String(text) => {
                serde_json::to_string(&text.nfc().collect::<String>()).map_err(|_| ())
            }
            _ => serde_json::to_string(value).map_err(|_| ()),
        }
    }

    fn ordered_entries<'a>(
        object: &'a Map<String, Value>,
        context: &str,
    ) -> Result<Vec<(&'a str, String)>, ()> {
        let preferred: &[&str] = match context {
            "root" => &["format", "baseline_commit", "baseline_tree", "documents"],
            "document" => &["key", "path", "bytes", "sha256"],
            _ => &[],
        };
        if !preferred.is_empty() {
            return Ok(preferred
                .iter()
                .filter_map(|key| {
                    object
                        .get_key_value(*key)
                        .map(|(key, _)| (key.as_str(), key.nfc().collect::<String>()))
                })
                .collect());
        }
        let mut entries = object
            .keys()
            .map(|key| (key.as_str(), key.nfc().collect::<String>()))
            .collect::<Vec<_>>();
        entries.sort_by(|left, right| left.1.as_bytes().cmp(right.1.as_bytes()));
        if entries
            .windows(2)
            .any(|pair| pair[0].1.as_bytes() == pair[1].1.as_bytes())
        {
            return Err(());
        }
        Ok(entries)
    }

    fn write(
        value: &Value,
        pointer: &str,
        depth: usize,
        context: &str,
        number_lexemes: &BTreeMap<String, String>,
        render_budget: usize,
        lines: &mut Vec<String>,
    ) -> Result<(), ()> {
        match value {
            Value::Object(object) => {
                let entries = ordered_entries(object, context)?;
                if entries.is_empty() {
                    lines.last_mut().unwrap().push_str("{}");
                    return Ok(());
                }
                lines.last_mut().unwrap().push('{');
                for (index, (key, normalized_key)) in entries.iter().enumerate() {
                    lines.push(format!(
                        "{}{}: ",
                        "  ".repeat(depth + 1),
                        serde_json::to_string(normalized_key).map_err(|_| ())?
                    ));
                    let child_context = if context == "root" && *key == "documents" {
                        "documents"
                    } else {
                        "other"
                    };
                    write(
                        &object[*key],
                        &format!("{pointer}/{}", pointer_token(key)),
                        depth + 1,
                        child_context,
                        number_lexemes,
                        render_budget,
                        lines,
                    )?;
                    if index + 1 != entries.len() {
                        lines.last_mut().unwrap().push(',');
                    }
                }
                lines.push(format!("{}}}", "  ".repeat(depth)));
            }
            Value::Array(values) => {
                if values.is_empty() {
                    lines.last_mut().unwrap().push_str("[]");
                    return Ok(());
                }
                lines.last_mut().unwrap().push('[');
                for (index, child) in values.iter().enumerate() {
                    lines.push("  ".repeat(depth + 1));
                    write(
                        child,
                        &format!("{pointer}/{index}"),
                        depth + 1,
                        if context == "documents" {
                            "document"
                        } else {
                            "other"
                        },
                        number_lexemes,
                        render_budget,
                        lines,
                    )?;
                    if index + 1 != values.len() {
                        lines.last_mut().unwrap().push(',');
                    }
                }
                lines.push(format!("{}]", "  ".repeat(depth)));
            }
            _ => lines.last_mut().unwrap().push_str(&scalar(
                value,
                pointer,
                number_lexemes,
                render_budget,
            )?),
        }
        Ok(())
    }

    let mut lines = vec![String::new()];
    write(
        &registry.value,
        "",
        0,
        "root",
        &registry.number_lexemes,
        render_budget,
        &mut lines,
    )?;
    Ok((lines.join("\n") + "\n").into_bytes())
}

fn authority_preflight(
    inputs: &PC7AuthorityInputsV1,
) -> Result<(Value, Vec<u8>), AuthorityPreflightRejection> {
    if !inputs.authority_root.is_dir() {
        return Err(reject(
            "invocation_authority_root",
            "authority#/root",
            "authority root invalid",
        ));
    }
    if inputs.registry_path != inputs.authority_root.join(REGISTRY_RELATIVE_PATH) {
        return Err(reject(
            "invocation_registry_binding",
            "authority#/registry",
            "registry path is not the fixed V1 path",
        ));
    }
    if inputs.registry_bytes.is_empty() {
        return Err(reject(
            "registry_read",
            "authority#/registry",
            "registry unreadable",
        ));
    }
    let registry = strict_registry_parse(&inputs.registry_bytes)?;
    let registry_value = &registry.value;

    let mut unknown = BTreeSet::new();
    if let Some(root) = registry_value.as_object() {
        for key in root.keys() {
            if !["format", "baseline_commit", "baseline_tree", "documents"].contains(&key.as_str())
            {
                unknown.insert(format!("authority#/registry/{}", pointer_token(key)));
            }
        }
        if let Some(rows) = root.get("documents").and_then(Value::as_array) {
            for (index, row) in rows.iter().enumerate() {
                if let Some(row) = row.as_object() {
                    for key in row.keys() {
                        if !["key", "path", "bytes", "sha256"].contains(&key.as_str()) {
                            unknown.insert(format!(
                                "authority#/registry/documents/{index}/{}",
                                pointer_token(key)
                            ));
                        }
                    }
                }
            }
        }
    }
    if let Some(path) = unknown.into_iter().next() {
        return Err(reject(
            "registry_unknown_members",
            path,
            "unknown registry member",
        ));
    }
    let registry_bytes_match = registry_pretty_bytes(&registry, inputs.registry_bytes.len())
        .is_ok_and(|bytes| bytes == inputs.registry_bytes);
    if !registry_bytes_match {
        return Err(reject(
            "registry_canonical_bytes",
            "authority#/registry",
            "registry bytes have no admitted V1 serialization",
        ));
    }

    let root = registry_value.as_object().ok_or_else(|| {
        reject(
            "registry_missing_members",
            "authority#/registry/format",
            "missing registry member",
        )
    })?;
    for member in ["format", "baseline_commit", "baseline_tree", "documents"] {
        if !root.contains_key(member) {
            return Err(reject(
                "registry_missing_members",
                format!("authority#/registry/{member}"),
                "missing registry member",
            ));
        }
    }
    let documents_value = &root["documents"];
    if let Some(documents) = documents_value.as_array() {
        for index in 0..8 {
            let Some(row) = documents.get(index) else {
                return Err(reject(
                    "registry_missing_members",
                    format!("authority#/registry/documents/{index}"),
                    "missing registry document",
                ));
            };
            if let Some(row) = row.as_object() {
                for member in ["key", "path", "bytes", "sha256"] {
                    if !row.contains_key(member) {
                        return Err(reject(
                            "registry_missing_members",
                            format!("authority#/registry/documents/{index}/{member}"),
                            "missing registry member",
                        ));
                    }
                }
            }
        }
    }

    for member in ["format", "baseline_commit", "baseline_tree"] {
        if !root[member].is_string() {
            return Err(reject(
                "registry_member_types",
                format!("authority#/registry/{member}"),
                "wrong member type",
            ));
        }
    }
    let documents = documents_value.as_array().ok_or_else(|| {
        reject(
            "registry_member_types",
            "authority#/registry/documents",
            "wrong member type",
        )
    })?;
    for (index, row) in documents.iter().enumerate() {
        let row = row.as_object().ok_or_else(|| {
            reject(
                "registry_member_types",
                format!("authority#/registry/documents/{index}"),
                "wrong member type",
            )
        })?;
        for member in ["key", "path", "sha256"] {
            if !row[member].is_string() {
                return Err(reject(
                    "registry_member_types",
                    format!("authority#/registry/documents/{index}/{member}"),
                    "wrong member type",
                ));
            }
        }
        let bytes_pointer = format!("/documents/{index}/bytes");
        if registry
            .number_lexemes
            .get(&bytes_pointer)
            .is_none_or(|value| !canonical_nonnegative_integer(value))
        {
            return Err(reject(
                "registry_member_types",
                format!("authority#/registry/documents/{index}/bytes"),
                "wrong member type",
            ));
        }
    }
    if root["format"] != REGISTRY_FORMAT {
        return Err(reject(
            "registry_format",
            "authority#/registry/format",
            "wrong registry format",
        ));
    }
    if root["baseline_commit"] != BASELINE_COMMIT {
        return Err(reject(
            "registry_baseline_commit",
            "authority#/registry/baseline_commit",
            "wrong baseline commit",
        ));
    }
    if root["baseline_tree"] != BASELINE_TREE {
        return Err(reject(
            "registry_baseline_tree",
            "authority#/registry/baseline_tree",
            "wrong baseline tree",
        ));
    }
    if documents.len() != AUTHORITY_DOCUMENTS.len() {
        return Err(reject(
            "registry_document_key_order",
            "authority#/registry/documents",
            "wrong document count",
        ));
    }
    for (index, (key, _)) in AUTHORITY_DOCUMENTS.iter().enumerate() {
        if documents[index]["key"] != *key {
            return Err(reject(
                "registry_document_key_order",
                format!("authority#/registry/documents/{index}/key"),
                "wrong document key or order",
            ));
        }
    }
    for (index, (_, path)) in AUTHORITY_DOCUMENTS.iter().enumerate() {
        if documents[index]["path"] != *path {
            return Err(reject(
                "registry_document_path_bindings",
                format!("authority#/registry/documents/{index}/path"),
                "wrong document path binding",
            ));
        }
    }
    let mut manifest_bytes = Vec::new();
    for (index, (key, path)) in AUTHORITY_DOCUMENTS.iter().enumerate() {
        let raw = fs::read(inputs.authority_root.join(path)).map_err(|_| {
            reject(
                "authority_document_bytes",
                format!("authority#/{key}"),
                "authority document unreadable",
            )
        })?;
        let expected_bytes = raw.len().to_string();
        let bytes_pointer = format!("/documents/{index}/bytes");
        if registry.number_lexemes.get(&bytes_pointer) != Some(&expected_bytes) {
            return Err(reject(
                "authority_document_bytes",
                format!("authority#/{key}"),
                "authority document byte count mismatch",
            ));
        }
        if documents[index]["sha256"].as_str() != Some(&sha256_digest(&raw).to_string()) {
            return Err(reject(
                "authority_document_bytes",
                format!("authority#/{key}"),
                "authority document SHA-256 mismatch",
            ));
        }
        if *key == "pc7_specified_conformance_manifest" {
            manifest_bytes = raw;
        }
    }
    Ok((registry.value, manifest_bytes))
}

pub fn execute_all(
    inputs: &PC7AuthorityInputsV1,
) -> Result<ExecutionSummary, AuthorityPreflightRejection> {
    execute_plan_bytes(inputs, PLAN_BYTES)
}

pub fn execute_plan_bytes(
    inputs: &PC7AuthorityInputsV1,
    plan_bytes: &[u8],
) -> Result<ExecutionSummary, AuthorityPreflightRejection> {
    let (_, manifest_bytes) = authority_preflight(inputs)?;
    let plan: Plan = serde_json::from_slice(plan_bytes).expect("strict PC7 executable plan");
    if plan.authority.registry_bytes != inputs.registry_bytes.len()
        || plan.authority.registry_sha256 != sha256_digest(&inputs.registry_bytes).to_string()
    {
        return Err(reject(
            "plan_registry_binding",
            "authority#/registry",
            "plan registry binding mismatch",
        ));
    }
    assert_eq!(sha256_digest(&manifest_bytes).to_string(), MANIFEST_SHA256);
    let manifest: Value = serde_json::from_slice(&manifest_bytes).expect("valid PC7 manifest JSON");
    assert_eq!(
        plan.fixture_plan_version,
        "threadsmith-pc7-resolve-executable-plan-0.1"
    );
    assert_eq!(
        plan.authority.manifest_path,
        "docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json"
    );
    assert_eq!(plan.authority.manifest_sha256, MANIFEST_SHA256);
    assert_eq!(plan.future_vector_ids.len(), 4);

    let defined = manifest["fixtures"]
        .as_array()
        .expect("fixtures array")
        .iter()
        .map(|fixture| fixture["id"].as_str().expect("fixture id").to_owned())
        .collect::<BTreeSet<_>>();
    let generated = plan
        .cases
        .iter()
        .map(|case| case.id().to_owned())
        .collect::<BTreeSet<_>>();
    assert_eq!(defined.len(), 118);
    assert_eq!(defined, generated);
    assert_eq!(plan.cases.len(), generated.len());

    let mut executed = BTreeSet::new();
    for case in &plan.cases {
        assert!(executed.insert(case.id().to_owned()), "duplicate execution");
        match case {
            Case::Diagnostic {
                expected,
                fixture_id,
                input_ref,
            } => execute_diagnostic(&manifest, fixture_id, input_ref, expected),
            Case::Success {
                expected,
                fixture_id,
                input_ref,
            } => {
                execute_success(&manifest, fixture_id, input_ref, expected);
            }
            Case::SuccessRelation {
                expected,
                fixture_id,
                input_refs,
            } => execute_relation(&manifest, fixture_id, input_refs, expected),
        }
    }
    assert_eq!(defined, executed);
    Ok(ExecutionSummary {
        defined: defined.len(),
        generated: generated.len(),
        executed: executed.len(),
        future_vectors: plan.future_vector_ids.len(),
    })
}

pub fn assert_lock_package_scalar_grammar_order() {
    let manifest: Value =
        serde_json::from_slice(MANIFEST_BYTES).expect("valid accepted PC7 manifest JSON");
    let (scanned, _) = construct_input(&manifest, "alias_distinct");
    let lock = serde_json::json!({
        "lock_version": 1,
        "lattice": "0.3",
        "profile": "core",
        "root_blueprint_digest": "lattice:blueprint:sha256:0000000000000000000000000000000000000000000000000000000000000000",
        "packages": [
            {
                "name": "alpha",
                "version": "invalid",
                "package_id": "lattice:package:sha256:0000000000000000000000000000000000000000000000000000000000000000",
                "requested_by": []
            },
            {
                "name": "INVALID",
                "version": "1.0.0",
                "package_id": "lattice:package:sha256:0000000000000000000000000000000000000000000000000000000000000000",
                "requested_by": []
            }
        ],
        "lock_id": "lattice:lock:sha256:0000000000000000000000000000000000000000000000000000000000000000"
    });
    let bytes = canonical_bytes(&lock).expect("canonical adversarial Lockfile");
    let diagnostic = resolve_source(scanned, ExistingLockfileInput::from_bytes(bytes))
        .expect_err("adversarial Lockfile must fail schema admission");
    assert_eq!(diagnostic.code(), "RESOLVE_LOCK_SCHEMA_INVALID");
    assert_eq!(diagnostic.path(), "lock#/packages/1/name");
}

pub fn assert_lock_top_level_type_stage_precedes_scalar_stage() {
    let manifest: Value =
        serde_json::from_slice(MANIFEST_BYTES).expect("valid accepted PC7 manifest JSON");
    let (scanned, _) = construct_input(&manifest, "alias_distinct");
    let lock = serde_json::json!({
        "lock_version": 2,
        "lattice": false,
        "profile": "core",
        "root_blueprint_digest": "lattice:blueprint:sha256:0000000000000000000000000000000000000000000000000000000000000000",
        "packages": [],
        "lock_id": "lattice:lock:sha256:0000000000000000000000000000000000000000000000000000000000000000"
    });
    let bytes = canonical_bytes(&lock).expect("canonical adversarial Lockfile");
    let diagnostic = resolve_source(scanned, ExistingLockfileInput::from_bytes(bytes))
        .expect_err("top-level Lockfile type defect must select the error branch");
    assert_eq!(diagnostic.code(), "RESOLVE_LOCK_SCHEMA_INVALID");
    assert_eq!(diagnostic.path(), "lock#/lattice");
    assert!(
        diagnostic.canonical_cycle().is_none(),
        "Lockfile schema diagnostics carry no structured detail"
    );
    assert_eq!(
        diagnostic.to_string(),
        "RESOLVE_LOCK_SCHEMA_INVALID at lock#/lattice"
    );
}

pub fn assert_lock_paths_encode_pointer_tokens() {
    let manifest: Value =
        serde_json::from_slice(MANIFEST_BYTES).expect("valid accepted PC7 manifest JSON");
    let (scanned, _) = construct_input(&manifest, "alias_distinct");
    let lock = serde_json::json!({
        "lock_version": 1,
        "lattice": "0.3",
        "profile": "core",
        "root_blueprint_digest": "lattice:blueprint:sha256:0000000000000000000000000000000000000000000000000000000000000000",
        "packages": [],
        "lock_id": "lattice:lock:sha256:0000000000000000000000000000000000000000000000000000000000000000",
        "a/b": 0
    });
    let bytes = canonical_bytes(&lock).expect("canonical adversarial Lockfile");
    let schema_diagnostic =
        resolve_source(scanned.clone(), ExistingLockfileInput::from_bytes(bytes))
            .expect_err("unknown Lockfile member must fail schema admission");
    assert_eq!(schema_diagnostic.code(), "RESOLVE_LOCK_SCHEMA_INVALID");
    assert_eq!(schema_diagnostic.path(), "lock#/a~1b");

    let duplicate_key_diagnostic = resolve_source(
        scanned,
        ExistingLockfileInput::from_bytes(br#"{"a/b":0,"a/b":1}"#.as_slice()),
    )
    .expect_err("duplicate Lockfile key must fail source admission");
    assert_eq!(
        duplicate_key_diagnostic.code(),
        "RESOLVE_LOCK_SOURCE_INVALID"
    );
    assert_eq!(duplicate_key_diagnostic.path(), "lock#/a~1b");

    let invalid_json_diagnostic = resolve_source(
        construct_input(&manifest, "alias_distinct").0,
        ExistingLockfileInput::from_bytes(br#"{"lock_version" 1}"#.as_slice()),
    )
    .expect_err("invalid JSON must fail Lockfile source intake");
    assert_eq!(
        invalid_json_diagnostic.code(),
        "RESOLVE_LOCK_SOURCE_INVALID"
    );
    assert_eq!(invalid_json_diagnostic.path(), "lock#");
}

pub fn assert_lock_negative_zero_rejected_at_source_intake() {
    let manifest: Value =
        serde_json::from_slice(MANIFEST_BYTES).expect("valid accepted PC7 manifest JSON");
    let (scanned, lock) = construct_input(&manifest, "lock_valid_reuse");
    let mut bytes = lock
        .bytes()
        .expect("valid reuse input carries Lockfile bytes")
        .to_vec();
    let source = br#""lock_version":1"#;
    let replacement = br#""lock_version":-0"#;
    assert_eq!(
        bytes
            .windows(source.len())
            .filter(|window| *window == source)
            .count(),
        1
    );
    let offset = bytes
        .windows(source.len())
        .position(|window| window == source)
        .unwrap();
    bytes.splice(offset..offset + source.len(), replacement.iter().copied());
    let diagnostic = resolve_source(scanned, ExistingLockfileInput::from_bytes(bytes))
        .expect_err("negative zero must fail direct Lockfile source intake");
    assert_eq!(diagnostic.code(), "RESOLVE_LOCK_SOURCE_INVALID");
    assert_eq!(diagnostic.path(), "lock#/lock_version");
}

fn execute_diagnostic(manifest: &Value, fixture_id: &str, input_ref: &str, expected: &Value) {
    let (scanned, lock) = construct_input(manifest, input_ref);
    let diagnostic = resolve_source(scanned, lock)
        .expect_err("diagnostic fixture must return only the error branch");
    let primary = &expected["primary_diagnostic"];
    assert_eq!(
        diagnostic.code(),
        primary["code"].as_str().expect("expected code"),
        "{fixture_id}: diagnostic code"
    );
    assert_eq!(
        diagnostic.path(),
        primary["path"].as_str().expect("expected path"),
        "{fixture_id}: diagnostic path"
    );
    match primary.get("canonical_cycle") {
        Some(expected_cycle) => {
            let actual = serde_json::to_value(
                diagnostic
                    .canonical_cycle()
                    .expect("cycle fixture must include detail"),
            )
            .expect("cycle serialization");
            assert_eq!(&actual, expected_cycle, "{fixture_id}: canonical cycle");
        }
        None => assert!(
            diagnostic.canonical_cycle().is_none(),
            "{fixture_id}: unexpected diagnostic detail"
        ),
    }
    assert!(expected["successful_output"].is_null());
}

struct SuccessObservation {
    actual: Value,
    materialized_expected: Value,
}

fn execute_success(
    manifest: &Value,
    fixture_id: &str,
    input_ref: &str,
    expected: &Value,
) -> SuccessObservation {
    let (scanned, lock) = construct_input(manifest, input_ref);
    let expected_scanned_source =
        scanned_source_oracle::PreResolveProjection::from_scanned(&scanned);
    let retained = scanned.clone();
    let resolved = resolve_source(scanned, lock)
        .unwrap_or_else(|error| panic!("{fixture_id}: unexpected {error}"));
    assert_eq!(
        resolved.scanned_source(),
        &retained,
        "{fixture_id}: exact ScannedSource continuity"
    );
    let actual = resolved.semantic_projection().clone();
    let materialized = materialize_output(expected, input_ref, manifest, &expected_scanned_source);
    assert_eq!(
        canonical_bytes(&actual).expect("actual canonical"),
        canonical_bytes(&materialized).expect("expected canonical"),
        "{fixture_id}: complete semantic output"
    );
    SuccessObservation {
        actual,
        materialized_expected: materialized,
    }
}

fn execute_relation(
    manifest: &Value,
    fixture_id: &str,
    input_refs: &[String],
    expectation: &RelationExpectation,
) {
    assert_eq!(input_refs.len(), expectation.outputs.len());
    let mut observations = Vec::new();
    for (input_ref, expected) in input_refs.iter().zip(&expectation.outputs) {
        observations.push(execute_success(manifest, fixture_id, input_ref, expected));
    }
    let actual = observations
        .iter()
        .map(|observation| observation.actual.clone())
        .collect::<Vec<_>>();
    let operation = expectation
        .operation
        .as_object()
        .expect("relation operation object");
    match operation["kind"].as_str().expect("operation kind") {
        "canonical_output_bytes_equal" => {
            assert_eq!(actual.len(), 2);
            assert_eq!(
                canonical_bytes(&actual[0]).unwrap(),
                canonical_bytes(&actual[1]).unwrap()
            );
        }
        "compare_fields" => {
            compare_selectors(operation, &actual, "equal_fields", true);
            compare_selectors(operation, &actual, "different_fields", false);
        }
        "compare_after_source_path_erasure" => {
            let erased = actual
                .iter()
                .cloned()
                .map(erase_source_paths)
                .collect::<Vec<_>>();
            compare_selectors(operation, &erased, "equal_fields", true);
        }
        "assert_no_later_artifacts" => {
            assert_eq!(actual.len(), 1);
            for selector in string_array(&operation["required_empty_fields"]) {
                assert_eq!(
                    project(&actual[0], selector),
                    vec![&Value::Array(Vec::new())]
                );
            }
            assert_eq!(
                actual[0]["authority"], operation["required_authority"],
                "{fixture_id}: authority"
            );
            for forbidden in string_array(&operation["forbidden_artifacts"]) {
                let folded = forbidden.to_ascii_lowercase();
                assert!(actual[0].get(&folded).is_none());
                for field in ["created_artifacts", "created_identities"] {
                    assert!(
                        !actual[0][field]
                            .as_array()
                            .expect("created array")
                            .iter()
                            .any(|value| value
                                .as_str()
                                .is_some_and(|text| { text.eq_ignore_ascii_case(forbidden) }))
                    );
                }
            }
        }
        "retained_boundary_repeatability" => {
            for input_ref in input_refs {
                assert_eq!(
                    manifest["resolve_inputs"][input_ref]["host_capabilities"],
                    Value::Array(Vec::new())
                );
            }
            compare_selectors(operation, &actual, "required_equal_fields", true);
        }
        "assert_scanned_source_independent_projection" => {
            assert_eq!(actual.len(), 1);
            assert_eq!(
                operation["correct_expected_source"],
                "pre_resolve_pc2_through_pc6_projection"
            );
            assert_eq!(operation["required_correct_comparison"], "equal");
            assert_eq!(operation["required_wrong_comparison"], "different");
            assert_eq!(operation["wrong_scanned_source_field"], "scanned_source");
            assert_eq!(
                canonical_bytes(&actual[0]).unwrap(),
                canonical_bytes(&observations[0].materialized_expected).unwrap(),
                "{fixture_id}: independently materialized pre-Resolve projection must compare equal"
            );
            let deliberately_wrong_source =
                scanned_source_oracle::ManifestWrongProjection::from_operation(operation);
            let deliberately_wrong = materialize_output(
                &expectation.outputs[0],
                &input_refs[0],
                manifest,
                &deliberately_wrong_source,
            );
            assert_ne!(
                canonical_bytes(&actual[0]).unwrap(),
                canonical_bytes(&deliberately_wrong).unwrap(),
                "{fixture_id}: manifest-supplied deliberately wrong projection must compare different"
            );
        }
        other => panic!("{fixture_id}: unknown relation operation {other}"),
    }
}

fn compare_selectors(
    operation: &Map<String, Value>,
    operands: &[Value],
    member: &str,
    expected_equal: bool,
) {
    assert_eq!(operands.len(), 2);
    for selector in string_array(&operation[member]) {
        let left = projection_bytes(&operands[0], selector);
        let right = projection_bytes(&operands[1], selector);
        assert_eq!(left == right, expected_equal, "{member}: {selector}");
    }
}

fn construct_input(manifest: &Value, input_ref: &str) -> (ScannedSource, ExistingLockfileInput) {
    construct_input_with_root_mutation(manifest, input_ref, |_| {}, false)
}

// Shared with pc8_lock; unused when this module is compiled by pc7_resolve alone.
#[allow(dead_code)]
pub fn construct_resolved_source_for_pc8<F>(
    input_ref: &str,
    mutate_root: F,
    reverse_package_visitation: bool,
) -> ResolvedSource
where
    F: FnOnce(&mut Value),
{
    let manifest: Value =
        serde_json::from_slice(MANIFEST_BYTES).expect("valid accepted PC7 manifest JSON");
    let (scanned, lock) = construct_input_with_root_mutation(
        &manifest,
        input_ref,
        mutate_root,
        reverse_package_visitation,
    );
    resolve_source(scanned, lock).expect("accepted PC7 success recipe")
}

// Shared with pc8_lock; unused when this module is compiled by pc7_resolve alone.
#[allow(dead_code)]
pub fn materialize_resolved_source_for_pc8(
    expected: &Value,
    input_ref: &str,
    source: &ResolvedSource,
) -> Value {
    let manifest: Value =
        serde_json::from_slice(MANIFEST_BYTES).expect("valid accepted PC7 manifest JSON");
    let scanned =
        scanned_source_oracle::PreResolveProjection::from_scanned(source.scanned_source());
    let mut materialized = materialize_output(expected, input_ref, &manifest, &scanned);
    if materialized["scanned_source"]["construction"] == "pc6_successful_scan" {
        materialized["scanned_source"] =
            scanned_source_oracle::MaterializationSource::value(&scanned).clone();
    }
    materialized
}

fn construct_input_with_root_mutation<F>(
    manifest: &Value,
    input_ref: &str,
    mutate_root: F,
    reverse_package_visitation: bool,
) -> (ScannedSource, ExistingLockfileInput)
where
    F: FnOnce(&mut Value),
{
    let input = &manifest["resolve_inputs"][input_ref];
    assert_eq!(input["host_capabilities"], Value::Array(Vec::new()));
    let scanned_plan = &input["scanned_source"];
    assert_eq!(scanned_plan["construction"], "pc6_successful_scan");

    let mut root_value = scanned_plan["defaulted_root"].clone();
    mutate_root(&mut root_value);
    let root_bytes = canonical_bytes(&root_value).expect("canonical defaulted root");
    let parsed = parse_blueprint_source(&root_bytes).expect("PC2 root construction");
    let validated = validate_blueprint_source(parsed).expect("PC3 root construction");
    let defaulted = apply_blueprint_defaults(validated);
    assert_eq!(
        defaulted.as_value(),
        &root_value,
        "{input_ref}: PC4 idempotent defaulted root"
    );
    let digested = digest_source(defaulted);
    if root_value == scanned_plan["defaulted_root"] {
        assert_eq!(
            digested.blueprint_digest().to_string(),
            scanned_plan["blueprint_digest"]
                .as_str()
                .expect("blueprint digest")
        );
    }

    let mut record_locators = scanned_plan["package_records"]
        .as_array()
        .expect("package records")
        .iter()
        .map(|value| value.as_str().expect("package record locator").to_owned())
        .chain(
            scanned_plan
                .get("package_family_ref")
                .and_then(Value::as_str)
                .into_iter()
                .flat_map(|family| {
                    manifest["generated_package_families"][family]["records"]
                        .as_array()
                        .expect("generated records")
                        .iter()
                        .enumerate()
                        .map(move |(index, _)| {
                            format!("generated_package_families.{family}.records/{index}")
                        })
                }),
        )
        .collect::<Vec<_>>();
    if reverse_package_visitation {
        record_locators.reverse();
    }
    let snapshot = package_snapshot(manifest, &record_locators);
    let scanned = scan_packages(
        digested,
        acquire_project_snapshot(Ok(Some(snapshot))).expect("snapshot acquisition"),
    )
    .expect("every current PC7 input uses successful public PC6 construction");
    compare_scanned(manifest, &record_locators, &scanned);

    let lock = input["existing_lock_ref"].as_str().map_or_else(
        ExistingLockfileInput::absent,
        |reference| {
            let bytes_reference = manifest["lock_inputs"][reference]["bytes_ref"]
                .as_str()
                .expect("lock bytes ref");
            ExistingLockfileInput::from_bytes(decode_constant(manifest, bytes_reference))
        },
    );
    (scanned, lock)
}

fn package_snapshot(manifest: &Value, locators: &[String]) -> SnapshotNode {
    let mut packages: BTreeMap<String, BTreeMap<String, Value>> = BTreeMap::new();
    for locator in locators {
        let record = record_value(manifest, locator);
        let descriptor = &record["descriptor"];
        let name = descriptor["package"].as_str().expect("package").to_owned();
        let version = descriptor["version"].as_str().expect("version").to_owned();
        assert!(
            packages
                .entry(name)
                .or_default()
                .insert(version, record)
                .is_none(),
            "PC6 current path cannot compose duplicate name/version"
        );
    }
    directory(
        packages
            .into_iter()
            .map(|(name, versions)| {
                entry(
                    &name,
                    directory(
                        versions
                            .into_iter()
                            .map(|(version, record)| {
                                let descriptor = &record["descriptor"];
                                let mut children = vec![entry(
                                    "package.yaml",
                                    regular(descriptor_source(descriptor)),
                                )];
                                for file in
                                    record["verified_files"].as_array().expect("verified files")
                                {
                                    children.push(entry(
                                        file["path"].as_str().expect("file path"),
                                        regular(decode_inline(&file["bytes"])),
                                    ));
                                }
                                entry(&version, directory(children))
                            })
                            .collect(),
                    ),
                )
            })
            .collect(),
    )
}

fn descriptor_source(descriptor: &Value) -> Vec<u8> {
    let mut source = String::new();
    source.push_str("package: ");
    source.push_str(descriptor["package"].as_str().unwrap());
    source.push('\n');
    source.push_str("version: \"");
    source.push_str(descriptor["version"].as_str().unwrap());
    source.push_str("\"\nlattice: \"0.3\"\nprofiles:\n");
    for profile in descriptor["profiles"].as_array().unwrap() {
        source.push_str("  - ");
        source.push_str(profile.as_str().unwrap());
        source.push('\n');
    }
    source.push_str("module_file: ");
    source.push_str(descriptor["module_file"].as_str().unwrap());
    source.push_str("\nfiles:\n");
    for file in descriptor["files"].as_array().unwrap() {
        source.push_str("  - path: ");
        source.push_str(file["path"].as_str().unwrap());
        source.push_str("\n    sha256: ");
        source.push_str(file["sha256"].as_str().unwrap());
        source.push('\n');
    }
    source.into_bytes()
}

fn compare_scanned(manifest: &Value, locators: &[String], scanned: &ScannedSource) {
    let mut expected = locators
        .iter()
        .map(|locator| record_value(manifest, locator))
        .collect::<Vec<_>>();
    expected.sort_by(record_cmp);
    let actual = scanned
        .packages()
        .iter()
        .map(actual_package_value)
        .collect::<Vec<_>>();
    assert_eq!(
        actual, expected,
        "complete PC6 ScannedSource package records"
    );
}

fn record_cmp(left: &Value, right: &Value) -> Ordering {
    left["descriptor"]["package"]
        .as_str()
        .unwrap()
        .as_bytes()
        .cmp(right["descriptor"]["package"].as_str().unwrap().as_bytes())
        .then_with(|| {
            compare_version(
                left["descriptor"]["version"].as_str().unwrap(),
                right["descriptor"]["version"].as_str().unwrap(),
            )
        })
}

fn compare_version(left: &str, right: &str) -> Ordering {
    for (left, right) in left.split('.').zip(right.split('.')) {
        let order = left
            .len()
            .cmp(&right.len())
            .then_with(|| left.as_bytes().cmp(right.as_bytes()));
        if order != Ordering::Equal {
            return order;
        }
    }
    Ordering::Equal
}

fn actual_package_value(package: &ScannedPackage) -> Value {
    let descriptor = package.descriptor();
    let descriptor_value = object([
        (
            "files",
            Value::Array(
                descriptor
                    .files()
                    .iter()
                    .map(|file| {
                        object([
                            ("path", Value::String(file.path().to_owned())),
                            ("sha256", Value::String(file.sha256().to_owned())),
                        ])
                    })
                    .collect(),
            ),
        ),
        ("lattice", Value::String(descriptor.lattice().to_owned())),
        (
            "module_file",
            Value::String(descriptor.module_file().to_owned()),
        ),
        ("package", Value::String(descriptor.package().to_owned())),
        (
            "profiles",
            Value::Array(
                descriptor
                    .profiles()
                    .iter()
                    .cloned()
                    .map(Value::String)
                    .collect(),
            ),
        ),
        ("version", Value::String(descriptor.version().to_owned())),
    ]);
    object([
        ("descriptor", descriptor_value),
        ("package_id", Value::String(package.identity().to_string())),
        (
            "verified_files",
            Value::Array(
                package
                    .verified_files()
                    .iter()
                    .map(|file| {
                        let sha = descriptor
                            .files()
                            .iter()
                            .find(|candidate| candidate.path() == file.path())
                            .unwrap()
                            .sha256();
                        object([
                            ("bytes", inline_bytes(file.bytes())),
                            ("path", Value::String(file.path().to_owned())),
                            ("sha256", Value::String(sha.to_owned())),
                        ])
                    })
                    .collect(),
            ),
        ),
    ])
}

fn record_value(manifest: &Value, locator: &str) -> Value {
    if let Some(record) = manifest["package_records"].get(locator) {
        let mut record = record.clone();
        for file in record["verified_files"].as_array_mut().unwrap() {
            let reference = file
                .as_object_mut()
                .unwrap()
                .remove("bytes_ref")
                .unwrap()
                .as_str()
                .unwrap()
                .to_owned();
            file.as_object_mut()
                .unwrap()
                .insert("bytes".to_owned(), constant_inline(manifest, &reference));
        }
        return record;
    }
    let prefix = "generated_package_families.chain255.records/";
    let index = locator
        .strip_prefix(prefix)
        .unwrap_or_else(|| panic!("unknown package locator {locator}"))
        .parse::<usize>()
        .expect("generated record index");
    let source = &manifest["generated_package_families"]["chain255"]["records"][index];
    object([
        ("descriptor", source["descriptor"].clone()),
        ("package_id", source["package_id"].clone()),
        (
            "verified_files",
            Value::Array(vec![object([
                (
                    "bytes",
                    object([
                        ("encoding", Value::String("lowercase_hex".to_owned())),
                        ("hex", source["module_hex"].clone()),
                    ]),
                ),
                ("path", source["descriptor"]["module_file"].clone()),
                ("sha256", source["module_sha256"].clone()),
            ])]),
        ),
    ])
}

mod scanned_source_oracle {
    use super::{Map, ScannedSource, Value, scanned_source_projection};

    pub(super) trait MaterializationSource {
        fn value(&self) -> &Value;
    }

    pub(super) struct PreResolveProjection {
        value: Value,
    }

    impl PreResolveProjection {
        pub(super) fn from_scanned(scanned: &ScannedSource) -> Self {
            Self {
                value: scanned_source_projection(scanned),
            }
        }
    }

    impl MaterializationSource for PreResolveProjection {
        fn value(&self) -> &Value {
            &self.value
        }
    }

    pub(super) struct ManifestWrongProjection<'a> {
        value: &'a Value,
    }

    impl<'a> ManifestWrongProjection<'a> {
        pub(super) fn from_operation(operation: &'a Map<String, Value>) -> Self {
            assert_eq!(operation["wrong_scanned_source_field"], "scanned_source");
            Self {
                value: &operation["wrong_scanned_source"],
            }
        }
    }

    impl MaterializationSource for ManifestWrongProjection<'_> {
        fn value(&self) -> &Value {
            self.value
        }
    }
}

fn scanned_source_projection(scanned: &ScannedSource) -> Value {
    object([
        (
            "active_profile",
            scanned.digested_source().defaulted_source().as_value()["profile"].clone(),
        ),
        (
            "blueprint_digest",
            Value::String(scanned.digested_source().blueprint_digest().to_string()),
        ),
        (
            "defaulted_root",
            scanned
                .digested_source()
                .defaulted_source()
                .as_value()
                .clone(),
        ),
        (
            "packages",
            Value::Array(
                scanned
                    .packages()
                    .iter()
                    .map(actual_package_value)
                    .collect(),
            ),
        ),
    ])
}

fn materialize_output<S: scanned_source_oracle::MaterializationSource>(
    expected: &Value,
    input_ref: &str,
    manifest: &Value,
    scanned_source: &S,
) -> Value {
    let mut output = expected.clone();
    materialize_node(&mut output, input_ref, manifest, scanned_source.value());
    output
}

fn materialize_node(value: &mut Value, input_ref: &str, manifest: &Value, scanned_source: &Value) {
    match value {
        Value::Array(values) => {
            for child in values {
                materialize_node(child, input_ref, manifest, scanned_source);
            }
        }
        Value::Object(object) => {
            if object.contains_key("scanned_source_ref") {
                let reference = object
                    .remove("scanned_source_ref")
                    .unwrap()
                    .as_str()
                    .unwrap()
                    .to_owned();
                assert_eq!(reference, input_ref);
                object.insert("scanned_source".to_owned(), scanned_source.clone());
            }
            if object.contains_key("record_ref") {
                let locator = object
                    .remove("record_ref")
                    .unwrap()
                    .as_str()
                    .unwrap()
                    .to_owned();
                object.insert("record".to_owned(), record_value(manifest, &locator));
            }
            if object.contains_key("retained_bytes_ref") {
                let locator = object
                    .remove("retained_bytes_ref")
                    .unwrap()
                    .as_str()
                    .unwrap()
                    .to_owned();
                object.insert(
                    "retained_bytes".to_owned(),
                    constant_inline(manifest, &locator),
                );
            }
            if object.contains_key("parsed_module_ref") {
                let locator = object
                    .remove("parsed_module_ref")
                    .unwrap()
                    .as_str()
                    .unwrap()
                    .to_owned();
                object.insert(
                    "parsed_module".to_owned(),
                    module_locator(manifest, &locator, "parsed_value"),
                );
            }
            if object.contains_key("imports_ref") {
                let locator = object
                    .remove("imports_ref")
                    .unwrap()
                    .as_str()
                    .unwrap()
                    .to_owned();
                object.insert(
                    "imports".to_owned(),
                    module_locator(manifest, &locator, "imports"),
                );
            }
            if object.contains_key("input_ref")
                && object.contains_key("package_decisions")
                && object.contains_key("unreferenced_entries")
            {
                let locator = object.remove("input_ref").unwrap();
                let bytes = locator.as_str().map_or(Value::Null, |reference| {
                    let bytes_ref = manifest["lock_inputs"][reference]["bytes_ref"]
                        .as_str()
                        .unwrap();
                    constant_inline(manifest, bytes_ref)
                });
                object.insert("input".to_owned(), bytes);
            }
            for child in object.values_mut() {
                materialize_node(child, input_ref, manifest, scanned_source);
            }
        }
        _ => {}
    }
}

fn module_locator(manifest: &Value, locator: &str, terminal: &str) -> Value {
    let mut parts = locator.split('.');
    assert_eq!(parts.next(), Some("module_oracles"));
    let name = parts.next().expect("module oracle name");
    assert_eq!(parts.next(), Some(terminal));
    assert_eq!(parts.next(), None);
    manifest["module_oracles"][name][terminal].clone()
}

fn constant_inline(manifest: &Value, locator: &str) -> Value {
    let constant = &manifest["byte_constants"][locator];
    object([
        ("encoding", Value::String("lowercase_hex".to_owned())),
        ("hex", constant["hex"].clone()),
    ])
}

fn decode_constant(manifest: &Value, locator: &str) -> Vec<u8> {
    decode_hex(
        manifest["byte_constants"][locator]["hex"]
            .as_str()
            .expect("constant hex"),
    )
}

fn decode_inline(value: &Value) -> Vec<u8> {
    assert_eq!(value["encoding"], "lowercase_hex");
    decode_hex(value["hex"].as_str().expect("inline hex"))
}

fn decode_hex(value: &str) -> Vec<u8> {
    assert_eq!(value.len() % 2, 0);
    value
        .as_bytes()
        .chunks_exact(2)
        .map(|pair| (hex_digit(pair[0]) << 4) | hex_digit(pair[1]))
        .collect()
}

fn hex_digit(value: u8) -> u8 {
    match value {
        b'0'..=b'9' => value - b'0',
        b'a'..=b'f' => value - b'a' + 10,
        _ => panic!("invalid lowercase hex"),
    }
}

fn inline_bytes(bytes: &[u8]) -> Value {
    const HEX: &[u8; 16] = b"0123456789abcdef";
    let mut text = String::with_capacity(bytes.len() * 2);
    for byte in bytes {
        text.push(char::from(HEX[usize::from(byte >> 4)]));
        text.push(char::from(HEX[usize::from(byte & 0x0f)]));
    }
    object([
        ("encoding", Value::String("lowercase_hex".to_owned())),
        ("hex", Value::String(text)),
    ])
}

fn erase_source_paths(mut value: Value) -> Value {
    fn visit(value: &mut Value) {
        match value {
            Value::Array(values) => {
                for child in values {
                    visit(child);
                }
            }
            Value::Object(object) => {
                let mut keys = object.keys().cloned().collect::<Vec<_>>();
                keys.sort_by(|left, right| left.as_bytes().cmp(right.as_bytes()));
                for key in keys {
                    let child = object.get_mut(&key).unwrap();
                    if key == "source_path" {
                        if let Some(path) = child.as_str() {
                            *child = Value::String(erase_import_index(path));
                        }
                    } else {
                        visit(child);
                    }
                }
            }
            _ => {}
        }
    }
    visit(&mut value);
    value
}

fn erase_import_index(path: &str) -> String {
    let Some((prefix, pointer)) = path.split_once('#') else {
        return path.to_owned();
    };
    if pointer.contains('#') {
        return path.to_owned();
    }
    let mut raw = pointer.split('/').map(str::to_owned).collect::<Vec<_>>();
    let decoded = raw
        .iter()
        .map(|token| token.replace("~1", "/").replace("~0", "~"))
        .collect::<Vec<_>>();
    for index in 0..decoded.len().saturating_sub(1) {
        if decoded[index] == "imports" && minimal_decimal(&decoded[index + 1]) {
            raw[index + 1] = "*".to_owned();
        }
    }
    format!("{prefix}#{}", raw.join("/"))
}

fn minimal_decimal(value: &str) -> bool {
    value == "0"
        || value
            .as_bytes()
            .first()
            .is_some_and(|byte| matches!(byte, b'1'..=b'9'))
            && value.as_bytes().iter().all(u8::is_ascii_digit)
}

fn projection_bytes(root: &Value, selector: &str) -> Vec<u8> {
    canonical_bytes(&Value::Array(
        project(root, selector).into_iter().cloned().collect(),
    ))
    .expect("projection canonical bytes")
}

fn project<'a>(root: &'a Value, selector: &str) -> Vec<&'a Value> {
    if selector == "$" {
        return vec![root];
    }
    assert!(selector.starts_with(|character: char| character.is_ascii_lowercase()));
    let bytes = selector.as_bytes();
    let mut position = 0;
    let mut projection = vec![root];
    while position < bytes.len() {
        if bytes[position..].starts_with(b"[*]") {
            let mut next = Vec::new();
            for value in projection {
                next.extend(value.as_array().expect("wildcard array"));
            }
            projection = next;
            position += 3;
            if position < bytes.len() && bytes[position] == b'.' {
                position += 1;
            }
            continue;
        }
        let start = position;
        while position < bytes.len()
            && (bytes[position].is_ascii_lowercase()
                || bytes[position].is_ascii_digit()
                || bytes[position] == b'_')
        {
            position += 1;
        }
        assert!(position > start, "valid member selector");
        let member = &selector[start..position];
        projection = projection
            .into_iter()
            .map(|value| {
                let object = value
                    .as_object()
                    .unwrap_or_else(|| panic!("{selector}: {member} requires object"));
                object
                    .get(member)
                    .or_else(|| member.strip_suffix("_ref").and_then(|key| object.get(key)))
                    .unwrap_or_else(|| panic!("{selector}: missing member {member}"))
            })
            .collect();
        if position < bytes.len() && bytes[position] == b'.' {
            position += 1;
        }
    }
    projection
}

fn string_array(value: &Value) -> Vec<&str> {
    value
        .as_array()
        .expect("string array")
        .iter()
        .map(|value| value.as_str().expect("string"))
        .collect()
}

fn name(value: &str) -> SnapshotName {
    SnapshotName::unicode(value)
}

fn entry(name_value: &str, node: SnapshotNode) -> SnapshotEntry {
    SnapshotEntry::new(name(name_value), node)
}

fn directory(children: Vec<SnapshotEntry>) -> SnapshotNode {
    SnapshotNode::directory(children)
}

fn regular(bytes: Vec<u8>) -> SnapshotNode {
    SnapshotNode::regular(bytes)
}

fn object<const N: usize>(entries: [(&str, Value); N]) -> Value {
    Value::Object(
        entries
            .into_iter()
            .map(|(key, value)| (key.to_owned(), value))
            .collect(),
    )
}
