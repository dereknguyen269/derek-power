"""
Search functions for Skill Manager
Executes skill-specific searches in their databases
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Optional

from .config import SHARED_DIR, SKILLS_DIR
from .utils import log, load_installed_skills


def search_skill_database(skill_name: str, query: str, limit: int = 10) -> Dict:
    """
    Search a skill's database
    
    Args:
        skill_name: Name of skill to search
        query: Search query string
        limit: Maximum number of results
        
    Returns:
        Result dictionary with success status and results
    """
    installed = load_installed_skills()
    
    if skill_name not in installed:
        return {
            'success': False,
            'message': f"Skill '{skill_name}' is not installed"
        }
    
    # Check if skill has search capability
    skill_dir = SHARED_DIR / skill_name
    if not skill_dir.exists():
        return {
            'success': False,
            'message': f"Skill '{skill_name}' has no data directory"
        }
    
    # Look for search script
    search_script = skill_dir / 'search.py'
    
    if search_script.exists():
        # Execute custom search script
        log(f"Using custom search script for {skill_name}")
        results = execute_search_script(search_script, query, skill_dir, limit)
    else:
        # Use built-in search
        log(f"Using built-in search for {skill_name}")
        results = builtin_search(skill_dir, query, limit)
    
    return {
        'success': True,
        'skill_name': skill_name,
        'query': query,
        'results': results,
        'count': len(results)
    }


def execute_search_script(script_path: Path, query: str, data_dir: Path, limit: int) -> List[Dict]:
    """
    Execute skill's search.py script safely
    
    Args:
        script_path: Path to search.py
        query: Search query
        data_dir: Path to skill's data directory
        limit: Maximum results
        
    Returns:
        List of result dictionaries
    """
    try:
        # Find all database files (JSON files)
        database_files = [str(f) for f in data_dir.glob('*.json') if f.name != 'config.json']
        
        # Create restricted globals for sandboxed execution
        safe_globals = {
            '__builtins__': {
                'len': len,
                'str': str,
                'int': int,
                'float': float,
                'bool': bool,
                'list': list,
                'dict': dict,
                'tuple': tuple,
                'set': set,
                'range': range,
                'enumerate': enumerate,
                'zip': zip,
                'sorted': sorted,
                'min': min,
                'max': max,
                'sum': sum,
                'any': any,
                'all': all,
                'abs': abs,
                'round': round,
            },
            'json': json,
            're': re,
            'Path': Path,
        }
        
        # Load and execute script
        code = compile(script_path.read_text(), str(script_path), 'exec')
        exec(code, safe_globals)
        
        # Call search function
        search_func = safe_globals.get('search')
        if not search_func:
            log("Search script missing search() function", "WARNING")
            return builtin_search(data_dir, query, limit)
        
        # Execute search
        results = search_func(query, database_files, limit)
        
        return results if results else []
        
    except Exception as e:
        log(f"Search script execution failed: {e}", "ERROR")
        # Fallback to built-in search
        return builtin_search(data_dir, query, limit)


def builtin_search(data_dir: Path, query: str, limit: int) -> List[Dict]:
    """
    Built-in fuzzy search across JSON databases
    
    Args:
        data_dir: Path to skill's data directory
        query: Search query
        limit: Maximum results
        
    Returns:
        List of result dictionaries
    """
    results = []
    query_lower = query.lower()
    
    # Search all JSON files
    for json_file in data_dir.glob('*.json'):
        if json_file.name == 'config.json':
            continue
        
        try:
            data = json.loads(json_file.read_text())
            
            # Handle different JSON structures
            if isinstance(data, list):
                items = data
            elif isinstance(data, dict):
                # Try common keys for lists
                items = data.get('items', data.get('data', data.get('entries', [data])))
            else:
                continue
            
            # Search each item
            for item in items:
                if not isinstance(item, dict):
                    continue
                
                # Search in all string values
                match_score = 0
                matched_fields = []
                
                for key, value in item.items():
                    if isinstance(value, str) and query_lower in value.lower():
                        match_score += 1
                        matched_fields.append(key)
                
                if match_score > 0:
                    results.append({
                        'title': item.get('title', item.get('name', item.get('id', 'Untitled'))),
                        'description': item.get('description', item.get('summary', ''))[:200],
                        'data': item,
                        'source': json_file.name,
                        'score': match_score,
                        'matched_fields': matched_fields
                    })
        
        except Exception as e:
            log(f"Failed to search {json_file}: {e}", "WARNING")
            continue
    
    # Sort by score and limit
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:limit]
