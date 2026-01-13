---
inclusion: manual
name: derek-init
description: Initialize or reinitialize D.E.R.E.K project memory system. Creates persistent markdown files for planning, progress tracking, and knowledge storage. Use "init" for new projects, "reinit" to refresh project overview while preserving accumulated knowledge.
category: initialization
---

# D.E.R.E.K Initialization

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

## Purpose

Initialize a comprehensive project overview and working memory system. This creates persistent markdown files that serve as your "memory on disk" - enabling context retention across sessions, structured planning, and knowledge accumulation.

**Commands:**
- `init` - Full initialization for new/unfamiliar projects
- `reinit` - Refresh PROJECT.md while preserving decisions, knowledge, and progress

**Use `init` when:**
- Starting work on a new or unfamiliar project
- Beginning a complex multi-step task
- Onboarding to a codebase you haven't worked with before
- Need to establish project context for long-running work

**Use `reinit` when:**
- Project structure has changed significantly
- Dependencies were added or upgraded
- Returning after a long break
- PROJECT.md feels outdated

---

## Memory System Architecture

```
.kiro/
├── resources/                    # Persistent Memory Storage (Global)
│   ├── PROJECT.md               # 🏗️ Project DNA - Architecture, stack, conventions
│   ├── PROGRESS.md              # 📊 Task Tracker - Current work, phases, blockers
│   ├── DECISIONS.md             # ⚖️ Decision Log - Choices made with rationale
│   ├── KNOWLEDGE.md             # 🧠 Knowledge Base - Finalized patterns & learnings
│   └── SCRATCHPAD.md            # 📝 Working Notes - Temporary session context
│
├── features/                     # Feature Planning (Per-Feature)
│   └── <feature-name>/
│       ├── requirements.md      # 📋 What to build (needs approval)
│       ├── design.md            # 🎨 How to build (needs approval)
│       ├── tasks.md             # ✅ Implementation tracking
│       └── notes.md             # 📝 Temporary knowledge during implementation
│
└── views/                        # Generated Outputs
    └── project-memory-*.html    # 🌐 Shareable HTML views
```

### File Purposes

