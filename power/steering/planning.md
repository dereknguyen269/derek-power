---
inclusion: manual
name: planning
description: Transforms workflow to use persistent markdown files for planning, progress tracking, and knowledge storage. Supports feature planning with dedicated folders for requirements, design, and tasks. Use when starting complex tasks, multi-step projects, research tasks, or when the user mentions planning, organizing work, or feature development.
category: planning
---
# Planning

Work like Manus: Use persistent markdown files as your "working memory on disk."

## Two Planning Modes

This steering file supports two planning modes:

| Mode | Use When | Location |
|------|----------|----------|
| **Quick Planning** | Simple tasks, bug fixes, small features | `.kiro/resources/PROGRESS.md` |
| **Feature Planning** | Complex features, new modules, multi-phase work | `.kiro/features/<feature-name>/` |

---

## Workflow Diagrams

### Overall Planning Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER REQUEST                                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │   Is this a complex feature?  │
                    │   (multiple files, sessions,  │
                    │    or components)             │
                    └───────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            ┌───────────┐                   ┌───────────────┐
            │    NO     │                   │      YES      │
            └───────────┘                   └───────────────┘
                    │                               │
                    ▼                               ▼
    ┌───────────────────────────┐   ┌───────────────────────────────┐
    │     QUICK PLANNING        │   │      FEATURE PLANNING         │
    │  .kiro/resources/         │   │  .kiro/features/<name>/       │
    │  └── PROGRESS.md          │   │  ├── requirements.md          │
    │                           │   │  ├── design.md                │
    │                           │   │  ├── tasks.md                 │
    │                           │   │  └── notes.md  📝 (temp)      │
    └───────────────────────────┘   └───────────────────────────────┘
```

### Quick Planning Workflow

```
┌──────────────────────────────────────────────────────────────────┐
│                      QUICK PLANNING MODE                          │
└──────────────────────────────────────────────────────────────────┘

    ┌─────────────┐
    │   START     │
    └──────┬──────┘
           │
           ▼
    ┌─────────────────────────┐
    │ 1. Update PROGRESS.md   │◄─────────────────────────┐
    │    with goal & phases   │                          │
    └──────────┬──────────────┘                          │
               │                                         │
               ▼                                         │
    ┌─────────────────────────┐                          │
    │ 2. Execute phase        │                          │
    │    (research/build)     │                          │
    └──────────┬──────────────┘                          │
               │                                         │
               ▼                                         │
    ┌─────────────────────────┐                          │
    │ 3. Store findings in    │                          │
    │    KNOWLEDGE.md         │                          │
    └──────────┬──────────────┘                          │
               │                                         │
               ▼                                         │
    ┌─────────────────────────┐                          │
    │ 4. Mark phase [x] in    │                          │
    │    PROGRESS.md          │                          │
    └──────────┬──────────────┘                          │
               │                                         │
               ▼                                         │
    ┌─────────────────────────┐      ┌────────────┐     │
    │   More phases left?     │─YES─▶│ Next phase │─────┘
    └──────────┬──────────────┘      └────────────┘
               │ NO
               ▼
    ┌─────────────────────────┐
    │ 5. Log decisions in     │
    │    DECISIONS.md         │
    └──────────┬──────────────┘
               │
               ▼
    ┌─────────────┐
    │    DONE     │
    └─────────────┘
```

### Feature Planning Workflow

```
┌──────────────────────────────────────────────────────────────────┐
│                     FEATURE PLANNING MODE                         │
└──────────────────────────────────────────────────────────────────┘

┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: REQUIREMENTS                                           │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ Create .kiro/features/<name>/requirements.md                │ │
│  │ • Problem statement    • User stories                       │ │
│  │ • Functional reqs      • Non-functional reqs                │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  ⛔ APPROVAL    │◄────┐
                  │     GATE        │     │
                  └────────┬────────┘     │
                           │              │
              ┌────────────┴────────────┐ │
              │                         │ │
              ▼                         ▼ │
       ┌────────────┐           ┌────────────┐
       │  APPROVED  │           │  REJECTED  │──► Revise requirements
       └─────┬──────┘           └────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: DESIGN                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ Create .kiro/features/<name>/design.md                      │ │
