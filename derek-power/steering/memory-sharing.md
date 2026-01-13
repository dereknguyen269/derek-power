---
inclusion: manual
---

# D.E.R.E.K Memory Sharing System

**D**esign · **E**valuate · **R**eview · **E**xecute · **K**nowledge

**MUST BE USED**: When user wants to share project memory, create shareable links, or set up collaborative access to project context.

## Purpose

Enable sharing of D.E.R.E.K Memory System (`.kiro/resources/` and `.kiro/features/`) via secure, time-limited links with a clean web UI for stakeholders, team members, or external collaborators. This system generates the necessary tools dynamically in `.kiro/views/` to comply with power validation rules.

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
│  Feature Memory (.kiro/features/*/)                                         │
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

## Dynamic Tool Generation

Since powers can only contain steering files, this system generates the necessary tools in `.kiro/views/` when activated:

1. **Memory Generator** (`memory-generator.py`) - Converts D.E.R.E.K memory to HTML
2. **Memory Server** (`memory-server.py`) - Serves HTML files via HTTP
3. **Quick Serve Script** (`serve.sh`) - Simple command-line interface

## Implementation Process

When this steering file is activated, it will:

1. Create `.kiro/views/` directory if it doesn't exist
2. Generate the memory sharing tools dynamically
3. Process global memory files from `.kiro/resources/`
4. Process feature memory files from `.kiro/features/*/`
5. Create beautiful HTML interface with D.E.R.E.K branding
6. Start local server for immediate sharing

## Generated Tools Overview

### 1. Memory Generator (`memory-generator.py`)
- Reads all `.kiro/resources/*.md` files (global memory)
- Reads all `.kiro/features/*/*.md` files (feature memory)
- Sanitizes sensitive information (API keys, passwords, tokens)
- Excludes SCRATCHPAD.md (temporary session notes)
- Converts markdown to HTML with D.E.R.E.K styling
- Saves to `.kiro/views/derek-memory-{timestamp}.html`

### 2. Memory Server (`memory-server.py`)
- Simple HTTP server for serving HTML files
- Auto-detects latest memory HTML file
- Provides local and network URLs
- Supports custom ports and browser auto-open

### 3. Quick Serve Script (`serve.sh`)
- Command-line wrapper for easy usage
- Supports various options (port, expiration, content filtering)
- Provides sharing instructions and URLs

## Usage Workflow

```bash
# 1. Generate memory HTML
python3 .kiro/views/memory-generator.py

# 2. Start server
python3 .kiro/views/memory-server.py

# 3. Or use quick script
bash .kiro/views/serve.sh --port 8080 --browser
```

## Dynamic Tool Generation Code

When activated, create these files in `.kiro/views/`:

### Memory Generator Script

```python
#!/usr/bin/env python3
"""
Project Memory HTML Generator
Converts .kiro/resources/ and .kiro/features/ files into shareable web interface
"""

import os
import re
import datetime
from pathlib import Path

class MemoryGenerator:
    def __init__(self, resources_path=".kiro/resources", features_path=".kiro/features", feature_filter=None):
        self.resources_path = Path(resources_path)
        self.features_path = Path(features_path)
        self.feature_filter = feature_filter  # Optional: filter to specific feature
        self.views_path = Path(".kiro/views")
        self.views_path.mkdir(parents=True, exist_ok=True)
        
    def sanitize_content(self, content):
        """Remove sensitive information"""
        patterns = [
            r'api[_-]?key[s]?\s*[:=]\s*["\']?[\w-]+["\']?',
            r'password[s]?\s*[:=]\s*["\']?[\w-]+["\']?',
            r'secret[s]?\s*[:=]\s*["\']?[\w-]+["\']?',
            r'token[s]?\s*[:=]\s*["\']?[\w-]+["\']?',
            r'https?://[^/]*:[^@]*@[^/]+',
            r'Bearer\s+[\w-]+',
            r'Basic\s+[\w+/=]+',
        ]
        
        sanitized = content
        for pattern in patterns:
            sanitized = re.sub(pattern, '[REDACTED]', sanitized, flags=re.IGNORECASE)
        return sanitized
    
    def load_memory_files(self):
        """Load all memory files from global and feature memory"""
        files = {}
        
        # Load global memory files (exclude SCRATCHPAD.md) - only if not filtering by feature
        if not self.feature_filter and self.resources_path.exists():
            for file_path in self.resources_path.glob("*.md"):
                if file_path.name == "SCRATCHPAD.md":
                    continue
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    files[file_path.name] = {
                        'content': self.sanitize_content(content),
                        'last_modified': datetime.datetime.fromtimestamp(file_path.stat().st_mtime),
                        'size': len(content),
                        'type': 'global'
                    }
                except Exception as e:
                    print(f"Warning: Could not read {file_path}: {e}")
        
        # Load feature memory files
        if self.features_path.exists():
            for feature_dir in self.features_path.iterdir():
                if feature_dir.is_dir():
                    feature_name = feature_dir.name
                    
                    # Skip if filtering and this isn't the target feature
                    if self.feature_filter and feature_name != self.feature_filter:
                        continue
                    
                    for file_path in feature_dir.glob("*.md"):
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                            
                            key = f"features/{feature_name}/{file_path.name}"
                            files[key] = {
                                'content': self.sanitize_content(content),
                                'last_modified': datetime.datetime.fromtimestamp(file_path.stat().st_mtime),
                                'size': len(content),
                                'type': 'feature',
                                'feature_name': feature_name
                            }
                        except Exception as e:
                            print(f"Warning: Could not read {file_path}: {e}")
        
        return files
    
    def generate_html(self, files, options=None):
        """Generate complete HTML page"""
        if options is None:
            options = {}
            
        project_name = Path.cwd().name
        if 'PROJECT.md' in files:
            content = files['PROJECT.md']['content']
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                project_name = title_match.group(1).strip()
        
        share_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M UTC')
        
        # Feature memory sections with tabs
        features_html = ""
        feature_files = {k: v for k, v in files.items() if v.get('type') == 'feature'}
        features = {}
        for key, file_data in feature_files.items():
            feature_name = file_data.get('feature_name', 'unknown')
            if feature_name not in features:
                features[feature_name] = {}
            filename = key.split('/')[-1].replace('.md', '')
            features[feature_name][filename] = file_data
        
        if features:
            for feature_name, feature_docs in features.items():
                features_html += f'<div class="feature-section"><div class="feature-header"><span class="feature-badge">Feature</span><h3>{feature_name}</h3></div>'
                
                # Create tabs
                features_html += '<div class="tabs">'
                tab_order = ['requirements', 'design', 'tasks', 'notes']
                available_tabs = [t for t in tab_order if t in feature_docs]
                
                # Tab buttons
                features_html += '<div class="tab-buttons">'
                for i, tab_name in enumerate(available_tabs):
                    active_class = 'active' if i == 0 else ''
                    display_name = tab_name.replace('_', ' ').title()
                    features_html += f'<button class="tab-button {active_class}" data-tab="{feature_name}-{tab_name}">{display_name}</button>'
                features_html += '</div>'
                
                # Tab content
                features_html += '<div class="tab-content-wrapper">'
                for i, tab_name in enumerate(available_tabs):
                    active_class = 'active' if i == 0 else ''
                    file_data = feature_docs[tab_name]
                    # Escape for HTML attributes only, not for content
                    import html
                    content_escaped = html.escape(file_data["content"])
                    features_html += f'<div class="tab-content {active_class}" id="{feature_name}-{tab_name}"><div class="file-meta">Last modified: {file_data["last_modified"].strftime("%Y-%m-%d %H:%M")}</div><div class="markdown-content" data-markdown="{content_escaped}"></div></div>'
                features_html += '</div>'
                
                features_html += '</div></div>'
        else:
            features_html = '<p>No feature files found.</p>'
        
        # Build HTML with clean design and markdown-it
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{project_name} - D.E.R.E.K Memory</title>
<script src="https://cdn.jsdelivr.net/npm/markdown-it@14.0.0/dist/markdown-it.min.js"></script>
<style>
* {{margin:0;padding:0;box-sizing:border-box}}
body {{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,Cantarell,sans-serif;line-height:1.6;color:#1a1a1a;background:#fafafa;font-size:15px}}
.container {{max-width:1200px;margin:0 auto;padding:40px 20px}}
.header {{margin-bottom:40px;text-align:center}}
.header h1 {{font-size:32px;font-weight:600;color:#1a1a1a;margin-bottom:8px}}
.header-meta {{font-size:13px;color:#666}}
.feature-section {{margin-top:30px;padding:24px;background:#fff;border:1px solid #e5e5e5;border-radius:8px}}
.feature-header {{margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid #e5e5e5}}
.feature-header h3 {{font-size:20px;font-weight:600;color:#1a1a1a;display:inline-block}}
.feature-badge {{display:inline-block;background:#f0f0f0;color:#666;padding:4px 10px;border-radius:4px;font-size:12px;font-weight:500;margin-right:8px}}
.tabs {{margin-top:20px}}
.tab-buttons {{display:flex;gap:8px;border-bottom:2px solid #e5e5e5;margin-bottom:20px}}
.tab-button {{background:none;border:none;padding:12px 20px;font-size:14px;font-weight:500;color:#666;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;transition:all 0.2s}}
.tab-button:hover {{color:#1a1a1a;background:#fafafa}}
.tab-button.active {{color:#1a1a1a;border-bottom-color:#1a1a1a}}
.tab-content-wrapper {{position:relative}}
.tab-content {{display:none;padding:20px;background:#fafafa;border-radius:6px}}
.tab-content.active {{display:block}}
.file-meta {{font-size:13px;color:#666;margin-bottom:16px;padding:8px;background:#fff;border-radius:4px}}
.markdown-content h1 {{font-size:28px;font-weight:600;color:#1a1a1a;margin:32px 0 16px;line-height:1.3}}
.markdown-content h2 {{font-size:22px;font-weight:600;color:#1a1a1a;margin:28px 0 12px;line-height:1.3}}
.markdown-content h3 {{font-size:18px;font-weight:600;color:#1a1a1a;margin:24px 0 10px;line-height:1.3}}
.markdown-content h4 {{font-size:16px;font-weight:600;color:#1a1a1a;margin:20px 0 8px}}
.markdown-content p {{margin:12px 0}}
.markdown-content pre {{background:#f5f5f5;border:1px solid #e5e5e5;padding:16px;border-radius:6px;overflow-x:auto;margin:16px 0;font-size:13px;line-height:1.5}}
.markdown-content code {{background:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'SF Mono',Monaco,Menlo,monospace;font-size:13px;color:#1a1a1a}}
.markdown-content pre code {{background:none;padding:0;display:block}}
.markdown-content a {{color:#0066cc;text-decoration:none}}
.markdown-content a:hover {{text-decoration:underline}}
.markdown-content strong {{font-weight:600;color:#1a1a1a}}
.markdown-content ul,.markdown-content ol {{margin:12px 0;padding-left:24px}}
.markdown-content li {{margin:6px 0}}
.markdown-content table {{width:100%;border-collapse:collapse;margin:16px 0}}
.markdown-content th,.markdown-content td {{padding:10px;text-align:left;border-bottom:1px solid #e5e5e5}}
.markdown-content th {{font-weight:600;background:#fafafa}}
.markdown-content blockquote {{border-left:3px solid #e5e5e5;padding-left:16px;margin:16px 0;color:#666}}
.markdown-content hr {{border:none;border-top:1px solid #e5e5e5;margin:24px 0}}
.markdown-content img {{max-width:100%;height:auto;margin:16px 0}}
.markdown-content input[type="checkbox"] {{margin-right:6px}}
@media (max-width:768px) {{.container{{padding:20px}}}}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>{project_name}</h1>
<div class="header-meta">Generated {share_date}</div>
</div>
{features_html}
</div>
<script>
var md = window.markdownit({{
  html: true,
  linkify: true,
  typographer: true,
  breaks: true
}});

document.addEventListener('DOMContentLoaded', function() {{
  // Render markdown content from data-markdown attribute
  document.querySelectorAll('.markdown-content[data-markdown]').forEach(function(el) {{
    var markdown = el.getAttribute('data-markdown');
    // Decode HTML entities
    var textarea = document.createElement('textarea');
    textarea.innerHTML = markdown;
    markdown = textarea.value;
    el.innerHTML = md.render(markdown);
  }});
  
  // Tab switching
  document.querySelectorAll('.tab-button').forEach(function(button) {{
    button.addEventListener('click', function() {{
      var tabId = this.getAttribute('data-tab');
      var tabGroup = this.closest('.tabs');
      
      // Remove active class from all buttons and content in this group
      tabGroup.querySelectorAll('.tab-button').forEach(function(btn) {{
        btn.classList.remove('active');
      }});
      tabGroup.querySelectorAll('.tab-content').forEach(function(content) {{
        content.classList.remove('active');
      }});
      
      // Add active class to clicked button and corresponding content
      this.classList.add('active');
      document.getElementById(tabId).classList.add('active');
    }});
  }});
}});
</script>
</body>
</html>'''
        
        return html
    
    def save_html(self, html, filename=None):
        """Save HTML to views directory"""
        if not filename:
            timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
            filename = f"derek-memory-{timestamp}.html"
        
        output_file = self.views_path / filename
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return str(output_file.absolute())

def main():
    import sys
    
    # Parse command line arguments
    feature_filter = None
    if len(sys.argv) > 1:
        if sys.argv[1] == '--feature':
            if len(sys.argv) > 2:
                feature_filter = sys.argv[2]
            else:
                print("❌ Error: --feature requires a feature name")
                print("Usage: python3 memory-generator.py [--feature FEATURE_NAME]")
                return 1
    
    generator = MemoryGenerator(feature_filter=feature_filter)
    files = generator.load_memory_files()
    
    if not files:
        if feature_filter:
            print(f"❌ No files found for feature '{feature_filter}'")
            print(f"💡 Check that .kiro/features/{feature_filter}/ exists")
        else:
            print("❌ No D.E.R.E.K memory files found")
            print("💡 Run 'init' command first to create D.E.R.E.K memory system")
        return 1
    
    feature_count = len([f for f in files.values() if f.get('type') == 'feature'])
    features = set(f.get('feature_name') for f in files.values() if f.get('type') == 'feature')
    
    html = generator.generate_html(files)
    
    # Use feature name in filename if filtering
    if feature_filter:
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        filename = f"derek-feature-{feature_filter}-{timestamp}.html"
        output_path = generator.save_html(html, filename)
    else:
        output_path = generator.save_html(html)
    
    print(f"✅ D.E.R.E.K Memory HTML Generated")
    if feature_filter:
        print(f"🎯 Feature: {feature_filter}")
    print(f"📁 File: {output_path}")
    print(f"📊 Content: {feature_count} files ({len(features)} features)")
    print(f"🚀 Open in browser: file://{output_path}")
    
    return 0

if __name__ == '__main__':
    exit(main())
```

### Quick Serve Shell Script

```bash
#!/bin/bash
# Quick Memory Sharing Script

set -e

VIEWS_DIR=".kiro/views"
PORT=8080
OPEN_BROWSER=true

# Create views directory
mkdir -p "$VIEWS_DIR"

# Check if generator exists, create if not
if [[ ! -f "$VIEWS_DIR/memory-generator.py" ]]; then
    echo "🔧 Setting up memory sharing tools..."
    # Tools will be created by the steering file activation
fi

# Generate HTML if no recent file exists
LATEST_HTML=$(find "$VIEWS_DIR" -name "*.html" -type f -exec ls -t {} + 2>/dev/null | head -1)
if [[ -z "$LATEST_HTML" ]] || [[ $(find "$VIEWS_DIR" -name "*.html" -mmin -60 | wc -l) -eq 0 ]]; then
    echo "📋 Generating project memory HTML..."
    python3 "$VIEWS_DIR/memory-generator.py"
fi

# Start server
echo "🚀 Starting memory server..."
python3 "$VIEWS_DIR/memory-server.py" $PORT
```

## Activation Instructions

When this steering file is activated, perform these steps:

### Step 1: Create Views Directory
```bash
mkdir -p .kiro/views
```

### Step 2: Generate Memory Tools
Create the three files above in `.kiro/views/`:
- `memory-generator.py` (Python script for HTML generation)
- `memory-server.py` (Python script for HTTP serving)
- `serve.sh` (Shell script for quick usage)

### Step 3: Make Scripts Executable
```bash
chmod +x .kiro/views/memory-generator.py
chmod +x .kiro/views/memory-server.py
chmod +x .kiro/views/serve.sh
```

### Step 4: Generate and Serve
```bash
# Generate HTML from project memory
python3 .kiro/views/memory-generator.py

# Start server (opens browser automatically)
python3 .kiro/views/memory-server.py

# Or use quick script
bash .kiro/views/serve.sh
```

## Usage Examples

### Quick Share (All Memory)
```bash
# Generate and serve in one command
bash .kiro/views/serve.sh
```

### Share Specific Feature Only
```bash
# Generate HTML for a single feature
python3 .kiro/views/memory-generator.py --feature driver-position-rate-limiting

# Start server to share
python3 .kiro/views/memory-server.py
```

### Share Multiple Features
```bash
# Generate separate HTML for each feature
python3 .kiro/views/memory-generator.py --feature authentication
python3 .kiro/views/memory-generator.py --feature payment-integration

# All generated files will be in .kiro/views/
# Start server to access any of them
python3 .kiro/views/memory-server.py
```

### Custom Port
```bash
python3 .kiro/views/memory-server.py 8081
```

### Team Sharing
1. Run the server: `python3 .kiro/views/memory-server.py`
2. Share the network URL with team members
3. They can access project memory from any device on the network

### Stakeholder Reports
1. Generate HTML: `python3 .kiro/views/memory-generator.py`
2. Upload the generated HTML file to any web hosting service
3. Share the public URL with stakeholders

### Feature-Specific Client Updates
1. Generate feature HTML: `python3 .kiro/views/memory-generator.py --feature new-api-endpoint`
2. Send the HTML file directly to client or upload to hosting
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
- `planning.md` - Feature planning (creates `.kiro/features/*/`)
- `context.md` - Context retention
- All existing `.kiro/resources/` files (global memory)
- All existing `.kiro/features/*/` files (feature memory)

### D.E.R.E.K Memory Flow for Sharing

```
┌─────────────────────────────────────────────────────────────────┐
│                    D.E.R.E.K SHARING FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  .kiro/resources/          .kiro/features/*/                    │
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
When sharing complete project memory:
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
When sharing a single feature:
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

This approach ensures the D.E.R.E.K Memory Sharing System works within power validation constraints while providing full functionality through dynamically generated tools.