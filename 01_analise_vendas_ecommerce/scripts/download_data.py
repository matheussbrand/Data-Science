"""Baixa o dataset Online Retail (UCI) — vendas reais de e-commerce."""
import io
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
OUT = Path(__file__).resolve().parents[1] / "data" / "online_retail.xlsx"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        print(f"Dataset já existe: {OUT}")
        return

    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    archive = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(req, timeout=120).read()))
    OUT.write_bytes(archive.read("Online Retail.xlsx"))
    print(f"Dataset salvo: {OUT}")


if __name__ == "__main__":
    main()
