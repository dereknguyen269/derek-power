---
name: "derek"
version: 0.1.2
displayName: "D.E.R.E.K"
description: |
  Design, Evaluate, Review, Execute, Knowledge.
  Enforces structured analysis, planning, approval, and review
  for all tasks before code changes. No vibe coding. Strong focus
  on security issues, maintainability, and task context retention.
  Includes persistent project memory system with web sharing capabilities via derek-memory MCP.
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

**IMPORTANT - Detection Logic:**
- If memory system already exists → Skip initialization, read existing files
- If partially exists → Create only missing files, preserve existing content
- If "reinit" command → Only regenerate PROJECT.md, preserve all other files
- Never overwrite existing memory files during "init"

## Folder Spec Planning System

For complex specifications, use dedicated folder specs under `.kiro/specs/`:

```
.kiro/specs/<spec-name>/
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

## Quick Implementation Modes

D.E.R.E.K supports three implementation approaches based on task complexity:

### 1. Full Spec Workflow (Complex Features)
**Command**: `"implement with specs [description]"`

**When to Use**:
- Multi-file features requiring coordination
- New systems or major refactors
- Features with unclear requirements
- Work spanning multiple sessions

**Process**:
1. Create requirements.md (get approval ⛔)
2. Create design.md (get approval ⛔)
3. Create tasks.md (implementation plan)
4. Execute tasks incrementally
5. Transfer learnings to KNOWLEDGE.md

**Steering Files to Use**:
- `planning.md` or `spec-planning.md` - Folder spec creation
- `analysis.md` - Requirements analysis
- Specialized agent - Domain-specific design and implementation
- `context.md` - Multi-session context retention
- `review.md` - Post-implementation review

**Example**: `"implement with specs: user authentication system with JWT"`

### 2. Quick Implementation (Simple Tasks)
**Command**: `"quick implement [description]"`

**When to Use**:
- Single-file changes
- Bug fixes
- Simple feature additions
- Clear, well-understood requirements

**Process**:
1. Brief analysis (no approval needed)
2. Direct implementation
3. Quick review
4. Update PROGRESS.md

**Steering Files to Use**:
- `analysis.md` - Quick task analysis
- Specialized agent (e.g., `specialized.python.md`, `specialized.react.md`) - Domain-specific implementation
- `review.md` - Post-implementation review

**Example**: `"quick implement: add email validation to signup form"`

### 3. Manual Spec Creation (Structured Planning)
**Commands**: `"create spec [name]"` → `"approve requirements"` → `"approve design"`

**When to Use**:
- Want to review each phase separately
- Collaborative planning with team
- Learning the D.E.R.E.K workflow
- Need to pause between phases

**Process**:
1. `create spec authentication` - Creates requirements.md
2. Review and iterate on requirements
3. `approve requirements` - Proceed to design
4. Review and iterate on design
5. `approve design` - Proceed to tasks
6. Execute tasks manually

**Steering Files to Use**:
- `spec-planning.md` - Detailed templates for requirements, design, tasks
- `planning.md` - Workflow overview
- Specialized agent - Domain-specific guidance
- `context.md` - Context retention between phases
- `review.md` - Final review

### Decision Matrix

| Task Type | Complexity | Files | Duration | Command | Steering Files |
|-----------|------------|-------|----------|---------|----------------|
| Bug fix | Low | 1 | < 1 hour | `quick implement` | analysis.md + specialized agent + review.md |
| Simple feature | Low-Medium | 1-2 | < 2 hours | `quick implement` | analysis.md + specialized agent + review.md |
| Feature with specs | Medium | 2-5 | 2-8 hours | `implement with specs` | planning.md + analysis.md + specialized agent + context.md + review.md |
| Complex system | High | 5+ | > 8 hours | `create spec` (manual) | spec-planning.md + specialized agent + context.md + review.md |
| Refactor | Medium-High | 3-10 | 4-16 hours | `implement with specs` | planning.md + code-archaeologist.md + specialized agent + review.md |

### Commands

**Memory & Initialization**
- `"init"` / `"reinit"` - Initialize or refresh project memory
- `"share memory"` - Generate shareable HTML of project memory (requires MCP)
- `"serve memory"` - Start local server to view shared memory

**Spec Planning (Structured Workflow)**
- `"create spec [name]"` - Create new folder spec with requirements.md
- `"approve requirements"` - Proceed to design phase
- `"approve design"` - Proceed to tasks/implementation phase
- `"complete spec"` - Transfer notes.md learnings to KNOWLEDGE.md

**Quick Implementation (Fast Track)**
- `"implement with specs [description]"` - Full spec workflow (requirements → design → tasks → code)
- `"quick implement [description]"` - Skip specs, direct implementation with minimal planning
- `"chat [question]"` (or `/chat [question]`) - Ask D.E.R.E.K a focused question using current context

**Skill Management**
- `"install skill [github-url]"` - Install skill from GitHub
- `"list skills"` - Show all available skills
- `"search skills [keyword]"` - Search for skills
- `"update skill [name]"` - Update installed skill
- `"uninstall skill [name]"` - Remove skill

**Automated Hooks** (Optional)
- Post-code context capture - Prompts to save decisions/learnings after code changes
- Auto-summary on context limit - Automatically summarizes when reaching 80% context
- See `hooks/README.md` for available hooks and setup instructions

## Steering File Organization

**70+ specialized agents organized by category**. Use dot notation (e.g., `core.code-reviewer.md`).

**Categories**: `core` (4) · `orchestrators` (4) · `infrastructure` (6) · `quality-testing` (3) · `security` (1) · `specialized` (40+) · `universal` (9)

**View full list**: Check `steering/*.md` index files or see tables below.

## When to Load Steering Files

**Token-Optimized Session Start**:
1. Read `PROGRESS.md` + `SCRATCHPAD.md` (90% of context)
2. Read `PROJECT.md` only if unfamiliar with project
3. Read `DECISIONS.md` / `KNOWLEDGE.md` only when needed
4. Never auto-edit files on session start

### Workflow Files

| File | Load When | Purpose |
|------|-----------|---------|
| `derek-init.md` | "init", new project | Initialize memory |
| `analysis.md` | New task | Task analysis |
| `planning.md` | After analysis | Implementation plan |
| `review.md` | After code | Quality & security |
| `context.md` | Long tasks | Context retention |

### Agent Categories

| Category | Count | When to Use |
|----------|-------|-------------|
| **Core** | 4 | Code review, debugging, performance, archaeology |
| **Orchestrators** | 4 | Project analysis, task breakdown, team config |
| **Infrastructure** | 6 | Cloud, deployment, DevOps, incidents |
| **Quality/Testing** | 3 | QA strategy, test automation |
| **Security** | 1 | Security audits |
| **Specialized** | 40+ | Go, Python, Rails, React, Vue, TS, Data/AI, Docs |
| **Universal** | 9 | API, backend, frontend, full-stack (any language) |

**Selection Priority**: Specialized → Universal → Core

### Quick Task Mapping

| Task | Load |
|------|------|
| New project | `derek-init.md` → `project-analyst.md` |
| Simple task | `analysis.md` → `planning.md` → `review.md` |
| Complex spec | `planning.md` (folder spec) → `context.md` |
| Debug | `debugger.md` |
| Performance | `performance-optimizer.md` |
| Security | `security-auditor.md` + `code-reviewer.md` |
| Legacy code | `code-archaeologist.md` |

## Skill Manager System

Install specialized "skills" - packages of steering files and domain intelligence.

**Commands**: `install skill <url>` · `list skills` · `search skills <keyword>` · `update skill <name>` · `uninstall skill <name>`

**Example**: `install skill https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`

**Features**: Auto-detect format · Cross-platform (Claude, Cursor, Windsurf) · Intelligent README parsing

---

## Activation Rules

**Activate when user mentions**: init · reinit · create spec · approve (requirements/design) · implement with specs · quick implement · chat · share memory · install skill · list skills · code review · planning · security audit · optimization

## Quick Reference

### Memory System Commands
```
init                    # Initialize project memory (first time only)
reinit                  # Refresh PROJECT.md (only when explicitly requested)
share memory            # Generate shareable HTML (via MCP)
serve memory            # Start local server to view HTML
```

### Spec Planning Commands (Structured Workflow)
```
create spec [name]      # Start folder spec planning
approve requirements    # Progress to design phase
approve design          # Progress to implementation
complete spec           # Transfer notes to KNOWLEDGE.md
```

### Quick Implementation Commands (Fast Track)
```
implement with specs [description]    # Full workflow: requirements → design → tasks → code
quick implement [description]         # Skip specs, direct implementation (use for simple tasks)
chat [question]                       # Ask a question using D.E.R.E.K with project context
```

### Skill Management Commands
```
install skill [github-url]   # Install skill from GitHub
list skills                  # Show all available skills
search skills [keyword]      # Search for skills
update skill [name]          # Update installed skill
uninstall skill [name]       # Remove skill
```

### Session Start Behavior (Token-Optimized)
```
✅ MINIMAL READS (in order):
1. PROGRESS.md (current task - REQUIRED)
2. SCRATCHPAD.md (last session - REQUIRED)
3. PROJECT.md (only if unfamiliar OR user mentions changes)
4. DECISIONS.md (only when decision context needed)
5. KNOWLEDGE.md (only when pattern/learning needed)

❌ DON'T:
- Read all files automatically (wastes tokens)
- Auto-edit any files on session start
- Reinitialize existing memory
- Update files without actual changes

📊 Optimization:
- PROGRESS.md + SCRATCHPAD.md = 90% context
- PROJECT.md = Read once, cache understanding
- Use selective line reading for large files

Update files ONLY when:
- PROJECT.md: User says "reinit" OR stack/architecture changes
- PROGRESS.md: Task status changes (started/blocked/completed)
- DECISIONS.md: New significant decision made
- KNOWLEDGE.md: Feature completed, learnings finalized
- SCRATCHPAD.md: Active work OR clearing after completion
```

### D.E.R.E.K Workflow
```
Design → Evaluate → Review → Execute → Knowledge
  ↓         ↓          ↓         ↓         ↓
requirements analysis  approval  tasks   KNOWLEDGE.md
design.md  planning.md  gates   notes.md  (finalized)
```

**Composable Framework**: Load multiple steering files as needed. Specialized → Universal → Core priority.
