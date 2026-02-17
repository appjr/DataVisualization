"""
Transform slide 34 image to retro cartoon style using OpenAI image edit
Send the existing slide image to ChatGPT and transform to Hannah-Barbera style
"""

import os
from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO

# Paths
input_image = "slide_images/slide_034.png"
output_image = "slide_images_ai/slide_034_cartoon_transform.png"

# Transformation prompt (must be under 1000 characters for dall-e-2)
prompt = """
Transform to 1960s Hanna-Barbera retro cartoon style (Flintstones/Jetsons era):
- Bold black outlines, soft grain texture
- Vintage palette: soft blues, oranges, yellows
- Flat 2D animation, no 3D
- Add cartoon professor character gesturing
- Keep all text exactly as shown
- Add retro classroom props (clock, charts)
- Maintain slide layout and readability
"""

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print("Transforming slide 34 to Hanna-Barbera cartoon style...")
print("=" * 60)
print(f"Input: {input_image}")
print(f"Output: {output_image}")
print("=" * 60)

try:
    # Load and prepare image (must be RGBA for edit API)
    print("Loading image...")
    img = Image.open(input_image).convert("RGBA")
    
    # Save to buffer as PNG
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)
    
    print("Sending to OpenAI for transformation...")
    
    # Use edit API with dall-e-2 (supports image transformation)
    response = client.images.edit(
        model="dall-e-2",
        image=("slide.png", img_buffer, "image/png"),
        prompt=prompt,
        size="1024x1024",  # dall-e-2 supports square sizes
        response_format="b64_json"
    )
    
    # Decode and save
    print("Receiving transformed image...")
    b64_data = response.data[0].b64_json
    img_bytes = base64.b64decode(b64_data)
    transformed = Image.open(BytesIO(img_bytes))
    
    # Resize to 16:9 if needed
    if transformed.size != (1792, 1024):
        print(f"Resizing from {transformed.size} to 16:9...")
        # Crop center to 16:9
        w, h = transformed.size
        target_h = int(w * 9 / 16)
        top = (h - target_h) // 2
        transformed = transformed.crop((0, top, w, top + target_h))
        # Resize to target
        transformed = transformed.resize((1792, 1024), Image.LANCZOS)
    
    # Save
    os.makedirs("slide_images_ai", exist_ok=True)
    transformed.save(output_image)
    
    print(f"\n✓ Image saved to: {output_image}")
    print(f"  Size: {transformed.size}")
    print(f"  File size: {os.path.getsize(output_image) / 1024 / 1024:.1f} MB")
    
    print("=" * 60)
    print("✅ Slide 34 transformed to cartoon style successfully!")
    print("\nThe image should now have a Hanna-Barbera retro cartoon look")
    print("with cartoon characters and vintage animation aesthetics.")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nNote: dall-e-2 image edit may have limitations.")
    print("If this fails, the generated version (slide_034_with_text.png) is available.")
