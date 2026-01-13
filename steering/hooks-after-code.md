---
inclusion: manual
name: hooks-after-code
description: D.E.R.E.K post-code review hook. Performs systematic code review with security focus. Load manually when setting up Kiro hooks.
---

# D.E.R.E.K After Code Hook

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose

Perform systematic code review with focus on security, maintainability, and knowledge capture. Implements the **Review** phase and captures **Knowledge**.

## Hook Configuration

To set up this hook in Kiro, create a hook with:
- **Trigger**: After code generation / on file save
- **Action**: Send message with this steering file content

## D.E.R.E.K Post-Code Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      D.E.R.E.K POST-CODE VALIDATION                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  [CODE COMPLETE] → REVIEW → VALIDATE → UPDATE MEMORY → KNOWLEDGE            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Review Framework

### 1. Security Analysis (CRITICAL)

#### Input Validation & Injection
- [ ] All inputs validated and sanitized
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Command injection prevention

#### Authentication & Authorization
- [ ] Proper auth checks implemented
- [ ] Authorization logic correct
- [ ] Session management secure

#### Data Protection
- [ ] Sensitive data not logged
- [ ] Proper encryption applied
- [ ] Secrets managed securely

### 2. Code Quality
- [ ] Idiomatic code for target language
- [ ] Proper error handling
- [ ] Single responsibility principle
- [ ] DRY - no duplication

### 3. Performance
- [ ] No N+1 queries
- [ ] Proper indexing
- [ ] Resource cleanup

### 4. Testing
- [ ] Unit tests for new code
- [ ] Edge cases covered

## Memory Updates

After review, update:
1. `PROGRESS.md` - Task status
2. `DECISIONS.md` - Key decisions made
3. `KNOWLEDGE.md` - Patterns learned (on feature completion)

## Review Output Template

```markdown
## D.E.R.E.K Code Review Summary

### 🔴 Critical Issues
| Issue | Location | Fix |
|-------|----------|-----|

### 🟡 High Priority
| Issue | Location | Recommendation |
|-------|----------|----------------|

### ✅ Positive Observations
- [Good practices noted]

### 📋 Memory Updates Required
- [ ] Update PROGRESS.md
- [ ] Log decisions in DECISIONS.md
```

## OWASP Quick Check

| Vulnerability | Status |
|---------------|--------|
| A01: Broken Access Control | ✅/❌ |
| A02: Cryptographic Failures | ✅/❌ |
| A03: Injection | ✅/❌ |
| A07: Auth Failures | ✅/❌ |
| A10: SSRF | ✅/❌ |

## Default Action

If critical issues found:
```
🔴 **D.E.R.E.K Security Gate Failed**

Critical issues detected. Fix before deployment.
```
