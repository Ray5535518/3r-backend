"""Integration tests for the example CLI."""

from pathlib import Path

from click.testing import CliRunner

from example.scripts.example_script import example_cli


def test_example_cli_integration(tmp_path: Path) -> None:
    """Verify that the CLI outputs expected mean counts from a CSV file."""
    csv_file = tmp_path / "devices.csv"
    csv_file.write_text(
        "device,daily_count\nDEV-A,170\nDEV-A,178\nDEV-B,210\n",
        encoding="utf-8",
    )

    runner = CliRunner()
    result = runner.invoke(example_cli, ["--input", str(csv_file)])

    assert result.exit_code == 0
    assert "DEV-A\t174.00" in result.output
    assert "DEV-B\t210.00" in result.output
