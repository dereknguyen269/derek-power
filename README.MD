# D.E.R.E.K Power

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

A Kiro Power that enforces structured analysis, planning, approval, and review for all development tasks. No vibe coding. Strong focus on security, maintainability, and persistent context retention.

## What Makes D.E.R.E.K Different?

Unlike typical AI coding assistants that jump straight into code generation, D.E.R.E.K enforces a disciplined workflow that prevents common pitfalls:

### The Problem with "Vibe Coding"
- 🚫 AI generates code based on vague requirements
- 🚫 No validation that the solution matches actual needs
- 🚫 Context lost between sessions
- 🚫 Security and quality issues discovered too late
- 🚫 Repeated mistakes because learnings aren't captured

### The D.E.R.E.K Solution
- ✅ **Approval gates** prevent wasted work on misunderstood requirements
- ✅ **Persistent memory** maintains context across sessions
- ✅ **Security-first** approach with built-in review processes
- ✅ **Knowledge accumulation** so you don't repeat mistakes
- ✅ **Structured planning** with clear requirements → design → implementation flow

Think of it as "working memory on disk" - your project context persists and evolves, not just in the AI's ephemeral context window.

## Overview

D.E.R.E.K transforms your development workflow by:

1. **Analyzing** tasks before jumping into code
2. **Planning** with persistent markdown files as "working memory on disk"
3. **Requiring approval** before implementation (approval gates)
4. **Reviewing** code for quality and security after implementation
5. **Retaining knowledge** across sessions with a project memory system

## Key Features

### 🧠 Project Memory System

Persistent markdown files in `.kiro/resources/` that maintain context across sessions:

- **PROJECT.md** - Project overview, tech stack, architecture
- **PROGRESS.md** - Current task tracking and status
- **DECISIONS.md** - Key decisions with rationale
- **KNOWLEDGE.md** - Finalized learnings and patterns
- **SCRATCHPAD.md** - Temporary working notes

### 📋 Two Planning Modes

#### Quick Planning
For simple tasks, bug fixes, and small changes:
- Uses `.kiro/resources/PROGRESS.md`
- Lightweight phase tracking
- Quick iteration

#### Folder Spec Planning
For complex specifications requiring multiple files/components:
- Uses `.kiro/features/<spec-name>/` folders
- Structured requirements → design → tasks workflow
- Approval gates at each phase
- Temporary knowledge capture during implementation

### 🚦 Approval Gates

Prevents wasted work on misunderstood requirements:
- ⛔ Requirements must be approved before design
- ⛔ Design must be approved before implementation
- Explicit human approval required at each gate

### 🔒 Security-First Approach

Built-in security awareness with specialized steering files for:
- Secure coding practices
- Code review with security focus
- Security audits and compliance
- Backend security implementation

## Quick Start

### Initialize Project Memory

```bash
# Say to Kiro:
"init"
```

This creates the project memory system and analyzes your codebase.

### Create a Folder Spec

```bash
# Say to Kiro:
"create spec authentication"
```

This creates `.kiro/features/authentication/` with:
- `requirements.md` - What to build
- `design.md` - How to build (after requirements approved)
- `tasks.md` - Implementation tracking (after design approved)
- `notes.md` - Temporary knowledge during implementation

### Approval Workflow

```bash
# After reviewing requirements.md:
"approve requirements"

# After reviewing design.md:
"approve design"

# After implementation complete:
"complete spec"
```

## Folder Spec Structure

```
.kiro/
├── resources/                    # Global Project Memory
│   ├── PROJECT.md               # Project overview
│   ├── PROGRESS.md              # Current task tracking
│   ├── DECISIONS.md             # Decision log
│   ├── KNOWLEDGE.md             # Finalized learnings
│   └── SCRATCHPAD.md            # Temporary notes
│
└── features/                     # Folder Specifications
    ├── authentication/           # Example spec
    │   ├── requirements.md      # WHAT to build
    │   ├── design.md            # HOW to build
    │   ├── tasks.md             # Implementation tracking
    │   └── notes.md             # Temporary knowledge
    │
    └── payment-integration/      # Another spec
        ├── requirements.md
        ├── design.md
        ├── tasks.md
        └── notes.md
```

## Workflow Diagram

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

## Commands

### Memory System
- `init` - Initialize project memory system
- `reinit` - Refresh PROJECT.md only (preserves other files)
- `share memory` - Generate shareable HTML view

### Folder Spec Planning
- `create spec [name]` - Create new folder spec
- `approve requirements` - Proceed to design phase
- `approve design` - Proceed to implementation phase
- `complete spec` - Finalize and transfer learnings

### Status
- `show spec status` - Display current spec progress
- `update task [ID]` - Update specific task status

## Steering Files

D.E.R.E.K includes comprehensive steering files organized by category:

