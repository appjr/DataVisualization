"""
Generate Jupyter notebooks from Class5 Part markdown files
Extracts code blocks and creates executable notebooks
"""

import json
import re
import os

def extract_code_and_text(md_file):
    """Extract code blocks and surrounding text from markdown"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cells = []
    
    # Split by code blocks
    parts = re.split(r'```python\n(.*?)```', content, flags=re.DOTALL)
    
    for i, part in enumerate(parts):
        if i % 2 == 0:
            # Text (markdown)
            if part.strip():
                # Clean up and create markdown cell
                text = part.strip()
                # Remove navigation links
                text = re.sub(r'\[.*?\]\(.*?\)', '', text)
                
                if text:
                    cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [text]
                    })
        else:
            # Code block
            if part.strip():
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [part]
                })
    
    return cells

def create_notebook(md_file, output_file, part_num):
    """Create Jupyter notebook from markdown file"""
    
    # Extract cells
    cells = extract_code_and_text(md_file)
    
    # Add title cell at the beginning
    title_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# Class 5 - Part {part_num}: Time Series & Temporal Visualization\n\n",
            "**MIS 6380 - Data Visualization**\n\n",
            f"This notebook contains all code examples from Part {part_num}.\n\n",
            "---\n"
        ]
    }
    
    cells.insert(0, title_cell)
    
    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    
    print(f"✓ Created {output_file}")
    print(f"  Cells: {len(cells)}")

# Generate notebooks for each part
parts = [
    ('Class5_Part1.md', 'Class5_Part1_Notebook.ipynb', 1),
    ('Class5_Part2.md', 'Class5_Part2_Notebook.ipynb', 2),
    ('Class5_Part3.md', 'Class5_Part3_Notebook.ipynb', 3),
    ('Class5_Part4.md', 'Class5_Part4_Notebook.ipynb', 4),
]

print("=" * 70)
print("Creating Jupyter Notebooks from Class 5 Parts")
print("=" * 70)
print()

for md_file, nb_file, part_num in parts:
    if os.path.exists(md_file):
        create_notebook(md_file, nb_file, part_num)
    else:
        print(f"✗ {md_file} not found")
    print()

print("=" * 70)
print("✅ Jupyter notebooks created successfully!")
print()
print("Files created:")
for _, nb_file, _ in parts:
    print(f"  - {nb_file}")
print()
print("To use: jupyter notebook in Class5 directory")