│  │ • Architecture          • Data model                        │ │
│  │ • API design            • Security design                   │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  ⛔ APPROVAL    │◄────┐
                  │     GATE        │     │
                  └────────┬────────┘     │
                           │              │
              ┌────────────┴────────────┐ │
              │                         │ │
              ▼                         ▼ │
       ┌────────────┐           ┌────────────┐
       │  APPROVED  │           │  REJECTED  │──► Revise design
       └─────┬──────┘           └────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: TASKS                                                  │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ Create .kiro/features/<name>/tasks.md                       │ │
│  │ • Task breakdown        • Dependencies                      │ │
│  │ • Estimates             • Acceptance criteria               │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: IMPLEMENTATION                                         │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    ┌──────────────┐                         │ │
│  │                    │  Next Task   │◄────────────────┐       │ │
│  │                    └──────┬───────┘                 │       │ │
│  │                           │                         │       │ │
│  │                           ▼                         │       │ │
│  │                    ┌──────────────┐                 │       │ │
│  │                    │   Execute    │                 │       │ │
│  │                    └──────┬───────┘                 │       │ │
│  │                           │                         │       │ │
│  │                           ▼                         │       │ │
│  │                    ┌──────────────┐                 │       │ │
│  │                    │ Update tasks │                 │       │ │
│  │                    │   status     │                 │       │ │
│  │                    └──────┬───────┘                 │       │ │
│  │                           │                         │       │ │
│  │                           ▼                         │       │ │
│  │                    ┌──────────────┐                 │       │ │
│  │                    │ Capture in   │                 │       │ │
│  │                    │  notes.md    │                 │       │ │
│  │                    └──────┬───────┘                 │       │ │
│  │                           │                         │       │ │
│  │                           ▼                         │       │ │
│  │                    ┌──────────────┐    ┌─────┐     │       │ │
│  │                    │ More tasks?  │─YES│     │─────┘       │ │
│  │                    └──────┬───────┘    └─────┘             │ │
│  │                           │ NO                              │ │
│  │                           ▼                                 │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: COMPLETION                                             │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ • Review notes.md for valuable content                      │ │
│  │ • Transfer learnings: notes.md → KNOWLEDGE.md               │ │
│  │ • Log decisions in DECISIONS.md                             │ │
│  │ • Update PROGRESS.md with completion                        │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    DONE     │
                    └─────────────┘
```

### Memory System Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROJECT MEMORY SYSTEM                                │
│                         .kiro/resources/                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  PROJECT.md  │  │ PROGRESS.md  │  │ DECISIONS.md │  │ KNOWLEDGE.md │    │
│  │              │  │              │  │              │  │              │    │
│  │  Project     │  │  Current     │  │  Decision    │  │  Finalized   │    │
│  │  overview    │  │  task &      │  │  log with    │  │  patterns &  │    │
│  │  & arch      │  │  phases      │  │  rationale   │  │  learnings   │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
│         │                 │                 │                 ▲             │
│         │    ┌────────────┴─────────────────┴─────────────────┘             │
│         │    │                                                              │
│         ▼    ▼                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    FEATURE FOLDERS                                   │   │
│  │                    .kiro/features/                                   │   │
│  │  ┌─────────────────────┐  ┌─────────────────────┐                   │   │
│  │  │   authentication/   │  │ payment-integration/ │  ...             │   │
│  │  │  ├─ requirements.md │  │  ├─ requirements.md  │                  │   │
│  │  │  ├─ design.md       │  │  ├─ design.md        │                  │   │
│  │  │  ├─ tasks.md        │  │  ├─ tasks.md         │                  │   │
│  │  │  └─ notes.md 📝     │  │  └─ notes.md 📝      │                  │   │
│  │  └─────────────────────┘  └─────────────────────┘                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Data Flow:                                                                  │
│  ─────────                                                                   │
│  PROJECT.md ──────► Referenced by all features for architecture context     │
│  PROGRESS.md ◄────► Links to active feature, updated during work            │
│  DECISIONS.md ◄─── Receives decisions from feature implementations          │
│  KNOWLEDGE.md ◄─── Receives learnings from notes.md after completion        │
│                                                                              │
│  notes.md Lifecycle:                                                         │
│  ──────────────────                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────────┐          │
│  │ Created  │───►│ Updated  │───►│ Reviewed │───►│ Transferred  │          │
│  │ at start │    │ during   │    │ at end   │    │ to KNOWLEDGE │          │
│  │ of impl  │    │ impl     │    │          │    │ .md          │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────────┘          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Approval Gate Detail

```
                    ┌─────────────────────────────────────┐
                    │         APPROVAL GATE               │
                    │                                     │
                    │  "approve requirements"             │
                    │  "requirements approved"            │
                    │           OR                        │
                    │  "approve design"                   │
                    │  "design approved"                  │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
            ┌───────────────┐            ┌───────────────┐
            │   APPROVED    │            │   FEEDBACK    │
            │               │            │               │
            │ ✅ Proceed to │            │ 🔄 Revise     │
            │   next phase  │            │   document    │
            └───────────────┘            └───────────────┘
                    │                             │
                    │                             │
                    ▼                             ▼
            ┌───────────────┐            ┌───────────────┐
            │ Generate next │            │ Update based  │
            │ document      │            │ on feedback   │
            └───────────────┘            └───────────────┘
                                                  │
                                                  │
                                                  ▼
                                         ┌───────────────┐
                                         │ Re-request    │
                                         │ approval      │
                                         └───────────────┘
