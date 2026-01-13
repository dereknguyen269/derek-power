"""
Configuration and constants for Skill Manager
"""

from pathlib import Path
from datetime import datetime

# Registry URL
REGISTRY_URL = "https://raw.githubusercontent.com/dereknguyen269/derek-power/refs/heads/main/registry.json"

# Directory paths
KIRO_DIR = Path.home() / ".kiro"
SHARED_DIR = Path.home() / ".shared"
CACHE_DIR = KIRO_DIR / "cache"
SKILLS_DIR = KIRO_DIR / "skills"
STEERING_DIR = KIRO_DIR / "steering"
BACKUP_DIR = KIRO_DIR / "backups"
LOG_DIR = KIRO_DIR / "logs"

# Ensure directories exist
for directory in [KIRO_DIR, SHARED_DIR, CACHE_DIR, SKILLS_DIR, STEERING_DIR, BACKUP_DIR, LOG_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# File paths
CACHE_PATH = CACHE_DIR / "registries.json"
INSTALLED_SKILLS_PATH = SKILLS_DIR / "installed-skills.json"
LOG_PATH = LOG_DIR / "skill-manager.log"

# Security patterns
MALICIOUS_PATTERNS = [
    r'eval\(',
    r'exec\(',
    r'__import__\(',
    r'subprocess\.',
    r'os\.system',
    r'open\(.+[\'"]w[\'"]',  # File writes
]

# Trusted domains
TRUSTED_DOMAINS = [
    'github.com',
    'raw.githubusercontent.com',
    'gitlab.com',
]

# Cache TTL (hours)
CACHE_TTL_HOURS = 24
