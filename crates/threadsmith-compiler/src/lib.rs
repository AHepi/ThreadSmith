#![forbid(unsafe_code)]

//! Restricted ThreadSmith YAML source projection.
//!
//! This crate owns only the PC2 boundary from UTF-8 YAML source to an
//! NFC-normalized, JSON-shaped value tree. It does not compile source or create
//! artifact identity, authority, manifests, package resolutions, or executable
//! output.

use core::fmt;
use saphyr_parser::{Event, Marker, Parser, ScalarStyle, Span};
use serde::Serialize;
use serde_json::{Map, Number, Value};
use std::collections::{BTreeMap, BTreeSet};
use unicode_normalization::UnicodeNormalization;

/// Stable PC2 source diagnostic.
///
/// Only these four fields are normative. Upstream parser messages are never
/// exposed through this API.
#[derive(Clone, Debug, Eq, PartialEq, Serialize)]
pub struct SourceDiagnostic {
    pub code: &'static str,
    pub path: String,
    pub line: Option<usize>,
    pub column: Option<usize>,
}

impl fmt::Display for SourceDiagnostic {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(formatter, "{} at {}", self.code, self.path)
    }
}

impl std::error::Error for SourceDiagnostic {}

/// Parse one PC2 Blueprint source document.
///
/// The returned value is a source projection, not a compiled or authoritative
/// artifact. Object keys and string values are NFC-normalized, arrays retain
/// source order, and absent optional root lists are injected as empty arrays.
///
/// # Errors
///
/// Returns the first deterministic diagnostic required by the frozen PC2
/// parser semantics.
pub fn parse_blueprint_source(source: &[u8]) -> Result<Value, SourceDiagnostic> {
    let source = validate_source_bytes(source)?;
    audit_yaml_features(source)?;
    let mut cursor = Cursor::new(source);

    cursor.expect_stream_start()?;
    cursor.expect_implicit_document_start()?;
    let root = cursor.parse_node(&Path::root())?;
    cursor.expect_implicit_document_end()?;
    cursor.expect_stream_end()?;

    validate_blueprint_root(root)
}

fn audit_yaml_features(source: &str) -> Result<(), SourceDiagnostic> {
    let mut cursor = Cursor::new(source);
    cursor.expect_stream_start()?;
    cursor.expect_implicit_document_start()?;
    cursor.audit_node(&Path::root())?;
    cursor.expect_implicit_document_end()?;
    cursor.expect_stream_end()
}

#[derive(Clone, Copy, Debug)]
struct Position {
    line: usize,
    column: usize,
}

impl Position {
    fn from_marker(marker: Marker) -> Self {
        Self {
            line: marker.line(),
            column: marker.col() + 1,
        }
    }
}

#[derive(Clone, Debug)]
struct LocatedNode {
    value: Node,
    position: Position,
}

#[derive(Clone, Debug)]
enum Node {
    Null,
    Bool(bool),
    Number(Number),
    String(String),
    Sequence(Vec<LocatedNode>),
    Mapping(Vec<Entry>),
}

#[derive(Clone, Debug)]
struct Entry {
    key: String,
    key_position: Position,
    value: LocatedNode,
}

#[derive(Clone, Debug)]
struct Path(String);

impl Path {
    fn root() -> Self {
        Self(String::new())
    }

    fn key(&self, key: &str) -> Self {
        let escaped = key.replace('~', "~0").replace('/', "~1");
        Self(format!("{}/{}", self.0, escaped))
    }

    fn index(&self, index: usize) -> Self {
        Self(format!("{}/{}", self.0, index))
    }
}

struct Cursor<'source> {
    parser: Parser<'source, saphyr_parser::StrInput<'source>>,
    source: &'source str,
}

impl<'source> Cursor<'source> {
    fn new(source: &'source str) -> Self {
        Self {
            parser: Parser::new_from_str(source),
            source,
        }
    }

