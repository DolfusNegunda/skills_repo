"""Validate an LLM's JSON output against a JSON-Schema-subset file.

The determinism gate for structured output: an LLM that "returns JSON" fails in
predictable ways (invalid JSON, markdown fences, missing required fields, wrong
types, enum drift, extra keys). This checks a produced JSON document against an
expected schema, prints machine-readable errors, and exits non-zero so the caller
can feed the errors back and retry — the produce -> validate -> fix loop.

Stdlib only (no jsonschema dependency). Supports a practical JSON Schema subset:
  type (object/array/string/number/integer/boolean/null or a list of them),
  properties, required, items, enum, additionalProperties (bool).

Usage:
    python scripts/validate_json_output.py output.json schema.json

The output file may be wrapped in ```json ... ``` fences or have surrounding prose;
this strips a fenced block if present, else tries to locate the first JSON value.
"""
import json
import re
import sys
from pathlib import Path

TYPES = {
    "object": dict, "array": list, "string": str, "number": (int, float),
    "integer": int, "boolean": bool, "null": type(None),
}


def extract_json(text):
    """Return parsed JSON from raw model output, tolerating fences/prose."""
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    candidate = fence.group(1).strip() if fence else text.strip()
    try:
        return json.loads(candidate), None
    except json.JSONDecodeError as e:
        # Last resort: first {...} or [...] span.
        m = re.search(r"(\{.*\}|\[.*\])", candidate, re.S)
        if m:
            try:
                return json.loads(m.group(1)), None
            except json.JSONDecodeError:
                pass
        return None, f"not valid JSON: {e}"


def type_ok(value, spec_type):
    types = spec_type if isinstance(spec_type, list) else [spec_type]
    for t in types:
        py = TYPES.get(t)
        if py is None:
            continue
        # bool is a subclass of int; keep them distinct.
        if t == "integer" and isinstance(value, bool):
            continue
        if t == "number" and isinstance(value, bool):
            continue
        if isinstance(value, py):
            return True
    return False


def validate(value, schema, path, errors):
    stype = schema.get("type")
    if stype and not type_ok(value, stype):
        errors.append(f"{path or '<root>'}: expected type {stype}, got {type(value).__name__}")
        return  # further checks assume the type held
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path or '<root>'}: value {value!r} not in enum {schema['enum']}")
    if isinstance(value, dict):
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path or '<root>'}: missing required key '{req}'")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for k in value:
                if k not in props:
                    errors.append(f"{path or '<root>'}: unexpected key '{k}'")
        for k, subschema in props.items():
            if k in value:
                validate(value[k], subschema, f"{path}.{k}" if path else k, errors)
    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            validate(item, schema["items"], f"{path}[{i}]", errors)


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: python scripts/validate_json_output.py <output.json> <schema.json>")
    out_path, schema_path = Path(sys.argv[1]), Path(sys.argv[2])
    for p in (out_path, schema_path):
        if not p.exists():
            sys.exit(f"file not found: {p}")

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data, parse_err = extract_json(out_path.read_text(encoding="utf-8"))

    errors = []
    if parse_err:
        errors.append(parse_err)
    else:
        validate(data, schema, "", errors)

    report = {
        "file": str(out_path),
        "status": "OK" if not errors else "FAILED",
        "errors": errors,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
