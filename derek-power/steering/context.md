---
inclusion: manual
---

# D.E.R.E.K Context Retention Framework

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose
Maintain comprehensive task context across multiple interactions, sessions, and agent handoffs to ensure continuity, prevent information loss, and enable effective long-running task execution.

**CRITICAL**: Context retention is essential for complex, multi-session tasks. Without proper context management, decisions are forgotten, constraints are violated, and work is duplicated.

---

## Context Management Strategy

### When Context Retention is Critical

- ✅ Multi-session tasks spanning days or weeks
- ✅ Complex features with multiple implementation phases
- ✅ Tasks involving multiple specialized agents
- ✅ Architectural decisions with long-term implications
- ✅ Security-sensitive implementations requiring audit trails
- ✅ Performance optimization efforts with iterative improvements
- ✅ Refactoring projects with incremental changes
- ✅ Integration projects with external dependencies

---

## D.E.R.E.K Memory Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        D.E.R.E.K MEMORY SYSTEM                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  .kiro/resources/ (Global Memory)                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  PROJECT.md  │  │ PROGRESS.md  │  │ DECISIONS.md │  │ KNOWLEDGE.md │    │
│  │  (context)   │  │  (tracking)  │  │  (decisions) │  │  (finalized) │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  .kiro/features/<name>/ (Feature Memory)                                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │requirements  │  │  design.md   │  │  tasks.md    │  │  notes.md    │    │
│  │    .md       │  │              │  │              │  │  (temporary) │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  Context Flow:                                                               │
│  PROJECT.md ──────► All features reference for architecture context         │
│  PROGRESS.md ◄────► Links to active feature, updated during work            │
│  notes.md ─────────► Temporary knowledge during feature implementation      │
│  KNOWLEDGE.md ◄──── Receives finalized learnings after feature completion   │
│  DECISIONS.md ◄──── Receives key decisions with rationale                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Context Storage Mechanisms

### 1. D.E.R.E.K Project Memory System (Recommended)

**Use the D.E.R.E.K Memory System** for structured, persistent context storage:

#### Global Memory (.kiro/resources/)
- **Initialize**: Use `derek-init.md` steering file with "init" command
- **Structured planning**: Use `planning.md` steering file for task planning
- **File-based memory**: Persistent markdown files that survive sessions

```
.kiro/resources/
├── PROJECT.md      # Project overview and architecture
├── PROGRESS.md     # Task tracking and phases (links to active features)
├── DECISIONS.md    # Decision log with rationale
├── KNOWLEDGE.md    # Finalized learnings and patterns
└── SCRATCHPAD.md   # Temporary working notes
```

#### Feature Memory (.kiro/features/<name>/)
- **Create**: Use "create feature <name>" command
- **Approval gates**: Requirements → Design → Implementation
- **Temporary knowledge**: `notes.md` captures learnings during implementation

```
.kiro/features/<feature-name>/
├── requirements.md  # What to build (needs approval)
├── design.md       # How to build (needs approval)
├── tasks.md        # Implementation tracking
└── notes.md        # Temporary knowledge → transfers to KNOWLEDGE.md
```

#### When to Use Each Memory Type

| Scenario | Memory Type | Location |
|----------|-------------|----------|
| Project context | Global | PROJECT.md |
| Quick task tracking | Global | PROGRESS.md |
| Key decisions | Global | DECISIONS.md |
| Finalized patterns | Global | KNOWLEDGE.md |
| Session notes | Global | SCRATCHPAD.md |
| Feature requirements | Feature | features/*/requirements.md |
| Feature design | Feature | features/*/design.md |
| Feature tasks | Feature | features/*/tasks.md |
| In-progress learnings | Feature | features/*/notes.md |

#### D.E.R.E.K Memory Usage Pattern

