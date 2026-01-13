---
name: quality-testing
description: Comprehensive quality assurance and testing guidance covering test strategy, automation frameworks, quality metrics, and continuous testing practices. This steering file provides foundational principles and best practices for ensuring software quality throughout the development lifecycle.
---

# Quality Assurance & Testing

**Purpose**: Establish comprehensive quality assurance and testing practices to ensure software products meet the highest standards of quality, reliability, security, and user satisfaction. This guidance covers test strategy, automation, quality metrics, and continuous testing integration across the entire software development lifecycle.

## Core Quality Principles

### 1. Quality Gates & Process
- **Prevention Over Detection**: Engage early in the development lifecycle to prevent defects rather than finding them later
- **Comprehensive Testing**: All new logic must be covered by unit, integration, and E2E tests
- **No Failing Builds**: Strict policy that failing builds are never merged into the main branch
- **Test Behavior, Not Implementation**: Focus on user interactions and observable outcomes, not internal details
- **Continuous Testing**: Automated testing integrated into every stage of the CI/CD pipeline
- **Risk-Based Testing**: Prioritize testing efforts based on potential impact and business criticality

### 2. Definition of Done
A feature is not considered "done" until it meets these criteria:
- All tests (unit, integration, E2E) are passing
- Code meets established style guides and quality standards
- No console errors or unhandled exceptions
- All API endpoints and contract changes are documented
- Code coverage meets minimum thresholds
- Performance benchmarks are met
- Security scanning shows no critical vulnerabilities
- Accessibility standards are validated

### 3. Test Pyramid Strategy
- **Large Base of Unit Tests**: Fast, isolated tests for individual components (70-80% of tests)
- **Integration Tests**: Verify interactions between modules and services (15-20% of tests)
- **E2E Tests**: Critical user journeys and business workflows (5-10% of tests)
- **Manual Exploratory Testing**: Human insight for usability and edge cases
- **Performance Tests**: Load, stress, and scalability validation
- **Security Tests**: Vulnerability scanning and penetration testing

### 4. Quality Culture
- **Shared Responsibility**: Quality is everyone's responsibility, not just QA
- **Blameless Post-Mortems**: Focus on system improvements, not individual blame
- **Continuous Improvement**: Regular retrospectives and process refinement
- **Metrics-Driven**: Use data to guide quality decisions and improvements
- **Customer Focus**: Prioritize user experience and satisfaction
- **Documentation**: Maintain clear, up-to-date testing documentation

## Test Strategy & Planning

### Test Strategy Development
- **Scope Definition**: Clear boundaries of what will and won't be tested
- **Test Objectives**: Specific, measurable quality goals aligned with business needs
- **Resource Planning**: Team allocation, tool selection, and timeline estimation
- **Risk Assessment**: Identify high-risk areas requiring focused testing attention
- **Environment Strategy**: Define test environments and data management approach
- **Entry/Exit Criteria**: Clear conditions for starting and completing test phases

### Test Case Design
- **Equivalence Partitioning**: Group similar inputs to reduce redundant tests
- **Boundary Value Analysis**: Test edge cases and limits
- **Decision Tables**: Cover complex business logic with multiple conditions
- **State Transition Testing**: Validate state changes and workflows
- **Error Guessing**: Leverage experience to anticipate likely defects
- **Exploratory Testing**: Unscripted testing for discovering unexpected issues

### Test Data Management
- **Realistic Data**: Test data that mirrors production scenarios
- **Data Privacy**: Anonymization and masking of sensitive information
- **Data Generation**: Automated creation of varied test datasets
- **Data Versioning**: Track and manage test data changes
- **Data Cleanup**: Automated cleanup after test execution
- **Production Subsets**: Carefully managed subsets of production data when needed

## Test Automation

