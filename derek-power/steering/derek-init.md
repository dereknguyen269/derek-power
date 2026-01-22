---
inclusion: manual
name: derek-init
description: Initialize or reinitialize D.E.R.E.K project memory system. Creates persistent markdown files for planning, progress tracking, and knowledge storage. Use "init" for new projects, "reinit" to refresh project overview while preserving accumulated knowledge.
category: initialization
---

# D.E.R.E.K Initialization

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose

Initialize project memory system with persistent markdown files for context retention across sessions.

**Commands:**
- `init` - Full initialization (new/unfamiliar projects, complex tasks, onboarding)
- `reinit` - Refresh PROJECT.md only (structure changes, dependency updates, outdated context)

---

## Memory System Structure

```
.kiro/
├── resources/              # Global Memory
│   ├── PROJECT.md         # Architecture, stack, conventions
│   ├── PROGRESS.md        # Current work, phases, blockers
│   ├── DECISIONS.md       # Choices with rationale
│   ├── KNOWLEDGE.md       # Finalized patterns
│   └── SCRATCHPAD.md      # Temporary session notes
├── specs/                 # Feature Planning
│   └── <name>/
│       ├── requirements.md
│       ├── design.md
│       ├── tasks.md
│       └── notes.md
└── views/                 # Generated HTML
```

**File Usage:**
- PROJECT.md: Read on session start, update on reinit only
- PROGRESS.md: Read/update every session
- DECISIONS.md: Update after key decisions
- KNOWLEDGE.md: Update after feature completion
- SCRATCHPAD.md: Use during session, clear at end
- notes.md: Temporary feature knowledge → transfers to KNOWLEDGE.md

---

## Initialization Workflow

### Step 1: Detect Existing System

**CRITICAL: Always check first!**

```bash
test -d .kiro/resources && echo "✓ resources exists"
test -f .kiro/resources/PROJECT.md && echo "✓ PROJECT.md exists"
# Check all 5 memory files
```

**Decision Logic:**

| Scenario | Action |
|----------|--------|
| No .kiro/resources/ | Full init |
| All files exist | Skip init, read existing |
| Some files missing | Create missing only |
| User says "reinit" | Regenerate PROJECT.md only |

**If exists:** Skip creation, read files, report "Already initialized"
**If partial:** Create missing only, preserve existing, report what was created
**Never:** Overwrite existing files or run mkdir when directories exist

### Step 2: Create Directories (if missing)

```bash
test -d .kiro/resources || mkdir -p .kiro/resources
test -d .kiro/specs || mkdir -p .kiro/specs
test -d .kiro/views || mkdir -p .kiro/views
```

### Step 3: Analyze Project

**Scan for:**
- Tech stack: package.json, Gemfile, go.mod, requirements.txt, pom.xml, Cargo.toml, composer.json
- Architecture: MVC (app/models/views/controllers), Services (app/services/), API (app/api/), Microservices (multiple Dockerfiles)
- Directory structure: app/, config/, db/, lib/, spec/test/, scripts/
- Integrations: Database, search, queue, storage, auth, payments, notifications, monitoring

### Step 4: Generate Memory Files

**PROJECT.md** (only if missing or reinit):
- Quick Summary: name, description, domain, status
- Technology Stack: core tech, dependencies, infrastructure
- Architecture: pattern, directory structure, key components
- Entry Points: application entry, configuration
- Development Commands: setup, testing, quality
- Code Conventions: naming, organization, patterns
- External Integrations
- Important Notes: gotchas, performance, security

**PROGRESS.md** (only if missing):
- Current Focus: task, phase, status, dates
- Goal, Phases (5-phase table), Key Questions, Blockers, Errors, Completed Tasks, Next Steps, Session Log
- Initial: Task "None - awaiting assignment", Phase "Initialization Complete", Status 🟢 Ready

**DECISIONS.md** (only if missing):
- Purpose, Decision Index (table), Decisions (detailed entries)
- Template: Decision, Context, Alternatives, Rationale, Impact, Reversible
- Initial: "Project Initialization" decision

**KNOWLEDGE.md** (only if missing):
- Purpose, Quick Reference, Architecture Patterns, Gotchas & Pitfalls, Useful Snippets, Lessons Learned, External Resources

**SCRATCHPAD.md** (only if missing):
- Purpose, Current Session, Working Notes, Questions, Temporary Context, Quick TODO, Session Cleanup Checklist
- Initial: Focus "Project initialization", Status "Active"

## Initialization Checklist

- [ ] Check if memory system exists
- [ ] If exists → Skip init, read files, report "Already initialized"
- [ ] If partial → Create missing only, preserve existing
- [ ] Create directories (only if missing)
- [ ] Scan project structure
- [ ] Detect tech stack and architecture
- [ ] Generate memory files (only if missing or reinit)
- [ ] Report summary

## Example Outputs

**New Project:**
```
✅ D.E.R.E.K Memory System Initialized
📁 Created .kiro/resources/ (5 files)
📁 Created .kiro/specs/
📊 Project: [name, stack, architecture]
🚀 Ready! Use "create spec <name>" for complex work
```

**Already Initialized:**
```
✅ Memory System Exists
📁 .kiro/resources/ (last updated: X days ago)
📊 Loading PROGRESS.md and SCRATCHPAD.md...
💡 Use "reinit" to refresh PROJECT.md
🚀 Current task: [name] ([phase])
```

**Partial Init:**
```
⚠️ Partial System Found
📁 Created missing: DECISIONS.md, KNOWLEDGE.md
🚀 Memory system complete, existing files preserved
```

**Reinit:**
```
🔄 Memory Refreshed
📁 Updated: PROJECT.md
📁 Preserved: PROGRESS, DECISIONS, KNOWLEDGE
📁 Cleared: SCRATCHPAD.md
📊 Changes: [new dependencies, directories]
```

## Workflow

**Daily:** Read PROGRESS/SCRATCHPAD → Work (update files) → Log decisions → End (update PROGRESS, clear SCRATCHPAD)

**Task Types:**
- Quick (bug fixes, config) → PROGRESS.md
- Complex (features, multi-file) → specs/<name>/

**Integration:** analysis.md → SCRATCHPAD | planning.md → specs/ + PROGRESS | review.md → KNOWLEDGE | context.md → PROGRESS/KNOWLEDGE

## Remember

Init checks first, creates only missing. Reinit regenerates PROJECT.md only. Memory system enables context retention and knowledge accumulation.
