#!/usr/bin/env python3
"""Convert Class4.md to HTML with styling"""

import markdown

# Read the markdown file
with open('Class4.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert to HTML with extensions
html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables', 'fenced_code'])

# Create full HTML with styling
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 4 – Exploratory Data Visualization</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 15px;
            margin-bottom: 20px;
            font-size: 2.5em;
        }}
        
        h2 {{
            color: #2c3e50;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 2em;
            border-left: 5px solid #3498db;
            padding-left: 15px;
        }}
        
        h3 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.5em;
        }}
        
        h4 {{
            color: #555;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}
        
        p {{
            margin-bottom: 15px;
        }}
        
        ul, ol {{
            margin-left: 25px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
            color: #e83e8c;
        }}
        
        pre {{
            background-color: #282c34;
            color: #abb2bf;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
            line-height: 1.5;
        }}
        
        pre code {{
            background-color: transparent;
            color: inherit;
            padding: 0;
            font-size: 0.95em;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        
        th, td {{
            border: 1px solid #dee2e6;
            padding: 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #f8f9fa;
            font-weight: 600;
            color: #495057;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            color: #555;
            font-style: italic;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #e9ecef;
            margin: 40px 0;
        }}
        
        strong {{
            font-weight: 600;
            color: #2c3e50;
        }}
        
        em {{
            font-style: italic;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        @media print {{
            body {{
                background-color: white;
            }}
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
            pre {{
                page-break-inside: avoid;
            }}
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}
            h1 {{
                font-size: 2em;
            }}
            h2 {{
                font-size: 1.5em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
{html_content}
    </div>
</body>
</html>"""

# Write to file
with open('Class4.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Successfully converted Class4.md to Class4.html')
