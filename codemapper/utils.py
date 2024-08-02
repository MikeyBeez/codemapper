import os
import sys
import pkg_resources
from .traverser import read_ignore_file, traverse_repository
from .parser import extract_info

def get_file_content(file_path, max_size=100 * 1024):  # 100 KB
    """
    Get the content of a file if it's smaller than max_size.
    
    Args:
        file_path (str): Path to the file.
        max_size (int): Maximum file size in bytes to read.
    
    Returns:
        str or None: File content if file is small enough, else None.
    """
    if os.path.getsize(file_path) <= max_size:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    return None

def get_version_info():
    """
    Get version information for the project and its dependencies.
    
    Returns:
        dict: Version information.
    """
    version_info = {
        'python': sys.version,
        'codemapper': pkg_resources.get_distribution('codemapper').version,
        'dependencies': {}
    }
    for dist in pkg_resources.working_set:
        version_info['dependencies'][dist.key] = dist.version
    return version_info

def is_config_file(file_path):
    """
    Check if a file is a configuration file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        bool: True if it's a config file, False otherwise.
    """
    config_extensions = ['.ini', '.cfg', '.conf', '.json', '.yaml', '.yml', '.toml']
    config_names = ['setup.py', 'requirements.txt', 'Pipfile', 'pyproject.toml']
    return (os.path.splitext(file_path)[1] in config_extensions or
            os.path.basename(file_path) in config_names)

def create_map(root_dir, ignore_file):
    """
    Creates a map of the code repository, including information about each file.

    Args:
        root_dir (str): The root directory of the repository.
        ignore_file (str): The path to the .ignore file.

    Returns:
        dict: A dictionary containing the map of the code repository.
    """
    ignore_patterns = read_ignore_file(ignore_file)
    file_paths = traverse_repository(root_dir, ignore_patterns)
    code_map = {
        "files": [],
        "version_info": get_version_info()
    }

    for file_path in file_paths:
        # Skip .gitignore file
        if os.path.basename(file_path) == '.gitignore':
            continue

        file_info = extract_info(file_path)
        if file_info is not None:
            # Include file content for README.md
            if os.path.basename(file_path).lower() == 'readme.md':
                file_info['content'] = get_file_content(file_path)
            
            # Include full content for configuration files
            elif is_config_file(file_path):
                file_info['content'] = get_file_content(file_path)
            
            # For other files, include content if they're small
            else:
                file_content = get_file_content(file_path)
                if file_content is not None:
                    file_info['content'] = file_content

            code_map["files"].append(file_info)

    return code_map
