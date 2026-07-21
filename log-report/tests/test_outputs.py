import json
from pathlib import Path

REPORT = Path("/app/report.json")
LOG = Path("/app/access.log")


def _load():
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Criterion: the agent wrote its findings to /app/report.json."""
    assert REPORT.exists(), "no /app/report.json found"


def test_report_is_valid_json_object_with_exact_keys():
    """Criterion: the report is valid JSON with exactly the keys total_requests, unique_ips, top_path."""
    data = _load()
    assert isinstance(data, dict), "report.json must contain a JSON object"
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        f"unexpected keys: {sorted(data.keys())}"
    )


def test_total_requests_correct():
    """Criterion 1: total_requests is the number of non-empty log lines (6)."""
    data = _load()
    assert data["total_requests"] == 6, f"total_requests={data['total_requests']!r}, expected 6"


def test_unique_ips_correct():
    """Criterion 2: unique_ips is the number of distinct client IPs (3)."""
    data = _load()
    assert data["unique_ips"] == 3, f"unique_ips={data['unique_ips']!r}, expected 3"


def test_top_path_correct():
    """Criterion 3: top_path is the most-requested path (/index.html, strictly most frequent)."""
    data = _load()
    assert data["top_path"] == "/index.html", f"top_path={data['top_path']!r}, expected '/index.html'"


def test_input_log_unmodified():
    """Criterion: /app/access.log was not modified (6 lines, original first line intact)."""
    lines = [l for l in LOG.read_text().splitlines() if l.strip()]
    assert len(lines) == 6, "access.log was modified"
    assert lines[0].startswith('192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html'), (
        "access.log content changed"
    )
