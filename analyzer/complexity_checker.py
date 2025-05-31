import subprocess

def run_radon(file_path):
    result = subprocess.run(["radon", "cc", file_path, "-a"], capture_output=True, text=True)
    return result.stdout
