---
inclusion: manual
---

# Task Analysis Framework

## Purpose
Enforce comprehensive analysis before any planning or implementation. This phase ensures complete understanding of requirements, risks, and constraints before proceeding to solution design.

**CRITICAL**: NO CODE should be generated during this phase. Analysis must be completed and approved before moving to planning.

---

## Analysis Workflow

### 1. Task Understanding & Goal Definition

#### Primary Objectives
- [ ] What is the core problem being solved?
- [ ] What are the expected outcomes and success criteria?
- [ ] Who are the stakeholders and end users affected?
- [ ] What business value does this deliver?

#### Scope Definition
- [ ] What is explicitly IN scope?
- [ ] What is explicitly OUT of scope?
- [ ] Are there any scope ambiguities that need clarification?
- [ ] What are the acceptance criteria?

#### Requirements Gathering
- [ ] Functional requirements clearly documented
- [ ] Non-functional requirements identified (performance, scalability, etc.)
- [ ] User experience and interface requirements
- [ ] Data and integration requirements
- [ ] Compliance and regulatory requirements

---

### 2. System Context & Impact Analysis

#### Affected Components
- [ ] Which modules, services, or systems will be modified?
- [ ] Which APIs or interfaces will be affected?
- [ ] What database tables or schemas are involved?
- [ ] Which background jobs or async processes are impacted?
- [ ] What frontend components or pages need changes?

#### Integration Points
- [ ] External service dependencies (APIs, webhooks, etc.)
- [ ] Internal service dependencies and communication patterns
- [ ] Database relationships and data flow
- [ ] Message queue or event streaming dependencies
- [ ] Cache invalidation and synchronization needs

#### Blast Radius Assessment
- [ ] How many users will be affected?
- [ ] What is the criticality of affected functionality?
- [ ] Are there any high-traffic or performance-sensitive areas?
- [ ] What is the rollback complexity?
- [ ] Are there any irreversible operations?

---

### 3. Risk Assessment & Mitigation

#### Technical Risks
- [ ] **Performance risks**: Query performance, memory usage, response times
- [ ] **Scalability risks**: Load handling, concurrent user impact
- [ ] **Data integrity risks**: Migration safety, data loss potential
- [ ] **Integration risks**: Third-party service failures, timeout handling
- [ ] **Compatibility risks**: Breaking changes, backward compatibility

#### Security Risks
- [ ] **Authentication risks**: Login, session management, token handling
- [ ] **Authorization risks**: Access control, permission escalation
- [ ] **Data exposure risks**: PII leakage, sensitive data in logs
- [ ] **Injection risks**: SQL, XSS, command injection vectors
- [ ] **API security risks**: Rate limiting, input validation, CSRF

#### Business Risks
- [ ] **Revenue impact**: Payment processing, billing, settlements
- [ ] **Operational impact**: Driver matching, booking lifecycle, dispatching
- [ ] **User experience impact**: Customer satisfaction, driver efficiency
- [ ] **Compliance risks**: Regulatory requirements, audit trails
- [ ] **Reputational risks**: Public-facing features, customer trust

#### Mitigation Strategies
- [ ] What safeguards can be implemented?
- [ ] What monitoring and alerting is needed?
- [ ] What rollback procedures are required?
- [ ] What testing strategies will validate safety?
- [ ] What gradual rollout or feature flags are appropriate?

---

### 4. Dependencies & Prerequisites

#### Technical Dependencies
- [ ] Required library or framework versions
- [ ] Database schema changes or migrations needed
- [ ] Infrastructure or configuration changes required
- [ ] Third-party service setup or API access
- [ ] Development environment setup needs

#### Data Dependencies
- [ ] Existing data that must be migrated or transformed
- [ ] Reference data or seed data requirements
- [ ] Data cleanup or preparation needed
- [ ] Backup and recovery procedures

#### Team Dependencies
- [ ] Other teams or services that must be coordinated
- [ ] Blocking tasks or parallel work streams
- [ ] Code review or approval requirements
- [ ] Documentation or knowledge transfer needs

#### Timeline Dependencies
- [ ] Hard deadlines or release windows
- [ ] Dependent features or projects
- [ ] Testing and QA timeline requirements
- [ ] Deployment scheduling constraints

---

### 5. Constraints & Assumptions

#### Technical Constraints
- [ ] Technology stack limitations (Ruby 2.5.3, Rails 4.2.x)
- [ ] Performance requirements and SLAs
- [ ] Browser or device compatibility requirements
- [ ] Database or infrastructure limitations
- [ ] API rate limits or quotas

#### Business Constraints
- [ ] Budget or resource limitations
- [ ] Time-to-market requirements
- [ ] Regulatory or compliance requirements
- [ ] Contractual obligations
- [ ] Market or competitive pressures

#### Assumptions
- [ ] What are we assuming about user behavior?
- [ ] What are we assuming about system state?
- [ ] What are we assuming about data quality?
- [ ] What are we assuming about external services?
- [ ] Which assumptions need validation?

---

### 6. Data & State Analysis

#### Current State
- [ ] What is the current system behavior?
- [ ] What data currently exists and in what format?
- [ ] What are the current performance characteristics?
- [ ] What are the current pain points or limitations?

#### Desired State
- [ ] What should the system behavior be after changes?
- [ ] What data transformations are required?
- [ ] What performance improvements are expected?
- [ ] What new capabilities will be enabled?

#### Transition Strategy
- [ ] How will we migrate from current to desired state?
- [ ] What is the data migration strategy?
- [ ] How will we handle in-flight transactions?
- [ ] What is the rollback strategy if needed?

---

### 7. Observability & Monitoring

#### Metrics & KPIs
- [ ] What metrics will measure success?
- [ ] What performance indicators need monitoring?
- [ ] What business metrics are affected?
- [ ] What error rates or thresholds are acceptable?

#### Logging Requirements
- [ ] What events need to be logged?
- [ ] What log levels are appropriate?
- [ ] What PII or sensitive data must be excluded?
- [ ] What audit trail requirements exist?

#### Alerting & Monitoring
- [ ] What alerts need to be configured?
- [ ] What dashboards need to be created or updated?
- [ ] What on-call procedures are needed?
- [ ] What health checks or probes are required?

---

### 8. Testing Strategy Outline

#### Test Scope
- [ ] Unit testing requirements and coverage goals
- [ ] Integration testing scenarios
- [ ] End-to-end testing workflows
- [ ] Performance and load testing needs
- [ ] Security testing requirements

#### Test Data
- [ ] What test data is needed?
- [ ] How will test data be generated or seeded?
- [ ] What edge cases must be covered?
- [ ] What error conditions need testing?

#### Test Environments
- [ ] Development environment testing
- [ ] Staging environment validation
- [ ] Production-like testing requirements
- [ ] Rollback testing procedures

---

## Analysis Output Template

```markdown
## Task Analysis Summary

### Goal & Scope
[Clear statement of what we're solving and why]

### Affected Systems
- **Components**: [List of modules, services, files]
- **Integrations**: [External/internal dependencies]
- **Data**: [Database tables, schemas, data flows]

### Risk Assessment
#### Critical Risks
- [Risk 1]: [Description] → [Mitigation]
- [Risk 2]: [Description] → [Mitigation]

#### Medium Risks
- [Risk 3]: [Description] → [Mitigation]

### Dependencies & Blockers
- [Dependency 1]: [Status/Action needed]
- [Dependency 2]: [Status/Action needed]

### Key Constraints
- [Constraint 1]: [Impact on solution]
- [Constraint 2]: [Impact on solution]

### Critical Assumptions
- [Assumption 1]: [Validation needed?]
- [Assumption 2]: [Validation needed?]

### Success Criteria
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]
- [ ] [Measurable outcome 3]

### Open Questions
1. [Question requiring clarification]
2. [Question requiring stakeholder input]

### Recommended Next Steps
1. [Action item 1]
2. [Action item 2]
3. Proceed to planning phase once approved
```

---

## Analysis Approval Checklist

Before proceeding to planning phase, verify:

- [ ] All stakeholders understand the problem and goals
- [ ] Scope is clearly defined with no major ambiguities
- [ ] Critical risks have identified mitigation strategies
- [ ] All dependencies and blockers are documented
- [ ] Constraints and assumptions are validated
- [ ] Success criteria are measurable and agreed upon
- [ ] Open questions have been resolved or escalated

**Only after this checklist is complete should planning begin.**

---

## Red Flags - Stop and Clarify

If any of these conditions exist, STOP and seek clarification:

- ❌ Requirements are vague or contradictory
- ❌ Critical security risks without clear mitigation
- ❌ Unclear scope or acceptance criteria
- ❌ Missing stakeholder input or approval
- ❌ Unvalidated assumptions about system behavior
- ❌ Unknown dependencies or integration points
- ❌ Insufficient understanding of current system state
- ❌ No clear rollback or recovery strategy for high-risk changes

---

## Remember

**Analysis is about understanding, not solving.** The goal is to gather complete information and identify risks before designing solutions. Rushing to code without thorough analysis leads to:

- Security vulnerabilities
- Performance problems
- Scope creep and rework
- Production incidents
- Technical debt
- User dissatisfaction

Take the time to analyze thoroughly. It's faster than fixing problems later.