    fn next(&mut self, path: &Path) -> Result<(Event<'source>, Span), SourceDiagnostic> {
        match self.parser.next_event() {
            Some(Ok(event)) => Ok(event),
            Some(Err(error)) => Err(diagnostic_at_marker(
                "SOURCE_FORBIDDEN_YAML",
                path,
                *error.marker(),
            )),
            None => Err(diagnostic_without_position("SOURCE_FORBIDDEN_YAML", path)),
        }
    }

    fn expect_stream_start(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::StreamStart, _) => Ok(()),
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn expect_implicit_document_start(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::DocumentStart(false), _) => Ok(()),
            (Event::DocumentStart(true), span) => {
                let marker = first_directive_marker(self.source, span.start).unwrap_or(span.start);
                Err(diagnostic_at(
                    "SOURCE_FORBIDDEN_YAML",
                    &Path::root(),
                    marker,
                ))
            }
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn expect_implicit_document_end(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::DocumentEnd, span) => {
                if source_at_marker_starts_with(self.source, span.start, "...") {
                    Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        &Path::root(),
                        span.start,
                    ))
                } else {
                    Ok(())
                }
            }
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn expect_stream_end(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::StreamEnd, _) if self.parser.next_event().is_none() => Ok(()),
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn parse_node(&mut self, path: &Path) -> Result<LocatedNode, SourceDiagnostic> {
        let (event, span) = self.next(path)?;
        self.parse_event(event, span, path)
    }

    fn audit_node(&mut self, path: &Path) -> Result<(), SourceDiagnostic> {
        let (event, span) = self.next(path)?;
        self.audit_event(event, span, path)
    }

    fn audit_event(
        &mut self,
        event: Event<'source>,
        span: Span,
        path: &Path,
    ) -> Result<(), SourceDiagnostic> {
        match event {
            Event::Alias(_) => Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start)),
            Event::Scalar(_, style, anchor, tag) => {
                let marker =
                    node_metadata_marker(self.source, span.start, anchor != 0 || tag.is_some());
                reject_node_metadata(style, anchor, tag.is_some(), path, marker)
            }
            Event::SequenceStart(anchor, tag) => {
                if anchor != 0 || tag.is_some() {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                let mut index = 0;
                loop {
                    let (event, span) = self.next(path)?;
                    if matches!(event, Event::SequenceEnd) {
                        return Ok(());
                    }
                    self.audit_event(event, span, &path.index(index))?;
                    index += 1;
                }
            }
            Event::MappingStart(anchor, tag) => {
                if anchor != 0 || tag.is_some() {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                self.audit_mapping(path)
            }
            _ => Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start)),
        }
    }

    fn audit_mapping(&mut self, path: &Path) -> Result<(), SourceDiagnostic> {
        loop {
            let (event, span) = self.next(path)?;
            if matches!(event, Event::MappingEnd) {
                return Ok(());
            }
            if is_explicit_key(self.source, span.start) {
                return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
            }

            let value_path = match event {
                Event::Scalar(value, style, anchor, tag) => {
                    let marker =
                        node_metadata_marker(self.source, span.start, anchor != 0 || tag.is_some());
                    reject_node_metadata(style, anchor, tag.is_some(), path, marker)?;
                    let key: String = value.nfc().collect();
                    if style == ScalarStyle::Plain && key == "<<" {
                        return Err(diagnostic_at(
                            "SOURCE_FORBIDDEN_YAML",
                            &path.key("<<"),
                            span.start,
                        ));
                    }
                    path.key(&key)
                }
                Event::Alias(_) => {
                    return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
                }
                other => {
                    self.audit_event(other, span, path)?;
                    path.clone()
                }
            };
            self.audit_node(&value_path)?;
        }
    }

    fn parse_event(
        &mut self,
        event: Event<'source>,
        span: Span,
        path: &Path,
    ) -> Result<LocatedNode, SourceDiagnostic> {
        let position = Position::from_marker(span.start);
        let value = match event {
            Event::Alias(_) => {
                return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
            }
            Event::Scalar(value, style, anchor, tag) => {
                let metadata_marker =
                    node_metadata_marker(self.source, span.start, anchor != 0 || tag.is_some());
                reject_node_metadata(style, anchor, tag.is_some(), path, metadata_marker)?;
                parse_scalar(value.as_ref(), style, path, span.start)?
            }
            Event::SequenceStart(anchor, tag) => {
                if anchor != 0 || tag.is_some() {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                let mut values = Vec::new();
                loop {
                    let (event, span) = self.next(path)?;
                    if matches!(event, Event::SequenceEnd) {
                        break;
                    }
                    let item_path = path.index(values.len());
                    values.push(self.parse_event(event, span, &item_path)?);
                }
                Node::Sequence(values)
            }
            Event::MappingStart(anchor, tag) => {
                if anchor != 0 || tag.is_some() {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                Node::Mapping(self.parse_mapping(path)?)
            }
            _ => return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start)),
        };
        Ok(LocatedNode { value, position })
    }

    fn parse_mapping(&mut self, path: &Path) -> Result<Vec<Entry>, SourceDiagnostic> {
        let mut entries = Vec::new();
        let mut decoded_keys = BTreeSet::new();
        let mut normalized_keys = BTreeMap::<String, String>::new();

        loop {
            let (event, span) = self.next(path)?;
            if matches!(event, Event::MappingEnd) {
                return Ok(entries);
            }

            let (raw_key, key) = self.parse_key(event, span, path)?;
            let key_path = path.key(&key);
            if decoded_keys.contains(&raw_key) {
                return Err(diagnostic_at("SOURCE_DUPLICATE_KEY", &key_path, span.start));
            }
            if normalized_keys.contains_key(&key) {
                return Err(diagnostic_at("SOURCE_NFC_COLLISION", &key_path, span.start));
            }
            decoded_keys.insert(raw_key.clone());
            normalized_keys.insert(key.clone(), raw_key.clone());

            let value = self.parse_node(&key_path)?;
            entries.push(Entry {
                key,
                key_position: Position::from_marker(span.start),
                value,
            });
        }
    }

    fn parse_key(
        &self,
        event: Event<'source>,
        span: Span,
        path: &Path,
    ) -> Result<(String, String), SourceDiagnostic> {
        let Event::Scalar(value, style, anchor, tag) = event else {
            if matches!(event, Event::Alias(_)) {
                return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
            }
            return Err(diagnostic_at("SOURCE_NON_STRING_KEY", path, span.start));
        };

        let metadata_marker =
            node_metadata_marker(self.source, span.start, anchor != 0 || tag.is_some());
        reject_node_metadata(style, anchor, tag.is_some(), path, metadata_marker)?;
        if matches!(style, ScalarStyle::Literal | ScalarStyle::Folded)
            || is_explicit_key(self.source, span.start)
        {
            return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
        }

        let raw = parse_key_scalar(value.as_ref(), style, path, span.start)?;
        if style == ScalarStyle::Plain && raw == "<<" {
            return Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &path.key("<<"),
                span.start,
            ));
        }
        let normalized = raw.nfc().collect();
        Ok((raw, normalized))
    }
}

