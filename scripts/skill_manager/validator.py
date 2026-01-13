"""
Validation functions for Skill Manager
Validates manifests, checksums, and scans for security issues
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Optional

from .config import MALICIOUS_PATTERNS
from .utils import log, verify_checksum


def validate_manifest(manifest: Dict) -> bool:
    """
    Validate skill manifest against schema
    
    Args:
        manifest: Manifest dictionary to validate
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If validation fails
    """
    # Check required fields
    required_fields = ['name', 'version', 'description', 'author', 'category', 'files']
    
    for field in required_fields:
        if field not in manifest:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate name format (lowercase, alphanumeric, hyphens only)
    if not re.match(r'^[a-z0-9-]+$', manifest['name']):
        raise ValueError(f"Invalid name format: {manifest['name']}. Use lowercase, numbers, and hyphens only")
    
    # Validate version format (semantic versioning)
    if not re.match(r'^\d+\.\d+\.\d+$', manifest['version']):
        raise ValueError(f"Invalid version format: {manifest['version']}. Use semantic versioning (e.g., 1.0.0)")
    
    # Validate category
    valid_categories = [
        'UI/UX', 'Security', 'Performance', 'API Design', 
        'Database', 'Testing', 'DevOps', 'Documentation', 'Other'
    ]
    if manifest['category'] not in valid_categories:
        raise ValueError(f"Invalid category: {manifest['category']}. Must be one of: {', '.join(valid_categories)}")
    
    # Validate description length
    desc = manifest['description']
    if len(desc) < 10:
        raise ValueError("Description too short (minimum 10 characters)")
    if len(desc) > 500:
        raise ValueError("Description too long (maximum 500 characters)")
    
    # Validate files structure
    if not isinstance(manifest['files'], dict):
        raise ValueError("'files' must be a dictionary")
    
    log(f"Manifest validation passed for {manifest['name']}")
    return True


def scan_for_malicious_patterns(file_path: Path) -> List[str]:
    """
    Scan file for potentially malicious code patterns
    
    Args:
        file_path: Path to file to scan
        
    Returns:
        List of issues found (empty if clean)
    """
    issues = []
    
    try:
        content = file_path.read_text()
        
        for pattern in MALICIOUS_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                issues.append(f"Potentially dangerous pattern '{pattern}' found in {file_path.name}")
                log(f"Security warning: {pattern} found in {file_path}", "WARNING")
        
    except Exception as e:
        log(f"Failed to scan {file_path}: {e}", "ERROR")
    
    return issues


def validate_source(url: str, trusted_domains: List[str]) -> bool:
    """
    Check if source URL is from a trusted domain
    
    Args:
        url: URL to validate
        trusted_domains: List of trusted domain names
        
    Returns:
        True if trusted, False otherwise
    """
    from urllib.parse import urlparse
    
    parsed = urlparse(url)
    domain = parsed.netloc
    
    # Check if domain matches any trusted domain
    for trusted in trusted_domains:
        if domain == trusted or domain.endswith('.' + trusted):
            return True
    
    log(f"Untrusted source: {url}", "WARNING")
    return False
