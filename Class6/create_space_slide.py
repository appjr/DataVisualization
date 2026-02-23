"""
Create a professional space-themed slide image from content
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_space_slide(slide_number, title, content_sections, background_image_path=None):
    """
    Create a professional space-themed slide
    
    Args:
        slide_number: Slide number
        title: Slide title
        content_sections: List of dicts with 'heading' and 'bullets'
        background_image_path: Optional path to background image
    """
    
    # Create figure
    fig = plt.figure(figsize=(16, 9), facecolor='#0a0e27')  # Dark space blue
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    # Add background image if provided
    if background_image_path and os.path.exists(background_image_path):
        try:
            bg_img = Image.open(background_image_path)
            ax.imshow(bg_img, extent=[0, 16, 0, 9], aspect='auto', alpha=0.3, zorder=0)
        except:
            pass
    
    # Add space background pattern (stars)
    import numpy as np
    np.random.seed(42)
    star_x = np.random.uniform(0, 16, 100)
    star_y = np.random.uniform(0, 9, 100)
    star_sizes = np.random.uniform(1, 10, 100)
    ax.scatter(star_x, star_y, s=star_sizes, color='white', alpha=0.6, zorder=1)
    
    # Add gradient background
    from matplotlib.patches import Rectangle
    for i in range(100):
        alpha_val = 0.05 * (1 - i/100)
        rect = Rectangle((0, i*0.09), 16, 0.09, 
                        facecolor='#1a1f4d', alpha=alpha_val, zorder=0)
        ax.add_patch(rect)
    
    # Add title with space styling
    title_box = mpatches.FancyBboxPatch(
        (0.5, 7.5), 15, 1.2,
        boxstyle="round,pad=0.1",
        facecolor='#1a3d7c',
        edgecolor='#00d4ff',
        linewidth=3,
        alpha=0.9,
        zorder=2
    )
    ax.add_patch(title_box)
    
    ax.text(8, 8.1, title, 
           fontsize=28, fontweight='bold', color='#00d4ff',
           ha='center', va='center', zorder=3,
           family='sans-serif')
    
    # Add content sections
    y_start = 6.8
    y_pos = y_start
    section_height = 6.5 / len(content_sections) if content_sections else 1.5
    
    for section in content_sections:
        # Section heading
        heading_text = section.get('heading', '')
        if heading_text:
            ax.text(0.8, y_pos, heading_text,
                   fontsize=18, fontweight='bold', color='#ffd700',
                   ha='left', va='top', zorder=3)
            y_pos -= 0.4
        
        # Bullets
        bullets = section.get('bullets', [])
        for bullet in bullets[:5]:  # Limit bullets per section
            wrapped = textwrap.wrap(bullet, width=70)
            for line in wrapped:
                ax.text(1.2, y_pos, f"🌟 {line}",
                       fontsize=14, color='white',
                       ha='left', va='top', zorder=3)
                y_pos -= 0.28
        
        y_pos -= 0.2  # Space between sections
        
        if y_pos < 0.5:
            break
    
    # Add footer with slide number
    ax.text(15.5, 0.3, f"🚀 Slide {slide_number}",
           fontsize=12, color='#00d4ff', alpha=0.7,
           ha='right', va='bottom', zorder=3)
    
    # Save
    output_file = f'Class6/slide_images/slide_{slide_number:03d}_space.png'
    os.makedirs('Class6/slide_images', exist_ok=True)
    plt.savefig(output_file, dpi=150, bbox_inches='tight', 
               facecolor='#0a0e27', edgecolor='none')
    plt.close()
    
    print(f"✅ Created: {output_file}")
    return output_file


# Generate Slide 3: Why Geographic Visualization Matters
def generate_slide_3():
    title = "🌌 Why Geographic Visualization Matters in the Cosmos"
    
    sections = [
        {
            'heading': '🚀 Business Applications',
            'bullets': [
                '📡 Galactic sales sector performance',
                '🛸 Cosmic storefront placement',
                '🌍 Interplanetary supply routes'
            ]
        },
        {
            'heading': '🌟 Public Health Applications',
            'bullets': [
                '🪐 Space plague tracking',
                '💫 Nebula health stations',
                '🚑 Meteor emergency response'
            ]
        },
        {
            'heading': '🪐 Key Insight',
            'bullets': [
                '80%+ of business data orbits around geography',
                'Star maps reveal patterns data tables cannot show'
            ]
        }
    ]
    
    return create_space_slide(3, title, sections, 'Class6/images/slide3_space_theme.png')


# Generate Slide 4: Types of Geographic Data
def generate_slide_4():
    title = "🚀 Types of Galactic Data"
    
    sections = [
        {
            'heading': '⭐ Star Point Data',
            'bullets': [
                'Individual celestial coordinates',
                'Examples: Stars, planets, space stations'
            ]
        },
        {
            'heading': '🌌 Orbit Line Data',
            'bullets': [
                'Cosmic highways and trajectories',
                'Examples: Spacecraft paths, satellite orbits'
            ]
        },
        {
            'heading': '🪐 Polygon Regions',
            'bullets': [
                'Galactic territories and zones',
                'Examples: Star systems, nebula boundaries'
            ]
        },
        {
            'heading': '💫 Cosmic Raster Data',
            'bullets': [
                'Continuous celestial surfaces',
                'Examples: Star fields, temperature maps'
            ]
        }
    ]
    
    return create_space_slide(4, title, sections, 'Class6/images/slide4_space_theme.png')


if __name__ == "__main__":
    print("🌌 CREATING SPACE-THEMED SLIDES")
    print("="*80)
    
    # Generate slides
    slide_3 = generate_slide_3()
    slide_4 = generate_slide_4()
    
    print("\n" + "="*80)
    print("✨ Space-themed slides created!")
    print(f"   🖼️  Slide 3: {slide_3}")
    print(f"   🖼️  Slide 4: {slide_4}")
    print("\n🚀 Open the images to view your space-themed slides!")