fn validate_source_bytes(source: &[u8]) -> Result<&str, SourceDiagnostic> {
    let source = std::str::from_utf8(source).map_err(|error| {
        let (line, column) = byte_position(source, error.valid_up_to());
        SourceDiagnostic {
            code: "SOURCE_INVALID_UTF8",
            path: String::new(),
            line: Some(line),
            column: Some(column),
        }
    })?;

    let mut line = 1;
    let mut column = 1;
    let mut characters = source.char_indices().peekable();
    while let Some((index, character)) = characters.next() {
        let forbidden = (index == 0 && character == '\u{feff}')
            || character == '\0'
            || (character == '\r' && !characters.peek().is_some_and(|(_, next)| *next == '\n'))
            || matches!(character, '\u{0001}'..='\u{0008}' | '\u{000b}' | '\u{000c}' | '\u{000e}'..='\u{001f}' | '\u{007f}'..='\u{009f}');
        if forbidden {
            return Err(SourceDiagnostic {
                code: "SOURCE_INVALID_UTF8",
                path: String::new(),
                line: Some(line),
                column: Some(column),
            });
        }
        if character == '\n' {
            line += 1;
            column = 1;
        } else if character != '\r' {
            column += 1;
        }
    }
    Ok(source)
}

fn byte_position(source: &[u8], offset: usize) -> (usize, usize) {
    let prefix = String::from_utf8_lossy(&source[..offset]);
    let line = prefix.bytes().filter(|byte| *byte == b'\n').count() + 1;
    let column = prefix
        .rsplit('\n')
        .next()
        .map_or(1, |tail| tail.chars().count() + 1);
    (line, column)
}