### Workflow Files
- `analysis.md` - Task analysis framework
- `planning.md` - Planning framework (quick & folder spec)
- `review.md` - Post-implementation review
- `context.md` - Context retention across sessions
- `derek-init.md` - Project initialization

### Core Quality Agents
- `core.code-archaeologist.md` - Deep codebase exploration
- `core.code-reviewer.md` - Security-aware code review
- `core.debugger.md` - Error resolution & debugging
- `core.performance-optimizer.md` - Performance optimization

### Specialized Agents
- **Go**: `specialized.golang-pro.md`
- **Python**: 9 agents (Django, FastAPI, ML/Data, Testing, Security, etc.)
- **Rails**: 3 agents (Backend, API, ActiveRecord)
- **React**: 2 agents (Component Architect, Next.js)
- **Vue**: 3 agents (Component Architect, Nuxt, State Manager)
- **TypeScript**: `specialized.typescript-pro.md`
- **Data & AI**: 8 agents (AI Engineer, Data Engineer, Database Optimizer, etc.)

### Infrastructure & DevOps
- `infrastructure.cloud-architect.md`
- `infrastructure.deployment-engineer.md`
- `infrastructure.devops-incident-responder.md`
- `infrastructure.performance-engineer.md`

### Security
- `security-auditor.md` - Comprehensive security audits
- Backend security coding practices built-in

## When to Use

### Use Folder Spec Planning For:
- ✅ New features requiring multiple files/components
- ✅ Authentication, authorization systems
- ✅ API endpoints with complex logic
- ✅ Database schema changes
- ✅ Integration with external services
- ✅ Refactoring major components
- ✅ Work spanning multiple sessions

### Use Quick Planning For:
- ✅ Bug fixes
- ✅ Single-file changes
- ✅ Configuration updates
- ✅ Documentation updates

## Benefits

### Prevents Common Problems
- ❌ No more coding based on misunderstood requirements
- ❌ No more forgetting context between sessions
- ❌ No more repeating the same mistakes
- ❌ No more security vulnerabilities from rushed code

### Enables Best Practices
- ✅ Structured analysis before coding
- ✅ Clear implementation guidance
- ✅ Transparent progress tracking
- ✅ Knowledge accumulation over time
- ✅ Effective handoffs between sessions
- ✅ Security-first development

## Example: Authentication Spec

### 1. Create Spec
```
"create spec authentication"
```

### 2. Requirements Phase
Kiro generates `requirements.md` with:
- Problem statement
- User stories
- Functional requirements
- Non-functional requirements
- Security requirements

### 3. Approval Gate
```
"approve requirements"
```

### 4. Design Phase
Kiro generates `design.md` with:
- Architecture overview
- Data model
- API design
- Security design
- Testing strategy

### 5. Approval Gate
```
"approve design"
```

### 6. Implementation Phase
Kiro generates `tasks.md` with:
- Phased task breakdown
- Dependencies
- Estimates
- Acceptance criteria

Work through tasks, capturing discoveries in `notes.md`

### 7. Completion
```
"complete spec"
```

Transfers valuable learnings from `notes.md` to `KNOWLEDGE.md`

## Integration with Project Memory

Folder specs integrate seamlessly with the global project memory:

- **PROJECT.md** provides architecture context for all specs
- **PROGRESS.md** links to active specs
- **DECISIONS.md** receives decisions from spec implementations
- **KNOWLEDGE.md** receives finalized learnings after spec completion

## File References

Specs can reference other files using `#[[file:path]]` syntax:

```markdown
## References
- #[[file:.kiro/resources/PROJECT.md]] - Project architecture
- #[[file:app/api/v1/base.rb]] - API base class
- #[[file:docs/api-spec.yaml]] - OpenAPI specification
```

This allows specs to:
- Reference existing code patterns
- Link to API specifications
- Include external documentation
- Connect to project context

## Best Practices

### 1. Always Initialize
Run `init` before starting work on an unfamiliar project

### 2. Respect Approval Gates
Never skip requirements or design approval - it prevents wasted work

### 3. One Folder Per Spec
Keep specs focused and manageable

### 4. Update Progress Continuously
Mark tasks complete immediately, log errors as they occur

### 5. Transfer Knowledge
Move valuable discoveries from `notes.md` to `KNOWLEDGE.md` after completion

### 6. Link to Global Memory
Reference PROJECT.md for context, update KNOWLEDGE.md with learnings

## Installation

This is a Kiro Power. To use it:

1. Place this power in your Kiro powers directory
2. Activate it when needed by mentioning keywords like:
   - "init", "initialize project"
   - "create spec", "spec planning"
   - "approve requirements", "approve design"
   - "analyze task", "review code"

## Version

Current version: 0.1.0

## License

[Your license here]

## Contributing

[Your contribution guidelines here]