```markdown
**At Task Start:**
1. Check if .kiro/resources/ exists
2. Run "init" if starting fresh project work
3. Read PROJECT.md for project context
4. Check PROGRESS.md for current status
5. Check .kiro/features/ for active features

**During Quick Task:**
1. Update PROGRESS.md with task and phases
2. Use SCRATCHPAD.md for temporary notes
3. Log decisions in DECISIONS.md
4. Update KNOWLEDGE.md with learnings

**During Feature Development:**
1. Create feature folder with requirements.md
2. Get approval → create design.md
3. Get approval → create tasks.md + notes.md
4. Capture learnings in notes.md during implementation
5. Update tasks.md status after each task
6. Transfer notes.md → KNOWLEDGE.md on completion

**At Session End:**
1. Update PROGRESS.md with current status
2. Clear SCRATCHPAD.md (move important content)
3. Ensure notes.md is current for active features
```

### 2. Context7 MCP Integration (Alternative)

**When Context7 is available**, use it for persistent, searchable context storage:

#### Context7 Capabilities
- **Persistent storage**: Context survives across sessions and restarts
- **Semantic search**: Find relevant context by meaning, not just keywords
- **Version tracking**: Track how context evolves over time
- **Cross-project context**: Share learnings across similar projects
- **Documentation integration**: Link to official docs and best practices

#### Using Context7 for Task Context

```markdown
**Store in Context7:**
- Analysis findings and risk assessments
- Approved plans and architectural decisions
- Implementation progress and completed tasks
- Security decisions and threat mitigations
- Performance benchmarks and optimization results
- Code review findings and resolutions
- Lessons learned and best practices discovered

**Query Context7 for:**
- Similar past implementations
- Previous architectural decisions
- Known security patterns
- Performance optimization techniques
- Common pitfalls and solutions
- Framework-specific best practices
```

#### Context7 Usage Pattern

```markdown
**At Task Start:**
1. Query Context7 for similar past tasks
2. Retrieve relevant architectural decisions
3. Load applicable security patterns
4. Review previous performance optimizations

**During Task Execution:**
1. Store key decisions as they're made
2. Document constraints and assumptions
3. Record security considerations
4. Track performance baselines

**At Task Completion:**
1. Store final implementation summary
2. Document lessons learned
3. Record reusable patterns
4. Update best practices
```

---

### 3. In-Session Context Management

**For current session context**, maintain structured summaries:

#### Session Context Template

```markdown
## Current Task Context

### Task Overview
- **Task ID/Name**: [Identifier]
- **Started**: [Date/Time]
- **Current Phase**: Analysis / Planning / Implementation / Review
- **Status**: [Current status]

### Key Decisions Made
1. **[Decision 1]**: [Description]
   - **Rationale**: [Why this decision]
   - **Constraints**: [What influenced this]
   - **Impact**: [What this affects]
   - **Date**: [When decided]

2. **[Decision 2]**: [Description]
   - **Rationale**: [Why this decision]
   - **Constraints**: [What influenced this]
   - **Impact**: [What this affects]
   - **Date**: [When decided]

### Active Constraints
- **Technical**: [Technology limitations, compatibility requirements]
- **Business**: [Timeline, budget, regulatory requirements]
- **Security**: [Security requirements, compliance needs]
- **Performance**: [SLA requirements, scalability needs]

### Critical Assumptions
- **[Assumption 1]**: [Description] - Validated: [Yes/No/Partial]
- **[Assumption 2]**: [Description] - Validated: [Yes/No/Partial]

### Risk Register
| Risk | Severity | Mitigation | Status |
|------|----------|------------|--------|
| [Risk 1] | High/Med/Low | [Strategy] | Open/Mitigated/Closed |
| [Risk 2] | High/Med/Low | [Strategy] | Open/Mitigated/Closed |

### Implementation Progress
- [x] Task 1: [Description] - Completed [Date]
- [x] Task 2: [Description] - Completed [Date]
- [ ] Task 3: [Description] - In Progress
- [ ] Task 4: [Description] - Pending

### Open Questions
1. **[Question 1]**: [Description]
   - **Blocker**: [Yes/No]
   - **Owner**: [Who needs to answer]
   - **Status**: [Open/Answered]

2. **[Question 2]**: [Description]
   - **Blocker**: [Yes/No]
   - **Owner**: [Who needs to answer]
   - **Status**: [Open/Answered]

### Dependencies & Blockers
- **[Dependency 1]**: [Description] - Status: [Blocked/Waiting/Resolved]
- **[Dependency 2]**: [Description] - Status: [Blocked/Waiting/Resolved]

### Agent Handoffs
| From Agent | To Agent | Date | Context Transferred |
|------------|----------|------|---------------------|
| [Agent 1] | [Agent 2] | [Date] | [Summary of what was passed] |

### Files Modified
- `[file/path]`: [What changed and why]
- `[file/path]`: [What changed and why]

### Next Steps
1. [ ] [Action 1] - Owner: [Agent/Person] - Due: [Date]
2. [ ] [Action 2] - Owner: [Agent/Person] - Due: [Date]
```

