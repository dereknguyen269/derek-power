---
name: "derek"
version: 0.1.1
displayName: "D.E.R.E.K"
description: |
  Design, Evaluate, Review, Execute, Knowledge.
  Enforces structured analysis, planning, approval, and review
  for all tasks before code changes. No vibe coding. Strong focus
  on security issues, maintainability, and task context retention.
  Includes persistent project memory system with web sharing capabilities.
keywords: ["analysis", "planning", "review", "security", "task context", "code quality", "analyst", "optimizer", "commits reviewer", "init", "initialize", "share memory", "memory sharing", "project memory", "serve memory", "derek", "spec", "specification"]
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
| `PROJECT.md` | Project overview, tech stack, architecture | **Read on session start**; update ONLY when project structure/stack changes |
| `PROGRESS.md` | Current task tracking and status | **Read on session start**; update ONLY when task status changes |
| `DECISIONS.md` | Key decisions with rationale | **Read on session start**; update ONLY after new significant decisions |
| `KNOWLEDGE.md` | Finalized learnings and patterns | **Read on session start**; update ONLY after feature completion |
| `SCRATCHPAD.md` | Temporary working notes | **Read on session start**; update during active work; clear when task completes |

**To initialize**: Use `derek-init.md` or say "init" to create the memory system.

## Folder Spec Planning System

For complex specifications, use dedicated folder specs under `.kiro/features/`:

```
.kiro/features/<spec-name>/
├── requirements.md   # WHAT to build (needs approval)
├── design.md        # HOW to build (needs approval)
├── tasks.md         # Implementation tracking
└── notes.md         # Temporary knowledge during implementation
```

### Folder Spec Planning Workflow

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
- `"create spec [name]"` - Create new folder spec with requirements.md
- `"approve requirements"` - Proceed to design phase
- `"approve design"` - Proceed to tasks/implementation phase
- `"complete spec"` - Transfer notes.md learnings to KNOWLEDGE.md

## Steering File Organization

Steering files are organized into categories using dot notation for easy discovery:

```
steering/
├── analysis.md              # Task analysis framework
├── planning.md              # Planning framework (quick & folder spec)
├── review.md                # Post-implementation review
├── context.md               # Context retention framework
├── derek-init.md            # Project initialization
├── memory-sharing.md        # Memory sharing system
├── examples.md              # Planning workflow examples
├── hooks-before-code.md     # Pre-code validation hook template
├── hooks-after-code.md      # Post-code review hook template
│
├── core.md                          # Index: Core quality agents
├── core.code-archaeologist.md       # Deep codebase exploration
├── core.code-reviewer.md            # Security-aware code review
├── core.debugger.md                 # Error resolution & debugging
├── core.performance-optimizer.md    # Performance optimization
│
├── orchestrators.md                     # Index: Orchestration agents
├── orchestrators.project-analyst.md     # Tech stack detection
├── orchestrators.tech-lead-orchestrator.md # Task breakdown & delegation
├── orchestrators.team-configurator.md   # AI team configuration
│
├── infrastructure.md                            # Index: Infrastructure & DevOps agents
├── infrastructure.cloud-architect.md            # Infrastructure architecture
├── infrastructure.deployment-engineer.md        # Pipeline automation
├── infrastructure.devops-incident-responder.md  # Incident response
├── infrastructure.incident-responder.md         # General incident management
├── infrastructure.performance-engineer.md       # Infrastructure optimization
│
├── quality-testing.md                # Index: QA & Testing agents
├── quality-testing.qa-expert.md      # Test strategy & QA process
├── quality-testing.test-automator.md # Test implementation
│
├── security-auditor.md              # Comprehensive security audits
│
├── specialized.golang.md            # Index: Go specialists
├── specialized.golang-pro.md        # Go 1.21+ expert
│
├── specialized.python.md                    # Index: Python specialists
├── specialized.python.python-expert.md      # Core Python expert
├── specialized.python.django-expert.md      # Django 5.0+ expert
├── specialized.python.fastapi-expert.md     # FastAPI async APIs
├── specialized.python.ml-data-expert.md     # ML & data science
├── specialized.python.testing-expert.md     # pytest & TDD
├── specialized.python.security-expert.md    # Python security
├── specialized.python.performance-expert.md # Optimization
├── specialized.python.devops-cicd-expert.md # CI/CD automation
├── specialized.python.web-scraping-expert.md # Data extraction
│
├── specialized.rails.md                         # Index: Rails specialists
├── specialized.rails-backend-expert.md          # Full-stack Rails
├── specialized.rails-api-developer.md           # Rails API
├── specialized.rails-activerecord-expert.md     # ORM optimization
│
├── specialized.react.md                     # Index: React specialists
├── specialized.react-component-architect.md # Component design
├── specialized.react-nextjs-expert.md       # Next.js expert
│
├── specialized.vue.md                     # Index: Vue specialists
├── specialized.vue-component-architect.md # Vue 3 components
├── specialized.vue-nuxt-expert.md         # Nuxt.js expert
├── specialized.vue-state-manager.md       # Pinia/Vuex state
│
├── specialized.typescript.md        # Index: TypeScript specialists
├── specialized.typescript-pro.md    # Advanced TypeScript
│
├── specialized..data-ai.md              # Index: Data & AI specialists
├── specialized.ai-engineer.md           # LLM apps, RAG systems
├── specialized.data-engineer.md         # ETL/ELT, pipelines
├── specialized.data-scientist.md        # SQL, BigQuery, analytics
├── specialized.database-optimizer.md    # Query optimization
├── specialized.graphql-architect.md     # GraphQL API design
├── specialized.ml-engineer.md           # MLOps, model deployment
├── specialized.postgres-pro.md          # PostgreSQL expert
├── specialized.prompt-engineer.md       # LLM prompting
│
├── specialized.documenter.md            # Index: Documentation specialists
├── specialized.api-documenter.md        # OpenAPI, API docs
├── specialized.documentation-expert.md  # Technical writing
│
├── universal.md                     # Index: Universal agents
├── universal.api-architect.md       # API design & specifications
├── universal.api-security-audit.md  # REST API security audits
├── universal.backend-developer.md   # Polyglot backend implementation
├── universal.frontend-developer.md  # Universal UI builder
├── universal.full-stack-developer.md # Complete web app development
├── universal.nextjs-pro.md          # SSR/SSG, App Router, performance
├── universal.diagram-creator.md     # AWS-style diagrams
└── universal.tailwind-css-expert.md # Utility-first styling
```

