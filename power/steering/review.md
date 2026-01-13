---
inclusion: manual
---

# Post-Implementation Review Framework

## Purpose
Validate that implemented code meets the approved plan, maintains quality standards, and is secure and maintainable. This is the final quality gate before code is considered complete.

**CRITICAL**: Review happens AFTER implementation but BEFORE considering the task complete. All critical issues must be addressed before closing the task.

---

## Review Prerequisites

Before starting review, verify:
- [ ] Implementation is complete according to the plan
- [ ] All planned tasks have been executed
- [ ] Tests have been written and are passing
- [ ] Code has been committed or is ready for review
- [ ] Documentation has been updated

**If prerequisites are not met, return to implementation phase.**

---

## Review Workflow

### Phase 1: Plan Compliance Review

#### Implementation vs. Plan Comparison
- [ ] Were all planned tasks completed?
- [ ] Were any unplanned changes made?
- [ ] Do the changes align with the approved approach?
- [ ] Were any shortcuts taken that compromise quality?
- [ ] Were any scope changes made without approval?

#### Deviation Analysis
If implementation deviates from plan:
- **Document deviations**: What changed and why?
- **Assess impact**: Do deviations introduce new risks?
- **Justify changes**: Are deviations improvements or compromises?
- **Update documentation**: Reflect actual implementation

#### Success Criteria Validation
- [ ] Are all success criteria from the plan met?
- [ ] Are acceptance criteria satisfied?
- [ ] Are performance targets achieved?
- [ ] Are security requirements fulfilled?

---

### Phase 2: Automated Code Review

#### Use `code-reviewer` Agent

The `code-reviewer` agent should be invoked for comprehensive automated analysis:

```markdown
**Invoke code-reviewer for:**
- Security vulnerability detection
- Code quality and maintainability assessment
- Performance issue identification
- Test coverage analysis
- Documentation completeness check
- Severity-tagged issue reporting
```

**When to use code-reviewer:**
- ✅ After every feature implementation
- ✅ After every bug fix
- ✅ Before pull request submission
- ✅ After significant refactoring
- ✅ Before deployment to production

**Code-reviewer provides:**
- Executive summary with scores (Security, Maintainability, Test Coverage)
- Critical issues (🔴) requiring immediate fix
- Major issues (🟡) requiring attention
- Minor suggestions (🟢) for improvement
- Positive highlights of good practices
- Action checklist with file:line references

---

### Phase 3: Manual Deep Review

#### Code Quality Assessment

**Readability & Maintainability**
- [ ] Code is self-documenting with clear naming
- [ ] Functions/methods are appropriately sized
- [ ] Complex logic has explanatory comments
- [ ] Code follows project conventions and style
- [ ] Abstractions are appropriate and not over-engineered
- [ ] Technical debt is minimized or documented

**Design & Architecture**
- [ ] Follows SOLID principles
- [ ] Appropriate design patterns used
- [ ] Separation of concerns maintained
- [ ] Dependencies are properly managed
- [ ] Code is modular and reusable
- [ ] Consistent with existing architecture

**Error Handling & Resilience**
- [ ] All error conditions are handled
- [ ] Error messages are informative but not leaky
- [ ] Graceful degradation where appropriate
- [ ] Proper logging of errors and exceptions
- [ ] Retry logic for transient failures
- [ ] Circuit breakers for external dependencies

---

### Phase 4: Security Deep Dive

#### Security Vulnerability Assessment

**Input Validation & Sanitization**
- [ ] All user inputs are validated
- [ ] Allowlist validation used where possible
- [ ] Input length and format restrictions enforced
- [ ] Special characters properly handled
- [ ] File uploads validated (type, size, content)

**Injection Prevention**
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Command injection prevented
- [ ] LDAP/NoSQL injection prevented
- [ ] Template injection prevented

**Authentication & Authorization**
- [ ] Authentication properly implemented
- [ ] Authorization checks on all sensitive operations
- [ ] Session management secure
- [ ] Token handling secure (JWT, API keys)
- [ ] Password handling secure (hashing, not logging)
- [ ] Multi-factor authentication where required

**Data Protection**
- [ ] Sensitive data encrypted at rest
- [ ] Sensitive data encrypted in transit (HTTPS/TLS)
- [ ] PII properly handled and not logged
- [ ] Secrets not hardcoded or committed
- [ ] Database credentials properly managed
- [ ] API keys and tokens securely stored

