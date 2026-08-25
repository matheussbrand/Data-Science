import csv
import io
import json
import time
import urllib.request
import zipfile
from pathlib import Path

from kafka import KafkaProducer

URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
DATA = Path(__file__).resolve().parents[1] / "data" / "transactions.csv"


def ensure_data():
    if DATA.exists():
        return

    DATA.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    archive = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(req, timeout=120).read()))

    import pandas as pd

    df = pd.read_excel(io.BytesIO(archive.read("Online Retail.xlsx")))
    df = df.dropna(subset=["Quantity", "UnitPrice", "CustomerID"])
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].head(100)

    with DATA.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["event_id", "customer_id", "amount"])
        for i, row in enumerate(df.itertuples(), start=1):
            w.writerow([i, int(row.CustomerID), round(float(row.Quantity * row.UnitPrice), 2)])


ensure_data()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode(),
)

with DATA.open(encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        event = {
            "event_id": int(row["event_id"]),
            "customer_id": int(row["customer_id"]),
            "amount": float(row["amount"]),
        }
        producer.send("orders", event)
        time.sleep(0.2)

producer.flush()
print(f"Eventos enviados a partir de {DATA}")
