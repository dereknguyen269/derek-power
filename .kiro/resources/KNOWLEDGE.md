# Project Knowledge Base

## Purpose

Accumulate learnings, patterns, and insights discovered during development. This prevents repeating mistakes and captures institutional knowledge.

## 📚 Quick Reference

### D.E.R.E.K Commands
```bash
# Initialize project memory
init

# Refresh project overview (preserves other files)
reinit

# Create folder spec for complex features
create spec <name>

# Progress through approval gates
approve requirements
approve design

# Complete feature and transfer learnings
complete spec

# Share project memory as HTML
share memory
```

### Memory File Purposes
```
PROJECT.md    - Project DNA (read every session, update on reinit only)
PROGRESS.md   - Task tracking (update when status changes)
DECISIONS.md  - Decision log (update after key decisions)
KNOWLEDGE.md  - Learnings (update after feature completion)
SCRATCHPAD.md - Working notes (update continuously, clear at session end)
```

---

## 🏗️ Architecture Patterns

### D.E.R.E.K Workflow Pattern
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Requirements│────►│   Design    │────►│   Tasks     │
│   (WHAT)    │     │   (HOW)     │     │  (TRACK)    │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
       ▼                   ▼                   ▼
  ⛔ APPROVAL         ⛔ APPROVAL         Implementation
     GATE                GATE              with notes.md
```

**Key Principle**: Never skip approval gates. They prevent wasted work on misunderstood requirements.

### Memory System Pattern
```
Session Start:
1. Read all memory files (.kiro/resources/*.md)
2. Understand current context
3. Continue from last known state

During Work:
1. Update SCRATCHPAD.md with working notes
2. Update PROGRESS.md when phase changes
3. Log decisions in DECISIONS.md with rationale
4. Capture discoveries in features/*/notes.md

Session End:
1. Update PROGRESS.md with final status
2. Transfer important notes to appropriate files
3. Clear SCRATCHPAD.md
```

### Folder Spec Pattern
```
.kiro/features/<feature-name>/
├── requirements.md  # WHAT to build (needs approval)
├── design.md        # HOW to build (needs approval)
├── tasks.md         # Implementation tracking
└── notes.md         # Temporary knowledge during implementation
                     # (transferred to KNOWLEDGE.md on completion)
```

**When to Use**:
- ✅ New features requiring multiple files/components
- ✅ Authentication, authorization systems
- ✅ API endpoints with complex logic
- ✅ Database schema changes
- ✅ Work spanning multiple sessions

**When NOT to Use**:
- ❌ Simple bug fixes (use quick planning in PROGRESS.md)
- ❌ Single-file changes
- ❌ Configuration updates

---

## ⚠️ Gotchas & Pitfalls

### Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Skipping approval gates | Wasted work on wrong solution | Always get explicit approval |
| Editing PROJECT.md on session start | Unnecessary churn | Only update on explicit "reinit" |
| Not reading memory files | Lost context | Always read at session start |
| Forgetting to transfer learnings | Knowledge loss | Move notes.md to KNOWLEDGE.md |
| Keeping stale SCRATCHPAD | Context pollution | Clear at session end |

### D.E.R.E.K Workflow

| Issue | Wrong Approach | Correct Approach |
|-------|----------------|------------------|
| Starting task | Jump into code | Run analysis.md first |
| Complex feature | Quick planning | Create folder spec |
| Requirements unclear | Guess and implement | Get approval before design |
| Design uncertain | Code and iterate | Get approval before implementation |
| Learning something | Keep in head | Document in notes.md |

---

## 🔧 Useful Patterns

### Session Start Pattern
```markdown
1. Check if .kiro/resources/ exists
2. Read PROJECT.md for project context
3. Read PROGRESS.md for current task status
4. Read DECISIONS.md for past decisions
5. Read KNOWLEDGE.md for accumulated learnings
6. Read SCRATCHPAD.md for last session notes
7. Continue work without modifying files unnecessarily
```

### Decision Logging Pattern
```markdown
### [date] - [Decision Title]

**Decision**: [What was decided]

**Context**: 
- [Why this decision was needed]
- [Current situation]

**Alternatives Considered**:
1. [Option 1] - [Pros/Cons]
2. [Option 2] - [Pros/Cons]

**Rationale**: 
- [Why this option was chosen]

**Impact**: 
- [What this affects]

**Reversible**: [Yes/No/Partially]
```

### Knowledge Transfer Pattern
```markdown
When completing a feature:
1. Review features/<name>/notes.md
2. Identify valuable learnings
3. Transfer to KNOWLEDGE.md with context
4. Organize by category (patterns, gotchas, snippets)
5. Delete or archive notes.md
```

---

## 📖 Lessons Learned

| Date | Lesson | Context |
|------|--------|---------|
| 2026-01-13 | Memory system prevents context loss | Initialization demonstrates persistent memory |
| 2026-01-13 | Approval gates prevent wasted work | Core principle of D.E.R.E.K workflow |
| 2026-01-13 | Using derek on itself is meta but effective | Best way to demonstrate is by doing |

---

## 🔗 External Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| D.E.R.E.K README | README.MD | Complete documentation |
| Steering Files | derek-power/steering/ | 70+ agent guidance files |
| POWER.md | derek-power/POWER.md | Power definition |

---

## 📝 Quick Tips

### For Users
- Always run `init` on new projects before starting work
- Respect approval gates - they save time in the long run
- Use folder specs for anything complex or multi-session
- Read memory files at session start to understand context
- Transfer learnings to KNOWLEDGE.md after completing features

### For AI Agents
- Read all memory files at session start
- Only update PROJECT.md on explicit "reinit" command
- Update PROGRESS.md when task status actually changes
- Log decisions with clear rationale in DECISIONS.md
- Transfer notes.md to KNOWLEDGE.md after feature completion
- Clear SCRATCHPAD.md at session end

---

## 🎯 Success Metrics

**D.E.R.E.K is working well when:**
- ✅ Context persists across sessions without re-explanation
- ✅ Decisions are documented and referenced later
- ✅ Mistakes aren't repeated because they're in KNOWLEDGE.md
- ✅ Requirements are clear before implementation starts
- ✅ Code reviews catch fewer issues because of upfront planning
- ✅ Team members can understand project state from memory files

---

*Last Updated: 2026-01-13*
