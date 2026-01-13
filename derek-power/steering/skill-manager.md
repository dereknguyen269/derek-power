---
name: skill-manager
description: Manage D.E.R.E.K skills - install, update, search, and discover specialized capabilities from GitHub or registries
category: system
keywords: skill, install, update, search, registry, github, capabilities
---

# Skill Manager

## Overview

The Skill Manager enables you to extend D.E.R.E.K's capabilities by installing specialized "skills" - packages of steering files and data that provide domain-specific intelligence.

**Key Features:**
- 🔍 **Discover** skills from registries or GitHub
- 📦 **Install** skills with one command (Kiro format: `.kiro/steering/` + `.shared/`)
- 🔄 **Update** skills automatically
- 🔎 **Search** skill databases
- 🌐 **Cross-platform** - works with skills from Claude, Cursor, Windsurf, etc.
- 🤖 **Intelligent** - auto-detects format and installs to correct Kiro paths

## Quick Start

### Install a Skill from GitHub

```
install skill https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
```

The Skill Manager will:
1. Download the repository
2. Extract skill name (remove `-skill` suffix)
3. Install steering file to `.kiro/steering/<skill-name>.md`
4. Install shared data to `.shared/<skill-name>/`
5. Show you how to use it

### List Available Skills

```
list skills
```

### Search for Skills

```
search skills ui design
```

## Kiro Installation Structure

Skills are installed to match Kiro's expected format:

```
.kiro/
└── steering/
    └── ui-ux-pro-max.md          # Steering file (commands, instructions)

.shared/
└── ui-ux-pro-max/                # Shared database (searchable data)
    ├── ui_styles.json
    ├── color_palettes.json
    ├── font_pairings.json
    └── ...
```

## Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `list skills` | List all available skills | `list skills` |
| `search skills <keyword>` | Search for skills | `search skills api design` |
| `install skill <url>` | Install from GitHub | `install skill https://github.com/...` |
| `update skill <name>` | Update a skill | `update skill ui-ux-pro-max` |
| `uninstall skill <name>` | Uninstall a skill | `uninstall skill ui-ux-pro-max` |

## Python Implementation

