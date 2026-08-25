from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).resolve().parents[1] / "data" / "mall_customers.csv"


def load_data() -> pd.DataFrame:
    if not DATA.exists():
        raise FileNotFoundError(
            "Dataset não encontrado. Execute: python scripts/download_data.py"
        )

    raw = pd.read_csv(DATA)
    return pd.DataFrame({
        "idade": raw["Age"],
        "renda_anual_k": raw["Annual Income (k$)"],
        "score_gasto": raw["Spending Score (1-100)"],
    })


df = load_data()

print("\n=== Dataset: Mall Customers ===")
print(f"Clientes: {len(df):,}")

features = ["idade", "renda_anual_k", "score_gasto"]
X = StandardScaler().fit_transform(df[features])

model = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)

perfil = df.groupby("cluster")[features].mean().round(2)
print("\n=== Perfil médio dos clusters ===")
print(perfil)

plt.figure(figsize=(9, 6))
plt.scatter(df["renda_anual_k"], df["score_gasto"], c=df["cluster"], alpha=0.6)
plt.xlabel("Renda anual (k$)")
plt.ylabel("Score de gasto (1-100)")
plt.title("Segmentação de clientes — Mall Customers")
plt.tight_layout()
plt.savefig("clusters.png", dpi=150)
plt.close()
