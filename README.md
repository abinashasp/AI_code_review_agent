# 🤖 AI Code Review Agent

The AI Code Review Agent is a Python-based tool that analyzes and improves Python codebases. It performs static code analysis, formatting, documentation, and generates detailed reports in Markdown, HTML, and PDF formats.

---

## 🚀 Features

- 🔍 **Static Analysis**:
  - ✅ `pylint` – syntax, convention, and style warnings
  - ✅ `radon` – cyclomatic complexity metrics
  - ✅ `bandit` – security vulnerability detection

- 🧹 **Code Improvement**:
  - ✅ Formats code using `black`
  - ✅ Adds placeholder docstrings to functions
  - ✅ Preserves project structure

- 📝 **Report Generation**:
  - ✅ Generates Markdown summary
  - ✅ Converts to HTML and PDF using `pdfkit + wkhtmltopdf`

---

## 📂 Input / Output

### Input:
- `.zip` archive of a Python codebase
- Or a folder path

### Output:
output/ # Improved codebase
reports/
├── report.md
├── report.html
└── report.pdf


---

## 📦 Technologies Used

| Task              | Tools Used                  |
|------------------|-----------------------------|
| Language          | Python 3.10+                |
| Linting           | pylint                      |
| Complexity        | radon                       |
| Security Audit    | bandit                      |
| Formatting        | black                       |
| Docstringing      | Custom logic                |
| Markdown → PDF    | markdown2 + pdfkit + wkhtmltopdf |
| CLI               | argparse                    |

---

## 🛠 Installation

### 1. Clone the repo

```bash
git clone https://github.com/abinashasp/ai-code-review-agent.git
cd ai-code-review-agent

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

3. Install Python dependencies

pip install -r requirements.txt

4. Install wkhtmltopdf (for PDF export)
Download from: https://wkhtmltopdf.org/downloads.html

Add path to wkhtmltopdf.exe in your system PATH
(e.g., C:\Program Files\wkhtmltopdf\bin)

▶️ Usage
Run the agent on a ZIP codebase
python main.py --input samples/test_project.zip --output output

Run on a folder
python main.py --input path/to/project/ --output output

🧠 Known Limitations
No dynamic performance profiling (e.g. runtime memory/CPU)

No web interface or CI/CD integration yet

Review config file support is planned (config.yaml)

Security fixes are not auto-applied (only reported)

✅ Completed Requirements (FRD)
Requirement	Status
Syntax, complexity, security scan	✅ Done
Code formatting & docstrings	✅ Done
Improved output folder	✅ Done
Markdown + HTML + PDF reports	✅ Done
CLI interface	✅ Done
Config, rollback, API integration	⚠️ Not yet (optional/future)

📬 Author
Abinash Panneer Selvam
GitHub: @abinashasp
Email: abinas.asp@gmail.com

📃 License
This project is open-source and intended for educational/demo use. All code reviews are performed locally and securely.