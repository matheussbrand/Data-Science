# 03 — Previsão de Demanda

Projeto simples de previsão de demanda para demonstrar como transformar histórico de vendas em uma previsão operacional.

## Abordagem
Série temporal real de temperaturas mínimas diárias (Melbourne), com engenharia de atributos via lags e médias móveis.

```bash
pip install -r requirements.txt
python scripts/download_data.py
python src/main.py
```
