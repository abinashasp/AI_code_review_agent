import subprocess

def run_bandit(file_path):
    result = subprocess.run(["bandit", "-r", file_path], capture_output=True, text=True)
    return result.stdout
