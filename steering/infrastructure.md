---
name: infrastructure
description: Comprehensive infrastructure and DevOps guidance covering cloud architecture, deployment automation, incident response, and performance engineering. This steering file provides foundational principles and best practices for building, deploying, and maintaining production-grade systems.
---

# Infrastructure & DevOps Engineering

**Purpose**: Establish comprehensive infrastructure and DevOps practices for building scalable, secure, and reliable production systems. This guidance covers cloud architecture, CI/CD automation, incident management, and performance optimization across the entire software delivery lifecycle.

## Core Infrastructure Principles

### 1. Infrastructure as Code (IaC)
- **Everything as Code**: All infrastructure components must be defined, versioned, and managed as code
- **Immutable Infrastructure**: Favor replacing infrastructure over modifying it in place
- **Version Control**: All IaC configurations must be stored in Git with proper change tracking
- **Automated Provisioning**: Manual infrastructure changes are prohibited in production
- **State Management**: Centralized state management with proper locking mechanisms
- **Modular Design**: Reusable, composable infrastructure modules with clear interfaces

### 2. Cloud-Native Architecture
- **Managed Services First**: Prefer cloud-managed services over self-hosted solutions
- **Multi-Region Design**: Architect for high availability across multiple regions
- **Auto-Scaling**: Implement dynamic scaling based on demand and performance metrics
- **Serverless Where Appropriate**: Leverage serverless technologies for event-driven workloads
- **Cost Optimization**: Continuous monitoring and optimization of cloud resource costs
- **Vendor Flexibility**: Design for portability to avoid vendor lock-in

### 3. Security by Design
- **Zero Trust Model**: Never trust, always verify - implement defense in depth
- **Least Privilege**: Grant minimum necessary permissions to all services and users
- **Encryption Everywhere**: Data encryption at rest and in transit by default
- **Secret Management**: Centralized secret storage with rotation and audit trails
- **Network Segmentation**: Proper VPC design with security groups and network policies
- **Compliance First**: Build compliance requirements into infrastructure from day one

### 4. Observability & Monitoring
- **Three Pillars**: Comprehensive logging, metrics, and distributed tracing
- **Proactive Monitoring**: Alert on symptoms before they become incidents
- **SLO-Driven**: Define and track Service Level Objectives for critical services
- **Centralized Logging**: Aggregated, searchable logs with retention policies
- **Real-Time Dashboards**: Visual monitoring of system health and performance
- **Automated Alerting**: Context-rich alerts with clear escalation paths

## CI/CD Pipeline Standards

### Pipeline Architecture
- **Single Source of Truth**: Git as the authoritative source for all code and configuration
- **Automated Testing**: Comprehensive test suites at every pipeline stage
- **Security Scanning**: Integrated SAST, DAST, and dependency vulnerability scanning
- **Quality Gates**: Automated checks that must pass before promotion
- **Artifact Management**: Immutable build artifacts with proper versioning
- **Environment Parity**: Consistent environments from development to production

### Deployment Strategies
- **Zero-Downtime Deployments**: Blue-green, canary, or rolling deployment patterns
- **Feature Flags**: Decouple deployment from release with feature toggles
- **Automated Rollbacks**: Instant rollback capability with health check validation
- **Progressive Delivery**: Gradual rollout with monitoring and automatic rollback
- **Database Migrations**: Backward-compatible migrations with rollback plans
- **Deployment Windows**: Scheduled deployments during low-traffic periods for high-risk changes

### Build Best Practices
- **Fast Feedback**: Optimize pipeline execution time for rapid iteration
- **Parallel Execution**: Run independent stages concurrently
- **Caching Strategy**: Intelligent caching of dependencies and build artifacts
- **Container Optimization**: Multi-stage builds with minimal final image size
- **Reproducible Builds**: Deterministic builds that produce identical artifacts
- **Build Once, Deploy Many**: Single artifact promoted across environments

## Incident Management Framework

