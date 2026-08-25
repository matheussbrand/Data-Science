# Arquitetura

Cada domínio é responsável por produzir e manter seus dados como produto.

Exemplo:
- Sales → `fct_sales`
- Finance → `fct_transactions`
- Customer → `dim_customer`

O contrato de dados define o que pode ser consumido por outros domínios.

Data Mesh não é apenas separar bancos. O ponto central é **ownership + data as a product + self-service + governança federada**.