```

---

## Integration with Project Memory System

The **Project Memory System** in `.kiro/resources/` provides global project context:

| Memory File | Purpose | Relationship to Specs |
|-------------|---------|----------------------|
| `PROJECT.md` | Project overview and architecture | Referenced by all specs |
| `PROGRESS.md` | Quick task tracking | Links to active specs |
| `DECISIONS.md` | Global decision log | Specs reference for consistency |
| `KNOWLEDGE.md` | Patterns and learnings | Updated from spec implementations |
| `SCRATCHPAD.md` | Temporary session notes | Working area during spec work |

**Feature folders** (`.kiro/features/<feature>/`) contain feature-specific planning:
- Self-contained feature documentation
- Isolated from other features
- Linked to global memory for context

---

## Quick Start

### For Simple Tasks (Quick Planning)
```
1. Check if `.kiro/resources/` exists
2. Update `PROGRESS.md` with task and phases
3. Work through phases, updating after each
4. Log decisions in `DECISIONS.md`
```

### For Complex Features (Feature Planning)
```
1. Create feature folder: `.kiro/features/<feature-name>/`
2. Generate requirements.md → Get approval
3. Generate design.md → Get approval  
4. Generate tasks.md → Get approval
5. Implement tasks, updating progress
6. Link findings to global KNOWLEDGE.md
```

---

# Part 1: Quick Planning Mode

## The Memory File Pattern

For non-trivial tasks that don't need full specs:

| File | Purpose | When to Update |
|------|---------|----------------|
| `PROGRESS.md` | Track current task, phases, status | After each phase |
| `KNOWLEDGE.md` | Store findings, patterns | During research |
| `DECISIONS.md` | Log decisions with rationale | After key decisions |
| `SCRATCHPAD.md` | Temporary working notes | During session |

## Core Workflow

```
Loop 1: Update PROGRESS.md with goal and phases
Loop 2: Research → save to KNOWLEDGE.md → update PROGRESS.md
Loop 3: Read KNOWLEDGE.md → create deliverable → update PROGRESS.md
Loop 4: Log decisions in DECISIONS.md → deliver final output
```

### The Loop in Detail

**Before each major action:**
```bash
Read .kiro/resources/PROGRESS.md   # Refresh goals in attention window
Read .kiro/resources/PROJECT.md    # Refresh project context (if exists)
```

**After each phase:**
```bash
Edit .kiro/resources/PROGRESS.md   # Mark [x], update status
```

---

# Part 2: Feature Planning Development

## When to Use Feature Planning

Use feature planning for:
- ✅ New features requiring multiple files/components
- ✅ Authentication, authorization systems
- ✅ API endpoints with complex logic
- ✅ Database schema changes
- ✅ Integration with external services
- ✅ Refactoring major components
- ✅ Features spanning multiple sessions

Skip feature planning for:
- ❌ Bug fixes
- ❌ Single-file changes
- ❌ Configuration updates
- ❌ Documentation updates

---

## Feature Folder Structure

Each feature gets its own folder under `.kiro/features/`:

```
.kiro/
├── resources/                    # Global Project Memory
│   ├── PROJECT.md
│   ├── PROGRESS.md              # Links to active features
│   ├── DECISIONS.md
│   ├── KNOWLEDGE.md             # Finalized learnings (from completed features)
│   └── SCRATCHPAD.md
│
└── features/                     # Feature Specifications
    ├── authentication/           # Example: Auth feature
    │   ├── requirements.md       # What to build
    │   ├── design.md            # How to build
    │   ├── tasks.md             # Implementation tasks
    │   └── notes.md             # 📝 Temporary knowledge during implementation
    │
    ├── payment-integration/      # Example: Payments
    │   ├── requirements.md
    │   ├── design.md
    │   ├── tasks.md
    │   └── notes.md
    │
    └── user-notifications/       # Example: Notifications
        ├── requirements.md
        ├── design.md
        ├── tasks.md
        └── notes.md