**API Security**
- [ ] Rate limiting implemented
- [ ] CORS properly configured
- [ ] CSRF protection in place
- [ ] Security headers configured
- [ ] API versioning secure
- [ ] Error responses don't leak information

#### Security Review Escalation

**When to escalate to security-guardian:**
- 🔴 Critical security vulnerabilities found
- 🔴 Authentication or authorization flaws
- 🔴 Data exposure or PII leakage risks
- 🔴 Injection vulnerabilities detected
- 🔴 Cryptographic implementation issues

---

### Phase 5: Performance Review

#### Performance Assessment

**Database Performance**
- [ ] No N+1 query problems
- [ ] Appropriate indexes exist
- [ ] Query complexity is reasonable
- [ ] Connection pooling properly configured
- [ ] Transactions scoped appropriately
- [ ] Bulk operations used where appropriate

**Application Performance**
- [ ] No obvious performance bottlenecks
- [ ] Caching used appropriately
- [ ] Async operations where beneficial
- [ ] Memory usage reasonable
- [ ] Resource cleanup proper (connections, files)
- [ ] Algorithm complexity acceptable

**Scalability Considerations**
- [ ] Code scales with increased load
- [ ] No hardcoded limits that constrain growth
- [ ] Stateless design where appropriate
- [ ] Horizontal scaling possible
- [ ] Resource usage predictable

#### Performance Review Escalation

**When to escalate to performance-optimizer:**
- 🟡 Significant performance degradation detected
- 🟡 N+1 query problems found
- 🟡 Memory leaks or excessive memory usage
- 🟡 Slow response times or timeouts
- 🟡 Inefficient algorithms or data structures

---

### Phase 6: Testing Review

#### Test Coverage Assessment

**Unit Tests**
- [ ] All new functions/methods have unit tests
- [ ] Edge cases are covered
- [ ] Error conditions are tested
- [ ] Mocks and stubs used appropriately
- [ ] Tests are deterministic and reliable
- [ ] Test coverage meets project standards

**Integration Tests**
- [ ] API endpoints have integration tests
- [ ] External service integrations tested
- [ ] Database interactions tested
- [ ] End-to-end workflows validated
- [ ] Error scenarios tested

**Security Tests**
- [ ] Authentication scenarios tested
- [ ] Authorization rules validated
- [ ] Input validation tested
- [ ] Injection attack prevention tested
- [ ] Security controls verified

**Performance Tests**
- [ ] Performance benchmarks exist
- [ ] Load testing performed if needed
- [ ] Database query performance validated
- [ ] Response time thresholds verified

#### Test Quality
- [ ] Tests are readable and maintainable
- [ ] Test data setup is clear
- [ ] Tests are isolated and independent
- [ ] Test names clearly describe what's tested
- [ ] Assertions are specific and meaningful

---

### Phase 7: Documentation Review

#### Code Documentation
- [ ] Complex logic has explanatory comments
- [ ] Public APIs are documented
- [ ] Function/method signatures documented
- [ ] Non-obvious decisions explained
- [ ] TODOs and FIXMEs addressed or tracked

#### Technical Documentation
- [ ] README updated if needed
- [ ] API documentation updated
- [ ] Architecture diagrams updated
- [ ] Configuration documentation updated
- [ ] Migration guides provided if needed

#### Operational Documentation
- [ ] Deployment procedures documented
- [ ] Rollback procedures documented
- [ ] Monitoring and alerting documented
- [ ] Troubleshooting guides updated
- [ ] Runbooks updated if needed

---

### Phase 8: Deployment Readiness

#### Pre-Deployment Checklist
- [ ] All tests passing in CI/CD
- [ ] Code review approved
- [ ] Security review passed
- [ ] Performance validated
- [ ] Database migrations tested
- [ ] Configuration changes documented
- [ ] Rollback plan ready
- [ ] Monitoring and alerts configured

#### Deployment Validation
- [ ] Smoke tests defined
- [ ] Health check endpoints working
- [ ] Metrics and logging verified
- [ ] Feature flags configured if used
- [ ] Gradual rollout plan if applicable

---

## Review Output Template

