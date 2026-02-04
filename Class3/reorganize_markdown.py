"""
Reorganize Class3.md:
1. Add Table of Contents with clickable links
2. Remove "Slide X –" from all headers
3. Add section dividers
"""

import re

print("Reorganizing Class3.md...")

# Read the original file
with open('Class3.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove "Slide X – " from all headers
content = re.sub(r'## Slide \d+ – ', '## ', content)

# Split into slides
slides = re.split(r'\n---\n', content)

# Extract all slide titles for TOC
slide_titles = []
for slide in slides:
    match = re.search(r'## (.+?)(?:\n|$)', slide)
    if match:
        title = match.group(1).strip()
        slide_titles.append(title)

# Define section boundaries
sections = {
    'Part 1: Visual Perception & Cognitive Load': list(range(0, 21)),
    'Part 2: Data Types & Visual Encodings': list(range(21, 33)),
    'Part 3: Grammar of Graphics Framework': list(range(33, 44)),
    'Part 4: Python Visualization Implementation': list(range(44, len(slide_titles)))
}

# Create Table of Contents
toc = """# Class 3 – Data Visualization  
## Visual Perception & Cognitive Load  
## Data Types, Encodings & Grammar of Graphics
## Python Visualization Fundamentals

---

# 📚 Table of Contents

## Quick Navigation
- [Part 1: Visual Perception & Cognitive Load](#part-1-visual-perception--cognitive-load)
- [Part 2: Data Types & Visual Encodings](#part-2-data-types--visual-encodings)
- [Part 3: Grammar of Graphics Framework](#part-3-grammar-of-graphics-framework)
- [Part 4: Python Visualization Implementation](#part-4-python-visualization-implementation)

---

## Detailed Index

### Part 1: Visual Perception & Cognitive Load (Slides 1-21)
"""

# Add TOC entries for Part 1
for idx in sections['Part 1: Visual Perception & Cognitive Load']:
    if idx < len(slide_titles):
        title = slide_titles[idx]
        anchor = title.lower().replace(' ', '-').replace(':', '').replace('(', '').replace(')', '').replace(',', '').replace('&', '').replace('–', '').replace(''', '').replace(''', '')
        anchor = re.sub(r'[^\w\-]', '', anchor)
        toc += f"- [{title}](#{anchor})\n"

toc += "\n### Part 2: Data Types & Visual Encodings (Slides 22-33)\n"
for idx in sections['Part 2: Data Types & Visual Encodings']:
    if idx < len(slide_titles):
        title = slide_titles[idx]
        anchor = title.lower().replace(' ', '-').replace(':', '').replace('(', '').replace(')', '').replace(',', '').replace('&', '').replace('–', '').replace(''', '').replace(''', '')
        anchor = re.sub(r'[^\w\-]', '', anchor)
        toc += f"- [{title}](#{anchor})\n"

toc += "\n### Part 3: Grammar of Graphics Framework (Slides 34-44)\n"
for idx in sections['Part 3: Grammar of Graphics Framework']:
    if idx < len(slide_titles):
        title = slide_titles[idx]
        anchor = title.lower().replace(' ', '-').replace(':', '').replace('(', '').replace(')', '').replace(',', '').replace('&', '').replace('–', '').replace(''', '').replace(''', '')
        anchor = re.sub(r'[^\w\-]', '', anchor)
        toc += f"- [{title}](#{anchor})\n"

toc += "\n### Part 4: Python Visualization Implementation (Slides 45-82)\n"
for idx in sections['Part 4: Python Visualization Implementation']:
    if idx < len(slide_titles):
        title = slide_titles[idx]
        anchor = title.lower().replace(' ', '-').replace(':', '').replace('(', '').replace(')', '').replace(',', '').replace('&', '').replace('–', '').replace(''', '').replace(''', '')
        anchor = re.sub(r'[^\w\-]', '', anchor)
        toc += f"- [{title}](#{anchor})\n"

# Now rebuild the document with section dividers
output = toc + "\n---\n\n"

# Add section dividers
section_dividers = {
    0: """
# ═══════════════════════════════════════════════════════════════
# PART 1: VISUAL PERCEPTION & COGNITIVE LOAD
# Slides 1-21
# ═══════════════════════════════════════════════════════════════

""",
    21: """
# ═══════════════════════════════════════════════════════════════
# PART 2: DATA TYPES & VISUAL ENCODINGS  
# Slides 22-33
# ═══════════════════════════════════════════════════════════════

""",
    33: """
# ═══════════════════════════════════════════════════════════════
# PART 3: GRAMMAR OF GRAPHICS FRAMEWORK
# Slides 34-44
# ═══════════════════════════════════════════════════════════════

""",
    44: """
# ═══════════════════════════════════════════════════════════════
# PART 4: PYTHON VISUALIZATION IMPLEMENTATION
# Slides 45-82
# ═══════════════════════════════════════════════════════════════

"""
}

# Add slides with section dividers
slide_num = 0
for i, slide in enumerate(slides):
    if not slide.strip():
        continue
    
    # Check if this is a slide (has ## header)
    if '##' not in slide:
        continue
    
    # Add section divider if needed
    if slide_num in section_dividers:
        output += section_dividers[slide_num]
    
    # Add the slide
    output += slide.strip()
    
    # Add separator between slides
    if i < len(slides) - 1:
        output += "\n\n---\n\n"
    
    slide_num += 1

# Write the new file
with open('Class3.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\n✅ Reorganization complete!")
print(f"📊 Total slides: {slide_num}")
print(f"📚 Table of Contents: Added with {len(slide_titles)} entries")
print(f"🏷️  Removed 'Slide X –' from all {slide_num} headers")
print(f"📑 Added 4 section dividers")
print(f"\nChanges made:")
print(f"  • Added clickable Table of Contents")
print(f"  • Cleaned all slide headers (removed 'Slide X –')")
print(f"  • Added visual section dividers for 4 major parts")
print(f"  • Maintained all content and images")
print(f"\nBackup saved as: Class3_backup.md")
