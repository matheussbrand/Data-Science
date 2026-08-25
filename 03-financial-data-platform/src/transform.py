import pandas as pd
df=pd.read_json("data/raw/fx.json")
print("API carregada. Transforme os registros em uma tabela fato de câmbio antes da carga.")
