---
inclusion: manual
name: planning
description: Transforms workflow to use persistent markdown files for planning, progress tracking, and knowledge storage. Supports folder spec planning with dedicated folders for requirements, design, and tasks. Use when starting complex tasks, multi-step projects, research tasks, or when the user mentions planning, organizing work, or spec development.
category: planning
---
# Planning

Work like Manus: Use persistent markdown files as your "working memory on disk."

## Two Planning Modes

This steering file supports two planning modes:

| Mode | Use When | Location |
|------|----------|----------|
| **Quick Planning** | Simple tasks, bug fixes, small changes | `.kiro/resources/PROGRESS.md` |
| **Folder Spec Planning** | Complex specs, new modules, multi-phase work | `.kiro/specs/<spec-name>/` |

---

## Workflows

**Decision:** Complex spec (multi-file/session)? → Folder Spec Planning | Simple task? → Quick Planning

**Quick Planning:** Update PROGRESS.md → Execute phases → Store in KNOWLEDGE.md → Mark complete → Log decisions

**Folder Spec:** Requirements (⛔ approval) → Design (⛔ approval) → Tasks → Implementation (capture in notes.md) → Transfer to KNOWLEDGE.md

**Approval Gates:** "approve requirements" or "approve design" to proceed. Rejected → revise → re-request approval.

**Memory Integration:** PROJECT.md (context for all) · PROGRESS.md (links to specs) · DECISIONS.md (receives decisions) · KNOWLEDGE.md (receives learnings from notes.md) · notes.md (temporary, transfer on completion)

---

## Integration with Project Memory System

| Memory File | Purpose | Relationship to Specs |
|-------------|---------|----------------------|
| `PROJECT.md` | Project overview | Referenced by all specs |
| `PROGRESS.md` | Task tracking | Links to active specs |
| `DECISIONS.md` | Decision log | Receives decisions from specs |
| `KNOWLEDGE.md` | Patterns/learnings | Updated from completed specs |
| `SCRATCHPAD.md` | Session notes | Working area during spec work |

**Folder specs** (`.kiro/specs/<name>/`): Self-contained with requirements, design, tasks, notes (temporary → KNOWLEDGE.md)

---

## Quick Start

**Simple Tasks:** Update PROGRESS.md → Work phases → Log decisions in DECISIONS.md

**Complex Specs:** Create `.kiro/specs/<name>/` → requirements.md (⛔ approval) → design.md (⛔ approval) → tasks.md → implement → transfer notes.md to KNOWLEDGE.md

---

# Quick Planning Mode

**Files:** PROGRESS.md (phases/status) · KNOWLEDGE.md (findings) · DECISIONS.md (rationale) · SCRATCHPAD.md (temp notes)

**Workflow:** Update PROGRESS.md with goal/phases → Research → Save to KNOWLEDGE.md → Update PROGRESS.md → Create deliverable → Log decisions → Deliver

**Before actions:** Read PROGRESS.md + PROJECT.md (if exists) | **After phases:** Mark [x] in PROGRESS.md

---

# Folder Spec Planning

## When to Use

**Use for:** Multi-file features · Auth/API systems · DB changes · External integrations · Major refactors · Multi-session work

**Skip for:** Bug fixes · Single-file changes · Config/doc updates

---

## Folder Spec Structure

```
.kiro/specs/<spec-name>/
├── requirements.md   # WHAT (needs ⛔ approval)
├── design.md        # HOW (needs ⛔ approval)
├── tasks.md         # Implementation tracking
└── notes.md         # Temporary knowledge → KNOWLEDGE.md on completion
```

**File Purposes:** requirements (permanent) · design (permanent) · tasks (permanent) · notes (temporary, transfer learnings)

**notes.md Usage:** Capture discoveries/gotchas during implementation · Transfer valuable content to KNOWLEDGE.md when complete · Use for unverified findings · KNOWLEDGE.md for confirmed patterns

---

## Folder Spec Workflow

### Phase 1: Requirements (requirements.md)

**Purpose:** Define WHAT to build and WHY | **Approval Gate:** ⛔ Do NOT proceed without explicit approval

**Required Sections:** Overview (status, approver) · Problem Statement · Goals/Non-Goals · User Stories (As/Want/So that + Acceptance Criteria) · Functional Requirements (description, priority, dependencies) · Non-Functional Requirements (performance, security, scalability) · Constraints · Assumptions · Dependencies · Out of Scope · Open Questions · References

