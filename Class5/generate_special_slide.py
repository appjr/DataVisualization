"""
Generate image for "What Makes Time Series Data Special?" slide
Using OpenAI DALL-E 3 with 1960s educational animation style
"""

import os
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Slide content
slide_content = """
WHAT MAKES TIME SERIES DATA SPECIAL?

7 Unique Properties:

1. Temporal Ordering Matters
   - Cannot shuffle data
   - Order contains critical information

2. Temporal Dependencies
   - Today's value depends on yesterday
   - Autocorrelation, lag effects

3. Non-IID (Not Independent & Identically Distributed)
   - Standard statistical assumptions VIOLATED
   - Need specialized methods

4. Multiple Time Scales Simultaneously
   - Hourly, daily, weekly, monthly patterns
   - All present at once

5. Non-Stationarity
   - Properties change over time
   - Mean, variance shift

6. Irregular Intervals & Missing Data
   - Gaps from weekends, holidays
   - Missing values have meaning

7. Context-Dependent Interpretation
   - Same value means different things
   - Temporal context matters
"""

# Create detailed prompt
prompt = f"""
Create a high-quality educational slide illustration in 1960s American limited television animation style (Hanna-Barbera inspired):

SLIDE CONTENT TO VISUALIZE:
{slide_content}

STYLE REQUIREMENTS:
- Classic 1960s retro cartoon aesthetic (Flintstones/Jetsons era)
- Thick ink outlines, flat cel shading
- Retro pastel palette: soft blues, oranges, yellows
- Minimal gradients, slight film grain texture
- Mid-century modern animation proportions
- Clean geometric backgrounds

COMPOSITION:
- Title "WHAT MAKES TIME SERIES DATA SPECIAL?" prominently displayed at top
- Show 7 numbered icons or visual metaphors representing each property
- Include a friendly cartoon professor/scientist character explaining
- Use visual symbols:
  * Clock/calendar for temporal ordering
  * Connected dots/arrows for dependencies  
  * Warning symbol for violated assumptions
  * Multiple layered charts for time scales
  * Wavy line for non-stationarity
  * Broken/dotted line for missing data
  * Question mark for context-dependency
- 16:9 landscape format for presentation
- Educational, clean, organized layout

DESIGN:
- Numbered list (1-7) clearly visible
- Icons or diagrams for each point
- Cartoon character pointing/gesturing
- Chalkboard or presentation board background
- Retro classroom/lab setting
- Professional yet playful educational vibe

Create a complete, visually informative slide that teaches these 7 concepts through illustration.
"""

# Initialize OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print("Generating 'What Makes Time Series Data Special?' slide...")
print("=" * 70)

try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",  # 16:9 landscape
        quality="hd",
        style="natural",
        n=1
    )
    
    image_url = response.data[0].url
    print(f"✓ Image generated successfully")
    print(f"  URL: {image_url[:80]}...")
    
    # Download
    print("\nDownloading image...")
    img_response = requests.get(image_url)
    img = Image.open(BytesIO(img_response.content))
    
    # Save to separate folder
    output_dir = "special_slides"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = f"{output_dir}/what_makes_ts_special.png"
    img.save(output_file)
    
    print(f"\n✓ Image saved successfully")
    print(f"  Output: {output_file}")
    print(f"  Dimensions: {img.size}")
    print(f"  File size: {os.path.getsize(output_file) / 1024 / 1024:.1f} MB")
    
    print("=" * 70)
    print("✅ Slide image created successfully!")
    print(f"\n📁 Saved to: Class5/{output_dir}/")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nCheck:")
    print("  1. API key: echo $OPENAI_API_KEY")
    print("  2. Billing: https://platform.openai.com/account/billing")