```markdown
# Post-Implementation Review Report

## Task: [Task Name/ID]
**Reviewer**: [Name/Agent]
**Date**: [Date]
**Implementation Status**: Complete / Incomplete / Needs Revision

---

## Executive Summary

### Plan Compliance
- **Status**: ✅ Fully Compliant / ⚠️ Minor Deviations / ❌ Major Deviations
- **Deviations**: [List any deviations from approved plan]
- **Justification**: [Rationale for deviations]

### Quality Scores
| Metric | Score | Notes |
|--------|-------|-------|
| Security | A-F | [Brief assessment] |
| Code Quality | A-F | [Brief assessment] |
| Performance | A-F | [Brief assessment] |
| Test Coverage | X% | [Coverage details] |
| Documentation | A-F | [Brief assessment] |

### Overall Assessment
[2-3 sentence summary of implementation quality and readiness]

---

## 🔴 Critical Issues (Must Fix Before Deployment)

| Priority | File:Line | Issue | Impact | Recommended Fix |
|----------|-----------|-------|--------|-----------------|
| P0 | [file:line] | [Description] | [Security/Data/Performance] | [Specific fix] |
| P0 | [file:line] | [Description] | [Security/Data/Performance] | [Specific fix] |

**Critical Issue Details**:
1. **[Issue Title]**
   - **Location**: [file:line]
   - **Description**: [Detailed description]
   - **Risk**: [What could go wrong]
   - **Fix**: [Step-by-step fix]
   - **Verification**: [How to verify fix]

---

## 🟡 Major Issues (Should Fix Soon)

| Priority | File:Line | Issue | Impact | Recommended Fix |
|----------|-----------|-------|--------|-----------------|
| P1 | [file:line] | [Description] | [Maintainability/Performance] | [Specific fix] |
| P1 | [file:line] | [Description] | [Maintainability/Performance] | [Specific fix] |

**Major Issue Details**:
1. **[Issue Title]**
   - **Location**: [file:line]
   - **Description**: [Detailed description]
   - **Impact**: [Technical debt/performance impact]
   - **Fix**: [Recommended approach]

---

## 🟢 Minor Suggestions (Optional Improvements)

- **[file:line]**: [Suggestion for improvement]
- **[file:line]**: [Style or documentation suggestion]
- **[file:line]**: [Refactoring opportunity]

---

## ✅ Positive Highlights

- ✅ **[Aspect]**: [What was done well]
- ✅ **[Aspect]**: [Good practice observed]
- ✅ **[Aspect]**: [Effective implementation]

---

## Security Review

### Security Assessment
- **Overall Security**: ✅ Secure / ⚠️ Minor Concerns / ❌ Critical Issues
- **Vulnerabilities Found**: [Count and severity]
- **Security Controls**: [List implemented controls]

### Security Findings
1. **[Finding]**: [Description and remediation]
2. **[Finding]**: [Description and remediation]

### Security Sign-off
- [ ] No critical security issues
- [ ] All security controls implemented
- [ ] Security testing passed
- [ ] Ready for security approval

---

## Performance Review

### Performance Assessment
- **Overall Performance**: ✅ Good / ⚠️ Acceptable / ❌ Issues Found
- **Response Times**: [Measurements]
- **Database Performance**: [Query analysis]
- **Resource Usage**: [Memory, CPU observations]

### Performance Findings
1. **[Finding]**: [Description and optimization]
2. **[Finding]**: [Description and optimization]

---

## Testing Review

### Test Coverage Summary
- **Unit Test Coverage**: [X%]
- **Integration Tests**: [Count/Status]
- **Security Tests**: [Count/Status]
- **Performance Tests**: [Count/Status]

### Test Quality Assessment
- **Test Completeness**: ✅ Comprehensive / ⚠️ Adequate / ❌ Insufficient
- **Edge Cases Covered**: [Yes/No/Partial]
- **Error Scenarios Tested**: [Yes/No/Partial]

### Testing Gaps
- [ ] [Missing test scenario]
- [ ] [Untested edge case]
- [ ] [Missing integration test]

---

## Documentation Review

### Documentation Completeness
- **Code Comments**: ✅ Good / ⚠️ Adequate / ❌ Insufficient
- **API Documentation**: ✅ Updated / ⚠️ Partial / ❌ Missing
- **Technical Docs**: ✅ Updated / ⚠️ Partial / ❌ Missing
- **Operational Docs**: ✅ Updated / ⚠️ Partial / ❌ Missing

### Documentation Gaps
- [ ] [Missing documentation item]
- [ ] [Incomplete documentation]

---

## Deployment Readiness

### Pre-Deployment Status
- [ ] All critical issues resolved
- [ ] All tests passing
- [ ] Security review approved
- [ ] Performance validated
- [ ] Documentation complete
- [ ] Rollback plan ready
- [ ] Monitoring configured

### Deployment Recommendation
- **Status**: ✅ Ready / ⚠️ Ready with Conditions / ❌ Not Ready
- **Conditions**: [Any conditions for deployment]
- **Risks**: [Remaining risks to be aware of]

---

## Action Checklist

### Immediate Actions (Before Deployment)
- [ ] **[Action 1]**: [Description] - Owner: [Name] - Due: [Date]
- [ ] **[Action 2]**: [Description] - Owner: [Name] - Due: [Date]

### Follow-up Actions (Post-Deployment)
- [ ] **[Action 1]**: [Description] - Owner: [Name] - Due: [Date]
- [ ] **[Action 2]**: [Description] - Owner: [Name] - Due: [Date]

### Technical Debt Created
- [ ] **[Debt Item]**: [Description] - Priority: [L/M/H] - Tracked: [Ticket ID]

---

## Specialist Agent Recommendations

### Escalations Required
- [ ] **security-guardian**: [Reason for escalation]
- [ ] **performance-optimizer**: [Reason for escalation]
- [ ] **refactoring-expert**: [Reason for escalation]

### Additional Reviews Needed
- [ ] [Type of review]: [Justification]

---

## Sign-off

### Review Completion
- **Reviewer**: [Name/Agent]
- **Review Date**: [Date]
- **Review Duration**: [Time spent]
- **Status**: ✅ Approved / ⚠️ Approved with Conditions / ❌ Rejected

### Approval Conditions
[List any conditions that must be met for approval]

### Next Steps
[Clear guidance on what happens next]
```

