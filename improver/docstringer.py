import os

def add_docstring_to_function(function_code: str, function_name: str) -> str:
    docstring = f'    """\n    TODO: Describe what {function_name} does.\n    """\n'
    lines = function_code.splitlines()
    if len(lines) > 1 and '"""' not in lines[1]:
        lines.insert(1, docstring)
    return "\n".join(lines)

def process_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    in_func = False
    func_name = ""
    func_block = []

    for line in lines:
        if line.strip().startswith("def "):
            in_func = True
            func_name = line.split("(")[0].split()[1]
            func_block = [line]
        elif in_func and line.startswith(" "):
            func_block.append(line)
        elif in_func:
            full_func = "".join(func_block)
            func_with_doc = add_docstring_to_function(full_func, func_name)
            new_lines.append(func_with_doc)
            new_lines.append(line)
            in_func = False
        else:
            new_lines.append(line)

    with open(file_path, "w") as f:
        f.writelines(new_lines)

def add_docstrings_to_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                process_file(os.path.join(root, file))
