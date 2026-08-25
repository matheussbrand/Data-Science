import requests
from pathlib import Path

URL="https://brasilapi.com.br/api/ibge/municipios/v1/RJ"
r=requests.get(URL,timeout=30)
r.raise_for_status()
Path("data/raw").mkdir(parents=True,exist_ok=True)
Path("data/raw/municipios.json").write_text(r.text)
print(f"Registros recebidos: {len(r.json())}")
