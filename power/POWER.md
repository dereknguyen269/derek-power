---
name: "derek"
version: 0.1.0
displayName: "D.E.R.E.K"
description: |
  Design, Evaluate, Review, Execute, Knowledge.
  Enforces structured analysis, planning, approval, and review
  for all tasks before code changes. No vibe coding. Strong focus
  on security issues, maintainability, and task context retention.
  Includes persistent project memory system with web sharing capabilities.
keywords: ["analysis", "planning", "review", "security", "task context", "code quality", "analyst", "optimizer", "commits reviewer", "init", "initialize", "share memory", "memory sharing", "project memory", "serve memory", "derek"]
---
# D.E.R.E.K

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

This power enforces a disciplined development workflow:

1. When a task is first shared, analyze the task problem and scope.
2. Generate an implementation plan — *no code* yet.
3. Require *explicit human approval* before generating code suggestions.
4. After code is written, perform a formal review for quality and security.
5. Maintain persistent context across sessions for large tasks.

## Project Memory System

When initialized, this power creates a persistent memory system in the user's workspace at `.kiro/resources/`. These files are created by `derek-init.md` and are compatible with `planning.md` workflow:

| File | Purpose | When to Read/Update |
|------|---------|---------------------|
| `PROJECT.md` | Project overview, tech stack, architecture | Read at task start; update when project changes |
| `PROGRESS.md` | Current task tracking and status | Read/update every phase |
| `DECISIONS.md` | Key decisions with rationale | Update after significant decisions |
| `KNOWLEDGE.md` | Finalized learnings and patterns | Update after feature completion |
| `SCRATCHPAD.md` | Temporary working notes | Use during sessions; clear at end |

**To initialize**: Use `derek-init.md` or say "init" to create the memory system.

## Feature Planning System

For complex features, use dedicated feature folders under `.kiro/features/`:

```
.kiro/features/<feature-name>/
├── requirements.md   # WHAT to build (needs approval)
├── design.md        # HOW to build (needs approval)
├── tasks.md         # Implementation tracking
└── notes.md         # Temporary knowledge during implementation
```

### Feature Planning Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Requirements│────►│   Design    │────►│   Tasks     │────►│  Implement  │
│   (WHAT)    │     │   (HOW)     │     │  (TRACK)    │     │   (CODE)    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                                       │
       ▼                   ▼                                       ▼
  ⛔ APPROVAL         ⛔ APPROVAL                            📝 notes.md
     GATE                GATE                               (temp knowledge)
                                                                   │
                                                                   ▼
                                                            Transfer to
                                                            KNOWLEDGE.md
