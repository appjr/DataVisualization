#!/usr/bin/env python3
"""
Convert all Class6 markdown files to a better formatted self-contained HTML file.
"""

from pathlib import Path
import re

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
            content = f.read()
            # Remove navigation links at top
            content = re.sub(r'\[Part \d+\]\(Class6_Part\d+\.md\).*?\n\n', '', content)
            # Remove separator lines that are just equals signs
            content = re.sub(r'^#+\s*═+\s*$', '', content, flags=re.MULTILINE)
            combined_md += content + "\n\n"
        print(f"Added: {md_file}")
    else:
        print(f"Warning: {md_file} not found")

# Simple markdown to HTML conversion
def convert_markdown_to_html(md_text):
    html = md_text
    
    # Headers (do in reverse order to avoid conflicts)
    html = re.sub(r'^####\s+(.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Code blocks
    html = re.sub(r'```python\n(.*?)\n```', r'<pre><code class="language-python">\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'```bash\n(.*?)\n```', r'<pre><code class="language-bash">\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'```(.*?)\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Bold and italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Horizontal rules
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    
    # Lists (simple version)
    lines = html.split('\n')
    in_list = False
    in_ordered = False
    result = []
    
    for line in lines:
        # Unordered list
        if re.match(r'^\s*[-*]\s+', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
                in_ordered = False
            item = re.sub(r'^\s*[-*]\s+', '', line)
            result.append(f'<li>{item}</li>')
        # Ordered list
        elif re.match(r'^\s*\d+\.\s+', line):
            if not in_list or not in_ordered:
                if in_list and not in_ordered:
                    result.append('</ul>')
                result.append('<ol>')
                in_list = True
                in_ordered = True
            item = re.sub(r'^\s*\d+\.\s+', '', line)
            result.append(f'<li>{item}</li>')
        else:
            if in_list:
                if in_ordered:
                    result.append('</ol>')
                else:
                    result.append('</ul>')
                in_list = False
                in_ordered = False
            result.append(line)
    
    if in_list:
        if in_ordered:
            result.append('</ol>')
        else:
            result.append('</ul>')
    
    html = '\n'.join(result)
    
    # Paragraphs (wrap non-tag lines)
    lines = html.split('\n')
    result = []
    in_para = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_para:
                result.append('</p>')
                in_para = False
            result.append('')
        elif stripped.startswith('<') and (
            stripped.startswith('<h') or 
            stripped.startswith('<pre') or 
            stripped.startswith('<ul') or 
            stripped.startswith('<ol') or 
            stripped.startswith('<hr') or
            stripped.startswith('</') or
            stripped.startswith('<li')
        ):
            if in_para:
                result.append('</p>')
                in_para = False
            result.append(line)
        else:
            if not in_para:
                result.append('<p>')
                in_para = True
            result.append(line)
    
    if in_para:
        result.append('</p>')
    
    return '\n'.join(result)

# Convert markdown to HTML
content_html = convert_markdown_to_html(combined_md)

# Create complete HTML document
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
            line-height: 1.8;
            color: #333;
            background: linear-gradient(to bottom, #f0f4f8 0%, #ffffff 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background-color: white;
            padding: 60px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border-radius: 12px;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 50px;
            padding: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        }}
        
        .header h1 {{
            color: white;
            font-size: 3em;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.95;
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 15px;
            margin: 50px 0 25px 0;
            font-size: 2.5em;
            page-break-after: avoid;
        }}
        
        h2 {{
            color: #34495e;
            margin: 40px 0 20px 0;
            font-size: 2em;
            border-left: 5px solid #3498db;
            padding-left: 20px;
            page-break-after: avoid;
        }}
        
        h3 {{
            color: #555;
            margin: 30px 0 15px 0;
            font-size: 1.6em;
            page-break-after: avoid;
        }}
        
        h4 {{
            color: #666;
            margin: 25px 0 12px 0;
            font-size: 1.3em;
            page-break-after: avoid;
        }}
        
        p {{
            margin-bottom: 20px;
            line-height: 1.8;
            text-align: justify;
        }}
        
        ul, ol {{
            margin: 15px 0 20px 40px;
            line-height: 1.8;
        }}
        
        li {{
            margin-bottom: 10px;
        }}
        
        code {{
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 3px 8px;
            font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
            font-size: 0.9em;
            color: #c7254e;
        }}
        
        pre {{
            background-color: #282c34;
            color: #abb2bf;
            border-radius: 8px;
            padding: 20px;
            overflow-x: auto;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            page-break-inside: avoid;
        }}
        
        pre code {{
            background-color: transparent;
            border: none;
            padding: 0;
            color: #abb2bf;
            font-size: 0.95em;
            line-height: 1.6;
        }}
        
        hr {{
            border: none;
            border-top: 3px solid #e0e0e0;
            margin: 40px 0;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }}
        
        a:hover {{
            border-bottom: 1px solid #3498db;
        }}
        
        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}
        
        em {{
            color: #555;
        }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
            
            .header {{
                background: #667eea !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}
            
            h1, h2, h3, h4 {{
                page-break-after: avoid;
            }}
            
            pre, blockquote {{
                page-break-inside: avoid;
            }}
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 30px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            h1 {{
                font-size: 2em;
            }}
            
            h2 {{
                font-size: 1.6em;
            }}
        }}
        
        footer {{
            text-align: center;
            color: #999;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 2px solid #e0e0e0;
            font-size: 0.95em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Class 6 – Geospatial & Geographic Visualization</h1>
            <p><strong>MIS 6380 - Data Visualization</strong></p>
            <p>Spring 2026 | University of Texas at Dallas</p>
        </div>
        
        {content_html}
        
        <footer>
            <p><strong>MIS 6380 - Data Visualization</strong> | Spring 2026 | University of Texas at Dallas</p>
            <p>Complete Course Materials - All Parts Combined</p>
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
print(f"✓ Open in browser to view")
