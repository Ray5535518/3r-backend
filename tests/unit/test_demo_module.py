"""Unit tests for the summarize_devices function."""

from pathlib import Path

import pytest

from example.demo_module import summarize_devices


def test_summarize_devices(tmp_path: Path) -> None:
    """Verify that mean daily counts are computed accurately per device."""
    csv_file = tmp_path / "devices.csv"
    csv_file.write_text(
        "device,daily_count\nDEV-A,170\nDEV-A,178\nDEV-B,210\n",
        encoding="utf-8",
    )

    result = summarize_devices(str(csv_file))

    assert result["DEV-A"] == pytest.approx(174.0)
    assert result["DEV-B"] == pytest.approx(210.0)