```

### Feature Files Purpose

| File | Purpose | When to Update | Lifecycle |
|------|---------|----------------|-----------|
| `requirements.md` | What to build | During requirements phase | Permanent |
| `design.md` | How to build | During design phase | Permanent |
| `tasks.md` | Implementation tracking | During implementation | Permanent |
| `notes.md` | Temporary knowledge capture | During implementation | Temporary → Transfer to KNOWLEDGE.md |

### notes.md - Temporary Knowledge File

The `notes.md` file captures knowledge **during** implementation before the feature is complete:

```markdown
# [Feature Name] - Implementation Notes

## Purpose
Temporary storage for discoveries, gotchas, and learnings during implementation.
Transfer valuable content to `.kiro/resources/KNOWLEDGE.md` when feature is complete.

---

## Discoveries

### [Date] - [Topic]
**Context**: [What you were doing]
**Finding**: [What you discovered]
**Impact**: [How this affects implementation]

---

## Gotchas & Pitfalls

| Issue | Cause | Solution |
|-------|-------|----------|
| [Issue] | [Why it happened] | [How to fix/avoid] |

---

## Code Snippets

### [Snippet Name]
**Purpose**: [What this does]
```[language]
// Useful code discovered during implementation
```

---

## External Resources

| Resource | URL | Why Useful |
|----------|-----|------------|
| [Name] | [URL] | [Description] |

---

## Questions Answered

| Question | Answer | Source |
|----------|--------|--------|
| [Question] | [Answer] | [Where found] |

---

## Transfer Checklist

Before completing feature, review and transfer:
- [ ] Valuable patterns → KNOWLEDGE.md
- [ ] Reusable snippets → KNOWLEDGE.md
- [ ] Gotchas for others → KNOWLEDGE.md
- [ ] Decisions made → DECISIONS.md

---
*Last Updated: [date]*
```

### When to Use notes.md vs KNOWLEDGE.md

| Scenario | Use notes.md | Use KNOWLEDGE.md |
|----------|--------------|------------------|
| Discovery during coding | ✅ | ❌ |
| Temporary workaround | ✅ | ❌ |
| Unverified finding | ✅ | ❌ |
| Confirmed pattern | ❌ | ✅ |
| Reusable across features | ❌ | ✅ |
| Feature complete | Transfer → | ✅ |

---

## Feature Planning Workflow

### Phase 1: Requirements (requirements.md)

**Purpose**: Define WHAT to build and WHY

**Approval Gate**: ⛔ Do NOT proceed to design without explicit approval

```markdown
# [Feature Name] - Requirements

## Overview
**Feature**: [Name]
**Created**: [Date]
**Status**: Draft | Under Review | Approved
**Approver**: [Name/Role]

## Problem Statement
[What problem does this solve? Why is it needed?]

## Goals
- [ ] [Goal 1 - measurable outcome]
- [ ] [Goal 2 - measurable outcome]

## Non-Goals
- [What this feature will NOT do]

## User Stories

### US-1: [Story Title]
**As a** [user type]
**I want** [capability]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### US-2: [Story Title]
...

