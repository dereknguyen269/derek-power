---
inclusion: always
name: specialized-data-ai
description: Data, AI, and database specialist agents for machine learning, data engineering, and database optimization. Use for data-intensive projects requiring specialized expertise.
---

# Data & AI Specialist Agents

Expert agents for data engineering, AI/ML development, database optimization, and GraphQL architecture.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **AI Engineer** | `specialized.ai-engineer.md` | LLM apps, RAG systems | AI-powered applications |
| **Data Engineer** | `specialized.data-engineer.md` | ETL/ELT, data pipelines | Data infrastructure |
| **Data Scientist** | `specialized.data-scientist.md` | SQL, BigQuery, analytics | Data analysis, insights |
| **Database Optimizer** | `specialized.database-optimizer.md` | Query & schema optimization | Performance tuning |
| **GraphQL Architect** | `specialized.graphql-architect.md` | GraphQL API design | GraphQL projects |
| **ML Engineer** | `specialized.ml-engineer.md` | MLOps, model deployment | Production ML systems |
| **PostgreSQL Pro** | `specialized.postgres-pro.md` | PostgreSQL, PgLite | Postgres optimization |
| **Prompt Engineer** | `specialized.prompt-engineer.md` | LLM prompting, agentic AI | Prompt optimization |

## Agent Selection Guide

### By Task Type

| Task | Recommended Agent |
|------|-------------------|
| LLM application | AI Engineer |
| RAG system | AI Engineer |
| Data pipeline | Data Engineer |
| ETL/ELT design | Data Engineer |
| SQL optimization | Data Scientist |
| Business analytics | Data Scientist |
| Query performance | Database Optimizer |
| Schema design | Database Optimizer |
| GraphQL API | GraphQL Architect |
| Model deployment | ML Engineer |
| MLOps pipeline | ML Engineer |
| PostgreSQL tuning | PostgreSQL Pro |
| Prompt design | Prompt Engineer |
| Agentic workflows | Prompt Engineer |

### Detection Signals

| Signal | Confidence | Agent |
|--------|------------|-------|
| `langchain`, `openai` in deps | High | AI Engineer |
| `pinecone`, `weaviate`, `chroma` | High | AI Engineer |
| `airflow`, `spark`, `kafka` | High | Data Engineer |
| `bigquery`, `snowflake` | High | Data Scientist |
| `EXPLAIN ANALYZE` queries | High | Database Optimizer |
| `graphql`, `apollo` in deps | High | GraphQL Architect |
| `mlflow`, `kubeflow` | High | ML Engineer |
| PostgreSQL config files | High | PostgreSQL Pro |
| System prompts, prompt templates | Medium | Prompt Engineer |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | Data/AI Agent Role |
|-----------------|-------------------|
| **D**esign | Data architecture, ML system design |
| **E**valuate | Requirements, data assessment |
| **E**xecute | Implementation with best practices |
| **R**eview | Performance review, optimization |
| **K**nowledge | Patterns, learnings, documentation |

## Key Technologies

- **AI/LLM**: OpenAI, Anthropic, LangChain, LlamaIndex, vector databases
- **Data Engineering**: Apache Spark, Airflow, Kafka, dbt
- **Databases**: PostgreSQL, BigQuery, Snowflake, MongoDB
- **MLOps**: MLflow, Kubeflow, TensorFlow Serving, ONNX
- **GraphQL**: Apollo, Federation, DataLoader
