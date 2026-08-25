import pandas as pd

new=pd.read_csv("data/raw/products.csv")
new["collected_at"]=pd.Timestamp.utcnow()
new=new.drop_duplicates(["sku","competitor","collected_at"])
new.to_parquet("data/processed/price_history.parquet",index=False)
print(f"{len(new)} registros históricos preparados.")
