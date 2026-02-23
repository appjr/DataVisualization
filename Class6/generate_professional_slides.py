"""
Generate professional space-themed slides using executive presentation designer approach
"""

import os
from openai import OpenAI

# EXACT content from markdown
SLIDE_3_CONTENT = """
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

SLIDE_4_CONTENT = """
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

def generate_slide(slide_num, content):
    """Generate professional slide using executive presentation template"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""Act as an expert executive presentation designer and storytelling strategist.

Create a professional slide based on the content I provide.

OBJECTIVE:
University lecture on Data Visualization - Geographic Data module

AUDIENCE:
Graduate business students (MIS program)

THEME:
Space/Cosmic theme - make geographic concepts engaging using space metaphors

TONE & STYLE:
Academic but engaging
Make it:
- Clear
- Visually structured
- Minimal text per slide
- Strong headlines (no generic titles)
- Educational
- Insight-focused

FORMAT REQUIREMENTS:
Provide:

Slide {slide_num}: 
Title (Powerful headline with space theme)
Key Message (1 clear takeaway)
Bullet Content (3–5 concise bullets max per section)
Visual Suggestion (what illustration/diagram would work)

DESIGN INSTRUCTIONS:
- Use space theme language
- Keep content minimal and focused
- Elevate to clear learning objectives
- Make it visually engaging
- Suggest appropriate space-themed visuals

Here is my content:
{content}

Return the slide design in clear format ready for image generation.
"""
    
    print(f"🚀 Generating professional slide {slide_num} design...")
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert presentation designer specializing in educational content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )
    
    result = response.choices[0].message.content
    
    print(f"\n{result}\n")
    
    # Save
    output_file = f'Class6/slide{slide_num}_professional.md'
    with open(output_file, 'w') as f:
        f.write(result)
    
    print(f"✅ Saved to: {output_file}")
    
    return result

def generate_image_from_design(slide_num, design_content):
    """Generate image based on the professional design"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""Create a professional university presentation slide image with space theme.

Use this slide design:
{design_content}

CRITICAL REQUIREMENTS:
- 16:9 aspect ratio (1792x1024)
- Space-themed background (subtle, professional)
- Clear readable text (white or light colored)
- Professional layout suitable for business school
- Clean design with good visual hierarchy
- Include all bullet points from the design
- Space elements should enhance, not distract

Style: Professional, educational, space-themed, modern
"""
    
    print(f"🎨 Generating image for slide {slide_num}...")
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url
    
    # Download
    import subprocess
    output_file = f'Class6/slide_images/slide_00{slide_num}_final.png'
    subprocess.run(['curl', '-s', '-o', output_file, image_url], check=True)
    
    print(f"✅ Image created: {output_file}")
    
    return output_file

if __name__ == "__main__":
    print("🌌 PROFESSIONAL SPACE-THEMED SLIDE GENERATOR")
    print("="*80)
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not set")
        exit(1)
    
    # Generate slide 3
    print("\n" + "="*80)
    print("SLIDE 3")
    print("="*80)
    design3 = generate_slide(3, SLIDE_3_CONTENT)
    
    print("\n" + "="*80)
    image3 = generate_image_from_design(3, design3)
    
    # Generate slide 4
    print("\n" + "="*80)
    print("SLIDE 4")
    print("="*80)
    design4 = generate_slide(4, SLIDE_4_CONTENT)
    
    print("\n" + "="*80)
    image4 = generate_image_from_design(4, design4)
    
    print("\n" + "="*80)
    print("✨ Professional space-themed slides created!")
    print(f"   📄 Slide 3 design: Class6/slide3_professional.md")
    print(f"   🖼️  Slide 3 image: {image3}")
    print(f"   📄 Slide 4 design: Class6/slide4_professional.md")
    print(f"   🖼️  Slide 4 image: {image4}")
