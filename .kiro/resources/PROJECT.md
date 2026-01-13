# Project Overview

## 🎯 Quick Summary

**Project Name**: D.E.R.E.K Power
**Description**: A Kiro Power that enforces structured development workflow with persistent memory, approval gates, and security-first approach. Prevents "vibe coding" by requiring analysis and planning before implementation.
**Domain**: Developer Tools / AI-Assisted Development
**Status**: Active Development

## 🏗️ Technology Stack

### Core Technologies
| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| Platform | Kiro IDE | Latest | AI-powered development environment |
| Format | Markdown | - | Documentation and memory files |
| Structure | Steering Files | - | AI agent guidance system |

### Key Components
| Component | Purpose |
|-----------|---------|
| POWER.md | Power definition and documentation |
| mcp.json | Model Context Protocol configuration |
| Steering Files | 70+ specialized agent guidance files |

## 📐 Architecture Overview

### Pattern
**Structured Workflow Framework** with persistent memory system

### High-Level Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                    D.E.R.E.K Power                          │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  Memory  │   │ Steering │   │Approval  │
        │  System  │   │  Files   │   │  Gates   │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                    ┌──────────────────┐
                    │   D.E.R.E.K      │
                    │   Workflow       │
                    └────────┬─────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  ┌──────────┐         ┌──────────┐         ┌──────────┐
  │ Design   │         │ Evaluate │         │  Review  │
  └──────────┘         └──────────┘         └──────────┘
        │                     │                     │
        ▼                     ▼                     ▼
  ┌──────────┐         ┌──────────┐         ┌──────────┐
  │ Execute  │         │Knowledge │         │  Memory  │
  └──────────┘         └──────────┘         └──────────┘
```

### Directory Structure
```
derek-power/
├── POWER.md                    # Power definition
├── mcp.json                    # MCP configuration
└── steering/                   # Agent guidance files
    ├── analysis.md             # Task analysis framework
    ├── planning.md             # Planning framework
    ├── review.md               # Post-implementation review
    ├── context.md              # Context retention
    ├── derek-init.md           # Project initialization
    ├── memory-sharing.md       # Memory sharing system
    ├── examples.md             # Workflow examples
    ├── hooks-*.md              # Kiro hook templates
    │
    ├── core.*.md               # Core quality agents (4 files)
    ├── orchestrators.*.md      # Orchestration agents (4 files)
    ├── infrastructure.*.md     # DevOps agents (6 files)
    ├── quality-testing.*.md    # QA agents (3 files)
    ├── security-auditor.md     # Security audit agent
    ├── specialized.*.md        # Framework specialists (40+ files)
    └── universal.*.md          # Cross-stack agents (9 files)
```

## 🔑 Key Components

### Memory System Files
| File | Purpose | Update Frequency |
|------|---------|------------------|
| `PROJECT.md` | Project overview, tech stack, architecture | On reinit only |
| `PROGRESS.md` | Current task tracking and status | Every phase change |
| `DECISIONS.md` | Key decisions with rationale | After decisions |
| `KNOWLEDGE.md` | Finalized learnings and patterns | After completion |
| `SCRATCHPAD.md` | Temporary working notes | Continuously |

### Workflow Steering Files
| File | Purpose | When to Load |
|------|---------|--------------|
| `analysis.md` | Task analysis framework | Starting new tasks |
| `planning.md` | Planning framework | After analysis |
| `review.md` | Post-implementation review | After implementation |
| `context.md` | Context retention | Long-running tasks |
| `derek-init.md` | Project initialization | "init" command |

### Agent Categories
| Category | Count | Purpose |
|----------|-------|---------|
| Core Quality | 4 | Code review, debugging, performance, archaeology |
| Orchestrators | 4 | Project analysis, task breakdown, team config |
| Infrastructure | 6 | Cloud, deployment, DevOps, incidents |
| Quality & Testing | 3 | QA strategy, test automation |
| Security | 1 | Comprehensive security audits |
| Specialized | 40+ | Framework-specific experts (Go, Python, Rails, React, Vue, etc.) |
| Universal | 9 | Cross-stack agents (API, backend, frontend, full-stack) |

## 🚀 Entry Points

### Commands
| Command | Purpose |
|---------|---------|
| `init` | Initialize project memory system |
| `reinit` | Refresh PROJECT.md only |
| `create spec [name]` | Create folder spec |
| `approve requirements` | Progress to design phase |
| `approve design` | Progress to implementation |
| `complete spec` | Finalize and transfer learnings |
| `share memory` | Generate shareable HTML |

### Workflow Phases
| Phase | Description | Approval Required |
|-------|-------------|-------------------|
| **D**esign | Requirements → Design | Yes (2 gates) |
| **E**valuate | Task analysis | No |
| **R**eview | Code review | No |
| **E**xecute | Implementation | No |
| **K**nowledge | Learning capture | No |

## 💻 Development Commands

### Setup
```bash
# No build required - this is a Kiro Power
# Simply install in Kiro powers directory
```

### Usage
```bash
# Initialize project memory
"init"

# Create a folder spec
"create spec authentication"

# Approve phases
"approve requirements"
"approve design"

# Complete spec
"complete spec"

# Share memory
"share memory"
```

## 📏 Code Conventions

### File Naming
| Type | Convention | Example |
|------|------------|---------|
| Memory Files | UPPERCASE.md | `PROJECT.md`, `PROGRESS.md` |
| Steering Files | lowercase-kebab.md | `analysis.md`, `derek-init.md` |
| Category Index | category.md | `core.md`, `specialized.golang.md` |
| Specialized Agents | category.subcategory.md | `core.code-reviewer.md` |

### Folder Structure
- **Memory**: `.kiro/resources/` - Global project memory
- **Features**: `.kiro/features/<name>/` - Per-feature specs
- **Views**: `.kiro/views/` - Generated HTML outputs

### Markdown Patterns
```markdown
# Use H1 for main title
## Use H2 for major sections
### Use H3 for subsections

| Tables | For | Structured | Data |
|--------|-----|------------|------|

- Bullet lists for items
- [ ] Checkboxes for tasks

**Bold** for emphasis
*Italic* for subtle emphasis
`code` for inline code
```

## 🔗 External Integrations

| Integration | Purpose |
|-------------|---------|
| Kiro IDE | Host platform |
| MCP (Model Context Protocol) | Power configuration |
| Markdown | Documentation format |

## ⚠️ Important Notes

### Design Principles
1. **No vibe coding** - Always analyze and plan before implementation
2. **Approval gates** - Prevent wasted work on misunderstood requirements
3. **Persistent memory** - Context survives across sessions
4. **Security-first** - Built-in security awareness
5. **Knowledge accumulation** - Learn and improve over time

### Workflow Rules
- Always read memory files at session start
- Only update PROJECT.md on explicit "reinit" command
- Update PROGRESS.md when task status changes
- Log decisions in DECISIONS.md with rationale
- Transfer learnings to KNOWLEDGE.md after completion
- Clear SCRATCHPAD.md at session end

### Best Practices
- Use folder specs for complex features
- Use quick planning for simple tasks
- Respect approval gates - never skip them
- Keep specs focused and manageable
- Link to global memory for context
- Update progress continuously

---
*Generated: 2026-01-13*
*Last Updated: 2026-01-13*
