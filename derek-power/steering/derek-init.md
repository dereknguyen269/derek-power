---
inclusion: manual
name: derek-init
description: Initialize or reinitialize D.E.R.E.K project memory system. Creates persistent markdown files for planning, progress tracking, and knowledge storage. Use "init" for new projects, "reinit" to refresh project overview while preserving accumulated knowledge.
category: initialization
---

# D.E.R.E.K Initialization

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose

Initialize a comprehensive project overview and working memory system. This creates persistent markdown files that serve as your "memory on disk" - enabling context retention across sessions, structured planning, and knowledge accumulation.

**Commands:**
- `init` - Full initialization for new/unfamiliar projects
- `reinit` - Refresh PROJECT.md while preserving decisions, knowledge, and progress

**Use `init` when:**
- Starting work on a new or unfamiliar project
- Beginning a complex multi-step task
- Onboarding to a codebase you haven't worked with before
- Need to establish project context for long-running work

**Use `reinit` when:**
- Project structure has changed significantly
- Dependencies were added or upgraded
- Returning after a long break
- PROJECT.md feels outdated

---

## Memory System Architecture

```
.kiro/
├── resources/                    # Persistent Memory Storage (Global)
│   ├── PROJECT.md               # 🏗️ Project DNA - Architecture, stack, conventions
│   ├── PROGRESS.md              # 📊 Task Tracker - Current work, phases, blockers
│   ├── DECISIONS.md             # ⚖️ Decision Log - Choices made with rationale
│   ├── KNOWLEDGE.md             # 🧠 Knowledge Base - Finalized patterns & learnings
│   └── SCRATCHPAD.md            # 📝 Working Notes - Temporary session context
│
├── features/                     # Feature Planning (Per-Feature)
│   └── <feature-name>/
│       ├── requirements.md      # 📋 What to build (needs approval)
│       ├── design.md            # 🎨 How to build (needs approval)
│       ├── tasks.md             # ✅ Implementation tracking
│       └── notes.md             # 📝 Temporary knowledge during implementation
│
└── views/                        # Generated Outputs
    └── project-memory-*.html    # 🌐 Shareable HTML views
```

### File Purposes

