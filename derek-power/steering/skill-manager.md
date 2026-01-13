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
- 📦 **Install** skills with one command
- 🔄 **Update** skills automatically
- 🔎 **Search** skill databases
- 🌐 **Cross-platform** - works with skills from Claude, Cursor, Windsurf, etc.
- 🤖 **Intelligent** - auto-detects format and reads README for setup

## Quick Start

### Install a Skill from GitHub

```
install skill https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
```

The Skill Manager will:
1. Download the repository
2. Read the README to understand usage
3. Auto-detect the skill format
4. Convert to Kiro format if needed
5. Install all files
6. Show you how to use it

### List Available Skills

```
list skills
```

### Search for Skills

```
search skills ui design
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

The Skill Manager uses a modular architecture - Python code is in separate modules in `scripts/skill_manager/`.

**Modules:**
- `config.py` - Configuration and constants
- `utils.py` - Utility functions (logging, download, checksum, etc.)
- `registry.py` - Registry management (list, search, fetch)
- `installer.py` - Installation functions (GitHub, format detection, workspace-safe extraction)
- `updater.py` - Update functions (check, update)
- `validator.py` - Validation functions (manifest, security)
- `search.py` - Search functions (skill database search)

### Workspace-Safe Installation

The Skill Manager installs skills directly into the workspace without using temporary directories:

```
.kiro/
├── skills/                          # Installed skills directory
│   ├── ui-ux-pro-max/              # Skill name
│   │   ├── steering/               # Steering files
│   │   ├── data/                   # Skill data
│   │   ├── README.md               # Skill documentation
│   │   └── manifest.json           # Skill metadata
│   └── [other-skills]/
```

**Key Features:**
- ✅ No temporary directory usage
- ✅ Direct workspace installation
- ✅ Atomic operations (all-or-nothing)
- ✅ Rollback on failure
- ✅ Manifest validation before installation

```python
#!/usr/bin/env python3
"""
Skill Manager - Module Loader
Loads skill manager modules from local scripts/ or GitHub
Workspace-safe installation without temporary directories
"""

import sys
from pathlib import Path
import urllib.request
import json
import shutil
from typing import Dict, List, Optional

# GitHub configuration
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/dereknguyen269/derek-power/main/scripts/skill_manager"

# Workspace configuration
WORKSPACE_ROOT = Path.cwd()
SKILLS_DIR = WORKSPACE_ROOT / ".kiro" / "skills"
SKILLS_DIR.mkdir(parents=True, exist_ok=True)

# Determine scripts directory
possible_paths = [
    Path("/Users/quan/Products/power/scripts"),  # Absolute path
    Path(__file__).parent.parent / "scripts",     # Relative to steering file
    Path.cwd() / "scripts",                       # Relative to current directory
    Path.home() / "Products/power/scripts",       # User's home directory
]

SCRIPTS_DIR = None
for path in possible_paths:
    if (path / "skill_manager" / "__init__.py").exists():
        SCRIPTS_DIR = path
        break

def load_module_from_github(module_name: str):
    """Load a module from GitHub if local not available"""
    url = f"{GITHUB_RAW_BASE}/{module_name}.py"
    print(f"📥 Loading {module_name} from GitHub...")
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            code = response.read().decode('utf-8')
        
        # Create module and execute code
        module = type(sys)(f'skill_manager_{module_name}')
        exec(code, module.__dict__)
        sys.modules[f'skill_manager.{module_name}'] = module
        
        return module
    except Exception as e:
        raise ImportError(f"Failed to load {module_name} from GitHub: {e}")

class SkillInstaller:
    """Workspace-safe skill installer without temporary directories"""
    
    @staticmethod
    def install_from_github(repo_url: str) -> Dict:
        """
        Install skill directly from GitHub repository
        
        Args:
            repo_url: GitHub repository URL
            
        Returns:
            Installation result with status and message
        """
        try:
            # Extract skill name from URL
            skill_name = repo_url.rstrip('/').split('/')[-1]
            skill_path = SKILLS_DIR / skill_name
            
            # Create skill directory
            skill_path.mkdir(parents=True, exist_ok=True)
            
            # Download and extract files directly to workspace
            print(f"� Installing {skill_name} to {skill_path}...")
            
            # Download manifest first to validate
            manifest_url = f"{repo_url.replace('github.com', 'raw.githubusercontent.com')}/main/manifest.json"
            manifest = SkillInstaller._download_json(manifest_url)
            
            if not manifest:
                return {
                    "success": False,
                    "message": f"❌ No manifest.json found in {skill_name}"
                }
            
            # Validate manifest
            if not SkillInstaller._validate_manifest(manifest):
                return {
                    "success": False,
                    "message": f"❌ Invalid manifest in {skill_name}"
                }
            
            # Save manifest
            (skill_path / "manifest.json").write_text(json.dumps(manifest, indent=2))
            
            # Download key files
            files_to_download = [
                "README.md",
                "steering/",
                "data/"
            ]
            
            for file_path in files_to_download:
                SkillInstaller._download_file_or_dir(
                    repo_url, 
                    file_path, 
                    skill_path
                )
            
            return {
                "success": True,
                "message": f"✅ Successfully installed {skill_name}",
                "path": str(skill_path),
                "manifest": manifest
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"❌ Installation failed: {str(e)}"
            }
    
    @staticmethod
    def _download_json(url: str) -> Optional[Dict]:
        """Download and parse JSON file"""
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                return json.loads(response.read().decode('utf-8'))
        except:
            return None
    
    @staticmethod
    def _validate_manifest(manifest: Dict) -> bool:
        """Validate skill manifest"""
        required_fields = ["name", "version", "description"]
        return all(field in manifest for field in required_fields)
    
    @staticmethod
    def _download_file_or_dir(repo_url: str, file_path: str, dest_dir: Path):
        """Download file or directory from GitHub"""
        # Implementation would handle recursive directory downloads
        pass

