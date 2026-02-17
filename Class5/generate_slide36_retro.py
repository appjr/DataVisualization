"""
Generate slide 36: Reference Lines and Benchmarks
High-quality 2D educational slide in 1960s American limited TV animation style
"""

import os
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Slide 36 content from markdown file
slide_content = """
REFERENCE LINES AND BENCHMARKS

Add context with:
• Average line
• Target threshold
• Historical benchmark

Code example:
ax.axhline(df['Sales'].mean(), color='red', linestyle='--', label='Average')
"""

# Create prompt following the exact specifications
prompt = f"""
Create a high-quality 2D educational slide illustration in a 1960s American limited television animation style.

SLIDE CONTENT (from attached file):
{slide_content}

STYLE CONSISTENCY:
- Thick ink outlines
- Flat cel shading
- Minimal gradients
- Retro pastel palette (soft blues, yellows, oranges, greens)
- Slight film grain texture
- Clean geometric backgrounds
- Mid-century animation proportions

VARIATION REQUIREMENTS (different from previous slides):
- Use a RIGHT-SIDE camera angle (board on right, character on left)
- Character pointing upward at the board content
- Diagonal board placement for dynamic composition
- Include props: vintage ruler, protractor, and chart paper
- Use warm orange-yellow color balance (sunrise/afternoon feel)
- Add retro wall clock showing learning time

COMPOSITION:
- Friendly cartoon professor/scientist character on LEFT side
- Chalkboard or presentation board on RIGHT side at slight angle
- Board shows example time series chart with reference lines (average line, threshold, benchmark)
- Clear labels on the chart showing the three types of reference lines
- Code snippet in small panel at bottom
- 16:9 landscape format

DESIGN QUALITY:
- Clear board area for legible text
- Balanced composition with rule of thirds
- Clean whitespace around elements
- No copyrighted characters
- No logos or watermarks
- Professional educational illustration quality

EDUCATIONAL PROPS SPECIFIC TO THIS SLIDE:
- Show a time series chart with three different reference lines:
  * Red dashed line for average
  * Blue dotted line for threshold
  * Green solid line for historical benchmark
- Small vintage calculator or slide rule in scene
- Stack of old data charts/graphs

Create a complete, professional educational slide that clearly teaches the concept while maintaining that classic 1960s TV animation charm.
"""

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print("Generating Slide 36: Reference Lines and Benchmarks")
print("Style: 1960s American limited TV animation (Hanna-Barbera inspired)")
print("=" * 70)

try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",  # 16:9 landscape for slides
        quality="hd",  # High quality for clarity
        style="natural",  # Better for educational content
        n=1
    )
    
    image_url = response.data[0].url
    print(f"✓ Image generated successfully")
    print(f"  Model: DALL-E 3 HD")
    print(f"  URL: {image_url[:80]}...")
    
    # Download and save
    print("\nDownloading image...")
    img_response = requests.get(image_url)
    img = Image.open(BytesIO(img_response.content))
    
    output_file = "slide_images_ai/slide_036_retro.png"
    os.makedirs("slide_images_ai", exist_ok=True)
    img.save(output_file)
    
    file_size_mb = os.path.getsize(output_file) / 1024 / 1024
    
    print(f"\n✓ Image saved successfully")
    print(f"  Output: {output_file}")
    print(f"  Dimensions: {img.size}")
    print(f"  File size: {file_size_mb:.1f} MB")
    print(f"  Format: {img.format}")
    
    print("=" * 70)
    print("✅ Slide 36 created in 1960s retro animation style!")
    print("\nFeatures:")
    print("  ✓ Different camera angle (right-side composition)")
    print("  ✓ Varied character pose and props")
    print("  ✓ Time series chart with reference lines illustrated")
    print("  ✓ Warm orange-yellow color balance")
    print("  ✓ Clean educational design")
    
except Exception as e:
    print(f"\n✗ Error generating image: {e}")
    print("\nCheck:")
    print("  1. API key set: echo $OPENAI_API_KEY")
    print("  2. Billing status: https://platform.openai.com/account/billing")