## Functional Requirements

### FR-1: [Requirement Title]
**Description**: [What the system must do]
**Priority**: Must Have | Should Have | Nice to Have
**Dependencies**: [Other requirements or systems]

### FR-2: [Requirement Title]
...

## Non-Functional Requirements

### NFR-1: Performance
- [Response time requirements]
- [Throughput requirements]

### NFR-2: Security
- [Security requirements]
- [Compliance requirements]

### NFR-3: Scalability
- [Scale requirements]

## Constraints
- [Technical constraints]
- [Business constraints]
- [Timeline constraints]

## Assumptions
- [Assumption 1]
- [Assumption 2]

## Dependencies
- **Internal**: [Other features/systems]
- **External**: [Third-party services]

## Out of Scope
- [Explicitly excluded items]

## Open Questions
- [ ] [Question 1] - Owner: [Name]
- [ ] [Question 2] - Owner: [Name]

## References
- #[[file:path/to/related/doc]]
- [External link](url)

---
## Approval

**Status**: ⏳ Pending Approval

To approve, respond with: "approve requirements" or "requirements approved"

---
*Last Updated: [date]*
```

---

### Phase 2: Design (design.md)

**Purpose**: Define HOW to build it

**Prerequisites**: Requirements must be approved
**Approval Gate**: ⛔ Do NOT proceed to tasks without explicit approval

```markdown
# [Feature Name] - Design

## Overview
**Feature**: [Name]
**Requirements**: [Link to requirements.md]
**Created**: [Date]
**Status**: Draft | Under Review | Approved

## Architecture Overview

### High-Level Design
```
[ASCII diagram or description of component interactions]
```

### Component Diagram
```
┌─────────────────┐     ┌─────────────────┐
│   Component A   │────▶│   Component B   │
└─────────────────┘     └─────────────────┘
         │                       │
         ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│   Component C   │     │   Component D   │
└─────────────────┘     └─────────────────┘
```

## Technical Approach

### Technology Stack
| Layer | Technology | Justification |
|-------|------------|---------------|
| [Layer] | [Tech] | [Why] |

### Design Patterns
- **[Pattern 1]**: [Where and why used]
- **[Pattern 2]**: [Where and why used]

## Data Model

### New Models/Tables
```
[Model Name]
├── id: uuid (PK)
├── field_1: type
├── field_2: type
├── created_at: timestamp
└── updated_at: timestamp

Indexes:
- idx_[model]_[field] ON [field]

Relationships:
- belongs_to: [other_model]
- has_many: [other_models]
```

### Schema Changes
```sql
-- Migration: [description]
CREATE TABLE [table_name] (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  ...
);

CREATE INDEX idx_[name] ON [table]([columns]);
```

## API Design

### Endpoints
| Method | Path | Description | Auth |
|--------|------|-------------|------|
| POST | /api/v1/[resource] | Create | Required |
| GET | /api/v1/[resource]/:id | Read | Required |

### Request/Response Examples
```json
// POST /api/v1/[resource]
// Request
{
  "field": "value"
}

// Response 201
{
  "id": "uuid",
  "field": "value",
  "created_at": "timestamp"
}
```

## Security Design

### Authentication
- [Auth mechanism and flow]

### Authorization
- [Permission model]
- [Access control rules]

### Data Protection
- [Encryption requirements]
- [PII handling]

## Error Handling

### Error Codes
| Code | Message | Cause | Resolution |
|------|---------|-------|------------|
| [CODE] | [Message] | [Why] | [How to fix] |

### Error Responses
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {}
  }
}
```

## Testing Strategy

### Unit Tests
- [What to unit test]
- [Coverage targets]

### Integration Tests
- [Integration scenarios]

### E2E Tests
- [End-to-end flows]

## Performance Considerations

### Expected Load
- [Requests per second]
- [Data volume]

### Optimization Strategies
- [Caching approach]
- [Query optimization]

## Deployment Strategy

### Feature Flags
- [Flag name]: [Purpose]

### Rollout Plan
1. [Phase 1]: [Description]
2. [Phase 2]: [Description]

### Rollback Plan
- [How to rollback if issues]

## Risks & Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| [Risk] | High/Med/Low | [Strategy] |

## Design Decisions

### DD-1: [Decision Title]
**Decision**: [What was decided]
**Alternatives**: [Other options considered]
**Rationale**: [Why this choice]

## Open Questions
- [ ] [Question 1]
- [ ] [Question 2]

## References
- #[[file:requirements.md]]
- #[[file:path/to/api/spec]]
- [External docs](url)

---
## Approval

**Prerequisites**: ✅ Requirements approved
**Status**: ⏳ Pending Approval

To approve, respond with: "approve design" or "design approved"

---
*Last Updated: [date]*
```

