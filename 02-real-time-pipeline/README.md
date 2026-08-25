# Pipeline de Dados em Tempo Real

**Nível:** ★★★★★  
**Stack:** Python, Kafka, PySpark Structured Streaming, PostgreSQL, Docker

## Objetivo

Construir uma versão pequena, reproduzível e didática de uma arquitetura usada no mercado.

Não estou tentando esconder a complexidade atrás de uma ferramenta. O foco é entender o fluxo:

**fonte → ingestão → armazenamento → transformação → qualidade → consumo**

## O que este projeto demonstra

Streaming, eventos, processamento distribuído e agregações em janela.

## Perguntas que eu consigo responder depois deste projeto

- Onde os dados entram?
- Onde ficam persistidos?
- Qual transformação acontece em cada etapa?
- Como evitar duplicidade?
- Como tratar falhas?
- Como validar qualidade?
- Como tornar o pipeline reexecutável?
- Onde o custo e a performance começam a importar?

## Execução

```bash
docker compose up -d
python -m pip install -r requirements.txt
```

Consulte os arquivos de código e o `docker-compose.yml` para o fluxo específico.

## O que eu aprendi

O principal aprendizado aqui não é decorar comandos. É conseguir explicar a arquitetura, suas decisões e seus limites.

## Próximos passos

- adicionar testes automatizados;
- adicionar observabilidade;
- trocar dados locais por cloud;
- reproduzir a transformação Spark no Databricks;
- documentar custos e performance.

## Fluxo mental

```mermaid
flowchart LR
    A[Fonte] --> B[Ingestão]
    B --> C[Storage]
    C --> D[Transformação]
    D --> E[Qualidade]
    E --> F[Consumo]
```