**Approval Request:** "⏳ Requirements created. Review `.kiro/specs/<name>/requirements.md`. To proceed: 'approve requirements' or 'requirements approved'"

---

### Phase 2: Design (design.md)

**Purpose:** Define HOW to build | **Prerequisites:** Requirements approved | **Approval Gate:** ⛔ Do NOT proceed without explicit approval

**Required Sections:** Overview (links requirements) · Architecture (high-level, component diagram) · Technical Approach (stack, patterns) · Data Model (schemas, migrations, relationships) · API Design (endpoints table, request/response examples) · Security Design (auth, authorization, data protection) · Error Handling (codes, responses) · Testing Strategy (unit, integration, E2E) · Performance (load, optimization) · Deployment (feature flags, rollout, rollback) · Risks & Mitigations · Design Decisions (decision, alternatives, rationale) · Open Questions · References

**Approval Request:** "⏳ Design created. Review `.kiro/specs/<name>/design.md`. To proceed: 'approve design' or 'design approved'"

---

### Phase 3: Tasks (tasks.md)

**Purpose:** Implementation tracking | **Prerequisites:** Design approved

**Required Sections:** Overview (links requirements/design) · Progress Summary (phase table) · Current Focus (active task, blocker, next) · Phased Tasks (TASK-XXX with status ⏳/🔄/✅/❌, estimate, actual, assignee, description, subtasks, files, acceptance criteria, notes) · Dependency Graph · Errors Encountered · Blockers · Time Tracking · Completion Checklist

**Task Statuses:** ⏳ Pending | 🔄 In Progress | ✅ Complete | ❌ Blocked

---

### Phase 4: Implementation

Work through tasks: Execute → Update status → Capture in notes.md → Repeat

---

### Phase 5: Completion

Review notes.md → Transfer learnings to KNOWLEDGE.md → Log decisions in DECISIONS.md → Update PROGRESS.md

---

## Creating a New Folder Spec

1. `mkdir -p .kiro/specs/<spec-name>`
2. Generate requirements.md → Request approval: "⏳ Review `.kiro/specs/<name>/requirements.md`. To proceed: 'approve requirements'"
3. After approval → Generate design.md → Request approval: "⏳ Review `.kiro/specs/<name>/design.md`. To proceed: 'approve design'"
4. After approval → Generate tasks.md with phased breakdown
5. Implement → Update task status → Capture in notes.md

---

## Linking to Project Memory

**PROGRESS.md:** Link to active spec: "Task: Implementing X Spec · Spec: `.kiro/specs/X/` · Phase: TASK-003 · Status: 🔄"

**KNOWLEDGE.md:** Transfer learnings after completion: "## Learnings from X Implementation · Patterns Used · Gotchas Discovered"

**DECISIONS.md:** Log decisions: "### [Date] - X Decision (Y Spec) · Decision · Context · Rationale · Spec Reference: `.kiro/specs/Y/design.md#section`"

**File References:** Use `#[[file:path]]` to link: `#[[file:.kiro/resources/PROJECT.md]]` · `#[[file:app/api/base.rb]]` · `#[[file:docs/spec.yaml]]`

---

## Critical Rules

1. **Approval Gates Mandatory:** ⛔ Never skip requirements/design approval - prevents wasted work
2. **One Folder Per Spec:** Keep focused and manageable
3. **Update Progress Continuously:** Mark tasks complete immediately, log errors real-time
4. **Link to Global Memory:** Reference PROJECT.md, update KNOWLEDGE.md, log in DECISIONS.md
5. **Keep Self-Contained:** Each spec understandable on its own with necessary context

---

## Commands

| Command | Action |
|---------|--------|
| "create spec [name]" | Create folder spec with requirements.md |
| "approve requirements" | Proceed to design |
| "approve design" | Proceed to tasks |
| "show spec status" | Display progress |
| "update task [ID]" | Update task status |
| "complete spec" | Finalize and transfer learnings |

---

## Remember

**Folder specs prevent misunderstandings, provide clear guidance, track progress, capture decisions, enable handoffs, and build knowledge. Approval gates are mandatory. Time invested in planning is recovered through fewer rewrites, clearer paths, better quality, and easier maintenance.**