---

### Phase 3: Tasks (tasks.md)

**Purpose**: Define implementation tasks with tracking

**Prerequisites**: Design must be approved

```markdown
# [Feature Name] - Implementation Tasks

## Overview
**Feature**: [Name]
**Requirements**: [Link to requirements.md]
**Design**: [Link to design.md]
**Created**: [Date]
**Status**: Not Started | In Progress | Complete

## Progress Summary

| Phase | Tasks | Complete | Progress |
|-------|-------|----------|----------|
| Setup | X | Y | Y/X |
| Core | X | Y | Y/X |
| Testing | X | Y | Y/X |
| Deploy | X | Y | Y/X |
| **Total** | **X** | **Y** | **Y/X** |

## Current Focus
**Active Task**: [Task ID and name]
**Blocker**: [None or description]
**Next Up**: [Next task]

---

## Phase 1: Setup & Preparation

### TASK-001: Environment Setup
**Status**: ⏳ Pending | 🔄 In Progress | ✅ Complete | ❌ Blocked
**Estimate**: [X hours]
**Actual**: [Y hours]
**Assignee**: [Agent/Person]

**Description**:
[What needs to be done]

**Subtasks**:
- [ ] [Subtask 1]
- [ ] [Subtask 2]

**Files to Create/Modify**:
- `path/to/file.rb` - [What change]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Notes**:
[Implementation notes, gotchas discovered]

---

### TASK-002: Database Migration
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-001

**Description**:
[What needs to be done]

**Subtasks**:
- [ ] Create migration file
- [ ] Add indexes
- [ ] Run migration locally
- [ ] Verify rollback works

**Files to Create/Modify**:
- `db/migrate/YYYYMMDD_create_[table].rb`

---

## Phase 2: Core Implementation

### TASK-003: [Model/Service Name]
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-002

**Description**:
[What needs to be done]

**Subtasks**:
- [ ] [Subtask 1]
- [ ] [Subtask 2]

**Files to Create/Modify**:
- `app/models/[model].rb`
- `app/services/[service].rb`

---

### TASK-004: [API Endpoint]
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-003

**Description**:
[What needs to be done]

**Subtasks**:
- [ ] Create endpoint
- [ ] Add authentication
- [ ] Add validation
- [ ] Add error handling

**Files to Create/Modify**:
- `app/api/v1/[resource].rb`
- `app/api/entities/[entity].rb`

---

## Phase 3: Testing

### TASK-005: Unit Tests
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-003, TASK-004

**Description**:
Write unit tests for models and services

**Subtasks**:
- [ ] Model specs
- [ ] Service specs
- [ ] Edge cases

**Files to Create/Modify**:
- `spec/models/[model]_spec.rb`
- `spec/services/[service]_spec.rb`

---

### TASK-006: Integration Tests
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-005

**Description**:
Write API integration tests

**Subtasks**:
- [ ] Happy path tests
- [ ] Error case tests
- [ ] Auth tests

**Files to Create/Modify**:
- `spec/requests/api/v1/[resource]_spec.rb`

---

## Phase 4: Documentation & Deployment

### TASK-007: Documentation
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-004

**Description**:
Update API documentation

**Subtasks**:
- [ ] API docs
- [ ] README updates
- [ ] Code comments

---

### TASK-008: Deployment
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: All previous tasks

**Description**:
Deploy to staging and production

**Subtasks**:
- [ ] Deploy to staging
- [ ] Smoke tests
- [ ] Deploy to production
- [ ] Monitor

---

## Dependency Graph

```
TASK-001 (Setup)
    │
    ▼
TASK-002 (Migration)
    │
    ▼
