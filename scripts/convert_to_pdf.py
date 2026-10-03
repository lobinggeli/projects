#!/usr/bin/env python3
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# Read the markdown file
with open('driver-poaching-playbook.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
md = markdown.Markdown(extensions=['tables', 'fenced_code', 'nl2br'])
html_content = md.convert(md_content)

# Create a complete HTML document with styling
html_doc = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Driver Poaching Playbook</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
            @bottom-right {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 9pt;
                color: #666;
            }}
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
            font-size: 11pt;
        }}
        h1 {{
            color: #1a1a1a;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 10px;
            margin-top: 30px;
            margin-bottom: 20px;
            font-size: 24pt;
            page-break-after: avoid;
        }}
        h2 {{
            color: #0066cc;
            margin-top: 25px;
            margin-bottom: 15px;
            font-size: 18pt;
            page-break-after: avoid;
        }}
        h3 {{
            color: #333;
            margin-top: 20px;
            margin-bottom: 12px;
            font-size: 14pt;
            page-break-after: avoid;
        }}
        h4 {{
            color: #555;
            margin-top: 15px;
            margin-bottom: 10px;
            font-size: 12pt;
        }}
        p {{
            margin-bottom: 10px;
            text-align: justify;
        }}
        ul, ol {{
            margin-bottom: 15px;
            padding-left: 25px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            font-size: 10pt;
            page-break-inside: avoid;
        }}
        th {{
            background-color: #0066cc;
            color: white;
            padding: 10px;
            text-align: left;
            font-weight: bold;
        }}
        td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        blockquote {{
            background-color: #f0f7ff;
            border-left: 4px solid #0066cc;
            padding: 12px 20px;
            margin: 15px 0;
            font-style: italic;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "Courier New", monospace;
            font-size: 10pt;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ddd;
            margin: 25px 0;
        }}
        strong {{
            color: #000;
            font-weight: 600;
        }}
        .page-break {{
            page-break-before: always;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
'''

# Configure fonts
font_config = FontConfiguration()

# Create PDF
HTML(string=html_doc).write_pdf(
    'driver-poaching-playbook.pdf',
    font_config=font_config
)

print("PDF created successfully: driver-poaching-playbook.pdf")