### Automation Strategy
- **Automation Pyramid**: Follow the test pyramid for optimal automation ROI
- **Tool Selection**: Choose frameworks that fit team skills and project needs
- **Maintainability**: Write clean, readable, and maintainable test code
- **Reusability**: Create reusable test components and utilities
- **Stability**: Eliminate flaky tests through proper synchronization and isolation
- **Speed**: Optimize test execution time with parallelization and smart selection

### Unit Testing Best Practices
- **Arrange-Act-Assert (AAA)**: Structure tests with clear setup, execution, and verification
- **Single Responsibility**: Each test validates one specific behavior
- **Test Isolation**: Tests must not depend on each other or shared state
- **Mock External Dependencies**: Isolate unit under test from external systems
- **Fast Execution**: Unit tests should run in milliseconds
- **Descriptive Names**: Test names clearly describe what is being tested
- **Code Coverage**: Aim for 80%+ coverage with focus on critical paths

### Integration Testing
- **API Testing**: Validate REST/GraphQL endpoints, status codes, and responses
- **Database Integration**: Test data persistence and retrieval operations
- **Service Integration**: Verify interactions between microservices
- **Message Queue Testing**: Validate asynchronous messaging patterns
- **Third-Party Integration**: Test external API integrations with mocks and contracts
- **Contract Testing**: Ensure API contracts are maintained between services
- **Testcontainers**: Use containerized dependencies for realistic integration tests

### End-to-End Testing
- **Critical User Journeys**: Focus on high-value business workflows
- **Cross-Browser Testing**: Validate across major browsers and versions
- **Mobile Testing**: Test responsive design and mobile-specific features
- **Visual Regression**: Detect unintended UI changes with screenshot comparison
- **Accessibility Testing**: Validate WCAG compliance and screen reader support
- **Performance Testing**: Monitor page load times and Core Web Vitals
- **Minimal E2E Tests**: Keep E2E suite small and focused on critical paths

### Test Automation Frameworks
- **JavaScript/TypeScript**: Jest, Vitest, Playwright, Cypress, Testing Library
- **Python**: Pytest, unittest, Robot Framework, Selenium
- **Java**: JUnit, TestNG, Mockito, REST Assured, Selenium
- **C#**: NUnit, xUnit, Moq, SpecFlow
- **Ruby**: RSpec, Minitest, Capybara
- **Go**: testing package, testify, Ginkgo

## CI/CD Integration

### Continuous Testing Pipeline
- **Commit Stage**: Fast unit tests run on every commit (< 5 minutes)
- **Integration Stage**: Integration tests after successful unit tests (< 15 minutes)
- **E2E Stage**: Critical E2E tests before deployment (< 30 minutes)
- **Performance Stage**: Load tests on staging environment
- **Security Stage**: Vulnerability scanning and security tests
- **Deployment Verification**: Smoke tests after production deployment

### Pipeline Best Practices
- **Fail Fast**: Run fastest tests first to provide rapid feedback
- **Parallel Execution**: Run independent tests concurrently
- **Test Sharding**: Distribute tests across multiple runners
- **Smart Test Selection**: Run only tests affected by code changes
- **Flaky Test Management**: Quarantine and fix flaky tests immediately
- **Test Reporting**: Clear, actionable test reports with failure details
- **Automatic Rollback**: Trigger rollback on test failures in production

### Quality Gates
- **Code Coverage Threshold**: Minimum coverage percentage required
- **Test Pass Rate**: 100% pass rate required for deployment
- **Performance Benchmarks**: Response time and throughput requirements
- **Security Scan Results**: No critical or high vulnerabilities allowed
- **Code Quality Metrics**: Complexity, duplication, and maintainability thresholds
- **Accessibility Compliance**: WCAG AA compliance validation

## Performance Testing

### Performance Test Types
- **Load Testing**: Validate system behavior under expected load
- **Stress Testing**: Determine breaking points and failure modes
- **Spike Testing**: Test response to sudden traffic increases
- **Endurance Testing**: Validate stability over extended periods
- **Scalability Testing**: Verify horizontal and vertical scaling capabilities
- **Capacity Planning**: Determine maximum sustainable load