```

### Commands
- `"init"` / `"reinit"` - Initialize or refresh project memory
- `"create feature [name]"` - Create new feature folder with requirements.md
- `"approve requirements"` - Proceed to design phase
- `"approve design"` - Proceed to tasks/implementation phase
- `"complete feature"` - Transfer notes.md learnings to KNOWLEDGE.md

## Steering File Organization

Steering files are organized into categories for easy discovery. All agent files are symlinked from `shared/steerings/` for easy access:

```
steering/
├── analysis.md              # Task analysis framework
├── planning.md              # Planning framework (quick & feature)
├── review.md                # Post-implementation review
├── context.md               # Context retention framework
├── derek-init.md            # Project initialization
├── memory-sharing.md        # Memory sharing system
├── examples.md              # Planning workflow examples
├── hooks-before-code.md     # Pre-code validation hook template
├── hooks-after-code.md      # Post-code review hook template
│
├── core.md                  # Index: Core quality agents
├── code-archaeologist.md    # → shared/steerings/core/
├── code-reviewer.md         # → shared/steerings/core/
├── debugger.md              # → shared/steerings/core/
├── performance-optimizer.md # → shared/steerings/core/
│
├── orchestrators.md         # Index: Orchestration agents
├── project-analyst.md       # → shared/steerings/orchestrators/
├── tech-lead-orchestrator.md # → shared/steerings/orchestrators/
├── team-configurator.md     # → shared/steerings/orchestrators/
│
├── infrastructure.md        # Index: Infrastructure & DevOps agents
├── cloud-architect.md       # → shared/steerings/infrastructure/
├── deployment-engineer.md   # → shared/steerings/infrastructure/
├── devops-incident-responder.md # → shared/steerings/infrastructure/
├── incident-responder.md    # → shared/steerings/infrastructure/
├── performance-engineer.md  # → shared/steerings/infrastructure/
│
├── quality-testing.md       # Index: QA & Testing agents
├── qa-expert.md             # → shared/steerings/quality-testing/
├── test-automator.md        # → shared/steerings/quality-testing/
│
├── security.md              # Index: Security agents
├── security-auditor.md      # → shared/steerings/security/
│
├── specialized/             # Framework-specific agents (symlinked)
│   ├── golang.md            # Index: Go specialists
│   ├── golang/             # → shared/steerings/specialized/golang/
│   │   └── golang-pro.md        # Go 1.21+ expert
│   │
│   ├── python.md            # Index: Python specialists
│   ├── python/             # → shared/steerings/specialized/python/
│   │   ├── python-expert.md     # Core Python expert
│   │   ├── django-expert.md     # Django 5.0+ expert
│   │   ├── fastapi-expert.md    # FastAPI async APIs
│   │   ├── ml-data-expert.md    # ML & data science
│   │   ├── testing-expert.md    # pytest & TDD
│   │   ├── security-expert.md   # Python security
│   │   ├── performance-expert.md # Optimization
│   │   ├── devops-cicd-expert.md # CI/CD automation
│   │   └── web-scraping-expert.md # Data extraction
│   │
│   ├── rails.md             # Index: Rails specialists
│   ├── rails/              # → shared/steerings/specialized/rails/
│   │   ├── rails-backend-expert.md   # Full-stack Rails
│   │   ├── rails-api-developer.md    # Rails API
│   │   └── rails-activerecord-expert.md # ORM optimization
│   │
│   ├── react.md             # Index: React specialists
│   ├── react/              # → shared/steerings/specialized/react/
│   │   ├── react-component-architect.md # Component design
│   │   └── react-nextjs-expert.md       # Next.js expert
│   │
│   ├── vue.md               # Index: Vue specialists
│   ├── vue/                # → shared/steerings/specialized/vue/
│   │   ├── vue-component-architect.md # Vue 3 components
│   │   ├── vue-nuxt-expert.md         # Nuxt.js expert
│   │   └── vue-state-manager.md       # Pinia/Vuex state
│   │
│   ├── typescript.md        # Index: TypeScript specialists
│   ├── typescript/         # → shared/steerings/specialized/typescript/
│   │   └── typescript-pro.md    # Advanced TypeScript
│   │
│   ├── data-ai.md           # Index: Data & AI specialists
│   ├── data-ai/            # → shared/steerings/specialized/data-ai/
│   │   ├── ai-engineer.md       # LLM apps, RAG systems
│   │   ├── data-engineer.md     # ETL/ELT, pipelines
│   │   ├── data-scientist.md    # SQL, BigQuery, analytics
│   │   ├── database-optimizer.md # Query optimization
│   │   ├── graphql-architect.md # GraphQL API design
│   │   ├── ml-engineer.md       # MLOps, model deployment
│   │   ├── postgres-pro.md      # PostgreSQL expert
│   │   └── prompt-engineer.md   # LLM prompting
│   │
│   ├── documenter.md        # Index: Documentation specialists
│   └── documenter/         # → shared/steerings/specialized/documenter/
│       ├── api-documenter.md    # OpenAPI, API docs
│       └── documentation-expert.md # Technical writing
│
└── universal/              # Cross-stack agents (symlinked)
    ├── universal.md         # Index: Universal agents
    ├── api-architect.md     # → shared/steerings/universal/
    ├── api-security-audit.md # → shared/steerings/universal/
    ├── backend-developer.md # → shared/steerings/universal/
    ├── frontend-developer.md # → shared/steerings/universal/
    ├── full-stack-developer.md # → shared/steerings/universal/
    ├── nextjs-pro.md        # → shared/steerings/universal/
    ├── diagram-creator.md   # → shared/steerings/universal/
    └── tailwind-css-expert.md # → shared/steerings/universal/
