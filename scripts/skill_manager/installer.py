"""
Installation functions for Skill Manager
Handles downloading, extracting, and installing skills from GitHub
"""

import json
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

from .config import STEERING_DIR, SHARED_DIR, SKILLS_DIR, BACKUP_DIR, TRUSTED_DOMAINS
from .utils import (
    log, load_installed_skills, save_installed_skills,
    download_file, parse_github_url
)
from .validator import validate_manifest, scan_for_malicious_patterns, validate_source


def detect_skill_format(skill_dir: Path) -> str:
    """
    Detect skill format by analyzing directory structure
    
    Args:
        skill_dir: Path to skill directory
        
    Returns:
        Format identifier string
    """
    # Check for Kiro format
    if (skill_dir / '.kiro' / 'steering').exists():
        return 'kiro'
    
    # Check for Claude format
    if (skill_dir / '.claude' / 'skills').exists():
        return 'claude'
    
    # Check for Cursor format
    if (skill_dir / '.cursor' / 'commands').exists():
        return 'cursor'
    
    # Check for Windsurf format
    if (skill_dir / '.windsurf' / 'workflows').exists():
        return 'windsurf'
    
    # Check for Antigravity format
    if (skill_dir / '.agent' / 'workflows').exists():
        return 'antigravity'
    
    # Check for GitHub Copilot format
    if (skill_dir / '.github' / 'prompts').exists():
        return 'github-copilot'
    
    # Check for Codex format
    if (skill_dir / '.codex' / 'skills').exists():
        return 'codex'
    
    # Check for Gemini format
    if (skill_dir / '.gemini' / 'skills').exists():
        return 'gemini'
    
    # Default to generic format
    return 'generic'