| File | Location | Read Frequency | Update Frequency | Purpose |
|------|----------|----------------|------------------|---------|
| `PROJECT.md` | resources/ | Every session start | On reinit only | Understand project structure |
| `PROGRESS.md` | resources/ | Every task start | Every phase change | Track current work |
| `DECISIONS.md` | resources/ | When making choices | After key decisions | Maintain consistency |
| `KNOWLEDGE.md` | resources/ | When facing issues | After feature completion | Finalized learnings |
| `SCRATCHPAD.md` | resources/ | During session | Continuously | Working memory |
| `notes.md` | features/*/ | During implementation | Continuously | Temporary feature knowledge |

### D.E.R.E.K Workflow Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           D.E.R.E.K WORKFLOW                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐  │
│  │  DESIGN  │──▶│ EVALUATE │──▶│  REVIEW  │──▶│ EXECUTE  │──▶│KNOWLEDGE │  │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘  │
│       │              │              │              │              │         │
│       ▼              ▼              ▼              ▼              ▼         │
│  requirements   analysis.md    Approval      tasks.md      KNOWLEDGE.md    │
│  design.md      planning.md    Gates         notes.md      (finalized)     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Initialization Workflow

### Step 1: Create Directory Structure

```bash
mkdir -p .kiro/resources
mkdir -p .kiro/views
```

### Step 2: Deep Project Analysis

Perform comprehensive analysis before generating files:

#### 2.1 Technology Stack Detection

```
📦 Package Files to Scan:
├── Gemfile / Gemfile.lock      → Ruby/Rails dependencies
├── package.json                 → Node.js dependencies
├── go.mod                       → Go modules
├── requirements.txt / Pipfile   → Python dependencies
├── pom.xml / build.gradle       → Java dependencies
├── Cargo.toml                   → Rust dependencies
└── composer.json                → PHP dependencies
```

#### 2.2 Architecture Pattern Recognition

| Pattern | Indicators | Confidence |
|---------|------------|------------|
| **MVC** | `app/models`, `app/views`, `app/controllers` | High |
| **Service Objects** | `app/services/`, `*_service.rb` | High |
| **API-First** | `app/api/`, Grape/GraphQL gems | High |
| **Microservices** | Multiple `Dockerfile`, service directories | Medium |
| **Event-Driven** | Kafka consumers, Sidekiq jobs | Medium |
| **Domain-Driven** | Domain folders, bounded contexts | Medium |

#### 2.3 Code Organization Analysis

```
📁 Directory Purposes:
├── app/                    → Application code
│   ├── api/               → API endpoints (Grape, GraphQL)
│   ├── controllers/       → Request handlers
│   ├── models/            → Data models & business logic
│   ├── services/          → Business logic services
│   ├── jobs/              → Background jobs
│   ├── consumers/         → Message consumers
│   └── mailers/           → Email templates
├── config/                 → Configuration files
├── db/                     → Database migrations & seeds
├── lib/                    → Shared libraries
├── spec/ or test/          → Test files
└── scripts/                → Utility scripts
```

#### 2.4 External Dependencies Mapping

```
🔗 Integration Points:
├── Database          → PostgreSQL, MySQL, MongoDB, Redis
├── Search            → Elasticsearch, Algolia
├── Queue             → Sidekiq, Kafka, RabbitMQ
├── Storage           → S3, GCS, local
├── Auth              → Devise, JWT, OAuth
├── Payments          → Stripe, PayPal
├── Notifications     → Twilio, Firebase, SendGrid
└── Monitoring        → Skylight, NewRelic, DataDog
```

---

### Step 3: Generate PROJECT.md

Create comprehensive project overview:

```markdown
# Project Overview

## 🎯 Quick Summary

**Project Name**: [Name from package/config]
**Description**: [What this project does in 2-3 sentences]
**Domain**: [Business domain - e-commerce, logistics, fintech, etc.]
**Status**: [Active development / Maintenance / Legacy]

## 🏗️ Technology Stack

### Core Technologies
| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| Language | Ruby | 2.5.3 | Primary language |
| Framework | Rails | 4.2.x | Web framework |
| Database | PostgreSQL | 12.x | Primary data store |
| Cache | Redis | 6.x | Caching & sessions |
| Search | Elasticsearch | 7.x | Full-text search |

### Key Dependencies
| Gem/Package | Version | Purpose |
|-------------|---------|---------|
| devise | x.x | Authentication |
| sidekiq | x.x | Background jobs |
| grape | x.x | REST API framework |
| paperclip | x.x | File uploads |

### Infrastructure
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud Provider**: AWS
- **CI/CD**: Bitbucket Pipelines

## 📐 Architecture Overview

### Pattern
[MVC with Service Objects / Microservices / Monolith / etc.]

### High-Level Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                        Load Balancer                         │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │   Web    │   │   API    │   │  Admin   │
        │  Server  │   │  Server  │   │  Panel   │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                    ┌──────────────────┐
                    │   Application    │
                    │     Layer        │
                    └────────┬─────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  ┌──────────┐         ┌──────────┐         ┌──────────┐
  │PostgreSQL│         │  Redis   │         │Elasticsearch│
  └──────────┘         └──────────┘         └──────────┘
```

### Directory Structure
```
app/
├── api/                    # Grape API endpoints
│   ├── v3/                # API version 3
│   ├── v4/                # API version 4 (current)
│   └── entities/          # Response serializers
├── models/                 # ActiveRecord models
│   └── concerns/          # Shared model behaviors
├── services/              # Business logic
│   ├── bookings/          # Booking domain services
│   ├── payments/          # Payment domain services
│   └── notifications/     # Notification services
├── jobs/                  # Sidekiq background jobs
├── consumers/             # Kafka message consumers
├── controllers/           # Rails controllers
│   ├── admin/             # Admin panel
│   └── business/          # Business portal
└── mailers/               # Email templates
```

## 🔑 Key Components

### Domain Models
| Model | Purpose | Key Relationships |
|-------|---------|-------------------|
| `User` | User accounts | has_many :bookings |
| `Booking` | Delivery orders | belongs_to :user, :driver |
| `Driver` | Delivery drivers | has_many :bookings |
| `Vehicle` | Driver vehicles | belongs_to :driver |

### Service Objects
| Service | Purpose | Location |
|---------|---------|----------|
| `BookingCreator` | Create new bookings | `app/services/bookings/` |
| `PriceCalculator` | Calculate delivery prices | `app/services/pricing/` |
| `DriverMatcher` | Match drivers to bookings | `app/services/matching/` |

### API Endpoints
| Endpoint | Version | Purpose |
|----------|---------|---------|
| `/api/v4/bookings` | v4 | Booking management |
| `/api/v4/drivers` | v4 | Driver operations |
| `/api/v4/vehicles` | v4 | Vehicle management |

### Background Jobs
| Job | Queue | Purpose |
|-----|-------|---------|
| `NotificationJob` | default | Send notifications |
| `MatchingJob` | critical | Driver matching |
| `ReportJob` | low | Generate reports |

## 🚀 Entry Points

### Application Entry
| Entry Point | Path | Purpose |
|-------------|------|---------|
| Rails App | `config/application.rb` | Main application config |
| Routes | `config/routes.rb` | URL routing |
| API Mount | `config/routes.rb` → `API::Root` | API entry point |

### Configuration
| Config | Path | Purpose |
|--------|------|---------|
| Database | `config/database.yml` | DB connection |
| Environment | `.env`, `.env.development` | Environment variables |
| Sidekiq | `config/sidekiq.yml` | Background job config |
| Redis | `config/initializers/redis.rb` | Redis connection |

## 💻 Development Commands

### Setup
```bash
# Install Ruby dependencies
bundle install

# Install Node dependencies
npm install

# Setup database
rake db:create db:migrate db:seed

# Start development server
rails server

# Start background workers
bundle exec sidekiq -C config/sidekiq.yml
```

### Testing
```bash
# Run all tests
bundle exec rspec

# Run specific test
bundle exec rspec spec/models/booking_spec.rb

# Run with coverage
COVERAGE=true bundle exec rspec
```

### Code Quality
```bash
# Ruby linting
bundle exec rubocop -a

# Security scan
bundle exec brakeman

# Code smell detection
bundle exec reek
```

## 📏 Code Conventions

### Naming Conventions
| Type | Convention | Example |
|------|------------|---------|
| Models | Singular, PascalCase | `Booking`, `UserProfile` |
| Controllers | Plural, PascalCase | `BookingsController` |
| Services | Action + Object | `BookingCreator`, `PriceCalculator` |
| Jobs | Noun + Job | `NotificationJob`, `CleanupJob` |

### File Organization
- **Model concerns**: `app/models/concerns/<model_name>/`
- **Service objects**: `app/services/<domain>/`
- **API versions**: `app/api/v<version>/`

### Code Patterns
```ruby
# Service Object Pattern
class MyService < ApplicationService
  def call
    # Business logic here
    # Return result or raise error
  end
end

# Usage
MyService.call(params)
```

## 🔗 External Integrations

| Service | Purpose | Config Location |
|---------|---------|-----------------|
| AWS S3 | File storage | `config/initializers/paperclip.rb` |
| Twilio | SMS/Voice | `config/initializers/twilio.rb` |
| Firebase | Push notifications | `config/initializers/firebase.rb` |
| Stripe | Payments | `config/initializers/stripe.rb` |

## ⚠️ Important Notes

### Known Gotchas
1. **Rails 4.2 Syntax**: Use `ActiveRecord::Base`, not `ApplicationRecord`
2. **Strong Params**: Define in controllers, not models
3. **Grape API**: Use `params` directly, not `permitted_params`
4. **PostGIS**: Use `st_distance` for location queries
5. **Multi-locale**: Support en, vi, th, id, tl

### Performance Considerations
- Use `includes` to avoid N+1 queries
- Cache expensive computations in Redis
- Use background jobs for slow operations

### Security Considerations
- Never log sensitive data (passwords, tokens)
- Always validate user input
- Use parameterized queries

---
*Generated: [date]*
*Last Updated: [date]*
```

---

### Step 4: Generate PROGRESS.md

```markdown
# Task Progress

## 📍 Current Focus

**Task**: [None - awaiting task assignment]
**Phase**: Initialization Complete
**Status**: 🟢 Ready for tasks
**Started**: [date]
**Last Updated**: [date]

## 🎯 Goal

[To be defined when task is assigned]

## 📋 Phases

| Phase | Status | Description |
|-------|--------|-------------|
| 1. Analysis | ⏳ Pending | Understand requirements |
| 2. Planning | ⏳ Pending | Design solution |
| 3. Implementation | ⏳ Pending | Write code |
| 4. Testing | ⏳ Pending | Verify solution |
| 5. Review | ⏳ Pending | Quality check |

## ❓ Key Questions

[To be populated during analysis]

## 🚧 Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| None | - | - |

## ❌ Errors Encountered

| Error | Context | Solution |
|-------|---------|----------|
| None | - | - |

## ✅ Completed Tasks

- [x] Project initialization - [date]

## 📌 Next Steps

1. [ ] Review PROJECT.md for accuracy
2. [ ] Assign first task
3. [ ] Begin analysis phase

## 📊 Session Log

### [date] - Initialization
- Created project memory system
- Analyzed project structure
- Generated PROJECT.md

---
*Last Updated: [date]*
```

---

### Step 5: Generate DECISIONS.md

```markdown
# Decision Log

## Purpose

Track key decisions made during development with rationale and context. This ensures consistency and helps future developers understand why choices were made.

## Decision Index

| Date | Decision | Impact | Reversible |
|------|----------|--------|------------|
| [date] | Project Initialization | Foundation | No |

---

## Decisions

### [date] - Project Initialization

**Decision**: Initialized project memory system with 5 core files

**Context**: 
- Starting work on this project
- Need persistent context across sessions
- Want structured approach to development

**Alternatives Considered**:
1. No memory system - rely on conversation context
2. Single file approach - all in one document
3. Full memory system - separate concerns into files

**Rationale**: 
- Separate files allow focused updates
- Reduces context loading time
- Enables selective sharing
- Compatible with manus-plaining workflow

**Impact**: 
- All future work uses this memory system
- Decisions are tracked and searchable
- Knowledge accumulates over time

**Reversible**: No (foundational decision)

---

## Decision Template

```markdown
### [date] - [Decision Title]

**Decision**: [What was decided]

**Context**: 
- [Why this decision was needed]
- [Current situation]
- [Constraints]

**Alternatives Considered**:
1. [Option 1] - [Pros/Cons]
2. [Option 2] - [Pros/Cons]
3. [Option 3] - [Pros/Cons]

**Rationale**: 
- [Why this option was chosen]
- [Key factors in decision]

**Impact**: 
- [What this affects]
- [Dependencies]
- [Future implications]

**Reversible**: [Yes/No/Partially] - [Explanation]
```

---
*Last Updated: [date]*
```

---

### Step 6: Generate KNOWLEDGE.md

```markdown
# Project Knowledge Base

## Purpose

Accumulate learnings, patterns, and insights discovered during development. This prevents repeating mistakes and captures institutional knowledge.

## 📚 Quick Reference

### Common Commands
```bash
# Start development
rails server
bundle exec sidekiq -C config/sidekiq.yml

# Run tests
bundle exec rspec

# Database operations
rake db:migrate
rake db:rollback STEP=1

# Console access
rails console
rails dbconsole
```

### Useful Queries
```ruby
# Find booking with associations
Booking.includes(:user, :driver, :locations).find(id)

# Active drivers in area
Driver.active.within_radius(lat, lng, 5.km)

# Recent bookings
Booking.where('created_at > ?', 1.day.ago).order(created_at: :desc)
```

---

## 🏗️ Architecture Patterns

### Service Object Pattern
```ruby
# Location: app/services/
class BookingCreator < ApplicationService
  def initialize(user:, params:)
    @user = user
    @params = params
  end

  def call
    booking = @user.bookings.build(@params)
    
    if booking.save
      notify_drivers(booking)
      booking
    else
      raise ServiceError, booking.errors.full_messages
    end
  end

  private

  def notify_drivers(booking)
    NotificationJob.perform_async(booking.id)
  end
end

# Usage
BookingCreator.call(user: current_user, params: booking_params)
```

### API Entity Pattern
```ruby
# Location: app/api/entities/
module Entities
  class Booking < Grape::Entity
    expose :id
    expose :status
    expose :created_at
    expose :user, using: Entities::User
    expose :locations, using: Entities::Location
  end
end
```

### Model Concern Pattern
```ruby
# Location: app/models/concerns/bookings/
module Bookings::Validations
  extend ActiveSupport::Concern

  included do
    validates :pickup_location, presence: true
    validates :dropoff_location, presence: true
    validate :valid_locations
  end

  private

  def valid_locations
    # Custom validation logic
  end
end
```

---

## ⚠️ Gotchas & Pitfalls

### Rails 4.2 Specific
| Issue | Wrong | Correct |
|-------|-------|---------|
| Base class | `ApplicationRecord` | `ActiveRecord::Base` |
| Strong params | In model | In controller |
| Enum syntax | `enum status: [:pending]` | `enum status: { pending: 0 }` |

### Database
| Issue | Problem | Solution |
|-------|---------|----------|
| N+1 queries | Lazy loading | Use `includes(:association)` |
| Large result sets | Memory issues | Use `find_each` or `in_batches` |
| Slow queries | Missing indexes | Add database indexes |

### API
| Issue | Problem | Solution |
|-------|---------|----------|
| Grape params | Using `permitted_params` | Use `params` directly |
| Authentication | Missing auth check | Add `before` filter |
| Versioning | Breaking changes | Create new API version |

---

## 🔧 Useful Snippets

### Debugging
```ruby
# Log SQL queries
ActiveRecord::Base.logger = Logger.new(STDOUT)

# Inspect object
pp object.attributes

# Trace method calls
set_trace_func proc { |event, file, line, id, binding, classname|
  printf "%8s %s:%-2d %10s %8s\n", event, file, line, id, classname
}
```

### Performance
```ruby
# Benchmark code
require 'benchmark'
Benchmark.measure { expensive_operation }

# Memory profiling
require 'memory_profiler'
MemoryProfiler.report { code_to_profile }.pretty_print
```

### Testing
```ruby
# Factory usage
let(:booking) { create(:booking, :with_driver) }

# Stub external service
allow(TwilioService).to receive(:send_sms).and_return(true)

# Time travel
travel_to(1.day.from_now) { expect(booking).to be_expired }
```

---

## 📖 Lessons Learned

| Date | Lesson | Context |
|------|--------|---------|
| [date] | Always check for N+1 queries | Performance issue in production |

---

## 🔗 External Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| Rails Guides | https://guides.rubyonrails.org | Framework documentation |
| Grape Wiki | https://github.com/ruby-grape/grape/wiki | API framework docs |
| Project Wiki | [internal URL] | Team documentation |

---
*Last Updated: [date]*
```

---

### Step 7: Generate SCRATCHPAD.md

```markdown
# Scratchpad

## Purpose

Temporary working notes, thoughts, and context for current session. This file is cleared at session end - move important content to appropriate files.

---

## 📅 Current Session

**Started**: [date/time]
**Focus**: Project initialization
**Status**: Active

---

## 📝 Working Notes

[Space for temporary notes during work]

---

## ❓ Questions to Investigate

- [ ] [Question 1]
- [ ] [Question 2]

---

## 🔍 Temporary Context

[Space for context that doesn't need permanent storage]

---

## 📋 Quick TODO

- [ ] [Task 1]
- [ ] [Task 2]

---

## 🗑️ Session Cleanup Checklist

Before ending session:
- [ ] Move important notes to KNOWLEDGE.md
- [ ] Update PROGRESS.md with status
- [ ] Log any decisions in DECISIONS.md
- [ ] Clear this scratchpad

---
*This file is for temporary notes. Move important content to appropriate files before session end.*
```

---

## Initialization Checklist

When running `init`, complete these steps:

- [ ] Create `.kiro/resources/` directory
- [ ] Create `.kiro/features/` directory
- [ ] Create `.kiro/views/` directory
- [ ] Scan project structure thoroughly
- [ ] Detect technology stack with versions
- [ ] Map architecture patterns
- [ ] Identify key components and relationships
- [ ] Generate `PROJECT.md` with comprehensive overview
- [ ] Initialize `PROGRESS.md` for task tracking
- [ ] Initialize `DECISIONS.md` with first decision
- [ ] Initialize `KNOWLEDGE.md` with patterns
- [ ] Initialize `SCRATCHPAD.md` for working notes
- [ ] Verify all files are accurate
- [ ] Report initialization summary with D.E.R.E.K branding

---

## Example Init Output

```
✅ D.E.R.E.K Memory System Initialized

📁 Created .kiro/resources/
   ├── PROJECT.md    - 🏗️ Project DNA (comprehensive overview)
   ├── PROGRESS.md   - 📊 Task Tracker (ready for tasks)
   ├── DECISIONS.md  - ⚖️ Decision Log (1 decision logged)
   ├── KNOWLEDGE.md  - 🧠 Knowledge Base (patterns documented)
   └── SCRATCHPAD.md - 📝 Working Notes (empty)

� Created .kiro/features/ (ready for feature planning)

�📊 Project Analysis:
   • Name: Deliveree Backend
   • Stack: Ruby 2.5.3 / Rails 4.2.x / PostgreSQL / Redis
   • Architecture: Monolithic MVC with Service Objects
   • API: Grape REST API (v3, v4)
   • Background: Sidekiq + Kafka consumers
   • Key Models: User, Booking, Driver, Vehicle
   • Test Framework: RSpec

🔑 Key Findings:
   • 4 API versions detected (v1-v4, v4 is current)
   • 15+ service objects in app/services/
   • Multi-country support (en, vi, th, id, tl)
   • PostGIS for geolocation queries

⚠️ Important Notes:
   • Rails 4.2 syntax (no ApplicationRecord)
   • Strong params in controllers only
   • Use st_distance for location queries

🚀 D.E.R.E.K Ready!
   • For simple tasks: Update PROGRESS.md directly
   • For complex features: Say "create feature <name>"
   • For analysis: Load analysis.md steering file

What would you like to work on?
```

---

## Reinit Command

When user says "reinit":

### What Gets Updated
- ✅ `PROJECT.md` - Regenerated with fresh analysis
- 🧹 `SCRATCHPAD.md` - Cleared

### What Gets Preserved
- 📌 `PROGRESS.md` - Current task context intact
- 📌 `DECISIONS.md` - All decisions retained
- 📌 `KNOWLEDGE.md` - All learnings retained

### Example Reinit Output

```
🔄 D.E.R.E.K Memory Refreshed

📁 Updated .kiro/resources/
   ├── PROJECT.md    - ✅ Regenerated
   ├── PROGRESS.md   - 📌 Preserved (current task intact)
   ├── DECISIONS.md  - 📌 Preserved (12 decisions)
   ├── KNOWLEDGE.md  - 📌 Preserved (8 patterns)
   └── SCRATCHPAD.md - 🧹 Cleared

� Preserved .kiro/features/
   ├── authentication/  - 📌 Preserved (in progress)
   └── payment-integration/ - 📌 Preserved (complete)

📊 Changes Detected:
   • New gem: stripe (payments integration)
   • New directory: app/services/payments/
   • New model: PaymentTransaction
   • Updated: sidekiq 6.0 → 7.0

📝 PROJECT.md updated with latest project state.
```

---

## Post-Initialization Workflow

### Daily Workflow (D.E.R.E.K Loop)
```
1. Start Session
   └── Read PROGRESS.md → Current status
   └── Read PROJECT.md → Refresh context
   └── Check features/*/ → Active feature status