fn reject_node_metadata(
    style: ScalarStyle,
    anchor: usize,
    has_tag: bool,
    path: &Path,
    marker: Marker,
) -> Result<(), SourceDiagnostic> {
    if anchor != 0 || has_tag || matches!(style, ScalarStyle::Literal | ScalarStyle::Folded) {
        Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, marker))
    } else {
        Ok(())
    }
}

fn parse_scalar(
    source: &str,
    style: ScalarStyle,
    path: &Path,
    marker: Marker,
) -> Result<Node, SourceDiagnostic> {
    if has_forbidden_decoded_character(source) {
        return Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker));
    }
    if style != ScalarStyle::Plain {
        return Ok(Node::String(source.nfc().collect()));
    }
    match source {
        "null" => Ok(Node::Null),
        "true" => Ok(Node::Bool(true)),
        "false" => Ok(Node::Bool(false)),
        "0" => Ok(Node::Number(Number::from(0))),
        _ if is_decimal_integer(source) => parse_integer(source)
            .map(Node::Number)
            .ok_or_else(|| diagnostic_at("SOURCE_INVALID_SCALAR", path, marker)),
        _ if is_invalid_numeric_scalar(source) || source == "~" || source.is_empty() => {
            Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker))
        }
        _ => Ok(Node::String(source.nfc().collect())),
    }
}

fn parse_key_scalar(
    source: &str,
    style: ScalarStyle,
    path: &Path,
    marker: Marker,
) -> Result<String, SourceDiagnostic> {
    if has_forbidden_decoded_character(source) {
        return Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker));
    }
    if style != ScalarStyle::Plain {
        return Ok(source.to_owned());
    }
    if matches!(source, "null" | "true" | "false" | "0") {
        return Err(diagnostic_at("SOURCE_NON_STRING_KEY", path, marker));
    }
    if is_decimal_integer(source) {
        return if parse_integer(source).is_some() {
            Err(diagnostic_at("SOURCE_NON_STRING_KEY", path, marker))
        } else {
            Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker))
        };
    }
    if is_invalid_numeric_scalar(source) || source == "~" || source.is_empty() {
        return Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker));
    }
    Ok(source.to_owned())
}

fn is_decimal_integer(value: &str) -> bool {
    let digits = value.strip_prefix('-').unwrap_or(value);
    !digits.is_empty()
        && !digits.starts_with('0')
        && digits.bytes().all(|byte| byte.is_ascii_digit())
}

fn parse_integer(value: &str) -> Option<Number> {
    if value.starts_with('-') {
        value.parse::<i64>().ok().map(Number::from)
    } else {
        value.parse::<u64>().ok().map(Number::from)
    }
}