---

## Review Severity Guidelines

### 🔴 Critical (P0) - Must Fix Immediately
- Security vulnerabilities (injection, auth bypass, data exposure)
- Data corruption or loss risks
- Production-breaking bugs
- Performance issues causing outages
- Compliance violations

**Action**: Block deployment until fixed

### 🟡 Major (P1) - Should Fix Soon
- Significant performance degradation
- Maintainability issues
- Missing important tests
- Incomplete error handling
- Technical debt that will compound

**Action**: Fix before next release or create tracked ticket

### 🟢 Minor (P2) - Optional Improvements
- Style inconsistencies
- Documentation improvements
- Refactoring opportunities
- Nice-to-have optimizations
- Code clarity enhancements

**Action**: Consider for future improvements

---

## Integration with Code-Reviewer Agent

### Automated Review Invocation

```markdown
**Step 1**: Invoke code-reviewer agent
- Provide: Changed files, commit range, or directory
- Receive: Comprehensive review report with severity tags

**Step 2**: Analyze code-reviewer output
- Review critical issues (🔴)
- Assess major issues (🟡)
- Note minor suggestions (🟢)
- Acknowledge positive highlights

**Step 3**: Perform manual deep dive
- Focus on areas code-reviewer flagged
- Validate security controls
- Verify performance characteristics
- Check test coverage

**Step 4**: Escalate to specialists if needed
- security-guardian for critical security issues
- performance-optimizer for performance problems
- refactoring-expert for complex refactoring needs

**Step 5**: Compile comprehensive review report
- Combine automated and manual findings
- Prioritize issues by severity
- Provide actionable recommendations
- Create clear action checklist
```

---

## Review Best Practices

### For Reviewers
- Be thorough but constructive
- Provide specific, actionable feedback
- Include code examples for fixes
- Acknowledge good practices
- Focus on high-impact issues first
- Consider maintainability and future developers

### For Implementers
- Address all critical issues before requesting re-review
- Provide context for deviations from plan
- Update tests and documentation
- Run automated checks before review
- Be open to feedback and suggestions
- Document decisions and trade-offs

---

## Red Flags - Reject and Revise

If any of these conditions exist, REJECT the implementation:

- ❌ Critical security vulnerabilities present
- ❌ No tests for new functionality
- ❌ Significant deviations from approved plan without justification
- ❌ Production-breaking bugs
- ❌ Data corruption or loss risks
- ❌ Hardcoded secrets or credentials
- ❌ Major performance regressions
- ❌ Missing error handling for critical paths

---

## Remember

**Review is the last line of defense before production.** A thorough review:
- Catches bugs before users do
- Prevents security vulnerabilities
- Maintains code quality over time
- Ensures documentation stays current
- Validates that implementation matches intent
- Protects the team from technical debt

**Never skip review, even for "small" changes.** Small changes can have big impacts.

**Review is not about finding fault—it's about ensuring quality and learning together.**
