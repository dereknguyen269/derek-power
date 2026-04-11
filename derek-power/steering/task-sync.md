---
inclusion: manual
description: Smart task synchronization between git branches with intelligent merge strategies
---

# Smart Task Sync

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

Enable intelligent synchronization of D.E.R.E.K tasks and code logic between git branches.

## Activation Keywords

- "sync tasks from [branch]"
- "task sync", "sync branches", "merge tasks"
- "branch task sync", "sync from [branch-name]"
- "compare branches", "task comparison"

## Smart Sync Features

### Task Synchronization

| Feature | Description |
|---------|-------------|
| **Fuzzy Title Matching** | Tasks matched by title, not just ID |
| **Status Preservation** | Completed tasks stay completed |
| **Smart Merge** | In-progress tasks merge intelligently |
| **Dependency Re-mapping** | Auto-update dependency IDs after reorder |
| **Conflict Detection** | Flag tasks needing manual review |
| **Soft Delete** | Archive deleted tasks instead of remove |

### Code Logic Sync (Optional)

| Feature | Description |
|---------|-------------|
| **File Change Detection** | Compare files between branches |
| **Uncommitted Change Detection** | Flag files with local changes |
| **Diff Summarization** | Show what changed, not full diff |
| **Conflict Highlighting** | Identify files needing attention |

## Sync Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                    SMART SYNC LOGIC                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Source Branch          Target Branch (Current)              │
│  ┌────────────┐         ┌────────────┐                      │
│  │ Task A ✅  │         │ Task A ✅  │  ← Keep completed    │
│  │ Task B ⏳  │         │ Task B 📝  │  ← Merge status      │
│  │ Task C 📋  │         │            │  ← Add new           │
│  │ Task D ❌  │         │ Task D 📝  │  ← Archive (soft)    │
│  └────────────┘         └────────────┘                      │
│                                                              │
│  Result: Intelligent merge preserving local progress         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Usage

### Quick Sync
```
User: "sync tasks from feature/auth"
D.E.R.E.K: Shows sync preview, asks confirmation
User: "yes"
D.E.R.E.K: Applies sync, reports results
```

### Sync with Code Changes
```
User: "sync tasks and code from feature/auth"
D.E.R.E.K: Shows task + file sync preview
User: "yes"
D.E.R.E.K: Applies both, flags conflicts
```

### Compare Only
```
User: "compare branches main"
D.E.R.E.K: Shows differences without applying
```

## Output Example

```
=== Task Sync Report ===
Source: feature/auth → Target: current-branch

📋 Tasks:
  + 3.1 Implement OAuth flow (NEW)
  ~ 3.2 Add JWT tokens (MODIFIED - new subtasks)
  ✓ 3.3 User model update (UNCHANGED)
  ⚠ 3.4 Session management (CONFLICT - local changes)

📁 Files:
  ? src/auth/oauth.ts (needs review)
  + src/auth/jwt.ts (new in source)

💡 Recommendations:
  - Review oauth.ts before syncing
  - Consider merging jwt.ts manually
```

## Integration Points

- **Drift Detection**: Sync can resolve drift by updating tasks
- **Memory System**: Sync updates PROGRESS.md automatically
- **Branch Awareness**: Auto-detects current branch context