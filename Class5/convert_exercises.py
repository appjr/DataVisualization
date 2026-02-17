#!/usr/bin/env python3
"""Convert Class5_Exercises.md to HTML and Jupyter notebook"""

import markdown
import json
import re

# Convert to HTML
print("Converting to HTML...")
with open('Class5_Exercises.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables', 'fenced_code'])

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Class 5 - Exercises</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; max-width: 1200px; margin: 20px auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; border-bottom: 4px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 30px; border-left: 5px solid #3498db; padding-left: 15px; }}
        h3 {{ color: #555; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; color: #e83e8c; }}
        pre {{ background: #282c34; color: #abb2bf; padding: 20px; border-radius: 5px; overflow-x: auto; }}
        pre code {{ background: transparent; color: inherit; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background: #f8f9fa; font-weight: 600; }}
        tr:nth-child(even) {{ background: #f8f9fa; }}
        ul {{ margin-left: 20px; }}
        li {{ margin: 8px 0; }}
        .nav {{ background: #ecf0f1; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="nav">
        <a href="Class5_Part1.html">Part 1</a> |
        <a href="Class5_Part2.html">Part 2</a> |
        <a href="Class5_Part3.html">Part 3</a> |
        <a href="Class5_Part4.html">Part 4</a> |
        <strong>Exercises</strong>
    </div>
{html_body}
</body>
</html>"""

with open('Class5_Exercises.html', 'w', encoding='utf-8') as f:
    f.write(html_full)

print("✓ Created Class5_Exercises.html")

# Convert to notebook
print("\nConverting to Jupyter notebook...")
parts = re.split(r'```python\n(.*?)```', md_content, flags=re.DOTALL)

cells = [{
    'cell_type': 'markdown',
    'metadata': {},
    'source': ['# Class 5 - Exercises\n\nTime Series & Temporal Visualization\n\nMIS 6380 - Data Visualization\n\n---\n']
}]

for i, part in enumerate(parts):
    if i % 2 == 0 and part.strip():
        cells.append({
            'cell_type': 'markdown',
            'metadata': {},
            'source': [part.strip()]
        })
    elif i % 2 == 1 and part.strip():
        cells.append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': [part]
        })

notebook = {
    'cells': cells,
    'metadata': {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        }
    },
    'nbformat': 4,
    'nbformat_minor': 4
}

with open('Class5_Exercises.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print(f"✓ Created Class5_Exercises.ipynb")
print(f"  Total cells: {len(cells)}")
print(f"\n✅ Both files created successfully!")
