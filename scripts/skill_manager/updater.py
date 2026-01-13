"""
Update functions for Skill Manager
Handles checking for and installing skill updates
"""

from typing import List, Dict
from .utils import log, load_installed_skills, compare_versions
from .registry import list_skills
from .installer import install_skill_from_github


def check_updates() -> List[Dict]:
    """
    Check for available updates for installed skills
    
    Returns:
        List of update info dictionaries
    """
    installed = load_installed_skills()
    registry_skills = list_skills()
    updates = []
    
    for name, info in installed.items():
        # Find skill in registry
        registry_skill = next((s for s in registry_skills if s['name'] == name), None)
        
        if registry_skill:
            current_version = info.get('version', '0.0.0')
            latest_version = registry_skill.get('version', '0.0.0')
            
            # Compare versions
            if compare_versions(current_version, latest_version) < 0:
                updates.append({
                    'name': name,
                    'current_version': current_version,
                    'latest_version': latest_version,
                    'download_url': registry_skill.get('download_url'),
                    'changelog': registry_skill.get('changelog_url')
                })
                log(f"Update available: {name} {current_version} → {latest_version}")
    
    return updates


def update_skill(skill_name: str) -> Dict:
    """
    Update a specific skill to the latest version
    
    Args:
        skill_name: Name of skill to update
        
    Returns:
        Result dictionary with success status and message
    """
    installed = load_installed_skills()
    
    if skill_name not in installed:
        return {
            'success': False,
            'message': f"Skill '{skill_name}' is not installed"
        }
    
    # Check if update is available
    updates = check_updates()
    update_info = next((u for u in updates if u['name'] == skill_name), None)
    
    if not update_info:
        return {
            'success': False,
            'message': f"No updates available for {skill_name}"
        }
    
    log(f"Updating {skill_name} from {update_info['current_version']} to {update_info['latest_version']}")
    
    # Get source URL from installed info
    source_url = installed[skill_name].get('source')
    if not source_url:
        # Try to get from registry
        source_url = update_info.get('download_url')
    
    if not source_url:
        return {
            'success': False,
            'message': f"No source URL found for {skill_name}"
        }
    
    # Use install with force=True to update
    result = install_skill_from_github(source_url, force=True)
    
    if result['success']:
        result['message'] = f"✅ Updated {skill_name} from {update_info['current_version']} to {update_info['latest_version']}"
        log(f"Successfully updated {skill_name}")
    
    return result


def update_all_skills() -> List[Dict]:
    """
    Update all skills with available updates
    
    Returns:
        List of update result dictionaries
    """
    updates = check_updates()
    results = []
    
    if not updates:
        log("No updates available")
        return [{
            'success': True,
            'message': "All skills are up to date"
        }]
    
    log(f"Updating {len(updates)} skill(s)")
    
    for update_info in updates:
        result = update_skill(update_info['name'])
        results.append(result)
    
    return results
