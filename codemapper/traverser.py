import os
import fnmatch

def read_ignore_file(ignore_file):
    """
    Reads and parses the .ignore file to get a list of patterns to ignore.

    Args:
        ignore_file (str): The path to the .ignore file.

    Returns:
        list: A list of ignore patterns.
    """
    with open(ignore_file, 'r') as f:
        ignore_patterns = f.readlines()
    
    ignore_patterns = [pattern.strip() for pattern in ignore_patterns 
                       if pattern.strip() and not pattern.strip().startswith('#')]
    
    return ignore_patterns

def should_ignore(file_path, ignore_patterns, root_dir):
    """
    Checks if a file should be ignored based on the ignore patterns.

    Args:
        file_path (str): The path to the file.
        ignore_patterns (list): A list of ignore patterns.
        root_dir (str): The root directory of the repository.

    Returns:
        bool: True if the file should be ignored, False otherwise.
    """
    relative_path = os.path.relpath(file_path, root_dir)
    
    for pattern in ignore_patterns:
        if pattern.endswith('/'):
            if fnmatch.fnmatch(relative_path + '/', pattern) or \
               fnmatch.fnmatch(relative_path, pattern[:-1] + '/*'):
                return True
        elif fnmatch.fnmatch(relative_path, pattern):
            return True
    return False

def traverse_repository(root_dir, ignore_patterns):
    """
    Recursively traverses the repository directory, excluding files and directories
    mentioned in the ignore patterns.

    Args:
        root_dir (str): The root directory of the repository.
        ignore_patterns (list): A list of ignore patterns.

    Yields:
        str: The path to each file that should not be ignored.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not should_ignore(os.path.join(dirpath, d), ignore_patterns, root_dir)]
        
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not should_ignore(file_path, ignore_patterns, root_dir):
                yield file_path
