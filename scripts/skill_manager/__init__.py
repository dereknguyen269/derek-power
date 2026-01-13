"""
Skill Manager for D.E.R.E.K Power
Handles installation, discovery, and management of skills
"""

from .installer import install_skill_from_github, uninstall_skill
from .registry import list_skills, search_skills, get_skill_info
from .updater import check_updates, update_skill, update_all_skills

__all__ = [
    'install_skill_from_github',
    'uninstall_skill',
    'list_skills',
    'search_skills',
    'get_skill_info',
    'check_updates',
    'update_skill',
    'update_all_skills',
]
