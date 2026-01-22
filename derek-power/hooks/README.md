# D.E.R.E.K Hooks

This directory contains Kiro hooks that automate D.E.R.E.K workflows.

## Available Hooks

### Context Management

#### `post-code-context-capture.kiro.hook`
**Trigger**: After agent stops (code generation complete)
**Purpose**: Comprehensive context capture with detailed prompts

Prompts for:
- Quick feedback on the solution
- Important decisions to save to DECISIONS.md
- Patterns/learnings to save to KNOWLEDGE.md
- Gotchas/pitfalls to remember
- Spec work to save to notes.md
- Progress updates for PROGRESS.md

**Use when**: You want detailed guidance on what to capture after each code change.

#### `quick-context-save.kiro.hook` ⭐ Recommended
**Trigger**: After agent stops (code generation complete)
**Purpose**: Quick, non-intrusive context save prompt

Brief reminder to save:
- Decisions → DECISIONS.md
- Patterns/learnings → KNOWLEDGE.md
- Gotchas → KNOWLEDGE.md
- Spec work → notes.md

**Use when**: You want a lightweight reminder without interrupting flow.

### Session Management

#### `auto-summary-on-context-limit.kiro.hook` ⭐ Enhanced
**Trigger**: On prompt submit
**Purpose**: Auto-summarize and save context when reaching 80% usage

Automatically:
- Saves current context to D.E.R.E.K memory files:
  - PROGRESS.md (task status and phase)
  - SCRATCHPAD.md (session notes)
  - DECISIONS.md (decisions made)
  - KNOWLEDGE.md (learnings)
- Summarizes key points and decisions
- Notes active powers
- Prepares context for new session
- Helps start new session with preserved context

**Use when**: Working on long sessions and want automatic context preservation with D.E.R.E.K integration.

#### `summary-session-command.kiro.hook` ⭐ Enhanced
**Trigger**: User-triggered (manual command)
**Purpose**: Manual session summary with D.E.R.E.K memory integration

Provides structured 4-step process:
1. **Save Context**: Updates PROGRESS.md, SCRATCHPAD.md, DECISIONS.md, KNOWLEDGE.md, and spec notes.md
2. **Generate Summary**: Key accomplishments, decisions, active powers, current task, blockers
3. **Prepare New Session**: Creates concise context summary with powers list and next steps
4. **Session Transition**: Formatted summary and command to start new session

**Use when**: You want to manually trigger a comprehensive session summary and transition with full context preservation.

#### `clear-chat-history.kiro.hook`
**Trigger**: User-triggered
**Purpose**: Clear chat history while preserving important context

**Use when**: You want to start fresh but keep essential context.

## Installation

1. **Enable a hook**: Hooks in this directory are automatically available when the derek power is installed
2. **Copy to project** (optional): Copy desired hooks to your project's `.kiro/hooks/` directory for project-specific customization
3. **Restart Kiro**: Hooks are loaded on startup
4. **Test**: Trigger the hook's event to verify it works

## Customization

Edit the `outputPrompt` field in any hook file to customize the prompt text.

## Recommendations

**For most users**: Start with these two hooks
```
✅ quick-context-save.kiro.hook (after code)
✅ auto-summary-on-context-limit.kiro.hook (session management)
```

**For structured teams**: Use detailed guidance
```
✅ post-code-context-capture.kiro.hook (detailed guidance)
✅ auto-summary-on-context-limit.kiro.hook (session management)
```

**For long sessions**: Essential for context preservation
```
✅ auto-summary-on-context-limit.kiro.hook (automatic context save)
```

## Hook Combinations

**Recommended Setup**:
```
✅ quick-context-save.kiro.hook (after code)
✅ auto-summary-on-context-limit.kiro.hook (session management)
```

**Learning Setup**:
```
✅ post-code-context-capture.kiro.hook (detailed guidance)
✅ auto-summary-on-context-limit.kiro.hook (session management)
```

## Disabling Hooks

To disable a hook, either:
1. Remove it from `.kiro/hooks/`
2. Rename it (e.g., add `.disabled` extension)
3. Delete the file

## Creating Custom Hooks

See [Kiro Hook Documentation](https://docs.kiro.ai/hooks) for creating your own hooks.

Key fields:
- `eventType`: When to trigger (agentStop, promptSubmit, fileEdited, etc.)
- `hookAction`: What to do (askAgent, runCommand)
- `outputPrompt`: The prompt to send to the agent

## Hook Enhancements

### Recent Updates

**auto-summary-on-context-limit.kiro.hook** (Enhanced):
- Now integrates with D.E.R.E.K memory system
- Automatically saves context to PROGRESS.md, SCRATCHPAD.md, DECISIONS.md, KNOWLEDGE.md
- Provides structured session transition
- Preserves active powers and current work state

**summary-session-command.kiro.hook** (Enhanced):
- Now integrates with D.E.R.E.K memory system
- 4-step structured process for comprehensive context preservation
- Manual trigger for user-controlled session transitions
- Ideal for planned breaks or end-of-day summaries

**New Hooks**:
- `post-code-context-capture.kiro.hook` - Detailed post-code context capture
- `quick-context-save.kiro.hook` - Lightweight context reminder

### Session Management Comparison

| Feature | auto-summary-on-context-limit | summary-session-command |
|---------|------------------------------|-------------------------|
| **Trigger** | Automatic at 80% context | Manual (user command) |
| **Best For** | Long sessions, automatic safety net | Planned breaks, end of day |
| **Context Save** | ✅ Full D.E.R.E.K integration | ✅ Full D.E.R.E.K integration |
| **User Control** | Automatic with confirmation | Complete user control |
| **Use Case** | "I don't want to think about it" | "I want to summarize now" |

**Recommendation**: Use both! 
- `auto-summary-on-context-limit` as safety net
- `summary-session-command` for planned transitions

## Benefits

✅ **Never lose context** - Automatic preservation at 80% usage
✅ **Capture learnings** - Prompts after code changes
✅ **Seamless transitions** - Start new sessions with full context
✅ **Non-intrusive** - Easy to skip when not needed
✅ **D.E.R.E.K integrated** - Works with memory system
