"""Baixa amostra do dataset Credit Card Fraud Detection (OpenML #1597)."""
from pathlib import Path

import pandas as pd
from sklearn.datasets import fetch_openml

OUT = Path(__file__).resolve().parents[1] / "data" / "creditcard_sample.csv"
SAMPLE_SIZE = 5000


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        print(f"Dataset já existe: {OUT}")
        return

    print("Baixando Credit Card Fraud Detection (OpenML)...")
    data = fetch_openml(data_id=1597, as_frame=True, parser="auto")
    df = data.frame.sample(n=SAMPLE_SIZE, random_state=42)
    df.to_csv(OUT, index=False)
    print(f"Dataset salvo: {OUT} ({len(df):,} transações)")


if __name__ == "__main__":
    main()
