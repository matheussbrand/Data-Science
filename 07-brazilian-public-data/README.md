# Pipeline de Dados Públicos Brasileiros

**Nível:** ★★★★☆  
**Stack:** Python, APIs, PySpark, MinIO, Docker

## Objetivo

Construir uma versão viável para o ingestão de dados publicos.

## O que este projeto demonstra

Dados públicos, ingestão em escala e transformação distribuída.

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