### Performance Testing Tools
- **Load Testing**: JMeter, Gatling, k6, Locust, Artillery
- **APM Tools**: New Relic, DataDog, Dynatrace, AppDynamics
- **Browser Performance**: Lighthouse, WebPageTest, Chrome DevTools
- **Database Performance**: pg_stat_statements, MySQL Performance Schema
- **Profiling**: py-spy, pprof, VisualVM, dotTrace

### Performance Metrics
- **Response Time**: Average, median, 95th/99th percentile response times
- **Throughput**: Requests per second, transactions per minute
- **Error Rate**: Percentage of failed requests
- **Resource Utilization**: CPU, memory, disk, network usage
- **Concurrency**: Number of simultaneous users/connections
- **Core Web Vitals**: LCP, INP, CLS for frontend performance

## Security Testing

### Security Testing Practices
- **Static Analysis (SAST)**: Scan source code for vulnerabilities
- **Dynamic Analysis (DAST)**: Test running application for security issues
- **Dependency Scanning**: Identify vulnerable third-party libraries
- **Secret Scanning**: Detect exposed credentials and API keys
- **Container Scanning**: Scan Docker images for vulnerabilities
- **Infrastructure Scanning**: Validate cloud and infrastructure security
- **Penetration Testing**: Simulate real-world attacks on the system

### Security Testing Tools
- **SAST**: SonarQube, Semgrep, CodeQL, Checkmarx, Veracode
- **DAST**: OWASP ZAP, Burp Suite, Acunetix
- **Dependency Scanning**: Snyk, Dependabot, npm audit, pip-audit
- **Secret Scanning**: GitGuardian, TruffleHog, detect-secrets
- **Container Scanning**: Trivy, Clair, Anchore
- **Infrastructure**: Prowler, ScoutSuite, CloudSploit

### OWASP Top 10 Testing
- **Injection**: SQL, NoSQL, LDAP, command injection testing
- **Broken Authentication**: Session management and authentication testing
- **Sensitive Data Exposure**: Encryption and data protection validation
- **XML External Entities (XXE)**: XML parsing security testing
- **Broken Access Control**: Authorization and privilege escalation testing
- **Security Misconfiguration**: Configuration and hardening validation
- **Cross-Site Scripting (XSS)**: Input sanitization and output encoding testing
- **Insecure Deserialization**: Serialization security validation
- **Using Components with Known Vulnerabilities**: Dependency vulnerability scanning
- **Insufficient Logging & Monitoring**: Audit logging and monitoring validation

## Quality Metrics & Reporting

### Key Quality Metrics
- **Test Coverage**: Percentage of code covered by tests
- **Test Pass Rate**: Percentage of tests passing
- **Defect Density**: Number of defects per lines of code
- **Defect Escape Rate**: Defects found in production vs. testing
- **Mean Time to Detection (MTTD)**: Time to discover defects
- **Mean Time to Resolution (MTTR)**: Time to fix defects
- **Test Execution Time**: Duration of test suite execution
- **Flaky Test Rate**: Percentage of unstable tests

### Quality Dashboards
- **Real-Time Status**: Current build and test status
- **Trend Analysis**: Quality metrics over time
- **Coverage Reports**: Code coverage by module and team
- **Defect Tracking**: Open defects by severity and age
- **Performance Trends**: Response time and throughput trends
- **Security Posture**: Vulnerability counts and remediation status
- **Test Stability**: Flaky test identification and tracking

### Reporting Best Practices
- **Stakeholder-Specific**: Tailor reports to audience needs
- **Actionable Insights**: Focus on what needs attention
- **Visual Presentation**: Use charts and graphs for clarity
- **Regular Cadence**: Consistent reporting schedule
- **Historical Context**: Show trends and progress over time
- **Root Cause Analysis**: Include analysis of major issues
- **Recommendations**: Provide clear next steps and improvements

## Defect Management

