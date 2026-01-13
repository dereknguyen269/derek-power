"""
Skill Registry - Lists and searches installed skills
"""

import json
from pathlib import Path
from typing import List, Dict, Optional

# Workspace configuration
WORKSPACE_ROOT = Path.cwd()
SKILLS_DIR = WORKSPACE_ROOT / ".kiro" / "skills"


def list_skills() -> List[Dict]:
    """
    List all installed skills
    
    Returns:
        List of skill information dictionaries
    """
    skills = []
    
    if not SKILLS_DIR.exists():
        return skills
    
    for skill_dir in SKILLS_DIR.iterdir():
        if skill_dir.is_dir():
            skill_info = _get_skill_metadata(skill_dir)
            if skill_info:
                skills.append(skill_info)
    
    return sorted(skills, key=lambda x: x['name'])


def search_skills(query: str) -> List[Dict]:
    """
    Search installed skills by name or description
    
    Args:
        query: Search query
        
    Returns:
        List of matching skills
    """
    all_skills = list_skills()
    query_lower = query.lower()
    
    results = []
    for skill in all_skills:
        if (query_lower in skill['name'].lower() or 
            query_lower in skill.get('description', '').lower() or
            any(query_lower in kw.lower() for kw in skill.get('keywords', []))):
            results.append(skill)
    
    return results


def get_skill_info(name: str) -> Optional[Dict]:
    """
    Get detailed information about a skill
    
    Args:
        name: Skill name
        
    Returns:
        Skill information or None if not found
    """
    skill_path = SKILLS_DIR / name
    if skill_path.exists() and skill_path.is_dir():
        return _get_skill_metadata(skill_path)
    return None


def _get_skill_metadata(skill_dir: Path) -> Optional[Dict]:
    """
    Extract metadata from a skill directory
    
    Args:
        skill_dir: Path to skill directory
        
    Returns:
        Skill metadata dictionary
    """
    try:
        manifest_path = skill_dir / "manifest.json"
        
        if manifest_path.exists():
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
        else:
            # Create default manifest if not found
            manifest = {
                "name": skill_dir.name,
                "version": "1.0.0",
                "description": "Installed skill"
            }
        
        # Count files
        steering_count = len(list((skill_dir / "steering").glob("*.md"))) if (skill_dir / "steering").exists() else 0
        data_count = len(list((skill_dir / "data").glob("*"))) if (skill_dir / "data").exists() else 0
        
        return {
            "name": manifest.get("name", skill_dir.name),
            "version": manifest.get("version", "1.0.0"),
            "description": manifest.get("description", ""),
            "author": manifest.get("author", "Unknown"),
            "keywords": manifest.get("keywords", []),
            "path": str(skill_dir),
            "steering_files": steering_count,
            "data_files": data_count,
            "installed": True
        }
    except Exception as e:
        print(f"⚠️  Error reading skill metadata from {skill_dir}: {str(e)}")
        return None
