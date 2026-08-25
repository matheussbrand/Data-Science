# Data-Projects

Repositório com projetos de **Ciência de Dados** e **Engenharia de Dados**, cada projeto independente com datasets públicos reais.

## Ciência de Dados

| Projeto | Dataset |
|---------|---------|
| [01_analise_vendas_ecommerce](01_analise_vendas_ecommerce/) | Online Retail (UCI) |
| [02_churn_clientes](02_churn_clientes/) | IBM Telco Customer Churn |
| [03_previsao_demanda](03_previsao_demanda/) | Daily Minimum Temperatures |
| [04_clusterizacao_clientes](04_clusterizacao_clientes/) | Mall Customers |
| [05_deteccao_anomalias](05_deteccao_anomalias/) | Credit Card Fraud (OpenML) |
| [06_pipeline_ml_producao](06_pipeline_ml_producao/) | Wisconsin Breast Cancer |

## Engenharia de Dados

| Projeto | Fonte de dados |
|---------|----------------|
| [01-data-lakehouse-ecommerce](01-data-lakehouse-ecommerce/) | Online Retail (UCI) |
| [02-real-time-pipeline](02-real-time-pipeline/) | Online Retail (UCI) |
| [03-financial-data-platform](03-financial-data-platform/) | API Frankfurter (câmbio) |
| [04-sales-data-warehouse](04-sales-data-warehouse/) | Online Retail (UCI) |
| [05-price-competitor-pipeline](05-price-competitor-pipeline/) | Web scraping |
| [06-data-quality-monitoring](06-data-quality-monitoring/) | Great Expectations |
| [07-brazilian-public-data](07-brazilian-public-data/) | Brasil API (IBGE) |
| [08-multitenant-data-platform](08-multitenant-data-platform/) | Multi-tenant SaaS |
| [09-cdc-debezium-kafka](09-cdc-debezium-kafka/) | CDC PostgreSQL |
| [10-feature-store-ml](10-feature-store-ml/) | Feast Feature Store |
| [11-application-log-pipeline](11-application-log-pipeline/) | Nginx logs (Elastic) |
| [12-data-mesh-enterprise](12-data-mesh-enterprise/) | Data Mesh / contratos |

## Como usar

Entre em qualquer pasta de projeto, instale as dependências e baixe os dados:

```bash
pip install -r requirements.txt
python scripts/download_data.py   # ou src/download_data.py
```
