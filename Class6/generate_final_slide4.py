"""
Generate Slide 4 Image with Playful Academic Cartoon Style
Using gpt-image-1 model
"""

import os
from openai import OpenAI
import subprocess
import base64

# Slide 4 content - CLEAN (no emojis)
SLIDE_4_CLEAN_TEXT = """
Types of Geographic Data

Understanding your spatial data type guides visualization choice

1. Point Data (Discrete Locations)
Definition: Individual locations with lat/lon coordinates
Examples: Store locations, Customer addresses, Disease cases, Earthquake epicenters, Cell towers
Attributes: Can attach data (sales, demographics, etc.)
Visualizations: Scatter on map, Bubble map (size = value), Heat map (density), Clustering

2. Line Data (Routes/Boundaries)
Definition: Connected sequences of points
Examples: Roads and highways, Rivers and streams, Flight paths, Delivery routes, Transit lines
Visualizations: Path/route maps, Flow maps (width = volume), Network diagrams

3. Polygon Data (Areas/Regions)
Definition: Enclosed boundaries defining regions
Examples: Countries/states/counties, ZIP codes, Sales territories, School districts, Climate zones
Visualizations: Choropleth maps (color = value), Cartograms (size = value), Boundary maps

4. Raster Data (Grid Surfaces)
Definition: Continuous surfaces on regular grids
Examples: Satellite imagery, Elevation (DEMs), Temperature surfaces, Land cover, Precipitation
Visualizations: Heat maps, Contour maps, 3D surfaces
"""

def generate_slide_4_image():
    """Generate complete slide image using gpt-image-1"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Comprehensive image generation prompt
    image_prompt = f"""Create a professional university presentation slide image with the following specifications:

SLIDE CONTENT:
{SLIDE_4_CLEAN_TEXT}

DESIGN THEME: Playful academic cartoon + clean university style

COLOR PALETTE:
- Soft blues (primary)
- Oranges (accents)
- Greens (secondary)
- White background with subtle texture

TYPOGRAPHY:
- Bold headers in rounded friendly font
- Body text in clean sans-serif
- Title: "Types of Geographic Data" - large, bold, top of slide
- Section headers: 1. Point Data, 2. Line Data, 3. Polygon Data, 4. Raster Data

VISUAL STYLE:
- Illustrated cartoon-style icons for each data type (simple, friendly)
- Simple diagrams showing each type visually
- Light shadows for depth
- Subtle paper/canvas texture background
- Clean layout with good spacing
- Playful but professional

LAYOUT:
- 16:9 aspect ratio landscape
- Title at top center
- 4 data types arranged in 2x2 grid or flowing layout
- Each section with:
  * Icon/illustration showing the concept
  * Data type name
  * Definition
  * 2-3 example bullet points
  * Visualization types
- Clean, organized, easy to read

REQUIREMENTS:
- All text from content must be included and readable
- Show visual examples of each data type (points, lines, polygons, grids)
- Professional enough for university
- Playful enough to be engaging
- Cartoon-style illustrations but not childish
- Clear differentiation between the 4 types

Style reference: Think Coursera or Khan Academy - educational, friendly, professional
"""
    
    print("🎨 Generating slide 4 with playful academic cartoon style...")
    print("Using gpt-image-1 model")
    print("\nDesign specs:")
    print("  - Palette: Soft blues, oranges, greens")
    print("  - Style: Playful academic cartoon")
    print("  - Typography: Bold + rounded friendly")
    print("  - Visuals: Illustrated icons for 4 data types")
    print()
    
    response = client.images.generate(
        model="gpt-image-1",
        prompt=image_prompt,
        size="1536x1024",  # 16:9 landscape format
        quality="high",
        n=1
    )
    
    print(f"✅ Image generated successfully!")
    
    # Save image
    output_file = 'Class6/slide_images/slide_004_final.png'
    os.makedirs('Class6/slide_images', exist_ok=True)
    
    print(f"\n📥 Saving image...")
    
    # Check if we have URL or b64_json
    if hasattr(response.data[0], 'url') and response.data[0].url:
        image_url = response.data[0].url
        print(f"🖼️  URL: {image_url}")
        subprocess.run(['curl', '-s', '-o', output_file, image_url], check=True)
    elif hasattr(response.data[0], 'b64_json') and response.data[0].b64_json:
        # Decode base64 image
        image_data = base64.b64decode(response.data[0].b64_json)
        with open(output_file, 'wb') as f:
            f.write(image_data)
        image_url = "Generated as base64 (no URL)"
    else:
        raise ValueError("No image data in response")
    
    print(f"✅ Saved to: {output_file}")
    
    # Save reference
    with open('Class6/slide_004_image_url.txt', 'w') as f:
        f.write(f"Slide 4 - Playful Academic Cartoon Style\n")
        f.write(f"Model: gpt-image-1\n")
        f.write(f"URL: {image_url}\n")
        f.write(f"\nPrompt used:\n{image_prompt}\n")
    
    return output_file

if __name__ == "__main__":
    print("="*80)
    print("🎓 SLIDE 4 GENERATOR - Playful Academic Cartoon Style")
    print("="*80)
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not set")
        exit(1)
    
    output_file = generate_slide_4_image()
    
    print("\n" + "="*80)
    print("✨ Slide 4 image generated!")
    print(f"📄 File: {output_file}")
    print("\n🎨 Design features:")
    print("   - Playful academic cartoon style")
    print("   - Soft blues, oranges, greens palette")
    print("   - Bold headers + friendly rounded font")
    print("   - Illustrated icons for 4 data types")
    print("   - Clean, professional university quality")
    print("\n🚀 Open the image to view the slide!")
