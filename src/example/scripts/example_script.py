"""Command-line interface for the example package."""

import click

from example.demo_module import summarize_devices


@click.command()
@click.option("--input", "input_path", required=True, help="Path to device CSV file.")
def example_cli(input_path: str) -> None:
    """Print the mean daily count for each device."""
    summary = summarize_devices(input_path)
    for device, mean_val in summary.items():
        click.echo(f"{device}\t{mean_val:.2f}")
