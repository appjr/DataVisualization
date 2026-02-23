"""
Generate Space-Themed Slides - Simplified version
Sends clean text to API without emojis/images
"""

import os
from openai import OpenAI
import pandas as pd
import re

def clean_content(text):
    """Remove emojis and special formatting from content"""
    # Remove emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove markdown bold
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    # Remove markdown headers
    text = re.sub(r'##\s+', '', text)
    return text.strip()

# SLIDE 3 - Clean content
SLIDE_3_CLEAN = """
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

Key Insight: 80%+ of business data has a geographic component. Maps make patterns visible that tables cannot show.
"""

# SLIDE 4 - Clean content
SLIDE_4_CLEAN = """
Types of Geographic Data

Understanding your spatial data type guides visualization choice

1. Point Data (Discrete Locations)
Definition: Individual locations with lat/lon coordinates
Examples: Store locations, Customer addresses, Disease cases, Earthquake epicenters, Cell towers
Visualizations: Scatter on map, Bubble map, Heat map, Clustering

2. Line Data (Routes/Boundaries)
Definition: Connected sequences of points
Examples: Roads and highways, Rivers and streams, Flight paths, Delivery routes, Transit lines
Visualizations: Path/route maps, Flow maps, Network diagrams

3. Polygon Data (Areas/Regions)
Definition: Enclosed boundaries defining regions
Examples: Countries/states/counties, ZIP codes, Sales territories, School districts, Climate zones
Visualizations: Choropleth maps, Cartograms, Boundary maps

4. Raster Data (Grid Surfaces)
Definition: Continuous surfaces on regular grids
Examples: Satellite imagery, Elevation DEMs, Temperature surfaces, Land cover, Precipitation
Visualizations: Heat maps, Contour maps, 3D surfaces
"""

def generate_space_slide(slide_num, clean_content):
    """Generate space-themed slide with clean text input"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""
Transform this educational slide into a SPACE THEME while keeping all information:

{clean_content}

Requirements:
- Replace earthly terms with space equivalents (stores→space stations, roads→orbits, etc.)
- Add space emojis appropriately (rocket, planet, star, satellite, etc.)
- Keep the same structure and all key information
- Make it fun but educational
- Output in clean Markdown format

Return ONLY the transformed slide content, ready to use.
"""
    
    print(f"🚀 Generating space-themed slide {slide_num}...")
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert at creating engaging educational content with creative themes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )
    
    result = response.choices[0].message.content
    
    # Save to file
    output_file = f'Class6/slide{slide_num}_space_clean.md'
    with open(output_file, 'w') as f:
        f.write(f"# Slide {slide_num} - Space Theme\n\n")
        f.write(result)
    
    print(f"✅ Saved to: {output_file}")
    print(f"\n{result}\n")
    
    return result

if __name__ == "__main__":
    print("🌌 SPACE-THEMED SLIDE GENERATOR (SIMPLIFIED)")
    print("="*80)
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not set")
        exit(1)
    
    # Generate slides
    print("\n" + "="*80)
    slide3 = generate_space_slide(3, SLIDE_3_CLEAN)
    
    print("\n" + "="*80)
    slide4 = generate_space_slide(4, SLIDE_4_CLEAN)
    
    print("\n" + "="*80)
    print("✨ Space-themed slides generated!")
    print("   📄 Slide 3: Class6/slide3_space_clean.md")
    print("   📄 Slide 4: Class6/slide4_space_clean.md")
