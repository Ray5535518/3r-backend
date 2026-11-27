import pandas as pd


def summarize_devices(csv_path: str) -> pd.Series:
    df = pd.read_csv(csv_path)
    return df.groupby("device")["daily_count"].mean()
