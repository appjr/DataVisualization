"""
Generate Space-Themed Slide 4 for Class 6 using OpenAI API
Transforms 'Types of Geographic Data' into a space theme
"""

import os
from openai import OpenAI
import pandas as pd

# Slide 4 content
SLIDE_4_CONTENT = """
## Types of Geographic Data

**Understanding your spatial data type guides visualization choice**

**1. Point Data (Discrete Locations)**

**Definition:** Individual locations with lat/lon coordinates

**Examples:**
- Store locations
- Customer addresses
- Disease cases
- Earthquake epicenters
- Cell towers

**Attributes:** Can attach data (sales, demographics, etc.)

**Visualizations:**
- Scatter on map
- Bubble map (size = value)
- Heat map (density)
- Clustering

**2. Line Data (Routes/Boundaries)**

**Definition:** Connected sequences of points

**Examples:**
- Roads and highways
- Rivers and streams
- Flight paths
- Delivery routes
- Transit lines

**Visualizations:**
- Path/route maps
- Flow maps (width = volume)
- Network diagrams

**3. Polygon Data (Areas/Regions)**

**Definition:** Enclosed boundaries defining regions

**Examples:**
- Countries, states, counties
- ZIP codes
- Sales territories
- School districts
- Climate zones

**Visualizations:**
- Choropleth maps (color = value)
- Cartograms (size = value)
- Boundary maps

**4. Raster Data (Grid Surfaces)**

**Definition:** Continuous surfaces on regular grids

**Examples:**
- Satellite imagery
- Elevation (DEMs)
- Temperature surfaces
- Land cover
- Precipitation

**Visualizations:**
- Heat maps
- Contour maps
- 3D surfaces
"""

def generate_space_themed_slide():
    """Generate space-themed version of slide 4"""
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create prompt for space theme transformation
    prompt = f"""
Transform the following educational slide about geographic data types into a SPACE-THEMED version while maintaining all the key information and educational value.

Requirements:
1. Keep all 4 data types (Point, Line, Polygon, Raster)
2. Transform the examples to have a space/cosmic theme (stars, planets, space stations, orbits, etc.)
3. Use space-related emojis (🚀, 🛸, 🌟, 🪐, ⭐, 🌌, 💫, 🛰️, etc.)
4. Make it engaging and fun while staying educational
5. Keep the structure organized with Definition, Examples, Visualizations for each type
6. Use creative space analogies that still make the concepts clear
7. Maintain the technical accuracy of the data type classifications

Original Slide Content:
{SLIDE_4_CONTENT}

Generate the space-themed slide in Markdown format, ready to be included in the class materials.
"""
    
    print("🚀 Calling OpenAI API to generate space-themed slide 4...")
    
    # Call ChatGPT API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative educational content designer who specializes in making technical content engaging through creative themes while maintaining educational integrity and technical accuracy."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=2500
    )
    
    space_themed_content = response.choices[0].message.content
    
    print("\n" + "="*80)
    print("SPACE-THEMED SLIDE 4 GENERATED:")
    print("="*80 + "\n")
    print(space_themed_content)
    print("\n" + "="*80)
    
    # Save to file
    output_file = 'Class6/slide4_space_theme.md'
    with open(output_file, 'w') as f:
        f.write("# Class 6 - Slide 4 (Space Theme)\n\n")
        f.write(space_themed_content)
    
    print(f"\n✅ Saved to: {output_file}")
    
    return space_themed_content

def generate_space_illustration():
    """Generate a space-themed illustration for slide 4"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    image_prompt = """
Create an educational illustration for a data visualization class showing the 4 TYPES OF GEOGRAPHIC DATA with a SPACE theme.

The image should show 4 distinct sections/quadrants:

1. POINT DATA (top-left): Individual stars, space stations, or asteroids representing discrete locations in space
2. LINE DATA (top-right): Orbital paths, flight routes between planets, cosmic highways connecting celestial bodies
3. POLYGON DATA (bottom-left): Defined regions like star systems, galaxies with borders, territorial zones in space
4. RASTER DATA (bottom-right): Heat map of cosmic radiation, nebula density grid, continuous surface showing temperature or energy

Requirements:
- Cosmic background with deep space colors (blues, purples, blacks with stars)
- Clear visual separation between the 4 types
- Each quadrant labeled clearly
- Professional but engaging style
- Educational diagrams integrated with space theme
- Data visualization elements visible (dots, lines, colored regions, grids)
- Suitable for a university business school presentation

Style: Modern, educational, space-themed, professional quality
"""
    
    print("\n🎨 Generating space-themed illustration for slide 4...")
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1792x1024",
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url
    
    print(f"\n✅ Image generated!")
    print(f"🖼️  URL: {image_url}")
    print(f"\n📝 Download and save to: Class6/images/slide4_space_theme.png")
    
    # Save URL to file for reference
    with open('Class6/slide4_space_image_url.txt', 'w') as f:
        f.write(f"Space-themed slide 4 illustration\n")
        f.write(f"Generated: {pd.Timestamp.now()}\n")
        f.write(f"URL: {image_url}\n")
        f.write(f"\nPrompt used:\n{image_prompt}\n")
    
    return image_url

if __name__ == "__main__":
    print("🚀 SPACE-THEMED SLIDE 4 GENERATOR")
    print("="*80)
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-key-here'")
        exit(1)
    
    # Generate space-themed content
    space_content = generate_space_themed_slide()
    
    # Ask user if they want to generate illustration
    print("\n" + "="*80)
    generate_image = input("\n🎨 Generate space-themed illustration? (y/n): ").lower()
    
    if generate_image == 'y':
        image_url = generate_space_illustration()
        print(f"\n✨ Complete! Check the files:")
        print(f"   📄 Content: Class6/slide4_space_theme.md")
        print(f"   🔗 Image URL: Class6/slide4_space_image_url.txt")
        
        # Download image
        print(f"\n📥 Downloading image...")
        import subprocess
        subprocess.run(['curl', '-o', 'Class6/images/slide4_space_theme.png', image_url])
        print(f"   🖼️  Image saved: Class6/images/slide4_space_theme.png")
    else:
        print(f"\n✨ Space-themed content saved to: Class6/slide4_space_theme.md")
    
    print("\n🌌 Space transformation complete!")
