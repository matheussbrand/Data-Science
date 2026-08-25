import json, urllib.request
from pathlib import Path

URL="https://api.frankfurter.app/latest?from=USD&to=BRL"
data=json.load(urllib.request.urlopen(URL))
Path("data/raw").mkdir(parents=True,exist_ok=True)
Path("data/raw/fx.json").write_text(json.dumps(data,indent=2))
print(data)
