---
inclusion: manual
name: orchestrators
description: Strategic orchestration agents for project analysis, task coordination, and team configuration. These agents analyze projects and delegate work to specialists.
---

# Orchestrator Agents

Strategic agents that analyze projects, detect tech stacks, and coordinate work across specialist agents.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **Project Analyst** | `orchestrators.project-analyst.md` | Rapid tech stack detection | New/unfamiliar codebases |
| **Tech Lead Orchestrator** | `orchestrators.tech-lead-orchestrator.md` | Strategic task orchestration | Multi-step tasks, feature implementation |
| **Team Configurator** | `orchestrators.team-configurator.md` | AI team setup & configuration | New repos, tech stack changes |

## Agent Details

### Project Analyst
**File**: `#[[file:orchestrators.project-analyst.md]]`

Provides structured snapshots of project languages, frameworks, architecture patterns, and recommended specialists.

**Use PROACTIVELY for:**
- Analyzing new or unfamiliar codebases
- Detecting frameworks and tech stacks
- Routing work to correct specialists

**Output**: Technology stack analysis with confidence scores and specialist recommendations.

**Detection Hints**:
| Signal | Framework | Confidence |
|--------|-----------|------------|
| `laravel/framework` in composer.json | Laravel | High |
| `django` in requirements.txt | Django | High |
| `Gemfile` with `rails` | Rails | High |
| `go.mod` + `gin` import | Gin (Go) | Medium |
| `nx.json` / `turbo.json` | Monorepo tool | Medium |

---

### Tech Lead Orchestrator
**File**: `#[[file:orchestrators.tech-lead-orchestrator.md]]`

Senior technical lead that analyzes requirements and assigns ALL tasks to sub-agents. Never implements directly.

**MUST BE USED for:**
- Multi-step development tasks
- Feature implementations
- Architectural decisions

**Critical Rules**:
1. Main agent NEVER implements - only delegates
2. Maximum 2 agents run in parallel
3. Every task gets a sub-agent assignment

**Output**: Structured task breakdown with agent assignments and execution order.

**Common Patterns**:
- **Full-Stack**: analyze → backend → API → frontend → integrate → review
- **API-Only**: design → implement → authenticate → document
- **Performance**: analyze → optimize queries → add caching → measure
- **Legacy**: explore → document → plan → refactor

---

### Team Configurator
**File**: `#[[file:orchestrators.team-configurator.md]]`

Sets up or refreshes the AI development team for the current project.

**Use PROACTIVELY for:**
- New repositories
- After major tech stack changes
- When user asks to configure AI team

**Workflow**:
1. Detect project stack
2. Discover available agents
3. Pick best specialists
4. Update CLAUDE.md with team configuration

**Output**: Updated CLAUDE.md with AI Team Configuration section.

---

## Loading Strategy

```
New Project:        orchestrators.project-analyst.md → orchestrators.team-configurator.md
Complex Feature:    orchestrators.tech-lead-orchestrator.md
Stack Detection:    orchestrators.project-analyst.md
Team Setup:         orchestrators.team-configurator.md
```

## Integration with D.E.R.E.K

These agents integrate with the D.E.R.E.K workflow:

| D.E.R.E.K Phase | Orchestrator Agent |
|-----------------|-------------------|
| **D**esign | Tech Lead Orchestrator (task breakdown) |
| **E**valuate | Project Analyst (stack detection) |

## Delegation Flow

```
┌─────────────────┐
│ Project Analyst │ ─── Detects stack, recommends specialists
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│ Tech Lead           │ ─── Breaks down tasks, assigns agents
│ Orchestrator        │
└────────┬────────────┘
         │
         ▼
┌─────────────────┐
│ Team            │ ─── Configures project with right agents
│ Configurator    │
└─────────────────┘
```
