import os
import zipfile
import shutil
import uuid

def prepare_input_folder(path):
    tmp_dir = f"input/{uuid.uuid4().hex[:8]}"
    os.makedirs(tmp_dir, exist_ok=True)

    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(tmp_dir)
    elif os.path.isdir(path):
        shutil.copytree(path, tmp_dir, dirs_exist_ok=True)
    else:
        raise ValueError("Invalid input: must be a .zip file or folder path")

    return tmp_dir


def get_python_files(folder):
    py_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files