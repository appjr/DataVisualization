"""
Generate Space-Themed Slide 3 for Class 6 using OpenAI API
Transforms 'Why Geographic Visualization Matters' into a space theme
"""

import os
from openai import OpenAI

# Slide 3 content
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

def generate_space_themed_slide():
    """Generate space-themed version of slide 3"""
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create prompt for space theme transformation
    prompt = f"""
Transform the following educational slide into a SPACE-THEMED version while maintaining all the key information and educational value.

Requirements:
1. Keep all the main sections (Business Applications, Public Health, etc.)
2. Transform the examples to have a space/cosmic theme
3. Use space-related emojis and metaphors (🚀, 🛸, 🌟, 🪐, ⭐, 🌌, etc.)
4. Make it engaging and fun while staying educational
5. Add a space-themed title
6. Include creative space analogies
7. Keep the structure clear and organized
8. Maintain the key insight at the end with a space twist

Original Slide Content:
{SLIDE_3_CONTENT}

Generate the space-themed slide in Markdown format, ready to be included in the class materials.
"""
    
    print("Calling OpenAI API to generate space-themed slide...")
    
    # Call ChatGPT API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative educational content designer who specializes in making technical content engaging through creative themes while maintaining educational integrity."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=2000
    )
    
    space_themed_content = response.choices[0].message.content
    
    print("\n" + "="*80)
    print("SPACE-THEMED SLIDE 3 GENERATED:")
    print("="*80 + "\n")
    print(space_themed_content)
    print("\n" + "="*80)
    
    # Save to file
    output_file = 'Class6/slide3_space_theme.md'
    with open(output_file, 'w') as f:
        f.write("# Class 6 - Slide 3 (Space Theme)\n\n")
        f.write(space_themed_content)
    
    print(f"\n✅ Saved to: {output_file}")
    
    return space_themed_content

def generate_space_illustration():
    """Generate a space-themed illustration for the slide"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    image_prompt = """
Create a vibrant, educational illustration for a data visualization class slide with a SPACE theme.

The image should show:
- A cosmic background with stars, galaxies, and nebulae
- Multiple planets or celestial bodies, each representing different applications:
  * A planet with business charts/graphs floating around it (Business Applications)
  * A planet with medical/health symbols (Public Health)
  * A planet with building/housing icons (Real Estate)
  * A planet with vehicle/transport symbols (Transportation)
  * A planet with nature/environmental symbols (Environmental)
- Data visualization elements (charts, graphs, maps) integrated into the space scene
- A central theme showing how data "orbits" around Earth or connects different worlds
- Professional yet playful style suitable for a university course
- Vibrant colors: blues, purples, oranges, cosmic colors
- Include subtle geographic/map elements integrated with the space theme

Style: Modern, educational, slightly whimsical but professional, suitable for a business school presentation.
"""
    
    print("\nGenerating space-themed illustration...")
    
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
    print(f"\n📝 Download and save to: Class6/images/slide3_space_theme.png")
    
    # Save URL to file for reference
    with open('Class6/slide3_space_image_url.txt', 'w') as f:
        f.write(f"Space-themed slide 3 illustration\n")
        f.write(f"Generated: {pd.Timestamp.now()}\n")
        f.write(f"URL: {image_url}\n")
        f.write(f"\nPrompt used:\n{image_prompt}\n")
    
    return image_url

if __name__ == "__main__":
    import pandas as pd
    
    print("🚀 SPACE-THEMED SLIDE 3 GENERATOR")
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
        print(f"   📄 Content: Class6/slide3_space_theme.md")
        print(f"   🔗 Image URL: Class6/slide3_space_image_url.txt")
    else:
        print(f"\n✨ Space-themed content saved to: Class6/slide3_space_theme.md")
    
    print("\n🌌 Space transformation complete!")
