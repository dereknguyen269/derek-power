---
inclusion: manual
---

# D.E.R.E.K Memory Sharing System

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

**MUST BE USED**: When user wants to share project memory, create shareable links, or set up collaborative access to project context.

## Purpose

Enable sharing of D.E.R.E.K Memory System (`.kiro/resources/` and `.kiro/specs/`) via secure, time-limited links with a clean web UI for stakeholders, team members, or external collaborators. This system generates the necessary tools dynamically in `.kiro/views/` to comply with power validation rules.

## Activation Keywords

- "share project memory", "create share link", "share context"
- "generate project link", "export project memory", "share project overview"
- "create shareable report", "team access link", "stakeholder view"
- "serve memory", "start memory server", "memory html"
- "share derek", "derek report", "export derek"
- "share feature [name]", "export feature [name]", "feature report [name]"

## What Gets Shared

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      D.E.R.E.K SHAREABLE CONTENT                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Global Memory (.kiro/resources/)                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  PROJECT.md  │  │ PROGRESS.md  │  │ DECISIONS.md │  │ KNOWLEDGE.md │    │
│  │  ✅ Shared   │  │  ✅ Shared   │  │  ✅ Shared   │  │  ✅ Shared   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  Feature Memory (.kiro/specs/*/)                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │requirements  │  │  design.md   │  │  tasks.md    │  │  notes.md    │    │
│  │  ✅ Shared   │  │  ✅ Shared   │  │  ✅ Shared   │  │  ✅ Shared   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  Excluded:                                                                   │
│  ❌ SCRATCHPAD.md (temporary session notes)                                 │
│  ❌ Sensitive data (auto-redacted)                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Activation Keywords

- "share project memory", "create share link", "share context"
- "generate project link", "export project memory", "share project overview"
- "create shareable report", "team access link", "stakeholder view"
- "serve memory", "start memory server", "memory html"

## MCP Integration

This system uses the **derek-memory MCP server** to provide memory sharing capabilities through the Model Context Protocol. The MCP server is already configured in `mcp.json` and provides tools for generating and serving shareable HTML from D.E.R.E.K memory.

### MCP Server Configuration

The derek-memory MCP is configured in `mcp.json`:

```json
{
  "mcpServers": {
    "derek-memory": {
      "command": "npx",
      "args": ["-y", "derek-memory-mcp"]
    }
  }
}
```

### Available MCP Tools

The derek-memory MCP provides the following tools:

1. **`share_feature_memory`** - Generate beautiful HTML documentation
   - Reads `.kiro/resources/*.md` (global memory)
   - Reads `.kiro/specs/*/*.md` (feature memory)
   - Sanitizes sensitive information
   - Supports feature filtering
   - Creates beautiful D.E.R.E.K branded HTML

2. **`serve_html`** - Start HTTP server to view HTML in browser
   - Auto-detects generated HTML files
   - Provides local and network URLs
   - Supports custom ports

## Implementation Process

When this steering file is activated:

1. **Verify MCP Configuration**: Ensure `derek-memory` is configured in `mcp.json`
2. **Use MCP Tools**: Call `share_feature_memory` to generate the report
3. **Serve Content**: Call `serve_html` to make it accessible
4. **Share URLs**: Provide shareable URLs to stakeholders

## Usage Workflow

### Quick Share (All Memory)
Use `share_feature_memory` to create HTML, then `serve_html` to start the server:

```
Agent uses: share_feature_memory(output_filename="derek-memory.html")
Agent uses: serve_html(html_file="derek-memory.html", port=8080)
```

### Share Specific Feature Only
Use the tool with feature filter:

```
Agent uses: share_feature_memory(feature_name="driver-position-rate-limiting", output_filename="feature-report.html")
Agent uses: serve_html(html_file="feature-report.html")
```

## Usage Examples

### Quick Share (All Memory)
When user requests to share all project memory:
1. Agent calls `share_feature_memory()` via MCP
2. Agent calls `serve_html()` via MCP
3. Agent provides URLs to user

### Share Specific Feature Only
When user requests to share a specific feature:
1. Agent calls `share_feature_memory(feature_name="feature-name")` via MCP
2. Agent calls `serve_html()` via MCP
3. Agent provides URLs to user

### Share Multiple Features
When user requests to share multiple features:
1. Agent calls `share_feature_memory(feature_name="authentication", output_filename="auth.html")` via MCP
2. Agent calls `share_feature_memory(feature_name="payment-integration", output_filename="payment.html")` via MCP
3. Agent calls `serve_html()` via MCP (serves directory or latest file)
4. All generated files will be accessible via the server

### Custom Port
When user requests a specific port:
1. Agent calls `share_feature_memory()` via MCP
2. Agent calls `serve_html(port=8081)` via MCP

### Team Sharing
When user wants to share with team:
1. Agent calls `share_feature_memory()` via MCP
2. Agent calls `serve_html(port=8080)` via MCP
3. Agent provides both local and network URLs
4. Team members can access from any device on the network

### Stakeholder Reports
When user wants to create a report for stakeholders:
1. Agent calls `share_feature_memory()` via MCP
2. Agent informs user of the generated HTML file location
3. User can upload to web hosting or email directly

### Feature-Specific Client Updates
When user wants to share feature progress with client:
1. Agent calls `share_feature_memory(feature_name="new-api-endpoint")` via MCP
2. Agent provides the HTML file path
3. Client sees only that feature's requirements, design, tasks, and notes

## Security Features

- **Automatic Sanitization**: Removes API keys, passwords, tokens
- **Local-First**: Files stay in your `.kiro/views/` directory
- **No External Dependencies**: Pure Python and HTML
- **Read-Only**: Generated content is static snapshot
- **Time-Stamped**: Each generation creates timestamped file

## Integration with D.E.R.E.K Memory System

This system works seamlessly with:
- `derek-init.md` - Project initialization (creates `.kiro/resources/`)
- `planning.md` - Feature planning (creates `.kiro/specs/*/`)
- `context.md` - Context retention
- All existing `.kiro/resources/` files (global memory)
- All existing `.kiro/specs/*/` files (feature memory)

### D.E.R.E.K Memory Flow for Sharing

```
┌─────────────────────────────────────────────────────────────────┐
│                    D.E.R.E.K SHARING FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  .kiro/resources/          .kiro/specs/*/                    │
│  ┌──────────────┐          ┌──────────────┐                     │
│  │ PROJECT.md   │          │requirements  │                     │
│  │ PROGRESS.md  │          │ design.md    │                     │
│  │ DECISIONS.md │          │ tasks.md     │                     │
│  │ KNOWLEDGE.md │          │ notes.md     │                     │
│  └──────┬───────┘          └──────┬───────┘                     │
│         │                         │                              │
│         └────────────┬────────────┘                              │
│                      ▼                                           │
│              ┌──────────────┐                                    │
│              │   Generator  │  (sanitize + convert)              │
│              └──────┬───────┘                                    │
│                     ▼                                            │
│              ┌──────────────┐                                    │
│              │ derek-memory │                                    │
│              │  -YYYYMMDD   │                                    │
│              │    .html     │                                    │
│              └──────┬───────┘                                    │
│                     ▼                                            │
│              ┌──────────────┐                                    │
│              │   Server     │  (HTTP serve)                      │
│              └──────┬───────┘                                    │
│                     ▼                                            │
│         ┌──────────────────────┐                                │
│         │  Shareable URLs      │                                │
│         │  • localhost:8080    │                                │
│         │  • 192.168.x.x:8080  │                                │
│         └──────────────────────┘                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Benefits

### Full Project Sharing
- **Stakeholder Communication**: Professional D.E.R.E.K project overviews
- **Team Collaboration**: Easy context sharing with feature progress
- **Client Updates**: Clean, branded project status with feature tracking
- **Documentation**: Persistent knowledge base with feature history
- **Onboarding**: Quick context for new team members
- **Feature Visibility**: Share feature requirements, design, and progress
- **Compliance**: Powers validation friendly (no binary files in power)

### Feature-Specific Sharing
- **Focused Communication**: Share only relevant feature details with specific stakeholders
- **Client Confidentiality**: Exclude other features and global project details
- **Contractor Scope**: Provide contractors with only their assigned feature context
- **Feature Reviews**: Send feature-specific reports for approval or feedback
- **Reduced Noise**: Recipients see only what they need, not entire project
- **Selective Disclosure**: Control what information is shared with external parties
- **Lightweight Files**: Smaller HTML files for faster loading and easier distribution

## Output Format

### Full Project Memory Share
When agent shares complete project memory via MCP:
```
✅ D.E.R.E.K Memory Shared Successfully

📋 Share Details:
   📁 File: .kiro/views/derek-memory-20240107-141136.html
   🌐 Local URL: http://localhost:8080
   📱 Network URL: http://192.168.1.100:8080
   📊 Content: 
      • Global Memory: 4 files (PROJECT, PROGRESS, DECISIONS, KNOWLEDGE)
      • Feature Memory: 2 features (authentication, payment-integration)

🔗 Quick Actions:
   • Share network URL with team
   • Upload HTML file to web hosting
   • Generate QR code for mobile access

⚠️  Security Note:
   • Sensitive information has been automatically redacted
   • SCRATCHPAD.md excluded (temporary session notes)
   • Files are stored locally in .kiro/views/
```

### Feature-Specific Share
When agent shares a single feature via MCP:
```
✅ D.E.R.E.K Feature Memory Shared Successfully

📋 Share Details:
   🎯 Feature: driver-position-rate-limiting
   📁 File: .kiro/views/derek-feature-driver-position-rate-limiting-20240107-141136.html
   🌐 Local URL: http://localhost:8080
   📱 Network URL: http://192.168.1.100:8080
   📊 Content: 
      • Feature Memory: 4 files (requirements.md, design.md, tasks.md, notes.md)
      • Global Memory: Excluded (feature-only view)

🔗 Quick Actions:
   • Share network URL with feature stakeholders
   • Upload HTML file for client review
   • Email file directly to specific team members

⚠️  Security Note:
   • Sensitive information has been automatically redacted
   • Only this feature's files are included
   • Files are stored locally in .kiro/views/
```

## MCP Tool Details

The derek-memory MCP server provides these tools that the agent can use:

### `share_feature_memory`
**Purpose**: Generate beautiful HTML documentation from D.E.R.E.K memory

**Parameters**:
- `feature_name` (optional): Filter to specific feature name (e.g., "auth-system"). If omitted, includes all features.
- `output_filename` (optional): Name of output HTML file (default: auto-generated timestamp)

**Returns**:
- `file_path`: Path to generated HTML file
- `message`: Success message with content summary

### `serve_html`
**Purpose**: Start HTTP server to view HTML in browser

**Parameters**:
- `html_file` (optional): Specific HTML file to serve. If omitted, serves the most recent HTML file in `.kiro/views/`.
- `port` (optional): Server port (default: 8080)

**Returns**:
- `local_url`: Local access URL
- `network_url`: Network access URL for sharing
- `status`: Server running status

This approach ensures the D.E.R.E.K Memory Sharing System works seamlessly with the MCP infrastructure, eliminating the need for manual Python script generation.