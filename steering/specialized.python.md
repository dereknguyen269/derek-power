---
inclusion: always
name: specialized-python
description: Python specialist agents for web development, data science, DevOps, and backend systems. Use for Python projects requiring framework-specific expertise.
---

# Python Specialist Agents

Expert agents for Python development across web frameworks, data science, security, and backend systems.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **Python Expert** | `specialized.python.python-expert.md` | Core Python development | General Python, best practices |
| **Django Expert** | `specialized.python.django-expert.md` | Full-stack Django 5.0+ | Django projects, DRF APIs |
| **FastAPI Expert** | `specialized.python.fastapi-expert.md` | Modern async APIs | FastAPI, async Python |
| **ML/Data Expert** | `specialized.python.ml-data-expert.md` | Machine learning & data science | ML, pandas, scikit-learn |
| **Testing Expert** | `specialized.python.testing-expert.md` | Python testing | pytest, TDD, test automation |
| **Security Expert** | `specialized.python.security-expert.md` | Python security | Secure coding, vulnerability fixes |
| **Performance Expert** | `specialized.python.performance-expert.md` | Python optimization | Profiling, optimization |
| **DevOps/CI-CD Expert** | `specialized.python.devops-cicd-expert.md` | Python DevOps | CI/CD, automation, deployment |
| **Web Scraping Expert** | `specialized.python.web-scraping-expert.md` | Data extraction | Scrapy, BeautifulSoup, Selenium |

## Agent Selection Guide

### By Task Type

| Task | Recommended Agent |
|------|-------------------|
| Django web app | Django Expert |
| REST API with FastAPI | FastAPI Expert |
| Machine learning model | ML/Data Expert |
| Test suite setup | Testing Expert |
| Security audit | Security Expert |
| Performance optimization | Performance Expert |
| CI/CD pipeline | DevOps/CI-CD Expert |
| Data scraping | Web Scraping Expert |
| General Python | Python Expert |

### Detection Signals

| Signal | Framework | Agent |
|--------|-----------|-------|
| `manage.py` + `django` | Django | Django Expert |
| `fastapi` in requirements | FastAPI | FastAPI Expert |
| `scikit-learn`, `pandas`, `torch` | ML/Data | ML/Data Expert |
| `pytest` in requirements | Testing | Testing Expert |
| `.github/workflows/` | CI/CD | DevOps/CI-CD Expert |
| `scrapy` or `beautifulsoup4` | Scraping | Web Scraping Expert |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | Python Agent Role |
|-----------------|-------------------|
| **D**esign | Architecture, API design, data modeling |
| **E**valuate | Requirements analysis, tech assessment |
| **E**xecute | Implementation with Python best practices |
| **R**eview | Code review, security audit, performance |
| **K**nowledge | Patterns, learnings, documentation |
