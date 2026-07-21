import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_success_criterion_1():
    """
    Success criterion 1: /app/report.json exists and contains one valid JSON
    object with exactly the three required keys.
    """
    assert REPORT_PATH.is_file(), "Missing /app/report.json"

    try:
        data = load_report()
    except json.JSONDecodeError as exc:
        raise AssertionError("report.json is not valid JSON") from exc

    assert isinstance(data, dict), "The report must be a JSON object"
    assert set(data) == EXPECTED_KEYS, (
        "The report must contain exactly total_requests, unique_ips, and top_path"
    )


def test_success_criterion_2():
    """
    Success criterion 2: total_requests is the integer number of non-empty
    access-log lines.
    """
    data = load_report()
    assert type(data["total_requests"]) is int
    assert data["total_requests"] == 6


def test_success_criterion_3():
    """
    Success criterion 3: unique_ips is the integer number of distinct client
    IP addresses.
    """
    data = load_report()
    assert type(data["unique_ips"]) is int
    assert data["unique_ips"] == 3


def test_success_criterion_4():
    """
    Success criterion 4: top_path is the string containing the most frequently
    requested path.
    """
    data = load_report()
    assert type(data["top_path"]) is str
    assert data["top_path"] == "/index.html"
