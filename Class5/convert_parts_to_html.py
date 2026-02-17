#!/usr/bin/env python3
"""Convert all Class5 Part files to HTML with styling"""

import markdown

def convert_to_html(input_file, output_file, part_num, part_title):
    """Convert markdown to HTML with styling"""
    
    # Read markdown
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables', 'fenced_code', 'toc'])
    
    # Create full HTML with styling
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 5 – Part {part_num}: {part_title}</title>
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
        
        ul, ol {{
            margin-left: 25px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        strong {{
            font-weight: 600;
            color: #2c3e50;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        .nav-links {{
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }}
        
        .nav-links a {{
            margin: 0 10px;
            padding: 8px 15px;
            background-color: #3498db;
            color: white;
            border-radius: 4px;
            text-decoration: none;
            display: inline-block;
        }}
        
        .nav-links a:hover {{
            background-color: #2980b9;
        }}
        
        @media print {{
            body {{
                background-color: white;
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
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="nav-links">
            <a href="Class5_Part1.html">Part 1</a>
            <a href="Class5_Part2.html">Part 2</a>
            <a href="Class5_Part3.html">Part 3</a>
            <a href="Class5_Part4.html">Part 4</a>
            <a href="Class5_Part1_Notebook.ipynb">📓 Notebooks</a>
        </div>
{html_content}
    </div>
</body>
</html>"""
    
    # Write HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✓ Converted {input_file} → {output_file}")

# Convert all parts
parts = [
    ('Class5_Part1.md', 'Class5_Part1.html', 1, 'Fundamentals'),
    ('Class5_Part2.md', 'Class5_Part2.html', 2, 'Temporal Patterns & Decomposition'),
    ('Class5_Part3.md', 'Class5_Part3.html', 3, 'Advanced Techniques'),
    ('Class5_Part4.md', 'Class5_Part4.html', 4, 'Implementation & Applications'),
]

print("=" * 70)
print("Converting Class 5 Parts to HTML")
print("=" * 70)
print()

for md_file, html_file, part_num, title in parts:
    convert_to_html(md_file, html_file, part_num, title)

print()
print("=" * 70)
print("✅ All HTML files created successfully!")
print()
print("Files created:")
for _, html_file, _, _ in parts:
    print(f"  - {html_file}")
print()
print("Open any HTML file in your browser to view.")
