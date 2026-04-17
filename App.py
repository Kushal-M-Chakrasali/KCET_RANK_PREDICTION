import pdfplumber
import csv

pdf_path = "ENGG_CUTOFF_2023_GENkannada.pdf"
csv_path = "kcet_cutoff_output.csv"

rows = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()

        if text:
            lines = text.split("\n")
            for line in lines:
                row = line.split()
                rows.append(row)

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("CSV file created successfully!")
