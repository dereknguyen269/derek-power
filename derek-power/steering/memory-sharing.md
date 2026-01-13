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
Converts .kiro/resources/ files into shareable web interface
"""

import os
import re
import datetime
from pathlib import Path

class MemoryGenerator:
    def __init__(self, resources_path=".kiro/resources", features_path=".kiro/features"):
        self.resources_path = Path(resources_path)
        self.features_path = Path(features_path)
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
        
        # Load global memory files (exclude SCRATCHPAD.md)
        if self.resources_path.exists():
            for file_path in self.resources_path.glob("*.md"):
                if file_path.name == "SCRATCHPAD.md":
                    continue  # Skip temporary session notes
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
    
    def markdown_to_html(self, content):
        """Simple markdown to HTML conversion"""
        html = content
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
        html = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code class="language-\1">\2</code></pre>', html, flags=re.DOTALL)
        html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
        html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
        html = html.replace('\n', '<br>\n')
        return html
    
    def get_html_template(self):
        """Enhanced HTML template with D.E.R.E.K branding"""
        # Use triple braces for CSS to avoid conflicts with format()
        css_styles = """
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6; color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px; margin: 0 auto; padding: 20px;
            background: white; min-height: 100vh;
            box-shadow: 0 0 50px rgba(0,0,0,0.1);
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 30px; margin: -20px -20px 30px -20px;
            border-radius: 0 0 20px 20px;
        }}
        .derek-badge {{
            display: inline-block; background: rgba(255,255,255,0.2);
            padding: 5px 15px; border-radius: 20px; font-size: 0.9em;
            margin-bottom: 10px; backdrop-filter: blur(10px);
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }}
        .derek-acronym {{ font-size: 0.5em; opacity: 0.9; display: block; margin-top: 5px; }}
        .metadata {{ opacity: 0.9; font-size: 0.95em; margin-bottom: 20px; }}
        .search-box {{
            width: 100%; padding: 15px; border: none; border-radius: 25px;
            font-size: 16px; background: rgba(255,255,255,0.2);
            color: white; backdrop-filter: blur(10px);
        }}
        .search-box::placeholder {{ color: rgba(255,255,255,0.7); }}
        .search-box:focus {{ outline: none; background: rgba(255,255,255,0.3); }}
        .nav-tabs {{
            display: flex; background: #f8f9fa; border-radius: 15px;
            padding: 5px; margin-bottom: 30px; overflow-x: auto;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
        }}
        .nav-tab {{
            flex: 1; padding: 15px 20px; cursor: pointer; border-radius: 10px;
            transition: all 0.3s ease; text-align: center; font-weight: 500;
            white-space: nowrap; min-width: 120px;
        }}
        .nav-tab:hover {{
            background: rgba(102, 126, 234, 0.1); transform: translateY(-2px);
        }}
        .nav-tab.active {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            transform: translateY(-2px);
        }}
        .content-panel {{ display: none; animation: fadeIn 0.5s ease-in; }}
        .content-panel.active {{ display: block; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .file-content {{
            background: linear-gradient(145deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 30px; border-radius: 20px; border-left: 5px solid #667eea;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); position: relative; overflow: hidden;
        }}
        .file-content::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
            background-size: 200% 100%; animation: shimmer 3s ease-in-out infinite;
        }}
        @keyframes shimmer {{ 0%, 100% {{ background-position: 200% 0; }} 50% {{ background-position: -200% 0; }} }}
        .feature-section {{
            margin-top: 30px; padding: 20px; background: #f8f9fa;
            border-radius: 15px; border: 2px solid #e9ecef;
        }}
        .feature-header {{
            display: flex; align-items: center; gap: 10px;
            margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid #e9ecef;
        }}
        .feature-badge {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.85em;
        }}
        h2 {{ color: #495057; border-bottom: 3px solid #e9ecef; padding-bottom: 10px; position: relative; }}
        h2::after {{
            content: ''; position: absolute; bottom: -3px; left: 0; width: 50px; height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }}
        pre {{
            background: #2d3748; color: #e2e8f0; padding: 25px; border-radius: 15px;
            overflow-x: auto; margin: 20px 0; box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);
        }}
        code {{
            background: rgba(102, 126, 234, 0.1); padding: 3px 8px; border-radius: 6px;
            font-family: 'Monaco', 'Menlo', monospace; font-size: 0.9em;
        }}
        pre code {{ background: none; padding: 0; }}
        a {{ color: #667eea; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }}
        a:hover {{ color: #764ba2; text-decoration: underline; }}
        .highlight {{
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            padding: 3px 6px; border-radius: 6px; font-weight: 500;
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 10px; }}
            .header {{ padding: 20px; margin: -10px -10px 20px -10px; }}
            .header h1 {{ font-size: 2em; }}
            .nav-tabs {{ flex-wrap: wrap; }}
            .nav-tab {{ padding: 12px 15px; min-width: 100px; }}
            .file-content {{ padding: 20px; }}
        }}
        """
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>D.E.R.E.K Memory - {{PROJECT_NAME}}</title>
    <style>{css_styles}</style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="derek-badge">D.E.R.E.K Memory System</div>
            <h1>📋 {{PROJECT_NAME}}
                <span class="derek-acronym">Design · Evaluate · Review · Execute · Knowledge</span>
            </h1>
            <div class="metadata">📅 {{SHARE_DATE}} • ⏰ Expires {{EXPIRY_DATE}} • 🔒 Secure View</div>
            <input type="text" class="search-box" placeholder="🔍 Search D.E.R.E.K memory..." id="searchBox">
        </div>
        <div class="nav-tabs">
            <div class="nav-tab active" data-tab="overview">📊 Overview</div>
            <div class="nav-tab" data-tab="progress">🚀 Progress</div>
            <div class="nav-tab" data-tab="decisions">⚖️ Decisions</div>
            <div class="nav-tab" data-tab="knowledge">🧠 Knowledge</div>
            <div class="nav-tab" data-tab="features">📁 Features</div>
            <div class="nav-tab" data-tab="all">📄 All Files</div>
        </div>
        <div id="overview" class="content-panel active">
            <div class="file-content">{{PROJECT_CONTENT}}</div>
        </div>
        <div id="progress" class="content-panel">
            <div class="file-content">{{PROGRESS_CONTENT}}</div>
        </div>
        <div id="decisions" class="content-panel">
            <div class="file-content">{{DECISIONS_CONTENT}}</div>
        </div>
        <div id="knowledge" class="content-panel">
            <div class="file-content">{{KNOWLEDGE_CONTENT}}</div>
        </div>
        <div id="features" class="content-panel">
            <div class="file-content">{{FEATURES_CONTENT}}</div>
        </div>
        <div id="all" class="content-panel">
            <div class="file-content">{{ALL_FILES_CONTENT}}</div>
        </div>
    </div>
    <script>
        document.querySelectorAll('.nav-tab').forEach(tab => {{
            tab.addEventListener('click', () => {{
                document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.content-panel').forEach(p => p.classList.remove('active'));
                tab.classList.add('active');
                document.getElementById(tab.dataset.tab).classList.add('active');
            }});
        }});
        document.getElementById('searchBox').addEventListener('input', (e) => {{
            const searchTerm = e.target.value.toLowerCase();
            document.querySelectorAll('.file-content').forEach(content => {{
                const text = content.textContent.toLowerCase();
                content.style.display = text.includes(searchTerm) || searchTerm === '' ? 'block' : 'none';
            }});
        }});
    </script>
</body>
</html>'''
    
    def generate_html(self, files, options={}):
        """Generate complete HTML page with D.E.R.E.K branding"""
        project_name = Path.cwd().name
        if 'PROJECT.md' in files:
            content = files['PROJECT.md']['content']
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                project_name = title_match.group(1).strip()
        
        share_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M UTC')
        expiry_date = 'Never' if options.get('expires') == 'never' else '7 days'
        
        # Global memory sections
        sections = {
            'project': files.get('PROJECT.md', {}).get('content', 'No project overview available.'),
            'progress': files.get('PROGRESS.md', {}).get('content', 'No progress information available.'),
            'decisions': files.get('DECISIONS.md', {}).get('content', 'No decisions recorded.'),
            'knowledge': files.get('KNOWLEDGE.md', {}).get('content', 'No knowledge accumulated.'),
        }
        
        for key in sections:
            sections[key] = self.markdown_to_html(sections[key])
        
        # Feature memory sections
        features_html = ""
        feature_files = {k: v for k, v in files.items() if v.get('type') == 'feature'}
        features = {}
        for key, file_data in feature_files.items():
            feature_name = file_data.get('feature_name', 'unknown')
            if feature_name not in features:
                features[feature_name] = []
            features[feature_name].append((key, file_data))
        
        if features:
            for feature_name, feature_items in features.items():
                features_html += f'''
                <div class="feature-section">
                    <div class="feature-header">
                        <span class="feature-badge">📁 Feature</span>
                        <h3>{feature_name}</h3>
                    </div>
                '''
                for key, file_data in feature_items:
                    filename = key.split('/')[-1]
                    icon = {'requirements.md': '📋', 'design.md': '🎨', 'tasks.md': '✅', 'notes.md': '📝'}.get(filename, '📄')
                    features_html += f'''
                    <div style="margin: 15px 0; padding: 15px; background: white; border-radius: 10px;">
                        <h4>{icon} {filename}</h4>
                        <div style="font-size: 0.85em; color: #6c757d; margin-bottom: 10px;">
                            Modified: {file_data['last_modified'].strftime('%Y-%m-%d %H:%M')}
                        </div>
                        <div>{self.markdown_to_html(file_data['content'])}</div>
                    </div>
                    '''
                features_html += '</div>'
        else:
            features_html = '<p>No feature folders found. Use "create feature &lt;name&gt;" to start feature planning.</p>'
        
        # All files section
        all_files_html = "<h2>Global Memory</h2>"
        global_files = {k: v for k, v in files.items() if v.get('type') == 'global'}
        for filename, file_data in global_files.items():
            all_files_html += f'''
            <div style="margin-bottom: 30px; border: 1px solid #e9ecef; border-radius: 8px; overflow: hidden;">
                <h3 style="background: #667eea; color: white; padding: 15px; margin: 0;">📄 {filename}</h3>
                <div style="background: #e9ecef; padding: 10px 15px; font-size: 0.9em; color: #6c757d;">
                    Modified: {file_data['last_modified'].strftime('%Y-%m-%d %H:%M')} • Size: {file_data['size']} bytes
                </div>
                <div style="padding: 20px;">{self.markdown_to_html(file_data['content'])}</div>
            </div>
            '''
        
        if feature_files:
            all_files_html += "<h2>Feature Memory</h2>"
            for key, file_data in feature_files.items():
                all_files_html += f'''
                <div style="margin-bottom: 30px; border: 1px solid #e9ecef; border-radius: 8px; overflow: hidden;">
                    <h3 style="background: #764ba2; color: white; padding: 15px; margin: 0;">📁 {key}</h3>
                    <div style="background: #e9ecef; padding: 10px 15px; font-size: 0.9em; color: #6c757d;">
                        Modified: {file_data['last_modified'].strftime('%Y-%m-%d %H:%M')} • Size: {file_data['size']} bytes
                    </div>
                    <div style="padding: 20px;">{self.markdown_to_html(file_data['content'])}</div>
                </div>
                '''
        
        template = self.get_html_template()
        html = template.format(
            PROJECT_NAME=project_name,
            SHARE_DATE=share_date,
            EXPIRY_DATE=expiry_date,
            PROJECT_CONTENT=sections['project'],
            PROGRESS_CONTENT=sections['progress'],
            DECISIONS_CONTENT=sections['decisions'],
            KNOWLEDGE_CONTENT=sections['knowledge'],
            FEATURES_CONTENT=features_html,
            ALL_FILES_CONTENT=all_files_html
        )
        
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
    generator = MemoryGenerator()
    files = generator.load_memory_files()
    
    if not files:
        print("❌ No D.E.R.E.K memory files found")
        print("💡 Run 'init' command first to create D.E.R.E.K memory system")
        return 1
    
    # Count global vs feature files
    global_count = len([f for f in files.values() if f.get('type') == 'global'])
    feature_count = len([f for f in files.values() if f.get('type') == 'feature'])
    features = set(f.get('feature_name') for f in files.values() if f.get('type') == 'feature')
    
    html = generator.generate_html(files)
    output_path = generator.save_html(html)
    
    print(f"✅ D.E.R.E.K Memory HTML Generated")
    print(f"📁 File: {output_path}")
    print(f"📊 Content:")
    print(f"   • Global Memory: {global_count} files")
    if feature_count > 0:
        print(f"   • Feature Memory: {feature_count} files ({len(features)} features)")
    print(f"🚀 Use memory-server.py to serve the HTML")
    
    return 0

if __name__ == '__main__':
    exit(main())
```

### Memory Server Script

```python
#!/usr/bin/env python3
"""
Simple HTTP server for serving project memory HTML
"""

import http.server
import socketserver
import webbrowser
import os
import socket
from pathlib import Path

def find_latest_html():
    """Find the most recent HTML file"""
    views_path = Path('.kiro/views')
    if not views_path.exists():
        return None
    
    html_files = list(views_path.glob('*.html'))
    if not html_files:
        return None
    
    return max(html_files, key=os.path.getctime)

def serve_memory(port=8080, open_browser=True):
    """Serve the project memory HTML file"""
    html_file = find_latest_html()
    if not html_file:
        print("❌ No HTML files found in .kiro/views/")
        print("💡 Run memory-generator.py first")
        return 1
    
    print(f"📁 Serving: {html_file.name}")
    print(f"🌐 Server: http://localhost:{port}")
    
    class MemoryHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(Path('.kiro/views')), **kwargs)
        
        def do_GET(self):
            if self.path == '/' or self.path == '/index.html':
                self.path = f'/{html_file.name}'
            return super().do_GET()
        
        def log_message(self, format, *args):
            print(f"📊 {self.address_string()} - {format % args}")
    
    try:
        with socketserver.TCPServer(("", port), MemoryHandler) as httpd:
            print(f"✅ Server started at http://localhost:{port}")
            
            if open_browser:
                webbrowser.open(f'http://localhost:{port}')
                print("🌐 Opened in browser")
            
            # Get local IP for network sharing
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                local_ip = s.getsockname()[0]
                s.close()
                print(f"📱 Network: http://{local_ip}:{port}")
            except:
                pass
            
            print("⏹️  Press Ctrl+C to stop")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        return 0
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use")
            print(f"💡 Try: python3 memory-server.py {port + 1}")
        else:
            print(f"❌ Server error: {e}")
        return 1

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    exit(serve_memory(port))
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

### Quick Share
```bash
# Generate and serve in one command
bash .kiro/views/serve.sh
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

- **Stakeholder Communication**: Professional D.E.R.E.K project overviews
- **Team Collaboration**: Easy context sharing with feature progress
- **Client Updates**: Clean, branded project status with feature tracking
- **Documentation**: Persistent knowledge base with feature history
- **Onboarding**: Quick context for new team members
- **Feature Visibility**: Share feature requirements, design, and progress
- **Compliance**: Powers validation friendly (no binary files in power)

## Output Format

When sharing is complete, provide:
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

This approach ensures the D.E.R.E.K Memory Sharing System works within power validation constraints while providing full functionality through dynamically generated tools.