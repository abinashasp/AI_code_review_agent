import subprocess

def run_pylint(file_path):
    result = subprocess.run(
        ["pylint", file_path, "--output-format=text", "--score=n"],
        capture_output=True,
        text=True
    )
    output_lines = result.stdout.splitlines()

    
    issue_lines = [
        line for line in output_lines
        if line.startswith(file_path) or ": " in line
    ]

    return "\n".join(issue_lines) if issue_lines else "No issues found."
