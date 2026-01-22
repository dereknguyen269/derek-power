---
inclusion: manual
name: spec-planning
description: Folder-based specification planning workflow. Creates structured spec folders with requirements, design, and implementation tracking. Use when planning complex features, new modules, or multi-phase work that requires formal specification.
category: planning
---
# Specification Planning

Work with structured folder-based specifications for complex development work.

## Overview

This workflow uses **folder specs** - structured specification folders under `.kiro/specs/` that contain requirements, design documents, and implementation tracking.

**Note**: This file provides detailed templates and examples. For a concise overview, see `planning.md`.

## When to Use Folder Specs

Use folder specs for:
- ✅ New features requiring multiple files/components
- ✅ Authentication, authorization systems
- ✅ API endpoints with complex logic
- ✅ Database schema changes
- ✅ Integration with external services
- ✅ Refactoring major components
- ✅ Work spanning multiple sessions

Skip folder specs for:
- ❌ Bug fixes
- ❌ Single-file changes
- ❌ Configuration updates
- ❌ Documentation updates

---

## Folder Spec Structure

Each specification gets its own folder under `.kiro/specs/`:

```
.kiro/
├── resources/                    # Global Project Memory
│   ├── PROJECT.md
│   ├── PROGRESS.md              # Links to active specs
│   ├── DECISIONS.md
│   ├── KNOWLEDGE.md
│   └── SCRATCHPAD.md
│
└── specs/                        # Specification Folders
    ├── authentication/           # Example: Auth spec
    │   ├── requirements.md       # What to build
    │   ├── design.md            # How to build
    │   ├── tasks.md             # Implementation tracking
    │   └── notes.md             # 📝 Temporary knowledge during implementation
    │
    ├── payment-integration/      # Example: Payments spec
    │   ├── requirements.md
    │   ├── design.md
    │   ├── tasks.md
    │   └── notes.md
    │
    └── user-notifications/       # Example: Notifications spec
        ├── requirements.md
        ├── design.md
        ├── tasks.md
        └── notes.md
```

### Spec Files Purpose

| File | Purpose | When to Update | Lifecycle |
|------|---------|----------------|-----------|
| `requirements.md` | What to build | During requirements phase | Permanent |
| `design.md` | How to build | During design phase | Permanent |
| `tasks.md` | Implementation tracking | During implementation | Permanent |
| `notes.md` | Temporary knowledge capture | During implementation | Temporary → Transfer to KNOWLEDGE.md |

---

## Folder Spec Workflow

### Complete Workflow Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                     FOLDER SPEC WORKFLOW                          │
└──────────────────────────────────────────────────────────────────┘

┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: REQUIREMENTS                                           │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ Create .kiro/specs/<name>/requirements.md                │ │
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
│  │ Create .kiro/specs/<name>/design.md                      │ │
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
│  │ Create .kiro/specs/<name>/tasks.md                       │ │
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

---

## Phase 1: Requirements (requirements.md)

**Purpose**: Define WHAT to build and WHY

**Approval Gate**: ⛔ Do NOT proceed to design without explicit approval

### Template

```markdown
# [Spec Name] - Requirements

## Overview
**Specification**: [Name]
**Created**: [Date]
**Status**: Draft | Under Review | Approved
**Approver**: [Name/Role]

## Problem Statement
[What problem does this solve? Why is it needed?]

## Goals
- [ ] [Goal 1 - measurable outcome]
- [ ] [Goal 2 - measurable outcome]

## Non-Goals
- [What this spec will NOT cover]

## User Stories

### US-1: [Story Title]
**As a** [user type]
**I want** [capability]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Functional Requirements

### FR-1: [Requirement Title]
**Description**: [What the system must do]
**Priority**: Must Have | Should Have | Nice to Have
**Dependencies**: [Other requirements or systems]

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
- **Internal**: [Other specs/systems]
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

## Phase 2: Design (design.md)

**Purpose**: Define HOW to build it

**Prerequisites**: Requirements must be approved
**Approval Gate**: ⛔ Do NOT proceed to tasks without explicit approval

### Template

```markdown
# [Spec Name] - Design

## Overview
**Specification**: [Name]
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

## Phase 3: Tasks (tasks.md)

**Purpose**: Define implementation tasks with tracking

**Prerequisites**: Design must be approved

### Template

```markdown
# [Spec Name] - Implementation Tasks

## Overview
**Specification**: [Name]
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

## Phase 3: Testing

### TASK-004: Unit Tests
**Status**: ⏳ Pending
**Estimate**: [X hours]
**Dependencies**: TASK-003

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

## Phase 4: Documentation & Deployment

### TASK-005: Documentation
**Status**: ⏳ Pending
**Estimate**: [X hours]

**Description**:
Update documentation

**Subtasks**:
- [ ] API docs
- [ ] README updates
- [ ] Code comments

---

## Dependency Graph

```
TASK-001 (Setup)
    │
    ▼
TASK-002 (Migration)
    │
    ▼
TASK-003 (Core)
    │
    ▼
TASK-004 (Testing)
    │
    ▼