2. During Work
   └── Update SCRATCHPAD.md → Working notes
   └── Update PROGRESS.md → Phase changes
   └── Update features/*/notes.md → Feature-specific findings

3. After Decisions
   └── Update DECISIONS.md → Log with rationale

4. When Learning
   └── Update features/*/notes.md → Temporary (during feature)
   └── Update KNOWLEDGE.md → Finalized (after feature complete)

5. End Session
   └── Update PROGRESS.md → Final status
   └── Clear SCRATCHPAD.md → Move important notes
```

### Quick Planning vs Feature Planning

| Scenario | Use | Location |
|----------|-----|----------|
| Bug fix | Quick Planning | PROGRESS.md |
| Config change | Quick Planning | PROGRESS.md |
| New feature | Feature Planning | features/<name>/ |
| Multi-file change | Feature Planning | features/<name>/ |
| Auth/Security work | Feature Planning | features/<name>/ |

### Integration with D.E.R.E.K Steering Files

| Steering File | Phase | Uses Memory Files |
|---------------|-------|-------------------|
| `analysis.md` | **E**valuate | Reads PROJECT.md, writes to SCRATCHPAD.md |
| `planning.md` | **D**esign | Reads PROJECT.md, creates features/*/, writes to PROGRESS.md |
| `review.md` | **R**eview | Reads all, writes to KNOWLEDGE.md |
| `context.md` | All | Uses PROGRESS.md, KNOWLEDGE.md for context retention |

### Feature Planning Integration

When creating a new feature, the memory system expands:

```
init (creates global memory)
  │
  ▼
"create feature authentication"
  │
  ▼
.kiro/features/authentication/
├── requirements.md  ◄── DESIGN phase
├── design.md        ◄── DESIGN phase (after approval)
├── tasks.md         ◄── EXECUTE phase (after approval)
└── notes.md         ◄── EXECUTE phase (temporary knowledge)
                           │
                           ▼ (on completion)
                     KNOWLEDGE.md (finalized learnings)
```

---

## Remember

**Initialization is the foundation for D.E.R.E.K workflow.**

A well-initialized project memory:
- ✅ Provides instant context for any session
- ✅ Prevents repeated discovery of same information
- ✅ Enables consistent decision-making
- ✅ Accumulates knowledge over time
- ✅ Supports effective handoffs between sessions
- ✅ Can be shared with team via memory-sharing system
- ✅ Integrates with feature planning workflow

**D.E.R.E.K Memory Flow:**
```
PROJECT.md ──► Context for all work
PROGRESS.md ──► Links to active features
features/*/notes.md ──► Temporary knowledge during implementation
KNOWLEDGE.md ◄── Finalized learnings after feature completion
DECISIONS.md ◄── Key decisions with rationale
```

**Always `init` before starting significant work on an unfamiliar project.**
