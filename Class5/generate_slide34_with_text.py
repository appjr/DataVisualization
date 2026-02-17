"""
Generate slide 34 with TEXT INCLUDED in retro cartoon style
Using ChatGPT/DALL-E to create a complete slide image
"""

import os
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Slide 34 complete content
slide_content = """
Y-AXIS DECISIONS

Should time series start at zero?

✓ YES - for absolute magnitude (e.g., revenue)
✗ NO - when showing percent change or deviation

Code example:
ax.set_ylim(0, None)  # force zero baseline
"""

# Create detailed prompt with TEXT INCLUDED
prompt = f"""
Create a complete presentation slide in classic 1960s Hanna-Barbera retro TV animation style.

SLIDE CONTENT TO INCLUDE (text must be readable and prominent):
---
{slide_content}
---

STYLE REQUIREMENTS:
- Classic Hanna-Barbera retro cartoon aesthetic (like Flintstones, Jetsons era)
- Clean, bold outlines with soft grain texture
- Vintage color palette: warm blues, oranges, soft yellows, pastels
- 2D flat animation style, playful but professional
- Hand-drawn lettering feel for titles

COMPOSITION & LAYOUT:
- Title "Y-AXIS DECISIONS" at top in large, bold, retro-style lettering
- Subtitle "Should time series start at zero?" in italics below
- Two main points with checkmark and X symbols clearly visible
- Code example in a distinct code box or panel at bottom
- Include a friendly cartoon professor/scientist character pointing to the content
- Maybe show example charts (one with Y-axis at zero, one not) as illustrations
- Small time-series themed props (clock, calendar, chart) in corners
- Clean chalkboard or whiteboard as main presentation surface
- 16:9 landscape slide format

TEXT REQUIREMENTS - CRITICAL:
- ALL text must be clearly readable and correctly spelled
- Use clean, legible font that fits the retro aesthetic
- Make sure "✓ YES" and "✗ NO" symbols are prominent
- Code example should be in monospace/typewriter style font
- Don't use overly stylized text that becomes unreadable

MOOD:
- Educational and friendly
- Retro 1960s TV educational show vibe
- Approachable and fun but still professional
- Like a vintage educational cartoon

Create a COMPLETE slide with all text visible and readable.
"""

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print("Generating complete retro cartoon slide 34 with text...")
print("=" * 60)
print(f"Content:\n{slide_content}")
print("=" * 60)

# Generate image using DALL-E 3
try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",  # Landscape for slides
        quality="hd",  # Use HD for better text clarity
        style="natural",  # More readable text
        n=1
    )
    
    image_url = response.data[0].url
    print(f"✓ Image generated successfully")
    print(f"  URL: {image_url}")
    print(f"  Revised prompt: {response.data[0].revised_prompt[:200]}...")
    
    # Download and save
    print("\nDownloading image...")
    img_response = requests.get(image_url)
    img = Image.open(BytesIO(img_response.content))
    
    output_file = "slide_images_ai/slide_034_with_text.png"
    os.makedirs("slide_images_ai", exist_ok=True)
    img.save(output_file)
    
    print(f"\n✓ Image saved to: {output_file}")
    print(f"  Size: {img.size}")
    print(f"  Format: {img.format}")
    print(f"  File size: {os.path.getsize(output_file) / 1024 / 1024:.1f} MB")
    
    print("=" * 60)
    print("✅ Complete slide 34 cartoon image created successfully!")
    print("\nOpen the image to verify text is readable and content is accurate.")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Check API key: export OPENAI_API_KEY='your-key'")
    print("2. Check billing: https://platform.openai.com/account/billing")
    print("3. If permission error, verify org: https://platform.openai.com/settings/organization/general")
