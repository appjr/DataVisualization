import os
import re
import textwrap
from PIL import Image, ImageDraw, ImageFont

slides_dir = "Class5/individual_slides"
output_dir = "Class5/locally_created_image"
os.makedirs(output_dir, exist_ok=True)

print("=== Local Slide Image Generation (Alphanumeric Only) ===")
print(f"Slides directory: {slides_dir}")
print(f"Output directory: {output_dir}")

# Try to load a readable font
try:
    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 28)
    font_bold = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", 32)
    print("Loaded Arial fonts for rendering.")
except Exception:
    font = ImageFont.load_default()
    font_bold = font
    print("Arial fonts not found, using default font.")

# Image settings
width, height = 1024, 1536
margin = 60
line_spacing = 12
print(f"Image size: {width}x{height}, margin: {margin}px")

slide_files = sorted([f for f in os.listdir(slides_dir) if f.endswith('.md')])
print(f"Total slides found: {len(slide_files)}\n")

alnum_pattern = re.compile(r"[^A-Za-z0-9\s]")

# Clear existing output images
removed = 0
for file in os.listdir(output_dir):
    if file.endswith(".png"):
        os.remove(os.path.join(output_dir, file))
        removed += 1
print(f"Cleared {removed} previous images in output folder.\n")

for idx, slide_file in enumerate(slide_files, 1):
    slide_path = os.path.join(slides_dir, slide_file)
    print(f"[{idx}/{len(slide_files)}] Reading {slide_file}...")

    with open(slide_path, 'r', encoding='utf-8') as f:
        text = f.read().strip()

    # Remove all non-alphanumeric characters (keep spaces)
    cleaned_text = alnum_pattern.sub("", text)

    # Prepare wrapped lines
    wrapped_lines = []
    for line in cleaned_text.splitlines():
        if line.strip():
            wrapped_lines.extend(textwrap.wrap(line, width=60) or [""])

    print(f"    Original length: {len(text)} chars")
    print(f"    Cleaned length:  {len(cleaned_text)} chars")
    print(f"    Wrapped into {len(wrapped_lines)} lines")

    # Create image
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    y = margin
    for line in wrapped_lines:
        if y > height - margin:
            print("    Reached bottom of image; truncating remaining text")
            break

        draw.text((margin, y), line, fill="black", font=font)
        y += font.getbbox(line)[3] + line_spacing

    output_path = os.path.join(output_dir, slide_file.replace('.md', '.png'))
    img.save(output_path)
    print(f"    ✓ Saved {output_path}\n")

print("✅ Local images created successfully with alphanumeric-only text!")
