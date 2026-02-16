import os
import time
import base64
from openai import OpenAI

client = OpenAI()

slides_dir = "Class5/individual_slides"
output_dir = "Class5/vintage_cartoon_slides"
os.makedirs(output_dir, exist_ok=True)

slide_files = sorted([f for f in os.listdir(slides_dir) if f.endswith('.md')])
print(f"\n=== Vintage Cartoon Image Generation ===")
print(f"Total slides found: {len(slide_files)}")
print(f"Input folder: {slides_dir}")
print(f"Output folder: {output_dir}\n")

for idx, slide_file in enumerate(slide_files, 1):
    slide_path = os.path.join(slides_dir, slide_file)
    with open(slide_path, 'r', encoding='utf-8') as f:
        slide_content = f.read().strip()

    prompt = f"make this on a vintage cartoon format. {slide_content}"

    print(f"[{idx}/{len(slide_files)}] Generating image for {slide_file}...")
    start = time.time()

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1536",
        quality="medium",
        n=1
    )

    image_base64 = result.data[0].b64_json
    output_path = os.path.join(output_dir, slide_file.replace('.md', '.png'))
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))

    elapsed = time.time() - start
    file_size_kb = os.path.getsize(output_path) / 1024

    print(f"    ✓ Saved: {output_path}")
    print(f"    ⏱  Time: {elapsed:.2f}s | Size: {file_size_kb:.1f} KB\n")

print("✅ All images generated successfully!\n")