## When to Load Steering Files

**IMPORTANT**: Before starting any task, check if `.kiro/resources/` exists. If it does:
- **READ ONLY** `PROJECT.md` and `PROGRESS.md` to understand current context
- **DO NOT EDIT** `PROJECT.md` on session start unless explicitly requested
- Only update `PROJECT.md` when project structure, tech stack, or architecture actually changes

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
| `core.code-archaeologist.md` | Legacy code, onboarding, audits | Deep codebase exploration |
| `core.code-reviewer.md` | After every feature/PR | Security-aware code review |
| `core.debugger.md` | Errors, test failures | Error resolution & debugging |
| `core.performance-optimizer.md` | Slowness, scaling issues | Performance optimization |

### Orchestrator Agents

Strategic agents for project analysis and coordination. See `steering/orchestrators.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `orchestrators.project-analyst.md` | New/unfamiliar codebase | Tech stack detection |
| `orchestrators.tech-lead-orchestrator.md` | Multi-step tasks | Task breakdown & delegation |
| `orchestrators.team-configurator.md` | New repo, stack changes | AI team configuration |

### Infrastructure Agents

DevOps and infrastructure specialists. See `steering/infrastructure.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `infrastructure.cloud-architect.md` | Cloud design, migrations | Infrastructure architecture |
| `infrastructure.deployment-engineer.md` | CI/CD setup, deployments | Pipeline automation |
| `infrastructure.devops-incident-responder.md` | Production outages | Incident response |
| `infrastructure.incident-responder.md` | Security incidents, data issues | General incident management |
| `infrastructure.performance-engineer.md` | Scaling, capacity planning | Infrastructure optimization |

### Quality & Testing Agents

QA and test automation specialists. See `steering/quality-testing.md` for full index.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `quality-testing.qa-expert.md` | Test planning, quality gates | Test strategy & QA process |
| `quality-testing.test-automator.md` | Writing tests, CI integration | Test implementation |

### Security Agents

Security audit and compliance specialists.

| Agent | When to Load | Purpose |
|-------|--------------|---------|
| `security-auditor.md` | Security reviews, compliance | Comprehensive security audits |

### Specialized Agents

Framework-specific experts. Check index files for available specialists.

| Category | Index File | Available Agents |
|----------|------------|------------------|
| **Go** | `specialized.golang.md` | 1 agent: Go 1.21+ expert |
| **Python** | `specialized.python.md` | 9 agents: Django, FastAPI, ML/Data, Testing, Security, Performance, DevOps, Web Scraping, Python Expert |
| **Rails** | `specialized.rails.md` | 3 agents: Backend Expert, API Developer, ActiveRecord Expert |
| **React** | `specialized.react.md` | 2 agents: Component Architect, Next.js Expert |
| **Vue** | `specialized.vue.md` | 3 agents: Component Architect, Nuxt Expert, State Manager |
| **TypeScript** | `specialized.typescript.md` | 1 agent: TypeScript Pro |
| **Data & AI** | `specialized..data-ai.md` | 8 agents: AI Engineer, Data Engineer, Data Scientist, Database Optimizer, GraphQL Architect, ML Engineer, PostgreSQL Pro, Prompt Engineer |
| **Documentation** | `specialized.documenter.md` | 2 agents: API Documenter, Documentation Expert |

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
| **Complex Spec** | `analysis.md` → `planning.md` (folder spec mode) → `context.md` → `review.md` |
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
- "create spec", "spec planning", "requirements", "approve design"
- "share memory", "serve memory", "memory sharing"
- Keywords related to code review, planning, or optimization

## Quick Reference

### Memory System Commands
```
init                    # Initialize project memory (first time only)
reinit                  # Refresh PROJECT.md (only when explicitly requested)
create spec [name]      # Start folder spec planning
approve requirements    # Progress to design phase
approve design          # Progress to implementation
complete spec           # Transfer notes to KNOWLEDGE.md
share memory            # Generate shareable HTML
```

### Session Start Behavior
```
✅ DO on session start:
- Check if .kiro/resources/ exists
- READ all memory files (PROJECT.md, PROGRESS.md, DECISIONS.md, KNOWLEDGE.md, SCRATCHPAD.md)
- Continue from last known state
- Understand current context without modifying

❌ DON'T on session start:
- Edit any memory files automatically
- Reinitialize existing memory
- Overwrite existing context
- Update files "just because" a session started

Only update memory files when:
- PROJECT.md: User requests "reinit" OR tech stack/architecture actually changes
- PROGRESS.md: Task status actually changes (started, blocked, completed)
- DECISIONS.md: New significant decision is made
- KNOWLEDGE.md: Feature/task is completed and learnings are finalized
- SCRATCHPAD.md: Active work in progress OR clearing after task completion
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