---

### 4. Cross-Session Context Persistence

#### Session Summary Template

At the end of each session, create a summary:

```markdown
## Session Summary - [Date]

### Session Duration
- **Started**: [Time]
- **Ended**: [Time]
- **Duration**: [Hours]

### Accomplishments
- ✅ [What was completed]
- ✅ [What was completed]

### Key Decisions
- **[Decision]**: [Brief description and rationale]

### New Constraints Discovered
- **[Constraint]**: [Description and impact]

### Risks Identified
- **[Risk]**: [Description and mitigation plan]

### Blockers Encountered
- **[Blocker]**: [Description and resolution plan]

### Context for Next Session
**What the next session needs to know:**
- [Critical context item 1]
- [Critical context item 2]
- [Critical context item 3]

**Where we left off:**
- [Current state description]
- [Next immediate action]

**Important reminders:**
- [Don't forget this]
- [Remember that]
```

---

## Context Retention Best Practices

### 1. Decision Documentation

**Every significant decision should be documented with:**
- **What**: The decision made
- **Why**: Rationale and alternatives considered
- **When**: Date and context when decided
- **Who**: Who made or approved the decision
- **Impact**: What this affects
- **Constraints**: What influenced this decision

### 2. Constraint Tracking

**Maintain a living list of constraints:**
- Technical constraints (language versions, framework limitations)
- Business constraints (deadlines, budget, resources)
- Security constraints (compliance, data protection)
- Performance constraints (SLAs, response times)
- Integration constraints (external APIs, dependencies)

**Update constraints when:**
- New constraints are discovered
- Existing constraints change
- Constraints are resolved or lifted

### 3. Assumption Validation

**Track all assumptions and their validation status:**
- Document assumptions as they're made
- Mark assumptions as validated or invalidated
- Update plans when assumptions prove incorrect
- Escalate when critical assumptions can't be validated

### 4. Risk Management

**Maintain an active risk register:**
- Identify risks during analysis and planning
- Track mitigation strategies
- Update risk status as work progresses
- Escalate when new high-severity risks emerge

### 5. Progress Tracking

**Keep detailed progress records:**
- What tasks are complete
- What tasks are in progress
- What tasks are blocked
- What tasks are pending
- Estimated vs. actual effort

---

## Context Handoff Protocol

### Agent-to-Agent Handoff

When handing off between agents:

