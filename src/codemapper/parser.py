import ast
import os

def extract_info(file_path):
    """
    Extracts information from a file. For Python files, it includes docstrings, function signatures,
    class names, and import statements. For non-Python files, it includes basic file information.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing the extracted information.
    """
    file_info = {
        "path": file_path,
        "type": "unknown",
        "size": os.path.getsize(file_path)
    }

    # If it's a Python file, extract detailed information
    if file_path.endswith('.py'):
        file_info["type"] = "python"
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()

            tree = ast.parse(file_content)
            file_info["docstring"] = ast.get_docstring(tree)
            file_info["functions"] = []
            file_info["classes"] = []
            file_info["imports"] = []

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

        except Exception as e:
            print(f"Error processing Python file {file_path}: {str(e)}")
    else:
        # For non-Python files, just include the file extension as the type
        file_info["type"] = os.path.splitext(file_path)[1][1:] or "unknown"

    return file_info