```

## When to Load Steering Files

**IMPORTANT**: Before starting any task, check if `.kiro/resources/` exists. If it does, read `PROJECT.md` and `PROGRESS.md` to understand current context.

### Workflow Steering Files (Root Level)

| File | When to Load | Purpose |
|------|--------------|---------|
| `derek-init.md` | "init", "reinit", new project | Initialize memory system |
| `analysis.md` | Starting any new task | Structure task analysis |
| `planning.md` | After analysis approved | Create implementation plan |
| `review.md` | After implementation | Validate quality & security |
| `context.md` | Long-running tasks | Maintain context across sessions |
| `memory-sharing.md` | "share memory", "serve memory" | Share project memory via web |
| `examples.md` | Learning D.E.R.E.K workflow | Planning workflow examples |
| `hooks-before-code.md` | Setting up Kiro hooks | Pre-code validation template |
| `hooks-after-code.md` | Setting up Kiro hooks | Post-code review template |

### Core Agents

Quality assurance agents for any project. See `steering/core.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `code-archaeologist.md` | Legacy code, onboarding, audits | Deep codebase exploration |
| `code-reviewer.md` | After every feature/PR | Security-aware code review |
| `debugger.md` | Errors, test failures | Error resolution & debugging |
| `performance-optimizer.md` | Slowness, scaling issues | Performance optimization |

### Orchestrator Agents

Strategic agents for project analysis and coordination. See `steering/orchestrators.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `project-analyst.md` | New/unfamiliar codebase | Tech stack detection |
| `tech-lead-orchestrator.md` | Multi-step tasks | Task breakdown & delegation |
| `team-configurator.md` | New repo, stack changes | AI team configuration |

### Infrastructure Agents

DevOps and infrastructure specialists. See `steering/infrastructure.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `cloud-architect.md` | Cloud design, migrations | Infrastructure architecture |
| `deployment-engineer.md` | CI/CD setup, deployments | Pipeline automation |
| `devops-incident-responder.md` | Production outages | Incident response |
| `incident-responder.md` | Security incidents, data issues | General incident management |
| `performance-engineer.md` | Scaling, capacity planning | Infrastructure optimization |

### Quality & Testing Agents

QA and test automation specialists. See `steering/quality-testing.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `qa-expert.md` | Test planning, quality gates | Test strategy & QA process |
| `test-automator.md` | Writing tests, CI integration | Test implementation |

### Security Agents

Security audit and compliance specialists. See `steering/security.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `security-auditor.md` | Security reviews, compliance | Comprehensive security audits |

### Specialized Agents

Framework-specific experts. Check index files for available specialists.

| Category | Index File | Available Agents |
|----------|------------|------------------|
| **Go** | `golang.md` | 1 agent: Go 1.21+ expert |
| **Python** | `python.md` | 9 agents: Django, FastAPI, ML/Data, Testing, Security, Performance, DevOps, Web Scraping, Python Expert |
| **Rails** | `rails.md` | 3 agents: Backend Expert, API Developer, ActiveRecord Expert |
| **React** | `react.md` | 2 agents: Component Architect, Next.js Expert |
| **Vue** | `vue.md` | 3 agents: Component Architect, Nuxt Expert, State Manager |
| **TypeScript** | `typescript.md` | 1 agent: TypeScript Pro |
| **Data & AI** | `data-ai.md` | 8 agents: AI Engineer, Data Engineer, Data Scientist, Database Optimizer, GraphQL Architect, ML Engineer, PostgreSQL Pro, Prompt Engineer |
| **Documentation** | `documenter.md` | 2 agents: API Documenter, Documentation Expert |

