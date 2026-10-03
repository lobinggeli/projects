#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, KeepTogether)
from reportlab.pdfgen import canvas
import re

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        page_num = len(self._saved_page_states)
        if page_num > 1:  # Skip page number on cover
            self.setFont("Helvetica", 9)
            self.setFillColor(colors.HexColor('#666666'))
            self.drawRightString(7.5*inch, 0.5*inch, f"Page {page_num - 1}")
            self.drawString(1*inch, 0.5*inch, "Driver Poaching Playbook")

# Read markdown
with open('/Users/loicbinggeli/Github/MASTER/driver-poaching-playbook.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Clean content
content = re.sub(r'[^\x00-\x7F]+', ' ', content)

# Create PDF
pdf_file = '/Users/loicbinggeli/Github/MASTER/driver-poaching-playbook.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Custom Styles
styles = getSampleStyleSheet()

# Title Style
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#0066cc'),
    spaceAfter=20,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

# Subtitle Style
subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=16,
    textColor=colors.HexColor('#666666'),
    spaceAfter=40,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

# H1 Style
h1_style = ParagraphStyle(
    'CustomH1',
    parent=styles['Heading1'],
    fontSize=20,
    textColor=colors.HexColor('#0066cc'),
    spaceAfter=12,
    spaceBefore=20,
    fontName='Helvetica-Bold',
    borderWidth=0,
    borderColor=colors.HexColor('#0066cc'),
    borderPadding=0,
)

# H2 Style
h2_style = ParagraphStyle(
    'CustomH2',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#0066cc'),
    spaceAfter=10,
    spaceBefore=15,
    fontName='Helvetica-Bold'
)

# H3 Style
h3_style = ParagraphStyle(
    'CustomH3',
    parent=styles['Heading3'],
    fontSize=13,
    textColor=colors.HexColor('#333333'),
    spaceAfter=8,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

# H4 Style
h4_style = ParagraphStyle(
    'CustomH4',
    parent=styles['Heading4'],
    fontSize=11,
    textColor=colors.HexColor('#555555'),
    spaceAfter=6,
    spaceBefore=10,
    fontName='Helvetica-Bold'
)

# Body Style
body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#333333'),
    alignment=TA_JUSTIFY,
    spaceAfter=6
)

# Bullet Style
bullet_style = ParagraphStyle(
    'CustomBullet',
    parent=styles['Normal'],
    fontSize=10,
    leading=13,
    textColor=colors.HexColor('#333333'),
    leftIndent=20,
    spaceAfter=4
)

# Quote Style
quote_style = ParagraphStyle(
    'CustomQuote',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#0066cc'),
    leftIndent=20,
    rightIndent=20,
    spaceAfter=12,
    spaceBefore=8,
    fontName='Helvetica-Oblique',
    backColor=colors.HexColor('#f0f7ff'),
    borderWidth=1,
    borderColor=colors.HexColor('#0066cc'),
    borderPadding=10
)

# Highlight Style
highlight_style = ParagraphStyle(
    'CustomHighlight',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#333333'),
    fontName='Helvetica-Bold',
    spaceAfter=6
)

story = []

# Cover Page
story.append(Spacer(1, 2*inch))
story.append(Paragraph("Driver Poaching Playbook", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Tactical Guide to Recruiting Rideshare Drivers from Competition", subtitle_style))
story.append(Spacer(1, 1*inch))

cover_table_data = [
    ['Market Opportunity', '80% of Uber/Lyft drivers quit within a year'],
    ['Expected Cost', '$1,200-1,850 per driver'],
    ['Payback Period', '3-6 months'],
    ['Target Growth', '35-50% revenue increase']
]

cover_table = Table(cover_table_data, colWidths=[2.2*inch, 3.8*inch])
cover_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#0066cc')),
    ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#f0f7ff')),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
    ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#333333')),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 1, colors.white),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
]))

story.append(cover_table)
story.append(Spacer(1, 1*inch))
story.append(Paragraph("Version 1.0 | January 2026",
                      ParagraphStyle('CoverMeta', parent=styles['Normal'],
                                   fontSize=10, textColor=colors.HexColor('#999999'),
                                   alignment=TA_CENTER)))
story.append(Paragraph("Confidential - Internal Use Only",
                      ParagraphStyle('CoverConf', parent=styles['Normal'],
                                   fontSize=9, textColor=colors.HexColor('#999999'),
                                   alignment=TA_CENTER, spaceAfter=0)))

story.append(PageBreak())

# Process content
lines = content.split('\n')
i = 0
skip_until_first_h2 = True

while i < len(lines):
    line = lines[i].strip()
    i += 1

    if not line or line == '---':
        story.append(Spacer(1, 0.1*inch))
        continue

    # Skip the title and subtitle from markdown (we have custom cover)
    if line.startswith('# Driver Poaching Playbook'):
        continue
    if 'Tactical Guide to Recruiting' in line:
        continue

    try:
        # Main headings
        if line.startswith('## '):
            text = line[3:].strip()
            story.append(Spacer(1, 0.15*inch))
            p = Paragraph(text, h1_style)
            story.append(p)
            # Add colored line under H1
            line_table = Table([['']], colWidths=[6.5*inch])
            line_table.setStyle(TableStyle([
                ('LINEABOVE', (0, 0), (-1, -1), 2, colors.HexColor('#0066cc')),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ]))
            story.append(line_table)
            story.append(Spacer(1, 0.1*inch))

        elif line.startswith('### '):
            text = line[4:].strip()
            p = Paragraph(text, h2_style)
            story.append(p)

        elif line.startswith('#### '):
            text = line[5:].strip()
            p = Paragraph(text, h3_style)
            story.append(p)

        elif line.startswith('##### '):
            text = line[6:].strip()
            p = Paragraph(text, h4_style)
            story.append(p)

        # Bullet points
        elif line.startswith('- ') or line.startswith('* '):
            text = line[2:].strip()
            # Handle bold
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'`(.*?)`', r'<font face="Courier">\1</font>', text)
            p = Paragraph(f'<bullet>&bull;</bullet> {text}', bullet_style)
            story.append(p)

        # Blockquotes
        elif line.startswith('> '):
            text = line[2:].strip()
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            p = Paragraph(text, quote_style)
            story.append(p)

        # Tables (skip markdown tables, they're too complex)
        elif line.startswith('|'):
            continue

        # Regular paragraphs
        elif line and not line.startswith('#'):
            text = line
            # Handle markdown formatting
            text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
            text = re.sub(r'`(.*?)`', r'<font face="Courier">\1</font>', text)
            # Remove markdown links but keep text
            text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)

            # Check if this is a highlighted line
            if text.startswith('<b>') and text.endswith('</b>') and len(text) < 100:
                p = Paragraph(text, highlight_style)
            else:
                p = Paragraph(text, body_style)
            story.append(p)

    except Exception as e:
        # Skip problematic lines
        continue

# Build PDF
doc.build(story, canvasmaker=NumberedCanvas)
print("Professional PDF created successfully!")
print(f"Location: {pdf_file}")