### Defect Lifecycle
- **Discovery**: Identify and document the defect
- **Triage**: Assess severity, priority, and impact
- **Assignment**: Assign to appropriate developer
- **Resolution**: Fix the defect and verify locally
- **Verification**: QA validates the fix
- **Closure**: Close defect after successful verification
- **Regression Prevention**: Add test to prevent recurrence

### Defect Reporting
- **Clear Title**: Concise description of the issue
- **Steps to Reproduce**: Detailed reproduction steps
- **Expected vs. Actual**: What should happen vs. what happens
- **Environment Details**: Browser, OS, version information
- **Supporting Evidence**: Screenshots, logs, videos
- **Severity Classification**: Critical, high, medium, low
- **Priority Assignment**: Immediate, high, normal, low

### Root Cause Analysis
- **Five Whys**: Ask "why" repeatedly to find root cause
- **Fishbone Diagram**: Identify contributing factors
- **Pattern Recognition**: Look for similar defects
- **Process Gaps**: Identify process improvements needed
- **Preventive Actions**: Implement measures to prevent recurrence
- **Knowledge Sharing**: Document learnings for the team

## Specialized Testing

### Accessibility Testing
- **WCAG Compliance**: Validate against WCAG 2.1 AA/AAA standards
- **Screen Reader Testing**: Test with NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: Ensure full keyboard accessibility
- **Color Contrast**: Validate sufficient contrast ratios
- **Semantic HTML**: Proper use of HTML elements and ARIA
- **Automated Tools**: axe, Lighthouse, WAVE, Pa11y

### Mobile Testing
- **Device Coverage**: Test on representative devices and OS versions
- **Responsive Design**: Validate layouts across screen sizes
- **Touch Interactions**: Test gestures and touch targets
- **Network Conditions**: Test on various network speeds
- **Battery Impact**: Monitor battery consumption
- **App Store Guidelines**: Validate compliance with store requirements

### API Testing
- **Functional Testing**: Validate endpoints, methods, and responses
- **Contract Testing**: Ensure API contracts are maintained
- **Schema Validation**: Verify request/response schemas
- **Authentication**: Test auth mechanisms and token handling
- **Rate Limiting**: Validate throttling and quota enforcement
- **Error Handling**: Test error responses and status codes
- **Documentation**: Validate API documentation accuracy

## Related Steering Files

For specialized quality and testing topics, refer to these detailed steering files:

- **quality-testing.qa-expert.md**: Comprehensive QA processes, test planning, defect management, quality metrics
- **quality-testing.test-automator.md**: Test automation strategy, frameworks, CI/CD integration, test maintenance

## Success Metrics

Track these key metrics to measure quality effectiveness:

- **Test Coverage**: 80%+ code coverage with focus on critical paths
- **Test Pass Rate**: 100% pass rate required for deployment
- **Defect Escape Rate**: < 5% of defects found in production
- **Mean Time to Detection**: < 24 hours for critical defects
- **Mean Time to Resolution**: < 48 hours for critical defects
- **Test Execution Time**: < 30 minutes for full test suite
- **Flaky Test Rate**: < 1% of tests are flaky
- **Automation Coverage**: 80%+ of regression tests automated

## Continuous Improvement

Quality and testing practices should evolve continuously:

1. **Regular Retrospectives**: Review what's working and what needs improvement
2. **Metric-Driven Decisions**: Use quality metrics to guide improvements
3. **Test Maintenance**: Regularly refactor and update test suites
4. **Tool Evaluation**: Stay current with testing tools and frameworks
5. **Skill Development**: Invest in team training and certifications
6. **Process Refinement**: Continuously optimize testing processes
7. **Automation Expansion**: Gradually increase test automation coverage
8. **Knowledge Sharing**: Document and share testing best practices

---

**Remember**: Quality is not just about finding bugs—it's about preventing them, building confidence in the product, and enabling rapid, safe delivery of value to users. Every quality decision should support faster delivery while maintaining high standards of reliability, security, and user satisfaction.
