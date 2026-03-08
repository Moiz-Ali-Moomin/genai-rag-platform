import sys
import subprocess

try:
    from fpdf import FPDF
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf"])
    from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)
pdf.cell(200, 10, txt="Abraham Lincoln: Quick Facts", ln=1, align='C')

pdf.set_font("Arial", size=12)
facts = [
    "",
    "Abraham Lincoln was the 16th president of the United States, serving from 1861 to 1865.",
    "He successfully led the country through the American Civil War, preserving the Union.",
    "Lincoln wrote and issued the Emancipation Proclamation, which began the process of freedom for America's slaves.",
    "He delivered the Gettysburg Address, one of the most famous speeches in American history.",
    "Lincoln was largely self-educated and became a lawyer, state legislator, and congressman.",
    "He was the first U.S. president to be assassinated, killed by John Wilkes Booth in April 1865.",
    "Lincoln is consistently ranked by scholars and the public as one of the greatest U.S. presidents."
]

for fact in facts:
    pdf.multi_cell(0, 10, txt=fact)

pdf.output("abraham_lincoln.pdf")
print("PDF created successfully: abraham_lincoln.pdf")
