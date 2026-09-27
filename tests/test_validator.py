from pathlib import Path

from tapetide_qa.validator import load_capture, validate_capture


def test_sample_capture_flags_mixed_periods():
    path = Path(__file__).parents[1] / "examples" / "sample_capture.json"
    data = load_capture(path)
    errors = validate_capture(data)
    assert "TPQ-TIME-002:mixed-periods" in errors


def test_valid_capture_passes():
    payload = {
        "test_id": "OK-001",
        "observed_at_ist": "2026-09-27T10:00:00+05:30",
        "question": "Compare two companies on FY2026 revenue.",
        "expected": {"same_reporting_basis": True, "period_visible": True, "units_visible": True},
        "actual": {"period_a": "FY2026", "period_b": "FY2026", "period_visible": True, "units_visible": True},
        "verification": {"status": "match"},
        "classification": [],
        "severity": "NONE",
        "confidence": "high",
        "recommended_fix": "None",
    }
    assert validate_capture(payload) == []
