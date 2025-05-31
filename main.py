import argparse 
from utils.file_utils import prepare_input_folder, get_python_files
from analyzer.syntax_checker import run_pylint
from analyzer.complexity_checker import run_radon
from analyzer.security_checker import run_bandit
from improver.formatter import copy_and_format
from improver.docstringer import add_docstrings_to_folder
from reporter.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("--input", required=True, help="Path to input ZIP or folder")
    parser.add_argument("--output", default="output", help="Path to store improved code")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    
    source_dir = prepare_input_folder(input_path)
    print(f"[✓] Input prepared at: {source_dir}")

    
    python_files = get_python_files(source_dir)
    results = {}

    for file in python_files:
        print(f"\n Analyzing {file}")
        pylint_output = run_pylint(file)
        radon_output = run_radon(file)
        bandit_output = run_bandit(file)

        print(" Pylint:")
        print(pylint_output)

        print(" Complexity (Radon):")
        print(radon_output)

        print(" Security (Bandit):")
        print(bandit_output)

        results[file] = {
            "pylint": pylint_output,
            "radon": radon_output,
            "bandit": bandit_output
        }

    
    print("\n Improving Code and Copying to Output Folder...")
    copy_and_format(source_dir, output_path)
    print(f"[✓] Improved code saved to: {output_path}")

    
    print(" Adding Docstrings...")
    add_docstrings_to_folder(output_path)
    print("[✓] Docstrings added to improved files.")

    
    print(" Generating Report...")
    generate_report(results)
    print("[✓] Report generated successfully.")

if __name__ == "__main__":
    main()
