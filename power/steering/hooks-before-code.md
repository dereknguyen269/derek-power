---
inclusion: manual
name: hooks-before-code
description: D.E.R.E.K pre-code validation hook. Enforces structured analysis and planning before code generation. Load manually when setting up Kiro hooks.
---

# D.E.R.E.K Before Code Hook

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose

Enforce structured analysis and planning before any code generation to ensure security, maintainability, and proper task context retention. This hook implements the **Design** and **Evaluate** phases of D.E.R.E.K.

## Hook Configuration

To set up this hook in Kiro, create a hook with:
- **Trigger**: Before code generation
- **Action**: Send message with this steering file content

## D.E.R.E.K Gate Check

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      D.E.R.E.K PRE-CODE VALIDATION                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐                             │
│  │  DESIGN  │────▶│ EVALUATE │────▶│  REVIEW  │────▶ [CODE GENERATION]      │
│  │    ✓?    │     │    ✓?    │     │    ✓?    │                             │
│  └──────────┘     └──────────┘     └──────────┘                             │
│       │                │                │                                    │
│       ▼                ▼                ▼                                    │
│  requirements.md   analysis.md    Approval Gate                              │
│  design.md         planning.md    (explicit)                                 │
│                                                                              │
│  If ANY gate fails → STOP and complete missing phase                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Validation Checklist

Before generating any code, verify:

### 1. D.E.R.E.K Memory Check
- [ ] `.kiro/resources/` exists (run "init" if not)
- [ ] `PROJECT.md` read for project context
- [ ] `PROGRESS.md` updated with current task

### 2. Design Phase Complete (for features)
- [ ] Feature folder exists: `.kiro/features/<name>/`
- [ ] `requirements.md` created and **approved**
- [ ] `design.md` created and **approved**

### 3. Evaluate Phase Complete
- [ ] Problem statement clearly defined
- [ ] Security implications assessed
- [ ] Dependencies mapped

### 4. Review Gate Passed
- [ ] Technical approach documented
- [ ] Security controls identified

## Response Templates

### If Memory Missing
```
⚠️ **D.E.R.E.K Memory System Not Initialized**

Run "init" to create `.kiro/resources/` before generating code.
```

### If Planning Missing
```
⚠️ **Analysis Required First**

Complete the D.E.R.E.K Evaluate phase before code generation.
Use `analysis.md` steering file.
```

## Security Gates

For high-risk operations (database, auth, external integrations):
- [ ] Input validation approach defined
- [ ] Authentication/authorization requirements clear
- [ ] Error handling strategy documented

## Default Response

If validation fails:
```
⛔ **D.E.R.E.K Gate Check Failed**

Code generation blocked. Please complete missing phases.
Commands: "init", "create feature <name>", "approve design"
```
