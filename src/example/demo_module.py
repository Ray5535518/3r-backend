"""Module for summarizing device counts from CSV files."""

import pandas as pd


def summarize_devices(csv_path: str) -> pd.Series:
    """Calculate the mean daily count per device from a CSV file."""
    df = pd.read_csv(csv_path)
    return df.groupby("device")["daily_count"].mean()
