---
inclusion: manual
name: drift-detection
description: Calculates and reports how out-of-sync the D.E.R.E.K memory system is from actual workspace changes. Triggers automatically at session start and on-demand via "check drift", "drift status", or "drift history".
category: memory
---

# Drift Detection

This steering file defines how the D.E.R.E.K agent calculates, classifies, and responds to memory drift — the gap between the current state of workspace files and the last time the Memory_System was updated. Follow these instructions deterministically whenever drift detection is triggered.

---

## Definitions

- **Memory_System**: The five persistent files in `.kiro/resources/` — `PROJECT.md`, `PROGRESS.md`, `DECISIONS.md`, `KNOWLEDGE.md`, `SCRATCHPAD.md`.
- **Drift_Score**: An integer in [0, 100] representing the percentage of tracked workspace files that have changed since the last memory update.
- **Tracked_Files**: All workspace files after applying the exclusion rules below.
- **Last_Memory_Timestamp**: The most recent modification time across all five Memory_System files.
- **Drift_Tier**: One of four severity levels derived from the Drift_Score.

---

## Drift_Score Formula

```
Drift_Score = round((changed_files / total_tracked_files) × 100)
```

Where:
- `changed_files` = count of Tracked_Files with `mtime > Last_Memory_Timestamp`
- `total_tracked_files` = count of all Tracked_Files in the workspace

**Special cases:**
- If the Memory_System has never been initialized (`.kiro/resources/` does not exist or none of the five files exist): `Drift_Score = 100`
- If `total_tracked_files = 0` (empty workspace after exclusions): `Drift_Score = 0`

---

## Tracked_Files Exclusion Rules

When building the Tracked_Files set, exclude any file whose path contains or matches any of the following:

**Excluded directories (any path segment):**
- `node_modules/`
- `vendor/`
- `.git/`
- `tmp/`
- `log/`
- `dist/`
- `build/`
- `.kiro/resources/`

**Excluded binary file extensions:**
- `*.jpg` `*.jpeg` `*.png` `*.gif` `*.ico`
- `*.pdf` `*.zip` `*.tar` `*.gz` `*.exe`
- `*.bin` `*.woff` `*.woff2` `*.ttf` `*.eot`

Any file not matching an excluded directory or extension is a Tracked_File.

---

## Last_Memory_Timestamp Derivation

Read the modification time (`mtime`) of each of the five Memory_System files:

```
Last_Memory_Timestamp = max(
  mtime(.kiro/resources/PROJECT.md),
  mtime(.kiro/resources/PROGRESS.md),
  mtime(.kiro/resources/DECISIONS.md),
  mtime(.kiro/resources/KNOWLEDGE.md),
  mtime(.kiro/resources/SCRATCHPAD.md)
)
```

If none of the five files exist, `Last_Memory_Timestamp` is undefined and `Drift_Score` defaults to 100 (see Special Cases above).

---

## Drift_Tier Classification

Map the calculated `Drift_Score` to exactly one tier using the following table. Every integer from 0 to 100 maps to exactly one tier — there are no gaps or overlaps.

| Score Range | Tier | Indicator | Recommended Action |
|---|---|---|---|
| 0–20% | Healthy | 🟢 | Proceed normally |
| 21–50% | Review | 🟡 | Consider running `reinit` before proceeding |
| 51–75% | Soft_Block | 🟠 | Acknowledge changed files before proceeding |
| 76–100% | Hard_Block | 🔴 | Run `reinit` or `update memory` before any task execution |

---

## Tier Response Templates

Use these exact output formats when reporting drift. Replace `X`, `N`, and file paths with actual values.

### Healthy (🟢 — Score 0–20%)

```
🟢 Drift Score: X% (Healthy) — Memory is fresh.
N files changed since last memory update. Proceeding normally.
```

### Review (🟡 — Score 21–50%)

```
🟡 Drift Score: X% (Review) — Memory is getting stale.
N files changed since last memory update.
Recommendation: Run `reinit` before starting complex work to refresh PROJECT.md.
Proceeding — but consider updating memory soon.
```

### Soft_Block (🟠 — Score 51–75%)

```
🟠 Drift Score: X% (Soft_Block) — Memory is significantly stale.
N files changed since last memory update.

Most recently changed files:
  1. path/to/file.rb (X minutes ago)
  2. path/to/file.rb (Y minutes ago)
  3. ...up to 5 files

⚠️  Please acknowledge before proceeding.
Reply "acknowledge drift" to continue, or run `update memory` to refresh context.
```

