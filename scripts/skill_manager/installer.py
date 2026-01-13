"""
Skill Installer - Downloads and installs skills from GitHub
Workspace-safe installation without temporary directories
"""

import json
import shutil
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, Optional

# Workspace configuration
WORKSPACE_ROOT = Path.cwd()
SKILLS_DIR = WORKSPACE_ROOT / ".kiro" / "skills"
SKILLS_DIR.mkdir(parents=True, exist_ok=True)


def install_skill_from_github(repo_url: str) -> Dict:
    """
    Install skill directly from GitHub repository
    
    Args:
        repo_url: GitHub repository URL (e.g., https://github.com/user/repo)
        
    Returns:
        Installation result with status and message
    """
    try:
        # Extract skill name from URL
        skill_name = repo_url.rstrip('/').split('/')[-1]
        skill_path = SKILLS_DIR / skill_name
        
        # Create skill directory
        skill_path.mkdir(parents=True, exist_ok=True)
        
        print(f"📦 Installing {skill_name} to {skill_path}...")
        
        # Convert GitHub URL to raw content URL
        # Example: https://github.com/user/repo → https://raw.githubusercontent.com/user/repo/main
        if repo_url.startswith('https://github.com/'):
            parts = repo_url.rstrip('/').replace('https://github.com/', '').replace('.git', '')
            raw_base = f'https://raw.githubusercontent.com/{parts}/main'
        else:
            # Fallback for other formats
            raw_base = repo_url.rstrip('/').replace('.git', '') + '/main'
        
        # Download README first
        readme_url = f"{raw_base}/README.md"
        readme_content = _download_file(readme_url)
        if readme_content:
            (skill_path / "README.md").write_text(readme_content)
            print(f"✅ Downloaded README.md")
        
        # Download manifest
        manifest_url = f"{raw_base}/manifest.json"
        manifest_json = _download_file(manifest_url)
        if manifest_json:
            try:
                manifest = json.loads(manifest_json)
                (skill_path / "manifest.json").write_text(json.dumps(manifest, indent=2))
                print(f"✅ Downloaded manifest.json")
            except json.JSONDecodeError:
                print(f"⚠️  Invalid manifest.json format")
                manifest = None
        else:
            print(f"⚠️  No manifest.json found, creating default")
            manifest = {
                "name": skill_name,
                "version": "1.0.0",
                "description": f"Skill: {skill_name}"
            }
            (skill_path / "manifest.json").write_text(json.dumps(manifest, indent=2))
        
        # Download steering files
        steering_dir = skill_path / "steering"
        steering_dir.mkdir(exist_ok=True)
        
        # Try multiple steering file locations
        steering_locations = [
            f"{raw_base}/steering/",
            f"{raw_base}/.kiro/steering/",
            f"{raw_base}/.shared/{skill_name}/",
        ]
        
        steering_files = [
            f"{skill_name}.md",
            "index.md",
            "core.md",
            "guidelines.md",
            "ui-ux-pro-max.md"
        ]
        
        steering_count = 0
        for location in steering_locations:
            for steering_file in steering_files:
                steering_url = f"{location}{steering_file}"
                content = _download_file(steering_url)
                if content:
                    (steering_dir / steering_file).write_text(content)
                    print(f"✅ Downloaded steering/{steering_file}")
                    steering_count += 1
                    break  # Found file, move to next file
            if steering_count > 0:
                break  # Found files in this location
        
        if steering_count == 0:
            print(f"⚠️  No steering files found")
        
        # Download data files
        data_dir = skill_path / "data"
        data_dir.mkdir(exist_ok=True)
        
        # Try multiple data file locations
        data_locations = [
            f"{raw_base}/data/",
            f"{raw_base}/.shared/{skill_name}/data/",
            f"{raw_base}/.shared/{skill_name}/",
        ]
        
        data_files = [
            "styles.json",
            "colors.json",
            "fonts.json",
            "guidelines.json",
            "database.json",
            "index.json",
            "database.md"
        ]
        
        data_count = 0
        for location in data_locations:
            for data_file in data_files:
                data_url = f"{location}{data_file}"
                content = _download_file(data_url)
                if content:
                    (data_dir / data_file).write_text(content)
                    print(f"✅ Downloaded data/{data_file}")
                    data_count += 1
                    break  # Found file, move to next file
            if data_count > 0:
                break  # Found files in this location
        
        if data_count == 0:
            print(f"⚠️  No data files found")
        
        # Summary
        print(f"\n📊 Installation Summary:")
        print(f"   Skill: {skill_name}")
        print(f"   Location: {skill_path}")
        print(f"   Steering files: {steering_count}")
        print(f"   Data files: {data_count}")
        
        return {
            "success": True,
            "message": f"✅ Successfully installed {skill_name}",
            "path": str(skill_path),
            "manifest": manifest,
            "files_downloaded": steering_count + data_count
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"❌ Installation failed: {str(e)}"
        }


def uninstall_skill(name: str) -> Dict:
    """
    Uninstall a skill
    
    Args:
        name: Skill name
        
    Returns:
        Uninstall result
    """
    try:
        skill_path = SKILLS_DIR / name
        if skill_path.exists():
            shutil.rmtree(skill_path)
            return {
                "success": True,
                "message": f"✅ Uninstalled {name}"
            }
        return {
            "success": False,
            "message": f"❌ Skill {name} not found"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"❌ Uninstall failed: {str(e)}"
        }


def _download_file(url: str) -> Optional[str]:
    """
    Download file content from URL
    
    Args:
        url: URL to download from
        
    Returns:
        File content or None if not found
    """
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None  # File doesn't exist, that's ok
        raise
    except Exception as e:
        print(f"⚠️  Failed to download {url}: {str(e)}")
        return None