| File | Location | Read Frequency | Update Frequency | Purpose |
|------|----------|----------------|------------------|---------|
| `PROJECT.md` | resources/ | Every session start | On reinit only | Understand project structure |
| `PROGRESS.md` | resources/ | Every task start | Every phase change | Track current work |
| `DECISIONS.md` | resources/ | When making choices | After key decisions | Maintain consistency |
| `KNOWLEDGE.md` | resources/ | When facing issues | After feature completion | Finalized learnings |
| `SCRATCHPAD.md` | resources/ | During session | Continuously | Working memory |
| `notes.md` | features/*/ | During implementation | Continuously | Temporary feature knowledge |

### D.E.R.E.K Workflow Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           D.E.R.E.K WORKFLOW                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐  │
│  │  DESIGN  │──▶│ EVALUATE │──▶│  REVIEW  │──▶│ EXECUTE  │──▶│KNOWLEDGE │  │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘  │
│       │              │              │              │              │         │
│       ▼              ▼              ▼              ▼              ▼         │
│  requirements   analysis.md    Approval      tasks.md      KNOWLEDGE.md    │
│  design.md      planning.md    Gates         notes.md      (finalized)     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Initialization Workflow

### Step 0: Detect Existing Memory System

**CRITICAL: Always check first before creating anything!**

Before initialization, check if the memory system already exists:

```bash
# Check for existing directories
test -d .kiro/resources && echo "✓ resources exists"
test -d .kiro/specs && echo "✓ features exists"
test -d .kiro/views && echo "✓ views exists"

# Check for existing memory files
test -f .kiro/resources/PROJECT.md && echo "✓ PROJECT.md exists"
test -f .kiro/resources/PROGRESS.md && echo "✓ PROGRESS.md exists"
test -f .kiro/resources/DECISIONS.md && echo "✓ DECISIONS.md exists"
test -f .kiro/resources/KNOWLEDGE.md && echo "✓ KNOWLEDGE.md exists"
test -f .kiro/resources/SCRATCHPAD.md && echo "✓ SCRATCHPAD.md exists"
```

**Decision Logic:**

| Scenario | Action | Command |
|----------|--------|---------|
| No `.kiro/resources/` directory | Full initialization | `init` |
| Directories exist, no files | Create memory files | `init` |
| All files exist | Skip initialization, load memory | Read existing files |
| Some files missing | Create missing files only | Partial init |
| User says "reinit" | Regenerate PROJECT.md only | `reinit` |

**If memory system already exists:**
- ✅ Skip directory creation (already exist)
- ✅ Skip file creation (already exist)
- ✅ Read existing files to understand current state
- ✅ Report: "Memory system already initialized. Reading existing context..."
- ❌ DO NOT overwrite existing files
- ❌ DO NOT run mkdir commands

**If memory system partially exists:**
- ✅ Create only missing directories
- ✅ Create only missing files
- ✅ Preserve all existing content
- ✅ Report what was created vs what was found

### Step 1: Create Directory Structure (Only if Missing)

**Only run if directories don't exist!**

```bash
# Create only if missing
test -d .kiro/resources || mkdir -p .kiro/resources
test -d .kiro/specs || mkdir -p .kiro/specs
test -d .kiro/views || mkdir -p .kiro/views
```

### Step 2: Deep Project Analysis

Perform comprehensive analysis before generating files:

#### 2.1 Technology Stack Detection

```
📦 Package Files to Scan:
├── Gemfile / Gemfile.lock      → Ruby/Rails dependencies
├── package.json                 → Node.js dependencies
├── go.mod                       → Go modules
├── requirements.txt / Pipfile   → Python dependencies
├── pom.xml / build.gradle       → Java dependencies
├── Cargo.toml                   → Rust dependencies
└── composer.json                → PHP dependencies
```

#### 2.2 Architecture Pattern Recognition

| Pattern | Indicators | Confidence |
|---------|------------|------------|
| **MVC** | `app/models`, `app/views`, `app/controllers` | High |
| **Service Objects** | `app/services/`, `*_service.rb` | High |
| **API-First** | `app/api/`, Grape/GraphQL gems | High |
| **Microservices** | Multiple `Dockerfile`, service directories | Medium |
| **Event-Driven** | Kafka consumers, Sidekiq jobs | Medium |
| **Domain-Driven** | Domain folders, bounded contexts | Medium |

#### 2.3 Code Organization Analysis

```
📁 Directory Purposes:
├── app/                    → Application code
│   ├── api/               → API endpoints (Grape, GraphQL)
│   ├── controllers/       → Request handlers
│   ├── models/            → Data models & business logic
│   ├── services/          → Business logic services
│   ├── jobs/              → Background jobs
│   ├── consumers/         → Message consumers
│   └── mailers/           → Email templates
├── config/                 → Configuration files
├── db/                     → Database migrations & seeds
├── lib/                    → Shared libraries
├── spec/ or test/          → Test files
└── scripts/                → Utility scripts
```

#### 2.4 External Dependencies Mapping

```
🔗 Integration Points:
├── Database          → PostgreSQL, MySQL, MongoDB, Redis
├── Search            → Elasticsearch, Algolia
├── Queue             → Sidekiq, Kafka, RabbitMQ
├── Storage           → S3, GCS, local
├── Auth              → Devise, JWT, OAuth
├── Payments          → Stripe, PayPal
├── Notifications     → Twilio, Firebase, SendGrid
└── Monitoring        → Skylight, NewRelic, DataDog
```

---

### Step 3: Generate PROJECT.md

Create comprehensive project overview with these sections:

**Required Sections:**
- 🎯 Quick Summary (name, description, domain, status)
- 🏗️ Technology Stack (core tech, dependencies, infrastructure)
- 📐 Architecture (pattern, directory structure, key components)
- 🚀 Entry Points (application entry, configuration)
- 💻 Development Commands (setup, testing, quality)
- 📏 Code Conventions (naming, organization, patterns)
- 🔗 External Integrations
- ⚠️ Important Notes (gotchas, performance, security)

**Format:** Use tables for structured data, code blocks for examples, bullet points for lists. Keep concise but comprehensive.

---

### Step 4: Generate PROGRESS.md

**Sections:** Current Focus (task, phase, status, dates) · Goal · Phases (5-phase table) · Key Questions · Blockers · Errors · Completed Tasks · Next Steps · Session Log

**Initial State:** Task "None - awaiting assignment", Phase "Initialization Complete", Status 🟢 Ready

---

### Step 5: Generate DECISIONS.md

**Sections:** Purpose · Decision Index (table) · Decisions (detailed entries with template)

**Template Fields:** Decision · Context · Alternatives Considered · Rationale · Impact · Reversible

**Initial Entry:** "Project Initialization" decision with memory system rationale

---

### Step 6: Generate KNOWLEDGE.md

**Sections:** Purpose · Quick Reference (commands, queries) · Architecture Patterns (code examples) · Gotchas & Pitfalls (tables) · Useful Snippets (debugging, performance, testing) · Lessons Learned · External Resources

**Populate with:** Project-specific commands, common patterns, known issues, helpful snippets

---

### Step 7: Generate SCRATCHPAD.md

**Sections:** Purpose · Current Session (started, focus, status) · Working Notes · Questions to Investigate · Temporary Context · Quick TODO · Session Cleanup Checklist

**Initial State:** Focus "Project initialization", Status "Active"

---

## Initialization Checklist

When running `init`, complete these steps:

- [ ] **FIRST: Check if memory system already exists**
- [ ] If all files exist → Skip init, read existing files, report "Already initialized"
- [ ] If partially exists → Note what exists, create only missing pieces
- [ ] Create `.kiro/resources/` directory (only if missing)
- [ ] Create `.kiro/specs/` directory (only if missing)
- [ ] Create `.kiro/views/` directory (only if missing)
- [ ] Scan project structure thoroughly
- [ ] Detect technology stack with versions
- [ ] Map architecture patterns
- [ ] Identify key components and relationships
- [ ] Generate `PROJECT.md` (only if missing or reinit)
- [ ] Initialize `PROGRESS.md` (only if missing)
- [ ] Initialize `DECISIONS.md` (only if missing)
- [ ] Initialize `KNOWLEDGE.md` (only if missing)
- [ ] Initialize `SCRATCHPAD.md` (only if missing)
- [ ] Verify all files are accurate
- [ ] Report initialization summary with D.E.R.E.K branding

---

## Example Init Outputs

### New Project
```
✅ D.E.R.E.K Memory System Initialized
📁 Created .kiro/resources/ (PROJECT, PROGRESS, DECISIONS, KNOWLEDGE, SCRATCHPAD)
📁 Created .kiro/specs/
📊 Project Analysis: [name, stack, architecture, key findings]
🚀 Ready! Use "create feature <name>" for complex work or update PROGRESS.md for simple tasks
```

### Already Initialized
```
✅ D.E.R.E.K Memory System Already Exists
📁 Found .kiro/resources/ (all files exist, last updated: X days ago)
� Found .kiro/specs/ (Xd specs: Y in progress, Z complete)
📊 Loading context from PROGRESS.md and SCRATCHPAD.md...
💡 Tip: Use "reinit" to refresh PROJECT.md
🚀 Ready! Current task: [task name] ([phase])
```

### Partial Init
```
⚠️ D.E.R.E.K Memory System Partially Initialized
📁 Found .kiro/resources/ (some files missing)
📁 Created missing: DECISIONS.md, KNOWLEDGE.md
🚀 Ready! Memory system now complete, existing files preserved
```

### Reinit
```
🔄 D.E.R.E.K Memory Refreshed
📁 Updated: PROJECT.md (regenerated with fresh analysis)
� Preserved: PROGRESS, DECISIONS, KNOWLEDGE (all intact)
📁 Cleared: SCRATCHPAD.md
📊 Changes Detected: [new dependencies, directories, models]
```

---

## Post-Initialization Workflow

**Daily Workflow:** Start Session (read PROGRESS/PROJECT/features) → During Work (update SCRATCHPAD/PROGRESS/notes) → After Decisions (log to DECISIONS) → When Learning (update notes/KNOWLEDGE) → End Session (update PROGRESS, clear SCRATCHPAD)

**Quick vs Feature Planning:** Bug fixes/config → PROGRESS.md | New features/multi-file/auth → features/<name>/

**Steering Integration:** analysis.md (reads PROJECT, writes SCRATCHPAD) · planning.md (reads PROJECT, creates features/, writes PROGRESS) · review.md (reads all, writes KNOWLEDGE) · context.md (uses PROGRESS/KNOWLEDGE)

**Feature Planning Flow:**
```
init → "create feature X" → features/X/ (requirements → design → tasks → notes) → KNOWLEDGE.md
```

---

## Remember

**Init checks first, creates only missing pieces. Reinit only regenerates PROJECT.md. Memory system enables context retention, consistent decisions, knowledge accumulation, and team sharing.**