List up to 5 of the most recently modified Tracked_Files, with their modification time expressed relative to `Last_Memory_Timestamp` (e.g., "3 minutes ago", "2 hours ago").

### Hard_Block (🔴 — Score 76–100%)

```
🔴 Drift Score: X% (Hard_Block) — Memory is severely out of date.
N files changed since last memory update.

Most recently changed files:
  1. path/to/file.rb (X minutes ago)
  2. ...up to 10 files

🚫 Task execution is blocked until memory is updated.
Run `reinit` to regenerate PROJECT.md, or `update memory` to update all memory files.
```

List up to 10 of the most recently modified Tracked_Files with relative timestamps. Do not proceed with any task execution until the user runs `reinit` or `update memory`.

---

## Session-Start Behavior Sequence

When a new D.E.R.E.K session begins (detected when the agent first reads `PROGRESS.md` via `derek-init.md`), execute the following steps in order:

1. **Scan Tracked_Files** — List all workspace files, apply the exclusion rules above, count the total. This is `total_tracked_files`.
2. **Read Last_Memory_Timestamp** — Check the `mtime` of all five `.kiro/resources/` files and take the maximum value.
3. **Count changed_files** — Count the Tracked_Files whose `mtime` is strictly greater than `Last_Memory_Timestamp`.
4. **Calculate Drift_Score** — Apply the formula: `round((changed_files / total_tracked_files) × 100)`. Apply special-case rules if applicable.
5. **Classify tier** — Map the score to Healthy, Review, Soft_Block, or Hard_Block using the classification table.
6. **Respond per tier** — Output the appropriate tier response template with actual values substituted.
7. **Write to PROGRESS.md** — Prepend a new entry to the `## Drift Status` section following the PROGRESS.md write rules below.

The drift report appears in session output between the memory read confirmation and the current task display:

```
✅ Memory System Exists
📁 .kiro/resources/ (last updated: X days ago)
🟡 Drift Score: 34% (Review) — 8 files changed. Consider running `reinit`.
🚀 Current task: [name] ([phase])
```

---

## On-Demand Command Patterns

Recognize the following user inputs (case-insensitive) and respond as described:

| User Input | Behavior |
|---|---|
| `check drift` | Full drift report: recalculate score, display tier, list top 5 most-recently-changed Tracked_Files with relative timestamps |
| `drift status` | Identical output to `check drift` |
| `drift history` | Read `## Drift Status` from PROGRESS.md and display the last 5 entries |
| `acknowledge drift` | Clear the Soft_Block gate and allow the session to proceed normally |

**`check drift` / `drift status` output** includes:
- Current Drift_Score and tier with indicator emoji
- Recommended action for the tier
- List of up to 5 most-recently-changed Tracked_Files with their modification time relative to `Last_Memory_Timestamp`

**`drift history` output** reads the `## Drift Status` section from PROGRESS.md and displays the 5 most recent entries. If fewer than 5 entries exist, display all available entries. If PROGRESS.md or the section does not exist, display: `(No drift history found — run a drift check to start recording history.)`

**`acknowledge drift`** clears the Soft_Block gate for the current session. The agent may proceed with the requested task. The Drift_Score is not recalculated; the acknowledgement simply removes the blocking requirement.

---

## PROGRESS.md Write Rules

After every drift calculation that produces a result (see error handling for exceptions), write a new entry to PROGRESS.md following these rules:

1. **Check for section**: Determine whether a `## Drift Status` section exists in PROGRESS.md.
2. **Create section if missing**: If the section does not exist, append `\n\n## Drift Status\n` after the last existing section in the file.
3. **Prepend new entry**: Insert the new entry immediately below the `## Drift Status` header line, before any existing entries.
4. **Enforce 10-entry cap**: Count the total number of entries in the section. If the count exceeds 10, remove the oldest (last) entry so the section contains exactly 10 entries.
5. **Entry format**:

```
[YYYY-MM-DD HH:MM] <indicator> Score: <X>% (<Tier>) — <N> files changed
```