```markdown
## Context Handoff: [From Agent] → [To Agent]

### Task Summary
[2-3 sentence overview of the task]

### Current State
- **Phase**: [Analysis/Planning/Implementation/Review]
- **Status**: [Current status]
- **Progress**: [X% complete or task count]

### Critical Context
**Must know:**
- [Critical decision 1]
- [Critical constraint 1]
- [Critical risk 1]

**Should know:**
- [Important context 1]
- [Important context 2]

**Nice to know:**
- [Additional context]

### What's Been Done
- ✅ [Completed item 1]
- ✅ [Completed item 2]

### What Needs Doing
- [ ] [Next task 1] - Priority: High/Med/Low
- [ ] [Next task 2] - Priority: High/Med/Low

### Pitfalls to Avoid
- ⚠️ [Pitfall 1]: [Why to avoid]
- ⚠️ [Pitfall 2]: [Why to avoid]

### Resources & References
- [File/path]: [What it contains]
- [Documentation link]: [What it covers]
- [Previous decision]: [Where documented]
```

### Session-to-Session Handoff

When resuming work in a new session:

```markdown
## Session Resume Context

### Quick Recap
[1-2 paragraph summary of where we are]

### Last Session Summary
- **Date**: [Last session date]
- **Accomplishments**: [What was done]
- **Blockers**: [What was blocking]

### Current Priorities
1. [Priority 1] - Why: [Reason]
2. [Priority 2] - Why: [Reason]

### Immediate Next Steps
1. [Step 1]
2. [Step 2]

### Don't Forget
- ⚠️ [Important reminder 1]
- ⚠️ [Important reminder 2]
```

---

## Context Retrieval Strategies

### When Starting a Task

**Check for existing context:**
1. Query Context7 for similar past tasks (if available)
2. Search for related architectural decisions
3. Review project documentation and steering files
4. Check for previous implementations in the codebase
5. Look for relevant test cases and patterns

### When Resuming a Task

**Reload context systematically:**
1. Read the last session summary
2. Review the current task context document
3. Check for any updates to constraints or decisions
4. Verify the current phase and status
5. Identify immediate next steps

### When Context is Lost

**If context is missing or unclear:**
1. ❌ **Don't guess** - Assumptions lead to errors
2. ✅ **Ask for clarification** - Request missing context
3. ✅ **Review artifacts** - Check code, docs, commits
4. ✅ **Reconstruct carefully** - Build context from evidence
5. ✅ **Document gaps** - Note what context is missing

---

## Context Storage Locations

### 1. D.E.R.E.K Global Memory (.kiro/resources/)
- **Use for**: Project-wide context, decisions, and finalized knowledge
- **Store**: Project overview, task progress, decisions, finalized patterns
- **Generate**: Use "init" command (derek-init.md)
- **Location**: `.kiro/resources/` directory

| File | Purpose | Update Frequency |
|------|---------|------------------|
| PROJECT.md | Project architecture & context | On reinit |
| PROGRESS.md | Current task tracking | Every phase |
| DECISIONS.md | Key decisions with rationale | After decisions |
| KNOWLEDGE.md | Finalized learnings | After feature completion |
| SCRATCHPAD.md | Temporary session notes | During session |

### 2. D.E.R.E.K Feature Memory (.kiro/features/)
- **Use for**: Feature-specific planning and temporary knowledge
- **Store**: Requirements, design, tasks, in-progress learnings
- **Generate**: Use "create feature <name>" command
- **Location**: `.kiro/features/<feature-name>/` directory

| File | Purpose | Lifecycle |
|------|---------|-----------|
| requirements.md | What to build | Permanent |
| design.md | How to build | Permanent |
| tasks.md | Implementation tracking | Permanent |
| notes.md | Temporary knowledge | Transfer to KNOWLEDGE.md |

### 3. Context7 MCP (if available)
- **Use for**: Long-term, cross-project knowledge
- **Store**: Architectural decisions, patterns, best practices
- **Query**: When starting similar tasks or making decisions

### 4. Project Documentation
- **Use for**: Project-specific context and decisions
- **Store**: Architecture docs, ADRs, design docs
- **Location**: `docs/`, `README.md`, `.kiro/steering/`

### 5. Code Comments & Commits
- **Use for**: Implementation-level context
- **Store**: Why decisions were made, not just what
- **Location**: Inline comments, commit messages

