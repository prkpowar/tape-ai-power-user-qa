from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED = [
    "test_id",
    "observed_at_ist",
    "question",
    "expected",
    "actual",
    "verification",
    "classification",
    "severity",
    "confidence",
    "recommended_fix",
]

VALID_SEVERITIES = {"P0", "P1", "P2", "P3", "NONE"}
VALID_CONFIDENCE = {"high", "medium", "low"}


def load_capture(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Capture must be a JSON object")
    return data


def validate_capture(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"MISSING:{key}")

    if data.get("severity") not in VALID_SEVERITIES:
        errors.append("INVALID:severity")
    if str(data.get("confidence", "")).lower() not in VALID_CONFIDENCE:
        errors.append("INVALID:confidence")
    if not isinstance(data.get("classification"), list):
        errors.append("INVALID:classification")
    if not isinstance(data.get("question"), str) or not data.get("question", "").strip():
        errors.append("INVALID:question")

    expected = data.get("expected", {})
    actual = data.get("actual", {})
    if isinstance(expected, dict) and isinstance(actual, dict):
        if expected.get("same_reporting_basis") is True:
            pa = actual.get("period_a")
            pb = actual.get("period_b")
            if pa and pb and pa != pb:
                errors.append("TPQ-TIME-002:mixed-periods")
        if expected.get("period_visible") is True and actual.get("period_visible") is False:
            errors.append("TPQ-UX-001:period-hidden")
        if expected.get("units_visible") is True and actual.get("units_visible") is False:
            errors.append("TPQ-UX-002:unit-hidden")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m tapetide_qa.validator path/to/capture.json")
        return 2
    data = load_capture(sys.argv[1])
    errors = validate_capture(data)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS")
    print(f"Test: {data['test_id']}")
    print(f"Severity: {data['severity']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
