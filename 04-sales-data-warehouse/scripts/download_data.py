"""Prepara sales.csv a partir do dataset Online Retail (UCI)."""
import csv
import io
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
OUT = Path(__file__).resolve().parents[1] / "data" / "raw" / "sales.csv"
MAX_ROWS = 3000


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        print(f"Dataset já existe: {OUT}")
        return

    print("Baixando Online Retail (UCI)...")
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    archive = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(req, timeout=120).read()))

    import pandas as pd

    df = pd.read_excel(io.BytesIO(archive.read("Online Retail.xlsx")))
    df = df.dropna(subset=["Quantity", "UnitPrice", "CustomerID"])
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].head(MAX_ROWS)

    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["order_id", "customer_id", "product_id", "order_date", "quantity", "unit_price"])
        for i, row in enumerate(df.itertuples(), start=1):
            w.writerow([
                i,
                int(row.CustomerID),
                hash(str(row.StockCode)) % 10000,
                row.InvoiceDate.date().isoformat(),
                int(row.Quantity),
                round(float(row.UnitPrice), 2),
            ])

    print(f"Dataset salvo: {OUT} ({len(df):,} linhas)")


if __name__ == "__main__":
    main()
