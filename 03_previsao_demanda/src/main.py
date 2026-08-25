from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

DATA = Path(__file__).resolve().parents[1] / "data" / "daily_min_temperatures.csv"


def load_data() -> pd.DataFrame:
    if not DATA.exists():
        raise FileNotFoundError(
            "Dataset não encontrado. Execute: python scripts/download_data.py"
        )

    raw = pd.read_csv(DATA, parse_dates=["Date"])
    df = pd.DataFrame({"data": raw["Date"], "demanda": raw["Temp"]})
    df["dia_semana"] = df["data"].dt.dayofweek
    df["mes"] = df["data"].dt.month
    df["lag_1"] = df["demanda"].shift(1)
    df["lag_7"] = df["demanda"].shift(7)
    df["media_7"] = df["demanda"].shift(1).rolling(7).mean()
    return df.dropna()


df = load_data()

print("\n=== Dataset: Daily Minimum Temperatures (Melbourne) ===")
print(f"Registros: {len(df):,} | Período: {df['data'].min().date()} a {df['data'].max().date()}")

features = ["dia_semana", "mes", "lag_1", "lag_7", "media_7"]
cut = int(len(df) * 0.8)

train, test = df.iloc[:cut], df.iloc[cut:]
model = RandomForestRegressor(n_estimators=250, random_state=42, n_jobs=-1)
model.fit(train[features], train["demanda"])

pred = model.predict(test[features])

print("MAE:", round(mean_absolute_error(test["demanda"], pred), 2))
print("RMSE:", round(mean_squared_error(test["demanda"], pred) ** 0.5, 2))

plt.figure(figsize=(12, 5))
plt.plot(test["data"], test["demanda"], label="Real")
plt.plot(test["data"], pred, label="Previsão")
plt.legend()
plt.title("Previsão de temperatura mínima diária")
plt.tight_layout()
plt.savefig("previsao_demanda.png", dpi=150)
plt.close()
