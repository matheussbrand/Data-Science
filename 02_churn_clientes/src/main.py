from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = Path(__file__).resolve().parents[1] / "data" / "telco_churn.csv"


def load_data() -> tuple[pd.DataFrame, pd.Series]:
    if not DATA.exists():
        raise FileNotFoundError(
            "Dataset não encontrado. Execute: python scripts/download_data.py"
        )

    raw = pd.read_csv(DATA)
    raw["TotalCharges"] = pd.to_numeric(raw["TotalCharges"], errors="coerce")
    raw = raw.dropna(subset=["TotalCharges"])

    df = pd.DataFrame({
        "idade": raw["SeniorCitizen"].astype(int) * 20 + 30,
        "meses_cliente": raw["tenure"].astype(int),
        "tickets_suporte": (raw["TechSupport"] == "No").astype(int),
        "valor_mensal": raw["MonthlyCharges"].round(2),
        "plano": raw["InternetService"],
        "contrato": raw["Contract"],
        "churn": (raw["Churn"] == "Yes").astype(int),
    })
    return df.drop(columns="churn"), df["churn"]


X, y = load_data()

print("\n=== Dataset: IBM Telco Customer Churn ===")
print(f"Clientes: {len(X):,} | Taxa de churn: {y.mean():.1%}")

cat = ["plano", "contrato"]
num = ["idade", "meses_cliente", "tickets_suporte", "valor_mensal"]

pre = ColumnTransformer([
    ("num", StandardScaler(), num),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat),
])

model = Pipeline([
    ("preprocessamento", pre),
    ("modelo", LogisticRegression(max_iter=1000)),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model.fit(X_train, y_train)
pred = model.predict(X_test)
score = model.predict_proba(X_test)[:, 1]

print("\n=== Classificação ===")
print(classification_report(y_test, pred))
print("ROC-AUC:", round(roc_auc_score(y_test, score), 4))
print("\nMatriz de confusão:")
print(confusion_matrix(y_test, pred))
