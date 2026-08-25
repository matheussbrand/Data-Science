import json
import subprocess
import sys
import time
from pathlib import Path

from kafka import KafkaProducer

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_logs.jsonl"


def ensure_data():
    if DATA.exists():
        return
    script = Path(__file__).resolve().parent / "download_data.py"
    subprocess.run([sys.executable, str(script)], check=True)


ensure_data()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode(),
)

with DATA.open(encoding="utf-8") as f:
    for i, line in enumerate(f):
        event = json.loads(line)
        producer.send("application-logs", event)
        time.sleep(0.1)

producer.flush()
print(f"Logs enviados a partir de {DATA}")