def extract_usage_from_readme(readme_path: Path) -> Optional[str]:
    """
    Extract usage instructions from README
    
    Args:
        readme_path: Path to README.md file
        
    Returns:
        Usage instructions string or None
    """
    if not readme_path.exists():
        return None
    
    try:
        content = readme_path.read_text()
        
        # Look for Usage, How to Use, or Commands sections
        patterns = [
            r'## Usage\n(.*?)(?=\n##|\Z)',
            r'## How to Use\n(.*?)(?=\n##|\Z)',
            r'## Commands\n(.*?)(?=\n##|\Z)',
            r'## Example Prompts\n(.*?)(?=\n##|\Z)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # Fallback: return first few paragraphs after title
        lines = content.split('\n')
        usage_lines = []
        skip_title = True
        
        for line in lines:
            if skip_title and line.startswith('#'):
                skip_title = False
                continue
            if not skip_title and line.strip():
                usage_lines.append(line)
                if len(usage_lines) >= 10:  # First 10 non-empty lines
                    break
        
        return '\n'.join(usage_lines) if usage_lines else None
        
    except Exception as e:
        log(f"Failed to extract usage from README: {e}", "WARNING")
        return None


def generate_manifest_from_repo(skill_dir: Path, readme_path: Optional[Path], skill_format: str) -> Dict:
    """
    Auto-generate manifest from repository structure and README
    
    Args:
        skill_dir: Path to skill directory
        readme_path: Path to README.md (optional)
        skill_format: Detected skill format
        
    Returns:
        Generated manifest dictionary
    """
    # Extract name from directory
    skill_name = skill_dir.name.lower().replace('_', '-').replace(' ', '-')
    # Remove common suffixes
    for suffix in ['-skill', '-skills', '-power', '-agent']:
        if skill_name.endswith(suffix):
            skill_name = skill_name[:-len(suffix)]
    
    # Parse README for description
    description = "Auto-generated skill"
    if readme_path and readme_path.exists():
        try:
            content = readme_path.read_text()
            # Get first paragraph after title
            lines = [l for l in content.split('\n') if l.strip() and not l.startswith('#')]
            if lines:
                description = lines[0][:500]  # First 500 chars
        except Exception:
            pass
    
    # Detect files to install
    files = {
        'steering': [],
        'data': [],
        'scripts': []
    }
    
    # Find steering files based on format
    if skill_format == 'kiro':
        steering_dir = skill_dir / '.kiro' / 'steering'
        if steering_dir.exists():
            for f in steering_dir.glob('*.md'):
                files['steering'].append({
                    'source': str(f.relative_to(skill_dir)),
                    'destination': f'.kiro/steering/{f.name}'
                })
    elif skill_format in ['claude', 'cursor', 'windsurf', 'generic']:
        # Look for markdown files in common locations
        for md_file in skill_dir.rglob('*.md'):
            if md_file.name.lower() not in ['readme.md', 'changelog.md', 'license.md']:
                files['steering'].append({
                    'source': str(md_file.relative_to(skill_dir)),
                    'destination': f'.kiro/steering/{skill_name}.md'
                })
                break  # Take first one
    
    # Find data files in .shared/ or data/
    for data_dir_name in ['.shared', 'data', 'database']:
        data_dir = skill_dir / data_dir_name
        if data_dir.exists():
            for f in data_dir.rglob('*'):
                if f.is_file():
                    rel_path = f.relative_to(data_dir)
                    if f.suffix == '.py':
                        files['scripts'].append({
                            'source': str(f.relative_to(skill_dir)),
                            'destination': f'.shared/{skill_name}/{rel_path}'
                        })
                    else:
                        files['data'].append({
                            'source': str(f.relative_to(skill_dir)),
                            'destination': f'.shared/{skill_name}/{rel_path}'
                        })
    
    # Generate manifest
    manifest = {
        'name': skill_name,
        'version': '1.0.0',
        'description': description,
        'author': 'Unknown',
        'category': 'Other',
        'tags': [],
        'files': files,
        'auto_generated': True
    }
    
    log(f"Generated manifest for {skill_name}")
    return manifest


def convert_to_kiro_format(skill_dir: Path, from_format: str, manifest: Dict) -> None:
    """
    Convert skill from other format to Kiro format
    
    Args:
        skill_dir: Path to skill directory
        from_format: Source format identifier
        manifest: Skill manifest
    """
    if from_format == 'kiro':
        return  # Already in Kiro format
    
    kiro_dir = skill_dir / '.kiro' / 'steering'
    kiro_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert based on format
    if from_format == 'claude':
        claude_dir = skill_dir / '.claude' / 'skills'
        if claude_dir.exists():
            for md_file in claude_dir.rglob('*.md'):
                dest = kiro_dir / md_file.name
                shutil.copy2(md_file, dest)
                log(f"Converted Claude skill file: {md_file.name}")
    
    elif from_format == 'cursor':
        cursor_dir = skill_dir / '.cursor' / 'commands'
        if cursor_dir.exists():
            for md_file in cursor_dir.glob('*.md'):
                dest = kiro_dir / md_file.name
                shutil.copy2(md_file, dest)
                log(f"Converted Cursor command file: {md_file.name}")
    
    elif from_format == 'windsurf':
        windsurf_dir = skill_dir / '.windsurf' / 'workflows'
        if windsurf_dir.exists():
            for md_file in windsurf_dir.glob('*.md'):
                dest = kiro_dir / md_file.name
                shutil.copy2(md_file, dest)
                log(f"Converted Windsurf workflow file: {md_file.name}")
    
    # Update manifest to reflect new paths
    for file_entry in manifest['files'].get('steering', []):
        old_source = file_entry['source']
        # Update source path to point to converted location
        if not old_source.startswith('.kiro/'):
            file_entry['source'] = f".kiro/steering/{Path(old_source).name}"
    
    log(f"Converted {from_format} format to Kiro format")


def install_files(manifest: Dict, skill_dir: Path) -> None:
    """
    Install skill files to their destinations
    
    Args:
        manifest: Skill manifest with file mappings
        skill_dir: Source directory containing skill files
    """
    skill_name = manifest['name']
    
    # Install steering files
    for file_info in manifest['files'].get('steering', []):
        source = skill_dir / file_info['source']
        dest = Path.home() / file_info['destination']
        
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        log(f"Installed steering file: {dest}")
    
    # Install data files
    for file_info in manifest['files'].get('data', []):
        source = skill_dir / file_info['source']
        dest = Path.home() / file_info['destination']
        
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        log(f"Installed data file: {dest}")
    
    # Install scripts
    for file_info in manifest['files'].get('scripts', []):
        source = skill_dir / file_info['source']
        dest = Path.home() / file_info['destination']
        
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        log(f"Installed script: {dest}")


def backup_skill(skill_name: str) -> Path:
    """
    Create backup of existing skill files
    
    Args:
        skill_name: Name of skill to backup
        
    Returns:
        Path to backup directory
    """
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_path = BACKUP_DIR / f"{skill_name}-{timestamp}"
    backup_path.mkdir(parents=True, exist_ok=True)
    
    # Backup steering files
    steering_file = STEERING_DIR / f"{skill_name}.md"
    if steering_file.exists():
        dest = backup_path / 'steering'
        dest.mkdir(exist_ok=True)
        shutil.copy2(steering_file, dest / steering_file.name)
    
    # Backup shared files
    shared_dir = SHARED_DIR / skill_name
    if shared_dir.exists():
        dest = backup_path / 'shared'
        shutil.copytree(shared_dir, dest / skill_name)
    
    log(f"Created backup: {backup_path}")
    return backup_path


def restore_backup(backup_path: Path) -> None:
    """
    Restore files from backup
    
    Args:
        backup_path: Path to backup directory
    """
    # Restore steering files
    steering_backup = backup_path / 'steering'
    if steering_backup.exists():
        for file in steering_backup.glob('*.md'):
            dest = STEERING_DIR / file.name
            shutil.copy2(file, dest)
            log(f"Restored steering file: {dest}")
    
    # Restore shared files
    shared_backup = backup_path / 'shared'
    if shared_backup.exists():
        for skill_dir in shared_backup.iterdir():
            dest = SHARED_DIR / skill_dir.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(skill_dir, dest)
            log(f"Restored shared files: {dest}")


def uninstall_skill(skill_name: str) -> Dict:
    """
    Uninstall a skill
    
    Args:
        skill_name: Name of skill to uninstall
        
    Returns:
        Result dictionary with success status and message
    """
    installed = load_installed_skills()
    
    if skill_name not in installed:
        return {
            'success': False,
            'message': f"Skill '{skill_name}' is not installed"
        }
    
    # Create backup before uninstalling
    backup_path = backup_skill(skill_name)
    
    try:
        # Remove steering files
        steering_file = STEERING_DIR / f"{skill_name}.md"
        if steering_file.exists():
            steering_file.unlink()
            log(f"Removed steering file: {steering_file}")
        
        # Remove shared files
        shared_dir = SHARED_DIR / skill_name
        if shared_dir.exists():
            shutil.rmtree(shared_dir)
            log(f"Removed shared directory: {shared_dir}")
        
        # Remove from installed registry
        del installed[skill_name]
        save_installed_skills(installed)
        
        return {
            'success': True,
            'message': f"Uninstalled {skill_name}",
            'backup': str(backup_path)
        }
        
    except Exception as e:
        log(f"Failed to uninstall {skill_name}: {e}", "ERROR")
        # Restore from backup
        restore_backup(backup_path)
        return {
            'success': False,
            'message': f"Failed to uninstall: {e}"
        }


def install_skill_from_github(github_url: str, force: bool = False) -> Dict:
    """
    Install a skill from GitHub URL with auto-detection and setup
    
    Args:
        github_url: GitHub repository URL
        force: Force reinstall if already installed
        
    Returns:
        Result dictionary with success status, message, and usage info
    """
    import re
    
    # Validate source
    if not validate_source(github_url, TRUSTED_DOMAINS):
        return {
            'success': False,
            'message': f"Untrusted source: {github_url}. Only install from trusted sources."
        }
    
    try:
        # Parse GitHub URL
        repo_info = parse_github_url(github_url)
        log(f"Installing from {repo_info['owner']}/{repo_info['repo']}")
        
        # Download repository as ZIP
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            
            # Download from GitHub
            zip_url = f"https://github.com/{repo_info['owner']}/{repo_info['repo']}/archive/refs/heads/{repo_info['branch']}.zip"
            package_path = tmpdir_path / "skill.zip"
            
            if not download_file(zip_url, package_path):
                return {
                    'success': False,
                    'message': f"Failed to download from {zip_url}"
                }
            
            # Extract
            extract_dir = tmpdir_path / "extracted"
            with zipfile.ZipFile(package_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            
            # Find the actual directory (GitHub adds repo name prefix)
            skill_dir = next(extract_dir.iterdir())
            
            # Read and parse README for usage instructions
            readme_path = skill_dir / "README.md"
            usage_instructions = extract_usage_from_readme(readme_path)
            
            # Detect skill format
            skill_format = detect_skill_format(skill_dir)
            log(f"Detected format: {skill_format}")
            
            # Check for existing manifest or generate one
            manifest_path = skill_dir / "skill.json"
            if manifest_path.exists():
                manifest = json.loads(manifest_path.read_text())
                log("Using existing manifest")
            else:
                # Auto-generate manifest
                manifest = generate_manifest_from_repo(skill_dir, readme_path, skill_format)
                log("Generated manifest from repository")
            
            # Convert to Kiro format if needed
            if skill_format != 'kiro':
                convert_to_kiro_format(skill_dir, skill_format, manifest)
            
            # Validate manifest
            validate_manifest(manifest)
            
            # Check if already installed
            installed = load_installed_skills()
            skill_name = manifest['name']
            if skill_name in installed and not force:
                return {
                    'success': False,
                    'message': f"Skill '{skill_name}' already installed. Use force=True to reinstall"
                }
            
            # Create backup if updating
            if skill_name in installed:
                backup_skill(skill_name)
            
            # Install files
            install_files(manifest, skill_dir)
            
            # Update installed registry
            installed[skill_name] = {
                'version': manifest['version'],
                'installed_at': datetime.now().isoformat(),
                'source': github_url,
                'format': skill_format,
                'usage': usage_instructions
            }
            save_installed_skills(installed)
            
            # Return success with usage instructions
            result = {
                'success': True,
                'message': f"✅ Installed {skill_name} v{manifest['version']}",
                'skill_name': skill_name,
                'version': manifest['version'],
                'format': skill_format,
                'usage': usage_instructions,
                'commands': manifest.get('commands', [])
            }
            
            log(f"Successfully installed {skill_name}")
            return result
            
    except Exception as e:
        log(f"Installation failed: {e}", "ERROR")
        return {
            'success': False,
            'message': f"Installation failed: {e}"
        }