TASK-005 (Docs)
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
| **Total** | **Xh** | **Yh** | **+/-Zh** |

## Completion Checklist

Before marking spec complete:
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

## Phase 4: notes.md - Temporary Knowledge

**Purpose**: Capture discoveries during implementation

### Template

```markdown
# [Spec Name] - Implementation Notes

## Purpose
Temporary storage for discoveries, gotchas, and learnings during implementation.
Transfer valuable content to `.kiro/resources/KNOWLEDGE.md` when spec is complete.

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

Before completing spec, review and transfer:
- [ ] Valuable patterns → KNOWLEDGE.md
- [ ] Reusable snippets → KNOWLEDGE.md
- [ ] Gotchas for others → KNOWLEDGE.md
- [ ] Decisions made → DECISIONS.md

---
*Last Updated: [date]*
```

---

## Creating a New Folder Spec

### Step 1: Create Spec Folder
```bash
mkdir -p .kiro/specs/<spec-name>
```

### Step 2: Generate Requirements
Create `requirements.md` using the template above.

### Step 3: Request Approval
```
⏳ Requirements document created for [Spec Name]

Please review `.kiro/specs/<spec-name>/requirements.md`

To proceed to design phase, respond with:
- "approve requirements" or "requirements approved"

To request changes, describe what needs modification.
```

### Step 4: Generate Design (after approval)
Create `design.md` using the template above.

### Step 5: Request Approval
```
⏳ Design document created for [Spec Name]

Please review `.kiro/specs/<spec-name>/design.md`

To proceed to implementation, respond with:
- "approve design" or "design approved"

To request changes, describe what needs modification.
```

### Step 6: Generate Tasks (after approval)
Create `tasks.md` using the template above.

### Step 7: Implement
Work through tasks, updating status after each completion.

---

## Integration with Project Memory

### Update PROGRESS.md
When working on a spec, update the global progress file:

```markdown
## Current Focus
**Task**: Implementing Authentication Spec
**Spec**: `.kiro/specs/authentication/`
**Phase**: Implementation - TASK-003
**Status**: 🔄 In Progress
```

### Update KNOWLEDGE.md
After completing a spec, transfer learnings from notes.md:

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
Log significant decisions made during spec work:

```markdown
### [Date] - JWT Token Strategy (Authentication Spec)

**Decision**: Use short-lived access tokens (15min) with refresh token rotation

**Context**: Implementing authentication for API

**Rationale**: 
- Short access tokens limit exposure if compromised
- Refresh rotation prevents token reuse attacks

**Spec Reference**: `.kiro/specs/authentication/design.md#security-design`
```

---

## File References in Specs

Specs can reference other files using the `#[[file:path]]` syntax:

```markdown
## References
- #[[file:.kiro/resources/PROJECT.md]] - Project architecture
- #[[file:app/api/v1/base.rb]] - API base class
- #[[file:config/routes.rb]] - Existing routes
- #[[file:docs/api-spec.yaml]] - OpenAPI specification
```

---

## Commands

| Command | Action |
|---------|--------|
| "create spec [name]" | Create new spec folder with requirements.md |
| "approve requirements" | Proceed to design phase |
| "approve design" | Proceed to tasks phase |
| "show spec status" | Display current spec progress |
| "update task [ID]" | Update specific task status |
| "complete spec" | Finalize and transfer learnings |

---

## Critical Rules

### 1. Approval Gates Are Mandatory
- ⛔ Never proceed to design without requirements approval
- ⛔ Never proceed to implementation without design approval
- This prevents wasted work on misunderstood requirements

### 2. One Folder Per Spec
- Each spec gets its own folder
- Don't mix unrelated specs in one folder
- Keep specs focused and manageable

### 3. Update Progress Continuously
- Mark tasks complete immediately when done
- Log errors as they occur
- Update blockers in real-time

### 4. Link to Global Memory
- Reference PROJECT.md for architecture context
- Update KNOWLEDGE.md with learnings
- Log decisions in DECISIONS.md

### 5. Keep Specs Self-Contained
- Each spec folder should be understandable on its own
- Include all necessary context in the spec files
- Use file references for external dependencies

---

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| Skip requirements phase | Always document requirements first |
| Start coding without design approval | Wait for explicit approval |
| Create monolithic specs | One folder per spec |
| Forget to update task status | Update immediately after completion |
| Keep learnings in spec only | Transfer to global KNOWLEDGE.md |
| Ignore blockers | Document and escalate blockers |

---

## Remember

**Folder specs are your specification's source of truth.**

Good folder specs:
- ✅ Prevent misunderstandings before coding starts
- ✅ Provide clear implementation guidance
- ✅ Track progress transparently
- ✅ Capture decisions and rationale
- ✅ Enable effective handoffs
- ✅ Build organizational knowledge

**The time invested in spec planning is recovered many times over through:**
- Fewer rewrites from misunderstood requirements
- Clearer implementation path
- Better code quality
- Easier maintenance
- Knowledge preservation

**Always get approval before proceeding to the next phase.**