TASK-003 (Model/Service)
    │
    ├──────────────┐
    ▼              ▼
TASK-004       TASK-005
(API)          (Unit Tests)
    │              │
    └──────┬───────┘
           ▼
       TASK-006
    (Integration Tests)
           │
    ┌──────┴──────┐
    ▼             ▼
TASK-007      TASK-008
(Docs)        (Deploy)
```

## Errors Encountered

| Task | Error | Resolution |
|------|-------|------------|
| [ID] | [Error description] | [How resolved] |

## Blockers

| Task | Blocker | Status | Resolution |
|------|---------|--------|------------|
| [ID] | [Description] | Open/Resolved | [Plan] |

## Time Tracking

| Task | Estimate | Actual | Variance |
|------|----------|--------|----------|
| TASK-001 | 2h | 2.5h | +0.5h |
| TASK-002 | 1h | - | - |
| ... | ... | ... | ... |
| **Total** | **Xh** | **Yh** | **+/-Zh** |

## Completion Checklist

Before marking feature complete:
- [ ] All tasks marked ✅ Complete
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] Smoke tests passed
- [ ] Deployed to production
- [ ] Monitoring confirmed
- [ ] Knowledge transferred to KNOWLEDGE.md

---
*Last Updated: [date]*
```

---

## Creating a New Feature Plan

When user requests a new feature, follow this workflow:

### Step 1: Create Feature Folder
```bash
mkdir -p .kiro/features/<feature-name>
```

### Step 2: Generate Requirements
Create `requirements.md` with:
- Problem statement
- User stories
- Functional requirements
- Non-functional requirements
- Constraints and assumptions

### Step 3: Request Approval
```
⏳ Requirements document created for [Feature Name]

Please review `.kiro/features/<feature-name>/requirements.md`

To proceed to design phase, respond with:
- "approve requirements" or "requirements approved"

To request changes, describe what needs modification.
```

### Step 4: Generate Design (after approval)
Create `design.md` with:
- Architecture overview
- Data model
- API design
- Security considerations
- Testing strategy

### Step 5: Request Approval
```
⏳ Design document created for [Feature Name]

Please review `.kiro/features/<feature-name>/design.md`

To proceed to implementation, respond with:
- "approve design" or "design approved"

To request changes, describe what needs modification.
```

### Step 6: Generate Tasks (after approval)
Create `tasks.md` with:
- Phased task breakdown
- Dependencies
- Estimates
- Acceptance criteria

### Step 7: Implement
Work through tasks, updating status after each:
- Mark tasks complete
- Log errors encountered
- Track time
- Update blockers

---

## Linking Features to Project Memory

### Update PROGRESS.md
When working on a feature, update the global progress file:

```markdown
## Current Focus
**Task**: Implementing Authentication Feature
**Feature**: `.kiro/features/authentication/`
**Phase**: Implementation - TASK-003
**Status**: 🔄 In Progress
```

### Update KNOWLEDGE.md
After completing a feature, transfer learnings:

```markdown
## Learnings from Authentication Implementation

### Patterns Used
- JWT with refresh token rotation
- Service object for token management

### Gotchas Discovered
- Must invalidate old refresh tokens on rotation
- Token expiry should be configurable per environment
```

### Update DECISIONS.md
Log significant decisions made during feature work:

```markdown
### [Date] - JWT Token Strategy (Authentication Feature)

**Decision**: Use short-lived access tokens (15min) with refresh token rotation

**Context**: Implementing authentication for API

**Rationale**: 
- Short access tokens limit exposure if compromised
- Refresh rotation prevents token reuse attacks

**Feature Reference**: `.kiro/features/authentication/design.md#security-design`
```

---

## File References in Feature Plans

Feature plans can reference other files using the `#[[file:path]]` syntax:

```markdown
## References
- #[[file:.kiro/resources/PROJECT.md]] - Project architecture
- #[[file:app/api/v1/base.rb]] - API base class
- #[[file:config/routes.rb]] - Existing routes
- #[[file:docs/api-spec.yaml]] - OpenAPI specification
```

This allows feature plans to:
- Reference existing code patterns
- Link to API specifications
- Include external documentation
- Connect to project context

---

## Critical Rules