Example entries:
```
[2025-01-15 09:32] 🟢 Score: 8% (Healthy) — 2 files changed
[2025-01-14 14:17] 🟡 Score: 34% (Review) — 8 files changed
[2025-01-13 11:05] 🟠 Score: 62% (Soft_Block) — 15 files changed
```

Use the local date and time in `YYYY-MM-DD HH:MM` format. Use the indicator emoji that matches the tier (🟢 Healthy, 🟡 Review, 🟠 Soft_Block, 🔴 Hard_Block).

---

## Memory Update Reset Behavior

### When any Memory_System file is saved

1. Recalculate `Drift_Score` using the new `Last_Memory_Timestamp` (which now reflects the saved file's updated `mtime`).
2. Report the updated score using the appropriate tier response template.
3. If the new score remains >= 51% (Soft_Block or Hard_Block): warn the user that additional memory updates are needed and list the remaining changed files.

### When `reinit` is run

- `PROJECT.md` is regenerated, updating its `mtime`.
- After regeneration completes, automatically recalculate `Drift_Score` using the new `Last_Memory_Timestamp`.
- Report the updated score.

### When `update memory` is run

- Prompt the user to update all relevant Memory_System files.
- After each file is saved, recalculate `Drift_Score` and report the updated score.
- Continue until the user has finished updating or the score drops below 51%.

---

## Post-Code-Change Behavior (Hook-Triggered)

When the `fileEdited` hook is active and a Tracked_File is edited, execute the following:

1. **Recalculate Drift_Score** using the current workspace state.
2. **Check tier**: If the tier is Review, Soft_Block, or Hard_Block, notify the user using the appropriate tier response template.
3. **Check for tier crossing**: Compare the current tier to the tier from the last check. If the score crossed a tier boundary, explicitly state the change. For example:
   - `"Drift crossed from Healthy → Review (score: 23%)"`
   - `"Drift crossed from Review → Soft_Block (score: 52%)"`
4. **Suppress duplicates**: If this hook has fired within the last 60 seconds, suppress the intermediate notification. Report only the final score at the end of the 60-second window.
5. **If tier is Healthy**: Remain silent — do not notify the user.

**Deduplication tracking**: Track the last hook-fire timestamp in SCRATCHPAD.md under the key `Last Drift Hook: <ISO timestamp>`. Before notifying, read this value. If the stored timestamp is within 60 seconds of the current time, suppress the notification and update the stored timestamp. If the stored timestamp is older than 60 seconds (or absent), proceed with notification and update the stored timestamp.

Example SCRATCHPAD.md entry:
```
Last Drift Hook: 2025-01-15T09:32:45Z
```

---

## Error Handling

### Uninitialized Memory System

**Condition**: `.kiro/resources/` does not exist, or none of the five Memory_System files exist.

**Behavior**:
- Set `Drift_Score = 100`, tier = Hard_Block.
- Display:
  ```
  🔴 Score: 100% (Hard_Block) — Memory system not initialized. Run 'init' to create the memory system.
  ```
- Do not attempt to write to PROGRESS.md (it likely does not exist either).

### Empty Workspace

**Condition**: After applying all exclusion rules, `total_tracked_files = 0`.

**Behavior**:
- Set `Drift_Score = 0`, tier = Healthy.
- Display:
  ```
  🟢 Score: 0% (Healthy) — No tracked files found in workspace.
  ```

### PROGRESS.md Missing `## Drift Status` Section

**Condition**: PROGRESS.md exists but does not contain a `## Drift Status` section.

**Behavior**:
- Append `\n\n## Drift Status\n` after the last existing section in the file.
- Write the new entry immediately below the newly created section header.
- Continue normally.

### PROGRESS.md Does Not Exist

**Condition**: PROGRESS.md itself is missing (partial or uninitialized memory system).

**Behavior**:
- Calculate and display the drift score normally using the appropriate tier response template.
- Skip the PROGRESS.md write step entirely.
- Append to the output: `(PROGRESS.md not found — drift history not saved)`

### Hook Deduplication

**Condition**: The `fileEdited` hook fires more than once within a 60-second window.

**Behavior**:
- Suppress intermediate notifications.
- Report only the final score at the end of the 60-second window.
- Track the last hook-fire timestamp in SCRATCHPAD.md under the key `Last Drift Hook: <ISO timestamp>`.
- On each hook fire: read the stored timestamp, compare to current time, suppress if within 60 seconds, update the stored timestamp regardless.
