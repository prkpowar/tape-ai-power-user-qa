from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required for catalog validation")
    raise SystemExit(2)

ID_RE = re.compile(r"^[A-Z]+-\d{3}$")
REQUIRED = {"id", "area", "prompt", "focus"}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_test_catalog.py test_cases/20_core_cases.yaml")
        return 2
    p = Path(sys.argv[1])
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("FAIL: catalog must be a YAML list")
        return 1
    seen = set()
    errors = []
    for i, case in enumerate(data, 1):
        if not isinstance(case, dict):
            errors.append(f"item {i}: not an object")
            continue
        missing = REQUIRED - case.keys()
        if missing:
            errors.append(f"item {i}: missing {sorted(missing)}")
        cid = case.get("id")
        if not isinstance(cid, str) or not ID_RE.fullmatch(cid):
            errors.append(f"item {i}: invalid id {cid!r}")
        elif cid in seen:
            errors.append(f"item {i}: duplicate id {cid}")
        else:
            seen.add(cid)
        if not isinstance(case.get("prompt"), str) or not case.get("prompt", "").strip():
            errors.append(f"item {i}: empty prompt")
        if not isinstance(case.get("focus"), list) or not case.get("focus"):
            errors.append(f"item {i}: focus must be a non-empty list")
    if errors:
        print("FAIL")
        for e in errors:
            print("-", e)
        return 1
    print(f"PASS: {len(data)} test cases validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