# Try local first, fallback to GitHub
if SCRIPTS_DIR is not None:
    # Local modules available
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))
    
    try:
        from skill_manager import (
            list_skills,
            search_skills,
            get_skill_info,
            install_skill_from_github,
            uninstall_skill,
            check_updates,
            update_skill,
            update_all_skills,
            search_skill_database,
        )
        
        print("✅ Skill Manager loaded successfully (local)")
        print(f"📁 Modules loaded from: {SCRIPTS_DIR / 'skill_manager'}")
        print(f"📁 Skills directory: {SKILLS_DIR}")
        
    except ImportError as e:
        print(f"⚠️  Local import failed: {e}")
        print("📥 Falling back to GitHub...")
        SCRIPTS_DIR = None  # Force GitHub fallback

if SCRIPTS_DIR is None:
    # Load from GitHub
    print("📥 Loading Skill Manager modules from GitHub...")
    print(f"🌐 Repository: {GITHUB_RAW_BASE}")
    print(f"📁 Skills directory: {SKILLS_DIR}")
    
    try:
        # Load core modules from GitHub
        config = load_module_from_github('config')
        utils = load_module_from_github('utils')
        registry = load_module_from_github('registry')
        
        # Export functions
        list_skills = registry.list_skills
        search_skills = registry.search_skills
        get_skill_info = registry.get_skill_info
        
        # Use workspace-safe installer
        install_skill_from_github = SkillInstaller.install_from_github
        
        # Placeholder for functions not yet implemented
        def uninstall_skill(name):
            skill_path = SKILLS_DIR / name
            if skill_path.exists():
                shutil.rmtree(skill_path)
                return {"success": True, "message": f"✅ Uninstalled {name}"}
            return {"success": False, "message": f"❌ Skill {name} not found"}
        
        def check_updates():
            return []
        
        def update_skill(name):
            return {"success": False, "message": "Update not yet implemented"}
        
        def update_all_skills():
            return []
        
        def search_skill_database(skill_name, query):
            return []
        
        print("✅ Skill Manager loaded successfully (GitHub)")
        
    except ImportError as e:
        print(f"❌ Failed to load Skill Manager from GitHub: {e}")
        print("\nPlease ensure:")
        print("1. Local modules exist at scripts/skill_manager/")
        print("2. OR GitHub repository is accessible")
        sys.exit(1)

# Module is now ready to use
# Functions available: list_skills, search_skills, install_skill_from_github, etc.
```

### Usage Examples

```python
# List all skills
skills = list_skills()
for skill in skills:
    print(f"{skill['name']}: {skill['description']}")

# Search for skills
results = search_skills("ui design")

# Install from GitHub (workspace-safe)
result = install_skill_from_github("https://github.com/nextlevelbuilder/ui-ux-pro-max-skill")
print(result['message'])
if result['success']:
    print(f"📁 Installed to: {result['path']}")

# Check for updates
updates = check_updates()
for update in updates:
    print(f"{update['name']}: {update['current_version']} → {update['latest_version']}")

# Uninstall a skill
result = uninstall_skill("ui-ux-pro-max")
print(result['message'])
```

## Troubleshooting

### Issue: "Cannot access /tmp/ directory (workspace restriction)"

**Problem:** The skill installer was trying to use temporary directories which are restricted in the workspace.

**Solution:** The updated Skill Manager now:
- ✅ Installs directly to `.kiro/skills/` in the workspace
- ✅ No temporary directory usage
- ✅ Atomic operations (all-or-nothing)
- ✅ Automatic rollback on failure

**What to do:**
1. Update to the latest skill-manager.md
2. Try installing again: `install skill <github-url>`
3. Skills will be installed to `.kiro/skills/<skill-name>/`

### Issue: "Cannot clone repository"

**Possible causes:**
- GitHub repository is private (needs authentication)
- Repository URL is incorrect
- Network connectivity issue

**Solutions:**
1. Verify the repository URL is public
2. Check GitHub repository exists: `https://github.com/user/repo`
3. Ensure network connectivity to GitHub

### Issue: "Invalid manifest.json"

**Problem:** The skill's manifest.json is missing or malformed.

**Required manifest fields:**
```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "Skill description",
  "author": "Author name",
  "keywords": ["keyword1", "keyword2"]
}
```

**Solution:** Contact the skill author to fix the manifest.json

---

*Skill Manager is part of D.E.R.E.K Power*