### Incident Response Protocol
- **Severity Classification**: Clear P0-P3 severity levels with defined response times
- **Incident Command**: Designated Incident Commander for coordination
- **Communication Cadence**: Regular stakeholder updates every 15-30 minutes
- **Blameless Culture**: Focus on system failures, not individual blame
- **Documentation**: Real-time incident timeline and action tracking
- **Post-Mortem Process**: Mandatory post-incident analysis with action items

### On-Call Best Practices
- **Runbook Automation**: Comprehensive runbooks for common incidents
- **Alert Fatigue Prevention**: Meaningful alerts only, with proper thresholds
- **Escalation Paths**: Clear escalation procedures for different scenarios
- **On-Call Rotation**: Fair distribution of on-call responsibilities
- **Handoff Procedures**: Structured handoff process between on-call shifts
- **Mental Health**: Respect for work-life balance and burnout prevention

### Recovery Procedures
- **Disaster Recovery Plan**: Documented and tested DR procedures
- **Backup Strategy**: Regular backups with tested restoration procedures
- **RTO/RPO Targets**: Defined Recovery Time and Recovery Point Objectives
- **Failover Testing**: Regular chaos engineering and failover drills
- **Data Integrity**: Validation procedures for data consistency after recovery
- **Communication Plan**: Stakeholder communication templates and procedures

## Performance Engineering

### Performance Strategy
- **Performance Budgets**: Defined performance targets for critical user journeys
- **Continuous Monitoring**: Real-time tracking of performance metrics
- **Proactive Optimization**: Regular performance audits and improvements
- **Load Testing**: Realistic load tests simulating production traffic patterns
- **Capacity Planning**: Forecasting and planning for growth and peak loads
- **Performance Culture**: Performance considerations in all design decisions

### Optimization Techniques
- **Caching Layers**: Multi-tier caching strategy (CDN, application, database)
- **Database Optimization**: Query optimization, indexing, and connection pooling
- **Async Processing**: Background jobs for non-critical operations
- **Resource Efficiency**: CPU, memory, and I/O optimization
- **Network Optimization**: Compression, CDN usage, and connection reuse
- **Frontend Performance**: Core Web Vitals optimization and asset optimization

### Scalability Patterns
- **Horizontal Scaling**: Scale out with load balancing and stateless services
- **Database Scaling**: Read replicas, sharding, and caching strategies
- **Message Queues**: Asynchronous processing with queue-based architectures
- **Microservices**: Service decomposition for independent scaling
- **Event-Driven Architecture**: Loose coupling with event streaming
- **API Gateway**: Centralized API management with rate limiting

## Container & Orchestration

### Container Best Practices
- **Minimal Base Images**: Use distroless or alpine images for security
- **Multi-Stage Builds**: Separate build and runtime environments
- **Non-Root Users**: Run containers as non-privileged users
- **Health Checks**: Liveness and readiness probes for all services
- **Resource Limits**: CPU and memory limits to prevent resource exhaustion
- **Image Scanning**: Automated vulnerability scanning in CI/CD pipeline

### Kubernetes Standards
- **Namespace Isolation**: Logical separation of environments and teams
- **Resource Quotas**: Prevent resource monopolization with quotas
- **Network Policies**: Fine-grained network access control
- **Pod Security**: Pod security policies and admission controllers
- **GitOps Workflow**: Declarative configuration with Git as source of truth
- **Service Mesh**: Consider service mesh for complex microservices communication

## Cost Optimization

### FinOps Practices
- **Cost Visibility**: Detailed cost tracking and allocation by service/team
- **Right-Sizing**: Regular review and adjustment of resource allocations
- **Reserved Capacity**: Leverage reserved instances and savings plans
- **Spot Instances**: Use spot/preemptible instances for fault-tolerant workloads
- **Auto-Scaling**: Dynamic scaling to match demand and reduce waste
- **Resource Tagging**: Comprehensive tagging strategy for cost attribution

