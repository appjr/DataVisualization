"""
Extract individual slides from Class5.md into separate files
Split by --- delimiter
"""

import os

# Create output directory
os.makedirs('individual_slides', exist_ok=True)

# Read the markdown file
with open('Class5.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by --- (slide separators)
slides = content.split('\n---\n')

print(f"Found {len(slides)} slides")

# Save each slide to a separate file
slide_counter = 0
for i, slide in enumerate(slides):
    slide = slide.strip()
    
    # Skip empty slides or table of contents sections
    if not slide or len(slide) < 20:
        continue
    
    # Skip if it's just a part header separator
    if slide.startswith('# ═══'):
        continue
    
    slide_counter += 1
    filename = f'individual_slides/slide_{slide_counter:03d}.md'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(slide)
    
    # Show first 60 chars of each slide for verification
    first_line = slide.split('\n')[0][:60]
    print(f"✓ slide_{slide_counter:03d}.md: {first_line}...")

print(f"\n✅ Successfully extracted {slide_counter} slides to individual_slides/")
