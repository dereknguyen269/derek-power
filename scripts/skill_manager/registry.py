"""
Registry management for Skill Manager
Handles fetching, caching, and querying skill registries
"""

import json
import urllib.request
import urllib.error
from typing import List, Dict, Optional
from datetime import datetime

from .config import REGISTRY_URL, CACHE_PATH, CACHE_TTL_HOURS
from .utils import log, load_installed_skills


def fetch_registry(url: str = REGISTRY_URL, force_refresh: bool = False) -> Dict:
    """
    Fetch and cache skill registry
    
    Args:
        url: Registry URL to fetch from
        force_refresh: Force refresh even if cache is valid
        
    Returns:
        Registry data dictionary
    """
    # Check cache first (unless force refresh)
    if not force_refresh and CACHE_PATH.exists():
        try:
            cache_data = json.loads(CACHE_PATH.read_text())
            # Check if cache is less than TTL hours old
            last_updated = datetime.fromisoformat(cache_data.get('last_updated', '2000-01-01'))
            age_hours = (datetime.now() - last_updated).total_seconds() / 3600
            
            if age_hours < CACHE_TTL_HOURS:
                log("Using cached registry data")
                return cache_data
        except (json.JSONDecodeError, ValueError):
            log("Cache corrupted, fetching fresh data", "WARNING")
    
    # Fetch from URL
    try:
        log(f"Fetching registry from {url}")
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        # Add timestamp and cache
        data['last_updated'] = datetime.now().isoformat()
        CACHE_PATH.write_text(json.dumps(data, indent=2))
        log("Registry cached successfully")
        
        return data
        
    except urllib.error.URLError as e:
        log(f"Failed to fetch registry: {e}", "ERROR")
        
        # Fallback to cache if available
        if CACHE_PATH.exists():
            log("Falling back to cached registry", "WARNING")
            return json.loads(CACHE_PATH.read_text())
        
        raise Exception(f"Failed to fetch registry and no cache available: {e}")


def list_skills(category: Optional[str] = None, installed_only: bool = False) -> List[Dict]:
    """
    List all available skills
    
    Args:
        category: Filter by category (e.g., 'UI/UX', 'Security')
        installed_only: Only show installed skills
        
    Returns:
        List of skill dictionaries with metadata
    """
    try:
        registry = fetch_registry()
        skills = registry.get('skills', [])
    except Exception as e:
        log(f"Failed to list skills: {e}", "ERROR")
        skills = []
    
    # Filter by category
    if category:
        skills = [s for s in skills if s.get('category') == category]
    
    # Add installation status
    installed = load_installed_skills()
    for skill in skills:
        skill_name = skill['name']
        skill['installed'] = skill_name in installed
        if skill['installed']:
            skill['installed_version'] = installed[skill_name].get('version', 'unknown')
    
    # Filter to installed only if requested
    if installed_only:
        skills = [s for s in skills if s['installed']]
    
    return skills


def search_skills(keyword: str) -> List[Dict]:
    """
    Search skills by keyword in name, description, or tags
    
    Args:
        keyword: Search term
        
    Returns:
        List of matching skill dictionaries
    """
    skills = list_skills()
    keyword_lower = keyword.lower()
    
    matching_skills = []
    for skill in skills:
        # Search in name
        if keyword_lower in skill.get('name', '').lower():
            matching_skills.append(skill)
            continue
        
        # Search in description
        if keyword_lower in skill.get('description', '').lower():
            matching_skills.append(skill)
            continue
        
        # Search in tags
        tags = skill.get('tags', [])
        if any(keyword_lower in tag.lower() for tag in tags):
            matching_skills.append(skill)
            continue
    
    return matching_skills


def get_skill_info(name: str) -> Optional[Dict]:
    """
    Get detailed information for a specific skill
    
    Args:
        name: Skill name
        
    Returns:
        Skill dictionary or None if not found
    """
    skills = list_skills()
    skill = next((s for s in skills if s['name'] == name), None)
    
    if not skill:
        # Check if it's installed but not in registry
        installed = load_installed_skills()
        if name in installed:
            return {
                'name': name,
                'installed': True,
                **installed[name]
            }
    
    return skill