### Waste Reduction
- **Idle Resource Detection**: Identify and eliminate unused resources
- **Storage Optimization**: Lifecycle policies and data archival strategies
- **Network Costs**: Optimize data transfer and inter-region traffic
- **Development Environments**: Automated shutdown of non-production resources
- **Cost Alerts**: Proactive alerting on budget thresholds and anomalies
- **Regular Audits**: Quarterly cost optimization reviews

## Compliance & Governance

### Security Compliance
- **Audit Logging**: Comprehensive audit trails for all infrastructure changes
- **Access Control**: Role-based access control with regular access reviews
- **Compliance Frameworks**: SOC2, PCI DSS, HIPAA, GDPR compliance as required
- **Security Scanning**: Regular vulnerability assessments and penetration testing
- **Patch Management**: Automated patching with testing and rollback procedures
- **Incident Response Plan**: Documented security incident response procedures

### Operational Governance
- **Change Management**: Formal change approval process for production
- **Documentation Standards**: Up-to-date architecture and operational documentation
- **Disaster Recovery Testing**: Regular DR drills and validation
- **Capacity Reviews**: Quarterly capacity planning and forecasting
- **Performance Reviews**: Regular SLO reviews and adjustments
- **Knowledge Sharing**: Regular knowledge transfer and training sessions

## Team Collaboration

### Communication Standards
- **Documentation First**: Document decisions and architecture in writing
- **Async Communication**: Respect time zones with async-first communication
- **Status Updates**: Regular status updates on ongoing work and incidents
- **Knowledge Base**: Centralized wiki for runbooks and procedures
- **Code Reviews**: Mandatory peer review for all infrastructure changes
- **Retrospectives**: Regular team retrospectives for continuous improvement

### Skill Development
- **Cross-Training**: Ensure knowledge distribution across team members
- **Certification Support**: Support for relevant cloud and DevOps certifications
- **Innovation Time**: Dedicated time for learning and experimentation
- **Conference Attendance**: Support for attending industry conferences
- **Internal Training**: Regular internal training sessions and workshops
- **Mentorship Program**: Structured mentorship for junior team members

## Related Steering Files

For specialized infrastructure topics, refer to these detailed steering files:

- **infrastructure-cloud-architect.md**: Cloud architecture design, multi-cloud strategies, Terraform IaC
- **infrastructure-deployment-engineer.md**: CI/CD pipelines, container orchestration, deployment automation
- **infrastructure-incident-responder.md**: Incident command, crisis management, blameless post-mortems
- **infrastructure-devops-incident-responder.md**: DevOps-specific incident response, observability tools
- **infrastructure-performance-engineer.md**: Performance strategy, optimization techniques, capacity planning

## Success Metrics

Track these key metrics to measure infrastructure effectiveness:

- **Deployment Frequency**: How often code is deployed to production
- **Lead Time for Changes**: Time from commit to production deployment
- **Mean Time to Recovery (MTTR)**: Average time to recover from incidents
- **Change Failure Rate**: Percentage of deployments causing incidents
- **System Availability**: Uptime percentage against SLO targets
- **Performance Metrics**: Response times, throughput, error rates
- **Cost Efficiency**: Cost per transaction or cost per user
- **Security Posture**: Vulnerability remediation time, security incidents

## Continuous Improvement

Infrastructure and DevOps practices should evolve continuously:

1. **Regular Retrospectives**: Learn from both successes and failures
2. **Metric-Driven Decisions**: Use data to guide improvement efforts
3. **Automation First**: Continuously automate repetitive tasks
4. **Stay Current**: Keep up with industry trends and emerging technologies
5. **Experiment Safely**: Use non-production environments for experimentation
6. **Share Knowledge**: Document and share learnings across the organization
7. **Measure Impact**: Track the impact of improvements on key metrics
8. **Iterate Quickly**: Make small, incremental improvements frequently

---

**Remember**: Infrastructure is not just about technology—it's about enabling teams to deliver value quickly, safely, and reliably. Every infrastructure decision should support the broader business objectives while maintaining security, reliability, and cost-effectiveness.
