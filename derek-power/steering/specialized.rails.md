---
inclusion: manual
name: specialized-rails
description: Ruby on Rails specialist agents for full-stack web development, API development, and database optimization. Use for Rails projects requiring framework-specific expertise.
---

# Rails Specialist Agents

Expert agents for Ruby on Rails development across web applications, APIs, and database optimization.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **Rails Backend Expert** | `specialized.rails-backend-expert.md` | Full-stack Rails development | Rails apps, MVC patterns |
| **Rails API Developer** | `specialized.rails-api-developer.md` | Rails API development | REST APIs, JSON:API, GraphQL |
| **Rails ActiveRecord Expert** | `specialized.rails-activerecord-expert.md` | Database & ORM optimization | Models, queries, migrations |

## Agent Selection Guide

### By Task Type

| Task | Recommended Agent |
|------|-------------------|
| Full Rails application | Rails Backend Expert |
| API-only Rails app | Rails API Developer |
| Database optimization | Rails ActiveRecord Expert |
| Complex queries | Rails ActiveRecord Expert |
| Authentication/Authorization | Rails Backend Expert |
| API versioning | Rails API Developer |

### Detection Signals

| Signal | Confidence | Agent |
|--------|------------|-------|
| `Gemfile` with `rails` | High | Rails Backend Expert |
| `config/routes.rb` with API namespace | High | Rails API Developer |
| Complex `app/models/` | Medium | Rails ActiveRecord Expert |
| `rails-api` or `grape` gems | High | Rails API Developer |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | Rails Agent Role |
|-----------------|------------------|
| **D**esign | Architecture, models, API design |
| **E**valuate | Requirements, database schema |
| **E**xecute | Implementation with Rails conventions |
| **R**eview | Code review, N+1 detection, security |
| **K**nowledge | Rails patterns, gems, best practices |

## Common Commands

```bash
# Development
rails server
rails console
rails generate model/controller/migration
rails db:migrate
rails routes

# Testing
bundle exec rspec
rails test

# Production
rails assets:precompile
RAILS_ENV=production rails db:migrate
```
