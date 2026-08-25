from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
XLSX = DATA_DIR / "online_retail.xlsx"
CSV = DATA_DIR / "online_retail.csv"


def load_data() -> pd.DataFrame:
    if not XLSX.exists() and not CSV.exists():
        raise FileNotFoundError(
            "Dataset não encontrado. Execute: python scripts/download_data.py"
        )

    if CSV.exists():
        raw = pd.read_csv(CSV, parse_dates=["InvoiceDate"])
    else:
        raw = pd.read_excel(XLSX, parse_dates=["InvoiceDate"])
        raw.to_csv(CSV, index=False)

    raw = raw.dropna(subset=["Quantity", "UnitPrice"])
    raw = raw[(raw["Quantity"] > 0) & (raw["UnitPrice"] > 0)]

    df = pd.DataFrame({
        "data": raw["InvoiceDate"].dt.normalize(),
        "categoria": raw["Description"].fillna("Sem descrição").str[:40],
        "regiao": raw["Country"],
        "quantidade": raw["Quantity"].astype(int),
        "preco": raw["UnitPrice"].round(2),
    })
    df["receita"] = (df["quantidade"] * df["preco"]).round(2)
    return df


df = load_data()

print("\n=== Dataset: Online Retail (UCI) ===")
print(f"Registros: {len(df):,} | Período: {df['data'].min().date()} a {df['data'].max().date()}")

print("\n=== KPIs ===")
print(f"Receita total: £ {df['receita'].sum():,.2f}")
print(f"Ticket médio: £ {df['receita'].mean():,.2f}")
print(f"Pedidos (linhas): {len(df):,}")

print("\n=== Top 10 categorias por receita ===")
top_cat = (
    df.groupby("categoria")["receita"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_cat)

mensal = df.assign(mes=df["data"].dt.to_period("M")).groupby("mes")["receita"].sum()
mensal.plot(figsize=(10, 5), title="Receita mensal — Online Retail")
plt.ylabel("Receita (£)")
plt.tight_layout()
plt.savefig("receita_mensal.png", dpi=150)
plt.close()

plot_df = df.groupby("categoria", as_index=False)["receita"].sum().nlargest(10, "receita")
plt.figure(figsize=(10, 5))
sns.barplot(data=plot_df, x="categoria", y="receita")
plt.title("Top 10 produtos por receita")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("receita_categoria.png", dpi=150)
plt.close()

print("\nAnálise concluída. Gráficos salvos na pasta atual.")
