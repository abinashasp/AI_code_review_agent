import os
import markdown2
import pdfkit

def generate_report(results, output_folder="reports", output_file="report.md"):
    os.makedirs(output_folder, exist_ok=True)

    md_path = os.path.join(output_folder, output_file)
    html_path = os.path.join(output_folder, "report.html")
    pdf_path = os.path.join(output_folder, "report.pdf")

    
    with open(md_path, "w", encoding="utf-8") as report:
        report.write("# AI Code Review Report\n\n")

        for file, data in results.items():
            clean_path = file.replace("\\", "/")  
            report.write(f"## File: `{clean_path}`\n\n")

            if data.get("pylint"):
                report.write("### Pylint Output\n")
                report.write("```\n" + data["pylint"] + "\n```\n")

            if data.get("radon"):
                report.write("### Radon Output\n")
                report.write("```\n" + data["radon"] + "\n```\n")

            if data.get("bandit"):
                report.write("### Bandit Output\n")
                report.write("```\n" + data["bandit"] + "\n```\n")

        report.write("\n---\n✔ Code formatted with Black.\n✔ Docstrings added to functions.\n")

    print(f"[✓] Markdown report generated at: {md_path}")

    
    with open(md_path, "r", encoding="utf-8") as md_file:
        html = markdown2.markdown(md_file.read())
        with open(html_path, "w", encoding="utf-8") as html_file:
            html_file.write(html)

    print(f"[✓] HTML report generated at: {html_path}")

    
    try:
        path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_file(html_path, pdf_path, configuration=config)
        print(f"[✓] PDF report generated at: {pdf_path}")
    except Exception as e:
        print(f"[!] PDF generation failed: {e}")
