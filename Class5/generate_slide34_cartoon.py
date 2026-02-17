"""
Generate a retro cartoon-style image for slide 34 using OpenAI API
"""

import os
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Slide 34 content
slide_title = "Y-Axis Decisions"
slide_subtitle = "Should time series start at zero?"
slide_bullets = [
    "Yes for absolute magnitude (e.g., revenue)",
    "No when showing percent change or deviation"
]
slide_code = "ax.set_ylim(0, None)   # force zero baseline"

# Create detailed prompt for retro cartoon style
prompt = f"""
Create a professional presentation slide illustration in a classic 1960s Hanna-Barbera retro TV animation style:

SLIDE CONTENT:
Title: "{slide_title}"
Subtitle: "{slide_subtitle}"

Key points to illustrate:
- {slide_bullets[0]}
- {slide_bullets[1]}

STYLE REQUIREMENTS:
- Classic 1960s Hanna-Barbera retro cartoon aesthetic
- Clean, simple outlines with soft grain texture
- Playful, educational vibe
- Warm, vintage color palette (blues, oranges, soft yellows)
- 2D flat animation style, NO 3D effects

COMPOSITION:
- Show a friendly cartoon professor/scientist character at a chalkboard or whiteboard
- The board should display Y-axis examples (one starting at zero, one not)
- Include simple chart illustrations showing the difference
- Maybe a small clock or calendar in the background (subtle time-series theme)
- Clean, uncluttered layout with generous whitespace
- 16:9 aspect ratio (landscape orientation for slides)

MOOD:
- Educational but fun
- Retro 1960s TV animation feel
- Friendly and approachable
- Professional yet playful

NO TEXT IN THE IMAGE - we'll overlay the actual text separately for clarity.
Create the illustrated background scene only.
"""

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print("Generating retro cartoon slide for: Y-Axis Decisions")
print("=" * 60)

# Generate image using DALL-E 3
try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",  # Landscape for slides
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url
    print(f"✓ Image generated successfully")
    print(f"  URL: {image_url}")
    
    # Download and save
    print("Downloading image...")
    img_response = requests.get(image_url)
    img = Image.open(BytesIO(img_response.content))
    
    output_file = "slide_images_ai/slide_034_cartoon.png"
    os.makedirs("slide_images_ai", exist_ok=True)
    img.save(output_file)
    
    print(f"✓ Image saved to: {output_file}")
    print(f"  Size: {img.size}")
    print(f"  Format: {img.format}")
    
    print("=" * 60)
    print("✅ Slide 34 cartoon image created successfully!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nIf you see a billing or permission error, you may need to:")
    print("1. Add credits to your OpenAI account")
    print("2. Verify your organization")
    print("3. Check your API key is set: export OPENAI_API_KEY='your-key'")
