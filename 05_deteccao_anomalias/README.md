# 05 — Detecção de Anomalias

Projeto para identificar transações fora do comportamento esperado.

## Técnica
Isolation Forest.

## Aplicação
A mesma ideia pode ser usada em fraude, monitoramento financeiro, sensores e operações.

O projeto não tenta "provar fraude". Ele cria uma camada de triagem para investigação humana.

**Dataset real:** [Credit Card Fraud Detection (OpenML #1597)](https://www.openml.org/search?type=data&status=active&id=1597).

```bash
pip install -r requirements.txt
python scripts/download_data.py
python src/main.py
```