### 1. Approval Gates Are Mandatory
- ⛔ Never proceed to design without requirements approval
- ⛔ Never proceed to implementation without design approval
- This prevents wasted work on misunderstood requirements

### 2. One Folder Per Feature
- Each feature gets its own folder
- Don't mix unrelated features in one folder
- Keep feature plans focused and manageable

### 3. Update Progress Continuously
- Mark tasks complete immediately when done
- Log errors as they occur
- Update blockers in real-time

### 4. Link to Global Memory
- Reference PROJECT.md for architecture context
- Update KNOWLEDGE.md with learnings
- Log decisions in DECISIONS.md

### 5. Keep Feature Plans Self-Contained
- Each feature folder should be understandable on its own
- Include all necessary context in the feature files
- Use file references for external dependencies

---

## Example: Authentication Feature

### Folder Structure
```
.kiro/features/authentication/
├── requirements.md    # What: JWT auth with refresh tokens
├── design.md         # How: Token service, middleware, endpoints
└── tasks.md          # Tasks: 8 tasks across 4 phases
```

### requirements.md (excerpt)
```markdown
# Authentication - Requirements

## Problem Statement
Users need secure authentication to access protected API endpoints.

## User Stories

### US-1: User Login
**As a** registered user
**I want** to log in with email and password
**So that** I can access my account

**Acceptance Criteria:**
- [ ] Valid credentials return access and refresh tokens
- [ ] Invalid credentials return 401 error
- [ ] Account lockout after 5 failed attempts
```

### design.md (excerpt)
```markdown
# Authentication - Design

## Architecture Overview
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  Auth API   │────▶│  Token Svc  │
└─────────────┘     └─────────────┘     └─────────────┘
                           │                    │
                           ▼                    ▼
                    ┌─────────────┐     ┌─────────────┐
                    │   User DB   │     │  Redis      │
                    └─────────────┘     └─────────────┘
```

## API Design
| Method | Path | Description |
|--------|------|-------------|
| POST | /api/v1/auth/login | User login |
| POST | /api/v1/auth/refresh | Refresh tokens |
| POST | /api/v1/auth/logout | User logout |
```

### tasks.md (excerpt)
```markdown
# Authentication - Tasks

## Progress Summary
| Phase | Tasks | Complete | Progress |
|-------|-------|----------|----------|
| Setup | 2 | 0 | 0/2 |
| Core | 3 | 0 | 0/3 |
| Testing | 2 | 0 | 0/2 |
| Deploy | 1 | 0 | 0/1 |

## Phase 2: Core Implementation

### TASK-003: Token Service
**Status**: ⏳ Pending
**Estimate**: 3 hours
**Dependencies**: TASK-002

**Subtasks**:
- [ ] Create TokenService class
- [ ] Implement JWT generation
- [ ] Implement refresh token rotation
- [ ] Add token validation

**Files to Create**:
- `app/services/auth/token_service.rb`
```

---

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| Skip requirements phase | Always document requirements first |
| Start coding without design approval | Wait for explicit approval |
| Create monolithic feature plans | One folder per feature |
| Forget to update task status | Update immediately after completion |
| Keep learnings in feature only | Transfer to global KNOWLEDGE.md |
| Ignore blockers | Document and escalate blockers |

---

## Quick Reference Commands

| Command | Action |
|---------|--------|
| "create feature [name]" | Create new feature folder with requirements.md |
| "approve requirements" | Proceed to design phase |
| "approve design" | Proceed to tasks phase |
| "show feature status" | Display current feature progress |
| "update task [ID]" | Update specific task status |
| "complete feature" | Finalize and transfer learnings |

---

## Remember

**Feature plans are your feature's source of truth.**

Good feature plans:
- ✅ Prevent misunderstandings before coding starts
- ✅ Provide clear implementation guidance
- ✅ Track progress transparently
- ✅ Capture decisions and rationale
- ✅ Enable effective handoffs
- ✅ Build organizational knowledge

**The time invested in feature planning is recovered many times over through:**
- Fewer rewrites from misunderstood requirements
- Clearer implementation path
- Better code quality
- Easier maintenance
- Knowledge preservation

**Always get approval before proceeding to the next phase.**