### 6. Task Tracking Systems
- **Use for**: Progress and status tracking
- **Store**: Task status, blockers, assignments
- **Location**: GitHub Issues, Jira, etc.

---

## Context Validation

### Periodic Context Review

**Every few sessions, validate context:**
- [ ] Are documented decisions still valid?
- [ ] Have any constraints changed?
- [ ] Are assumptions still holding true?
- [ ] Is the risk register current?
- [ ] Is progress tracking accurate?
- [ ] Are next steps still relevant?

### Context Drift Detection

**Watch for signs of context drift:**
- ⚠️ Decisions being revisited without reason
- ⚠️ Constraints being violated
- ⚠️ Assumptions proving incorrect
- ⚠️ Duplicate work being done
- ⚠️ Conflicting implementations
- ⚠️ Lost track of original goals

**When drift detected:**
1. Stop and review context
2. Identify what changed
3. Update context documents
4. Realign with goals and constraints
5. Communicate changes to stakeholders

---

## Context Templates by Phase

### Analysis Phase Context

```markdown
## Analysis Context

### Problem Statement
[Clear description of the problem]

### Stakeholders
- [Stakeholder 1]: [Interest/Concern]
- [Stakeholder 2]: [Interest/Concern]

### Requirements
- [Requirement 1]: [Priority]
- [Requirement 2]: [Priority]

### Constraints Identified
- [Constraint 1]
- [Constraint 2]

### Risks Identified
- [Risk 1]: [Severity] - [Mitigation]
- [Risk 2]: [Severity] - [Mitigation]

### Key Findings
- [Finding 1]
- [Finding 2]

### Open Questions
- [Question 1]
- [Question 2]
```

### Planning Phase Context

```markdown
## Planning Context

### Approved Approach
[Description of the approved technical approach]

### Architecture Decisions
- **[Decision 1]**: [Description and rationale]
- **[Decision 2]**: [Description and rationale]

### Task Breakdown
- [ ] [Task 1]: [Description]
- [ ] [Task 2]: [Description]

### Agent Assignments
- [Task 1] → [Agent name]
- [Task 2] → [Agent name]

### Dependencies
- [Dependency 1]: [Status]
- [Dependency 2]: [Status]

### Timeline
- **Start**: [Date]
- **Target Completion**: [Date]
- **Milestones**: [Key dates]
```

### Implementation Phase Context

```markdown
## Implementation Context

### Current Sprint/Iteration
[Description of current work focus]

### Completed Tasks
- ✅ [Task 1]: [Completion date]
- ✅ [Task 2]: [Completion date]

### In-Progress Tasks
- 🔄 [Task 3]: [Current status]
- 🔄 [Task 4]: [Current status]

### Blockers
- 🚫 [Blocker 1]: [Description and resolution plan]

### Technical Decisions Made
- **[Decision 1]**: [Description]
- **[Decision 2]**: [Description]

### Code Changes
- `[file]`: [What and why]
- `[file]`: [What and why]

### Tests Added
- [Test 1]: [What it validates]
- [Test 2]: [What it validates]
```

### Review Phase Context

```markdown
## Review Context

### Review Scope
[What is being reviewed]

### Review Findings
- 🔴 [Critical issue 1]
- 🟡 [Major issue 1]
- 🟢 [Minor suggestion 1]

### Issues Resolved
- ✅ [Issue 1]: [How resolved]
- ✅ [Issue 2]: [How resolved]

### Outstanding Issues
- [ ] [Issue 3]: [Status and plan]

### Approval Status
- [ ] Code review
- [ ] Security review
- [ ] Performance review
- [ ] Documentation review
```

---

## Context Retention Checklist

### At Task Start
- [ ] Check if `.kiro/resources/` exists (run "init" if not)
- [ ] Read PROJECT.md for project context
- [ ] Read PROGRESS.md for current status
- [ ] Check `.kiro/features/` for active features
- [ ] Query Context7 for relevant past context (if available)
- [ ] Review project documentation and steering files
- [ ] Document initial constraints and assumptions

