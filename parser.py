import ast

def extract_functions(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions
