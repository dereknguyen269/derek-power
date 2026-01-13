---
inclusion: always
name: specialized-documenter
description: Documentation specialist agents for API documentation and technical writing. Use for comprehensive documentation projects.
---

# Documentation Specialist Agents

Expert agents for creating comprehensive, developer-friendly documentation.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **API Documenter** | `documenter/api-documenter.md` | OpenAPI specs, API docs | REST API documentation |
| **Documentation Expert** | `documenter/documentation-expert.md` | Technical writing, guides | General documentation |

## Agent Selection Guide

### By Task Type

| Task | Recommended Agent |
|------|-------------------|
| OpenAPI specification | API Documenter |
| API reference docs | API Documenter |
| Postman collections | API Documenter |
| Code examples | API Documenter |
| User manuals | Documentation Expert |
| Technical guides | Documentation Expert |
| Style guides | Documentation Expert |
| Documentation strategy | Documentation Expert |

### Detection Signals

| Signal | Confidence | Agent |
|--------|------------|-------|
| `openapi.yaml` present | High | API Documenter |
| REST API endpoints | High | API Documenter |
| `docs/` directory | Medium | Documentation Expert |
| README updates needed | Medium | Documentation Expert |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | Documenter Role |
|-----------------|-----------------|
| **D**esign | Documentation architecture |
| **E**valuate | Audience analysis |
| **E**xecute | Content creation |
| **R**eview | Quality review |
| **K**nowledge | Documentation patterns |

## Key Outputs

- OpenAPI 3.0 specifications
- Multi-language code examples
- Postman collections
- User manuals and guides
- API reference documentation
- Style guides and standards
