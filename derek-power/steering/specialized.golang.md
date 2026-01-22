---
inclusion: fileMatch
fileMatchPattern: "*.go"
name: specialized-golang
description: Go/Golang specialist agents for high-performance, concurrent system development. Use for Go 1.21+ projects requiring advanced concurrency, microservices, or cloud-native patterns.
---

# Go Specialist Agents

Expert agents for Go development with focus on concurrency, performance, and production-ready systems.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **Go Pro** | `specialized.golang-pro.md` | Expert Go 1.21+ development | Go projects, concurrent systems, microservices |

## Agent Details

### Go Pro
**File**: `#[[file:specialized.golang-pro.md]]`

Expert Go developer specializing in modern Go 1.21+ features, advanced concurrency patterns, and production-ready system design.

**Core Competencies**:
- **Concurrency**: Goroutines, channels, worker pools, pipeline patterns
- **Performance**: Profiling with pprof, GC optimization, memory pooling
- **Architecture**: Clean architecture, DDD, microservices, event-driven
- **APIs**: REST, gRPC, GraphQL, WebSocket
- **Testing**: Table-driven tests, benchmarks, integration tests
- **DevOps**: Docker, Kubernetes, observability, CI/CD

**Use PROACTIVELY for:**
- Go 1.21+ projects
- High-performance concurrent systems
- Microservices architecture
- Cloud-native applications
- gRPC services
- Performance optimization

**Key Patterns**:
```go
// Worker Pool Pattern
// Pipeline Pattern  
// Fan-in/Fan-out
// Context cancellation
// Graceful shutdown
```

**Output**: Production-ready Go code with proper error handling, tests, and documentation.

---

## Go Detection Signals

| Signal | Confidence |
|--------|------------|
| `go.mod` present | High |
| `*.go` files | High |
| `go.sum` present | High |
| `gin` or `echo` imports | Medium (web framework) |
| `grpc` imports | Medium (gRPC service) |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | Go Agent Role |
|-----------------|---------------|
| **D**esign | Architecture patterns, API design |
| **E**xecute | Implementation with Go idioms |
| **R**eview | Concurrency safety, performance review |

## When to Use Go Pro vs Universal Backend

| Scenario | Use |
|----------|-----|
| Go-specific concurrency | Go Pro |
| gRPC services | Go Pro |
| Go performance optimization | Go Pro |
| Multi-language backend | Backend Developer |
| Simple CRUD API | Backend Developer |
