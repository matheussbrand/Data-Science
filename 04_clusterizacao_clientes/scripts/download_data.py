"""Baixa o dataset Mall Customers (segmentação de clientes em shopping)."""
import urllib.request
from pathlib import Path

URL = (
    "https://raw.githubusercontent.com/tirthajyoti/"
    "Machine-Learning-with-Python/master/Datasets/Mall_Customers.csv"
)
OUT = Path(__file__).resolve().parents[1] / "data" / "mall_customers.csv"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        print(f"Dataset já existe: {OUT}")
        return

    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    OUT.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    print(f"Dataset salvo: {OUT}")


if __name__ == "__main__":
    main()
