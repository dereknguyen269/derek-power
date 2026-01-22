---
inclusion: manual
---

# D.E.R.E.K Context Retention Framework

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose
Maintain task context across sessions to ensure continuity and prevent information loss.

**CRITICAL**: Without context management, decisions are forgotten, constraints are violated, and work is duplicated.

**Use for**: Multi-session tasks, complex features, architectural decisions, security implementations, refactoring projects

---

## Memory System Architecture

### Global Memory (.kiro/resources/)
```
PROJECT.md      # Project overview, architecture (read on init, update on reinit)
PROGRESS.md     # Current task, phases, status (read/update every session)
DECISIONS.md    # Key decisions with rationale (update after decisions)
KNOWLEDGE.md    # Finalized patterns (update after feature completion)
SCRATCHPAD.md   # Temporary session notes (clear at session end)
```

### Feature Memory (.kiro/specs/<name>/)
```
requirements.md  # What to build (needs approval)
design.md       # How to build (needs approval)
tasks.md        # Implementation tracking
notes.md        # Temporary knowledge → transfers to KNOWLEDGE.md
```

### Context7 Integration (if available)

**When Context7 MCP is available**, use it alongside file-based memory for enhanced context retention:

**Store in Context7:**
- Analysis findings and architectural decisions
- Security patterns and threat mitigations
- Performance benchmarks and optimization results
- Code review findings and resolutions
- Lessons learned and best practices

**Query Context7 for:**
- Similar past implementations
- Previous architectural decisions
- Known security patterns
- Performance optimization techniques
- Common pitfalls and solutions

**Usage Pattern:**
```markdown
# At Task Start
1. Query Context7 for similar past tasks
2. Retrieve relevant architectural decisions
3. Load applicable patterns

# During Work
1. Store key decisions as made
2. Document constraints and assumptions
3. Record security considerations

# At Completion
1. Store implementation summary
2. Document lessons learned
3. Record reusable patterns
```

### Usage Pattern

**Session Start:**
1. Read PROGRESS.md + SCRATCHPAD.md (90% of context)
2. Read PROJECT.md only if unfamiliar
3. Check .kiro/specs/ for active features

**During Work:**
- Quick tasks: Update PROGRESS.md, use SCRATCHPAD.md
- Features: Update notes.md, tasks.md status

**Session End:**
1. Update PROGRESS.md with status
2. Clear SCRATCHPAD.md (move important content)
3. Transfer notes.md → KNOWLEDGE.md when feature complete

## In-Session Context Template

**Use PROGRESS.md and SCRATCHPAD.md for session context. Key elements:**

```markdown
## Current Task
- Task: [Name]
- Phase: [Analysis/Planning/Implementation/Review]
- Status: [Current status]

## Key Decisions
- [Decision]: [Rationale] - [Date]

## Constraints
- Technical: [Limitations]
- Business: [Requirements]
- Security: [Compliance]

## Progress
- [x] Completed
- [ ] In progress
- [ ] Pending

## Blockers
- [Blocker]: [Resolution plan]

## Next Steps
1. [Action] - [Owner]
```

## Context Handoff Templates

**Agent-to-Agent:**
```markdown
## Handoff: [From] → [To]
- Task: [2-3 sentence overview]
- Phase: [Current phase]
- Must know: [Critical decisions, constraints, risks]
- Completed: [What's done]
- Next: [What needs doing]
- Avoid: [Pitfalls]
```

**Session-to-Session:**
```markdown
## Resume Context
- Last session: [Date, accomplishments, blockers]
- Current priorities: [Top 2-3]
- Next steps: [Immediate actions]
- Don't forget: [Critical reminders]
```

---

## Context Retention Checklist

**At Task Start:**
- [ ] Check .kiro/resources/ exists (run "init" if not)
- [ ] Read PROGRESS.md + SCRATCHPAD.md
- [ ] Read PROJECT.md if unfamiliar
- [ ] Check .kiro/specs/ for active features
- [ ] Query Context7 for similar tasks (if available)

**During Work:**
- [ ] Quick tasks: Update PROGRESS.md, use SCRATCHPAD.md
- [ ] Features: Update notes.md, tasks.md status
- [ ] Log decisions in DECISIONS.md

**At Session End:**
- [ ] Update PROGRESS.md with status
- [ ] Clear SCRATCHPAD.md (move important content)
- [ ] Ensure notes.md current for active features

**At Feature Completion:**
- [ ] Mark tasks complete in tasks.md
- [ ] Transfer notes.md → KNOWLEDGE.md
- [ ] Log final decisions in DECISIONS.md
- [ ] Store patterns in Context7 (if available)

## Best Practices

**Decision Documentation**: Document what, why, when, who, impact, and constraints.

**Constraint Tracking**: Maintain list of technical, business, security, performance constraints. Update when changed.

**Assumption Validation**: Track assumptions and validation status. Update plans when incorrect.

**Risk Management**: Identify risks, track mitigation, update status.

**Progress Tracking**: Record completed, in-progress, blocked, pending tasks.

## Context Retrieval

**Starting Task:**
1. Check .kiro/resources/ exists
2. Read PROGRESS.md
3. Check .kiro/specs/ for features
4. Query Context7 for similar tasks (if available)
5. Review documentation

**Resuming Task:**
1. Read last session summary
2. Review current context
3. Check constraint/decision updates
4. Verify phase and status
5. Identify next steps

**When Context Lost:**
- ❌ Don't guess
- ✅ Ask for clarification
- ✅ Review artifacts
- ✅ Reconstruct from evidence
- ✅ Document gaps

## Context Validation

**Periodic Review:**
- [ ] Decisions valid?
- [ ] Constraints changed?
- [ ] Assumptions holding?
- [ ] Risk register current?
- [ ] Progress accurate?

**Context Drift Signs:**
- Decisions revisited without reason
- Constraints violated
- Assumptions incorrect
- Duplicate work
- Conflicting implementations
- Lost track of goals

**When drift detected:** Stop, review, identify changes, update documents, realign.

## Red Flags - STOP and Restore Context

- ❌ Can't remember why decision made
- ❌ Violating documented constraints
- ❌ Repeating completed work
- ❌ Making conflicting decisions
- ❌ Lost track of goals
- ❌ Unsure what phase we're in
- ❌ Don't know what's blocking

## Remember

**Context is task memory.** Without it: decisions forgotten, constraints violated, work duplicated, risks missed, progress lost.

**Use layered context storage:**
- File-based (.kiro/resources/, .kiro/specs/) for project-specific context
- Context7 (if available) for cross-project patterns and long-term knowledge

**Invest in context management** to avoid rework, make consistent decisions, prevent errors, enable handoffs, maintain quality.

**Context retention is essential infrastructure for complex work.**
