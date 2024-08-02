from codemapper.traverser import read_ignore_file, traverse_repository
from codemapper.parser import extract_info

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
    code_map = {"files": []}

    for file_path in file_paths:
        file_info = extract_info(file_path)
        code_map["files"].append(file_info)

    return code_map

