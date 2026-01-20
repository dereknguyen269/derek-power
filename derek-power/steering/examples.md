---
inclusion: manual
name: examples
description: Examples of D.E.R.E.K planning workflow in action. Reference for understanding how to use the memory system effectively.
---

# D.E.R.E.K Planning Examples

## Example 1: Research Task

**User Request:** "Research the benefits of morning exercise and write a summary"

### Phase 1: Create Plan (PROGRESS.md)
```markdown
## Current Focus
**Task**: Research morning exercise benefits
**Phase**: Planning
**Status**: 🔄 In Progress
```

### Phase 2: Research & Notes
- WebSearch for sources
- Capture findings in SCRATCHPAD.md
- Update PROGRESS.md status

### Phase 3: Synthesize & Deliver
- Create summary document
- Mark task complete in PROGRESS.md

---

## Example 2: Bug Fix Task

**User Request:** "Fix the login bug in the authentication module"

### PROGRESS.md Updates
```markdown
## Current Focus
**Task**: Fix login bug in auth module
**Phase**: Investigation → Implementation → Review
**Status**: 🔄 In Progress

## Investigation Notes
- Error: TypeError in validateToken()
- Root cause: user object not awaited
- Fix: Add await to getUserById call
```

### DECISIONS.md Entry
```markdown
### [Date] - Login Bug Fix Approach
**Decision**: Add proper async/await to token validation
**Context**: TypeError due to missing await
**Rationale**: Simplest fix, maintains existing patterns
```

---

## Example 3: Feature Development

**User Request:** "Add dark mode toggle to settings"

### Feature Folder Structure
```
.kiro/specs/dark-mode/
├── requirements.md   # WHAT: Dark mode toggle in settings
├── design.md        # HOW: CSS variables, localStorage
├── tasks.md         # Implementation steps
└── notes.md         # Discoveries during implementation
```

### requirements.md
```markdown
# Dark Mode Feature Requirements

## User Story
As a user, I want to toggle dark mode in settings.

## Acceptance Criteria
- [ ] Toggle visible in settings page
- [ ] Preference persists across sessions
- [ ] Smooth transition between themes
```

### design.md
```markdown
# Dark Mode Design

## Technical Approach
- CSS custom properties for theming
- localStorage for persistence
- useTheme hook for state management

## Files to Modify
1. src/styles/theme.ts - Add dark colors
2. src/components/SettingsPage.tsx - Add toggle
3. src/hooks/useTheme.ts - Create hook
```

### tasks.md
```markdown
# Implementation Tasks

- [x] TASK-1: Define dark theme colors
- [x] TASK-2: Create useTheme hook
- [ ] TASK-3: Add toggle component (CURRENT)
- [ ] TASK-4: Test and polish
```

---

## Example 4: Error Recovery

When something fails, document it:

### PROGRESS.md
```markdown
## Errors Encountered
- config.json not found
  → Resolution: Created default config
  → Lesson: Check file existence before read
```

### KNOWLEDGE.md (after resolution)
```markdown
## Gotchas
- Always check file existence before reading
- Use try/catch for file operations
```

---

## The Read-Before-Decide Pattern

**Always read your plan before major decisions:**

```
[Many actions completed...]
[Context getting long...]

→ Read PROGRESS.md    # Refresh goals
→ Make decision       # Goals fresh in context
```

This keeps you on track during complex tasks.
