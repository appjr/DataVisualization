"""
Generate Slide 3 Image with Playful Academic Cartoon Style
Using latest ChatGPT model (GPT-4) to create complete slide
"""

import os
from openai import OpenAI
import subprocess

# Slide 3 content - CLEAN (no emojis)
SLIDE_3_CLEAN_TEXT = """
Why Geographic Visualization Matters

Location data is everywhere in business and science:

Business Applications:
- Sales territory performance
- Store location analysis
- Supply chain optimization
- Market demographics
- Global expansion planning

Public Health:
- Disease outbreak tracking
- Hospital coverage areas
- Vaccination rate mapping
- Emergency response planning

Real Estate:
- Property value mapping
- Neighborhood analysis
- Development planning
- Amenity proximity

Transportation:
- Traffic flow visualization
- Route optimization
- Transit coverage
- Parking utilization

Environmental:
- Climate patterns
- Flood risk zones
- Deforestation tracking
- Pollution monitoring

Key Insight: 80% of business data has a geographic component. Maps make patterns visible that tables cannot show.
"""

def generate_slide_3_image():
    """Generate complete slide image using DALL-E 3"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Comprehensive image generation prompt
    image_prompt = f"""Create a professional university presentation slide image with the following specifications:

SLIDE CONTENT:
{SLIDE_3_CLEAN_TEXT}

DESIGN THEME: Playful academic cartoon + clean university style

COLOR PALETTE:
- Soft blues (primary)
- Oranges (accents)
- Greens (secondary)
- White background with subtle texture

TYPOGRAPHY:
- Bold headers in rounded friendly font
- Body text in clean sans-serif
- Title: "Why Geographic Visualization Matters" - large, bold, top of slide
- Section headers: Business Applications, Public Health, Real Estate, Transportation, Environmental

VISUAL STYLE:
- Illustrated cartoon-style icons for each section (simple, friendly)
- Simple map graphics integrated subtly
- Light shadows for depth
- Subtle paper/canvas texture background
- Clean layout with good spacing
- Playful but professional

LAYOUT:
- 16:9 aspect ratio (1792x1024)
- Title at top center
- 5 sections arranged in grid or flowing layout
- Each section with:
  * Icon/illustration
  * Section name
  * 3-5 bullet points in clean text
- Key insight at bottom

REQUIREMENTS:
- All text from content must be included and readable
- Professional enough for university
- Playful enough to be engaging
- Cartoon-style illustrations but not childish
- Clean, organized, easy to read

Style reference: Think Coursera or Khan Academy - educational, friendly, professional
"""
    
    print("🎨 Generating slide 3 with playful academic cartoon style...")
    print("Using latest OpenAI model (ChatGPT 5.2 + DALL-E 3)")
    print("\nDesign specs:")
    print("  - Palette: Soft blues, oranges, greens")
    print("  - Style: Playful academic cartoon")
    print("  - Typography: Bold + rounded friendly")
    print("  - Visuals: Illustrated icons, map graphics")
    print()
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1792x1024",
        quality="hd",  # Use HD quality for better text rendering
        n=1
    )
    
    image_url = response.data[0].url
    
    print(f"✅ Image generated successfully!")
    print(f"🖼️  URL: {image_url}")
    
    # Download image
    output_file = 'Class6/slide_images/slide_003_final.png'
    os.makedirs('Class6/slide_images', exist_ok=True)
    
    print(f"\n📥 Downloading image...")
    subprocess.run(['curl', '-s', '-o', output_file, image_url], check=True)
    
    print(f"✅ Saved to: {output_file}")
    
    # Save URL for reference
    with open('Class6/slide_003_image_url.txt', 'w') as f:
        f.write(f"Slide 3 - Playful Academic Cartoon Style\n")
        f.write(f"URL: {image_url}\n")
        f.write(f"\nPrompt used:\n{image_prompt}\n")
    
    return output_file

if __name__ == "__main__":
    print("="*80)
    print("🎓 SLIDE 3 GENERATOR - Playful Academic Cartoon Style")
    print("="*80)
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not set")
        exit(1)
    
    output_file = generate_slide_3_image()
    
    print("\n" + "="*80)
    print("✨ Slide 3 image generated!")
    print(f"📄 File: {output_file}")
    print("\n🎨 Design features:")
    print("   - Playful academic cartoon style")
    print("   - Soft blues, oranges, greens palette")
    print("   - Bold headers + friendly rounded font")
    print("   - Illustrated icons with map graphics")
    print("   - Clean, professional university quality")
    print("\n🚀 Open the image to view the slide!")
