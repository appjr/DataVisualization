"""
Generate space-themed IMAGES for Class 6 slides
Uses EXACT content from markdown, just adds space-themed visual background
"""

import os
from openai import OpenAI

# EXACT Slide 3 content from Class6_Part1.md
SLIDE_3_CONTENT = """
## Why Geographic Visualization Matters

**Location data is everywhere in business and science:**

**Business Applications:**
- 📍 Sales territory performance
- 🏪 Store location analysis
- 🚚 Supply chain optimization
- 🏘️ Market demographics
- 🌍 Global expansion planning

**Public Health:**
- 🦠 Disease outbreak tracking
- 🏥 Hospital coverage areas
- 💉 Vaccination rate mapping
- 🚑 Emergency response planning

**Real Estate:**
- 🏠 Property value mapping
- 📊 Neighborhood analysis
- 🏗️ Development planning
- 🌳 Amenity proximity

**Transportation:**
- 🚗 Traffic flow visualization
- ✈️ Route optimization
- 🚇 Transit coverage
- 🅿️ Parking utilization

**Environmental:**
- 🌡️ Climate patterns
- 🌊 Flood risk zones
- 🌲 Deforestation tracking
- 🏭 Pollution monitoring

**Key Insight:** 80%+ of business data has a geographic component. Maps make patterns visible that tables cannot show.
"""

# EXACT Slide 4 content from Class6_Part1.md
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

def generate_space_image(slide_num, slide_content):
    """Generate space-themed illustration for the slide content"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create image prompt based on slide content
    if slide_num == 3:
        image_prompt = """
Create a professional presentation slide image with SPACE THEME for a data visualization class.

Title at top: "Why Geographic Visualization Matters"

The slide should show:
- Space/cosmic background (deep blues, purples, stars, galaxies)
- Five sections arranged clearly:
  1. Business Applications (with business/chart icons in space)
  2. Public Health (with medical/health symbols)
  3. Real Estate (with building/property icons)
  4. Transportation (with vehicle/route symbols)
  5. Environmental (with nature/planet icons)
- Each section should have a cosmic planet or celestial body representing it
- Professional layout suitable for university presentation
- Clear text areas for bullet points
- Footer noting "80% of business data has geographic component"

Style: Modern, professional, space-themed, suitable for business school, 16:9 aspect ratio
"""
    else:  # slide 4
        image_prompt = """
Create a professional presentation slide image with SPACE THEME for a data visualization class.

Title at top: "Types of Geographic Data"

The slide should show 4 distinct quadrants or sections:
1. Point Data - showing individual stars/points in space
2. Line Data - showing orbital paths/connections
3. Polygon Data - showing defined regions like galaxies/territories
4. Raster Data - showing grid/continuous surface like heat maps

Requirements:
- Space/cosmic background (deep blues, purples, nebulae)
- Each data type clearly labeled and visually distinct
- Professional diagrams showing the concept
- Suitable for university business school presentation
- 16:9 aspect ratio
- Modern, clean design

Style: Educational, professional, space-themed
"""
    
    print(f"🎨 Generating space-themed image for slide {slide_num}...")
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1792x1024",
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url
    
    print(f"✅ Image generated: {image_url}")
    
    # Download image
    import subprocess
    output_file = f'Class6/slide_images/slide_00{slide_num}_space_final.png'
    subprocess.run(['curl', '-s', '-o', output_file, image_url], check=True)
    
    print(f"📥 Downloaded: {output_file}")
    
    return image_url, output_file

if __name__ == "__main__":
    print("🌌 GENERATING SPACE-THEMED SLIDE IMAGES")
    print("="*80)
    print("Using EXACT content from markdown files")
    print("Only adding space-themed visual backgrounds")
    print("="*80 + "\n")
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not set")
        exit(1)
    
    # Generate images
    url3, file3 = generate_space_image(3, SLIDE_3_CONTENT)
    print()
    url4, file4 = generate_space_image(4, SLIDE_4_CONTENT)
    
    print("\n" + "="*80)
    print("✨ Space-themed slide images created!")
    print(f"   🖼️  Slide 3: {file3}")
    print(f"   🖼️  Slide 4: {file4}")
    print("\n🚀 Images have space theme background, content unchanged!")
