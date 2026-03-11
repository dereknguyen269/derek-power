# Changelog

All notable changes to the D.E.R.E.K power will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2026-03-11

### Added
- **Drift Detection**
  - New `derek-power/steering/drift-detection.md` steering file (`inclusion: manual`)
  - Drift_Score formula: `round((changed_files / total_tracked_files) × 100)`
  - Four severity tiers: 🟢 Healthy (0–20%) · 🟡 Review (21–50%) · 🟠 Soft_Block (51–75%) · 🔴 Hard_Block (76–100%)
  - Automatic drift check on every session start (integrated into `derek-init.md`)
  - On-demand commands: `check drift`, `drift status`, `drift history`, `acknowledge drift`
  - PROGRESS.md `## Drift Status` section with rolling 10-entry history
  - Hard_Block tier gates task execution until `reinit` or `update memory` is run
  - Soft_Block tier requires `acknowledge drift` before proceeding
  - Memory update reset: drift recalculates automatically after `reinit` or `update memory`
  - Hook deduplication: suppresses duplicate notifications within a 60-second window (tracked in SCRATCHPAD.md)
  - Optional `drift-detection.kiro.hook` template for real-time drift checks on file edits
    - Install: `cp derek-power/hooks/drift-detection.kiro.hook .kiro/hooks/`
    - Covers common source extensions: rb, js, ts, jsx, tsx, py, go, java, kt, swift, rs, md, yml, yaml, json, toml, sh, sql
    - Notifies only on Review, Soft_Block, or Hard_Block tiers (silent on Healthy)
    - Explicitly states tier-crossing events (e.g., "Healthy → Review")

### Changed
- **`derek-init.md`** - Added `## Drift Check (Session Start)` section; drift score now appears between memory read confirmation and current task display
- **`POWER.md`** - Added 9 drift detection keywords to frontmatter; added `Drift Detection` command group
- **`README.MD`** - Added Drift Detection to Key Features, Commands, comparison table, and activation keywords

---

## [0.1.3] - 2026-01-29

### Added
- **Debug & Investigation Mode**
  - New `debug mode` command to enter specialized investigation workflows
  - Structured investigation phases: Discovery → Analysis → Hypothesis → Validation → Documentation
  - Investigation memory files: INVESTIGATION.md, EVIDENCE.md, FINDINGS.md, HYPOTHESES.md
  - Specialized investigation agents:
    - `investigation-discovery.md` - Map codebase structure and entry points
    - `investigation-analysis.md` - Deep dive analysis of target components
    - `investigation-tracer.md` - Trace execution flows and data paths
  - Commands: `investigate [target]`, `trace [path]`, `exit debug`
  - Automatic knowledge transfer from investigation findings to project memory

## [0.1.2] - 2026-01-22

### Added
- **Post-Code Context Capture Hooks**
  - `post-code-context-capture.kiro.hook` - Detailed guidance for saving context after code changes
  - `quick-context-save.kiro.hook` - Lightweight reminder to save decisions/learnings
  - Automatic prompts to save to DECISIONS.md, KNOWLEDGE.md, or spec notes.md
- **Context7 Integration**
  - Added Context7 MCP support to context.md for cross-project knowledge sharing
  - Layered context storage: file-based + semantic search
  - Query past implementations and patterns across projects
- **Steering File Guidance**
  - Added "Steering Files to Use" sections to POWER.md for all 3 implementation modes
  - Updated Decision Matrix with steering file recommendations
  - Clear guidance on which agents to use: analysis.md + specialized agent + review.md (quick) vs planning.md + context.md + specialized agent + review.md (complex)
- **Hooks Documentation**
  - Comprehensive `hooks/README.md` with 172 lines of documentation
  - Hook comparison tables and use case recommendations
  - Installation and customization instructions

### Enhanced
- **Session Management Hooks**
  - `auto-summary-on-context-limit.kiro.hook` - Now integrates with D.E.R.E.K memory system
    - Automatically saves to PROGRESS.md, SCRATCHPAD.md, DECISIONS.md, KNOWLEDGE.md
    - Structured 3-step process for context preservation
    - Triggers at 80% context usage
  - `summary-session-command.kiro.hook` - Enhanced with 4-step structured process
    - Full D.E.R.E.K memory integration
    - Manual trigger for user-controlled session transitions
    - Ideal for planned breaks or end-of-day summaries

### Optimized
- **Steering Files** - Major token efficiency improvements
  - `context.md` - Reduced from ~500 to 199 lines (~60% reduction)
  - `derek-init.md` - Reduced from ~400 to 180 lines (~55% reduction)
  - Consolidated redundant sections while preserving all essential information
  - Maintained all critical templates and workflows
- **Planning Files**
  - Added cross-references between planning.md and spec-planning.md
  - Clarified relationship: planning.md (concise) ↔ spec-planning.md (detailed)

### Fixed
- **Consistency Issues**
  - Fixed directory naming: `.kiro/specs/` (was inconsistently `.kiro/features/`)
  - Fixed filename typo: `specialized..data-ai.md` → `specialized.data-ai.md`
  - Ensured consistent terminology across all documentation

### Removed
- `steering/hooks-after-code.md` - Replaced by actual hook implementations
- `steering/hooks-before-code.md` - Replaced by actual hook implementations
- Redundant and verbose documentation sections

### Changed
- **Inclusion Logic** - Updated specialized steering files (golang, python, rails, typescript)
- **POWER.md** - Added automated hooks section to commands list

### Statistics
- **Net Change**: -674 lines (35% reduction in codebase)
- **Added**: +531 lines (features + documentation)
- **Removed**: -1,205 lines (redundant/verbose content)
- **Files Modified**: 14 files
- **New Files**: 3 hooks + 1 README

---

## [0.1.1] - Previous Release

### Initial Features
- Project memory system with 5 core files (PROJECT, PROGRESS, DECISIONS, KNOWLEDGE, SCRATCHPAD)
- Folder spec planning system with approval gates
- 70+ specialized steering files organized by category
- Three implementation modes: quick implement, full spec workflow, manual spec creation
- Skill manager system for installing specialized capabilities
- Memory sharing via derek-memory MCP

---

## How to Upgrade

### From 0.1.3 to 0.1.4

1. **No breaking changes** — all existing functionality preserved
2. **Enable drift hook** (optional):
   - `cp derek-power/hooks/drift-detection.kiro.hook .kiro/hooks/`
   - Enables real-time drift recalculation on every file save
3. **Drift check runs automatically** on session start — no setup required

### From 0.1.1 to 0.1.2

1. **Update the power** in Kiro
2. **Enable new hooks** (optional):
   - Copy `quick-context-save.kiro.hook` to your project's `.kiro/hooks/` for automatic context reminders
   - `auto-summary-on-context-limit.kiro.hook` is automatically enhanced
3. **No breaking changes** - All existing functionality preserved
4. **Benefit from optimizations** - Steering files are now more token-efficient

### Recommended Setup

For most users:
```
✅ quick-context-save.kiro.hook (after code changes)
✅ auto-summary-on-context-limit.kiro.hook (session management)
```

For structured teams:
```
✅ post-code-context-capture.kiro.hook (detailed guidance)
✅ auto-summary-on-context-limit.kiro.hook (session management)
```

---

## Links

- [GitHub Repository](https://github.com/yourusername/derek-power)
- [Documentation](./derek-power/POWER.md)
- [Hooks Documentation](./derek-power/hooks/README.md)
