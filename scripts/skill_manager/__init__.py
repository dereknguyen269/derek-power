"""
Skill Manager - Modular Python implementation
Manages D.E.R.E.K skills installation, updates, and discovery
"""

__version__ = "1.0.0"

from .registry import list_skills, search_skills, get_skill_info, fetch_registry
from .installer import install_skill_from_github, uninstall_skill
from .updater import check_updates, update_skill, update_all_skills
from .search import search_skill_database

__all__ = [
    'list_skills',
    'search_skills', 
    'get_skill_info',
    'fetch_registry',
    'install_skill_from_github',
    'uninstall_skill',
    'check_updates',
    'update_skill',
    'update_all_skills',
    'search_skill_database',
]
