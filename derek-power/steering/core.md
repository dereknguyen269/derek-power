---
inclusion: manual
name: core
description: Core quality assurance agents for code exploration, review, and performance optimization. These agents are essential for maintaining code quality across any project.
---

# Core Agents

Essential quality assurance agents that work across all projects and tech stacks.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **Code Archaeologist** | `core.archaeologist.md` | Deep codebase exploration & documentation | Legacy code, onboarding, audits, refactoring prep |
| **Code Reviewer** | `core.reviewer.md` | Security-aware code review | After every feature, bug fix, or PR |
| **Debugger** | `core.debugger.md` | Error resolution & root cause analysis | Errors, test failures, unexpected behavior |
| **Performance Optimizer** | `core.performance-optimizer.md` | Bottleneck resolution & optimization | Slowness, high costs, scaling concerns |

## Agent Details

### Code Archaeologist
**File**: `#[[file:core.archaeologist.md]]`

Uncovers the real structure and quality of codebases. Produces comprehensive reports covering architecture, metrics, risks, and prioritized action plans.

**Use PROACTIVELY for:**
- Exploring unfamiliar or legacy codebases
- Pre-refactoring analysis
- Onboarding documentation
- Security and risk audits

**Output**: Full codebase assessment with health score, architecture diagrams, and prioritized recommendations.

---

### Code Reviewer
**File**: `#[[file:core.code-reviewer.md]]`

High-trust quality gate ensuring all code is secure, maintainable, performant, and understandable.

**Use PROACTIVELY for:**
- Every feature implementation
- Every bug fix
- Before merging to main branch
- Pull request reviews

**Output**: Severity-tagged review report with file:line references and action checklist.

**Delegation**: Routes issues to specialists:
- Security issues → `security-auditor` and `universal.api-security-audit`
- Performance issues → `core.performance-optimizer`

---

### Debugger
**File**: `#[[file:core.debugger.md]]`

Expert debugging agent for systematic error resolution and root cause analysis.

**Use PROACTIVELY for:**
- Error messages and stack traces
- Test failures
- Unexpected behavior
- Logic errors
- Performance debugging

**Output**: Debugging report with root cause, evidence, code fix (diff), and prevention recommendations.

**Key Techniques**: Systematic debugging, hypothesis testing, state inspection, log analysis.

---

### Performance Optimizer
**File**: `#[[file:core.performance-optimizer.md]]`

Locates real bottlenecks, applies high-impact fixes, and proves improvements with metrics.

**Use PROACTIVELY for:**
- User-reported slowness
- High cloud costs
- Scaling concerns
- Pre-release optimization
- Traffic spike preparation

**Output**: Performance report with before/after metrics and prioritized recommendations.

**Key Techniques**: Algorithm optimization, caching, concurrency, query tuning, infrastructure improvements.

---

## Loading Strategy

```
Single Review:     core.code-reviewer.md
Legacy Codebase:   core.code-archaeologist.md → core.code-reviewer.md
Debugging:         core.debugger.md
Performance Issue: core.performance-optimizer.md
Full Audit:        core.code-archaeologist.md → core.code-reviewer.md → core.performance-optimizer.md
```

## Integration with D.E.R.E.K

These agents integrate with the D.E.R.E.K workflow:

| D.E.R.E.K Phase | Core Agent |
|-----------------|------------|
| **E**valuate | Code Archaeologist (understand codebase) |
| **R**eview | Code Reviewer (quality gate) |
| **E**xecute | Performance Optimizer (optimize implementation) |
