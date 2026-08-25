import joblib
from sklearn.datasets import load_breast_cancer

model = joblib.load("models/model.joblib")
data = load_breast_cancer(as_frame=True)

sample = data.data.iloc[[0]]
prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0].max()

print("Classe prevista:", data.target_names[prediction])
print("Confiança aproximada:", round(probability, 4))