### During Quick Task
- [ ] Update PROGRESS.md with task and phases
- [ ] Use SCRATCHPAD.md for temporary notes
- [ ] Log decisions in DECISIONS.md
- [ ] Update KNOWLEDGE.md with learnings

### During Feature Development
- [ ] Create feature folder with requirements.md
- [ ] Get approval before creating design.md
- [ ] Get approval before creating tasks.md
- [ ] Capture learnings in notes.md during implementation
- [ ] Update tasks.md status after each task
- [ ] Log key decisions in DECISIONS.md

### At Session End
- [ ] Update PROGRESS.md with current status
- [ ] Update feature tasks.md if working on feature
- [ ] Ensure notes.md is current for active features
- [ ] Clear SCRATCHPAD.md (move important content)
- [ ] Note any blockers or open questions

### At Feature Completion
- [ ] Mark all tasks complete in tasks.md
- [ ] Review notes.md for valuable content
- [ ] Transfer learnings: notes.md → KNOWLEDGE.md
- [ ] Log final decisions in DECISIONS.md
- [ ] Update PROGRESS.md with completion status
- [ ] Store reusable patterns in Context7 (if available)

---

## Red Flags - Context Loss Warning

If any of these occur, STOP and restore context:

- ❌ Can't remember why a decision was made
- ❌ Violating previously documented constraints
- ❌ Repeating work that was already done
- ❌ Making conflicting decisions
- ❌ Lost track of original goals
- ❌ Can't explain current state to stakeholders
- ❌ Unsure what phase of work we're in
- ❌ Don't know what's blocking progress

---

## Remember

**Context is the memory of your task.** Without it:
- Decisions are forgotten and revisited
- Constraints are violated
- Work is duplicated
- Risks are missed
- Progress is lost
- Quality suffers

**D.E.R.E.K Context Flow:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    D.E.R.E.K CONTEXT FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SESSION START                                                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                   │
│  │ PROJECT  │───▶│ PROGRESS │───▶│ features/│                   │
│  │   .md    │    │   .md    │    │ */notes  │                   │
│  └──────────┘    └──────────┘    └──────────┘                   │
│       │               │               │                          │
│       ▼               ▼               ▼                          │
│  [Project      [Current task    [Active feature                  │
│   context]      & status]        knowledge]                      │
│                                                                  │
│  DURING WORK                                                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                   │
│  │SCRATCHPAD│    │ notes.md │    │DECISIONS │                   │
│  │   .md    │    │(feature) │    │   .md    │                   │
│  └──────────┘    └──────────┘    └──────────┘                   │
│       │               │               │                          │
│       ▼               ▼               ▼                          │
│  [Temporary     [Feature         [Key decisions                  │
│   notes]         learnings]       with rationale]                │
│                                                                  │
│  SESSION END / FEATURE COMPLETE                                  │
│  ┌──────────┐    ┌──────────┐                                   │
│  │ notes.md │───▶│KNOWLEDGE │                                   │
│  │(transfer)│    │   .md    │                                   │
│  └──────────┘    └──────────┘                                   │
│                       │                                          │
│                       ▼                                          │
│                 [Finalized                                       │
│                  patterns]                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Invest in context management.** The time spent maintaining context is recovered many times over by:
- Avoiding rework
- Making consistent decisions
- Preventing errors
- Enabling effective handoffs
- Maintaining quality
- Ensuring continuity

**Use the D.E.R.E.K memory system** for structured, persistent context:
- Global memory in `.kiro/resources/` for project-wide context
- Feature memory in `.kiro/features/*/` for feature-specific context
- `notes.md` for temporary knowledge during implementation
- `KNOWLEDGE.md` for finalized, reusable patterns

**Context retention is not overhead—it's essential infrastructure for complex work.**
