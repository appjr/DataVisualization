#!/usr/bin/env python3
"""
Convert all Class6 markdown files to a single self-contained HTML file.
"""

import markdown
from pathlib import Path

# Read all markdown files in order
md_files = [
    'Class6_Part1.md',
    'Class6_Part2.md',
    'Class6_Part3.md',
    'Class6_Part4.md',
    'Class6_Exercises.md'
]

# Combine all markdown content
combined_md = ""
for md_file in md_files:
    file_path = Path(__file__).parent / md_file
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            combined_md += f.read() + "\n\n"
        print(f"Added: {md_file}")
    else:
        print(f"Warning: {md_file} not found")

# Convert to HTML with extensions
md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'toc'])
content_html = md.convert(combined_md)

# Create complete HTML document with styling
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 6 - Geospatial & Geographic Visualization - MIS 6380</title>
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
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 2.5em;
        }}
        
        h2 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 2em;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}
        
        h3 {{
            color: #555;
            margin-top: 25px;
            margin-bottom: 12px;
            font-size: 1.5em;
        }}
        
        h4 {{
            color: #666;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        code {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 3px;
            padding: 2px 6px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
        }}
        
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            margin-bottom: 20px;
        }}
        
        pre code {{
            background-color: transparent;
            border: none;
            padding: 0;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        
        td {{
            padding: 10px;
            border: 1px solid #ddd;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        tr:hover {{
            background-color: #f0f0f0;
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
            border-top: 2px solid #e0e0e0;
            margin: 30px 0;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        .toc {{
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        
        .toc h2 {{
            margin-top: 0;
            border-left: none;
            padding-left: 0;
        }}
        
        .highlight {{
            background-color: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin-bottom: 20px;
        }}
        
        .success {{
            background-color: #d4edda;
            padding: 15px;
            border-left: 4px solid #28a745;
            margin-bottom: 20px;
        }}
        
        .warning {{
            background-color: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin-bottom: 20px;
        }}
        
        .danger {{
            background-color: #f8d7da;
            padding: 15px;
            border-left: 4px solid #dc3545;
            margin-bottom: 20px;
        }}
        
        @media print {{
            body {{
                background-color: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 20px;
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
            
            table {{
                font-size: 0.9em;
            }}
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 8px;
        }}
        
        .header h1 {{
            color: white;
            border: none;
            margin-bottom: 10px;
        }}
        
        .nav-links {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }}
        
        .nav-links a {{
            margin: 0 15px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Class 6 – Geospatial & Geographic Visualization</h1>
            <p><strong>MIS 6380 - Data Visualization</strong></p>
            <p>Spring 2026</p>
        </div>
        
        {content_html}
        
        <hr>
        <footer style="text-align: center; color: #666; margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd;">
            <p>MIS 6380 - Data Visualization | Spring 2026 | University of Texas at Dallas</p>
            <p>Generated on: {Path(__file__).parent.name}</p>
        </footer>
    </div>
</body>
</html>
"""

# Write to file
output_path = Path(__file__).parent / 'Class6_Complete.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"\n✓ Successfully created: {output_path}")
print(f"✓ File size: {output_path.stat().st_size / 1024:.1f} KB")