fn is_invalid_numeric_scalar(value: &str) -> bool {
    let lower = value.to_ascii_lowercase();
    if matches!(lower.as_str(), ".inf" | "+.inf" | "-.inf" | ".nan") {
        return true;
    }
    let unsigned = value.strip_prefix(['+', '-']).unwrap_or(value);
    if value.starts_with('+')
        && unsigned
            .bytes()
            .next()
            .is_some_and(|byte| byte.is_ascii_digit())
    {
        return true;
    }
    if unsigned.starts_with("0x")
        || unsigned.starts_with("0X")
        || unsigned.starts_with("0o")
        || unsigned.starts_with("0O")
    {
        return unsigned.len() > 2;
    }
    if unsigned.len() > 1
        && unsigned.starts_with('0')
        && unsigned.bytes().all(|byte| byte.is_ascii_digit())
    {
        return true;
    }
    if value == "-0" {
        return true;
    }
    let numeric_characters = unsigned.bytes().all(|byte| {
        byte.is_ascii_digit() || matches!(byte, b'.' | b'e' | b'E' | b'+' | b'-' | b'_')
    });
    numeric_characters
        && unsigned
            .bytes()
            .any(|byte| matches!(byte, b'.' | b'e' | b'E' | b'_'))
        && unsigned.bytes().any(|byte| byte.is_ascii_digit())
}

fn has_forbidden_decoded_character(value: &str) -> bool {
    value.chars().any(|character| {
        character == '\0'
            || matches!(character, '\u{0001}'..='\u{0008}' | '\u{000b}' | '\u{000c}' | '\u{000e}'..='\u{001f}' | '\u{007f}'..='\u{009f}')
    })
}

fn validate_blueprint_root(root: LocatedNode) -> Result<Value, SourceDiagnostic> {
    let Node::Mapping(entries) = root.value else {
        return Err(diagnostic_from_position(
            "SOURCE_ROOT_TYPE",
            &Path::root(),
            root.position,
        ));
    };

    for entry in &entries {
        if entry.key == "defaults" {
            return Err(diagnostic_from_position(
                "SOURCE_ILLEGAL_DEFAULT_OVERRIDE",
                &Path::root().key("defaults"),
                entry.key_position,
            ));
        }
    }

    const PERMITTED: [&str; 11] = [
        "profile",
        "module",
        "version",
        "purpose",
        "imports",
        "resources",
        "contracts",
        "units",
        "links",
        "policies",
        "scenarios",
    ];
    for entry in &entries {
        if !PERMITTED.contains(&entry.key.as_str()) {
            return Err(diagnostic_from_position(
                "SOURCE_UNKNOWN_KEY",
                &Path::root().key(&entry.key),
                entry.key_position,
            ));
        }
    }

    const REQUIRED: [&str; 4] = ["profile", "module", "version", "purpose"];
    for key in REQUIRED {
        if !entries.iter().any(|entry| entry.key == key) {
            return Err(diagnostic_without_position(
                "SOURCE_REQUIRED_KEY_MISSING",
                &Path::root().key(key),
            ));
        }
    }

    for key in REQUIRED {
        let entry = entries.iter().find(|entry| entry.key == key).unwrap();
        let Node::String(value) = &entry.value.value else {
            return Err(diagnostic_from_position(
                "SOURCE_INVALID_ROOT_VALUE",
                &Path::root().key(key),
                entry.value.position,
            ));
        };
        if value.is_empty() || (key == "profile" && value != "lattice-core-0.1") {
            return Err(diagnostic_from_position(
                "SOURCE_INVALID_ROOT_VALUE",
                &Path::root().key(key),
                entry.value.position,
            ));
        }
    }

    const OPTIONAL: [&str; 7] = [
        "imports",
        "resources",
        "contracts",
        "units",
        "links",
        "policies",
        "scenarios",
    ];
    for key in OPTIONAL {
        if let Some(entry) = entries.iter().find(|entry| entry.key == key)
            && !matches!(entry.value.value, Node::Sequence(_))
        {
            return Err(diagnostic_from_position(
                "SOURCE_INVALID_ROOT_VALUE",
                &Path::root().key(key),
                entry.value.position,
            ));
        }
    }

    validate_unit_kinds(&entries)?;

    let mut output = Map::new();
    for entry in entries {
        output.insert(entry.key, node_to_json(entry.value.value));
    }
    for key in OPTIONAL {
        output
            .entry(key.to_owned())
            .or_insert_with(|| Value::Array(Vec::new()));
    }
    Ok(Value::Object(output))
}

