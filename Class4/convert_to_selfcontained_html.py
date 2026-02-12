#!/usr/bin/env python3
"""Convert Class4.md to self-contained HTML with embedded images"""

import markdown
import base64
import re
import os

def image_to_base64(image_path):
    """Convert an image file to base64 data URI"""
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            
            # Determine image type from extension
            ext = os.path.splitext(image_path)[1].lower()
            mime_types = {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.gif': 'image/gif',
                '.svg': 'image/svg+xml'
            }
            mime_type = mime_types.get(ext, 'image/png')
            
            return f"data:{mime_type};base64,{b64_data}"
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return image_path  # Return original path if conversion fails

# Read the markdown file
with open('Class4.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Find all image references and convert to base64
image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
images_found = re.findall(image_pattern, md_content)

print(f"Found {len(images_found)} images to embed...")

# Replace each image path with base64 data URI
for alt_text, img_path in images_found:
    if os.path.exists(img_path):
        print(f"  Embedding: {img_path}")
        base64_uri = image_to_base64(img_path)
        # Replace in markdown content
        md_content = md_content.replace(f']({img_path})', f']({base64_uri})')
    else:
        print(f"  Warning: {img_path} not found")

# Convert to HTML with extensions
html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables', 'fenced_code'])

# Create full HTML with styling
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 4 – Exploratory Data Visualization (Self-Contained)</title>
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
        
        .info-banner {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
            text-align: center;
            font-weight: 600;
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
            .info-banner {{
                display: none;
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
        <div class="info-banner">
            📦 Self-Contained HTML - All images embedded (no external files needed)
        </div>
{html_content}
    </div>
</body>
</html>"""

# Write to file
output_file = 'Class4_SelfContained.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f'\nSuccessfully created {output_file}')
print(f'File size: {len(full_html) / 1024 / 1024:.2f} MB')
print('This HTML file contains all images embedded and works standalone!')
