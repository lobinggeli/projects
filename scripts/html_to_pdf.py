#!/usr/bin/env python3
from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    def header(self):
        # No header on first page (cover page)
        if self.page_no() > 1:
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, 'Driver Poaching Playbook', 0, 0, 'L')
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'R')
            self.ln(15)

# Read HTML file
with open('driver-poaching-playbook.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

try:
    pdf.write_html(html_content)
    pdf.output('driver-poaching-playbook.pdf')
    print("PDF created successfully: driver-poaching-playbook.pdf")
except Exception as e:
    print(f"Error creating PDF: {e}")
    print("\nTrying alternative method...")

    # If HTML parsing fails, create a simpler PDF from markdown
    import re

    # Read markdown instead
    with open('driver-poaching-playbook.md', 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Create new PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 11)

    # Simple conversion of markdown to text
    lines = md_content.split('\n')

    for line in lines:
        if line.startswith('# '):
            pdf.set_font('Arial', 'B', 18)
            pdf.ln(5)
            pdf.multi_cell(0, 10, line[2:])
            pdf.ln(3)
            pdf.set_font('Arial', '', 11)
        elif line.startswith('## '):
            pdf.set_font('Arial', 'B', 14)
            pdf.ln(4)
            pdf.multi_cell(0, 8, line[3:])
            pdf.ln(2)
            pdf.set_font('Arial', '', 11)
        elif line.startswith('### '):
            pdf.set_font('Arial', 'B', 12)
            pdf.ln(3)
            pdf.multi_cell(0, 7, line[4:])
            pdf.ln(1)
            pdf.set_font('Arial', '', 11)
        elif line.startswith('#### '):
            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(0, 6, line[5:])
            pdf.set_font('Arial', '', 11)
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            pdf.multi_cell(0, 5, '  • ' + line.strip()[2:])
        elif line.strip().startswith('**') and line.strip().endswith('**'):
            pdf.set_font('Arial', 'B', 11)
            pdf.multi_cell(0, 5, line.strip()[2:-2])
            pdf.set_font('Arial', '', 11)
        elif line.strip():
            # Clean up markdown formatting
            clean_line = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
            clean_line = re.sub(r'\*(.*?)\*', r'\1', clean_line)
            clean_line = re.sub(r'`(.*?)`', r'\1', clean_line)
            pdf.multi_cell(0, 5, clean_line)
        else:
            pdf.ln(2)

    pdf.output('driver-poaching-playbook.pdf')
    print("PDF created successfully from markdown: driver-poaching-playbook.pdf")