fn validate_unit_kinds(entries: &[Entry]) -> Result<(), SourceDiagnostic> {
    let Some(units) = entries.iter().find(|entry| entry.key == "units") else {
        return Ok(());
    };
    let Node::Sequence(items) = &units.value.value else {
        return Ok(());
    };
    const CORE_KINDS: [&str; 5] = ["program", "model", "gate", "controller", "broker"];
    for (index, item) in items.iter().enumerate() {
        let Node::Mapping(fields) = &item.value else {
            continue;
        };
        let Some(kind) = fields.iter().find(|entry| entry.key == "kind") else {
            continue;
        };
        let Node::String(value) = &kind.value.value else {
            continue;
        };
        if !CORE_KINDS.contains(&value.as_str()) {
            return Err(diagnostic_from_position(
                "PROFILE_UNSUPPORTED_UNIT_KIND",
                &Path::root().key("units").index(index).key("kind"),
                kind.value.position,
            ));
        }
    }
    Ok(())
}

fn node_to_json(node: Node) -> Value {
    match node {
        Node::Null => Value::Null,
        Node::Bool(value) => Value::Bool(value),
        Node::Number(value) => Value::Number(value),
        Node::String(value) => Value::String(value),
        Node::Sequence(values) => Value::Array(
            values
                .into_iter()
                .map(|value| node_to_json(value.value))
                .collect(),
        ),
        Node::Mapping(entries) => {
            let mut object = Map::new();
            for entry in entries {
                object.insert(entry.key, node_to_json(entry.value.value));
            }
            Value::Object(object)
        }
    }
}

fn diagnostic_at(code: &'static str, path: &Path, marker: Marker) -> SourceDiagnostic {
    diagnostic_from_position(code, path, Position::from_marker(marker))
}

fn diagnostic_at_marker(code: &'static str, path: &Path, marker: Marker) -> SourceDiagnostic {
    diagnostic_at(code, path, marker)
}

fn diagnostic_from_position(
    code: &'static str,
    path: &Path,
    position: Position,
) -> SourceDiagnostic {
    SourceDiagnostic {
        code,
        path: path.0.clone(),
        line: Some(position.line),
        column: Some(position.column),
    }
}

fn diagnostic_without_position(code: &'static str, path: &Path) -> SourceDiagnostic {
    SourceDiagnostic {
        code,
        path: path.0.clone(),
        line: None,
        column: None,
    }
}

fn source_at_marker_starts_with(source: &str, marker: Marker, needle: &str) -> bool {
    source
        .chars()
        .skip(marker.index())
        .take(needle.chars().count())
        .eq(needle.chars())
}

fn first_directive_marker(source: &str, before: Marker) -> Option<Marker> {
    let mut char_index = 0;
    for (line_index, line) in source.lines().enumerate() {
        if char_index >= before.index() {
            break;
        }
        if line.starts_with('%') {
            return Some(Marker::new(char_index, line_index + 1, 0));
        }
        char_index += line.chars().count() + 1;
    }
    None
}

fn is_explicit_key(source: &str, marker: Marker) -> bool {
    let prefix: String = source
        .lines()
        .nth(marker.line().saturating_sub(1))
        .unwrap_or_default()
        .chars()
        .take(marker.col())
        .collect();
    prefix.trim_end().ends_with('?')
}

fn node_metadata_marker(source: &str, marker: Marker, has_metadata: bool) -> Marker {
    if !has_metadata {
        return marker;
    }
    let line = source
        .lines()
        .nth(marker.line().saturating_sub(1))
        .unwrap_or_default();
    let prefix: String = line.chars().take(marker.col()).collect();
    let column = prefix
        .chars()
        .enumerate()
        .filter_map(|(index, character)| matches!(character, '&' | '!').then_some(index))
        .last();
    column.map_or(marker, |column| {
        Marker::new(
            marker.index().saturating_sub(marker.col() - column),
            marker.line(),
            column,
        )
    })
}