### Universal Agents

Cross-stack agents when no specialist exists. See `steering/universal.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `api-architect.md` | New/revised API contracts | API design & specifications |
| `api-security-audit.md` | Security reviews, compliance | REST API security audits |
| `backend-developer.md` | Server-side code, any language | Polyglot backend implementation |
| `frontend-developer.md` | UI code, any framework | Universal UI builder |
| `full-stack-developer.md` | End-to-end applications | Complete web app development |
| `nextjs-pro.md` | Next.js projects | SSR/SSG, App Router, performance |
| `diagram-creator.md` | Architecture visualization | AWS-style diagrams |
| `tailwind-css-expert.md` | Tailwind CSS work | Utility-first styling |

## Loading Strategy

### By Task Type

| Task | Load These Files |
|------|------------------|
| **New Project** | `derek-init.md` → `project-analyst.md` |
| **Simple Task** | `analysis.md` → `planning.md` → `review.md` |
| **Complex Feature** | `analysis.md` → `planning.md` (feature mode) → `context.md` → `review.md` |
| **Legacy Code** | `code-archaeologist.md` → `analysis.md` |
| **Debugging** | `debugger.md` |
| **Performance Issue** | `performance-optimizer.md` |
| **Security Review** | `security-auditor.md` + `code-reviewer.md` |
| **Multi-Step Task** | `tech-lead-orchestrator.md` |
| **Production Incident** | `devops-incident-responder.md` |
| **Test Planning** | `qa-expert.md` → `test-automator.md` |
| **Cloud Architecture** | `cloud-architect.md` |

### By D.E.R.E.K Phase

| Phase | Primary Files | Support Files |
|-------|---------------|---------------|
| **D**esign | `planning.md` | `tech-lead-orchestrator.md`, `api-architect.md`, `cloud-architect.md` |
| **E**valuate | `analysis.md` | `project-analyst.md`, `code-archaeologist.md`, `security-auditor.md` |
| **R**eview | `review.md` | `code-reviewer.md`, `security-auditor.md`, `qa-expert.md` |
| **E**xecute | `backend-developer.md` | Specialized agents (e.g., `golang-pro.md`), `test-automator.md` |
| **K**nowledge | `context.md` | `memory-sharing.md`, `performance-optimizer.md` |

### Agent Selection Priority

```
1. Specialized agent (e.g., golang-pro.md for Go projects)
2. Universal agent (e.g., backend-developer.md)
3. Core agent (e.g., code-reviewer.md)
```

## Activation Rules

Activate this power when a team member mentions:
- "init", "initialize project", "project overview", "setup memory"
- "reinit", "reinitialize", "refresh project", "update project overview"
- "analyze task", "design plan", "review code", "security audit"
- "create feature", "feature planning", "requirements", "approve design"
- "share memory", "serve memory", "memory sharing"
- Keywords related to code review, planning, or optimization

## Quick Reference

### Memory System Commands
```
init                    # Initialize project memory
reinit                  # Refresh PROJECT.md only
create feature [name]   # Start feature planning
approve requirements    # Progress to design phase
approve design          # Progress to implementation
complete feature        # Transfer notes to KNOWLEDGE.md
share memory            # Generate shareable HTML
```

### D.E.R.E.K Workflow
```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  DESIGN  │──▶│ EVALUATE │──▶│  REVIEW  │──▶│ EXECUTE  │──▶│KNOWLEDGE │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
requirements   analysis.md    Approval      tasks.md      KNOWLEDGE.md
design.md      planning.md    Gates         notes.md      (finalized)
```

**Remember**: You can load multiple steering files when relevant. The framework is designed to be composable and context-aware.
