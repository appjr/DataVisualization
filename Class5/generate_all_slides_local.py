"""
Generate slide images from ALL markdown files locally (no API calls)
Reads each .md file and creates a professional slide image
"""

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import textwrap

def create_slide_from_md(md_file, output_file, slide_num):
    """Create a slide image from markdown content"""
    
    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse content
    lines = content.strip().split('\n')
    title = ""
    subtitle = ""
    bullets = []
    code_blocks = []
    
    in_code_block = False
    code_content = []
    
    for line in lines:
        stripped = line.strip()
        
        # Code blocks
        if stripped.startswith('```'):
            if in_code_block:
                code_blocks.append('\n'.join(code_content))
                code_content = []
                in_code_block = False
            else:
                in_code_block = True
            continue
        
        if in_code_block:
            code_content.append(line)
            continue
        
        # Title (## heading)
        if stripped.startswith('## '):
            if not title:
                title = stripped[3:].strip()
        # Subtitle (### or **bold**)
        elif stripped.startswith('### '):
            if not subtitle:
                subtitle = stripped[4:].strip()
        elif stripped.startswith('**') and stripped.endswith('**') and not title:
            title = stripped[2:-2].strip()
        # Bullets
        elif stripped.startswith('- ') or stripped.startswith('* '):
            bullets.append(stripped[2:].strip())
        # Bold lines as bullets
        elif stripped.startswith('**') and stripped.endswith('**'):
            bullets.append(stripped[2:-2].strip())
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    # Background
    rect = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, 
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2c3e50', 
                          facecolor='#ecf0f1',
                          linewidth=3)
    ax.add_patch(rect)
    
    # Title
    if title:
        wrapped_title = '\n'.join(textwrap.wrap(title, width=50))
        ax.text(5, 8.8, wrapped_title, 
                ha='center', va='top',
                fontsize=28, fontweight='bold',
                color='#2c3e50')
        y_pos = 8.2 - (wrapped_title.count('\n') * 0.4)
    else:
        y_pos = 8.5
    
    # Subtitle
    if subtitle:
        wrapped_subtitle = '\n'.join(textwrap.wrap(subtitle, width=60))
        ax.text(5, y_pos, wrapped_subtitle,
                ha='center', va='top',
                fontsize=20, style='italic',
                color='#34495e')
        y_pos -= 0.6 + (wrapped_subtitle.count('\n') * 0.3)
    
    # Bullets
    if bullets:
        y_pos -= 0.3
        for bullet in bullets[:8]:  # Limit to 8 bullets
            wrapped = textwrap.wrap(bullet, width=70)
            for i, line in enumerate(wrapped[:3]):  # Max 3 lines per bullet
                prefix = '•' if i == 0 else ' '
                x_offset = 1.5 if i == 0 else 1.8
                ax.text(x_offset, y_pos, f"{prefix} {line}",
                        ha='left', va='top',
                        fontsize=16,
                        color='#2c3e50')
                y_pos -= 0.4
            if y_pos < 1.5:  # Stop if too low
                break
    
    # Code block (if present and space available)
    if code_blocks and y_pos > 2:
        code = code_blocks[0]
        code_lines = code.split('\n')[:5]  # Max 5 lines
        
        # Code box
        code_box = FancyBboxPatch((1, y_pos - len(code_lines)*0.35 - 0.5), 8, len(code_lines)*0.35 + 0.3,
                                 boxstyle="round,pad=0.05",
                                 edgecolor='#95a5a6',
                                 facecolor='#34495e',
                                 linewidth=2)
        ax.add_patch(code_box)
        
        y_code = y_pos - 0.3
        for line in code_lines:
            ax.text(1.3, y_code, line[:80],
                    ha='left', va='top',
                    fontsize=12,
                    color='#3498db',
                    family='monospace')
            y_code -= 0.35
    
    # Footer
    ax.text(5, 0.8, f'Class 5 – Time Series & Temporal Visualization',
            ha='center', va='center',
            fontsize=12, color='#7f8c8d')
    
    ax.text(9.5, 0.4, f'Slide {slide_num}',
            ha='right', va='center',
            fontsize=10, color='#95a5a6', style='italic')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def main():
    import glob
    
    # Create output directory
    os.makedirs('slide_images', exist_ok=True)
    
    # Get all markdown files
    md_files = sorted(glob.glob('individual_slides/slide_*.md'))
    
    print(f"Generating {len(md_files)} slide images...")
    print("=" * 60)
    
    for md_file in md_files:
        basename = os.path.basename(md_file)
        slide_num = int(basename.replace('slide_', '').replace('.md', ''))
        output_file = f'slide_images/{basename.replace(".md", ".png")}'
        
        create_slide_from_md(md_file, output_file, slide_num)
        print(f"✓ Created {output_file}")
    
    print("=" * 60)
    print(f"✅ Successfully created {len(md_files)} slide images!")
    print(f"📁 Location: Class5/slide_images/")

if __name__ == "__main__":
    main()
