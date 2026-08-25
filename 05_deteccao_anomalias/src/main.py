from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest

DATA = Path(__file__).resolve().parents[1] / "data" / "creditcard_sample.csv"


def load_data() -> pd.DataFrame:
    if not DATA.exists():
        raise FileNotFoundError(
            "Dataset não encontrado. Execute: python scripts/download_data.py"
        )

    raw = pd.read_csv(DATA)
    return pd.DataFrame({
        "valor": raw["Amount"].abs(),
        "hora": (raw["Time"] // 3600 % 24).astype(int),
        "distancia_km": raw["V1"].abs() * 10,
    })


df = load_data()

print("\n=== Dataset: Credit Card Fraud Detection (amostra OpenML) ===")
print(f"Transações: {len(df):,}")

model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42,
)

features = ["valor", "hora", "distancia_km"]
df["anomalia"] = model.fit_predict(df[features])
df["score"] = model.decision_function(df[features])

suspeitas = df[df["anomalia"] == -1].sort_values("score")
print("Transações sinalizadas:", len(suspeitas))
print(suspeitas.head(10))
