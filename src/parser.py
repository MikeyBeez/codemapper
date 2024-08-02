import ast

def extract_info(file_path):
    """
    Extracts information from a Python file, including docstrings, function signatures,
    class names, and import statements.

    Args:
        file_path (str): The path to the Python file.

    Returns:
        dict: A dictionary containing the extracted information.
    """
    with open(file_path, 'r') as f:
        file_content = f.read()

    tree = ast.parse(file_content)
    file_info = {
        "path": file_path,
        "docstring": ast.get_docstring(tree),
        "functions": [],
        "classes": [],
        "imports": []
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            file_info["functions"].append({
                "name": node.name,
                "signature": ast.dump(node),
                "docstring": ast.get_docstring(node)
            })
        elif isinstance(node, ast.ClassDef):
            class_info = {
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "methods": []
            }
            for method in node.body:
                if isinstance(method, ast.FunctionDef):
                    class_info["methods"].append({
                        "name": method.name,
                        "signature": ast.dump(method),
                        "docstring": ast.get_docstring(method)
                    })
            file_info["classes"].append(class_info)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            file_info["imports"].append(ast.dump(node))

    return file_info

