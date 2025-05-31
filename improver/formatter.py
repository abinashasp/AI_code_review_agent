import subprocess
import shutil
import os

def format_with_black(file_path):
    subprocess.run(["black", file_path], capture_output=True)

def copy_and_format(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)

    
    for root, _, files in os.walk(dest_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                format_with_black(file_path)
