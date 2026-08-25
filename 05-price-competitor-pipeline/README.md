# Pipeline de Preços e Concorrentes

**Nível:** ★★★★★  
**Stack:** Python, Scrapy, PostgreSQL, dbt, Docker

## Objetivo

Construir uma versão pequena, reproduzível e didática de uma arquitetura usada no mercado.

Fluxo:

**fonte → ingestão → armazenamento → transformação → qualidade → consumo**

## O que este projeto demonstra

Ingestão, scraping, histórico, deduplicação e dados incrementais.

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

## Fluxo mental

```mermaid
flowchart LR
    A[Fonte] --> B[Ingestão]
    B --> C[Storage]
    C --> D[Transformação]
    D --> E[Qualidade]
    E --> F[Consumo]
```
