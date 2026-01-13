"""
Utility functions for Skill Manager
"""

import json
import hashlib
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, Tuple
from datetime import datetime
import time

from .config import LOG_PATH, INSTALLED_SKILLS_PATH


def log(message: str, level: str = "INFO"):
    """Log message to file and optionally print"""
    timestamp = datetime.now().isoformat()
    log_entry = f"{timestamp} [{level}] {message}\n"
    
    try:
        with open(LOG_PATH, 'a') as f:
            f.write(log_entry)
    except Exception:
        pass  # Fail silently if logging fails
    
    if level in ["ERROR", "WARNING"]:
        print(f"[{level}] {message}")


def load_installed_skills() -> Dict:
    """Load registry of installed skills"""
    if not INSTALLED_SKILLS_PATH.exists():
        return {}
    
    try:
        return json.loads(INSTALLED_SKILLS_PATH.read_text())
    except json.JSONDecodeError:
        log("Failed to parse installed-skills.json", "ERROR")
        return {}


def save_installed_skills(installed: Dict):
    """Save registry of installed skills"""
    INSTALLED_SKILLS_PATH.write_text(json.dumps(installed, indent=2))
    log("Updated installed skills registry")


def download_file(url: str, dest: Path, max_retries: int = 3) -> bool:
    """Download file with retry logic and exponential backoff"""
    for attempt in range(max_retries):
        try:
            log(f"Downloading {url} (attempt {attempt + 1}/{max_retries})")
            
            with urllib.request.urlopen(url, timeout=30) as response:
                dest.write_bytes(response.read())
            
            log(f"Downloaded to {dest}")
            return True
            
        except urllib.error.URLError as e:
            if attempt == max_retries - 1:
                log(f"Failed to download after {max_retries} attempts: {e}", "ERROR")
                return False
            
            wait_time = 2 ** attempt  # Exponential backoff
            log(f"Download failed, retrying in {wait_time}s...", "WARNING")
            time.sleep(wait_time)
    
    return False


def calculate_checksum(file_path: Path) -> str:
    """Calculate SHA-256 checksum of file"""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return f"sha256:{sha256.hexdigest()}"


def verify_checksum(file_path: Path, expected: str) -> bool:
    """Verify file checksum matches expected"""
    actual = calculate_checksum(file_path)
    return actual == expected


def compare_versions(v1: str, v2: str) -> int:
    """
    Compare semantic versions
    Returns: -1 if v1 < v2, 0 if equal, 1 if v1 > v2
    """
    def parse_version(v: str) -> Tuple[int, int, int]:
        parts = v.split('.')
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    
    try:
        ver1 = parse_version(v1)
        ver2 = parse_version(v2)
        
        if ver1 < ver2:
            return -1
        elif ver1 > ver2:
            return 1
        else:
            return 0
    except (ValueError, IndexError):
        log(f"Invalid version format: {v1} or {v2}", "WARNING")
        return 0


def parse_github_url(url: str) -> Dict:
    """Parse GitHub URL to extract owner, repo, branch"""
    import re
    
    # Handle different GitHub URL formats
    patterns = [
        r'github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$',  # https://github.com/owner/repo
        r'github\.com/([^/]+)/([^/]+)/tree/([^/]+)',   # https://github.com/owner/repo/tree/branch
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            owner = match.group(1)
            repo = match.group(2).replace('.git', '')
            branch = match.group(3) if len(match.groups()) > 2 else 'main'
            
            return {
                'owner': owner,
                'repo': repo,
                'branch': branch,
                'url': url
            }
    
    raise ValueError(f"Invalid GitHub URL: {url}")