```python
#!/usr/bin/env python3
"""
Skill Manager - Kiro Format Installer
Installs skills to .kiro/steering/ and .shared/ directories
"""

import sys
from pathlib import Path
import urllib.request
import json
import shutil
from typing import Dict, List, Optional

# Workspace configuration
WORKSPACE_ROOT = Path.cwd()

class SkillInstaller:
    """Kiro-format skill installer"""
    
    @staticmethod
    def install_from_github(repo_url: str) -> Dict:
        """
        Install skill from GitHub to Kiro format:
        - .kiro/steering/<skill-name>.md
        - .shared/<skill-name>/
        
        Args:
            repo_url: GitHub repository URL
            
        Returns:
            Installation result with status and message
        """
        try:
            # Extract skill name from URL (remove -skill suffix if present)
            skill_name = repo_url.rstrip('/').split('/')[-1]
            if skill_name.endswith('-skill'):
                skill_name = skill_name[:-6]  # Remove '-skill' suffix
            
            # Kiro paths
            steering_file = WORKSPACE_ROOT / ".kiro" / "steering" / f"{skill_name}.md"
            shared_dir = WORKSPACE_ROOT / ".shared" / skill_name
            
            print(f"📦 Installing {skill_name} for Kiro...")
            print(f"📁 Steering: {steering_file}")
            print(f"📁 Shared: {shared_dir}")
            
            # Create directories
            steering_file.parent.mkdir(parents=True, exist_ok=True)
            shared_dir.mkdir(parents=True, exist_ok=True)
            
            # Convert GitHub URL to raw content URL
            raw_base = repo_url.replace('github.com', 'raw.githubusercontent.com') + '/main'
            
            # Download steering file from .kiro/steering/ in repo
            steering_url = f"{raw_base}/.kiro/steering/{skill_name}.md"
            print(f"\n📥 Downloading steering file...")
            
            try:
                with urllib.request.urlopen(steering_url, timeout=10) as response:
                    steering_content = response.read().decode('utf-8')
                    steering_file.write_text(steering_content)
                    print(f"✅ {steering_file.name}")
            except Exception as e:
                return {
                    "success": False,
                    "message": f"❌ Failed to download steering file: {e}\nURL: {steering_url}"
                }
            
            # Download shared directory contents recursively using GitHub API
            print(f"\n📥 Downloading shared files...")
            api_base = repo_url.replace('github.com', 'api.github.com/repos')
            SkillInstaller._download_directory(
                api_base,
                f".shared/{skill_name}",
                shared_dir
            )
            
            return {
                "success": True,
                "message": f"""✅ Successfully installed {skill_name} for Kiro

📁 Files installed:
   • {steering_file}
   • {shared_dir}/

🎯 Usage:
   Type '/' in Kiro chat to see available commands, then select '{skill_name}'
   Or just ask naturally: "Build a landing page for my SaaS product"
""",
                "steering_file": str(steering_file),
                "shared_dir": str(shared_dir)
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"❌ Installation failed: {str(e)}"
            }
    
    @staticmethod
    def _download_directory(api_base: str, path: str, dest_dir: Path):
        """Recursively download directory contents from GitHub"""
        api_url = f"{api_base}/contents/{path}"
        
        try:
            with urllib.request.urlopen(api_url, timeout=10) as response:
                items = json.loads(response.read().decode('utf-8'))
                
                for item in items:
                    item_name = item['name']
                    item_path = dest_dir / item_name
                    
                    if item['type'] == 'file':
                        # Download file
                        with urllib.request.urlopen(item['download_url'], timeout=10) as file_response:
                            item_path.write_bytes(file_response.read())
                        print(f"  ✅ {item['path']}")
                    
                    elif item['type'] == 'dir':
                        # Create directory and recurse
                        item_path.mkdir(parents=True, exist_ok=True)
                        SkillInstaller._download_directory(
                            api_base,
                            item['path'],
                            item_path
                        )
        except Exception as e:
            print(f"  ⚠️  Warning: Could not download {path}: {e}")
    
    @staticmethod
    def uninstall_skill(skill_name: str) -> Dict:
        """Uninstall a skill by removing its files"""
        steering_file = WORKSPACE_ROOT / ".kiro" / "steering" / f"{skill_name}.md"
        shared_dir = WORKSPACE_ROOT / ".shared" / skill_name
        
        removed = []
        
        if steering_file.exists():
            steering_file.unlink()
            removed.append(str(steering_file))
        
        if shared_dir.exists():
            shutil.rmtree(shared_dir)
            removed.append(str(shared_dir))
        
        if removed:
            return {
                "success": True,
                "message": f"✅ Uninstalled {skill_name}\n" + "\n".join(f"   • {f}" for f in removed)
            }
        else:
            return {
                "success": False,
                "message": f"❌ Skill {skill_name} not found"
            }
    
    @staticmethod
    def list_installed_skills() -> List[Dict]:
        """List all installed skills"""
        steering_dir = WORKSPACE_ROOT / ".kiro" / "steering"
        shared_dir = WORKSPACE_ROOT / ".shared"
        
        skills = []
        
        if steering_dir.exists():
            for steering_file in steering_dir.glob("*.md"):
                skill_name = steering_file.stem
                skill_shared = shared_dir / skill_name
                
                skills.append({
                    "name": skill_name,
                    "steering_file": str(steering_file),
                    "shared_dir": str(skill_shared) if skill_shared.exists() else None,
                    "has_data": skill_shared.exists()
                })
        
        return skills

# Export functions
install_skill_from_github = SkillInstaller.install_from_github
uninstall_skill = SkillInstaller.uninstall_skill
list_installed_skills = SkillInstaller.list_installed_skills

# Placeholder functions for future implementation
def search_skills(query: str) -> List[Dict]:
    """Search for skills in registry"""
    return []

def check_updates() -> List[Dict]:
    """Check for skill updates"""
    return []

def update_skill(name: str) -> Dict:
    """Update a skill"""
    return {"success": False, "message": "Update not yet implemented"}

print("✅ Skill Manager loaded successfully")
print(f"📁 Workspace: {WORKSPACE_ROOT}")
```

### Usage Examples

```python
# Install from GitHub (Kiro format)
result = install_skill_from_github("https://github.com/nextlevelbuilder/ui-ux-pro-max-skill")
print(result['message'])

# List installed skills
skills = list_installed_skills()
for skill in skills:
    print(f"• {skill['name']}")
    print(f"  Steering: {skill['steering_file']}")
    if skill['has_data']:
        print(f"  Data: {skill['shared_dir']}")

# Uninstall a skill
result = uninstall_skill("ui-ux-pro-max")
print(result['message'])
```

## Troubleshooting

### Issue: "Failed to download steering file"

**Problem:** The repository doesn't have the file at `.kiro/steering/<skill-name>.md`

**Solution:** 
1. Check if the repository has Kiro format support
2. Look for the steering file in the repository structure
3. Contact the skill author to add Kiro support

### Issue: "Could not download shared files"

**Problem:** The repository doesn't have shared data at `.shared/<skill-name>/`

**Solution:**
1. Some skills may not have shared data (steering-only)
2. Check if the repository has `.shared/` directory
3. You can manually copy the files if needed

### Issue: "Skill not working after installation"

**Checklist:**
1. ✅ Steering file exists at `.kiro/steering/<skill-name>.md`
2. ✅ Shared data exists at `.shared/<skill-name>/` (if required)
3. ✅ Python 3.x is installed (for search scripts)
4. ✅ Try restarting Kiro to reload steering files

### Manual Installation

If automatic installation fails, you can manually copy files:

```bash
# Clone the repository
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

# Copy steering file
cp ui-ux-pro-max-skill/.kiro/steering/ui-ux-pro-max.md .kiro/steering/

# Copy shared data
cp -r ui-ux-pro-max-skill/.shared/ui-ux-pro-max .shared/

# Clean up
rm -rf ui-ux-pro-max-skill
```

---

*Skill Manager is part of D.E.R.E.K Power*
